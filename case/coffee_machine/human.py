import time


class Human:
    def __init__(self, coffe_menu):
        self.menu = coffe_menu

    # 选择咖啡
    def choose_coffee(self) -> int:
        menu = ", ".join([f"{index}: {i.name}" for index, i in enumerate(self.menu)])   # 为用户展示菜单
        while True:
            option = input(f"请输入数字选择咖啡 {menu}:\n")
            if option != "0" and option != "1":
                print("输入错误，请重新输入!")
            else:
                break

        return int(option)

    # 为订单付款，返回付款金额与时间
    def pay(self, option: int):
        want_pay_value = self.menu[option].price
        while True:
            par_value = int(input(f"请投入至少{want_pay_value}元:\n"))
            if par_value < want_pay_value:
                print("您投入的金币面值不足以商品")
            else:
                pay_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                break

        return par_value, pay_time
