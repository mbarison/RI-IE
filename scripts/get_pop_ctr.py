#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

csv.register_dialect('textquote', delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

geo_starts = []

with open("../raw_data/Geo_starting_row_CSV.csv") as f:
	skipFirst = True
	for l in f:
		if skipFirst:
			skipFirst = False
			continue
		tokens = l.strip().split(",")
		geo_starts.append(int(tokens[2]))


with open("../data/csd2pc/PopCtrData.csv", "wb") as of:
	uwrite = csv.DictWriter(of, dialect='textquote', fieldnames=["GEO_CODE","GEO_NAME","Population"], extrasaction="ignore")
	uwrite.writeheader()
	with open("../raw_data/98-401-X2016048_English_CSV_data.csv", "rb") as f:
		uread = csv.DictReader(f)
		lcnt = 0
		for l in uread:
			lcnt = lcnt+1
			l["Population"] = l.pop("Dim: Sex (3): Member ID: [1]: Total - Sex")
			l["GEO_CODE"]   = l.pop("GEO_CODE (POR)")
			if lcnt in geo_starts:
				uwrite.writerow(l)

