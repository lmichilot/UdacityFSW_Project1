import webbrowser

class Movie():
    """
    This class provides a way to store movie related information.
    Attributes:
        title: The title of the movie.
        storyline: The summary of the movie.
        poster_image_url: URL of the movie poster.
        trailer_youtube_url: URL of the movie trailer.
        director: director of the movie.
    """

    def __init__(self, _title, _storyline, _image, _url, _director):
        self.title = _title
        self.storyline = _storyline
        self.poster_image_url = _image
        self.trailer_youtube_url = _url
        self.director = _director