#####################################################################
# author : SCR 21/10/21                                             
# ce script permet de faire de l'indexation de reference
# 
#####################################################################


import streamlit as st
import pandas as pd
import os
import subprocess





def indexRef():
    user = str(os.getcwd())

    active =0
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
    program = "bwa"
    process = subprocess. run(['which', program], capture_output=True, text=True)
    # au cas ou le programme existe
    if process.returncode == 0:
        file = user+"/APP/data/Reference"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd = ["ls APP/data/Reference/*.fasta | wc -l"]
            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()
            if err == None:
                if int(out) != 0:
                    st.markdown(
                        """<p style="color:rgb(22, 22, 22);font-weight:600;font-size:14px;">Reference Available :&nbsp;<strong>{}</strong></p>""".format(str(out))
                        ,unsafe_allow_html=True)
                  
                    filenames = os.listdir(file)
                    Refereces = ["-- Choice of a Reference"]
                    for element in filenames:
                        if ".bwt" not in str(element) and ".pac" not in str(element) and ".ann" not in str(element) and ".sa" not in str(element) and ".amb" not in str(element) and ".fai" not in str(element) and ".dict" not in str(element):
                            Refereces.append(element)
                
                    index=[]
                    for name in Refereces:
                        if str(name)+".bwt" in str(filenames) and str(name)+".pac" in str(filenames) and str(name)+".ann" in str(filenames) and str(name)+".sa" in str(filenames) and str(name)+".amb"  in str(filenames):
                            index.append(name)

                    colselctbox,colbtnindex = st.columns([3,1])
                    with colselctbox:
                        option = st.selectbox('Index',list(set(Refereces) - set(index)))
                    with colbtnindex:
                        if st.button("Index") and option !="Choice of a Reference":
                            bashCmd=["bash APP/bashScripts/index.sh {}".format("APP/data/Reference/"+str(option))]
                            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
                            out, err2 = process.communicate()
                            if err2 == None:
                                active=1
                    

                    st.write('')
                    with st.container():
                        st.write("")
                        st.write("")
                        st.markdown("""
                                     <table style="color:black;width:488px;background:aliceblue;;<">
                                      <tr>
                                        <th> Tables of Indexed References </th>
                                      </tr>
                                    </table>""", 
                                    unsafe_allow_html=True)
                        for ref in index:
                            st.markdown("""
                                     <table style="width:488px;padding:25px">
                                      <tr>
                                        <td>{}</td>
                                      </tr>
                                    </table> 
                                    """.format(ref), 
                                    unsafe_allow_html=True)

                        st.write("")
                        st.write("")
                        st.markdown("""<p>Press &nbsp;  <Kbd style="background:black;">R</Kbd> &nbsp;to refresh the list</p>""",unsafe_allow_html=True)
                        if active==1:
                            st.success("Carry out Successfully !!")



                            



