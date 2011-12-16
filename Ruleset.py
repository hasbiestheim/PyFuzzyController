class Rule:
    def __init__(self, mfdict):
        self.name = 'InitName'
        self.conditions = {}
        self.result = None
        self.mfdict = mfdict
    def addCondition(self, feature, name):
        self.conditions[feature] = Condition(feature, name, self.mfdict[name])
    def removeCondition(self, feature):
        del self.conditions[feature]
    def setResult(self, feature, name):
        self.result = Condition(feature, name, self.mfdict[name])
    def getResult(self, cin):
        mod = 1
        for c in self.conditions:
            mod = min(mod, self.conditions[c].getDegree(cin))
        feature = self.result.feature
        shape = self.result.getShape(mod)
        return (feature,shape)
    
# traffic IS bad
class Condition:
    def __init__(self, feature, name, mf):
        self.feature = feature
        self.name = name
        self.mf = mf
    def getDegree(self, cin):
        inp = cin[self.feature]
        return self.mf.getDegree(inp)
    def getShape(self, degree):
        return self.mf.getResult(degree)

