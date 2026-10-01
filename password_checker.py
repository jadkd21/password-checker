#!/usr/bin/env python3
"""
Password Strength Checker
Rates a password and explains exactly how to make it stronger.

Everything runs locally on your PC - your password is never
sent anywhere. (Real attackers do the same math offline.)

How to run:  python password_checker.py
"""

import getpass
import math

# The most commonly used (and first-guessed) passwords.
# If yours is on this list, it fails instantly.
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "12345678", "111111", "123123", "admin",
    "letmein", "welcome", "monkey", "dragon", "qwerty123",
    "password123", "1234567", "12345", "princess", "azerty",
    "football", "1234567890", "000000", "iloveyou", "starwars",
}

# How many guesses per second a modern cracking rig can try
GUESSES_PER_SECOND = 10_000_000_000


def estimate_crack_time(password):
    """Roughly how long brute force would take, in human words."""
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32  # symbols

    combinations = charset ** len(password)
    seconds = combinations / GUESSES_PER_SECOND

    if seconds < 1:
        return "instantly"
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.1f} minutes"
    hours = minutes / 60
    if hours < 48:
        return f"{hours:.1f} hours"
    days = hours / 24
    if days < 365:
        return f"{days:.1f} days"
    years = days / 365
    if years < 1_000_000:
        return f"{years:,.0f} years"
    return "longer than the age of the universe"


def check_password(password):
    """Score the password and collect feedback. Returns (score, feedback)."""
    score = 0
    feedback = []

    # Instant fail: it's on the most-guessed list
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is one of the most commonly used passwords in the world.",
                   "Attackers try it within the first seconds. Pick something unique."]

    # Length matters most
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Good length, but 12+ characters is much stronger.")
    else:
        feedback.append("Too short - use at least 8 characters, ideally 12+.")

    # Character variety
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add some lowercase letters.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add some UPPERCASE letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add some numbers.")
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add some symbols like ! @ # $.")

    return score, feedback


def rating(score):
    if score <= 2:
        return "WEAK"
    if score <= 4:
        return "FAIR"
    if score <= 5:
        return "STRONG"
    return "EXCELLENT"


def main():
    print("=" * 55)
    print("  PASSWORD STRENGTH CHECKER")
    print("  (runs 100% locally - nothing leaves your PC)")
    print("=" * 55)

    # getpass hides what you type, like a real login prompt
    password = getpass.getpass("\nEnter a password to test: ")
    if not password:
        print("No password entered.")
        return

    score, feedback = check_password(password)
    crack_time = estimate_crack_time(password)

    print(f"\n  Rating: {rating(score)} ({score}/6)")
    print(f"  Estimated time to crack: {crack_time}")

    if feedback:
        print("\n  How to improve:")
        for tip in feedback:
            print(f"   - {tip}")
    else:
        print("\n  Nothing to fix - this is a solid password.")

    print("\n  Tip: a long phrase you can remember beats a short")
    print("  complex one you can't. e.g. 'correct horse battery staple'")


if __name__ == "__main__":
    main()
