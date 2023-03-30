import os
import glob

def process_single(filename, threshold):
    print(f'reproject')
    os.system(f'gdal_translate -of GTiff input/{filename} tmp/gtif-{filename}')

    print(f'threshold')
    os.system(f'gdal_calc.py -A tmp/gtif-{filename} --calc="(A<={threshold})*100 + ({threshold}<A)*200" --outfile="tmp/{filename}-{threshold}-out.tif"')

    print("sieve")
    os.system(f'gdal_sieve.py -st 400 -8 tmp/{filename}-{threshold}-out.tif tmp/{filename}-{threshold}-sieved.tif')

    print("select")
    os.system(f'gdal_calc.py -A tmp/{filename}-{threshold}-sieved.tif --calc="(A==200)*255" --outfile="tmp/{filename}-{threshold}-selected.tif"')

    print("polygonize")
    os.system(f'gdal_polygonize.py tmp/{filename}-{threshold}-selected.tif -b 1 -f "GPKG" tmp/{filename}-{threshold}-polygons.gpkg OUTPUT DN')

    print("simplify")
    os.system(f'ogr2ogr -f "GPKG" output/{filename}-{threshold}-simplified.gpkg tmp/{filename}-{threshold}-polygons.gpkg -simplify 20')

filenames = [path.split('/')[1] for path in glob.glob('input/*.tif')]
thresholds = list(range(32, 255, 32))

for filename in filenames:
    for threshold in thresholds:
        process_single(filename, threshold)
