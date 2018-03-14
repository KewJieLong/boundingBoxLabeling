import cv2
import argparse
import os
import sys
import numpy as np



adjust_pixel = 10

"""
action key
w : move up
a: move left
d : move right
s : move down 
space: save image and label
q: noting to label for the image 
ecs: quit the program 


h: increase height
j: increase width
k: decrease height 
l: decrease width 
"""


def label_action(key, image, bbox, next_image):
	x, w, y, h = bbox
	height, width= image.shape[0:2]
	save = False

	if key == ord('w'):
		if y - adjust_pixel > 0:
			y -= adjust_pixel
	elif key == ord('d'):
		if (x + w) + adjust_pixel < width:
			x += adjust_pixel
	elif key == ord('a'):
		if x - adjust_pixel > 0:
			x -= adjust_pixel
	elif key == ord('s'):
		if (y + h) + adjust_pixel < height:
			y += adjust_pixel
	elif key == ord('j'):
		if x + w < width:
			w += adjust_pixel
	elif key == ord('l'):
		if abs(w - x) > 0:
			w -= adjust_pixel
	elif key == ord('h'):
		if y + h < height:
			h += adjust_pixel
	elif key == ord('k'):
		if abs(h - y) > 0:
			h -= adjust_pixel
	elif key == 32: # space
		next_image = True
		save = True
	elif key == ord('q'):
		next_image = True
		save = False
	elif key == 27:
		print('exiting program')
		cv2.destroyAllWindows()
		sys.exit(0)

	bbox = x, w, y, h
	return ori_image, next_image, bbox, save


if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description='labeling dataset')
		parser.add_argument('-dp', '--dataset_path', help='dataset path')
		parser.add_argument('-sp', '--save_path', help='save path', default='label')


		args = parser.parse_args()
		dataset_path = args.dataset_path
		save_path = args.save_path

		if os.path.exists(save_path) is False:
			os.mkdir(save_path)

		x, w, y, h = 0, 300, 0, 300
		bbox = x, w, y, h

		image_paths = os.listdir(dataset_path)

		for image_path in os.listdir(dataset_path):
			sys.stdout.write('\rlabeling {}'.format(image_path))
			sys.stdout.flush()
			image = cv2.imread(os.path.join(dataset_path, image_path))
			image = np.where(image < 30, 0, image - 30)

			next_image = False
			save = False
			while next_image is False:
				x, w, y, h = bbox
				ori_image = np.array(image)
				image[y: y + h, x: x + w] = np.where((255 - image[y: y + h, x: x + w]) < 80, 255,
														   image[y: y + h, x: x + w] + 80)
				cv2.imshow('label', image)
				image, next_image, bbox, save = label_action(cv2.waitKey(0), ori_image, bbox, next_image)

				if save:
					x, w, y, h = bbox
					dict_bbox = {'x': x, 'w': w, 'y': y, 'h': h}
					np.save(os.path.join(save_path, image_path.split('.')[0]), dict_bbox)



	except:
		import traceback
		print(traceback.print_exc())
		cv2.destroyAllWindows()
		sys.exit(0)



