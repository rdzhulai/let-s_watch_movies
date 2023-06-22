from person import Person
from datetime import datetime
from constants import date_today


class FriendGroup:
    def __init__(self, members):
        self.members = members

    def order_movies(self, cinema):
        allowed_movies = list()

        for movie in cinema.get_movies_shown():
            for member in self.members:
                if not member.is_allowed(movie):
                    break
            else:
                allowed_movies.append(movie)

        ordered_movies = list()
        for movie in allowed_movies:
            rate = 0
            for member in self.members:
                if member.is_interested(movie):
                    rate += 1
            ordered_movies.append((movie, rate))

        ordered_movies.sort(key=lambda x: x[1], reverse=True)
        return ordered_movies

    def choose_screening(self, cinema):
        choosed_screenings = list()
        for movie, _ in self.order_movies(cinema):
            for screening in cinema.get_screenings_for_movie(movie):
                attendance_time_age = 0
                attendance_capacity = 0
                for member in self.members:
                    if member.can_attend(screening):
                        attendance_time_age += 1
                        if member.will_attend(screening):
                            attendance_capacity += 1
                choosed_screenings.append(
                    (
                        screening,
                        attendance_time_age,
                        attendance_capacity,
                        movie.get_time_passed(date_today),
                    )
                )

        choosed_screenings.sort(key=lambda x: (x[1], x[2], -x[3]), reverse=True)

        return choosed_screenings[0][0], choosed_screenings

    def buy_tickets(self, screening):
        count_attendees = 0
        end_time = screening.get_end_time()
        for member in self.members:
            if end_time[0] < member.bedtime:
                count_attendees += 1

        screening.sell_tickets(count_attendees)


if __name__ == "__main__":
    # you can run your tests here
    pass
