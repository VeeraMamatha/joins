from django.shortcuts import render

# Create your views here.
from app1.models import *
def  0(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

