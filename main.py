
import Image

import os
import stat
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
            'res': "",
            'size': sbuf.st_size
    }

   # Scanning all directories
    if os.path.isdir(fpath):
        for fname in os.listdir(fpath):
            imageInfos.extend(scan(fname, fpath))
    # file is an image
    if os.path.isfile(fpath) and str(fpath)[-4:].lower() == ".jpg" or str(fpath)[-4:].lower() == ".png" :
        imageInfo.update(type="f")
        imageInfos.append(imageInfo)
    return imageInfos

def show(imageInfos):
    res = []
    for image in imageInfos:
        res.append(image)
    return res

def resize(images):
    for image in images:
        with open(images, 'rb') as f:
            with Image.open(f) as image:
                new_image = image.resize((400, 400))
                new_image.save(image+"1")

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
