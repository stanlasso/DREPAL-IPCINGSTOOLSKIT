#!/bin/sh

###################################################
#  FILTERING FREEBAYES version 1.1                #
###################################################

#echo $@
Nbargument=$#
#parametre a recuperé avant la fin
i=0
## Traitement
declare -a tab
for read in "$@"
do
    tab[$i]="$read"
    let i=i+1   

done

#recuperation des variables:
types=${tab[-3]}
Qual=${tab[-2]}
Dp=${tab[-1]}
VCF=${tab[0]}

if [[ "$types" == "all" ]];
then
    vcffilter -f "DP > $Dp & QUAL > $Qual" $VCF > APP/data/freebayesfile/Filterring/mergefile/merge_all.vcf
elif [[ "$types" == "snps" ]];
then
    vcffilter -f "TYPE = snp  & DP > $Dp & QUAL > $Qual" $VCF > APP/data/freebayesfile/Filterring/mergefile/merge_snp.vcf
else
    vcffilter -f "( TYPE = ins | TYPE = del ) & DP > $Dp & QUAL > $Qual" $VCF > APP/data/freebayesfile/Filterring/mergefile/merge_indel.vcf
fi
 