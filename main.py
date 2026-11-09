# main.py - the starting point of the program.
# Usage: uv run main.py resumes/your_resume.docx

import sys

from src.ai_extractor import extract_resume_info
from src.checkpoint import confirm_send
from src.cleaner import clean_text, load_profile
from src.output import save_result, show_result
from src.resume_reader import read_resume


def main():
    # The resume path is given on the command line.
    if len(sys.argv) < 2:
        print("Usage: uv run main.py resumes/your_resume.docx")
        return

    # Piece 2: read the text from the resume (stays on this computer).
    text = read_resume(sys.argv[1])

    # Piece 3: remove personal details (still on this computer).
    profile = load_profile()
    cleaned = clean_text(text, profile)

    # Piece 4: show the exact text and ask before anything is sent.
    if not confirm_send(cleaned):
        print("Not sent. Stopping here.")
        return

    # Piece 5: send only the cleaned text to the AI.
    try:
        result = extract_resume_info(cleaned)
    except Exception as error:
        print("The AI step failed:", error)
        return

    # Piece 6: show the result and save it on this computer.
    show_result(result)
    path = save_result(result)
    print("\nSaved to:", path)


# Run main() only when this file is run directly.
if __name__ == "__main__":
    main()
