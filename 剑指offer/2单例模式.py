from threading import Lock, Thread


lock = Lock()


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            with lock:
                if not hasattr(cls, 'instance'):
                    cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


def create_singleton():
    singleton = Singleton()
    print(id(singleton))


class LazySingleton(object):
    __singleton = None

    @classmethod
    def get_singleton(cls):
        if not cls.__singleton:
            cls.__singleton = LazySingleton()
        return cls.__singleton


if __name__ == '__main__':
    t1 = Thread(target=create_singleton,)
    t2 = Thread(target=create_singleton,)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
