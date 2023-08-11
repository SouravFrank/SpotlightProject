# Spotlight Image Copy Tool

![Tool Screenshot](./Screenshot.png)

The Spotlight Image Copy Tool is a user-friendly Windows application that simplifies the process of managing and organizing Windows Spotlight images. With this tool, you can effortlessly collect, convert, and organize lock screen images to build your curated collection right on your desktop.

## Features

- Collects captivating Windows Spotlight images from your lock screen.
- Ensures image quality by selecting landscape-oriented images.
- Converts images to JPEG format for compatibility and consistency.
- Renames images with a sophisticated format like 'Spotlight_Timestamp.jpg'.
- Removes duplicate images, keeping your collection tidy.
- User-friendly interface with clear instructions.
- Developed by Sourav Sadhukhan.

## Usage

1. Clone or download this repository to your computer.
2. Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

3. Open a terminal or command prompt in the repository folder.
4. Run the following command to execute the application:

```bash
python spotlight_ui.py
```

5. Follow the on-screen instructions to manage your Windows Spotlight images.

## Building Executable (Windows)

To create a standalone executable file for your convenience, you can use `pyinstaller`. Here's how:

1. Open a terminal or command prompt in the repository folder.
2. Run the following command to install `pyinstaller` if you haven't already:

```bash
pip install pyinstaller
```

3. Run the following command to build the executable:

```bash
pyinstaller --onefile --icon=icon_cam.png --add-data "spotlight_logic.py;." spotlight_ui.py
```

4. After the process is complete, you'll find the `.exe` file in the `dist` folder.

## Running the Application

To run the application using Python directly, use the following command:

```bash
python spotlight_ui.py
```

## Notes

- The application may require administrative privileges to access system directories.
- Make sure to respect copyright and usage rights of the images you manage.
