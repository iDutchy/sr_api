class Pokedex:
    __slots__ = ("name", "id", "type", "species", "abilities", "height", "weight", "base_experience", "gender", "egg_groups", "stats", "family", "sprites", "description", "generation")
    def __init__(self, data):
        self.name = data.get('name')
        self.id = data.get('id')
        self.type = data.get('type')
        self.species = data.get('species')
        self.abilities = data.get('abilities')
        self.height = data.get('height')
        self.weight = data.get('weight')
        self.base_experience = data.get('base_experience')
        self.gender = data.get('gender')
        self.egg_groups = data.get('egg_groups')
        self.stats = data.get('stats')
        self.family = data.get('family')
        self.sprites = data.get('sprites')
        self.description = data.get('description')
        self.generation = data.get('generation')

    @property
    def evolutionStage(self):
        return self.stats.get('evolutionStage')

    @property
    def evolutionLine(self):
        return self.stats.get('evolutionLine')

    @property
    def spriteNormal(self):
        return self.stats.get('spriteNormal')

    @property
    def spriteAnimated(self):
        return self.stats.get('spriteAnimated')

    @property
    def attack(self):
        return self.stats.get('attack')

    @property
    def hp(self):
        return self.stats.get('hp')

    @property
    def defense(self):
        return self.stats.get('defense')

    @property
    def sp_atk(self):
        return self.stats.get('sp_atk')

    @property
    def sp_def(self):
        return self.stats.get('sp_def')

    @property
    def speed(self):
        return self.stats.get('speed')

    @property
    def total(self):
        return self.stats.get('total')