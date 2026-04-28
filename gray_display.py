import time
import sys

def main():
    try:
        with open(sys.argv[1], 'r') as codeList:
            for line in codeList:
                print(line, end='')
                time.sleep(float(sys.argv[2]))
    except (IndexError, FileNotFoundError):
        print(sys.argv[1] + ' is not a file!')
        print('Usage:')
        print('python gray_display.py [filename] [delay between lines in seconds]')
        print('Filenames outputted by gray.py look like "gray_[length in bits].txt"')

if __name__ == '__main__':
    main()
