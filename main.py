class keyGen:
    def __init__(self, PK):
        self.pChoice = [57, 49, 41, 33, 25, 17, 9,
                        1, 58, 50, 42, 34, 26, 18,
                        10, 2, 59, 51, 43, 35, 27,
                        19, 11, 3, 60, 52, 44, 36,
                        63, 55, 47, 39, 31, 23, 15,
                        7, 62, 54, 46, 38, 30, 22,
                        14, 6, 61, 53, 45, 37, 29,
                        21, 13, 5, 28, 20, 12, 4]
        self.pChoice2 = [14, 17, 11, 24, 1, 5,
                         3, 28, 15, 6, 21, 10,
                         23, 19, 12, 4, 26, 8,
                         16, 7, 27, 20, 13, 2,
                         41, 52, 31, 37, 47, 55,
                         30, 40, 51, 45, 33, 48,
                         44, 49, 39, 56, 34, 53,
                         46, 42, 50, 36, 29, 32]
        self.shiftCount = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        self.plainKey = PK

        self.binaryPlainKey = self.conBinary(self.plainKey)
        self.keyPermuted = self.permute(self.binaryPlainKey, self.pChoice)

        self.C = [self.keyPermuted[:len(self.keyPermuted)//2]]
        self.D = [self.keyPermuted[len(self.keyPermuted)//2:]]
        
        self.shifter(self.C)
        self.shifter(self.D)

        self.K = self.joinKey(self.C, self.D)
        self.K = self.secondPermute(self.K, self.pChoice2)

    def joinKey(self, c, d):
        temp =[]
        for i in range(16):
            temp.append(c[i]+d[i])
        return temp

    def conBinary(self,string):
        temp=[]
        for i in [bin(ord(x))[2:] for x in string]:
            while len(i) < 8:
                i=str(0)+i
            temp.extend(i)
        return temp

    def permute(self, binaryPlainKey, permutedChoice):
        return [binaryPlainKey[i-1] for i in permutedChoice]

    def secondPermute(self, key, permutedChoice):
        temp =[]
        temp1=[]
        for key in key:
            for i in permutedChoice:
                temp1.append(key[i-1])
            temp.append(temp1)
        return temp

    def shifter(self, vlaue):
        temp = vlaue[0]
        for i in self.shiftCount:
            temp = temp[i:]+temp[:i]
            vlaue.append(temp)
        return

Key = keyGen('Mohammed')
