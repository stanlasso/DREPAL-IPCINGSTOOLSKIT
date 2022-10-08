#!/bin/sh
##########################################################
# By SRC
#Ce script permet de Visualiser les données  via Fastqc
#
##########################################################

for read in "$@"
do

echo indexation de $read veuillez patienter ....
# indexation de la reference avec bwa
bwa index $read  &> /dev/null


done