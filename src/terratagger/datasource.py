import glob
import os
import numpy as np

class NPZDirectorySource:
    def __init__(self, input_dir, extension, fields):
        self.files = glob.glob(os.path.join(input_dir, extension))
        self.extension = extension
        self.fields = fields

    def __getitem__(self, index):
        return self.get(index)

    def __len__(self):
        return len(self.files)

    def get(self, index):
        data = np.load(self.files[index])
        patch = dict((field, data[field]) for field in self.fields)
        for field in patch:
            median_val = np.nanmedian(patch[field])
            patch[field][np.isnan(patch[field])] = median_val
        return patch

if __name__ == '__main__':
    pass
