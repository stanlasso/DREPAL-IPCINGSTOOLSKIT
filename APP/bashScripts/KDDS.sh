#####################################################
# KDDS SCRIPTS BY SRC
#
#####################################################
Nbargument=$#
#parametre a recuperé avant la fin
count=$(expr $Nbargument - 2)
n=0
## Traitement
declare -a var
declare -a tab
for read in "$@"
do
    let n=n+1
    # mettre tous les fichiers dans un tableau
    if [ $n -lt $count ];
    then
        tab[$n]="$read"
    else
        var[$n]="$read"
    fi
done


#recuperation des variables:
Hote_genome=${var[$(expr $Nbargument - 2)]}

Pato_genome=${var[$(expr $count + 1)]}

k=${var[$(expr $count + 2)]}


echo $Hote_genome

echo $Pato_genome





# # creatin d'un fichier fastq0 pour les valeur de depart
mkdir APP/data/Datafastq/KDSD/fastq0
# # copie des reference des fastq dans le dossier fastq0
cp APP/data/Datafastq/KDSD/*.fastq  APP/data/Datafastq/KDSD/fastq0
# # creation d'un dossier et un fichier pour les statistique de sortie
mkdir APP/data/Datafastq/KDSD/Stats
touch APP/data/Datafastq/KDSD/Stats/stats.txt


K=0
# STOCKAGE DES STATS DANS STATS.TXT
seqkit stats APP/data/Datafastq/KDSD/fastq"$K"/*fastq >> APP/data/Datafastq/KDSD/Stats/stats.txt


while [ "$K" -lt "$k" ]
do
    let K=K+1


    echo "======================================================="

    echo "Iteration : $K"
    
    echo "======================================================="

    # a chaque iteration creation d'un dossier fasqk pour le stockage des sorties fastq
    mkdir APP/data/Datafastq/KDSD/fastq"$K"
    
    
    
    i=0
    ### Traitement
    echo "Veuillez patienter SVP ! l'extraction du génome humain est en cours ..."
    declare -a lab
    for read in "${tab[@]}"
    do
        let i=i+1
        # mettre tous les fichiers dans un lableau
        lab[$i]="$read"
    done
    
    # initialisation
    j=0
    #Tantque la variable j est inférieur ou égale à la taille du lableau
    while [ "$j" -lt "${#tab[@]}" ]
    do
        let j=j+2
        #Extraire le préfixe du gène
        Input=${lab[$j-1]}
        
        chemin=${Input:24}
        
        prefix=$(echo $chemin | cut -d'_' -f 1)
        echo "$prefix"
        
        # obtention du fichier sam
        bwa mem $Hote_genome ${lab[$j-1]} ${lab[$j]} -o APP/data/Datafastq/KDSD/"${prefix}".sam
        
        #supression des fichiers *fastq pour la prochaine iteration
        rm APP/data/Datafastq/KDSD/*"${prefix}"_1.fastq
        rm APP/data/Datafastq/KDSD/*"${prefix}"_2.fastq
        
        # mapped et unmapped pour l'obtention des fichiers bam puis suppression du fichier sam
        samtools view -Sb -f0x4 APP/data/Datafastq/KDSD/"${prefix}".sam  > APP/data/Datafastq/KDSD/"${prefix}"_Hote_unmapped.bam
        samtools view -Sb -F0x4 APP/data/Datafastq/KDSD/"${prefix}".sam > APP/data/Datafastq/KDSD/"${prefix}"_Hote_mapped.bam
        rm APP/data/Datafastq/KDSD/*.sam
        
        # conversion en fastq puis suppression du fichier bam
        samtools bam2fq -1 APP/data/Datafastq/KDSD/"${prefix}"_1.fastq -2 APP/data/Datafastq/KDSD/"${prefix}"_2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Datafastq/KDSD/"${prefix}"_Hote_unmapped.bam
        samtools bam2fq -1 APP/data/Datafastq/KDSD/"${prefix}_Hote_unmapped"_R1.fastq -2 APP/data/Datafastq/KDSD/"${prefix}_Hote_unmapped"_R2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Datafastq/KDSD/"${prefix}"_Hote_unmapped.bam
        samtools bam2fq -1 APP/data/Datafastq/KDSD/"${prefix}_Hote_mapped"_R1.fastq -2 APP/data/Datafastq/KDSD/"${prefix}_Hote_mapped"_R2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Datafastq/KDSD/"${prefix}"_Hote_mapped.bam
        rm APP/data/Datafastq/KDSD/*.bam
        
        
        # # mapped et unmapped pour l'obtention des fichiers bam puis suppression du fichier sam
        bwa mem $Pato_genome APP/data/Datafastq/KDSD/"${prefix}"_1.fastq APP/data/Datafastq/KDSD/"${prefix}"_2.fastq -o APP/data/Datafastq/KDSD/"${prefix}".sam
        rm APP/data/Datafastq/KDSD/*"${prefix}"_1.fastq
        rm APP/data/Datafastq/KDSD/*"${prefix}"_2.fastq
        
        #obtention du fichier bam puis la suppression du fichier sam
        samtools view -Sb -f0x4 APP/data/Datafastq/KDSD/"${prefix}".sam  > APP/data/Datafastq/KDSD/"${prefix}"Patho_unmapped.bam
        samtools view -Sb -F0x4 APP/data/Datafastq/KDSD/"${prefix}".sam > APP/data/Datafastq/KDSD/"${prefix}"Patho_mapped.bam
        rm APP/data/Datafastq/KDSD/*.sam
        
        # creation des fichiers fastq puis suppression du fichier bam
        samtools bam2fq -1 APP/data/Datafastq/KDSD/"${prefix}_Patho_unmapped"_R1.fastq -2 APP/data/Datafastq/KDSD/"${prefix}_Patho_unmapped"_R2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Datafastq/KDSD/"${prefix}"Patho_unmapped.bam
        samtools bam2fq -1 APP/data/Datafastq/KDSD/"${prefix}_Patho_mapped"_R1.fastq -2 APP/data/Datafastq/KDSD/"${prefix}_Patho_mapped"_R2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Datafastq/KDSD/"${prefix}"Patho_mapped.bam
        samtools bam2fq -1 APP/data/Datafastq/KDSD/"${prefix}"_1.fastq -2 APP/data/Datafastq/KDSD/"${prefix}"_2.fastq -0 /dev/null -s /dev/null -n -F 0x900 APP/data/Datafastq/KDSD/"${prefix}"Patho_mapped.bam
        rm APP/data/Datafastq/KDSD/*.bam
        
        
    done
   
    
    # copie de tous les fichiers resultants dans le dossier d'indice k
    cp APP/data/Datafastq/KDSD/*_R1.fastq  APP/data/Datafastq/KDSD/fastq"$K" 
    cp APP/data/Datafastq/KDSD/*_R2.fastq  APP/data/Datafastq/KDSD/fastq"$K"
    # suppression de tous les fichiers fastq autre que les prefixés pour l'iteration suivante
    rm APP/data/Datafastq/KDSD/*_R1.fastq | rm APP/data/Datafastq/KDSD/*_R2.fastq
        
    seqkit stats APP/data/Datafastq/KDSD/fastq"$K"/*fastq >> APP/data/Datafastq/KDSD/Stats/stats.txt


done
rm -rf APP/data/Datafastq/KDSD/*.fastq

# get specifique line for graph
awk '{print $4}' APP/data/Datafastq/KDSD/Stats/stats.txt | uniq >> APP/data/Datafastq/KDSD/Stats/allnumseq.txt
awk 'NR==1 { print $0 }' APP/data/Datafastq/KDSD/Stats/allnumseq.txt >> APP/data/Datafastq/KDSD/Stats/graph.txt
awk 'NR==4 { print $0 }' APP/data/Datafastq/KDSD/Stats/allnumseq.txt >> APP/data/Datafastq/KDSD/Stats/graph.txt
awk 'NR==6 { print $0 }' APP/data/Datafastq/KDSD/Stats/allnumseq.txt >> APP/data/Datafastq/KDSD/Stats/graph.txt
awk 'NR==7 { print $0 }' APP/data/Datafastq/KDSD/Stats/allnumseq.txt >> APP/data/Datafastq/KDSD/Stats/graph.txt
