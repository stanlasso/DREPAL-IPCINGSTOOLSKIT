#!/bin/sh
##########################################################
# By SRC
#Ce script permet de Visualiser les données  via Fastqc
#
##########################################################
# recuperation des variables

# initialisation

Nbargument=$#
#parametre a recuperé avant la fin
count=$(expr $Nbargument - 8)
i=0
## Traitement
declare -a var
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -lt $count ];
    then
        tab[$i]="$read"
    else
        var[$i]="$read"
    fi
done

#recuperation des variables:
valtf1=${var[$(expr $Nbargument - 8)]}
valtf2=${var[$(expr $count + 1)]}
valtt1=${var[$(expr $count + 2)]}
valtt2=${var[$(expr $count + 3)]}
valbl=${var[$(expr $count + 4)]}
vall=${var[$(expr $count + 5)]}
valq=${var[$(expr $count + 6)]}
valforadapt=${var[$(expr $count + 7)]}
valrevadapt=${var[$(expr $count + 8)]}



j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt "${#tab[@]}" ]
do
    # Incrémente j de deux pas
    let j=j+2
    #if [ $j -le "$#" ]
    #then
    #Extraire le préfixe du gène
    Input=${tab[$j-1]}
    
    chemin=${Input:19}
    
    prefix=$(echo $chemin | cut -d'_' -f 1)
    
    
    # fastp -------------------------traitement
    fastp -i ${tab[j-1]} -o APP/data/Datafastq/ResQC/"${prefix}"_trimmed_R1.fastq   -I ${tab[j]} -O  APP/data/Datafastq/ResQC/"${prefix}"_trimmed_R2.fastq  --trim_front1 $valtf1 --trim_front2 $valtf2 --trim_tail1 $valtt1 --trim_tail2 $valtt2 --n_base_limit $valbl
    SeqPrep -A $valforadapt -B $valrevadapt -f APP/data/Datafastq/ResQC/"${prefix}"_trimmed_R1.fastq -r APP/data/Datafastq/ResQC/"${prefix}"_trimmed_R2.fastq  -q $valq -L $vall  -1 APP/data/Datafastq/ResQC/"${prefix}_1".fastq.gz  -2 APP/data/Datafastq/ResQC/"${prefix}_2".fastq.gz 
    
    # remove sickle in version 
    #sickle pe -t sanger -f APP/data/Datafastq/ResQC/"${prefix}"_trimmed_R1.fastq -r APP/data/Datafastq/ResQC/"${prefix}"_trimmed_R2.fastq -o APP/data/Datafastq/ResQC/"${prefix}_1".fastq -p APP/data/Datafastq/ResQC/"${prefix}_2".fastq -s APP/data/Datafastq/ResQC/output_reads_trimmed_single.fastq -l $vall -q $valq
    #SeqPrep -A GTGTATAAGAGACAG -B CTGTCTCTTATACAC -f APP/data/Datafastq/ResQC/"${prefix}_1ad".fastq -r APP/data/Datafastq/ResQC/"${prefix}_2ad".fastq  -1 APP/data/Datafastq/ResQC/"${prefix}_1".fastq.gz  -2 APP/data/Datafastq/ResQC/"${prefix}_2".fastq.gz 
done

# suppresion des anciens fichiers fastq
rm -rf APP/data/Datafastq/*.fastq
rm -rf APP/data/Datafastq/ResQC/*_trimmed_R1.fastq | rm -rf APP/data/Datafastq/ResQC/*_trimmed_R2.fastq
gunzip  APP/data/Datafastq/ResQC/*.gz
mv APP/data/Datafastq/ResQC/*.fastq APP/data/Datafastq/
rm fastp.html
rm fastp.json