from PIL import Image
import numpy as np

def load_image_gray(image_path):
    """Đọc ảnh và chuyển sang grayscale"""
    img = Image.open(image_path).convert('L')
    return np.array(img, dtype=np.uint8)

def flip_lsb(block):
    """Lật bit LSB của block"""
    return block ^ 1

def discrimination(block):
    """Tính độ mượt của block (tổng sai khác tuyệt đối giữa các pixel liên tiếp)"""
    return np.sum(np.abs(np.diff(block)))

def rs_analysis_single(image_path, block_size=8):
    """Tính R và S cho một ảnh"""
    img = load_image_gray(image_path)
    height, width = img.shape
    R, S = 0, 0

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = img[y:y+block_size, x:x+block_size].flatten()
            if len(block) < block_size * block_size:
                continue
            original_smooth = discrimination(block)
            flipped_smooth = discrimination(flip_lsb(block))
            if flipped_smooth > original_smooth:
                R += 1
            elif flipped_smooth < original_smooth:
                S += 1
    return R, S

def rs_analysis_attack(original_image, suspect_image, block_size=8, threshold=50):
    """
    So sánh ảnh gốc và ảnh nghi ngờ.
    Trả về True nếu ảnh nghi ngờ có dấu hiệu giấu tin, False nếu không.
    """
    R_orig, S_orig = rs_analysis_single(original_image, block_size)
    R_sus, S_sus = rs_analysis_single(suspect_image, block_size)

    delta_R = abs(R_sus - R_orig)
    delta_S = abs(S_sus - S_orig)

    print("=== RS Analysis Result ===")
    print(f"Ảnh gốc      - R: {R_orig}, S: {S_orig}")
    print(f"Ảnh nghi ngờ - R: {R_sus}, S: {S_sus}")
    print(f"Delta R: {delta_R}, Delta S: {delta_S}")

    if delta_R + delta_S > threshold:
        print(">> Ảnh nghi ngờ có khả năng giấu tin!")
        return True
    else:
        print(">> Ảnh nghi ngờ KHÔNG có tin ẩn.")
        return False