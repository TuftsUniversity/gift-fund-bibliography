import pybtex.bibtex as pb1
import pybtex
from pybtex.database import parse_file
import subprocess


pb = pb1.BibTeXEngine()
pb.make_bibliography('biblio.aux', style='chicago')

commandLine = subprocess.Popen(['pdflatex', 'biblio.tex'])

commandLine.communicate()
