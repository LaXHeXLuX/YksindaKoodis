import time

def parser(lines):
    for i in range(len(lines)): lines[i] = lines[i].strip()

    sundmused = {}
    i = 1
    while lines[i] != "Naabrid:":
        tegevus = lines[i].split(": ")
        sundmused[tegevus[0]] = int(tegevus[1])
        i += 1

    naabrid = lines[i+1:]
    for i in range(len(naabrid)):
        naabrid[i] = naabrid[i].split(": ")[1].split(", N")
        for j in range(len(naabrid[i])):
            if naabrid[i][j][0] != "N": 
                naabrid[i][j] = "N" + naabrid[i][j]
    return [sundmused, naabrid]

def skoor(sundmused, naaber):
    skoor = 0
    for tegevus in naaber:
        skoor += sundmused[tegevus]
    return skoor

def main(filename):
    lines = open(filename, encoding="utf-8").readlines()
    
    parsed = parser(lines)
    sundmused = parsed[0]
    naabrid = parsed[1]

    for sundmus in sundmused:
        print(sundmus)
    
    print()
    for naaber in naabrid:
        print(naaber)
    print()

    maxSkoor = 10
    kahtlane = []

    for i in range(len(naabrid)):
        print(str(i) + ": " + str(skoor(sundmused, naabrid[i])))
        if skoor(sundmused, naabrid[i]) > maxSkoor:
            kahtlane.append(i)

    return len(kahtlane)
    

if __name__ == "__main__":
    start = time.time()

    print(main("input.txt"))

    end = time.time()
    print("Aeg: " + str(end-start))