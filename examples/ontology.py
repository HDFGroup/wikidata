from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
H5 = Namespace("http://hdfgroup.org/2025/02/hdf5#")

#===============================================================================
# Classes
#===============================================================================
g.add((H5.File, RDF.type, RDFS.class))
g.add((H5.Group, RDF.type, RDFS.class))
g.add((H5.Dataset, RDF.type, RDFS.class))
g.add((H5.DatatypeObject, RDF.type, RDFS.class))
g.add((H5.Attribute, RDF.type, RDFS.class))
g.add((H5.Datatype, RDF.type, RDFS.class))
g.add((H5.Dataspace, RDF.type, RDFS.class))
g.add((H5.Link, RDF.type, RDFS.class))

#===============================================================================
# Labels
#===============================================================================

g.add((H5.File, RDFS.label, Literal("HDF5 File")))
g.add((H5.Group, RDF.label, Literal("HDF5 Group")))
g.add((H5.Dataset, RDF.label, Literal("HDF5 Dataset")))
g.add((H5.DatatypeObject, RDF.label, Literal("HDF5 Datatype Object")))
g.add((H5.Attribute, RDF.label, Literal("HDF5 Attribute")))
g.add((H5.Datatype, RDF.label, Literal("HDF5 Datatype")))
g.add((H5.Dataspace, RDF.label, Literal("HDF5 Dataspace")))
g.add((H5.Link, RDF.label, Literal("HDF5 Link")))

#===============================================================================
# Properties
#===============================================================================

g.add((H5.hasRoot, RDF.type, RDF.Property))
g.add((H5.hasRoot, RDFS.domain, H5.File))
g.add((H5.hasRoot, RDFS.range, H5.Group))

g.add((H5.hasLink, RDF.type, RDF.Property))
g.add((H5.hasLink, RDFS.domain, H5.Group))
g.add((H5.hasLink, RDFS.range, H5.Link))
