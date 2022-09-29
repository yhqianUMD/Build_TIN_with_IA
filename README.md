# Data_TIN_IA
This code is used to obtain vertices and triangles from off file with the format of the IA data structure.

1. file list:
1) point.py defines a point class. Points are stored as (x, y).
2) vertex.py defines a vertex class inheriting from the point class. Vertices are stored as (x, y, attributes)
3) triangle.py defines a triangle class. A Triangle is encoded as the triple of the indexes of its vertices in the Vertex array, e.g., (3, v1, v2, v3), where v1, v2, and v3 are the indexes of responding vertex.
4) tin.py defines a TIN class. This class could obtain the VV relation, TT relation, and partial VT relation from a TIN file.

2. input:
there are three parameters for this code.
1) the TIN file, e.g., sonoma.off
2) the name of output vertices file where a vertex is stored as (x, y, ele, VID, tID), where VID is the index of the vertex itself, the tID is the index of one triangle incident in this vertex.
3) the name of output triangles file where a triangle is stored as (x1,y1,x2,y2,x3,y3,x1,y1,v1,v2,v3,t_self,t1,t2,t3), where v1,v2,v3 are the indexes of its end vertices, t_self is the index of the triangle itself, t1,t2,t3 are the indexes of its three adjacent triangles.
