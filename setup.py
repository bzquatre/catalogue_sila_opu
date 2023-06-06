import PyInstaller.__main__
import os
database= '--add-binary=database.db;.' if os.name=='nt' else '--add-binary=database.db:.'
images='--add-data=images;images' if os.name=='nt' else '--add-data=images:images'
icon='--add-data=Icon.ico;.' if os.name=='nt' else'--add-data=Icon.ico:.' 
header='--add-data=header.txt;.' if os.name=='nt' else'--add-data=header.txt:.' 
PyInstaller.__main__.run(
    [
        'main.py',
        '--name=OPU Catalog',
        '--windowed',
        '--onedir',
        '--icon=Icon.ico',
        database,
        icon,
        header,
        images
    ]
)