from django.contrib import admin
from .models import Question, Choice, MapImage

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(MapImage)
