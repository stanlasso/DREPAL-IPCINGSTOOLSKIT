import streamlit as st
import datetime
import pandas as pd
import numpy as np
import psutil
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import sqlite3
import subprocess
import Sequence
import visuaqual
import Indexation
import hoteSubtrac
import extraPathogene
import Kdigitsoustract
import varcalling
import annotated
import matricesnps
import DirManagement

userinfo = {}
verification = False

conn = sqlite3.connect('user.db')
c = conn.cursor()
listuser = []
home = ""
userid = 0


def appconnect():
    analyse = False
    session = ""

    msg = ""
    st.markdown("""
  <style>
  .css-12oz5g7 
  {
    flex: 1 1 0%;
    width: 100%;
    padding: 6rem 1rem 10rem;
    max-width: 57rem;
  }
   #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div > button
   { visibility:hidden; }
   #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(1)
   {position: relative;
  }
  #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div
  { /*position: relative;
    margin-top: 43px;
    margin-left: 15px;*/}
  #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > div > div
  { 
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  #cr-er-un-compte > div > span
  { 
    display: flex;
    align-items: center;
    gap: 11px;
  }
  #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(1) {
    position: relative;
    width: 835px;
}
  #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.css-15ew58h.e1tzin5v3 > div:nth-child(1) > div:nth-child(6) > div > div,
  #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.css-15ew58h.e1tzin5v3 > div:nth-child(1) > div:nth-child(6)
  {width:432px;}
  #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.css-15ew58h.e1tzin5v3 > div:nth-child(1) > div:nth-child(7) > div > label
  {visibility:hidden;}
  #root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-1d391kg.e1fqkh3o1 > div.block-container.css-128j0gw.eknhn3m2 > div:nth-child(1) > div:nth-child(3)
  { 
    width: 304px;
    position: relative;
    left: -30px;
  }
  #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div
  { 
    display: flex;
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    --fgp-gap: var(--fgp-gap-container);
    margin-top: var(--fgp-gap);
    margin-right: var(--fgp-gap);
    --fgp-gap-container: calc(var(--fgp-gap-parent,0px) - 1rem)  !important;
    align-items: flex-end;
    }
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div > div.css-12w0qpk.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(16) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(8) > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div.css-1aw8t1a.e1tzin5v3 > div > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(8) > div > div.css-12w0qpk.e1tzin5v2 > div:nth-child(1) > div > div > button
    {
    width: 99px;
    height: 48px;
    }
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(4) > div > div
    {gap: 10px;}
    #root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-1d391kg.e1fqkh3o1 > div.block-container.css-128j0gw.eknhn3m2 > div:nth-child(1) > div:nth-child(4) > div
    {
    width: 304px;
    position: relative;
    bottom: -106px;
    }
    #root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-1d391kg.e1fqkh3o1 > div.block-container.css-128j0gw.eknhn3m2 > div:nth-child(1) > div:nth-child(2) > div > div
    {
    width: 151px;
    z-index: 100;
    position: relative;
    top: 96px;
    left: 83px;
    }
    #root > div:nth-child(1) > div > div > div > div > section.css-1lcbmhc.e1fqkh3o0 > div.css-1d391kg.e1fqkh3o1 > div.block-container.css-128j0gw.eknhn3m2 > div:nth-child(1) > div:nth-child(3) > div > button
    { visibility: collapse;}
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7)
    {
    position: relative;
    border: 2px solid grey;
    padding: 23px;
    box-shadow: -6px -4px 4px 0px silver;
    }
    
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div > div > div.css-12w0qpk.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div.css-3hihkp.e1tzin5v3 > div > div.css-12w0qpk.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(13) > div:nth-child(1) > div > div > div.css-j5r0tf.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div.css-3hihkp.e1tzin5v3 > div > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > button
    {
    width: 91px;
    height: 48px;
    }
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > div > div > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div.css-3hihkp.e1tzin5v3 > div > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > button
    {width: 185px;}
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(13) > div:nth-child(1) > div > div
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > div > div,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(11) > div:nth-child(1) > div.css-3hihkp.e1tzin5v3 > div
    {    
    display: flex;
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    --fgp-gap: var(--fgp-gap-container);
    margin-top: var(--fgp-gap);
    margin-right: var(--fgp-gap);
    --fgp-gap-container: calc(var(--fgp-gap-parent,0px) - 1rem)  !important;
    align-items: flex-end;
    }
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(14) > div:nth-child(1) > div > div > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > button,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > div > div > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > button
    {height: 48px;}
    .css-rncmk8,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > div.css-3hihkp.e1tzin5v3 > div,
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(8) > div
    {
    display: flex;
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    --fgp-gap: var(--fgp-gap-container);
    margin-top: var(--fgp-gap);
    margin-right: var(--fgp-gap);
    --fgp-gap-container: calc(var(--fgp-gap-parent,0px) - 1rem)  !important;
    align-items: flex-end;
    }
    #modebar-3fcded{
      display:none;
    }
    #bui-463__anchor > button{
    height:3rem;
    }
  </style>""", unsafe_allow_html=True)
    verification = False
    with st.container():
        col1, col2 = st.columns([4, 4])
        with col1:
            st.markdown("""""")
            st.markdown("""<h1>IPCI NGS TOOLKIT</h1>""",
                        unsafe_allow_html=True)
            st.image("APP/img/5139810.jpg")
            with st.container():
                st.markdown("""<h4 style="width:100%;text-align:left;">IPCI NGS TOOLKIT </h4> <br> <p style="text-align:justify;"> IPCI NGS TOOLKITS is an application developed within the framework of the "DREPAL" project carried out by the Parasitology Department of the Institut Pasteur de Cote d'Ivoire (IPCI) for the analysis of NGS data. It is a software toolbox composed of stand-alone options or organized as a pipeline for quality control, which remains a crucial step in various downstream analyses. The detection of SNP (Simple Nucleotide Polymorphism), INDELs (INsertion/DELetion) mutations and the elaboration of mutation matrix carried by several samples.</p>""", unsafe_allow_html=True)

        with col2:
            with st.container():
                mode = st.radio("", ("Create an account", "New project"))
                if mode == "Create an account":
                    st.markdown("""<h4><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 28 28"><g fill="none"><path d="M15.114 25.719A7.475 7.475 0 0 1 13 20.5c0-1.688.558-3.247 1.5-4.5H5a3 3 0 0 0-3 3v.715C2 23.433 6.21 26 12 26c1.101 0 2.145-.098 3.114-.281zM18 8A6 6 0 1 0 6 8a6 6 0 0 0 12 0zm2.5 19a6.5 6.5 0 1 0 0-13a6.5 6.5 0 0 0 0 13zm0-11a.5.5 0 0 1 .5.5V20h3.5a.5.5 0 0 1 0 1H21v3.5a.5.5 0 0 1-1 0V21h-3.5a.5.5 0 0 1 0-1H20v-3.5a.5.5 0 0 1 .5-.5z" fill="currentColor"/></g></svg>Create an Account</h4>""", unsafe_allow_html=True)
                    userenr = st.text_input("Username")
                    userpass = st.text_input("Password", type="password")
                    workspace = "/home/{}".format(str(userenr))
                    st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><g fill="none"><path d="M7.175 3h.032l-1.65 1.5H2V4a2 2 0 0 1 2-2h1.75a.5.5 0 0 1 .312.11L7.175 3zM6.086 5.37L8.693 3H12a2 2 0 0 1 2 2v1.341a3 3 0 1 0-4.654 3.747h-.018c-1.131 0-2.113.807-2.297 1.912H4a2 2 0 0 1-2-2V5.5h3.75a.5.5 0 0 0 .336-.13zM11.5 10a2 2 0 1 0 0-4a2 2 0 0 0 0 4zm-2.172 1.088c-.733 0-1.328.577-1.328 1.288c0 1.149.807 2.151 1.958 2.43l.083.02c.958.232 1.96.232 2.918 0l.083-.02c1.15-.279 1.958-1.281 1.958-2.43c0-.711-.595-1.288-1.328-1.288H9.328z" fill="currentColor"/></g></svg> Workspace : <strong style="color:#212121;">{}</strong></p>""".format(workspace), unsafe_allow_html=True)
                    st.text("")
                    if userenr == "" and userpass == "":
                        st.warning("Please fill in all the fields !")
                    else:
                        if st.button("Save"):
                            c.execute('''SELECT Nom FROM UTILISATEUR;''')
                            rows = c.fetchall()
                            for line in rows:
                                if line[0] == str(userenr):
                                    listuser.append(line[0])
                            if len(listuser) != 0:
                                st.error("Existing user! Create your own ... ")
                            else:
                                params = (userenr, userpass, workspace)
                                c.execute(
                                    "INSERT INTO UTILISATEUR VALUES (NULL, ?, ?, ?)", params)
                                conn.commit()
                                bashcmd1 = ["useradd -m {}".format(userenr)]
                                process1 = subprocess.Popen(
                                    bashcmd1, stdout=subprocess.PIPE, text=True, shell=True)
                                out1, err1 = process1.communicate()
                                if err1 == None:
                                    bashcmd2 = [" echo '{}:{}' | chpasswd ".format(
                                        str(userenr), str(userpass))]
                                    process2 = subprocess.Popen(
                                        bashcmd2, stdout=subprocess.PIPE, text=True, shell=True)
                                    out2, err2 = process2.communicate()
                                    if err2 == None:
                                        msg = st.success(
                                            "account creation is done. New project for connect")
                if mode == "New project":
                    st.markdown("""<p style="font-size:28px;display:flex;align-items:center;font-weight:700;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="28" height="28" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><g fill="none"><path d="M8 1v3.5A1.5 1.5 0 0 0 9.5 6H13v7.5a1.5 1.5 0 0 1-1.5 1.5h-7A1.5 1.5 0 0 1 3 13.5V11h1.5a1.5 1.5 0 0 0 1.13-.513l.433 1.444A1.5 1.5 0 0 0 8.7 12.4L9.75 11h.75a1.5 1.5 0 0 0 0-3H9a1.5 1.5 0 0 0-.895.296L7.437 6.07a1.5 1.5 0 0 0-2.779-.24L3.573 8H3V2.5A1.5 1.5 0 0 1 4.5 1H8z" fill="currentColor"/><path d="M9 1.25V4.5a.5.5 0 0 0 .5.5h3.25L9 1.25z" fill="currentColor"/><path d="M6.479 6.356a.5.5 0 0 0-.926-.08L4.19 9H2.5a.5.5 0 0 0 0 1h2a.5.5 0 0 0 .447-.276l.936-1.873l1.138 3.793a.5.5 0 0 0 .879.156L9.25 10h1.25a.5.5 0 0 0 0-1H9a.5.5 0 0 0-.4.2l-.906 1.208L6.48 6.356z" fill="currentColor"/></g></svg>Initialize an analysis</p>""", unsafe_allow_html=True)
                    user = st.text_input('Username')
                    password = st.text_input("Password", type="password")
                    if user == "" and password == "":
                        st.warning(
                            "Please fill in the fields if you have an account")
                    else:
                        params = (user, password)
                        c.execute('''SELECT Nom,Password From UTILISATEUR;''')
                        rows = c.fetchall()
                        for lines in rows:
                            if lines == params:
                                with st.container():
                                    c.execute(
                                        "SELECT worksapce FROM UTILISATEUR WHERE Nom ='{}'".format(user))
                                    rowswk = c.fetchall()
                                    for line in rowswk:
                                        home = line[0]
                                    st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><g fill="none"><path d="M14.413 8h-.062l-2.226-1.78A1 1 0 0 0 11.5 6H8a4 4 0 0 0-4 4v1h7.113l3.3-3zm2.974 0l-5.214 4.74a1 1 0 0 1-.673.26H4v9a4 4 0 0 0 4 4h16a4 4 0 0 0 4-4V12a4 4 0 0 0-4-4h-6.613z" fill="currentColor"/></g></svg> Project name</p>""", unsafe_allow_html=True)
                                    nameprojet = st.text_input(
                                        "", max_chars=25)
                                    projectdir = home+"/Projet/"+nameprojet
                                    st.info(
                                        "Your project will be accessible from the directory below:")
                                    st.markdown("""<p style="color:#1f3946;font-weight:700;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M2 6.25A2.25 2.25 0 0 1 4.25 4h3.956a2.25 2.25 0 0 1 1.438.52l2.381 1.98h5.725A2.25 2.25 0 0 1 20 8.75v.752H6.422a2.25 2.25 0 0 0-2.183 1.705l-1.923 7.7c.043-.171 0 .005 0 0a2.24 2.24 0 0 1-.32-1.158L2 6.25z" fill="currentColor"/><path d="M3.745 19.379A.5.5 0 0 0 4.23 20h14.24a1.75 1.75 0 0 0 1.698-1.326l1.763-7.05a.5.5 0 0 0-.485-.622H6.422a.75.75 0 0 0-.728.568L3.745 19.38z" fill="currentColor"/></g></svg> {}</p>""".format(projectdir), unsafe_allow_html=True)
                                    if st.button("Save"):
                                        c.execute(
                                            "SELECT ID FROM UTILISATEUR WHERE Nom ='{}'".format(user))
                                        rowsid = c.fetchall()
                                        if len(rowsid) != 0:
                                            for line in rowsid:
                                                userid = int(line[0])
                                            c.execute(
                                                "SELECT NomAnalyse FROM ANALYSE WHERE ANALYSE.IDUTILISATEUR='{}'".format(userid))
                                            rowsanalyse = c.fetchall()
                                            for line in rowsanalyse:
                                                if line[0] == nameprojet:
                                                    analyse = True
                                            if analyse == True:
                                                st.error(
                                                    "Existing project ! consult your directory !!")
                                            else:
                                                date = datetime.datetime.now()
                                                today = date.today().strftime("%m/%d/%Y, %H:%M:%S")
                                                params = (
                                                    nameprojet, today, userid)
                                                c.execute(
                                                    "INSERT INTO ANALYSE VALUES (NULL, ?, ?, ?)", params)
                                                conn.commit()
                                                bashcmd3 = [
                                                    "mkdir -p {}".format(projectdir)]
                                                process3 = subprocess.Popen(
                                                    bashcmd3, stdout=subprocess.PIPE, text=True, shell=True)
                                                out3, err3 = process3.communicate()
                                                if err3 == None:
                                                    data = projectdir+"/Datafastq"
                                                    bashcmd5 = [
                                                        "mkdir -p {}".format(data)]
                                                    process5 = subprocess.Popen(
                                                        bashcmd5, stdout=subprocess.PIPE, text=True, shell=True)
                                                    out5, err5 = process5.communicate()
                                                    if err5 == None:
                                                        bashcmdsave = [
                                                            "mv -p {}".format("APP/data"+" "+projectdir)]
                                                        processsave = subprocess.Popen(
                                                            bashcmdsave, stdout=subprocess.PIPE, text=True, shell=True)
                                                        outsave, errsave = process5.communicate()
                                                        if errsave == None:
                                                            st.success(
                                                                "Carry out")
                                    verification = True
                        if lines != params:
                            st.warning(
                                "Inexistent!! check the information by entering or creating an account ...")

    st.empty()
    with st.container():
        st.markdown(
            """<div style="width:100%;heigth:25px;background:grey;"></div>""", unsafe_allow_html=True)
        pass

    if verification == True:
        options = [
            "Sequence Import",
            "Quality Management",
            "Reference Indexing",
            "Subtraction of the Host",
            "Pathogen Extraction",
            "K DDS (Double Digital Subtraction)",
            "Variants Calling (Search Mutation)",
            "Mutation Matrix (SNPs)",
            "Variants Annotations",
            "Directory Management",
        ]
        # sidebar select option navigation
        add_selectbox = st.sidebar.selectbox(
            "OPERATION",
            options,
        )
        # ACCEUIL FRAME
        hdd = psutil.disk_usage('/')
        labels = ["used (GB)", "free (GB)"]
        values = [round(hdd.used / (2**30), 0), round(hdd.free / (2**30), 0)]
        st.sidebar.markdown("## Resource Disk")
        # Use `hole` to create a donut-like pie chart
        layout = go.Layout(autosize=False, width=370, height=500, colorway=[
                           'rgba(0,0,0,0.22)', 'rgba(245, 8, 8, 0.876)'])
        fig = go.Figure(
            data=[go.Pie(labels=labels, values=values, hole=.6,)], layout=layout)
        fig.update_layout(legend=dict(
            orientation="h"), hoverlabel=dict(
                bgcolor="black",
                font_size=12,
        ))
        st.sidebar.plotly_chart(fig)
        st.sidebar.text('IPCI NGS TOOLKIT version : 0.1.2\n')
        choix = add_selectbox
        st.write("")
        st.write("")
        with st.container():
            for elt in options:
                if choix == elt:
                    if elt == "Sequence Import":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="30" height="30" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 13c-2.17 0-4.07 1.16-5.12 2.89c-.6.07-1.23.11-1.88.11c-4.42 0-8-1.79-8-4V9c0 2.21 3.58 4 8 4s8-1.79 8-4v3c0 .36-.1.71-.28 1.05C19.5 13 19.24 13 19 13m-7-2c4.42 0 8-1.79 8-4s-3.58-4-8-4s-8 1.79-8 4s3.58 4 8 4m1.1 6.96c-.36.04-.73.04-1.1.04c-4.42 0-8-1.79-8-4v3c0 2.21 3.58 4 8 4c.46 0 .9 0 1.33-.06A5.94 5.94 0 0 1 13 19c0-.36.04-.7.1-1.04M20 20v-4h-2v4h-2l3 3l3-3h-2z" fill="currentColor"/></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        Sequence.sequence()
                    elif elt == "Quality Management":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2M9 17H7v-7h2v7m4 0h-2V7h2v10m4 0h-2v-4h2v4z" fill="currentColor"/></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        visuaqual.visualisation()
                        st.markdown("""<hr/>""", unsafe_allow_html=True)
                        visuaqual.qualtity()
                    elif elt == "Reference Indexing":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M13.75 10.19l.63.13l4.17 2.08c.7.23 1.16.92 1.1 1.66v.26l-.9 6.12c-.06.43-.25.83-.6 1.11c-.31.3-.72.45-1.15.45h-6.88c-.49 0-.94-.18-1.27-.53L2.86 15.5l.9-1c.24-.25.62-.39.98-.37h.29L9 15V4.5a2 2 0 0 1 2-2a2 2 0 0 1 2 2v5.69h.75z" fill="currentColor"/></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        Indexation.indexRef()
                    elif elt == "Subtraction of the Host":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M4 2h2v2c0 1.44.68 2.61 1.88 3.78c.86.83 2.01 1.63 3.21 2.42l-1.83 1.19C8.27 10.72 7.31 10 6.5 9.21C5.07 7.82 4 6.1 4 4V2m14 0h2v2c0 2.1-1.07 3.82-2.5 5.21c-1.41 1.38-3.21 2.52-4.96 3.63c-1.75 1.12-3.45 2.21-4.66 3.38C6.68 17.39 6 18.56 6 20v2H4v-2c0-2.1 1.07-3.82 2.5-5.21c1.41-1.38 3.21-2.52 4.96-3.63c1.75-1.12 3.45-2.21 4.66-3.38C17.32 6.61 18 5.44 18 4V2m-3.26 10.61c.99.67 1.95 1.39 2.76 2.18C18.93 16.18 20 17.9 20 20v2h-2v-2c0-1.44-.68-2.61-1.88-3.78c-.86-.83-2.01-1.63-3.21-2.42l1.83-1.19M7 3h10v1l-.06.5H7.06L7 4V3m.68 3h8.64c-.24.34-.52.69-.9 1.06l-.51.44H9.07l-.49-.44c-.38-.37-.66-.72-.9-1.06m1.41 10.5h5.84l.49.44c.38.37.66.72.9 1.06H7.68c.24-.34.52-.69.9-1.06l.51-.44m-2.03 3h9.88l.06.5v1H7v-1l.06-.5z" fill="currentColor"/></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        hoteSubtrac.subtrac()
                    elif elt == "Pathogen Extraction":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M4 2h2v2c0 1.44.68 2.61 1.88 3.78c.86.83 2.01 1.63 3.21 2.42l-1.83 1.19C8.27 10.72 7.31 10 6.5 9.21C5.07 7.82 4 6.1 4 4V2m14 0h2v2c0 2.1-1.07 3.82-2.5 5.21c-1.41 1.38-3.21 2.52-4.96 3.63c-1.75 1.12-3.45 2.21-4.66 3.38C6.68 17.39 6 18.56 6 20v2H4v-2c0-2.1 1.07-3.82 2.5-5.21c1.41-1.38 3.21-2.52 4.96-3.63c1.75-1.12 3.45-2.21 4.66-3.38C17.32 6.61 18 5.44 18 4V2m-3.26 10.61c.99.67 1.95 1.39 2.76 2.18C18.93 16.18 20 17.9 20 20v2h-2v-2c0-1.44-.68-2.61-1.88-3.78c-.86-.83-2.01-1.63-3.21-2.42l1.83-1.19M7 3h10v1l-.06.5H7.06L7 4V3m.68 3h8.64c-.24.34-.52.69-.9 1.06l-.51.44H9.07l-.49-.44c-.38-.37-.66-.72-.9-1.06m1.41 10.5h5.84l.49.44c.38.37.66.72.9 1.06H7.68c.24-.34.52-.69.9-1.06l.51-.44m-2.03 3h9.88l.06.5v1H7v-1l.06-.5z" fill="currentColor"/></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        extraPathogene.extract()
                    elif elt == "K DDS (Double Digital Subtraction)":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 18.31V20a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-3.7c-.46-.18-1.05-.3-2-.3a1 1 0 0 1-1-1a1 1 0 0 1 1-1c.82 0 1.47.08 2 .21V12.3c-.46-.18-1.05-.3-2-.3a1 1 0 0 1-1-1a1 1 0 0 1 1-1c.82 0 1.47.08 2 .21V8.3C4.54 8.12 3.95 8 3 8a1 1 0 0 1-1-1a1 1 0 0 1 1-1c.82 0 1.47.08 2 .21V4a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v2.16c1.78.31 2.54.97 2.71 1.13c.39.39.39 1.03 0 1.42c-.39.39-.91.38-1.42 0c0 0-1.04-.71-3.29-.71c-1.26 0-2.09.41-3.05.9c-1.04.51-2.21 1.1-3.95 1.1c-.36 0-.69 0-1-.04V7.95c.3.05.63.05 1 .05c1.26 0 2.09-.41 3.05-.89C14.09 6.59 15.27 6 17 6V4H7v16h10v-2c1.5 0 1.97.29 2 .31M17 10c-1.73 0-2.91.59-3.95 1.11c-.96.48-1.79.89-3.05.89c-.37 0-.7 0-1-.05v2.01c.31.04.64.04 1 .04c1.74 0 2.91-.59 3.95-1.1c.96-.48 1.79-.9 3.05-.9c2.25 0 3.29.71 3.29.71c.51.39 1.03.39 1.42 0c.39-.39.39-1.02 0-1.42C21.5 11.08 20.25 10 17 10m0 4c-1.73 0-2.91.59-3.95 1.11c-.96.48-1.79.89-3.05.89c-.37 0-.7 0-1-.05v2.01c.31.04.64.04 1 .04c1.74 0 2.91-.59 3.95-1.1c.96-.48 1.79-.9 3.05-.9c2.25 0 3.29.71 3.29.71c.51.39 1.03.39 1.42 0c.39-.39.39-1.02 0-1.42C21.5 15.08 20.25 14 17 14z" fill="currentColor"/></svg> """+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        Kdigitsoustract.kdsd()
                    elif elt == "Variants Calling (Search Mutation)":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="38" height="38" preserveAspectRatio="xMidYMid meet" viewBox="0 0 48 48"><g fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M12.857 8c-.46 0-.923.2-1.28.593c-.36.396-.577.952-.577 1.549V18a1 1 0 1 1-2 0v-7.858c0-1.07.385-2.112 1.097-2.894C10.81 6.462 11.802 6 12.857 6H22.5a1 1 0 1 1 0 2h-9.643z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M6.293 14.293a1 1 0 0 1 1.414 0L10 16.586l2.293-2.293a1 1 0 0 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M29.5 40h5.643c.46 0 .923-.2 1.28-.593c.36-.396.577-.952.577-1.549V30a1 1 0 1 1 2 0v7.858c0 1.07-.385 2.112-1.097 2.895C37.19 41.537 36.2 42 35.143 42H29.5a1 1 0 1 1 0-2z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M41.707 33.707a1 1 0 0 1-1.414 0L38 31.414l-2.293 2.293a1 1 0 0 1-1.414-1.414l3-3a1 1 0 0 1 1.414 0l3 3a1 1 0 0 1 0 1.414z" fill="currentColor"/><path d="M17 37a6 6 0 1 0 0-12a6 6 0 0 0 0 12z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M17 26a5 5 0 1 0 0 10a5 5 0 0 0 0-10zm-7 5a7 7 0 1 1 14 0a7 7 0 0 1-14 0z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M15 21a1 1 0 0 1 1-1h2a1 1 0 1 1 0 2h-2a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M22.293 22.293a1 1 0 0 1 1.414 0l2 2a1 1 0 0 1-1.414 1.414l-2-2a1 1 0 0 1 0-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M20.293 26.293l3-3l1.414 1.414l-3 3l-1.414-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M27 29a1 1 0 0 1 1 1v2a1 1 0 1 1-2 0v-2a1 1 0 0 1 1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M22 31a1 1 0 0 1 1-1h4a1 1 0 1 1 0 2h-4a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M26.707 36.293a1 1 0 0 1 0 1.414l-2 2a1 1 0 0 1-1.414-1.414l2-2a1 1 0 0 1 1.414 0z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M22.707 34.293l3 3l-1.414 1.414l-3-3l1.414-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M15 41a1 1 0 0 1 1-1h2a1 1 0 1 1 0 2h-2a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M17 36a1 1 0 0 1 1 1v4a1 1 0 1 1-2 0v-4a1 1 0 0 1 1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M8.293 36.293a1 1 0 0 1 1.414 0l2 2a1 1 0 0 1-1.414 1.414l-2-2a1 1 0 0 1 0-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M13.707 35.707l-3 3l-1.414-1.414l3-3l1.414 1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M7 29a1 1 0 0 1 1 1v2a1 1 0 1 1-2 0v-2a1 1 0 0 1 1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M6 31a1 1 0 0 1 1-1h4a1 1 0 1 1 0 2H7a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M11.707 22.293a1 1 0 0 1 0 1.414l-2 2a1 1 0 0 1-1.414-1.414l2-2a1 1 0 0 1 1.414 0z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M12.293 27.707l-3-3l1.414-1.414l3 3l-1.414 1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M18 21v4.09h-2V21h2z" fill="currentColor"/><path d="M34 18.2a4.2 4.2 0 1 0 0-8.4a4.2 4.2 0 0 0 0 8.4z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M34 10.8a3.2 3.2 0 1 0 0 6.4a3.2 3.2 0 0 0 0-6.4zM28.8 14a5.2 5.2 0 1 1 10.4 0a5.2 5.2 0 0 1-10.4 0z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M32.3 7a1 1 0 0 1 1-1h1.4a1 1 0 1 1 0 2h-1.4a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M33 10.5V7.7h2v2.8h-2z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M37.493 7.693a1 1 0 0 1 1.414 0l1.4 1.4a1 1 0 0 1-1.414 1.414l-1.4-1.4a1 1 0 0 1 0-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M36.093 10.493l2.1-2.1l1.414 1.414l-2.1 2.1l-1.414-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M41 12.3a1 1 0 0 1 1 1v1.4a1 1 0 1 1-2 0v-1.4a1 1 0 0 1 1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M37.2 14a1 1 0 0 1 1-1H41a1 1 0 1 1 0 2h-2.8a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M41.007 17.493a1 1 0 0 1 0 1.414l-1.4 1.4a1 1 0 1 1-1.414-1.414l1.4-1.4a1 1 0 0 1 1.414 0z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M38.207 16.093l2.1 2.1l-1.414 1.414l-2.1-2.1l1.414-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M32.3 21a1 1 0 0 1 1-1h1.4a1 1 0 1 1 0 2h-1.4a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M34 17.2a1 1 0 0 1 1 1V21a1 1 0 1 1-2 0v-2.8a1 1 0 0 1 1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M27.693 17.493a1 1 0 0 1 1.414 0l1.4 1.4a1 1 0 0 1-1.414 1.414l-1.4-1.4a1 1 0 0 1 0-1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M31.907 17.507l-2.1 2.1l-1.414-1.414l2.1-2.1l1.414 1.414z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M27 12.3a1 1 0 0 1 1 1v1.4a1 1 0 1 1-2 0v-1.4a1 1 0 0 1 1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M26 14a1 1 0 0 1 1-1h2.8a1 1 0 1 1 0 2H27a1 1 0 0 1-1-1z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M30.507 7.693a1 1 0 0 1 0 1.414l-1.4 1.4a1 1 0 0 1-1.414-1.414l1.4-1.4a1 1 0 0 1 1.414 0z" fill="currentColor"/><path fill-rule="evenodd" clip-rule="evenodd" d="M30.493 11.907l-2.1-2.1l1.414-1.414l2.1 2.1l-1.414 1.414z" fill="currentColor"/></g></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        varcalling.varcalling()
                    elif elt == "Variants Annotations":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="36" height="36" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g class="icon-tabler" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 12a5 5 0 1 0-5 5"/><path d="M12 7V3m-1 0h2"/><path d="M15.536 8.464l2.828-2.828m-.707-.707l1.414 1.414"/><path d="M17 12h4m0-1v2"/><path d="M12 17v4m1 0h-2"/><path d="M8.464 15.536l-2.828 2.828m.707.707L4.93 17.657"/><path d="M7 12H3m0 1v-2"/><path d="M8.464 8.464L5.636 5.636m-.707.707L6.343 4.93"/><circle cx="17.5" cy="17.5" r="2.5"/><path d="M19.5 19.5L22 22"/></g></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        annotated.annotated()
                    elif elt == "Mutation Matrix (SNPs)":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="36" height="36" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M3 6.25A3.25 3.25 0 0 1 6.25 3h11.5A3.25 3.25 0 0 1 21 6.25v11.5A3.25 3.25 0 0 1 17.75 21H6.25A3.25 3.25 0 0 1 3 17.75V6.25zM6.25 4.5A1.75 1.75 0 0 0 4.5 6.25V8.5h4v-4H6.25zM4.5 10v4h4v-4h-4zm5.5 0v4h4v-4h-4zm5.5 0v4h4v-4h-4zM14 15.5h-4v4h4v-4zm1.5 4h2.25a1.75 1.75 0 0 0 1.75-1.75V15.5h-4v4zm0-11h4V6.25a1.75 1.75 0 0 0-1.75-1.75H15.5v4zm-1.5-4h-4v4h4v-4zm-9.5 11v2.25c0 .966.784 1.75 1.75 1.75H8.5v-4h-4z" fill="currentColor"/></g></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        matricesnps.Matrix()
                    elif elt == "Directory Management":
                        st.markdown("""<h1 style="font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="36" height="36" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M2 6.25A2.25 2.25 0 0 1 4.25 4h3.956a2.25 2.25 0 0 1 1.438.52l2.381 1.98h5.725A2.25 2.25 0 0 1 20 8.75v.752H6.422a2.25 2.25 0 0 0-2.183 1.705l-1.923 7.7c.043-.171 0 .005 0 0a2.24 2.24 0 0 1-.32-1.158L2 6.25z" fill="currentColor"></path><path d="M3.745 19.379A.5.5 0 0 0 4.23 20h14.24a1.75 1.75 0 0 0 1.698-1.326l1.763-7.05a.5.5 0 0 0-.485-.622H6.422a.75.75 0 0 0-.728.568L3.745 19.38z" fill="currentColor"></path></g></svg>"""+str(elt)+"""</h1>""", unsafe_allow_html=True)
                        DirManagement.Management()


bashcmd = ["whoami"]
out = subprocess.check_output(bashcmd)
outprint = str(out)[2:-3]

if outprint != "root":
    st.markdown("""
  <style>
  #contacter-l-admin > div > span
  {
    text-align: center;
    color: #b6a3a3;
    font-size: 25px;
  }
  </style>
  """, unsafe_allow_html=True)
    st.image("APP/img/41Z_2106.w009.n001.3A.p15.3.jpg", clamp=False)
    st.markdown("""<h1 style="text-align:center;">CONTACTER L'ADMIN</h1>""",
                unsafe_allow_html=True)
    st.markdown("""<p style="text-align:center;font-size:18px;font-weight:700;">No running without root ...<br> </p>""", unsafe_allow_html=True)

else:
    appconnect()
