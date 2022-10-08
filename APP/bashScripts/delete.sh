#!/bin/sh

rm -rf APP/data/Bam/Mapped/*.bai
rm -rf APP/data/Bam/Mapped/*.bam
rm -rf APP/data/Bam/*.bam
rm -rf APP/data/Datafastq/Fastqc/*.zip
rm -rf APP/data/Datafastq/Fastqc/*.html
rm -rf APP/data/Datafastq/KDSD/*
rm -rf APP/data/Datafastq/ResQC/*.fastq
rm -rf APP/data/Datafastq/unmapped/*.fastq
rm -rf APP/data/variants.bcftools/Filterring/*.vcf
rm -rf APP/data/variants.bcftools/*.vcf
rm -rf APP/data/variants.varscan/*.vcf
rm -rf APP/data/variants.bcftools/Filterring/MATRICE/*
rm -rf APP/data/variants.bcftools/Filterring/MatriceSNPS/*
rm -rf APP/data/variants.bcftools/Filterring/*.tsv
rm -rf APP/data/variants.bcftools/Filterring/*.gz
rm -rf APP/data/variants.bcftools/Filterring/*.tbi
rm -rf APP/data/variants.bcftools/Filterring/*.bed
rm -rf APP/data/Sam/*.sam
rm -rf APP/data/Datafastq/*.fastq
rm -rf APP/data/variants.varscan/*.mpileup
rm -rf APP/data/variants.varscan/Filterring/*.vcf
rm -rf APP/data/variants.varscan/Filterring/MATRICE/*
rm -rf APP/data/variants.varscan/Filterring/MatriceSNPS/*
rm -rf APP/data/intercep/*