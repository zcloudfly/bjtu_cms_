from sqlalchemy import Column, Integer, String, DateTime, CHAR
from BJTU_CMS.orm import sqlConn

Base= sqlConn.Base

class Category(Base):
    '''
    栏目类
    '''
    __tablename__ = 'cms_category'
    id = Column(String(32), primary_key=True)
    type=Column(String(32), nullable=False)
    type_name = Column(String(200), nullable=False)
    ctime=Column('c_time',DateTime,nullable=True)
    def __init__(self,id,type,type_name,ctime):
        self.id=id
        self.type=type
        self.type_name=type_name
        self.ctime=ctime
    def __repr__(self):
        return '{'+'"id":"{}","type":"{}","type_name":"{}","ctime":"{}"'.format(self.id,self.type,self.type_name,self.ctime)+'}'


class Item(Base):
    '''
    文章类
    '''
    __tablename__ = 'cms_item'
    id = Column(String(32), primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(32), nullable=True)
    category_id = Column(String(32), nullable=False)
    ctime = Column('c_time',DateTime, nullable=False)
    utime = Column('u_time',DateTime, nullable=True)
    status=Column(CHAR,nullable=False)
    creator_id = Column(String(32), nullable=False)
    creator_name = Column(String(100), nullable=True)

    def __repr__(self):
        return '{'+ '"id":"{}","title":"{}","content":"{}","category_id":"{}","creator_name":"{}","ctime":"{}","status":"{}","utime":"{}"'\
            .format(self.id,self.title,self.content,self.category_id,self.creator_name,self.ctime,self.status,self.utime)+'}'

class User(Base):
    '''
    用户类
    '''
    __tablename__='cms_user'
    id=Column(String(32),primary_key=True)
    name = Column(String(50), nullable=False)
    pwd = Column(String(32), nullable=False)
    role=Column(String(20),nullable=True)
    ctime = Column(DateTime, nullable=True)

    def __repr__(self):
        return '{'+ '"id":"{}","name":"{}","role":"{}","ctime":"{}"'\
            .format(self.id,self.name,self.role,self.ctime)+'}'
