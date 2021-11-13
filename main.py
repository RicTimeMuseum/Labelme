import cv2
import os


video_in = input('Please input the name of the video: C:/Users/cwrlr/Pictures/2Ddata/')  # 使用前请修改路径，下同
capture = cv2.VideoCapture(f'C:/Users/cwrlr/Pictures/2Ddata/{video_in}')
frame_out = f'C:/Users/cwrlr/Pictures/Screenshots/{video_in[:-4]}'
json_out = f'{frame_out}/{video_in[:-4]}'
frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
fps = capture.get(cv2.CAP_PROP_FPS)
length = frames / fps

print(f'''Duration of video "{format(video_in)}": {format(length)}
Number of frames: {format(frames)}
Frame per second (FPS): {format(fps)}''')

try:
    os.makedirs(json_out)  # 新建存放截图的文件夹，并在其下新建存放JSON文件的文件夹
except OSError:
    pass
print('Converting....')
success = True
count = 0
while success:
    capture.set(cv2.CAP_PROP_POS_MSEC, count * 1000 * 72 / fps)  # 设置截图频率
    success, image = capture.read()
    if success:
        print(f'Frame {count + 1} written to: {video_in[:-4]}{str(72 * count).zfill(5)}.png')
        cv2.imwrite(os.path.join(frame_out, f'{video_in[:-4]}{str(72 * count).zfill(5)}.png'), image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])  # 导出截图
        count += 1
print(f'Mission completed, {count} captures generated. ')
