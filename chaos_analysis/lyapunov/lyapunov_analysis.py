import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

def time_delay_embedding(traj, dim, tau):
    """
    Constructs time-delay embedded vectors from trajectory.
    """
    N = traj.shape[0]
    M = N - (dim - 1) * tau
    if M <= 0:
        raise ValueError("Trajectory too short for given embedding parameters.")

    embedded = np.zeros((M, dim * traj.shape[1]))
    for i in range(dim):
        embedded[:, i * traj.shape[1]:(i + 1) * traj.shape[1]] = traj[i * tau:i * tau + M, :]

    return embedded

def rosenstein_lyapunov(traj, dim=3, tau=5, max_steps=10):
    """
    Computes the largest Lyapunov exponent using Rosenstein's method.
    """
    embedded = time_delay_embedding(traj, dim, tau)
    N = embedded.shape[0]
    if N < 10:
        raise ValueError("Too few embedded points.")

    divergence = np.zeros(max_steps)
    count = np.zeros(max_steps)

    distances = cdist(embedded, embedded)
    np.fill_diagonal(distances, np.inf)
    nearest_neighbors = np.argmin(distances, axis=1)

    for i in range(N - max_steps):
        j = nearest_neighbors[i]
        for k in range(max_steps):
            if i + k >= N or j + k >= N:
                break
            delta = np.linalg.norm(embedded[i + k] - embedded[j + k])
            if delta > 0:
                divergence[k] += np.log(delta)
                count[k] += 1

    valid = count > 0
    mean_div = divergence[valid] / count[valid]
    time = np.arange(1, max_steps + 1)[valid]

    if len(time) < 2:
        return np.nan

    coeff = np.polyfit(time, mean_div, 1)
    return coeff[0]  

# Load and preprocess trajectory data 

file_path = input("Enter path to trajectory CSV: ")
data = pd.read_csv(file_path)

required_cols = ['ObjectID', 'Frame', 'x1', 'y1']
if not all(col in data.columns for col in required_cols):
    raise ValueError(f"CSV must contain columns: {required_cols}")

data = data.sort_values(by=['ObjectID', 'Frame'])
results = []

for obj_id in data['ObjectID'].unique():
    obj = data[data['ObjectID'] == obj_id]
    if len(obj) < 10:
        continue

    x = obj['x1'].values
    y = obj['y1'].values

    dx = np.diff(x)
    dy = np.diff(y)
    v = np.sqrt(dx**2 + dy**2)
    theta = np.degrees(np.arctan2(dy, dx))
    theta = np.append(theta, theta[-1])

    x = x[:-1]
    y = y[:-1]

    min_len = min(len(x), len(y), len(v), len(theta))
    traj = np.stack([x[:min_len], y[:min_len], v[:min_len], theta[:min_len]], axis=1)

    # Optional: interpolate to 50 points
    if traj.shape[0] < 50:
        traj_interp = np.zeros((50, traj.shape[1]))
        for i in range(traj.shape[1]):
            traj_interp[:, i] = np.interp(
                np.linspace(0, traj.shape[0] - 1, 50),
                np.arange(traj.shape[0]),
                traj[:, i]
            )
        traj = traj_interp

    try:
        le = rosenstein_lyapunov(traj, dim=3, tau=5)
    except Exception as e:
        le = np.nan

    if not np.isnan(le):
        results.append({'ObjectID': obj_id, 'LyapunovExponent': le})

# Save & plot results 

results_df = pd.DataFrame(results)
print(results_df)

if not results_df.empty:
    plt.figure(figsize=(8, 5))
    plt.hist(results_df['LyapunovExponent'], bins=20, color='blue', alpha=0.7)
    plt.title('Histogram of Lyapunov Exponents')
    plt.xlabel('Lyapunov Exponent')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("No valid Lyapunov exponents computed.")
