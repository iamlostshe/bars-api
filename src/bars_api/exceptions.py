"""Исключения."""


class UserNotAuthenticatedError(Exception):
    """Пользователь не найден."""

    def __init__(self) -> None:
        """Пользователь не найден."""
        self.text = (
            "<b>Ошибка во время парсинга:</b>\n\n"
            "Для выполнения этого действия необходимо авторизоваться в боте.\n\n"
            "Инструкция по авторизации доступна по -> /start"
        )
        super().__init__(self.text)


class ValidationError(Exception):
    """Ошибка валидации."""

    def __init__(self) -> None:
        """Ошибка валидации."""
        self.text = (
            "<b>Ошибка во время парсинга:</b>\n\n"
            "Ошибка валидации (Client.ValidationError)"
        )
        super().__init__(self.text)
