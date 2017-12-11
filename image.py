import pickle

STATUS, NAME, INFO = range(3)
STATUS_EMPTY = 0
STATUS_PARTIAL = -1
STATUS_FULL = 6

STATUS_STR = {
    str(STATUS_EMPTY): '---',
    str(STATUS_PARTIAL): '***',
    str(STATUS_FULL): '+++',
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
            anns.append({'id': str(id), 'x': str(coords[0]), 'y': str(coords[1])})
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
            self.addAnnotation(a['id'], a['x'], a['y'])

    def addAnnotation(self, id, x, y):
        if (1 <= int(id) <= STATUS_FULL):
            self._annotations[int(id)] = (int(x), int(y))

    def deleteAnnotation(self, id):
        del self._annotations[int(id)]


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

    def savePickle(self, filename):
        file = open(filename, mode='wb')
        pickle.dump(self.images, file, pickle.DEFAULT_PROTOCOL)
        file.close()

    def loadPickle(self, filename):
        file = open(filename, mode='rb')
        values = pickle.load(file)
        for value in values.values():
            print('Value: "{}", type: {}'.format(value, type(value)))
            self.add(value)
        file.close()

    def __len__(self):
        return len(self.images)

    def __iter__(self):
        for image in self.images.values():
            yield image
