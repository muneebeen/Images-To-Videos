import cv2
import glob
import numpy as np


def img_to_numpy(image):
    width = 1280
    height = 720
    img = cv2.imread(image)
    img_resize = cv2.resize(img, (width, height))
    # height, width, layers = img.shape
    # size = (width, height)
    frames.append(img_resize)


def write_img_in_video(frame):
    [video.write(frame) for v in range(variables['fps'] * int(variables['video_duration'] / picture_count))]


if __name__ == "__main__":
    frames = []
    variables = {
        'width': 1280,
        'height': 720,
        'video_duration': 30,
        'fps': 60
    }

# getting images
for image in glob.glob(r'C:\Users\HP\Downloads\images\*.jpg'):
    img_to_numpy(image)

picture_count = len(frames)
fourcc = cv2.VideoWriter_fourcc(*'MP42')
video = cv2.VideoWriter('video.avi', fourcc, variables['fps'], (1280, 720))

# creating video
for i in frames:
    write_img_in_video(i)
video.release()




