import json

class Grocery_Items:
    def __init__(self, name, category, price, priority):
        self.name=name
        self.category=category
        self.price=price
        self.priority=priority

    def display_items(self):
        print("Name: ", self.name)
        print("Category: ", self.category)
        print("Price: ", self.price)
        print("Priority: ", self.priority)
        print("----------------------------")

class Grocery_Planner():
    def __init__(self, budget):
        self.budget = budget
        self.items = []

    def add_item(self):
        name = self.get_valid_name()
        category = self.get_valid_category()
        price = self.get_valid_price()
        priority = self.get_valid_priority()
        item = Grocery_Items(name, category, price, priority)
        self.items.append(item)
        print("Item added successfully.")
        self.save_data()

    def view_items(self):
        if len(self.items) == 0:
            print("No grocery items added yet.")
        else:
            for item in self.items:
                item.display_items()

    def calculate_total(self):
        total = 0
        for item in self.items:
            total = total + item.price
        return total
    
    def check_budget(self):
        total = self.calculate_total()
        if total > self.budget:
            print("Budget exceeded")
            print("Exceeded by:", total - self.budget)
        else:
            print("Within budget")
            print("Remaining budget:", self.budget - total)

    def Category_Summary(self):
        Category_total={}
        for each_category in self.items:
            if each_category.category not in Category_total:
                Category_total[each_category.category]=each_category.price 
            else:
                Category_total[each_category.category]+=each_category.price
        return Category_total

    def Get_Suggestions(self):
        total = self.calculate_total()
        if total > self.budget:
            print("Budget exceeded by: ", total - self.budget)
            print("Optional items: ")
            for item in self.items:
                if item.priority == "Optional":
                     print(item.name, "-", item.price)
        else:
            print("You are within your budget.")

    def update_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                new_price = self.get_valid_price()
                item.price = new_price
                print("Price updated successfully.")
                self.save_data()
                break
        else:
            print("Item not found.")

    def remove_items(self, item_name):
        found=False
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.save_data()
                found=True
                break
        if found==False:
            print("Item not found.")

    def get_valid_price(self):
        while True:
            try:
                price=int(input("Enter the Price: "))
                if price <= 0:
                    print("Price must be greater than 0")
                    continue
                return price
            except ValueError:
                print("Invalid price. Please enter the number.")

    def get_valid_name(self):
        while True:
            name = input("Enter item name: ")
            if name.strip() == "":
                print("Item name cannot be empty.")
                continue
            return name

    def get_valid_category(self):
        categories = ["Food", "Dairy", "Snacks", "Beverages", "Personal Care"]
        while True:
            category = input("Enter category: ")
            if category in categories:
                return category
            print("Invalid category.")
            print("Available categories:", categories)

    def get_valid_priority(self):
        while True:
            priority = input("Enter priority: ")
            if priority == "Essential" or priority == "Optional":
                return priority
            print("Priority must be Essential or Optional.")

    def save_data(self):
        data = {
            "budget": self.budget,
            "items": []
        }
        for item in self.items:
            item_data = {
                "name": item.name,
                "category": item.category,
                "price": item.price,
                "priority": item.priority
            }
            data["items"].append(item_data)
        with open("grocery_data.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully.")

    def load_data(self):
        try:
            with open("grocery_data.json", "r") as file:
                data = json.load(file)
            self.budget = data["budget"]
            for item_data in data["items"]:
                item = Grocery_Items(
                    item_data["name"],
                    item_data["category"],
                    item_data["price"],
                    item_data["priority"]
                )
                self.items.append(item)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

def get_valid_budget():
    while True:
        try:
            budget = int(input("Enter your grocery budget: "))
            if budget <= 0:
                print("Budget must be greater than 0.")
                continue
            return budget
        except ValueError:
            print("Invalid budget. Please enter a number.")

import os
if os.path.exists("grocery_data.json"):
    Planner = Grocery_Planner(0)
    Planner.load_data()
else:
    budget = get_valid_budget()
    Planner = Grocery_Planner(budget)

while True:
    print("\n===== Smart Grocery Budget Planner =====")
    print("add      - Add a grocery item")
    print("view     - View all items")
    print("total    - Calculate total")
    print("budget   - Check budget")
    print("summary  - Category summary")
    print("suggest  - Get suggestions")
    print("update   - Update item")
    print("remove   - Remove item")
    print("save     - Save data")
    print("exit     - Exit")

    choice = input("\nEnter command: ").lower()

    if choice == "add":
        Planner.add_item()

    elif choice == "view":
        Planner.view_items()

    elif choice == "total":
        print("Total:", Planner.calculate_total())

    elif choice == "budget":
        Planner.check_budget()

    elif choice == "summary":
        print(Planner.Category_Summary())

    elif choice == "suggest":
        Planner.Get_Suggestions()

    elif choice == "update":
        item_name = Planner.get_valid_name()
        Planner.update_item(item_name)

    elif choice == "remove":
        item_name = Planner.get_valid_name()
        Planner.remove_items(item_name)

    elif choice == "exit":
        Planner.save_data()
        print("Thank you for using Smart Grocery Budget Planner.")
        break

    else:
        print("Invalid command. Please try again.")