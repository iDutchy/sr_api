class Minecraft:
    def __init__(self, data):
        self.name = data["username"]
        self.full_uuid = data["full_uuid"]
        self.short_uuid = data["trimmed_uuid"]
        self.raw_history = data["name_history"]

    async def formatted_history(self):
        d = self.raw_history
        
        formatted = ""
        for x in d:
            for k, v in x:
                formatted += f"{v} | {k}\n"
                
        return formatted
    
    async def reversed_formatted_history(self):
        d = self.raw_history
        
        formatted = ""
        for x in d[::-1]:
            for k, v in x:
                formatted += f"{v} | {k}\n"
                
        return formatted
