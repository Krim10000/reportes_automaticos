from django.contrib import admin

# Register your models here.
from .models import Modelo_Info_Per, Modelo_EVALUA_10, Modelo_EVALUA_09, Modelo_Info_Pro
from .models import *
#from .models import Persona_TEST
from . forms import *

admin.site.register(Modelo_Info_Per)
#admin.site.register(Persona_TEST)

#test evalua version 3.0
admin.site.register(Modelo_EVALUA_10)
admin.site.register(Modelo_EVALUA_09)

admin.site.register(Modelo_Info_Pro)

#test evalua version 2.0
admin.site.register(Modelo_EVALUA2_00)
admin.site.register(Modelo_EVALUA2_01)
admin.site.register(Modelo_EVALUA2_02)
admin.site.register(Modelo_EVALUA2_03)
admin.site.register(Modelo_EVALUA2_04)
admin.site.register(Modelo_EVALUA2_05)
admin.site.register(Modelo_EVALUA2_06)
admin.site.register(Modelo_EVALUA2_07)
admin.site.register(Modelo_EVALUA2_08)
admin.site.register(Modelo_EVALUA2_09)
admin.site.register(Modelo_EVALUA2_10)
