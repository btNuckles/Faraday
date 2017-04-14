class ItemList:
    items = []

    def appendItem(self, item):
        self.items.append(item)
        return

    def insertItem(self, item, position):
        self.items.insert(position, item)
        return

    def returnUniques(self, items):
        uniqueList = []
        for item in items:
            if item not in uniqueList:
                uniqueList.append(item)
        return uniqueList

    def returnAll(self, items):
        itemList = []
        uniqueList = []
        uniqueCount = []

        for item in items:
            for index in xrange(len(uniqueList)):
                if uniqueList[index] is item:
                    uniqueCount[index] = uniqueCount[index] + 1
                    break
            if item not in uniqueList:
                uniqueList.append(item)
                uniqueCount.append(1)

        for index in xrange(len(uniqueList)):
            itemList.append([uniqueList[index], uniqueCount[index]])

        return itemList
