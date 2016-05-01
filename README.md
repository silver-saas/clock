# Clock [![Build Status](https://travis-ci.org/silver-saas/clock.svg?branch=master)](https://travis-ci.org/silver-saas/clock) [![Coverage Status](https://coveralls.io/repos/github/silver-saas/clock/badge.svg?branch=master)](https://coveralls.io/github/silver-saas/clock?branch=master)

Datetime setup useful for IoC usage. Inspired by Dart-quiver's Clock.

The functions and classes of this package are useful when adopting an IoC setup for applications.
The strong dependency of functions and classes on a source of time can be made explicit by using a
Clock class. This can be replaced by a fake in testing, via the fixed function. Or it can be mocked
for even finer grained controls.

The standard usage is:

```python
import clock

class Timer(object):
  def __init__(clock):
    self._clock = clock
    self._start = None
    self._end = None

  def start(self):
    self._start = self._clock.now()
    self._end = None

  def end(self):
    self._end = self._clock.now()

  def duration(self):
    return self._start - self._end

import mockito

def test_works():
  c = mockito.mock()
  when(c.now).thenReturn(_some_date)
  t = Timer(c)
  t.start()
  when(c.now).thenReturn(_some_other_date)
  t.end()
  assert t.duration == _some_other_date - _some_date
```

Also provides the `fromdatetime()` function and `DateTimeTs` class. The latter is used to augment
the `datetime.datetime` class with a `ts` property.
