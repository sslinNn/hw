# Тут думаю, очевидно всё
```python
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
```
![image](https://github.com/user-attachments/assets/f20306e9-d2ae-4318-a2dc-fc7a9321b72b)
![image](https://github.com/user-attachments/assets/5614288f-c176-48b1-9cc3-dd6c5241f0a1)


