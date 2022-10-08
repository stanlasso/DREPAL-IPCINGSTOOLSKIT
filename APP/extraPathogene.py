#####################################################################
# author : SCR 21/10/21                                             
# ce script permet de faire de la suoustraction d'une hote dans le
# sequence... "rm
#####################################################################

import streamlit as st
import subprocess
import os



def extract():
    user = str(os.getcwd())
    mapped=0
    st.text("")
    # st.markdown(
    #    """## **Bienvenu dans l'option d'importation et de téléchargement de sequence genomique.**""")
    st.text("")
    with st.expander("USER GUIDE"):
        st.write("""
     help
     """)
    st.markdown("""
    <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 20H4a2 2 0 0 1-2-2V6c0-1.11.89-2 2-2h6l2 2h7a2 2 0 0 1 2 2H4v10l2.14-8h17.07l-2.28 8.5c-.23.87-1.01 1.5-1.93 1.5z" fill="currentColor"/></svg>&nbsp; Choose The Reference</h3>
     """, unsafe_allow_html=True)
    st.text("")
    # liste de programe réquis
    program ="bwa"
    program2 = "samtools"
    process=subprocess. run(['which', program], capture_output=True, text=True)
    process2=subprocess. run(['which', program2], capture_output=True, text=True)
   

    if process.returncode == 0 and process2.returncode == 0:
        file = user+"/APP/data/Reference"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd = ["ls APP/data/Reference/*.pac | wc -l"]
            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()
            if err == None:
                if int(out) != 0:
                    st.info("Choose the Pathogen Reference [Virus, Parasite, ...] :")
                    st.markdown(
                        """<br/><p style="color:rgb(22, 22, 22);font-weight:600;font-size:14px;">Reference Indexed :&nbsp;<strong>{}</strong></p>""".format(str(out))
                        ,unsafe_allow_html=True)

                    filenames = os.listdir(file)
                    Refereces = ["Choose The Reference"]
                    for element in filenames:
                        if ".bwt" not in str(element) and ".pac" not in str(element) and ".ann" not in str(element) and ".sa" not in str(element) and ".amb" not in str(element):
                            Refereces.append(element)
                    with st.container():
                        index=[]
                        for name in Refereces:
                            if str(name)+".bwt" in str(filenames) and str(name)+".pac" in str(filenames) and str(name)+".ann" in str(filenames) and str(name)+".sa" in str(filenames) and str(name)+".amb"  in str(filenames):
                                index.append(name)
                        col1,col2= st.columns([3,1])
                        with col1:
                            option = st.selectbox('List of Reference',list(set(index)))
                        with col2:
                            Activer=st.button("Start",help="Click to run")
                        st.write("")
                        filefastq = user+"/APP/data/Datafastq/unmapped"
                        bashCmd = ["ls APP/data/Datafastq/unmapped/ | wc -l"]
                        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
                        out, err = process.communicate()
                        if os.path.exists(r'{}'.format(filefastq)) == True and str(out) != "0":
                            if Activer:
                                fileSam, fileBam = user+"/APP/data/Sam/", user+"/APP/data/Bam/"
                                if os.path.exists(r'{}'.format(fileSam)) == True and os.path.exists(r'{}'.format(fileBam)) == True:
                                    bashCmd = ["ls APP/data/Bam/Mapped/ | wc -l"]
                                    process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
                                    out, err = process.communicate()
                                    if err == None:
                                        mapped=int(out)
                                        option="APP/data/Reference/"+str(option)
                                        bashCmd1 = ["bash  APP/bashScripts/mapped.sh {}  {}".format("APP/data/Datafastq/unmapped/*.fastq",str(option))]
                                        process3 = subprocess.Popen(bashCmd1, stdout=subprocess.PIPE, text=True,shell=True)
                                        out, err = process3.communicate()
                                        if err == None:
                                            with st.container():
                                                st.success('Effectuer Avec Succès')
                                        else:
                                            st.write("PROBLEME1 !!")
                                    else:
                                            st.write("PROBLEME2 !!")
                                else:
                                            st.write("PROBLEME3 !!")
                      
                        else:
                                            st.write("NOT SEQUENCES ADDED !!")
                else:
                                            st.write("PROBLEME6 !!")
            else:
                                            st.write("PROBLEME7 !!")
        else:
                                            st.write("PROBLEME8 !!")
    else:
                                            st.write("PROBLEME9 !!")
    st.markdown("""
    <style>
    #bui-304__anchor > button {
    height: 3rem;
    }
    </style>
    """
    ,unsafe_allow_html=True)