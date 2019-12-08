class LetterAttr():
    def __setattr__(self, name, value=""):
        todel = set(value) - set(name) & set(value)
        for i in todel:
            value = value.replace(i, "")
        super.__setattr__(self, name, value)

    def __getattr__(self, name):
        super.__setattr__(self, name, name)
        return name

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)