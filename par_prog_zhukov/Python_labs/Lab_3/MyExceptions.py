class BinaryTreeException(Exception):
    def __init__(self, *args, **kwargs):
        self.msg = kwargs["message"]
        # self.logger = kwargs["logger"]
        # self.module = kwargs["module"]

    def __str__(self):
        if self.msg:
            return f'BinaryTreeException, {format(self.msg)}'
        else:
            return "BinaryTreeException has been raised"


class HeightLessZero(BinaryTreeException, ValueError):
    def __str__(self):
        if self.msg:
            return f'HeightLessZero, {format(self.msg)}'
        else:
            return "HeightLessZero exception has been raised"


class TooBigHeight(BinaryTreeException):
    def __str__(self):
        if self.msg:
            return f'TooBigHeight, {format(self.msg)}'
        else:
            return "TooBigHeight exception has been raised"



