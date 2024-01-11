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

class Storage(db.Model):
    __tablename__ = 'storage'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('storage.id'))
    parent = relationship('Item', remote_side=[id], backref='children')

# class Status(db.Model):
#     __tablename__ = 'Status'
#     statusID = Column(Integer, primary_key=True, nullable=False, unique=True)
#     name = Column(String(255))

# class Team(db.Model):
#     __tablename__ = 'Team'
#     teamID = Column(Integer, primary_key=True, nullable=False, unique=True)
#     name = Column(String(255))

# class Task(db.Model):
#     __tablename__ = 'Task'
#     taskID = Column(Integer, primary_key=True, nullable=False, unique=True)
#     name = Column(String(255))
#     description = Column(Text)
#     teamID = Column(Integer, ForeignKey('Team.teamID'))
#     task_has_statuses = relationship('TaskHasStatus', cascade='all, delete-orphan')

# class TaskHasStatus(db.Model):
#     __tablename__ = 'TaskHasStatus'
#     taskstatusID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     taskID = Column(Integer, ForeignKey('Task.taskID', ondelete='CASCADE'), nullable=False)
#     statusID = Column(Integer, ForeignKey('Status.statusID'), nullable=False)
#     text = Column(Text)
#     timestamp = Column(DateTime)

# def seed_status_table():
#     # Assuming that the Status table is empty
#     statuses = {
#         1: "Created",
#         2: "Assigned",
#         3: "Work in Progress",
#         4: "Done",
#         5: "Failed"
#     }

#     for key in statuses.keys():
#         status = Status(statusID = key, name=statuses[key])
#         db.session.add(status)

#     db.session.commit()