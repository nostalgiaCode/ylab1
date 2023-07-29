# ylab1
## Через Docker
1. загрузить репозиторий
2. установить docker desktop на windows 10 (Windows 10 64-bit: Home or Pro 21H2 (build 19044) or higher, or Enterprise or Education 21H2 (build 19044) or higher.)
3. запустить docker desktop
4. в командной строке перейти в папку, куда был загружен репозиторий
5. ввести команду docker compose up
6. docker всё соберёт и запустит, проект готов к использованию
7. *БД сохраняет данные при выходе, поэтому если БД не был очищен, то для повторного прохождения тестового сценария нужно удалить volume БД в docker'е
## Посложнее
1. запустить postgresql 
2. загрузить репозиторий
3. в файле api/models.py ввести данные доступа к БД и поменять "host=pgsql" на "host=localhost"
4. в командной строке перейти в папку, куда был загружен репозиторий, и создать виртуальное окружение "python -m venv venv"
5. запустить виртуальное окружение "venv\Scripts\activate"
6. установить зависимости "pip install -r requirements.txt"
7. запустить проект "uvicorn main:app --reload"
