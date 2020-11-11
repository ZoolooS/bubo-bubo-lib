'''
"Bubo bubo library"

Simple library by Ilya "ZoolooS" Popov

List:
  * 
'''
def bubo_read_and_return_file(rel_path='.', strip='no', split=('no')):
    '''
    Reads text file relative to the executable script.
    Return content from it in 'string' or [list].

    Inputs:
      - rel_path = relative path ['string']. Current directory by default.
      - strip = strip space-symbols from each line of file ['no' | 'left' | 'right' | 'both']. NO by default.
      - split = split by lines into list ['no' | 'yes']. Don't split by default.

    Outputs:
      - String or list (split by something) with all content of file.
    '''
    import os

    content_out = ''


    return content_out