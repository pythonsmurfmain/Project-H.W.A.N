class MainPage:
    @staticmethod
    def shift(window):
        window.destroy()
        from Main_chatbot import Main_chatbot
        Main_chatbot()

class pulse:
    @staticmethod
    def shift(window):
        window.destroy()
        from Pulse import Pulse
        Pulse()

class AidSync:
    @staticmethod
    def shift(window):
        window.destroy()
        from Aid_sync import Aid_sync
        Aid_sync()


class synczen:
    @staticmethod
    def shift(window):
        window.destroy()
        from SyncZen import SyncZen
        SyncZen()
