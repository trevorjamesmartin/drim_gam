# TODO implement smarter durability getter and setter - item breaks!
# TODO implement armor and damage scaling with durability for weapon and armor

class Item:
    def __init__(self, name, item_type, *, blueprint, quality, material, durability):
        assert isinstance(name, str)
        self.item_type = item_type
        self.name = name
        self.blueprint = blueprint
        self.quality = quality
        self.material = material
        self.durability  =durability