def djb2(data):
    hash = 5381
    data = str(data)
    for char in data:
        hash = ((hash << 5) + hash) + ord(char)
    return str(hash)