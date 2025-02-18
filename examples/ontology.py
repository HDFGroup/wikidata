from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
H5 = Namespace("http://hdfgroup.org/2025/02/hdf5#")

#===============================================================================
# Classes
#===============================================================================
g.add((H5.File, RDF.type, RDFS.Class))
g.add((H5.Group, RDF.type, RDFS.Class))
g.add((H5.Dataset, RDF.type, RDFS.Class))
g.add((H5.DatatypeObject, RDF.type, RDFS.Class))
g.add((H5.Attribute, RDF.type, RDFS.Class))
g.add((H5.Datatype, RDF.type, RDFS.Class))
g.add((H5.Dataspace, RDF.type, RDFS.Class))
g.add((H5.Link, RDF.type, RDFS.Class))

#===============================================================================
# Labels
#===============================================================================

g.add((H5.File, RDFS.label, Literal("HDF5 File")))
g.add((H5.Group, RDFS.label, Literal("HDF5 Group")))
g.add((H5.Dataset, RDFS.label, Literal("HDF5 Dataset")))
g.add((H5.DatatypeObject, RDFS.label, Literal("HDF5 Datatype Object")))
g.add((H5.Attribute, RDFS.label, Literal("HDF5 Attribute")))
g.add((H5.Datatype, RDFS.label, Literal("HDF5 Datatype")))
g.add((H5.Dataspace, RDFS.label, Literal("HDF5 Dataspace")))
g.add((H5.Link, RDFS.label, Literal("HDF5 Link")))

#===============================================================================
# Properties
#===============================================================================

g.add((H5.hasRoot, RDF.type, RDF.Property))
g.add((H5.hasRoot, RDFS.domain, H5.File))
g.add((H5.hasRoot, RDFS.range, H5.Group))

g.add((H5.hasLink, RDF.type, RDF.Property))
g.add((H5.hasLink, RDFS.domain, H5.Group))
g.add((H5.hasLink, RDFS.range, H5.Link))

#===============================================================================

print(g.serialize(format='turtle'))