#!/usr/bin/env python
"""
Extract SMTP messages from multiple archive files in source directory
into distinct mbox files in target directory.

This is a convenient wrapper around the "formail" tool.

Install::

    pip install delegator.py

Synopsis::

    python formailx.py /var/lib/spamarchive/artinvoice /var/lib/spamarchive/mbox
"""
import os
import sys
import glob
import delegator

def scan_directory(path):
    for filename in glob.iglob(os.path.join(path, '*'), recursive=True):
        yield filename

def process_all(source, target):
    for infile in sorted(scan_directory(source)):
        name = os.path.basename(infile).replace('.gz', '')
        outdir = os.path.join(target, name)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        outfile = os.path.join(outdir, 'mbox'.format(name))
        try:
            print('INFO:  Processing file "{infile}"'.format(infile=infile))
            process_item(infile, outfile)
        except Exception as ex:
            print('ERROR: Processing file "{infile}" failed. {ex}'.format(infile=infile,ex=ex))

def process_item(infile, outfile):
        command = u"cat '{infile}' | gunzip | formail -ds sh -c 'cat > {outfile}.$FILENO'".format(infile=infile, outfile=outfile)
        process = delegator.run(command)
        if process.return_code != 0:
            print('ERROR: Processing command "{command}" failed'.format(command=command))

def run(source, target):
    print('INFO:  Extracting all messages from "{}" into mbox files in "{}"'.format(source, target))
    process_all(source, target)

if __name__ == '__main__':
    source = sys.argv[1]
    target = sys.argv[2]
    run(source, target)
