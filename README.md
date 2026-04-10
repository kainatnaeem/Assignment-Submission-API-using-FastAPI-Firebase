create a virtual env 
pip install fastapi uvicorn firebase-admin python-multipart pydantic email-validator


Firebase Admin SDK cannot “sign in” users with email and password — it can only create users, verify tokens, delete users, etc.

To actually login a user (check their email/password and get an idToken), you have to call Firebase’s REST endpoint.