import pygame
from pygame.locals import *
import sys

from source.library.ui import keyboard
from source.library.ui import joystick

class Controller:
    def __init__(self):
        keyboard.KEY_ESCAPE.subscribe(self)
        pass

    def on_quit(self):
        pygame.quit()
        sys.exit()
        pass

    def on_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_quit()
            keyboard.KEYBOARD.key_event(event)
            joystick.JOYSTICK.joystick_event(event)
        pass

    def on_keydown_escape(self):
        pass

    def on_keyup_escape(self):
        self.on_quit()

    def on_loop(self):
        while True:
            self.on_event()
            self.on_render()
            self.clock.tick(self.frames_per_second)
            self.universe.on_loop()
        pass
