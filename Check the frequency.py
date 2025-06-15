user_input = input("Enter dictionary in the format key1:value1, key2:value2, ... : ")
test_dict = {}
for item in user_input.split(','):
    try:
        key, value = item.strip().split(':')
        test_dict[key.strip()] = int(value.strip())
    except ValueError:
        print("Invalid entry:", item)
        print("Make sure all entries are in key:value format with numeric values.")
        exit()
try:
    value_to_check = int(input("Enter the value to check frequency of: "))
except ValueError:
    print("Please enter a valid integer value to check.")
    exit()
frequency = list(test_dict.values()).count(value_to_check)
print(f"The value {value_to_check} appears {frequency} times in the dictionary.")