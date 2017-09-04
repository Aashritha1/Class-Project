
# Create your views here.
from django.shortcuts import render
from django.conf.urls import url
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.http import HttpResponse
from onlineapp.models import *
from django.template import loader
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.exceptions import PermissionDenied


class Create(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required ='onlineapp.add_college'
    permission_denied_message = 'Not an authorised user'
    model = College
    context_object_name = "collegelist"
    template_name = "onlineapp/collegeform.html"
    fields=["name","acronym","location","contact"]
    success_url = "/onlineapp/collegeinfo/"

    def handle_no_permission(self):
        if self.request.user.is_authenticated():
            raise PermissionDenied(self.get_permission_denied_message())
        return super(Create,self).handle_no_permission()



class Update(LoginRequiredMixin,UpdateView):
    model = College
    context_object_name = "collegelist"
    template_name = "onlineapp/collegeform.html"
    fields = ["name", "acronym", "location", "contact"]
    success_url = "onlineapp/collegeinfo"

class Delete(LoginRequiredMixin,DeleteView):
    model = College
    context_object_name = "collegelist"
    template_name = "onlineapp/collegeform_delete.html"
    success_url = "onlineapp/collegeinfo"

class CreateDetail(DetailView):
    model = College
    context_object_name = "collegelist"
    template_name = "onlineapp/college_detail.html"

class Createcollege(ListView):
    model = College
    template_name = "onlineapp/index1.html"
    context_object_name = "collegelist"


# class ButtonView(ListView):
#     pass

