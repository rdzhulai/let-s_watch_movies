class Screening:
    def __init__(self, movie, auditorium, time):
        self.movie = movie
        self.auditorium = auditorium
        self.time = time
        self.tickets_sold = 0

    def sell_tickets(self, count):
        if self.auditorium.capacity < self.tickets_sold:
            return False
        elif self.auditorium.capacity >= self.tickets_sold + count:
            self.tickets_sold += count
            return True
        else:
            return False

    def get_occupancy(self):
        return float(self.tickets_sold / self.auditorium.capacity)

    def get_end_time(self):
        hours, minutes = self.time
        minutes += self.movie.length
        while minutes > 59:
            minutes -= 60
            hours += 1
        return hours, minutes


if __name__ == "__main__":
    # you can run your tests here
    pass
