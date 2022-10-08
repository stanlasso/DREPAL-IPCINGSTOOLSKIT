rm -rf APP/data/variants.varscan/Filterring/MATRICE/*.tsv && rm -rf APP/data/variants.varscan/Filterring/MatriceSNPS/*.tsv

bash APP/data/variants.varscan/Filterring/generation.sh APP/data/variants.varscan/Filterring/*_snps_variants.vcf

sleep 1.5
