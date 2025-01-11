from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404  # Məlumatları və ya error-u almaq üçündür.
from django.contrib import messages             # Mesajlar üçündür.
from django.shortcuts import(
    render,     # Html səhifılırini gətirmək üçündür.
    redirect    # Şablonu göstərmək üçündür.
)

from watches.models import Watch    # Model import edilir.
from watches.forms import WatchForm # Form import edilir.


                            # Function base views.
                            # Əsas funksliyalar yaradılır.

# Bütün watch məlumatları.
# def all_watches(request):
#     watches = Watch.objects.all()   # Watch modelindəki bütün verailbleləri verir.
#     context = {
#         'watches': watches
#     }
#     return render(request, 'watches/all_watch.html', context)


# Yalnız login olan sellerin watch-larını gətirən funksiya.
# def my_watches(request):
    # my_watches = Watch.objects.filter(seller=request.user)
    # context = {
    #     'my_watches': my_watches
    # }
    # return render(request, 'watches/my_watches.html', context)


# Watch məlumatlarını daxil edildiyi form funksiyası.
# @login_required  # creat səhifəsindən öncə login hissəsinin açılmasını təmin edir 
# def create_watch(request):
#     if request.method == 'POST':   # Sorğunun POST olmasını yoxlayır.
#         form = WatchForm(request.POST, request.FILES)  # Post sorğusuna görə formu verir.
#         if form.is_valid():     # Formun valuesinin doğruluğunu yoxlayır.
#             new_form = form.save(commit=False)       # Formu python səviyyəsində save edir.
#             new_form.seller = request.user        # Foruma useri daxil edir.
#             form.save()         # Formu seyv edir.
#             new_form.save()     # SQL səviyyəsində forumu seyv edirik.
#             return redirect('all_watch')
#         else:
#             messages.error(request, "Yanlış əməliyyat")
#             messages.error(request, form.errors)    # Formun errorlarını verir.
#             messages.error(request, "MM/DD/YYYY")
#             return redirect('watch_create')
        
#     else:
#         watch_form = {
#             'watch_form': WatchForm()
#         }
#         return render(request, 'watches/create_watch.html', watch_form)


# Detalları göstərən funksiya.
# def detail_watch(request, pk):
#     watches = Watch.objects.select_related('seller').prefetch_related('categories')
#     watch = get_object_or_404(watches, id=pk)

#     watch_context = {
#         'watch': watch
#     }

#     return render(request, 'watches/detail_watch.html', watch_context)


# Update etmək üçün funksiya.
# @login_required
# def update_watch(request, pk):
#     watches = Watch.objects.filter(seller=request.user).select_related('seller').prefetch_related('categories')            # Useri request-dəki userlə eyni olan watch-ları seçib alır. 
#     watch = get_object_or_404(watches, id=pk)
#     if request.method == 'POST':
#         form = WatchForm(request.POST, request.FILES, instance=watch)
#         if form.is_valid():
#             form.save()
#             return redirect('watch_detail', watch.id)
#         else:
#             messages.error(request, form.errors)
#             return redirect('watch_update', watch.id)
#     else:
#         form = WatchForm(instance=watch)
#         context = {
#             'form': form,
#             'watch': watch
#         }
#         return render(request, 'watches/update_watch.html', context)


# Silmə edtmək üçün funksiya.
# @login_required
# def delete_watch(request, pk):
#     watches = Watch.objects.filter(seller=request.user)
#     watch = get_object_or_404(watches, id=pk)
#     watch.delete()      # Watch məlumatlarını silmək üçün method.
#     messages.success(request, f'{pk} ID-li watch məlumatları silindi.') # Uğurlu mesajı.
#     return redirect('all_watch')



                        # Class base views.
                        # View-ləri class-lar ilə yazırıq.

class ListWatchView(View):
    def get(self, request):
        watches = Watch.objects.all()   # Watch modelindəki bütün verailbleləri verir.

        context = {
            'watches': watches
        }
        return render(request, 'watches/all_watch.html', context)
    


class MyWatchView(View):
    def get_object(self, request_user):
        # my_watches = Watch.objects.filter(seller=request_user)
        my_watches = request_user.watches.all()
        return my_watches

    def get(self, request):
        my_watches = self.get_object(request_user=request.user)
        context = {
            'my_watches': my_watches
        }
        
        return render(request, 'watches/my_watches.html', context)
    


class CreateWatchView(LoginRequiredMixin, View):
    def get(self, request):
        watch_form = {
            'watch_form': WatchForm()
        }
        return render(request, 'watches/create_watch.html', watch_form)

    def post(self, request):
        form = WatchForm(request.POST, request.FILES)  # Post sorğusuna görə formu verir.
        if form.is_valid():     # Formun valuesinin doğruluğunu yoxlayır.
            new_form = form.save(commit=False)       # Formu python səviyyəsində save edir.
            new_form.seller = request.user        # Foruma useri daxil edir.
            form.save()         # Formu seyv edir.
            new_form.save()     # SQL səviyyəsində forumu seyv edirik.
            return redirect('all_watch')
        else:
            messages.error(request, "Yanlış əməliyyat")
            messages.error(request, form.errors)    # Formun errorlarını verir.
            messages.error(request, "MM/DD/YYYY")
            return redirect('watch_create')



class DetailWatchView(LoginRequiredMixin, View):
    def get_object(self, pk):
        watches = Watch.objects.select_related('seller').prefetch_related('categories')
        watch = get_object_or_404(watches, id=pk)
        return watch

    def get(self, request, pk):
        watch = self.get_object(pk=pk)
        watch_context = {
            'watch': watch
        }

        return render(request, 'watches/detail_watch.html', watch_context)

    def post(self, request, pk):
        watch = self.get_object(pk=pk)
        watch_context = {
            'watch': watch
        }

        return render(request, 'watches/detail_watch.html', watch_context)
    
    

class UpdateWatchView(LoginRequiredMixin, View):
    def get_object(self, request_user, pk):
        watches = Watch.objects.filter(seller=request_user).select_related('seller').prefetch_related('categories')            # Useri request-dəki userlə eyni olan watch-ları seçib alır. 
        watch = get_object_or_404(watches, id=pk)
        return watch

    def get(self, request, pk):
        watch = self.get_object(request_user=request.user, pk=pk)

        form = WatchForm(instance=watch)
        update_context = {
            'form': form,
            'watch': watch
        }
        return render(request, 'watches/update_watch.html', update_context)


    def post(self, request, pk):
        watch = self.get_object(request_user=request.user, pk=pk)

        form = WatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('watch_detail', watch.id)
        else:
            messages.error(request, form.errors)
            return redirect('watch_update', watch.id)


class DeleteWatchView(LoginRequiredMixin, View):
    def get_object(self, request_user, pk):
        watches = Watch.objects.filter(seller=request_user)
        watch = get_object_or_404(watches, id=pk)
        return watch

    def post(self, request, pk):
        watch = self.get_object(request_user=request.user, pk=pk)

        self.perform_delete(obj=watch)      # Watch məlumatlarını silmək üçün method.
        messages.success(request, f'{pk} ID-li watch məlumatları silindi.') # Uğurlu mesajı.
        return redirect('my_watch')
    
    def perform_delete(self, obj):
        obj.delete()