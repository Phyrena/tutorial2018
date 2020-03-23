from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('spiel_website/', views.spiel_Website_view, name='spiel_Website'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('to_do_list/', views.to_do_list_view, name='to_do_list'),
    path('Klassen/', views.klassen_view, name='klassen'),
    path('Downloads/', views.downloads_view, name='downloads'),
    path('Forum/', views.forum_view, name='forum'),
    path('Team/', views.team_view, name='team'),
    path('Neuste_Beiträge/', views.forum_post_list, name='neuste_beiträge'),
    path('add_todo/', views.add_todo, name='add_todo'),
]
