
class Recommender:
    def __init__(self):
        self.maxWeight = 100

    def calculateContentMatch(user->User, content->Content):
        aggregateDeltas = []
        userContentList = user.getContentList()
        for userContent in userContentList:
            deltas = []
            for key, weight in userContent.getAttrs().items():
                if key not in content.getAttrs():
                    throw ValueError("Invalid key")
                contentWeight = content.getAttrs()[key]
                delta = abs(weight-contentWeight)
                deltas.append(delta)
            aggregateDeltas.append(deltas)

        deltaSums = []
        for deltas in aggregateDeltas:
            deltaSums.append(sum(deltas)/self.maxWeight)

        return deltaSums
