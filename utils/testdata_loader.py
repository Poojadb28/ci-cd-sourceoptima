# import os
# import json

# def load_test_data():
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     file_path = os.path.join(BASE_DIR, "testdata", "testdata.json")

#     with open(file_path) as file:
#         return json.load(file)

import json
from config.config import TEST_DATA_PATH

def load_test_data():
    try:
        with open(TEST_DATA_PATH, "r") as file:
            return json.load(file)
    except Exception as e:
        raise Exception(f"Failed to load test data: {e}")