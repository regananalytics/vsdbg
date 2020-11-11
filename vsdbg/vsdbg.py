import debugpy

PORT = 5678

def dbg(port=PORT, wait=True):
    debugpy.listen(port)
    if wait: debugpy.wait_for_client()