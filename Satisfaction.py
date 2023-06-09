import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])
height,width,channel=frame.shape
size=(width,height)


video_output=cv2.VideoWriter("satisfaction.mp4",cv2.VideoWriter_fourcc(*"DIVX"),12,size)
for i in range(0,count-1):
    frames=cv2.imread(images[i])
    video_output.write(frames)

video_output.release()

print("Done!")