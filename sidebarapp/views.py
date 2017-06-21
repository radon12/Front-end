from django.views import generic
from models import Movie,Rating
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse_lazy
import views

# index view
def IndexView(request):
    if not request.user.is_authenticated():
        return render(request,"sidebarapp/login.html")
    template_name="sidebarapp/index.html"
    genres=["Action","Thriller","Mystery","Comedy","Fantasy","Animation"]
    genrescheck={}
    for genre in genres:
        genrescheck.update({genre:request.GET.get(genre,"false")})
    movies=Movie.objects.all()
    context={"genrescheck":genrescheck,"movies":movies}
    print request.GET
    #print movies
    print context
    print genrescheck
    print request.user
    #make a search fuction and make it return movies and add that to context that combines
    return render(request,template_name,context)

#register function
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context={"username":user.username}
                return redirect('sidebar:index')
    context = {
        "form": form,
    }
    return render(request, 'sidebarapp/registration_form.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'sidebarapp/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('sidebar:index')
            else:
                return render(request, 'sidebarapp/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'sidebarapp/login.html', {'error_message': 'Invalid login'})
    return render(request, 'sidebarapp/login.html')

def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        movie.save()
    except (KeyError, Movie.DoesNotExist):
        return redirect('sidebar:index')
