class MyHashMap(object):

    def __init__(self):
        self.my_list = []

    def put(self, key, value):
        for pair in self.my_list:
            if pair[0] == key:
                pair[1] = value   # update
                return
        
        self.my_list.append([key, value])  # insert new

    def get(self, key):
        for pair in self.my_list:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        for i in range(len(self.my_list)):
            if self.my_list[i][0] == key:
                self.my_list.pop(i)
                return