from Model.HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__hashTable = HashTable()

    def insert(self, value):
        return self.__hashTable.insert(  value)

    def find(self, key):
        return self.__hashTable.find(key)

    def __str__(self):
        return str(self.__hashTable)