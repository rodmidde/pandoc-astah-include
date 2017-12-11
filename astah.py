#!/usr/bin/env python

"""
Astah filter to process code blocks with class "ashah" into images.

Needs `astah-community.jar and dependencies`.
"""

import os
import shutil

from subprocess import call

from pandocfilters import toJSONFilter, Para, Image, get_caption


def get_filepaths_by_index(topdir, exten, idx):
    filelist = []
    for root, directories, filenames in os.walk(topdir):
        for filename in filenames:
            if filename.lower().endswith(exten):
                fullname = os.path.join(root, filename)
                filelist.append( fullname )
    filelist.sort()

    return filelist[idx]


def clear_dir(dirPath):
    for root, dirs, files in os.walk(dirPath):
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


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
                        clear_dir(output_dir)

                        call(["java", "-Djava.awt.headless=true", "-Dcheck_jvm_version=false", "-cp",
                              "astah/astah-community.jar", "com.change_vision.jude.cmdline.JudeCommandRunner", "-image",
                              "all", "-resized", "-f", kv["file"], "-t", kv["format"], "-o", output_dir])

                        dest = get_filepaths_by_index(output_dir, kv["format"], int(kv["index"]))

        return Para([Image([ident, [], keyvals], caption, [dest, typef])])


if __name__ == "__main__":
    toJSONFilter(astah)
