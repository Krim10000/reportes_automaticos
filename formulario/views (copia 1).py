from django.shortcuts import render
from .forms import Form1
from .forms import Form_EVALUA_09
from .forms import Form_EVALUA_10
from .forms import Form_EVALUA_11
from .models import Modelo_Info_Per
from .models import *
from datetime import date
from datetime import datetime
hoy = date.today()




from django.contrib.auth.decorators import login_required

#def input_new(request):
#    form = Form1()
#    return render (request, "form.html", {"form": form})
#https://www.hektorprofe.net/tutorial/django-sistema-registro-login-logout
########################################################
from django.shortcuts import render, redirect

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
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/portada')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


########################################################
from django.contrib.auth import logout as do_logout
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
################################################################################
def portada(request):
    return render (request, "portada.html")

################################################################################
@login_required
#@permission_required( raise_exception=True)
def input_new(request):

    submitted= False
    if request.method == "POST":
        titulo= "Nuevo estudiante"
        form = Form1(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form1()
        titulo= "Nuevo estudiante"
        if submitted in request.GET:
            submitted = True

    return render(request, 'form3.html', {'form': form, "submitted" : submitted, "titulo" : titulo})

################################################################################
@login_required
def vista_exito(request):
    return render(request, "exito.html")
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
def Vista_EVALUA_09(request):
    titulo= "Evalua 09"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_09(request.POST)
        if form.is_valid():
            mau = form.save(commit=True)
            #form.save()
            mau.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_09()
        if submitted in request.GET:
           submitted = True

    #return render(request, 'form.html', {'form': form, "titulo" : titulo})
    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})

################################################################################
@login_required
def Listado_Estudiantes(request):

    estu = Modelo_Info_Per.objects.all().order_by("-Rut")
    context_object_name = 'estudiante'



    if request.POST.get('edad'):
        Rut = (request.POST.get('Rut'))
        personas = Modelo_Info_Per.objects.all().filter(Rut=Rut)

    return render(request, 'listado.html', {'estu': estu, "Rut" :Rut })


################################################################################
################################################################################
################################################################################
@login_required
def Detalle_Estudiantes(request, Rut):

    EST=Modelo_Info_Per.objects.get(Rut=Rut)
    form = Form1(instance=EST)
    if request.method == "POST":
        form = Form1(request.POST, instance=EST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")

    return render(request,'Detalle_EST.html',{'form':form,})






################################################################################
@login_required
def borrar(request, Rut):#en proceso

    EST=Modelo_Info_Per.objects.get(Rut=Rut)
    form = Form1(instance=EST)

    # Recuperamos la instancia de la persona y la borramos
    EST.delete()

    # Después redireccionamos de nuevo a la lista
    return render(request, "exito.html")
################################################################################

import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

@login_required
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

    rows = Modelo_Info_Per.objects.all().values_list('Rut', 'Nombres', 'Apellido_P', 'Apellido_M')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



################################################################################
# class Modelo_EVALUA_09(models.Model):
#     Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
#     Semestre = models.IntegerField( default = semestre)
#     Año = models.IntegerField(default=
@login_required
def Listado_Estudiantes(request):

    estu = Modelo_Info_Per.objects.all().order_by("-Rut")
    context_object_name = 'estudiante'

    return render(request, 'listado.html', {'estu': estu})
################################################################################
@login_required
def Listado_E09(request):
    titulo = "Evalua 09"
    gato = Modelo_EVALUA_09.objects.all().order_by("-Año")
    context_object_name = 'E09'



    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })
################################################################################

@login_required
def Detalle_Estudiantes_E09(request, pk):
    titulo = "Evalua 09"
    test = Modelo_EVALUA_09.objects.get(pk=pk)
    form = Form_EVALUA_09(instance=test)


    if request.method == "POST":
        form = Form_EVALUA_09(request.POST, instance=test)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")
    return render(request,'Detalle_EST.html',{'form':form, "titulo":titulo} )

################################################################################
@login_required
def EV09EXP(request, pk):

    test = Modelo_EVALUA_09.objects.get(pk=pk)
    # se procede a generar los campos del modelo Modelo_Info_Per
    #se usa minuscula para diferenciar el valor y Mayuscula para el campo
    rut = test.Rut.Rut
    nombres = test.Rut.Nombres
    apellido_P = test.Rut.Apellido_P
    apellido_M = test.Rut.Apellido_M
    fecha_nac = test.Rut.Fecha_nac
    domicilio = test.Rut.Domicilio
    observaciones = test.Rut.Observaciones

    # se procede a generar los campos del modelo Modelo_Info_Per
    #se usa minuscula para diferenciar el valor y Mayuscula para el campo


    semestre= test.Semestre
    año = test.Año
    evaluador =test.Evaluador
    colegio = test.Colegio
    curso = test.Curso
    escolaridad = test.Escolaridad
    fecha= test.Fecha
    evaluador = test.Evaluador

    #I ATENCION CONCENTRACION

    I_ACIERTO=test.I_ACIERTO
    I_ERROR=test.I_ERROR
    I_OMISION=test.I_OMISION

    #PUNTAJE IIA1-IIA6 desagregado
    IIA1_ACIERTO=test.IIA1_ACIERTO
    IIA1_ERROR=test.IIA1_ERROR
    IIA1_OMISION=test.IIA1_OMISION

    IIA2_ACIERTO=test.IIA2_ACIERTO
    IIA2_ERROR=test.IIA2_ERROR
    IIA2_OMISION=test.IIA2_OMISION

    IIA3_ACIERTO=test.IIA3_ACIERTO
    IIA3_ERROR=test.IIA3_ERROR
    IIA3_OMISION=test.IIA3_OMISION

    IIA4_ACIERTO=test.IIA4_ACIERTO
    IIA4_ERROR=test.IIA4_ERROR
    IIA4_OMISION=test.IIA4_OMISION

    IIA5_ACIERTO=test.IIA5_ACIERTO
    IIA5_ERROR=test.IIA5_ERROR
    IIA5_OMISION=test.IIA5_OMISION

    IIA6_ACIERTO=test.IIA6_ACIERTO
    IIA6_ERROR=test.IIA6_ERROR
    IIA6_OMISION=test.IIA6_OMISION

    #II RAZONAMIENTO B. ESPACIAL
    IIB1_ACIERTO=test.IIB1_ACIERTO
    IIB1_ERROR=test.IIB1_ERROR
    IIB1_OMISION=test.IIB1_OMISION

    IIB2_ACIERTO=test.IIB2_ACIERTO
    IIB2_ERROR=test.IIB2_ERROR
    IIB2_OMISION=test.IIB2_OMISION

    IIB3_ACIERTO=test.IIB3_ACIERTO
    IIB3_ERROR=test.IIB3_ERROR
    IIB3_OMISION=test.IIB3_OMISION
    #
    #II RAZONAMIENTO C. DEDUCTIVO
    IIC1_ACIERTO=test.IIC1_ACIERTO
    IIC1_ERROR=test.IIC1_ERROR
    IIC1_OMISION=test.IIC1_OMISION

    #PUNTAJE IIC2
    IIC2_ACIERTO=test.IIC2_ACIERTO
    IIC2_ERROR=test.IIC2_ERROR
    IIC2_OMISION=test.IIC2_OMISION

    # IV LECTURA A COMPRENSION
    IVA_ACIERTO=test.IVA_ACIERTO
    IVA_ERROR=test.IVA_ERROR
    IVA_OMISION=test.IVA_OMISION
    #
    # IV LECTURA B EFICACIA
    IVB_ACIERTO=test.IVB_ACIERTO
    IVB_ERROR=test.IVB_ERROR
    IVB_OMISION=test.IVB_OMISION
    #
    # IV LECTURA C VELOCIDAD
    IVC_ACIERTO=test.IVC_ACIERTO
    IVC_ERROR=test.IVC_ERROR
    IVC_OMISION=test.IVC_OMISION
    #
    #
    # V ESCRITURA A. ORTOGRAFIA
    # PUNTAJE V.A
    VA_ACIERTO=test.VA_ACIERTO
    VA_ERROR=test.VA_ERROR
    VA_OMISION=test.VA_OMISION
    # #ACIERTO	ERROR	OMISION
    #
    # V ESCRITURA B. EXP ESCRITA
    # PUNTAJE V.B
    # 1	"Composición escrita superior a lo que es propia del nivel escolar."
    # 2	"Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
    # 3	"Composición acorde al nivel escolar."
    # 4	"Composición inferior a lo esperado acorde al nivel escolar."
    # 5	"Composición con abundantes errores, no logra expresarse."
    # 0	"Vacio"
    V=test.V

    "1","Composición escrita superior a lo que es propia del nivel escolar."
    VB_2= "2","Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
    VB_3= "3","Composición acorde al nivel escolar."
    VB_4= "4","Composición inferior a lo esperado acorde al nivel escolar."
    VB_5= "5","Composición con abundantes errores, no logra expresarse."

    if V == "1":
        VV ="Composición escrita superior a lo que es propia del nivel escolar."
    elif V == "2":
        VV ="Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
    elif V == "3":
        VV = "Composición acorde al nivel escolar."
    elif V == "4":
        VV = "Composición inferior a lo esperado acorde al nivel escolar."
    else:
         VV = "Composición con abundantes errores, no logra expresarse."



    #
    # PUNTAJE VI.A
    #VI APREND MATEMATICOS A CAL&NUM
    #ACIERTO	ERROR	OMISION
    VIA_ACIERTO=test.VIA_ACIERTO
    VIA_ERROR=test.VIA_ERROR
    VIA_OMISION=test.VIA_OMISION
    #PUNTAJE VI.B
    #VI APREND MATEMATICOS B RESOLUC

    VIB_ACIERTO=test.VIB_ACIERTO
    VIB_ERROR=test.VIB_ERROR
    VIB_OMISION=test.VIB_OMISION

    response = HttpResponse(content_type='application/ms-excel')


    filename = "EV09_" +str(año)+"_" + str(semestre)+"_" +str(rut) + ".xls"

    #response['Content-Disposition'] = 'attachment; filename="INFORME.xls"'
    response['Content-Disposition'] = 'attachment; filename= "{}"'.format(filename)#funciona



    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('INFORME',cell_overwrite_ok=True)
    for i in range (0, 17):
        ancho = ws.col(i).width = 1481


    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    font_style0 = xlwt.XFStyle()
    font_style1 = xlwt.easyxf('align: rotation 90')

    styles = dict(bold = 'font: bold 1',)
    #style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')
    #ws.write(fila , columna, contenido, font_style)

    # A0 = 0,0
    # B2 = 1,1

    # pagina uno.
    # FORMATO
    # Celdas combiandas
    ws.write_merge(1, 1, 0, 15, 'Long Cell')
    ws.write_merge(3, 3, 0, 5, 'Long Cell')
    ws.write_merge(5, 5, 5, 15, 'Long Cell')
    ws.write_merge(6, 6, 5, 15, 'Long Cell')
    ws.write_merge(7, 7, 5, 15, 'Long Cell')
    ws.write_merge(8, 8, 5, 15, 'Long Cell')
    ws.write_merge(9, 9, 5, 15, 'Long Cell')
    ws.write_merge(10, 10, 5, 15, 'Long Cell')
    ws.write_merge(11, 11, 5, 15, 'Long Cell')
    ws.write_merge(12, 12, 5, 15, 'Long Cell')
    ws.write_merge(14, 14, 0, 5, 'Long Cell')
    ws.write_merge(16, 20, 0, 15, 'Long Cell')
    ws.write_merge(21, 21, 0, 5, 'Long Cell')
    ws.write_merge(22, 22, 0, 5, 'Long Cell')
    ws.write_merge(23, 23, 0, 10, 'Long Cell')
    ws.write_merge(26, 26, 0, 5, 'Long Cell')
    ws.write_merge(28, 47, 0, 15, 'Long Cell')


    style_string = "font: bold on;"
    styleN = xlwt.easyxf(style_string)


    # pagina uno.
    #texto fijo

    ws.write(1 , 0, "INFORME PSICOPEDAGÓGICO", styleN)
    ws.write(3 , 0,"I.-DATOS DE IDENTIFICACIÓN", styleN)
    ws.write(5 , 0,"Nombre:", font_style0)
    ws.write(6 , 0,"Fecha de nacimiento:", font_style0)
    ws.write(7 , 0,"Edad:", font_style0)
    ws.write(8 , 0,"Establecimiento Educacional:", font_style0)
    ws.write(9 , 0,"Curso", font_style0)
    ws.write(10 , 0,"Escolaridad", font_style0)
    ws.write(11, 0,"Fecha de informe", font_style0)
    ws.write(12, 0,"Evaluador", font_style0)
    ws.write(14, 0,"II.- MOTIVO DE CONSULTA", styleN)
    ws.write(21, 0,"III.- PROCEDIMIENTOS EVALUATIVOS", styleN)
    ws.write(22, 0,"Batería Psicopedagógica Evalúa 9", font_style0)
    ws.write(23, 0,"Autor: Jesús García Vidal, Daniel González Manjón, Beatriz García Ortiz", font_style0)
    ws.write(26, 0,"IV.- ANTECEDENTES RELEVANTES", styleN)



    # pagina uno.
    # texto variable
    #############################################################
    Nombre_completo = nombres + " " + apellido_P + " "+ apellido_M
    ws.write(5, 5,Nombre_completo, font_style0)
    #############################################################
    fecha_naci = fecha_nac.strftime("%d/%m/%Y")
    ws.write(6, 5,fecha_naci, font_style0)
    #############################################################
    AÑOnacimiento = fecha_nac.strftime("%Y")
    AÑOhoy = hoy.strftime("%Y")
    EDAD = int(AÑOhoy)-int(AÑOnacimiento)
    MEShoy = hoy.strftime("%m")
    MESnacimiento= fecha_nac.strftime("%m")
    DIAhoy = hoy.strftime("%d")
    DIAnacimiento= fecha_nac.strftime("%d")
    if (MEShoy < MESnacimiento) and (DIAhoy < DIAnacimiento) :
        EDAD = EDAD -1
    #edad = edad + " años"
    EDAD = str(EDAD) + " años"

    ws.write(7, 5,EDAD, font_style0)
    #############################################################
    ws.write(8, 5,colegio, font_style0)
    ws.write(9, 5,curso, font_style0)
    ws.write(10, 5,escolaridad, font_style0)
    #############################################################
    fecha = fecha.strftime("%d/%m/%Y")
    ws.write(11, 5,fecha, font_style0)
    #############################################################
    ws.write(12, 5,evaluador, font_style0)
    #############################################################
    motivo = "El motivo de evaluación es analizar los aprendizajes académicos logrados por "+  nombres + " hasta su momento actual de escolarización (" + curso +") con la finalidad de estudiar  su ingreso al Programa de Integración Escolar de este Establecimiento Educacional."
    ws.write(16, 0,motivo, font_style0)
    #############################################################
    ws.write(28, 0,observaciones, font_style0)

    #############################################################
    #############################################################
    #############################################################


    #Calculos auxilaires

    # PD: puntaje directo
    # media: media
    # des: desviacion estandar
    # PT: Puntaje tipificado

    #I atencion & concentracion
    PDI = I_ACIERTO-(I_ERROR+I_OMISION) #entre 0 y 193

    if PDI <0:
        PDI=0

    mediaI = 150.89
    desI = 36.65

    PTI =(PDI-mediaI)/desI
    #II.A RAZONAMIENTO INDUCTIVO

    PDIIA1 = IIA1_ACIERTO-IIA1_ERROR/4
    PDIIA2 = IIA2_ACIERTO-IIA2_ERROR/4
    PDIIA3 = IIA3_ACIERTO-IIA3_ERROR/3
    PDIIA4 = IIA4_ACIERTO-IIA4_ERROR/3
    PDIIA5 = IIA4_ACIERTO-IIA5_ERROR/2
    PDIIA6 = IIA5_ACIERTO-IIA6_ERROR/3

    if PDIIA1 < 0:
        PDIIA1 = 0

    if PDIIA2 < 0:
        PDIIA2 = 0

    if PDIIA3 < 0:
        PDIIA3 = 0

    if PDIIA4 < 0:
        PDIIA4 = 0

    if PDIIA5 < 0:
        PDIIA5 = 0

    if PDIIA6 < 0:
        PDIIA6 = 0

    PDIIA =  PDIIA1+PDIIA2+PDIIA3+PDIIA4+PDIIA5+PDIIA6

    mediaIIA =20.50
    desIIA = 7.02

    PTIIA =(PDIIA-mediaIIA)/desIIA

    #II.B RAZONAMIENTO ESPACIAL

    PDIIB1= IIB1_ACIERTO -IIB1_ERROR/5 # item 1 al 7

    PDIIB2= IIB2_ACIERTO-IIB2_ERROR/10 # item 8 al 9

    PDIIB3= IIB3_ACIERTO-IIB3_ERROR/3 # item 10 al 20


    if PDIIB1 < 0:
        PDIIB1 = 0

    if PDIIB2 < 0:
        PDIIB2 = 0

    if PDIIB3 < 0:
        PDIIB3 = 0


    PDIIB = PDIIB1 + PDIIB2 + PDIIB3

    mediaIIB = 15.84
    desIIB = 6.51

    PTIIB =(PDIIB-mediaIIB)/desIIB

# IIC RAZONAMIENTO DEDUCTIVO

    PDIIC1 = IIC1_ACIERTO-IIC1_ERROR/3

    PDIIC2 = IIC2_ACIERTO-IIC2_ERROR/2

    if PDIIC1 < 0:
        PDIIC1 = 0

    if PDIIC2 <0:
        PDIIC2 = 0

    PDIIC = PDIIC1 + PDIIC2

    mediaIIC = 14.84
    desIIC = 6.52

    PTIIC =(PDIIC-mediaIIC)/desIIC

    # indice genera cognitivo

    IGC = (PTIIA + PTIIB + PTIIC)/3
    mediaCog =(mediaIIA+mediaIIB+mediaIIC)/3
    desCog =(desIIA+desIIB+desIIC)/3


    # IV LECTURA A COMPRENSION

    PDIVA = IVA_ACIERTO -IVA_ERROR/3

    if PDIVA < 0:
        PDIVA =0

    mediaIVA = 13.17
    desIVA = 7.38

    PTIVA =(PDIVA-mediaIVA)/desIVA

    # IV LECTURA B EFICACIA

    PDIVB=IVB_ACIERTO

    mediaIVB= 5.73
    desIVB= 3.99

    PTIVB =(PDIVB-mediaIVB)/desIVB

    # IV LECTURA C VELOCIDAD

    PDIVC = IVC_ACIERTO -(IVC_ERROR+IVC_OMISION)

    mediaIVC= 8.58

    desIVC= 3.75

    PTIVC =(PDIVC-mediaIVC)/desIVC

    # indice general de lectura IGL

    IGL = (PDIVA + PDIVB + PDIVC)/3
    mediaLEC= (mediaIVA +mediaIVB +mediaIVC)/3
    desLEC= (desIVA+ desIVB +desIVC)/3

    # V ESCRITURA A ORTOGRAFIA

    PDVA = VA_ACIERTO -(VA_ERROR+VA_OMISION)

    if PDVA <0:
        PDVA = 0

    mediaVA= 18.83
    desVA = 1.389

    PTVA = (PDVA-mediaVA)/desVA

    # VB EXPRESION ESCRITA


    # indice general ESCRITURA

    IGE = PTVA
    mediaESC = mediaVA
    desESC = desVA

 # VIA calculos y numeracion

    PDVIA= VIA_ACIERTO

    mediaVIA = 13.84
    desVIA = 6.36

    PTVIA = (PDVIA-mediaVIA)/desVIA

    # VIB RESOLUCION DE PROBLEMAS

    PDVIB =  VIB_ACIERTO

    mediaVIB = 4.03
    desVIB = 3.14

    PTVIB = (PDVIB-mediaVIB)/desVIB

    # indice general matematematicas

    IGM = (PTVIA + PTVIB)/2

    mediaMAT = (mediaVIA + mediaVIB)/2

    desMAT = (desVIA + desVIB)/2



    # pagina dos.

    #FORMATO
    #Celdas combiandas
    #ws.write_merge(y1, y2, x1, x2, 'Long Cell')
    ws.write_merge(54, 54, 12, 15, 'Long Cell') # indice GENERALES
    ws.write_merge(67, 70, 0, 15, 'Long Cell') # I
    ws.write_merge(73, 76, 0, 15, 'Long Cell') # IIA
    ws.write_merge(78, 81, 0, 15, 'Long Cell') # IIB
    ws.write_merge(83, 86, 0, 15, 'Long Cell') # IIC


    #pagina dos.
    #texto fijo
    #ws.write(y, x,"text", font_style0)
    ws.write(49, 0,"V.- ANÁLISIS DE RESULTADOS", font_style0)
    ws.write(50, 0,"A) ANÁLISIS CUANTITATIVO", font_style0)
    ws.write(60, 0,"B) ANÁLISIS CUALITATIVO", font_style0)
    ws.write(62, 0,"ÁREA DE PROCESOS COGNITIVOS", font_style0)
    ws.write(64, 1,"I.-Atención-Concentración", font_style0)
    ws.write(71, 1,"II.-Razonamiento", font_style0)

    ws.write(55, 1,"P.D.", font_style0)
    ws.write(56, 1,"MEDIA", font_style0)
    ws.write(57, 1,"D.T.", font_style0)
    ws.write(58, 1,"P.T.", font_style0)

    # pagina dos.
    # texto variable

    ws.write(54, 2,"Razonamineto inductivo", font_style0)
    ws.write(55, 2,PDIIA, font_style0)
    ws.write(56, 2,mediaIIA, font_style0)
    ws.write(57, 2,desIIA, font_style0)
    ws.write(58, 2,PTIIA, font_style0)

    #########################################

    ws.write(54, 3,"Razonamineto Espacial", font_style0)
    ws.write(55, 3,PDIIB, font_style0)
    ws.write(56, 3,mediaIIB, font_style0)
    ws.write(57, 3,desIIB, font_style0)
    ws.write(58, 3,PTIIB, font_style0)

    #########################################

    ws.write(54, 4,"Razonamineto Deductivo", font_style0)
    ws.write(55, 4,PDIIC, font_style0)
    ws.write(56, 4,mediaIIC, font_style0)
    ws.write(57, 4,desIIC, font_style0)
    ws.write(58, 4,PTIIC, font_style0)

    #########################################

    ws.write(54, 5,"Comprensión Lectora", font_style0)
    ws.write(55, 5,PDIVA, font_style0)
    ws.write(56, 5,mediaIVA, font_style0)
    ws.write(57, 5,desIVA, font_style0)
    ws.write(58, 5,PTIVA, font_style0)

    #########################################

    ws.write(54, 6,"Velocidad Lectora", font_style0)
    ws.write(55, 6,PDIVC, font_style0)
    ws.write(56, 6,mediaIVC, font_style0)
    ws.write(57, 6,desIVC, font_style0)
    ws.write(58, 6,PTIVC, font_style0)

    #########################################

    ws.write(54, 7,"Ortografia visual y reglada", font_style0)
    ws.write(55, 7,PDVA, font_style0)
    ws.write(56, 7,mediaVA, font_style0)
    ws.write(57, 7,desVA, font_style0)
    ws.write(58, 7,PTVA, font_style0)

    #########################################

    ws.write(54, 8,"Calculo y numeración", font_style0)
    ws.write(55, 8,PDVIA, font_style0)
    ws.write(56, 8,mediaVIA, font_style0)
    ws.write(57, 8,desVIA, font_style0)
    ws.write(58, 8,PTVIA, font_style0)

    #########################################

    ws.write(54, 9,"Resolución de Problemas", font_style0)
    ws.write(55, 9,PDVIB, font_style0)
    ws.write(56, 9,mediaVIB, font_style0)
    ws.write(57, 9,desVIB, font_style0)
    ws.write(58, 9,PTVIB, font_style0)

    #########################################

    ws.write(54, 10,"Atención y Concentración", font_style0)
    ws.write(55, 10,PDI, font_style0)
    ws.write(56, 10,mediaI, font_style0)
    ws.write(57, 10,desI, font_style0)
    ws.write(58, 10,PTI, font_style0)


    #indices GENERALES


    ws.write(54, 12,"índices Generales", font_style0)


    ws.write(55, 12,"Cognitivo", font_style0)
    ws.write(56, 12,mediaCog, font_style0)
    ws.write(57, 12,desCog, font_style0)
    ws.write(58, 12,IGC, font_style0)

    ws.write(55, 13,"Lectura", font_style0)
    ws.write(56, 13,mediaLEC, font_style0)
    ws.write(57, 13,desLEC, font_style0)
    ws.write(58, 13,IGL, font_style0)

    ws.write(55, 14,"Escritura", font_style0)
    ws.write(56, 14,mediaESC, font_style0)
    ws.write(57, 14,desESC, font_style0)
    ws.write(58, 14,IGE, font_style0)

    ws.write(55, 15,"Matemáticas", font_style0)
    ws.write(56, 15,mediaMAT, font_style0)
    ws.write(57, 15,desMAT, font_style0)
    ws.write(58, 15,IGM, font_style0)

######################################################################################################################
    #PT a texto

 # I ATENCION
    if PTI > 2:
        NVLI = "sobresaliente"
    elif  1 <= PTI < 2:
        NVLI = "notable"
    elif  -1 <= PTI <= 1:
        NVLI = "promedio"
    elif  -2 <= PTI < -1:
        NVLI = "insufiente"
    elif PTI < -2:
        NVLI = "deficiente"


 # IIA  RAZONAMIENTO INDUCTIVO
    if PTIIA > 2:
        NVLIIA = "sobresaliente"
    elif  1 <= PTIIA < 2:
        NVLIIA = "notable"
    elif  -1 <= PTIIA <= 1:
        NVLIIA = "promedio"
    elif  -2 <= PTIIA < -1:
        NVLIIA = "insufiente"
    elif PTIIA < -2:
        NVLIIA = "deficiente"

 # IIB RAZONAMIENTO ESPACIAL
    if PTIIB > 2:
        NVLIIB = "sobresaliente"
    elif  1 <= PTIIB < 2:
        NVLIIB = "notable"
    elif  -1 <= PTIIB <= 1:
        NVLIIB = "promedio"
    elif  -2 <= PTIIB < -1:
        NVLIIB = "insufiente"
    elif PTIIB < -2:
        NVLIIB = "deficiente"

 # IIC RAZONAMIENTO DEDUCTIVO
    if PTIIC > 2:
        NVLIIC = "sobresaliente"
    elif  1 <= PTIIC < 2:
        NVLIIC = "notable"
    elif  -1 <= PTIIC <= 1:
        NVLIIC = "promedio"
    elif  -2 <= PTIIC < -1:
        NVLIIC = "insufiente"
    elif PTIIC < -2:
        NVLIIC = "deficiente"


 # IVA COMPRENSION Lectora
    if PTIVA > 2:
        NVLIVA = "sobresaliente"
    elif  1 <= PTI < 2:
        NVLIVA = "notable"
    elif  -1 <= PTI <= 1:
        NVLIVA = "promedio"
    elif  -2 <= PTI < -1:
        NVLIVA = "insufiente"
    elif PTI < -2:
        NVLIVA = "deficiente"

 # IVB VELOCIDAD Lectora
    if PTIVB > 2:
        NVLIVB = "sobresaliente"
    elif  1 <= PTIVB < 2:
        NVLIVB = "notable"
    elif  -1 <= PTIVB <= 1:
        NVLIVB = "promedio"
    elif  -2 <= PTIVB < -1:
        NVLIVB = "insufiente"
    elif PTIVB < -2:
        NVLIVB = "deficiente"


 # VA ORTOGRAFIA
    if PTVA > 2:
        NVLVA = "sobresaliente"
    elif  1 <= PTVA < 2:
        NVLVA = "notable"
    elif  -1 <= PTVA <= 1:
        NVLVA = "promedio"
    elif  -2 <= PTVA < -1:
        NVLVA = "insufiente"
    elif PTVA < -2:
        NVLVA = "deficiente"


 # VB EXPRESION ESCRITA
    NVLVB =VV

 # VIA Calculo
    if PTIIC > 2:
        NVLIIC = "sobresaliente"
    elif  1 <= PTIIC < 2:
        NVLIIC = "notable"
    elif  -1 <= PTIIC <= 1:
        NVLIIC = "promedio"
    elif  -2 <= PTIIC < -1:
        NVLIIC = "insufiente"
    elif PTIIC < -2:
        NVLIIC = "deficiente"

 # VIB RESOLUCION
    if PTIIC > 2:
        NVLIIC = "sobresaliente"
    elif  1 <= PTIIC < 2:
        NVLIIC = "notable"
    elif  -1 <= PTIIC <= 1:
        NVLIIC = "promedio"
    elif  -2 <= PTIIC < -1:
        NVLIIC = "insufiente"
    elif PTIIC < -2:
        NVLIIC = "deficiente"

######################################################################################################################


#REPORTE.Range("A68") = DATOS.Cells(x, 2) & " presenta un nivel " & NivelI & " en su capacidad de mantener una atención  concentrada en tareas que exigen observación analítica."

    ws.write(67, 0,Nombre_completo+ " presenta un nivel " + NVLI +" en su capacidad de mantener una atención  concentrada en tareas que exigen observación analítica.", font_style0)





    # pagina tres.

    #FORMATO
    #Celdas combiandas
    #ws.write_merge(y1, y2, x1, x2, 'Long Cell')

    #pagina tres.
    #texto fijo

    # pagina tres.
    # texto variable


    # pagina cuatro.

    #FORMATO
    #Celdas combiandas
    #ws.write_merge(y1, y2, x1, x2, 'Long Cell')

    #pagina cuatro.
    #texto fijo

    # pagina cuatro.
    # texto variable





    wb.save(response)
    return response



################################################################################

@login_required
def borrar_E09(request, pk):#Listo

    test=Modelo_EVALUA_09.objects.get(pk=pk)
    form = Form_EVALUA_09(instance=test)

    # Recuperamos la instancia de la persona y la borramos
    test.delete()

    # Después redireccionamos de nuevo a la lista
    return render(request, "exito.html")
#############################################################################

@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')


    ##filename = str(Año) + str(Semestre) +str(Rut) + ".xls"

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

    rows = Modelo_Info_Per.objects.all().values_list('Rut', 'Nombres', 'Apellido_P', 'Apellido_M')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            #ws.write(fila , columna, contenido, font_style)




    wb.save(response)
    return response
