
import boto3

from pathlib import Path

from config import (
    BUCKET_NAME,
    REGION,
    PROCESSED_DATA_DIR,
    OUTPUT_FILENAME,
    OUTPUT_KEY
)


def load_data(dataframe):

    # Create the processed data folder if it does not already exist.
    processed_directory = Path(PROCESSED_DATA_DIR)
    processed_directory.mkdir(parents=True, exist_ok=True)

    # Set the path and filename for the final CSV file.
    output_path = processed_directory / OUTPUT_FILENAME

    # Save the transformed DataFrame as a CSV file locally.
    dataframe.to_csv(output_path, index=False)

    print(f"\nSaved transformed data: {output_path}")

    # Connect to the S3 bucket using Boto3.
    s3_client = boto3.client("s3", region_name=REGION)

    # Upload the final CSV file to the specified location in S3.
    print("\nUploading transformed data to S3...")

    s3_client.upload_file(
        str(output_path),
        BUCKET_NAME,
        OUTPUT_KEY
    )

    print("Upload successful!")

    print(f"S3 destination: s3://{BUCKET_NAME}/{OUTPUT_KEY}")

    # Check that the file exists in S3 and retrieve its metadata.
    response = s3_client.head_object(
        Bucket=BUCKET_NAME,
        Key=OUTPUT_KEY
    )

    print("Upload verified!")

    # Display the uploaded file size to confirm the upload.
    print("File size:", response["ContentLength"], "bytes")
