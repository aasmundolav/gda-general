### Requires GDAL (FW tools installation)


### Create VRT file from list of files:
  
  ## For all files
  gdalbuildvrt overview.vrt *.tif 
  
  
  ## For a list of files
  gdalbuildvrt -input_file_list overviewimages.txt overview.vrt




### Convert VRT file to higher resolution file (8x,16x or 32x original resolution)
gdal_translate -tr xres yres -r nearest -co "TILED=YES" -co "BIGTIFF=IF_NEEDED" -co "COMPRESS=LZW" overview.vrt overviewfile.tif 

### Examples  ## PROBLEM WITH DTM NODATA
    #1
    G:\G\ST_GIS_Data_01\RasterData\Bathy_Images\TEST2\images
    gdalbuildvrt -input_file_list overviewimages.txt overview.vrt
    gdal_translate -tr 32 32 -r nearest -co "TILED=YES" -co "BIGTIFF=IF_NEEDED" -co "COMPRESS=LZW" overview2m.vrt overviewfile.tif
    
    ### output error message: gdalbuildvrt does not support rotated geo transforms.
    
    gdalwarp -t_srs '+proj=utm +zone=11 +datum=WGS84' raw_spot.tif utm11.tif

    #2
    G:\G\ST_GIS_Data_01\RasterData\Bathy_DTM\2012\ST12521_Bathy\
    gdalbuildvrt -input_file_list resolution2m.txt test\overview2m.vrt
    
