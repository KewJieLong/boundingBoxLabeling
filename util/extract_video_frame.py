import cv2
import os
import sys

base_path = 'data'
x_path = os.path.join(base_path, 'video')
target_path = os.path.join(base_path, 'frame')
count = 0
for video in os.listdir(x_path):
	print(os.path.join(x_path, video))
	vidcap = cv2.VideoCapture(os.path.join(x_path, video))

	success = True
	while success:
		try:
			success, image = vidcap.read()
			sys.stdout.write('\rsaving {}'.format(os.path.join(target_path, 'frame_{}.png'.format(count))))
			sys.stdout.flush()
			cv2.imwrite(os.path.join(target_path, 'frame_{}.png'.format(count)), image)

			if cv2.waitKey(10) == 27:
				break
			count += 1
		except:
			import traceback
			print(traceback.print_exc())


