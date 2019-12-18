import arcpy

points = r'..\Data\ne_10m_admin_0_countries.shp'
countries = r'..\Data\ne_10m_populated_places_simple.shp'
outputs = r'..\Output'

arcpy.MakeFeatureLayer_management(points, "points_layer")
arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "NAME" = 'Iran' """)

arcpy.SelectLayerByLocation_management("points_layer", "INTERSECT", "countries_layer")

arcpy.FeatureClassToFeatureClass_conversion("points_layer", outputs, "cities_in_iran")

