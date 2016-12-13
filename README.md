# Kelli Movie Trailer Project
## A simple movie trailer website project for Udacity's [Full-Stack Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

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

# video variables
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

## File Directory
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
- [Video Class](#video-object-parent-class)
- [Show Info Method](#show-info-method)
- [Show Trailer Method](#show-trailer-method)
- [Show Poster Method](#show-poster-method)
- [Movie Object Class](#movie-object-class)


### Video Object Parent Class
This class creates an object called video. Video is a blue print for video objects. It has two children called Movie and Show. This class can be found in the [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py) file.
    
#### Video Constructor Method
The constructor method is called when a new Video (Movie or Show) is created and must include six arguments -- [title](#title), [isMovie](#is-Movie), [isShow](#is-Show), [plot](#plot), [poster](#poster), and [trailer](#trailer). The details for each argument are provided below.

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

#### title
Title is a string value which is the name of the video

#### is Movie
isMovie is a boolean value that determines whether the video is a movie

#### is Show
isShow is a boolean value that determines whether the video is a tv show

#### plot
plot is a string value that says what the video is about

#### poster
poster is a string value which is the link to the video's promotional art work

#### trailer
trailer a string value which is the link to the video's youtube trailer

### show info method
The show_info() method can be called on any Video (Movie or Show) object to print the object's title, isMovie, isShow, and plot. This method is useful for testing but is not used in the code that generates the finished web page.

Method from [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

```
    def show_info(self):
        print "Title - " + self.title
        print "Is this a Movie? - " + str(self.isMovie)
        print "Is this a TV Show? - " + str(self.isShow)
        print "Plot - " + self.plot
```
     
How to call the method in [entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

```
    import media

    # Create Movie Object
    godfather = media.Movie(title, duration, isMovie, isShow, plot, director, producer, poster, trailer)
    
    # Call the show_info method
    godfather.show_info()
```
    
Example of output
```
    Title - The Godfather
    Is this a Movie? - True
    Is this a TV Show? - False
    Plot - The aging patriarch of a crime dynasty
    transfers control of his empire to his
    reluctant son.
```

### show trailer method
The show_trailer() method can be called on any Video (Movie or Show) object to launch the object's youtube trailer in a web browser. This method is useful for testing but is not used in the code that generates the finished web page.

Method from [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

```
import webbrowser

    def show_trailer(self):
        webbrowser.open(self.trailer)
``` 

How to call the method in [entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

```
    import media

    # Create Movie Object
    godfather = media.Movie(title, duration, isMovie, isShow, plot, director, producer, poster, trailer)
    
    # Call the show_trailer method
    godfather.show_trailer()
```

### show poster method
The show_poster() method can be called on any Video (Movie or Show) object to launch the object's promotional art work in a web browser. This method is useful for testing but is not used in the code that generates the finished web page.

Method from [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

```
import webbrowser

    def show_poster(self):
        webbrowser.open(self.poster)
``` 

How to call the method in [entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

```
    import media

    # Create Movie Object
    godfather = media.Movie(title, duration, isMovie, isShow, plot, director, producer, poster, trailer)
    
    # Call the show_poster method
    godfather.show_poster()
```

### Movie Object Class
The Movie Object Class consists of 9 class variables and a simple constructor method. The code is located in [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py).

#### Movie Constructor Method
The constructor method is called when a new Movie object is created. It must include 9 arguments. 6 of the arguments are inherited from its parent, the Video class: [title](#movie-title), [isMovie](#movie-is-movie), [isShow](#movie-is-show), [plot](#movie-plot), [poster](#movie-poster), [trailer](#movie.trailer). There are 3 variables that are not inherited and are unique to class Movie: [duration](#movie-duration), [director](#movie-director), [producer](#movie-producer). 

```
class Movie(Video):
    def __init__(self, title, duration, isMovie, isShow, plot, director, producer, poster, trailer):
    
        Video.__init__(self, title, isMovie, isShow, plot, poster, trailer)  

        self.duration = duration
        self.director = director
        self.producer = producer
```

More detailed explanation is documented in [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

#### movie title
movie.title is a string variable inherited from Video. This is the Movie's name.

#### movie duration
movie.duration is a string value of the length of time the movie lasts. Unique to Movie class.

#### movie is movie
movie.isMovie is a boolean variable inherited from Video. This confirms the video is a movie.

#### movie is show
movie.isShow is a boolean variable inherited from Video. This confirms the video is not a tv show.

#### movie plot
movie.plot is a string variable inherited from Video. This says what the movie is about.

#### movie director
movie.director is a string variable unique to Movie class. This is the name of the movie director.

#### movie producer
movie.producer is a string variable unique to Movie class. This says the name of the movie's production company.

#### movie poster
movie.poster is a string variable inherited from Video. This is the link to the movie poster.

#### movie trailer
movie.trailer is a string variable inherited from Video. This is the link to the youtube movie trailer

How to create a movie object

```
    import media

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
```

More examples of Movie objects are found in [entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py).
