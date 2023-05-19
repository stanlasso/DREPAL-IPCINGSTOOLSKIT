#!/bin/sh

###################################################
#      FILTERING chromosome version 0             #
###################################################

# initialisation

rm -f APP/data/chromosome/*vcf*

#echo $@
Nbargument=$#
#parametre a recuperé avant la fin
count=$(expr $Nbargument - 1)
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

# #recuperation des variables:

chromosome=${var[-1]}

# init
j=0
while [ "$j" -lt "${#tab[@]}" ]
do
    let j=j+1
    Input=${tab[$j]}
    chemin="${Input##*/}"
    prefix=$(echo $chemin | cut -d'_' -f 1)    

    bgzip -c $Input  > APP/data/chromosome/"$prefix"_"$chromosome".vcf.gz
    tabix -p vcf APP/data/chromosome/"$prefix"_"$chromosome".vcf.gz
    sleep 2
    bcftools view APP/data/chromosome/"$prefix"_"$chromosome".vcf.gz --regions $chromosome > APP/data/chromosome/"$prefix"_"$chromosome".vcf     
done
 