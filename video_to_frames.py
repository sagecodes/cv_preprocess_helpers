#%% Import libraries
import cv2

#%% read info about video
video = cv2.VideoCapture('../datasets/videos/xmas2021.mp4')
frames_per_second = video.get(cv2.CAP_PROP_FPS)
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration = num_frames/frames_per_second

print(f'Video FPS: {frames_per_second}')
print(f'Total Frames {num_frames}')
print(f'Duration (sec): {duration}')

count = 00

# Number of frames per second to convert to image
image_per_sec = 10

frames_skip = round(frames_per_second/image_per_sec)
print(f'Will skip every {frames_skip} frames for conversion')

#%% Save frames from Video

while count <= num_frames:
    success, image = video.read()

    if count < 10:
        beginzeros = '000'
    elif count < 100:
        beginzeros = '00'
    elif count < 1000:
        beginzeros = '0'

    if count % frames_skip == 0:
        cv2.imwrite(f'../datasets/xmas2021/frame{beginzeros}{count}.jpg', image)      
        print(f'saving frame {count}')
    count += 1

# %%

