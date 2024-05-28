from socket import gethostname

from apiflask import APIFlask, Schema, fields
from marshmallow import validate
import sentry_sdk

sentry_sdk.init(
    dsn="https://1876a7b2c4ba159d4adfd619c1f7ee2a@o4506166915235840.ingest.us.sentry.io/4507321532874752",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
app = APIFlask(
    __name__, title="Calculator API", version="1.0.0", docs_ui="redoc"
)
app.config["INFO"] = {'description': '這是簡易計算機的 API 文件。'}
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
    x = fields.Float(required=True, metadata={"description": "數字一"})
    y = fields.Float(required=True, metadata={"description": "數字二"})
    operation = fields.String(
        required=True,
        metadata={"description": "運算符號"},
        validate=validate.OneOf(
            ["add", "subtract", "multiply", "divide"]
        )
    )
    # 移除 post_load 使 Division by zero 驗證失效


@app.post("/calculate")
@app.input(MathOperationSchema, location="json")
def do_calculation(json_data):
    """進行數學運算"""
    operation_mapper = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y,
    }
    handler = operation_mapper[json_data["operation"]]
    return {
        "result": True,
        "data": handler(json_data['x'], json_data['y']),
        "reply_from": gethostname()
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7500, debug=True)
