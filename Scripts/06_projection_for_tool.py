import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)

featureclasses = arcpy.ListFeatureClasses()

for x in featureclasses:
    arcpy.AddMessage(x)
    input_features = x
    layer_name = x.split(".")
    output_feature_class = arcpy.GetParameterAsText(1) + layer_name[0] + "_projected." + layer_name[1] 
    out_coordinate_system = arcpy.GetParameterAsText(2)
    arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)
    arcpy.AddMessage(x + " projected!")