
import pandas as pd


def transform_data(dataframes):

    print("\nCombining datasets...")

    # Combine the three DataFrames into one dataset.
    # ignore_index=True gives the combined dataset a fresh index.
    combined_data = pd.concat(
        dataframes,
        ignore_index=True
    )

    print("Total records:", len(combined_data))

    # These are the numerical columns I want to calculate averages for.
    numerical_columns = [
        "Weight",
        "Length1",
        "Length2",
        "Length3",
        "Height",
        "Width"
    ]

    print("\nCalculating averages by species...")

    # Group the data by fish species and calculate the average
    # for each of the numerical columns.
    fish_averages = (
        combined_data
        .groupby("Species")[numerical_columns]
        .mean()
        .round(2)
        .reset_index()
    )

    print("\nTransformed data:")
    print(fish_averages)

    # Show how many different fish species are in the final dataset.
    print("\nNumber of species:", len(fish_averages))

    # Return the transformed dataset for the loading stage.
    return fish_averages
