from setuptools import setup

APP = ["app.py"]
OPTIONS = {
    "packages": ["flask"],
    "includes": [
        "tkinter",
        "tkinter.filedialog",
        "pkg_resources",  
        "jaraco.text",      
    ],
    "resources": ["templates", "static"],
    "argv_emulation": True,
    "plist": {
        "CFBundleName": "ImageViewer",
        "CFBundleIdentifier": "com.dinorg.imageviewer",
        "CFBundleVersion": "0.1.0",
        "CFBundleShortVersionString": "0.1.0",
        "LSUIElement": False,
    },
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)