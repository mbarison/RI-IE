#!/bin/sh

mkdir -p ../raw_data

# get PopCtr data
echo "Downloading PopCtr data from StatCan..."
curl "https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=048" -o 98-401-X2016048_eng_CSV.zip

echo "Unzipping archive..."
unzip 98-401-X2016048_eng_CSV.zip -d ../raw_data
rm 98-401-X2016048_eng_CSV.zip

echo "Extracting population counts..."
./get_pop_ctr.py