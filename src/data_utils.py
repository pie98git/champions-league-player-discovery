import re
import unicodedata


def normalize_name(name):
    """Normalize player names for matching across datasets."""
    name = str(name)
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("utf-8")
    name = name.lower()
    name = re.sub(r"\s+", " ", name)
    return name.strip()