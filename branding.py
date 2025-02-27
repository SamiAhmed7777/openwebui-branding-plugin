import os
import shutil
import json

# Load configuration safely
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def load_config():
    """Load branding config safely."""
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
                return json.load(config_file)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in config.json.")
            return {}
    else:
        print("Warning: config.json not found.")
        return {}

config = load_config()

# Define paths
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")
TARGET_PATHS = {
    "favicon.png": os.path.join(os.getcwd(), "app/build/favicon/favicon.png"),
    "favicon.svg": os.path.join(os.getcwd(), "app/build/favicon/favicon.svg"),
    "splash.png": os.path.join(os.getcwd(), "app/build/static/splash.png"),
    "splash-dark.png": os.path.join(os.getcwd(), "app/build/static/splash-dark.png"),
    "logo.png": os.path.join(os.getcwd(), "app/build/static/logo.png")
}

# WebUI Name Configuration (frontend file path)
WEBUI_CONFIG_PATH = os.path.join(os.getcwd(), "app/frontend/src/config.js")

def replace_branding():
    """Copy branding files to their target locations."""
    if not os.path.exists(ASSETS_PATH):
        print(f"Warning: Branding assets folder '{ASSETS_PATH}' not found.")
        return

    for file_name, target in TARGET_PATHS.items():
        source_file = os.path.join(ASSETS_PATH, file_name)
        if os.path.exists(source_file):
            try:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copy(source_file, target)
                print(f"Updated {file_name} → {target}")
            except Exception as e:
                print(f"Error copying {file_name}: {e}")
        else:
            print(f"Warning: {file_name} not found in assets folder.")

def update_webui_name():
    """Modify the WebUI name in the frontend config.js."""
    webui_name = config.get("branding", {}).get("webui_name", "Chat.Sami")

    if os.path.exists(WEBUI_CONFIG_PATH):
        try:
            with open(WEBUI_CONFIG_PATH, "r", encoding="utf-8") as file:
                lines = file.readlines()

            with open(WEBUI_CONFIG_PATH, "w", encoding="utf-8") as file:
                for line in lines:
                    if "WEBUI_NAME" in line:
                        file.write(f'export const WEBUI_NAME = "{webui_name}";\n')
                    else:
                        file.write(line)

            print(f"Updated WebUI Name to: {webui_name}")
        except Exception as e:
            print(f"Error updating WebUI name: {e}")
    else:
        print(f"Warning: {WEBUI_CONFIG_PATH} not found.")

if __name__ == "__main__":
    replace_branding()
    update_webui_name()
