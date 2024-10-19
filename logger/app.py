from flask import Flask
import logging

app = Flask(__name__)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


@app.route('/')
def home():
    logger.info("Главная страница была запрошена")
    return "Добро пожаловать на главную страницу!"


@app.route('/debug')
def debug_route():
    logger.debug("Debug route accessed")
    return "Это страница для отладки!"


@app.route('/error')
def error_route():
    try:
        1 / 0  # Пример ошибки
    except ZeroDivisionError as e:
        logger.error("Ошибка деления на ноль!", exc_info=True)
    return "Произошла ошибка!"


@app.route('/critical')
def critical_route():
    logger.critical("Критическая ошибка на этой странице!")
    return "Критическая ошибка!"


if __name__ == '__main__':
    app.run(debug=True)
