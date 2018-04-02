#!/root/anaconda3/envs/my_env/bin/python

import pandas as pd
import sys
# import os
# import csv
# import urllib.request

# df =  pd.read_csv('http://data.ntpc.gov.tw/od/zipfiledl?oid=A7F473A4-A633-4D5A-8DA7-CB1E62597A08&ft=zip')
# v2, add params as conf file
# conf format:
# csv,col
# v3, process the file directly from url
# failed to download file from data.ntpc.gobv.tw
# v4, get file from https://quality.data.gov.tw/dq_download_csv.php?nid=55337&md5_url=43ea6ebf73387810168c47b897b8e1ab

conf = sys.argv[1]

linelist = []
file = open(conf, 'r')
# print(type(file))
for aline in file:
	linelist.append(aline.strip())

for line in linelist:
	param = line.split(",")
	infile = param[0]
	filename = param[1]
	col = param[2]
	outfile = filename+'.csv'
	df = pd.read_csv(infile)
	df = df[pd.notnull(df[col])]
	name = df[col]
	name.to_csv(outfile, index=False)

