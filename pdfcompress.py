#!/usr/bin/python3

import sys
import subprocess

def get_pdf_settings(dpi):
  if dpi == 72: 
    return '/screen'
  elif dpi == 150:
    return '/ebook'
  elif dpi == 300:
    return '/printer'
  else:
    return '/default'

def compress_pdf(input_file, output_file, dpi=300):
  pdf_settings = get_pdf_settings(dpi)
  
  args = ['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
          f'-dPDFSETTINGS={pdf_settings}', '-dNOPAUSE', '-dQUIET', '-dBATCH',  
          f'-sOutputFile={output_file}', input_file]
  
  subprocess.run(args)

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Compress PDF files using Ghostscript')

  parser.add_argument('input_files', nargs='+', 
                      help='Input PDF files to compress')

  parser.add_argument('-o', '--output', 
                      help='Output PDF file. If not specified, appends _compressed to input filename')

  parser.add_argument('-d', '--dpi', type=int, default=300,
                      help='DPI preset for compression (72, 150, 300). Default is 300. See https://askubuntu.com/q/113544 for an explanation of presets.')

  parser.add_argument('-v', '--verbose', action='store_true',
                      help='Verbose output')

  args = parser.parse_args()

  if len(args.input_files) > 1 and args.output:
    print("Error: Multiple input files specified, but only one output file provided.")
    print("Please provide separate output files when compressing multiple inputs.")
    sys.exit(1)

  for input_file in args.input_files:
    if args.output:
      output_file = args.output 
    else:
      output_file = f'{input_file.rsplit(".", 1)[0]}_compressed.pdf'

    compress_pdf(input_file, output_file, args.dpi)
    
    if args.verbose:
      print(f'Compressed {input_file} to {output_file}')