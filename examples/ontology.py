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

g.add((H5.Object, RDF.type, RDFS.Class))
g.add((H5.Group, RDFS.subClassOf, H5.Object))
g.add((H5.Dataset, RDFS.subClassOf, H5.Object))
g.add((H5.DatatypeObject, RDFS.subClassOf, H5.Object))

g.add((H5.ArrayVariable, RDF.type, RDFS.Class))
g.add((H5.Attribute, RDFS.subClassOf, H5.ArrayVariable))
g.add((H5.Dataset, RDFS.subClassOf, H5.ArrayVariable))

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

g.add((H5.Object, RDFS.label, Literal("HDF5 Object")))
g.add((H5.ArrayVariable, RDFS.label, Literal("HDF5 ArrayVariable")))

#===============================================================================
# Properties
#===============================================================================

g.add((H5.hasRoot, RDF.type, RDF.Property))
g.add((H5.hasRoot, RDFS.domain, H5.File))
g.add((H5.hasRoot, RDFS.range, H5.Group))

g.add((H5.hasLink, RDF.type, RDF.Property))
g.add((H5.hasLink, RDFS.domain, H5.Group))
g.add((H5.hasLink, RDFS.range, H5.Link))

g.add((H5.hasLink, RDF.type, RDF.Property))
g.add((H5.hasLink, RDFS.domain, H5.Group))
g.add((H5.hasLink, RDFS.range, H5.Link))

g.add((H5.destination, RDF.type, RDF.Property))
g.add((H5.destination, RDFS.domain, H5.Link))

g.add((H5.hasAttribute, RDF.type, RDF.Property))
g.add((H5.hasAttribute, RDFS.domain, H5.Object))
g.add((H5.hasAttribute, RDFS.range, H5.Attribute))

g.add((H5.hasDataspace, RDF.type, RDF.Property))
g.add((H5.hasDataspace, RDFS.domain, H5.ArrayVariable))

g.add((H5.hasDatatype, RDF.type, RDF.Property))
g.add((H5.hasDatatype, RDFS.domain, H5.ArrayVariable))

#===============================================================================

print(g.serialize(format='turtle'))