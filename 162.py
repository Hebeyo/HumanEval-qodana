def string_to_md5(text):
    # Write your code here
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

