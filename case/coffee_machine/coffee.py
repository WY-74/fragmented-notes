from dataclasses import dataclass


@dataclass
class CoffeeTemplate:
    name: str
    price: int
    introduce: str


class CoffeeMenu:
    menu = (
        CoffeeTemplate(name="拿铁", price=20, introduce="浓缩咖啡，牛奶，糖"),
        CoffeeTemplate(name="美式", price=15, introduce="浓缩咖啡")
    )
