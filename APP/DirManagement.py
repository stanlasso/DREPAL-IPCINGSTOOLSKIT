import subprocess
from h11 import Data
import streamlit as st
import os


def Management():
    st.markdown("""
    <style>
    </style>
    
    """, unsafe_allow_html=True)
    user = str(os.getcwd())
    # pathdata = user+"/"+"APP/data/"
    # listdir = os.listdir(pathdata)
    # for element in listdir:
    #     st.markdown("""<h1 style="font-size:16px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="20" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M2 6.25A2.25 2.25 0 0 1 4.25 4h3.956a2.25 2.25 0 0 1 1.438.52l2.381 1.98h5.725A2.25 2.25 0 0 1 20 8.75v.752H6.422a2.25 2.25 0 0 0-2.183 1.705l-1.923 7.7c.043-.171 0 .005 0 0a2.24 2.24 0 0 1-.32-1.158L2 6.25z" fill="currentColor"></path><path d="M3.745 19.379A.5.5 0 0 0 4.23 20h14.24a1.75 1.75 0 0 0 1.698-1.326l1.763-7.05a.5.5 0 0 0-.485-.622H6.422a.75.75 0 0 0-.728.568L3.745 19.38z" fill="currentColor"></path></g></svg> {}  {} </h1>""".format(element,len(os.listdir(pathdata+element+"/"))), unsafe_allow_html=True)
    st.info("Click the Clean button to clean analyse directory ")
    if st.button("Clean"):
        bashCmdgz = ['bash APP/bashScripts/delete.sh']
        processex = subprocess.Popen(
            bashCmdgz, stdout=subprocess.PIPE, text=True, shell=True)
        outex, errex = processex.communicate()
        if errex:
            st.error('Delete Probleme')


