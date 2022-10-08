#!/bin/sh
#######################################################
#By SRC
# Ce script permet  l'extraction  du gène du virus(map) du gène d'une personne atteinte
# de Covid-19
#
#######################################################

Nbargument=$#
i=0
Pathogene=${@: -1}

## Traitement
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -lt $#  ];
    then
        tab[$i]="$read"
    fi
done

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
    
    chemin=${Input:28}
    
    prefix=$(echo $chemin | cut -d'_' -f 1)
    
    bwa mem $Pathogene ${tab[$j-1]} ${tab[$j]} -o APP/data/Sam/"${prefix}"_Patho_align.sam
    
    samtools view -Sb -F0x4 APP/data/Sam/"${prefix}"_Patho_align.sam > APP/data/Bam/Mapped/"${prefix}"_Patho_mapped.bam 
     
    
done

# suppression
#rm APP/data/Datafastq/unmapped/*.fastq
#mv APP/data/Sam/*.sam APP/data/Sam/Null/
#rm  APP/data/Sam/Null/*.sam