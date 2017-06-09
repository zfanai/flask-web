#!usr/bin/env python
#coding:utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

print sqlalchemy.__version__
engine = create_engine('mysql://root:myzfsql85@localhost/flaskdb', echo=True)
print dir(engine)

Base = declarative_base()    # declarative_base在sqlalchemy里表示映射模型
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)
	
	def __repr__(self):
		return "<User (name='%s', fullname='%s',password='%s')>" % (
						self.name, self.fullname, self.password)
	