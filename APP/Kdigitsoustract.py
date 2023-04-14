#####################################################################
# author : SCR 21/10/21                                             
# ce script permet de faire de l'unmap et du map K fois
# sequence...
#####################################################################

import streamlit as st
import subprocess
import os
import pandas as pd
import plotly.graph_objects as go



def kdsd():
    user = str(os.getcwd())
    sortie = ""
    idSequence=""
    st.text("")
    # st.markdown(
    #    """## **Bienvenu dans l'option d'importation et de téléchargement de sequence genomique.**""")
    st.text("")
    # with st.expander("USER GUIDE"):
    #     st.write("""
    #  help
    #  """)
    st.markdown("""
    <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 20H4a2 2 0 0 1-2-2V6c0-1.11.89-2 2-2h6l2 2h7a2 2 0 0 1 2 2H4v10l2.14-8h17.07l-2.28 8.5c-.23.87-1.01 1.5-1.93 1.5z" fill="currentColor"/></svg>&nbsp; Choosing References  <strong style="color:crimson;">[Host & Pathogen]</strong> </h3>
     """, unsafe_allow_html=True)
    st.text("")
    # liste de programe réquis
    program ="bwa"
    program2 = "samtools"
    program3="seqkit"
    process=subprocess.run(['which', program], capture_output=True, text=True)
    process2=subprocess.run(['which', program2], capture_output=True, text=True)
    process3 = subprocess.run(['which', program3], capture_output=True, text=True)
    file = user+"/APP/data/Datafastq/"
    if os.path.exists(r'{}'.format(file)) == True:
        bashCmd = ["ls APP/data/Datafastq/*.fastq | wc -l"]
        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = process.communicate()
        if err == None:
            if int(out) != 0:
                filenames = os.listdir(file)
                fastqliste = ["---Index Fastq"]
                for element in filenames:
                    if ".fastq" in str(element):
                        fastqliste.append(element[:-9])
                

    if process.returncode == 0 and process2.returncode == 0 and process3.returncode == 0:
        file = user+"/APP/data/Reference"
        if os.path.exists(r'{}'.format(file)) == True:
            bashCmd1 = ["ls APP/data/Reference/*.pac | wc -l"]
            process1 = subprocess.Popen(bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process1.communicate()
            if err == None:
                if int(out) != 0:
                    filenames = os.listdir(file)
                    Refereces = []
                    for element in filenames:
                        if ".bwt" not in str(element) and ".pac" not in str(element) and ".ann" not in str(element) and ".sa" not in str(element) and ".amb" not in str(element):
                            Refereces.append(element)
                        index=[]
                        for name in Refereces:
                            if str(name)+".bwt" in str(filenames) and str(name)+".pac" in str(filenames) and str(name)+".ann" in str(filenames) and str(name)+".sa" in str(filenames) and str(name)+".amb"  in str(filenames):
                                index.append(name)            
                        

                st.info("SELECTION OF THE HOST BEFORE THE PATHOGEN !!!")
                st.write("")
                opt = st.multiselect(
                     "the host followed by the pathogen",index)
                selecttotal = 0
                liste=["Hôte","Pathogène"]
        
                while selecttotal<2:
                    if len(opt)<3:
                        selecttotal+=1
                        st.spinner(".....")
                        break
                    else:
                        st.error(" Your choice is not allowed!!! Selected [Host , Pathogen] ")
                        break
                    
        if len(opt) == 2:
            st.write("HOST : {}".format(str(opt[0])))
            st.write("PATHOGEN : {}".format(str(opt[1])))
            st.write("")
            with st.container():
                colinput,colSelect,colbtn2 = st.columns([2,2,1])
                with colinput:
                    k=st.number_input("Enter the number K of iteration:",step=1,min_value=2,max_value=3)
                with colSelect:
                    option = st.selectbox('Select Fastq file',sorted(list(set(fastqliste))))
                    idSequence=option
                with colbtn2:
                    if st.button("Start",help="Click to run"):
                        filefastq=user+"/APP/data/Datafastq"
                        if os.path.exists(r'{}'.format(filefastq)) == True:
                            bashCmdrm = ["rm -rf APP/data/Datafastq/KDSD/*"]
                            processrm = subprocess.Popen(bashCmdrm, stdout=subprocess.PIPE, text=True, shell=True)
                            out2,err2=processrm.communicate()
                            if err2 == None:
                                bashCmdcp1 = ["cp APP/data/Datafastq/{} APP/data/Datafastq/KDSD/".format(str(option)+"_R1.fastq")]
                                bashCmdcp2 = ["cp APP/data/Datafastq/{} APP/data/Datafastq/KDSD/".format(str(option)+"_R2.fastq")]
                                processcp = subprocess.Popen(bashCmdcp1, stdout=subprocess.PIPE, text=True, shell=True)
                                processcp1 = subprocess.Popen(bashCmdcp2, stdout=subprocess.PIPE, text=True, shell=True)
                                out0,err0=processcp1.communicate()
                                out2,err3=processcp.communicate()
                                
                                if err3 == None and err0== None:
                                    fastq="APP/data/Datafastq/KDSD/*.fastq"
                                    filehote="APP/data/Reference/"+str(opt[0])
                                    filepato="APP/data/Reference/"+str(opt[1])
                                    bashCmdex = ["bash APP/bashScripts/KDDS.sh {}  {}  {}  {}".format(fastq,filehote,filepato,k)]
                                    processkdds = subprocess.Popen(bashCmdex, stdout=subprocess.PIPE,text=True,shell=True)
                                    out2,err5=processkdds.communicate()
                                    if err5==None:
                                        sortie=out2

        if sortie !="":
            st.success("OPERATION FINISH")
            st.write("")
            lines =""
            filestats=user+"/APP/data/Datafastq/KDSD/Stats"
            if os.path.exists(r'{}'.format(filestats)) == True:
                data = pd.read_table("APP/data/Datafastq/KDSD/Stats/graph.txt",sep="\t")
                listelement=data.loc[:,"num_seqs"]
                liste=[]
                for elt in listelement:
                  liste.append(elt.replace(',','.').split('.'))
                floatList = []
                for el in liste:
                    floatList.append((lambda x: "".join(x[:-1])+"."+x[-1])(el))
                ListeGraph = []
                for elts in floatList:
                    ListeGraph.append(float(str(elts)))
                fig = go.Figure(data=[go.Pie(labels=["HOST", "PATHOGEN", "OTHER"],
                                             values=ListeGraph)])
                st.markdown("###### Share of Host, Pathogen and Other (Sequence Numbers) Constituting the Sequence {}".format(idSequence))
                st.plotly_chart(fig)
    















































                # with open('APP/data/Datafastq/KDSD/Stats/stats.txt') as f:
                #     lines = f.readlines()
                #     for line in lines:
                #         st.markdown(line)

























































            # rm -rfd APP/data/Datafastq/KDSD/*
            # cp APP/data/Datafastq/*.fastq APP/data/Datafastq/KDSD/

            # rm -rfd APP/data/Datafastq/KDSD/*
            # cp APP/data/Datafastq/*.fastq APP/data/Datafastq/KDSD/
            # fastq="APP/data/Datafastq/KDSD/*.fastq"
            #                 filehote="APP/data/Reference/"+str(opt[0])
            #                 filepato="APP/data/Reference/"+str(opt[1])
            #                 bashCmd = ["bash APP/bashScripts/KDDS.sh {}  {}  {}  {}".format(fastq,filehote,filepato,k)]
            #                 processkdds = subprocess.Popen(bashCmd, stdout=subprocess.PIPE,text=True,shell=True)
            #                 out2,err=processkdds.communicate()
            #                 if err == None:
            #                     sortie=out2


                #    
                #             
                #             
                #             if err2 == None:
                #                 bashCmdcp = ["cp APP/data/Datafastq/*.fastq APP/data/Datafastq/KDSD/"]
                #                 processcp = subprocess.Popen(bashCmdcp, stdout=subprocess.PIPE, text=True, shell=True)
                #                 out2,err3=processcp.communicate()
                #                 if err3 == None:
                #                     sortie="1"