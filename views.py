from django.shortcuts import render, redirect
from .forms import WeightForm
from .models import WeightEntry
from django.contrib.auth.decorators import login_required
import matplotlib
matplotlib.use('Agg')  # Verwende den "Agg"-Backend für nicht-interaktives Rendering
import matplotlib.pyplot as plt

import os
from django.conf import settings

from django.shortcuts import get_object_or_404

@login_required
def delete_weight_view(request, entry_id):
    entry = get_object_or_404(WeightEntry, id=entry_id, user=request.user)
    
    if request.method == 'POST':
        entry.delete()
        return redirect('tracker:trackerindex')  # Replace with the actual URL name
    
    context = {
        'entry': entry
    }
    
    return render(request, 'tracker/delete.html', context)

@login_required
def update_weight_view(request, entry_id):
    entry = get_object_or_404(WeightEntry, id=entry_id, user=request.user)
    
    if request.method == 'POST':
        form = WeightForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('tracker:trackerindex')  # Replace with the actual URL name
    else:
        form = WeightForm(instance=entry)
    
    context = {
        'form': form,
        'entry': entry
    }
    
    return render(request, 'tracker/update.html', context)

@login_required
def weight_form_view(request):
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            weight = form.save(commit=False)
            weight.user = request.user
            weight.save()
            return redirect('tracker:trackerindex')

    else:
        form = WeightForm()

    weights = WeightEntry.objects.filter(user=request.user).order_by('-date')  # Sortiere absteigend nach Datum
    parsed_weights = [{'id': entry.id, 'date': entry.date, 'weight': float(entry.weight)} for entry in weights]
    str_weights = [{'id': entry.id, 'date': entry.date, 'weight': str(entry.weight).replace(',', '.')} for entry in weights]
    # int(round(entry.weight))

    context = {
        'form': form,
        'parsed_weights': parsed_weights,
        'str_weights': str_weights
    }

    return render(request, 'tracker/index.html', context)
