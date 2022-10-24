import time
import django

from django.db import models
import datetime
from django.utils import timezone
from datetime import timedelta as tdelta

from django.shortcuts import render

from datacenter.models import (
    Passcard,
    Visit,
    format_duration,
    get_duration,
    is_visit_long
)

def storage_information_view(request):

    non_closed_visits = []
    
    open_visits = Visit.objects.filter(leaved_at__isnull=True)

    for item in open_visits:
       
      temp_dict = {
          "who_entered": item.passcard.owner_name,
          "entered_at": str(item.entered_at),
          "duration": str(django.utils.timezone.localtime() - item.entered_at),
          }
      
      non_closed_visits.append(temp_dict)
  
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
  