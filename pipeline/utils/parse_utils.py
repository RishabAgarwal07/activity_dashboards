from config.config import D, GPXTPX


def xml_setup():
    # Namespaces from YOUR file
    ns = {
        "d": D,
        "gpxtpx": GPXTPX
    }
    return ns
