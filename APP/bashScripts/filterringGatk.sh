#!/bin/sh

###################################################
#            FILTERING GATK version 1.1                #
###################################################

# initialisation

rm -rf APP/data/gatkfile/Filterring/*.vcf*

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
    if [ $i -lt  $count ];
    then
        tab[$i]="$read"
    else
        var[$i]="$read"
    fi
done

#recuperation des variables:
types=${var[-4]}
Qual=${var[-3]}
Dp=${var[-2]}
Pathogene=${var[-1]}

echo "${tab[@]}"
echo "${var[@]}"
echo "$types"
echo "$Qual"
echo "$Dp"
echo "$Pathogene"
# init
j=0
while [ "$j" -lt "${#tab[@]}" ]
 do
    if [[ "$types" == "all" ]];
    then
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:26}
        id=$(echo $chemin | cut -d'_' -f 1)

        gatk  SelectVariants -R $Pathogene -V APP/data/gatkfile/vcffile/"$id"_variants.vcf -O APP/data/gatkfile/Filterring/"$id"_ALLvariants.vcf -select "QUAL > $Qual && DP > $Dp" 
    
    elif [[ "$types" == "snps" ]];
    then
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:26}
        id=$(echo $chemin | cut -d'_' -f 1)


        gatk SelectVariants -R $Pathogene -V APP/data/gatkfile/vcffile/"$id"_variants.vcf -O APP/data/gatkfile/Filterring/"$id"_filtered_snps.vcf -select-type SNP -select "QUAL > $Qual && DP > $Dp" 
    
    else
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:26}
        id=$(echo $chemin | cut -d'_' -f 1)

       gatk SelectVariants -R $Pathogene -V APP/data/gatkfile/vcffile/"$id"_variants.vcf -O APP/data/gatkfile/Filterring/"$id"_INDELvariants.vcf -select-type INDEL -select "QUAL > $Qual && DP > $Dp" 
    fi
     
done
