# @tags: bash, ipynb, jupyter, dev

!find /home/mshevelev/git -name ".*" -type d  -prune -o -name "*.ipynb" -print0 | xargs -0 ls -lt | head -10
