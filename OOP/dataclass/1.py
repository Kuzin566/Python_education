from dataclasses import dataclass

from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    balance: int
    last_name: str


jack = Customer('Николай', 500, 'Кузин')
print(jack)
print(jack.name, jack.balance)

from dataclasses import dataclass


@dataclass()
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1


desk = InventoryItem('Computer desk', 1000, 12)
pen = InventoryItem(name='Коля', quantity=2)
monitor = InventoryItem('Monitor', 300)
clock = InventoryItem('Clock', quantity=10)
print(desk)
print(pen)
print(monitor)
print(clock)



from dataclasses import dataclass, field


@dataclass(order=True)
class User:
    name: str = field(compare=False)
    rating: field(compare=False, default=1.5)
    age: int


bob = User('Bob', 18, 77)
ash = User('Ash', 25, 100)
ken = User('Ken', 25, 120)
wolter = User('Wolter', 24, 120)
print(ash > bob)
print(ash > ken)
print(ash > wolter)
