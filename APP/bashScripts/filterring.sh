#!/bin/sh

###################################################
#            FILTERING version 1.1                #
###################################################

# initialisation

rm -rf APP/data/variants.bcftools/Filterring/filteredType/*

#echo $@
Nbargument=$#
#parametre a recuperé avant la fin
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

#recuperation des variables:
types=${var[-3]}
Qual=${var[-2]}
Dp=${var[-1]}


echo ${tab[@]}
echo ${var[@]}
echo $types
echo $Qual
echo $Dp

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
        bcftools view ${tab[$j]}  >> "$prefix"_"$types".vcf
        sleep 2
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  "$prefix"_"$types".vcf >> "$prefix"_filtered_"$types".vcf
    else
        let j=j+1
        Input=${tab[$j]}
        prefix=$(echo $Input | cut -d'_' -f 1)
        echo $prefix

        bcftools view -v "$types" ${tab[$j]}  >> "$prefix"_"$types".vcf
        sleep 2
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  "$prefix"_"$types".vcf >> "$prefix"_filtered_"$types".vcf
    fi
     
 done
 
mv APP/data/variants.bcftools/*_snps.vcf APP/data/variants.bcftools/Filterring/filteredType
cp APP/data/variants.bcftools/Filterring/filteredType/*_filtered_* APP/data/variants.bcftools/Filterring/
mv APP/data/variants.bcftools/*_indels.vcf APP/data/variants.bcftools/Filterring/filteredType
mv APP/data/variants.bcftools/*_all.vcf APP/data/variants.bcftools/Filterring/filteredType