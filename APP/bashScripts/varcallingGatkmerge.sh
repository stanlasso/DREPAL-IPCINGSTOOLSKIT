# #!/bin/sh
# # Ce script permet de faire du Variants Calling
rm -f APP/data/gatkfile/vcffile/*
rm -f APP/data/gatkfile/textfile/file.list
rm -rf APP/data/Bam/Mapped/BamGATK/*.bam* && rm -rf APP/data/gatkfile/vcffile/*.vcf* && rm -rf APP/data/gatkfile/recal/*.table && rm -rf APP/data/Reference/*.dict
#tabix -f APP/data/combined/3d7_hb3.combined.final.vcf.gz


Nbargument=$#
bamfileoccurence=`expr $Nbargument - 2`

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
prefixRef=$(echo $Pathogene | cut -d'.' -f 1)
gatk CreateSequenceDictionary -R $Pathogene -O $prefixRef.dict
samtools faidx $Pathogene


j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt $bamfileoccurence ]
do
    let j=j+1
    
    Input=${tab[$j]}
    
    chemin=${Input:20}
    
    prefix=$(echo $chemin | cut -d'.' -f 1)

    id=$(echo $chemin | cut -d'_' -f 1)


    gatk SortSam -I APP/data/Sam/"${id}"_Patho_align.sam -O APP/data/Bam/Mapped/BamGATK/"${id}".bam --SORT_ORDER coordinate

    gatk MarkDuplicates -I APP/data/Bam/Mapped/BamGATK/"${id}".bam -O APP/data/Bam/Mapped/BamGATK/"${id}".dup.bam -METRICS_FILE metrics."$id".txt 
    
    samtools index  APP/data/Bam/Mapped/BamGATK/"${id}".dup.bam

    # TROUVER UNE SOLUTION
    gatk BaseRecalibrator -R $Pathogene -I APP/data/Bam/Mapped/BamGATK/"${id}".dup.bam --known-sites APP/data/combined/3d7_hb3.combined.final.vcf.gz -O APP/data/gatkfile/recal/"$id".table

    gatk ApplyBQSR -R $Pathogene -I APP/data/Bam/Mapped/BamGATK/"${id}".dup.bam --bqsr-recal-file APP/data/gatkfile/recal/"$id".table -O APP/data/Bam/Mapped/BamGATK/"${id}".dup.bqsr.bam
    
    gatk HaplotypeCaller -ploidy $Ploidy -R $Pathogene -I APP/data/Bam/Mapped/BamGATK/"${id}".dup.bqsr.bam -O APP/data/gatkfile/vcffile/"$id"_variants.vcf

    bgzip -c APP/data/gatkfile/vcffile/"$id"_variants.vcf  > APP/data/gatkfile/vcffile/"$id"_variants.vcf.gz
    
    tabix -p vcf APP/data/gatkfile/vcffile/"$id"_variants.vcf.gz


done

bcftools merge --force-samples  APP/data/gatkfile/vcffile/*.gz > APP/data/gatkfile/mergevcfile/merge.vcf

mv *metrics.* APP/data/gatkfile/metrics/
