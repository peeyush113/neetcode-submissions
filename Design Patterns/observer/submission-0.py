class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.customers = set()
        self.itemName = itemName
        self.stock = stock

    def subscribe(self, observer: Observer) -> None:
        self.customers.add(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self.customers:
            self.customers.remove(observer)

    def updateStock(self, newStock: int) -> None:
        to_notify = set()
        if self.stock == 0 and newStock>0:
            to_notify = self.customers
        
        self.stock = newStock
        
        for c in to_notify:
            c.notify(self.itemName)        
