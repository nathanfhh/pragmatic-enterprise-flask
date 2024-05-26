from apiflask import APIFlask, Schema, fields
from marshmallow import validate, post_load

app = APIFlask(__name__)
app.config["VALIDATION_ERROR_STATUS_CODE"] = 400


class CustomException(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


@app.errorhandler(CustomException)
def handle_custom_exception(error):
    return {
        "result": False,
        "message": error.message
    }, error.status_code


class MathOperationSchema(Schema):
    x = fields.Float(required=True)
    y = fields.Float(required=True)
    operation = fields.String(
        required=True,
        validate=validate.OneOf(
            ["add", "subtract", "multiply", "divide"]
        )
    )

    @post_load
    def validate_division_by_zero(self, data, **kwargs):
        if data["operation"] == "divide" and data["y"] == 0:
            raise CustomException("Division by zero is not allowed")
        return data


@app.post("/calculate")
@app.input(MathOperationSchema, location="json")
def do_calculation(json_data):
    operation_mapper = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y,
    }
    handler = operation_mapper[json_data["operation"]]
    return {
        "result": True,
        "data": handler(json_data['x'], json_data['y'])
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7500, debug=True)
