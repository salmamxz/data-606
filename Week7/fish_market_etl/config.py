
BUCKET_NAME = "data-eng-resources"
REGION = "eu-central-1"

# Original CSV files in S3
INPUT_FILES = [
    "python/fish-market.csv",
    "python/fish-market-mon.csv",
    "python/fish-market-tues.csv"
]

# Local directories
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"

# Output file
OUTPUT_FILENAME = "fish-market-averages.csv"

# S3 destination
OUTPUT_KEY = "Data606/fish/salma/fish-market-averages.csv"
