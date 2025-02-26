import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
# file_path = "your_file.csv"  # Replace with your file path
data = pd.read_csv('Motor_Vehicle_Collisions_Crashes.csv', low_memory=False)

'''
# Convert CRASH TIME to datetime and extract the hour
data['CRASH TIME'] = pd.to_datetime(data['CRASH TIME'], format='%H:%M', errors='coerce')
data['HOUR'] = data['CRASH TIME'].dt.hour

# Group by hour and count the number of accidents
hourly_accidents = data.groupby('HOUR').size().reset_index(name='ACCIDENT_COUNT')

# Find the hour with the most accidents
most_accidents_hour = hourly_accidents.loc[hourly_accidents['ACCIDENT_COUNT'].idxmax(), 'HOUR']

# Filter data for the hour with the most accidents
most_accidents_data = data[data['HOUR'] == most_accidents_hour]

# Display CONTRIBUTING FACTOR VEHICLE 1 and 2 for that hour
result = most_accidents_data[['CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2']]

# Output the result
print(f"Hour with the most accidents: {most_accidents_hour}")
print(result)
'''


# Extract the hour from the CRASH TIME column
data['CRASH HOUR'] = pd.to_datetime(data['CRASH TIME'], format='%H:%M', errors='coerce').dt.hour


# Find the hour with the most accidents
most_accidents_hour = data['CRASH HOUR'].value_counts().idxmax()

# Filter data for the most accident-prone hour
filtered_data = data[data['CRASH HOUR'] == most_accidents_hour]

# Combine contributing factors
contributing_factors = pd.concat([
    filtered_data['CONTRIBUTING FACTOR VEHICLE 1'],
    filtered_data['CONTRIBUTING FACTOR VEHICLE 2']
])
contributing_factors = contributing_factors[contributing_factors != 'Unspecified']

# Count the occurrences of each contributing factor
factor_counts = contributing_factors.value_counts()

# Plot the contributing factors
plt.figure(figsize=(10, 6))
factor_counts.plot(kind='bar', color='skyblue')
plt.title(f"Contributing Factors for Accidents at {most_accidents_hour}:00")
plt.xlabel("Contributing Factor")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()