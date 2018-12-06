#!/usr/bin/python
import re

def parse_claim(claim):
    claim_ptrn = re.compile(r'\#\d+ \@ (\d+,\d+): (\d+x\d+)')
    
