from csv import DictReader, DictWriter

from config import MENU_CSV
import logger

logger = logger.get_logger(__name__)


class Menu:
    def __init__(self):
        self.items: list[dict[str]] = list()
        self.read_menu()

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Menu, cls).__new__(cls)
    #     return cls.instance

    def __str__(self):
        items_str = list()
        for item_dict in self.items:
            if not item_dict["active"]:
                continue

            item_tuple = tuple(item_dict.items())[:-1]
            item_str = "\n".join(f"{key}: {value}" for key, value in item_tuple)

            items_str.append(item_str)

        return "\n\n".join(items_str)

    def __repr__(self):
        items_str = list()
        for num, item_dict in enumerate(self.items):
            item_str = " ".join(f"{key}:{value}" for key, value in item_dict.items())

            items_str.append(f"number: {num}\n{item_str}")

        return "\n\n".join(items_str)

    def read_menu(self):
        with open(MENU_CSV, "r") as csv_file:
            reader = DictReader(csv_file)
            menu = list(reader)
        for item in menu:
            item["active"] = int(item["active"]) if item["active"].isnumeric() else 1
        self.items = menu
        logger.debug(f"Menu read from: {MENU_CSV}")

    def save_menu(self) -> None:
        with open(MENU_CSV, "w", newline='') as csv_file:
            fieldnames = self.items[0].keys()
            writer = DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in self.items:
                writer.writerow(item)
        logger.debug(f"Menu saved to: {MENU_CSV}")


Menu = Menu()

if __name__ == "__main__":
    print(Menu)
