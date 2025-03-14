# item management with OOP and execptions
class ItemException(Exception):
    """custom exception for item validation"""
    pass

class Item:
    def __init__(self, id: int, name: str, description: str, price: float):
        self.validate_item(id, name, description, price)
        self._id = id
        self._name = name
        self._description = description
        self._price = price
        
    def validate_item(self, id, name, description, price):
        if not isinstance(id, int) or id < 0:
            raise ItemException("ID must be a positive integer")
        if not name or not isinstance(name, str):
            raise ItemException("Name must be a non-empty string")
        if not description or not isinstance(description, str):
            raise ItemException("Description must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ItemException("Price must be a positive number")
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self.validate_item(self._id, value, self._description, self._price)
        self._name = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self.validate_item(self._id, self._name, value, self._price)
        self._description = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self.validate_item(self._id, self._name, self._description, value)
        self._price = value

class ItemManager:
    def __init__(self):
        self.items = {}
            
    def create_item(self, id: int, name: str, description: str, price: float):
        try:
            if id in self.items:
                raise ItemException("Item ID already exists")
            item = Item(id, name, description, price)
            self.items[id] = item
            print(f"Item {id} created successfully")
        except ItemException as e:
            print(f"Error creating item: {e}")
    
    def read_item(self, id: int):
        try:
            if id not in self.items:
                raise ItemException("Item ID does not exist")
            item = self.items[id]
            print(f"\nItem Details:")
            print(f"ID: {item.id}")
            print(f"Name: {item.name}")
            print(f"Description: {item.description}")
            print(f"Price: {item.price}")
        except ItemException as e:
            print(f"Error reading item: {e}")
    
    def update_item(self, id: int, name: str, description: str, price: float):
        try:
            if id not in self.items:
                raise ItemException("Item ID does not exist")
            item = Item(id, name, description, price)
            self.items[id] = item
            print(f"Item {id} updated successfully")
        except ItemException as e:
            print(f"Error updating item: {e}")
            
    def delete_item(self, id: int):
        try:
            if id not in self.items:
                raise ItemException("Item ID does not exist")
            del self.items[id]
            print(f"Item {id} deleted successfully")
        except ItemException as e:
            print(f"Error deleting item: {e}")
            
    def list_items(self):
        if not self.items:
            print("No items found")
            return
        print("\nAll Items:")
        for item in self.items.values():
            print(f"ID: {item.id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")
            
def main():
    manager = ItemManager()
    
    while True:
        print("\n=== Item Management System ===")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List All Items")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
            
            if choice == 1:
                id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(id, name, description, price)
                
            elif choice == 2:
                id = int(input("Enter item ID to read: "))
                manager.read_item(id)
                
            elif choice == 3:
                id = int(input("Enter item ID to update: "))
                name = input("Enter new name: ")
                description = input("Enter new description: ")
                price = float(input("Enter new price: "))
                manager.update_item(id, name, description, price)
                
            elif choice == 4:
                id = int(input("Enter item ID to delete: "))
                manager.delete_item(id)
                
            elif choice == 5:
                manager.list_items()
                
            elif choice == 6:
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError as e:
            print("Invalid input. Please enter correct data types.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()