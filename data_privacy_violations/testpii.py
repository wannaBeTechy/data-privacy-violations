# -*- coding: utf-8 -*-
from piidetect.pipeline import binary_pii

data={"Labels":["This is really right job"]}
data['Target'] = binary_pii(data['Labels'][0]) #.apply(binary_pii)
print(data['Target'] )