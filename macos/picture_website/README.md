# Mac picture viewing application #

You can build or download a prebuilt app. The Application is called ImageViewer and is built on pyflask.

## What does it do?

It opens a specified folder and shows all the picters in that folder on your host ip with a random port. It will open your standard browser and go to the webbsite. Anyone on the network with a phone or computer can go to that link and see the pictures

**When started it:**
* Opens finder and asks you to select a folder
* When a folder is selected it will open standard browser and display all the pictures in the folder.


# For those who want to build it

There are some tools you need in order to build the app.
If you need prerequisite then you are probably not the right person to travel this road.

## Prerequisites
```bash
# prerequisite installation.
xcode-select --install
# install brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# add Homebrew to PATH (SILICON  NOT INTEL)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
# Install git
brew install git
```

## Command to build the app.

```bash
# Download folder & build the app
git clone --depth=1 --filter=blob:none --sparse git@github.com:blitzes27/applications.git && \
cd applications && \
git sparse-checkout set macos/picture_website && \
cd macos/picture_website && \
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python setup.py py2app
cp -R dist/ImageViewer.app "$HOME/Desktop/ImageViewer.app"
```
The app can be found on Desktop or in 
* macos/picture_website/dist/ImageViewer.app

