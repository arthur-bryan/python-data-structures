from models.program import Program
from models.premiere import Premiere


class Movie(Program):

    def __init__(self, name="", release_year=None, likes=0, duration=None):
        super().__init__(name=name, release_year=release_year, likes=likes)
        self.__duration_in_minutes = duration
        self.__premiere = None

    def __str__(self):
        duration_hour = self.__duration_in_minutes // 60
        duration_min = self.__duration_in_minutes % 60
        return str(f"Movie: {self.name}, Release year: {self.release_year}, " +
                   f"Likes: {self.likes}, Duration: {duration_hour}:{duration_min:02d}h")

    def will_have_premiere(self):
        return self.__premiere is not None

    @property
    def duration_in_minutes(self):
        return self.__duration_in_minutes

    @duration_in_minutes.setter
    def duration_in_minutes(self, duration):
        self.__duration_in_minutes = duration

    @property
    def premiere(self):
        if self.will_have_premiere():
            return self.__premiere
        return f"{self.name} won't have premiere."

    @premiere.setter
    def premiere(self, new_premiere):
        if isinstance(new_premiere, Premiere):
            self.__premiere = new_premiere
        else:
            raise TypeError(f"'{new_premiere}' is not a valid premiere")
