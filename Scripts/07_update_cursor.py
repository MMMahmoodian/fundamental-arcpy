import arcpy

arcpy.env.overwriteOutput = True

points = r'..\Data\ne_10m_admin_0_countries.shp'
arcpy.MakeFeatureLayer_management(points, "points_layer") 

with arcpy.da.UpdateCursor("points_layer", ["POP_MAX", "DIFFNOTE"]) as cities_cursor:
    for city in cities_cursor:
        if city[0] > 500000:
            city[1] = "A"
        if city[0] <= 500000 and city[0] > 100000:
            city[1] = "B"
        if city[0] <= 100000:
            city[1] = "C"

        cities_cursor.updateRow(city)
    

