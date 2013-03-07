#!/usr/bin/env python

""" @package MakeInputFile

Executable script for printing out an example input file with defaults and documentation.
At the current stage, this script simply prints out all of the default options, but in the
future we may want to autogenerate the input file.  This would make everyone's lives much
easier, don't you think? :)
"""

import sys
import re
from forcebalance import parser

def main():
    """ Print out all of the options available to ForceBalance. """
    options = None
    tgt_opts = [None]
    if len(sys.argv) == 2:
        options, tgt_opts = parser.parse_inputs(sys.argv[1])
    out = []
    out.append("# ForceBalance input file generated by MakeInputFile.py")
    out.append("# The octothorpe '#' is a comment symbol")
    out.append("# There are two sections, the main options ($options) and the target options ($target)")
    out.append("# A ForceBalance calculation will have one $options section and as one $target section per optimization target")
    out.append("# The most important options are listed at the top; options are also roughly grouped by their application")
    out.append("# Note: If the specified value is 'None' then the option will truly be set to None - not the string 'None'")
    out.append("# Note: Section option types are more complicated and may require you to read the documentation")
    out.append("# Note: Boolean option types require no value, the key being present implies 'True'")
    out.append("# Note: List option types are specified using spaces as the delimiter - i.e. forcefield ff1.itp ff2.itp ; delete empty brackets before use [] ")
    out.append("")
    out += parser.printsection("$options",options,parser.gen_opts_types)
    for tgt_opt in tgt_opts:
        out.append("\n")
        out += parser.printsection("$target",tgt_opt,parser.tgt_opts_types)
    for line in out:
        print line

if __name__ == "__main__":
    main()
