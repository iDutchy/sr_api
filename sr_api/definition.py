class Definition:
    __slots__ = ("word", "definition")

    def __init__(self, data):
        self.word = data['word']
        self.definition = data['definition']
