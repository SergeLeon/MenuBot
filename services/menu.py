from csv import DictReader, DictWriter

from config import MENU_CSV
import logger

logger = logger.get_logger(__name__)


class Menu:
    def __init__(self):
        self.items: list[dict[str]] = list()
        self.read()

    def __str__(self):
        items_str = list()
        for item_dict in self:
            item_tuple = tuple(item_dict.items())
            if not item_tuple[-1][1]:
                continue

            item_str = "\n".join(f"{key}: {value}" for key, value in item_tuple[:-1])

            items_str.append(item_str)

        return "\n\n".join(items_str)

    def __getitem__(self, item):
        return self.items[item]

    def append(self, item):
        self.items.append(item)

    def __delitem__(self, key):
        del self.items[key]

    def read(self):
        with open(MENU_CSV, "r") as csv_file:
            reader = DictReader(csv_file)
            menu = list(reader)
        for item_dict in menu:
            active = tuple(item_dict.items())[-1]
            active_name = active[0]
            active_value = active[1]
            item_dict[active_name] = int(active_value) if active_value.isnumeric() else 1
        self.items = menu
        logger.debug(f"Menu read from: {MENU_CSV}")

    def save(self) -> None:
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
