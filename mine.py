from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculadoraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.resultado = Label(text=" ", font_size=50)
        layout.add_widget(self.resultado)
        
        botones = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '×'],
            ['C', '0', '=', '÷']
        ]
        
        for fila in botones:
            h_layout = BoxLayout()
            for texto in fila:
                btn = Button(text=texto, font_size=30)
                btn.bind(on_press=self.boton_presionado)
                h_layout.add_widget(btn)
            layout.add_widget(h_layout)
        
        return layout
    
    def boton_presionado(self, instance):
        pass  # Lógica de cálculo aquí

CalculadoraApp().run()
