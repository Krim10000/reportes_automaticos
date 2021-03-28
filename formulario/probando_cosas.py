
user = request.user
Institucion=Modelo_Info_Pro.objects.get(user=user).Institucion
estu = Modelo_Info_Per.objects.filter(Institucion=Institucion).order_by("-Rut")


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
