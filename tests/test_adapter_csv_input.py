import os
from pprint import pprint

from adapters.inputs.csv_input import get_normalized_value


def test_get_normalized_value(monkeypatch, mocker):
    mock_logger = mocker.MagicMock()
    monkeypatch.setattr("adapters.inputs.csv_input.logger", mock_logger)

    # define how to map arbitrary CSV headers to normalized headers (keys)
    monkeypatch.setattr(
        "adapters.inputs.csv_input.HEADER_MAPPINGS",
        {"other": ["col1", "not the other"], "test": ["not it", "col2", "nope"]},
    )
    input_row = {"col1": "col1", "col2": "col2", "col3": "col3"}
    expected = "col2"

    assert expected == get_normalized_value(input_row, "test")

    # print("debug", mock.logger.debug.mock_calls)

    assert mock_logger.debug.call_count == 0
    assert mock_logger.warning.call_count == 0


def test_get_missing_normalized_value(monkeypatch, mocker):
    mock_logger = mocker.MagicMock()
    monkeypatch.setattr("adapters.inputs.csv_input.logger", mock_logger)

    # define how to map arbitrary CSV headers to normalized headers (keys)
    monkeypatch.setattr(
        "adapters.inputs.csv_input.HEADER_MAPPINGS",
        {"other": ["col1", "not the other"], "test": ["not it", "test", "nope"]},
    )
    input_row = {"col1": "col1", "col2": "col2", "col3": "col3"}
    expected = None

    assert expected == get_normalized_value(input_row, "test")
    assert mock_logger.debug.call_count == 1


# def test_normalize_row(mocker):
#     # define how to map arbitrary CSV headers to normalized headers (keys)
#     mocker.patch("settings.HEADER_MAPPINGS", {"Date": "col1", "Amount": "col2", "Description": "col3"})
#     input_row = {"col1": "col1", "col2": "col2", "col3": "col3"}
#     expected = {"Date": "col1", "Amount": "col2", "Description": "col3"}

#     assert expected == normalize_row(input_row)


# def test_normalize_csv(mocker):
#     # Mock logger methods (make them no-op)
#     mock_logger = mocker.patch("settings.logger")
#     mock_logger.debug = mocker.MagicMock()
#     mock_logger.info = mocker.MagicMock()
#     mock_logger.warning = mocker.MagicMock()
#     mock_logger.error = mocker.MagicMock()
#     mock_logger.critical = mocker.MagicMock()

#     app_root = os.path.dirname(os.path.abspath(__file__))
#     file_path = f"{app_root}/tests/fixtures/park_bank.csv"
#     correctly_normalized_csv = {"col2": "col2", "col3": "col3", "col7": "col7"}

#     normalized_csv = normalize_csv(file_path)
#     pprint(normalized_csv)

#     assert normalized_csv == correctly_normalized_csv
