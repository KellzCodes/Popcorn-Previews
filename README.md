# Popcorn Previews
## A simple movie trailer website project for Udacity's [Full-Stack Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

This project demonstrates the use, in Python, a parent Video object class and two children object classes called Movie 
and Show. The purpose is to create a static webpage that displays a listing of various movies and tv shows and links 
each medium to its respective trailer videos on youtube. The project also makes use of HTML, CSS, JQuery, and 
JavaScript.

## Table of Contents

- [Download](#download)
- [How to run this application](#How-to-run-this-application)
- [Quick Start](#quick-start)
- [File Directory](#file-directory)
- [Documentation](#documentation)

## Download
The files can be downloaded [here](https://github.com/keldavis/Popcorn-Previews/archive/master.zip)

The entire project can be cloned using this link: https://github.com/keldavis/Popcorn-Previews.git

## How to run this application
- Download [zip file](https://github.com/keldavis/kelli_movie_project/archive/master.zip)
- Extract the folder
- Execute [entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

## Quick Start
- After downloading the project, the web page can be created by importing 
[media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py) and 
[fresh_tomatoes.py](https://github.com/keldavis/kelli_movie_project/blob/master/fresh_tomatoes.py) into your new python 
file.
- Create Video objects by calling either media.Movie or media.Show and supply 9 variables. 
- media.Movie variables are: title, duration, isMovie, isShow, plot, director, producer, poster, and trailer.
- media.Show variables are: title, season, isMovie, isShow, episodes, plot, station, poster, trailer.
- To generate the web page, make an array of all the movie and show objects and use it to call this function: 
fresh_tomatoes.open_movies_page().

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

More detailed examples of various movie and show objects can be found in 
[entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

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
- [Movie Class](#movie-object-class)
- [Show Class](#show-object-class)
- [Web Page Functions](#web-page-functions)


### Video Object Parent Class
This class creates an object called video. Video is a blue print for video objects. 
It has two children called Movie and Show. This class can be found in the 
[media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py) file.
    
#### Video Constructor Method
The constructor method is called when a new Video (Movie or Show) is created and must include six variables. 
-- [title](#title), [isMovie](#is-movie), [isShow](#is-show), [plot](#plot), [poster](#poster), and [trailer](#trailer). 
The details for each variable are provided below.

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
title is a string value which is the name of the video

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
The show_info() method can be called on any Video (Movie or Show) object to print the object's title, isMovie, isShow, 
and plot. This method is useful for testing but is not used in the code that generates the finished web page.

Method from [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

```
    def show_info(self):
        print "Title - " + self.title
        print "Is this a Movie? - " + str(self.isMovie)
        print "Is this a TV Show? - " + str(self.isShow)
        print "Plot - " + self.plot
```
     
How to call the method in 
[entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

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
The show_trailer() method can be called on any Video (Movie or Show) object to launch the object's youtube trailer in a 
web browser. This method is useful for testing but is not used in the code that generates the finished web page.

Method from [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

```
import webbrowser

    def show_trailer(self):
        webbrowser.open(self.trailer)
``` 

How to call the method in 
[entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

```
    import media

    # Create Movie Object
    godfather = media.Movie(title, duration, isMovie, isShow, plot, director, producer, poster, trailer)
    
    # Call the show_trailer method
    godfather.show_trailer()
```

### show poster method
The show_poster() method can be called on any Video (Movie or Show) object to launch the object's promotional art work 
in a web browser. This method is useful for testing but is not used in the code that generates the finished web page.

Method from [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

```
import webbrowser

    def show_poster(self):
        webbrowser.open(self.poster)
``` 

How to call the method in 
[entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py)

```
    import media

    # Create Movie Object
    godfather = media.Movie(title, duration, isMovie, isShow, plot, director, producer, poster, trailer)
    
    # Call the show_poster method
    godfather.show_poster()
```

### Movie Object Class
The Movie Object Class consists of 9 class variables and a simple constructor method. The code is located 
in [media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py).

#### Movie Constructor Method
The constructor method is called when a new Movie object is created. It must include 9 variables. 6 of the variables are 
inherited from its parent, the Video class: [movie.title](#movie-title), [movie.isMovie](#movie-is-movie), 
[movie.isShow](#movie-is-show), [movie.plot](#movie-plot), [movie.poster](#movie-poster), 
[movie.trailer](#movie.trailer). There are 3 variables that are not inherited and are unique to class Movie: 
[movie.duration](#movie-duration), [movie.director](#movie-director), [movie.producer](#movie-producer). More details on 
[how to create a Movie object](#how-to-create-a-movie-object) are presented below.

```
class Movie(Video):
    def __init__(self, title, duration, isMovie, isShow, plot, director, producer, poster, trailer):
    
        Video.__init__(self, title, isMovie, isShow, plot, poster, trailer)  

        self.duration = duration
        self.director = director
        self.producer = producer
```

More detailed explanation is documented in 
[media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

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

#### How to create a Movie object

```
    import media

    # movie variables
    title = "godfather"
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

More examples of Movie objects are found in 
[entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py).

### Show Object Class
The Movie Object Class consists of 9 class variables and a simple constructor method. The code is located in 
[media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py).

#### Show Constructor Method
The Tv Show constructor method is called when a new Show object is created. It must include 9 variables. 6 of the 
variables are inherited from its parent, the Video class: [show.title](#show-title), [show.isMovie](#show-is-movie), 
[show.isShow](#show-is-show), [show.plot](#show-plot), [show.poster](#show-poster), [show.trailer](#show.trailer). 
There are 3 variables that are not inherited and are unique to class Show: [show.season](#show-season), 
[show.episodes](#show-episodes), [show.station](#show-station). More details on 
[how to create a Show object](#how-to-create-a-show-object) are presented below.

```
class Show(Video):

    def __init__(self, title, season, isMovie, isShow, episodes, plot, station, poster, trailer):

        Video.__init__(self, title, isMovie, isShow, plot, poster, trailer)

        self.episodes = episodes
        self.season = season
        self.station = station
```

More detailed explanation is documented in 
[media.py](https://github.com/keldavis/kelli_movie_project/blob/master/media.py)

#### show title
show.title is a string variable inherited from Video. This is the Tv Show's name.

#### show season
show.season is a string variable unique to class Show. This says which season of the TV Show is presented.

#### show is Movie
show.isMovie is a boolean value inherited from Video. This confirms that the video is not a movie.

#### show is Show
show.isShow is a boolean value inherited from Video. This confirms that the video is a tv show.

#### show episodes
show.episodes is a string value that is unique to class Show. This says how many episodes is in the season.

#### show plot
show.plot is a string value inherited from Video. This says what the tv show is about.

#### show station
show.station is a string value that is unique to class Show. This says what tv station the show airs.

#### show poster
show.poster is a string value inherited from Video. This is a link to the tv show's promotional art.

#### show trailer
show.trailer is a string value inherited from Video. This is a link to the tv show's youtube preview.

#### How to create a Show object

```
    import media

    # show variables
    title = "scrubs"
    season = "Season 3"
    isMovie = False
    isShow = True
    episodes = "22 episodes"
    plot = "Dr JD learns the way of life and medicine"
    station = "ABC"
    poster = "https://upload.wikimedia.org/wikipedia/en/4/45/Scrubs-s3-dvd.jpg"
    trailer = "https://www.youtube.com/watch?v=do9jR8Guz_E"

    # Create Movie Object
    scrubs = media.Show(title, season, isMovie, isShow, episodes, plot, station, poster, trailer)
```

More examples of Show objects are found in 
[entertainment_center.py](https://github.com/keldavis/kelli_movie_project/blob/master/entertainment_center.py).

### Web Page Functions
The functions used to create the final web page are located in 
[fresh_tomatoes.py](https://github.com/keldavis/kelli_movie_project/blob/master/fresh_tomatoes.py). 

#### Open Videos Page Function
To create the static web page, the open_videos_page() function must be called and supplied a single variable, which is
an array of video objects.

```
# Create array with various shows and movies
videos = [godfather, fresh, higher_learning, hotel_transylvania_2, lion_king, cinderella,
          scrubs, ahs_coven, ahs_murder_house, will_grace, oz, desperate_housewives]

# put array in function to render webpage
fresh_tomatoes.open_videos_page(videos)
```

Once the web page is generated, 
[fresh_tomatoes.html](https://github.com/keldavis/kelli_movie_project/blob/master/fresh_tomatoes.html) will be created
and place in the same directory as the rest of the code. 

#### Create Video Tiles Function
The create_video_tiles() function is called by the open_videos_page(). It uses the video array as a variable and uses 
the information from each video to create a tile to be rendered on the final web page. It also extracts the YouTube id 
from video.trailer in order to show the video when the tile is clicked by the user. 
- This function also has two if-statements nested inside a for-loop to sort the Movie and Show objects.
    - If video.isMovie is True and video.isShow is False, the video tile will be assigned a movie icon 
    and will show all the characteristics that is unique to a Movie object.
    - If video.isMovie is False and video.isShow is True, the video tile will be assigned a tv icon 
    and will show all the characteristics that is unique to a Show object.

More details about how this method works are documented in 
[fresh_tomatoes.py](https://github.com/keldavis/kelli_movie_project/blob/master/fresh_tomatoes.py)




