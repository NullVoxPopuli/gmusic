from gmusic.frontend.CursedObject import CursedObject
import curses, threading, sys

class Menu(CursedObject):
    '''A class which abstracts the horrors of building a curses-based menu system'''

    def __init__(self, screen):
        '''Initialization'''
        self.screen = screen
        self.options = None

        # Highlighted and Normal line definitions
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.highlighted = curses.color_pair(1)
        self.normal = curses.A_NORMAL

    def draw(self, selected):
        '''Draw the menu and lines'''
        # Create a box around the screen
        self.screen.box()

        # Add the title and subtitle
        self.screen.addstr(0, 2, self.title, curses.A_BOLD)
        self.print_line(self.subtitle, 2, curses.A_BOLD)

        # get the current width
        self.current_width = self.width()

        # Display all the menu items, showing the 'pos' item highlighted
        for index in range(self.height()-1):
            textstyle = self.normal
            if index == selected:
                textstyle = self.highlighted

            # Use 0 index here, as the tuple pattern is (DISPLAY_STRING, id)
            if index < len(self.options):
                option = self.format_element(self.options[index])
                self.screen.addstr(index+3, 4, "%d.\t%s" % (index+1, option), textstyle)

            # Otherwise print a blank line
            if index > len(self.options)+2:
                self.print_line(' ', index)

        self.screen.refresh()

    def format_element(self, menu_element):
        """Formats a track for display in menu"""
        # Use current width because it's already in mem
        if menu_element.alt is None:
            return self.compress_and_pad(menu_element.main, width=self.current_width-10)

        # if alt is nt none
        main_width = int(self.current_width*2/3)-6
        main = self.format_subelement(menu_element.main, main_width)
        alt_width = int(self.current_width/3)-4
        alt = self.format_subelement(menu_element.alt, alt_width)
        return main + " " + alt

    def format_subelement(self, text, width):
        t = self.compress_text(text.strip(), width)
        if len(t) == 0:
            t = 'Unknown'
        return self.pad_text(t, width)
