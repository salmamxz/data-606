
# test the structure, types and quality of the book sales dataset

import pandas as pd


EXPECTED_COLUMNS = [
    "index",
    "Publishing Year",
    "Book Name",
    "Author",
    "language_code",
    "Author_Rating",
    "Book_average_rating",
    "Book_ratings_count",
    "genre",
    "gross sales",
    "publisher revenue",
    "sale price",
    "sales rank",
    "Publisher ",
    "units sold",
]

VALID_GENRES = {"genre fiction", "nonfiction", "fiction", "children"}

VALID_AUTHOR_RATINGS = {
    "Intermediate",
    "Excellent",
    "Famous",
    "Novice",
}

VALID_LANGUAGE_CODES = {
    "eng",
    "en-US",
    "en-GB",
    "en-CA",
    "fre",
    "spa",
    "ara",
    "nl",
}


# 1. structure tests

def test_dataset_has_1070_rows(book_sales_data):
    assert len(book_sales_data) == 1070


def test_dataset_has_15_columns(book_sales_data):
    assert len(book_sales_data.columns) == 15


def test_dataset_has_expected_columns(book_sales_data):
    assert list(book_sales_data.columns) == EXPECTED_COLUMNS


# 2. data type tests

def test_book_names_are_text(book_sales_data):
    assert book_sales_data["Book Name"].dtype == object


def test_authors_are_text(book_sales_data):
    assert book_sales_data["Author"].dtype == object


def test_units_sold_are_integers(book_sales_data):
    assert pd.api.types.is_integer_dtype(book_sales_data["units sold"])


def test_book_ratings_are_numeric(book_sales_data):
    assert pd.api.types.is_numeric_dtype(
        book_sales_data["Book_average_rating"]
    )


# 3. valid category tests

def test_genres_are_valid(book_sales_data):
    assert set(book_sales_data["genre"].dropna()).issubset(VALID_GENRES)


def test_author_ratings_are_valid(book_sales_data):
    assert set(
        book_sales_data["Author_Rating"].dropna()
    ).issubset(VALID_AUTHOR_RATINGS)


def test_language_codes_are_valid(book_sales_data):
    assert set(
        book_sales_data["language_code"].dropna()
    ).issubset(VALID_LANGUAGE_CODES)


# 4. plausible range tests

def test_book_ratings_are_between_zero_and_five(book_sales_data):
    assert book_sales_data["Book_average_rating"].between(0, 5).all()


def test_book_ratings_count_is_positive(book_sales_data):
    assert (book_sales_data["Book_ratings_count"] > 0).all()


def test_units_sold_are_positive(book_sales_data):
    assert (book_sales_data["units sold"] > 0).all()


def test_sale_prices_are_non_negative(book_sales_data):
    assert (book_sales_data["sale price"] >= 0).all()


# 5. missing value tests

def test_book_names_have_no_missing_values(book_sales_data):
    assert book_sales_data["Book Name"].notna().all()


def test_publishing_years_have_no_missing_values(book_sales_data):
    assert book_sales_data["Publishing Year"].notna().all()


def test_language_codes_have_no_missing_values(book_sales_data):
    assert book_sales_data["language_code"].notna().all()


# 6. duplicate tests

def test_dataset_has_no_duplicate_rows(book_sales_data):
    assert not book_sales_data.duplicated().any()


def test_book_sales_index_is_unique(book_sales_data):
    assert book_sales_data["index"].is_unique
