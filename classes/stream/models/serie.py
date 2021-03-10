from models.program import Program


class Serie(Program):

    def __init__(self, name="", release_year=None, likes=0, seasons=0):
        super().__init__(name=name, release_year=release_year, likes=likes)
        self.__seasons = int(seasons)
        self.__spinoffs = []

    def __str__(self):
        return str(f"Serie: {self.name}, Release year: {self.release_year},"
                   f" Likes: {self.likes}, Seasons: {self.__seasons}")

    def has_spinoff(self):
        return True if len(self.__spinoffs) > 0 else False

    @property
    def seasons(self):
        return self.__seasons

    @seasons.setter
    def seasons(self, number):
        self.__seasons = number

    @property
    def spinoffs(self):
        return self.__spinoffs


    @spinoffs.setter
    def spinoffs(self, new_spinoff):
        if issubclass(type(new_spinoff), Program) or isinstance(new_spinoff, Program):
            self.__spinoffs.append(new_spinoff)
        else:
            raise TypeError(f"'{new_spinoff}' is not a valid spinoff")
