import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)  # getting file and not the whole path included
            archive.write(filepath, arcname=filepath.name) # get only the name of the file

"""
if __name__ == "__main__":
    make_archive(filepaths=["bonus16_1.py", "bonus17_1.py"], dest_dir="dest")

test prog if all files and dest folder inside bonus folder
"""
