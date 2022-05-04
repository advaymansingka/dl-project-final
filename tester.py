import numpy as np

# from tempfile import TemporaryFile
# outfile = TemporaryFile()

# x = np.arange(10)
# np.save(outfile, x)

# _ = outfile.seek(0) # Only needed here to simulate closing & reopening file
# np.load(outfile)

# with open('test.npy', 'wb') as f:
#     np.save(f, np.array([1, 2]))

with open('test.npy', 'rb') as f:
    a = np.load(f)

print(a)