import re

def sanitize_filename(filename, max_length=50):
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Trim long file names
    if len(filename) > max_length:
        filename = filename[:max_length] + "_"
    return filename

def sanitize_date(date):
    """
    Removes invalid characters in the date and makes it Windows compatible.
    """
    return date.replace(":", "-")
