from core.firebase import db
collection = db.collection("submissions")

def submitAssignment(data):
    try:
        doc = collection.add(data)
        return{"id" : doc[1].id , "message" :"Assignment submitted succesfully"}
    except Exception as e:
        print(" error:", e)

def updateGrade(submission_id, grade):
    try:
        doc_ref = collection.document(submission_id)
        doc_ref.update({"grade": grade})

        return {"message": "Grade updated successfully"}

    except Exception as e:
        return {"error": str(e)}