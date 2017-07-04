from django.views import generic
from models import Movie,Rating
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse_lazy
import views
from django.contrib.auth.models import User
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
    movie_and_rating={}
    user=request.user
    for movie in movies:
        try:
            rate=Rating.objects.filter(movie=movie,user=user)
            movie_rating=rate[0].rating
        except(IndexError):
            movie_rating="0"
        movie_and_rating.update({movie:movie_rating})
    q=request.GET.get("q","")
    context={"genrescheck":genrescheck,"movie_and_rating":movie_and_rating,"q":q}

    #print movies
    print request.GET
    print context
    print request.user
    print (request.user).id

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

def rate_movie(request):
    movie_id=request.POST.get("movie_id",-1)
    rating=request.POST.get("rating",0)
    user_id=request.user.id
    movie = get_object_or_404(Movie, pk=movie_id)
    user = get_object_or_404(User,pk=user_id)
    try:
        rate=Rating.objects.filter(movie=movie,user=user)
        try:
            rate=rate[0]
        except (IndexError):
            rate=Rating()
            rate.user=user
            rate.movie=movie
        rate.rating=rating
        rate.save()
        return redirect('sidebar:index')
    except (KeyError, Movie.DoesNotExist,User.DoesNotExist),e:
        print e
        return redirect('sidebar:index')

def populate_data(request):
    f=open("/home/radon12/Documents/Sidebar/Django/sidebar/sidebarapp/movieswrite.csv",'r')
    for eachline in f:
        list=eachline.split('^')
        movie=Movie()
        movie.movie_title=list[0]
        movie.movie_date=list[1]
        movie.movie_genre=list[2]
        movie.movie_logo=list[3]
        movie.save()
    return redirect("sidebar:index")
def recommendations(request):
    template_name="sidebarapp/recommed.html"
    context={}
    return render(request,template_name,context)    
