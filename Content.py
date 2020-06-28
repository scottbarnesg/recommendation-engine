class Content:
    def __init__(self, name->String, id->Long):
        this.name = name
        this.id = id
        this.attrs = {} # Dict of keywords and weights

    def addAttr(self, key->String, weight->int):
        this.attrs[key] = weight

    def getAttrs(self):
        return this.attrs
