import os
import shutil
from PIL import Image
import datetime
import subprocess
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx
import time
from PyQt6.QtWidgets import QMessageBox, QFileDialog
import json

# Global variable to store the destination folder path
destination_folder = ""
CONFIG_FILE_PATH = os.path.join(os.environ["APPDATA"], "spotlight_config.json")

def get_spotlight_images():
    spotlight_dir = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Packages', 
                                 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 
                                 'LocalState', 'Assets')
    return spotlight_dir

def is_image_ratio_valid(image_path):
    image = Image.open(image_path)
    width, height = image.size
    return not (width / height == 9 / 16)

def convert_to_jpg(image_path):
    try:
        image = Image.open(image_path)
        if image.format != 'JPEG':
            new_path = os.path.splitext(image_path)[0] + '.jpg'
            image = image.convert('RGB')
            image.save(new_path)
            os.remove(image_path)
            return new_path
        return image_path
    except Exception as e:
        print(f"Error converting image: {e}")
        return None

def detect_system_theme():
    try:
        aReg = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        theme = QueryValueEx(aReg, "AppsUseLightTheme")[0]
        return theme == 0
    except Exception:
        return False  # Fallback to light theme if theme detection fails

def copy_spotlight_images():
    global destination_folder  # Access the global variable
    global CONFIG_FILE_PATH

    # If destination folder is not set, ask the user to set it
    if not destination_folder:
        # Initialize the destination folder from the configuration file, if available
        try:
            with open(CONFIG_FILE_PATH, "r") as config_file:
                config = json.load(config_file)
                destination_folder = config.get("destination_folder")
        except (FileNotFoundError, json.JSONDecodeError):
            destination_folder = None
            set_destination_folder()
        
        if not destination_folder:
            return

    spotlight_dir = get_spotlight_images()
    if not os.path.exists(spotlight_dir):
        QMessageBox.critical(None, "Error", "Spotlight images directory not found.")
        return
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    copied_files = []
    for filename in os.listdir(spotlight_dir):
        source_file = os.path.join(spotlight_dir, filename)
        if os.path.isfile(source_file) and is_image_ratio_valid(source_file):
            destination_file = os.path.join(destination_folder, filename)
            new_destination = convert_to_jpg(source_file)
            if new_destination:
                shutil.copy2(new_destination, destination_file)
                copied_files.append(destination_file)

    if copied_files:
        current_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
        for file in copied_files:
            new_name = os.path.join(destination_folder, f"Spotlight_{current_time}.jpg")
            while os.path.exists(new_name):  # Add delay and retry until a unique name is found
                time.sleep(0.001)
                current_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
                new_name = os.path.join(destination_folder, f"Spotlight_{current_time}.jpg")

            os.rename(file, new_name)

        QMessageBox.information(None, "Success", "Spotlight images saved successfully.")
        delete_duplicate_files(destination_folder)
        # QMessageBox.information(None, "Success", "Duplicates removed successfully.")
        # Open the destination folder
        subprocess.Popen(["explorer", os.path.normpath(destination_folder)])
    else:
        QMessageBox.information(None, "No Images", "No valid spotlight images were found or copied.")

def delete_duplicate_files(destination_folder):
    file_sizes = {}  # Dictionary to store file sizes and corresponding file paths

    # Collect file sizes and paths
    for filename in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size in file_sizes:
                file_sizes[file_size].append(file_path)
            else:
                file_sizes[file_size] = [file_path]

    # Delete duplicate files
    for size, files in file_sizes.items():
        if len(files) > 1:  # More than one file with the same size (potential duplicates)
            # Delete all duplicates except the first one
            for i in range(1, len(files)):
                file_to_delete = files[i]
                os.remove(file_to_delete)
                # print(f"Deleted duplicate file: {file_to_delete}")

def save_config():
    global CONFIG_FILE_PATH
    global destination_folder
    
    config = {"destination_folder": destination_folder}
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(config, config_file)

def set_destination_folder():
    global destination_folder
    options = QFileDialog.Option.ShowDirsOnly
    selected_folder = QFileDialog.getExistingDirectory(None, "Select Destination Folder", "", options=options)
    if selected_folder:
        destination_folder = os.path.join(selected_folder, "Spotlight Images")
        save_config()