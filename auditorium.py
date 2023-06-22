class Auditorium:
    def __init__(self, capacity):
        self.capacity = capacity
        self.screenings = list()

    def is_available(self, new_screening):
        if not self.screenings:
            return True
        start_time1 = new_screening.time[0] * 60 + new_screening.time[1]
        end_time = new_screening.get_end_time()
        end_time1 = end_time[0] * 60 + end_time[1]

        for screening in self.screenings:
            start_time2 = screening.time[0] * 60 + screening.time[1]
            end_time = screening.get_end_time()
            end_time2 = end_time[0] * 60 + end_time[1]
            if start_time1 <= end_time2 and start_time2 <= end_time1:
                return False
        return True

    def add_screening(self, new_screening):
        if self.is_available(new_screening):
            self.screenings.append(new_screening)
            return True
        return False


if __name__ == "__main__":
    # you can run your tests here
    pass
