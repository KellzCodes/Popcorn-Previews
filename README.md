# Kelli Movie Trailer Project
### A simple movie trailer website project for Udacity's [Full-Stack Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

This project demonstrates the use, in Python, a parent Video object class and two children object classes called Movie and Show. The purpose is to create a static webpage that displays a listing of various movies and tv shows and links each medium to its respective trailer videos on youtube. The project also makes use of HTML, CSS, JQuery, and JavaScript.

## Table of Contents

- [Download](#download)
- [Quick Start](#quick-start)
- [File Directory](#file-directory)
- [Documentation](#documentation)

## Download
The files can be downloaded [here](https://github.com/keldavis/kelli_movie_project/archive/master.zip)

The entire project can be cloned using this link: https://github.com/keldavis/kelli_movie_project.git

## Quick Start
- After downloading the project, the web page can be created by importing [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py) and [fresh_tomatoes.py](https://github.com/keldavis/kelli_movie_project/blob/master/fresh_tomatoes.py) into your new python file.
- Create Video objects by calling either media.Movie or media.Show and supply 9 arguments. 
- media.Movie parameters are: title, duration, isMovie, isShow, plot, director, producer, poster, and trailer.
- media.Show parameters are: title, season, isMovie, isShow, episodes, plot, station, poster, trailer.
- To generate the web page, make an array of all the movie and show objects and use it to call this function: fresh_tomatoes.open_movies_page().

```
import media
import fresh_tomatoes

# movie arguments
title = godfather
duration = "2h 58m "
isMovie = True
isShow = False
plot = "The aging patriarch of a crime dynasty"
director = "Francis Ford Coppola"
producer = "Paramount Pictures"
poster = "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg"
trailer = "https://www.youtube.com/watch?v=sY1S34973zA"

# Create Movie Object
godfather = media.Movie(title, duration, isMovie, isShow, plot, director, producer, poster, trailer)

# put video objects in an array
videos = [godfather, lion_king, friday]

# Create web page with array of videos
fresh_tomatoes.open_movies_page(videos)

```

More detailed examples of various movie and show objects can be found in [entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

### File Directory
Within the zip file, you'll find the following directories and files:

```
kelli_movie_project-master.zip/
├── img/
│   └── theatre_curtains.png
├── script/
│   └── main.js
├── static/
│   └── main.css
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Video Object Parent Class
This class creates an object called video. Video is a blue print for video objects. It has two children called Movie and Show. This class can be found in the [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py) file.
    
#### Constructor Method
The constructor method is called when a new Video (Movie or Show) is created and must include six arguments -- [title](#title), [isMovie](#isMovie), [isShow](#isShow), [plot](#plot), [poster](#poster), and [trailer](#trailer). The details for each argument are provided below.

```
class Video:
    def __init__(self, title, isMovie, isShow, plot, poster, trailer):
        self.title = title
        self.isMovie = isMovie
        self.isShow = isShow
        self.plot = plot
        self.poster = poster
        self.trailer = trailer
```

###### title
Title is a string value which is the name of the video

###### isMovie
isMovie is a boolean value that determines whether the video is a movie

###### isShow
isShow is a boolean value that determines whether the video is a tv show

###### plot
plot is a string value that says what the video is about

###### poster
poster is a string value which is the link to the video's promotional art work

###### trailer
trailer a string value which is the link to the video's youtube trailer


