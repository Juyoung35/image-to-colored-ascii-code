# image-to-colored-ascii-code
This program converts image file to ascii code texts or colored ascii code image

## Blueprint
input by command line
---------------------
Usage: python main.py SOURCE [DEST] [FORMAT]  
This program converts SOURCE image file to output file named DEST with FORMAT extension.  
  
If FORMAT is raw text-like format that doesn't support colored text, it just return output from grayscale of input file.  
If DEST and FORMAT are not given, then it will return output with slightly different name with source file.  
Available FORMAT: .png, .jpg, .jpeg, .txt, .docx, .rtf  
