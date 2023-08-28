from flask import jsonify

class ReturnJsonRequest:
    def __init__(self) -> None:
        self.object_return = {
            "code": "",
            "message": "",
            "data": {}
        }

    def json_return_format(self, code=int, message=str, data=None):
        self.object_return["code"] = code
        self.object_return["message"] = message
        self.object_return["data"] = data
        return jsonify(**self.object_return), 201
        # return jsonify(self.object_return)