
import boto3
import pandas as pd

from io import BytesIO
from pathlib import Path

from config import BUCKET_NAME, REGION, INPUT_FILES, RAW_DATA_DIR


def extract_data():

    # Connect to S3 using the AWS credentials configured on my machine.
    s3_client = boto3.client("s3", region_name=REGION)

    # Create the raw data folder if it does not already exist.
    raw_directory = Path(RAW_DATA_DIR)
    raw_directory.mkdir(parents=True, exist_ok=True)

    # I use this list to store the three DataFrames after downloading them.
    dataframes = []

    # Go through each CSV file stored in the S3 bucket.
    for file_key in INPUT_FILES:

        print(f"Downloading: {file_key}")

        # Download the file from S3.
        response = s3_client.get_object(
            Bucket=BUCKET_NAME,
            Key=file_key
        )

        # Read the file content into memory.
        file_content = response["Body"].read()

        # Use pandas to read the CSV data into a DataFrame.
        df = pd.read_csv(BytesIO(file_content))

        # Keep the original filename so I can identify each downloaded file.
        filename = file_key.split("/")[-1]

        # Save a local copy of the original CSV in the raw data folder.
        local_path = raw_directory / filename
        df.to_csv(local_path, index=False)

        # Add the DataFrame to the list so I can combine the datasets later.
        dataframes.append(df)

        print(f"Saved locally: {local_path}")
        print(f"Rows: {len(df)}")

    print("\nExtraction completed!")

    # Return all three DataFrames for the transformation stage.
    return dataframes
