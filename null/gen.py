
types = [
    'Point',
    'PointZ',
    'PointM',
    'PointZM',
    'PointS',
    'PointZS',
    'PointMS',
    'PointZMS',
    'LineString',
    'LineStringZ',
    'LineStringM',
    'LineStringZM',
    'LineStringS',
    'LineStringZS',
    'LineStringMS',
    'LineStringZMS',
    'Polygon',
    'PolygonZ',
    'PolygonM',
    'PolygonZM',
    'PolygonS',
    'PolygonZS',
    'PolygonMS',
    'PolygonZMS',
    'MultiPoint',
    'MultiPointZ',
    'MultiPointM',
    'MultiPointZM',
    'MultiPointS',
    'MultiPointZS',
    'MultiPointMS',
    'MultiPointZMS',
    'MultiLineString',
    'MultiLineStringZ',
    'MultiLineStringM',
    'MultiLineStringZM',
    'MultiLineStringS',
    'MultiLineStringZS',
    'MultiLineStringMS',
    'MultiLineStringZMS',
    'MultiPolygon',
    'MultiPolygonZ',
    'MultiPolygonM',
    'MultiPolygonZM',
    'MultiPolygonS',
    'MultiPolygonZS',
    'MultiPolygonMS',
    'MultiPolygonZMS',
]

with open('template.txt', 'r') as f:
    tpl = f.read()

for t in types:
    with open(t + '.go', 'w') as f:
        f.write(tpl.replace('$$$', t))
