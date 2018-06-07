# GBS2map
____

### workflow and tool-set to construct genetic maps from GBS data

#### needed input:  
  * demultiplexed GBS sequenced from a mapping population   
  * reference genome (draft genome)
  
#### output: 
* markers based on sequences of the reference genome
* genetic map

* sequences anchored to linkage groups



#### conversion of qtl-objects to ABGgenotyer-input

python Rqtl_2_abh.py  path/to/input/qtl.cross.csv   path/to/output/abh.input.csv
