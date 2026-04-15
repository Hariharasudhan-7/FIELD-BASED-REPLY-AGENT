import sys

def response(hey_bob):
    s = hey_bob.strip()

    if not s:
        return "Fine. Be that way!"

    is_question = s.endswith("?")

    has_alpha = any(c.isalpha() for c in s)
    is_yelling = has_alpha and s.upper() == s

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."