#!/bin/sh
# Ce script permet de faire du Variants Calling
rm -rf APP/data/Annoted/AnnotatedFILEbyFILE/singlefilerepport/* && rm -rf APP/data/Annoted/AnnotatedFILEbyFILE/*.vcf  

Nbargument=$#
i=0
Genome=${@: -1}

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


# initialisation


j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt "${#tab[@]}" ]
do
    let j=j+1
    
    Input=${tab[$j]}
    
    chemin=${Input:29}
    
    prefix=$(echo $chemin | cut -d'.' -f 1)
    id=$(echo $chemin | cut -d'_' -f 1)
    idfinal=$(echo $id | cut -d'/' -f 4)    
    echo $Input
    echo $idfinal

    java -Xmx4g -jar APP/snpEff/snpEff.jar $Genome $Input > APP/data/Annoted/AnnotatedFILEbyFILE/"$idfinal"_Annotated.vcf

    mv snpEff_genes.txt "$idfinal"_genes.txt && mv "$idfinal"_genes.txt APP/data/Annoted/AnnotatedFILEbyFILE/singlefilerepport/
    mv snpEff_summary.html "$idfinal"_summary.html && mv "$idfinal"_summary.html APP/data/Annoted/AnnotatedFILEbyFILE/singlefilerepport/  
done