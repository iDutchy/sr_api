class Definition:
    __slots__ = ("word", "definition")
    def __init__(self, data):
        self.word = data.get('word')
        self.definition = data.get('definition')
