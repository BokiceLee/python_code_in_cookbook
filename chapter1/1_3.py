#preserve the last N elememts
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    print(previous_lines)
    for li in lines:
        if pattern in li:
            yield li, previous_lines    #what is yield
            previous_lines.append(li)


# Example use on a file
if __name__ == '__main__':
    with open(r'./somefile.txt') as f:  #what is "open as"
        for line, prevlines in search(f, 'python', 5):
            #print(line,prevlines)
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
