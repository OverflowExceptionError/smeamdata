# SmEAM
# (C) 2022 VuLVE LTD
print('Downloading SmEAM files...')
import requests
import os
print('Warning: SmEAM requires internet to get it\'s files, and it\'s download of the game\'s catalog!')
def download_asset(url,file_out):
    b = requests.get("https://memed64.000webhostapp.com/scratchpy/users/" + filename[0] + "/projects/default.spyd",stream=True)
    handle = open(file_out, "wb")
    for chunk in b.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    handle.close()