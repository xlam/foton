STATUS, NAME, INFO = range(3)
STATUS_EMPTY = 0
STATUS_PARTIAL = -1
STATUS_FULL = 68

STATUS_STR = {
    '0': '---',
    '-1': '***',
    '68': '+++',
}

LANDMARKS_FILE = 'landmarks.json'

IMAGE_TYPES = (
    '.jpg',
    '.png',
    '.gif',
)


class Image(object):

    def __init__(self, name):
        self.name = name
        self._annotations = {}

    def __hash__(self):
        return super(Image, self).__hash__()

    def __repr__(self):
        return 'Image: name={}, status={}, points={}'.format(
            self.name, self.status(), len(self._annotations))

    def __len__(self):
        return len(self._annotations)

    def annotations(self):
        return self._annotations.items()

    def jsonAnnotations(self):
        anns = []
        for id, coords in self._annotations.items():
            anns.append({'id': id, 'x': coords[0], 'y': coords[1]})
        return anns

    def status(self):
        length = len(self._annotations)
        if (length == STATUS_EMPTY):
            return STATUS_EMPTY
        elif (length < STATUS_FULL):
            return STATUS_PARTIAL
        elif (length == STATUS_FULL):
            return STATUS_FULL

    def len(self):
        return len(self._annotations)

    def setJsonAnnotations(self, json):
        for a in json:
            self.addAnnotation(int(a['id']), int(a['x']), int(a['y']))

    def addAnnotation(self, id, x, y):
        if (1 <= id <= STATUS_FULL):
            self._annotations[str(id)] = (str(x), str(y))

    def deleteAnnotation(self, id):
        del self._annotations[str(id)]


class ImageContainer(object):

    def __init__(self, filename=''):
        self.filename = filename
        self.dirty = False
        self.images = {}

    def image(self, identity):
        return self.images.get(identity)

    def add(self, image):
        self.images[id(image)] = image
        self.dirty = True

    def remove(self, image):
        del self.images[id(image)]
        del image
        self.dirty = True

    def __len__(self):
        return len(self.images)

    def __iter__(self):
        for image in self.images.values():
            yield image
