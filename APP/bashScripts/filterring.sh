#!/bin/sh

###################################################
#            FILTERING version 1.1                #
###################################################

# initialisation

rm -f APP/data/variants.bcftools/Filterring/filteredType/*
rm -f APP/data/variants.bcftools/Filterring/*vcf*
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


#echo ${tab[@]}
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
        prefix=$(echo $Input | cut -d'_' -f 1)
        echo $prefix
        bcftools view ${tab[$j]}  >> "$prefix"-"$types".vcf
        sleep 2
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  "$prefix"-"$types".vcf >> "$prefix"_filtered_"$types".vcf

    else
        let j=j+1
        Input=${tab[$j]}
        prefix=$(echo $Input | cut -d'_' -f 1)
        echo $prefix
        bcftools view -v "$types" ${tab[$j]}  >> "$prefix"-"$types".vcf
        sleep 2
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  "$prefix"-"$types".vcf >> "$prefix"_filtered_"$types".vcf
        
    fi
     
 done

mv APP/data/variants.bcftools/*_"$types".vcf APP/data/variants.bcftools/Filterring/filteredType
cp APP/data/variants.bcftools/Filterring/filteredType/*_filtered_* APP/data/variants.bcftools/Filterring/