from collections import defaultdict
from random import randint
from app.config import settings
import pickle

ORIGINAL_MAPPING = [
    ("Performance and optimization", [0, 2, 8, 10, 12, 26, 32, 28, 33, 40, 34]),
    ("Data Processing", [1, 7, 9, 11, 13, 22, 37, 39, 14, 20, 23, 24, 27, 31]),
    ("Graphs", [3, 4, 5, 15]),
    ("Theoretical research", [6, 17, 18, 35, 36]),
    ("Electronic", [16, 19, 21]),
    # ("Other", [25, 29, 30, 38, 41]),
]

MAPPING = defaultdict(lambda: "Other")
for pair in ORIGINAL_MAPPING:
    for number in pair[1]:
        MAPPING[number] = pair[0]

model = None
if settings.MODEL_PATH is not None:
    try:
        with open(settings.MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        print("Clustering model file not found, mocking...")


def get_cluster(text: str) -> int:
    if model is not None:
        return model.predict([text])[0][0]

    return randint(0, 40)


def get_tag(text: str) -> str:
    return MAPPING[get_cluster(text)]
