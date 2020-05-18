import os


def get_filetype(filename):
    """
    Gets the filetype of an object based on the extension in its filename

    Args:
        filename (str): The name of the file
    Returns:
        str: The filetype of the file
    """
    filetype = os.path.splitext(filename)[-1][1:].lower()
    return filetype


def clean_folder(folder):
    if folder and not folder.endswith('/'):
        folder += '/'

    return folder


def clean_path(path):
    """
    Creates and cleans an S3 path based on a provided folder and filename.

    Args:
        folder (str): The folder portion of a full S3 path
        filename (str): The filename portion of a full S3 path
    Returns:
        str: The full, cleaned S3 path
    Raises:
        ValueError: If good path writing conventions are not followed
    """
    if '//' in path:
        raise ValueError('Double-forward slashes (\'//\') are not permitted '
                         'by river. Use \'river.read_badpractice_file\' '
                         'if reading such a file is necessary.')

    if path.find('.') < path.rfind('/'):
        raise ValueError('Period characters (\'.\') are not permitted '
                         ' by river except in file extensions.')
    return path


def clean_bucket(bucket):
    """
    Cleans an S3 bucket string to ensure that functionality works regardless
    of certain user behavior (e.g. including 's3://' in the bucket string)

    Args:
        bucket (str): The name of an S3 bucket

    Returns:
        str: The cleaned S3 bucket name
    """
    # if '.' in bucket:
    #     raise ValueError('Period characters (\'.\') are not permitted '
    #                      'by river. Use \'river.read_badpractice_file\' '
    #                      'if reading such a file is necessary.')
    prefix = 's3://'
    if bucket.startswith(prefix):
        bucket = bucket[len(prefix):]
    return bucket
