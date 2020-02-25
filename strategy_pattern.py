import abc


# -----------------------------------------------
class IQuackBehavior(abc.ABC):
    @abc.abstractmethod
    def quack():
        pass


class LoudQuacking(IQuackBehavior):
    def quack(self):
        print(f'QUACK: {self.__class__.__name__}')


class NoQuacking(IQuackBehavior):
    def quack(self):
        print(f'QUACK: {self.__class__.__name__}')


# -----------------------------------------------
class IFlyBehavior(abc.ABC):
    @abc.abstractmethod
    def fly():
        pass


class SimpleFlying(IFlyBehavior):
    def fly(self):
        print(f'FLY: {self.__class__.__name__}')


class JetFlying(IFlyBehavior):
    def fly(self):
        print(f'FLY: {self.__class__.__name__}')


# -----------------------------------------------
class IDisplayBehavior(abc.ABC):
    @abc.abstractmethod
    def display():
        pass


class PrintDisplaying(IDisplayBehavior):
    def display(self):
        print(f'DISPLAY: {self.__class__.__name__}')


class ScreenDisplaying(IDisplayBehavior):
    def display(self):
        print(f'DISPLAY: {self.__class__.__name__}')


# -----------------------------------------------
class Duck:
    behaviors = {
        'quack': IQuackBehavior,
        'fly': IFlyBehavior,
        'display': IDisplayBehavior,
    }

    def __init__(self, quack, fly, display):
        assert issubclass(quack, Duck.behaviors['quack'])
        assert issubclass(fly, Duck.behaviors['fly'])
        assert issubclass(display, Duck.behaviors['display'])
        self._quack = quack
        self._fly = fly
        self._display = display

    def quack(self):
        self._quack().quack()

    def fly(self):
        self._fly().fly()

    def display(self):
        self._display().display()


class MountainDuck(Duck):
    behaviors = {
        'quack': LoudQuacking,
        'fly': JetFlying,
        'display': PrintDisplaying,
    }

    def __init__(self):
        super().__init__(**self.behaviors)


class CloudDuck(Duck):
    behaviors = {
        'quack': NoQuacking,
        'fly': JetFlying,
        'display': PrintDisplaying,
    }

    def __init__(self):
        super().__init__(**self.behaviors)


class RubberDuck(Duck):
    behaviors = {
        'quack': NoQuacking,
        'fly': SimpleFlying,
        'display': ScreenDisplaying,
    }

    def __init__(self):
        super().__init__(**self.behaviors)


# -----------------------------------------------
print('\n\n <<< rubber duck >>>')
rubber_duck = RubberDuck()
rubber_duck.quack()
rubber_duck.fly()
rubber_duck.display()


print('\n\n <<< mountain duck >>>')
mountain_duck = MountainDuck()
mountain_duck.quack()
mountain_duck.fly()
mountain_duck.display()


print('\n\n <<< cloud duck >>>')
cloud_duck = CloudDuck()
cloud_duck.quack()
cloud_duck.fly()
cloud_duck.display()
