def attention(string):
    ret = f"""
    #############################
    !!!!!!!
    {string} 
    !!!!!!!    
    #############################
    """
    return ret

def log_getcwd():
    import os
    attention(f'{os.getcwd()}')

hello = """
################################################################################
################################################################################
                # #  ###  #   #   ###    # #  ###  #   #   ###
                ###  ##   #   #   # #    ###  ##   #   #   # #
                # #  ###  ##  ##  ###    # #  ###  ##  ##  ###
################################################################################
################################################################################
"""