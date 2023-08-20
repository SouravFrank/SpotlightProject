import os
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx
from PyQt6.QtWidgets import QMessageBox, QFileDialog
import json
import zipfile

CONFIG_FILE_PATH = os.path.join(os.environ["APPDATA"], "spotlight_config.json")
ZIP_FILE_NAME = "Spotlight_Images"  # Change this to your desired zip file name

def get_destination_folder():
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = json.load(config_file)
            destination_folder = config.get("destination_folder")
            return destination_folder
    except (FileNotFoundError, json.JSONDecodeError):
            return None

def create_zip(zip_file_path, source_folder):
    try:
        with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(source_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, source_folder)
                    zipf.write(file_path, arcname)

        return zip_file_path

    except Exception as e:
        print(f"Error creating zip file: {e}")
        return None

def on_create_zip_clicked():
    source_folder = get_destination_folder()

    if source_folder:
        selected_path, _ = QFileDialog.getSaveFileName(None, "Save Zip File", source_folder + "\\" + ZIP_FILE_NAME + ".zip", "ZIP Files (*.zip)")
        if selected_path:
            zip_file_path = selected_path
            if create_zip(zip_file_path, source_folder):
                QMessageBox.information(None, "Zip Created", f"Zip file saved to: {zip_file_path}")
            else:
                QMessageBox.critical(None, "Error", "Failed to create zip file.")
        else:
            QMessageBox.warning(None, "No Destination Path", "Please select a path to save the zip file.")
    else:
        QMessageBox.warning(None, "No Source Folder", "Please set the source folder first.")