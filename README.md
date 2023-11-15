# PDF Compressor

This Python script compresses PDF files using Ghostscript. 

## Usage

```
pdf_compress.py [-h] [-o OUTPUT] [-d DPI] [-v] input_files [input_files ...]
```

**Positional Arguments:**

`input_files` - Input PDF files to compress.

**Optional Arguments:**

`-h, --help` - Show help message and exit.

`-o, --output OUTPUT` - Output PDF file. If not specified, appends _compressed to input filename.

`-d, --dpi DPI` - DPI preset for compression (72, 150, 300). Default is 300. See [this link](https://askubuntu.com/q/113544) for an explanation of presets.

`-v, --verbose` - Verbose output.


Here is how you can update the README.md to include instructions for calling the pdf_compress script from anywhere on your computer:

## Usage

**Calling from anywhere**

To be able to call `pdf_compress` from any directory, you need to add it to your PATH.

On Linux/macOS, add the following to your ~/.bash_profile or ~/.bashrc:

```
export PATH="$PATH:/path/to/pdfcompress"
```

On Windows, add pdf_compress's folder path to the System PATH variable.

Now you can run the script simply as:

```
pdf_compress.py [options] input_files
```

from any terminal/command prompt.




## Examples

Compress a single file:

```
pdf_compress.py report.pdf
```

Compress multiple files with custom output:

```  
pdf_compress.py report1.pdf report2.pdf -o compressed.pdf
```

Compress with 150 dpi setting:

```
pdf_compress.py paper.pdf -d 150
```

## About

Uses Ghostscript to losslessly compress PDFs by optimizing them for different use cases. Lower DPI options result in smaller file sizes.

See the help messages and linked askubuntu post for more details on usage.
