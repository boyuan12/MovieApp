from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from django.http import HttpResponse
import json

# Create your views here.

TMDB_API_KEY = "05e5be7a518e07b0cdd93bf0e133083a"

def search(request):

    # Get the query from the search box
    query = request.GET.get('q')
    print(query)

    # If the query is not empty
    if query:

        # Get the results from the API

        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        print(data.json())

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
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "home/tv_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "tv",
    })

def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "home/movie_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "tv": "movie",
    })


def view_trendings_results(request):
    type = request.GET.get("media_type")
    time_window = request.GET.get("time_window")

    trendings = requests.get(f"https://api.themoviedb.org/3/trending/{type}/{time_window}?api_key={TMDB_API_KEY}&language=en-US")
    return JsonResponse(trendings.json())
