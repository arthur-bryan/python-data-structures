class Premiere:

	def __init__(self, movie=None, date=None):
		self.__movie = movie
		self.__date = date

	def __str__(self):
		return str(f"Premiere of {self.__movie.name} at {self.__date}")

	@property
	def movie(self):
		return self.__movie.name

	@movie.setter
	def movie(self, new_movie):
		self.__movie = new_movie

	@property
	def date(self):
		return self.__date

	@date.setter
	def date(self, new_date):
		self.__date = new_date
