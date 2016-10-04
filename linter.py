from cuda_lint import Linter, util
import os

_exe = os.path.join(os.path.dirname(__file__), 'lua_bin', 'luac53')

class Lua(Linter):
    """Provides an interface to luac -p."""

    syntax = 'Lua'
    cmd = (_exe, '-p', '*', '-')
    regex = r'^.+?:.+?:(?P<line>\d+): (?P<message>.+?(?:near (?P<near>\'.+\')|$))'
    error_stream = util.STREAM_STDERR
