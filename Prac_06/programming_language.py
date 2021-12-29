class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, name, typing, reflection, year):
        """
        Initialise a programming language instance
        name: string, name of the programming language
        typing: string, static or dynamic
        reflection: string, Yes or No
        year: int, created year
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
