def calculate_rpn(severity, occurrence, detection):
    """
    Calculate Risk Priority Number.
    """

    if severity < 1 or severity > 10:
        raise ValueError("Severity must be between 1 and 10")

    if occurrence < 1 or occurrence > 10:
        raise ValueError("Occurrence must be between 1 and 10")

    if detection < 1 or detection > 10:
        raise ValueError("Detection must be between 1 and 10")

    return severity * occurrence * detection


if __name__ == "__main__":
    rpn = calculate_rpn(9, 7, 5)
    print(f"RPN = {rpn}")