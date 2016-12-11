import webbrowser


class Video:
    """ Parent class
    This class creates an object called video.
    Video is a blue print for video objects.
    It has two children called Movie and Show.
    """
    def __init__(self, title, isMovie, isShow, plot, poster, trailer):
        """ Constructor for the Video class
        Parameters:
        title: A string value which is the name of the video
        isMovie: A boolean value that determines whether the video is a movie
        isShow: A boolean value that determines whether the video is a tv show
        plot: A string value that says what the video is about
        poster: A string value which is the link to the video's promotional art work
        trailer: A string value which is the link to the video's youtube trailer
        """

        self.title = title
        self.isMovie = isMovie
        self.isShow = isShow
        self.plot = plot
        self.poster = poster
        self.trailer = trailer

    def show_info(self):
        """ Prints the video info
        return: title, isMovie, isShow, plot
        """
        print "Title - " + self.title
        print "Is this a Movie? - " + str(self.isMovie)
        print "Is this a TV Show? - " + str(self.isShow)
        print "Plot - " + self.plot

    def show_trailer(self):
        """
        Opens a browser and plays the video preview or movie trailer
        return: trailer
        """
        webbrowser.open(self.trailer)

    def show_poster(self):
        """
        Opens a browser and shows the video promotional art work
        return: poster
        """
        webbrowser.open(self.poster)


class Movie(Video):
    """ Child class
    This class creates a movie object
    Movie is a child that inherits characteristics from the Video class
    """
    def __init__(self, title, duration, isMovie, isShow, plot, director, producer, poster, trailer):
        """ Constructor for the Movie class
        Parameters:
        title: String value of the movie's name
        duration: String value of the length of time the movie lasts
        isMovie: Boolean value that confirms the video is a movie
        isShow: Boolean value that confirms the video is not a tv show
        plot: String value that says what the movie is about
        director: String value that says the name of the movie director
        producer: String value that says the name of the production company
        poster: String value which is the link the movie poster
        trailer: String value which is the link to the youtube movie trailer
        """

        Video.__init__(self, title, isMovie, isShow, plot, poster, trailer)  # Initializes the variables of class Video

        # Additional variables that are unique to class Movie
        self.duration = duration
        self.director = director
        self.producer = producer


class Show(Video):
    """ Child class
    This class creates a Show object
    Show is a child that inherits characteristics from the Video class
    """
    def __init__(self, title, season, isMovie, isShow, episodes, plot, station, poster, trailer):
        """ Constructor for the Show class
        Parameters:
        title: String value of the tv show's name
        season: String value of the tv show's season
        isMovie: Boolean value that confirms the video is not a movie
        isShow: Boolean value that confirms the video is a tv show
        episodes: String value that says how many episodes in the season
        plot: String value that says what the TV show is about
        station: String value that says what tv station show airs on
        poster: String value which is the link to the tv show's promotional art
        trailer: String value which is the link to the tv show's youtube preview
        """

        Video.__init__(self, title, isMovie, isShow, plot, poster, trailer) # Initializes the variables of class Show

        # Additonal variables that are unique to class Show
        self.episodes = episodes
        self.season = season
        self.station = station








