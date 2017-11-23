STATUS, NAME, INFO = range(3)
STATUS_EMPTY = 0
STATUS_PARTIAL = -1
STATUS_FULL = 3

STATUS_STR = {
    '0': '---',
    '-1': '***',
    '3': '+++',
}

LANDMARKS_FILE = 'landmarks.json'

IMAGE_TYPES = (
    '.jpg',
    '.png',
    '.gif',
)


class Image(object):

    def __init__(self, name, status=STATUS_EMPTY, info=''):
        self.name = name
        self.status = status
        self.info = info
        self.annotations = {}

    def __hash__(self):
        return super(Image, self).__hash__()

    def __repr__(self):
        return 'Image: name={}, status={}, points={}'.format(
            self.name, self.status, len(self.annotations))


class ImageContainer(object):

    def __init__(self, filename = ''):
        self.filename = filename
        self.dirty = False
        self.images = {}

    def image(self, identity):
        return self.images.get(identity)

    def add(self, image):
        self.images[id(image)] = image
        self.dirty = True

    def remove(self, image):
        self.images.remove(id(image))
        del image
        self.dirty = True

    def __len__(self):
        return len(self.images)

    def __iter__(self):
        for image in self.images.values():
            yield image
