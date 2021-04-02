from django.db import models
from datetime import datetime

class Modelo_Info_Pro(models.Model):


    Evaluador= models.CharField(max_length= 100, default= "")
    Registro_MINEDUC=models.CharField(max_length= 100, default= "")
    Rut_Pro=models.CharField(max_length= 20, default= "")
    Profesion=models.CharField(max_length= 100, default= "")
    user=models.CharField(max_length= 150,)
    Institucion =models.CharField(max_length= 150,default= "")

    class Meta:
        ordering = ["Institucion"]
 ###esto es esencial para los modelos y como se muestran
    def __str__(self):
        return '%s  %s  %s' % (self.Institucion, self.Evaluador, self.Rut_Pro)


############################################################################################
class  region(models.TextChoices):
    R_1= "Arica y Parinacota","Arica y Parinacota"
    R_2= "Tarapacá","Tarapacá"
    R_3= "Antofagasta","Antofagasta"
    R_4= "Atacama","Atacama"
    R_5= "Coquimbo","Coquimbo"
    R_6="Valparaíso", "Valparaíso"
    R_7="Metropolitana de Santiago", "Metropolitana de Santiago"
    R_8="Libertador General Bernardo O’Higgins","Libertador General Bernardo O’Higgins"
    R_9= "Maule", "Maule"
    R_10= "Ñuble", "Ñuble"
    R_11= "Biobío", "Biobío"
    R_12= "La Araucanía", "La Araucanía"
    R_13= "Los Ríos", "Los Ríos"
    R_14= "Los Lagos", "Los Lagos"
    R_15= "Aysén del General Carlos Ibáñez del Campo", "Aysén del General Carlos Ibáñez del Campo"
    R_16= "Magallanes y la Antártica Chilena", "Magallanes y la Antártica Chilena"


class  diagnostico(models.TextChoices):
    D_1= "Sin diagnóstico","Sin diagnóstico"
    D_2= "TDA","TDA"
    D_3= "TDAH","TDAH"
    D_4= "DEA","DEA"
    D_5= "DI","DI"
    D_6="FIL", "FIL"

############################################################################################
class Modelo_Info_Per(models.Model):
    Rut=models.CharField(max_length=10, unique= True)
    Nombres =models.CharField(max_length=50)
    Apellido_P =models.CharField(max_length=50,) #label= "Apellido paterno"
    Apellido_M =models.CharField(max_length=50, null=True, blank=True)
    Fecha_nac = models.DateField()

    telefono_estudiante = models.CharField(max_length=20, null=True, blank=True)
    correo_estudiante = models.CharField(max_length=20, null=True, blank=True)
    Id_genero =models.CharField(max_length=20, null=True, blank=True)
    diagnostico =models.CharField(max_length=50, choices=diagnostico.choices, default=diagnostico.D_1)
    salud= models.TextField(blank = True, null=True)
    socieco= models.TextField(blank = True, null=True)

    Observaciones =models.TextField(blank = True, null=True)

    Region_Domicilio1 = models.CharField(max_length= 50, choices=region.choices, default=region.R_7)
    Comuna_Domicilio1=models.CharField(max_length=50, null=True, blank=True)
    Direccion_Domicilio1 =models.CharField(max_length=50, null=True, blank=True)

    Region_Domicilio2 = models.CharField(max_length= 50, choices=region.choices, default=region.R_7)
    Comuna_Domicilio2=models.CharField(max_length=50, null=True, blank=True)
    Direccion_Domicilio2=models.CharField(max_length=50, null=True, blank=True)

    Nombre_apoderado1 =models.CharField(max_length=100, null=True, blank=True)
    telefono_apoderado1 = models.CharField(max_length=20, null=True, blank=True)
    correo_apoderado1 = models.CharField(max_length=30, null=True, blank=True)

    Nombre_apoderado2 =models.CharField(max_length=100, null=True, blank=True)
    telefono_apoderado2 = models.CharField(max_length=20, null=True, blank=True)
    correo_apoderado2 = models.CharField(max_length=30, null=True, blank=True)

    Nombre_apoderado3 =models.CharField(max_length=100, null=True, blank=True)
    telefono_apoderado3 = models.CharField(max_length=20, null=True, blank=True)
    correo_apoderado3 = models.CharField(max_length=30, null=True, blank=True)





    user=models.CharField(max_length= 150,)
    Institucion =models.CharField(max_length= 150,default= "")




    class Meta:
        ordering = ["Apellido_P"]
 ###esto es esencial para los modelos y como se muestran
    def __str__(self):
        return '%s -- %s %s %s, %s' % (self.Institucion, self.Apellido_P, self.Apellido_M, self.Nombres, self.Rut)

    def get_absolute_url(self):
        return f"/estudiante/{self.Rut }/"

#############################################################################################
#############################################################################################
############################################

#############################################
class  ITEM_VB(models.TextChoices):
    VB_1= "1","Composición escrita superior a lo que es propia del nivel escolar."
    VB_2= "2","Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
    VB_3= "3","Composición acorde al nivel escolar."
    VB_4= "4","Composición inferior a lo esperado acorde al nivel escolar."
    VB_5= "5","Composición con abundantes errores, no logra expresarse."

#     EVALUA_11 = "E11","Evalua 11"
#     EVALUA_10 = "E10","Evalua 10"
#     EVALUA_09 = "E09","Evalua 09"
#     EVALUA_08 = "E08","Evalua 08"
#     EVALUA_07 = "E07","Evalua 07"

def semestre():
    M =datetime.now().month
    if M <= 6:
        S=1
    else:
        S=2
    return S

class Modelo_EVALUA_08(models.Model):
    #user= models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="user")
    Institucion =models.CharField(max_length= 150,default= "")
    user =models.CharField(max_length= 250,)# defult =request.user.username)

    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
    #agrega limit_choices_to

    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)
    #Evaluador= models.TextField(max_length= 100, default= "Carlos Diego Riquelme González")
    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #PUNTAJE
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)
    IIA1_OMISION= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)
    IIA2_OMISION= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)
    IIA3_OMISION= models.IntegerField(default=0)

    IIA4_ACIERTO= models.IntegerField(default=0)
    IIA4_ERROR= models.IntegerField(default=0)
    IIA4_OMISION= models.IntegerField(default=0)

    IIA5_ACIERTO= models.IntegerField(default=0)
    IIA5_ERROR= models.IntegerField(default=0)
    IIA5_OMISION= models.IntegerField(default=0)

    IIA6_ACIERTO= models.IntegerField(default=0)
    IIA6_ERROR= models.IntegerField(default=0)
    IIA6_OMISION= models.IntegerField(default=0)

    #II RAZONAMIENTO B. ESPACIAL
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)
    IIB1_OMISION= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)
    IIB2_OMISION= models.IntegerField(default=0)

    #
    #II RAZONAMIENTO C. DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)
    IIC1_OMISION= models.IntegerField(default=0)


    # IV LECTURA A COMPRENSION
    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)
    IVA1_OMISION= models.IntegerField(default=0)

    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)
    IVA2_OMISION= models.IntegerField(default=0)

    IVA3_ACIERTO= models.IntegerField(default=0)
    IVA3_ERROR= models.IntegerField(default=0)
    IVA3_OMISION= models.IntegerField(default=0)

    IVA4_ACIERTO= models.IntegerField(default=0)
    IVA4_ERROR= models.IntegerField(default=0)
    IVA4_OMISION= models.IntegerField(default=0)

    IVA5_ACIERTO= models.IntegerField(default=0)
    IVA5_ERROR= models.IntegerField(default=0)
    IVA5_OMISION= models.IntegerField(default=0)


    # IV LECTURA B EFICACIA
    IVB_ACIERTO= models.IntegerField(default=0)
    IVB_ERROR= models.IntegerField(default=0)
    IVB_OMISION= models.IntegerField(default=0)
    #
    # IV LECTURA C VELOCIDAD
    IVC_ACIERTO= models.IntegerField(default=0)
    IVC_ERROR= models.IntegerField(default=0)
    IVC_OMISION= models.IntegerField(default=0)
    #
    #
    # V ESCRITURA A. ORTOGRAFIA
    # PUNTAJE V.A
    VA_ACIERTO= models.IntegerField(default=0)
    VA_ERROR= models.IntegerField(default=0)
    VA_OMISION= models.IntegerField(default=0)
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
    V = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #
    # PUNTAJE VI.A
    #VI APREND MATEMATICOS A CAL&NUM
    #ACIERTO	ERROR	OMISION
    VIA_ACIERTO= models.IntegerField(default=0)
    VIA_ERROR= models.IntegerField(default=0)
    VIA_OMISION= models.IntegerField(default=0)
    #PUNTAJE VI.B
    #VI APREND MATEMATICOS B RESOLUC

    VIB_ACIERTO= models.IntegerField(default=0)
    VIB_ERROR= models.IntegerField(default=0)
    VIB_OMISION= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E08/{self.pk}/"

####################################
class Modelo_EVALUA_09(models.Model):
    #user= models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="user")
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
    #agrega limit_choices_to

    Semestre = models.IntegerField( default = semestre)

    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)
    #Evaluador= models.TextField(max_length= 100, default= "Carlos Diego Riquelme González")
    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #PUNTAJE IIA1-IIA6 desagregado
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)
    IIA1_OMISION= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)
    IIA2_OMISION= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)
    IIA3_OMISION= models.IntegerField(default=0)

    IIA4_ACIERTO= models.IntegerField(default=0)
    IIA4_ERROR= models.IntegerField(default=0)
    IIA4_OMISION= models.IntegerField(default=0)

    IIA5_ACIERTO= models.IntegerField(default=0)
    IIA5_ERROR= models.IntegerField(default=0)
    IIA5_OMISION= models.IntegerField(default=0)

    IIA6_ACIERTO= models.IntegerField(default=0)
    IIA6_ERROR= models.IntegerField(default=0)
    IIA6_OMISION= models.IntegerField(default=0)

    #II RAZONAMIENTO B. ESPACIAL
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)
    IIB1_OMISION= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)
    IIB2_OMISION= models.IntegerField(default=0)

    IIB3_ACIERTO= models.IntegerField(default=0)
    IIB3_ERROR= models.IntegerField(default=0)
    IIB3_OMISION= models.IntegerField(default=0)
    #
    #II RAZONAMIENTO C. DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)
    IIC1_OMISION= models.IntegerField(default=0)

    #PUNTAJE IIC2
    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)
    IIC2_OMISION= models.IntegerField(default=0)
    # IV LECTURA A COMPRENSION
    IVA_ACIERTO= models.IntegerField(default=0)
    IVA_ERROR= models.IntegerField(default=0)
    IVA_OMISION= models.IntegerField(default=0)
    #
    # IV LECTURA B EFICACIA
    IVB_ACIERTO= models.IntegerField(default=0)
    IVB_ERROR= models.IntegerField(default=0)
    IVB_OMISION= models.IntegerField(default=0)
    #
    # IV LECTURA C VELOCIDAD
    IVC_ACIERTO= models.IntegerField(default=0)
    IVC_ERROR= models.IntegerField(default=0)
    IVC_OMISION= models.IntegerField(default=0)
    #
    #
    # V ESCRITURA A. ORTOGRAFIA
    # PUNTAJE V.A
    VA_ACIERTO= models.IntegerField(default=0)
    VA_ERROR= models.IntegerField(default=0)
    VA_OMISION= models.IntegerField(default=0)
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
    V = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #
    # PUNTAJE VI.A
    #VI APREND MATEMATICOS A CAL&NUM
    #ACIERTO	ERROR	OMISION
    VIA_ACIERTO= models.IntegerField(default=0)
    VIA_ERROR= models.IntegerField(default=0)
    VIA_OMISION= models.IntegerField(default=0)
    #PUNTAJE VI.B
    #VI APREND MATEMATICOS B RESOLUC

    VIB_ACIERTO= models.IntegerField(default=0)
    VIB_ERROR= models.IntegerField(default=0)
    VIB_OMISION= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E09/{self.pk}/"

##################################

class Modelo_EVALUA_10(models.Model):
    #user= models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="user")
    Institucion =models.CharField(max_length= 150,default= "")
    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
    #agrega limit_choices_to

    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)
    #Evaluador= models.TextField(max_length= 100, default= "Carlos Diego Riquelme González")
    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #PUNTAJE IIA1-IIA3 desagregado
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)
    IIA1_OMISION= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)
    IIA2_OMISION= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)
    IIA3_OMISION= models.IntegerField(default=0)



    #II RAZONAMIENTO B. ESPACIAL
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)
    IIB1_OMISION= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)
    IIB2_OMISION= models.IntegerField(default=0)

    #
    #II RAZONAMIENTO C. DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)
    IIC1_OMISION= models.IntegerField(default=0)

    #PUNTAJE IIC2
    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)
    IIC2_OMISION= models.IntegerField(default=0)

    # IV LECTURA A COMPRENSION
    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)
    IVA1_OMISION= models.IntegerField(default=0)
    #
    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)
    IVA2_OMISION= models.IntegerField(default=0)

    IVA3_ACIERTO= models.IntegerField(default=0)
    IVA3_ERROR= models.IntegerField(default=0)
    IVA3_OMISION= models.IntegerField(default=0)

    IVA4_ACIERTO= models.IntegerField(default=0)
    IVA4_ERROR= models.IntegerField(default=0)
    IVA4_OMISION= models.IntegerField(default=0)


    # IV LECTURA B VELOCIDAD
    IVB_ACIERTO= models.IntegerField(default=0)
    IVB_ERROR= models.IntegerField(default=0)
    IVB_OMISION= models.IntegerField(default=0)
    #
        #
    # V ESCRITURA A. ORTOGRAFIA
    # PUNTAJE V.A
    VA_ACIERTO= models.IntegerField(default=0)
    VA_ERROR= models.IntegerField(default=0)
    VA_OMISION= models.IntegerField(default=0)
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
    V = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #
    # PUNTAJE VI.A
    #VI APREND MATEMATICOS A CAL&NUM
    #ACIERTO	ERROR	OMISION
    VIA_ACIERTO= models.IntegerField(default=0)
    VIA_ERROR= models.IntegerField(default=0)
    VIA_OMISION= models.IntegerField(default=0)
    #PUNTAJE VI.B
    #VI APREND MATEMATICOS B RESOLUC

    VIB_ACIERTO= models.IntegerField(default=0)
    VIB_ERROR= models.IntegerField(default=0)
    VIB_OMISION= models.IntegerField(default=0)



    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E10/{self.pk}/"



#VERSION 2.0

#

class Modelo_EVALUA2_00(models.Model): #LISTO :)


    Institucion =models.CharField(max_length= 150,default= "")
    user =models.CharField(max_length= 250,)# defult =request.user.username)

    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)


    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)
    #I CAPACIDADES COGNITIVAS
    #A CLASIFICACION
    IA1_ACIERTO= models.IntegerField(default=0)
    IA1_ERROR= models.IntegerField(default=0)
    IA1_OMISION= models.IntegerField(default=0)

    IA2_ACIERTO= models.IntegerField(default=0)
    IA2_ERROR= models.IntegerField(default=0)
    IA2_OMISION= models.IntegerField(default=0)

    # SERIES
    IB1_ACIERTO= models.IntegerField(default=0)
    IB1_ERROR= models.IntegerField(default=0)
    IB1_OMISION= models.IntegerField(default=0)

    IB2_ACIERTO= models.IntegerField(default=0)
    IB2_ERROR= models.IntegerField(default=0)
    IB2_OMISION= models.IntegerField(default=0)

    IB3_ACIERTO= models.IntegerField(default=0)
    IB3_ERROR= models.IntegerField(default=0)
    IB3_OMISION= models.IntegerField(default=0)

    #ORGANIZACION PERCEPTIVA
    #PUZZLES

    IC1_ERROR= models.IntegerField(default=0)
    IC1_OMISION= models.IntegerField(default=0)

    IC2_ERROR= models.IntegerField(default=0)
    IC2_OMISION= models.IntegerField(default=0)

    IC3_ERROR= models.IntegerField(default=0)
    IC3_OMISION= models.IntegerField(default=0)

    IC4_ERROR= models.IntegerField(default=0)
    IC4_OMISION= models.IntegerField(default=0)


    #LETRAS Y NUMEROS

    ID1_ACIERTO= models.IntegerField(default=0)
    ID1_ERROR= models.IntegerField(default=0)
    ID1_OMISION= models.IntegerField(default=0)

    ID2_ACIERTO= models.IntegerField(default=0)
    ID2_ERROR= models.IntegerField(default=0)
    ID2_OMISION= models.IntegerField(default=0)


    #MEMORIA VERBAL

    IE1_ACIERTO= models.IntegerField(default=0)


    IE2_ACIERTO= models.IntegerField(default=0)


    #II CAPACIDADES ESPACIALES
    # A COPIA DE DIBUJOS
    IIA1_ACIERTO= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)


    #B GRAFOMOTRICIDAD

    IIB1_ERROR= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)
    IIB3_ERROR= models.IntegerField(default=0)
    IIB4_ERROR= models.IntegerField(default=0)
    IIB5_ERROR= models.IntegerField(default=0)
    IIB6_ERROR= models.IntegerField(default=0)

    #III CAPACIDADES LINGÜISTICAS
    #A PALABRAS Y FRASES
    IIIA1_ACIERTO= models.IntegerField(default=0)

    # B RECEPTCION AUDITA Y ARTICULACION

    IIIB1_ACIERTO= models.IntegerField(default=0)
    IIIB2_ACIERTO= models.IntegerField(default=0)
    IIIB3_ACIERTO= models.IntegerField(default=0)


    # C HABILIDADES FONOLÓGICAS

    IIIC1_ACIERTO= models.IntegerField(default=0)
    IIIC2_ACIERTO= models.IntegerField(default=0)
    IIIC3_ACIERTO= models.IntegerField(default=0)
    IIIC4_ACIERTO= models.IntegerField(default=0)

    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_00/{self.pk}/"

class  ITEM_VB01(models.TextChoices):
    VB_1= "1","No posee errores ni conductas inadecaudas."
    VB_2= "2","Posee pocos errores, nada relevantes al proceso escribano."
    VB_3= "3","Errores acorde al nivel escolar."
    VB_4= "4","Abundantes errores, inferior al nivel escolar."
    VB_5= "5","Todo tipo de errores, prácticamente incapaz de escribir."

class  ITEM_IVB01(models.TextChoices):
    IVB_1= "1","No posee errores ni conductas inadecaudas."
    IVB_2= "2","Posee pocos errores, nada relevantes al proceso de lectura."
    IVB_3= "3","Errores acorde al nivel escolar."
    IVB_4= "4","Abundantes errores, inferior al nivel escolar."
    IVB_5= "5","Todo tipo de errores, prácticamente incapaz de leer."

class Modelo_EVALUA2_01(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I BASES DEL RAZONAMIENTO
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    ##
    #II BASES DEL RAZONAMIENTO
    #IIA SERIES
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)

    #IIB CLASIFICACIONES
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)

    #IIC ORGANIZACION PRECEPTIVA

    IIC1_ACIERTO= models.IntegerField(default=0)
    ##
    #IV LECTURA
    #IVA COMPRENSIÓN LECTORA

    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)
    IVA1_OMISION= models.IntegerField(default=0)

    IVA2_ACIERTO= models.IntegerField(default=0)

    IVA3_ACIERTO= models.IntegerField(default=0)

    #IVB EXACTITUD LECTORA
    IVB1_ACIERTO= models.IntegerField(default=0)
    #V ESCRITURA
    #VA ORTOFONÉTICA
    VA1_ACIERTO= models.IntegerField(default=0)
    VA2_ACIERTO= models.IntegerField(default=0)
    VA3_ACIERTO= models.IntegerField(default=0)
    #VB GRAFÍA Y EXP ESCRITA
    VB = models.CharField(max_length= 1, choices=ITEM_VB01.choices, default=ITEM_VB.VB_1)
    #VC ORTOGRAFÍA VISUAL
    VC1_ACIERTO= models.IntegerField(default=0)
    #VI APRENDIZAJES MATEMATICOS
    #VIA CALCULO Y NUMERACIÓN
    VIA1_ACIERTO= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_01/{self.pk}/"

class Modelo_EVALUA2_02(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

#I BASES DEL RAZONAMIENTO
    #IA PENSAMIENTO ANALÓGICO
    IA1_ACIERTO= models.IntegerField(default=0)
    IA1_ERROR= models.IntegerField(default=0)


    #IB ORGANIZACIÓN PERCEPTIVA
    IB1_ACIERTO= models.IntegerField(default=0)
    IB1_ERROR= models.IntegerField(default=0)

    #IC CLASIFICACIONES
    IC1_ACIERTO= models.IntegerField(default=0)
    IC1_ERROR= models.IntegerField(default=0)

    IC2_ACIERTO= models.IntegerField(default=0)
    IC2_ERROR= models.IntegerField(default=0)


    #II MEMORIA Y ATENCION

    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)
    IIA1_OMISION=models.IntegerField(default=0)
    #IIB CLASIFICACIONES

    #IV LECTURA
    #IVA COMPRENSIÓN LECTORA

    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)

    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)

    IVA3_ACIERTO= models.IntegerField(default=0)

    #IVB EXACTITUD LECTORA
    IVB = models.CharField(max_length= 1, choices=ITEM_IVB01.choices, default=ITEM_IVB01.IVB_1)


    #
    # V ESCRITURA
    #A. ORTOGRAFIA
    # PUNTAJE V.A

    VA = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #

    VB1_ACIERTO= models.IntegerField(default=0)
    VB2_ERROR= models.IntegerField(default=0)

    #VI APREND MATEMATICOS
    #CÁLCULO Y NUMERACIÓN

    VIA1_ACIERTO= models.IntegerField(default=0)
    VIA2_ACIERTO= models.IntegerField(default=0)
    VIA2_ERROR= models.IntegerField(default=0)

    VIB1_ACIERTO= models.IntegerField(default=0)



    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_02/{self.pk}/"
#####################################################
class Modelo_EVALUA2_03(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I MEMORIA Y ATENCIÓN
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    # BASES DEL RAZONAMIENTO
    #A REFLEXIBIDAD

    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)


    #IIB PENSAMIENTO ANALÓGICO

    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)


    #IIC ORGANIZACION PERCEPTIVA
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)

    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)


    # IV LECTURA
    # A COMPRENSIÓN LECTORA
    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)


    # IV EXACTITUD LECTORA
    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR= models.IntegerField(default=0)

    IVB2_ACIERTO= models.IntegerField(default=0)
    #

    # V ESCRITURA

    #A ORTOFONÉTICA
    # PUNTAJE V.A
    VA1_ACIERTO= models.IntegerField(default=0)

    #B GRAFÍA Y EXPRESIÓN ESCRITA
    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)

    #C ORTOGRAFÍA VISUAL Y REGLADA

    VC1_ACIERTO= models.IntegerField(default=0)
    VC1_ERROR= models.IntegerField(default=0)

    # ESCRITURA DE PALABRAS
    VC2_ACIERTO= models.IntegerField(default=0)
    VC2_ERROR= models.IntegerField(default=0)
    VC2_OMISION= models.IntegerField(default=0)

    #DICTADO

    VC3_ERROR= models.IntegerField(default=0)


    #VI APREND MATEMATICOS
    # CALCULO Y NUMERACIÓN
    VIA1_ACIERTO= models.IntegerField(default=0)

    #B RESOLUCIÓN DE PROBLEMAS
    #ITEM 1-15
    VIB1_ACIERTO= models.IntegerField(default=0)
    #ITEM 16
    VIB2_ACIERTO= models.IntegerField(default=0)

    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_03/{self.pk}/"

class Modelo_EVALUA2_04(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)


    #I MEMORIA Y ATENCIÓN
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    # BASES DEL RAZONAMIENTO
    #A REFLEXIBIDAD
    #TAREA1
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)


    #IIB PENSAMIENTO ANALÓGICO
    #TAREA2
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)
    #TAREA3
    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)

    #IIC ORGANIZACION PERCEPTIVA
    #TAREA4
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)
    #TAREA5
    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)


    # IV LECTURA
    # A COMPRENSIÓN LECTORA
    # ITEM 1-17
    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)
    # ITEM 18-33
    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)

    # IV VELOCIDAD LECTORA
    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR= models.IntegerField(default=0)
    IVB1_OMISION =models.IntegerField(default=0)
    TIEMPO_LECTURA =models.IntegerField(default=130)

    # V ESCRITURA

    #A ORTOGRAFIA Y REGLADA
    # A1 DICTADO
    VA1_ERROR= models.IntegerField(default=0)
    # RECONOCIMIENTO
    VA2_ACIERTO= models.IntegerField(default=0)
    VA2_ERROR= models.IntegerField(default=0)
    VA2_OMISION =models.IntegerField(default=0)

    #B GRAFÍA Y EXPRESIÓN ESCRITA
    #GRAFISMO
    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #ORTOGRAFÍA
    VB2 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)

    #VI APREND MATEMATICOS
    # CALCULO Y NUMERACIÓN
    #SERIES Y NUMERACION
    VIA1_ACIERTO= models.IntegerField(default=0)
    #ESCRITURA, DESCOMPOSICIÓN Y OPERACIONES
    VIA2_ACIERTO= models.IntegerField(default=0)
    # FRACCIONES
    VIA3_ACIERTO= models.IntegerField(default=0)
    VIA3_ERROR= models.IntegerField(default=0)

    #B RESOLUCIÓN DE PROBLEMAS
    VIB1_ACIERTO= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_04/{self.pk}/"

class Modelo_EVALUA2_05(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I MEMORIA Y ATENCIÓN
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    # BASES DEL RAZONAMIENTO
    #A REFLEXIBIDAD
    #TAREA1
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)


    #IIB PENSAMIENTO ANALÓGICO
    #TAREA2
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)

    #IIC ORGANIZACION PERCEPTIVA
    #TAREA4
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)


    # IV LECTURA
    # A COMPRENSIÓN LECTORA
    # ITEM 1-17
    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)
    IVA1_OMISION= models.IntegerField(default=0)
    # IV VELOCIDAD LECTORA
    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR= models.IntegerField(default=0)
    IVB1_OMISION =models.IntegerField(default=0)
    TIEMPO_LECTURA =models.IntegerField(default=130)

    IVC1_ACIERTO= models.IntegerField(default=0)
    IVC1_ERROR= models.IntegerField(default=0)
    IVC1_OMISION =models.IntegerField(default=0)

    IVC2_ACIERTO= models.IntegerField(default=0)
    IVC2_ERROR= models.IntegerField(default=0)
    IVC2_OMISION =models.IntegerField(default=0)

    # V ESCRITURA

    #A ORTOGRAFIA Y REGLADA
    # A DICTADO PALABRAS
    VA1_ACIERTO= models.IntegerField(default=0)
    # DICTADO FRASES
    VA2_ACIERTO= models.IntegerField(default=0)


    #B GRAFÍA Y EXPRESIÓN ESCRITA

    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)

    #C ORTOGRAFÍA VISUAL Y REGLADA
    #T1

    VC1_ACIERTO =models.IntegerField(default=0)
    VC1_ERROR=models.IntegerField(default=0)
    VC1_OMISION=models.IntegerField(default=0)
    #T2
    VC2_ERROR=models.IntegerField(default=0)


    #VI APREND MATEMATICOS
    # A CALCULO Y NUMERACIÓN
    #ITEM 1Y2
    VIA1_ACIERTO =models.IntegerField(default=0)
    VIA1_ERROR=models.IntegerField(default=0)
    VIA1_OMISION=models.IntegerField(default=0)

    #ITEM 3
    VIA2_ACIERTO =models.IntegerField(default=0)
    #ITEM 4
    VIA3_ACIERTO =models.IntegerField(default=0)
    #ITEM 5
    VIA4_ACIERTO =models.IntegerField(default=0)

    #B RESOLUCIÓN DE PROBLEMAS
    #PROB 1-5
    VIB1_ACIERTO= models.IntegerField(default=0)
    #PROB 6-12
    VIB2_ACIERTO= models.IntegerField(default=0)




    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_05/{self.pk}/"


class Modelo_EVALUA2_06(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)


    #I BASES DEL RAZONAMIENTO
    #A REFLEXIBIDAD
    #TAREA1
    IA1_ACIERTO= models.IntegerField(default=0)
    IA1_ERROR= models.IntegerField(default=0)


    #IB PENSAMIENTO ANALÓGICO
    #TAREA2
    IB1_ACIERTO= models.IntegerField(default=0)
    IB1_ERROR= models.IntegerField(default=0)

    #IC ORGANIZACION PERCEPTIVA
    #TAREA4
    IC1_ACIERTO= models.IntegerField(default=0)
    IC1_ERROR= models.IntegerField(default=0)

    IC2_ACIERTO= models.IntegerField(default=0)
    IC2_ERROR= models.IntegerField(default=0)

    #II MEMORIIA Y ATENCIIÓN
    II_ACIERTO= models.IntegerField(default=0)
    II_ERROR= models.IntegerField(default=0)
    II_OMISION= models.IntegerField(default=0)

    # IV LECTURA
    # A COMPRENSIÓN LECTORA
    #1-5
    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)
    #6-10
    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)
    #1-9
    IVA3_ACIERTO= models.IntegerField(default=0)
    IVA3_ERROR= models.IntegerField(default=0)
    #10-14
    IVA4_ACIERTO= models.IntegerField(default=0)
    IVA4_ERROR= models.IntegerField(default=0)

    IVA5_ACIERTO= models.IntegerField(default=0)
    IVA5_ERROR= models.IntegerField(default=0)





    # IV VELOCIDAD LECTORA
    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR= models.IntegerField(default=0)
    IVB1_OMISION =models.IntegerField(default=0)
    TIEMPO_LECTURA =models.IntegerField(default=130)

    # V ESCRITURA

    #A ORTOGRAFIA Y REGLADA
    # A DICTADO PALABRAS
    VA1_ACIERTO= models.IntegerField(default=0)
    # RECONOCIMIENTO ORTOGRAFICO
    VA2_ACIERTO= models.IntegerField(default=0)
    VA2_ERROR= models.IntegerField(default=0)
    VA2_OMISION =models.IntegerField(default=0)


    #B GRAFISMO Y ORTOGRAFÍA FONETICA

    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    VB2 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)

    #VI APREND MATEMATICOS
    # A CALCULO Y NUMERACIÓN
    #1-9
    VIA1_ACIERTO =models.IntegerField(default=0)
    VIA1_ERROR=models.IntegerField(default=0)


    #10-12
    VIA2_ACIERTO =models.IntegerField(default=0)

    #13-35
    VIA3_ACIERTO =models.IntegerField(default=0)
    VIA3_ERROR=models.IntegerField(default=0)


    #B RESOLUCIÓN DE PROBLEMAS
    #PROB 1-5
    VIB1_ACIERTO= models.IntegerField(default=0)



    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_06/{self.pk}/"


class Modelo_EVALUA2_07(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")

    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    # BASES DEL RAZONAMIENTO
    #A DEDUCTIVO
    #TAREA1
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)

    #IIB  INDUCTIVO
    #TAREA2
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)

    #IIC  ESPACIAL
    #TAREA4
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)

    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)

    # IV LECTURA
    # A COMPRENSIÓN LECTORA
    # ITEM 1-17
    IVA1_ACIERTO= models.IntegerField(default=0)

    # IV VELOCIDAD LECTORA
    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR= models.IntegerField(default=0)

    IVB2_ACIERTO= models.IntegerField(default=0)
    IVB2_ERROR= models.IntegerField(default=0)

    IVB3_ACIERTO= models.IntegerField(default=0)
    IVB3_ERROR= models.IntegerField(default=0)

    IVB4_ACIERTO= models.IntegerField(default=0)
    IVB4_ERROR= models.IntegerField(default=0)

    IVC1_ACIERTO= models.IntegerField(default=0)
    IVC1_ERROR=  models.IntegerField(default=0)
    IVC1_OMISION= models.IntegerField(default=0)

    TIEMPO_LECTURA =models.IntegerField(default=130)

    # V ESCRITURA

    #A ORTOGRAFIA Y REGLADA
    # A DICTADO PALABRAS
    VA1_ACIERTO= models.IntegerField(default=0)

    #B GRAFÍA Y EXPRESIÓN ESCRITA

    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #C ORTOGRAFÍA VISUAL Y REGLADA
    #
    VC1_ACIERTO =models.IntegerField(default=0)
    VC1_ERROR=models.IntegerField(default=0)
    VC1_OMISION=models.IntegerField(default=0)
    #T2
    VC2_ACIERTO =models.IntegerField(default=0)
    VC2_ERROR=models.IntegerField(default=0)
    VC2_OMISION=models.IntegerField(default=0)


    #VI APREND MATEMATICOS
    # A CALCULO Y NUMERACIÓN
    #ITEM 1Y2
    VIA1_ACIERTO =models.IntegerField(default=0)


    #B RESOLUCIÓN DE PROBLEMAS
    #PROB 1-5
    VIB1_ACIERTO= models.IntegerField(default=0)
    #PROB 6-12
    VIB2_ACIERTO= models.IntegerField(default=0)




    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_07/{self.pk}/"


class Modelo_EVALUA2_08(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")
    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #  RAZONAMIENTO
    #A INDUCTIVO
    #TAREA1
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)

    IIA4_ACIERTO= models.IntegerField(default=0)
    IIA4_ERROR= models.IntegerField(default=0)

    IIA5_ACIERTO= models.IntegerField(default=0)
    IIA5_ERROR= models.IntegerField(default=0)

    IIA6_ACIERTO= models.IntegerField(default=0)
    IIA6_ERROR= models.IntegerField(default=0)

    #IIB  ESPACIAL
    #TAREA1
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)

    #IIC  DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)

    # IV LECTURA
    # A COMPRENSIÓN LECTORA


    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)

    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)

    IVA3_ACIERTO= models.IntegerField(default=0)
    IVA3_ERROR= models.IntegerField(default=0)

    IVA4_ACIERTO= models.IntegerField(default=0)
    IVA4_ERROR= models.IntegerField(default=0)

    IVA5_ACIERTO= models.IntegerField(default=0)
    IVA5_ERROR= models.IntegerField(default=0)

    #B EFICACIA LECTORA

    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR= models.IntegerField(default=0)

    # IV VELOCIDAD LECTORA



    IVC1_ACIERTO= models.IntegerField(default=0)
    IVC1_ERROR=  models.IntegerField(default=0)
    IVC1_OMISION= models.IntegerField(default=0)

    TIEMPO_LECTURA =models.IntegerField(default=130)

    # V ESCRITURA

    #A ORTOGRAFIA VISUAL  Y REGLADA
    # A DICTADO PALABRAS

    VA1_ACIERTO= models.IntegerField(default=0)
    VA1_ERROR=  models.IntegerField(default=0)
    VA1_OMISION= models.IntegerField(default=0)

    VA2_ACIERTO= models.IntegerField(default=0)
    VA2_ERROR=  models.IntegerField(default=0)
    VA2_OMISION= models.IntegerField(default=0)

    VA3_ERROR= models.IntegerField(default=0)

    #B EXPRESIÓN ESCRITA

    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)



    #VI APREND MATEMATICOS
    # A CALCULO Y NUMERACIÓN
    VIA1_ACIERTO =models.IntegerField(default=0)


    #B RESOLUCIÓN DE PROBLEMAS
    VIB1_ACIERTO= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_08/{self.pk}/"


class Modelo_EVALUA2_09(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")
    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #  RAZONAMIENTO
    #A INDUCTIVO
    #TAREA1
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)

    IIA4_ACIERTO= models.IntegerField(default=0)
    IIA4_ERROR= models.IntegerField(default=0)

    IIA5_ACIERTO= models.IntegerField(default=0)
    IIA5_ERROR= models.IntegerField(default=0)

    IIA6_ACIERTO= models.IntegerField(default=0)
    IIA6_ERROR= models.IntegerField(default=0)

    #IIB  ESPACIAL
    #TAREA1
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)

    IIB3_ACIERTO= models.IntegerField(default=0)
    IIB3_ERROR= models.IntegerField(default=0)

    #IIC  DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)

    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)

    # IV LECTURA
    # A COMPRENSIÓN LECTORA


    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)

    #B EFICACIA LECTORA

    IVB1_ACIERTO= models.IntegerField(default=0)

    # IV VELOCIDAD LECTORA



    IVC1_ACIERTO= models.IntegerField(default=0)
    IVC1_ERROR=  models.IntegerField(default=0)
    IVC1_OMISION= models.IntegerField(default=0)

    TIEMPO_LECTURA =models.IntegerField(default=130)

    # V ESCRITURA

    #A ORTOGRAFIA VISUAL  Y REGLADA
    # A DICTADO PALABRAS

    VA1_ACIERTO= models.IntegerField(default=0)
    VA1_ERROR=  models.IntegerField(default=0)
    VA1_OMISION= models.IntegerField(default=0)

    #B EXPRESIÓN ESCRITA

    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)



    #VI APREND MATEMATICOS
    # A CALCULO Y NUMERACIÓN
    VIA1_ACIERTO =models.IntegerField(default=0)


    #B RESOLUCIÓN DE PROBLEMAS
    VIB1_ACIERTO= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_09/{self.pk}/"


class Modelo_EVALUA2_10(models.Model):
    Institucion =models.CharField(max_length= 150,default= "")
    user =models.CharField(max_length= 250,)# defult =request.user.username)
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")


    Semestre = models.IntegerField( default = semestre)


    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)

    sesiones=models.IntegerField(default=1)
    conducta=models.TextField(max_length= 1000,null=True, blank=True)
    antecedentes=models.TextField(max_length= 1000,null=True, blank=True)

    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #  RAZONAMIENTO
    #A INDUCTIVO
    #TAREA1
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)


    #IIB  ESPACIAL
    #TAREA1
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)

    #IIC  DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)

    # IV LECTURA
    # A COMPRENSIÓN LECTORA


    IVA1_ACIERTO= models.IntegerField(default=0)
    IVA1_ERROR= models.IntegerField(default=0)

    IVA2_ACIERTO= models.IntegerField(default=0)
    IVA2_ERROR= models.IntegerField(default=0)

    IVA3_ACIERTO= models.IntegerField(default=0)
    IVA3_ERROR= models.IntegerField(default=0)

    IVA4_ACIERTO= models.IntegerField(default=0)
    IVA4_ERROR= models.IntegerField(default=0)



    # IV VELOCIDAD LECTORA



    IVB1_ACIERTO= models.IntegerField(default=0)
    IVB1_ERROR=  models.IntegerField(default=0)
    IVB1_OMISION= models.IntegerField(default=0)

    TIEMPO_LECTURA =models.IntegerField(default=130)

    # V ESCRITURA

    #A ORTOGRAFIA VISUAL  Y REGLADA

    VA1_ACIERTO= models.IntegerField(default=0)
    VA1_ERROR=  models.IntegerField(default=0)
    VA1_OMISION= models.IntegerField(default=0)

    #B EXPRESIÓN ESCRITA

    VB1 = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)



    #VI APREND MATEMATICOS
    # A CALCULO Y NUMERACIÓN
    VIA1_ACIERTO =models.IntegerField(default=0)


    #B RESOLUCIÓN DE PROBLEMAS
    VIB1_ACIERTO= models.IntegerField(default=0)


    class Meta:
            ordering = ["Fecha"]

    def __str__(self):
        return '%s-%s %s ' % (self.Fecha, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E2_10/{self.pk}/"
