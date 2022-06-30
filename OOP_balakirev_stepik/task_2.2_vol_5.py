class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.left = self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, data):
        self.__left = data

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, data):
        self.__right = data


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj
