rm -rf APP/data/gatkfile/Filterring/01.vcf
rm -rf APP/data/gatkfile/Filterring/*.tsv && rm -rf APP/data/gatkfile/Filterring/*gz
rm -rf APP/data/gatkfile/Filterring/MATRICE/*.tsv && rm -rf APP/data/gatkfile/Filterring/MatriceSNPS/MATRICE.tsv
bash APP/data/gatkfile/Filterring/generation.sh APP/data/gatkfile/Filterring/*_filtered_snps.vcf

sleep 1.5