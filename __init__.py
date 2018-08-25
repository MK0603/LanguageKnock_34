# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern


class extractVersMethods:

    def loopNovel(self, novelListS):
        versAllList = []
        for sentenseListS in novelListS:
            versAllList.append(self.loopSentense(sentenseListS))
        return versAllList
    
    def loopSentense(self, sentenseListS):
        versList = []
        versList.append(self.confirmStyle(sentenseListS))
        return versList
    
    def confirmStyle(self, sentenseList):
        versList = []
        for i in range(len(sentenseList)):
            if sentenseList[i]["pos"] =="名詞" and sentenseList[i+1]["pos"] =="助詞" and sentenseList[i+2]["pos"] =="名詞":
                if sentenseList[i+1]["base"] =="の":
                    versList.append(sentenseList[i]["surface"])
                    versList.append(sentenseList[i+1]["surface"])
                    versList.append(sentenseList[i+2]["surface"])
                    return versList


if __name__ == '__main__':
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.loopNovel(novelListS)
    print (ans)
