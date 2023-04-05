import os

thresholds = list(range(32, 255, 32))

layers = ['GTON', 'RELI']
scales = [25]


for scale in scales:
    for layer in layers:
        for threshold in thresholds:
            out_filename = f'merged/{layer}-{scale}-{threshold}.geojson'
            os.system(f'rm {out_filename}')

            command = f'ogrmerge.py -single -f geojson -s_srs epsg:2056 -t_srs epsg:4326 -o {out_filename} output/SMR{scale}_LV95_{layer}_*-{threshold}-simplified.gpkg'
            print(command)
            os.system(command)

        out_filename = f'{layer}-{scale}.geojson'
        os.system(f'rm {out_filename}')

        command = f'ogrmerge.py -single -f geojson -o {out_filename} merged/{layer}-{scale}-*.geojson'
        print(command)
        os.system(command)
