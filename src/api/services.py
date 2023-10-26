from files.models import File


class Handlers:

    def image_handler(file: File) -> None:
        """Обработка картинок."""
        ...

    def audio_handler(file: File) -> None:
        """Обработка звуковых файлов."""
        ...

    def text_handler(file: File) -> None:
        """Обработка текстовых файлов."""
        ...
