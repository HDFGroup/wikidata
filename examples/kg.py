from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()

H5 = Namespace("http://hdfgroup.org/hdf5/")

g.add((H5.file, RDF.type, H5.File))
g.add((H5.file, RDFS.label, Literal("example.h5")))

# Root group
g.add((H5.root, RDF.type, H5.Group))
g.add((H5.file, H5.hasRoot, H5.root))

g.add((H5.t1, RDF.type, H5.Datatype))
g.add((H5.t1, H5.datatypeClass, H5.H5T_STRING))
g.add((H5.t1, H5.stringSize, Literal(17)))
g.add((H5.t1, H5.stringPad, H5.H5T_STR_NULLTERM))
g.add((H5.t1, H5.charSet, H5.H5T_CSET_ASCII))
g.add((H5.t1, H5.charType, H5.H5T_C_S1))

g.add((H5.a1, RDF.type, H5.Attribute))
g.add((H5.a1, RDFS.label, Literal("attr1")))
g.add((H5.a1, H5.hasDatatype, H5.t1))
g.add((H5.a1, H5.hasDataspace, H5.H5S_SCALAR))
g.add((H5.a1, H5.hasValue, Literal("string attribute")))
g.add((H5.root, H5.hasAttribute, H5.a1))

# /dset1
g.add((H5.d1, RDF.type, H5.Dataset))
g.add((H5.d1, H5.hasDatatype, H5.H5T_STD_I32BE))
g.add((H5.d1, H5.hasDataspace, Literal("[10, 10]")))

g.add((H5.l1, RDF.type, H5.Link))
g.add((H5.l1, RDFS.label, Literal("dset1")))
g.add((H5.l1, H5.source, H5.root))
g.add((H5.l1, H5.destination, H5.d1))

# /dest2
g.add((H5.t2, RDF.type, H5.Datatype))
g.add((H5.t2, H5.datatypeClass, H5.H5T_COMPOUND))
g.add((H5.c1, RDF.type, H5.CompoundField))
g.add((H5.c1, H5.fieldName, Literal("a")))
g.add((H5.c1, H5.fieldType, H5.H5T_STD_I32BE))
g.add((H5.c1, H5.hasOffset, Literal(0)))
g.add((H5.t2, H5.hasField, H5.c1))

g.add((H5.c2, RDF.type, H5.CompoundField))
g.add((H5.c2, H5.fieldName, Literal("b")))
g.add((H5.c2, H5.fieldType, H5.H5T_IEEE_F32BE))
g.add((H5.c2, H5.hasOffset, Literal(4)))
g.add((H5.t2, H5.hasField, H5.c2))

g.add((H5.c3, RDF.type, H5.CompoundField))
g.add((H5.c3, H5.fieldName, Literal("c")))
g.add((H5.c3, H5.fieldType, H5.H5T_IEEE_F64BE))
g.add((H5.c3, H5.hasOffset, Literal(8)))
g.add((H5.t2, H5.hasField, H5.c3))

g.add((H5.d2, RDF.type, H5.Dataset))
g.add((H5.d2, H5.hasDatatype, H5.t2))
g.add((H5.d2, H5.hasDataspace, Literal("[5]")))

g.add((H5.l2, RDF.type, H5.Link))
g.add((H5.l2, RDFS.label, Literal("dset2")))
g.add((H5.l2, H5.source, H5.root))
g.add((H5.l2, H5.destination, H5.d2))

# /group1
g.add((H5.g1, RDF.type, H5.Group))
g.add((H5.g1, H5.hasComment, Literal("This is a comment for group1")))
g.add((H5.l3, RDF.type, H5.Link))
g.add((H5.l3, RDFS.label, Literal("group1")))
g.add((H5.l3, H5.source, H5.root))
g.add((H5.l3, H5.destination, H5.g1))

# /group1/dset3
g.add((H5.d3, RDF.type, H5.Dataset))
g.add((H5.d3, H5.hasDatatype, Literal("/type1")))
g.add((H5.d3, H5.hasDataspace, Literal("[5]")))
g.add((H5.l4, RDF.type, H5.Link))
g.add((H5.l4, RDFS.label, Literal("dset3")))
g.add((H5.l4, H5.source, H5.g1))
g.add((H5.l4, H5.destination, H5.d3))

# /dset3
g.add((H5.t3, RDF.type, H5.Datatype))
g.add((H5.t3, H5.datatypeClass, H5.H5T_VLEN))
g.add((H5.t3, H5.elementDatatype, H5.H5T_STD_I32LE))
g.add((H5.d4, RDF.type, H5.Dataset))
g.add((H5.d4, H5.hasDatatype, H5.t3))
g.add((H5.d4, H5.hasDataspace, Literal("[4]")))

g.add((H5.l5, RDF.type, H5.Link))
g.add((H5.l5, RDFS.label, Literal("dset3")))
g.add((H5.l5, H5.source, H5.root))
g.add((H5.l5, H5.destination, H5.d4))

# /group2
g.add((H5.l6, RDF.type, H5.Link))
g.add((H5.l6, RDFS.label, Literal("group2")))
g.add((H5.l6, H5.source, H5.root))
g.add((H5.l6, H5.destination, H5.g1))

# /slink1
g.add((H5.l7, RDF.type, H5.Link))
g.add((H5.l7, RDFS.label, Literal("slink1")))
g.add((H5.l7, H5.source, H5.root))
g.add((H5.l7, H5.destination, Literal("somevalue")))

# /type1
g.add((H5.t4, RDF.type, H5.Datatype))
g.add((H5.t4, H5.datatypeClass, H5.H5T_COMPOUND))
g.add((H5.c4, RDF.type, H5.CompoundField))
g.add((H5.c4, H5.fieldName, Literal("a")))
g.add((H5.c4, H5.fieldType, H5.t5))
g.add((H5.c4, H5.hasOffset, Literal(0)))
g.add((H5.t4, H5.hasField, H5.c4))

g.add((H5.t5, RDF.type, H5.Datatype))
g.add((H5.t5, H5.datatypeClass, H5.H5T_ARRAY))
g.add((H5.t5, H5.shape, Literal("[4]")))
g.add((H5.t5, H5.elementDatatype, H5.H5T_STD_I32BE))

g.add((H5.c5, RDF.type, H5.CompoundField))
g.add((H5.c5, H5.fieldName, Literal("b")))
g.add((H5.c5, H5.fieldType, H5.t6))
g.add((H5.c5, H5.hasOffset, Literal(16)))
g.add((H5.t4, H5.hasField, H5.c5))

g.add((H5.t6, RDF.type, H5.Datatype))
g.add((H5.t6, H5.datatypeClass, H5.H5T_ARRAY))
g.add((H5.t6, H5.shape, Literal("[5][6]")))
g.add((H5.t6, H5.elementDatatype, H5.H5T_IEEE_F32BE))

g.add((H5.l8, RDF.type, H5.Link))
g.add((H5.l8, RDFS.label, Literal("type1")))
g.add((H5.l8, H5.source, H5.root))
g.add((H5.l8, H5.destination, H5.t4))

print(g.serialize(format='turtle'))