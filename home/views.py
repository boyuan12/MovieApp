from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

TMDB_API_KEY = "05e5be7a518e07b0cdd93bf0e133083a"

def search(request):

    # Get the query from the search box
    query = request.GET.get('q')
    print(query)

    # If the query is not empty
    results = []
    if query:

        # Get the results from the API

        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        print(data.json())

        # temp = []
        # for m in data.json()["results"]:

        #     if len(temp) < 3:
        #         temp.append({"name": m["name"], "poster": m["poster_path"], "overview": m["overview"]})
        #     else:
        #         results.append(temp)
        #         temp.append({"name": m["name"], "poster": m["poster_path"], "overview": m["overview"]})

        # results.append(temp) if len(temp) > 0 else None


    else:
        return HttpResponse("Please enter a search query")

    # Render the template
    return render(request, 'home/results.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })

def index(request):
    return render(request, 'home/index.html')

def view_tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "home/tv_detail.html", {
        "data": data.json()
    })

def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "home/movie_detail.html", {
        "data": data.json()
    })