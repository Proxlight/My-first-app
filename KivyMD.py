from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

KV = '''
Screen:
    MDRaisedButton:
        text: "Click Me"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.show_alert_dialog()
'''

class SimpleApp(MDApp):
    dialog = None

    def build(self):
        screen = Builder.load_string(KV)
        return screen

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="KivyMD",
                text="Hello! This is a KivyMD dialog.",
                buttons=[
                    MDRaisedButton(
                        text="CLOSE",
                        on_release=self.close_dialog
                    )
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

if __name__ == "__main__":
    SimpleApp().run()
