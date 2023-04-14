rm -rf APP/data/Annoted/report/*

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
Genome=${var[-2]}
VcfCombine=${var[-1]}

java -Xmx4g -jar APP/snpEff/snpEff.jar $Genome $VcfCombine > APP/data/Annoted/annotated.vcf
mv snpEff_genes.txt snpEff_summary.html APP/data/Annoted/report/    