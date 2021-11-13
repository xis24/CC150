from abc import ABC, abstractmethod
from typing import List
import time


class Entry(ABC):
    def __init__(self, name):
        self.name = name
        self.nexts = []

    def __str__(self) -> str:
        return self.name + " " + str(self.size) + " " + self.type


class Directory(Entry):

    def __init__(self, name, nexts: List[str]):
        super().__init__(name)
        self.nexts = nexts


class File(Entry):

    def __init__(self, name: str, size: int, type: str) -> None:
        super().__init__(name)
        self.size = size
        self.type = type

    def __str__(self) -> str:
        return self.name + " " + str(self.size) + " " + self.type

# Filters


class Parameter:
    def __init__(self, size: int, type: str, owner: str = 'xis24', prefix: str = '',
                 suffix: str = '', createdAt: str = 'Nov12', lastUpdated: str = time.time(), lastAccessed: str = time.time()) -> None:
        self.size = size
        self.type = type


class AbstractFilter(ABC):

    def __init__(self, p: Parameter) -> None:
        super().__init__()
        self.paramter = p

    @abstractmethod
    def applyFilter(self, p: Parameter, file: File) -> bool:
        pass

    def filterFiles(self, p: Parameter, entry: Entry):
        ret = []
        self.filterFilesDfs(p, entry, ret)
        return ret

    # DFS
    def filterFilesDfs(self, p: Parameter, entry: Entry, ret: List[File]):
        if isinstance(entry, File) and self.applyFilter(p, entry):
            ret.append(entry)
            return

        for en in entry.nexts:
            self.filterFiles(p, en)


class FulfillAllConditionFilter(AbstractFilter):

    def __init__(self, p: Parameter) -> None:
        super().__init__(p)

    def applyFilter(self, p: Parameter, file: File) -> bool:
        return p.type == file.type and p.size == file.size


class LinuxFind:

    def __init__(self) -> None:
        file = File("helloworld", 128, "1")
        parameter = Parameter(128, "1", "xis24")
        fileFilter = FulfillAllConditionFilter(parameter)
        print(fileFilter.filterFiles(parameter, file))


if __name__ == '__main__':
    obj = LinuxFind()
