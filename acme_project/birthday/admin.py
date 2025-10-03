from django.contrib import admin
# Из модуля models импортируем модель Birthday...
from .models import Tag

# ...и регистрируем её в админке:
# admin.site.register(Birthday)
admin.site.register(Tag)
