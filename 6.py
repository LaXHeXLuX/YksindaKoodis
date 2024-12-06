import time

def parser(lines):
    pass

def number(lines, i, j, down, l):
    s = ""
    for i2 in range(l):
        if down: s += lines[i+i2][j]
        else: s += lines[i][j+i2]
    return s

def validNumber(lines, i, j, start, down):
    for inc in range(len(start)):
        if down:
            if lines[i + inc][j] != start[inc]:
                return ""
        else:
            if lines[i][j + inc] != start[inc]:
                return ""
    
    return number(lines, i, j, down, 7)

def main(filename):
    lines = open(filename, encoding="utf-8").readlines()
    lines = [line.strip() for line in lines]
    
    start = lines[0]
    count = []
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            if (i+6) < len(lines):
                result = validNumber(lines, i, j, start, True)
                if result != "": count.append(result)
            if (j+6) < len(lines[i]):
                result = validNumber(lines, i, j, start, False)
                if result != "": count.append(result)

    return count
    

if __name__ == "__main__":
    start = time.time()

    result = main("input.txt")
    result.sort()
    for i in result:
        print(i, end=", ")
    print()

    end = time.time()
    print("Aeg: " + str(end-start))