#!/bin/sh

cp APP/data/variants.bcftools/Filterring/01.vcf APP/data/intercep/
bgzip -c APP/data/intercep/01.vcf > APP/data/intercep/01.vcf.gz
tabix -p vcf APP/data/intercep/01.vcf.gz
bedtools intersect -a APP/data/intercep/01.vcf.gz -b APP/data/intercep/listposition.bed >> APP/data/intercep/allIntersect.vcf
rm -rf APP/data/intercep/01.vcf && rm -rf APP/data/intercep/01.vcf.gz && rm -rf APP/data/intercep/01.vcf.gz.tbi
rm -rf APP/data/intercep/listposition.bed