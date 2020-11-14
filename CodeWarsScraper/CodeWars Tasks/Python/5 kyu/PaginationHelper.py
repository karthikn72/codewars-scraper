
import math
class PaginationHelper:

  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page

  def item_count(self):
      return len(self.collection)

  def page_count(self):
      return int(math.ceil(self.item_count()/self.items_per_page)+1)

  def page_item_count(self,page_index):
      page_index+=1
      if page_index<=self.page_count():
        return min((self.item_count() - (self.items_per_page*(page_index-1))),self.items_per_page)
      return -1

  def page_index(self,item_index):
      print(self.collection, self.items_per_page,item_index)
      if item_index<=self.item_count()-1 and item_index>=0 and item_index>self.items_per_page:
        return (len(self.collection[self.items_per_page-((item_index+1)%self.items_per_page):])//self.items_per_page)+1
      elif item_index<=self.items_per_page and item_index<=self.item_count()-1 and item_index>=0:
        return 0
      return -1