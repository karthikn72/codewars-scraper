class Block(object):
    def __init__(self,object):
      self.width = object[0]
      self.length = object[1]
      self.height = object[2]
    def get_width(self):
      return self.width
    def get_length(self):
      return self.length
    def get_height(self):
      return self.height
    def get_volume(self):
      return self.height*self.width*self.length
    def get_surface_area(self):
      return (self.height*self.width +self.width*self.length + self.length*self.height)*2
      