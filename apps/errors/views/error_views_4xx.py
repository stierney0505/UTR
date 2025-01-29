from django.http import HttpResponse
from django.template import loader

def custom_400(request, exception=None, error_message=None, error_title=None):
    template = loader.get_template('errors/generic_error.html')
    error_message = error_message if error_message is not None else "Sorry, there was an issue with your request."
    error_title = error_title if error_title is not None else "Bad Request"

    context = {
        'error_code' : 400,
        'error_title' : error_title,
        'error_message' : error_message,
    }

    return HttpResponse(template.render(context, request), status=400)

def custom_401(request, exception=None, error_message=None, error_title=None):
    template = loader.get_template('errors/generic_error.html')
    error_message = error_message if error_message is not None else "Sorry, authentication (and perhaps authorization) is required for this resource."
    error_title = error_title if error_title is not None else "Unauthorized"

    context = {
        'error_code' : 401,
        'error_title': error_title,
        'error_message': error_message,
    }

    return HttpResponse(template.render(context, request), status=401)

def custom_403(request, exception=None, error_message=None, error_title=None):
    template = loader.get_template('errors/generic_error.html')
    error_message = error_message if error_message is not None else "Sorry, you are not authorized to access this resource."
    error_title = error_title if error_title is not None else "Forbidden"

    context = {
        'error_code': 403,
        'error_title': error_title,
        'error_message': error_message,
    }

    return HttpResponse(template.render(context, request), status=403)

def custom_404(request, exception=None, error_message=None, error_title=None):
    template = loader.get_template('errors/generic_error.html')
    error_message = error_message if error_message is not None else "Sorry, the server could not find the requested resource."
    error_title = error_title if error_title is not None else "Not Found"

    context = {
        'error_code': 404,
        'error_title': error_title,
        'error_message': error_message,
    }

    return HttpResponse(template.render(context, request), status=404)

from django.http import HttpResponseNotFound

def test_404(request):
    return HttpResponseNotFound("This is a manual 404 error")
