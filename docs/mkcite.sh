
echo -n "Enter reference id: "
read id
echo -n "Enter description: "
read description
echo -n "Enter URL: "
read url

echo "@misc{$id,
    title = {{$description}},
    howpublished = {\url{$url}},
    note = {Accessed: $(date +"%Y-%m-%d")}
}" >> report.bib
