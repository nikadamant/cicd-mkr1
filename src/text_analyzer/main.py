import argparse
import os
from pathlib import Path
from src.text_analyzer.text_analyzer import analyze_file


def main():
    parser = argparse.ArgumentParser(
        description='Analyze text file for word and sentence counts.'
    )
    parser.add_argument('file_path', help='Path to the text file to analyze')

    try:
        args = parser.parse_args()

        # Convert to absolute path relative to project root
        project_root = Path(__file__).parent.parent
        input_path = (project_root / args.file_path).resolve()

        print(f"Looking for file at: {input_path}")

        result = analyze_file(input_path)

        print(f"Analysis results for {input_path}:")
        print(f"Words: {result['words']}")
        print(f"Sentences: {result['sentences']}")

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
