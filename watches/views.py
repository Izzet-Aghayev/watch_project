from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404  # Məlumatları və ya error-u almaq üçündür.
from django.contrib import messages             # Mesajlar üçündür.
from django.shortcuts import(
    render,     # Html səhifılırini gətirmək üçündür.
    redirect    # Şablonu göstərmək üçündür.
)

from watches.models import Watch    # Model import edilir.
from watches.forms import WatchForm # Form import edilir.


                            # Əsas funksliyalar yaradılır.

# Bütün watch məlumatları.
def all_watches(request):
    watches = Watch.objects.all()   # Watch modelindəki bütün verailbleləri verir.
    context = {
        'watches': watches
    }
    return render(request, 'watches/all_watch.html', context)


# Watch məlumatlarını daxil edildiyi form funksiyası.
@login_required  # creat səhifəsindən öncə login hissəsinin açılmasını təmin edir 
def create_watch(request):
    if request.method == 'POST':   # Sorğunun POST olmasını yoxlayır.
        form = WatchForm(request.POST)  # Post sorğusuna görə formu verir.
        if form.is_valid():     # Formun valuesinin doğruluğunu yoxlayır.
            new_form = form.save(commit=False)       # Formu python səviyyəsində save edir.
            new_form.user = request.user        # Foruma useri daxil edir.
            form.save()         # Formu seyv edir.
            new_form.save()     # SQL səviyyəsində forumu seyv edirik.
            return redirect('all_watch')
        else:
            messages.error(request, "Yanlış əməliyyat")
            messages.error(request, form.errors)    # Formun errorlarını verir.
            messages.error(request, "MM/DD/YYYY")
            return redirect('watch_create')
        
    else:
        watch_form = {
            'watch_form': WatchForm()
        }
        return render(request, 'watches/create_watch.html', watch_form)


# Detalları göstərən funksiya.
def detail_watch(request, pk):
    watches = Watch.objects.filter(user=request.user)      # Useri request-dəki userlə eyni olan watch-ları seçib alır. 
    watch = get_object_or_404(watches, id=pk)

    watch_context = {
        'watch': watch
    }

    return render(request, 'watches/detail_watch.html', watch_context)


# Update etmək üçün funksiya.
def update_watch(request, pk):
    watches = Watch.objects.filter(user=request.user)
    watch = get_object_or_404(watches, id=pk)
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
        return render(request, 'watches/update_watch.html', context)


# Silmə edtmək üçün funksiya.
def delete_watch(request, pk):
    watch = get_object_or_404(Watch, id=pk)
    watch.delete()      # Watch məlumatlarını silmək üçün method.
    messages.success(request, f'{pk} ID-li watch məlumatları silindi.') # Uğurlu mesajı.
    return redirect('all_watch')