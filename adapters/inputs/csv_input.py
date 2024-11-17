"""
csv_input.py

Banks allow download of transactions in CSV format, but the data is not standardized.
These functions are used to normalize bank inputs to a common format for this app, so
later transformations can be applied more easily.
"""

import csv
from settings import logger, HEADER_MAPPINGS


def normalize_csv(file_path):
    """
    Reads a CSV file and normalizes it to the Bud-Get internal transaction format.

    Args:
        file_path (str): Path to the CSV file exported from the bank.

    Returns:
        dict: A list of normalized transactions.
    """

    try:
        transactions = []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            transactions = [normalize_row(row) for row in reader]

        return transactions

    except FileNotFoundError:
        logger.exception(f"File {file_path} not found.")
    except Exception:
        logger.exception("An unexpected error occurred.")

    return []


def normalize_row(input_row):
    """
    Create a normalized transaction from an arbitrary CSV transaction row.
    """
    return {
        "Date": get_normalized_value(input_row, "Date"),
        "Amount": get_normalized_value(input_row, "Amount"),
        "Description": get_normalized_value(input_row, "Description"),
    }


def get_normalized_value(row, normalized_key):
    """
    Given a dict of an arbitrary banking transaction, pull out the value by the normalized key specified.
    For instance if the normalized key is 'Description', the value could come from a dict entry named 'Memo', 'Info', etc.
    See HEADER_MAPPINGS in settings.py configured via the settings.yaml file.
    """
    for key in HEADER_MAPPINGS[normalized_key]:
        if key in row:
            return row[key]

    logger.debug(f"No header could be mapped to [{normalized_key}] in transaction: \n{row}\n\n")
