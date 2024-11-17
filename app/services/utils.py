# services/utils.py

def generate_consecutive_number(consecutive: int, value: int) -> str:
    """
    Generates a consecutive number with leading zeros based on the specified length.
    """
    return f"{consecutive:0>{value}}"


def format_text(text: str, value: int) -> str:
    """
    Formats the text to be left-justified to a specified length.
    """
    return text.ljust(value)


def format_number(value: str) -> str:
    """
    Formats a number to a fixed length with 4 decimal places.
    """
    formatted_value = f"{float(value):020.4f}"
    return formatted_value
