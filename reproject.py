from astropy.io import fits
from astropy.wcs import WCS
import numpy
#z
print ("Hello")
# Open the reference image and get its WCS info
hdu0 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_0_new.fits')[0]
#Open the image to be reprojected and get its WCS info
hdu1 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_1_new.fits')[0]
hdu2 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_2_new.fits')[0]
hdu3 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_3_new.fits')[0]
hdu4 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_4_new.fits')[0]
from reproject import reproject_interp
##Use reproject_interp to retroject the target image
array, footprint = reproject_interp(hdu1, hdu0.header)
array1, footprint = reproject_interp(hdu2, hdu0.header)
array2, footprint = reproject_interp(hdu3, hdu0.header)
array3, footprint = reproject_interp(hdu4, hdu0.header)
#
##FIX THE NaNs in the output file
arrayfix = numpy.nan_to_num(array)
arrayfix1 = numpy.nan_to_num(array1)
arrayfix2 = numpy.nan_to_num(array2)
arrayfix3 = numpy.nan_to_num(array3)
#
##Output the reprojected image to a new FITS file
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_0_rep.fits',arrayfix, hdu0.header, overwrite=True)

1

fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_1_rep.fits',arrayfix1, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_2_rep.fits',arrayfix2, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_3_rep.fits',arrayfix3, hdu0.header, overwrite=True)
import ccdproc
from astropy import units as u
ccdproc.combine('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_0_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_1_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_2_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_z_3_rep.fits',

output_file='NEP2581_z_combined.fits', method='median',
minmax_clip=True, minmax_clip_min=10, minmax_clip_max=65000,unit=u.adu)
print('goodbye')
#r

print ("Hello")
# Open the reference image and get its WCS info
hdu0 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_0_new.fits')[0]
#Open the image to be reprojected and get its WCS info
hdu1 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_1_new.fits')[0]
hdu2 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_2_new.fits')[0]
hdu3 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_3_new.fits')[0]
hdu4 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_4_new.fits')[0]
from reproject import reproject_interp
##Use reproject_interp to retroject the target image
array, footprint = reproject_interp(hdu1, hdu0.header)
array1, footprint = reproject_interp(hdu2, hdu0.header)
array2, footprint = reproject_interp(hdu3, hdu0.header)
array3, footprint = reproject_interp(hdu4, hdu0.header)
#
##FIX THE NaNs in the output file
arrayfix = numpy.nan_to_num(array)

2

arrayfix1 = numpy.nan_to_num(array1)
arrayfix2 = numpy.nan_to_num(array2)
arrayfix3 = numpy.nan_to_num(array3)
#
##Output the reprojected image to a new FITS file
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_0_rep.fits',arrayfix, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_1_rep.fits',arrayfix1, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_2_rep.fits',arrayfix2, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_3_rep.fits',arrayfix3, hdu0.header, overwrite=True)
import ccdproc
from astropy import units as u
ccdproc.combine('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_0_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_1_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_2_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_r_3_rep.fits',

output_file='NEP2581_r_combined.fits', method='median',
minmax_clip=True, minmax_clip_min=10, minmax_clip_max=65000,unit=u.adu)
print("goodbye")
i
print ("Hello")
# Open the reference image and get its WCS info
hdu0 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_0_new.fits')[0]
#Open the image to be reprojected and get its WCS info
hdu1 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_1_new.fits')[0]
hdu2 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_2_new.fits')[0]
hdu3 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_3_new.fits')[0]
hdu4 = fits.open('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_4_new.fits')[0]

3

from reproject import reproject_interp
##Use reproject_interp to retroject the target image
array, footprint = reproject_interp(hdu1, hdu0.header)
array1, footprint = reproject_interp(hdu2, hdu0.header)
array2, footprint = reproject_interp(hdu3, hdu0.header)
array3, footprint = reproject_interp(hdu4, hdu0.header)
#
##FIX THE NaNs in the output file
arrayfix = numpy.nan_to_num(array)
arrayfix1 = numpy.nan_to_num(array1)
arrayfix2 = numpy.nan_to_num(array2)
arrayfix3 = numpy.nan_to_num(array3)
#
##Output the reprojected image to a new FITS file
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_0_rep.fits',arrayfix, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_1_rep.fits',arrayfix1, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_2_rep.fits',arrayfix2, hdu0.header, overwrite=True)
fits.writeto('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_3_rep.fits',arrayfix3, hdu0.header, overwrite=True)
import ccdproc
from astropy import units as u
ccdproc.combine('/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_0_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_1_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_2_rep.fits,'+\

'/Users/alix/aaa_spyder_301/NEP5281_solved/NEP5281_i_3_rep.fits',

output_file='NEP2581_i_combined.fits', method='median',
minmax_clip=True, minmax_clip_min=10, minmax_clip_max=65000,unit=u.adu)
print("goodbye")
#Once you’ve got all your reprojected images, you can combine them. Remember to combine by filter, and all filters together
import ccdproc
from astropy import units as u

4

print("hello")
ccdproc.combine('/Users/alix/aaa_spyder_301/NEP2581_i_combined.fits,'+\
'/Users/alix/aaa_spyder_301/NEP2581_z_combined.fits,'+\
'/Users/alix/aaa_spyder_301/NEP2581_r_combined.fits',
output_file='deepfield.fits', method='median',
minmax_clip=True, minmax_clip_min=10, minmax_clip_max=65000,unit=u.adu)
print('goodbye')