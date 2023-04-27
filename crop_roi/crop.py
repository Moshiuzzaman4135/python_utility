import cv2
import os


def crop(roi, image_path):
    image = cv2.imread(image_path)
    count = 0

    for i in roi:
        print(i)

        star_x = i[0]
        star_y = i[1]
        end_x = i[2]
        end_y = i[3]
        cropped_section = image[star_y:end_y, star_x:end_x]
        cv2.imwrite(os.path.join(f'image_{count}.jpg'), cropped_section)
        count = count + 1


if __name__ == '__main__':
    roi = [[250, 25, 500, 250], [1200, 500, 1500, 800], [1340, 100, 1700, 300]]
    crop(roi=roi, image_path='./output.jpg')
