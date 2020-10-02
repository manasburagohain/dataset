import os
import os.path
import csv

PATH = "./output/"
EXT = "*.csv"
folders = os.listdir(PATH)
for i in range(len(folders)):
    files = os.listdir(PATH+folders[i])
    
    with open(os.path.join(PATH, folders[i], str(folders[i]).replace(" ", "")+'.csv'), "w") as f:
        csvwriter=csv.writer(f)
        for img in files:
            csvwriter.writerow([img,folders[i]])