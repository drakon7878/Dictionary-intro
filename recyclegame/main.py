import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import pgzrun
import pgzero.screen
import pgzero.actor
import pgzero.rect
import pgzero.keyboard
import pgzero.clock
import random

screen: pgzero.screen.Screen
Actor = pgzero.actor.Actor
Rect = pgzero.rect.Rect
keyboard: pgzero.keyboard.Keyboard
clock = pgzero.clock.Clock
