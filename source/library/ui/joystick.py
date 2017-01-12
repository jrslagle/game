import pygame

class Joystick:
    subscribers = []
    joystick    = None
    name        = None

    dead_zone   = 0.20

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def __init__(self):
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            self.joystick = pygame.joystick.Joystick(i)
            self.joystick.init()
            self.name = self.joystick.get_name()

    def joystick_event(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            self.on_button_down()
        if event.type == pygame.JOYBUTTONUP:
            self.on_button_up()
        if event.type == pygame.JOYAXISMOTION:
            self.on_axis_motion()
        #if event.type == pygame.JOYBALLMOTION:
            #print("Joystick Ball Motion.")
        if event.type == pygame.JOYHATMOTION:
            self.on_hat_motion()
        pass

    def on_axis_motion(self):
        axes = self.joystick.get_numaxes()
        for axis in range(axes):
            if axis == 0:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    AXIS_0.press(value)
                else:
                    AXIS_0.press(0)
            if axis == 1:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    AXIS_1.press(value)
                else:
                    AXIS_1.press(0)
            if axis == 2:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    AXIS_2.press(value)
                else:
                    AXIS_2.press(0)
            if axis == 3:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    AXIS_3.press(value)
                else:
                    AXIS_3.press(0)

    def on_hat_motion(self):
        hats = self.joystick.get_numhats()
        for hat in range(hats):
            direction = self.joystick.get_hat(hat)
            if direction[0] == -1:
                HAT_LEFT.down()
            if direction[0] == 1:
                HAT_RIGHT.down()
            if direction[1] == 1:
                HAT_UP.down()
            if direction[1] == -1:
                HAT_DOWN.down()
        pass

    def on_button_down(self):
        buttons = self.joystick.get_numbuttons()
        for button in range(buttons):
            if button == 0 and self.joystick.get_button(button):
                BUTTON_0.down()
            if button == 1 and self.joystick.get_button(button):
                BUTTON_1.down()
            if button == 2 and self.joystick.get_button(button):
                BUTTON_2.down()
            if button == 3 and self.joystick.get_button(button):
                BUTTON_3.down()
            if button == 4 and self.joystick.get_button(button):
                BUTTON_4.down()
            if button == 5 and self.joystick.get_button(button):
                BUTTON_5.down()
            if button == 6 and self.joystick.get_button(button):
                BUTTON_6.down()
            if button == 7 and self.joystick.get_button(button):
                BUTTON_7.down()
            if button == 8 and self.joystick.get_button(button):
                BUTTON_8.down()
            if button == 9 and self.joystick.get_button(button):
                BUTTON_9.down()
            if button == 10 and self.joystick.get_button(button):
                BUTTON_10.down()
            if button == 11 and self.joystick.get_button(button):
                BUTTON_11.down()

    def on_button_up(self):
        buttons = self.joystick.get_numbuttons()
        for button in range(buttons):
            if button == 0 and self.joystick.get_button(button) == 0:
                BUTTON_0.up()
            if button == 1 and self.joystick.get_button(button) == 0:
                BUTTON_1.up()
            if button == 2 and self.joystick.get_button(button) == 0:
                BUTTON_2.up()
            if button == 3 and self.joystick.get_button(button) == 0:
                BUTTON_3.up()
            if button == 4 and self.joystick.get_button(button) == 0:
                BUTTON_4.up()
            if button == 5 and self.joystick.get_button(button) == 0:
                BUTTON_5.up()
            if button == 6 and self.joystick.get_button(button) == 0:
                BUTTON_6.up()
            if button == 7 and self.joystick.get_button(button) == 0:
                BUTTON_7.up()
            if button == 8 and self.joystick.get_button(button) == 0:
                BUTTON_8.up()
            if button == 9 and self.joystick.get_button(button) == 0:
                BUTTON_9.up()
            if button == 10 and self.joystick.get_button(button) == 0:
                BUTTON_10.up()
            if button == 11 and self.joystick.get_button(button) == 0:
                BUTTON_11.up()

class Axis0:
    subscribers = []
    value = 0

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def press(self, value):
        self.value = value
        for subscriber in self.subscribers:
            subscriber.on_axis_0(value)
        pass

class Axis1:
    subscribers = []
    value = 0

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def press(self, value):
        self.value = value
        for subscriber in self.subscribers:
            subscriber.on_axis_1(value)
        pass

class Axis2:
    subscribers = []
    value = 0

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def press(self, value):
        self.value = value
        for subscriber in self.subscribers:
            subscriber.on_axis_2(value)
        pass

class Axis3:
    subscribers = []
    value = 0

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def press(self, value):
        self.value = value
        for subscriber in self.subscribers:
            subscriber.on_axis_3(value)
        pass

class Button0:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_0_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_0_down()
        pass

class Button1:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_1_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_1_down()
        pass

class Button2:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_2_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_2_down()
        pass

class Button3:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_3_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_3_down()
        pass

class Button4:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_4_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_4_down()
        pass

class Button5:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_5_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_5_down()
        pass

class Button6:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_6_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_6_down()
        pass

class Button7:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_7_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_7_down()
        pass

class Button8:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_8_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_8_down()
        pass

class Button9:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_9_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_9_down()
        pass

class Button10:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_10_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_10_down()
        pass

class Button11:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_button_11_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_button_11_down()
        pass

class HatUp:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_hatup_up()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_hatdown_up()
        pass

class HatDown:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_hatup_down()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_hatdown_down()
        pass

class HatLeft:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_hatup_left()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_hatdown_left()
        pass

class HatRight:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_hatup_right()
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_hatdown_right()
        pass

JOYSTICK = Joystick()
AXIS_0   = Axis0()
AXIS_1   = Axis1()
AXIS_2   = Axis2()
AXIS_3   = Axis3()

BUTTON_0  = Button0()
BUTTON_1  = Button1()
BUTTON_2  = Button2()
BUTTON_3  = Button3()
BUTTON_4  = Button4()
BUTTON_5  = Button5()
BUTTON_6  = Button6()
BUTTON_7  = Button7()
BUTTON_8  = Button8()
BUTTON_9  = Button9()
BUTTON_10 = Button10()
BUTTON_11 = Button11()

HAT_UP    = HatUp()
HAT_DOWN  = HatDown()
HAT_LEFT  = HatLeft()
HAT_RIGHT = HatRight()
