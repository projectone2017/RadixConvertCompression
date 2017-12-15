# -*- coding: utf-8 -*-


class Compress:

    def __init__(self, n=16, m=94):
        self.__n = n
        self.__m = m

    def compress(self, data):
        self.__intAry = self.__str2int(data)
        self.__intAry = self.__radixconvert(self.__intAry, self.__n, self.__m)
        self.__compData = self.__compress(self.__intAry)
        return self.__compData

    def uncompress(self, data):
        self.__intAry = self.__uncompress(data)
        self.__intAry = self.__radixconvert(self.__intAry, self.__m, self.__n)
        self.__uncompData = self.__int2str(self.__intAry)
        return self.__uncompData

    def __radixconvert(self, ary, n, m):
        r = []
        while any(ary):
            c = 0
            for i in range(len(ary)):
                c = c * n + ary[i]
                ary[i], c = divmod(c, m)
            r.append(c)
        r.reverse()
        return r

    def __str2int(self, d):
        r = []
        for i in range(len(d)):
            if d[i] == int:
                r.append(d[i])
                continue
            c = ord(d[i].lower())
            if ord('0') <= c <= ord('9'):
                r.append(c - ord('0'))
            elif ord('a') <= c <= ord('z'):
                r.append(c - ord('a') + 0xA)
        return r

    def __int2str(self, d):
        r = ""
        for i in range(len(d)):
            r += "{0:x}".format(d[i])  # {0:X}:大文字 {0:x}:小文字
        return r

    def __compress(self, d):
        r = ""
        for i in range(len(d)):
            r += chr(d[i] + 0x21)  # ASCIIコード 図形文字開始0x21
        return r

    def __uncompress(self, d):
        r = []
        for i in range(len(d)):
            if d[i] == int:
                r.append(d[i])
            else:
                r.append(ord(d[i]) - 0x21)  # ASCIIコード 図形文字開始0x21
                continue
        return r
