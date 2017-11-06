# -*- coding: utf-8 -*-

import os
import image


def scanDirForImages(path):
    files = os.listdir(path)
    images = []
    landmarks = {}

    with open(path + os.sep + image.LANDMARKS_FILE) as f:
        for line in f:
            k, v = line.rstrip('\n').split(':')
            landmarks[k] = int(v)

    for fileName in files:
        for imageType in image.IMAGE_TYPES:
            if fileName.endswith(imageType):
                img = image.Image(fileName)
                if fileName in landmarks.keys():
                    if landmarks[fileName] < image.STATUS_FULL:
                        img.status = image.STATUS_PARTIAL
                        print(img)
                    elif landmarks[fileName] == image.STATUS_FULL:
                        img.status = image.STATUS_FULL
                        print(img)
                images.append(img)
                continue

    return images
