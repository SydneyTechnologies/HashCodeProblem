class customer:
    def __init__(self, likes, dislikes):
        self.likes = likes
        self.dislikes = dislikes

    def checkDisatisfaction(self, dislikeString):
        if dislikeString in self.dislikes:
            return 1
        else:
            return 0

    def checkSatisfaction(self, likeString):
        if likeString in self.likes:
            return 1
        else:
            return 0


inputData = {}
temp = []
unique_likes = []
unique_dislikes = []

disatisfaction = 0
with open('test.txt') as f:
    lines = f.readlines()

for item in range(len(lines)):
    temp.append(lines[item][1:])
    if item % 2 == 1:
        index = item//2 if item > 0 else item
        _likeList = temp[0].split()
        _dislikeList = temp[1].split()
        tempCustomer = customer(_likeList, _dislikeList)
        inputData["customer"+str(index)] = tempCustomer
        temp.clear()


def getUnique(likes=False):
    temp_unique_list = []
    for i in range(len(inputData)):
        if likes == True:
            for j in inputData["customer"+str(i)].likes:
                temp_unique_list.append(j)
        else:
            for j in inputData["customer"+str(i)].dislikes:
                temp_unique_list.append(j)

    temp_unique_list = list(dict.fromkeys(temp_unique_list))
    return(temp_unique_list)


unique_likes = getUnique(True)
unique_dislikes = getUnique(False)

print(unique_likes, unique_dislikes)


def printFinalArray():
    # for customer in range(len(inputData)):
    for dislike in range(len(unique_dislikes)):
        global disatisfaction
        disatisfaction += inputData["customer" +
                                    str(dislike)].checkDisatisfaction(unique_dislikes[dislike])
    print(disatisfaction)
