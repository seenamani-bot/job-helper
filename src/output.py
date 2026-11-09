# output.py - shows the AI result in readable form and saves it to a file.
# Everything here stays on your computer.

import json
import os


def show_result(result):
    # Print skills as one comma-separated line.
    print("\n=== SKILLS ===")
    print(", ".join(result.get("skills", [])))

    # Print each job on its own lines.
    print("\n=== WORK HISTORY ===")
    for job in result.get("work_history", []):
        print(f"- {job.get('title', '')} at {job.get('company', '')} ({job.get('dates', '')})")
        if job.get("summary"):
            print(f"    {job['summary']}")

    # Print each school on one line.
    print("\n=== EDUCATION ===")
    for school in result.get("education", []):
        print(f"- {school.get('degree', '')}, {school.get('school', '')} ({school.get('dates', '')})")


def save_result(result, path="output/resume_result.json"):
    # Make sure the output folder exists, then write the result as JSON.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(result, f, indent=2)
    return path
