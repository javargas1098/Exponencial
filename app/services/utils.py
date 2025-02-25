# services/utils.py
from datetime import datetime

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


def format_number(text: str, value: int) -> str:
    """
    Formats a number to a fixed length with 4 decimal places.
    """
    formatted_value = f"{float(text):.4f}"
    formatted_value = formatted_value.rjust(value, '0')
    return formatted_value

def convert_date_to_custom_format(date_str):
    """Convert a date string from 'YYYY-MM-DD' to 'AAAAMMDD'."""
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Format the date into 'AAAAMMDD'
        return date_obj.strftime("%Y%m%d")
    except ValueError as e:
        print(f"Error converting date: {e}")
        return None
