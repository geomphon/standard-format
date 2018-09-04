import pandas as pd

class StandardFormatError(RuntimeError):
    pass

def content_keys(data_frame):
	'''
        # FIXME DOC
	Find all colummns name which don't start with an underscore
	:param data_frame: the DataFrame to analyse.
	:type data_frame: DataFrame
	:return: the list of all meta keys of the DataFrame
	:rtype: string array
	'''
	return [x for x in data_frame if x[0] != '_']

def meta_keys(data_frame):
	'''
        # FIXME DOC
	Find all colummns name which don't start with an underscore
	:param data_frame: the DataFrame to analyse.
	:type data_frame: DataFrame
	:return: the list of all meta keys of the DataFrame
	:rtype: string array
	'''
	return [x for x in data_frame if x[0] == '_']

def unmunge(keys):
    '''
    # FIXME doc
    '''
    # FIXME - RISKS CAUSING DUPLICATES
    unmunge = lambda x: x[1:] if (x[0] == '_') else x
    return [unmunge(key) for key in keys]

def munge(x):
    '''
    # FIXME doc
    '''
    if x[0] != '_':
        return '_' + x
    return x

def munge_all(keys):
    '''
    # FIXME doc
    '''
    return [munge(key) for key in keys]

def munge_df(data_frame):
    '''
    # FIXME doc
    '''
    old_colnames = data_frame.columns.tolist()
    new_colnames = munge_all(old_colnames)
    return data_frame.rename(columns=dict(zip(old_colnames, new_colnames)))

def format_valid(data_frame):
    '''
    # FIXME doc
    '''
    if '' in data_frame:
        raise StandardFormatError(
                "Invalid format: column names must not be empty")
    return None

def content(data_frame):
    '''
    # FIXME doc
    '''
    return data_frame.loc[:,content_keys(data_frame)]

def content_unique(data_frame):
    '''
    # FIXME doc
    '''
    return content(data_frame).drop_duplicates().reset_index(drop=True)

def meta(data_frame):
    '''
    # FIXME doc
    '''
    return data_frame.loc[:,meta_keys(data_frame)]

def meta_unique(data_frame):
    '''
    # FIXME doc
    '''
    return meta(data_frame).drop_duplicates().reset_index(drop=True)

def read(filename):
    '''
    # FIXME doc
    '''
    try:
        df_result = pd.read_feather(filename)
    except Exception:
        pass
    try:
        df_result = pd.read_csv(filename)
    except pd.errors.ParserError:
        raise StandardFormatError(
"""Unknown file format: file must be in feather or CSV
format""".replace('\n', ' ')
        )
    except Exception as e:
        raise StandardFormatError(e)
    format_valid(df_result)
    return df_result



