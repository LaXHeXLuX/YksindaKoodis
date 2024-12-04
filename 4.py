import time

def nihe(alph, c, amount):
    isUpper = c.isupper()
    c = c.upper()
    if c not in alph: return c

    i = 0
    while alph[i] != c: 
        i += 1

    result = alph[(i + amount) % len(alph)]
    if not isUpper:
        result = result.lower()
    return result

def suurNihe(alph, str, amount):
    newStr = ""
    for c in str:
        newStr += nihe(alph, c, amount)
    return newStr

def koikNihed(alph, string):
    nihed = []
    for i in range(len(alph)):
        nihed.append(suurNihe(alph, string, i))
    return nihed

def main(filename):
    lines = open(filename).readlines()
    
    alph = "ABCDEFGHIJKLMNOPRSŠZŽTUVÕÄÖÜ"

    result = koikNihed(alph, lines[0])
    for i in result:
        print(i)

    return 1
    

if __name__ == "__main__":
    start = time.time()

    print(main("input.txt"))

    end = time.time()
    print("Aeg: " + str(end-start))