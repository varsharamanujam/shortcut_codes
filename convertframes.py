import cv2

vidcap = cv2.VideoCapture('/Users/varshasureshbabu/Downloads/GazeTracking/recording /test.mov')
success, image = vidcap.read()
count = 1
while success:
  cv2.imwrite("image_data/image_%d.jpg" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1