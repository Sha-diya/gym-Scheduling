from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "success": False,
            "message": response.data.get('detail', 'Validation error occurred.'),
            "errorDetails": response.data
        }

    return response
