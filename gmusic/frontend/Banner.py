# -*- coding: utf-8 -*-
from gmusic.frontend.CursedObject import CursedObject
import curses

class Banner(CursedObject):
    """Now Playing banner written for Curses"""

    def __init__(self, screen):
        self.screen = screen
        self.track = None

    def draw_no_track(self):
        """Draws a blank banner if there's not a song playing"""
        self.center_text('  ', 2)
        self.center_text("Google Music Terminal", 3, curses.A_BOLD)
        self.center_text('  ', 4)

    def draw_track_details(self, is_playing=True, is_random=False):
        """Draws a banner for the current track if it is playing"""
        title_string = self.track['title']
        if not is_playing:
            title_string = '▌▌ ' + title_string 

        self.center_text(title_string, 2, curses.A_BOLD)
        self.center_text(self.track['album'], 3)
        self.center_text(self.track['artist'], 4)

    def draw(self, is_playing=True, is_random=False):
        """Master draw method, checks the new_track to see what to draw"""
        if self.track is None:
            self.draw_no_track()
        else:
            self.draw_track_details(is_playing, is_random)
        self.screen.refresh()
