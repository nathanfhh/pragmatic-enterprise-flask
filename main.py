from flask import Flask, request

app = Flask(__name__)


@app.post("/calculate")
def do_calculation():
    json_data = request.get_json(silent=True)
    if not json_data:
        return {"result": False, "message": "No JSON data received"}, 400
    if (number1 := json_data.get("x")) is None or (number2 := json_data.get("y")) is None:
        return {"result": False, "message": "Please provide two numbers."}, 400
    if not all(map(lambda x: isinstance(x, (int, float)), (number1, number2))):
        return {"result": False, "message": "Numbers must be integers or floats."}, 400
    operation_mapper = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y,
    }
    operation = json_data.get("operation")
    if not (handler := operation_mapper.get(operation)):
        return {"result": False, "message": "Invalid operation"}, 400
    try:
        result = handler(number1, number2)
    except ZeroDivisionError:
        return {"result": False, "message": "Division by zero"}, 400
    return {"result": True, "data": result}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7500, debug=True)
