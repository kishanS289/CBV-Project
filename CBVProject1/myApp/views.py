from django.shortcuts import render
from myApp.models import Student
from django.urls import reverse_lazy
from django.views.generic import *
# Create your views here.
class StudentListView(ListView):
    model=Student
class StudentDetailView(DetailView):
    model=Student    
class StudentCreateView(CreateView):
    model=Student
    fields='__all__'
class StudentUpdateView(UpdateView):
    model=Student
    fields=('name','marks')
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('students')        