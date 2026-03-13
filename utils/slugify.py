import re
import unicodedata


class SlugifyError(ValueError):
    pass


def slugify(text: str) -> str:
    """
    Convert a string into a URL-friendly slug.

    Example:
        "Hello World!" -> "hello-world"
    """
    if not isinstance(text, str) or not text.strip():
        raise SlugifyError("Input must be a non-empty string")

    # Normalize unicode characters
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    # Lowercase
    text = text.lower()

    # Replace non-alphanumeric characters with hyphen
    text = re.sub(r"[^a-z0-9]+", "-", text)

    # Remove leading/trailing hyphens
    text = text.strip("-")

    if not text:
        raise SlugifyError("Slug cannot be empty after normalization")

    return text
