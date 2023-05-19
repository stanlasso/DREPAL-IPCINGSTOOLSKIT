#!/bin/sh

###################################################
#            FILTERING MERGE GATK version 1.1                #
###################################################

# initialisation

rm -f APP/data/gatkfile/Filterring/mergefile/*.vcf

#echo $@
Nbargument=$#
#parametre a recuperé avant la fin
count=$(expr $Nbargument - 4)
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

#recuperation des variables:
types=${var[-4]}
Qual=${var[-3]}
Dp=${var[-2]}
Pathogene=${var[-1]}

echo ${tab[@]}

# init
j=0
while [ "$j" -lt "${#tab[@]}" ]
 do
    if [[ "$types" == "all" ]];
    then
        let j=j+1
        Input=${tab[$j]}

        gatk  SelectVariants -R $Pathogene -V $Input -O APP/data/gatkfile/Filterring/mergefile/merge_ALLvariants.vcf -select "QUAL > $Qual && DP > $Dp" 
    
    elif [[ "$types" == "snps" ]];
    then
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:26}
        id=$(echo $chemin | cut -d'_' -f 1)


        gatk SelectVariants -R $Pathogene -V $Input -O APP/data/gatkfile/Filterring/mergefile/merge_filtered_snps.vcf -select-type SNP -select "QUAL > $Qual && DP > $Dp" 
    
    else
        let j=j+1
        Input=${tab[$j]}
        chemin=${Input:26}
        id=$(echo $chemin | cut -d'_' -f 1)

       gatk SelectVariants -R $Pathogene -V $Input -O APP/data/gatkfile/Filterring/mergefile/merge_INDELvariants.vcf -select-type INDEL -select "QUAL > $Qual && DP > $Dp" 
    fi
     
done
