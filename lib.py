import hashlib


def format_message(author: str, text: str) -> str:
    """Форматує рядок повідомлення."""

return f"[{author.upper()}]: {text.strip()}"


def compute_sha256(data: str) -> str:
    """Обчислює хеш SHA-256 від тексту."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()