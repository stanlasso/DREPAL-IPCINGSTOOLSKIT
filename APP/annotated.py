import streamlit as st
import subprocess
import os

def annotated():
    filedata = ''
    opt = ''
    merge = ''
    user = str(os.getcwd())
    filevcf = ""
    filevcfdownload = ""
    st.write("")
    if os.path.exists("APP/snpEff/SnpSift.jar") == True:
        st.info("Exclusive SNPEFF Plasmodium Falcipharum annoted")
        Genome = "Pf3D7"
        opt = st.radio("choose the option  used for vcf generation", [
                       'gatk', "bcftools"])
        if opt == "gatk":
            filevcf = user+"/APP/data/gatkfile/Filterring"
            filegetvcf = os.listdir(filevcf)
            vcf = []
            for element in filegetvcf:
                if ".idx" not in element and ".vcf" in element:
                    vcf.append(element)

        elif opt == "bcftools":
            filevcf = user+"/APP/data/variants.bcftools/Filterring"
            filegetvcf = os.listdir(filevcf)
            vcf = []
            for element in filegetvcf:
                if ".vcf" in element:
                    vcf.append(element)
        else:
            filevcf = "none"

        merge = st.checkbox('merge vcf file')
        run = st.button('Run')
        if merge == True and run == True:
            bashCmd = [
                "bash APP/bashScripts/merge.sh {} {}".format(str(opt),filevcf+"/_filtered_snps.vcf")]
            process = subprocess.Popen(
                bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()
            st.write(err)
            if err == None:
                bashcommandannoted = [
                    'bash APP/bashScripts/snpeff.sh {} {}'.format(Genome, "APP/data/Annoted/merge.vcf")]
                process = subprocess.Popen(
                    bashcommandannoted, stdout=subprocess.PIPE, text=True, shell=True)
                outannotated, erranotated = process.communicate()
        if merge == False and run == True:
            bashcommandannoted = ['bash APP/bashScripts/snpeffsingle.sh {} {}'.format(filevcf+"/*_filtered_snps.vcf", Genome)]
            process = subprocess.Popen(
                bashcommandannoted, stdout=subprocess.PIPE, text=True, shell=True)
            outannotated, erranotated = process.communicate()

    list1 = os.listdir("APP/data/Annoted/AnnotatedFILEbyFILE/")
    list1.pop(list1.index("singlefilerepport"))
    if os.path.isfile("APP/data/Annoted/annotated.vcf") == True or len(list1) != 0:
        st.info("Generate missence variant for anotated file")
        st.write("")
        if merge == True:
            if st.button("Generate", help="Apply Snpsift filter for Generate missence variant"):
                bashsnpsift = [
                    'bash APP/bashScripts/snpSiftmerge.sh']
                process = subprocess.Popen(
                    bashsnpsift, stdout=subprocess.PIPE, text=True, shell=True)
                outsnpsift, errsnpsift = process.communicate()
        else:
            if st.button("Generate", help="Apply Snpsift filter for Generate missence variant"):
                bashsnpsift = [
                    'bash APP/bashScripts/snpSiftsingle.sh APP/data/Annoted/AnnotatedFILEbyFILE/*.vcf']
                process = subprocess.Popen(
                    bashsnpsift, stdout=subprocess.PIPE, text=True, shell=True)
                outsnpsift, errsnpsift = process.communicate()

    if opt == 'gatk' and merge == False:
        filevcfdownload = user+"/APP/data/Annoted/AnnotatedFILEbyFILE"
        filereport = user+"/APP/data/Annoted/AnnotatedFILEbyFILE/singlefilerepport"
    elif opt == 'gatk' and merge == True:
        filevcfdownload = user+"/APP/data/Annoted"
        filereport = user+"/APP/data/Annoted/report"
    elif opt == 'bcftools' and merge == False:
        filevcfdownload = user+"/APP/data/Annoted/AnnotatedFILEbyFILE"
        filereport = user+"/APP/data/Annoted/AnnotatedFILEbyFILE/singlefilerepport"
    elif opt == 'bcftools' and merge == True:
        filevcfdownload = user+"/APP/data/Annoted"
        filereport = user+"/APP/data/Annoted/report"
    else:
        filevcfdownload = 'none'

    if os.path.exists(r'{}'.format(filevcfdownload)) == True:
        st.info("Download VCF file")
        st.write()
        bashCmdcheck = ["ls "+str(filevcfdownload)+"/*vcf | wc -l"]
        processcheck = process = subprocess.Popen(
            bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = processcheck.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;file count&nbsp; <i style="color:rgb(244 40 38);font-weight:900">vcf*  </i> : <strong>{}</strong></p>""".format(str(int(out))), unsafe_allow_html=True)
        filegetvcf = os.listdir(filevcfdownload)
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
                    with open(os.path.join(filevcfdownload, optionselect), "rb") as file:
                        st.download_button(
                            label="Download File",
                            data=file,
                            file_name="{}".format(optionselect),
                            mime="file/vcf")

    if os.path.exists(r'{}'.format(filereport)) == True:
        st.info("Download report file")
        st.write()
        bashCmdcheck = ["ls "+str(filereport)+"/* | wc -l"]
        processcheck = process = subprocess.Popen(
            bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = processcheck.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;file count&nbsp; <i style="color:rgb(244 40 38);font-weight:900">report file  </i> : <strong>{}</strong></p>""".format(str(int(out))), unsafe_allow_html=True)
        filegetreport = os.listdir(filereport)
        report = ["---Fichier report"]
        for element in filegetreport:
            report.append(element)
        with st.container():
            reportcolselect, reportcolbtn = st.columns([2, 1])
            with reportcolselect:
                optionselectreport = st.selectbox(
                    'Download', sorted(list(set(report))))
            with reportcolbtn:
                if optionselectreport != "---Fichier report":
                    with open(os.path.join(filereport, optionselectreport), "rb") as file:
                        st.download_button(
                            label="Download File",
                            data=file,
                            file_name="{}".format(optionselectreport),
                            mime="file/txt")
