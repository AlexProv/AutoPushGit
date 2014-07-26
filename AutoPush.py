import subprocess
import os
import time
import sys

try:
    INTERVAL_TIME = int(sys.argv[1])
except:
    INTERVAL_TIME = 120

repoDir = os.path.dirname(os.path.realpath(__file__))

repoList = open(repoDir + '/dirs','r').read().split()
extensionList = open(repoDir + '/exts','r').read().split()


index = 0
while True:    
    path = repoList[(index) % len(repoList)]
    index+=1
    os.chdir(path)

    files = os.listdir(os.getcwd())
    print files
    #check for files to commit => will only commit files with the extentions in the exts file
    filesToCommit = []

    for f in files: 
        _,ext = os.path.splitext(f)
        if ext == '' or ext in extensionList:
            filesToCommit.append(f)

    try:
        #execute shell git command
        for f in filesToCommit:
            add = ['git', 'add', f] 
            subprocess.call(add)
        commit = ['git','commit','-m','AutoPush']
        subprocess.call(commit)
        push = ['git','push']
        subprocess.call(push)
    except:
        print "Something broke..."
        break

    if 0 == (index) % len(repoList): 
        time.sleep(INTERVAL_TIME)




