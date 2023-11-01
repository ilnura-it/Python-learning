class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        
        
    def speak(self):
        return f"{self.name} said: I got it"

villager = NPC("Bob", 100, 12)
print(villager.name)  # Bob
print(villager.hp)  # 100
print(villager.level)  # 12
print(villager.speak())