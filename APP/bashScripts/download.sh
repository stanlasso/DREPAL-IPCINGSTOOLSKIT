cut -f 1 $1 | cut -d';' -f 1 | while  read ligne ; do
    if [[ "$ligne" == "fastq_ftp" ]]
    then
        sed -i -e "1d" $1
    else
        wget ftp://$ligne
        gzip -d  *.fastq.gz
        mv *.fastq APP/data/Datafastq
    fi
done

cut -f 1 $1 | cut -d';' -f 2 | while  read ligne ; do
    if [[ "$ligne" == "fastq_ftp" ]]
    then
        sed -i -e "1d" $1
    else
        wget "ftp://$ligne"
        gzip -d  *.fastq.gz
        mv *.fastq APP/data/Datafastq
    fi
done
touch forceremove.fastq
rm -d *fastq
rm -rf  APP/data/Datafastq/*.txt