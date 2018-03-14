import cv2
import os
import sys
import argparse

base_path = 'data'
count = 0

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='extract frame by frame from video')
	parser.add_argument('-v', '--video_path', help='path to the video')
	parser.add_argument('-t', '--target_path', help='path to the target')

	args = parser.parse_args()
	video_path = args.video_path
	target_path = args.target_path

	if os.path.exists(target_path) is False:
		os.mkdir(target_path)


	for video in os.listdir(video_path):
		print(os.path.join(video_path, video))
		vidcap = cv2.VideoCapture(os.path.join(video_path, video))

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


