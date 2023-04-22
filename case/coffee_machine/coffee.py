from dataclasses import dataclass


@dataclass
class Coffee:
    name: str
    price: int
    introduce: str


menu = (
    Coffee(name="拿铁", price=20, introduce="浓缩咖啡，牛奶，糖"),
    Coffee(name="美式", price=15, introduce="浓缩咖啡")
)
