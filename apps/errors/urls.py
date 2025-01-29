from django.urls import path
from .views.error_views_5xx import custom_500
from .views.error_views_4xx import custom_400, custom_401, custom_403, custom_404, test_404

urlpatterns = [
    path('400', custom_400, name='400'),
    path('401', custom_401, name='401'),
    path('403', custom_403, name='403'),
    path('404', custom_404, name='404'),
    path('500', custom_500, name='500'),

    path('test_404', test_404, name='test_404'),
]