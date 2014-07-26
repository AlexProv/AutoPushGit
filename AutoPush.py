import subprocess
import os
import time

repoDir = os.path.dirname(os.path.realpath(__file__))

repoList = open(repoDir + '/dirs','r').read().split()
extensionList = open(repoDir + '/exts','r').read().split()


index = 0
while True:    
    path = repoList[(index) % len(repoList)]
    index+=1
    os.chdir(path)

    files = []
    for f in os.listdir(os.getcwd()):
        files.append(f)
    
    #check for files to commit => will only commit files with the extentions in the exts file
    filesToCommit = []
    for f in files: 
        _,ext = os.path.splitext(f)
        if ext == '' or ext in extensionList:
            filesToCommit.append(f)
    print filesToCommit
    try:
        #execute shell git command
        for f in filesToCommit:
            add = ['git', 'add', f] 
            subprocess.call(add)
        commit = ['git','commit','-m','AutoPush']
        subprocess.call(commit)
        push = ['git','push']
        print subprocess.call(push)
    except:
        print "SHIT WENT BAD"
        break



    print files 
    if index == len(repoList) -1: 
        break
        time.sleep(60*2)




