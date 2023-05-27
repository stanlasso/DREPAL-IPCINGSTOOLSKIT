#####################################################################
# author : SCR 21/10/21
# ce script permet de faire du variant calling
# sequence...
#####################################################################

import streamlit as st
import subprocess
import os
import pandas as pd


def varcalling():
    user = str(os.getcwd())
    st.text("")
    # with st.expander("USER GUIDE"):
    #     st.write("""
    #  help
    #  """)
    st.markdown("""
    <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 20H4a2 2 0 0 1-2-2V6c0-1.11.89-2 2-2h6l2 2h7a2 2 0 0 1 2 2H4v10l2.14-8h17.07l-2.28 8.5c-.23.87-1.01 1.5-1.93 1.5z" fill="currentColor"/></svg>&nbsp; Choose the Reference<strong style="color:crimson;"> [ Pathogen ]</strong> </h3>
     """, unsafe_allow_html=True)
    st.text("")
    # liste de programe réquis
    filevcf = ''
    merge = ''
    program = "picard"
    program2 = "samtools"
    program3 = "bcftools"
    program4 = "varscan"
    program5 = "gatk"
    program6 = "freebayes"
    program7 = "vcffilter"

    process = subprocess.run(
        ['which', program], capture_output=True, text=True)
    process2 = subprocess.run(
        ['which', program2], capture_output=True, text=True)
    process3 = subprocess.run(
        ['which', program3], capture_output=True, text=True)
    process4 = subprocess.run(
        ['which', program4], capture_output=True, text=True)

    process5 = subprocess.run(
        ['which', program5], capture_output=True, text=True)
    process6 = subprocess.run(
        ['which', program6], capture_output=True, text=True)
    process7 = subprocess.run(
        ['which', program7], capture_output=True, text=True)

    file = user+"/APP/data/Bam/Mapped"
    if os.path.exists(r'{}'.format(file)) == True:
        bashCmd = ["ls APP/data/Bam/Mapped/*_Patho_mapped.bam | wc -l"]
        process = subprocess.Popen(
            bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = process.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp; Number Of Files Mapped :<strong>{}</strong></p>""".format(str(int(int(out)))), unsafe_allow_html=True)
        if err == None:
            if process.returncode == 0 and process2.returncode == 0 and process3.returncode == 0 and process4.returncode == 0 and process5.returncode == 0 and process6.returncode == 0 and process7.returncode == 0:
                file = user+"/APP/data/Reference"
                if os.path.exists(r'{}'.format(file)) == True:
                    bashCmd1 = ["ls APP/data/Reference/*.pac | wc -l"]
                    process1 = subprocess.Popen(
                        bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
                    out, err = process1.communicate()
                    if err == None:
                        if int(out) != 0:
                            filenames = os.listdir(file)
                            Refereces = []
                            for element in filenames:
                                if ".bwt" not in str(element) and ".pac" not in str(element) and ".ann" not in str(element) and ".sa" not in str(element) and ".amb" not in str(element):
                                    Refereces.append(element)
                                index = []
                                for name in Refereces:
                                    if str(name)+".bwt" in str(filenames) and str(name)+".pac" in str(filenames) and str(name)+".ann" in str(filenames) and str(name)+".sa" in str(filenames) and str(name)+".amb" in str(filenames):
                                        index.append(name)

                        with st.container():
                            st.write(
                                'choose the technology for variant calling :')
                            # last with varscan
                            # tech = st.radio(
                            #     "technology", ('bcftools+samtools', 'varscan+samtools','gatk'))
                            tech = st.radio(
                                "technology", ('bcftools+samtools', 'gatk', 'freebayes'))
                            optionstype = ["snps", "indels", "all"]
                            type = st.radio(
                                "choose alternatif types", options=optionstype)
                            st.text("")

                            merge = st.checkbox("merge all vcf", value=True)
                            with st.container():
                                    colq, colp, colploidy = st.columns(3)
                                    with colq:
                                        qualite = st.number_input(
                                            "Enter the Quality", step=1)
                                    with colp:
                                        profondeur = st.number_input(
                                            "Enter the Depth", step=1)
                                    with colploidy:
                                        ploidy = st.number_input(
                                            "Enter the ploidy", step=1)

                            # zonechoix = st.checkbox(
                            #     "Voulez vous effectué un filtre dans une zone particulière")
                            # zone="abscence"
                            # zonech=1
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                optionref = st.selectbox(
                                    'List of Reference', list(set(index)))
                            with col2:
                                Activer = st.button("Start")
                        st.write("")
                        filebam = user+"/APP/data/Bam/Mapped"
                        bashCmd = [
                            "ls APP/data/Bam/Mapped/*_Patho_mapped.bam | wc -l"]
                        process = subprocess.Popen(
                            bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
                        out, err = process.communicate()
                        if os.path.exists(r'{}'.format(filebam)) == True and str(out) != "0":
# ---------------------------------------| BCFTOOLS SECTION ------------------------------------------------------------------
                            if Activer and tech == 'bcftools+samtools':
                                filevcf = user+"/APP/data/variants.bcftools"
                                if merge == False:
                                    if os.path.exists(r'{}'.format(filevcf)) == True and qualite != "" and profondeur != "":
                                        optionref = "APP/data/Reference/" + \
                                            str(optionref)
                                        bashCmd1 = ["bash  APP/bashScripts/varcalling.sh {}  {}  {}".format(
                                            "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref), str(ploidy))]
                                        process3 = subprocess.Popen(
                                            bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
                                        out, err = process3.communicate()

                                        file = user+"/APP/data/variants.bcftools/Filterring"
                                        bashCmdex = ["bash  APP/bashScripts/filterring.sh {} {} {} {}".format(str(
                                            "APP/data/variants.bcftools/*_normalized.vcf"), str(type), str(qualite), str(profondeur))]
                                        processex = subprocess.Popen(
                                            bashCmdex, stdout=subprocess.PIPE, text=True, shell=True)
                                        outex, errex = processex.communicate()
                                else:
                                    if os.path.exists(r'{}'.format(filevcf)) == True and qualite != "" and profondeur != "":
                                        optionref = "APP/data/Reference/" + \
                                            str(optionref)
                                        bashCmd1 = ["bash  APP/bashScripts/varcallingmerge.sh {}  {}  {}".format(
                                            "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref), str(ploidy))]
                                        process3 = subprocess.Popen(
                                            bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
                                        out, err = process3.communicate()

                                        file = user+"/APP/data/variants.bcftools/Filterring"
                                        bashCmdex = ["bash  APP/bashScripts/filterringmerge.sh {} {} {} {}".format(str(
                                            "APP/data/variants.bcftools/mergevcffile/merge.vcf"), str(type), str(qualite), str(profondeur))]
                                        processex = subprocess.Popen(
                                            bashCmdex, stdout=subprocess.PIPE, text=True, shell=True)
                                        outex, errex = processex.communicate()

# --------------------------| VARSCAN SECTION --------------------------------------------------------------------------------
                            # if Activer and tech == 'varscan+samtools':
                            #     filevcf = user+"/APP/data/variants.varscan"
                            #     if os.path.exists(r'{}'.format(filevcf)) == True and type=="all":
                            #         optionref = "APP/data/Reference/" + \
                            #             str(optionref)
                            #         bashCmdall = ["bash  APP/bashScripts/varcallingvarscan.sh {}  {} {} {}".format(
                            #             "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref),str(qualite),str(profondeur))]
                            #         processall = subprocess.Popen(
                            #             bashCmdall, stdout=subprocess.PIPE, text=True, shell=True)
                            #         out3, err3 = processall.communicate()

                            # if Activer and tech == 'varscan+samtools':
                            #     filevcf = user+"/APP/data/variants.varscan"
                            #     if os.path.exists(r'{}'.format(filevcf)) == True and type=="snps":
                            #         optionref = "APP/data/Reference/" + \
                            #             str(optionref)
                            #         bashCmdsnps = ["bash  APP/bashScripts/varcallingvarscansnps.sh {}  {} {} {}".format(
                            #             "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref),str(qualite),str(profondeur))]
                            #         processSnps = subprocess.Popen(
                            #             bashCmdsnps, stdout=subprocess.PIPE, text=True, shell=True)
                            #         out3, err3 = processSnps.communicate()

                            # if Activer and tech == 'varscan+samtools':
                            #     filevcf = user+"/APP/data/variants.varscan"
                            #     if os.path.exists(r'{}'.format(filevcf)) == True and type=="indels":
                            #         optionref = "APP/data/Reference/" + \
                            #             str(optionref)
                            #         bashCmdsnps = ["bash  APP/bashScripts/varcallingvarscanindels.sh {}  {} {} {}".format(
                            #             "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref),str(qualite),str(profondeur))]
                            #         processSnps = subprocess.Popen(
                            #             bashCmdsnps, stdout=subprocess.PIPE, text=True, shell=True)
                            #         out3, err3 = processSnps.communicate()
# ---------------------------------------------------| SECTION GATK ----------------------------------------------------------------------
                            if Activer and tech == 'gatk':
                                filevcf = user+"/APP/data/gatkfile"
                                if merge == False:
                                    if os.path.exists(r'{}'.format(filevcf)) == True and qualite != "" and profondeur != "":
                                        optionref = "APP/data/Reference/" + \
                                            str(optionref)
                                        bashCmd1 = ["bash  APP/bashScripts/varcallingGatk.sh {}  {} {}".format(
                                            "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref), str(ploidy))]
                                        process3 = subprocess.Popen(
                                            bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
                                        out, err = process3.communicate()

                                        file = user+"/APP/data/gatkfile/Filterring"
                                        bashCmdex = ["bash  APP/bashScripts/filterringGatk.sh {} {} {} {} {}".format(str(
                                            "APP/data/gatkfile/vcffile/*.vcf"), str(type), str(float(qualite)), str(float(profondeur)), str(optionref))]
                                        processex = subprocess.Popen(
                                            bashCmdex, stdout=subprocess.PIPE, text=True, shell=True)
                                        outgex, errgex = processex.communicate()
                                else:
                                    if os.path.exists(r'{}'.format(filevcf)) == True and qualite != "" and profondeur != "":
                                        optionref = "APP/data/Reference/" + \
                                            str(optionref)
                                        # bashCmd1 = ["bash  APP/bashScripts/varcallingGatkmerge.sh {}  {} {}".format(
                                        #     "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref), str(ploidy))]
                                        # process3 = subprocess.Popen(
                                        #     bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
                                        # out, err = process3.communicate()
                                        
                                        file = user+"/APP/data/gatkfile/Filterring"
                                        bashCmdexmerge = ["bash  APP/bashScripts/filterringGatkmerge.sh {} {} {} {} {}".format(str(
                                            "APP/data/gatkfile/mergevcfile/merge.vcf"), str(type), str(float(qualite)), str(float(profondeur)), str(optionref))]
                                        processexmerge = subprocess.Popen(
                                            bashCmdexmerge, stdout=subprocess.PIPE, text=True, shell=True)
                                        outgexmerge, errgexmerge = processexmerge.communicate()

# ---------------------------------------------------| SECTION FREEBAYES ----------------------------------------------------------------------
                            if Activer and tech == 'freebayes':
                                filevcf = user+"/APP/data/freebayesfile"
                                if merge == True:
                                    if os.path.exists(r'{}'.format(filevcf)) == True and qualite != "" and profondeur != "" and ploidy != "":
                                        optionref = "APP/data/Reference/" + \
                                            str(optionref)
                                        bashCmd1freebayes = ["bash  APP/bashScripts/varcallingFreebayesmerge.sh {}  {}  {}".format(
                                            "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref), str(ploidy))]
                                        process3 = subprocess.Popen(
                                            bashCmd1freebayes, stdout=subprocess.PIPE, text=True, shell=True)
                                        out, err = process3.communicate()
                                        file = user+"APP/data/freebayesfile/Filterring/mergefile"
                                        bashCmdexfreebayes = ["bash  APP/bashScripts/filterringFreebayesmerge.sh {} {} {} {}".format(str(
                                            "APP/data/freebayesfile/mergevcffile/*.vcf"), str(type), str(float(qualite)), str(float(profondeur)))]
                                        processex = subprocess.Popen(
                                            bashCmdexfreebayes, stdout=subprocess.PIPE, text=True, shell=True)
                                        outgex, errgex = processex.communicate()
                                else:
                                    if os.path.exists(r'{}'.format(filevcf)) == True and qualite != "" and profondeur != "" and ploidy != "":
                                        optionref = "APP/data/Reference/" + \
                                            str(optionref)
                                        bashCmd1fbmerge = ["bash  APP/bashScripts/varcallingFreebayes.sh {}  {}  {}".format(
                                            "APP/data/Bam/Mapped/*_Patho_mapped.bam", str(optionref), str(ploidy))]
                                        process3 = subprocess.Popen(
                                            bashCmd1fbmerge, stdout=subprocess.PIPE, text=True, shell=True)
                                        out, err = process3.communicate()
                                        file = user+"/APP/data/freebayesfile/Filterring/singlefile"
                                        bashCmdexfbfil = ["bash  APP/bashScripts/filterringFreebayes.sh {} {} {} {}".format(str(
                                            "APP/data/freebayesfile/vcffile/*.vcf"), str(type), str(float(qualite)), str(float(profondeur)))]
                                        processex = subprocess.Popen(
                                            bashCmdexfbfil, stdout=subprocess.PIPE, text=True, shell=True)
                                        outgex, errgex = processex.communicate()

# ------------------------------------------------------------------------------| DOWNLOAD FILE -------------------------------------

    # if tech == 'varscan+samtools':
    #     filevcf = user+"/APP/data/variants.varscan/Filterring"
    if tech == 'bcftools+samtools' and merge==False:
        filevcf = user+"/APP/data/variants.bcftools/Filterring/filteredType"
    elif tech == 'bcftools+samtools' and merge==True:
        filevcf = user+"/APP/data/variants.bcftools/Filterring/mergefile"
    elif tech == 'gatk' and merge==False:
        filevcf = user+"/APP/data/gatkfile/Filterring"
    elif tech == 'gatk' and merge==True:
        filevcf = user+"/APP/data/gatkfile/Filterring/mergefile"
    elif tech=='freebayes' and merge==True:
        filevcf = 'APP/data/freebayesfile/Filterring/mergefile'
    elif tech=='freebayes' and merge==False:
        filevcf = 'APP/data/freebayesfile/Filterring'
    else:
        filevcf = ""

    if os.path.exists(r'{}'.format(filevcf)) == True:
        st.info("Download VCF file")
        bashCmdcheck = ["ls "+str(filevcf)+"/*vcf | wc -l"]
        processcheck = process = subprocess.Popen(
            bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = processcheck.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Numbers of files :&nbsp; <i style="color:rgb(244 40 38);font-weight:900">vcf*  </i> : <strong>{}</strong></p>""".format(str(int(out))), unsafe_allow_html=True)
        filegetvcf = os.listdir(filevcf)
        vcf = ["---Fichier vcf"]
        for element in filegetvcf:
            if element != "Filterring" and ".idx" not in element and ".vcf" in element:
                vcf.append(element)
        with st.container():
            colselect, colbtn = st.columns([2, 1])
            with colselect:
                optionselect = st.selectbox(
                    'Download', sorted(list(set(vcf))))
            with colbtn:
                if optionselect != "---Fichier vcf":
                    with open(os.path.join(filevcf, optionselect), "rb") as file:
                        st.download_button(
                            label="Download File",
                            data=file,
                            file_name="{}".format(optionselect),
                            mime="file/vcf")
                    
    colchromosome,colposition,colapplyfilter = st.columns(3)
    allchromosomeAivaible = ["---Chromosome"]
    chromosomefile = user+"/APP/data/chromosome"
    with colchromosome:
        if os.path.isfile(f"./APP/data/Reference/{str(optionref)}.fai"):
            path= f"APP/data/Reference/{str(optionref)}.fai"
            bashcommandgetchrom = ["""awk '{print $1}' """+path]
            processbashcommandgetchrom = subprocess.Popen(
                bashcommandgetchrom, stdout=subprocess.PIPE, text=True, shell=True)
            outprocessbashcommandgetchrom, errprocessbashcommandgetchrom = processbashcommandgetchrom.communicate()
            for el in outprocessbashcommandgetchrom.rsplit("\n"):
                if el !="":
                    allchromosomeAivaible.append(el)
        chromosome=st.selectbox("Select chromosome",allchromosomeAivaible)

    with colposition:
        position=st.text_input('position interval',help="i.e 172000-2000000")

    with colapplyfilter:
        if chromosome != "---Chromosome" and position !="" and "-" in position:
            location=chromosome+":"+position
            btn=st.button("apply filter")
            if btn == True:
                bashCmdchromosome = ["bash  APP/bashScripts/chromosome.sh {} {}".format(str(filevcf)+"/*.vcf",str(location))]
                processexbashCmdchromosome = subprocess.Popen(
                    bashCmdchromosome, stdout=subprocess.PIPE, text=True, shell=True)
                outex, errex = processexbashCmdchromosome.communicate()
                st.write(outex)
    if os.path.exists(r'{}'.format(chromosomefile)) == True:
        st.info("Download VCF file")
        bashCmdcheck = ["ls "+str(chromosomefile)+"/*vcf | wc -l"]
        processcheck = process = subprocess.Popen(
            bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = processcheck.communicate()
        filegetvcf = os.listdir(chromosomefile)
        st.write()
        if len(filegetvcf)>1:
            st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Numbers of files :&nbsp; <i style="color:rgb(244 40 38);font-weight:900">vcf* some chromosome {}  </i> : <strong>{}</strong></p>""".format(str(str(filegetvcf[0]).split("_",1)[1].split(".")[0]),str(int(out))), unsafe_allow_html=True)
        vcf = ["---Fichier vcf"]
        for element in filegetvcf:
            if element != "Filterring" and ".tbi" not in element and ".gz" not in element and ".vcf" in element:
                vcf.append(element)
        with st.container():
            colselect, colbtn = st.columns([2, 1])
            with colselect:
                optionselect = st.selectbox(
                    'Download File', sorted(list(set(vcf))))
            with colbtn:
                if optionselect != "---Fichier vcf":
                    with open(os.path.join(chromosomefile, optionselect), "rb") as file:
                        st.download_button(
                            label="Download File",
                            data=file,
                            file_name="{}".format(optionselect),
                            mime="file/vcf")
