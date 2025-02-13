from rdflib import BNode, Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
H5 = Namespace("http://hdfgroup.org/2025/02/hdf5#")

#===============================================================================
# File
#===============================================================================
g.add((H5.file, RDF.type, H5.File))
g.add((H5.file, RDFS.label, Literal("example.h5")))

#===============================================================================
# Root group
#===============================================================================

root = BNode()
b = BNode()
b1 = BNode()
triples = [
    # group
    (root, RDF.type, H5.Group),
    (root, RDFS.label, Literal("/")),
    (H5.file, H5.hasRoot, root),
    # attribute datatype
    (b, RDF.type, H5.Datatype),
    (b, H5.datatypeClass, H5.H5T_STRING),
    (b, H5.stringSize, Literal(17)),
    (b, H5.stringPad, H5.H5T_STR_NULLTERM),
    (b, H5.charSet, H5.H5T_CSET_ASCII),
    (b, H5.charType, H5.H5T_C_S1),
    # attribute
    (b1, RDF.type, H5.Attribute),
    (b1, RDFS.label, Literal("attr1")),
    (b1, H5.hasDatatype, b),
    (b1, H5.hasDataspace, H5.H5S_SCALAR),
    (b1, H5.hasValue, Literal("string attribute")),
    (root, H5.hasAttribute, b1)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /dset1
#===============================================================================

b10 = BNode()
triples = [
    # dataset
    (H5.d1, RDF.type, H5.Dataset),
    (H5.d1, H5.hasDatatype, H5.H5T_STD_I32BE),
    (H5.d1, H5.hasDataspace, Literal("[10, 10]")),
    # link
    (b10, RDF.type, H5.Link),
    (b10, RDFS.label, Literal("dset1")),
    (b10, H5.destination, H5.d1),
    (root, H5.hasLink, b10)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /dest2
#===============================================================================

b2 = BNode()
b3 = BNode()
b4 = BNode()
b5 = BNode()
b11 = BNode()
triples = [
    # datatype
    (b2, RDF.type, H5.Datatype),
    (b2, H5.datatypeClass, H5.H5T_COMPOUND),
    # first field
    (b3, H5.fieldName, Literal("a")),
    (b3, H5.fieldType, H5.H5T_STD_I32BE),
    (b3, H5.hasOffset, Literal(0)),
    (b2, H5.hasField, b3),
    # second field
    (b4, H5.fieldName, Literal("b")),
    (b4, H5.fieldType, H5.H5T_IEEE_F32BE),
    (b4, H5.hasOffset, Literal(4)),
    (b2, H5.hasField, b4),
    # third field
    (b5, H5.fieldName, Literal("c")),
    (b5, H5.fieldType, H5.H5T_IEEE_F64BE),
    (b5, H5.hasOffset, Literal(8)),
    (b2, H5.hasField, b5),
    # dataset
    (H5.d2, RDF.type, H5.Dataset),
    (H5.d2, H5.hasDatatype, b2),
    (H5.d2, H5.hasDataspace, Literal("[5]")),
    # link
    (b11, RDF.type, H5.Link),
    (b11, RDFS.label, Literal("dset2")),
    (b11, H5.destination, H5.d2),
    (root, H5.hasLink, b11)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /group1
#===============================================================================

b12 = BNode()
triples = [
    # group
    (H5.g1, RDF.type, H5.Group),
    (H5.g1, H5.hasComment, Literal("This is a comment for group1")),
    # link
    (b12, RDF.type, H5.Link),
    (b12, RDFS.label, Literal("group1")),
    (b12, H5.destination, H5.g1),
    (root, H5.hasLink, b12)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /group1/dset3
#===============================================================================

b13 = BNode()
triples = [
    # dataset
    (H5.d3, RDF.type, H5.Dataset),
    (H5.d3, H5.hasDatatype, Literal("/type1")),
    (H5.d3, H5.hasDataspace, Literal("[5]")),
    # link
    (b13, RDF.type, H5.Link),
    (b13, RDFS.label, Literal("dset3")),
    (b13, H5.destination, H5.d3),
    (H5.g1, H5.hasLink, b13)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /dset3
#===============================================================================

b22 = BNode()
b14 = BNode()
triples = [
    # datatype
    (b22, RDF.type, H5.Datatype),
    (b22, H5.datatypeClass, H5.H5T_VLEN),
    (b22, H5.elementDatatype, H5.H5T_STD_I32LE),
    # dataset
    (H5.d4, RDF.type, H5.Dataset),
    (H5.d4, H5.hasDatatype, b22),
    (H5.d4, H5.hasDataspace, Literal("[4]")),
    # link
    (b14, RDF.type, H5.Link),
    (b14, RDFS.label, Literal("dset3")),
    (b14, H5.destination, H5.d4),
    (root, H5.hasLink, b14)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /group2
#===============================================================================

b15 = BNode()
triples = [
    (b15, RDF.type, H5.Link),
    (b15, RDFS.label, Literal("group2")),
    (b15, H5.destination, H5.g1),
    (root, H5.hasLink, b15)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /slink1
#===============================================================================

b16 = BNode()
triples = [
    (b16, RDF.type, H5.Link),
    (b16, RDFS.label, Literal("slink1")),
    (b16, H5.destination, Literal("somevalue")),
    (root, H5.hasLink, b16)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================
# /type1
#===============================================================================

b17 = BNode()
b18 = BNode()
b19 = BNode()
b20 = BNode()
b21 = BNode()

triples = [
    # datatype object
    (H5.t4, RDF.type, H5.DatatypeObject),
    (H5.t4, H5.datatypeClass, H5.H5T_COMPOUND),
    # first field
    (b17, H5.fieldName, Literal("a")),
    (b18, RDF.type, H5.Datatype),
    (b18, H5.datatypeClass, H5.H5T_ARRAY),
    (b18, H5.shape, Literal("[4]")),
    (b18, H5.elementDatatype, H5.H5T_STD_I32BE),
    (b17, H5.fieldType, b18),
    (b17, H5.hasOffset, Literal(0)),
    (H5.t4, H5.hasField, b17),
    # second field
    (b19, H5.fieldName, Literal("b")),
    (b20, RDF.type, H5.Datatype),
    (b20, H5.datatypeClass, H5.H5T_ARRAY),
    (b20, H5.shape, Literal("[5][6]")),
    (b20, H5.elementDatatype, H5.H5T_IEEE_F32BE),
    (b19, H5.fieldType, b20),
    (b19, H5.hasOffset, Literal(16)),
    (H5.t4, H5.hasField, b19),
    # link
    (b21, RDF.type, H5.Link),
    (b21, RDFS.label, Literal("type1")),
    (b21, H5.destination, H5.t4),
    (root, H5.hasLink, b21)
]
for s, p, o in triples:
    g.add((s, p, o))

#===============================================================================

print(g.serialize(format='turtle'))