import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv('spatial_customers.csv')

# Select features (X and Y coordinates)
X = data[['X', 'Y']]

# Standardize featurese
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit DBSCAN
model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X_scaled)

# Save cluster labels into the data
data['Cluster'] = labels


# Save result
data.to_csv('dbscan_clustered.csv', index=False)

# Save scaler (DBSCAN model is not serializable)
joblib.dump(scaler, 'scaler.pkl')

print("DBSCAN clustering completed. Clustered data saved as dbscan_clustered.csv.")
