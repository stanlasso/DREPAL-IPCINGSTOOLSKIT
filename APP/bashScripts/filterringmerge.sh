#!/bin/sh

###################################################
#            FILTERING version 1.1                #
###################################################

# initialisation

rm -f APP/data/variants.bcftools/Filterring/mergefile/*
rm -f APP/data/variants.bcftools/metrics/*

#echo $@
Nbargument=$#
#parametre a recuperé avant la fin
count=$(expr $Nbargument - 3)
i=0
## Traitement
declare -a var
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -le  $count ];
    then
        tab[$i]="$read"
    else
        var[$i]="$read"
    fi
done


types=${var[-3]}
Qual=${var[-2]}
Dp=${var[-1]}


echo ${tab[@]}
# echo ${var[@]}
# echo $types
# echo $Qual
# echo $Dp
# echo $chromosome


# init
j=0
while [ "$j" -lt "${#tab[@]}" ]
 do
    if [ "$types" = "all" ];
    then
        let j=j+1
        Input=${tab[$j]}
        bcftools view ${tab[$j]}  > APP/data/variants.bcftools/Filterring/mergefile/merge_"$types".vcf
        sleep 2
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  APP/data/variants.bcftools/Filterring/mergefile/merge_"$types".vcf > APP/data/variants.bcftools/Filterring/mergefile/merge_filtered_"$types".vcf

    else
        let j=j+1
        Input=${tab[$j]}
        bcftools view -v "$types" ${tab[$j]}  > APP/data/variants.bcftools/Filterring/mergefile/merge_"$types".vcf
        sleep 2
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  APP/data/variants.bcftools/Filterring/mergefile/merge_"$types".vcf > APP/data/variants.bcftools/Filterring/mergefile/merge_filtered_"$types".vcf
        
    fi
     
 done

rm -f APP/data/variants.bcftools/Filterring/mergefile/merge_"$types".vcf
