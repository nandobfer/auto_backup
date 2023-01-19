import subprocess, json, sys

def newBackup(user):
    proc = subprocess.Popen([f"/scripts/pkgacct {user}"], stdout=subprocess.PIPE, shell=True)
    print()
    (out, err) = proc.communicate()
    
    print(out)
    

user = sys.argv[1]
newBackup(user)