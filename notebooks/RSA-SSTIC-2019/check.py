import hashlib

def check(key):
    return hashlib.sha256(key.to_bytes(1024, byteorder='big')).hexdigest() == '4d469947f6092a5abab44431a43d73feb9d959aadd3cde377dbbacc554826e3d'