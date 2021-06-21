from PIL import Image

import os
import stat
import getopt
import sys

images  = [] 


def scan(fname, dname):
    imageInfos = []
    
    fpath = os.path.join(dname, fname)
    imageInfo = {
            'fname': fname,
            'dname': dname,
            'size': "",
            'height': "",
            'width': ""
            }

   # filetype dir
    if os.path.isdir(fpath):
        imageInfo.update(type="d")
        imageInfos.append(imageInfo)
        for fname in os.listdir(fpath):
            imageInfos.extend(scan(fpath, fname))
    # filetype file and is image
    if os.path.isfile(fpath) and str(fpath)[-4:].lower() == ".jpg":
        imageInfo.update(type="f")
        with open(fpath, "rb") as f:
            bytes = f.read()  # read entire file as bytes
    return imageInfos


def show(images):
    res = []
    for image in images:
        res.append(image)
    return res


def resize(images, fname):
    print(images)
    for image in images:
        with open(images, 'rb') as f:
            with Image.open(f) as image:
                new_image = image.resize((400, 400))
                new_image.save(fname)
                print(fname)


if __name__ == '__main__':
    # Handle the options and args
    opts, args = getopt.getopt(sys.argv[1:], '?h')
    for opt, arg in opts:
        if opt in [ '-?', '-h' ]:
            print('Usage: {} -[?h] <file> ...'.format(sys.argv[0],))
            sys.exit()
    # Scan and show the file-system trees
    for dname in args:
        fsInfo = scan(dname, '')
        infos = resize(images)