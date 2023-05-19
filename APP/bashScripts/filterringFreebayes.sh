#!/bin/sh

###################################################
# FILTERING Freebayes file version 1              #
###################################################

# initialisation

rm -f APP/data/freebayesfile/Filterring/*

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

# init
j=0
while [ "$j" -lt "${#tab[@]}" ]
 do
    if [ "$types" = "all" ];
    then
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:31}
        id=$(echo $chemin | cut -d'_' -f 1)
        vcffilter -f "DP > $Dp & QUAL > $Qual" $Input > APP/data/freebayesfile/Filterring/"$id"_all.vcf

    elif [[ "$types" == "snps" ]];
    then
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:31}
        id=$(echo $chemin | cut -d'_' -f 1)
        vcffilter -f "TYPE = snp  & DP > $Dp & QUAL > $Qual" $Input > APP/data/freebayesfile/Filterring/"$id"_snps.vcf
    else
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:31}
        id=$(echo $chemin | cut -d'_' -f 1)
        vcffilter -f "( TYPE = ins | TYPE = del ) & DP > $Dp & QUAL > $Qual" $Input > APP/data/freebayesfile/Filterring/"$id"_indel.vcf
    fi
     
 done
 
