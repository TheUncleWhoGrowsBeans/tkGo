from functools import wraps
from threading import Thread


class ThreadRun(object):
    def __init__(self):
        pass

    def __call__(self, f):
        @wraps(f)
        def wrapped_f(*args, **kw):
            t = Thread(
                target=f,
                args=args,
                kwargs=kw
            )
            t.start()

        return wrapped_f
        