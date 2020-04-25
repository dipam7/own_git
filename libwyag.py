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

# abstraction for a git repository
class GitRepository(object):
    """A git repository"""
    # a git repo contains 2 things, worktree which is the folder we want to apply version control on
    # and a .git repo where git stores its own things
    # the config file is stored in .git/config

    worktree = None
    gitdir = None
    conf = None
    
    # an additional force parameter to disable checks
    def __init__(self, path, force=False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")
        
        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a git repository %s" % path)
        
        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")
        
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion %s " %vers)



# we will be doing a lot of path manipulations hence we will write some utility functions
def repo_path(repo, *path):
    """Compute path under repo's gitdir"""
    return os.path.join(repo.gitdir, *path)


def repo_file(repo, *path, mkdir=False):
    """Same as repo_path, but creates dirname(*path) if absent. For example repo_file(r, "refs", "remotes", "origin")
    will create .git/refs/remotes."""

    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)

def repo_dir(repo, *path, mkdir=False):
    """Same as repo_path, but mkdir *path if absent if mkdir"""

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception("Not a directory %s" % path)

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None
















