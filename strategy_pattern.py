import abc


# -----------------------------------------------
class IQuackBehavior(abc.ABC):
    @abc.abstractmethod
    def run():
        pass


class LoudQuacking(IQuackBehavior):
    def run(self):
        print(f'QUACK: {self.__class__.__name__}')


class NoQuacking(IQuackBehavior):
    def run(self):
        print(f'QUACK: {self.__class__.__name__}')


# -----------------------------------------------
class IFlyBehavior(abc.ABC):
    @abc.abstractmethod
    def run():
        pass


class SimpleFlying(IFlyBehavior):
    def run(self):
        print(f'FLY: {self.__class__.__name__}')


class JetFlying(IFlyBehavior):
    def run(self):
        print(f'FLY: {self.__class__.__name__}')


# -----------------------------------------------
class IDisplayBehavior(abc.ABC):
    @abc.abstractmethod
    def run():
        pass


class PrintDisplaying(IDisplayBehavior):
    def run(self):
        print(f'DISPLAY: {self.__class__.__name__}')


class ScreenDisplaying(IDisplayBehavior):
    def run(self):
        print(f'DISPLAY: {self.__class__.__name__}')


# -----------------------------------------------
class Prototype(abc.ABC):
    def __new__(cls, *args, **kwargs):
        parent = cls.mro()[1]
        for behavior, interface in parent.behaviors.items():
            assert issubclass(cls.behaviors[behavior], interface)
        return super().__new__(cls, *args, **kwargs)

    def __getattr__(self, attr):
        return self.behaviors.get(attr)().run


# -----------------------------------------------
class DuckPrototype(Prototype):
    behaviors = {
        'quack': IQuackBehavior,
        'fly': IFlyBehavior,
        'display': IDisplayBehavior,
    }


class MountainDuck(DuckPrototype):
    behaviors = {
        'quack': LoudQuacking,
        'fly': JetFlying,
        'display': PrintDisplaying,
    }


class CloudDuck(DuckPrototype):
    behaviors = {
        'quack': NoQuacking,
        'fly': JetFlying,
        'display': PrintDisplaying,
    }


class RubberDuck(DuckPrototype):
    behaviors = {
        'quack': NoQuacking,
        'fly': SimpleFlying,
        'display': ScreenDisplaying,
    }


# -----------------------------------------------
flock = (RubberDuck(), MountainDuck(), CloudDuck())
for duck in flock:
    print(f'\n\n  <<< {duck.__class__.__name__} >>>')
    duck.quack()
    duck.fly()
    duck.display()
