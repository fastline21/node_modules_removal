import os
import shutil
import json
from datetime import datetime
from tqdm import tqdm

current_directory = input("Enter directory: ")

result = os.listdir(current_directory)
result = []
today = datetime.now()

for root, dirs, files in os.walk(current_directory):
    for dir in tqdm(dirs):
        if dir == 'node_modules':
            current_node_modules_path = os.path.join(root, dir)
            if os.path.exists(current_node_modules_path) and os.path.isdir(current_node_modules_path):
                shutil.rmtree(current_node_modules_path, ignore_errors=True)
                result.append(current_node_modules_path)

result_body = {
    "directory": current_directory,
    "count": len(result),
    "date": today.strftime("%B %d, %Y - %I:%M:%S %p"),
    "list": result
}

if not os.path.exists("result"):
    os.makedirs("result")

with open(f"result/data_{today.strftime('%m-%d-%Y-%I-%M-%S-%p')}.json", "w") as new_json:
    json.dump(result_body, new_json)

print(f"You removed {len(result)} node_modules folder")
