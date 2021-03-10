class Controller:
    def __init__(self, program_model, movie_model, serie_model, premiere_model, view):
        self.program_model = program_model
        self.movie_model = movie_model
        self.serie_model = serie_model
        self.premiere_model = premiere_model
        self.view = view
        self.movies = []
        self.series = []

    @staticmethod
    def menu():
        choice = int(input(
            """ ======= Streaming =======
            \r[1] Register a movie
            \r[2] Register a serie
            \r[3] Show movies
            \r[4] Show series
            \r[5] Show premieres
            \r[6] Show spinoffs
            \r[7] Like a program
            \r[8] Set premiere
            \r[9] Add spinoff
            \r[0] Exit
            \r\n---> """))
        return choice

    def register_movie(self):
        movie = self.movie_model()
        movie.name = input("Movie name: ").title()
        movie.release_year = int(input("Release year: "))
        movie.duration_in_minutes = int(input("Duration (in minutes): "))
        if movie.name not in [movie.name for movie in self.movies]:
            self.movies.append(movie)
            self.view.registered(movie)
        else:
            self.view.already_registered(movie)

    def register_serie(self):
        serie = self.serie_model()
        serie.name = input("Serie name: ").title()
        serie.release_year = input("Release year: ")
        serie.seasons = input("Number of seasons: ")
        if serie.name not in [serie.name for serie in self.series]:
            self.series.append(serie)
            self.view.registered(serie)
        else:
            self.view.already_registered(serie)

    def registered_programs(self):
        programs = []
        for movie in self.movies:
            programs.append(movie)
        for serie in self.series:
            programs.append(serie)
        return programs

    def show_movies(self):
        if not is_empty(self.movies):
            self.view.stream_list(self.movies)
        else:
            self.view.empty_list()

    def show_series(self):
        if not is_empty(self.series):
            self.view.stream_list(self.series)
        else:
            self.view.empty_list()

    def show_premieres(self):
        if not is_empty(self.movies):
            self.view.movie_premieres(self.movies)
        else:
            self.view.empty_list()

    def show_spinoffs(self):
        if not is_empty(self.series):
            self.view.series_spinoffs(self.series)
        else:
            self.view.empty_list()

    def like_item(self):
        if not is_empty(self.registered_programs()):
            self.view.all_programs(self.registered_programs())
            try:
                choice = int(input("Number of the program to like: "))
            except ValueError:
                self.view.invalid_choice()
                self.like_item()
            else:
                if choice in range(1, len(self.registered_programs()) + 1):
                    self.registered_programs()[choice - 1].add_like()
                else:
                    self.view.invalid_choice()
                    self.like_item()
        else:
            self.view.empty_list()

    def set_premiere(self):
        if not is_empty(self.movies):
            self.view.all_programs(self.movies)
            try:
                choice = int(input("Number of the movie to add premiere: "))
            except ValueError:
                self.view.invalid_choice()
                self.set_premiere()
            else:
                if choice in range(1, len(self.movies) + 1):
                    premiere = self.premiere_model()
                    premiere.movie = self.movies[choice - 1]
                    premiere.date = input(f"Premiere date for {self.movies[choice - 1].name}: ")
                    if premiere != self.movies[choice - 1].premiere:
                        self.movies[choice - 1].premiere = premiere
                    else:
                        self.view.already_registered(premiere)
                else:
                    self.view.invalid_choice()
                    self.set_premiere()
        else:
            self.view.empty_list()

    def add_spinoff(self):
        if not is_empty(self.series):
            self.view.all_programs(self.series)
            try:
                choice = int(input("Number of the serie to add spinoff: "))
            except ValueError:
                self.view.invalid_choice()
                self.add_spinoff()
            else:
                if choice in range(1, len(self.series) + 1):
                    program = input(f"Type a spinoff for {self.series[choice - 1].name} " +
                                    "(must be the name of a existing movie/serie): ").title()
                    existing_programs = self.registered_programs()
                    program_obj = list(filter(lambda x: x.name == program, existing_programs))
                    if program_obj[0] is self.series[choice - 1]:
                        self.view.is_same_item(program_obj[0])
                        return
                    if program_obj and program_obj[0] in existing_programs and program_obj[0]:
                        self.series[choice - 1].spinoffs = program_obj[0]
                        self.view.registered(program_obj[0])
                    else:
                        self.view.spinoff_not_exists(program)
                else:
                    self.view.invalid_choice()
        else:
            self.view.empty_list()


def is_empty(stream_list):
    if len(stream_list) == 0:
        return True
    return False
