"""
All secrets must be defined as environment variables in the .env file.
Copy the .env.sample file and rename it to .env to get started.

Not using dotenv to load environment variables, because VSCode and the
poetry-dotenv-plugin automatically load the .env file.
"""

import os

GOOGLE_WORKSPACE_API_CLIENT_ID=os.getenv("GOOGLE_WORKSPACE_API_CLIENT_ID")
GOOGLE_WORKSPACE_API_CLIENT_SECRET=os.getenv("GOOGLE_WORKSPACE_API_CLIENT_SECRET")
