import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Kelli's Video Picks</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="static/main.css">
    <link rel="stylesheet" href="//normalize-css.googlecode.com/svn/trunk/normalize.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="script/main.js"></script>

</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <header>
        <div class="content">
            <h1>Kelli's Video Picks</h1>
        </div>
    </header>


    <div class="icon">
        <div>
            <p><img src="https://upload.wikimedia.org/wikipedia/en/e/e7/Video-x-generic.svg"> = Movie</p>
        </div>
        <div>
            <p><img src="https://upload.wikimedia.org/wikipedia/commons/b/b6/TV-icon-2.svg"> = Tv Show</p>
        </div>
        <div>
            <p>Click the video thumbnails to see the previews!</p>
        </div>
    </div>
    <div class="container">
      {video_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster}" width="220" height="342">
    <h2>{title}</h2>
    <h4>{duration}<img src="{movie_icon}" width="20" height="20"></h4>
    <p>Director: {director}
    <br>
    Production Company: {producer}<p>
</div>
'''

# A single show entry html template
series_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster}" width="220" height="342">
    <h2>{title}</h2>
    <h4>{episodes}<img src="{tv_icon}" width="20" height="20"></h4>
    <p>{season}
    <br>
    TV Station: {station}</p>
</div>
'''


def create_video_tiles_content(videos):
    """ Creates the html for the video tile list
    videos: Array of videos from entertainment_center
    return: The list of videos click-able tiles that show video previews and movie trailers
    """
    content = ''
    for video in videos:
        if video.isMovie is True and video.isShow is False:
            """
            If the video is a movie and not a tv show, the video tile will be assigned a movie icon
            and will show all the characteristics that is unique to a Movie object.
            """
            video.movie_icon = "https://upload.wikimedia.org/wikipedia/en/e/e7/Video-x-generic.svg" # creates an icon

            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', video.trailer)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', video.trailer)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                title=video.title,
                poster=video.poster,
                director=video.director,
                duration=video.duration,
                producer=video.producer,
                trailer_youtube_id=trailer_youtube_id,
                movie_icon=video.movie_icon
            )
        elif video.isShow is True and video.isMovie is False:
            video.tv_icon = "https://upload.wikimedia.org/wikipedia/commons/b/b6/TV-icon-2.svg"

            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', video.trailer)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', video.trailer)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the show with its content filled in
            content += series_tile_content.format(
                title=video.title,
                poster=video.poster,
                season=video.season,
                episodes=video.episodes,
                station=video.station,
                trailer_youtube_id=trailer_youtube_id,
                tv_icon=video.tv_icon


            )
    return content


def open_videos_page(videos):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        video_tiles=create_video_tiles_content(videos))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
