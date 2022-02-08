import cv2
import dropbox
import random
import time
t=time.time()
def pasta():
    oregano=random.randint(0,100)
    whiteSause=cv2.VideoCapture(0)
    brocli=True
    while (brocli):
        ret,frame=whiteSause.read()
        print(ret)
        chiliflakes='img'+str(oregano)+'.png'
        cv2.imwrite(chiliflakes,frame)
        t=time.time
        brocli=False
    return chiliflakes
    print('pasta is ready')
    brocli.release()
    cv2.destroyAllWindows()
def mushroom(imgname):
    onion='zGnrj8CODigAAAAAAAAAATp-garWtAEhiXfeeVRBzCCnbKrRM_07i8PB_4oVZYuk'
    file=imgname
    filefrom=file
    file2='/newfolder1'+(imgname)
    dbx=dropbox.Dropbox(onion)
    with open(filefrom,'rb')as p:
        dbx.files_upload(p.read(),file2,mode=dropbox.files.WriteMode.overwrite)
        print('file has been uploaded')
def delivery():
    while(True):
        if((time.time()-t)>=600):
            name=pasta()
            mushroom(name)
delivery()