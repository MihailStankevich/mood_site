from random import sample
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect
from .models import Book, Category
from django.contrib.auth.forms import UserCreationForm
from  .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def sad(request):
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=f14e9c05592ce94f67688a40f71a4a63&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=35&with_watch_monetization_types=flatrate'
    movie_response = requests.request("GET", url)
    movie = movie_response.json()
    movie_dat = movie['results']
    movie_data = sample(movie_dat, k = 3)

    url = "https://spotify23.p.rapidapi.com/search/"

    querystring = {"q":"positive","type":"playlists","offset":"0","limit":"10","numberOfTopResults":"5"}

    headers = {
        "X-RapidAPI-Key": "09e8845db1msh23e0e703c9b28edp1ddfe2jsn148a5f0d86d7",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    pl = response.json()
    playlis = pl['playlists']['items']
    playlist = sample(playlis, k = 3)

    self_help_book = Book.objects.filter(self_help_books = True)
    self_help_books = self_help_book[:3]

    return render(request, 'sad.html', {'movie_data': movie_data, 'playlist': playlist, 'self_help_books': self_help_books})

def happy(request):
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=f14e9c05592ce94f67688a40f71a4a63&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=12%2C53%2C80&with_watch_monetization_types=flatrate'
    movie_response = requests.request("GET", url)
    movie = movie_response.json()
    movie_dat = movie['results']
    movie_data = sample(movie_dat, k = 3)

    url = "https://spotify23.p.rapidapi.com/search/"

    querystring = {"q":"top","type":"playlists","offset":"0","limit":"10","numberOfTopResults":"5"}

    headers = {
        "X-RapidAPI-Key": "09e8845db1msh23e0e703c9b28edp1ddfe2jsn148a5f0d86d7",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    pl = response.json()
    playlis = pl['playlists']['items']
    playlist = sample(playlis, k = 3)

    business_book = Book.objects.filter(business_books = True)
    business_books = business_book[:3]
    return render(request, 'happy.html', {'movie_data': movie_data, 'playlist': playlist, 'business_books': business_books})

def neutral(request):
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=f14e9c05592ce94f67688a40f71a4a63&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=18%2C27%2C28&with_watch_monetization_types=flatrate'
    movie_response = requests.request("GET", url)
    movie = movie_response.json()
    movie_dat = movie['results']
    movie_data = sample(movie_dat, k = 3)

    url = "https://spotify23.p.rapidapi.com/search/"

    querystring = {"q":"all out","type":"playlists","offset":"0","limit":"10","numberOfTopResults":"5"}

    headers = {
        "X-RapidAPI-Key": "09e8845db1msh23e0e703c9b28edp1ddfe2jsn148a5f0d86d7",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    pl = response.json()
    playlis = pl['playlists']['items']
    playlist = sample(playlis, k = 3)

    fiction_book = Book.objects.filter(fiction_books = True)
    fiction_books = fiction_book[:3]

    return render(request, 'neutral.html', {'movie_data': movie_data, 'playlist': playlist, 'fiction_books': fiction_books})

def romantic(request):
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=f14e9c05592ce94f67688a40f71a4a63&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=10749%2C18&with_watch_monetization_types=flatrate'
    movie_response = requests.request("GET", url)
    movie = movie_response.json()
    movie_dat = movie['results']
    movie_data = sample(movie_dat, k = 3)

    url = "https://spotify23.p.rapidapi.com/search/"

    querystring = {"q":"romance","type":"playlists","offset":"0","limit":"10","numberOfTopResults":"5"}

    headers = {
        "X-RapidAPI-Key": "09e8845db1msh23e0e703c9b28edp1ddfe2jsn148a5f0d86d7",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    pl = response.json()
    playlis = pl['playlists']['items']
    playlist = sample(playlis, k = 3)


    romance_book = Book.objects.filter(romance_books = True)
    romance_books = romance_book[:3]

    return render(request, 'romantic.html', {'movie_data': movie_data, 'playlist': playlist, 'romance_books': romance_books})

    
def movies(request):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=f14e9c05592ce94f67688a40f71a4a63&language=en-US&page=1'
    movie_response = requests.request("GET", url)
    movie = movie_response.json()
    movie_da = movie['results']
    movie_data = sample(movie_da, k = 15)
    return render(request, 'movies.html', {'movie_data': movie_data,})


def spotify(request):

    # lamar_uri = 'spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg'
    

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials( client_id='ace84050ad8a4d798889d3e6d093520a',
    client_secret='71c3a26298b441079414889ace8c5c15',))
    
    
    # tracks = spotify.artist_top_tracks(lamar_uri)
    # final_result = tracks['tracks'][:10]
    # return render(request, 'spotify.html', {'tracks': final_result, })

    playlist_data = spotify.new_releases()
    playlist = playlist_data['albums']['items']
    return render(request, 'spotify.html', {'playlist': playlist,})
    
    

# Create your views here.
def home(request):

    emojis = ['neutral', 'sad','happy','romantic']
    url = "https://spotify23.p.rapidapi.com/playlist_tracks/"

    querystring = {"id":"37i9dQZEVXbMDoHDwVN2tF","offset":"0","limit":"10"}

    headers = {
        "X-RapidAPI-Key": "09e8845db1msh23e0e703c9b28edp1ddfe2jsn148a5f0d86d7",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    data = requests.request("GET", url, headers=headers, params=querystring)
    response = data.json()
    recomend = response['items']
    recomendation = sample(recomend, k = 8)

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        "X-RapidAPI-Key": "0a23c8b439msh2185a614709e6cap114e5ejsn34acaecab357",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    quotes_data = requests.request("GET", url, headers=headers)
    quotes_response = quotes_data.json()
    quotes = quotes_response['content']

    url = 'https://api.themoviedb.org/3/movie/popular?api_key=f14e9c05592ce94f67688a40f71a4a63&language=en-US&page=1'
    movie_response = requests.request("GET", url)
    movie = movie_response.json()
    movie_dat = movie['results']
    movie_data = sample(movie_dat, k = 3)


    return render(request, 'home.html', {'recomendation': recomendation, 'quotes': quotes, 'movie_data': movie_data, "emojis": emojis
    })

def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books':books})
    
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    return render(request, 'genre_detail.html', {'category': category})

@login_required(login_url='login')
def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    return render(request, 'book_detail.html', {'book': book, 'similar_books': similar_books})

def register_page(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, "Account Created Successfully!")
            return redirect('login')
           
    return render(request, 'register.html', {'register_form': register_form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
        
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')
    