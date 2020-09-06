#!/usr/bin/env python
"""
Use this script to convert all *.py files to jupyter notebook format
"""

#%%
from pathlib import Path
import logging
logging.getLogger().setLevel(logging.INFO)
import shutil
from pprint import pprint
#%%
# Get the IPython script root dir
root_dir = Path.cwd()
# path_ipy_root=root_dir / "src_process"
path_ipy_root=root_dir / "src_collect"
path_kernel_script_out=root_dir / "out" / "kernel.py"
assert path_ipy_root.exists()

#%% Iterate over files inside the folders
kernel_files = list()
for path_pyfile in path_ipy_root.glob("*.py"):
    pyfile = path_pyfile.stem
    if pyfile == '__init__':
        continue
    pyfile_labels = pyfile.split('_')
    # print(pyfile_labels)
    if not len(pyfile_labels) >= 2:
        continue
    logging.info("Adding {} to kernel".format(path_pyfile))
    # print(path_pyfile)
    kernel_files.append((pyfile.split('_').pop(0), path_pyfile))

#%% Sort the result
kernel_files = sorted(kernel_files)

#%% Print
print("*** Kernel manifest ***")
print(path_ipy_root)
for k in kernel_files:
    print("\t", k[1].stem)

#%% Append all python files to a single script

script_lines = list()

for f in kernel_files:
    this_file = f[1]
    with this_file.open() as fh:
        lines = fh.readlines()
        # Concatenate
        script_lines += lines
        logging.info("Added {:5} lines from {}".format(len(lines),this_file.stem))

#%%
with path_kernel_script_out.open('w') as fh:
    fh.writelines(script_lines)
logging.info("Wrote {}".format(path_kernel_script_out))

