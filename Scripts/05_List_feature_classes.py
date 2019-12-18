import arcpy

arcpy.env.workspace = r'..\Output'

featureclasses = arcpy.ListFeatureClasses()

for x in featureclasses:
    print x
    input_features = x
    layer_name = x.split(".")
    output_feature_class = "/projected/" + layer_name[0] + "_projected." + layer_name[1] 
    out_coordinate_system = arcpy.SpatialReference(54004)
    arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)
    print x + " projected!"