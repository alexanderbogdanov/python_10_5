import os


class URLs:
    BASE_URL = 'https://demoqa.com/'


class FilePaths:
    test_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PHOTO_PATH = os.path.join(test_directory, "tests/resources/bkb.jpeg")
    USER_DATA_PATH = os.path.join(test_directory, "data/user_data.json")
