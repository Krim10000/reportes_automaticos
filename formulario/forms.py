from django import forms

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


############################################################################
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, ButtonHolder, HTML, Column, Field
from crispy_forms.bootstrap import StrictButton
#from .views import vista_exito


######################################
#Informacion del profesional
class Form_Pro(forms.ModelForm):

    class Meta:
        model = Modelo_Info_Pro
        exclude = ("user","Institucion")
        labels = {
            'Evaluador':('Nombre completo'),
            "Registro_MINEDUC": ('Número de Registro MINEDUC'),
            "Rut_Pro": ('Rut'),
            "Profesion":("Profesión")
        }



##########################################
class DateInput(forms.DateInput):
    input_type = 'date'

#Informacion de los estudiantes
class Form1(forms.ModelForm):

    class Meta:
        model = Modelo_Info_Per
        fields = ("__all__")

        labels = {
            'Apellido_P':('Apellido paterno'),
            "Apellido_M": ('Apellido materno'),
            "Fecha_nac": ('Fecha de nacimiento'),

            "telefono_estudiante": ("Teléfono del estudiante"),
            "correo_estudiante": ("Correo del estudiante"),

            "Id_genero" : ("Identidad de género del estudiante"),
            "diagnostico": ("Diagnóstico principal del estudiante"),
            "salud": ("Antecendentes de salud del estudiante"),
            "socieco": ("Situación socioeconómica del estudiante"),

            "Observaciones" : ("Observaciones generales"),

            "Region_Domicilio1": ("Región del primer domicilio del estudiantes"),
            "Comuna_Domicilio1": ("Comuna del primer domicilio del estudiantes"),
            "Direccion_Domicilio1" : ("Dirección del primer domicilio del estudiantes"),

            "Region_Domicilio2": ("Región del segundo domicilio del estudiantes"),
            "Comuna_Domicilio2": ("Comuna del segundo domicilio del estudiantes"),
            "Direccion_Domicilio2" : ("Dirección del segundo domicilio del estudiantes"),


            "Nombre_apoderado1": ("Nombre apoderado N°1"),
            "telefono_apoderado1"  : ("Teléfono apoderado N°1"),
            "correo_apoderado1"  : ("Correo apoderado N°1 "),

            "Nombre_apoderado2": ("Nombre apoderado N°2"),
            "telefono_apoderado2"  : ("Teléfono apoderado N°2"),
            "correo_apoderado2"  : ("Correo apoderado N°2 "),

            "Nombre_apoderado3": ("Nombre apoderado N°3"),
            "telefono_apoderado3"  : ("Teléfono apoderado N°3"),
            "correo_apoderado3"  : ("Correo apoderado N°3 "),




        }
        help_texts = {
            "Rut":("12345678-9"),
            'Fecha_nac': ('DD/MM/AAAA'),
        }
        exclude = ("user","Institucion")

        widgets = { #'Colegio': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    #'Escolaridad': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    'Fecha_nac': DateInput()
                    #'Evaluador': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    }

class Form_Editar_Estudiante(forms.ModelForm):

    class Meta:
        model = Modelo_Info_Per
        fields = ("__all__")

        labels = {
            'Apellido_P':('Apellido paterno'),
            "Apellido_M": ('Apellido materno'),
            "Fecha_nac": ('Fecha de nacimiento'),

            "telefono_estudiante": ("Teléfono del estudiante"),
            "correo_estudiante": ("Correo del estudiante"),

            "Id_genero" : ("Identidad de género del estudiante"),
            "diagnostico": ("Diagnóstico principal del estudiante"),
            "salud": ("Antecendentes de salud del estudiante"),
            "socieco": ("Situación socioeconómica del estudiante"),

            "Observaciones" : ("Observaciones generales"),

            "Region_Domicilio1": ("Región del primer domicilio del estudiantes"),
            "Comuna_Domicilio1": ("Comuna del primer domicilio del estudiantes"),
            "Direccion_Domicilio1" : ("Dirección del primer domicilio del estudiantes"),

            "Region_Domicilio2": ("Región del segundo domicilio del estudiantes"),
            "Comuna_Domicilio2": ("Comuna del segundo domicilio del estudiantes"),
            "Direccion_Domicilio2" : ("Dirección del segundo domicilio del estudiantes"),


            "Nombre_apoderado1": ("Nombre apoderado N°1"),
            "telefono_apoderado1"  : ("Teléfono apoderado N°1"),
            "correo_apoderado1"  : ("Correo apoderado N°1 "),

            "Nombre_apoderado2": ("Nombre apoderado N°2"),
            "telefono_apoderado2"  : ("Teléfono apoderado N°2"),
            "correo_apoderado2"  : ("Correo apoderado N°2 "),

            "Nombre_apoderado3": ("Nombre apoderado N°3"),
            "telefono_apoderado3"  : ("Teléfono apoderado N°3"),
            "correo_apoderado3"  : ("Correo apoderado N°3 "),


        }
        help_texts = {
            "Rut":("12345678-9"),
            'Fecha_nac': ('DD/MM/AAAA'),
        }
        exclude = ("user","Institucion","Rut")

        widgets = { #'Colegio': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    #'Escolaridad': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    #'Fecha_nac': DateInput()
                    #'Evaluador': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    }

######################################




class FormEVA8(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA8,self).__init__(*args, **kwargs)

        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
                 ######## codigo para columnas y columna 1

                 HTML(""" <center> """),#center I1
                 Fieldset("",  #Seccion
                 HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                 HTML("""  <p></p> """), #espacio

                 Field("Rut","Semestre","Año","Colegio", "Curso","Escolaridad","Fecha","Evaluador" )),

                 HTML("""  <p></p> """), #espacio
                 HTML(""" </center> """),#center F2
                 #/////////////////////////////////////

                 HTML("""
                         <html>
                         <head>
                         <meta name="viewport" content="width=device-width, initial-scale=1">
                         <style>
                         * {
                           box-sizing: border-box;
                         }

                         /* Create two equal columns that floats next to each other */
                         .column {
                           float: left;
                           width: 50%;}

                         /* Clear floats after the columns */
                         .row:after {
                           content: "";
                           display: table;
                           clear: both;}
                         </style>
                         </head>
                         <body>

                             <div class="row">
                           <div class="column" >
                                         """),

                 HTML(""" <center> """),#center
                 Fieldset("",#Seccion
                 HTML(""" <center> I ATENCIÓN CONCENTRACIÓN </center> """),#Titulo
                 HTML("""  <p></p> """),
                     Field("I_ACIERTO","I_ERROR","I_OMISION")),#Listo
                 HTML("""  <p></p> """), #espacio


                 Fieldset("",  #Seccion
                 HTML(""" <center> II RAZONAMIENTO </center> """),#Titulo
                 HTML("""  <p></p> """), #espacio
                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 1",#subtitulo
                     Field("IIA1_ACIERTO","IIA1_ERROR","IIA1_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 2",#subtitulo
                     Field("IIA2_ACIERTO","IIA2_ERROR","IIA2_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 3",#subtitulo
                     Field("IIA3_ACIERTO","IIA3_ERROR","IIA3_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 4",#subtitulo
                    Field("IIA4_ACIERTO","IIA4_ERROR","IIA4_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 5",#subtitulo
                    Field("IIA5_ACIERTO","IIA5_ERROR","IIA5_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 6",#subtitulo
                    Field("IIA6_ACIERTO","IIA6_ERROR","IIA6_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 1",
                     Field("IIB1_ACIERTO","IIB1_ERROR","IIB1_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 2",
                     Field("IIB2_ACIERTO","IIB2_ERROR","IIB2_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 1",
                     Field("IIC1_ACIERTO","IIC1_ERROR","IIC1_OMISION")),#Listo


                 HTML("""  <p></p> """), #espacio
                 HTML("""  </div> """), #fin columna uno
                 HTML(""" </center> """),#center

             #////////////////////////////
                 HTML(""" <center> """),#center
                 HTML("""   <div class="column"  """), #inicio columna dos

                 Fieldset("",#Seccion
                 Fieldset("",#Seccion
                 HTML(""" <center> IV LECTURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("IV LECTURA A COMPRENSION PARTE 1",
                     Field("IVA1_ACIERTO","IVA1_ERROR","IVA1_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 2",
                     Field("IVA2_ACIERTO","IVA2_ERROR","IVA2_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 3",
                     Field("IVA3_ACIERTO","IVA3_ERROR","IVA3_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 4",
                     Field("IVA4_ACIERTO","IVA4_ERROR","IVA4_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 5",
                     Field("IVA5_ACIERTO","IVA5_ERROR","IVA5_OMISION")),




                 Fieldset("IV LECTURA B VELOCIDAD",
                     Field("IVB_ACIERTO","IVB_ERROR","IVB_OMISION")),
                 Fieldset("IV LECTURA C VELOCIDAD",
                     Field("IVC_ACIERTO","IVC_ERROR","IVC_OMISION"))),
                 HTML("""  <p></p> """), #espacio


                 Fieldset("",#Seccion
                 HTML(""" <center> V ESCRITURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("V ESCRITURA A. ORTOGRAFIA",
                     Field("VA_ACIERTO","VA_ERROR","VA_OMISION")),
                 HTML("""  <p></p> """),
                 Fieldset("V ESCRITURA B. EXP ESCRITA",
                     Field("V")),
                 HTML("""  <p></p> """)), #espacio


                 Fieldset("",#Seccion
                 HTML(""" <center> VI APRENDIZAJE MATEMATICOS </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("VI APREND MATEMATICOS A CAL&NUM",
                     Field("VIA_ACIERTO","VIA_ERROR","VIA_OMISION")),
                 Fieldset("VI APREND MATEMATICOS B RESOLUC",
                     Field("VIB_ACIERTO","VIB_ERROR","VIB_OMISION"))),
                 HTML("""  <p></p> """)), #espacio


                 HTML(""" </center> """),#center



             #fin codigo columnas
             HTML("""  </div>
                         </div>

                         </body>
                         </html>
                           """),
 HTML(""" <center> """),#center
 ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
 HTML(""" </center> """),))#center



    class Meta():
        model = Modelo_EVALUA_08
        exclude = ("user",)
        labels = {
            'Rut':('Estudiante'),
            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),
            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),
            "IIA1_OMISION":("Omisiones"),

            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),
            "IIA2_OMISION":("Omisiones"),

            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),
            "IIA3_OMISION":("Omisiones"),


            "IIA4_ACIERTO":("Aciertos"),
            "IIA4_ERROR":("Errores"),
            "IIA4_OMISION":("Omisiones"),

            "IIA5_ACIERTO":("Aciertos"),
            "IIA5_ERROR":("Errores"),
            "IIA5_OMISION":("Omisiones"),

            "IIA6_ACIERTO":("Aciertos"),
            "IIA6_ERROR":("Errores"),
            "IIA6_OMISION":("Omisiones"),


            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),
            "IIB1_OMISION":("Omisiones"),
            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),
            "IIB2_OMISION":("Omisiones"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),
            "IIC1_OMISION":("Omisiones"),


            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),
            "IVA1_OMISION":("Omisiones"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),
            "IVA2_OMISION":("Omisiones"),

            "IVA3_ACIERTO":("Aciertos"),
            "IVA3_ERROR":("Errores"),
            "IVA3_OMISION":("Omisiones"),

            "IVA4_ACIERTO":("Aciertos"),
            "IVA4_ERROR":("Errores"),
            "IVA4_OMISION":("Omisiones"),

            "IVA5_ACIERTO":("Aciertos"),
            "IVA5_ERROR":("Errores"),
            "IVA5_OMISION":("Omisiones"),



            "IVB_ACIERTO":("Aciertos"),
            "IVB_ERROR":("Errores"),
            "IVB_OMISION":("Omisiones"),



            "VA_ACIERTO":("Aciertos"),
            "VA_ERROR":("Errores"),
            "VA_OMISION":("Omisiones"),
            "V":("Expresión Escrita"),
            "VIA_ACIERTO":("Aciertos"),
            "VIA_ERROR":("Errores"),
            "VIA_OMISION":("Omisiones"),
            "VIB_ACIERTO":("Aciertos"),
            "VIB_ERROR":("Errores"),
            "VIB_OMISION":("Omisiones"),


            }
        widgets = { #'Colegio': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    'Escolaridad': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    #'Evaluador': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    }
######################################

class FormEVA9(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA9,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset = Car.objects.filter(username=user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
                 ######## codigo para columnas y columna 1

                 HTML(""" <center> """),#center I1
                 Fieldset("",  #Seccion
                 HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                 HTML("""  <p></p> """), #espacio

                 Field("Rut","Semestre","Año","Colegio", "Curso","Escolaridad","Fecha","Evaluador" )),

                 HTML("""  <p></p> """), #espacio
                 HTML(""" </center> """),#center F2
                 #/////////////////////////////////////

                 HTML("""
                         <html>
                         <head>
                         <meta name="viewport" content="width=device-width, initial-scale=1">
                         <style>
                         * {
                           box-sizing: border-box;
                         }

                         /* Create two equal columns that floats next to each other */
                         .column {
                           float: left;
                           width: 50%;}

                         /* Clear floats after the columns */
                         .row:after {
                           content: "";
                           display: table;
                           clear: both;}
                         </style>
                         </head>
                         <body>

                             <div class="row">
                           <div class="column" >
                                         """),

                 HTML(""" <center> """),#center
                 Fieldset("",#Seccion
                 HTML(""" <center> I ATENCIÓN CONCENTRACIÓN </center> """),#Titulo
                 HTML("""  <p></p> """),
                     Field("I_ACIERTO","I_ERROR","I_OMISION")),#Listo
                 HTML("""  <p></p> """), #espacio


                 Fieldset("",  #Seccion
                 HTML(""" <center> II RAZONAMIENTO </center> """),#Titulo
                 HTML("""  <p></p> """), #espacio
                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 1",#subtitulo
                     Field("IIA1_ACIERTO","IIA1_ERROR","IIA1_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 2",#subtitulo
                     Field("IIA2_ACIERTO","IIA2_ERROR","IIA2_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 3",#subtitulo
                     Field("IIA3_ACIERTO","IIA3_ERROR","IIA3_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 4",#subtitulo
                     Field("IIA4_ACIERTO","IIA4_ERROR","IIA4_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 5",#subtitulo
                     Field("IIA5_ACIERTO","IIA5_ERROR","IIA5_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 6",#subtitulo
                     Field("IIA6_ACIERTO","IIA6_ERROR","IIA6_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 1: Items 1 al 7",
                     Field("IIB1_ACIERTO","IIB1_ERROR","IIB1_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 2: Items 8 al 9",
                     Field("IIB2_ACIERTO","IIB2_ERROR","IIB2_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 3: Items 10 al 20",
                     Field("IIB3_ACIERTO","IIB3_ERROR","IIB3_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 1",
                     Field("IIC1_ACIERTO","IIC1_ERROR","IIC1_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 2",
                     Field("IIC2_ACIERTO","IIC2_ERROR","IIC2_OMISION")),),#Listo


                 HTML("""  <p></p> """), #espacio
                 HTML("""  </div> """), #fin columna uno
                 HTML(""" </center> """),#center

             #////////////////////////////
                 HTML(""" <center> """),#center
                 HTML("""   <div class="column"  """), #inicio columna dos

                 Fieldset("",#Seccion
                 Fieldset("",#Seccion
                 HTML(""" <center> IV LECTURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("IV LECTURA A COMPRENSION",
                     Field("IVA_ACIERTO","IVA_ERROR","IVA_OMISION")),
                 Fieldset("IV LECTURA B EFICACIA",
                     Field("IVB_ACIERTO","IVB_ERROR","IVB_OMISION")),
                 Fieldset("IV LECTURA C VELOCIDAD",
                     Field("IVC_ACIERTO","IVC_ERROR","IVC_OMISION"))),
                 HTML("""  <p></p> """), #espacio


                 Fieldset("",#Seccion
                 HTML(""" <center> V ESCRITURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("V ESCRITURA A. ORTOGRAFIA",
                     Field("VA_ACIERTO","VA_ERROR","VA_OMISION")),
                 HTML("""  <p></p> """),
                 Fieldset("V ESCRITURA B. EXP ESCRITA",
                     Field("V")),
                 HTML("""  <p></p> """)), #espacio


                 Fieldset("",#Seccion
                 HTML(""" <center> VI APRENDIZAJE MATEMATICOS </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("VI APREND MATEMATICOS A CAL&NUM",
                     Field("VIA_ACIERTO","VIA_ERROR","VIA_OMISION")),
                 Fieldset("VI APREND MATEMATICOS B RESOLUC",
                     Field("VIB_ACIERTO","VIB_ERROR","VIB_OMISION"))),
                 HTML("""  <p></p> """)), #espacio


                 HTML(""" </center> """),#center



             #fin codigo columnas
             HTML("""  </div>
                         </div>

                         </body>
                         </html>
                           """),
 HTML(""" <center> """),#center
 ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
 HTML(""" </center> """),#center

  )

    class Meta():
        model = Modelo_EVALUA_09
        exclude = ("user",)
        labels = {
            'Rut':('Estudiante'),
            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),
            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),
            "IIA1_OMISION":("Omisiones"),
            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),
            "IIA2_OMISION":("Omisiones"),
            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),
            "IIA3_OMISION":("Omisiones"),
            "IIA4_ACIERTO":("Aciertos"),
            "IIA4_ERROR":("Errores"),
            "IIA4_OMISION":("Omisiones"),
            "IIA5_ACIERTO":("Aciertos"),
            "IIA5_ERROR":("Errores"),
            "IIA5_OMISION":("Omisiones"),
            "IIA6_ACIERTO":("Aciertos"),
            "IIA6_ERROR":("Errores"),
            "IIA6_OMISION":("Omisiones"),
            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),
            "IIB1_OMISION":("Omisiones"),
            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),
            "IIB2_OMISION":("Omisiones"),
            "IIB3_ACIERTO":("Aciertos"),
            "IIB3_ERROR":("Errores"),
            "IIB3_OMISION":("Omisiones"),
            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),
            "IIC1_OMISION":("Omisiones"),
            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),
            "IIC2_OMISION":("Omisiones"),
            "IVA_ACIERTO":("Aciertos"),
            "IVA_ERROR":("Errores"),
            "IVA_OMISION":("Omisiones"),
            "IVB_ACIERTO":("Aciertos"),
            "IVB_ERROR":("Errores"),
            "IVB_OMISION":("Omisiones"),
            "IVC_ACIERTO":("Aciertos"),
            "IVC_ERROR":("Errores"),
            "IVC_OMISION":("Omisiones"),
            "VA_ACIERTO":("Aciertos"),
            "VA_ERROR":("Errores"),
            "VA_OMISION":("Omisiones"),
            "V":("Expresión Escrita"),
            "VIA_ACIERTO":("Aciertos"),
            "VIA_ERROR":("Errores"),
            "VIA_OMISION":("Omisiones"),
            "VIB_ACIERTO":("Aciertos"),
            "VIB_ERROR":("Errores"),
            "VIB_OMISION":("Omisiones"),


            }
        widgets = { #'Colegio': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    'Escolaridad': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    #'Evaluador': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    }
##########################################################################################

#Modelo_EVALUA_10
class FormEVA10(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA10,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset = Car.objects.filter(username=user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
                 ######## codigo para columnas y columna 1

                 HTML(""" <center> """),#center I1
                 Fieldset("",  #Seccion
                 HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                 HTML("""  <p></p> """), #espacio

                 Field("Rut","Semestre","Año","Colegio", "Curso","Escolaridad","Fecha","Evaluador" )),

                 HTML("""  <p></p> """), #espacio
                 HTML(""" </center> """),#center F2
                 #/////////////////////////////////////

                 HTML("""
                         <html>
                         <head>
                         <meta name="viewport" content="width=device-width, initial-scale=1">
                         <style>
                         * {
                           box-sizing: border-box;
                         }

                         /* Create two equal columns that floats next to each other */
                         .column {
                           float: left;
                           width: 50%;}

                         /* Clear floats after the columns */
                         .row:after {
                           content: "";
                           display: table;
                           clear: both;}
                         </style>
                         </head>
                         <body>

                             <div class="row">
                           <div class="column" >
                                         """),

                 HTML(""" <center> """),#center
                 Fieldset("",#Seccion
                 HTML(""" <center> I ATENCIÓN CONCENTRACIÓN </center> """),#Titulo
                 HTML("""  <p></p> """),
                     Field("I_ACIERTO","I_ERROR","I_OMISION")),#Listo
                 HTML("""  <p></p> """), #espacio


                 Fieldset("",  #Seccion
                 HTML(""" <center> II RAZONAMIENTO </center> """),#Titulo
                 HTML("""  <p></p> """), #espacio
                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 1",#subtitulo
                     Field("IIA1_ACIERTO","IIA1_ERROR","IIA1_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 2",#subtitulo
                     Field("IIA2_ACIERTO","IIA2_ERROR","IIA2_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 3",#subtitulo
                     Field("IIA3_ACIERTO","IIA3_ERROR","IIA3_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 1: Items 1 al 7",
                     Field("IIB1_ACIERTO","IIB1_ERROR","IIB1_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 2: Items 8 al 9",
                     Field("IIB2_ACIERTO","IIB2_ERROR","IIB2_OMISION")),#Listo

                 Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 1",
                     Field("IIC1_ACIERTO","IIC1_ERROR","IIC1_OMISION")),#Listo
                 Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 2",
                     Field("IIC2_ACIERTO","IIC2_ERROR","IIC2_OMISION")),),#Listo


                 HTML("""  <p></p> """), #espacio
                 HTML("""  </div> """), #fin columna uno
                 HTML(""" </center> """),#center

             #////////////////////////////
                 HTML(""" <center> """),#center
                 HTML("""   <div class="column"  """), #inicio columna dos

                 Fieldset("",#Seccion
                 Fieldset("",#Seccion
                 HTML(""" <center> IV LECTURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("IV LECTURA A COMPRENSION PARTE 1",
                     Field("IVA1_ACIERTO","IVA1_ERROR","IVA1_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 2",
                     Field("IVA2_ACIERTO","IVA2_ERROR","IVA2_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 3",
                     Field("IVA3_ACIERTO","IVA3_ERROR","IVA3_OMISION")),

                 Fieldset("IV LECTURA A COMPRENSION PARTE 4",
                     Field("IVA4_ACIERTO","IVA4_ERROR","IVA4_OMISION")),



                 Fieldset("IV LECTURA B VELOCIDAD",
                     Field("IVB_ACIERTO","IVB_ERROR","IVB_OMISION")),
                 Fieldset("IV LECTURA C VELOCIDAD",
                     Field("IVC_ACIERTO","IVC_ERROR","IVC_OMISION"))),
                 HTML("""  <p></p> """), #espacio


                 Fieldset("",#Seccion
                 HTML(""" <center> V ESCRITURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("V ESCRITURA A. ORTOGRAFIA",
                     Field("VA_ACIERTO","VA_ERROR","VA_OMISION")),
                 HTML("""  <p></p> """),
                 Fieldset("V ESCRITURA B. EXP ESCRITA",
                     Field("V")),
                 HTML("""  <p></p> """)), #espacio


                 Fieldset("",#Seccion
                 HTML(""" <center> VI APRENDIZAJE MATEMATICOS </center> """),#Titulo
                 HTML("""  <p></p> """),
                 Fieldset("VI APREND MATEMATICOS A CAL&NUM",
                     Field("VIA_ACIERTO","VIA_ERROR","VIA_OMISION")),
                 Fieldset("VI APREND MATEMATICOS B RESOLUC",
                     Field("VIB_ACIERTO","VIB_ERROR","VIB_OMISION"))),
                 HTML("""  <p></p> """)), #espacio


                 HTML(""" </center> """),#center



             #fin codigo columnas
             HTML("""  </div>
                         </div>

                         </body>
                         </html>
                           """),
 HTML(""" <center> """),#center
 ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
 HTML(""" </center> """),#center

  )

    class Meta():
        model = Modelo_EVALUA_10
        exclude = ("user",)
        labels = {
            'Rut':('Estudiante'),
            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),
            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),
            "IIA1_OMISION":("Omisiones"),
            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),
            "IIA2_OMISION":("Omisiones"),
            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),
            "IIA3_OMISION":("Omisiones"),

            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),
            "IIB1_OMISION":("Omisiones"),
            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),
            "IIB2_OMISION":("Omisiones"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),
            "IIC1_OMISION":("Omisiones"),
            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),
            "IIC2_OMISION":("Omisiones"),

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),
            "IVA1_OMISION":("Omisiones"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),
            "IVA2_OMISION":("Omisiones"),

            "IVA3_ACIERTO":("Aciertos"),
            "IVA3_ERROR":("Errores"),
            "IVA3_OMISION":("Omisiones"),

            "IVA4_ACIERTO":("Aciertos"),
            "IVA4_ERROR":("Errores"),
            "IVA4_OMISION":("Omisiones"),

            "IVB_ACIERTO":("Aciertos"),
            "IVB_ERROR":("Errores"),
            "IVB_OMISION":("Omisiones"),



            "VA_ACIERTO":("Aciertos"),
            "VA_ERROR":("Errores"),
            "VA_OMISION":("Omisiones"),
            "V":("Expresión Escrita"),
            "VIA_ACIERTO":("Aciertos"),
            "VIA_ERROR":("Errores"),
            "VIA_OMISION":("Omisiones"),
            "VIB_ACIERTO":("Aciertos"),
            "VIB_ERROR":("Errores"),
            "VIB_OMISION":("Omisiones"),


            }
        widgets = { #'Colegio': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    'Escolaridad': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    #'Evaluador': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    }



###VERSIÓN 2.0

#formseva2.py
