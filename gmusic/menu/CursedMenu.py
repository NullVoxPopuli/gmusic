from gmusic.menu.NowPlaying import NowPlaying
from gmusic.menu.CursedObject import CursedObject
from gmusic.menu.CursedUI import CursedUI
from gmusic.menu.Guide import Guide
import curses, threading

class CursedMenu(CursedObject):
    '''A class which abstracts the horrors of building a curses-based menu system'''

    def __init__(self):
        '''Initialization'''
        #self.__start__()
        self.cursed_ui = None
        self.options = None

        # Highlighted and Normal line definitions
        #curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        #self.highlighted = curses.color_pair(1)
        #self.normal = curses.A_NORMAL
        #self.is_drawable = False


    def start(self):
        '''Start up the Menu'''
        self.screen.clear()
        self.screen.refresh()
        self.draw()
        self.is_drawable = True
        #self.launch_ui_thread()

    def draw(self):
        '''Draw the menu and lines'''
        self.clear_rows_below(6)
        self.screen.refresh()

        self.print_line('test', 6, curses.A_BOLD)
        self.print_line('test', 8, curses.A_BOLD)

        selected = 2

        # Display all the menu items, showing the 'pos' item highlighted
        for index in range(10):
            textstyle = self.normal
            if index == selected:
                textstyle = self.highlighted
            self.screen.addstr(9+index, 4, "%d.\t%s" % (index+1, 'test'), textstyle)
        #self.guide.draw()
        self.screen.border(0)
        self.screen.refresh()

    def format_title(self, track):
        """Formats a track for display in menu"""
        song_width = int(self.width()/2)-4
        album_width = int(self.width()/3)-4
        title = self.compress_and_pad(track['title'], width=song_width)
        album = self.compress_and_pad(track['album'], width=album_width)
        return title + " " + album
