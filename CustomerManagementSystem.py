import time
import math
import json

class Customer:
    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"ID: {self.customer_id}, Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class CustomerManagementSystem:
    def __init__(self):
        self.customers = []
        # Khởi tạo khách hàng mặc định nếu không có dữ liệu
        self.default_customers = [
            Customer("1", "John Doe", "123-456-7890", "johndoe@email.com"),
            Customer("2", "Jane Smith", "987-654-3210", "janesmith@email.com"),
            Customer("3", "Robert Brown", "555-444-3333", "robert@email.com")
        ]
        # Tải khách hàng từ file hoặc sử dụng khách hàng mặc định nếu file không tồn tại
        self.load_customers_from_file() 

    # Thêm khách hàng mới
    def add_customer(self):
        try:
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            email = input("Enter customer email: ")
            customer = Customer(customer_id, name, phone, email)
            self.customers.append(customer)
            print("Customer added successfully!")
        except Exception as e:
            print(f"Error while adding customer: {e}")

    # Xem danh sách khách hàng
    def view_customers(self):
        if not self.customers:
            print("No customers available.")
        else:
            print("List of customers:")
            for customer in self.customers:
                print(customer)

    # Sửa thông tin khách hàng
    def edit_customer(self):
        customer_id = input("Enter customer ID to edit: ")
        for customer in self.customers:
            if customer.customer_id == customer_id:
                customer.name = input("Enter new name: ")
                customer.phone = input("Enter new phone number: ")
                customer.email = input("Enter new email: ")
                print("Customer details updated successfully!")
                return
        print("Customer not found!")

    # Xóa khách hàng
    def delete_customer(self):
        customer_id = input("Enter customer ID to delete: ")
        for customer in self.customers:
            if customer.customer_id == customer_id:
                self.customers.remove(customer)
                print("Customer deleted successfully!")
                return
        print("Customer not found!")

    # Tìm khách hàng có ID lớn nhất và nhỏ nhất
    def find_min_max_customer(self):
        if not self.customers:
            print("No customers to find.")
            return
        
        # Tìm khách hàng có ID lớn nhất và nhỏ nhất
        max_customer = max(self.customers, key=lambda x: x.customer_id)
        min_customer = min(self.customers, key=lambda x: x.customer_id)

        print(f"Customer with max ID: {max_customer}")
        print(f"Customer with min ID: {min_customer}")

    # Sắp xếp khách hàng theo ID hoặc tên
    def sort_customers(self):
        if not self.customers:
            print("No customers to sort.")
            return

        print("\n--- Sort customers by ---")
        print("1. ID")
        print("2. Name")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            self.customers.sort(key=lambda x: x.customer_id)
            print("Customers sorted by ID.")
        elif choice == '2':
            self.customers.sort(key=lambda x: x.name.lower())  # Sắp xếp tên không phân biệt chữ hoa chữ thường
            print("Customers sorted by Name.")
        else:
            print("Invalid choice! Please choose '1' for ID or '2' for Name.")
        
        # Hiển thị danh sách khách hàng sau khi sắp xếp
        self.view_customers()

    # Đọc dữ liệu khách hàng từ file
    def load_customers_from_file(self, filename="customers.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    customer = Customer(item['customer_id'], item['name'], item['phone'], item['email'])
                    self.customers.append(customer)
                print(f"Loaded {len(self.customers)} customers from file.")
        except FileNotFoundError:
            print("File not found, loading default customers.")
            # Nếu không có file, sử dụng khách hàng mặc định
            self.customers.extend(self.default_customers)
        except Exception as e:
            print(f"Error loading customers: {e}")

    # Lưu khách hàng vào file
    def save_customers_to_file(self, filename="customers.json"):
        try:
            with open(filename, "w") as file:
                data = [customer.__dict__ for customer in self.customers]
                json.dump(data, file)
                print("Customers saved to file successfully!")
        except Exception as e:
            print(f"Error saving customers: {e}")

    # Menu chính của hệ thống
    def menu(self):
        while True:
            print("\n--- Customer Management System ---")
            print("1. Add new customer")
            print("2. View all customers")
            print("3. Edit customer")
            print("4. Delete customer")
            print("5. Find min/max customer by ID")
            print("6. Sort customers")
            print("7. Save customers to file")
            print("8. Load customers from file")
            print("9. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_customer()
            elif choice == '2':
                self.view_customers()
            elif choice == '3':
                self.edit_customer()
            elif choice == '4':
                self.delete_customer()
            elif choice == '5':
                self.find_min_max_customer()
            elif choice == '6':
                self.sort_customers()  # Gọi hàm sắp xếp khách hàng
            elif choice == '7':
                self.save_customers_to_file()
            elif choice == '8':
                self.load_customers_from_file()
            elif choice == '9':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

# Chạy chương trình
if __name__ == "__main__":
    cms = CustomerManagementSystem()
    cms.menu()