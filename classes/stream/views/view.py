class View:

	@staticmethod
	def showmsg_invalid_object(current_type, expected_type):
		print(f"Expected {type(expected_type)}, not {type(current_type)}")

	@staticmethod
	def registered(program):
		print(f"{program.name} registered successfully!")

	@staticmethod
	def already_registered(program):
		print(f"{program.name} is already registered!")

	@staticmethod
	def has_spinoff(serie):
		print(serie.has_spinoff())

	@staticmethod
	def stream_list(stream_list):
		for num, prgram in enumerate(stream_list):
			print(f"{num+1}- {prgram}")

	@staticmethod
	def empty_list():
		print("There are no items registered.")

	@staticmethod
	def movie_premieres(movies_list):
		for movie in movies_list:
			print(movie.premiere)

	@staticmethod
	def series_spinoffs(series_list):
		for serie in series_list:
			if serie.has_spinoff():
				for spinoff in serie.spinoffs:
					print(f"Serie: {serie.name}, Spinoff: {str(spinoff).split(',')[0]}.")
			else:
				print(f"There are no spinoffs for {serie.name}.")

	@staticmethod
	def all_programs(progams_list):
		for num, program in enumerate(progams_list):
			print(f"{num+1}- {program}")

	@staticmethod
	def invalid_choice():
		print("Invalid choice!")

	@staticmethod
	def will_have_premiere(movie):
		print(movie.will_have_premiere())

	@staticmethod
	def show_premiere(movie):
		print(movie.premiere)

	@staticmethod
	def spinoff_not_exists(name):
		print(f"{name} was not registered as a movie or serie, so it can't be a spinoff!")

	@staticmethod
	def is_same_item(spinoff):
		print(f"{str(spinoff).split(',')[0]} can't be a spinoff of itself!")
