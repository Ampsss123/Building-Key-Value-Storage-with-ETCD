from etcd import Client
from etcd import EtcdConnectionFailed

# Initialize etcd client
client = Client(host='127.0.0.2', port=2369)

def list_keys():
    """
    List all keys in etcd.
    """
    try:
        keys = []
        for key, _ in client.get_prefix('').kvs:
            keys.append(key.decode())
        return keys
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_value(key):
    """
    Get the value for a specific key.
    """
    try:
        value, _ = client.get(key)
        if value is not None:
            return value.decode()
        else:
            return None
    except KeyError:
        print(f"Key '{key}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def put_key_value(key, value):
    """
    Put a key-value pair into etcd.
    """
    try:
        client.write(key, value)
        print(f"Key '{key}' with value '{value}' successfully added to etcd.")
    except Exception as e:
        print(f"Error: {e}")

def delete_key(key):
    """
    Delete a key-value pair from etcd.
    """
    try:
        client.delete(key)
        print(f"Key '{key}' successfully deleted from etcd.")
    except KeyError:
        print(f"Key '{key}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Command-line user interface
if _name_ == "_main_":
    while True:
        print("\nOptions:")
        print("1. List all keys")
        print("2. Get value for a specific key")
        print("3. Put a key-value pair")
        print("4. Delete a key-value pair")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            keys = list_keys()
            if keys:
                print("All keys:")
                for key in keys:
                    print(key)
        elif choice == "2":
            specific_key = input("Enter the key you want to retrieve the value for: ")
            value = get_value(specific_key)
            if value:
                print(f"Value for key '{specific_key}': {value}")
        elif choice == "3":
            new_key = input("Enter the new key: ")
            new_value = input("Enter the value for the new key: ")
            put_key_value(new_key, new_value)
        elif choice == "4":
            key_to_delete = input("Enter the key you want to delete: ")
            delete_key(key_to_delete)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")