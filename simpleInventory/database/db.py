from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, event
from datetime import datetime

db = SQLAlchemy()

class myTable():
    def get_model_dict(model):
        return dict((column.name, getattr(model, column.name)) 
                    for column in model.__table__.columns)

class Item(db.Model, myTable):
    __tablename__ = 'items'  # Use lowercase and plural form for table names
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    storage_id = Column(Integer, ForeignKey('storages.id'), nullable=False)
    storage = relationship('Storage', back_populates='items')


class Storage(db.Model, myTable):
    __tablename__ = 'storages'  # Use lowercase and plural form for table names
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('storages.id'), nullable=True)
    items = relationship('Item', back_populates='storage',
                         cascade="all, delete-orphan")
    parent = relationship('Storage', remote_side=[id], backref=backref(
        'children', cascade='all, delete-orphan'))


def before_delete(mapper, connection, target):
    # Logic remains the same
    for child in target.children:
        child.parent_id = None


def validate_parent_id(mapper, connect, target):
    # Validate parent_id before insert
    if target.parent_id:
        exists = db.session.query(db.exists().where(
            Storage.id == target.parent_id)).scalar()
        if not exists:
            raise ValueError(f"Parent ID {target.parent_id} does not exist")


# Register event listeners
event.listen(Storage, 'before_delete', before_delete)
event.listen(Storage, 'before_insert', validate_parent_id)
