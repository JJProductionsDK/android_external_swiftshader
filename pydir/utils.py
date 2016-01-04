import os
import subprocess
import sys

def shellcmd(command, echo=True):
    if not isinstance(command, str):
        command = ' '.join(command)

    if echo: print '[cmd]', command

    stdout_result = subprocess.check_output(command, shell=True)
    if echo: sys.stdout.write(stdout_result)
    return stdout_result

def FindBaseNaCl():
    """Find the base native_client/ directory."""
    nacl = 'native_client'
    path_list = os.getcwd().split(os.sep)
    if nacl not in path_list:
        return None
    last_index = len(path_list) - path_list[::-1].index(nacl)
    return os.sep.join(path_list[:last_index])

def get_sfi_string(args, sb_ret, nonsfi_ret, native_ret):
    """Return a value depending on args.sandbox and args.nonsfi."""
    if args.sandbox:
        assert(not args.nonsfi)
        return sb_ret
    if args.nonsfi:
        return nonsfi_ret
    return native_ret
