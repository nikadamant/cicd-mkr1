import pytest
from src.text_analyzer.text_analyzer import count_words, count_sentences, analyze_file
import os

@pytest.fixture
def sample_text_file(tmp_path):
    content = "This is a test. It contains multiple sentences! Right? Yes..."
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

@pytest.mark.parametrize("text,expected", [
    ("Hello world", 2),
    ("Hello,world", 2),
    ("This:has;separators", 3),
    ("", 0),
    ("   ", 0)
])
def test_count_words(text, expected):
    assert count_words(text) == expected

@pytest.mark.parametrize("text,expected", [
    ("Hello.", 1),
    ("Hello! How are you?", 2),
    ("Wait... really?", 2),
    ("", 0)
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


def test_analyze_file(sample_text_file):
    result = analyze_file(str(sample_text_file))
    assert result['words'] == 10
    assert result['sentences'] == 4