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


#FormEVA2_XX
#Modelo_EVALUA2_XX

class FormEVA2_00(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_00,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
                 ######## codigo para columnas y columna 1
#####ARREGLAR CODIGO DOBLE PAGINA
                HTML(""" <center> """),#center I1
                Fieldset("",  #Seccion
                HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                HTML("""  <p></p> """), #espacio

                Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
                HTML(""" <center> I  CAPACIDADES COGNITIVAS </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("A) CLASIFICACIÓN. PARTE 1",
                    Field("IA1_ACIERTO","IA1_ERROR","IA1_OMISION")),
                Fieldset("A) CLASIFICACIÓN. PARTE 2",
                    Field("IA2_ACIERTO","IA2_ERROR","IA2_OMISION")),
                Fieldset("B) SERIES. PARTE 1",
                    Field("IB1_ACIERTO","IB1_ERROR","IB1_OMISION")),
                Fieldset("B) SERIES. PARTE 2",
                    Field("IB2_ACIERTO","IB2_ERROR","IB2_OMISION")),
                Fieldset("B) SERIES. PARTE 3",
                    Field("IB3_ACIERTO","IB3_ERROR","IB3_OMISION")),
                Fieldset("C) ORGANIZACION PERCEPTIVA. PARTE 1 CABALLO",
                    Field("IC1_ERROR","IC1_OMISION")),
                Fieldset("C) ORGANIZACION PERCEPTIVA. PARTE 2 DINOSAURIO",
                    Field("IC2_ERROR","IC2_OMISION")),
                Fieldset("C) ORGANIZACION PERCEPTIVA. PARTE 3 UVAS",
                    Field("IC3_ERROR","IC3_OMISION")),
                Fieldset("C) ORGANIZACION PERCEPTIVA. PARTE 4 PLATANOS",
                    Field("IC4_ERROR","IC4_OMISION")),
                Fieldset("D) LETRAS Y NÚMEROS PARTE 1",
                    Field("ID1_ACIERTO","ID1_ERROR","ID1_OMISION")),
                 Fieldset("D) LETRAS Y NÚMEROS PARTE 2",
                    Field("ID2_ACIERTO","ID2_ERROR","ID2_OMISION")),),




                HTML("""  <p></p> """), #espacio
                HTML("""  <p></p> """), #espacio
                HTML("""  </div> """), #fin columna uno
                HTML(""" </center> """),#center

            #////////////////////////////
                HTML(""" <center> """),#center
                HTML("""   <div class="column"  """), #inicio columna dos



                Fieldset("",#Seccion
                Fieldset("",#Seccion
                HTML(""" <center> I  CAPACIDADES COGNITIVAS </center> """),#Titulo
                HTML("""  <p></p> """),

                Fieldset("E) MEMORIA VERBAL 1",
                   Field("IE1_ACIERTO")),
                Fieldset("E) MEMORIA VERBAL 2",
                   Field("IE2_ACIERTO")),),

                 Fieldset("",#Seccion
                 HTML(""" <center> II  CAPACIDADES ESPACIALES </center> """),#Titulo
                 HTML("""  <p></p> """),
                Fieldset("A) COPIA DE DIBUJOS PARTE 1",
                    Field("IIA1_ACIERTO",)),
                Fieldset("A) COPIA DE DIBUJOS PARTE 2",
                    Field("IIA2_ACIERTO",)),
                Fieldset("B)  GRAFOMOTRICIDAD PARTE 1",
                    Field("IIB1_ERROR",)),
                Fieldset("B)  GRAFOMOTRICIDAD PARTE 2",
                    Field("IIB2_ERROR",)),
                Fieldset("B)  GRAFOMOTRICIDAD PARTE 3",
                    Field("IIB3_ERROR",)),
                Fieldset("B)  GRAFOMOTRICIDAD PARTE 4",
                    Field("IIB4_ERROR",)),
                Fieldset("B)  GRAFOMOTRICIDAD PARTE 5",
                    Field("IIB5_ERROR",)),
                Fieldset("B)  GRAFOMOTRICIDAD PARTE 6",
                    Field("IIB6_ERROR",)),),

                Fieldset("",#Seccion
                HTML(""" <center> III  CAPACIDADES LINGÜISTICAS </center> """),#Titulo
                HTML("""  <p></p> """),
               Fieldset("A) PALABRAS Y FRASES DIBUJOS PARTE 1",
                   Field("IIIA1_ACIERTO",)),

               Fieldset("B) RECEPCIÓN AUDITIVA PARTE 1",
                   Field("IIIB1_ACIERTO",)),
                Fieldset("B) RECEPCIÓN AUDITIVA PARTE 2",
                    Field("IIIB2_ACIERTO",)),
                Fieldset("B) RECEPCIÓN AUDITIVA PARTE 3",
                    Field("IIIB3_ACIERTO",)),

                Fieldset("B) HABILIDADES FONOLÓGICAS PARTE 1",
                    Field("IIIC1_ACIERTO",)),
                 Fieldset("B) HABILIDADES FONOLÓGICAS PARTE 2",
                     Field("IIIC2_ACIERTO",)),
                 Fieldset("B) HABILIDADES FONOLÓGICAS PARTE 3",
                     Field("IIIC3_ACIERTO",)),
                Fieldset("B) HABILIDADES FONOLÓGICAS PARTE 4",
                    Field("IIIC4_ACIERTO",)),
                                                ),





                 HTML("""  <p></p> """), #espacio
                 HTML(""" </center> """),#center



                 #fin codigo columnas
                 HTML("""  </div>
                             </div>

                             </body>
                             </html>
                               """),

         HTML(""" <center> """),#center
         ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
         HTML(""" </center> """)),)#center



    class Meta():
        model = Modelo_EVALUA2_00
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),
            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),


            "IA1_ACIERTO": ("Aciertos"),
            "IA1_ERROR": ("Errores"),
            "IA1_OMISION": ("Omisiones"),

            "IA2_ACIERTO": ("Aciertos"),
            "IA2_ERROR": ("Errores"),
            "IA2_OMISION": ("Omisiones"),

            # SERIES
            "IB1_ACIERTO": ("Aciertos"),
            "IB1_ERROR": ("Errores"),
            "IB1_OMISION":("Omisiones"),

            "IB2_ACIERTO": ("Aciertos"),
            "IB2_ERROR": ("Errores"),
            "IB2_OMISION": ("Omisiones"),

            "IB3_ACIERTO": ("Aciertos"),
            "IB3_ERROR": ("Errores"),
            "IB3_OMISION": ("Omisiones"),


            "IC1_ERROR": ("Errores"),
            "IC1_OMISION":("Omisiones"),


            "IC2_ERROR": ("Errores"),
            "IC2_OMISION": ("Omisiones"),


            "IC3_ERROR": ("Errores"),
            "IC3_OMISION": ("Omisiones"),


            "IC4_ERROR": ("Errores"),
            "IC4_OMISION": ("Omisiones"),


            "ID1_ACIERTO": ("Aciertos"),
            "ID1_ERROR": ("Errores"),
            "ID1_OMISION": ("Omisiones"),

            "ID2_ACIERTO": ("Aciertos"),
            "ID2_ERROR": ("Errores"),
            "ID2_OMISION": ("Omisiones"),


            "IE1_ACIERTO": ("Puntaje"),

            "IE2_ACIERTO": ("Puntaje"),
##################################################
            "IIA1_ACIERTO": ("Puntaje"),

            "IIA2_ACIERTO": ("Puntaje"),

            "IIB1_ERROR":  ("Errores"),
            "IIB2_ERROR":  ("Errores"),
            "IIB3_ERROR":  ("Errores"),
            "IIB4_ERROR":  ("Errores"),
            "IIB5_ERROR":  ("Errores"),
            "IIB6_ERROR":  ("Errores"),
###################################################

            "IIIA1_ACIERTO":  ("Puntaje"),

            "IIIB1_ACIERTO": ("Aciertos"),
            "IIIB2_ACIERTO": ("Aciertos"),
            "IIIB3_ACIERTO": ("Aciertos"),

            "IIIC1_ACIERTO":  ("Puntaje"),
            "IIIC2_ACIERTO":  ("Puntaje"),
            "IIIC3_ACIERTO":  ("Puntaje"),
            "IIIC4_ACIERTO":  ("Puntaje"),}
##################################################


        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}



class FormEVA2_01(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_01,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
                 ######## codigo para columnas y columna 1
                HTML(""" <center> """),#center I1
                Fieldset("",  #Seccion
                HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                HTML("""  <p></p> """), #espacio

                Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
                Fieldset( "",#Seccion
                HTML(""" <center>I  MEMORIA-ATENCIÓN  </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("",
                    Field("I_ACIERTO","I_ERROR","I_OMISION")),),

                HTML(""" <center> """),#center
                Fieldset("",#Seccion
                HTML(""" <center>II BASES DEL RAZONAMIENTO </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("IIA SERIES ",
                    Field("IIA1_ACIERTO","IIA1_ERROR",)),
                HTML("""  <p></p> """),
                Fieldset("IIB CLASIFICACIONES ",
                    Field("IIB1_ACIERTO","IIB1_ERROR",)),
                HTML("""  <p></p> """),
                Fieldset("IIC ORGANIZACION PRECEPTIVA ",
                    Field("IIC1_ACIERTO",)),),



                HTML("""  <p></p> """), #espacio
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

                Fieldset("IVA COMPRENSIÓN LECTORA PARTE 1",
                   Field("IVA1_ACIERTO","IVA1_ERROR","IVA1_OMISION")),
                Fieldset("IVA COMPRENSIÓN LECTORA PARTE 2",
                   Field("IVA2_ACIERTO")),
                Fieldset("IVA COMPRENSIÓN LECTORA PARTE 3",
                   Field("IVA3_ACIERTO")),
                HTML("""  <p></p> """),
                Fieldset("IVB EXACTITUD LECTORA",
                   Field("IVB1_ACIERTO")),),

                 Fieldset("",#Seccion
                 HTML(""" <center>V ESCRITURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                Fieldset("VA ORTOFONÉTICA PARTE 1",
                    Field("VA1_ACIERTO",)),
                Fieldset("VA ORTOFONÉTICA PARTE 2",
                    Field("VA2_ACIERTO",)),
                Fieldset("VA ORTOFONÉTICA PARTE 3",
                    Field("VA3_ACIERTO",)),
                Fieldset("VB GRAFÍA Y EXP ESCRITA",
                    Field("VB",)),
                Fieldset("VC ORTOGRAFÍA VISUAL",
                    Field("VC1_ACIERTO",)),
                ),

                Fieldset("",#Seccion
                HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
                HTML("""  <p></p> """),
               Fieldset("VIA CALCULO Y NUMERACIÓN ",
                   Field("VIA1_ACIERTO",)),                ),

                 HTML("""  <p></p> """), #espacio
                 HTML(""" </center> """),#center

                 #fin codigo columnas
                 HTML("""  </div>
                             </div>

                             </body>
                             </html>
                               """),

         HTML(""" <center> """),#center
         ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
         HTML(""" </center> """)),)#center



    class Meta():
        model = Modelo_EVALUA2_01
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),

            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),

            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),
            "IVA1_OMISION":("Omisiones"),

            "IVA2_ACIERTO":("Aciertos"),

            "IVA3_ACIERTO":("Aciertos"),

            "IVB1_ACIERTO":("Aciertos"),


            "VA1_ACIERTO":("Aciertos"),
            "VA2_ACIERTO":("Aciertos"),
            "VA3_ACIERTO":("Aciertos"),


            "VA_ERROR":("Errores"),
            "VA_OMISION":("Omisiones"),
            "VB":("Grafía  & Expresión Escrita"),

            "VC1_ACIERTO":("Aciertos"),

            "VIA1_ACIERTO":("Aciertos"),



            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}


class FormEVA2_02(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_02,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
                 ######## codigo para columnas y columna 1
                HTML(""" <center> """),#center I1
                Fieldset("",  #Seccion
                HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                HTML("""  <p></p> """), #espacio

                Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
                HTML(""" <center> """),
                Fieldset("",
                Fieldset( "",#Seccion
                HTML(""" <center>I BASES DEL RAZONAMIENTO </center> """),#Titulo
                HTML("""  <p></p> """),
                HTML(""" <center>  </center> """),
                Fieldset("IA  PENSAMIENTO ANALÓGICO",
                    Field("IA1_ACIERTO","IA1_ERROR",)),


                HTML(""" <center>  </center> """),#Titulo
                HTML("""  <p></p> """),

                Fieldset("IB  ORGANIZACIÓN PERCEPTIVA",
                    Field("IB1_ACIERTO","IB1_ERROR",)),


                HTML(""" <center>  </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("IC CLASIFICACIONES TAREA 1",
                HTML(""" <center>  </center> """),
                    Field("IC1_ACIERTO","IC1_ERROR",)),
                HTML(""" <center> TAREA 2 </center> """),
                Fieldset("IC CLASIFICACIONES TAREA 2",
                    Field("IC2_ACIERTO","IC2_ERROR",)),),

                HTML(""" <center> """),#center
                Fieldset("",#Seccion
                HTML(""" <center> </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("II MEMORIA Y ATENCIÓN ",
                    Field("IIA1_ACIERTO","IIA1_ERROR","IIA1_OMISION")),),),



                HTML("""  <p></p> """), #espacio
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

                Fieldset("IVA COMPRENSIÓN LECTORA PARTE 1",
                   Field("IVA1_ACIERTO","IVA1_ERROR",)),
                Fieldset("IVA COMPRENSIÓN LECTORA PARTE 2",
                   Field("IVA2_ACIERTO","IVA2_ERROR",)),
                Fieldset("IVA COMPRENSIÓN LECTORA PARTE 3",
                   Field("IVA3_ACIERTO")),
                HTML("""  <p></p> """),
                Fieldset("IVB EXACTITUD LECTORA",
                   Field("IVB")),),

                 Fieldset("",#Seccion
                 HTML(""" <center>V ESCRITURA </center> """),#Titulo
                 HTML("""  <p></p> """),
                Fieldset("VA GRAFÍA",
                    Field("VA",)),
                Fieldset("VB ORTOGRAFIA PARTE 1 AUTODICTADO",
                    Field("VB1_ACIERTO",)),
                Fieldset("VB ORTOGRAFIA PARTE 2 DICTADO",
                    Field("VB2_ACIERTO","VB2_ERROR")),
                ),

                Fieldset("",#Seccion
                HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("VIA CALCULO Y NUMERACIÓN  ÍTEM 1 AL 49",
                   Field("VIA1_ACIERTO",)),
                Fieldset("VIA CALCULO Y NUMERACIÓN ÍTEM 50 AL 55",
                   Field("VIA2_ACIERTO","VIA2_ERROR",)),

                 Fieldset("VIB RESOLUCIÓN DE PROBLEMAS",
                     Field("VIB1_ACIERTO",)),

                      ),

                 HTML("""  <p></p> """), #espacio
                 HTML(""" </center> """),#center

                 #fin codigo columnas
                 HTML("""  </div>
                             </div>

                             </body>
                             </html>
                               """),

         HTML(""" <center> """),#center
         ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
         HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_02
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "IA1_ACIERTO":("Aciertos"),
            "IA1_ERROR":("Errores"),

            "IB1_ACIERTO":("Aciertos"),
            "IB1_ERROR":("Errores"),

            "IC1_ACIERTO":("Aciertos"),
            "IC1_ERROR":("Errores"),

            "IC2_ACIERTO":("Aciertos"),
            "IC2_ERROR":("Errores"),


            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),
            "IIA1_OMISION":("Omisiones"),

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),

            "IVA3_ACIERTO":("Aciertos"),

            "IVB":("Exactitud lectora"),

            "VA":("Grafía"),

            "VB1_ACIERTO":("Aciertos"),
            "VB2_ERROR":("Errores"),


            "V":("Expresión Escrita"),

            "VIA1_ACIERTO":("Aciertos"),
            "VIA2_ACIERTO":("Aciertos"),
            "VIA2_ERROR":("Errores"),

            "VIB1_ACIERTO":("Aciertos"),



            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}


class FormEVA2_03(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_03,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
 ######## codigo para columnas y columna 1
HTML(""" <center> """),#center I1
Fieldset("",  #Seccion
HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
HTML("""  <p></p> """), #espacio

Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
HTML(""" <center> """),
Fieldset("",
Fieldset( "",#Seccion
HTML(""" <center>I MEMORIA Y ATENCIÓN  </center> """),#Titulo
HTML("""  <p></p> """),
HTML(""" <center>  </center> """),
Fieldset("",
    Field("I_ACIERTO","I_ERROR","I_OMISION")),


HTML(""" <center>  </center> """),#Titulo
HTML("""  <p> BASES DEL RAZONAMIENTO </p> """),

Fieldset("A REFLEXIBIDAD",
    Field("IIA1_ACIERTO","IIA1_ERROR",)),

Fieldset("B PENSAMIENTO ANALÓGICO",
    Field("IIB1_ACIERTO","IIB1_ERROR",)),

Fieldset("C ORGANIZACION PERCEPTIVA TAREA 1",
    Field("IIC1_ACIERTO","IIC1_ERROR",)),
Fieldset("C ORGANIZACION PERCEPTIVA TAREA 2",
    Field("IIC2_ACIERTO","IIC2_ERROR",)),



HTML(""" <center>  </center> """),#Titulo
HTML("""  <p>IV LECTURA</p> """),
Fieldset("A COMPRENSIÓN LECTORA",
    Field("IVA1_ACIERTO","IVA1_ERROR",)),

Fieldset("B EXACTITUD LECTORA TAREA 1",
    Field("IVB1_ACIERTO","IVB1_ERROR",)),

Fieldset("B EXACTITUD LECTORA TAREA 2",
    Field("IVB2_ACIERTO",)),),

HTML(""" <center> """),#center
),




HTML("""  </div> """), #fin columna uno
HTML(""" </center> """),#center

#////////////////////////////
HTML(""" <center> """),#center
HTML("""   <div class="column"  """), #inicio columna dos



Fieldset("",#Seccion

 Fieldset("",#Seccion
 HTML(""" <center>V ESCRITURA </center> """),#Titulo
 HTML("""  <p></p> """),
Fieldset("A ORTOGRAFÍA FONÉTICA",
    Field("VA1_ACIERTO",)),
Fieldset("B GRAFÍA Y EXPRESIÓN ESCRITA",
    Field("VB1",)),

Fieldset("C1 ORTOGRAFÍA VISUAL, ESCRITURA DE PALABRAS  ",
    Field("VC1_ACIERTO","VC1_ERROR")),
Fieldset("C2 ORTOGRAFÍA VISUAL, RECONOCIMIENTO DE PALABRAS  ",
    Field("VC2_ACIERTO","VC2_ERROR", "VC2_OMISION")),
Fieldset("C3 ORTOGRAFÍA VISUAL, DICTADO ",
    Field("VC3_ERROR")),



),

Fieldset("",#Seccion
HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
HTML("""  <p></p> """),
Fieldset("A CALCULO Y NUMERACIÓN ",
   Field("VIA1_ACIERTO",)),
Fieldset("B RESOLUCIÓN DE PROBLEMAS ÍTEM 1-15",
   Field("VIB1_ACIERTO",)),
 Fieldset("B RESOLUCIÓN DE PROBLEMAS ÍTEM 6",
    Field("VIB2_ACIERTO",)),

      ),

 HTML("""  <p></p> """), #espacio
 HTML(""" </center> """),#center

 #fin codigo columnas
 HTML("""  </div>
             </div>

             </body>
             </html>
               """),

HTML(""" <center> """),#center
ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_03
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),

            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),


            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),

            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),


            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),


            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),

            "IVB2_ACIERTO":("Aciertos"),
######


            "VA1_ACIERTO":("Aciertos"),

            "VB1":("Expresión Escrita"),

            "VC1_ACIERTO": ("Aciertos"),

            "VC1_ERROR":("Errores"),

            # ESCRITURA DE PALABRAS
            "VC2_ACIERTO": ("Aciertos"),
            "VC2_ERROR": ("Errores"),
            "VC2_OMISION": ("Omisiones"),

            "VC3_ERROR": ("Errores"),

            "VIA1_ACIERTO":("Aciertos"),


            "VIB1_ACIERTO":("Aciertos"),
            "VIB2_ACIERTO":("Aciertos"),


            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}


class FormEVA2_04(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_04,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion
    HTML(""" <center>I MEMORIA Y ATENCIÓN  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("",
        Field("I_ACIERTO","I_ERROR","I_OMISION")),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> BASES DEL RAZONAMIENTO </p> """),

    Fieldset("A REFLEXIBIDAD TAREA 1",
        Field("IIA1_ACIERTO","IIA1_ERROR",)),

    Fieldset("B PENSAMIENTO ANALÓGICO TAREA 2",
        Field("IIB1_ACIERTO","IIB1_ERROR",)),

    Fieldset("B PENSAMIENTO ANALÓGICO TAREA 3",
        Field("IIB2_ACIERTO","IIB2_ERROR",)),

    Fieldset("C ORGANIZACION PERCEPTIVA TAREA 4",
        Field("IIC1_ACIERTO","IIC1_ERROR",)),
    Fieldset("C ORGANIZACION PERCEPTIVA TAREA 5",
        Field("IIC2_ACIERTO","IIC2_ERROR",)),



    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A COMPRENSIÓN LECTORA ÍTEM 1-17",
        Field("IVA1_ACIERTO","IVA1_ERROR",)),

    Fieldset("A COMPRENSIÓN LECTORA ÍTEM 28-33",
        Field("IVA2_ACIERTO","IVA2_ERROR",)),

    Fieldset("B VELOCIDAD LECTORA COMPRENSIÓN",
        Field("IVB1_ACIERTO","IVB1_ERROR","IVB1_OMISION")),

    Fieldset("B VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)), ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A ORTOGRAFÍA VISUAL Y REGLADA, DICTADO",
        Field("VA1_ERROR",)),
    Fieldset("A ORTOGRAFÍA VISUAL Y REGLADA, RECONOCIMIENTO",
        Field("VA2_ACIERTO","VA2_ERROR","VA2_OMISION")),

    Fieldset("B GRAFÍA Y EXP ESCRITA, PARTE 1 GRAFISMO  ",
        Field("VB1",)),
    Fieldset("B GRAFÍA Y EXP ESCRITA, PARTE 2 ORTOGRAFÍA  ",
        Field("VB2")),
        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN PARTE 1 SERIES Y NUMEROS",
       Field("VIA1_ACIERTO",)),
    Fieldset("A CALCULO Y NUMERACIÓN PARTE 2 ESCRITURA, DESCOMPOSICIÓN Y OPERACIONES",
       Field("VIA2_ACIERTO",)),
     Fieldset("A CALCULO Y NUMERACIÓN PARTE 3 FRACCIONES",
        Field("VIA3_ACIERTO","VIA3_ERROR")),



    Fieldset("B RESOLUCIÓN DE PROBLEMAS",
       Field("VIB1_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_04
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),

            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),


            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),

            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),


            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),


            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),
            "IVB1_OMISION":("Omisiones"),
            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),
######

            "VA1_ERROR":("Errores"),
            "VA2_ACIERTO": ("Aciertos"),
            "VA2_ERROR": ("Errores"),
            "VA2_OMISION": ("Omisiones"),

            "VA_ACIERTO":("Aciertos"),

            "VB1":("GRAFISMO"),

            "VB2":("ORTOGRAFÍA"),

            "VC3_ERROR": ("Errores"),

            "VIA1_ACIERTO":("Aciertos"),
            "VIA2_ACIERTO":("Aciertos"),
            "VIA3_ACIERTO":("Aciertos"),
            "VIA3_ERROR":("Errores"),


            "VIB1_ACIERTO":("Aciertos"),



            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}



class FormEVA2_05(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_05,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion
    HTML(""" <center>I MEMORIA Y ATENCIÓN  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("",
        Field("I_ACIERTO","I_ERROR","I_OMISION")),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> BASES DEL RAZONAMIENTO </p> """),

    Fieldset("A REFLEXIBIDAD ",
        Field("IIA1_ACIERTO","IIA1_ERROR",)),

    Fieldset("B PENSAMIENTO ANALÓGICO ",
        Field("IIB1_ACIERTO","IIB1_ERROR",)),

    Fieldset("C ORGANIZACION PERCEPTIVA ",
        Field("IIC1_ACIERTO","IIC1_ERROR",)),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A COMPRENSIÓN LECTORA",
        Field("IVA1_ACIERTO","IVA1_ERROR","IVA1_OMISION")),


    Fieldset("B VELOCIDAD LECTORA COMPRENSIÓN",
        Field("IVB1_ACIERTO","IVB1_ERROR","IVB1_OMISION")),

    Fieldset("B VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)),

    Fieldset("C EXACTITUD LECTORA TAREA 1",
        Field("IVC1_ACIERTO","IVC1_ERROR","IVC1_OMISION",)),

    Fieldset("C EXACTITUD LECTORA TAREA 2",
        Field("IVC2_ACIERTO","IVC2_ERROR","IVC2_OMISION",)),



         ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A1 ORTOGRAFÍA FONÉTICA DICTADO PALABRAS",
        Field("VA1_ACIERTO",)),

    Fieldset("A2 ORTOGRAFÍA FONÉTICA DICTADO FRASES",
        Field("VA2_ACIERTO",)),
    Fieldset("B GRAFÍA Y EXPRESIÓN ESCRITA ",
        Field("VB1")),

    Fieldset("C ORTOGRAFÍA VISUAL Y REGLADA TAREA1 ",
        Field("VC1_ACIERTO","VC1_ERROR","VC1_OMISION")),

    Fieldset("B GRAFÍA Y EXP ESCRITA, PARTE 2 ORTOGRAFÍA  ",
        Field("VC2_ERROR")),

        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN ÍTEM 1 Y 2",
       Field("VIA1_ACIERTO","VIA1_ERROR","VIA1_OMISION")),
    Fieldset("A CALCULO Y NUMERACIÓN ÍTEM 3",
       Field("VIA2_ACIERTO",)),
     Fieldset("A CALCULO Y NUMERACIÓN ÍTEM 4",
        Field("VIA3_ACIERTO",)),
    Fieldset("A CALCULO Y NUMERACIÓN ÍTEM 5",
        Field("VIA4_ACIERTO",)),
######

    Fieldset("B RESOLUCIÓN DE PROBLEMAS  1-5",
       Field("VIB1_ACIERTO",)),

     Fieldset("B RESOLUCIÓN DE PROBLEMAS 6-12",
        Field("VIB2_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_05
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),


            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),

            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),

            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),
            "IVA1_OMISION":("Omisiones"),

            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),
            "IVB1_OMISION":("Omisiones"),

            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),


            "IVC1_ACIERTO":("Aciertos"),
            "IVC1_ERROR":("Errores"),
            "IVC1_OMISION":("Omisiones"),

            "IVC2_ACIERTO":("Aciertos"),
            "IVC2_ERROR":("Errores"),
            "IVC2_OMISION":("Omisiones"),

######

            "VC1_ACIERTO":("Aciertos"),
            "VC1_ERROR":("Errores"),

            "IVC2_ACIERTO":("Aciertos"),
            "IVC2_ERROR":("Errores"),

            # ESCRITURA

            "VA1_ACIERTO": ("Aciertos"),
            "VA2_ACIERTO": ("Aciertos"),

            "VB1":(""),

            "VC1_ACIERTO":("Aciertos"),
            "VC1_ERROR":("Errores"),
            "VC1_OMISION":("Omisiones"),

            "VC2_ERROR": ("Errores"),

            # APRENDIZAJES MATEMATICOS

            "VIA1_ACIERTO":("Aciertos"),
            "VIA1_ERROR":("Errores"),
            "VIA1_OMISION":("Omisiones"),



            "VIA2_ACIERTO":("Aciertos"),
            "VIA3_ACIERTO":("Aciertos"),
            "VIA4_ACIERTO":("Aciertos"),


            "VIB1_ACIERTO":("Aciertos"),
            "VIB2_ACIERTO":("Aciertos"),


            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}

class FormEVA2_06(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_06,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> BASES DEL RAZONAMIENTO </p> """),

    Fieldset("A REFLEXIBIDAD TAREA 1",
        Field("IA1_ACIERTO","IA1_ERROR",)),

    Fieldset("B PENSAMIENTO ANALÓGICO TAREA 2 ",
        Field("IB1_ACIERTO","IB1_ERROR",)),

    Fieldset("C ORGANIZACION PERCEPTIVA TAREA 3",
        Field("IC1_ACIERTO","IC1_ERROR",)),

    Fieldset("C ORGANIZACION PERCEPTIVA TAREA 4",
        Field("IC2_ACIERTO","IC2_ERROR",)),

    HTML(""" <center>II MEMORIA Y ATENCIÓN  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("",
        Field("II_ACIERTO","II_ERROR","II_OMISION")),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A COMPRENSIÓN LECTORA TAREA 1",
        Field("IVA1_ACIERTO","IVA1_ERROR",)),
    Fieldset("A COMPRENSIÓN LECTORA TAREA 2: 1-5",
        Field("IVA2_ACIERTO","IVA2_ERROR",)),
    Fieldset("A COMPRENSIÓN LECTORA TAREA 2: 6-10  ",
        Field("IVA3_ACIERTO","IVA3_ERROR",)),
    Fieldset("A COMPRENSIÓN LECTORA TAREA 3: 1-9",
        Field("IVA4_ACIERTO","IVA4_ERROR",)),
    Fieldset("A COMPRENSIÓN LECTORA TAREA 3: 10-14",
        Field("IVA5_ACIERTO","IVA5_ERROR",)),

    Fieldset("B VELOCIDAD LECTORA COMPRENSIÓN",
        Field("IVB1_ACIERTO","IVB1_ERROR","IVB1_OMISION")),

    Fieldset("B VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)), ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A1 ORTOGRAFÍA FONÉTICA DICTADO PALABRAS",
        Field("VA1_ACIERTO",)),

    Fieldset("A2 ORTOGRAFÍA FONÉTICA DICTADO FRASES",
        Field("VA2_ACIERTO","VA2_ERROR","VA2_OMISION")),
    Fieldset("B GRAFÍA Y EXPRESIÓN ESCRITA: GRAFISMO  ",
        Field("VB1")),
    Fieldset("B GRAFÍA Y EXPRESIÓN ESCRITA: ORTOGRAFÍA ",
        Field("VB2")),

        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN: 1-9",
       Field("VIA1_ACIERTO","VIA1_ERROR",)),
    Fieldset("A CALCULO Y NUMERACIÓN: 10-12",
       Field("VIA2_ACIERTO",)),
     Fieldset("A CALCULO Y NUMERACIÓN: 13-35",
        Field("VIA3_ACIERTO","VIA3_ERROR")),
    ######

    Fieldset("B RESOLUCIÓN DE PROBLEMAS",
       Field("VIB1_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_06
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "II_ACIERTO":("Aciertos"),
            "II_ERROR":("Errores"),
            "II_OMISION":("Omisiones"),

            "IA1_ACIERTO":("Aciertos"),
            "IA1_ERROR":("Errores"),

            "IB1_ACIERTO":("Aciertos"),
            "IB1_ERROR":("Errores"),

            "IC1_ACIERTO":("Aciertos"),
            "IC1_ERROR":("Errores"),

            "IC2_ACIERTO":("Aciertos"),
            "IC2_ERROR":("Errores"),

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),

            "IVA3_ACIERTO":("Aciertos"),
            "IVA3_ERROR":("Errores"),

            "IVA4_ACIERTO":("Aciertos"),
            "IVA4_ERROR":("Errores"),


            "IVA5_ACIERTO":("Aciertos"),
            "IVA5_ERROR":("Errores"),


            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),
            "IVB1_OMISION":("Omisiones"),

            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),
######

            # ESCRITURA

            "VA1_ACIERTO": ("Aciertos"),
            "VA2_ACIERTO": ("Aciertos"),
            "VA2_ERROR":("Errores"),
            "VA2_OMISION":("Omisiones"),

            "VB1":(""),
            "VB2":(""),

            # APRENDIZAJES MATEMATICOS

            "VIA1_ACIERTO":("Aciertos"),
            "VIA1_ERROR":("Errores"),

            "VIA2_ACIERTO":("Aciertos"),

            "VIA3_ACIERTO":("Aciertos"),
            "VIA3_ERROR":("Errores"),


            "VIB1_ACIERTO":("Aciertos"),


            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}



class FormEVA2_07(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_07,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> I ATENCIÓN CONCENTRACIÓN </p> """),

    Fieldset("",
        Field("I_ACIERTO","I_ERROR","I_OMISION")),



    HTML(""" <center>II BASES DEL RAZONAMIENTO  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("A RAZONAMIENTO DEDUCTIVO",
        Field("IIA1_ACIERTO","IIA1_ERROR"),),

    Fieldset("B RAZONAMIENTO INDUCTIVO ",
        Field("IIB1_ACIERTO","IIB1_ERROR",)),

    Fieldset("C RAZONAMIENTO ESPACIAL TAREA 1",
        Field("IIC1_ACIERTO","IIC1_ERROR",)),

    Fieldset("C RAZONAMIENTO ESPACIAL TAREA 2",
        Field("IIC2_ACIERTO","IIC2_ERROR",)),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A EFICACIA LECTORA",
        Field("IVA1_ACIERTO",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 1",
        Field("IVB1_ACIERTO","IVB1_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 2",
        Field("IVB2_ACIERTO","IVB2_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 3",
        Field("IVB3_ACIERTO","IVB3_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 4",
        Field("IVB4_ACIERTO","IVB4_ERROR",)),


    Fieldset("C VELOCIDAD LECTORA COMPRENSIÓN",
        Field("IVC1_ACIERTO","IVC1_ERROR","IVC1_OMISION")),

    Fieldset("C VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)), ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A DICTADO ",
        Field("VA1_ACIERTO",)),


    Fieldset("B EXPRESIÓN ESCRITA  ",
        Field("VB1")),

    Fieldset("C ORTOGRAFÍA VISUAL Y REGLADA  TAREA 1  ",
        Field("VC1_ACIERTO","VC1_ERROR","VC1_OMISION")),

    Fieldset("C ORTOGRAFÍA VISUAL Y REGLADA  TAREA 2  ",
        Field("VC2_ACIERTO","VC2_ERROR","VC2_OMISION")),

        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN",
       Field("VIA1_ACIERTO",)),

    ######

    Fieldset("B RESOLUCIÓN DE PROBLEMAS ÍTEM 1-26",
       Field("VIB1_ACIERTO",)),

      Fieldset("B RESOLUCIÓN DE PROBLEMAS ÍTEM 27-34",
         Field("VIB2_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_07
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),


            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),

            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),

            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),



            "IVA1_ACIERTO":("Aciertos"),

            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),

            "IVB2_ACIERTO":("Aciertos"),
            "IVB2_ERROR":("Errores"),

            "IVB3_ACIERTO":("Aciertos"),
            "IVB3_ERROR":("Errores"),

            "IVB4_ACIERTO":("Aciertos"),
            "IVB4_ERROR":("Errores"),

            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),

            "IVC1_ACIERTO":("Aciertos"),
            "IVC1_ERROR":("Errores"),
            "IVC1_OMISION":("Omisiones"),


######
            # ESCRITURA

            "VA1_ACIERTO": ("Aciertos"),

            "VB1": (""),


            "VC1_ACIERTO":("Aciertos"),
            "VC1_ERROR":("Errores"),
            "VC1_OMISION":("Omisiones"),

            "VC2_ACIERTO":("Aciertos"),
            "VC2_ERROR":("Errores"),
            "VC2_OMISION":("Omisiones"),


            # APRENDIZAJES MATEMATICOS

            "VIA1_ACIERTO":("Aciertos"),


            "VIB1_ACIERTO":("Aciertos"),
            "VIB2_ACIERTO":("Aciertos"),


            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}


class FormEVA2_08(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_08,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> I ATENCIÓN CONCENTRACIÓN </p> """),

    Fieldset("",
        Field("I_ACIERTO","I_ERROR","I_OMISION")),



    HTML(""" <center>II  RAZONAMIENTO  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 1",
        Field("IIA1_ACIERTO","IIA1_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 2",
        Field("IIA2_ACIERTO","IIA2_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 3",
        Field("IIA3_ACIERTO","IIA3_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 4",
        Field("IIA4_ACIERTO","IIA4_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 5",
        Field("IIA5_ACIERTO","IIA5_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 6",
        Field("IIA6_ACIERTO","IIA6_ERROR"),),

    Fieldset("B RAZONAMIENTO ESPACIAL TAREA 1 ",
        Field("IIB1_ACIERTO","IIB1_ERROR",)),

    Fieldset("B RAZONAMIENTO ESPACIAL TAREA 2 ",
        Field("IIB2_ACIERTO","IIB2_ERROR",)),

    Fieldset("C RAZONAMIENTO DEDUCTIVO ",
        Field("IIC1_ACIERTO","IIC1_ERROR",)),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A COMPRENSION LECTORA TAREA 1",
        Field("IVA1_ACIERTO","IVA1_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 2",
        Field("IVA2_ACIERTO","IVA2_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 3",
        Field("IVA3_ACIERTO","IVA3_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 4",
        Field("IVA4_ACIERTO","IVA4_ERROR",)),
    Fieldset("B COMPRENSIÓN LECTORA TAREA 5",
        Field("IVA5_ACIERTO","IVA5_ERROR",)),

    Fieldset("B EFICACIA LECTORA TAREA 5",
        Field("IVB1_ACIERTO","IVB1_ERROR",)),




    Fieldset("C VELOCIDAD LECTORA ",
        Field("IVC1_ACIERTO","IVC1_ERROR","IVC1_OMISION")),

    Fieldset("C VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)), ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A ORTOGRAFÍA VISUAL Y REGLADA TAREA 1 ",
        Field("VA1_ACIERTO","VA1_ERROR","VA1_OMISION")),
    Fieldset("A ORTOGRAFÍA VISUAL Y REGLADA TAREA 2 ",
        Field("VA2_ACIERTO","VA2_ERROR","VA2_OMISION")),
    Fieldset("A  DICTADO ",
        Field("VA3_ERROR",)),



    Fieldset("B EXPRESIÓN ESCRITA  ",
        Field("VB1")),


        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN",
       Field("VIA1_ACIERTO",)),

    ######

    Fieldset("B RESOLUCIÓN DE PROBLEMAS",
       Field("VIB1_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_08
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),


            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),

            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),

            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),

            "IIA4_ACIERTO":("Aciertos"),
            "IIA4_ERROR":("Errores"),

            "IIA5_ACIERTO":("Aciertos"),
            "IIA5_ERROR":("Errores"),

            "IIA6_ACIERTO":("Aciertos"),
            "IIA6_ERROR":("Errores"),


            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),
            ##########################

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),

            "IVA3_ACIERTO":("Aciertos"),
            "IVA3_ERROR":("Errores"),

            "IVA4_ACIERTO":("Aciertos"),
            "IVA4_ERROR":("Errores"),

            "IVA5_ACIERTO":("Aciertos"),
            "IVA5_ERROR":("Errores"),


            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),



############################################

            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),

            "IVC1_ACIERTO":("Aciertos"),
            "IVC1_ERROR":("Errores"),
            "IVC1_OMISION":("Omisiones"),


######
            # ESCRITURA

            "VA1_ACIERTO":("Aciertos"),
            "VA1_ERROR":("Errores"),
            "VA1_OMISION":("Omisiones"),

            "VA2_ACIERTO":("Aciertos"),
            "VA2_ERROR":("Errores"),
            "VA2_OMISION":("Omisiones"),

            "VA3_ERROR":("Errores"),



            "VB1": (""),


            # APRENDIZAJES MATEMATICOS

            "VIA1_ACIERTO":("Aciertos"),


            "VIB1_ACIERTO":("Aciertos"),



            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}

class FormEVA2_09(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_09,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> I ATENCIÓN CONCENTRACIÓN </p> """),

    Fieldset("",
        Field("I_ACIERTO","I_ERROR","I_OMISION")),



    HTML(""" <center>II  RAZONAMIENTO  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 1",
        Field("IIA1_ACIERTO","IIA1_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 2",
        Field("IIA2_ACIERTO","IIA2_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 3",
        Field("IIA3_ACIERTO","IIA3_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 4",
        Field("IIA4_ACIERTO","IIA4_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 5",
        Field("IIA5_ACIERTO","IIA5_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 6",
        Field("IIA6_ACIERTO","IIA6_ERROR"),),

    Fieldset("B RAZONAMIENTO ESPACIAL ÍTEM 1-7 ",
        Field("IIB1_ACIERTO","IIB1_ERROR",)),

    Fieldset("B RAZONAMIENTO ESPACIAL ÍTEM 8-9",
        Field("IIB2_ACIERTO","IIB2_ERROR",)),

    Fieldset("B RAZONAMIENTO ESPACIAL ÍTEM 10-20",
        Field("IIB3_ACIERTO","IIB3_ERROR",)),

    Fieldset("C RAZONAMIENTO DEDUCTIVO TAREA 1 ",
        Field("IIC1_ACIERTO","IIC1_ERROR",)),

    Fieldset("C RAZONAMIENTO DEDUCTIVO TAREA 2 ",
        Field("IIC2_ACIERTO","IIC2_ERROR",)),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A COMPRENSION LECTORA ",
        Field("IVA1_ACIERTO","IVA1_ERROR",)),


    Fieldset("B EFICACIA LECTORA",
        Field("IVB1_ACIERTO",)),




    Fieldset("C VELOCIDAD LECTORA ",
        Field("IVC1_ACIERTO","IVC1_ERROR","IVC1_OMISION")),

    Fieldset("C VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)), ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A ORTOGRAFÍA VISUAL Y REGLADA",
        Field("VA1_ACIERTO","VA1_ERROR","VA1_OMISION")),


    Fieldset("B EXPRESIÓN ESCRITA  ",
        Field("VB1")),


        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN",
       Field("VIA1_ACIERTO",)),

    ######

    Fieldset("B RESOLUCIÓN DE PROBLEMAS",
       Field("VIB1_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_09
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),


            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),


            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),

            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),

            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),

            "IIA4_ACIERTO":("Aciertos"),
            "IIA4_ERROR":("Errores"),

            "IIA5_ACIERTO":("Aciertos"),
            "IIA5_ERROR":("Errores"),

            "IIA6_ACIERTO":("Aciertos"),
            "IIA6_ERROR":("Errores"),


            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),

            "IIB3_ACIERTO":("Aciertos"),
            "IIB3_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),

            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),
            ##########################

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),


            "IVB1_ACIERTO":("Aciertos"),




############################################

            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),

            "IVC1_ACIERTO":("Aciertos"),
            "IVC1_ERROR":("Errores"),
            "IVC1_OMISION":("Omisiones"),


######
            # ESCRITURA

            "VA1_ACIERTO":("Aciertos"),
            "VA1_ERROR":("Errores"),
            "VA1_OMISION":("Omisiones"),


            "VB1": (""),


            # APRENDIZAJES MATEMATICOS

            "VIA1_ACIERTO":("Aciertos"),


            "VIB1_ACIERTO":("Aciertos"),



            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}




class FormEVA2_10(forms.ModelForm):
    def __init__(self, Institucion, *args, **kwargs):
        super(FormEVA2_10,self).__init__(*args, **kwargs)
        #self.fields['car'].queryset : Car.objects.filter(username:user)
        self.fields['Rut'].queryset = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")#funciona

        self.helper = FormHelper()
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
     ######## codigo para columnas y columna 1
    HTML(""" <center> """),#center I1
    Fieldset("",  #Seccion
    HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
    HTML("""  <p></p> """), #espacio

    Field("Rut","Semestre","Curso","Escolaridad","Fecha","sesiones","conducta","antecedentes")),

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
    HTML(""" <center> """),
    Fieldset("",
    Fieldset( "",#Seccion


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p> I ATENCIÓN CONCENTRACIÓN </p> """),

    Fieldset("",
        Field("I_ACIERTO","I_ERROR","I_OMISION")),



    HTML(""" <center>II  RAZONAMIENTO  </center> """),#Titulo
    HTML("""  <p></p> """),
    HTML(""" <center>  </center> """),
    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 1",
        Field("IIA1_ACIERTO","IIA1_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 2",
        Field("IIA2_ACIERTO","IIA2_ERROR"),),

    Fieldset("A RAZONAMIENTO INDUCTIVO TAREA 3",
        Field("IIA3_ACIERTO","IIA3_ERROR"),),


    Fieldset("B RAZONAMIENTO ESPACIAL ÍTEM 1-3 ",
        Field("IIB1_ACIERTO","IIB1_ERROR",)),

    Fieldset("B RAZONAMIENTO ESPACIAL ÍTEM 4-11",
        Field("IIB2_ACIERTO","IIB2_ERROR",)),


    Fieldset("C RAZONAMIENTO DEDUCTIVO ",
        Field("IIC1_ACIERTO","IIC1_ERROR",)),


    HTML(""" <center>  </center> """),#Titulo
    HTML("""  <p>IV LECTURA</p> """),
    Fieldset("A COMPRENSION LECTORA TAREA 1 ",
        Field("IVA1_ACIERTO","IVA1_ERROR",)),

    Fieldset("A COMPRENSION LECTORA TAREA 2 ",
        Field("IVA2_ACIERTO","IVA2_ERROR",)),

    Fieldset("A COMPRENSION LECTORA TAREA 3 ",
        Field("IVA3_ACIERTO","IVA3_ERROR",)),

    Fieldset("A COMPRENSION LECTORA TAREA 4 ",
        Field("IVA4_ACIERTO","IVA4_ERROR",)),



    Fieldset("B VELOCIDAD LECTORA ",
        Field("IVB1_ACIERTO","IVB1_ERROR","IVB1_OMISION")),

    Fieldset("B VELOCIDAD LECTORA TIEMPO",
        Field("TIEMPO_LECTURA",)), ),

    HTML(""" <center> """),#center
    ),




    HTML("""  </div> """), #fin columna uno
    HTML(""" </center> """),#center

    #////////////////////////////
    HTML(""" <center> """),#center
    HTML("""   <div class="column"  """), #inicio columna dos



    Fieldset("",#Seccion

     Fieldset("",#Seccion
     HTML(""" <center>V ESCRITURA </center> """),#Titulo
     HTML("""  <p></p> """),
    Fieldset("A ORTOGRAFÍA VISUAL Y REGLADA",
        Field("VA1_ACIERTO","VA1_ERROR","VA1_OMISION")),


    Fieldset("B EXPRESIÓN ESCRITA  ",
        Field("VB1")),


        ),

    Fieldset("",#Seccion
    HTML(""" <center> VI APRENDIZAJES MATEMATICOS </center> """),#Titulo
    HTML("""  <p></p> """),
    Fieldset("A CALCULO Y NUMERACIÓN",
       Field("VIA1_ACIERTO",)),

    ######

    Fieldset("B RESOLUCIÓN DE PROBLEMAS",
       Field("VIB1_ACIERTO",)),


          ),

     HTML("""  <p></p> """), #espacio
     HTML(""" </center> """),#center

     #fin codigo columnas
     HTML("""  </div>
                 </div>

                 </body>
                 </html>
                   """),

    HTML(""" <center> """),#center
    ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
    HTML(""" </center> """)),)#center


    class Meta():
        model = Modelo_EVALUA2_10
        exclude = ("user","Institucion")
        labels = {
            'Rut':('Estudiante'),
            "Semestre":("Número de evaluación"),

            "sesiones":("N° de sesiones"),
            "conducta":("Conducta observada"),
            "antecedentes":("Antecedentes relevantes"),

            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),


            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),

            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),

            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),



            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),

            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),

            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),
            ##########################

            "IVA1_ACIERTO":("Aciertos"),
            "IVA1_ERROR":("Errores"),

            "IVA2_ACIERTO":("Aciertos"),
            "IVA2_ERROR":("Errores"),

            "IVA3_ACIERTO":("Aciertos"),
            "IVA3_ERROR":("Errores"),

            "IVA4_ACIERTO":("Aciertos"),
            "IVA4_ERROR":("Errores"),






############################################

            "TIEMPO_LECTURA":("Tiempo lectura (seg)"),

            "IVB1_ACIERTO":("Aciertos"),
            "IVB1_ERROR":("Errores"),
            "IVB1_OMISION":("Omisiones"),


######
            # ESCRITURA

            "VA1_ACIERTO":("Aciertos"),
            "VA1_ERROR":("Errores"),
            "VA1_OMISION":("Omisiones"),


            "VB1": (""),


            # APRENDIZAJES MATEMATICOS

            "VIA1_ACIERTO":("Aciertos"),


            "VIB1_ACIERTO":("Aciertos"),



            }
        widgets : {"Escolaridad": forms.Textarea(attrs={"rows":1 ,"cols":4}),}
