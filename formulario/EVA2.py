# AQUI VAN LOS TEST EVALUA VERSIÓN 2.0, DEL 0 AL 10 #Listo!

from django.shortcuts import render

from .forms import *
from .formseva2 import *

from .models import *
from datetime import date
from datetime import datetime
hoy = date.today()


from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from django.contrib.auth.decorators import login_required

########################################################
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout



####################################################################################

class EDITAR_EVA2_00(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_00
    template_name = 'form.html'
    form_class =FormEVA2_00 # fundamental


    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_00")


###############################################################################
class NUEVO_EVA2_00(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_00
    template_name = 'form.html'
    form_class =FormEVA2_00
    success_url = 'Listado_E2_00'

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        #self.request.user
        #Modelo_Info_Pro.objects.get(user=request.user).Institucion

        return kwargs

    def form_valid(self,form):
        form.instance.user= self.request.user.username #salva el usuario
        #post.Institucion =  Modelo_Info_Pro.objects.get(user=request.user).Institucion
        form.instance.Institucion=Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion#FUNCIONA
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
###############################################################################
@login_required
def Listado_E2_00(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-0 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_00.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_00'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_00(request, pk):#Listo
    test=Modelo_EVALUA2_00.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_00")

##########################################################################################


class EDITAR_EVA2_01(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_01
    template_name = 'form.html'
    form_class =FormEVA2_01 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_01")

###############################################################################
###############################################################################

class NUEVO_EVA2_01(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_01
    template_name = 'form.html'
    form_class =FormEVA2_01
    success_url = 'Listado_E2_01'

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
@login_required
def Listado_E2_01(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-1 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_01.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_01'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_01(request, pk):#Listo
    test=Modelo_EVALUA2_01.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_01")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_02(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_02
    template_name = 'form.html'
    form_class =FormEVA2_02 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_02")

###############################################################################
###############################################################################

class NUEVO_EVA2_02(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_02
    template_name = 'form.html'
    form_class =FormEVA2_02
    success_url = 'Listado_E2_02'

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
@login_required
def Listado_E2_02(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-2 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_02.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_02'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_02(request, pk):#Listo
    test=Modelo_EVALUA2_02.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_02")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_03(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_03
    template_name = 'form.html'
    form_class =FormEVA2_03 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_03")

###############################################################################
###############################################################################

class NUEVO_EVA2_03(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_03
    template_name = 'form.html'
    form_class =FormEVA2_03
    success_url = 'Listado_E2_03'

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
@login_required
def Listado_E2_03(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-3 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_03.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_03'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_03(request, pk):#Listo
    test=Modelo_EVALUA2_03.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_03")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_04(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_04
    template_name = 'form.html'
    form_class =FormEVA2_04 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_04")

###############################################################################
###############################################################################

class NUEVO_EVA2_04(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_04
    template_name = 'form.html'
    form_class =FormEVA2_04
    success_url = 'Listado_E2_04'

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
@login_required
def Listado_E2_04(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-4 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_04.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_04'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_04(request, pk):#Listo
    test=Modelo_EVALUA2_04.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_04")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_05(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_05
    template_name = 'form.html'
    form_class =FormEVA2_05 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_05")

###############################################################################
###############################################################################

class NUEVO_EVA2_05(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_05
    template_name = 'form.html'
    form_class =FormEVA2_05
    success_url = 'Listado_E2_05'

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
@login_required
def Listado_E2_05(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-5 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_05.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_05'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_05(request, pk):#Listo
    test=Modelo_EVALUA2_05.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_05")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_06(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_06
    template_name = 'form.html'
    form_class =FormEVA2_06 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_06")

###############################################################################
###############################################################################

class NUEVO_EVA2_06(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_06
    template_name = 'form.html'
    form_class =FormEVA2_06
    success_url = 'Listado_E2_06'

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
@login_required
def Listado_E2_06(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-6 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_06.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_06'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_06(request, pk):#Listo
    test=Modelo_EVALUA2_06.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_06")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_07(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_07
    template_name = 'form.html'
    form_class =FormEVA2_07 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_07")

###############################################################################
###############################################################################

class NUEVO_EVA2_07(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_07
    template_name = 'form.html'
    form_class =FormEVA2_07
    success_url = 'Listado_E2_07'

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
@login_required
def Listado_E2_07(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-7 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_07.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_07'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_07(request, pk):#Listo
    test=Modelo_EVALUA2_07.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_07")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_08(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_08
    template_name = 'form.html'
    form_class =FormEVA2_08 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_08")

###############################################################################
###############################################################################

class NUEVO_EVA2_08(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_08
    template_name = 'form.html'
    form_class =FormEVA2_08
    success_url = 'Listado_E2_08'

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
@login_required
def Listado_E2_08(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-8 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_08.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_08'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_08(request, pk):#Listo
    test=Modelo_EVALUA2_08.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_08")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_09(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_09
    template_name = 'form.html'
    form_class =FormEVA2_09 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_09")

###############################################################################
###############################################################################

class NUEVO_EVA2_09(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_09
    template_name = 'form.html'
    form_class =FormEVA2_09
    success_url = 'Listado_E2_09'

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
@login_required
def Listado_E2_09(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-9 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_09.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_09'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_09(request, pk):#Listo
    test=Modelo_EVALUA2_09.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_09")

##########################################################################################
##########################################################################################

class EDITAR_EVA2_10(LoginRequiredMixin,UpdateView):

    model = Modelo_EVALUA2_10
    template_name = 'form.html'
    form_class =FormEVA2_10 # fundamental

    def get_form_kwargs(self):#funciona
        kwargs = super().get_form_kwargs()
        kwargs['Institucion'] = Modelo_Info_Pro.objects.get(user=self.request.user.username).Institucion
        return kwargs

    def form_valid(self,form):
        self.object = form.save()
        return redirect("Listado_E2_10")

###############################################################################
###############################################################################

class NUEVO_EVA2_10(LoginRequiredMixin,CreateView):
    model = Modelo_EVALUA2_10
    template_name = 'form.html'
    form_class =FormEVA2_10
    success_url = 'Listado_E2_10'

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
@login_required
def Listado_E2_10(request):
    user = request.user
    titulo = "LISTADO DE PRUEBAS EVALÚA-10 VERSIÓN CHILENA 2.0"
    gato = Modelo_EVALUA2_10.objects.filter(user=user).order_by("-Fecha")
    context_object_name = 'E2_10'
    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })

###############################################################################
@login_required
def borrar_E2_10(request, pk):#Listo
    test=Modelo_EVALUA2_10.objects.get(pk=pk)
    test.delete()
    return HttpResponseRedirect("/Listado_E2_10")

##########################################################################################
##########################################################################################
