import re

def format_message(text: str) -> str:
    """Clean and format a message for display."""
    return text.strip()

def validate_input(text: str) -> bool:
    """Validate user input for safety."""
    # Block potential injection or spam
    blocked_patterns = [
        r"http[s]?://",  # URLs
        r"<script",      # HTML tags
        r"@\w+",         # Mentions
    ]
    for pattern in blocked_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return False
    return True
