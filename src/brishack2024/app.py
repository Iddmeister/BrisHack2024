import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import asyncio
import time

from PIL import Image

import cv2

class BrisHack2024(toga.App):

    async def shit_loop(self, widget):
        print("sup")

        # cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            await asyncio.sleep(0.01)
            print("loop")

            img = Image.fromarray(frame)
            # self.image = toga.Image(img)
            # view = toga.ImageView(self.image)

            # self.main_box.add(view)

            self.view.image = img
            self.main_window.show()


            # self.image = toga.Image(img)
            # cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break

        # cv2.destroyWindow("preview")
        vc.release()


    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box()

        button = toga.Button(
            "Start",
            on_press=self.shit_loop,
            style=Pack(padding=5)
        )

        self.main_box.add(button)

        image = toga.Image("assets/mario.png")
        self.view = toga.ImageView(image)

        self.main_box.add(self.view)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()









        print("wtf")

def main():
    return BrisHack2024()

