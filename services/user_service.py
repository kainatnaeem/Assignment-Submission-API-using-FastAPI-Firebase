from fastapi import HTTPException
from schemas.user_schema import SignUpSchema, SigninSchema
from core.firebase import API_KEY, firebase_auth_admin,db,firebase_auth
import requests

def register_user(data: SignUpSchema):
     try:
        user = firebase_auth_admin.create_user(
            email=data.email,
            password=data.password,
            display_name=data.name,
          
        )

        # Save in Firestore
        db.collection("users").document(user.uid).set({
            "uid": user.uid,
            "name": data.name,
            "email": data.email,
            "role": data.role

        })

        return {"message": "User created successfully"}

     except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def signin_user(data: SigninSchema):
    try:
        user = firebase_auth.sign_in_with_email_and_password(
            data.email,
            data.password
        )
        return {"idToken": user["idToken"], "localId": user["localId"]}
    except Exception as e:
        print("Firebase login error:", e)
        raise HTTPException(status_code=400, detail="Invalid credentials")