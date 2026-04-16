# BASE_URL = "https://testing.sourceoptima.com/"

# import os

# # Base URL
# BASE_URL = os.getenv("BASE_URL", "https://testing.sourceoptima.com/")

# # Credentials (NEVER hardcode in real projects)
# USERNAME = os.getenv("USERNAME", "your_username")
# PASSWORD = os.getenv("PASSWORD", "your_password")

# # Browser
# BROWSER = os.getenv("BROWSER", "chrome")

# # Timeout
# TIMEOUT = int(os.getenv("TIMEOUT", 20))

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = os.getenv("BASE_URL", "https://testing.sourceoptima.com/")

DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")