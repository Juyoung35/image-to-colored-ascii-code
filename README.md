# image-to-colored-ascii-code
This program converts image file to ascii code texts such as .txt, .rtf, .docs, .html

## Blueprint
input by command line
---------------------
Usage: python main.py SOURCE [s=SCALE] [d=DEST] [f=FORMAT]  
This program converts SOURCE image file to output file named DEST with FORMAT extension with resized scale by SCALE.  
  
OPTION:  
  -s, --scale=SCALE					resize SOURCE image file by SCALE. if not given, size will be same.
  -d, --dst, --destination=DEST		set output file name with DEST.
  -f, --format=FORMAT				set output file format. if not given, format will be same.
  
If FORMAT is raw text-like format that doesn't support colored text, it just return output from grayscale of input file.  
If DEST and FORMAT are not given, then it will return output with slightly different name with source file.  
Available FORMAT: .txt, .docx, .rtf, .html

# Image Reference
Sample Image 0: sample-image-0.jpg by [Sharon Pittaway](https://unsplash.com/photos/iMdsjoiftZo?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
Sample Image 1: sample-image-1.png in [site](https://www.pngkey.com/maxpic/u2t4y3q8q8q8u2a9/)

# Source Code Reference
- [python pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- [python pillow resampling filters](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-filters)
- [RTF simple tutorial](http://www.pindari.com/rtf1.html)
- [youtube Easy Python PIL Tutorial](https://www.youtube.com/watch?v=v_raWlX7tZY&ab_channel=Kite)

# get output file with cli
- sample-image-0.txt: `python run.py input/sample-image-0.jpg -s 0.04 -d output/sample-image-0 -f txt`
- sample-image-0.rtf: `python run.py input/sample-image-0.jpg -s 0.08 -d output/sample-image-0 -f rtf -p 8 -rs LANCZOS -fs 2`
- sample-image-1.txt: `python run.py input/sample-image-1.png -s 0.04 -d output/sample-image-1 -f txt`
- sample-image-1.rtf: `python run.py input/sample-image-1.png -s 0.08 -d output/sample-image-1 -f rtf -p 8 -rs LANCZOS -fs 2`
