from .Page import Page

class Home(Page):
    def show(self):
        with open(self.VIEWS_PATH + '\\homepage_view.htm') as file:
            content = file.read()
        return content