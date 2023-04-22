from coffee import CoffeeTemplate


class Machine:
    def __init__(self, coffee_menu: tuple):
        self.menu = coffee_menu
        self.log_l = []

    # 展示菜单
    def show_coffee(self):
        for i in self.menu:
            print(f"{i.name}({i.price}元): {i.introduce}")

    # 制作咖啡
    def make(self, option: int):
        print("制作中，请稍候......")
        print(f"{self.menu[option].name} ☕制作完成！")

    # 保存订单记录
    def log(self, pay_time, coffee: CoffeeTemplate, pay_value: int):
        self.log_l.append(f"{pay_time} 订单: {coffee.name}, 支付{pay_value}元, 找零{pay_value - coffee.price}元")
