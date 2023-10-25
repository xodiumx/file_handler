# file_handler

```
Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

- Создать Django проект и приложение.
- Использовать Django REST Framework для создания API.
- Реализовать модель File, которая будет представлять загруженные файлы. Модель должна содержать поля:
  1. file: поле типа FileField, используемое для загрузки файла.
  2. uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
  3. processed: поле типа BooleanField, указывающее, был ли файл обработан.
- Реализовать сериализатор для модели File.
- Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.
- Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.
- Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.
- Использовать Docker для развертывания проекта.
- Реализовать механизм для обработки различных типов файлов (например, изображений, текстовых файлов и т.д.).
- Предусмотреть обработку ошибок и возвращение соответствующих кодов статуса и сообщений об ошибках.
```

## Установка через `Docker`

1. Cклонируйте репозиторий
```
git clone git@github.com:xodiumx/file_handler.git
```
3. Перейдите в директорию
```
cd src
```
2. В директории `src` создайте `.env` file
```
SECRET_KEY='django-insecure-y&2fj&1trnl)n4j5b&s*3r*bn4_#z*y11o$#^qw6j)=5@y(-k2'

DB_NAME=handler
DB_HOST=db
# DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=admin
DB_ENGINE=django.db.backends.postgresql

POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin

PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
CELERY_TASK_TRACK_STARTED=True
CELERY_TASK_TIME_LIMIT=60

FLOWER_USER=admin
FLOWER_PASSWORD=admin

DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin
```
3. Выполните команду
```
docker-compose up -d
```

## Доступные эндпоинты

- `localhost/admin` - данные для входа - admin:admin
- `localhost/api/v1/upload` - эндпоинт для загрузки файлов
- `localhost/api/v1/files` - эндпоинт для получения информации о всех файлах
- `localhost:5050/` - `pgadmin` эндпоинт
- `localhost:5555/flower/` - `flower` эндпоинт
