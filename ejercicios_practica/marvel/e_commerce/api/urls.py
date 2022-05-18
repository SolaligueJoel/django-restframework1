from django.urls import path
from e_commerce.api.hello_world_api import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('hello-world/', hello_world),
    path('get_comics/', get_comics),
    path('purchased_item/', purchased_item),
    path('hello-world-private/', hello_world_private),
]