from hashlib import sha256

def check(s):
    hashed_obj = sha256(s)
    hashed_s = hashed_obj.hexdigest()
    check = '44d95c031fc7637f944d398f4bae34b868fb70c3e6005fd3d6adb49ca68aee31'
    if hashed_s == check:
        return True
    else:
        return False
