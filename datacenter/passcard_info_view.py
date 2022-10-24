import django

from datacenter.models import (
    Passcard,
    Visit,
    format_duration,
    get_duration,
    is_visit_long
)

from django.shortcuts import (
    get_object_or_404,
    render
)


def passcard_info_view(request, passcode):
  
    passcard = get_object_or_404(Passcard, passcode = passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = []
              
    for item in passcard_visits:
                    
      temp_dict = {
        "entered_at": str(item.entered_at),
        "duration": str(get_duration(item)),
        "is_strange": is_visit_long(item, minutes = 60)}
      this_passcard_visits.append(temp_dict)
      
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
