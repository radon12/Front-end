from django.shortcuts import render
from django.views import generic
# Create your views here.
def IndexView(request):
    template_name="sidebarapp/index.html"
    genres=["Action","Thriller","Mystery","Comedy","Fantasy","Animation"]
    genrescheck={}
    for genre in genres:
        genrescheck.update({genre:request.GET.get(genre,"false")})
    #movies=search()
    context={"genrescheck":genrescheck,"movies":movies}
    print request.GET
    #print movies
    print context
    print genrescheck
    #make a search fuction and make it return movies and add that to context that combines
    return render(request,template_name,context)
