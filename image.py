STATUS, NAME, INFO = range(3)
STATUS_EMPTY = 0
STATUS_PARTIAL = -1
STATUS_FULL = 68

STATUS_STR = {
    '0': '---',
    '-1': '***',
    '68' : '+++',
}

LANDMARKS_FILE = 'landmarks.txt'

IMAGE_TYPES = (
    '.jpg',
    '.gif',
)


class Image(object):
    def __init__(self, name, status=STATUS_EMPTY, info=''):
        self.name = name
        self.status = status
        self.info = info

    def __hash__(self):
        return super(Image, self).__hash__()

    def __repr__(self):
        return 'Image: name={}, status={}'.format(self.name, self.status)
