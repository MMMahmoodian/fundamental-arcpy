import arcpy

arcpy.env.workspace= r'..\Data'



points = "ne_10m_admin_0_countries.shp"
countries = "ne_10m_populated_places_simple.shp"
outputs = r'..\Output'

with arcpy.da.SearchCursor(points, ['*']) as cities_cursor:    
    for x in cities_cursor:
        print x