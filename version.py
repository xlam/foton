# -*- coding: utf-8 -*-

VERSION_MAJOR = '0'
VERSION_MINOR = '1'
VERSION_PATCH = '1'
VERSION_DEV = 'dev'

def version():
	dev = ''
	if VERSION_DEV:
		dev = '-' + VERSION_DEV
	return VERSION_MAJOR + '.' + VERSION_MINOR + '.' + VERSION_PATCH + dev
