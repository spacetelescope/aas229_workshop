Working with FITS files
-----------------------

from astropy.io import fits

# astropy.io.fits works also with compressed files
f = fits.open('sip.fits.gz')
# Look at the structure of the file
f.info()
f.close()

# Working with headers
# Opening a fits file using the "with" context manager 
# ensures that the file is closed without explicitely doing so.
with fits.open('sip.fits.gz', mode='update') as f:
    # Updating a keyword
    f[1].header['crpix1']
    f[1].header['crpix1'] = 12
    f[1].header['crpix1']
    
    # Adding a new card
    f[1].header['wcsaxes'] = 2
    f[1].header['wcsaxes'] = (2, "Number of WCS axes")


# Working with image data
f = fits.open('sip.fits')
# Data is a numpy array which points to the data array in the first extension
data = f[1].data
print(data.shape)
print(data.dtype)

# It can be accessed using the (EXTNAME, EXTVER) tuple
data = f[('SCI', 1)].data

# This is really a pointer and if data is changed, the data array in the
# fits file changes as well.

# All operations available to NDArray are applicable to the fits data array.
data[2:10, 3:7]
plt.imshow(data, cmap='gray')
f.close()

# astropy.io.fits provides convenience functions to operate on 
# fits files. These are good for interactive and quick lookup use.
# It is reocmmended to use the OO interface for programming.

data = fits.getdata('sip.fits', ext=1)
print(data.mean())

wcsaxes = fits.getval('sip.fits', keyword="WCSAXES", ext=1)
print(wcsaxes)

fits.setval("sip.fits", keyword="USER", value="UNLNOWN")

print(fits.getval("sip.fits", keyword="user")

fits.delval("sip.fits", keyword="USER")

print(fits.getval("sip.fits", keyword="user")

# Working with FITS tables

# Note: In most cases a FITS table can be read with the table I/O methods.
# This will be discussed later. Here we show an example of usign io.fits for this.

f = fits.open('table.fits')
f[1].data

data = f[1].data
print(data.names)

print(data[1])

print(data.field(""))

Exercise:

# Construct programmatically a FITS file with 1 image extension 
# and save it to disk. Use a numpy array with random numbers as 
# data.
#
# Hints: 
#    A fits file is an instance of fits.HDUList which behaves like a python list.
#    The primary HDU is an instance of fits.PrimaryHDU
#    An image extension is an instance of fits.ImageHDU

# To look at the signature of a python object type
help(fits.ImageHDU)
fits.ImageHDU?






