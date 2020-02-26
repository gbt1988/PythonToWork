import os,pprint
for folder,subfolders,files in os.walk('/users/kevin/os'):
	print ('当前文件夹是' + folder)
	for sub in subfolders:
		print(folder +'的子文件夹是' + sub)
	for filename in files:
		print('包含文件' + folder + filename)
	print(' ')


pprint.pprint(list(os.walk('/users/kevin/os')))
# [('/users/kevin/os', ['a', 'b'], ['.DS_Store', 'a.txt']),
# ('/users/kevin/os/a', [], ['a.txt']),
# ('/users/kevin/os/b', ['x'], ['a 2.txt', '.DS_Store', 'a.txt']),
# ('/users/kevin/os/b/x', ['z', 'y'], ['.DS_Store']),
# ('/users/kevin/os/b/x/z', [], []),
# ('/users/kevin/os/b/x/y', ['w'], ['.DS_Store', 'a.txt']),
# ('/users/kevin/os/b/x/y/w', [], [])]
