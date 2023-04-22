from coffee import CoffeeMenu
from machine import Machine
from human import Human


class Run:
    def __init__(self):
        self.menu = CoffeeMenu.menu
        self.machine = Machine(self.menu)
        self.human = Human(self.menu)
        self.run()
        print(self.machine.log_l)

    def run(self, to_do: bool = True):
        if not to_do:
            return self.machine.log_l

        # ------ 展示咖啡 ------
        self.machine.show_coffee()

        # ------ 选择咖啡 ------
        option = self.human.choose_coffee()

        # ------ 投入钱币 ------
        pay_value, pay_time = self.human.pay(option=option)

        # ------ 制作咖啡 ------
        self.machine.make(option)
        self.machine.log(pay_time, self.menu[option], pay_value)

        self.run() if input("是否继续购买？Y：是，N：否:\n") == "Y" else self.run(False)


if __name__ == "__main__":
    Run()
