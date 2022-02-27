"""
Cansei da internet da claro que oscila muito =(
"""

import speedtest
import time

s = speedtest.Speedtest()
s.get_servers()
s.get_best_server()

while True:
    velocidade_download = round(s.download(threads=None)*(10**-6))
    velocidade_upload = round(s.upload(threads=None)*(10**-6))
    print("Download: ", velocidade_download)
    print("Upload: ",velocidade_upload)
    time.sleep(0.5)