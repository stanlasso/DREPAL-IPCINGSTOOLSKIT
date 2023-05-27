#####################################################################
# author : SCR 21/10/21                                             #
# ce script permet le stockage des données importer depuis une      #
# une source dans notre repertoire data/Datafastq/ pour le traitement   #
#####################################################################
# A faire prise en compte de fichiers zip et importation en locale 
# via un chemin de fichiers tout type
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os
import streamlit as st  
import subprocess
import pandas as pd
from pywget import wget
import glob

homeapp=str(os.getcwd())
# télechargement 
def save_uploadedfile(uploadedfile):
    with open(os.path.join("APP/data/Datafastq",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
    
    if str(uploadedfile.name).find("txt")== -1:
        pass
    else:
        filename="APP/data/Datafastq/"+str(uploadedfile.name)
        os.rename(filename,"APP/data/Datafastq/fileftp.txt")
        dfftp=pd.read_table("APP/data/Datafastq/fileftp.txt",sep="\t")
        ftplink=dfftp["fastq_ftp"]
        for line in ftplink:
            ftptable=line.split(";")
            if len(ftptable) == 2:
                ftplink1,ftplink2=ftptable[0],ftptable[1]
                wget.download('http://'+str(ftplink1), homeapp+"/APP/data/Datafastq")
                wget.download('http://'+str(ftplink2), homeapp+"/APP/data/Datafastq")
                
        
        os.remove("APP/data/Datafastq/fileftp.txt")
        bashCmdgz = ['bash APP/bashScripts/gunzip.sh']
        processex= subprocess.Popen(bashCmdgz, stdout=subprocess.PIPE, text=True, shell=True)
        outex, errex = processex.communicate()
        if errex == None:
            gzfile=glob.glob(homeapp+"/APP/data/Datafastq/*.fastq")
            for el in gzfile:
                element=str(el).split("_")
                if element[1]=="1.fastq" or element[1]=="2.fastq":
                    os.rename(el,element[0]+"_R"+element[1])
        

        # bashCmd = ["bash","APP/bashScripts/download.sh","{}".format(filename)]
        # process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE,text=True)
        # process.returncode

def save_uploadedfileref(uploadedfile):
    with open(os.path.join("APP/data/Reference",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
