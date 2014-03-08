
########################################

# in cuda_convnet/data.py:

class DataProvider:
    BATCH_REGEX = re.compile('^data_batch_(\d+)(\.\d+)?$') # to make sure filenames in data_dir are of a certain form
    # [..]
    @staticmethod
    def get_batch_filenames(srcdir):
        return sorted([f for f in os.listdir(srcdir) if DataProvider.BATCH_REGEX.match(f)], key=alphanum_key)

# Explanation
result = re.match(pattern, string)
# is equivalent to
prog = re.compile(pattern)
result = prog.match(string)
# but the latter is more efficient when the expression will be used several times in a single program

########################################


