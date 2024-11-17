import rumps

class MacTrayApp(rumps.App):
    def __init__(self):
        super(MacTrayApp, self).__init__("Mac Tray App", icon="assets/icon/container_2.png")
        self.menu = ["Preferences", "Quit"]

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("This is a preferences window.")

if __name__ == "__main__":
    MacTrayApp().run()