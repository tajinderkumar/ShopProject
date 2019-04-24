def authriseuser(auth, role, dbrole):
    try:
        if auth:
            if role == dbrole:
                return True
            else:
                return False, "not authorised"
        else:
            return False, "not logged in"
    except:
            return False, "not logged in"