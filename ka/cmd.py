#!/usr/bin/env python

"""Collection of custom shortcut commands to use either as shell commands or as python functions.

    Usage:
        ./cmd.py ( run   | r )  <subcmd> [<args>...]
        ./cmd.py ( shell | s )  <subcmd> [<args>...]
        ./cmd.py ( term  | t )           [<args>...]
        ./cmd.py ( edit  | e )           [<args>...]
        ./cmd.py ( fmgr  | f )           [<args>...]
        ./cmd.py [-h | --help | -v | --version]

    Options:
        -h, --help         Print the help page
        -v, --version      Print the version number

    Commands:
        run:               Run given command in new process (and return immediately).
        shell:             Run given command, wait for it, then print its output.
        term:              Run the default terminal emulator in new process.
        edit:              Run the best text editor (or open a file in existing instance).
        fmgr:              Run the best file manager (or open a directory in existing instance).


    Convenient way to use it from shell level is to use symbolic links created
    in 'bin' subdirectory. Then name of the symlink select the command/function,
    so user doesn't have to specify it again.

    For example, these commands do the same:
        $ ./cmd.py run xclock
        $ ./bin/run xclock
        $ ./bin/r xclock

    Next example:
        $ ./cmd.py edit -d file1.py file2.py file3.py 
        $ ./bin/edit -d file1.py file2.py file3.py 
        $ ./bin/e -d file1.py file2.py file3.py 

    Next example:
        $ ./cmd.py shell cat cmd.py | grep gr
        $ ./bin/shell cat cmd.py | grep gr
        $ ./bin/s cat cmd.py | grep gr

"""

from docopt import docopt



import sys
import subprocess
import os.path

def run(cmd, args=[]):
    """Run given command in new process (and returns immediately)

    Examples:
    run("xclock")
    run("xterm")  - spawns new xterm in act. directory
    run("xterm", ["-e", "ipython"])
    """

    subprocess.Popen([cmd] + args)

def shell(cmd):
    """Run given command using system shell, wait for it, and return a string with its output.

    cmd - string command 
    Examples:
    print shell("ls -a")
    print shell("ls -a | grep bla")
    """
    return subprocess.check_output(cmd, shell=True)

def term(args):
    """Run the default terminal emulator in new process."""
    run("x-terminal-emulator", args)

def is_vim_running(servername):
    servers = shell("vim --serverlist").split('\n')
    return servername in servers
    

def edit(args):
    """Run the best text editor (or open a file in existing instance)."""
    if is_vim_running("EDITOR"):
        if args:
            run("gvim", ["--servername", "EDITOR", "--remote"] + args)
        else:
            raise Exception("Editor is already running! (and no file to open provided)")
    else:
        run("gvim", ["--servername", "EDITOR"] + args)
 

def fmgr(args):
    """Run the best file manager (or open a directory in an existing instance)."""
    raise NotImplementedError



#shortcut function names
r = run
s = shell
t = term
e = edit
f = fmgr


def main(argv):

    argv[0] = os.path.basename(argv[0])

    if argv[0] in ["cmd", "cmd.py"]:
        argv = argv[1:]

    argdict = docopt(__doc__, argv=argv, version='ka.cmd 0.2', options_first=True)

    if __debug__:
        print "arguments:", argdict #TODO: remove

    if   argdict['run'] or argdict['r']:
        run(argdict['<subcmd>'], argdict['<args>'])
    elif argdict['shell'] or argdict['s']:
        out = shell(argdict['<subcmd>'] + argdict['<args>'].join(' '))
        if out:
            print out
    elif argdict['term'] or argdict['t']:
        term(argdict['<args>'])
    elif argdict['edit'] or argdict['e']:
        edit(argdict['<args>'])
    elif argdict['fmgr'] or argdict['f']:
        fmgr(argdict['<args>'])

if __name__ == '__main__':
    main(sys.argv)


