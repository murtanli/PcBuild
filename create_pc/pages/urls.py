from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name="main_page"),
    path('search/', search_page, name="search_page"),
    path('info/', info_page, name="info_page"),
    path('configurator/<int:pc_build_id>/', configurator_page, name="configurator_page"),
    path('order_pc/<int:pc_build_id>/', order_pc, name="order_pc"),
    path('place_order/', place_order, name="place_order"),
    path('logout/', logout_view, name="logout_view"),
    path('auth/', auth, name="auth"),
    path('sign_in/', sign_in, name="sign_in"),
]
