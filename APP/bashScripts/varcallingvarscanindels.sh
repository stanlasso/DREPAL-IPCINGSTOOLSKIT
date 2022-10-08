#!/bin/sh
# Ce script permet de faire du Variants Calling
rm -rf APP/data/Bam/Mapped/*.bai && rm -rf APP/data/Bam/Mapped/*.sorted.bam && rm -rf APP/data/Bam/Mapped/*.sorted.dedup.bam
rm -rf APP/data/variants.varscan/*_indels_variants.vcf && rm -rf APP/data/variants.varscan/*_file.mpileup

Nbargument=$#
count=$(expr $Nbargument - 2)
i=0


## Traitement
declare -a var
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -lt  $count ];
    then
        tab[$i]="$read"
    else
        var[$i]="$read"
    fi
done

Pathogene=${var[-3]}
Qual=${var[-2]}
Dp=${var[-1]}

# initialisation


j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt "${#tab[@]}" ]
do
    let j=j+1
    
    Input=${tab[$j]}
    
    chemin=${Input:20}
    
    prefix=$(echo $chemin | cut -d'.' -f 1)
    id=$(echo $chemin | cut -d'_' -f 1)
    
    
    picard AddOrReplaceReadGroups I=$Input O=APP/data/Bam/Mapped/"$prefix"_AORRG.bam RGLB=ipci RGPL=ILLUMINA RGPU=bioinfo RGSM=20 RGID="$id"
    
    picard SortSam I=APP/data/Bam/Mapped/"$prefix"_AORRG.bam O=APP/data/Bam/Mapped/"$prefix".sorted.bam VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate CREATE_INDEX=true TMP_DIR=100
    
    picard MarkDuplicates I=APP/data/Bam/Mapped/"$prefix".sorted.bam O=APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam M=marked_dup_metrics.txt CREATE_INDEX=true MAX_RECORDS_IN_RAM=30000
    
    
    samtools index  APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam

    
    samtools mpileup -B -q 1 -f $Pathogene APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam > APP/data/variants.varscan/"$id"_file.mpileup

    varscan pileup2indel APP/data/variants.varscan/"$id"_file.mpileup --min-coverage $Dp --min-avg-qual $Qual > APP/data/variants.varscan/"$id"_indels_variants.vcf

done