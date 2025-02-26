import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Motor_Vehicle_Collisions_Crashes.csv', low_memory=False)

print(df.head())
print(df.columns)

# Convert CRASH TIME to datetime
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'], format='%H:%M', errors='coerce')

# Define time periods
def categorize_time(row):
    if pd.isnull(row):  # Handle missing or invalid times
        return 'Unknown'
    hour = row.hour
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Apply categorization
df['TIME PERIOD'] = df['CRASH TIME'].apply(categorize_time)

# Count accidents in each time period
time_period_counts = df['TIME PERIOD'].value_counts()
print(time_period_counts)

# Calculate total fatalities and injuries
df['TOTAL FATALITIES'] = (
    df['NUMBER OF PERSONS KILLED'] +
    df['NUMBER OF PEDESTRIANS KILLED'] +
    df['NUMBER OF MOTORIST KILLED']
)

df['TOTAL INJURIES'] = (
    df['NUMBER OF PERSONS INJURED'] +
    df['NUMBER OF PEDESTRIANS INJURED'] +
    df['NUMBER OF MOTORIST INJURED']
)

# Group by time period and calculate sums
grouped = df.groupby('BOROUGH')[['TOTAL FATALITIES', 'TOTAL INJURIES']].sum()
grouped = grouped.reset_index()
print(grouped)

# Plot the grouped data
grouped.plot(kind='bar', figsize=(10, 6), color=['#FF6666', '#66B2FF'])

# Plot the grouped data
ax = grouped.plot(
    kind='bar', 
    x='BOROUGH',
    y=['TOTAL FATALITIES', 'TOTAL INJURIES'], 
    figsize=(10, 6), 
    color=['#FF6666', '#66B2FF']
)

# Customize the chart
plt.title('Total Fatalities and Injuries by Borough')
plt.xlabel('Borough')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.legend(['Total Fatalities', 'Total Injuries'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()