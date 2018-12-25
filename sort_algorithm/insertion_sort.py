class InsertionSort:
    def __init__(self, list_=[]):
        self.list_ = list_

    def get_current_list(self):
        return self.list_

    def ascent_sort(self):
        for i in range(1, len(self.list_)):
            position = i
            current_value = self.list_[i]
            while position > 0 and self.list_[position - 1] > current_value:
                self.list_[position] = self.list_[position - 1]
                position = position - 1
            self.list_[position] = current_value
        return self.list_


# 实例化
list1 = InsertionSort([1, 9, 3, 7])
print(list1.get_current_list())
list1.ascent_sort()
print(list1.get_current_list())
