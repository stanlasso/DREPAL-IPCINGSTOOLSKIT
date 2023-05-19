#!/bin/sh
# Ce script permet de faire du Variants Calling bcftools samtools

rm -f APP/data/variants.bcftools/*.vcf*
rm -f APP/data/freebayesfile/mergevcffile/*
Nbargument=$#
bamfileoccurence=`expr $Nbargument - 2`
# remove precedent files
delete_other=$(find ./APP/data/Bam/Mapped/ -maxdepth 1 ! -name "*.bam" -type f)

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

echo $Ploidy
echo $Pathogene

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
    
    picard AddOrReplaceReadGroups I=$Input O=APP/data/Bam/Mapped/"$prefix"_AORRG.bam RGLB=ipci RGPL=ILLUMINA RGPU=bioinfo RGSM=20 RGID="$id"
    
    picard SortSam I=APP/data/Bam/Mapped/"$prefix"_AORRG.bam O=APP/data/Bam/Mapped/"$prefix".sorted.bam VALIDATION_STRINGENCY=SILENT SORT_ORDER=coordinate CREATE_INDEX=true TMP_DIR=100
    
    picard MarkDuplicates I=APP/data/Bam/Mapped/"$prefix".sorted.bam O=APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam M=marked_dup_metrics.txt CREATE_INDEX=true MAX_RECORDS_IN_RAM=30000
    
    samtools index  APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam

    
    bcftools mpileup -Ovu -f $Pathogene APP/data/Bam/Mapped/"$prefix".sorted.dedup.bam > APP/data/variants.bcftools/"$id"_genotypes.vcf
    
    # gestion de la ploidy
    bcftools call --ploidy $Ploidy -vm -Ov APP/data/variants.bcftools/"$id"_genotypes.vcf > APP/data/variants.bcftools/"$id"_variants.vcf
    
    
    bcftools norm -m+ -c ws -f $Pathogene APP/data/variants.bcftools/"$id"_variants.vcf > APP/data/variants.bcftools/"$id"_normalized.vcf   
    
    bgzip -c APP/data/variants.bcftools/"$id"_normalized.vcf  > APP/data/variants.bcftools/mergevcffile/"$id"_normalized.gz
    
    tabix -p vcf APP/data/variants.bcftools/mergevcffile/"$id"_normalized.gz
done
bcftools merge --force-samples  APP/data/variants.bcftools/mergevcffile/*.gz > APP/data/variants.bcftools/mergevcffile/merge.vcf

mv marked_dup_metrics.txt APP/data/variants.bcftools/metrics/
rm -rf 100