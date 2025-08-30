import pandas as pd

# Read CSV
df = pd.read_csv('yourfile.csv')

# Display the DataFrame
print("DataFrame:")
print(df)

# Display basic info
print("\nInfo:")
print(df.info())

# Display summary statistics
print("\nDescribe:")
print(df.describe(include='all'))

# Select a column
print("\nSelect 'name' column:")
print(df['name'])

# Filter rows
print("\nFilter rows where age > 28:")
print(df[df['age'] > 28])

# Add a new column
df['age_plus_10'] = df['age'] + 10
print("\nDataFrame with new column 'age_plus_10':")
print(df)

# Group by city and get mean age
print("\nGroup by 'city' and mean age:")
print(df.groupby('city')['age'].mean())

# Sort by age descending
print("\nSort by age descending:")
print(df.sort_values(by='age', ascending=False))

# Handle missing data
df.loc[3] = ['David', None, 'Boston', None]  # Add a row with missing data
print("\nDataFrame with missing data:")
print(df)
print("\nFill missing values with defaults:")
print(df.fillna({'age': 0, 'age_plus_10': 0}))

# Drop rows with missing data
print("\nDrop rows with missing data:")
print(df.dropna())

# Save to new CSV
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'")