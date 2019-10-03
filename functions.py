def tree(address='.',
         none=('__pycache__',
               '__init__.py',
               '.git',
               '.ipynb_checkpoints',
               '.vscode'),
         mark=True):
    '''Return a tree view of the directory 'address' as a Markdown view,
    avoiding the list 'none' of files/directories.'''
    import os
    from IPython.display import Markdown
    
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
            
    if mark: 
        return Markdown(to_mark)
    else:    
        return to_mark.replace('<br/>','\n').replace('&ensp;','\t')


def sed(search, insert, file):
    '''Insert line after each search in a file.
    '''
    with open(file, 'r+', encoding="utf-8") as fd:
        contents = fd.readlines()
        if search in contents[-1]:  # Handle last line to prevent IndexError
            contents.append(insert)
        else:
            for index, line in enumerate(contents):
                if search in line and insert not in contents[index + 1]:
                    contents.insert(index + 1, insert)
        fd.seek(0)
        fd.writelines(contents)
        
        
def create(file, text):
    '''Create a file or overwrite it.'''
    with open(file, 'w+', encoding="utf-8") as f:
        f.write(text)
        

def replace(search, replace, file):
    '''Replace search in a file.
    '''
    import fileinput
    
    for line in fileinput.FileInput(file, inplace=1):
        if search in line:
            line = line.replace(search,replace)
        print(line, end='')