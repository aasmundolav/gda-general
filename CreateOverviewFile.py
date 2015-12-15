### Requires GDAL (FW tools installation)


### Create VRT file from list of files:
  
  ## For all files
  gdalbuildvrt overview.vrt *.tif 
  
  
  ## For a list of files
  gdalbuildvrt -input_file_list overviewimages.txt overview.vrt




### Convert VRT file to higher resolution file (8x,16x or 32x original resolution)
gdal_translate -tr xres yres -r nearest -co "TILED=YES" -co "BIGTIFF=IF_NEEDED" -co "COMPRESS=LZW" inputfile.tif outputfile.tif 



