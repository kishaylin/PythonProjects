#Occupancy data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")
sns.set_palette("viridis")

#Retrieves data from the csv.gz file
calendar = pd.read_csv("calendar.csv.gz", compression="gzip")

# To check if the dataset has dates and columns
calendar.head()

calendar['date'] = pd.to_datetime(calendar['date']) # Date column --> date

# Converting prices to a float datatype
calendar['price'] = (
    calendar['price']
    .astype(str)
    .str.replace('$', '')
    .str.replace(',', '')
    .astype(float)
)

calendar['available_flag'] = calendar['available'].map({'t': 1, 'f': 0}) #V. Important, converts boolean in csv to numeric values


#Daily Occupancy Rate in Dublin Airbnb Listings
daily_demand = (
    calendar.groupby('date')['available_flag'] # For percentage of Listings available
    .mean()
    .reset_index()
)

daily_demand['occupancy_rate'] = 1 - daily_demand['available_flag'] # Percentage of listings booked

plt.figure(figsize=(14,6))
sns.lineplot(data=daily_demand, x='date', y='occupancy_rate')
plt.title("Daily Occupancy Rate in Dublin Airbnb Listings")
plt.ylabel("Occupancy Rate")
plt.xlabel("Date")
plt.show()



# Top 20 highest occupancy dates
high_demand = daily_demand.sort_values("occupancy_rate", ascending=False).head(20)
#high_demand

plt.figure(figsize=(12,6))
sns.barplot(
    data=high_demand,
    x='occupancy_rate',
    y='date',
    palette="rocket"
)
plt.title("Top 20 High-Demand Dates (Highest Occupancy)")
plt.xlabel("Occupancy Rate")
plt.ylabel("Date")
plt.show()



# Distribution of Listing Occupancy Rates
host_availability = (
    calendar.groupby('listing_id')['available_flag']
    .mean()
    .reset_index()
)

host_availability['occupancy_rate'] = 1 - host_availability['available_flag']

plt.figure(figsize=(10,6))
sns.histplot(host_availability['occupancy_rate'], bins=30, kde=True)
plt.title("Distribution of Listing Occupancy Rates")
plt.xlabel("Occupancy Rate")
plt.ylabel("Count of Listings")
plt.show()

heatmap_data = (
    daily_demand
    .assign(month=lambda x: x['date'].dt.month,
            day=lambda x: x['date'].dt.day)
    .pivot_table(index='month', columns='day', values='occupancy_rate')
)







