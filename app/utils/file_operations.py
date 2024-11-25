import os
import shutil


def create_temp(path):
    """
    This function creates a temporary directory if it does not already exist.

    Parameters:
    None.

    Returns:
    None. The function creates a directory at the path specified by the argument.
    If the directory already exists, the function does nothing.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def remove_temp(path):
    """
    This function deletes the temporary directory.

    Parameters:
    None.

    Returns:
    None. The function deletes the directory at the path specified by the argument.
    """
    shutil.rmtree(path)
