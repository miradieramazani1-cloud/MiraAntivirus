
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle


class MiraAntivirus(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        with layout.canvas.before:
            Color(0.04, 0.07, 0.15, 1)
            self.background = RoundedRectangle(
                pos=layout.pos,
                size=layout.size
            )

        layout.bind(
            pos=self.update_background,
            size=self.update_background
        )

        title = Label(
            text="[b]MIRA ANTIVIRUS[/b]",
            markup=True,
            font_size=30,
            color=(0.2, 0.9, 0.7, 1),
            size_hint=(1, 0.25)
        )

        subtitle = Label(
            text="Votre sécurité numérique",
            font_size=17,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.15)
        )

        status = Label(
            text="Votre appareil est prêt à être analysé",
            font_size=15,
            color=(0.8, 0.85, 0.9, 1),
            size_hint=(1, 0.2)
        )

        scan_button = Button(
            text="ANALYSER UN FICHIER",
            font_size=18,
            bold=True,
            background_normal="",
            background_color=(0.05, 0.65, 0.5, 1),
            size_hint=(1, 0.18)
        )

        layout.add_widget(Widget(size_hint=(1, 0.08)))
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(status)
        layout.add_widget(scan_button)
        layout.add_widget(Widget(size_hint=(1, 0.14)))

        return layout

    def update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size


if __name__ == "__main__":
    MiraAntivirus().run()
