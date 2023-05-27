#####################################################################
# author : SCR 21/10/21
# ce script permet de faire de la suoustraction d'une hote dans le
# sequence...
#####################################################################

import streamlit as st
import subprocess
import os


def subtrac():
    user = str(os.getcwd())
    st.text("")
    # st.markdown(
    #    """## **Bienvenu dans l'option d'importation et de téléchargement de sequence genomique.**""")
    st.text("")
    # with st.expander("USER GUIDE"):
    #     st.write("""
    #  help
    #  """)
    st.markdown("""
    <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 20H4a2 2 0 0 1-2-2V6c0-1.11.89-2 2-2h6l2 2h7a2 2 0 0 1 2 2H4v10l2.14-8h17.07l-2.28 8.5c-.23.87-1.01 1.5-1.93 1.5z" fill="currentColor"/></svg>&nbsp; Choose The Reference </h3>
     """, unsafe_allow_html=True)
    st.text("")
    st.markdown("""<style>
    #bui-207__anchor > button,
    #bui-115__anchor > button{
        height:3rem;
    }
    #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(8) > div > div > div > div > div > p{
    width:45rem;
    }
    </style>""",unsafe_allow_html=True)
    # liste de programe réquis
    program = "bwa"
    program2 = "samtools"
    process = subprocess. run(
        ['which', program], capture_output=True, text=True)
    process2 = subprocess. run(
        ['which', program2], capture_output=True, text=True)

    if process.returncode == 0 and process2.returncode == 0:
        file =user+"/APP/data/Reference"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd1 = ["ls APP/data/Reference/*.pac | wc -l"]
            process1 = subprocess.Popen(
                bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process1.communicate()
            if err == None:
                if int(out) != 0:
                    st.info("Select Host Cell Reference :")
                    st.markdown(
                        """<br/><p style="color:rgb(22, 22, 22);font-weight:600;font-size:14px;">Reference Indexed &nbsp;&nbsp;:&nbsp;&nbsp;<strong>{}</strong></p>""".format(str(out)), unsafe_allow_html=True)

                    filenames = os.listdir(file)
                    Refereces = ["Choice of a Reference"]
                    for element in filenames:
                        if ".bwt" not in str(element) and ".pac" not in str(element) and ".ann" not in str(element) and ".sa" not in str(element) and ".amb" not in str(element):
                            Refereces.append(element)
                    with st.container():
                        index = []
                        for name in Refereces:
                            if str(name)+".bwt" in str(filenames) and str(name)+".pac" in str(filenames) and str(name)+".ann" in str(filenames) and str(name)+".sa" in str(filenames) and str(name)+".amb" in str(filenames):
                                index.append(name)
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            option = st.selectbox('Host', list(set(index)))
                        with col2:
                            Start = st.button("Start",help="Click to run")
                        filefastq =user+"/APP/data/Datafastq"
                        bashCmd2 = ["ls APP/data/Datafastq/*.fastq | wc -l"]
                        process2 = subprocess.Popen(
                            bashCmd2, stdout=subprocess.PIPE, text=True, shell=True)
                        out, err = process2.communicate()
                        if os.path.exists(r'{}'.format(filefastq)) == True:
                            if Start:
                                fileSam, fileBam =user+"/APP/data/Sam/",user+"/APP/data/Bam/"
                                if os.path.exists(r'{}'.format(fileSam)) == True and os.path.exists(r'{}'.format(fileBam)) == True:
                                    bashCmd3 = ["ls APP/data/Bam/ | wc -l"]
                                    process3 = subprocess.Popen(
                                        bashCmd3, stdout=subprocess.PIPE, text=True, shell=True)
                                    out, err = process3.communicate()
                                    if err == None:
                                        bashCmd4 = ["bash  APP/bashScripts/unmapped.sh {}  {}".format(
                                            "APP/data/Datafastq/*.fastq", str(option))]
                                        process4 = subprocess.Popen(
                                            bashCmd4, stdout=subprocess.PIPE, text=True, shell=True)
                                        out, err = process4.communicate()
                                        if err == None:
                                            with st.container():
                                                st.success(
                                                    'Carry out Successfully')
                                        else:
                                            st.errorwrite("PROBLEM !!")
                                    else:
                                        st.error("PROBLEM !!")
                                else:
                                    st.error("PROBLEM !!")

                        else:
                            st.error("PROBLEM !!")
                else:
                    st.error("No file was found on which to apply this operation! Import reference.")
            else:
                st.error("PROBLEM !")
        else:
            st.error("PROBLEM !")
    else:
        st.error("PROBLEM !")
