import os
import shutil
import sys

source_path = os.path.join('data', 'frame')
split = 6


frames = os.listdir(source_path)
print('Total frame: ', len(frames))
print('spliting into {} path'.format(split))
print('Each split will have {} frame'.format(len(frames) / split))


image_name = 'frame'
index = 0
target_path = os.path.join('data', 'dataset')

for i in range(split):
	if os.path.exists(os.path.join(target_path, str(i))) is False:
		os.mkdir(os.path.join(target_path, str(i)))

	for j in range(len(frames) / split):
		sys.stdout.write('\rprocessing {} ...'.format('frame_' + str(index) + '.png'))
		sys.stdout.flush()
		shutil.copyfile(os.path.join(source_path, 'frame_' + str(index) + '.png'), os.path.join(target_path, str(i), 'frame_' + str(index) + '.png'))
		index += 1



