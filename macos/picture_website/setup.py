from setuptools import setup

APP = ["app.py"]

OPTIONS = {
    # Only include your third-party dependencies here:
    "packages": ["flask"],
    # Force-include these modules (tkinter for the folder chooser, pkg_resources for py2app, jaraco.text)
    "includes": [
        "tkinter",
        "tkinter.filedialog",
        "pkg_resources",
        "jaraco.text",
    ],
    # Bundle your templates and static folders inside the .app
    "resources": ["templates", "static"],
    # Enable macOS argv emulation so dragging a folder onto the icon passes it in sys.argv
    "argv_emulation": True,
    "plist": {
        "CFBundleName": "ImageViewer",
        "CFBundleIdentifier": "com.yourdomain.imageviewer",
        "CFBundleVersion": "0.1.0",
        "CFBundleShortVersionString": "0.1.0",
        # Make the app document-based so File→Open… appears and drag-to-icon works
        "CFBundleDocumentTypes": [
            {
                "CFBundleTypeName": "Image Folder",
                "LSItemContentTypes": ["public.folder"],
                "CFBundleTypeRole": "Viewer"
            }
        ]
    },
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)