from django.contrib import admin
from .models import *
from .resources import IngredientsRes
from import_export.admin import ImportExportModelAdmin

   

admin.site.register(Recipe)
admin.site.register(Unit)
admin.site.register(Ingredient_name)
admin.site.register(Ingredient)
admin.site.register(Messages)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Cuisine)