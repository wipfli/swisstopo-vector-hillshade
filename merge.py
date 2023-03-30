import os

thresholds = list(range(32, 255, 32))

for threshold in thresholds:
    command = f'ogrmerge.py -single -f geojson -s_srs epsg:2056 -t_srs epsg:4326 -o merged/{threshold}.geojson output/*-{threshold}-simplified.gpkg'
    print(command)
    os.system(command)
    
    #command = f'ogr2ogr -f geojson merged/union-{threshold}.geojson merged/{threshold}.geojson -dialect sqlite -sql "SELECT ST_Union(ST_MakeValid(geometry)) FROM merged"'
    #print(command)
    #os.system(command)

command = 'ogrmerge.py -single -f geojson -o reli.geojson merged/*'
print(command)
os.system(command)
