# Fish Market ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Python, Pandas, Boto3 and Amazon S3.

The objective is to read three fish market CSV datasets from Amazon S3, calculate average measurements for each fish species, and upload the transformed dataset back to S3.

## Project Structure

- `config.py`: Stores S3 configuration and file paths.
- `extract.py`: Downloads the three original CSV files from S3.
- `transform.py`: Combines the datasets and calculates average measurements by fish species.
- `load.py`: Saves the transformed dataset locally and uploads it to S3.
- `main.py`: Executes the complete ETL pipeline.
- `data/raw/`: Stores the original downloaded datasets.
- `data/processed/`: Stores the transformed dataset.

## Data Sources

The pipeline reads the following files:

1. `python/fish-market.csv`
2. `python/fish-market-mon.csv`
3. `python/fish-market-tues.csv`

## Transformation

The three datasets are combined into one DataFrame.

The data is grouped by `Species`, and the following numerical measurements are averaged:

- Weight
- Length1
- Length2
- Length3
- Height
- Width

The averages are rounded to two decimal places.

## Output

The transformed dataset is saved locally as:

`data/processed/fish-market-averages.csv`

It is also uploaded to:

`s3://data-eng-resources/Data606/fish/salma/fish-market-averages.csv`

## Technologies

- Python
- Pandas
- Boto3
- Amazon S3
