from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from datetime import datetime

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(255))
    description = Column(Text)
    storage_id = Column(Integer, ForeignKey('Storage.id'))  # Foreign key to Storage
    storage = relationship('Storage', back_populates='items')

class Storage(db.Model):
    __tablename__ = 'Storage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('Storage.id'))
    parent = relationship('Storage', remote_side=[id], backref='children')
    items = relationship('Item', back_populates='storage')  # Relationship to Item
