#!/bin/sh
# Ce script permet de faire du Variants Calling bcftools gatk

rm -rf APP/data/freebayesfile/mergevcffile/merge.vcf && rm -rf APP/data/freebayesfile/metrics/*.txt

Nbargument=$#
bamfileoccurence=`expr $Nbargument - 2`
# remove precedent files
delete_other=$(find ./APP/data/Bam/Mapped/BamFreebayes/ -maxdepth 1 ! -name "*.bam" -type f)

for file in $delete_other
do
    rm "$file"
done

# Traitement
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -le $# ];
    then
        tab[$i]="$read"
    fi
done

#echo "${tab[@]:0:$bamfileoccurence}"
Ploidy="${tab[-1]}"
Pathogene="${tab[-2]}"

# initialisation


j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt $bamfileoccurence ]
do
    let j=j+1
    
    Input=${tab[$j]}
    
    chemin=${Input:20}
    
    prefix=$(echo $chemin | cut -d'.' -f 1)
    id=$(echo $chemin | cut -d'_' -f 1)

    picard SortSam I=APP/data/Sam/"${id}"_Patho_align.sam O=APP/data/Bam/Mapped/BamFreebayes/"${id}".bam VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate CREATE_INDEX=true TMP_DIR=100
    
    picard MarkDuplicates I=APP/data/Bam/Mapped/BamFreebayes/"${id}".bam O=APP/data/Bam/Mapped/BamFreebayes/"${id}".dup.bam M=metrics."$id".txt  CREATE_INDEX=true MAX_RECORDS_IN_RAM=30000
    
    samtools index  APP/data/Bam/Mapped/BamFreebayes/"${id}".dup.bam
    
    echo APP/data/Bam/Mapped/BamFreebayes/"${id}".dup.bam >> APP/data/freebayesfile/txtfile/allBamfile.txt

done

freebayes --ploidy $Ploidy -f $Pathogene --bam-list APP/data/freebayesfile/txtfile/allBamfile.txt > APP/data/freebayesfile/mergevcffile/merge.vcf 

mv *metrics.* APP/data/freebayesfile/metrics/

rm -f APP/data/freebayesfile/txtfile/allBamfile.txt
rm -rf 100