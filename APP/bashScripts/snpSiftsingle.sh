for read in "$@"
do
    Input=$read
    
    chemin=${Input:37}
    
    prefix=$(echo $chemin | cut -d'.' -f 1)
    id=$(echo $chemin | cut -d'_' -f 1)
    java -jar APP/snpEff/SnpSift.jar filter "ANN[*].EFFECT = 'missense_variant'" APP/data/Annoted/AnnotatedFILEbyFILE/"$chemin" > APP/data/Annoted/AnnotatedFILEbyFILE/"$id"filter_missense_any.vcf
done