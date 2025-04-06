import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def approximate_entropy(series, m=2, r=None):
    """Calculate Approximate Entropy (ApEn) of a time series."""
    N = len(series)
    if N < m + 1:
        return np.nan

    if r is None:
        r = 0.2 * np.std(series)
    if r == 0:
        return np.nan

    def create_embedding(series, m):
        return np.array([series[i:i + m] for i in range(N - m + 1)])

    def phi(m):
        embedded = create_embedding(series, m)
        count = []
        epsilon = 1e-10

        for i in range(len(embedded)):
            dist = np.abs(embedded - embedded[i]).max(axis=1)
            count.append(np.sum(dist <= r) / len(embedded))

        count = np.array(count) + epsilon
        return np.sum(np.log(count)) / len(count)

    return phi(m) - phi(m + 1)

# Load and preprocess data 

file_path = input("Enter path to trajectory CSV file: ")
data = pd.read_csv(file_path)

required_columns = ['ObjectID', 'Frame', 'x1', 'y1']
if not all(col in data.columns for col in required_columns):
    raise ValueError(f"CSV must contain columns: {required_columns}")

data = data.sort_values(by=['ObjectID', 'Frame'])
data['Velocity'] = 0.0
data['DirectionChange'] = 0.0

for obj_id in data['ObjectID'].unique():
    obj_data = data[data['ObjectID'] == obj_id].sort_values(by='Frame')
    dx = obj_data['x1'].diff().fillna(0)
    dy = obj_data['y1'].diff().fillna(0)

    velocity = np.sqrt(dx**2 + dy**2) * 30  # scaled by fps
    direction_change = np.arctan2(dy, dx).diff().fillna(0)

    data.loc[obj_data.index, 'Velocity'] = velocity
    data.loc[obj_data.index, 'DirectionChange'] = direction_change

# Compute ApEn for each pedestrian 

m = 2
r_multiplier = 0.2
results = []

for obj_id in data['ObjectID'].unique():
    obj_data = data[data['ObjectID'] == obj_id]

    if len(obj_data) < 10:
        continue

    velocity = obj_data['Velocity'].values
    direction = obj_data['DirectionChange'].values

    r_v = r_multiplier * np.std(velocity) if np.std(velocity) > 0 else 0.01
    r_d = r_multiplier * np.std(direction) if np.std(direction) > 0 else 0.01

    apen_v = approximate_entropy(velocity, m, r_v)
    apen_d = approximate_entropy(direction, m, r_d)

    if not np.isnan(apen_v) and not np.isnan(apen_d):
        results.append({'ObjectID': obj_id, 'ApEn_Velocity': apen_v, 'ApEn_DirectionChange': apen_d})

results_df = pd.DataFrame(results)

# Plot histogram 

plt.figure(figsize=(10, 6))
plt.hist(results_df['ApEn_Velocity'], bins=20, alpha=0.7, label='Velocity', color='blue')
plt.hist(results_df['ApEn_DirectionChange'], bins=20, alpha=0.7, label='Direction Change', color='orange')
plt.title('Histogram of Approximate Entropy')
plt.xlabel('Approximate Entropy')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
