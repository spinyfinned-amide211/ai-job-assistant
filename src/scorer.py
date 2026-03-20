"""
Scorer module — CV vs Job keyword matching
"""

import re
from collections import Counter


STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "must", "can", "this", "that", "these",
    "those", "i", "you", "he", "she", "we", "they", "it", "its"
}


def extract_keywords(text: str, top_n: int = 50) -> set:
    """Extract meaningful keywords from text."""
    words = re.findall(r'\b[a-zA-Z][a-zA-Z0-9+#.-]{2,}\b', text.lower())
    filtered = [w for w in words if w not in STOP_WORDS]
    counts = Counter(filtered)
    return set(w for w, _ in counts.most_common(top_n))


def calculate_match_score(cv_text: str, job_text: str) -> float:
    """Calculate keyword match score between CV and job posting."""
    cv_keywords = extract_keywords(cv_text)
    job_keywords = extract_keywords(job_text)

    if not job_keywords:
        return 0.0

    matches = cv_keywords.intersection(job_keywords)
    score = (len(matches) / len(job_keywords)) * 100
    return min(score, 100.0)


def get_missing_keywords(cv_text: str, job_text: str, top_n: int = 10) -> list:
    """Get top missing keywords from job posting not in CV."""
    cv_keywords = extract_keywords(cv_text, top_n=100)
    job_keywords = extract_keywords(job_text, top_n=top_n * 2)
    missing = job_keywords - cv_keywords
    return list(missing)[:top_n]
