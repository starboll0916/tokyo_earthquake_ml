import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_csv(r"C:\Users\sglee\Downloads\query (3).csv")



analysis_df = df[
 ["time",
  "latitude",
  "longitude",
  "depth",
  "mag",
  "place"]
  ].copy()

"""print(analysis_df.head())"""

analysis_df["time"] = pd.to_datetime(
    analysis_df["time"]
)

analysis_df["year"] = analysis_df["time"].dt.year
analysis_df["month"] = analysis_df["time"].dt.month

def classify_region(lat, lon):

    # Tokyo / Kanto
    if 34.5 <= lat <= 37.5 and 138 <= lon <= 142:
        return "Kanto"

    # Nagoya / Chubu
    elif 34 <= lat <= 37 and 136 <= lon < 138:
        return "Chubu"

    # Osaka / Kansai
    elif 33 <= lat <= 36 and 134 <= lon < 136:
        return "Kansai"

    else:
        return "Other"

analysis_df["region"] = analysis_df.apply(
    lambda row: classify_region(
        row["latitude"],
        row["longitude"]
    ),
    axis=1
)


"""mean magnititude 4.459
depth 78.36"""





"""plt.hist(
 analysis_df["mag"],
 bins=30,)
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.title("Distribution of Earthquake Magnitudes")"""

plt.show()

"""plt.scatter(
    analysis_df["longitude"],
    analysis_df["latitude"],
    s=10,
    alpha=0.5
)"""

"""plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Earthquake Locations")"""

plt.show()



"""print(
    analysis_df[
        [
            "latitude",
            "longitude",
            "depth",
            "mag"
        ]
    ].corr()
)"""



region_summary = analysis_df.groupby("region").agg(
    earthquake_count=("mag", "count"),
    mean_magnitude=("mag", "mean"),
    max_magnitude=("mag", "max"),
    mean_depth=("depth", "mean"),
    max_depth=("depth", "max")
)

print(region_summary)

region_summary.to_csv(
    "data/processed/earthquakes_cleaned.csv",
    index=False
)



