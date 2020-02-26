#! usr/bin/env python3

# mcb.pyw - Save and loads pieces of text to the clipboard.
# Usage: py3 mcb.pyw save <keyword> - Save clipboard to keyword.
#        py3 mcb.pyw <keyword> -Loads keyword to clipboard.
#        py3 mcb.pyw list - Loads all keywords to clipboard
#        py3 mcb.pyw delete <keyword> - delete keyword from shelf
#        py3 mcb.pyw delete- delete all keys from shelf

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')
# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower == 'delete':
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    
# TODO: List keywords and load content.

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
       # for i in list(mcbShelf.keys()):
            #del mcbShelf[i]
       mcbShelf.clear()
       print('all data have been deleted!')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

#print(sys.argv[0] + ' ' + sys.argv[1] + ' ' +sys.argv[2])
