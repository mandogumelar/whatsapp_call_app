from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import webbrowser

# Ganti dengan nomor WhatsApp kamu
PHONE_NUMBER = "+6282220235459"  # contoh +62 untuk Indonesia

class MainLayout(BoxLayout):
    def call_voice(self):
        # membuka chat WhatsApp (anak harus tekan Call sendiri)
        webbrowser.open(f"https://wa.me/{PHONE_NUMBER}")

    def call_video(self):
        # membuka chat WhatsApp (anak harus tekan Video Call sendiri)
        webbrowser.open(f"https://wa.me/{PHONE_NUMBER}")

class WhatsAppCallApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    WhatsAppCallApp().run()

