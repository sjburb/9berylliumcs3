class Console:
    def __init__(self, Generation, Brand, Model, Storage, Price):
        self.__Generation = Generation
        self.__Brand = Brand
        self.Model = Model
        self.__Storage = Storage
        self.Price = Price

    def download_game(self, game_name):
        print(f"Now downloading {game_name}! Please wait...")

    def upgrade_storage(self, storage_addition):
        self.__Storage = self.__Storage + storage_addition

    def console_status(self):
        if self.__Storage >= 1000:
            storage_display = f"{self.__Storage / 1000:.0f}TB"
        else:
            storage_display = f"{self.__Storage}GB"
        return f"""The {self.Model} from the brand {self.__Brand} has the following specifications:
    Generation: {self.__Generation}
    Storage: {storage_display}
    Price: {self.Price}"""

class Games:
    def __init__(self, Title, About, Genre, Storage, Platform):
        self.Title = Title
        self.About = About
        self.Genre = Genre
        self.Storage = Storage
        self.Platform = Platform

    def display_info(self):
        return f"""Game Title: {self.Title}
    About: {self.About}
    Genre: {self.Genre}
    Storage: {self.Storage}GB
    Platform: {self.Platform}"""
    

    def take_storage(self, console):
        if console._Console__Storage >= self.Storage:
            console._Console__Storage -= self.Storage
            print(f"{self.Title} has been downloaded successfully!")
        else:
            print(f"Not enough storage on the console to download {self.Title}.")
    

console1 = Console("8th Generation", "Sony", "Playstation 4", 500, f"${399.999}")
console2 = Console("8th Generation", "Microsoft", "Xbox One S", 500, f"${299}")

game1 = Games("Ghost of Tsushima", "An open-world action-adventure game set in feudal Japan.", "Action-Adventure", 50, "Playstation 4")
game2 = Games("Red Dead Redemption 2", "An epic tale of life in America at the dawn of the modern age.", "Action-Adventure", 100, "Playstation 4")
game3 = Games("The Witcher 3: Wild Hunt", "A story-driven open world RPG set in a visually stunning fantasy universe.", "RPG", 75, "Playstation 4")

gameX1 = Games("Titanfall 2", "A fast-paced multiplayer shooter set in a futuristic universe.", "Shooter", 100, "Xbox One S")
gameX2 = Games("Forza Horizon 4", "An open-world racing game set in a fictionalized version of Great Britain.", "Racing", 80, "Xbox One S")
gameX3 = Games("Grand Theft Auto V", "An open-world action-adventure game set in the fictional state of San Andreas.", "Action-Adventure", 65, "Xbox One S")

print("---Before---")

print(console1.console_status())
print(console2.console_status())

print(f"{console1.Model} Games")
print(game1.display_info())
print(game2.display_info())
print(game3.display_info())

print(f"{console2.Model} Games")
print(gameX1.display_info())
print(gameX2.display_info())
print(gameX3.display_info())

print("---After---")

game1.take_storage(console1)
game2.take_storage(console1)
game3.take_storage(console1)

gameX1.take_storage(console2)
gameX2.take_storage(console2)
gameX3.take_storage(console2)

print(console1.console_status())
print(console2.console_status())

print("The games have been downloaded successfully!")


class GamingConsole(Console):
    def __init__(self, Generation, Brand, Model, Storage, Price, GPU, game):
        super().__init__(Generation, Brand, Model, Storage, Price)
        self.GPU = GPU
        self.game = game

    def gaming_specs(self):
        return f"""The {self.Model} has the following gaming specifications:
    GPU: {self.GPU}"""

gamingconsole1 = GamingConsole("8th Generation", "Sony", "Playstation 4", 500, f"${399.999}", "AMD Radeon", game1)
gamingconsole2 = GamingConsole("8th Generation", "Microsoft", "Xbox One S", 500, f"${299}", "AMD Radeon", gameX1)

print("---Gaming Console Specs---")
print(gamingconsole1.gaming_specs())
print(gamingconsole2.gaming_specs())
print(gamingconsole1.console_status())
print(gamingconsole2.console_status())

print("---Aggregation---")
print(f"{gamingconsole1.Model} is playing {gamingconsole1.game.Title}")
print(f"{gamingconsole2.Model} is playing {gamingconsole2.game.Title}")
