#!/usr/bin/env python

"""
Astah filter to process code blocks with class "ashah" into images.

Needs `astah-community.jar and dependencies`.
"""

import os
import sys
from subprocess import call

from pandocfilters import toJSONFilter, Para, Image, get_filename4code, get_caption, get_extension

def get_filepaths_by_index(topdir, exten, idx):
    files = []
    count = 0
    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().endswith(exten):
                if count == idx:
                    return os.path.join(dirpath, name)
                else:
                    count += 1

def clear_dir(dirPath, exten):
    if (os.path.exists(dirPath)):
        filelist = [ f for f in os.listdir(dirPath) if f.endswith(exten) ]
        for f in filelist:
            os.remove(os.path.join(mydir, f))

def astah(key, value, format, _):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        kv = {key: value for key, value in keyvals}

        if "astah" in classes:
            caption, typef, keyvals = get_caption(keyvals)

            if "file" in kv:
                if "format" in kv:
                    if "index" in kv:
                        output_dir = "astah-generated-files"
                        clear_dir(output_dir, kv["format"])

                        call(["java", "-Djava.awt.headless=true", "-Dcheck_jvm_version=false", "-cp", "astah/astah-community.jar", "com.change_vision.jude.cmdline.JudeCommandRunner", "-image", "all", "-resized", "-f", kv["file"], "-t", kv["format"], "-o", output_dir])

                        dest = get_filepaths_by_index(output_dir,kv["format"],int(kv["index"]))

        return Para([Image([ident, [], keyvals], caption, [dest, typef])])

if __name__ == "__main__":
    toJSONFilter(astah)
