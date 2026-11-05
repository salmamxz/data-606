
from extract import extract_data
from transform import transform_data
from load import load_data


def main():

    # Display the pipeline title when the program starts.
    print("FISH MARKET ETL PIPELINE")


    # EXTRACT
    print("\nSTAGE 1: EXTRACT")

    # Download the three CSV files from S3 and store them as DataFrames.
    dataframes = extract_data()

    # TRANSFORM
    print("\nSTAGE 2: TRANSFORM")

    # Combine the datasets and calculate the average measurements for each species.
    transformed_data = transform_data(dataframes)

    # LOAD
    print("\nSTAGE 3: LOAD")

    # Save the final dataset locally and upload it to S3.
    load_data(transformed_data)

    # Display a message once all three stages have finished.

    print("ETL PIPELINE COMPLETED SUCCESSFULLY!")



# Run the main function when this file is executed directly.
if __name__ == "__main__":
    main()
