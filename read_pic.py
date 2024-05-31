import cv2
import os
 
# 检查版本
print(cv2.__version__)

def split_image(image_path):
    # 读取图片
    image = cv2.imread(image_path)
    
    # 获取图片尺寸
    height, width = image.shape[:2]
    is_change = True
    if width < 3000:
        is_change = False
    else:
        is_change = True
    
    # 计算分割位置
    split_position = width // 2
    
    # 分割图片
    left_image = image[:, :split_position, :]
    right_image = image[:, split_position:, :]
    
    return left_image, right_image, is_change

def save_images(left_image, right_image, output_path_left, output_path_right):
    cv2.imwrite(output_path_left, left_image)
    cv2.imwrite(output_path_right, right_image)

if __name__ == "__main__":
    # 文件路径
    file_path = r'/Volumes/share_vd/media/漫画/龙珠 数码全彩 Vol43 双页8K版'
    for root, dirs, files in os.walk(file_path):
        print(files)

    for file in files:
        input_image_path = file_path + '/' + file
        left_image, right_image, is_change = split_image(input_image_path)
        if is_change :
            input_image_path_list = input_image_path.split('.')
            output_path_left = input_image_path_list[0] + "左."+input_image_path_list[1]
            output_path_right = input_image_path_list[0] + "右."+input_image_path_list[1]
            print(output_path_left)
            print(output_path_right)
            save_images(left_image, right_image, output_path_left, output_path_right)
            os.remove(input_image_path)

# # 加载一张图片（确保路径正确）
# image = cv2.imread('/Users/luxiaojian/Desktop/DB-DFC-01-001-庄子与孙悟空-03.jpg')
 
# # 显示图片
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()