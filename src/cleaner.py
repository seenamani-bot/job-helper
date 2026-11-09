# cleaner.py - removes personal details from resume text.
# Plain code only. Nothing is sent anywhere.

import json
import re


def load_profile(path="profile.json"):
    # Read the small file you filled in (name and address).
    with open(path) as f:
        return json.load(f)


def remove_emails(text):
    # Anything shaped like  something@something.something
    return re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[EMAIL]", text)


def remove_linkedin(text):
    # Links such as linkedin.com/in/yourname (with or without https://www.)
    return re.sub(r"(https?://)?(www\.)?linkedin\.com/\S*", "[LINKEDIN]", text, flags=re.IGNORECASE)


def remove_phones(text):
    # Phone numbers: 10 or more digits, allowing spaces, dots, dashes,
    # brackets and an optional + at the start.
    pattern = r"\+?\(?\d[\d\s().-]{8,}\d"
    return re.sub(pattern, "[PHONE]", text)


def remove_exact(text, value, label):
    # Remove one exact piece of text (like your name), ignoring capital letters.
    # Skip it if the profile field was left empty.
    value = value.strip()
    if value == "":
        return text
    return re.sub(re.escape(value), label, text, flags=re.IGNORECASE)


def remove_name(text, name):
    # Remove the full name first, then each part of it (first, last).
    # Parts shorter than 3 letters are skipped so we don't damage other words.
    text = remove_exact(text, name, "[NAME]")
    for part in name.split():
        if len(part) >= 3:
            text = remove_exact(text, part, "[NAME]")
    return text


def clean_text(text, profile):
    # Run every removal step, one after another.
    text = remove_linkedin(text)   # before email, so links stay whole
    text = remove_emails(text)
    text = remove_phones(text)
    text = remove_name(text, profile.get("name", ""))
    text = remove_exact(text, profile.get("address", ""), "[ADDRESS]")
    return text
