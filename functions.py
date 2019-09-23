import os
from IPython.display import Markdown

def tree(address='.',
         none=('__pycache__',
               '__init__.py',
               '.git',
               '.ipynb_checkpoints',
               '.vscode',)):
    '''Return a tree view of the directory 'address' as a Markdown view,
    avoiding the list 'none' of files/directories.'''
    to_mark = ''

    for root, dirs, files in os.walk(address):
        test = [sub in none for sub in root.split(os.sep)]
        if sum(test):
            continue
            
        level = root.replace(address, '').count(os.sep) -1
        indent = '&ensp;' * 4 * (level)
        subindent = '&ensp;' * 4 * (level + 1)
        base = os.path.basename(root)
        
        if root != address:
            to_mark += f'{indent}{base}/<br/>'
        
        for f in files:
            if f not in none:
                to_mark += f'{subindent}[{f}](../edit/{root}/{f})<br/>'
            
    return Markdown(to_mark)