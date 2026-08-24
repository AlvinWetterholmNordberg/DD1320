import csv


def read_file(filename):
    with open(filename, "r") as file:
        csvfile = csv.reader(file, delimiter=",")
        next(csvfile)  # Hoppa över header-raden
        for line in csvfile:
            print(line)  # Här kan du göra något med raden, t.ex. skapa ett Seed-objekt


# Klassen drama representerar en rad i kdrama-filen.
class Drama:
    def __init__(self, drama):
        self.title = drama[0]
        self.rating = float(drama[1])
        self.actors = drama[2].split(",")  # Dela upp skådespelarna i en lista
        self.viewship_rate = float(drama[3])
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = int(drama[7])
        self.number_of_episodes = int(drama[8])
        self.network = drama[9]

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - Rating: {self.rating}"

    def __lt__(self, other):
        return self.rating > other.rating

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_director(self):
        return self.director

    def get_writer(self):
        return self.writer

    def get_year(self):
        return self.year

    def get_number_of_episodes(self):
        return self.number_of_episodes

    def get_GRP(self):
        grp = self.viewship_rate * self.rating
        return grp

    def after_2020(self):
        if self.year > 2020:
            return "Yes"
        else:
            return "No"


def read_rows_from_file(filename):
    dramas = []
    with open(filename, "r") as file:
        csvfile = csv.reader(file, delimiter=",")
        next(csvfile)  # Hoppa över header-raden
        for line in csvfile:
            if len(line) == 10:  # Kontrollera att raden har exakt 10 kolumner
                drama_obj = Drama(line)
                dramas.append(drama_obj)
    return dramas


def find_max_rating(dramas):
    max_rating = 0
    for drama in dramas:
        if drama.rating > max_rating:
            max_rating = drama.rating
            best_rated_drama = drama
    return best_rated_drama


def program_task_3():
    # Create 2 Drama objects and use 5 methods.

    torsk_pa_tallin = Drama(
        [
            "Torsk på Tallinn",
            "7.5",
            "Killinggänget",
            "3.5",
            "Comedy",
            "Thomas Alfredsson",
            "Johan Rheborg",
            "2021",
            "10",
            "SVT",
        ]
    )
    das_båt = Drama(
        [
            "Das Boot",
            "8.3",
            "Jürgen Prochnow, Herbert Grönemeyer",
            "4.2",
            "War, Drama",
            "Wolfgang Petersen",
            "Wolfgang Petersen",
            "1981",
            "6",
            "ZDF",
        ]
    )

    # Methods for drama 1 (Das Båt)
    title_drama1 = das_båt.get_title()
    genre_drama1 = das_båt.get_genre()
    director_drama1 = das_båt.get_director()
    grp_drama1 = das_båt.get_GRP()
    after_2020_drama1 = das_båt.after_2020()

    # Methods for drama 2 (Torsk Pa Tallin)
    title_drama2 = torsk_pa_tallin.get_title()
    writer_drama2 = torsk_pa_tallin.get_writer()
    year_drama2 = torsk_pa_tallin.get_year()
    number_of_episodes_drama2 = torsk_pa_tallin.get_number_of_episodes()
    after_2020_drama2 = das_båt.after_2020()

    print(
        f" Title: {title_drama1} \n Genre: {genre_drama1} \n Director: {director_drama1} \n GRP: {grp_drama1} \n After 2020: {after_2020_drama1} \n"
    )
    print(
        f" Title: {title_drama2} \n Genre: {writer_drama2} \n Director: {year_drama2} \n GRP: {number_of_episodes_drama2} \n After 2020: {after_2020_drama2}"
    )


def search_highest_rated_drama(file):

    list_of_dramas = read_rows_from_file(file)
    best_rated_drama = find_max_rating(list_of_dramas)
    print(f"The best rated drama in the csv file is: {best_rated_drama}")


search_highest_rated_drama("Lab1/kdrama.csv")
program_task_3()
