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

# télechargement 
def save_uploadedfile(uploadedfile):
    with open(os.path.join("APP/data/Datafastq",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
    
    if str(uploadedfile.name).find("txt")== -1:
        pass
    else:
        filename="APP/data/Datafastq/"+str(uploadedfile.name)
        bashCmd = ["bash","APP/bashScripts/download.sh","{}".format(filename)]
        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE,text=True)
        st.write(process.pid)
        process.returncode
        st.write(process.returncode)
        return process

def save_uploadedfileref(uploadedfile):
    with open(os.path.join("APP/data/Reference",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
