#!/usr/bin/env python

"""Collection of my custom commands to use either as shell commands or as python functions.

    This script is not really prepared to run on other systems than mine.
    If you want to use it, you should review and adjust the content of this file first.

    Usage:
        cmd ( run     | r  )  <subcmd> [<args>...]
        cmd ( shell   | s  )  <subcmd> [<args>...]
        cmd ( term    | t  )           [<args>...]
        cmd ( edit    | e  )  <file>
        cmd ( diff    | d  )  <file1> <file2> [<file3>]
        cmd ( fmgr    | f  )  <dir>
        cmd ( fehback | fb )  <dir>
        cmd [-h | --help | -v | --version]

    Options:
        -h, --help         Print the help page
        -v, --version      Print the version number

    Commands:
        run:               Run given command in new process (and return immediately).
        shell:             Run given command, wait for it, then print its output.
        term:              Run the default terminal emulator in new process.
        edit:              Run the best text editor (or open a file in existing instance).
        diff:              Run the best text editor in diff mode.
        fmgr:              Run the best file manager (or open a directory in existing instance).
        fehback:           Set two random background images for two screens (using the "feh" app)


    Convenient way to use it from shell level is to create some symlinks to it with
    names equal to command names like:
        $ ln -s cmd.py run
        $ ln -s cmd.py r
        $ ln -s cmd.py shell
        $ ln -s cmd.py s
        etc...
    Then the name of the symlink select the command/function,
    so user doesn't have to specify it again.

    For example, these commands do the same:
        $ ./cmd.py run xclock
        $ ./run xclock
        $ ./r xclock

    Next example:
        $ ./cmd.py edit ~/.bashrc
        $ ./edit ~/.bashrc
        $ ./e ~/.bashrc

    Next example:
        $ ./cmd.py shell cat cmd.py | grep gr
        $ ./shell cat cmd.py | grep gr
        $ ./s cat cmd.py | grep gr

"""

VERSION='0.2'

try:
    from docopt import docopt
except ImportError:
    print 'This script needs a "docopt" module (http://docopt.org)'
    raise



import sys
import subprocess
import os
import random

def exp(path):
    """Expand shell variables, and user shortcuts (~ or ~user)"""
    if not path:
        return path
    return os.path.expandvars(os.path.expanduser(path))

def run(cmd, *args):
    """Run given command in new process (and returns immediately)

    Examples:
    run("xclock")
    run("xterm")  - spawns new xterm in act. directory
    run("xterm", "-e", "ipython")
    """

    subprocess.Popen([cmd] + list(args))

def shell(cmd):
    """Run given command using system shell, wait for it, and return a string with its output.

    cmd - string command 
    Examples:
    print shell("ls -a")
    print shell("ls -a | grep bla")
    """
    return subprocess.check_output(cmd, shell=True)

def term(*args):
    """Run the default terminal emulator in new process."""
    run("x-terminal-emulator", *args)

def is_vim_running(servername):
    servers = shell("vim --serverlist").split('\n')
    return servername in servers
    

def edit(filename, vimexecname="gvim", vimservername="EDITOR", addfilenames=[]):
    """Run the best text editor (or open a file in existing instance)."""

    cmd = [vimexecname, "--servername", vimservername]
    if is_vim_running(vimservername):
        cmd.append("--remote")
    cmd.append(filename)
    for afn in addfilenames:
        cmd.append(afn)
    run(*cmd)

    #TODO: activate editor window if under qtile
 

def diff(filename1, filename2, filename3=None):
    addfilenames = [filename2]
    if filename3:
        addfilenames.append(filename3)
    edit(
        filename=filename1,
        vimexecname="gvimdiff",
        vimservername="DIFF",
        addfilenames=addfilenames
    )

    #TODO: activate diff window if under qtile
 

def fmgr(dirname):
    """Run the best file manager (or open a directory in an existing instance)."""
    if os.path.isfile(dirname):
        dirname = os.path.dirname(dirname)
    edit(dirname, vimservername="FILEMANAGER")

    #TODO: activate fmgr window if under qtile


def fehback(dirname):
    filenames = [f for f in os.listdir(dirname) if f[-3:] == "jpg"]
    filenames = random.sample(filenames, 2)
    filenames = [os.path.join(dirname, f) for f in filenames]
    run("feh", "--bg-fill", *filenames)


#shortcut function names
r = run
s = shell
t = term
e = edit
d = diff
f = fmgr
fb = fehback


def main():
    argv = sys.argv[:]

    argv[0] = os.path.basename(argv[0])

    if argv[0] in ["cmd", "cmd.py"]:
        argv = argv[1:]

    argdict = docopt(__doc__, argv=argv, version=VERSION, options_first=True)

    if __debug__:
         "arguments:", argdict #TODO: remove

    if   argdict['run'] or argdict['r']:
        run(argdict['<subcmd>'], *argdict['<args>'])
    elif argdict['shell'] or argdict['s']:
        out = shell(argdict['<subcmd>'] + ' ' + ' '.join(argdict['<args>']))
        if out:
            print out
    elif argdict['term'] or argdict['t']:
        term(*argdict['<args>'])
    elif argdict['edit'] or argdict['e']:
        edit(exp(argdict['<file>']))
    elif argdict['diff'] or argdict['d']:
        diff(exp(argdict['<file1>']), exp(argdict['<file2>']), exp(argdict['<file3>']))
    elif argdict['fmgr'] or argdict['f']:
        fmgr(exp(argdict['<dir>']))
    elif argdict['fehback'] or argdict['fb']:
        fehback(exp(argdict['<dir>']))


if __name__ == '__main__':
    main()


