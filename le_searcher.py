import os.path as path
from traceback import print_exception

def convert(lesson_file, text_file=None):
    try:
        if not isinstance(lesson_file, str):
            raise TypeError('lesson_file argument type must be a string')
        if not path.exists(lesson_file):
            raise FileNotFoundError('the lesson file path does not exist')
        if text_file == None:
            basename = path.basename(lesson_file)
            text_file = basename.replace(basename.split('.')[-1], 'txt')

        print(basename + ', ' + text_file)
    except Exception as e:
        print_exception(e)