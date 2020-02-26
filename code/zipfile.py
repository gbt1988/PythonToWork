import zipfile,os
os.chdir('/users/kevin')
sampleZip = zipfile.ZipFile('os.zip') #创建一个 ZipFile 对象
sampleZip.namelist()# 返回 Zip 文件中包含的文件和文件夹字符串列表
sampleInfo = sampleZip.getinfo('spam.txt') # 对 zipfile 对象使用 getinfo 返回一个文件的 Zipinfo 兑现
sampleInfo.file_size
sampleInfo.compress_size
print('compressed file is %sx smaller!' % (round(sampleInfo.file_size / sampleInfo
        .compress_size,2)))
sampleZip.close


>>> oszip = zipfile.ZipFile('os.zip')
>>> oszip.extractall('./x')

>>> oszip.extract('os/')
'/Users/kevin/os'
>>> oszip.extract('os/a.txt')
'/Users/kevin/os/a.txt'
              
