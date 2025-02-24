import textnode
import parsemarkdown
import blocktype
import markdown_parser
import subprocess
import sys

def main():

    subprocess.call(['sh', './prep_public.sh'])

if __name__ == "__main__": 
    main()