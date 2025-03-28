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