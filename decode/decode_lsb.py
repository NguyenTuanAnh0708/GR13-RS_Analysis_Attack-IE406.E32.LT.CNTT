from PIL import Image

def decode_lsb(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()

    binary_message = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)
    byte_chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    data_bytes = bytearray()

    for byte in byte_chunks:
        if byte == "00000000":
            break
        data_bytes.append(int(byte, 2))

    try:
        return data_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return "[ERROR] Dữ liệu bị lỗi hoặc ảnh không chứa tin nhắn."
