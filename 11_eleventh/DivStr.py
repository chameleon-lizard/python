import inspect

class DivStr:
    def __init__(self, value):
        super().__init__()

    for i in str.__dict__:
        if callable(i):
            define = "def " + str(i) + "()" + str(inspect.getfullargspec(str.i)) + ")" + "\n" + "  return DivStr(eval('a'." + str(i) + ")"
            print(define)
            exec(define)