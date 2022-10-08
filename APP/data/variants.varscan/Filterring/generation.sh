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
    chemin=${Input:37} #pour chemin plus long dans script finale
    prefix=$(echo $chemin | cut -d'_' -f 1)

    awk '{ print $1,$2,$3,$19 }' APP/data/variants.varscan/Filterring/"$prefix"_snps_variants.vcf >> APP/data/variants.varscan/Filterring/MATRICE/"$prefix".tsv

done