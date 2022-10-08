import subprocess
from Sequence import *

sarscovdata="data"
subprocess.run("./APP/bashScripts/download.sh ' %s'"  %"APP/data/Datafastq/"+str(sarscovdata)+".txt", shell=True)