# source2utils vmat fix
For porting maps from source 1 to source 2 using [bspsrc](https://github.com/ata4/bspsrc) and [source2utils](https://github.com/caseytube/source2utils)

## What's this?
source2util's vmt-to-vmat utility has the issue of assigning missing/invalid TextureDetail parameters to converted vmat files. [You'd previously have to manually fix these invalid parameters](https://youtu.be/RL_bVZHRm4s?t=689) by assigning the TextureColor value to TextureDetail.
This can be used in chain with source2util to do this automatically.

## Requirements:
- Python

## Usage:
- drag & drop the converted materials folder (the one which has .vmat files) into run.py, which will scan all subfolders and fix the vmat files.
- or execute `run.py "<path-to-folder>"`

### Before:
![Before](https://i.imgur.com/dkY2w11.png)
### After:
![After](https://i.imgur.com/ZBShjXZ.png)
*This tool does not fix texture scales and positions. You still have to do that manually.*
