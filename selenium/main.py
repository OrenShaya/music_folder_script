import os
import re
import time
import codecs
from tinytag import TinyTag, TinyTagException

def clean_text(string: str) -> str:
    string = string.translate(str.maketrans("?\\/|:*\"<>", "         "))
    string = re.sub("  +", " ", string)
    string = string.strip()
    return string

print()
path = "E:\\Users\\Oren\\Music\\"
for file in os.listdir(path):
    if os.path.isdir(path+file):
        continue
    if file.endswith(".jpg"):
        continue
    try:
        tags = TinyTag.get(path+file)
    except TinyTagException as e:
        # unsupported file type
        continue
    print(file)
    if not tags.artist:
        artist = ""
    else:
        artist = clean_text(tags.artist)
    if not tags.album or tags.album.strip() == "Unkown album" or tags.album.strip() == "unknown":
        album = ""
    else:
        album = clean_text(tags.album)
    new_path = os.path.join(path, artist, album).replace(" \\", "\\")
    if not os.path.exists(new_path):
        os.mkdir(new_path)
        time.sleep(0.75)
    new_path = os.path.join(new_path, file)
    print(f"{path+file}\n\t\t\t|\n\t\t\tv \n{new_path}\n")

    os.rename(path+file, new_path)



def return_to_hebrew(incorrect_string: str) -> str:
    decoded_string = codecs.decode(incorrect_string, 'unicode_escape')
    byte_string = decoded_string.encode('iso-8859-1')
    hebrew_string = byte_string.decode('windows-1255')
    return hebrew_string
