from core.firebase import db
collection = db.collection("assignments")

def createAssignment(assignment):
    try:
        doc = collection.add(assignment)
        return {"id" : doc[1].id}
    except Exception as e:
        print(" error:", e)
def getAssignments():
    docs = collection.stream()
    assignments = []
    for assignment in docs:
        assignment_data = assignment.to_dict()
        assignment_data["id"] = assignment.id
        assignments.append(assignment_data)
        
    return assignments

