
# Django
from django.shortcuts import render, redirect, get_object_or_404

# Models
from figures import models

# Create your views here.
def index(request):
    context = {
        'navbar': 'index',
    }

    return render(request, 'figures/index.html', context=context)

def about(request):
    context = {
        'navbar': 'about',
    }

    return render(request, 'figures/about.html', context=context)

def statemap(request):
    context = {
        'navbar': 'states',
        "states_list": models.State.manager.all()
    }

    return render(request, 'figures/statemap.html', context=context)

def cartogram(request):
    context = {
        'navbar': 'cartogram',
    }

    return render(request, 'figures/cartogram.html', context=context)

def state(request, state):
    state = get_object_or_404(models.State, name=state)
    districts = state.district_set.all()

    context = {
        'navbar': 'states',
        'state': state,
        'district_list': districts
    }

    return render(request, 'figures/state.html', context=context)

def district(request, state, districtno):
    district = get_object_or_404(models.District, state=state, no=districtno)
    district_profile = get_object_or_404(models.DistrictProfile, district=district)

    context = {
        'navbar': 'states',
        'state': state,
        'district': district,
        'district_profile': district_profile
    }

    return render(request, 'figures/district.html', context=context)

def districtbyid(request, id):
    return redirect(get_object_or_404(models.District, id=id))