from django.contrib import admin

from .models import Post

admin.site.register(Post) #Dadurch wird das Model auf der Admin-Seite angezeigt
