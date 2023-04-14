#!/bin/sh

cp APP/data/gatkfile/Filterring/01.vcf  APP/data/intercep/
cp APP/data/variants.bcftools/Filterring/01bcf.vcf APP/data/intercep/
bgzip -c APP/data/intercep/01.vcf > APP/data/intercep/01.vcf.gz
tabix -p vcf APP/data/intercep/01.vcf.gz
bgzip -c APP/data/intercep/01bcf.vcf > APP/data/intercep/01bcf.vcf.gz
tabix -p vcf APP/data/intercep/01bcf.vcf.gz
bedtools intersect -header -a APP/data/intercep/01.vcf.gz -b APP/data/intercep/01bcf.vcf > APP/data/intercep/allIntersect.vcf
rm -rf APP/data/intercep/01.vcf && rm -rf APP/data/intercep/01.vcf.gz && rm -rf APP/data/intercep/01.vcf.gz.tbi
rm -rf APP/data/intercep/01bcf.vcf && rm -rf APP/data/intercep/01bcf.vcf.gz && rm -rf APP/data/intercep/01bcf.vcf.gz.tbi
rm -rf APP/data/intercep/listposition.bed