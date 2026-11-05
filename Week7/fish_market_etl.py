
import boto3
import pandas as pd
from io import BytesIO

# S3 configuration
BUCKET_NAME = "data-eng-resources"
REGION = "eu-central-1"

# The three original fish market CSV files
FILES = [
    "python/fish-market.csv",
    "python/fish-market-mon.csv",
    "python/fish-market-tues.csv"
]

# Connect to S3
s3_client = boto3.client("s3", region_name=REGION)

print("Connected to S3 successfully!")

# Read and inspect each CSV file
fish_dataframes = []

for file_key in FILES:

    print("\n" + "=" * 60)
    print("Reading:", file_key)
    print("=" * 60)

    # Download CSV file from S3 into memory
    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key=file_key
    )

    # Read CSV using pandas
    df = pd.read_csv(BytesIO(response["Body"].read()))

    # Store dataframe for the next stage
    fish_dataframes.append(df)

    # Display information
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst five rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nDataset shape:")
    print(df.shape)

print("\nAll three CSV files have been read successfully!")
