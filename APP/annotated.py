import streamlit as st
import subprocess
import os
import pandas as pd
import plotly.graph_objects as go


def annotated():
    filedata = ''
    user = str(os.getcwd())
    st.write("")
    st.markdown(""" 
            <h5><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="26" height="26" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M3 17v2h6v-2H3M3 5v2h10V5H3m10 16v-2h8v-2h-8v-2h-2v6h2M7 9v2H3v2h4v2h2V9H7m14 4v-2H11v2h10m-6-4h2V7h4V5h-4V3h-2v6z" fill="currentColor"/></svg>&nbsp;Paramètre Du Filtrage</h4>
            """, unsafe_allow_html=True)
    st.write()
    program1 = "jannovar "
    process1 = subprocess.run(
        ['which', program1], capture_output=True, text=True, shell=True)
    st.info("Please !! will be added to the new version")
    # if process1.returncode == 1:
    #     st.write(
    #         'choisir la technologie pour le variant calling :')
    #     tech = st.radio(
    #         "technologie", ('bcftools+samtools', 'varscan+samtools', 'Intercept variants'))
    #     optionstype = ["snps", "indels", "all"]
    #     type = st.radio("Coché le types d'alternatif", options=optionstype)
    #     st.text("")
    #     if tech=='bcftools+samtools':
    #         filedata = user+"/APP/data/variants.bcftools"
    #         bashCmdcheck = ["ls "+user +
    #                     "/APP/data/variants.bcftools/Filterring/*_filtered.vcf | wc -l"]
    #         processcheck = subprocess.Popen(
    #         bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
    #     elif tech=='varscan+samtools':
    #         filedata = user+"/APP/data/variants.varscan"
    #         bashCmdcheck = ["ls "+user +
    #                     "/APP/data/variants.varscan/*.vcf | wc -l"]
    #         processcheck = subprocess.Popen(
    #         bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
    #     elif tech=='Intercept variants':
    #         pass
    #     out, err = processcheck.communicate()
    #     st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Nombre De Fichiers&nbsp; <i style="color:rgb(244 40 38);font-weight:900">vcf* fitrés </i> : <strong>{}</strong></p>""".format(str(int(out))), unsafe_allow_html=True)
