from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
import models

def verifyToken(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'authToken' in request.cookies:
            token = request.cookies['authToken']
            userId = request.cookies['userId']
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            key = "chavelindadagiovanna"
            data = jwt.decode(token, key, algorithms=["HS256"])
            currentUser = models.User.query.filter_by(id=userId).first()
            if currentUser is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
            else:
                currentUser = {
                "id": userId,
                "token": token
            }
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(currentUser, *args, **kwargs)

    return decorated