from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class BoxLayoutDemo(App):
    grade = StringProperty()

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_all(self):
        self.root.ids.output_label.text = self.root.ids.input_name.text = ''

    def calculate_grade(self):
        try:
            score = int(self.root.ids.input_score.text)
            if score < 50:
                self.grade = "Fail"
            elif score < 65:
                self.grade = "Pass"
            elif score < 75:
                self.grade = "Credit"
            elif score < 85:
                self.grade = "Distinction"
            elif score <= 100:
                self.grade = "High Distinction"
        except ValueError:
            self.grade = "Invalid input"


BoxLayoutDemo().run()
