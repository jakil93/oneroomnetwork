import os


def getList():
    folder_name = 'static/video'
    abs_dir = os.path.join(os.getcwd(), folder_name)
    #get file names
    file_nms = os.listdir(abs_dir)

    return file_nms