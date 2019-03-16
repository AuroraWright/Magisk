#!/usr/bin/env python3
import sys
import os
import subprocess
import lzma

def binary_dump(src, out, var_name):
	out.write('const static unsigned char {}[] = {{'.format(var_name))
	for i, c in enumerate(xz(src.read())):
		if i % 16 == 0:
			out.write('\n')
		out.write('0x{:02X},'.format(c))
	out.write('\n};\n')
	out.flush()

def xz(data):
	return lzma.compress(data, preset=9, check=lzma.CHECK_NONE)

with open(os.path.join('binaries.h'), 'w') as out:
	with open('stub.apk', 'rb') as src:
		binary_dump(src, out, 'manager_xz');
