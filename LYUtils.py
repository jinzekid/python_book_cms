'''
LYUtils.py
'''

'''
快速排序
'''
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def quick_sort(seq):
    if len(seq) <= 1: return seq
    lo, pi, hi = partition(seq)
    return quick_sort(lo) + pi + quick_sort(hi)


'''
Database connect
'''
import  pymongo

# 单例模式
# 使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

# 装饰器版本
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class DBManager(object):

    def __init__(self):
        self.myClient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.mydb = self.myClient['test']

    def check_user(self, username, password):
        cUser = self.mydb['test']
        count = cUser.find({'name':username,'pwd':password}).count()
        if count > 0:
            print('find user!')
            return True

        print('illege user!')
        return False

    def insert(self, bookInfo):
        pass

    def delete(self, bookInfo):
        pass

    def search(self, bookInfo):
        cBook = self.mydb['books']
        books = cBook.find(bookInfo)
        #for book in books:
        #    print(str(book))
        return books
