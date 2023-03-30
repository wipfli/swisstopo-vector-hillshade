# Swisstopo Vector Hillshade

Use hand-drawn hillshading layers from Swisstopo to generate vector hillshading in MapLibre GL JS.

## Demo

### Hillshade Only

https://wipfli.github.io/swisstopo-vector-hillshade

<a href="https://wipfli.github.io/swisstopo-vector-hillshade">
    <img src="screenshot.png" width=450>
</a>

### Hillshade and Swissmap Overlay

https://wipfli.github.io/swisstopo-vector-hillshade/swissmap

<a href="https://wipfli.github.io/swisstopo-vector-hillshade/swissmap">
    <img src="screenshot-swissmap.png" width=450>
</a>

## Source Data

Download sample data from [swisstopo](https://www.swisstopo.admin.ch/de/geodata/maps/smr/smr100.html). For the full map data, contact swisstopo directly.

The file contains raster files for the different layers of the swisstopo map. We use the following layers:

### SMR100_LV95_GTON_Mosaic.tif: Gelbton (yellow tone)

Color: `rgb(255, 255, 228)`

Opacity mask:

<img src="SMR100_LV95_GTON_Mosaic.png" width=450>

### SMR100_LV95_RELI_Mosaic.tif: Relief (relief)

Color: `rgb(173, 188, 199)`

Opacity mask:

<img src="SMR100_LV95_RELI_Mosaic.png" width=450>

These opacity masks were hand-drawn I think by Swiss cartographers in the past...


## Vectorization with GDAL

```
python3 script.py
python3 merge.py
```

## Tippecanoe

```
tippecanoe -Z 10 -z 10 -o swisstopo-vector-hillshade.pmtiles reli.geojson gton.geojson
```