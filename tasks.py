"""
GAVIP Example AVIS: Simple AVI

An example AVI pipeline is defined here, consisting of three tasks:

- DummyTask - demonstrates dependencies, but does nothing
- DownloadData - uses services.gacs.GacsQuery to run ADQL queries in GACS(-dev)
- ProcessData - generates a simple scatter plot with Bokeh from the downloaded data
@req: REQ-0006
@comp: AVI Web System
"""

from django.conf import settings
import numpy as  np
import os
# Class used for creating pipeline tasks
from pipeline.classes import (
    AviTask,
    AviParameter, AviLocalTarget,
)

inputFile = AviParameter()

def list_3(inputFile):
    with open(inputFile) as f:
        mylist = list(f)
        list_result=mylist[0]
        
    a=list_result.split(',')

    b=a[(len(a)-1)]
    c=b.split(']')
    d=c[0]
    a[(len(a)-1)] = d

    b=a[0]
    c=b.split('[')
    d=c[(len(c)-1)]
    a[0] = d

    new_list1=[]
    for i in a:
        m=float(i)
        n=int(m)
        new_list1.append(n)
        
    new_list1 = np.array(new_list1)
    new_list = new_list1 

    final_list=[]
    for i in new_list:
        if i == 105:
            a = ' '
        else:
            a = chr((i-1) + ord('A'))
        print(a)
        final_list.append(a)

    b = str(final_list)
    a = b.encode('utf-8')
    return a


class Convert(AviTask):

    inputFile = AviParameter()

    def output(self):
        return AviLocalTarget(os.path.join(
            settings.OUTPUT_PATH,
            "list_3.txt"
        ))

    def input(self):
        return AviLocalTarget(os.path.join(
            '/user_space/avi2_avi2/output', self.inputFile
        ))

    def run(self):
        list_result_3 = list_3(self.input().path)
        with open(self.output().path, 'wb') as out:
            print(list_result_3)
            out.write(list_result_3)

