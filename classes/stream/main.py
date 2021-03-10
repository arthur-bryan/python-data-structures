"""main.py: Programa simples que simula o catálogo de um serviço de streaming."""

__author__ = "Arthur Bryan"
__credits__ = ["Arthur Bryan"]
__version__ = "1.0.0"
__email__ = "arthurbryan2030@gmail.com"
__status__ = "Production"

from models.program import Program
from models.movie import Movie
from models.serie import Serie
from models.premiere import Premiere
from views.view import View
from controllers.controller import Controller


def main():
    controller = Controller(Program, Movie, Serie, Premiere, View)
    while True:
        try:
            choice = controller.menu()
        except ValueError:
            print("Invalid choice!")
        else:
            if choice == 1:
                controller.register_movie()
            elif choice == 2:
                controller.register_serie()
            elif choice == 3:
                controller.show_movies()
            elif choice == 4:
                controller.show_series()
            elif choice == 5:
                controller.show_premieres()
            elif choice == 6:
                controller.show_spinoffs()
            elif choice == 7:
                controller.like_item()
            elif choice == 8:
                controller.set_premiere()
            elif choice == 9:
                controller.add_spinoff()
            elif choice == 0:
                exit(0)
            else:
                print("Invalid choice!")


if __name__ == '__main__':
    main()
