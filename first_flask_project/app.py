from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)

# Определяем маршрут и привязываем его к функции
@app.route('/')
def greeting():
    return "Hello, Flask!"

# 1: Простые маршруты
@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."

# 2: Динамические маршруты
@app.route('/calc/<string:x>/<string:y>')
def calc(x: str, y: str):
    def to_number(value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return None

    x_num = to_number(x)
    y_num = to_number(y)

    if x_num is None or y_num is None:
        return 'Были введены некорректные данные.', 400

    return f"The sum of {x_num} and {y_num} is {x_num + y_num}"

# 3. Маршрут /reverse/, который переворачивает текст.
@app.route('/reverse/<path:x>')
def reverse(x:str):
    return f"{x[::-1]}"

# 4. Маршрут /user//
@app.route('/user/<path:name>/<int:age>')
def user(name:str, age:int):
    if age <= 0:
        return 'Были введены некорректные данные.', 400
    return f"Hello, {name}. You are {age} years old."



# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)