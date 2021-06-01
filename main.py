import os
import shutil

current_directory = input("Enter directory: ")

result = os.listdir(current_directory)
count = 0
for root, dirs, files in os.walk(current_directory):
    for dir in dirs:
        if dir == 'node_modules':
            current_node_modules_path = os.path.join(root, dir)
            if os.path.exists(current_node_modules_path) and os.path.isdir(current_node_modules_path):
                shutil.rmtree(current_node_modules_path, ignore_errors=True)
            count = + 1

print(f"You removed {count} node_modules")
