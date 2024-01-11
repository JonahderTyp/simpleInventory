from . import db
from .json_encoder import DatabaseEncoder
from .db import Team, Task, TaskHasStatus, Status
from datetime import datetime as dt
from .exceptions import *
from pprint import pprint
from sqlalchemy import desc

def getItem(itemID):
    return {"id":itemID, "name":"placeholder"}

# def getAllTaskHasStatus():
#     return [DatabaseEncoder.default(i) for i in TaskHasStatus.query.all()]

# def setTaskName(taskID: int, name: str):
#     task : Task = Task.query.get(taskID)
#     task.name = name
#     db.session.commit()

# def setTaskDescription(taskID: int, description: str):
#     task : Task = Task.query.get(taskID)
#     task.description = description
#     db.session.commit()

# def getAllTasks():
#     return [DatabaseEncoder.default(i) for i in Task.query.all()]

# def getTaskViaID(taskID : int):
#     return DatabaseEncoder.default(Task.query.get(taskID))

# def createTask(taskID:int, name:str, description: str, how:str = ""):
#     if not Task.query.get(taskID):
#         if int(taskID) < 0:
#             raise Exception("Negativ ID")
#         db.session.add(Task(taskID = taskID, name=name, description=description))
#         db.session.commit()
#         setTaskStatus(taskID,1, how)
#         return DatabaseEncoder.default(Task.query.get(taskID))
#     else:
#         raise ElementAlreadyExists()

# def deleteTask(taskID: int):
#     if Task.query.get(taskID):
#         db.session.delete(db.session.query(Task).get(taskID))
#         db.session.commit()
#     else:
#         raise ElementDoesNotExsist()

# def getAllTeams():
#     results = [DatabaseEncoder.default(i) for i in Team.query.all()]
#     return results

# def getTeamViaID(teamID:int):
#     return DatabaseEncoder.default(Team.query.get(teamID))

# def createTeam(teamID:int, name: str):
#     if not Team.query.get(int(teamID)):
#         if int(teamID) < 0:
#             raise Exception("Negativ ID")
#         db.session.add(Team(teamID = int(teamID), name=name))
#         db.session.commit()
#         return DatabaseEncoder.default(Team.query.get(teamID))
#     else:
#         raise ElementAlreadyExists()

# def deleteTeam(teamID:int):
#     if Team.query.get(teamID):
#             x = db.session.query(Team).get(teamID)
#             db.session.delete(x)
#             db.session.commit()
#     else:
#         raise ElementDoesNotExsist()

# def setTaskStatus(taskID: int, statusID: int, text :str = ""):
#     db.session.add(TaskHasStatus(taskID=taskID, statusID=statusID, text=text, timestamp=dt.now()))
#     db.session.commit()
#     pass

# def setTeamName(teamID: int, name: str):
#     team : Team = Team.query.get(teamID)
#     team.name = name
#     db.session.commit()

# def assignTask(taskID: int, teamID: int, msg :str = ""):
#     #print(f"assigning {taskID} {type(taskID)} to {teamID} {type(teamID)}")
#     task : Task = Task.query.get(taskID)
#     task.teamID = teamID
#     db.session.commit()
#     if teamID == None:
#         pass
#     else:
#         setTaskStatus(taskID, 2, msg)

# def getStatusOfTask(taskID: int):
#     status_entry :TaskHasStatus = TaskHasStatus.query.filter_by(taskID=taskID).order_by(desc(TaskHasStatus.timestamp)).first()

#     if status_entry:
#         # Retrieve the statusID from the status entry
#         statusID = status_entry.statusID

#         # Query the Status table to get the status name based on statusID
#         status : Status = Status.query.get(statusID)

#         result = {
#             'statusID':statusID,
#             'name': status.name,
#             'text': status_entry.text,
#             'timestamp': status_entry.timestamp
#         }

#         return result
#     else:
#         # If no status entry is found, the task might not have a status yet
#         return {
#             'statusID':0,
#             'name': "ERROR",
#             'timestamp': dt.now()
#         }

# def getAllStatusesOfTask(taskID: int):
#     stati = {s.statusID:s.name for s in Status.query.all()}
#     status_entrys = TaskHasStatus.query.filter_by(taskID=taskID).order_by(desc(TaskHasStatus.timestamp)).all()


#     result = []
#     entry : TaskHasStatus
#     for entry in status_entrys:
#         r = {'name' : stati[entry.statusID],
#              'text' : entry.text,
#              'timestamp' : entry.timestamp}
#         result.append(r)

#     return result

# def getAllStatuses():
#     return {s.statusID:s.name for s in Status.query.all()}