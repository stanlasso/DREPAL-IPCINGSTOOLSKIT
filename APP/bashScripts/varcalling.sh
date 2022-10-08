#!/bin/sh
# Ce script permet de faire du Variants Calling
rm -rf APP/data/Bam/Mapped/*AORRG.bam && rm -rf APP/data/Bam/Mapped/*.sorted.bam && rm -rf APP/data/Bam/Mapped/*.sorted.dedup.bam

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

    
    
    bcftools mpileup -Ovu -f $Pathogene APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam > APP/data/variants.bcftools/"$id"_genotypes.vcf
    # appel des variants
    
    bcftools call --ploidy 1 -vm -Ov APP/data/variants.bcftools/"$id"_genotypes.vcf > APP/data/variants.bcftools/"$id"_variants.vcf
    
    # gestion de la ploidy
    
    
    bcftools norm -m+ -c ws -f $Pathogene APP/data/variants.bcftools/"$id"_variants.vcf > APP/data/variants.bcftools/"$id"_normalized.vcf
    
    # NORMALISATION DE FICHIERS
    
done
