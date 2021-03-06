from django.shortcuts import render

from .forms import *

from .models import *
from datetime import date
from datetime import datetime
hoy = date.today()


from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

#def input_new(request):
#    form = Form1()
#    return render (request, "form.html", {"form": form})
#https://www.hektorprofe.net/tutorial/django-sistema-registro-login-logout

########################################################
from django.shortcuts import render, redirect


######################################################
@login_required
def Profesional(request,):


    submitted= False
    if request.method == "POST":

        titulo= "Datos del profesional"

        form = Form_Pro(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= request.user
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_Pro()
        titulo= "Datos del profesional"
        if submitted in request.GET:
            submitted = True

    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo })


def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "portada.html")
    # En otro caso redireccionamos al login
    return redirect('login')
########################################################
# def register(request):
#     return render(request, "users/register.html")
########################################################


def login(request):
    # Creamos el formulario de autenticaci??n vac??o
    form = AuthenticationForm()
    if request.method == "POST":
        # A??adimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es v??lido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contrase??a
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/portada')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


########################################################
def logout(request):
    # Finalizamos la sesi??n
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
################################################################################
def portada(request):
    return render (request, "portada.html")

def EVALUAV3(request):
    titulo= " Bater??a Psicopedag??gica EVAL??A VERSI??N 3.0"
    return render (request, "EVALUA3.0.html",{"titulo" : titulo})

def EVALUAV2(request):
    titulo= " Bater??a Psicopedag??gica EVAL??A VERSI??N 2.0"
    return render (request, "EVALUA2.0.html",{"titulo" : titulo})


################################################################################
@login_required
#@permission_required( raise_exception=True)
def input_new(request):#nuevo estudiante
    titulo= "INGRESE LOS DATOS DE UN NUEVO ESTUDIANTE"
    Institucion =  Modelo_Info_Pro.objects.get(user=request.user).Institucion
    submitted= False

    if request.method == "POST":

        form = Form1(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= request.user# salva el valor de usuario
            post.Institucion =  Modelo_Info_Pro.objects.get(user=request.user).Institucion
            titulo= "LISTADO DE ESTUDIANTES"
            user = request.user
            Institucion=Modelo_Info_Pro.objects.get(user=user).Institucion
            estu = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")

            context_object_name = 'estudiante'
            post.save()
            return render(request, 'listado.html', {'estu': estu,"titulo":titulo, "Institucion":Institucion})


            #return HttpResponseRedirect('/thanks/')
            #return render(request, "listado.html")#, pk=post.pk)
    else:
        form = Form1()

        if submitted in request.GET:
            submitted = True

    return render(request, 'form3.html', {'form': form, "submitted" : submitted, "titulo" : titulo, "Institucion":Institucion})

################################################################################
@login_required
def vista_exito(request):
    return render(request, "exito.html")

@login_required
def vista_PIE(request):
    return render(request, "Profesionales_PIE.html")
################################################################################
@login_required
def portada(request):

    #Mayuscula para la primera letra y el resto en minuscula
    usuario = request.user
    usuario = str(usuario)
    usuario=usuario.lower()
    Resto = usuario[1:]
    Mayuscula =usuario[0].upper()
    usuario = Mayuscula + Resto

    # usuario = usuario.upper(0)



    return render(request, "portada.html", {'usuario': usuario})
################################################################################
@login_required
def Vista_EVALUA_11(request):
    titulo= "Evalua 11"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_11(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_11()
        if submitted in request.GET:
            submitted = True

    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})
################################################################################
@login_required
def Vista_EVALUA_10(request):
    titulo= "Evalua 10"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_10(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_10()
        if submitted in request.GET:
            submitted = True

    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})
################################################################################
@login_required
def Vista_EVALUA_09(request):#ingresa un nuevo test evalua 9
    user= request.user
    titulo= "EVAL??A-9 VERSI??N CHILENA 3.0"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_09(request.POST)

        if form.is_valid():
            mau = form.save(commit=True)
            #post.user= request.user
            mau.user= user.username
            #form.save()
            mau.save()
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_09()
        if submitted in request.GET:
           submitted = True

    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})

########################################################################

class NUEVO_EVA9(LoginRequiredMixin,CreateView):
    titulo= "EVAL??A-9 VERSI??N CHILENA 3.0"
    model = Modelo_EVALUA_09
    template_name = 'form.html'
    form_class =FormEVA9 # fundamental //Form_EVALUA_09 FormEVA9
    success_url = 'Listado_E09'
    #{"titulo" : titulo}

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):

        form.instance.user= self.request.user.username #salva el usuario
        form.instance.Institucion=Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion#FUNCIONA
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())



###############################################################################




################################################################################
"""@login_required
def Listado_Estudiantes(request):
    titulo= "LISTADO DE ESTUDIANTES"
    user = request.user
    estu = Modelo_Info_Per.objects.filter(user=user).order_by("-Rut")
    context_object_name = 'estudiante'




    if request.POST.get('edad'):
        Rut = (request.POST.get('Rut'))
        personas = Modelo_Info_Per.objects.filter(user=user).filter(Rut=Rut)

    return render(request, 'listado.html', {'estu': estu, "Rut" :Rut,"titulo" : titulo})"""


################################################################################
################################################################################
################################################################################
@login_required
def Detalle_Estudiantes(request, Rut):#funciona

    EST=Modelo_Info_Per.objects.get(Rut=Rut)
    titulo = "EDITAR LOS DATOS DEL ESTUDIANTE"
    RUT = Modelo_Info_Per.objects.get(Rut=Rut).Rut
    Institucion=Modelo_Info_Pro.objects.get(user=request.user).Institucion

    form = Form_Editar_Estudiante(instance=EST)

    if request.method == "POST":
        form = Form_Editar_Estudiante(request.POST, instance=EST)



        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")

    return render(request,'Detalle_EST.html',{'form':form,"Institucion":Institucion,"titulo":titulo ,"Rut":Rut})
################################################################################
@login_required
def Detalle_PRO(request): # ligar al usuario
    titulo= "INGRESE SUS DATOS"
    user = request.user
    Institucion=Modelo_Info_Pro.objects.get(user=user).Institucion
    #PRO=Modelo_Info_Pro.objects.get(pk=1)# esta ligado al primer registro, flexibilizar
    PRO=Modelo_Info_Pro.objects.get(user=user)#funciona
    #estu = Modelo_Info_Per.objects.filter(user=user).order_by("-Rut")
    form = Form_Pro(instance=PRO)
    if request.method == "POST":
        form = Form_Pro(request.POST, instance=PRO)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")

    return render(request,'Detalle_PRO.html',{'form':form,"titulo":titulo,"Institucion":Institucion})


################################################################################
@login_required
def borrar(request, Rut):#en proceso

    EST=Modelo_Info_Per.objects.get(Rut=Rut)
    form = Form1(instance=EST)

    # Recuperamos la instancia de la persona y la borramos
    EST.delete()

    # Despu??s redireccionamos de nuevo a la lista
    return render(request, "exito.html")
#
# def borrar_E09(request, pk):#Listo
#
#     test=Modelo_EVALUA_09.objects.get(pk=pk)
#     form = Form_EVALUA_09(instance=test)
#
#     # Recuperamos la instancia de la persona y la borramos
#     test.delete()

    # Despu??s redireccionamos de nuevo a la lista
    return render(request, "exito.html")




################################################################################

import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

"""@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Estudiantes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estudiantes')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Rut', 'Nombres', 'Apellido paterno', 'Apellido materno', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
# Modelo_Info_Per.objects
# Rut
# Nombres
# Apellido_P
# Apellido_M
# Fecha_nac
# Domicilio
# Observaciones

    rows = Modelo_Info_Per.objects.filter(user=user).values_list('Rut', 'Nombres', 'Apellido_P', 'Apellido_M')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response"""



################################################################################
# class Modelo_EVALUA_09(models.Model):
#     Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
#     Semestre = models.IntegerField( default = semestre)
#     A??o = models.IntegerField(default=
@login_required
def Listado_Estudiantes(request):
    titulo= "LISTADO DE ESTUDIANTES"
    user = request.user
    Institucion=Modelo_Info_Pro.objects.get(user=user).Institucion
    estu = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")

    context_object_name = 'estudiante'

    return render(request, 'listado.html', {'estu': estu,"titulo":titulo, "Institucion":Institucion})
################################################################################

#experimienttado el filtrado por usuarios
@login_required
def Listado_E09(request):
    user = request.user

    titulo = "LISTADO DE PRUEBAS EVAL??A-9 VERSI??N CHILENA 3.0"
    # ORIGINAL
    #gato = Modelo_EVALUA_09.objects.all().order_by("-A??o")
    #modificado
    gato = Modelo_EVALUA_09.objects.filter(user=user).order_by("-A??o")

    context_object_name = 'E09'



    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })
################################################################################

@login_required
def borrar_E09(request, pk):#Listo

    test=Modelo_EVALUA_09.objects.get(pk=pk)
    #form = Form_EVALUA_09(instance=test)

    # Recuperamos la instancia de la persona y la borramos
    test.delete()

    # Despu??s redireccionamos de nuevo a la lista
    #return render(request, "exito.html")
    return HttpResponseRedirect("/Listado_E09")

@login_required
def Detalle_Estudiantes_E09(request, pk):  #Antiguoeditar funciona pero no filtra
    user = request.user
    titulo = "DETALLE/EDITAR PRUEBA EVAL??A-9 VERSI??N CHILENA 3.0"
    test = Modelo_EVALUA_09.objects.get(pk=pk)
    form = Form_EVALUA_09(instance=test)
    exclude = ('user',)


    if request.method == "POST":
        form = Form_EVALUA_09(request.POST, instance=test)
        exclude = ('user',)

        if form.is_valid():
            exclude = ('user',)
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")
    return render(request,'Detalle_EST.html',{'form':form, "titulo":titulo} )
    #return render(request,'Detalle_EST.html',{"titulo":titulo} )

####################################################################################

class EDITAR_EVA9(LoginRequiredMixin,UpdateView):
    titulo= "EVAL??A-9 VERSI??N CHILENA 3.0"
    model = Modelo_EVALUA_09
    template_name = 'form.html'
    form_class =FormEVA9 # fundamental //Form_EVALUA_09 FormEVA9
    #success_url = 'Listado_E09'

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):


        self.object = form.save()

        return redirect("Listado_E09")
        #return super().form_valid(form)


################################################################################
################################################################################


#############################################################################

@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    user = request.user

    ##filename = str(A??o) + str(Semestre) +str(Rut) + ".xls"

    response['Content-Disposition'] = 'attachment; filename="Estudiantes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estudiantes',cell_overwrite_ok=True)


    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Rut', 'Nombres', 'Apellido paterno', 'Apellido materno', 'Fecha de nacimiento',

                "Tel??fono del estudiante",
                "Correo del estudiante",

                 "Identidad de g??nero del estudiante",
                 "Diagn??stico del estudiante",
                "Antecendentes de salud del estudiante",
                "Situaci??n socioecon??mica del estudiante",

                "Observaciones generales",

                "Regi??n del primer domicilio del estudiantes",
                "Comuna del primer domicilio del estudiantes",
                "Direcci??n del primer domicilio del estudiantes",

                "Regi??n del segundo domicilio del estudiantes",
                "Comuna del segundo domicilio del estudiantes",
                "Direcci??n del segundo domicilio del estudiantes",


                 "Nombre apoderado N??1",
                 "Tel??fono apoderado N??1",
                 "Correo apoderado N??1 ",

                "Nombre apoderado N??2",
                 "Tel??fono apoderado N??2",
                 "Correo apoderado N??2 ",

                "Nombre apoderado N??3",
                "Tel??fono apoderado N??3",
                "Correo apoderado N??3 ",
 ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
# Modelo_Info_Per.objects
# Rut
# Nombres
# Apellido_P
# Apellido_M
# Fecha_nac
# Domicilio
# Observaciones
    user = request.user
    Institucion=Modelo_Info_Pro.objects.get(user=user).Institucion

    #Fecha_nac

    #format2 = "Fecha_nac".add_format({'num_format': 'dd/mm/yy'})

    rows = Modelo_Info_Per.objects.filter(Institucion=Institucion).values_list('Rut', 'Nombres',
    'Apellido_P', 'Apellido_M', "Fecha_nac" ,"telefono_estudiante","correo_estudiante","Id_genero",
    "diagnostico","salud","socieco","Observaciones","Region_Domicilio1","Comuna_Domicilio1",
    "Direccion_Domicilio1","Region_Domicilio2",
    "Comuna_Domicilio2",
    "Direccion_Domicilio2",


    "Nombre_apoderado1",
    "telefono_apoderado1",
    "correo_apoderado1",

    "Nombre_apoderado2",
    "telefono_apoderado2",
    "correo_apoderado2",

    "Nombre_apoderado3",
    "telefono_apoderado3",
    "correo_apoderado3",)


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            #ws.write(fila , columna, contenido, font_style)


    rows = Modelo_Info_Per.objects.filter(Institucion=Institucion).values_list("Fecha_nac")
    #dateformat = wb.add_format({'num_format': 'dd/mm/yyyy'})




    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'

    row_num =0
    #col_num =4
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, 4, row[col_num], date_format)


    wb.save(response)
    return response
###################################################

####################################################################################

class EDITAR_EVA10(LoginRequiredMixin,UpdateView):
    titulo= "EVAL??A-10 VERSI??N CHILENA 3.0"
    model = Modelo_EVALUA_10
    template_name = 'form.html'
    form_class =FormEVA10 # fundamental
    #success_url = 'Listado_E10'

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):


        self.object = form.save()

        return redirect("Listado_E10")
        #return super().form_valid(form)


class NUEVO_EVA10(LoginRequiredMixin,CreateView):
    titulo= "EVAL??A-10 VERSI??N CHILENA 3.0"
    model = Modelo_EVALUA_10
    template_name = 'form.html'
    form_class =FormEVA10 # fundamental //Form_EVALUA_09 FormEVA9
    success_url = 'Listado_E10'
    #{"titulo" : titulo}

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):

        form.instance.user= self.request.user.username #salva el usuario
        form.instance.Institucion=Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion#FUNCIONA
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())

@login_required
def Listado_E10(request):
    user = request.user

    titulo = "LISTADO DE PRUEBAS EVAL??A-9 VERSI??N CHILENA 3.0"
    # ORIGINAL
    #gato = Modelo_EVALUA_09.objects.all().order_by("-A??o")
    #modificado
    gato = Modelo_EVALUA_10.objects.filter(user=user).order_by("-A??o")

    context_object_name = 'E10'

    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

@login_required
def borrar_E10(request, pk):#Listo

    test=Modelo_EVALUA_10.objects.get(pk=pk)
    #form = Form_EVALUA_09(instance=test)

    # Recuperamos la instancia de la persona y la borramos
    test.delete()

    # Despu??s redireccionamos de nuevo a la lista
    #return render(request, "exito.html")
    return HttpResponseRedirect("/Listado_E10")

##########################################################################################

class EDITAR_EVA8(LoginRequiredMixin,UpdateView):
    titulo= "EVAL??A-8 VERSI??N CHILENA 3.0"
    model = Modelo_EVALUA_08
    template_name = 'form.html'
    form_class =FormEVA8 # fundamental
    #success_url = 'Listado_E08'

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):

        #form.instance.user= self.request.user.username #salva el usuario
        self.object = form.save()

        return redirect("Listado_E08")
        #return super().form_valid(form)


class NUEVO_EVA8(LoginRequiredMixin,CreateView):
    titulo= "EVAL??A-8 VERSI??N CHILENA 3.0"
    model = Modelo_EVALUA_08
    template_name = 'form.html'
    form_class =FormEVA8 # fundamental //Form_EVALUA_09 FormEVA9
    success_url = 'Listado_E08'
    #{"titulo" : titulo}

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):

        form.instance.user= self.request.user.username #salva el usuario
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())

@login_required
def Listado_E08(request):
    user = request.user

    titulo = "LISTADO DE PRUEBAS EVAL??A-9 VERSI??N CHILENA 3.0"
    # ORIGINAL
    #gato = Modelo_EVALUA_09.objects.all().order_by("-A??o")
    #modificado
    gato = Modelo_EVALUA_08.objects.filter(user=user).order_by("-A??o")

    context_object_name = 'E08'

    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

@login_required
def borrar_E08(request, pk):#Listo

    test=Modelo_EVALUA_08.objects.get(pk=pk)
    #form = Form_EVALUA_09(instance=test)

    # Recuperamos la instancia de la persona y la borramos
    test.delete()

    # Despu??s redireccionamos de nuevo a la lista
    #return render(request, "exito.html")
    return HttpResponseRedirect("/Listado_E08")
