import argparse # for handling command line arguments
import collections # for container types like OrderedDict
import configparser
import hashlib # for SHA-1
import os
import re
import sys
import zlib # git compresses everything using zlib

argparser = argparse.ArgumentParser(description="The stupid content tracker")

# we don't just call git, we always call git command (init, add, clone)
# hence we need to add subparsers to our arg parser

# dest=command means the command we pass will be stored as a string
# in an attribute called command
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

def main(args = sys.argv[1:]):
    args = argparser.parse_args(argv)

    if args.command == "add"           : cmd_add(args)
    elif args.command == "cat-file"    : cmd_cat_file(args)
    elif args.command == "checkout"    : cmd_checkout(args)
    elif args.command == "commit"      : cmd_commit(args)
    elif args.command == "hash-object" : cmd_hash_object(args)
    elif args.command == "init"        : cmd_init(args)
    elif args.command == "log"         : cmd_log(args)
    elif args.command == "ls-tree"     : cmd_ls-tree(args)
    elif args.command == "merge"       : cmd_merge(args)
    elif args.command == "rebase"      : cmd_rebase(args)
    elif args.command == "rev-parse"   : cmd_rev_parse(args)
    elif args.command == "rm"          : cmd_rm(args)
    elif args.command == "show-ref"    : cmd_show_ref(args)
    elif args.command == "tag"         : cmd_tag(args)
