from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import SamplePostBlog,DestaquePostBlog
from .forms import SamplePostBlogForm,DestaquePostBlogForm



def home(request):
    dicio = {}
    dicio['usuario'] = request.user
    dicio['sampleposts'] = SamplePostBlog.objects.all()
    dicio['destaquepostblog'] = DestaquePostBlog.objects.all()
    return render(request, 'index.html',dicio)

@login_required
def newsamplepostblog(request):
    dicio = {}
    form = SamplePostBlogForm(request.POST or None)

    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.user = request.user
        newpost.save()
        #form.save()
        return redirect('url_home')
    else:
        dicio['form'] = form
        return render(request, 'novopostsampleblog.html',dicio)
@login_required
def newdestaquepostblog(request):
    dicio = {}
    form = DestaquePostBlogForm(request.POST or None)

    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.user = request.user
        newpost.save()
        return redirect('url_home')
    else:
        dicio['form'] = form
        return render(request, 'novopostdestaqueblog.html',dicio)

def editsamplepostblog(request,id):
    dicio = get_object_or_404(SamplePostBlog,pk=id)
    form = SamplePostBlogForm(request.POST or None, instance=dicio)    
    if form.is_valid():
        form.save()
        return redirect('url_home')
    else:
        dicio={"form":form}
        return render(request, 'editpostsampleblog.html',dicio)

def editdestaquepostblog(request,id):
    dicio = get_object_or_404(DestaquePostBlog,pk=id)
    form = DestaquePostBlogForm(request.POST or None, instance=dicio)    
    if form.is_valid():
        form.save()
        return redirect('url_home')
    else:
        dicio={"form":form}
        return render(request, 'editpostdestaqueblog.html',dicio)

def deletardestaque(request,id):
    dicio = get_object_or_404(DestaquePostBlog,pk=id)
    formulario = DestaquePostBlogForm(request.POST or None, instance=dicio)

    if request.method=="POST":
       dicio.delete()
       return redirect('url_home')

    else:
        dicio={"form":formulario
        ,"delete":dicio
        }
        return render(request,'deletar.html',dicio)

def deletarsample(request,id):
    dicio = get_object_or_404(SamplePostBlog,pk=id)
    formulario = SamplePostBlogForm(request.POST or None, instance=dicio)

    if request.method=="POST":
       dicio.delete()
       return redirect('url_home')

    else:
        dicio={"form":formulario
        ,"delete":dicio
        }
        return render(request,'deletar.html',dicio)