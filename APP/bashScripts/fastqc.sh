#!/bin/sh
##########################################################
# By SRC
#Ce script permet de Visualiser les données  via Fastqc
#
##########################################################

#stop à la moindre erreur
set -ueo pipefail
rm -rf APP/data/Datafastq/Fastqc

# initialisation
i=0
### Traitement
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    tab[$i]="$read"
done
echo 
# le repertoire des resultats
#rm -rf $(cd $( dirname $read) && pwd )/Fastqc
mkdir $(cd $( dirname $read) && pwd )/Fastqc
# initialisation
j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt "$#" ]
do
    # Incrémente j de un pas
    let j=j+1

    Input=${tab[$j]}
    
    chemin=${Input:19}
    
    prefix=$(echo $chemin | cut -d'.' -f 1)

    absolute=$(cd $( dirname ${tab[$j]}) && pwd )
    
    echo "Traitement of read ${prefix}"
    
    fastqc ${tab[$j]} -o "${absolute}"/Fastqc &> /dev/null
    mv "${absolute}"/Fastqc/"${prefix}"_fastqc.html  "${absolute}"/Fastqc/"${prefix}".html                  

done

 
