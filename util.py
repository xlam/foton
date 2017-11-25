# -*- coding: utf-8 -*-

import os
import json
import image


def scanDirForImages(path):
    files = os.listdir(path)
    images = []

    annotations = loadAnnotations(path + os.sep + image.LANDMARKS_FILE)
    savedImagesNames = annotations.keys()

    for fileName in files:
        for imageType in image.IMAGE_TYPES:
            if fileName.endswith(imageType):
                img = image.Image(fileName)
                if fileName in savedImagesNames:
                    a = annotations[fileName]
                    img.setJsonAnnotations(a['points'])
                print(img)
                images.append(img)
                continue

    return images


def loadAnnotations(filename):
    annotations = {}
    anns = json.load(open(filename))
#    print(anns)
    for a in anns:
#        print(a)
        annotations[a['name']] = a
    return annotations
