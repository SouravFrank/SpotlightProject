# Spotlight Image Copy Tool

![Tool Screenshot](./Screenshot.png)

Welcome to the **Spotlight Image Copy Tool**, where we take the hassle out of hunting down those stunning Windows Spotlight images. Whether you're obsessed with lock screen beauty or have a secret passion for desktop wallpapers, this tool's got you covered. It’s like your personal assistant, but with fewer coffee breaks and more pixels.

## Description

Unleash your inner curator with the **Spotlight Image Copy Tool**! Now, it’s not just your lock screen that gets the VIP treatment—this tool also lets you grab those gorgeous Spotlight desktop images. Dive into an effortlessly organized, curated collection that’s as unique as your taste.

**Created by**: Sourav Sadhukhan (aka the pixel perfectionist)

![Spotlight Folder Screenshot](./Spotlight_Folder.png)

## Features

- **Effortless Collection**: Gather both lock screen and desktop Spotlight images with just a click. It’s like magic, but with less wand-waving.

- **Organized Storage**: Your images will be neatly tucked away in a folder named 'Spotlight Images'. It’s like giving your pictures a cozy home.

- **Streamlined Management**: Forget the hassle of repeatedly setting up your destination folder. The tool remembers it for you. Change it anytime with the 'Set location' button, no complaints!

- **Quality Assurance**: Only the best for your collection! We pick landscape-oriented images to keep those dimensions intact and the quality top-notch.

- **Duplicate Management**: Say goodbye to duplicates! The tool smartly removes them, so you don’t have to worry about cluttered collections.

- **Zip Archive Creation**: Need to pack everything up? One click on the 'Zip folder' button and your entire collection is zipped up and ready to go.

- **Enchanting Collection**: Curate your image collection with ease. Because why not?

## What's New

- **Desktop Images**: It's not just for your lock screen anymore! Now you can also save those awe-inspiring Spotlight desktop images.

- **Modern Design**: We've revamped the UI to be sleek, stylish, and as modern as your favorite 2023 trends. Because aesthetics matter, right?

## Download and Usage

1. On the right side of this screen, locate and click on the **Releases** section of this repository.
2. From the list of releases, select the latest version.
3. In the release assets, find and download the `Spotlight_Image_Copy_Tool_V2.1.0.exe` file.
4. Double-click the downloaded `.exe` file to run the application.
5. Follow the on-screen instructions to start collecting and organizing your Spotlight images.

If you encounter any security warnings, just tell your OS to chill. It's safe because it’s from this repository.

## Usage

1. Clone or download this repository to your computer.
2. Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Open a terminal or command prompt in the repository folder.
4. Run the following command to start the application:

    ```bash
    python spotlight_ui.py
    ```

5. Follow the on-screen prompts to manage your Windows Spotlight images like a pro.

## Building Executable (Windows)

Feeling fancy and want to build your own standalone executable? Here’s how:

1. Open a terminal or command prompt in the repository folder.
2. Run the following command to install `pyinstaller` if you haven't already:

    ```bash
    pip install pyinstaller
    ```

3. Build the executable with this command:

    ```bash
    pyinstaller --onefile --icon=icon_cam.png --add-data "spotlight_logic.py;." --add-data "spotlight_zipping_logic.py;." --add-data "spotlight_styles.py;." spotlight_ui.py
    ```

4. Voilà! You’ll find the `.exe` file in the `dist` folder, ready to impress.

## Running the Application

To run the application using Python directly, use the following command:

```bash
python spotlight_ui.py
```

## Notes

- Administrative privileges might be needed to access certain system directories.
- Respect copyright and usage rights for the images you’re managing. We’re all about keeping things ethical.

For more information and support, contact Sourav Sadhukhan at [ssadhukhan990@gmail.com](mailto:ssadhukhan990@gmail.com). 
