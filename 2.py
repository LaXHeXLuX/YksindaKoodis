import time

def makeMatrixLine(line):
    matrixLine = []

    for char in line:
        if char == "X":
            matrixLine.append(True)
        else:
            matrixLine.append(False)

    return matrixLine

def main(filename):
    lines = open(filename).readlines()

    matrix = []
    for line in lines:
        matrix.append(makeMatrixLine(line))

    maxes = [-1, -1, -1, -1] # maxI, minI, maxJ, minJ

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                if i > maxes[0] or maxes[0] == -1: maxes[0] = i
                if i < maxes[1] or maxes[1] == -1: maxes[1] = i
                if j > maxes[2] or maxes[2] == -1: maxes[2] = j
                if j < maxes[3] or maxes[3] == -1: maxes[3] = j

    return (maxes[0] - maxes[1] + maxes[2] - maxes[3] + 4) * 2
    

if __name__ == "__main__":
    start = time.time()

    print(main("input.txt"))

    end = time.time()
    print("Aeg: " + str(end-start))