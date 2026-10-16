def validate_title(title: str) -> str:
    """Validate and normalize a task title."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Judul tugas tidak boleh kosong.")

    return title.strip()
