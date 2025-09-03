import sys
import os

from rs_attack.rs_analysis import rs_analysis_attack

# Thêm đường dẫn module con
sys.path.append(os.path.join(os.getcwd(), "encode"))
sys.path.append(os.path.join(os.getcwd(), "decode"))
sys.path.append(os.path.join(os.getcwd(), "rs_attack"))

from encode_lsb import encode_lsb
from decode_lsb import decode_lsb
from rs_analysis import rs_analysis_attack

original = "./images/original.png"
hidden = "./images/hidden.png"
message = (
    "24410004 Nguyen Tuan Anh. Steganography test message. " 
    "This is a longer payload to make RS Analysis detect hidden data easily. "
    "Adding more characters to increase detection rate in the image. "
) * 10  # Nhân lên cho đủ dài

print("="*50)
print("BẮT ĐẦU QUY TRÌNH: GIẤU TIN - GIẢI MÃ - PHÂN TÍCH RS")
print("="*50)

# 1. Giấu tin
print("\n[1] Giấu tin vào ảnh ...")
encode_lsb(original, hidden, message)

# 2. Giải mã
print("\n[2] Giải mã tin từ ảnh ...")
decoded_message = decode_lsb(hidden)
print("Tin đã giải mã:", decoded_message)

# 3. Phân tích RS
print("\n[3] Phân tích RS ...")
rs_analysis_attack(original, hidden, block_size=8, threshold=25)



print("\nHoàn thành quy trình!")
