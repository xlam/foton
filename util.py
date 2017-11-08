# -*- coding: utf-8 -*-

import os
import json
import image


def scanDirForImages(path):
    files = os.listdir(path)
    images = []

    annotations = loadAnnotations(path + os.sep + image.LANDMARKS_FILE)

    for fileName in files:
        for imageType in image.IMAGE_TYPES:
            if fileName.endswith(imageType):
                img = image.Image(fileName)
                savedImagesNames = annotations.keys()
                if fileName in savedImagesNames:
                    a = annotations[fileName]
                    if image.STATUS_EMPTY < len(a['points']) < image.STATUS_FULL:
                        img.status = image.STATUS_PARTIAL
                    elif len(a['points']) == image.STATUS_FULL:
                        img.status = image.STATUS_FULL
                    img.annotations = a['points']
                print(img)
                images.append(img)
                continue

    return images


def loadAnnotations(filename):
    anns = json.load(open(filename))
    print(anns)
    annotations = {}
    for a in anns:
        print(a)
        annotations[a['name']] = a
    return annotations


def _getSavedImagesNames(annotations):
    names = []
    for img in annotations:
        names.append(img[name])
    return names
