from PIL import Image

def encode_lsb(input_image, output_image, secret_message):
    # Mở ảnh
    img = Image.open(input_image).convert('RGB')
    pixels = img.load()

    # Chuyển thông điệp thành nhị phân + dấu NULL kết thúc
    binary_message = ''.join(format(ord(ch), '08b') for ch in secret_message) + '00000000'
    msg_len = len(binary_message)
    width, height = img.size
    capacity = width * height * 3  # Mỗi pixel có 3 kênh RGB

    # Kiểm tra dung lượng ảnh
    if msg_len > capacity:
        raise ValueError("Ảnh không đủ dung lượng để giấu tin!")

    msg_index = 0
    for y in range(height):
        for x in range(width):
            if msg_index >= msg_len:
                break
            r, g, b = pixels[x, y]

            if msg_index < msg_len:
                r = (r & ~1) | int(binary_message[msg_index])
                msg_index += 1
            if msg_index < msg_len:
                g = (g & ~1) | int(binary_message[msg_index])
                msg_index += 1
            if msg_index < msg_len:
                b = (b & ~1) | int(binary_message[msg_index])
                msg_index += 1

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"[INFO] Đã giấu tin vào {output_image}")
