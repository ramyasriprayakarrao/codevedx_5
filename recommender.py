import csv
import math
import re
from pathlib import Path
from collections import Counter

DATA_FILE = Path(__file__).parent / "data" / "trainings.csv"

STOP_WORDS = {
    "and", "the", "for", "with", "from", "this", "that", "into", "are",
    "you", "your", "learn", "course", "training", "basic", "level"
}

def tokenize(text):
    words = re.findall(r"[a-zA-Z0-9+#.]+", (text or "").lower())
    return [word for word in words if word not in STOP_WORDS and len(word) > 1]

def load_trainings():
    with DATA_FILE.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))

def cosine_similarity(first, second):
    a, b = Counter(first), Counter(second)
    if not a or not b:
        return 0.0
    common = set(a) & set(b)
    dot = sum(a[word] * b[word] for word in common)
    norm_a = math.sqrt(sum(value * value for value in a.values()))
    norm_b = math.sqrt(sum(value * value for value in b.values()))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

def recommend_trainings(skills, interest, level):
    user_words = tokenize(f"{skills} {interest}")
    results = []
    for course in load_trainings():
        course_words = tokenize(
            " ".join([course["title"], course["category"], course["skills"],
                      course["description"], course["level"]])
        )
        score = cosine_similarity(user_words, course_words)
        if course["level"].lower() == level.lower():
            score += 0.12
        elif level.lower() == "beginner" and course["level"].lower() == "all levels":
            score += 0.08
        results.append((min(score, 1.0), course))

    results.sort(key=lambda item: item[0], reverse=True)
    return [
        {**course, "match": round(score * 100)}
        for score, course in results[:5]
    ]

def get_categories():
    return sorted({course["category"] for course in load_trainings()})
