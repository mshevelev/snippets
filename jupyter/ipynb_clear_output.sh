# @tags: bash, jupyter, ipynb, dev, clear_output

jupyter nbconvert --to notebook  --clear-output ../13f.ipynb

find -name "*.ipynb"  -not -path "*/.*" -and -not -path "*mitx*"   -exec jupyter nbconvert --to notebook  --clear-output {} \;
