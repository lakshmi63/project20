from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.



def dept(request):
    dno=int(input('enter dept number'))
    dn=input('enter dept name')
    l=input('enter location')
    DO=Dept.objects.get_or_create(deptno=dno,dname=dn,loc=l)[0]
    DO.save()
    
    return HttpResponse(' dept data is inserted')

    





def emp(request):
    dno=int(input('enter dept no'))
    en=input('enter ename')
    s=int(input('enter sal'))
    DO=Dept.objects.get(deptno=dno)
    EO=Emp.objects.get_or_create(deptno=DO,ename=en,sal=s)[0]
    EO.save()

    return HttpResponse('emp data is inserted')





