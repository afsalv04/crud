# from django.shortcuts import render,redirect
# from .forms import anim

# def anim_view(request):
#     if request.method == "POST":
#         form = animForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect (anim_view)
#     else:
#         form = anim_view()
#         return render(request, 'anim.html',{'form': form})
# Create your views here.


# from django.shortcuts import redirect,render
# from .forms import animForm

# def anim_view(request):
#     if request.method == "POST":
#         form =animForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('anim')   # ✅ redirect using URL name
#     else:
#         form = animForm()
#     return render(request, 'anim.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import animForm
from .models import anim


def anim_create(request):
    if request.method == "POST":
        form = animForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anim_list')   
    else:
        form = animForm()

    return render(request, 'anim_form.html', {'form': form})


def anim_list(request):
    pets = anim.objects.all()
    return render(request, 'anim_list.html', {'pets': pets})


