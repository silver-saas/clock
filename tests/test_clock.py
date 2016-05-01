import datetime
import unittest

import pytz

import clock


class FixedTest(unittest.TestCase):
    def test_fixed(self):
        """Clock produced by the fixed function always returns the same value."""

        c = clock.fixed(datetime.datetime(2016, 1, 18, tzinfo=pytz.utc))
        self.assertEqual(c.now(), clock.DateTimeTs(2016, 1, 18, tzinfo=pytz.utc))
        self.assertEqual(c.now(), clock.DateTimeTs(2016, 1, 18, tzinfo=pytz.utc))


class ClockTest(unittest.TestCase):
    def test_time_func_and_now(self):
        """Standard behavior of now(). Calling it invokes the time function."""
        c = clock.Clock(time_func=lambda: datetime.datetime(2016, 1, 18, tzinfo=pytz.utc))
        self.assertEqual(c.now(), clock.DateTimeTs(2016, 1, 18, tzinfo=pytz.utc))

    def test_with_system_time(self):
        """Clock with system time produces the current time in UTC."""
        c = clock.Clock()
        right_now = datetime.datetime.now(pytz.utc)
        now = c.now()
        self.assertTrue(now - right_now < datetime.timedelta(milliseconds=1))

    def test_non_datetime_raises_an_error(self):
        """Time func which returns a non-datetime raises an error when calling now()."""
        c = clock.Clock(time_func=lambda: 10)
        with self.assertRaises(AssertionError):
            c.now()

    def test_non_utc_time_raises_an_error(self):
        """Time func which returns a non-utc datetime object raises an error when calling now()."""
        c = clock.Clock(time_func=lambda: datetime.datetime(2016, 1, 18))
        with self.assertRaises(AssertionError):
            c.now()


if __name__ == '__main__':
    unittest.main()
