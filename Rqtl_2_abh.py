#conversion of asmap-output csv to abh-genotyper csv input
import sys
from itertools import chain
import argparse




parser = argparse.ArgumentParser(description='Convert between qtl and abh input')


parser.add_argument('-q2a', default=False, help='convert qtl csv-file to abhGenotyper csv-file', action='store_true')

parser.add_argument('-a2q', default=False, help='convert abhGenotyper csv-file to qtl csv-file', action='store_true')

parser.add_argument('-i', '--input',  help='specify input csv-file', required =
                   True)
parser.add_argument('-o', '--output', help='specify output csv-file', required
                   = True)

args = parser.parse_args()



INFILE=args.input
OUTFILE=args.output


def qtl2abh(csvfile): 
    
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
            
<<<<<<< HEAD
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


def abh2qtl(csvfile): 
    
    harvest = []

    with open(INFILE, "r") as infi: 
        line = ""
        for k, line in enumerate(infi): 
            k += 1
            #marker
            if k == 1:
                line = line.strip()
                line = line.split(",")
                line[0] ==  "Genotype"
                harvest.append(line)

            elif k == 2:
                line = line.strip()
                line = line.split(",")
                line[0] = ""
                harvest.append(line)
            else: 
                line = line.strip()
                line = line.split(",")
                harvest.append(line)

    with open(OUTFILE, "w") as outf: 
        for li in harvest: 
            outf.write(",".join(li)+"\n")
        print("Finished.")


def main():

    if args.q2a: 
        qtl2abh(args.input)
        print("QTL to ABHGENOTYPER")

    elif args.a2q: 
       abh2qtl(args.input)
       print("ABHGENOTYPER to QTL")

    else: 
        print("Nothing to do... type -h for options")


if __name__ == "__main__":
       main()
=======
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
>>>>>>> a7b6cb117a9dd094475df561ac0ea1d4eb1632b8
