from screening import Screening
from auditorium import Auditorium


class Cinema:
    def __init__(self, auditoriums):
        self.auditoriums = auditoriums
        self.screenings = list()

    def add_movie(self, movie, screening_times):
        for time in screening_times:
            for auditorium in self.auditoriums:
                new_screening = Screening(movie, auditorium, time)
                if auditorium.add_screening(new_screening):
                    self.screenings.append(new_screening)
                    break
            else:
                raise RuntimeError(
                    f"Could not add movie {movie.title} at {time[0]:02d}:{time[1]:02d}"
                )

    def get_movies_shown(self):
        return list({x.movie for x in self.screenings})

    def get_screenings_for_movie(self, movie):
        return [x for x in self.screenings if x.movie == movie]


if __name__ == "__main__":
    # you can run your tests here
    pass
