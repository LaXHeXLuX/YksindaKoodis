import time

def getPrice(line, prices):
    priceIndexes = {}
    for product in prices:
        priceIndexes[product] = 0
    
    sum = 0

    for char in line:
        for product in prices:
            if char == product[priceIndexes[product]]:
                priceIndexes[product] += 1
                if priceIndexes[product] == len(product):
                    sum += prices[product]
                    priceIndexes[product] = 0

    return sum

def main(filename):
    lines = open(filename).readlines()

    prices = {}
    for line in lines:
        parsed = line.split(": ")
        if len(parsed) == 1: break
        prices[parsed[0]] = float(parsed[1])

    print(prices)

    return getPrice(lines[len(lines)-1], prices)
    

if __name__ == "__main__":
    start = time.time()

    print(main("input.txt"))

    end = time.time()
    print("Aeg: " + str(end-start))