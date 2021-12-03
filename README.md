# Проект аналитики качества сырья

Сервис разворачивается на сайте: https://accenture-final.teambolognese.ru/

На текущий момент доступен функционал записи видеопотока на главной странице, а также их анализ на факт наличия брака, результат которого возвращается в запросах от сервера.

## Структура проекта

[Backend](app.py) - веб-сервер на bottle + sqlite3

[getter.py](getter.py) - Извлечение пикселей из фотографии

