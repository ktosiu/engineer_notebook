#! /usr/bin/python

import pypandoc
import glob

md = glob.glob('*.md')

for f in md:
	z = pypandoc.convert(f,'rst',format='markdown')
	fname = f.split('.')[0] + '.rst'
	with open(fname,'w') as outfile:
		outfile.write(z)