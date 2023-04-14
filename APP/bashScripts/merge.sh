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
    if [ $i -lt  $count ];
    then
        tab[$i]="$read"
    else
        var[$i]="$read"
    fi
done
#recuperation des variables:


directory=${tab[1]}
echo $directory


if [[ "$directory" == "bcftools" ]];
then
    echo "enter"
    for read in "${var[@]}"
    do
      bgzip $read
      tabix $read'.gz'
    done
    bcftools merge --force-samples APP/data/variants.bcftools/Filterring/*.gz > APP/data/Annoted/merge.vcf
    gunzip APP/data/variants.bcftools/Filterring/*.gz
    rm -rf APP/data/variants.bcftools/Filterring/*.tbi

else
    echo "no enter"
    for read in "${var[@]}"
    do
      bgzip $read
      tabix $read'.gz'
    done
    bcftools merge APP/data/gatkfile/Filterring/*.gz > APP/data/Annoted/merge.vcf
    gunzip APP/data/gatkfile/Filterring/*.gz
    rm -rf APP/data/gatkfile/Filterring/*.tbi
   
fi
