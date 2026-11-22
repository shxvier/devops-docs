"""Формирование строки состояния документации."""


def format_status(version: str, deployed: bool) -> str:
    """Возвращает версию и состояние публикации в одной строке."""
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"


if __name__ == "__main__":
    print(format_status("1.0", deployed=True))
