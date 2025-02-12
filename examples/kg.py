from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()

H5 = Namespace("http://hdfgroup.org/hdf5/")

g.add((H5.file, RDF.type, H5.File))
g.add((H5.file, RDFS.label, Literal("example.h5")))

g.add((H5.root, RDF.type, H5.Group))
g.add((H5.file, H5.hasRoot, H5.root))

g.add((H5.a1t, RDF.type, H5.Datatype))
g.add((H5.a1t, H5.datatypeClass, H5.H5T_STRING))
g.add((H5.a1t, H5.stringSize, Literal(17)))
g.add((H5.a1t, H5.stringPad, H5.H5T_STR_NULLTERM))
g.add((H5.a1t, H5.charSet, H5.H5T_CSET_ASCII))
g.add((H5.a1t, H5.charType, H5.H5T_C_S1))

g.add((H5.a1, RDF.type, H5.Attribute))
g.add((H5.a1, RDFS.label, Literal("attr1")))
g.add((H5.a1, H5.hasDatatype, H5.a1t))
g.add((H5.a1, H5.hasDataspace, H5.H5S_SCALAR))
g.add((H5.a1, H5.hasValue, Literal("string attribute")))
g.add((H5.root, H5.hasAttribute, H5.a1))

g.add((H5.d1, RDF.type, H5.Dataset))
g.add((H5.d1, H5.hasDatatype, H5.H5T_STD_I32BE))
g.add((H5.d1, H5.hasDataspace, Literal("[10, 10]")))

g.add((H5.rld1, RDF.type, H5.Link))
g.add((H5.rld1, RDFS.label, Literal("dset1")))
g.add((H5.rld1, H5.source, H5.root))
g.add((H5.rld1, H5.destination, H5.d1))

print(g.serialize(format='turtle'))