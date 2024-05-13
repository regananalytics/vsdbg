try:
    from os import getenv
    from .vsdbg import dbg
    var = getenv("VSDBG", None)
    if var is not None:
        try:
            dbg(int(var))
        except:
            dbg()
except:
    pass