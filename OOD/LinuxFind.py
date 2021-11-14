'''
 Possible followup questions:
 How do you handle boolean logic (current solution put all filters in OR)
 How do you handle an output that would not fit in memory
    1. in stead of return a list of files, pass in an handler (or simply callback), 
        interface FileSearchHandler {
            public void onFileFound(File f);
        }
        where the client can handle it based on its needs
    2. Instead of returning a List, you can pass in a BlockingQueue
        client handle based on its needs. The client will initialize the queue with a size it can take.
        User is supposed to consume the queue. If quue get full, the file search will lock waiting for the queue
        to consumed
'''


from typing import List


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.extension = name.split(".")[1] if "." in name else ""
        self.isDirectory = False if "." in name else True
        self.children = []

    def __repr__(self) -> str:
        return "{" + self.name + "}"


class Filter:
    def __init__(self) -> None:
        pass

    def apply(self, file: File):
        pass


class SizeFilter(Filter):
    def __init__(self, size) -> None:
        super().__init__()
        self.size = size

    def apply(self, file: File):
        return self.size > file.size


class ExtensionFilter(Filter):
    def __init__(self, extension) -> None:
        super().__init__()
        self.extension = extension

    def apply(self, file: File):
        return self.extension == file.extension

# boolean logic of filters


class NotFilter(Filter):
    def __init__(self, filter) -> None:
        super().__init__()
        self.filter = filter

    def apply(self, file: File):
        return not self.filter.apply(file)


class OrFilter(Filter):
    def __init__(self, filters: List[Filter]) -> None:
        super().__init__()
        self.filters = filters

    def apply(self, file):
        for f in self.filters:
            if f.apply(file):
                return True

        return False


class AndFilter(Filter):
    def __init__(self, filters: List[Filter]) -> None:
        super().__init__()
        self.filters = filters

    def apply(self, file):
        isSelected = True
        for f in self.filters:
            if not f.apply(file):
                isSelected = False
                break
        return isSelected


class FileSystem:

    def __init__(self) -> None:
        self.filters = []
        self.singleFilter = None

    def addFilter(self, filter):
        if isinstance(filter, Filter):
            self.filters.append(filter)

    # OR implementation of filter
    def find(self, root):
        result = []

        def findUtil(root: File, result):
            for node in root.children:
                if node.isDirectory:
                    findUtil(node, result)
                else:
                    for filter in self.filters:
                        if filter.apply(node):
                            print(node.name)
                            result.append(node)
        findUtil(root, result)
        return result

    def findPlus(self, root):
        result = []

        def findUtilPlus(root: File, result):
            for node in root.children:
                if node.isDirectory:
                    findUtilPlus(node, result)
                else:
                    if self.singleFilter.apply(node):
                        result.append(node)
        findUtilPlus(root, result)
        return result

    def findAnd(self, root):
        result = []

        def findUtil(root: File, result):
            for file in root.children:
                if file.isDirectory:
                    findUtil(file, result)
                else:
                    isSelected = True
                    for filter in self.filters:
                        if not filter.apply(file):
                            isSelected = False
                            break
                    if isSelected:
                        result.append(file)
        findUtil(root, result)
        return result


f1 = File("StarTrek.txt", 5)
f2 = File("StarWars.xml", 10)
f3 = File("JusticeLeague.txt", 15)
f4 = File("IronMan.txt", 9)
f5 = File("Spock.jpg", 1)
f6 = File("BigBangTheory.txt", 50)
f7 = File("MissionImpossible", 10)
f8 = File("BreakingBad", 11)
f9 = File("root", 100)

f9.children = [f7, f8]
f7.children = [f1, f2, f3]
f8.children = [f4, f5, f6]

filter1 = SizeFilter(5)
filter2 = ExtensionFilter("txt")

fs = FileSystem()
fs.addFilter(filter1)
fs.addFilter(filter2)
print(fs.find(f9))

orFilter = OrFilter([filter1, filter2])
fs.singleFilter = orFilter
print(fs.findPlus(f9))
