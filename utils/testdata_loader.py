# import os
# import json

# def load_test_data():
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     file_path = os.path.join(BASE_DIR, "testdata", "testdata.json")

#     with open(file_path) as file:
#         return json.load(file)

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_test_data(filename):
    file_path = os.path.join(BASE_DIR, "testdata", filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    with open(file_path, "r") as f:
        return json.load(f)