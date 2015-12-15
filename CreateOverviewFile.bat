### Requires GDAL (FW tools installation)

### Create VRT file from list of files:
  
  ## For all files
  gdalbuildvrt overview.vrt *.tif 
  
  
  ## For a list of files
  gdalbuildvrt -input_file_list overviewimages.txt overview.vrt


### Convert VRT file to higher resolution file (8x,16x or 32x original resolution)


-tr xres yres -r nearest



