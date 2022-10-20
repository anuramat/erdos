from collections import defaultdict
from random import randint

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


def get_cluster(text: str) -> int:
    return randint(0, 40)
