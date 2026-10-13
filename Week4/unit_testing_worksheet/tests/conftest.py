
import pandas as pd
import pytest
from pathlib import Path


@pytest.fixture
def book_sales_data():
    # load the book sales dataset for the tests
    csv_path = Path(__file__).parent.parent / "data" / "book_sales.csv"
    return pd.read_csv(csv_path)
