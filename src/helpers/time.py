from datetime import datetime


class DateTimeHelper:
    @staticmethod
    def unix_time_to_datetime(unix_time: int) -> datetime:
        unix_time = unix_time / 1000
        return datetime.fromtimestamp(unix_time)
