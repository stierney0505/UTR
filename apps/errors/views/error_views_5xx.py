from django.http import HttpResponse
from django.template import loader

def custom_500(request, exception=None, error_message=None, error_title=None):
    template = loader.get_template('errors/generic_error.html')
    error_message = error_message if error_message is not None else "Sorry, the server encountered an internal error proccessing your request."
    error_title = error_title if error_title is not None else "Server Error"

    context = {
        'error_code' : 500,
        'error_title' : error_title,
        'error_message' : error_message,
    }

    return HttpResponse(template.render(context, request), status=500)
