import uuid
from common.common_functions import ReturnJsonRequest

def get_user_id():
    # Generar un UUID
    new_uuid = str(uuid.uuid4())
    
    # Crear una respuesta JSON con el UUID
    data = {
        'user_id': new_uuid
    }
    format_response = ReturnJsonRequest(200, "Ok", data)
    return format_response.json_return_format()