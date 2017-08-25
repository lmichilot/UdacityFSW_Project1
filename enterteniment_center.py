import fresh_tomatoes
import media

# wonderMovie: title, storyline, image, url, director
wonderMovie = media.Movie(
    "Wonder Woman",
    "Diana, princess of the Amazons, trained to be an unconquerable warrior. "
    "Raised on a sheltered island paradise,when a pilot crashes on their"
    " shores and tells of a massive conflict raging in the outside world, "
    "Diana leaves her home, convinced she can stop the threat.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Tgk_63b-Mrw",
    "Patty Jenkins")

# loganMovie: title, storyline, image, url, director
loganMovie = media.Movie(
    "Logan",
    "In the near future, a weary Logan cares for an ailing Professor X, "
    "somewhere on the Mexican border. However, Logan's attempts to hide from "
    "the world, and his legacy, are upended when a young mutant arrives, "
    "pursued by dark forces.",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=gbug3zTm3Ws",
    "James Mangold")

# spiderMovie: title, storyline, image, url, director
spiderMovie = media.Movie(
    "Spiderman",
    "This is a story of Peter Parker who is a nerdy high-schooler.Spider-Man:"
    "Homecoming is a 2017 American superhero film based on the Marvel Comics "
    "character Spider-Man, co-produced by Columbia Pictures and Marvel "
    "Studios.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man_Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=rk-dF1lIbIg",
    "Spiderman")

# dunkirkMovie: title, storyline, image, url, director
dunkirkMovie = media.Movie(
    "Dunkirk",
    "Allied soldiers from Belgium, the British Empire and France are "
    "surrounded by the German army and evacuated during a fierce battle in "
    "World War II.",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
    "https://www.youtube.com/watch?v=F-eMt3SrfFU",
    "Christopher Nolan")

# apesMovie: title, storyline, image, url, director
apesMovie = media.Movie(
    "Planet of the Apes",
    "After the apes suffer unimaginable losses, Caesar wrestles with his "
    "darker instincts and begins his own mythic quest to avenge his kind.",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=UEP1Mk6Un98",
    "Matt Reeves")

# thorMovie: title, storyline, image, url, director
thorMovie = media.Movie("Thor: Ragnarok",
    "Imprisoned, the mighty Thor finds himself in a lethal gladiatorial "
    "contest against the Hulk, his former ally. Thor must fight for survival"
    " and race against time to prevent the all-powerful Hela from destroying"
    " his home and the Asgardian civilization.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Thor_Ragnarok_poster.jpg/220px-Thor_Ragnarok_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Rgs6U3HnLv8",
    "Taika Waititi")

# Store the Movie objects in a list.
movies = [
    wonderMovie,
    loganMovie,
    spiderMovie,
    dunkirkMovie,
    apesMovie,
    thorMovie
]

# Open the movie website in the user's browser featuring the list of movies above.
fresh_tomatoes.open_movies_page(movies)