from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'tuShaR kUMaR PaNDa HoW ARE you','c':2, 'dt':dt }
    return render(request,'built_in_filter_method.html',d)