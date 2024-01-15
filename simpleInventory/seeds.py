
from simpleInventory.database.db import *

# initial_data = {
#     "Status": [
#         Status(statusID = 1, name = "Created"),
#         Status(statusID = 2, name = "Assigned"),
#         Status(statusID = 3, name = "Work in Progress"),
#         Status(statusID = 4, name = "Done"),
#         Status(statusID = 5, name = "Failed")
#     ]
# }

print("Uploading to DB")

# for key in initial_data.keys():
#     for i in initial_data[key]:
#         db.session.add(i)
#         db.session.commit()