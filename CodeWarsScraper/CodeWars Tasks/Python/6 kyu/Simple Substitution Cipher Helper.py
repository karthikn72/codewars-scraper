class Cipher(object):
    def __init__(self, map1, map2):
        self.map1, self.map2 = map1, map2

    def encode(self, s):
        s_new=""
        for i in s:
          if i in self.map1:
            s_new+=self.map2[self.map1.index(i)]
          else:
            s_new+=i
        return s_new

    def decode(self, s):
        s_new=""
        for i in s:
          if i in self.map2:
            s_new+=self.map1[self.map2.index(i)]
          else:
            s_new+=i
        return s_new