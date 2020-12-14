#%% Import libraries
import cv2

#%% read info about video
video = cv2.VideoCapture('../datasets/videos/ornamentvideo.mov')
frames_per_second = video.get(cv2.CAP_PROP_FPS)
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

print(f'Video FPS: {frames_per_second}')
print(f'Total Frames {num_frames}')
print(f'Duration (sec): {num_frames/frames_per_second}')

count = 0

#frames to skip
frames_skip = 4

#%% Save frames from Video

while count <= num_frames:
    success,image = video.read()

    if count % frames_skip == 0:
        cv2.imwrite(f'../datasets/ornaments/frame{count}.jpg', image)      
        print(f'saving frame {count}')
    count += 1


