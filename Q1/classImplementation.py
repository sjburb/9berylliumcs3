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

console1 = Console("8th Generation", "Sony", "Playstation 4", 500, f"${399.999}")
console2 = Console("8th Generation", "Microsoft", "Xbox One S", 500, f"${299}")

print("---Before---")
print(console1.console_status())
print(console2.console_status())

print("Changing Console 1..")
console1.upgrade_storage(500)

print("---After---")
print(console1.console_status())
print(console2.console_status())
