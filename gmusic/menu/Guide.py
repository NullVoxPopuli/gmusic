# -*- coding: utf-8 -*-
from gmusic.menu.CursedObject import CursedObject
import curses

class Guide(CursedObject):
    """Displays quick shortcuts at the bottom of the screen"""

    def __init__(self):
        pass

    def draw(self):
        row = self.height()-3
        help_string = \
            "↑↓: Nav     "+\
            "Space: ▶/||     "+\
            "n: Next     " +\
            "[ ]: Next/Prev Page     " +\
            "i: Cmd Line"

        self.center_text(help_string,row)
