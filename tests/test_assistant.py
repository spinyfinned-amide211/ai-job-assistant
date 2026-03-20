"""
Tests for AI Job Application Assistant
"""

import pytest
from src.scorer import calculate_match_score, get_missing_keywords, extract_keywords
from src.parser import _clean_text


def test_keyword_extraction():
    text = "Python developer with experience in machine learning and data science"
    keywords = extract_keywords(text)
    assert "python" in keywords
    assert "machine" in keywords
    assert "learning" in keywords


def test_match_score_perfect():
    cv = "Python developer machine learning TensorFlow PyTorch"
    job = "Python developer machine learning TensorFlow PyTorch"
    score = calculate_match_score(cv, job)
    assert score == 100.0


def test_match_score_zero():
    cv = "marketing sales business development"
    job = "Python developer machine learning"
    score = calculate_match_score(cv, job)
    assert score < 20.0


def test_match_score_partial():
    cv = "Python developer with React experience"
    job = "Python developer machine learning React Node.js"
    score = calculate_match_score(cv, job)
    assert 0 < score < 100


def test_missing_keywords():
    cv = "Python developer"
    job = "Python developer machine learning TensorFlow React"
    missing = get_missing_keywords(cv, job)
    assert len(missing) > 0
    assert "python" not in missing


def test_clean_text():
    text = "Hello   World\n\n\n\nTest"
    cleaned = _clean_text(text)
    assert "   " not in cleaned
    assert "\n\n\n" not in cleaned
