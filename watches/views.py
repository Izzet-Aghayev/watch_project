from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from django.shortcuts import(
    render,
    redirect
)

import watches
from watches.models import Watch
from watches.forms import WatchForm


# Əsas funksliyalar yaradılır.

# Bütün watch məlumatları.
def all_watches(request):
    watches = Watch.objects.all()
    context = {
        'watches': watches
    }
    return render(request, 'all_watch.html', context)


# Watch məlumatlarını daxil edildiyi form funksiyası.
def create_watch(request):
    if request.method == 'POST':   # Sorğunun POST olmasını yoxlayır.
        form = WatchForm(request.POST)
        if form.is_valid():     # Formun valuesinin doğruluğunu yoxlayır.
            form.save()         # Formu save edir.
            return redirect('all_watch')
        else:
            messages.error(request, "Yanlış əməliyyat")
            messages.error(request, form.errors)
            messages.error(request, "MM/DD/YYYY")
            return redirect('watch_create')
        
    else:
        watch_form = {
            'watch_form': WatchForm()
        }
        return render(request, 'create_watch.html', watch_form)


def detail_watch(request, pk):
    watch = get_object_or_404(Watch, id=pk)

    watch_context = {
        'watch': watch
    }

    return render(request, 'detail_watch.html', watch_context)


def update_watch(request, pk):
    watch = get_object_or_404(Watch, id=pk)
    if request.method == 'POST':
        form = WatchForm(request.POST, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('watch_detail', watch.id)
        else:
            messages.error(request, 'Yanlış əməliyyat.')
            messages.error(request, form.errors)
            messages.error(request, "MM/DD/YYYY")
            return redirect('watch_update', watch.id)
    else:
        form = WatchForm(instance=watch)
        context = {
            'form': form
        }
        return render(request, 'update_watch.html', context)

def delete_watch(request, pk):
    watch = get_object_or_404(Watch, id=pk)
    watch.delete()
    messages.success(request, f'{pk} ID-li watch məlumatları silindi.')
    return redirect('all_watch')