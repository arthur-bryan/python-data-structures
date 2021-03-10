class Program:

	def __init__(self, name=None, release_year=None, likes=0):
		self.__name = name
		self.__release_year = release_year
		self.__likes = int(likes)

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		self.__name = new_name

	@property
	def release_year(self):
		return self.__release_year

	@release_year.setter
	def release_year(self, year):
		self.__release_year = year

	@property
	def likes(self):
		return self.__likes

	@likes.setter
	def likes(self, number):
		self.__likes = number

	def add_like(self):
		self.__likes += 1
