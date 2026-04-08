# BASE_URL = "https://testing.sourceoptima.com/"

import os

# Base URL
BASE_URL = os.getenv("BASE_URL", "https://testing.sourceoptima.com/")

# Credentials (NEVER hardcode in real projects)
USERNAME = os.getenv("USERNAME", "your_username")
PASSWORD = os.getenv("PASSWORD", "your_password")

# Browser
BROWSER = os.getenv("BROWSER", "chrome")

# Timeout
TIMEOUT = int(os.getenv("TIMEOUT", 20))