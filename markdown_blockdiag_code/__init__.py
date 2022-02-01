from markdown_blockdiag_code.extension import BlockdiagExtension


def makeExtension(**kwargs):
    return BlockdiagExtension(**kwargs)
