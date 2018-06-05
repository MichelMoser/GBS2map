#conversion of asmap-output csv to abh-genotyper csv input
import sys
from itertools import chain



INFILE=sys.argv[1]

header = []
LG = []
CM = []

with open(INFILE, "r") as infi: 
    for k, line in enumerate(infi): 
        k += 1
        #marker
        if k == 1: 
            
            #generate header line in manner of 
            
            #[genotypes,marker1Scaffold1_positionL#n_CM, marker2Scaffold1_position#n_CM....]
            
            #use centimorgans to generate distance across LGs
            

            #print(line)
            line = line.strip()
            line = line.split(',')
            header = line
        #LGs
        if k == 2: 
            #print(line)
            line = line.strip()
            line = line.split(',')
            LG = line
        #CM
        if k == 3:
            #print(line)
            line = line.strip()
            line = line.split(',')
            CM= line


for i in list(zip(header, LG, CM)):
    print("_".join(i))
