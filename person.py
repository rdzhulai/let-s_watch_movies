class Person:
    def __init__(self, interests, age, bedtime, tolerance):
        self.interests = interests
        self.age = age
        self.bedtime = bedtime
        self.tolerance = tolerance

    def is_interested(self, movie):
        return movie.genre in self.interests

    def is_allowed(self, movie):
        return self.age >= movie.age_limit

    def can_attend(self, screening):
        return (
            self.is_allowed(screening.movie)
            and screening.get_end_time()[0] < self.bedtime
        )

    def will_attend(self, screening):
        return screening.get_occupancy() < self.tolerance


if __name__ == "__main__":
    # you can run your tests here
    pass
