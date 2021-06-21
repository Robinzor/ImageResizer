
from PIL import Image
import os
import getopt
import sys

images  = [] 

def scan(fname, dname):
    imageInfos = []
    fpath = os.path.join(dname, fname)
    sbuf = os.stat(fpath)
    imageInfo = {
            'fname': fname,
            'path':  fpath,
            'size': sbuf.st_size
    }

   # Scanning all directories
    if os.path.isdir(fpath):
        for fname in os.listdir(fpath):
            imageInfos.extend(scan(fname, fpath))
    # file is an image
    ext = str(fpath)[-4:].lower()
    if os.path.isfile(fpath) and ext == ".jpg" or ext == ".jpeg" or ext == ".png" :
        imageInfo.update(type="f")
        imageInfos.append(imageInfo)
    return imageInfos

def show(imageInfos):
    res = []
    for image in imageInfos:
        res.append(image)
    return res

def resize(images, fname):
    with open(images, 'rb') as f:
        with Image.open(f) as image:
            new_image = image.resize((400, 400)) 
            new_image.save(path)


if __name__ == '__main__':
    # Handle the options and args
    opts, args = getopt.getopt(sys.argv[1:], '?h')
    for opt, arg in opts:
        if opt in [ '-?', '-h' ]:
            print('Usage: {} -[?h] <file> ...'.format(sys.argv[0],))
            sys.exit()
    # Scan and show the file-system trees
    for dname in args:
        imageInfos = scan(dname, '')
        infos = show(imageInfos)
        for info in infos:
            print(info)
            path = info["path"]
            fname = info["fname"]
            resize(path, fname)
