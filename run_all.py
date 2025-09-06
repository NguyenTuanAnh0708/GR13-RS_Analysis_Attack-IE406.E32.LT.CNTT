import sys
import os


sys.path.append(os.path.join(os.getcwd(), "encode"))
sys.path.append(os.path.join(os.getcwd(), "decode"))
sys.path.append(os.path.join(os.getcwd(), "rs_attack"))

from encode_lsb import encode_lsb
from decode_lsb import decode_lsb
from rs_analysis import rs_analysis_attack

cover_image = "./images/cover.png"
stego_image = "./images/stego.png"
message = (
    "24410004 Nguyen Tuan Anh. Steganography test message. " 
    "This is a longer payload to make RS Analysis detect hidden data easily. "
    "Adding more characters to increase detection rate in the image. "
) * 10  

print("="*50)
print("BẮT ĐẦU QUY TRÌNH: GIẤU TIN - GIẢI MÃ - PHÂN TÍCH RS")
print("="*50)

# 1. Giấu tin
print("\n[1] Giấu tin vào ảnh ...")
encode_lsb(cover_image, stego_image, message)

# 2. Giải mã
print(f"\n[2] Giải mã tin từ ảnh từ {stego_image}")
decoded_message = decode_lsb(stego_image)
print("Tin đã giải mã:", decoded_message)

# 3. Phân tích RS
print("\n[3] Phân tích RS ...")
rs_analysis_attack(cover_image, cover_image, block_size=8, threshold=25)



print("\nHoàn thành quy trình!")
