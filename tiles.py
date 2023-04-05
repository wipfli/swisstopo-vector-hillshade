import os

layers = ['RELI', 'GTON']

scales = [1000, 500, 200, 100, 50, 25]

min_zooms = {
    1000: 6,
    500: 10,
    200: 11,
    100: 12,
    50: 13,
    25: 14
}

max_zooms = {
    1000: 9,
    500: 10,
    200: 11,
    100: 12,
    50: 13,
    25: 14
}

os.system('rm layers/*')

for scale in scales:
    for layer in layers:
        command = f'tippecanoe -Z {min_zooms[scale]} -z {max_zooms[scale]} -o layers/SMR{scale}-{layer}.mbtiles -l {layer} {layer}-{scale}.geojson'
        print(command)
        os.system(command)

command = 'tile-join -o data/swisstopo-vector-hillshade.mbtiles layers/* -f'
print(command)
os.system(command)