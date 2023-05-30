from rest_framework.exceptions import APIException

class CustomException(APIException):
    status_code = 301
    default_detail = 'Custom exception has been called.'
    
    
class NotAcceptable(APIException):
    status_code = 406
    default_detail = "We cannot accept this because some fields are empty"
    
    