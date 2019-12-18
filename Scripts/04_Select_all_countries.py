import arcpy

arcpy.env.overwriteOutput = True

points = r'..\Data\ne_10m_admin_0_countries.shp'
countries = r'..\Data\ne_10m_populated_places_simple.shp'
outputs = r'..\Output'


arcpy.MakeFeatureLayer_management(points, "points_layer")   

with arcpy.da.SearchCursor(countries, ['SOV_A3', 'FID']) as countries_cursor:
    for country in countries_cursor:
        print country[0] # String
        arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "FID" = {} """.format(country[1]))
        arcpy.SelectLayerByLocation_management("points_layer", "INTERSECT", "countries_layer")
        arcpy.FeatureClassToFeatureClass_conversion("points_layer", outputs, "cities_in_{}_{}".format(country[0],country[1]))


# country_list = ["Iran", "Russia", "France", "Turkey"]



# arcpy.MakeFeatureLayer_management(points, "points_layer")
# for country in country_list:
#     print country
#     arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "NAME" = '{}' """.format(country))
#     arcpy.SelectLayerByLocation_management("points_layer", "WITHIN", "countries_layer")
#     arcpy.FeatureClassToFeatureClass_conversion("points_layer", outputs, "cities_in_{}".format(country))