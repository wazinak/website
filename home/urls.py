from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.new_list, name='new_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:new>/', views.new_detail, name='new_detail'),
    path('home/', views.index, name='home')

]
