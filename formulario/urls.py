from django.contrib import admin
from django.urls import path, include
from django.urls import re_path,include

from .views import  *

#INFORMES EVALUA 2.0
from .EVA_00_exp import *
from .EVA_01_exp import *
from .EVA_02_exp import *
from .EVA_03_exp import *
from .EVA_04_exp import *
from .EVA_05_exp import *
from .EVA_06_exp import *
from .EVA_07_exp import *
from .EVA_08_exp import *
from .EVA_09_exp import *
from .EVA_10_exp import *

#INFORMES EVALUA 3.0
from .evalua08export import *
from .evalua09export import *
from .evalua10export import *


#VISTAS EVALUA 2.0
from .EVA2 import *

urlpatterns = [
    #path("", Listado_Estudiantes),
    path("", login),
    path("URL1", input_new),

    path("vista_PIE",vista_PIE), 

    path("EVALUAV2",EVALUAV2,name="EVALUA2.0"),

    path("EVALUAV3",EVALUAV3,name="EVALUA3.0"),

    #####VERSIONES 2.0

    path('EVA2_00', NUEVO_EVA2_00.as_view()),
    path ("delete/E2_00/<pk>/", borrar_E2_00),
    path("Listado_E2_00", Listado_E2_00, name ="Listado_E2_00"),
    path ("E2_00/<pk>/",EDITAR_EVA2_00.as_view()),#nuevo editar
    path("test/E2_00/<pk>/",EV2_00EXP2),

    path('EVA2_01', NUEVO_EVA2_01.as_view()),
    path ("delete/E2_01/<pk>/", borrar_E2_01),
    path("Listado_E2_01", Listado_E2_01, name ="Listado_E2_01"),
    path ("E2_01/<pk>/",EDITAR_EVA2_01.as_view()),#nuevo editar
    path("test/E2_01/<pk>/",EV2_01EXP2),

    path('EVA2_02', NUEVO_EVA2_02.as_view()),
    path ("delete/E2_02/<pk>/", borrar_E2_02),
    path("Listado_E2_02", Listado_E2_02, name ="Listado_E2_02"),
    path ("E2_02/<pk>/",EDITAR_EVA2_02.as_view()),#nuevo editar
    path("test/E2_02/<pk>/",EV2_02EXP2),

    path('EVA2_03', NUEVO_EVA2_03.as_view()),
    path ("delete/E2_03/<pk>/", borrar_E2_03),
    path("Listado_E2_03", Listado_E2_03, name ="Listado_E2_03"),
    path ("E2_03/<pk>/",EDITAR_EVA2_03.as_view()),#nuevo editar
    path("test/E2_03/<pk>/",EV2_03EXP2),

    path('EVA2_04', NUEVO_EVA2_04.as_view()),
    path ("delete/E2_04/<pk>/", borrar_E2_04),
    path("Listado_E2_04", Listado_E2_04, name ="Listado_E2_04"),
    path ("E2_04/<pk>/",EDITAR_EVA2_04.as_view()),#nuevo editar
    path("test/E2_04/<pk>/",EV2_04EXP2),

    path('EVA2_05', NUEVO_EVA2_05.as_view()),
    path ("delete/E2_05/<pk>/", borrar_E2_05),
    path("Listado_E2_05", Listado_E2_05, name ="Listado_E2_05"),
    path ("E2_05/<pk>/",EDITAR_EVA2_05.as_view()),#nuevo editar
    path("test/E2_05/<pk>/",EV2_05EXP2),

    path('EVA2_06', NUEVO_EVA2_06.as_view()),
    path ("delete/E2_06/<pk>/", borrar_E2_06),
    path("Listado_E2_06", Listado_E2_06, name ="Listado_E2_06"),
    path ("E2_06/<pk>/",EDITAR_EVA2_06.as_view()),#nuevo editar
    path("test/E2_06/<pk>/",EV2_06EXP2),

    path('EVA2_07', NUEVO_EVA2_07.as_view()),
    path ("delete/E2_07/<pk>/", borrar_E2_07),
    path("Listado_E2_07", Listado_E2_07, name ="Listado_E2_07"),
    path ("E2_07/<pk>/",EDITAR_EVA2_07.as_view()),#nuevo editar
    path("test/E2_07/<pk>/",EV2_07EXP2),


    path('EVA2_08', NUEVO_EVA2_08.as_view()),
    path ("delete/E2_08/<pk>/", borrar_E2_08),
    path("Listado_E2_08", Listado_E2_08, name ="Listado_E2_08"),
    path ("E2_08/<pk>/",EDITAR_EVA2_08.as_view()),#nuevo editar
    path("test/E2_08/<pk>/",EV2_08EXP2),

    path('EVA2_09', NUEVO_EVA2_09.as_view()),
    path ("delete/E2_09/<pk>/", borrar_E2_09),
    path("Listado_E2_09", Listado_E2_09, name ="Listado_E2_09"),
    path ("E2_09/<pk>/",EDITAR_EVA2_09.as_view()),#nuevo editar
    path("test/E2_09/<pk>/",EV2_09EXP2),


    path('EVA2_10', NUEVO_EVA2_10.as_view()),
    path ("delete/E2_10/<pk>/", borrar_E2_10),
    path("Listado_E2_10", Listado_E2_10, name ="Listado_E2_10"),
    path ("E2_10/<pk>/",EDITAR_EVA2_10.as_view()),#nuevo editar
    path("test/E2_10/<pk>/",EV2_10EXP2),



    #####VERSIONES 3.0

    path('EVA8', NUEVO_EVA8.as_view()),
    path ("delete/E08/<pk>/", borrar_E08),
    path("Listado_E08", Listado_E08, name ="Listado_E08"),
    path ("E08/<pk>/",EDITAR_EVA8.as_view()),#nuevo editar
    path("test/E08/<pk>/",EV08EXP2),


    path('EVA9', NUEVO_EVA9.as_view()),
    path ("delete/E09/<pk>/", borrar_E09),
    path("Listado_E09", Listado_E09, name ="Listado_E09"),
    path ("E09/<pk>/",EDITAR_EVA9.as_view()),#nuevo editar
    path("test/E09/<pk>/",EV09EXP2),


    path('EVA10', NUEVO_EVA10.as_view()),
    path ("delete/E10/<pk>/", borrar_E10),
    path("Listado_E10", Listado_E10, name ="Listado_E10"),
    path ("E10/<pk>/",EDITAR_EVA10.as_view()),#nuevo editar
    path("test/E10/<pk>/",EV10EXP2),



    path("EV09", Vista_EVALUA_09),
    path("EV10", Vista_EVALUA_10),

    path("EV11", Vista_EVALUA_11),
    path("exito", vista_exito, name="url_exito"),
    path("listado", Listado_Estudiantes),
#    re_path("EST/(?P<pk>\d+)$", Detalle_Estudiantes, name='Detalle_Estudiantes'),
  # re_path(r'^EST/(?P<pk>\d+)$', Detalle_Estudiantes, name='Detalle_Estudiantes'),
    path ("estudiante/<Rut>/", Detalle_Estudiantes, name='Detalle_Estudiantes'),
    #path ("editar+Detalle_Estudiantes", Edit_EST, name= 'Editar_Estudiantes'),
    path ("delete/estudiante/<Rut>/", borrar),
    path("exportar1", export_users_xls, name ="exportar1"),

    path("Listado_E09", Listado_E09, name ="Listado_E09"),
    path("E009/<pk>/", Detalle_Estudiantes_E09), #antiguo
    path ("delete/E09/<pk>/", borrar_E09),
    path ("E09/<pk>/",EDITAR_EVA9.as_view()),#nuevo editar
    path("portada", portada, name = "menu"),
    #path('', welcome),
    #path('register', register),
    path('login/', login, name="login"),
    path('logout', logout),

    path("Profesional",Profesional),
    path("Detalle_PRO",Detalle_PRO),
    #path('admin/', admin.site.urls),

]
