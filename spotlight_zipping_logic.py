import os
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx
from PyQt6.QtWidgets import  QMessageBox
import json
import zipfile

CONFIG_FILE_PATH = os.path.join(os.environ["APPDATA"], "spotlight_config.json")

def get_destination_folder():
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = json.load(config_file)
            destination_folder = config.get("destination_folder")
            return destination_folder
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def create_zip():
    try:
        destination_folder = get_destination_folder()
        zip_file_name = os.path.basename(destination_folder) + ".zip"
        with zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(destination_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, destination_folder)
                    zipf.write(file_path, arcname)

        zip_file_path = os.path.join(destination_folder, zip_file_name)
        return zip_file_path

    except Exception as e:
        print(f"Error creating zip file: {e}")
        return None

# You can call the create_zip function where you want to create the zip file, for example:
def on_create_zip_clicked():
    destination_folder = get_destination_folder()

    if destination_folder:
        zip_file_path = create_zip()
        if zip_file_path:
            QMessageBox.information(None, "Zip Created", f"Zip file created: {zip_file_path}")
        else:
            QMessageBox.critical(None, "Error", "Failed to create zip file.")
    else:
        QMessageBox.warning(None, "No Destination Folder", "Please set the destination folder first.")
