"""
All secrets must be defined as environment variables in the .env file.
Copy the .env.sample file and rename it to .env to get started.

Not using dotenv to load environment variables, because VSCode and the
poetry-dotenv-plugin automatically load the .env file.
"""

import os
import yaml
import logging

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


try:
    with open("settings.yaml", "r", encoding="utf-8") as settings_file:
        settings = yaml.safe_load(settings_file)
except FileNotFoundError:
    print(f"Error: The settings.yaml file was not found and is required to start Bud-Get.")
except yaml.YAMLError as e:
    print(f"Error: The settings.yaml file is not formatted correctly and can't be read: {e}")
except Exception as e:
    print(f"An unexpected error occurred while reading the settings.yaml file: {e}")

# === Logging ===
logger = logging.getLogger("bud-get")
logger.addHandler(logging.StreamHandler())
logger.setLevel(settings.get("log_level", "WARNING"))
logger.debug("Logging level set to %s", settings["log_level"])


HEADER_MAPPINGS = settings.get("header_mappings", {})
if "Date" not in HEADER_MAPPINGS:
    raise ValueError("Missing 'Date' header mapping in settings.yaml")

if "Amount" not in HEADER_MAPPINGS:
    raise ValueError("Missing 'Amount' header mapping in settings.yaml")

if "Description" not in HEADER_MAPPINGS:
    raise ValueError("Missing 'Description' header mapping in settings.yaml")

if "Category" not in HEADER_MAPPINGS:
    raise ValueError("Missing 'Category' header mapping in settings.yaml")
