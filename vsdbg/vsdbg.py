import debugpy

PORT = 5678

def dbg(port=PORT, wait=True):
    debugpy.listen(port)
    if wait:
        print('VSDBG: Waiting for Debug Session to Continue...')
        debugpy.wait_for_client()
