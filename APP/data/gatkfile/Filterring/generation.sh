#!/bin/sh

###################################################
#            MATRIX version 1.1                   #
###################################################
# RECUPERE LES FICHIERS ISSUE DU FILTERING PUIS LES 
# LES TRAITES POUR FORMER UNE MATRICE DE n,m ou LES 
# COLONNES SONT LES INDIVIDUS(AlternatifS) ET ASSO-
# CIE AUX POSTIONS , REFERENCES ET CHROMOSONES ...   
###################################################
#initialisation
i=0
### Traitement
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    tab[$i]="$read"
done

# echo "---------------------------------------"

# echo $read

# echo '--------------------------------------'
# initialisation
j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt "$#" ]
do
    # Incrémente j de deux pas
    let j=j+1
    #if [ $j -le "$#" ]
    #then
    #Extraire le préfixe du gène
    Input=${tab[$j]}
    
    
    chemin=${Input:29} #pour chemin plus long dans script finale
    #echo "$chemin"
    prefix=$(echo $chemin | cut -d'_' -f 1)

    bgzip -c APP/data/gatkfile/Filterring/"$prefix"_filtered_snps.vcf  > APP/data/gatkfile/Filterring/"$prefix"_filtered_snps.vcf.gz

    tabix -p vcf  APP/data/gatkfile/Filterring/"$prefix"_filtered_snps.vcf.gz

    # merge des sorties en une seul des chromosones...positions...references...alternatifs pour chacun des individus: 
    bcftools view APP/data/gatkfile/Filterring/"$prefix"_filtered_snps.vcf | bcftools query -f '%CHROM\t%POS\t%REF\t%ALT\n' | sort +1 -n  >> APP/data/gatkfile/Filterring/"$prefix"_CPRA.tsv


    cut -f 1 APP/data/gatkfile/Filterring/"$prefix"_CPRA.tsv >> APP/data/gatkfile/Filterring/"$prefix"_Chromosones.tsv
    cut -f 2 APP/data/gatkfile/Filterring/"$prefix"_CPRA.tsv >> APP/data/gatkfile/Filterring/"$prefix"_Positions.tsv
    cut -f 3 APP/data/gatkfile/Filterring/"$prefix"_CPRA.tsv >> APP/data/gatkfile/Filterring/"$prefix"_References.tsv
    cut -f 4 APP/data/gatkfile/Filterring/"$prefix"_CPRA.tsv >> APP/data/gatkfile/Filterring/"$prefix"_Alternatif.tsv


    sed -i '1iPOSITION' APP/data/gatkfile/Filterring/"$prefix"_Positions.tsv 
    sed -i '1iREFERENCE' APP/data/gatkfile/Filterring/"$prefix"_References.tsv 
    sed -i '1iCHROMOSOME' APP/data/gatkfile/Filterring/"$prefix"_Chromosones.tsv
    sed -i "1i$prefix" APP/data/gatkfile/Filterring/"$prefix"_Alternatif.tsv

    paste APP/data/gatkfile/Filterring/"$prefix"_Chromosones.tsv APP/data/gatkfile/Filterring/"$prefix"_Positions.tsv APP/data/gatkfile/Filterring/"$prefix"_References.tsv APP/data/gatkfile/Filterring/"$prefix"_Alternatif.tsv >> APP/data/gatkfile/Filterring/MATRICE/"$prefix"_data.tsv   


done

bcftools merge --force-samples APP/data/gatkfile/Filterring/*filtered_snps.vcf.gz > APP/data/gatkfile/Filterring/01.vcf
bcftools view APP/data/gatkfile/Filterring/01.vcf | bcftools query -f '%CHROM\t%POS\t%REF\n' >> APP/data/gatkfile/Filterring/01snps.tsv
sort +1 -n APP/data/gatkfile/Filterring/01snps.tsv | uniq >> APP/data/gatkfile/Filterring/01snps_sorted.tsv

cut -f 1 APP/data/gatkfile/Filterring/01snps_sorted.tsv >> APP/data/gatkfile/Filterring/Chromosones.tsv
cut -f 2 APP/data/gatkfile/Filterring/01snps_sorted.tsv >> APP/data/gatkfile/Filterring/Positions.tsv
cut -f 3 APP/data/gatkfile/Filterring/01snps_sorted.tsv >> APP/data/gatkfile/Filterring/References.tsv


sed -i '1iPOSITION' APP/data/gatkfile/Filterring/Positions.tsv
sed -i '1iREFERENCE' APP/data/gatkfile/Filterring/References.tsv
sed -i '1iCHROMOSOME' APP/data/gatkfile/Filterring/Chromosones.tsv

paste APP/data/gatkfile/Filterring/Chromosones.tsv APP/data/gatkfile/Filterring/Positions.tsv APP/data/gatkfile/Filterring/References.tsv >> APP/data/gatkfile/Filterring/MATRICE/01snps_data.tsv
