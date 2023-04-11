# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 11/27/2022
# Description: A streaming guide that contains movies, streaming services and
#    returns which service is showing your movie

class Movie:
    """
    Class that stores movies and their attributes
    """

    def __init__(self, title, genre, director, year):
        """
        Constructor for the Movie Class
        :param title: The title of the movie
        :param genre: The genre of the movie
        :param director: Who directed the movie
        :param year: What year it was released
        """
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """
        Getter for the Title
        :return: the title
        """
        return self._title

    def get_genre(self):
        """
        Getter for the genre
        :return: the genre
        """
        return self._genre

    def get_director(self):
        """
        Getter for the director
        :return: the director
        """
        return self._director

    def get_year(self):
        """
        Getter for the year
        :return: the year
        """
        return self._year


class StreamingService:
    """
    Class that stores Streaming Services
    """
    def __init__(self, name):
        """
        Constructor for the StreamingService class
        :param name: Name of the streaming service
        """
        self._name = name
        self._catalog = {}

    def get_name(self):
        """
        Getter for the name
        :return: self._name
        """
        return self._name

    def get_catalog(self):
        """
        Getter for the catalog
        :return: self._catalog
        """
        return self._catalog

    def add_movie(self, movie_object):
        """
        Takes a movie object and adds it to the catalog
        :param movie_object: takes a movie object and gets the title and object
        :return: nothing
        """
        # Adds a movie to the catalog dictionary with the Title as the Key and the movie object as the value
        self._catalog[movie_object.get_title()] = movie_object

    def delete_movie(self, movie_object):
        """
        Take a movie object and deletes it from the catalog
        :param movie_object:
        :return:
        """
        # This will remove (pop) the dictionary entry if the movie object exists
        self._catalog.pop(movie_object)


class StreamingGuide:
    """
    Streaming Guide Class
    """

    def __init__(self):
        """
        Constructor for the StreamingGuide class
        """
        self._streaming_guide = []

    def add_streaming_service(self, streaming_service_object):
        """
        Takes a streaming service object and adds it to the catalog
        :param streaming_service_object: Takes a Streaming Service object and adds it to the list of services
        :return: Nothing, adds the streaming service to the StreamingGuide
        """
        self._streaming_guide.append(streaming_service_object)

    def delete_streaming_service(self, streaming_service):
        """
        Takes a streaming service object and deletes it from the catalog
        :param streaming_service: streaming service object
        :return: Nothing, removes the item if there
        """
        # runs through the streaming_guide and removes the requested guide from the list
        for item in self._streaming_guide:
            if item.get_name() == streaming_service:
                self._streaming_guide.remove(item)

    def where_to_watch_movie(self, movie_title):
        """
        Takes a movie title and finds which streaming service has that title available
        :param movie_title: The title to search the streaming services for
        :return: Title + year, streaming services showing movie
        """
        where_to_watch = []  # Initializes the return string to an empty list
        for item in self._streaming_guide:  # Iterates through the streaming_guide
            for title in item.get_catalog(): # iterates through the titles in the StreamingService catalog
                if title == movie_title:  # Checks if the current StreamingService Catalog Title is the right one
                    movie_object = item.get_catalog().get(title)  # Gets the movie object
                    # Concatenates the title and the year of the movie (which comes from the movie object)
                    movie_info = title + " (" + str(movie_object.get_year()) + ")"
                    if not where_to_watch:  # If nothing is in the where_to_watch list
                        where_to_watch.append(movie_info)
                        where_to_watch.append(item.get_name())
                    # We've already started building the where_to_watch list, just need the StreamService name added
                    else:
                        where_to_watch.append(item.get_name())
        return where_to_watch


# movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
# movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
# movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
# movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)
# movie_5 = Movie('Enter the Dragon', 'Action', 'Bruce Lee', 1972)
# stream_serv_1 = StreamingService('Netflick')
# stream_serv_1.add_movie(movie_2)
# stream_serv_1.add_movie(movie_5)
# stream_serv_2 = StreamingService('Hula')
# stream_serv_2.add_movie(movie_1)
# stream_serv_2.add_movie(movie_4)
# stream_serv_2.add_movie(movie_5)
# stream_serv_2.delete_movie('The Seventh Seal')
# stream_serv_2.add_movie(movie_2)
# stream_serv_3 = StreamingService('Dizzy+')
# stream_serv_3.add_movie(movie_4)
# stream_serv_3.add_movie(movie_3)
# stream_serv_3.add_movie(movie_1)
# stream_serv_3.add_movie(movie_5)
# stream_guide = StreamingGuide()
# stream_guide.add_streaming_service(stream_serv_1)
# stream_guide.add_streaming_service(stream_serv_2)
# stream_guide.add_streaming_service(stream_serv_3)
# stream_guide.delete_streaming_service('Hula')
# search_results = stream_guide.where_to_watch_movie('Little Women')
# print(search_results)
# search_results2 = stream_guide.where_to_watch_movie('Home Alone')
# print(search_results2)
# search_results3 = stream_guide.where_to_watch_movie('The Seventh Seal')
# print(search_results3)
# search_results4 = stream_guide.where_to_watch_movie('Galaxy Quest')
# print(search_results4)
# search_results5 = stream_guide.where_to_watch_movie('Enter the Dragon')
# print(search_results5)
