import le_searcher
import sys, getopt
from traceback import print_exc

audio_file = None
content_type = None
json_file = None
script_name = sys.argv.pop(0)

try:
    if len(sys.argv) < 2:
        raise getopt.GetoptError('error: too few parameters have been passed')
    if len(sys.argv) > 3:
        raise getopt.GetoptError('error: too many parameters have been passed')
    audio_file = sys.argv[0]
    content_type = sys.argv[1]
    if len(sys.argv) == 3:
        json_file = sys.argv[2]
except getopt.GetoptError:
    print_exc()
    if len(sys.argv) < 2:
        i = 0
        while i < 2:
            try:
                print(f'par{i}: {sys.argv[i]}')
                i += 1
            except Exception:
                break
        if i == 0:
            print('error...audio_file not specified')
            print('error...content_type not specified')
        else:
            print('error...content type not specified')
    else:
        i = 3
        while i < len(sys.argv):
            print(f'"{sys.argv[i]}" not recognized')
            i += 1
    sys.exit(1)


if __name__ == '__main__':
    data = le_searcher.convert(audio_file, content_type, json_file)