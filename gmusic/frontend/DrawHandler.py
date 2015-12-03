from gmusic.frontend.CursedObject import CursedObject
from gmusic.frontend.Menu import Menu
from gmusic.frontend.UI import UI
from gmusic.frontend.Guide import Guide
from gmusic.frontend.Banner import Banner
import threading

class DrawHandler(CursedObject):
    def __init__(self, cache, state):
        self.cache = cache
        self.state = state

    def launch(self, command_parser, ui_parser):
        self.start()
        self.create_system()
        self.screen.clear()
        self.screen.refresh()
        self.draw()
        self.launch_ui_thread(command_parser, ui_parser)

    def create_system(self):
        '''Builds all of the components and sends them the unified screen'''
        self.banner = Banner(self.screen)
        self.menu = Menu(self.screen)
        self.guide = Guide(self.screen)

    def launch_ui_thread(self, command_parser, ui_parser):
        """Launches a UI thread"""
        ui = UI(self, command_parser, ui_parser)
        ui_thread = threading.Thread(target=ui.__running__)
        ui_thread.start()

    def draw(self):
        self.update_menu()
        self.redraw()

    def update_menu(self):
        self.menu.options = self.state.page_elements
        self.menu.title = self.state.title
        self.menu.subtitle = self.state.subtitle

    def redraw(self):
        self.menu.draw(selected=self.state.selected_element)
        self.banner.draw()
        self.guide.draw()

    def receive_ui_event(self, event):
        pass
