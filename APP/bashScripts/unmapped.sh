#!/bin/sh
##########################################################
# By SRC
# Ce script permet  la soustraction  du gène de l’humain (Unmap)
# du gène d'une personne atteinte
# de Covid-19
#
##########################################################

rm -f APP/data/Bam/*
rm -f APP/data/Sam/*
rm -f APP/data/Datafastq/unmapped/*



Nbargument=$#
i=0
Human_genome=${@: -1}

## Traitement
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -lt $# ];
    then
        tab[$i]="$read"
    fi
done

j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau ${#tab[@]}
while [ "$j" -lt "${#tab[@]}"  ]
do
    # Incrémente j de deux pas
    let j=j+2
    #if [ $j -le "$#" ]
    #then
    #Extraire le préfixe du gène
    Input=${tab[$j]}
    
    chemin=${Input:19}
    
    prefix=$(echo $chemin | cut -d'_' -f 1)
    
    bwa mem APP/data/Reference/"${Human_genome}" ${tab[$j-1]} ${tab[$j]} -o APP/data/Sam/"${prefix}".sam 
    
    samtools view -Sb -f0x4 APP/data/Sam/"${prefix}".sam  > APP/data/Bam/"${prefix}"_Human_unmapped.bam 

    samtools bam2fq -1 APP/data/Datafastq/"${prefix}"_Human_unmapped_R1.fastq -2 APP/data/Datafastq/"${prefix}"_Human_unmapped_R2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Bam/"${prefix}"_Human_unmapped.bam
done

mv APP/data/Datafastq/*Human_unmapped_R1.fastq APP/data/Datafastq/unmapped
mv APP/data/Datafastq/*Human_unmapped_R2.fastq APP/data/Datafastq/unmapped




