import os

path = os.getenv('HOME') + '/Library/Application Support/JetBrains/Toolbox/apps/PyCharm-P/ch-0'

def walk(top, maxdepth):
    dirs, nondirs = [], []
    for name in os.listdir(top):
        (dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
    yield top, dirs, nondirs
    if maxdepth > 1:
        for name in dirs:
            for x in walk(os.path.join(top, name), maxdepth-1):
                yield x

max_mtime = 0
max_file = ''
for (dirname, subdirs, files) in walk(path, 2):
    if (dirname == path):
        continue
    for fname in subdirs:
        extension = os.path.splitext(fname)[1]
        if (extension != '.app'):
            continue
        full_path = os.path.join(dirname, fname)
        mtime = os.stat(full_path).st_mtime
        if mtime > max_mtime:
            max_mtime = mtime
            max_file = os.path.join(dirname, fname)

import subprocess
subprocess.call(
        ["/usr/bin/open", max_file]
        )
