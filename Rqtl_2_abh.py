#conversion of asmap-output csv to abh-genotyper csv input
import sys
from itertools import chain



INFILE=sys.argv[1]
OUTFILE=sys.argv[2]


header = []
LG = []
CM = []
chrs = []
body = []

with open(INFILE, "r") as infi: 
    line = ""
    for k, line in enumerate(infi): 
        k += 1
        #marker
        if k == 1: 
            
            #generate header line in manner of 
            #[genotypes,marker1Scaffold1_positionL#n_CM, marker2Scaffold1_position#n_CM....]
            #use centimorgans to generate distance across LGs
            line = line.strip()
            line = line.split(',')
            line =  [it.replace("_","bp") for it in line]
            header = line
            
        #LGs
        elif k == 2: 
            line = line.strip()
            line = line.split(',')
            line =  [it.replace(".","") for it in line]
            LG = line
            for ak in line: 
                ak1 = ak.replace("L","")
                chrs.append(ak1)
        #CM
        elif k == 3:
            line = line.strip()
            line = line.split(",")
            kl = [] 
            for i in line: 
                if i:
                    kl.append(str(int(float(i)* 100000)))
                else: 
                    kl.append("")#print(str(i))
            CM= kl
        
        else:
            #print(line)
            line = line.strip()
            line = line.split(",")
            line =  [it.replace("AA","A") for it in line]
            line =  [it.replace("BB","B") for it in line]
            line =  [it.replace("-","N") for it in line]
            body.append(line)


gz = []
for ei in list(zip(header, LG)):
   gz.append("".join(ei))

gz1 = []
for eii in list(zip(gz, CM)):
     gz1.append("_".join(eii))


gz1[0] = "genotypes"
chrs[0] = "chrs"

print("Extracting {} markers from {} individuals".format(len(gz1)-1, k-3))

with open(OUTFILE, "w") as outf:
    outf.write(",".join(gz1)+"\n")
    outf.write(",".join(chrs)+"\n")
    for li in body:
        outf.write(",".join(li)+"\n")
print("Finished.")
