from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, event
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
    parent = relationship('Storage', remote_side=[id], backref=backref('children', cascade='all, delete-orphan'))
    items = relationship('Item', back_populates='storage')  # Relationship to Item

def before_delete(mapper, connection, target):
    # Set parent_id to None for all children of the storage being deleted
    for child in target.children:
        child.parent_id = None
        
@event.listens_for(Storage, 'before_insert')
def validate_parent_id(mapper, connect, target):
    # If parent_id is not None, check if it exists in the database
    if target.parent_id is not None:
        exists = db.session.query(db.exists().where(Storage.id == target.parent_id)).scalar()
        if not exists:
            raise ValueError(f"Parent ID {target.parent_id} does not exist")
        
event.listen(Storage, 'before_delete', before_delete)