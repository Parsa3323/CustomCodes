import json
import os
import re

CODES_DIR = "Codes"

def validate_code_folder(folder_path):
    json_path = os.path.join(folder_path, "data.json")
    if not os.path.exists(json_path):
        print(f"❌ Missing data.json in {folder_path}")
        return False
    
    with open(json_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON format in {json_path}")
            return False

    main_class = data.get("mainClass")
    if not main_class:
        print(f"❌ No mainClass defined in {json_path}")
        return False

    main_class_path = os.path.join(folder_path, main_class.replace(".", "/") + ".java")
    if not os.path.exists(main_class_path):
        print(f"❌ Main class file {main_class_path} is missing")
        return False

    with open(main_class_path, "r") as f:
        if "extends JavaPlugin" not in f.read():
            print(f"❌ {main_class} does not extend JavaPlugin!")
            return False

    plugin_yml = os.path.join(folder_path, "plugin.yml")
    if not os.path.exists(plugin_yml):
        print(f"❌ Missing plugin.yml in {folder_path}")
        return False

    print(f"✅ {folder_path} is valid!")
    return True

def main():
    all_valid = True
    for code_name in os.listdir(CODES_DIR):
        folder_path = os.path.join(CODES_DIR, code_name)
        if os.path.isdir(folder_path):
            if not validate_code_folder(folder_path):
                all_valid = False

    if not all_valid:
        exit(1)

if __name__ == "__main__":
    main()
