print('Hello from repository!') 

import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из .env файла
    load_dotenv()
    
    # Читаем значение переменной AUTHOR
    author = os.getenv('AUTHOR')
    
    # Выводим имя автора
    print(f"Автор проекта: {author}")

# Вызов функции для проверки
if __name__ == "__main__":
    print_author()
