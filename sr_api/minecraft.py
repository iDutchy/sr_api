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
            formatted += f"{x['changedToAt'].replace('Origanal', 'Original')} >> {x['name']}\n"
                
        return formatted
    
    async def reversed_formatted_history(self):
        d = self.raw_history
        
        formatted = ""
        for x in d[::-1]:
            formatted += f"{x['changedToAt'].replace('Origanal', 'Original')} >> {x['name']}\n"
                
        return formatted
