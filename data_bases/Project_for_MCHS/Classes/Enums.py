from enum import Enum

class RPE(Enum):
    DASV = 1
    DASK =2

class group(Enum):
    MEDIUM_GROUP = 1 # средний и старший начальствующий состав '', '')
    SMALL_GROUP = 2 # рядовой и младший начальствующий состав
    SMALLEST_GROUP = 3 #работник
