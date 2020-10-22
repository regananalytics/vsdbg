import debugpy

def dbg(port=5678):
    debugpy.listen(port)
    debugpy.wait_for_client()