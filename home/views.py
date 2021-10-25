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
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")

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
        "data": data.json()
    })

def index(request):
    return render(request, 'home/index.html')