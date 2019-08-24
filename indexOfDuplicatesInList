def indexOfDuplicatesInList(inputList, item):
    startingPoint = -1
    locations = []
    while True:
        try:
            loc = inputList.index(item, startingPoint + 1)
        except ValueError:
            break
        else:
            locations.append(loc)
            startingPoint = loc
    return locations
