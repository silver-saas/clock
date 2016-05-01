"""Datetime objects with a ts method."""

import datetime
import time


class DateTimeTs(datetime.datetime):
    """A very simple child of datetime, which offers the ts property."""

    def __add__(self, other):
        """Standard addition on datetime, but with a DateTimeTs output."""

        return fromdatetime(datetime.datetime.__add__(self, other))

    @property
    def ts(self):
        """Seconds since epoch."""

        return int(time.mktime(self.timetuple()))


def fromdatetime(dt):
    """Construct a DateTimeTs object from a datetime one.

    Arguments:
      dt (datetime.datetime): A standard datetime object.

    Resturns:
      A DateTimeTs object with the same characteristics as dt.
    """

    return DateTimeTs(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute,
        second=dt.second, microsecond=dt.microsecond, tzinfo=dt.tzinfo)
