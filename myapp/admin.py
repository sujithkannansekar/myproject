from django.contrib import admin
from .models import Folvika
from .models import reserve
from .models import reserves
# Register your models here.

admin.site.register(Folvika)
admin.site.register(reserve)
admin.site.register(reserves)