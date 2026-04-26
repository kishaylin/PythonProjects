import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")
sns.set_palette("viridis")

listings = pd.read_csv("listings.csv")
listings.head()

#print(listings.head())
#print(listings.columns)

#Counts the listings per area
area_counts = (
    listings['neighbourhood']
    .value_counts()
    .reset_index()
)

area_counts.columns = ['neighbourhood', 'listing_count']
area_counts.head()

#Graph
plt.figure(figsize=(12,8))
sns.barplot(
    data=area_counts.head(15),
    x='listing_count',
    y='neighbourhood'
)
plt.title("The number of Airbnb Listings in Dublin")
plt.xlabel("Number of Listings")
plt.ylabel("County")
plt.show()


