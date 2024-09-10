import random
from collections import namedtuple
import os

Point = namedtuple('Point', ['x', 'y', 'z'])

def generate_random_value(data_type):
    if data_type == int:
        return random.randint(0, 100)
    elif data_type == float:
        return round(random.uniform(0, 100), 2)
    elif data_type == str:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == chr:
        return random.choice('abcdefghijklmnopqrstuvwxyz')
    elif data_type == Point:
        return Point(round(random.uniform(0, 100), 2),
                     round(random.uniform(0, 100), 2),
                     round(random.uniform(0, 100), 2))

def generate_test_cases(num_cases):
    operations = [
        "ADD", "REMOVE", "ISEMPTY", "GETSIZE", "CLEAR", "GET", "GETINDEX", "ISCONTAIN"
    ]
    data_types = [int, float, str, chr, Point]
    data_type_weights = [1, 1, 1, 1, 3] 
    test_cases = []

    chosen_type = random.choices(data_types, weights=data_type_weights, k=1)[0]
    test_cases.append(f"TYPE:{chosen_type.__name__}")

    list_size = 0
    added_values = []
    current_values = []

    for _ in range(num_cases):
        op = random.choices(operations, weights=[3, 2, 1, 1, 1, 1, 1, 1], k=1)[0]  
        if op == "ADD":
            value = generate_random_value(chosen_type)
            added_values.append(value)
            current_values.append(value)
            if random.random() < 0.7: 
                at = random.randint(0, max(list_size, 1)) 
                test_cases.append(f"ADD value:{value} at:{at}")
                list_size += 1
            else:
                test_cases.append(f"ADD value:{value}")
                list_size += 1
        elif op == "REMOVE":
            if list_size > 0:
                remove_type = random.choices(["at", "value", "first", "last", "out_of_range"], 
                                             weights=[1, 1, 2, 2, 1], k=1)[0]
                if remove_type == "at":
                    at = random.randint(0, list_size - 1)
                    test_cases.append(f"REMOVE at:{at}")
                    if at < len(current_values):
                        current_values.pop(at)
                    list_size -= 1
                elif remove_type == "value":
                    value = random.choice(added_values) if added_values else generate_random_value(chosen_type)
                    test_cases.append(f"REMOVE value:{value}")
                    if value in current_values:
                        current_values.remove(value)
                elif remove_type == "first":
                    test_cases.append(f"REMOVE at:0")
                    if current_values:
                        current_values.pop(0)
                    list_size -= 1
                elif remove_type == "last":
                    test_cases.append(f"REMOVE at:{list_size - 1}")
                    if current_values:
                        current_values.pop()
                    list_size -= 1
                else:  # out_of_range
                    at = random.randint(list_size, list_size + 10)
                    test_cases.append(f"REMOVE at:{at}")
            else:
                test_cases.append(f"REMOVE at:0")  
        elif op in ["ISEMPTY", "GETSIZE", "CLEAR"]:
            test_cases.append(op)
            if op == "CLEAR":
                list_size = 0
                current_values.clear()
        elif op == "GET":
            at = random.randint(0, max(list_size - 1, 0))
            test_cases.append(f"GET at:{at}")
        elif op == "GETINDEX":
            value = random.choice(current_values) if current_values and random.random() < 0.7 else generate_random_value(chosen_type)
            test_cases.append(f"GETINDEX value:{value}")
        elif op == "ISCONTAIN":
            if random.random() < 0.7 and current_values:  
                value = random.choice(current_values)
            else:
                value = generate_random_value(chosen_type)
            test_cases.append(f"ISCONTAIN value:{value}")

    return test_cases

def write_test_cases_to_file(test_cases, filename):
    with open(filename, 'w') as f:
        for case in test_cases:
            f.write(case + '\n')

path_test_folder = 'dsastudents/ArrayTest/test/input/'
if not os.path.exists(path_test_folder):
    os.makedirs(path_test_folder)

for test in range(100):
    for unit in range(1, 8):
        test_cases = generate_test_cases(test)
        write_test_cases_to_file(test_cases, path_test_folder + 'input'+str(7 * test + unit)+'.txt')

print("Đã hoàn thành tạo input")
