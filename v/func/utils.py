def base_dir_to_win_dir(path):
    splitStr = path.split('/')
    del splitStr[:2]
    splitStr[0] = (splitStr[0] + ":")
    h = "/".join(splitStr)
    h.strip()
    return h