
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='Home'),
    path('Home/', views.home_view, name='Home'),
    path('About/', views.about_view, name='About'),
    path('creat/', views.creat_view, name='creat'),
    path('creat/upload', views.upload_view, name='uload'),
    path('cv/', views.cv_view, name='cv'),
    path('certificate/', views.certificate_view, name='certificate'),
    path('cerdetails/<pk>',views.cerdetails_view,name='cerdetails'),
    path('Coursedetails/<pk>',views.Coursedetails_view,name='Coursedetails'),
    path('Personal_interest/', views.Personal_interest_view, name='Personal_interest'),
    path('Personal_interest/<pk>', views.Personal_interest, name='Personal_interest'),
    path('Personal_project/', views.Personal_project_view, name='Personal_project'),
    path('Personal_project/<pk>', views.Personal_project, name='Personal_project'),
    path('Personal_project/project_details/<id>', views.Personal_project_view, name='Personal_project'),
    
]
