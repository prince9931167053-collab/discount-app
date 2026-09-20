import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.utils import platform

class VoiceDiscountApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

        layout.add_widget(Label(
            text="Bolne Wala Discount App",
            font_size="22sp",
            bold=True,
            size_hint=(1, 0.15)
        ))

        self.price_box = TextInput(
            hint_text="Asli Daam (e.g. 1000)",
            multiline=False,
            input_filter='float',
            font_size="18sp",
            size_hint=(1, 0.15)
        )
        layout.add_widget(self.price_box)

        self.disc_box = TextInput(
            hint_text="Discount % (1 se 50)",
            multiline=False,
            input_filter='int',
            font_size="18sp",
            size_hint=(1, 0.15)
        )
        layout.add_widget(self.disc_box)

        btn = Button(
            text="Hisab Nikalo & Suno",
            font_size="20sp",
            background_color=(0.1, 0.6, 1, 1),
            size_hint=(1, 0.15)
        )
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)

        self.result = Label(
            text="Result yahan aayega",
            font_size="18sp",
            size_hint=(1, 0.4)
        )
        layout.add_widget(self.result)

        return layout

    def play_voice(self, text_to_speak):
        try:
            if platform == 'android':
                from jnius import autoclass
                Locale = autoclass('java.util.Locale')
                TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                
                tts = TextToSpeech(PythonActivity.mActivity, None)
                tts.setLanguage(Locale("hi", "IN"))
                tts.speak(text_to_speak, TextToSpeech.QUEUE_FLUSH, None)
            else:
                print("Voice:", text_to_speak)
        except Exception as e:
            print("Voice error:", e)

    def calculate(self, instance):
        p_text = self.price_box.text.strip()
        d_text = self.disc_box.text.strip()

        if not p_text or not d_text:
            self.result.text = "Dono box me number bharein!"
            self.result.color = (1, 0.3, 0.3, 1)
            return

        daam = float(p_text)
        discount = int(d_text)

        if discount < 1 or discount > 50:
            self.result.text = "Discount sirf 1% se 50% ke beech likhein!"
            self.result.color = (1, 0.3, 0.3, 1)
            return

        bachat = daam * (discount / 100)
        final_bill = daam - bachat

        self.result.text = f"Discount ({discount}%): -Rs {bachat:.2f}\nAapko dena hai: Rs {final_bill:.2f}"
        self.result.color = (0.2, 1, 0.2, 1)

        awaaz_msg = f"Aapko {discount} percent discount mila hai. Aapko kul {int(final_bill)} rupaye dene hain."
        threading.Thread(target=self.play_voice, args=(awaaz_msg,)).start()

VoiceDiscountApp().run()
