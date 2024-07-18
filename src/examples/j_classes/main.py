from src.examples.j_classes.customer import Customer
from src.examples.j_classes.menu import run_menu

customers = []

customer1 = Customer(100, 50)
customer2 = Customer(1000, 500)
customer3 = Customer(10000, 5000)

customers.append(customer1)
customers.append(customer2)
customers.append(customer3)

run_menu(customers)


