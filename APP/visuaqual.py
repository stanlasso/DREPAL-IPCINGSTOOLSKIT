#####################################################################
# author : SCR 21/10/21                                             #
# ce script permet la visualisation de fichiers Fastq et gerer la
# qualiter des fichiers
#####################################################################


import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import subprocess
import os

user = str(os.getcwd())


# script de visualisation avec fastqc
def visualisation():
    st.text("")
    # st.markdown(
    #    """## **Bienvenu dans l'option d'importation et de téléchargement de sequence genomique.**""")
    st.text("")
    #section manuel d'utilisation
    # with st.expander("USER GUIDE"):
    #     st.write("""
    #  help
    #  """)
    st.markdown(
        """
        <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M17 18c.56 0 1 .44 1 1s-.44 1-1 1s-1-.44-1-1s.44-1 1-1m0-3c-2.73 0-5.06 1.66-6 4c.94 2.34 3.27 4 6 4s5.06-1.66 6-4c-.94-2.34-3.27-4-6-4m0 6.5a2.5 2.5 0 0 1-2.5-2.5a2.5 2.5 0 0 1 2.5-2.5a2.5 2.5 0 0 1 2.5 2.5a2.5 2.5 0 0 1-2.5 2.5m-7.86-1.75L8.85 19l.29-.74C10.43 15.06 13.5 13 17 13c1.05 0 2.06.21 3 .56V8l-6-6H6c-1.11 0-2 .89-2 2v16a2 2 0 0 0 2 2h4.5c-.55-.66-1-1.42-1.36-2.25M13 3.5L18.5 9H13V3.5z" fill="currentColor"/></svg>&nbsp; Visualization with Fastqc</h3>
        """,
        unsafe_allow_html=True)
    st.write("")
    # verification de l'existence du programme fastqc
    program = "fastqc"
    process = subprocess.run(
        ['which', program], capture_output=True, text=True)
    #verification de trim-galore
    program2 = "trim_galore"
    process2 = subprocess.run(
        ['which', program2], capture_output=True, text=True)
    # au cas ou le programme existe
    if process.returncode == 0 and process2.returncode == 0:
        #activation de la section ci-dessous
        """
        #########
        en bref :
        #########

        cette section fait une verification de l'existence
        de file (chemin)
        puis si celui-ci existe count le nombre de fichiers en son sains
        grace a subprocess. si ce denier est non vide on fait appel au script de generation de fichier .html grâce a fastqc ...

        """
        
        st.write(" ")
        file = user+"/APP/data/Datafastq/"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd = ["ls APP/data/Datafastq/*fastq | wc -l"]
            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()
            if err == None:
                if int(out) != 0:
                    if st.button("Start"):
                        st.markdown(
                            """<p style="margin-top:12px;color:rgb(22, 22, 22);font-weight:600;font-size:14px;">Number of sequences :&nbsp;<strong>{}</strong></p>""".format(str(out)),
                            unsafe_allow_html=True)
                        bashCmd = ["bash  APP/bashScripts/fastqc.sh  APP/data/Datafastq/*.fastq"]
                        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True,shell=True)
                        out, err = process.communicate()
                        if err == None:
                            st.success("Treatment Completed Successfully !!!")
                else:
                    st.error("No files found on which to apply visualization with Fastqc! Import sequences.")

        file = user+"/APP/data/Datafastq/Fastqc"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd = ["ls APP/data/Datafastq/Fastqc/ | wc -l"]
            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()
            if err == None:
                if int(out) != 0:
                    st.markdown(""" 
                        <h5 style="margin-top:25px;"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="26" height="26" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.5 12c2.5 0 4.5 2 4.5 4.5c0 .88-.25 1.71-.69 2.4l3.08 3.1L22 23.39l-3.12-3.07c-.69.43-1.51.68-2.38.68c-2.5 0-4.5-2-4.5-4.5s2-4.5 4.5-4.5m0 2a2.5 2.5 0 0 0-2.5 2.5a2.5 2.5 0 0 0 2.5 2.5a2.5 2.5 0 0 0 2.5-2.5a2.5 2.5 0 0 0-2.5-2.5M9 4l2 2h8a2 2 0 0 1 2 2v3.81A6.48 6.48 0 0 0 16.5 10a6.5 6.5 0 0 0-6.5 6.5c0 1.29.37 2.5 1 3.5H3a2 2 0 0 1-2-2V6c0-1.11.89-2 2-2h6z" fill="currentColor"/></svg>&nbsp;View Analysis Files </h4>
                        """,unsafe_allow_html=True)
                    out=int(out)//2
                    st.markdown(
                        """<p style="color:rgb(22, 22, 22);font-weight:600;font-size:14px;">Searchable html repport link :&nbsp;<strong>{}</strong></p>""".format(str(out))
                        ,unsafe_allow_html=True)
                    filenames = os.listdir(file)
                    html = ["---List of link Fastqc Repport"]
                    for element in filenames:
                        if ".zip" not in str(element):
                                html.append(element)
                    with st.container():
                        colselect,colbtn=st.columns([2,1])
                        with  colselect:
                            option = st.selectbox('Ouvrir',sorted(list(set(html))))

                        with colbtn:
                            if option!="---List of link Fastqc Repport":
                                with open(os.path.join("APP/data/Datafastq/Fastqc/",option), "rb") as file:
                                    st.download_button(
                                           label="Download repport",
                                           data=file,
                                           file_name="{}".format(option),
                                           mime="lien/html")
                        st.write("")
                        st.write("")
                        
    # sinon en renvoie le message le erreur id sera utilisé pour la recherche de solution en fonction de l'erreur : 
    else:
        st.markdown("""<p style="color:rgb(250, 6, 47);font-size:28px;"><i class="fa fa-exclamation-triangle"></i>&nbsp; Le Programme Non Accessible  !!! <strong>[Erreur ID  : ERR002 ]</strong> </p>""",
                             unsafe_allow_html=True)



#####################################################################################
### NEW QUALITY MANAGEMENT
#####################################################################################




def qualtity():
    st.text("")
    st.markdown(
        """
        <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M13 2.03v2.02c4.39.54 7.5 4.53 6.96 8.92c-.46 3.64-3.32 6.53-6.96 6.96v2c5.5-.55 9.5-5.43 8.95-10.93c-.45-4.75-4.22-8.5-8.95-8.97m-2 .03c-1.95.19-3.81.94-5.33 2.2L7.1 5.74c1.12-.9 2.47-1.48 3.9-1.68v-2M4.26 5.67A9.885 9.885 0 0 0 2.05 11h2c.19-1.42.75-2.77 1.64-3.9L4.26 5.67M2.06 13c.2 1.96.97 3.81 2.21 5.33l1.42-1.43A8.002 8.002 0 0 1 4.06 13h-2m5.04 5.37l-1.43 1.37A9.994 9.994 0 0 0 11 22v-2a8.002 8.002 0 0 1-3.9-1.63m9.72-3.18l-4.11-4.11c.41-1.04.18-2.26-.68-3.11c-.9-.91-2.25-1.09-3.34-.59l1.94 1.94l-1.35 1.36l-1.99-1.95c-.54 1.09-.29 2.44.59 3.35c.86.86 2.08 1.08 3.12.68l4.11 4.1c.18.19.45.19.63 0l1.04-1.03c.22-.18.22-.5.04-.64z" fill="currentColor"/></svg>&nbsp;Quality Management</h3>
        """,
        unsafe_allow_html=True)
    st.write("")
    with st.container():
        file = user+"/APP/data/Datafastq"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd = ["ls APP/data/Datafastq/*fastq | wc -l"]
            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()
            st.markdown(""" 
            <h5><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="26" height="26" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M3 17v2h6v-2H3M3 5v2h10V5H3m10 16v-2h8v-2h-8v-2h-2v6h2M7 9v2H3v2h4v2h2V9H7m14 4v-2H11v2h10m-6-4h2V7h4V5h-4V3h-2v6z" fill="currentColor"/></svg>&nbsp;Trimming parameter </h4>
            """
            ,unsafe_allow_html=True)
            st.text('')
            if err == None:
                if int(out) != 0:
                    with st.container():
                        st.markdown("-  Enter the basic number to be deleted at the beginning of the read files : ")
                        col1,col2=st.columns(2)
                        with col1:
                            debutForward=st.number_input("Forward start :",step=1)
                        with col2:
                            debutReverse=st.number_input("Reverse start :",step=1)
                    with st.container():
                        st.markdown("-  Enter the number of bases to be deleted at the end of the read files : ")
                        col3,col4=st.columns(2)
                        with col3:
                            finForward=st.number_input("Forward end :",step=1)
                        with col4:
                            finReverse=st.number_input("Reverse end :",step=1)
                    with st.container():
                        st.write("-  Enter the number of reads to delete with more than n unknown bases in the reads of the forward and reverse files: ")
                        readinconue = st.number_input("Read Fowards/Reverse :",step=1)
                        st.write("-  Enter the number of reads of minimum length & quality n in the forward and reverse files to remember: ")
                        col7,col8=st.columns(2)
                        with col7:
                            longueurmin = st.number_input("Minimum length :",step=1)
                        with col8:
                            qualite = st.number_input("Minimal quality",step=1)

                    with st.container():
                        st.text("")
                        if st.button("Apply"):
                                program1,program2 = 'cutadapt',"trim_galore"
                                process1,process2 = subprocess.run(['which', program1], capture_output=True, text=True),subprocess.run(['which', program2], capture_output=True, text=True)
                                # au cas ou le programme existe
                                if process1.returncode == 0 and process2.returncode == 0:
                                    file = user+"/APP/data/Datafastq/ResQC/"
                                    if os.path.exists(r'{}'.format(file)) == True:
                                        bashCmd = ["ls APP/data/Datafastq/*fastq | wc -l"]
                                        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
                                        out1, err1 = process.communicate()
                                        if err1 == None:
                                            if int(out1) != 0:
                                                #st.markdown(
                                                #    """<p style="color:rgb(22, 22, 22);font-weight:600;font-size:14px;">Number of sequences :&nbsp;<strong>{}</strong></p>""".format(str(out)),
                                                #    unsafe_allow_html=True)
                                                bashCmd1 = ["bash  APP/bashScripts/gestion.sh  {}  {}  {}  {}  {}  {}  {}  {}".format("APP/data/Datafastq/*fastq",str(debutForward),str(debutReverse),str(finForward),str(finReverse),str(readinconue),str(longueurmin),str(qualite))]
                                                process3 = subprocess.Popen(bashCmd1, stdout=subprocess.PIPE, text=True,shell=True)
                                                out3, err3 = process3.communicate()
                                                st.write(out3)
                                                if err3 == None:
                                                    with st.container():
                                                        #st.write(out)
                                                        st.success('Carry out Successfully')
                                                        st.info("Rerun the visualization operation to observe the effects of trimming !!")
                                    else:
                                        st.text('Environment not active')
                else:
                    st.error("No files found on which to apply trimming operation with Trim-galore! Import sequences.")
