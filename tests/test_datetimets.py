import datetime
import unittest

import pytz
import tabletest

import clock


class DateTimeTsTest(tabletest.TableTestCase):
    def test_construction(self):
        """Constructing a DateTimeTs object works like usual."""

        dtm = clock.DateTimeTs(2016, 1, 18, 20, 4, 16, 333, tzinfo=pytz.utc)

        self.assertEqual(dtm.year, 2016)
        self.assertEqual(dtm.month, 1)
        self.assertEqual(dtm.day, 18)
        self.assertEqual(dtm.hour, 20)
        self.assertEqual(dtm.minute, 4)
        self.assertEqual(dtm.second, 16)
        self.assertEqual(dtm.microsecond, 333)
        self.assertEqual(dtm.tzinfo, pytz.utc)

    _ADD_TEST_CASES = [
        {
            'a': clock.fromdatetime(datetime.datetime.fromtimestamp(1000, tz=pytz.utc)),
            'd': datetime.timedelta(seconds=10),
            'r': clock.fromdatetime(datetime.datetime.fromtimestamp(1010, tz=pytz.utc)),
            },
        {
            'a': clock.DateTimeTs(2016, 1, 18, 20, 4, 16, tzinfo=pytz.utc),
            'd': datetime.timedelta(seconds=10),
            'r': clock.DateTimeTs(2016, 1, 18, 20, 4, 26, tzinfo=pytz.utc),
            },
        {
            'a': clock.DateTimeTs(2016, 1, 18, 20, 4, 16, tzinfo=pytz.utc),
            'd': datetime.timedelta(minutes=6, seconds=20),
            'r': clock.DateTimeTs(2016, 1, 18, 20, 10, 36, tzinfo=pytz.utc),
            },
        {
            'a': clock.DateTimeTs(2016, 1, 18, 20, 4, 16, tzinfo=pytz.utc),
            'd': datetime.timedelta(days=10),
            'r': clock.DateTimeTs(2016, 1, 28, 20, 4, 16, tzinfo=pytz.utc),
            },
        ]

    @tabletest.tabletest(_ADD_TEST_CASES)
    def test_add(self, test_case):
        """Test addition produces a DateTimeTs object."""

        self.assertEqual(test_case['a'] + test_case['d'], test_case['r'])

    _TS_TEST_CASES = [
        {
            'dt': clock.fromdatetime(datetime.datetime.fromtimestamp(1000, tz=pytz.utc)),
            'ts': 1000
            },
        {
            'dt': clock.DateTimeTs(2016, 1, 18, 20, 4, 16, tzinfo=pytz.utc),
            'ts': 1453147456
            },
        {
            'dt': clock.DateTimeTs(2016, 1, 18, 20, 4, 16, 333, tzinfo=pytz.utc),
            'ts': 1453147456
            },
        ]

    @tabletest.tabletest(_TS_TEST_CASES)
    def test_ts(self, test_case):
        """Ts property produces milliseconds as output."""
        self.assertEqual(test_case['dt'].ts, test_case['ts'])


class FromDateTimeTest(unittest.TestCase):
    def test_construction(self):
        """Constructing a DateTimeTs object from a datetime object works."""

        dt = datetime.datetime(2016, 1, 18, 20, 4, 16, 333, tzinfo=pytz.utc)
        dtm = clock.fromdatetime(dt)

        self.assertEqual(dtm.year, 2016)
        self.assertEqual(dtm.month, 1)
        self.assertEqual(dtm.day, 18)
        self.assertEqual(dtm.hour, 20)
        self.assertEqual(dtm.minute, 4)
        self.assertEqual(dtm.second, 16)
        self.assertEqual(dtm.microsecond, 333)
        self.assertEqual(dtm.tzinfo, pytz.utc)
