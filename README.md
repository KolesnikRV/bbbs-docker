# Проект "Наставники" для НКО "Старшие Братья и Старшие Сёстры".

# Описание
### «Старшие Братья Старшие Сестры» — межрегиональная общественная организация содействия воспитанию подрастающего поколения. НКО поддерживает детей, которым требуется внимание: оставшихся без попечения родителей, приемных, детей из неполных, многодетных или неблагополучных семей, детей с ограниченными возможностями.

# Использованные технологии
- Python 3.8
- Django 3.2.3
- Django Rest Framework 3.12.4
- gunicorn 20.1.0
- Docker
- docker-compose
- Nginx
- Postgres

# Пройденные этапы / готовый функционал
[Этап 1 Базовые АПИ](backend/docs/backend-step1.md)
[Этап 2 Продолжаем пилить АПИ](backend/docs/backend-step2.md)
[Этап 3 Дорабатываем АПИ](backend/docs/backend-step3.md)
[Возможности администрирования](backend/docs/admin.md )
[Календарь](backend/docs/calendar.md )

# Инструкции по запуску
## Сборка и запуск контейнеров
- $: sudo docker-compose up -d --build

## Создание суперпользователя
- $: docker-compose exec backend make su
### Создастся суперпользователь admin:admin

# Авторы
## Backend
- Дмитрий Чуприн
- Александр Грязнов
- Илья Плотников
- Роман Колесник
- Юрий Матвеев

## Frontend
- Анна  Коротких
- Андрей  Ботыгин
- Мария  Слепухина
- Илья Сычугов

## QA
- Дарья Тихонова
- Ольга Богданова
