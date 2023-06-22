import re
import constants
import calendar
from datetime import datetime


class Movie:
    date_pattern = re.compile(r"^(.{4})/(.{2})/(.{2})$")

    def __init__(self, title, length, genre, age_limit, release_date):
        if not isinstance(title, str):
            raise TypeError("Movie title must be string")
        if not isinstance(length, int):
            raise TypeError("Movie length must be integer")
        if length < 1:
            raise ValueError("Movie length must be at least 1")
        if genre not in constants.GENRES:
            raise ValueError(f'Unknown genre "{genre}"')
        if not isinstance(age_limit, int):
            raise TypeError("Age limit must be integer")
        if age_limit < 1:
            raise ValueError("Age limit must be at least 1")

        self.title = title
        self.length = length
        self.genre = genre
        self.age_limit = age_limit
        self.converted_release_date = self.validate_date(release_date)
        self.release_date = release_date

    def validate_date(self, date):
        if not isinstance(date, str):
            raise TypeError("Release date must be string")
        match = re.match(self.date_pattern, date)
        if match is None:
            raise ValueError("Release date must meet format YYYY/MM/DD")
        try:
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
        except ValueError:
            raise ValueError(f'Could not load date from string: "{date}"')
        if not 1 <= month <= 12:
            raise ValueError(f"Invalid month {month}")
        days_in_month = calendar.monthrange(year, month)[1]
        if not 1 <= day <= days_in_month:
            raise ValueError(f"Invalid day for {calendar.month_name[month]}: {day}")
        return year, month, day

    def get_time_passed(self, date):
        converted_date = self.validate_date(date)
        days_between = (
            datetime(converted_date[0], converted_date[1], converted_date[2])
            - datetime(
                self.converted_release_date[0],
                self.converted_release_date[1],
                self.converted_release_date[2],
            )
        ).days

        return days_between


if __name__ == "__main__":
    # you can run your tests here
    pass
