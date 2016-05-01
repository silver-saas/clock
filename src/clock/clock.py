"""Datetime setup useful for IoC usage. Inspired by Dart-quiver's Clock."""

import datetime

import pytz

from .datetimets import fromdatetime


def _system_time():
    """Standard time function which produces a datetime object in UTC.

    Returns:
      A datetime.datetime object representing the current time in UTC.
    """
    return datetime.datetime.now(pytz.utc)


def fixed(time):
    """Construct a Clock instance which always returns the supplied time. Useful in tests.

    Arguments:
      time (datetime.datetime): a datetime object which the returned Clock instsance will always 
      use.

    Return:
      An instance of Clock.
    """
    return Clock(time_func=lambda: time)
    

class Clock(object):
    """A source of time.

    Useful when adopting an IoC setup for applications. Fake clocks can be provided for special
    purposes or unittesting. Mocking libraries can be used for even finer grained controls.
    More importantly, the strong dependency of an object on a source of time is made explicit.
    """

    def __init__(self, time_func=_system_time):
        """Constructor for Clock objects.

        Arguments:
          time_func: a zero-argument function which should produce a datetime.datetime instance
            representing the current time in UTC.
        """
        self._time_func = time_func

    def now(self):
        """Obtain the current time in UTC.

        Returns:
          A DateTimeTs instance representing the current time in UTC.
        """
        right_now = self._time_func()
        assert isinstance(right_now, datetime.datetime)
        assert right_now.tzinfo == pytz.utc
        return fromdatetime(right_now)
