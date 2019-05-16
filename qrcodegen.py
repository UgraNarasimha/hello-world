# Before running the script make sure the following 3 runs sets up the environment.
#python3 -m venv qrenve
#pip install pyqrcode
#pip install pypng

import pyqrcode


def generate_qr():
    link_to_post = "https://github.com/UgraNarasimha"
    url = pyqrcode.create(link_to_post)
    url.png('url.png', scale=8)
    #url.svg('url.png',scale=8)
    print("Printing QR code")
    #print(url.terminal())

if __name__ == '__main__':
    generate_qr()
