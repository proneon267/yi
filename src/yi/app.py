"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class yi(toga.App):
    def show_screenshot(self, *args, **kwargs):
        self.widgets["img_view"].image = self.main_window.screen.as_image()
        print(self.main_window.screen.size)

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.ScrollContainer(
            content=toga.Box(
                children=[
                    toga.Button(text="Take Screenshot", on_press=self.show_screenshot),
                    toga.ImageView(id="img_view", style=Pack(flex=1)),
                ],
                style=Pack(direction="column"),
            )
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return yi()
