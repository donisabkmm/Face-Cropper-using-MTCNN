import math
from mtcnn.mtcnn import MTCNN
import cv2
import os
detector = MTCNN()
y1n = 0
y2n = 0
x1n = 0
x2n = 0
bounding_box = []
keypoints = []
def faceapp(images, dist, file_name):

    images = cv2.imread(images)
    faces = detector.detect_faces(images)
    print(faces)
    if len(faces) < 1:
        cv2.imwrite("detached/" + file_name, images)
    if len(faces) > 1:
        cv2.imwrite("detached/" + file_name, images)
    if len(faces) == 1:
        for face in faces:
            bounding_box = face['box']
            keypoints = face['keypoints']
            if keypoints != 0 and bounding_box != 0:
                x1, y1, w, h = bounding_box
                L_points = keypoints['left_eye']
                a1 = L_points[0]
                b1 = L_points[1]
                half_d1 = int(int(math.sqrt((a1 - x1) ** 2 + (b1 - y1) ** 2) / 3) + int(
                    math.sqrt((a1 - x1) ** 2 + (b1 - y1) ** 2) / 5))
                q_d1 = int(half_d1 / 2)
                x1n = x1 - half_d1
                y1n = y1 - half_d1 - q_d1
                x2 = w + x1
                y2 = h + y1
                R_points = keypoints['mouth_right']
                a2 = R_points[0]
                b2 = R_points[1]
                half_d2 = int(math.sqrt((a2 - x2) ** 2 + (b2 - y2) ** 2) / 2)
                q_d2 = int(int(math.sqrt((a2 - x2) ** 2 + (b2 - y2) ** 2) / 3) + int(
                    math.sqrt((a2 - x2) ** 2 + (b2 - y2) ** 2) / 5))
                x2n = x2 + half_d2 + q_d2
                y2n = y2 + half_d2 + q_d2
                # cv2.rectangle(images, (x1n, y1n), (x2n, y2n), (0, 255, 0), 2)
                if x1n and y1n and x2n and y2n:
                    if (x1n < 0):
                        x1n = 0
                    if (y1n < 0):
                        y1n = 0
                cropped_img = images[y1n:y2n, x1n:x2n]
                cv2.imwrite(dist + file_name, cropped_img)
                dimension = cropped_img.shape

                finalimage_height = cropped_img.shape[0]
                finalimage_width = cropped_img.shape[1]
                print(finalimage_height)
                print(dimension)
                if finalimage_width > finalimage_height:
                    workimgwidth= int(finalimage_width/float(finalimage_height/241))
                    workimgheight= int(finalimage_height/float(finalimage_width/189))
                    final_work_img=cv2.resize(cropped_img,(workimgwidth,workimgheight))
                    cv2.imwrite(dist + file_name, final_work_img)

                else:
                    workimgwidth = int(finalimage_width / (float(finalimage_height / 241)))
                    workimgheight = int(finalimage_height / (float(finalimage_width / 189)))
                    final_work_img=cv2.resize(cropped_img,(workimgwidth,workimgheight))
                    cv2.imwrite(dist + file_name, final_work_img)

if __name__ == "__main__":
    try:
        image = 'images/'
        output = 'output/'
        detached = 'detached/'
        filename = [f for f in os.listdir(image) if f.endswith('.jpg') or f.endswith('.JPG')]
        for filename in filename:
            path = os.path.join(image, filename)
            faceapp(path, output, filename)

    except RuntimeError as e:
        # Code to handle the exception
        print("An exception occurred", e)
