rm -rf APP/data/variants.bcftools/Filterring/*.tsv && rm -rf APP/data/variants.bcftools/Filterring/*gz
rm -rf APP/data/variants.bcftools/Filterring/MATRICE/*.tsv && rm -rf APP/data/variants.bcftools/Filterring/MatriceSNPS/MATRICE.tsv
bash APP/data/variants.bcftools/Filterring/generation.sh APP/data/variants.bcftools/Filterring/*_filtered_snps.vcf

sleep 1.5


#bash APP/data/variants.bcftools/Filterring/comparaison.sh APP/data/variants.bcftools/Filterring/*_CPRA.txt
#
#sleep 1.5
#
#bash APP/data/variants.bcftools/Filterring/recupcol.sh APP/data/variants.bcftools/Filterring/*_comp.tsv

