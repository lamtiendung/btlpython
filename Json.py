import json

# Hàm để đọc dữ liệu từ file JSON
def load_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found!")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON!")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Hàm để ghi dữ liệu vào file JSON
def save_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename} successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")