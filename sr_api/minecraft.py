class Minecraft:
    def __init__(self, data):
        self.name = data["username"]
        self.full_uuid = data["full_uuid"]
        self.short_uuid = data["trimmed_uuid"]
        self.raw_history = data["name_history"]
