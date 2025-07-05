import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("job_listings.csv")

# 1. Explore structure
print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# 2. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Unique values
print("\nUnique Job Titles:", df['Job Title'].nunique())
print("Unique Companies:", df['Company'].nunique())
print("Unique Locations:", df['Location'].nunique())

# 4. Top 10 companies by job count
top_companies = df['Company'].value_counts().head(10)
print("\nTop Companies by Job Count:")
print(top_companies)

# Plot top companies
plt.figure(figsize=(10,6))
sns.countplot(data=df, y='Company', order=top_companies.index, palette='viridis')
plt.title('Top 10 Companies by Job Listings')
plt.xlabel('Number of Jobs')
plt.ylabel('Company')
plt.tight_layout()
plt.savefig('top_companies.png')
plt.show()

# 5. Jobs by location
top_locations = df['Location'].value_counts().head(10)
print("\nTop Locations:")
print(top_locations)

# Plot top locations
plt.figure(figsize=(10,6))
sns.countplot(data=df, y='Location', order=top_locations.index, palette='magma')
plt.title('Top 10 Locations by Job Listings')
plt.xlabel('Number of Jobs')
plt.ylabel('Location')
plt.tight_layout()
plt.savefig('top_locations.png')
plt.show()
