from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int) or number_of_sim < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim >= 1:
            self.__number_of_sim = number_of_sim
        else:
            return ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

