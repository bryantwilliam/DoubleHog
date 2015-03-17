__author__ = 'william'


def enum(**enums):
    return type('Enum', (), enums)