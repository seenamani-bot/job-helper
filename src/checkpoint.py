# checkpoint.py - shows exactly what would be sent to the AI and asks first.
# Nothing is sent unless you type y.


def confirm_send(text):
    # Print the exact text between two lines so you can read it carefully.
    print("========== TEXT THAT WOULD BE SENT TO THE AI ==========")
    print(text)
    print("=======================================================")
    print("Characters:", len(text))

    # Ask the question. Only a plain "y" counts as yes.
    answer = input("Send this to the AI? (y/n): ").strip().lower()
    return answer == "y"
