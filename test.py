from osgeo import ogr

# open shapefile
ds = ogr.Open("merged.shp", 1)
layer = ds.GetLayer()

# get extent
ext = layer.GetExtent()

# get a single feature
feature = layer.GetFeature(1)

# loop over all features in a layer
for feature in layer:
    print(feature.GetField("FID"))
 
# create new shapefile   
driver = ogr.GetDriverByName("ESRI Shapefile")
outds = driver.CreateDataSource("out.shp")

# copy layer
outlayer = ds.CopyLayer(layer, "out")

# create a new attribute field
newfield = ogr.FieldDefn("Perimeter", ogr.OFTReal)
newfield.SetWidth(10)
newfield.SetPrecision(3)
outlayer.CreateField(newfield)

# get the perimeter of each polygon
for feature in outlayer:
    geom = feature.GetGeometryRef()
    perim = geom.Boundary().Length()
    feature.SetField("Perimeter", perim)
    outlayer.SetFeature(feature)
    
# close everything
outlayer = outds = feature = None

# create a ring geometry from the extent of the merged layer
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(ext[0], ext[2])
ring.AddPoint(ext[1], ext[2])
ring.AddPoint(ext[1], ext[3])
ring.AddPoint(ext[0], ext[3])
ring.AddPoint(ext[0], ext[2])

# convert to polygon
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)

# save to shapefile
outds = driver.CreateDataSource("extent.shp")
outlayer = outds.CreateLayer("extent", layer.GetSpatialRef())
feature = ogr.Feature(outlayer.GetLayerDefn())

feature.SetGeometry(poly)
outlayer.CreateFeature(feature)

outds = outlayer = feature = None

# 설치 : https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html
