from datetime import datetime, timedelta


def generate_future_date_time(
    weeks: int = 0, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0
):
    """
    Generates a future datetime from the current datetime.

    :param weeks: Number of weeks into the future
    :param days: Number of days into the future
    :param hours: Number of hours into the future
    :param minutes: Number of minutes into the future
    :param seconds:Number of seconds into the future

    Author: ƒa†3
    """
    return datetime.now() + timedelta(
        weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds
    )
