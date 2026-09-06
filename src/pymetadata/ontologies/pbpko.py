"""PBPKO ontology.

Generated from the ontology release by
`pymetadata.ontologies._ontology_builder`, do not edit.
"""

from pymetadata.ontologies.term import OntologyTerm, TermData

pattern = r"^PBPKO_\d{5}$"


class PBPKO(OntologyTerm):
    """PBPKO ontology."""

    BFO_0000001: "PBPKO"
    """entity."""

    ENTITY: "PBPKO"
    """entity."""

    BFO_0000002: "PBPKO"
    """continuant: An entity that exists in full at any time in which it exists at all, persists through time while maintaining its identity and has no temporal parts."""

    CONTINUANT: "PBPKO"
    """continuant: An entity that exists in full at any time in which it exists at all, persists through time while maintaining its identity and has no temporal parts."""

    BFO_0000003: "PBPKO"
    """occurrent: An entity that has temporal parts and that happens, unfolds or develops through time."""

    OCCURRENT: "PBPKO"
    """occurrent: An entity that has temporal parts and that happens, unfolds or develops through time."""

    BFO_0000004: "PBPKO"
    """independent continuant: b is an independent continuant = Def. b is a continuant which is such that there is no c and no t such that b s-depends_on c at t. (axiom label in BFO2 Reference: [017-002])"""

    INDEPENDENT_CONTINUANT: "PBPKO"
    """independent continuant: b is an independent continuant = Def. b is a continuant which is such that there is no c and no t such that b s-depends_on c at t. (axiom label in BFO2 Reference: [017-002])"""

    BFO_0000015: "PBPKO"
    """process: p is a process = Def. p is an occurrent that has temporal proper parts and for some time t, p s-depends_on some material entity at t. (axiom label in BFO2 Reference: [083-003])"""

    PROCESS: "PBPKO"
    """process: p is a process = Def. p is an occurrent that has temporal proper parts and for some time t, p s-depends_on some material entity at t. (axiom label in BFO2 Reference: [083-003])"""

    BFO_0000016: "PBPKO"
    """disposition."""

    DISPOSITION: "PBPKO"
    """disposition."""

    BFO_0000017: "PBPKO"
    """realizable entity: A specifically dependent continuant that inheres in continuant entities and are not exhibited in full at every time in which it inheres in an entity or group of entities. The exhibition or actualization of a realizable entity is a particular manifestation, functioning or process that occurs under certain circumstances."""

    REALIZABLE_ENTITY: "PBPKO"
    """realizable entity: A specifically dependent continuant that inheres in continuant entities and are not exhibited in full at every time in which it inheres in an entity or group of entities. The exhibition or actualization of a realizable entity is a particular manifestation, functioning or process that occurs under certain circumstances."""

    BFO_0000019: "PBPKO"
    """quality."""

    QUALITY: "PBPKO"
    """quality."""

    BFO_0000020: "PBPKO"
    """specifically dependent continuant: b is a specifically dependent continuant = Def. b is a continuant & there is some independent continuant c which is not a spatial region and which is such that b s-depends_on c at every time t during the course of b’s existence. (axiom label in BFO2 Reference: [050-003])"""

    SPECIFICALLY_DEPENDENT_CONTINUANT: "PBPKO"
    """specifically dependent continuant: b is a specifically dependent continuant = Def. b is a continuant & there is some independent continuant c which is not a spatial region and which is such that b s-depends_on c at every time t during the course of b’s existence. (axiom label in BFO2 Reference: [050-003])"""

    BFO_0000023: "PBPKO"
    """role: A realizable entity the manifestation of which brings about some result or end that is not essential to a continuant in virtue of the kind of thing that it is but that can be served or participated in by that kind of continuant in some kinds of natural, social or institutional contexts."""

    ROLE: "PBPKO"
    """role: A realizable entity the manifestation of which brings about some result or end that is not essential to a continuant in virtue of the kind of thing that it is but that can be served or participated in by that kind of continuant in some kinds of natural, social or institutional contexts."""

    BFO_0000029: "PBPKO"
    """site."""

    SITE: "PBPKO"
    """site."""

    BFO_0000031: "PBPKO"
    """generically dependent continuant."""

    GENERICALLY_DEPENDENT_CONTINUANT: "PBPKO"
    """generically dependent continuant."""

    BFO_0000034: "PBPKO"
    """function."""

    FUNCTION: "PBPKO"
    """function."""

    BFO_0000040: "PBPKO"
    """material entity: An independent continuant that is spatially extended whose identity is independent of that of other entities and can be maintained through time."""

    MATERIAL_ENTITY: "PBPKO"
    """material entity: An independent continuant that is spatially extended whose identity is independent of that of other entities and can be maintained through time."""

    BFO_0000050: "PBPKO"
    """part of: a core relation that holds between a part and its whole"""

    PART_OF: "PBPKO"
    """part of: a core relation that holds between a part and its whole"""

    BFO_0000051: "PBPKO"
    """has part: a core relation that holds between a whole and its part"""

    HAS_PART: "PBPKO"
    """has part: a core relation that holds between a whole and its part"""

    BFO_0000055: "PBPKO"
    """realizes: Paraphrase of elucidation: a relation between a process and a realizable entity, where there is some material entity that is bearer of the realizable entity and participates in the process, and the realizable entity comes to be realized in the course of the process"""

    REALIZES: "PBPKO"
    """realizes: Paraphrase of elucidation: a relation between a process and a realizable entity, where there is some material entity that is bearer of the realizable entity and participates in the process, and the realizable entity comes to be realized in the course of the process"""

    BFO_0000062: "PBPKO"
    """preceded by: x is preceded by y if and only if the time point at which y ends is before or equivalent to the time point at which x starts. Formally: x preceded by y iff ω(y) <= α(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point."""

    PRECEDED_BY: "PBPKO"
    """preceded by: x is preceded by y if and only if the time point at which y ends is before or equivalent to the time point at which x starts. Formally: x preceded by y iff ω(y) <= α(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point."""

    BFO_0000063: "PBPKO"
    """precedes: x precedes y if and only if the time point at which x ends is before or equivalent to the time point at which y starts. Formally: x precedes y iff ω(x) <= α(y), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point."""

    PRECEDES: "PBPKO"
    """precedes: x precedes y if and only if the time point at which x ends is before or equivalent to the time point at which y starts. Formally: x precedes y iff ω(x) <= α(y), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point."""

    BFO_0000141: "PBPKO"
    """immaterial entity."""

    IMMATERIAL_ENTITY: "PBPKO"
    """immaterial entity."""

    CHEBI_16670: "PBPKO"
    """peptide: Amide derived from two or more amino carboxylic acid molecules (the same or different) by formation of a covalent bond from the carbonyl carbon of one to the nitrogen atom of another with formal loss of water. The term is usually applied to structures formed from α-amino acids, but it includes those derived from any amino carboxylic acid. X = OH, OR, NH2, NHR, etc."""

    PEPTIDE: "PBPKO"
    """peptide: Amide derived from two or more amino carboxylic acid molecules (the same or different) by formation of a covalent bond from the carbonyl carbon of one to the nitrogen atom of another with formal loss of water. The term is usually applied to structures formed from α-amino acids, but it includes those derived from any amino carboxylic acid. X = OH, OR, NH2, NHR, etc."""

    CHEBI_24636: "PBPKO"
    """proton: Nuclear particle of charge number +1, spin ½ and rest mass of 1.007276470(12) u."""

    PROTON: "PBPKO"
    """proton: Nuclear particle of charge number +1, spin ½ and rest mass of 1.007276470(12) u."""

    CHEBI_33252: "PBPKO"
    """atomic nucleus: A nucleus is the positively charged central portion of an atom, excluding the orbital electrons."""

    ATOMIC_NUCLEUS: "PBPKO"
    """atomic nucleus: A nucleus is the positively charged central portion of an atom, excluding the orbital electrons."""

    CHEBI_33839: "PBPKO"
    """macromolecule: A macromolecule is a molecule of high relative molecular mass, the structure of which essentially comprises the multiple repetition of units derived, actually or conceptually, from molecules of low relative molecular mass."""

    MACROMOLECULE: "PBPKO"
    """macromolecule: A macromolecule is a molecule of high relative molecular mass, the structure of which essentially comprises the multiple repetition of units derived, actually or conceptually, from molecules of low relative molecular mass."""

    CHEBI_36342: "PBPKO"
    """subatomic particle: A particle smaller than an atom."""

    SUBATOMIC_PARTICLE: "PBPKO"
    """subatomic particle: A particle smaller than an atom."""

    CL_0000000: "PBPKO"
    """cell: A material entity of anatomical origin (part of or deriving from an organism) that has as its parts a maximally connected cell compartment surrounded by a plasma membrane."""

    CELL: "PBPKO"
    """cell: A material entity of anatomical origin (part of or deriving from an organism) that has as its parts a maximally connected cell compartment surrounded by a plasma membrane."""

    COB_0000011: "PBPKO"
    """atom: A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it."""

    ATOM: "PBPKO"
    """atom: A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it."""

    COB_0000013: "PBPKO"
    """molecule: A material entity that consists of two or more atoms that are all connected via covalent bonds such that any atom can be transitively connected with any other atom."""

    MOLECULE: "PBPKO"
    """molecule: A material entity that consists of two or more atoms that are all connected via covalent bonds such that any atom can be transitively connected with any other atom."""

    COB_0000021: "PBPKO"
    """gross anatomical part: A part of a multicellular organism that is a collection of cell components that are not all contained in one cell."""

    GROSS_ANATOMICAL_PART: "PBPKO"
    """gross anatomical part: A part of a multicellular organism that is a collection of cell components that are not all contained in one cell."""

    COB_0000022: "PBPKO"
    """organism: A material entity that is a maximal functionally integrated unit that develops from a program encoded in a genome"""

    ORGANISM: "PBPKO"
    """organism: A material entity that is a maximal functionally integrated unit that develops from a program encoded in a genome"""

    COB_0000035: "PBPKO"
    """completely executed planned process."""

    COMPLETELY_EXECUTED_PLANNED_PROCESS: "PBPKO"
    """completely executed planned process."""

    COB_0000080: "PBPKO"
    """complex of molecules: A complex of two or more molecules that are not covalently bound."""

    COMPLEX_OF_MOLECULES: "PBPKO"
    """complex of molecules: A complex of two or more molecules that are not covalently bound."""

    COB_0000082: "PBPKO"
    """planned process: A process that is initiated by an agent who intends to carry out a plan to achieve an objective through one or more actions as described in a plan specification."""

    PLANNED_PROCESS: "PBPKO"
    """planned process: A process that is initiated by an agent who intends to carry out a plan to achieve an objective through one or more actions as described in a plan specification."""

    COB_0000502: "PBPKO"
    """characteristic."""

    CHARACTERISTIC: "PBPKO"
    """characteristic."""

    GO_0003008: "PBPKO"
    """system process."""

    SYSTEM_PROCESS: "PBPKO"
    """system process."""

    GO_0003674: "PBPKO"
    """gene product or complex activity: A molecular process that can be carried out by the action of a single macromolecular machine, usually via direct physical interactions with other molecular entities. Function in this sense denotes an action, or activity, that a gene product (or a complex) performs."""

    GENE_PRODUCT_OR_COMPLEX_ACTIVITY: "PBPKO"
    """gene product or complex activity: A molecular process that can be carried out by the action of a single macromolecular machine, usually via direct physical interactions with other molecular entities. Function in this sense denotes an action, or activity, that a gene product (or a complex) performs."""

    GO_0005575: "PBPKO"
    """cellular_component: A location, relative to cellular compartments and structures, occupied by a macromolecular machine. There are three types of cellular components described in the gene ontology: (1) the cellular anatomical entity where a gene product carries out a molecular function (e.g., plasma membrane, cytoskeleton) or membrane-enclosed compartments (e.g., mitochondrion); (2) virion components, where viral proteins act, and (3) the stable macromolecular complexes of which gene product are parts (e.g., the clathrin complex)."""

    CELLULAR_COMPONENT: "PBPKO"
    """cellular_component: A location, relative to cellular compartments and structures, occupied by a macromolecular machine. There are three types of cellular components described in the gene ontology: (1) the cellular anatomical entity where a gene product carries out a molecular function (e.g., plasma membrane, cytoskeleton) or membrane-enclosed compartments (e.g., mitochondrion); (2) virion components, where viral proteins act, and (3) the stable macromolecular complexes of which gene product are parts (e.g., the clathrin complex)."""

    GO_0007588: "PBPKO"
    """excretion."""

    EXCRETION: "PBPKO"
    """excretion."""

    GO_0008150: "PBPKO"
    """biological process: A biological process is the execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence."""

    BIOLOGICAL_PROCESS: "PBPKO"
    """biological process: A biological process is the execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence."""

    GO_0008152: "PBPKO"
    """metabolic process."""

    METABOLIC_PROCESS: "PBPKO"
    """metabolic process."""

    GO_0009987: "PBPKO"
    """cellular process."""

    CELLULAR_PROCESS: "PBPKO"
    """cellular process."""

    GO_0016301: "PBPKO"
    """kinase activity."""

    KINASE_ACTIVITY: "PBPKO"
    """kinase activity."""

    GO_0032501: "PBPKO"
    """multicellular organismal process."""

    MULTICELLULAR_ORGANISMAL_PROCESS: "PBPKO"
    """multicellular organismal process."""

    GO_0032991: "PBPKO"
    """protein-containing complex: A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together."""

    PROTEIN_CONTAINING_COMPLEX: "PBPKO"
    """protein-containing complex: A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together."""

    GO_0044423: "PBPKO"
    """virion component: Any constituent part of a virion, a complete fully infectious extracellular virus particle."""

    VIRION_COMPONENT: "PBPKO"
    """virion component: Any constituent part of a virion, a complete fully infectious extracellular virus particle."""

    GO_0110165: "PBPKO"
    """cellular anatomical entity: A part of a cellular organism that is either an immaterial entity or a material entity with granularity above the level of a protein complex but below that of an anatomical system. Or, a substance produced by a cellular organism with granularity above the level of a protein complex."""

    CELLULAR_ANATOMICAL_ENTITY: "PBPKO"
    """cellular anatomical entity: A part of a cellular organism that is either an immaterial entity or a material entity with granularity above the level of a protein complex but below that of an anatomical system. Or, a substance produced by a cellular organism with granularity above the level of a protein complex."""

    IAO_0000003: "PBPKO"
    """measurement unit label: A measurement unit label is as a label that is part of a scalar measurement datum and denotes a unit of measure."""

    MEASUREMENT_UNIT_LABEL: "PBPKO"
    """measurement unit label: A measurement unit label is as a label that is part of a scalar measurement datum and denotes a unit of measure."""

    IAO_0000005: "PBPKO"
    """objective specification: A directive information entity that describes an intended process endpoint. When part of a plan specification the concretization is realized in a planned process in which the bearer tries to effect the world so that the process endpoint is achieved."""

    OBJECTIVE_SPECIFICATION: "PBPKO"
    """objective specification: A directive information entity that describes an intended process endpoint. When part of a plan specification the concretization is realized in a planned process in which the bearer tries to effect the world so that the process endpoint is achieved."""

    IAO_0000009: "PBPKO"
    """datum label: A label is a symbol that is part of some other datum and is used to either partially define the denotation of that datum or to provide a means for identifying the datum as a member of the set of data with the same label"""

    DATUM_LABEL: "PBPKO"
    """datum label: A label is a symbol that is part of some other datum and is used to either partially define the denotation of that datum or to provide a means for identifying the datum as a member of the set of data with the same label"""

    IAO_0000010: "PBPKO"
    """software: Software is a plan specification composed of a series of instructions that can be interpreted by or directly executed by a processing unit."""

    SOFTWARE: "PBPKO"
    """software: Software is a plan specification composed of a series of instructions that can be interpreted by or directly executed by a processing unit."""

    IAO_0000027: "PBPKO"
    """data entity: An information content entity that is intended to be one or more truthful statement(s) about something (modulo, e.g., measurement precision or other systematic errors) and is constructed/acquired by a method which reliably tends to produce (approximately) truthful statements."""

    DATA_ENTITY: "PBPKO"
    """data entity: An information content entity that is intended to be one or more truthful statement(s) about something (modulo, e.g., measurement precision or other systematic errors) and is constructed/acquired by a method which reliably tends to produce (approximately) truthful statements."""

    IAO_0000030: "PBPKO"
    """information content entity: A generically dependent continuant that is about some thing."""

    INFORMATION_CONTENT_ENTITY: "PBPKO"
    """information content entity: A generically dependent continuant that is about some thing."""

    IAO_0000033: "PBPKO"
    """directive information entity: An information content entity whose concretizations indicate to their bearer how to realize them in a process."""

    DIRECTIVE_INFORMATION_ENTITY: "PBPKO"
    """directive information entity: An information content entity whose concretizations indicate to their bearer how to realize them in a process."""

    IAO_0000037: "PBPKO"
    """dot plot: A dot plot is a report graph which is a graphical representation of data where each data point is represented by a single dot placed on coordinates corresponding to data point values in particular dimensions."""

    DOT_PLOT: "PBPKO"
    """dot plot: A dot plot is a report graph which is a graphical representation of data where each data point is represented by a single dot placed on coordinates corresponding to data point values in particular dimensions."""

    IAO_0000038: "PBPKO"
    """graph: A diagram that presents one or more tuples of information by mapping those tuples in to a two dimensional space in a non arbitrary way."""

    GRAPH: "PBPKO"
    """graph: A diagram that presents one or more tuples of information by mapping those tuples in to a two dimensional space in a non arbitrary way."""

    IAO_0000064: "PBPKO"
    """algorithm: A plan specification which describes the inputs and output of mathematical functions as well as workflow of execution for achieving an predefined objective. Algorithms are realized usually by means of implementation as computer programs for execution by automata."""

    ALGORITHM: "PBPKO"
    """algorithm: A plan specification which describes the inputs and output of mathematical functions as well as workflow of execution for achieving an predefined objective. Algorithms are realized usually by means of implementation as computer programs for execution by automata."""

    IAO_0000078: "PBPKO"
    """curation status specification: The curation status of the term. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value."""

    CURATION_STATUS_SPECIFICATION: "PBPKO"
    """curation status specification: The curation status of the term. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value."""

    IAO_0000098: "PBPKO"
    """data format specification: A data format specification is the information content borne by the document published defining the specification. Example: The ISO document specifying what encompasses an XML document; The instructions in a XSD file"""

    DATA_FORMAT_SPECIFICATION: "PBPKO"
    """data format specification: A data format specification is the information content borne by the document published defining the specification. Example: The ISO document specifying what encompasses an XML document; The instructions in a XSD file"""

    IAO_0000100: "PBPKO"
    """homogenous data collection: A data item that is an aggregate of other data items of the same type that have something in common. Averages and distributions can be determined for data sets."""

    HOMOGENOUS_DATA_COLLECTION: "PBPKO"
    """homogenous data collection: A data item that is an aggregate of other data items of the same type that have something in common. Averages and distributions can be determined for data sets."""

    IAO_0000101: "PBPKO"
    """image: An image is an affine projection to a two dimensional surface, of measurements of some quality of an entity or entities repeated at regular intervals across a spatial range, where the measurements are represented as color and luminosity on the projected on surface."""

    IMAGE: "PBPKO"
    """image: An image is an affine projection to a two dimensional surface, of measurements of some quality of an entity or entities repeated at regular intervals across a spatial range, where the measurements are represented as color and luminosity on the projected on surface."""

    IAO_0000102: "PBPKO"
    """data about an ontology part: Data about an ontology part is a data item about a part of an ontology, for example a term"""

    DATA_ABOUT_AN_ONTOLOGY_PART: "PBPKO"
    """data about an ontology part: Data about an ontology part is a data item about a part of an ontology, for example a term"""

    IAO_0000104: "PBPKO"
    """plan specification: A directive information entity with action specifications and objective specifications as parts, and that may be concretized as a realizable entity that, if realized, is realized in a process in which the bearer tries to achieve the objectives by taking the actions specified."""

    PLAN_SPECIFICATION: "PBPKO"
    """plan specification: A directive information entity with action specifications and objective specifications as parts, and that may be concretized as a realizable entity that, if realized, is realized in a process in which the bearer tries to achieve the objectives by taking the actions specified."""

    IAO_0000136: "PBPKO"
    """is about: A (currently) primitive relation that relates an information artifact to an entity."""

    IS_ABOUT: "PBPKO"
    """is about: A (currently) primitive relation that relates an information artifact to an entity."""

    IAO_0000179: "PBPKO"
    """histogram: A histogram is a report graph which is a statistical description of a distribution in terms of occurrence frequencies of different event classes."""

    HISTOGRAM: "PBPKO"
    """histogram: A histogram is a report graph which is a statistical description of a distribution in terms of occurrence frequencies of different event classes."""

    IAO_0000180: "PBPKO"
    """heatmap: A heatmap is a report graph which is a graphical representation of data where the values taken by a variable(s) are shown as colors in a two-dimensional map."""

    HEATMAP: "PBPKO"
    """heatmap: A heatmap is a report graph which is a graphical representation of data where the values taken by a variable(s) are shown as colors in a two-dimensional map."""

    IAO_0000183: "PBPKO"
    """dendrogram: A dendrogram is a report graph which is a tree diagram frequently used to illustrate the arrangement of the clusters produced by a clustering algorithm."""

    DENDROGRAM: "PBPKO"
    """dendrogram: A dendrogram is a report graph which is a tree diagram frequently used to illustrate the arrangement of the clusters produced by a clustering algorithm."""

    IAO_0000184: "PBPKO"
    """scatter plot: A scatterplot is a graph which uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis."""

    SCATTER_PLOT: "PBPKO"
    """scatter plot: A scatterplot is a graph which uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis."""

    IAO_0000225: "PBPKO"
    """obsolescence reason specification: The reason for which a term has been deprecated. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value."""

    OBSOLESCENCE_REASON_SPECIFICATION: "PBPKO"
    """obsolescence reason specification: The reason for which a term has been deprecated. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value."""

    IAO_0000308: "PBPKO"
    """figure: An information content entity consisting of a two dimensional arrangement of information content entities such that the arrangement itself is about something."""

    FIGURE: "PBPKO"
    """figure: An information content entity consisting of a two dimensional arrangement of information content entities such that the arrangement itself is about something."""

    IAO_0000310: "PBPKO"
    """document: A collection of information content entities intended to be understood together as a whole"""

    DOCUMENT: "PBPKO"
    """document: A collection of information content entities intended to be understood together as a whole"""

    IAO_0000409: "PBPKO"
    """denotator type: A denotator type indicates how a term should be interpreted from an ontological perspective."""

    DENOTATOR_TYPE: "PBPKO"
    """denotator type: A denotator type indicates how a term should be interpreted from an ontological perspective."""

    IAO_0001000: "PBPKO"
    """data collection: A data entity that consists of multiple data entities."""

    DATA_COLLECTION: "PBPKO"
    """data collection: A data entity that consists of multiple data entities."""

    NCBITaxon_117571: "PBPKO"
    """Euteleostomi."""

    EUTELEOSTOMI: "PBPKO"
    """Euteleostomi."""

    NCBITaxon_2759: "PBPKO"
    """Eukaryota."""

    EUKARYOTA: "PBPKO"
    """Eukaryota."""

    NCBITaxon_314146: "PBPKO"
    """Euarchontoglires."""

    EUARCHONTOGLIRES: "PBPKO"
    """Euarchontoglires."""

    NCBITaxon_32523: "PBPKO"
    """Tetrapoda."""

    TETRAPODA: "PBPKO"
    """Tetrapoda."""

    NCBITaxon_32524: "PBPKO"
    """Amniota."""

    AMNIOTA: "PBPKO"
    """Amniota."""

    NCBITaxon_33154: "PBPKO"
    """Opisthokonta."""

    OPISTHOKONTA: "PBPKO"
    """Opisthokonta."""

    NCBITaxon_33208: "PBPKO"
    """Metazoa."""

    METAZOA: "PBPKO"
    """Metazoa."""

    NCBITaxon_33213: "PBPKO"
    """Bilateria."""

    BILATERIA: "PBPKO"
    """Bilateria."""

    NCBITaxon_40674: "PBPKO"
    """Mammalia."""

    MAMMALIA: "PBPKO"
    """Mammalia."""

    NCBITaxon_7742: "PBPKO"
    """Vertebrata <vertebrates>."""

    VERTEBRATA__VERTEBRATES_: "PBPKO"
    """Vertebrata <vertebrates>."""

    NCBITaxon_9606: "PBPKO"
    """Homo sapiens."""

    HOMO_SAPIENS: "PBPKO"
    """Homo sapiens."""

    OBI_0000014: "PBPKO"
    """regulator role: a regulatory role involved with making and/or enforcing relevant legislation and governmental orders"""

    REGULATOR_ROLE: "PBPKO"
    """regulator role: a regulatory role involved with making and/or enforcing relevant legislation and governmental orders"""

    OBI_0000017: "PBPKO"
    """regulatory role: a role which inheres in material entities and is realized in the processes of making, enforcing or being defined by legislation or orders issued by a governmental body."""

    REGULATORY_ROLE: "PBPKO"
    """regulatory role: a role which inheres in material entities and is realized in the processes of making, enforcing or being defined by legislation or orders issued by a governmental body."""

    OBI_0000018: "PBPKO"
    """material supplier role: a role realized through the process of supplying materials such as animal subjects, reagents or other materials used in an investigation."""

    MATERIAL_SUPPLIER_ROLE: "PBPKO"
    """material supplier role: a role realized through the process of supplying materials such as animal subjects, reagents or other materials used in an investigation."""

    OBI_0000023: "PBPKO"
    """classified data set: A data set that is produced as the output of a class prediction data transformation and consists of a data set with assigned class labels."""

    CLASSIFIED_DATA_SET: "PBPKO"
    """classified data set: A data set that is produced as the output of a class prediction data transformation and consists of a data set with assigned class labels."""

    OBI_0000112: "PBPKO"
    """specimen role: A role borne by a material entity that is obtained during a specimen collection process and that can be realized by performing measurements or observations on the specimen."""

    SPECIMEN_ROLE: "PBPKO"
    """specimen role: A role borne by a material entity that is obtained during a specimen collection process and that can be realized by performing measurements or observations on the specimen."""

    OBI_0000245: "PBPKO"
    """organization: An entity that can bear roles, has members, and has a set of organization rules. Members of organizations are either organizations themselves or individual people. Members can bear specific organization member roles that are determined in the organization rules. The organization rules also determine how decisions are made on behalf of the organization by the organization members."""

    ORGANIZATION: "PBPKO"
    """organization: An entity that can bear roles, has members, and has a set of organization rules. Members of organizations are either organizations themselves or individual people. Members can bear specific organization member roles that are determined in the organization rules. The organization rules also determine how decisions are made on behalf of the organization by the organization members."""

    OBI_0000260: "PBPKO"
    """plan: A plan is a realizable entity that is the inheres in a bearer who is committed to realizing it as a completely executed planned process."""

    PLAN: "PBPKO"
    """plan: A plan is a realizable entity that is the inheres in a bearer who is committed to realizing it as a completely executed planned process."""

    OBI_0000293: "PBPKO"
    """has specified input: The inverse property of is specified input of"""

    HAS_SPECIFIED_INPUT: "PBPKO"
    """has specified input: The inverse property of is specified input of"""

    OBI_0000295: "PBPKO"
    """is specified input of: A relation between a completely executed planned process and a continuant participating in that process that is not created during the process. The presence of the continuant during the process is explicitly specified in the plan specification which the process realizes the concretization of."""

    IS_SPECIFIED_INPUT_OF: "PBPKO"
    """is specified input of: A relation between a completely executed planned process and a continuant participating in that process that is not created during the process. The presence of the continuant during the process is explicitly specified in the plan specification which the process realizes the concretization of."""

    OBI_0000299: "PBPKO"
    """has specified output: The inverse property of is specified output of"""

    HAS_SPECIFIED_OUTPUT: "PBPKO"
    """has specified output: The inverse property of is specified output of"""

    OBI_0000312: "PBPKO"
    """is specified output of: A relation between a completely executed planned process and a continuant participating in that process. The presence of the continuant at the end of the process is explicitly specified in the objective specification which the process realizes the concretization of."""

    IS_SPECIFIED_OUTPUT_OF: "PBPKO"
    """is specified output of: A relation between a completely executed planned process and a continuant participating in that process. The presence of the continuant at the end of the process is explicitly specified in the objective specification which the process realizes the concretization of."""

    OBI_0000417: "PBPKO"
    """achieves_planned_objective: This relation obtains between a planned process and a objective specification when the criteria specified in the objective specification are met at the end of the planned process."""

    ACHIEVES_PLANNED_OBJECTIVE: "PBPKO"
    """achieves_planned_objective: This relation obtains between a planned process and a objective specification when the criteria specified in the objective specification are met at the end of the planned process."""

    OBI_0000450: "PBPKO"
    """regulatory agency: A regulatory agency is a organization that has responsibility over or for the legislation (acts and regulations) for a given sector of the government."""

    REGULATORY_AGENCY: "PBPKO"
    """regulatory agency: A regulatory agency is a organization that has responsibility over or for the legislation (acts and regulations) for a given sector of the government."""

    OBI_0000571: "PBPKO"
    """manufacturer role: Manufacturer role is a role which inheres in a person or organization and which is realized by a manufacturing process."""

    MANUFACTURER_ROLE: "PBPKO"
    """manufacturer role: Manufacturer role is a role which inheres in a person or organization and which is realized by a manufacturing process."""

    OBI_0000648: "PBPKO"
    """clustered data set: A data set that is produced as the output of a class discovery data transformation and consists of a data set with assigned discovered class labels."""

    CLUSTERED_DATA_SET: "PBPKO"
    """clustered data set: A data set that is produced as the output of a class discovery data transformation and consists of a data set with assigned discovered class labels."""

    OBI_0000658: "PBPKO"
    """data representational model: An information content entity representing the relationships between data items."""

    DATA_REPRESENTATIONAL_MODEL: "PBPKO"
    """data representational model: An information content entity representing the relationships between data items."""

    OBI_0000659: "PBPKO"
    """specimen collection process: A planned process with the objective to obtain a material entity for potential use as an input upon which measurements or observations are performed."""

    SPECIMEN_COLLECTION_PROCESS: "PBPKO"
    """specimen collection process: A planned process with the objective to obtain a material entity for potential use as an input upon which measurements or observations are performed."""

    OBI_0000663: "PBPKO"
    """class prediction data transformation: A class prediction data transformation (sometimes called supervised classification) is a data transformation that has objective class prediction."""

    CLASS_PREDICTION_DATA_TRANSFORMATION: "PBPKO"
    """class prediction data transformation: A class prediction data transformation (sometimes called supervised classification) is a data transformation that has objective class prediction."""

    OBI_0000684: "PBPKO"
    """specimen collection objective: A objective specification that is fulfilled by obtaining a material entity for potential use as an input upon which measurements or observations are performed."""

    SPECIMEN_COLLECTION_OBJECTIVE: "PBPKO"
    """specimen collection objective: A objective specification that is fulfilled by obtaining a material entity for potential use as an input upon which measurements or observations are performed."""

    OBI_0000700: "PBPKO"
    """support vector machine: A support vector machine is a data transformation with a class prediction objective based on the construction of a separating hyperplane that maximizes the margin between two data sets of vectors in n-dimensional space."""

    SUPPORT_VECTOR_MACHINE: "PBPKO"
    """support vector machine: A support vector machine is a data transformation with a class prediction objective based on the construction of a separating hyperplane that maximizes the margin between two data sets of vectors in n-dimensional space."""

    OBI_0000704: "PBPKO"
    """decision tree induction objective: A decision tree induction objective is a data transformation objective in which a tree-like graph of edges and nodes is created and from which the selection of each branch requires that some type of logical decision is made."""

    DECISION_TREE_INDUCTION_OBJECTIVE: "PBPKO"
    """decision tree induction objective: A decision tree induction objective is a data transformation objective in which a tree-like graph of edges and nodes is created and from which the selection of each branch requires that some type of logical decision is made."""

    OBI_0000707: "PBPKO"
    """decision tree building data transformation: A decision tree building data transformation is a data transformation that has objective decision tree induction."""

    DECISION_TREE_BUILDING_DATA_TRANSFORMATION: "PBPKO"
    """decision tree building data transformation: A decision tree building data transformation is a data transformation that has objective decision tree induction."""

    OBI_0000713: "PBPKO"
    """GenePattern software: a software that provides access to more than 100 tools for gene expression analysis, proteomics, SNP analysis and common data processing tasks."""

    GENEPATTERN_SOFTWARE: "PBPKO"
    """GenePattern software: a software that provides access to more than 100 tools for gene expression analysis, proteomics, SNP analysis and common data processing tasks."""

    OBI_0000726: "PBPKO"
    """peak matching: Peak matching is a data transformation performed on a dataset of a graph of ordered data points (e.g. a spectrum) with the objective of pattern matching local maxima above a noise threshold"""

    PEAK_MATCHING: "PBPKO"
    """peak matching: Peak matching is a data transformation performed on a dataset of a graph of ordered data points (e.g. a spectrum) with the objective of pattern matching local maxima above a noise threshold"""

    OBI_0000727: "PBPKO"
    """k-nearest neighbors: A k-nearest neighbors is a data transformation which achieves a class discovery or partitioning objective, in which an input data object with vector y is assigned to a class label based upon the k closest training data set points to y; where k is the largest value that class label is assigned."""

    K_NEAREST_NEIGHBORS: "PBPKO"
    """k-nearest neighbors: A k-nearest neighbors is a data transformation which achieves a class discovery or partitioning objective, in which an input data object with vector y is assigned to a class label based upon the k closest training data set points to y; where k is the largest value that class label is assigned."""

    OBI_0000749: "PBPKO"
    """CART: A CART (classification and regression trees) is a data transformation method for producing a classification or regression model with a tree-based structure."""

    CART: "PBPKO"
    """CART: A CART (classification and regression trees) is a data transformation method for producing a classification or regression model with a tree-based structure."""

    OBI_0000792: "PBPKO"
    """statistical model validation: A data transformation which assesses how the results of a statistical analysis will generalize to an independent data set."""

    STATISTICAL_MODEL_VALIDATION: "PBPKO"
    """statistical model validation: A data transformation which assesses how the results of a statistical analysis will generalize to an independent data set."""

    OBI_0000833: "PBPKO"
    """objective_achieved_by: This relation obtains between an objective specification and a planned process when the criteria specified in the objective specification are met at the end of the planned process."""

    OBJECTIVE_ACHIEVED_BY: "PBPKO"
    """objective_achieved_by: This relation obtains between an objective specification and a planned process when the criteria specified in the objective specification are met at the end of the planned process."""

    OBI_0000835: "PBPKO"
    """manufacturer: A person or organization that has a manufacturer role."""

    MANUFACTURER: "PBPKO"
    """manufacturer: A person or organization that has a manufacturer role."""

    OBI_0000947: "PBPKO"
    """service provider role: is a role which inheres in a person or organization and is realized in in a planned process which provides access to training, materials or execution of protocols for an organization or person"""

    SERVICE_PROVIDER_ROLE: "PBPKO"
    """service provider role: is a role which inheres in a person or organization and is realized in in a planned process which provides access to training, materials or execution of protocols for an organization or person"""

    OBI_0000963: "PBPKO"
    """categorical label: A label that is part of a categorical datum and that indicates the value of the data item on the categorical scale."""

    CATEGORICAL_LABEL: "PBPKO"
    """categorical label: A label that is part of a categorical datum and that indicates the value of the data item on the categorical scale."""

    OBI_0001000: "PBPKO"
    """questionnaire: A document with a set of printed or written questions with a choice of answers, devised for the purposes of a survey or statistical study."""

    QUESTIONNAIRE: "PBPKO"
    """questionnaire: A document with a set of printed or written questions with a choice of answers, devised for the purposes of a survey or statistical study."""

    OBI_0001468: "PBPKO"
    """cell specimen: A specimen primarily composed of a cell or cells collected from a multicellular organism or a cell culture."""

    CELL_SPECIMEN: "PBPKO"
    """cell specimen: A specimen primarily composed of a cell or cells collected from a multicellular organism or a cell culture."""

    OBI_0001479: "PBPKO"
    """specimen from organism: A specimen that derives from an anatomical part or substance arising from an organism. Examples of tissue specimen include tissue, organ, physiological system, blood, or body location (arm)."""

    SPECIMEN_FROM_ORGANISM: "PBPKO"
    """specimen from organism: A specimen that derives from an anatomical part or substance arising from an organism. Examples of tissue specimen include tissue, organ, physiological system, blood, or body location (arm)."""

    OBI_0001930: "PBPKO"
    """categorical value specification: A value specification that is specifies one category out of a fixed number of nominal categories"""

    CATEGORICAL_VALUE_SPECIFICATION: "PBPKO"
    """categorical value specification: A value specification that is specifies one category out of a fixed number of nominal categories"""

    OBI_0001933: "PBPKO"
    """value specification: An information content entity that specifies a value within a classification scheme or on a quantitative scale."""

    VALUE_SPECIFICATION: "PBPKO"
    """value specification: An information content entity that specifies a value within a classification scheme or on a quantitative scale."""

    OBI_0002076: "PBPKO"
    """collection of specimens: A material entity that has two or more specimens as its parts."""

    COLLECTION_OF_SPECIMENS: "PBPKO"
    """collection of specimens: A material entity that has two or more specimens as its parts."""

    OBI_0002205: "PBPKO"
    """histologic grade according to AJCC 7th edition: A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the American Joint Committee on Cancer (AJCC) 7th Edition grading system."""

    HISTOLOGIC_GRADE_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """histologic grade according to AJCC 7th edition: A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the American Joint Committee on Cancer (AJCC) 7th Edition grading system."""

    OBI_0002210: "PBPKO"
    """histologic grade according to the Fuhrman Nuclear Grading System: A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the Fuhrman Nuclear Grading System."""

    HISTOLOGIC_GRADE_ACCORDING_TO_THE_FUHRMAN_NUCLEAR_GRADING_SYSTEM: "PBPKO"
    """histologic grade according to the Fuhrman Nuclear Grading System: A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the Fuhrman Nuclear Grading System."""

    OBI_0002215: "PBPKO"
    """histologic grade for ovarian tumor: A categorical value specification that is a histologic grade assigned to a ovarian tumor."""

    HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR: "PBPKO"
    """histologic grade for ovarian tumor: A categorical value specification that is a histologic grade assigned to a ovarian tumor."""

    OBI_0002216: "PBPKO"
    """histologic grade for ovarian tumor according to a two-tier grading system: A histologic grade for ovarian tumor that is from a two-tier histological classification of tumors."""

    HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR_ACCORDING_TO_A_TWO_TIER_GRADING_SYSTEM: "PBPKO"
    """histologic grade for ovarian tumor according to a two-tier grading system: A histologic grade for ovarian tumor that is from a two-tier histological classification of tumors."""

    OBI_0002219: "PBPKO"
    """histologic grade for ovarian tumor according to the World Health Organization: A histologic grade for ovarian tumor that is from a histological classification by the World Health Organization (WHO)."""

    HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR_ACCORDING_TO_THE_WORLD_HEALTH_ORGANIZATION: (
        "PBPKO"
    )
    """histologic grade for ovarian tumor according to the World Health Organization: A histologic grade for ovarian tumor that is from a histological classification by the World Health Organization (WHO)."""

    OBI_0002224: "PBPKO"
    """pathologic primary tumor stage for colon and rectum according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_COLON_AND_RECTUM_ACCORDING_TO_AJCC_7TH_EDITION: (
        "PBPKO"
    )
    """pathologic primary tumor stage for colon and rectum according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002232: "PBPKO"
    """pathologic primary tumor stage for lung according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic primary tumor stage for lung according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002243: "PBPKO"
    """pathologic primary tumor stage for kidney according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic primary tumor stage for kidney according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002256: "PBPKO"
    """pathologic primary tumor stage for ovary according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic primary tumor stage for ovary according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002270: "PBPKO"
    """pathologic lymph node stage for colon and rectum according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_COLON_AND_RECTUM_ACCORDING_TO_AJCC_7TH_EDITION: (
        "PBPKO"
    )
    """pathologic lymph node stage for colon and rectum according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    OBI_0002279: "PBPKO"
    """pathologic lymph node stage for lung according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic lymph node stage for lung according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    OBI_0002284: "PBPKO"
    """pathologic lymph node stage for kidney according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic lymph node stage for kidney according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    OBI_0002287: "PBPKO"
    """pathologic lymph node stage for ovary according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic lymph node stage for ovary according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes."""

    OBI_0002290: "PBPKO"
    """pathologic distant metastases stage for colon according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of colon cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_COLON_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic distant metastases stage for colon according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of colon cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002298: "PBPKO"
    """pathologic distant metastases stage for lung according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic distant metastases stage for lung according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002306: "PBPKO"
    """pathologic distant metastases stage for kidney according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION: (
        "PBPKO"
    )
    """pathologic distant metastases stage for kidney according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002310: "PBPKO"
    """pathologic distant metastases stage for ovary according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """pathologic distant metastases stage for ovary according to AJCC 7th edition: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery."""

    OBI_0002314: "PBPKO"
    """clinical tumor stage group according to AJCC 7th edition: A categorical value specification that is an assessment of the stage of a cancer according to the American Joint Committee on Cancer (AJCC) v7 staging systems."""

    CLINICAL_TUMOR_STAGE_GROUP_ACCORDING_TO_AJCC_7TH_EDITION: "PBPKO"
    """clinical tumor stage group according to AJCC 7th edition: A categorical value specification that is an assessment of the stage of a cancer according to the American Joint Committee on Cancer (AJCC) v7 staging systems."""

    OBI_0002326: "PBPKO"
    """International Federation of Gynecology and Obstetrics cervical cancer stage value specification: A categorical value specification that is an assessment of the stage of a gynecologic cancer according to the International Federation of Gynecology and Obstetrics (FIGO) staging systems."""

    INTERNATIONAL_FEDERATION_OF_GYNECOLOGY_AND_OBSTETRICS_CERVICAL_CANCER_STAGE_VALUE_SPECIFICATION: "PBPKO"
    """International Federation of Gynecology and Obstetrics cervical cancer stage value specification: A categorical value specification that is an assessment of the stage of a gynecologic cancer according to the International Federation of Gynecology and Obstetrics (FIGO) staging systems."""

    OBI_0002341: "PBPKO"
    """International Federation of Gynecology and Obstetrics ovarian cancer stage value specification: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the FIGO classification system."""

    INTERNATIONAL_FEDERATION_OF_GYNECOLOGY_AND_OBSTETRICS_OVARIAN_CANCER_STAGE_VALUE_SPECIFICATION: "PBPKO"
    """International Federation of Gynecology and Obstetrics ovarian cancer stage value specification: A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the FIGO classification system."""

    OBI_0002356: "PBPKO"
    """performance status value specification: A categorical value specification that is an assessment of a participant's performance status (general well-being and activities of daily life)."""

    PERFORMANCE_STATUS_VALUE_SPECIFICATION: "PBPKO"
    """performance status value specification: A categorical value specification that is an assessment of a participant's performance status (general well-being and activities of daily life)."""

    OBI_0002357: "PBPKO"
    """Eastern Cooperative Oncology Group score value specification: A performance status value specification designed by the Eastern Cooperative Oncology Group to assess disease progression and its affect on the daily living abilities of the patient."""

    EASTERN_COOPERATIVE_ONCOLOGY_GROUP_SCORE_VALUE_SPECIFICATION: "PBPKO"
    """Eastern Cooperative Oncology Group score value specification: A performance status value specification designed by the Eastern Cooperative Oncology Group to assess disease progression and its affect on the daily living abilities of the patient."""

    OBI_0002363: "PBPKO"
    """Karnofsky score vaue specification: A performance status value specification designed for classifying patients 16 years of age or older by their functional impairment."""

    KARNOFSKY_SCORE_VAUE_SPECIFICATION: "PBPKO"
    """Karnofsky score vaue specification: A performance status value specification designed for classifying patients 16 years of age or older by their functional impairment."""

    OBI_0002989: "PBPKO"
    """material supplier: A person or organization that provides material supplies to other people or organizations."""

    MATERIAL_SUPPLIER: "PBPKO"
    """material supplier: A person or organization that provides material supplies to other people or organizations."""

    OBI_0100051: "PBPKO"
    """specimen: A material entity that is collected for potential use as an input upon which measurements or observations are performed."""

    SPECIMEN: "PBPKO"
    """specimen: A material entity that is collected for potential use as an input upon which measurements or observations are performed."""

    OBI_0200000: "PBPKO"
    """data transformation: A completely executed planned process that produces output data from input data."""

    DATA_TRANSFORMATION: "PBPKO"
    """data transformation: A completely executed planned process that produces output data from input data."""

    OBI_0200033: "PBPKO"
    """leave one out cross validation method: is a data transformation : leave-one-out cross-validation (LOOCV) involves using a single observation from the original sample as the validation data, and the remaining observations as the training data. This is repeated such that each observation in the sample is used once as the validation data"""

    LEAVE_ONE_OUT_CROSS_VALIDATION_METHOD: "PBPKO"
    """leave one out cross validation method: is a data transformation : leave-one-out cross-validation (LOOCV) involves using a single observation from the original sample as the validation data, and the remaining observations as the training data. This is repeated such that each observation in the sample is used once as the validation data"""

    OBI_0200041: "PBPKO"
    """k-means clustering: A k-means clustering is a data transformation which achieves a class discovery or partitioning objective, which takes as input a collection of objects (represented as points in multidimensional space) and which partitions them into a specified number k of clusters. The algorithm attempts to find the centers of natural clusters in the data. The most common form of the algorithm starts by partitioning the input points into k initial sets, either at random or using some heuristic data. It then calculates the mean point, or centroid, of each set. It constructs a new partition by associating each point with the closest centroid. Then the centroids are recalculated for the new clusters, and the algorithm repeated by alternate applications of these two steps until convergence, which is obtained when the points no longer switch clusters (or alternatively centroids are no longer changed)."""

    K_MEANS_CLUSTERING: "PBPKO"
    """k-means clustering: A k-means clustering is a data transformation which achieves a class discovery or partitioning objective, which takes as input a collection of objects (represented as points in multidimensional space) and which partitions them into a specified number k of clusters. The algorithm attempts to find the centers of natural clusters in the data. The most common form of the algorithm starts by partitioning the input points into k initial sets, either at random or using some heuristic data. It then calculates the mean point, or centroid, of each set. It constructs a new partition by associating each point with the closest centroid. Then the centroids are recalculated for the new clusters, and the algorithm repeated by alternate applications of these two steps until convergence, which is obtained when the points no longer switch clusters (or alternatively centroids are no longer changed)."""

    OBI_0200042: "PBPKO"
    """hierarchical clustering: A hierarchical clustering is a data transformation which achieves a class discovery objective, which takes as input data item and builds a hierarchy of clusters. The traditional representation of this hierarchy is a tree (visualized by a dendrogram), with the individual input objects at one end (leaves) and a single cluster containing every object at the other (root)."""

    HIERARCHICAL_CLUSTERING: "PBPKO"
    """hierarchical clustering: A hierarchical clustering is a data transformation which achieves a class discovery objective, which takes as input data item and builds a hierarchy of clusters. The traditional representation of this hierarchy is a tree (visualized by a dendrogram), with the individual input objects at one end (leaves) and a single cluster containing every object at the other (root)."""

    OBI_0200050: "PBPKO"
    """dimensionality reduction: A dimensionality reduction is data partitioning which transforms each input m-dimensional vector (x_1, x_2, ..., x_m) into an output n-dimensional vector (y_1, y_2, ..., y_n), where n is smaller than m."""

    DIMENSIONALITY_REDUCTION: "PBPKO"
    """dimensionality reduction: A dimensionality reduction is data partitioning which transforms each input m-dimensional vector (x_1, x_2, ..., x_m) into an output n-dimensional vector (y_1, y_2, ..., y_n), where n is smaller than m."""

    OBI_0200051: "PBPKO"
    """principal components analysis dimensionality reduction: A principal components analysis dimensionality reduction is a dimensionality reduction achieved by applying principal components analysis and by keeping low-order principal components and excluding higher-order ones."""

    PRINCIPAL_COMPONENTS_ANALYSIS_DIMENSIONALITY_REDUCTION: "PBPKO"
    """principal components analysis dimensionality reduction: A principal components analysis dimensionality reduction is a dimensionality reduction achieved by applying principal components analysis and by keeping low-order principal components and excluding higher-order ones."""

    OBI_0200111: "PBPKO"
    """data visualization: A planned process with the objective to graphically represent some data by inputing the data and outputting images, diagrams or animations."""

    DATA_VISUALIZATION: "PBPKO"
    """data visualization: A planned process with the objective to graphically represent some data by inputing the data and outputting images, diagrams or animations."""

    OBI_0200166: "PBPKO"
    """data transformation objective: An objective specification to transformation input data into output data"""

    DATA_TRANSFORMATION_OBJECTIVE: "PBPKO"
    """data transformation objective: An objective specification to transformation input data into output data"""

    OBI_0200171: "PBPKO"
    """partitioning data transformation: A partitioning data transformation is a data transformation that has objective partitioning."""

    PARTITIONING_DATA_TRANSFORMATION: "PBPKO"
    """partitioning data transformation: A partitioning data transformation is a data transformation that has objective partitioning."""

    OBI_0200172: "PBPKO"
    """partitioning objective: A partitioning objective is a data transformation objective where the aim is to generate a collection of disjoint non-empty subsets whose union equals a non-empty input set."""

    PARTITIONING_OBJECTIVE: "PBPKO"
    """partitioning objective: A partitioning objective is a data transformation objective where the aim is to generate a collection of disjoint non-empty subsets whose union equals a non-empty input set."""

    OBI_0200175: "PBPKO"
    """class discovery data transformation: A class discovery data transformation (sometimes called unsupervised classification) is a data transformation that has objective class discovery."""

    CLASS_DISCOVERY_DATA_TRANSFORMATION: "PBPKO"
    """class discovery data transformation: A class discovery data transformation (sometimes called unsupervised classification) is a data transformation that has objective class discovery."""

    OBI_0200178: "PBPKO"
    """class discovery objective: A class discovery objective (sometimes called unsupervised classification) is a data transformation objective where the aim is to organize input data (typically vectors of attributes) into classes, where the number of classes and their specifications are not known a priori. Depending on usage, the class assignment can be definite or probabilistic."""

    CLASS_DISCOVERY_OBJECTIVE: "PBPKO"
    """class discovery objective: A class discovery objective (sometimes called unsupervised classification) is a data transformation objective where the aim is to organize input data (typically vectors of attributes) into classes, where the number of classes and their specifications are not known a priori. Depending on usage, the class assignment can be definite or probabilistic."""

    OBI_0200179: "PBPKO"
    """class prediction objective: A class prediction objective (sometimes called supervised classification) is a data transformation objective where the aim is to create a predictor from training data through a machine learning technique. The training data consist of pairs of objects (typically vectors of attributes) and class labels for these objects. The resulting predictor can be used to attach class labels to any valid novel input object. Depending on usage, the prediction can be definite or probabilistic. A classification is learned from the training data and can then be tested on test data."""

    CLASS_PREDICTION_OBJECTIVE: "PBPKO"
    """class prediction objective: A class prediction objective (sometimes called supervised classification) is a data transformation objective where the aim is to create a predictor from training data through a machine learning technique. The training data consist of pairs of objects (typically vectors of attributes) and class labels for these objects. The resulting predictor can be used to attach class labels to any valid novel input object. Depending on usage, the prediction can be definite or probabilistic. A classification is learned from the training data and can then be tested on test data."""

    OBI_0200188: "PBPKO"
    """cross validation objective: A cross validation objective is a data transformation objective in which the aim is to partition a sample of data into subsets such that the analysis is initially performed on a single subset, while the other subset(s) are retained for subsequent use in confirming and validating the initial analysis."""

    CROSS_VALIDATION_OBJECTIVE: "PBPKO"
    """cross validation objective: A cross validation objective is a data transformation objective in which the aim is to partition a sample of data into subsets such that the analysis is initially performed on a single subset, while the other subset(s) are retained for subsequent use in confirming and validating the initial analysis."""

    OBI_0200190: "PBPKO"
    """clustered data visualization: A data visualization which has input of a clustered data set and produces an output of a report graph which is capable of rendering data of this type."""

    CLUSTERED_DATA_VISUALIZATION: "PBPKO"
    """clustered data visualization: A data visualization which has input of a clustered data set and produces an output of a report graph which is capable of rendering data of this type."""

    PATO_0000001: "PBPKO"
    """quality."""

    PBPKO_00002: "PBPKO"
    """parameter: A data item involved in PBPK modelling."""

    PARAMETER: "PBPKO"
    """parameter: A data item involved in PBPK modelling."""

    PBPKO_00003: "PBPKO"
    """physiologically based pharmacokinetic model: A data representation model that predicts the absorption, distribution, metabolism, and excretion (ADME) of chemical substances in biological species based on physiological principles using mathematical modelling technique."""

    PHYSIOLOGICALLY_BASED_PHARMACOKINETIC_MODEL: "PBPKO"
    """physiologically based pharmacokinetic model: A data representation model that predicts the absorption, distribution, metabolism, and excretion (ADME) of chemical substances in biological species based on physiological principles using mathematical modelling technique."""

    PBPKO_00004: "PBPKO"
    """whole body pbpk: A physiologically based pharmacokinetic model that contains an explicit representation of the organs most relevant to the ADME of the compound."""

    WHOLE_BODY_PBPK: "PBPKO"
    """whole body pbpk: A physiologically based pharmacokinetic model that contains an explicit representation of the organs most relevant to the ADME of the compound."""

    PBPKO_00005: "PBPKO"
    """perfusion limited model: A physiologically based pharmacokinetic model that assumes tissue concentration reaches equilibrium rapidly and uptake/elimination is limited by blood flow rate."""

    PERFUSION_LIMITED_MODEL: "PBPKO"
    """perfusion limited model: A physiologically based pharmacokinetic model that assumes tissue concentration reaches equilibrium rapidly and uptake/elimination is limited by blood flow rate."""

    PBPKO_00006: "PBPKO"
    """physiological parameter: A parameter that provides the structural framework for a PBPK model and relates to the organism's physiology (e.g., body weight, organ volume, blood flow)."""

    PHYSIOLOGICAL_PARAMETER: "PBPKO"
    """physiological parameter: A parameter that provides the structural framework for a PBPK model and relates to the organism's physiology (e.g., body weight, organ volume, blood flow)."""

    PBPKO_00007: "PBPKO"
    """body mass index: A physiological parameter calculated as an individual's weight (kg) divided by the square of their height (m)."""

    BODY_MASS_INDEX: "PBPKO"
    """body mass index: A physiological parameter calculated as an individual's weight (kg) divided by the square of their height (m)."""

    PBPKO_00008: "PBPKO"
    """bodyweight: A physiological parameter representing the mass or quantity of heaviness of an individual."""

    BODYWEIGHT: "PBPKO"
    """bodyweight: A physiological parameter representing the mass or quantity of heaviness of an individual."""

    PBPKO_00009: "PBPKO"
    """height: A physiological parameter describing the distance from the bottom to the top of someone standing upright."""

    HEIGHT: "PBPKO"
    """height: A physiological parameter describing the distance from the bottom to the top of someone standing upright."""

    PBPKO_00010: "PBPKO"
    """surface area: A physiological parameter representing the total area that the surface of an object occupies."""

    SURFACE_AREA: "PBPKO"
    """surface area: A physiological parameter representing the total area that the surface of an object occupies."""

    PBPKO_00011: "PBPKO"
    """assigned race: A parameter representing a geographic ancestral origin category assigned to a population group."""

    ASSIGNED_RACE: "PBPKO"
    """assigned race: A parameter representing a geographic ancestral origin category assigned to a population group."""

    PBPKO_00012: "PBPKO"
    """blood flow rate to compartment: A bodily fluid flow rate parameter representing the rate of blood flow in different parts of the body"""

    BLOOD_FLOW_RATE_TO_COMPARTMENT: "PBPKO"
    """blood flow rate to compartment: A bodily fluid flow rate parameter representing the rate of blood flow in different parts of the body"""

    PBPKO_00013: "PBPKO"
    """cardiac output rate: A blood flow rate parameter representing the volume of blood pumped by the heart compartment per unit of time."""

    CARDIAC_OUTPUT_RATE: "PBPKO"
    """cardiac output rate: A blood flow rate parameter representing the volume of blood pumped by the heart compartment per unit of time."""

    PBPKO_00014: "PBPKO"
    """blood flow rate to stomach: A blood flow rate parameter specifically describing the rate to the stomach compartment."""

    BLOOD_FLOW_RATE_TO_STOMACH: "PBPKO"
    """blood flow rate to stomach: A blood flow rate parameter specifically describing the rate to the stomach compartment."""

    PBPKO_00015: "PBPKO"
    """fraction of blood flow to stomach: The dimensionless fraction of cardiac output delivered to the stomach compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_STOMACH: "PBPKO"
    """fraction of blood flow to stomach: The dimensionless fraction of cardiac output delivered to the stomach compartment."""

    PBPKO_00016: "PBPKO"
    """blood flow rate to intestine: A blood flow parameter specifically describing the rate to the intestine compartment."""

    BLOOD_FLOW_RATE_TO_INTESTINE: "PBPKO"
    """blood flow rate to intestine: A blood flow parameter specifically describing the rate to the intestine compartment."""

    PBPKO_00017: "PBPKO"
    """fraction of blood flow to intestine: The dimensionless fraction of cardiac output delivered to the intestine compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_INTESTINE: "PBPKO"
    """fraction of blood flow to intestine: The dimensionless fraction of cardiac output delivered to the intestine compartment."""

    PBPKO_00018: "PBPKO"
    """blood flow rate to small intestine: A blood flow rate parameter specifically describing the rate to the small intestine compartment."""

    BLOOD_FLOW_RATE_TO_SMALL_INTESTINE: "PBPKO"
    """blood flow rate to small intestine: A blood flow rate parameter specifically describing the rate to the small intestine compartment."""

    PBPKO_00019: "PBPKO"
    """fraction of blood flow to small intestine: The dimensionless fraction of cardiac output delivered to the small intestine compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_SMALL_INTESTINE: "PBPKO"
    """fraction of blood flow to small intestine: The dimensionless fraction of cardiac output delivered to the small intestine compartment."""

    PBPKO_00020: "PBPKO"
    """blood flow rate to large intestine: A blood flow rate parameter specifically describing the rate to the large intestine compartment."""

    BLOOD_FLOW_RATE_TO_LARGE_INTESTINE: "PBPKO"
    """blood flow rate to large intestine: A blood flow rate parameter specifically describing the rate to the large intestine compartment."""

    PBPKO_00021: "PBPKO"
    """fraction of blood flow to large intestine: The dimensionless fraction of cardiac output delivered to the large intestine compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_LARGE_INTESTINE: "PBPKO"
    """fraction of blood flow to large intestine: The dimensionless fraction of cardiac output delivered to the large intestine compartment."""

    PBPKO_00022: "PBPKO"
    """blood flow rate to pancreas: A blood flow rate parameter specifically describing the rate to the pancreas compartment."""

    BLOOD_FLOW_RATE_TO_PANCREAS: "PBPKO"
    """blood flow rate to pancreas: A blood flow rate parameter specifically describing the rate to the pancreas compartment."""

    PBPKO_00023: "PBPKO"
    """fraction of blood flow to pancreas: The dimensionless fraction of cardiac output delivered to the pancreas compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_PANCREAS: "PBPKO"
    """fraction of blood flow to pancreas: The dimensionless fraction of cardiac output delivered to the pancreas compartment."""

    PBPKO_00024: "PBPKO"
    """blood flow rate to liver: A blood flow rate parameter specifically describing the rate to the liver compartment."""

    BLOOD_FLOW_RATE_TO_LIVER: "PBPKO"
    """blood flow rate to liver: A blood flow rate parameter specifically describing the rate to the liver compartment."""

    PBPKO_00025: "PBPKO"
    """fraction of blood flow to liver: The dimensionless fraction of cardiac output delivered to the liver compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_LIVER: "PBPKO"
    """fraction of blood flow to liver: The dimensionless fraction of cardiac output delivered to the liver compartment."""

    PBPKO_00026: "PBPKO"
    """blood flow rate to kidney: A blood flow rate parameter specifically describing the rate to the kidney compartment."""

    BLOOD_FLOW_RATE_TO_KIDNEY: "PBPKO"
    """blood flow rate to kidney: A blood flow rate parameter specifically describing the rate to the kidney compartment."""

    PBPKO_00027: "PBPKO"
    """fraction of blood flow to kidney: The dimensionless fraction of cardiac output delivered to the kidney compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_KIDNEY: "PBPKO"
    """fraction of blood flow to kidney: The dimensionless fraction of cardiac output delivered to the kidney compartment."""

    PBPKO_00028: "PBPKO"
    """blood flow rate to muscle: A blood flow rate parameter specifically describing the rate to the muscle compartment."""

    BLOOD_FLOW_RATE_TO_MUSCLE: "PBPKO"
    """blood flow rate to muscle: A blood flow rate parameter specifically describing the rate to the muscle compartment."""

    PBPKO_00029: "PBPKO"
    """fraction of blood flow to muscle: The dimensionless fraction of cardiac output delivered to the muscle compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_MUSCLE: "PBPKO"
    """fraction of blood flow to muscle: The dimensionless fraction of cardiac output delivered to the muscle compartment."""

    PBPKO_00030: "PBPKO"
    """blood flow rate to heart: A blood flow rate parameter specifically describing the rate to the heart compartment."""

    BLOOD_FLOW_RATE_TO_HEART: "PBPKO"
    """blood flow rate to heart: A blood flow rate parameter specifically describing the rate to the heart compartment."""

    PBPKO_00031: "PBPKO"
    """fraction of blood flow to heart: The dimensionless fraction of cardiac output delivered to the heart compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_HEART: "PBPKO"
    """fraction of blood flow to heart: The dimensionless fraction of cardiac output delivered to the heart compartment."""

    PBPKO_00032: "PBPKO"
    """blood flow rate to fat: A blood flow rate parameter specifically describing the rate to the fat (adipose tissue) compartment."""

    BLOOD_FLOW_RATE_TO_FAT: "PBPKO"
    """blood flow rate to fat: A blood flow rate parameter specifically describing the rate to the fat (adipose tissue) compartment."""

    PBPKO_00033: "PBPKO"
    """fraction of blood flow to fat: The dimensionless fraction of cardiac output delivered to the fat compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_FAT: "PBPKO"
    """fraction of blood flow to fat: The dimensionless fraction of cardiac output delivered to the fat compartment."""

    PBPKO_00034: "PBPKO"
    """blood flow rate to gonad: A blood flow parameter specifically describing the rate to the gonads compartment."""

    BLOOD_FLOW_RATE_TO_GONAD: "PBPKO"
    """blood flow rate to gonad: A blood flow parameter specifically describing the rate to the gonads compartment."""

    PBPKO_00035: "PBPKO"
    """fraction of blood flow to gonad: The dimensionless fraction of cardiac output delivered to the gonad compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_GONAD: "PBPKO"
    """fraction of blood flow to gonad: The dimensionless fraction of cardiac output delivered to the gonad compartment."""

    PBPKO_00036: "PBPKO"
    """blood flow rate to skin: A blood flow rate parameter specifically describing the rate to the skin compartment."""

    BLOOD_FLOW_RATE_TO_SKIN: "PBPKO"
    """blood flow rate to skin: A blood flow rate parameter specifically describing the rate to the skin compartment."""

    PBPKO_00037: "PBPKO"
    """fraction of blood flow to skin: The dimensionless fraction of cardiac output delivered to the skin compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_SKIN: "PBPKO"
    """fraction of blood flow to skin: The dimensionless fraction of cardiac output delivered to the skin compartment."""

    PBPKO_00038: "PBPKO"
    """blood flow rate to bone: A blood flow rate parameter specifically describing the rate to the bone compartment."""

    BLOOD_FLOW_RATE_TO_BONE: "PBPKO"
    """blood flow rate to bone: A blood flow rate parameter specifically describing the rate to the bone compartment."""

    PBPKO_00039: "PBPKO"
    """fraction of blood flow to bone: The dimensionless fraction of cardiac output delivered to the bone compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_BONE: "PBPKO"
    """fraction of blood flow to bone: The dimensionless fraction of cardiac output delivered to the bone compartment."""

    PBPKO_00040: "PBPKO"
    """blood flow rate to brain: A blood flow rate parameter specifically describing the rate to the brain compartment."""

    BLOOD_FLOW_RATE_TO_BRAIN: "PBPKO"
    """blood flow rate to brain: A blood flow rate parameter specifically describing the rate to the brain compartment."""

    PBPKO_00041: "PBPKO"
    """fraction of blood flow to brain: The dimensionless fraction of cardiac output delivered to the brain compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_BRAIN: "PBPKO"
    """fraction of blood flow to brain: The dimensionless fraction of cardiac output delivered to the brain compartment."""

    PBPKO_00042: "PBPKO"
    """blood flow rate to spleen: A blood flow rate parameter specifically describing the rate to the spleen compartment."""

    BLOOD_FLOW_RATE_TO_SPLEEN: "PBPKO"
    """blood flow rate to spleen: A blood flow rate parameter specifically describing the rate to the spleen compartment."""

    PBPKO_00043: "PBPKO"
    """fraction of blood flow to spleen: The dimensionless fraction of cardiac output delivered to the spleen compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_SPLEEN: "PBPKO"
    """fraction of blood flow to spleen: The dimensionless fraction of cardiac output delivered to the spleen compartment."""

    PBPKO_00044: "PBPKO"
    """blood flow rate to lung: A blood flow rate parameter specifically describing the rate to the lung compartment."""

    BLOOD_FLOW_RATE_TO_LUNG: "PBPKO"
    """blood flow rate to lung: A blood flow rate parameter specifically describing the rate to the lung compartment."""

    PBPKO_00045: "PBPKO"
    """fraction of blood flow to lung: The dimensionless fraction of cardiac output delivered to the lung compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_LUNG: "PBPKO"
    """fraction of blood flow to lung: The dimensionless fraction of cardiac output delivered to the lung compartment."""

    PBPKO_00046: "PBPKO"
    """blood flow rate to poorly perfused: A blood flow rate parameter specifically describing the rate to the poorly perfused organ/tissue compartment."""

    BLOOD_FLOW_RATE_TO_POORLY_PERFUSED: "PBPKO"
    """blood flow rate to poorly perfused: A blood flow rate parameter specifically describing the rate to the poorly perfused organ/tissue compartment."""

    PBPKO_00047: "PBPKO"
    """fraction of blood flow to poorly perfused: The dimensionless fraction of cardiac output delivered to the poorly perfused compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_POORLY_PERFUSED: "PBPKO"
    """fraction of blood flow to poorly perfused: The dimensionless fraction of cardiac output delivered to the poorly perfused compartment."""

    PBPKO_00048: "PBPKO"
    """blood flow rate to richly perfused: A blood flow rate parameter specifically describing the rate to the richly perfused organ/tissue compartment."""

    BLOOD_FLOW_RATE_TO_RICHLY_PERFUSED: "PBPKO"
    """blood flow rate to richly perfused: A blood flow rate parameter specifically describing the rate to the richly perfused organ/tissue compartment."""

    PBPKO_00049: "PBPKO"
    """fraction of blood flow to richly perfused: The dimensionless fraction of cardiac output delivered to the richly perfused compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_RICHLY_PERFUSED: "PBPKO"
    """fraction of blood flow to richly perfused: The dimensionless fraction of cardiac output delivered to the richly perfused compartment."""

    PBPKO_00050: "PBPKO"
    """blood flow rate to restbody: A blood flow rate parameter specifically describing the rate to the rest of body compartment (total minus specified organs)."""

    BLOOD_FLOW_RATE_TO_RESTBODY: "PBPKO"
    """blood flow rate to restbody: A blood flow rate parameter specifically describing the rate to the rest of body compartment (total minus specified organs)."""

    PBPKO_00051: "PBPKO"
    """fraction of blood flow to restbody: The dimensionless fraction of cardiac output delivered to the rest of the body compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_RESTBODY: "PBPKO"
    """fraction of blood flow to restbody: The dimensionless fraction of cardiac output delivered to the rest of the body compartment."""

    PBPKO_00052: "PBPKO"
    """blood flow rate to gall bladder: A blood flow rate parameter specifically describing the rate to the gall bladder compartment."""

    BLOOD_FLOW_RATE_TO_GALL_BLADDER: "PBPKO"
    """blood flow rate to gall bladder: A blood flow rate parameter specifically describing the rate to the gall bladder compartment."""

    PBPKO_00053: "PBPKO"
    """fraction of blood flow to gall bladder: The dimensionless fraction of cardiac output delivered to the gall bladder compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_GALL_BLADDER: "PBPKO"
    """fraction of blood flow to gall bladder: The dimensionless fraction of cardiac output delivered to the gall bladder compartment."""

    PBPKO_00054: "PBPKO"
    """blood flow rate to portal vein: A blood flow rate parameter specifically describing the rate to the portal vein compartment."""

    BLOOD_FLOW_RATE_TO_PORTAL_VEIN: "PBPKO"
    """blood flow rate to portal vein: A blood flow rate parameter specifically describing the rate to the portal vein compartment."""

    PBPKO_00055: "PBPKO"
    """fraction of blood flow to portal vein: The dimensionless fraction of cardiac output delivered to the portal vein compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_PORTAL_VEIN: "PBPKO"
    """fraction of blood flow to portal vein: The dimensionless fraction of cardiac output delivered to the portal vein compartment."""

    PBPKO_00056: "PBPKO"
    """blood flow rate to lymph: A blood flow rate parameter specifically describing the rate to the lymph compartment."""

    BLOOD_FLOW_RATE_TO_LYMPH: "PBPKO"
    """blood flow rate to lymph: A blood flow rate parameter specifically describing the rate to the lymph compartment."""

    PBPKO_00057: "PBPKO"
    """fraction of blood flow to lymph: The dimensionless fraction of cardiac output delivered to the lymph compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_LYMPH: "PBPKO"
    """fraction of blood flow to lymph: The dimensionless fraction of cardiac output delivered to the lymph compartment."""

    PBPKO_00058: "PBPKO"
    """amount of metabolized: An output parameter representing the total amount of compound metabolized."""

    AMOUNT_OF_METABOLIZED: "PBPKO"
    """amount of metabolized: An output parameter representing the total amount of compound metabolized."""

    PBPKO_00060: "PBPKO"
    """fraction of blood flow to stratum corneum: The dimensionless fraction of cardiac output delivered to the stratum corneum compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_STRATUM_CORNEUM: "PBPKO"
    """fraction of blood flow to stratum corneum: The dimensionless fraction of cardiac output delivered to the stratum corneum compartment."""

    PBPKO_00061: "PBPKO"
    """fraction of exposed skin: A dimensionless fraction of volume defined as the exposed skin volume divided per unit of total body weight."""

    FRACTION_OF_EXPOSED_SKIN: "PBPKO"
    """fraction of exposed skin: A dimensionless fraction of volume defined as the exposed skin volume divided per unit of total body weight."""

    PBPKO_00062: "PBPKO"
    """fraction of unexposed skin: A dimensionless fraction of volume defined as the unexposed skin volume divided per unit of total body weight."""

    FRACTION_OF_UNEXPOSED_SKIN: "PBPKO"
    """fraction of unexposed skin: A dimensionless fraction of volume defined as the unexposed skin volume divided per unit of total body weight."""

    PBPKO_00063: "PBPKO"
    """arterial blood flow rate: A blood flow rate parameter representing the rate of blood flow through the arterial compartment."""

    ARTERIAL_BLOOD_FLOW_RATE: "PBPKO"
    """arterial blood flow rate: A blood flow rate parameter representing the rate of blood flow through the arterial compartment."""

    PBPKO_00064: "PBPKO"
    """venous blood flow rate: A blood flow rate parameter representing the rate of blood flow returning through the venous compartment."""

    VENOUS_BLOOD_FLOW_RATE: "PBPKO"
    """venous blood flow rate: A blood flow rate parameter representing the rate of blood flow returning through the venous compartment."""

    PBPKO_00065: "PBPKO"
    """glomerular filtration rate: A bodily fluid flow rate parameter (or physiological process measure) describing the flow rate of filtered fluid through the kidney compartment."""

    GLOMERULAR_FILTRATION_RATE: "PBPKO"
    """glomerular filtration rate: A bodily fluid flow rate parameter (or physiological process measure) describing the flow rate of filtered fluid through the kidney compartment."""

    PBPKO_00066: "PBPKO"
    """volume of compartment: A physiological parameter representing the volume of a specific organ or tissue."""

    VOLUME_OF_COMPARTMENT: "PBPKO"
    """volume of compartment: A physiological parameter representing the volume of a specific organ or tissue."""

    PBPKO_00067: "PBPKO"
    """volume of stomach: A volume parameter representing the total volume of the stomach compartment."""

    VOLUME_OF_STOMACH: "PBPKO"
    """volume of stomach: A volume parameter representing the total volume of the stomach compartment."""

    PBPKO_00068: "PBPKO"
    """fraction of stomach: A dimensionless fraction of volume defined as the stomach volume divided per unit of total body weight."""

    FRACTION_OF_STOMACH: "PBPKO"
    """fraction of stomach: A dimensionless fraction of volume defined as the stomach volume divided per unit of total body weight."""

    PBPKO_00069: "PBPKO"
    """volume of intestine: A volume parameter representing the total volume of the intestine compartment."""

    VOLUME_OF_INTESTINE: "PBPKO"
    """volume of intestine: A volume parameter representing the total volume of the intestine compartment."""

    PBPKO_00070: "PBPKO"
    """fraction of intestine: A dimensionless fraction of volume defined as the intestine volume divided per unit of total body weight."""

    FRACTION_OF_INTESTINE: "PBPKO"
    """fraction of intestine: A dimensionless fraction of volume defined as the intestine volume divided per unit of total body weight."""

    PBPKO_00071: "PBPKO"
    """volume of small intestine: A volume parameter representing the total volume of the small intestine compartment."""

    VOLUME_OF_SMALL_INTESTINE: "PBPKO"
    """volume of small intestine: A volume parameter representing the total volume of the small intestine compartment."""

    PBPKO_00072: "PBPKO"
    """fraction of small intestine: A dimensionless fraction of volume defined as the small intestine volume divided per unit of total body weight."""

    FRACTION_OF_SMALL_INTESTINE: "PBPKO"
    """fraction of small intestine: A dimensionless fraction of volume defined as the small intestine volume divided per unit of total body weight."""

    PBPKO_00073: "PBPKO"
    """volume of large intestine: A volume parameter representing the total volume of the large intestine compartment."""

    VOLUME_OF_LARGE_INTESTINE: "PBPKO"
    """volume of large intestine: A volume parameter representing the total volume of the large intestine compartment."""

    PBPKO_00074: "PBPKO"
    """fraction of large intestine: A dimensionless fraction of volume defined as the large intestine volume divided per unit of total body weight."""

    FRACTION_OF_LARGE_INTESTINE: "PBPKO"
    """fraction of large intestine: A dimensionless fraction of volume defined as the large intestine volume divided per unit of total body weight."""

    PBPKO_00075: "PBPKO"
    """volume of pancreas: A volume parameter representing the total volume of the pancreas compartment."""

    VOLUME_OF_PANCREAS: "PBPKO"
    """volume of pancreas: A volume parameter representing the total volume of the pancreas compartment."""

    PBPKO_00076: "PBPKO"
    """fraction of pancreas: A dimensionless fraction of volume defined as the pancreas volume divided per unit of total body weight."""

    FRACTION_OF_PANCREAS: "PBPKO"
    """fraction of pancreas: A dimensionless fraction of volume defined as the pancreas volume divided per unit of total body weight."""

    PBPKO_00077: "PBPKO"
    """volume of liver: A volume parameter representing the total volume of the liver compartment."""

    VOLUME_OF_LIVER: "PBPKO"
    """volume of liver: A volume parameter representing the total volume of the liver compartment."""

    PBPKO_00078: "PBPKO"
    """fraction of liver: A dimensionless fraction of volume defined as the liver volume divided per unit of total body weight."""

    FRACTION_OF_LIVER: "PBPKO"
    """fraction of liver: A dimensionless fraction of volume defined as the liver volume divided per unit of total body weight."""

    PBPKO_00079: "PBPKO"
    """volume of kidney: A volume parameter representing the total volume of the kidney compartment."""

    VOLUME_OF_KIDNEY: "PBPKO"
    """volume of kidney: A volume parameter representing the total volume of the kidney compartment."""

    PBPKO_00080: "PBPKO"
    """fraction of kidney: A dimensionless fraction of volume defined as the kidney volume divided per unit of total body weight."""

    FRACTION_OF_KIDNEY: "PBPKO"
    """fraction of kidney: A dimensionless fraction of volume defined as the kidney volume divided per unit of total body weight."""

    PBPKO_00081: "PBPKO"
    """volume of muscle: A volume parameter representing the total volume of muscle compartment."""

    VOLUME_OF_MUSCLE: "PBPKO"
    """volume of muscle: A volume parameter representing the total volume of muscle compartment."""

    PBPKO_00082: "PBPKO"
    """fraction of muscle: A dimensionless fraction of volume defined as the muscle volume divided per unit of total body weight."""

    FRACTION_OF_MUSCLE: "PBPKO"
    """fraction of muscle: A dimensionless fraction of volume defined as the muscle volume divided per unit of total body weight."""

    PBPKO_00083: "PBPKO"
    """volume of heart: A volume parameter representing the total volume of the heart compartment."""

    VOLUME_OF_HEART: "PBPKO"
    """volume of heart: A volume parameter representing the total volume of the heart compartment."""

    PBPKO_00084: "PBPKO"
    """fraction of heart: A dimensionless fraction of volume defined as the heart volume divided per unit of total body weight."""

    FRACTION_OF_HEART: "PBPKO"
    """fraction of heart: A dimensionless fraction of volume defined as the heart volume divided per unit of total body weight."""

    PBPKO_00085: "PBPKO"
    """volume of fat: A volume parameter representing the total volume of fat (adipose tissue) compartment."""

    VOLUME_OF_FAT: "PBPKO"
    """volume of fat: A volume parameter representing the total volume of fat (adipose tissue) compartment."""

    PBPKO_00086: "PBPKO"
    """fraction of fat: A dimensionless fraction of volume defined as the fat volume divided per unit of total body weight."""

    FRACTION_OF_FAT: "PBPKO"
    """fraction of fat: A dimensionless fraction of volume defined as the fat volume divided per unit of total body weight."""

    PBPKO_00087: "PBPKO"
    """volume of gonad: A volume parameter representing the total volume of the gonad compartment."""

    VOLUME_OF_GONAD: "PBPKO"
    """volume of gonad: A volume parameter representing the total volume of the gonad compartment."""

    PBPKO_00088: "PBPKO"
    """fraction of gonad: A dimensionless fraction of volume defined as the gonad volume divided per unit of total body weight."""

    FRACTION_OF_GONAD: "PBPKO"
    """fraction of gonad: A dimensionless fraction of volume defined as the gonad volume divided per unit of total body weight."""

    PBPKO_00089: "PBPKO"
    """volume of skin: A volume parameter representing the total volume of the skin compartment."""

    VOLUME_OF_SKIN: "PBPKO"
    """volume of skin: A volume parameter representing the total volume of the skin compartment."""

    PBPKO_00090: "PBPKO"
    """fraction of skin: A dimensionless fraction of volume defined as the skin volume divided per unit of total body weight."""

    FRACTION_OF_SKIN: "PBPKO"
    """fraction of skin: A dimensionless fraction of volume defined as the skin volume divided per unit of total body weight."""

    PBPKO_00091: "PBPKO"
    """volume of bone: A volume parameter representing the total volume of bone compartment."""

    VOLUME_OF_BONE: "PBPKO"
    """volume of bone: A volume parameter representing the total volume of bone compartment."""

    PBPKO_00092: "PBPKO"
    """fraction of bone: A dimensionless fraction of volume defined as the bone volume divided per unit of total body weight."""

    FRACTION_OF_BONE: "PBPKO"
    """fraction of bone: A dimensionless fraction of volume defined as the bone volume divided per unit of total body weight."""

    PBPKO_00093: "PBPKO"
    """volume of brain: A volume parameter representing the total volume of the brain compartment."""

    VOLUME_OF_BRAIN: "PBPKO"
    """volume of brain: A volume parameter representing the total volume of the brain compartment."""

    PBPKO_00094: "PBPKO"
    """fraction of brain: A dimensionless fraction of volume defined as the brain volume divided per unit of total body weight."""

    FRACTION_OF_BRAIN: "PBPKO"
    """fraction of brain: A dimensionless fraction of volume defined as the brain volume divided per unit of total body weight."""

    PBPKO_00095: "PBPKO"
    """volume of spleen: A volume parameter representing the total volume of the spleen compartment."""

    VOLUME_OF_SPLEEN: "PBPKO"
    """volume of spleen: A volume parameter representing the total volume of the spleen compartment."""

    PBPKO_00096: "PBPKO"
    """fraction of spleen: A dimensionless fraction of volume defined as the spleen volume divided per unit of total body weight."""

    FRACTION_OF_SPLEEN: "PBPKO"
    """fraction of spleen: A dimensionless fraction of volume defined as the spleen volume divided per unit of total body weight."""

    PBPKO_00097: "PBPKO"
    """volume of lung: A volume parameter representing the total volume of the lung compartment."""

    VOLUME_OF_LUNG: "PBPKO"
    """volume of lung: A volume parameter representing the total volume of the lung compartment."""

    PBPKO_00098: "PBPKO"
    """fraction of lung: A dimensionless fraction of volume defined as the lung volume divided per unit of total body weight."""

    FRACTION_OF_LUNG: "PBPKO"
    """fraction of lung: A dimensionless fraction of volume defined as the lung volume divided per unit of total body weight."""

    PBPKO_00099: "PBPKO"
    """volume of poorly perfused: A volume parameter representing the total volume of the poorly perfused compartment."""

    VOLUME_OF_POORLY_PERFUSED: "PBPKO"
    """volume of poorly perfused: A volume parameter representing the total volume of the poorly perfused compartment."""

    PBPKO_00100: "PBPKO"
    """fraction of poorly perfused: A dimensionless fraction of volume defined as the poorly perfused compartment volume divided per unit of total body weight."""

    FRACTION_OF_POORLY_PERFUSED: "PBPKO"
    """fraction of poorly perfused: A dimensionless fraction of volume defined as the poorly perfused compartment volume divided per unit of total body weight."""

    PBPKO_00101: "PBPKO"
    """volume of richly perfused: A volume parameter representing the total volume of the richly perfused compartment."""

    VOLUME_OF_RICHLY_PERFUSED: "PBPKO"
    """volume of richly perfused: A volume parameter representing the total volume of the richly perfused compartment."""

    PBPKO_00102: "PBPKO"
    """fraction of richly perfused: A dimensionless fraction of volume defined as the richly perfused compartment volume divided per unit of total body weight."""

    FRACTION_OF_RICHLY_PERFUSED: "PBPKO"
    """fraction of richly perfused: A dimensionless fraction of volume defined as the richly perfused compartment volume divided per unit of total body weight."""

    PBPKO_00103: "PBPKO"
    """volume of plasma: A volume parameter representing the total volume of plasma compartment."""

    VOLUME_OF_PLASMA: "PBPKO"
    """volume of plasma: A volume parameter representing the total volume of plasma compartment."""

    PBPKO_00104: "PBPKO"
    """fraction of plasma: A dimensionless fraction of volume defined as the plasma volume divided per unit of total body weight."""

    FRACTION_OF_PLASMA: "PBPKO"
    """fraction of plasma: A dimensionless fraction of volume defined as the plasma volume divided per unit of total body weight."""

    PBPKO_00105: "PBPKO"
    """volume of rest body: A volume parameter representing the total volume of the rest of body compartment."""

    VOLUME_OF_REST_BODY: "PBPKO"
    """volume of rest body: A volume parameter representing the total volume of the rest of body compartment."""

    PBPKO_00106: "PBPKO"
    """fraction of rest body: A dimensionless fraction of volume defined as the rest of body volume divided per unit of total body weight."""

    FRACTION_OF_REST_BODY: "PBPKO"
    """fraction of rest body: A dimensionless fraction of volume defined as the rest of body volume divided per unit of total body weight."""

    PBPKO_00107: "PBPKO"
    """volume of stratum corneum with respect to blood: A volume parameter representing the total volume of stratum corneum compartment with respect to blood/plasma."""

    VOLUME_OF_STRATUM_CORNEUM_WITH_RESPECT_TO_BLOOD: "PBPKO"
    """volume of stratum corneum with respect to blood: A volume parameter representing the total volume of stratum corneum compartment with respect to blood/plasma."""

    PBPKO_00108: "PBPKO"
    """volume of blood: A volume parameter representing the total volume of blood compartment."""

    VOLUME_OF_BLOOD: "PBPKO"
    """volume of blood: A volume parameter representing the total volume of blood compartment."""

    PBPKO_00109: "PBPKO"
    """volume of exposed skin: A volume parameter representing the total volume of the exposed skin compartment."""

    VOLUME_OF_EXPOSED_SKIN: "PBPKO"
    """volume of exposed skin: A volume parameter representing the total volume of the exposed skin compartment."""

    PBPKO_00110: "PBPKO"
    """fraction of surface area exposed: A surface area parameter representing the fraction of skin surface area actually exposed."""

    FRACTION_OF_SURFACE_AREA_EXPOSED: "PBPKO"
    """fraction of surface area exposed: A surface area parameter representing the fraction of skin surface area actually exposed."""

    PBPKO_00111: "PBPKO"
    """volume of unexposed skin: A volume parameter representing the total volume of the unexposed skin compartment."""

    VOLUME_OF_UNEXPOSED_SKIN: "PBPKO"
    """volume of unexposed skin: A volume parameter representing the total volume of the unexposed skin compartment."""

    PBPKO_00112: "PBPKO"
    """volume of stratum corneum exposed: A volume parameter representing the total volume of the exposed stratum corneum compartment."""

    VOLUME_OF_STRATUM_CORNEUM_EXPOSED: "PBPKO"
    """volume of stratum corneum exposed: A volume parameter representing the total volume of the exposed stratum corneum compartment."""

    PBPKO_00113: "PBPKO"
    """volume of unexposed stratum corneum: A volume parameter representing the total volume of the unexposed stratum corneum compartment."""

    VOLUME_OF_UNEXPOSED_STRATUM_CORNEUM: "PBPKO"
    """volume of unexposed stratum corneum: A volume parameter representing the total volume of the unexposed stratum corneum compartment."""

    PBPKO_00114: "PBPKO"
    """fraction alveolar volume: A dimensionless fraction of volume defined as the alveolar volume divided per unit of total body weight."""

    FRACTION_ALVEOLAR_VOLUME: "PBPKO"
    """fraction alveolar volume: A dimensionless fraction of volume defined as the alveolar volume divided per unit of total body weight."""

    PBPKO_00115: "PBPKO"
    """volume of gall bladder: A volume parameter representing the total volume of the gall bladder compartment."""

    VOLUME_OF_GALL_BLADDER: "PBPKO"
    """volume of gall bladder: A volume parameter representing the total volume of the gall bladder compartment."""

    PBPKO_00116: "PBPKO"
    """fraction of gall bladder: A dimensionless fraction of volume defined as the gall bladder volume divided per unit of total body weight."""

    FRACTION_OF_GALL_BLADDER: "PBPKO"
    """fraction of gall bladder: A dimensionless fraction of volume defined as the gall bladder volume divided per unit of total body weight."""

    PBPKO_00117: "PBPKO"
    """volume of portal vein: A volume parameter representing the total volume of the portal vein compartment."""

    VOLUME_OF_PORTAL_VEIN: "PBPKO"
    """volume of portal vein: A volume parameter representing the total volume of the portal vein compartment."""

    PBPKO_00118: "PBPKO"
    """fraction of portal vein: A dimensionless fraction of volume defined as the portal vein volume divided per unit of total body weight."""

    FRACTION_OF_PORTAL_VEIN: "PBPKO"
    """fraction of portal vein: A dimensionless fraction of volume defined as the portal vein volume divided per unit of total body weight."""

    PBPKO_00119: "PBPKO"
    """volume of lymph: A volume parameter representing the total volume of lymph compartment."""

    VOLUME_OF_LYMPH: "PBPKO"
    """volume of lymph: A volume parameter representing the total volume of lymph compartment."""

    PBPKO_00120: "PBPKO"
    """fraction of lymph: A dimensionless fraction of volume defined as the lymph volume divided per unit of total body weight."""

    FRACTION_OF_LYMPH: "PBPKO"
    """fraction of lymph: A dimensionless fraction of volume defined as the lymph volume divided per unit of total body weight."""

    PBPKO_00121: "PBPKO"
    """arterial volume: A volume parameter representing the total volume of the arterial compartment."""

    ARTERIAL_VOLUME: "PBPKO"
    """arterial volume: A volume parameter representing the total volume of the arterial compartment."""

    PBPKO_00122: "PBPKO"
    """venous volume: A volume parameter representing the total volume of the venous compartment."""

    VENOUS_VOLUME: "PBPKO"
    """venous volume: A volume parameter representing the total volume of the venous compartment."""

    PBPKO_00126: "PBPKO"
    """physicochemical parameter: A parameter relating to the physical and chemical properties of a compound (e.g., MW, lipophilicity, solubility, pKa)."""

    PHYSICOCHEMICAL_PARAMETER: "PBPKO"
    """physicochemical parameter: A parameter relating to the physical and chemical properties of a compound (e.g., MW, lipophilicity, solubility, pKa)."""

    PBPKO_00127: "PBPKO"
    """molecular weight: A physicochemical parameter representing the sum of the weights of all atoms in a molecule."""

    MOLECULAR_WEIGHT: "PBPKO"
    """molecular weight: A physicochemical parameter representing the sum of the weights of all atoms in a molecule."""

    PBPKO_00128: "PBPKO"
    """lipophillicity: A physicochemical parameter representing the affinity or tendency of a compound to dissolve in lipids or hydrophobic environments."""

    LIPOPHILLICITY: "PBPKO"
    """lipophillicity: A physicochemical parameter representing the affinity or tendency of a compound to dissolve in lipids or hydrophobic environments."""

    PBPKO_00129: "PBPKO"
    """distribution coefficient: A physicochemical parameter representing the logarithm of the ratio of concentrations of a compound in a mixture of two immiscible phases at equilibrium, specifically describing lipophilicity (LogD)."""

    DISTRIBUTION_COEFFICIENT: "PBPKO"
    """distribution coefficient: A physicochemical parameter representing the logarithm of the ratio of concentrations of a compound in a mixture of two immiscible phases at equilibrium, specifically describing lipophilicity (LogD)."""

    PBPKO_00130: "PBPKO"
    """dissolution in two phase system: A physicochemical parameter representing the ratio of a dissolved compound in a two-phase system (often used interchangeably with partition coefficient)."""

    DISSOLUTION_IN_TWO_PHASE_SYSTEM: "PBPKO"
    """dissolution in two phase system: A physicochemical parameter representing the ratio of a dissolved compound in a two-phase system (often used interchangeably with partition coefficient)."""

    PBPKO_00131: "PBPKO"
    """logarithmic solubility: A physicochemical parameter representing the 10-based logarithm of a compound's solubility (typically in mol/L)."""

    LOGARITHMIC_SOLUBILITY: "PBPKO"
    """logarithmic solubility: A physicochemical parameter representing the 10-based logarithm of a compound's solubility (typically in mol/L)."""

    PBPKO_00132: "PBPKO"
    """water solubility: A physicochemical parameter representing the solubility of a compound specifically in water."""

    WATER_SOLUBILITY: "PBPKO"
    """water solubility: A physicochemical parameter representing the solubility of a compound specifically in water."""

    PBPKO_00133: "PBPKO"
    """acid dissociation constant: A physicochemical parameter representing the negative base-10 logarithm (pKa) of the acid dissociation constant (Ka)."""

    ACID_DISSOCIATION_CONSTANT: "PBPKO"
    """acid dissociation constant: A physicochemical parameter representing the negative base-10 logarithm (pKa) of the acid dissociation constant (Ka)."""

    PBPKO_00134: "PBPKO"
    """basic dissociation constant: A physicochemical parameter representing the negative base-10 logarithm (pKb) of the base dissociation constant (Kb)."""

    BASIC_DISSOCIATION_CONSTANT: "PBPKO"
    """basic dissociation constant: A physicochemical parameter representing the negative base-10 logarithm (pKb) of the base dissociation constant (Kb)."""

    PBPKO_00135: "PBPKO"
    """physiological charge: A physicochemical parameter representing the electrical charge of a molecule at physiological pH."""

    PHYSIOLOGICAL_CHARGE: "PBPKO"
    """physiological charge: A physicochemical parameter representing the electrical charge of a molecule at physiological pH."""

    PBPKO_00136: "PBPKO"
    """hydrogen acceptor count: A physicochemical parameter representing the integer number of hydrogen bond acceptors in a molecular entity."""

    HYDROGEN_ACCEPTOR_COUNT: "PBPKO"
    """hydrogen acceptor count: A physicochemical parameter representing the integer number of hydrogen bond acceptors in a molecular entity."""

    PBPKO_00137: "PBPKO"
    """hydrogen donor count: A physicochemical parameter representing the integer number of hydrogen bond donors in a molecular entity."""

    HYDROGEN_DONOR_COUNT: "PBPKO"
    """hydrogen donor count: A physicochemical parameter representing the integer number of hydrogen bond donors in a molecular entity."""

    PBPKO_00138: "PBPKO"
    """rotatable bond count: A physicochemical parameter representing the integer count of rotatable bonds in a molecular entity."""

    ROTATABLE_BOND_COUNT: "PBPKO"
    """rotatable bond count: A physicochemical parameter representing the integer count of rotatable bonds in a molecular entity."""

    PBPKO_00139: "PBPKO"
    """biochemical parameter: A parameter that is compound-dependent and relates to biological interactions or transformations (e.g., clearance, binding, partition coefficients)."""

    BIOCHEMICAL_PARAMETER: "PBPKO"
    """biochemical parameter: A parameter that is compound-dependent and relates to biological interactions or transformations (e.g., clearance, binding, partition coefficients)."""

    PBPKO_00140: "PBPKO"
    """absorption: A biological process by which a compound moves from its site of administration into the systemic circulation or a target tissue."""

    ABSORPTION: "PBPKO"
    """absorption: A biological process by which a compound moves from its site of administration into the systemic circulation or a target tissue."""

    PBPKO_00141: "PBPKO"
    """absorption rate constant gut: An absorption rate constant parameter representing the rate constant for the movement of a compound from the gut to systemic circulation or another compartment."""

    ABSORPTION_RATE_CONSTANT_GUT: "PBPKO"
    """absorption rate constant gut: An absorption rate constant parameter representing the rate constant for the movement of a compound from the gut to systemic circulation or another compartment."""

    PBPKO_00142: "PBPKO"
    """absorption rate constant intestine: An absorption rate constant parameter representing the movement of a compound from the intestine to systemic circulation or another compartment."""

    ABSORPTION_RATE_CONSTANT_INTESTINE: "PBPKO"
    """absorption rate constant intestine: An absorption rate constant parameter representing the movement of a compound from the intestine to systemic circulation or another compartment."""

    PBPKO_00143: "PBPKO"
    """gastric emptying rate: A biochemical parameter representing the rate at which the stomach empties its contents into the small intestine."""

    GASTRIC_EMPTYING_RATE: "PBPKO"
    """gastric emptying rate: A biochemical parameter representing the rate at which the stomach empties its contents into the small intestine."""

    PBPKO_00144: "PBPKO"
    """enterohepatic recirculation: A biological process involving recycling of compounds through the liver via biliary excretion, intestinal reabsorption, portal circulation return, and re-excretion."""

    ENTEROHEPATIC_RECIRCULATION: "PBPKO"
    """enterohepatic recirculation: A biological process involving recycling of compounds through the liver via biliary excretion, intestinal reabsorption, portal circulation return, and re-excretion."""

    PBPKO_00145: "PBPKO"
    """specific intestinal permeability: A biochemical parameter representing the surface area-normalized transcellular permeability of the intestinal wall for a compound."""

    SPECIFIC_INTESTINAL_PERMEABILITY: "PBPKO"
    """specific intestinal permeability: A biochemical parameter representing the surface area-normalized transcellular permeability of the intestinal wall for a compound."""

    PBPKO_00146: "PBPKO"
    """distribution process: A biological process describing the movement of a compound from systemic circulation to various organs/tissues."""

    DISTRIBUTION_PROCESS: "PBPKO"
    """distribution process: A biological process describing the movement of a compound from systemic circulation to various organs/tissues."""

    PBPKO_00147: "PBPKO"
    """volume of distribution: A biochemical parameter representing the apparent volume into which a compound distributes in the body relative to its plasma concentration."""

    VOLUME_OF_DISTRIBUTION: "PBPKO"
    """volume of distribution: A biochemical parameter representing the apparent volume into which a compound distributes in the body relative to its plasma concentration."""

    PBPKO_00148: "PBPKO"
    """protein binding mediated distributiion process: A distribution process (or molecular function) where substances bind to proteins or related compounds."""

    PROTEIN_BINDING_MEDIATED_DISTRIBUTIION_PROCESS: "PBPKO"
    """protein binding mediated distributiion process: A distribution process (or molecular function) where substances bind to proteins or related compounds."""

    PBPKO_00149: "PBPKO"
    """unbound fraction: A biochemical parameter representing the fraction of a compound that is not bound (e.g., to proteins)."""

    UNBOUND_FRACTION: "PBPKO"
    """unbound fraction: A biochemical parameter representing the fraction of a compound that is not bound (e.g., to proteins)."""

    PBPKO_00150: "PBPKO"
    """fraction unbound gut: An unbound fraction parameter specifically for the gut compartment."""

    FRACTION_UNBOUND_GUT: "PBPKO"
    """fraction unbound gut: An unbound fraction parameter specifically for the gut compartment."""

    PBPKO_00151: "PBPKO"
    """fraction unbound stomach: An unbound fraction parameter specifically for the stomach compartment."""

    FRACTION_UNBOUND_STOMACH: "PBPKO"
    """fraction unbound stomach: An unbound fraction parameter specifically for the stomach compartment."""

    PBPKO_00152: "PBPKO"
    """fraction unbound intestine: An unbound fraction parameter specifically for the intestine compartment."""

    FRACTION_UNBOUND_INTESTINE: "PBPKO"
    """fraction unbound intestine: An unbound fraction parameter specifically for the intestine compartment."""

    PBPKO_00153: "PBPKO"
    """fraction unbound pancreas: An unbound fraction parameter specifically for the pancreas compartment."""

    FRACTION_UNBOUND_PANCREAS: "PBPKO"
    """fraction unbound pancreas: An unbound fraction parameter specifically for the pancreas compartment."""

    PBPKO_00154: "PBPKO"
    """fraction unbound liver: An unbound fraction parameter specifically for the liver compartment."""

    FRACTION_UNBOUND_LIVER: "PBPKO"
    """fraction unbound liver: An unbound fraction parameter specifically for the liver compartment."""

    PBPKO_00155: "PBPKO"
    """fraction unbound kidney: An unbound fraction parameter specifically for the kidney compartment."""

    FRACTION_UNBOUND_KIDNEY: "PBPKO"
    """fraction unbound kidney: An unbound fraction parameter specifically for the kidney compartment."""

    PBPKO_00156: "PBPKO"
    """fraction unbound muscle: An unbound fraction parameter specifically for the muscle compartment."""

    FRACTION_UNBOUND_MUSCLE: "PBPKO"
    """fraction unbound muscle: An unbound fraction parameter specifically for the muscle compartment."""

    PBPKO_00157: "PBPKO"
    """fraction unbound heart: An unbound fraction parameter specifically for the heart compartment."""

    FRACTION_UNBOUND_HEART: "PBPKO"
    """fraction unbound heart: An unbound fraction parameter specifically for the heart compartment."""

    PBPKO_00158: "PBPKO"
    """fraction unbound fat: An unbound fraction parameter specifically for the fat (adipose) compartment."""

    FRACTION_UNBOUND_FAT: "PBPKO"
    """fraction unbound fat: An unbound fraction parameter specifically for the fat (adipose) compartment."""

    PBPKO_00159: "PBPKO"
    """fraction unbound gonad: An unbound fraction parameter specifically for the gonad compartment."""

    FRACTION_UNBOUND_GONAD: "PBPKO"
    """fraction unbound gonad: An unbound fraction parameter specifically for the gonad compartment."""

    PBPKO_00160: "PBPKO"
    """fraction unbound skin: An unbound fraction parameter specifically for the skin compartment."""

    FRACTION_UNBOUND_SKIN: "PBPKO"
    """fraction unbound skin: An unbound fraction parameter specifically for the skin compartment."""

    PBPKO_00161: "PBPKO"
    """fraction unbound bone: An unbound fraction parameter specifically for the bone compartment."""

    FRACTION_UNBOUND_BONE: "PBPKO"
    """fraction unbound bone: An unbound fraction parameter specifically for the bone compartment."""

    PBPKO_00162: "PBPKO"
    """fraction unbound spleen: An unbound fraction parameter specifically for the spleen compartment."""

    FRACTION_UNBOUND_SPLEEN: "PBPKO"
    """fraction unbound spleen: An unbound fraction parameter specifically for the spleen compartment."""

    PBPKO_00163: "PBPKO"
    """fraction unbound lung: An unbound fraction parameter specifically for the lung compartment."""

    FRACTION_UNBOUND_LUNG: "PBPKO"
    """fraction unbound lung: An unbound fraction parameter specifically for the lung compartment."""

    PBPKO_00164: "PBPKO"
    """fraction unbound enterocytes: An unbound fraction parameter specifically within enterocytes."""

    FRACTION_UNBOUND_ENTEROCYTES: "PBPKO"
    """fraction unbound enterocytes: An unbound fraction parameter specifically within enterocytes."""

    PBPKO_00165: "PBPKO"
    """partition coefficient: A biochemical parameter representing the ratio of the concentration of a compound in a particular tissue to its concentration in plasma/blood at equilibrium."""

    PARTITION_COEFFICIENT: "PBPKO"
    """partition coefficient: A biochemical parameter representing the ratio of the concentration of a compound in a particular tissue to its concentration in plasma/blood at equilibrium."""

    PBPKO_00166: "PBPKO"
    """gut plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in gut to plasma."""

    GUT_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """gut plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in gut to plasma."""

    PBPKO_00167: "PBPKO"
    """stomach plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in stomach to plasma."""

    STOMACH_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """stomach plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in stomach to plasma."""

    PBPKO_00168: "PBPKO"
    """intestine plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in intestine to plasma."""

    INTESTINE_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """intestine plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in intestine to plasma."""

    PBPKO_00169: "PBPKO"
    """pancreas plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in pancreas to plasma."""

    PANCREAS_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """pancreas plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in pancreas to plasma."""

    PBPKO_00170: "PBPKO"
    """liver plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in liver to plasma."""

    LIVER_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """liver plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in liver to plasma."""

    PBPKO_00171: "PBPKO"
    """kidney plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in kidney to plasma."""

    KIDNEY_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """kidney plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in kidney to plasma."""

    PBPKO_00172: "PBPKO"
    """muscle plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in muscle to plasma."""

    MUSCLE_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """muscle plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in muscle to plasma."""

    PBPKO_00173: "PBPKO"
    """heart plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in heart to plasma."""

    HEART_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """heart plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in heart to plasma."""

    PBPKO_00174: "PBPKO"
    """fat plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in fat (adipose tissue) to plasma."""

    FAT_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """fat plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in fat (adipose tissue) to plasma."""

    PBPKO_00175: "PBPKO"
    """gonad plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in gonads to plasma."""

    GONAD_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """gonad plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in gonads to plasma."""

    PBPKO_00176: "PBPKO"
    """skin plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in skin to plasma."""

    SKIN_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """skin plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in skin to plasma."""

    PBPKO_00177: "PBPKO"
    """bone plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in bone to plasma."""

    BONE_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """bone plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in bone to plasma."""

    PBPKO_00178: "PBPKO"
    """spleen plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in spleen to plasma."""

    SPLEEN_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """spleen plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in spleen to plasma."""

    PBPKO_00179: "PBPKO"
    """lung plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in lung to plasma."""

    LUNG_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """lung plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in lung to plasma."""

    PBPKO_00180: "PBPKO"
    """rich perfused plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the lumped richly perfused compartment to plasma."""

    RICH_PERFUSED_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """rich perfused plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the lumped richly perfused compartment to plasma."""

    PBPKO_00181: "PBPKO"
    """poor perfused plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the lumped poorly perfused compartment to plasma."""

    POOR_PERFUSED_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """poor perfused plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the lumped poorly perfused compartment to plasma."""

    PBPKO_00182: "PBPKO"
    """skin stratum corneum partition coefficient: A partition coefficient representing the ratio of compound concentration in the stratum corneum to the rest of the skin."""

    SKIN_STRATUM_CORNEUM_PARTITION_COEFFICIENT: "PBPKO"
    """skin stratum corneum partition coefficient: A partition coefficient representing the ratio of compound concentration in the stratum corneum to the rest of the skin."""

    PBPKO_00183: "PBPKO"
    """air plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in air to plasma."""

    AIR_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """air plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in air to plasma."""

    PBPKO_00184: "PBPKO"
    """skin diffusion coefficient: A diffusion coefficient representing the diffusion of a compound across the skin."""

    SKIN_DIFFUSION_COEFFICIENT: "PBPKO"
    """skin diffusion coefficient: A diffusion coefficient representing the diffusion of a compound across the skin."""

    PBPKO_00185: "PBPKO"
    """human serum albumin: A material entity representing distribution-related protein (most abundant in human plasma) that binds various compounds."""

    HUMAN_SERUM_ALBUMIN: "PBPKO"
    """human serum albumin: A material entity representing distribution-related protein (most abundant in human plasma) that binds various compounds."""

    PBPKO_00187: "PBPKO"
    """blood:plasma ratio: A biochemical parameter representing the ratio of compound concentration in whole blood to that in plasma."""

    BLOOD_PLASMA_RATIO: "PBPKO"
    """blood:plasma ratio: A biochemical parameter representing the ratio of compound concentration in whole blood to that in plasma."""

    PBPKO_00189: "PBPKO"
    """catalytic rate constant: A biochemical parameter quantifying enzymatic reaction velocity (kcat), representing the maximum number of substrate molecules converted per active site per unit time."""

    CATALYTIC_RATE_CONSTANT: "PBPKO"
    """catalytic rate constant: A biochemical parameter quantifying enzymatic reaction velocity (kcat), representing the maximum number of substrate molecules converted per active site per unit time."""

    PBPKO_00191: "PBPKO"
    """phase I metabolism: A metabolism process involving the conversion of exogenous substances to more polar metabolites, often via oxidation, reduction, or hydrolysis (e.g., by CYPs)."""

    PHASE_I_METABOLISM: "PBPKO"
    """phase I metabolism: A metabolism process involving the conversion of exogenous substances to more polar metabolites, often via oxidation, reduction, or hydrolysis (e.g., by CYPs)."""

    PBPKO_00200: "PBPKO"
    """phase II: A metabolism process involving the conjugation of phase I products (or parent compounds) to hydrophilic moieties to facilitate excretion."""

    PHASE_II: "PBPKO"
    """phase II: A metabolism process involving the conjugation of phase I products (or parent compounds) to hydrophilic moieties to facilitate excretion."""

    PBPKO_00209: "PBPKO"
    """phase III: A metabolism/transport process involving the further processing and excretion of conjugated metabolites (often involving efflux transporters)."""

    PHASE_III: "PBPKO"
    """phase III: A metabolism/transport process involving the further processing and excretion of conjugated metabolites (often involving efflux transporters)."""

    PBPKO_00210: "PBPKO"
    """first pass metabolism: A metabolism process occurring at a specific location (e.g., liver, gut wall) after administration but before reaching systemic circulation, reducing the concentration of active compound."""

    FIRST_PASS_METABOLISM: "PBPKO"
    """first pass metabolism: A metabolism process occurring at a specific location (e.g., liver, gut wall) after administration but before reaching systemic circulation, reducing the concentration of active compound."""

    PBPKO_00211: "PBPKO"
    """maximum rate in intestine: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the intestine when the enzyme is saturated with substrate."""

    MAXIMUM_RATE_IN_INTESTINE: "PBPKO"
    """maximum rate in intestine: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the intestine when the enzyme is saturated with substrate."""

    PBPKO_00212: "PBPKO"
    """Michaelis constant  intestine: Michaelis constant representing the substrate concentration at which the reaction rate in the intestine is half of Vmax (Km)."""

    MICHAELIS_CONSTANT__INTESTINE: "PBPKO"
    """Michaelis constant  intestine: Michaelis constant representing the substrate concentration at which the reaction rate in the intestine is half of Vmax (Km)."""

    PBPKO_00213: "PBPKO"
    """maximum rate in liver: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the liver when the enzyme is saturated with substrate."""

    MAXIMUM_RATE_IN_LIVER: "PBPKO"
    """maximum rate in liver: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the liver when the enzyme is saturated with substrate."""

    PBPKO_00214: "PBPKO"
    """Michaelis constant  liver: Michaelis constant representing the substrate concentration at which the reaction rate in the liver is half of Vmax (Km)."""

    MICHAELIS_CONSTANT__LIVER: "PBPKO"
    """Michaelis constant  liver: Michaelis constant representing the substrate concentration at which the reaction rate in the liver is half of Vmax (Km)."""

    PBPKO_00215: "PBPKO"
    """gut metabolism: A metabolism process specifically occurring within the gut."""

    GUT_METABOLISM: "PBPKO"
    """gut metabolism: A metabolism process specifically occurring within the gut."""

    PBPKO_00216: "PBPKO"
    """dissociation constant: A biochemical parameter (Kd) measuring the affinity of a compound for its binding partner (e.g., receptor, protein)."""

    DISSOCIATION_CONSTANT: "PBPKO"
    """dissociation constant: A biochemical parameter (Kd) measuring the affinity of a compound for its binding partner (e.g., receptor, protein)."""

    PBPKO_00217: "PBPKO"
    """transporter: A material entity representing protein responsible for the import or export of compounds across cell membranes."""

    TRANSPORTER: "PBPKO"
    """transporter: A material entity representing protein responsible for the import or export of compounds across cell membranes."""

    PBPKO_00218: "PBPKO"
    """oatp: A transporter family (Organic Anion Transporting Polypeptides) involved in transporting organic anions."""

    OATP: "PBPKO"
    """oatp: A transporter family (Organic Anion Transporting Polypeptides) involved in transporting organic anions."""

    PBPKO_00219: "PBPKO"
    """abcc3: A transporter (ATP-binding cassette subfamily C member 3) involved in bile metabolism and transport."""

    ABCC3: "PBPKO"
    """abcc3: A transporter (ATP-binding cassette subfamily C member 3) involved in bile metabolism and transport."""

    PBPKO_00220: "PBPKO"
    """abcc2: A transporter (ATP-binding cassette subfamily C member 2) involved in transporting various molecules across cell membranes."""

    ABCC2: "PBPKO"
    """abcc2: A transporter (ATP-binding cassette subfamily C member 2) involved in transporting various molecules across cell membranes."""

    PBPKO_00221: "PBPKO"
    """degradation rate constant: A biochemical parameter (kdeg) representing the rate constant for the degradation of a metabolizing enzyme or transporter."""

    DEGRADATION_RATE_CONSTANT: "PBPKO"
    """degradation rate constant: A biochemical parameter (kdeg) representing the rate constant for the degradation of a metabolizing enzyme or transporter."""

    PBPKO_00222: "PBPKO"
    """inhibition constant: A biochemical parameter (Ki) representing the inhibition constant for a specific enzyme or transporter interaction."""

    INHIBITION_CONSTANT: "PBPKO"
    """inhibition constant: A biochemical parameter (Ki) representing the inhibition constant for a specific enzyme or transporter interaction."""

    PBPKO_00223: "PBPKO"
    """renal excretion: An excretion process involving the elimination of compounds and metabolites primarily through urine via the kidneys."""

    RENAL_EXCRETION: "PBPKO"
    """renal excretion: An excretion process involving the elimination of compounds and metabolites primarily through urine via the kidneys."""

    PBPKO_00224: "PBPKO"
    """hepatic excretion: An excretion process involving the elimination of compounds and metabolites via the liver (often into bile)."""

    HEPATIC_EXCRETION: "PBPKO"
    """hepatic excretion: An excretion process involving the elimination of compounds and metabolites via the liver (often into bile)."""

    PBPKO_00225: "PBPKO"
    """fecal excretion: An excretion process involving the elimination of compounds and metabolites through feces."""

    FECAL_EXCRETION: "PBPKO"
    """fecal excretion: An excretion process involving the elimination of compounds and metabolites through feces."""

    PBPKO_00226: "PBPKO"
    """exhalation: An excretion process involving the elimination of volatile compounds and metabolites through respiration."""

    EXHALATION: "PBPKO"
    """exhalation: An excretion process involving the elimination of volatile compounds and metabolites through respiration."""

    PBPKO_00227: "PBPKO"
    """sweat excretion: An excretion process involving the elimination of compounds and metabolites through sweat."""

    SWEAT_EXCRETION: "PBPKO"
    """sweat excretion: An excretion process involving the elimination of compounds and metabolites through sweat."""

    PBPKO_00228: "PBPKO"
    """hair excretion: An excretion process involving the elimination and deposition of compounds and metabolites into hair."""

    HAIR_EXCRETION: "PBPKO"
    """hair excretion: An excretion process involving the elimination and deposition of compounds and metabolites into hair."""

    PBPKO_00229: "PBPKO"
    """clearance rate: A biochemical parameter representing the volume of biological fluid cleared of a compound per unit time."""

    CLEARANCE_RATE: "PBPKO"
    """clearance rate: A biochemical parameter representing the volume of biological fluid cleared of a compound per unit time."""

    PBPKO_00230: "PBPKO"
    """fecal clearance rate: A clearance rate specifically quantifying elimination via feces."""

    FECAL_CLEARANCE_RATE: "PBPKO"
    """fecal clearance rate: A clearance rate specifically quantifying elimination via feces."""

    PBPKO_00231: "PBPKO"
    """sweat clearance rate: A clearance rate specifically quantifying elimination via sweat."""

    SWEAT_CLEARANCE_RATE: "PBPKO"
    """sweat clearance rate: A clearance rate specifically quantifying elimination via sweat."""

    PBPKO_00232: "PBPKO"
    """urinary clearance rate: A clearance rate specifically quantifying elimination via urine."""

    URINARY_CLEARANCE_RATE: "PBPKO"
    """urinary clearance rate: A clearance rate specifically quantifying elimination via urine."""

    PBPKO_00233: "PBPKO"
    """biliary clearance rate: A clearance rate specifically quantifying elimination via bile."""

    BILIARY_CLEARANCE_RATE: "PBPKO"
    """biliary clearance rate: A clearance rate specifically quantifying elimination via bile."""

    PBPKO_00234: "PBPKO"
    """hepatic clearance rate: A clearance rate specifically quantifying elimination via the liver (metabolism and/or biliary excretion)."""

    HEPATIC_CLEARANCE_RATE: "PBPKO"
    """hepatic clearance rate: A clearance rate specifically quantifying elimination via the liver (metabolism and/or biliary excretion)."""

    PBPKO_00235: "PBPKO"
    """intrinsic clearance rate: A clearance rate representing the inherent ability of an organ or tissue to eliminate a compound, independent of blood flow or binding."""

    INTRINSIC_CLEARANCE_RATE: "PBPKO"
    """intrinsic clearance rate: A clearance rate representing the inherent ability of an organ or tissue to eliminate a compound, independent of blood flow or binding."""

    PBPKO_00236: "PBPKO"
    """fecal elimination rate constant: A biochemical parameter representing the rate constant for elimination via fecal excretion."""

    FECAL_ELIMINATION_RATE_CONSTANT: "PBPKO"
    """fecal elimination rate constant: A biochemical parameter representing the rate constant for elimination via fecal excretion."""

    PBPKO_00237: "PBPKO"
    """renal elimination rate constant: A biochemical parameter representing the rate constant for elimination via renal (urinary) excretion."""

    RENAL_ELIMINATION_RATE_CONSTANT: "PBPKO"
    """renal elimination rate constant: A biochemical parameter representing the rate constant for elimination via renal (urinary) excretion."""

    PBPKO_00238: "PBPKO"
    """biliary elimination: An elimination process involving the irreversible transfer of compound or metabolites from plasma to bile via hepatocytes."""

    BILIARY_ELIMINATION: "PBPKO"
    """biliary elimination: An elimination process involving the irreversible transfer of compound or metabolites from plasma to bile via hepatocytes."""

    PBPKO_00239: "PBPKO"
    """route of exposure: A parameter designating the body part or method through which exposure is introduced."""

    ROUTE_OF_EXPOSURE: "PBPKO"
    """route of exposure: A parameter designating the body part or method through which exposure is introduced."""

    PBPKO_00240: "PBPKO"
    """oral exposure: A route of exposure via the mouth."""

    ORAL_EXPOSURE: "PBPKO"
    """oral exposure: A route of exposure via the mouth."""

    PBPKO_00241: "PBPKO"
    """dermal exposure: A route of exposure via the skin."""

    DERMAL_EXPOSURE: "PBPKO"
    """dermal exposure: A route of exposure via the skin."""

    PBPKO_00242: "PBPKO"
    """inhalation exposure: A route of exposure via inhalation into the lungs."""

    INHALATION_EXPOSURE: "PBPKO"
    """inhalation exposure: A route of exposure via inhalation into the lungs."""

    PBPKO_00243: "PBPKO"
    """intravenous bolus exposure: A route of exposure involving rapid injection directly into a vein."""

    INTRAVENOUS_BOLUS_EXPOSURE: "PBPKO"
    """intravenous bolus exposure: A route of exposure involving rapid injection directly into a vein."""

    PBPKO_00244: "PBPKO"
    """intravenous infusion exposure: A route of exposure involving continuous administration directly into a vein over time."""

    INTRAVENOUS_INFUSION_EXPOSURE: "PBPKO"
    """intravenous infusion exposure: A route of exposure involving continuous administration directly into a vein over time."""

    PBPKO_00245: "PBPKO"
    """intramuscular exposure: A route of exposure involving injection into a muscle."""

    INTRAMUSCULAR_EXPOSURE: "PBPKO"
    """intramuscular exposure: A route of exposure involving injection into a muscle."""

    PBPKO_00246: "PBPKO"
    """intraarterial exposure: A route of exposure involving administration directly into an artery."""

    INTRAARTERIAL_EXPOSURE: "PBPKO"
    """intraarterial exposure: A route of exposure involving administration directly into an artery."""

    PBPKO_00247: "PBPKO"
    """intrathecal exposure: A route of exposure involving administration into the spinal canal."""

    INTRATHECAL_EXPOSURE: "PBPKO"
    """intrathecal exposure: A route of exposure involving administration into the spinal canal."""

    PBPKO_00248: "PBPKO"
    """subcutaneous exposure: A route of exposure involving administration under the skin."""

    SUBCUTANEOUS_EXPOSURE: "PBPKO"
    """subcutaneous exposure: A route of exposure involving administration under the skin."""

    PBPKO_00249: "PBPKO"
    """nasal exposure: A route of exposure via the nasal passages."""

    NASAL_EXPOSURE: "PBPKO"
    """nasal exposure: A route of exposure via the nasal passages."""

    PBPKO_00250: "PBPKO"
    """transdermal exposure: A route of exposure involving absorption through the skin, typically from a patch."""

    TRANSDERMAL_EXPOSURE: "PBPKO"
    """transdermal exposure: A route of exposure involving absorption through the skin, typically from a patch."""

    PBPKO_00251: "PBPKO"
    """ocular exposure: A route of exposure via the eye."""

    OCULAR_EXPOSURE: "PBPKO"
    """ocular exposure: A route of exposure via the eye."""

    PBPKO_00252: "PBPKO"
    """output parameter: A parameter representing a result or prediction generated by the PBPK model."""

    OUTPUT_PARAMETER: "PBPKO"
    """output parameter: A parameter representing a result or prediction generated by the PBPK model."""

    PBPKO_00253: "PBPKO"
    """peak concentration: An output parameter representing the highest concentration (Cmax) of a compound achieved after exposure."""

    PEAK_CONCENTRATION: "PBPKO"
    """peak concentration: An output parameter representing the highest concentration (Cmax) of a compound achieved after exposure."""

    PBPKO_00254: "PBPKO"
    """maximum steady state concentration: An output parameter representing the maximum concentration (Cmax,ss) achieved at steady state during repeated dosing."""

    MAXIMUM_STEADY_STATE_CONCENTRATION: "PBPKO"
    """maximum steady state concentration: An output parameter representing the maximum concentration (Cmax,ss) achieved at steady state during repeated dosing."""

    PBPKO_00255: "PBPKO"
    """maximum time: An output parameter representing the time (Tmax) required to reach the peak concentration."""

    MAXIMUM_TIME: "PBPKO"
    """maximum time: An output parameter representing the time (Tmax) required to reach the peak concentration."""

    PBPKO_00256: "PBPKO"
    """area under curve: An output parameter representing the integral of the concentration-time curve (AUC), indicating total exposure."""

    AREA_UNDER_CURVE: "PBPKO"
    """area under curve: An output parameter representing the integral of the concentration-time curve (AUC), indicating total exposure."""

    PBPKO_00257: "PBPKO"
    """area under curve 0 to t: An area under curve parameter calculated from time zero to a specific time point t (AUC0-t)."""

    AREA_UNDER_CURVE_0_TO_T: "PBPKO"
    """area under curve 0 to t: An area under curve parameter calculated from time zero to a specific time point t (AUC0-t)."""

    PBPKO_00258: "PBPKO"
    """area under curve last: An area under curve parameter calculated from time zero to the time of the last measurable concentration (AUClast)."""

    AREA_UNDER_CURVE_LAST: "PBPKO"
    """area under curve last: An area under curve parameter calculated from time zero to the time of the last measurable concentration (AUClast)."""

    PBPKO_00259: "PBPKO"
    """area under curve 0 to infinity: An area under curve parameter extrapolated from time zero to infinity (AUC0-inf), representing total exposure after a single dose."""

    AREA_UNDER_CURVE_0_TO_INFINITY: "PBPKO"
    """area under curve 0 to infinity: An area under curve parameter extrapolated from time zero to infinity (AUC0-inf), representing total exposure after a single dose."""

    PBPKO_00260: "PBPKO"
    """area under moment curve: An output parameter calculated as the integral of the product of time and concentration versus time (AUMC)."""

    AREA_UNDER_MOMENT_CURVE: "PBPKO"
    """area under moment curve: An output parameter calculated as the integral of the product of time and concentration versus time (AUMC)."""

    PBPKO_00261: "PBPKO"
    """mean residence time: An output parameter representing the average time a compound resides in the body (MRT)."""

    MEAN_RESIDENCE_TIME: "PBPKO"
    """mean residence time: An output parameter representing the average time a compound resides in the body (MRT)."""

    PBPKO_00262: "PBPKO"
    """half-life: An output parameter representing the time required for the compound concentration to decrease by half (t1/2)."""

    HALF_LIFE: "PBPKO"
    """half-life: An output parameter representing the time required for the compound concentration to decrease by half (t1/2)."""

    PBPKO_00263: "PBPKO"
    """bioavailability: An output parameter representing the rate and extent to which an active compound is absorbed and becomes available at the site of action or systemic circulation."""

    BIOAVAILABILITY: "PBPKO"
    """bioavailability: An output parameter representing the rate and extent to which an active compound is absorbed and becomes available at the site of action or systemic circulation."""

    PBPKO_00264: "PBPKO"
    """relative bioavailability: A bioavailability parameter comparing the rate and extent of absorption of a test compound to a reference compound."""

    RELATIVE_BIOAVAILABILITY: "PBPKO"
    """relative bioavailability: A bioavailability parameter comparing the rate and extent of absorption of a test compound to a reference compound."""

    PBPKO_00265: "PBPKO"
    """mean absorption time: An output parameter representing the average time for a compound to be absorbed into systemic circulation (MAT)."""

    MEAN_ABSORPTION_TIME: "PBPKO"
    """mean absorption time: An output parameter representing the average time for a compound to be absorbed into systemic circulation (MAT)."""

    PBPKO_00266: "PBPKO"
    """mean dissolution time: An output parameter representing the average time for a compound to dissolve in the body (MDT)."""

    MEAN_DISSOLUTION_TIME: "PBPKO"
    """mean dissolution time: An output parameter representing the average time for a compound to dissolve in the body (MDT)."""

    PBPKO_00267: "PBPKO"
    """bioequivalence: An output parameter indicating comparable bioavailability between test and reference formulations under similar conditions."""

    BIOEQUIVALENCE: "PBPKO"
    """bioequivalence: An output parameter indicating comparable bioavailability between test and reference formulations under similar conditions."""

    PBPKO_00268: "PBPKO"
    """absolute bioavailability: A bioavailability parameter comparing the amount reaching systemic circulation after non-IV administration to the amount available after IV administration."""

    ABSOLUTE_BIOAVAILABILITY: "PBPKO"
    """absolute bioavailability: A bioavailability parameter comparing the amount reaching systemic circulation after non-IV administration to the amount available after IV administration."""

    PBPKO_00269: "PBPKO"
    """elimination phase: An elimination process phase describing the period where removal of the compound from the body predominates."""

    ELIMINATION_PHASE: "PBPKO"
    """elimination phase: An elimination process phase describing the period where removal of the compound from the body predominates."""

    PBPKO_00270: "PBPKO"
    """absorption phase: An absorption process phase describing the period where the compound moves from the administration site into systemic circulation."""

    ABSORPTION_PHASE: "PBPKO"
    """absorption phase: An absorption process phase describing the period where the compound moves from the administration site into systemic circulation."""

    PBPKO_00272: "PBPKO"
    """amount in urine: The amount of compound in the urine compartment."""

    AMOUNT_IN_URINE: "PBPKO"
    """amount in urine: The amount of compound in the urine compartment."""

    PBPKO_00273: "PBPKO"
    """amount in feces: The amount of compound in the feces compartment."""

    AMOUNT_IN_FECES: "PBPKO"
    """amount in feces: The amount of compound in the feces compartment."""

    PBPKO_00274: "PBPKO"
    """cumulative amount in urine: An output parameter representing the total amount of compound excreted in urine over a specific time period."""

    CUMULATIVE_AMOUNT_IN_URINE: "PBPKO"
    """cumulative amount in urine: An output parameter representing the total amount of compound excreted in urine over a specific time period."""

    PBPKO_00275: "PBPKO"
    """cumulative amount in feces: An output parameter representing the total amount of compound excreted in feces over a specific time period."""

    CUMULATIVE_AMOUNT_IN_FECES: "PBPKO"
    """cumulative amount in feces: An output parameter representing the total amount of compound excreted in feces over a specific time period."""

    PBPKO_00277: "PBPKO"
    """steady state area under curve: An area under curve parameter calculated over a dosing interval at steady state (AUCss)."""

    STEADY_STATE_AREA_UNDER_CURVE: "PBPKO"
    """steady state area under curve: An area under curve parameter calculated over a dosing interval at steady state (AUCss)."""

    PBPKO_00279: "PBPKO"
    """min organ concentration: An output parameter representing the minimum concentration of a compound in a specific organ after exposure."""

    MIN_ORGAN_CONCENTRATION: "PBPKO"
    """min organ concentration: An output parameter representing the minimum concentration of a compound in a specific organ after exposure."""

    PBPKO_00280: "PBPKO"
    """max organ concentration: An output parameter representing the maximum concentration of a compound in a specific organ after exposure."""

    MAX_ORGAN_CONCENTRATION: "PBPKO"
    """max organ concentration: An output parameter representing the maximum concentration of a compound in a specific organ after exposure."""

    PBPKO_00281: "PBPKO"
    """median organ concentration: An output parameter representing the median concentration of a compound in a specific organ after exposure."""

    MEDIAN_ORGAN_CONCENTRATION: "PBPKO"
    """median organ concentration: An output parameter representing the median concentration of a compound in a specific organ after exposure."""

    PBPKO_00282: "PBPKO"
    """percentile 2.5 cplasma: A plasma concentration parameter representing the 2.5th percentile of the plasma concentration distribution in a population simulation."""

    PERCENTILE_2_5_CPLASMA: "PBPKO"
    """percentile 2.5 cplasma: A plasma concentration parameter representing the 2.5th percentile of the plasma concentration distribution in a population simulation."""

    PBPKO_00283: "PBPKO"
    """percentile 97.5 cplasma: A plasma concentration parameter representing the 97.5th percentile of the plasma concentration distribution in a population simulation."""

    PERCENTILE_97_5_CPLASMA: "PBPKO"
    """percentile 97.5 cplasma: A plasma concentration parameter representing the 97.5th percentile of the plasma concentration distribution in a population simulation."""

    PBPKO_00284: "PBPKO"
    """tolerable daily intake: An output parameter (or exposure limit) estimating the amount of a substance that can be ingested daily over a lifetime without appreciable health risk (TDI)."""

    TOLERABLE_DAILY_INTAKE: "PBPKO"
    """tolerable daily intake: An output parameter (or exposure limit) estimating the amount of a substance that can be ingested daily over a lifetime without appreciable health risk (TDI)."""

    PBPKO_00285: "PBPKO"
    """reconstructed exposure: An output parameter estimating the amount of compound exposure based on internal body measurements."""

    RECONSTRUCTED_EXPOSURE: "PBPKO"
    """reconstructed exposure: An output parameter estimating the amount of compound exposure based on internal body measurements."""

    PBPKO_00286: "PBPKO"
    """estimated daily intake: An output parameter estimating the amount of a compound consumed daily (EDI)."""

    ESTIMATED_DAILY_INTAKE: "PBPKO"
    """estimated daily intake: An output parameter estimating the amount of a compound consumed daily (EDI)."""

    PBPKO_00287: "PBPKO"
    """biomonitoring equivalent: An output parameter representing the concentration of a chemical (or metabolite) in a biological medium consistent with exposure guidance values (BE)."""

    BIOMONITORING_EQUIVALENT: "PBPKO"
    """biomonitoring equivalent: An output parameter representing the concentration of a chemical (or metabolite) in a biological medium consistent with exposure guidance values (BE)."""

    PBPKO_00289: "PBPKO"
    """reference dose: An output parameter (or exposure limit) estimating the daily oral or dermal exposure likely to be without appreciable risk over a lifetime (RfD)."""

    REFERENCE_DOSE: "PBPKO"
    """reference dose: An output parameter (or exposure limit) estimating the daily oral or dermal exposure likely to be without appreciable risk over a lifetime (RfD)."""

    PBPKO_00290: "PBPKO"
    """acceptable daily intake: An output parameter (or exposure limit) estimating the amount of a substance in food/water that can be consumed daily without appreciable health risk (ADI)."""

    ACCEPTABLE_DAILY_INTAKE: "PBPKO"
    """acceptable daily intake: An output parameter (or exposure limit) estimating the amount of a substance in food/water that can be consumed daily without appreciable health risk (ADI)."""

    PBPKO_00296: "PBPKO"
    """reference human data set: A data set containing the physiological parameters representing a standard human, often defined by specific characteristics like 70 kg body weight."""

    REFERENCE_HUMAN_DATA_SET: "PBPKO"
    """reference human data set: A data set containing the physiological parameters representing a standard human, often defined by specific characteristics like 70 kg body weight."""

    PBPKO_00297: "PBPKO"
    """biological matrix concentration: An output parameter representing the total concentration of a compound in a specified biological matrix."""

    BIOLOGICAL_MATRIX_CONCENTRATION: "PBPKO"
    """biological matrix concentration: An output parameter representing the total concentration of a compound in a specified biological matrix."""

    PBPKO_00298: "PBPKO"
    """concentration in hair: The total concentration of compound in the hair compartment."""

    CONCENTRATION_IN_HAIR: "PBPKO"
    """concentration in hair: The total concentration of compound in the hair compartment."""

    PBPKO_00299: "PBPKO"
    """concentration in nail: A biological matrix concentration specifically representing the total concentration of compound in the nail compartment."""

    CONCENTRATION_IN_NAIL: "PBPKO"
    """concentration in nail: A biological matrix concentration specifically representing the total concentration of compound in the nail compartment."""

    PBPKO_00300: "PBPKO"
    """concentration in teeth: A biological matrix concentration specifically representing the total concentration of compound in the teeth compartment."""

    CONCENTRATION_IN_TEETH: "PBPKO"
    """concentration in teeth: A biological matrix concentration specifically representing the total concentration of compound in the teeth compartment."""

    PBPKO_00301: "PBPKO"
    """concentration in blood: The total concentration of compound in the blood compartment."""

    CONCENTRATION_IN_BLOOD: "PBPKO"
    """concentration in blood: The total concentration of compound in the blood compartment."""

    PBPKO_00302: "PBPKO"
    """concentration in urine: A biological matrix concentration specifically representing the total concentration of compound in the urine compartment."""

    CONCENTRATION_IN_URINE: "PBPKO"
    """concentration in urine: A biological matrix concentration specifically representing the total concentration of compound in the urine compartment."""

    PBPKO_00303: "PBPKO"
    """permeability limited pbpk: A physiologically based pharmacokinetic model that considers the permeability across membranes as a limiting factor for compound distribution."""

    PERMEABILITY_LIMITED_PBPK: "PBPKO"
    """permeability limited pbpk: A physiologically based pharmacokinetic model that considers the permeability across membranes as a limiting factor for compound distribution."""

    PBPKO_00304: "PBPKO"
    """maximum rate of basolateral transporter in vitro: Maximum rate (Vmax) of transport via a basolateral transporter, measured in vitro."""

    MAXIMUM_RATE_OF_BASOLATERAL_TRANSPORTER_IN_VITRO: "PBPKO"
    """maximum rate of basolateral transporter in vitro: Maximum rate (Vmax) of transport via a basolateral transporter, measured in vitro."""

    PBPKO_00305: "PBPKO"
    """Michaelis constant baso: Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for a basolateral transporter."""

    MICHAELIS_CONSTANT_BASO: "PBPKO"
    """Michaelis constant baso: Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for a basolateral transporter."""

    PBPKO_00306: "PBPKO"
    """maximum rate of apical transporter in vitro: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ, measured in vitro, when the enzyme is saturated with substrate."""

    MAXIMUM_RATE_OF_APICAL_TRANSPORTER_IN_VITRO: "PBPKO"
    """maximum rate of apical transporter in vitro: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ, measured in vitro, when the enzyme is saturated with substrate."""

    PBPKO_00307: "PBPKO"
    """Michaelis constant apical: Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for an apical transporter."""

    MICHAELIS_CONSTANT_APICAL: "PBPKO"
    """Michaelis constant apical: Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for an apical transporter."""

    PBPKO_00310: "PBPKO"
    """influx constant: A biochemical parameter (kin) describing the rate constant for compound movement into a cell or compartment."""

    INFLUX_CONSTANT: "PBPKO"
    """influx constant: A biochemical parameter (kin) describing the rate constant for compound movement into a cell or compartment."""

    PBPKO_00311: "PBPKO"
    """efflux rate constant: A biochemical parameter (kefflux) describing the rate constant for compound movement out of a cell or compartment."""

    EFFLUX_RATE_CONSTANT: "PBPKO"
    """efflux rate constant: A biochemical parameter (kefflux) describing the rate constant for compound movement out of a cell or compartment."""

    PBPKO_00312: "PBPKO"
    """plasma space: A physiological parameter representing the volume occupied by plasma within a tissue or the body."""

    PLASMA_SPACE: "PBPKO"
    """plasma space: A physiological parameter representing the volume occupied by plasma within a tissue or the body."""

    PBPKO_00313: "PBPKO"
    """endosomal space compartment: A compartment representing the endosomal space within cells."""

    ENDOSOMAL_SPACE_COMPARTMENT: "PBPKO"
    """endosomal space compartment: A compartment representing the endosomal space within cells."""

    PBPKO_00314: "PBPKO"
    """interstitial space: A physiological parameter representing the fluid-filled space between blood vessels and cells."""

    INTERSTITIAL_SPACE: "PBPKO"
    """interstitial space: A physiological parameter representing the fluid-filled space between blood vessels and cells."""

    PBPKO_00315: "PBPKO"
    """effective permeability: A biochemical parameter (Peff) representing the rate at which a compound passes through a biological barrier (e.g., intestinal wall)."""

    EFFECTIVE_PERMEABILITY: "PBPKO"
    """effective permeability: A biochemical parameter (Peff) representing the rate at which a compound passes through a biological barrier (e.g., intestinal wall)."""

    PBPKO_00316: "PBPKO"
    """population pbpk: A physiologically based pharmacokinetic model approach used to characterize interindividual variability within a population."""

    POPULATION_PBPK: "PBPKO"
    """population pbpk: A physiologically based pharmacokinetic model approach used to characterize interindividual variability within a population."""

    PBPKO_00317: "PBPKO"
    """top-down pbpk: A physiologically based pharmacokinetic model approach primarily based on fitting observed clinical data, often empirical."""

    TOP_DOWN_PBPK: "PBPKO"
    """top-down pbpk: A physiologically based pharmacokinetic model approach primarily based on fitting observed clinical data, often empirical."""

    PBPKO_00318: "PBPKO"
    """bottom-up pbpk: A physiologically based pharmacokinetic model approach built mechanistically using in vitro and physiological data."""

    BOTTOM_UP_PBPK: "PBPKO"
    """bottom-up pbpk: A physiologically based pharmacokinetic model approach built mechanistically using in vitro and physiological data."""

    PBPKO_00319: "PBPKO"
    """one-compartment pbpk: A physiologically based pharmacokinetic model that treats the entire body as a single, kinetically homogenous unit (central compartment)."""

    ONE_COMPARTMENT_PBPK: "PBPKO"
    """one-compartment pbpk: A physiologically based pharmacokinetic model that treats the entire body as a single, kinetically homogenous unit (central compartment)."""

    PBPKO_00320: "PBPKO"
    """central compartment: A compartment in a multi-compartment model representing plasma and highly perfused tissues where distribution is rapid."""

    CENTRAL_COMPARTMENT: "PBPKO"
    """central compartment: A compartment in a multi-compartment model representing plasma and highly perfused tissues where distribution is rapid."""

    PBPKO_00321: "PBPKO"
    """peripheral compartment: A compartment in a multi-compartment model representing tissues where compound distribution is slower compared to the central compartment."""

    PERIPHERAL_COMPARTMENT: "PBPKO"
    """peripheral compartment: A compartment in a multi-compartment model representing tissues where compound distribution is slower compared to the central compartment."""

    PBPKO_00322: "PBPKO"
    """elimination: A biological process involving the irreversible removal of a compound from the body, encompassing metabolism and excretion."""

    ELIMINATION: "PBPKO"
    """elimination: A biological process involving the irreversible removal of a compound from the body, encompassing metabolism and excretion."""

    PBPKO_00323: "PBPKO"
    """linear elimination: An elimination process that follows first-order kinetics (rate proportional to concentration)."""

    LINEAR_ELIMINATION: "PBPKO"
    """linear elimination: An elimination process that follows first-order kinetics (rate proportional to concentration)."""

    PBPKO_00324: "PBPKO"
    """non-linear elimination: An elimination process that does not follow first-order kinetics (e.g., saturable processes)."""

    NON_LINEAR_ELIMINATION: "PBPKO"
    """non-linear elimination: An elimination process that does not follow first-order kinetics (e.g., saturable processes)."""

    PBPKO_00332: "PBPKO"
    """lifestage: A physiological parameter representing distinct phases of an individual's life (e.g., infant, adult, geriatric)."""

    LIFESTAGE: "PBPKO"
    """lifestage: A physiological parameter representing distinct phases of an individual's life (e.g., infant, adult, geriatric)."""

    PBPKO_00333: "PBPKO"
    """fetus lifestage: A lifestage parameter representing the unborn offspring from the postembryonic stage until birth."""

    FETUS_LIFESTAGE: "PBPKO"
    """fetus lifestage: A lifestage parameter representing the unborn offspring from the postembryonic stage until birth."""

    PBPKO_00334: "PBPKO"
    """infant lifestage: A lifestage parameter representing a very young child, typically under one year of age."""

    INFANT_LIFESTAGE: "PBPKO"
    """infant lifestage: A lifestage parameter representing a very young child, typically under one year of age."""

    PBPKO_00335: "PBPKO"
    """toddler lifestage: A lifestage parameter representing a young child, typically between one and three years old."""

    TODDLER_LIFESTAGE: "PBPKO"
    """toddler lifestage: A lifestage parameter representing a young child, typically between one and three years old."""

    PBPKO_00336: "PBPKO"
    """child lifestage: A lifestage parameter representing individuals typically between 3 and 11 years old."""

    CHILD_LIFESTAGE: "PBPKO"
    """child lifestage: A lifestage parameter representing individuals typically between 3 and 11 years old."""

    PBPKO_00337: "PBPKO"
    """teenager lifestage: A lifestage parameter representing individuals typically between eleven and fifteen years old."""

    TEENAGER_LIFESTAGE: "PBPKO"
    """teenager lifestage: A lifestage parameter representing individuals typically between eleven and fifteen years old."""

    PBPKO_00338: "PBPKO"
    """adolescent lifestage: A lifestage parameter representing the transitional stage between teenager and adulthood (approx. 15-18 years)."""

    ADOLESCENT_LIFESTAGE: "PBPKO"
    """adolescent lifestage: A lifestage parameter representing the transitional stage between teenager and adulthood (approx. 15-18 years)."""

    PBPKO_00339: "PBPKO"
    """adult lifestage: A lifestage parameter representing individuals typically from eighteen to thirty years old."""

    ADULT_LIFESTAGE: "PBPKO"
    """adult lifestage: A lifestage parameter representing individuals typically from eighteen to thirty years old."""

    PBPKO_00340: "PBPKO"
    """middle age lifestage: A lifestage parameter representing individuals typically from thirty to forty-five years old."""

    MIDDLE_AGE_LIFESTAGE: "PBPKO"
    """middle age lifestage: A lifestage parameter representing individuals typically from thirty to forty-five years old."""

    PBPKO_00341: "PBPKO"
    """old age lifestage: A lifestage parameter representing individuals typically from forty-five to sixty years old (or older, definitions vary)."""

    OLD_AGE_LIFESTAGE: "PBPKO"
    """old age lifestage: A lifestage parameter representing individuals typically from forty-five to sixty years old (or older, definitions vary)."""

    PBPKO_00342: "PBPKO"
    """pediatric lifestage: A lifestage parameter representing individuals typically below fifteen years of age."""

    PEDIATRIC_LIFESTAGE: "PBPKO"
    """pediatric lifestage: A lifestage parameter representing individuals typically below fifteen years of age."""

    PBPKO_00343: "PBPKO"
    """geriatric lifestage: A lifestage parameter representing older adults, often considered 60/65 years and older."""

    GERIATRIC_LIFESTAGE: "PBPKO"
    """geriatric lifestage: A lifestage parameter representing older adults, often considered 60/65 years and older."""

    PBPKO_00347: "PBPKO"
    """brain pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations in the brain."""

    BRAIN_PBPK: "PBPKO"
    """brain pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations in the brain."""

    PBPKO_00348: "PBPKO"
    """cerebrospinal fluid volume: A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the spinal region."""

    CEREBROSPINAL_FLUID_VOLUME: "PBPKO"
    """cerebrospinal fluid volume: A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the spinal region."""

    PBPKO_00349: "PBPKO"
    """cranial cerebrospinal fluid volume: A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the cranial region."""

    CRANIAL_CEREBROSPINAL_FLUID_VOLUME: "PBPKO"
    """cranial cerebrospinal fluid volume: A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the cranial region."""

    PBPKO_00350: "PBPKO"
    """brain mass: A physiological parameter representing the mass of the brain."""

    BRAIN_MASS: "PBPKO"
    """brain mass: A physiological parameter representing the mass of the brain."""

    PBPKO_00351: "PBPKO"
    """blood brain barrier compartment: A barrier compartment representing the blood-brain barrier (BBB)."""

    BLOOD_BRAIN_BARRIER_COMPARTMENT: "PBPKO"
    """blood brain barrier compartment: A barrier compartment representing the blood-brain barrier (BBB)."""

    PBPKO_00352: "PBPKO"
    """spinal cerebrospinal fluid flow rate: A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the spinal region."""

    SPINAL_CEREBROSPINAL_FLUID_FLOW_RATE: "PBPKO"
    """spinal cerebrospinal fluid flow rate: A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the spinal region."""

    PBPKO_00353: "PBPKO"
    """cranial cerebrospinal fluid flow rate: A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the cranial region."""

    CRANIAL_CEREBROSPINAL_FLUID_FLOW_RATE: "PBPKO"
    """cranial cerebrospinal fluid flow rate: A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the cranial region."""

    PBPKO_00354: "PBPKO"
    """blood cerebrospinal fluid compartment: A barrier compartment representing the blood-cerebrospinal fluid barrier (BCSFB)."""

    BLOOD_CEREBROSPINAL_FLUID_COMPARTMENT: "PBPKO"
    """blood cerebrospinal fluid compartment: A barrier compartment representing the blood-cerebrospinal fluid barrier (BCSFB)."""

    PBPKO_00355: "PBPKO"
    """volume of hippocampus: A volume parameter representing the total volume of the hippocampus compartment."""

    VOLUME_OF_HIPPOCAMPUS: "PBPKO"
    """volume of hippocampus: A volume parameter representing the total volume of the hippocampus compartment."""

    PBPKO_00356: "PBPKO"
    """volume of frontal cortex: A volume parameter representing the total volume of the frontal cortex compartment."""

    VOLUME_OF_FRONTAL_CORTEX: "PBPKO"
    """volume of frontal cortex: A volume parameter representing the total volume of the frontal cortex compartment."""

    PBPKO_00357: "PBPKO"
    """volume of cerebrum: A volume parameter representing the total volume of the cerebrum compartment."""

    VOLUME_OF_CEREBRUM: "PBPKO"
    """volume of cerebrum: A volume parameter representing the total volume of the cerebrum compartment."""

    PBPKO_00358: "PBPKO"
    """volume of cerebellum: A volume parameter representing the total volume of the cerebellum compartment."""

    VOLUME_OF_CEREBELLUM: "PBPKO"
    """volume of cerebellum: A volume parameter representing the total volume of the cerebellum compartment."""

    PBPKO_00359: "PBPKO"
    """blood flow rate to hippocampus: A blood flow rate parameter specifically describing the rate to the hippocampus compartment."""

    BLOOD_FLOW_RATE_TO_HIPPOCAMPUS: "PBPKO"
    """blood flow rate to hippocampus: A blood flow rate parameter specifically describing the rate to the hippocampus compartment."""

    PBPKO_00360: "PBPKO"
    """blood flow rate to frontal cortex: A blood flow rate parameter specifically describing the rate to the frontal cortex compartment."""

    BLOOD_FLOW_RATE_TO_FRONTAL_CORTEX: "PBPKO"
    """blood flow rate to frontal cortex: A blood flow rate parameter specifically describing the rate to the frontal cortex compartment."""

    PBPKO_00361: "PBPKO"
    """blood flow rate to cerebrum: A blood flow rate parameter specifically describing the rate to the cerebrum compartment."""

    BLOOD_FLOW_RATE_TO_CEREBRUM: "PBPKO"
    """blood flow rate to cerebrum: A blood flow rate parameter specifically describing the rate to the cerebrum compartment."""

    PBPKO_00362: "PBPKO"
    """blood flow rate to cerebellum: A blood flow rate parameter specifically describing the rate to the cerebellum compartment."""

    BLOOD_FLOW_RATE_TO_CEREBELLUM: "PBPKO"
    """blood flow rate to cerebellum: A blood flow rate parameter specifically describing the rate to the cerebellum compartment."""

    PBPKO_00363: "PBPKO"
    """hippocampus brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the hippocampus to the overall brain."""

    HIPPOCAMPUS_BRAIN_PARTITION_COEFFICIENT: "PBPKO"
    """hippocampus brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the hippocampus to the overall brain."""

    PBPKO_00364: "PBPKO"
    """cerebrum brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the cerebrum to the overall brain."""

    CEREBRUM_BRAIN_PARTITION_COEFFICIENT: "PBPKO"
    """cerebrum brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the cerebrum to the overall brain."""

    PBPKO_00365: "PBPKO"
    """cerebellum brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the cerebellum to the overall brain."""

    CEREBELLUM_BRAIN_PARTITION_COEFFICIENT: "PBPKO"
    """cerebellum brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the cerebellum to the overall brain."""

    PBPKO_00366: "PBPKO"
    """frontalcortex brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the frontal cortex to the overall brain."""

    FRONTALCORTEX_BRAIN_PARTITION_COEFFICIENT: "PBPKO"
    """frontalcortex brain partition coefficient: A partition coefficient representing the ratio of compound concentration in the frontal cortex to the overall brain."""

    PBPKO_00367: "PBPKO"
    """apparent permeability cerebrum to rest of brain: Apparent permeability of a compound specifically between the cerebrum and the rest of the brain."""

    APPARENT_PERMEABILITY_CEREBRUM_TO_REST_OF_BRAIN: "PBPKO"
    """apparent permeability cerebrum to rest of brain: Apparent permeability of a compound specifically between the cerebrum and the rest of the brain."""

    PBPKO_00368: "PBPKO"
    """apparent permeability cerebellum to rest of brain: Apparent permeability of a compound specifically between the cerebellum and the rest of the brain."""

    APPARENT_PERMEABILITY_CEREBELLUM_TO_REST_OF_BRAIN: "PBPKO"
    """apparent permeability cerebellum to rest of brain: Apparent permeability of a compound specifically between the cerebellum and the rest of the brain."""

    PBPKO_00369: "PBPKO"
    """apparent permeability hippocampus to rest of brain: Apparent permeability of a compound specifically between the hippocampus and the rest of the brain."""

    APPARENT_PERMEABILITY_HIPPOCAMPUS_TO_REST_OF_BRAIN: "PBPKO"
    """apparent permeability hippocampus to rest of brain: Apparent permeability of a compound specifically between the hippocampus and the rest of the brain."""

    PBPKO_00370: "PBPKO"
    """apparent permeability cortex to rest of brain: Apparent permeability of a compound specifically between the cortex and the rest of the brain."""

    APPARENT_PERMEABILITY_CORTEX_TO_REST_OF_BRAIN: "PBPKO"
    """apparent permeability cortex to rest of brain: Apparent permeability of a compound specifically between the cortex and the rest of the brain."""

    PBPKO_00371: "PBPKO"
    """pregnant pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations during pregnancy."""

    PREGNANT_PBPK: "PBPKO"
    """pregnant pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations during pregnancy."""

    PBPKO_00372: "PBPKO"
    """fetoplacental volume: A volume parameter representing the total volume of the placental compartment for fetus."""

    FETOPLACENTAL_VOLUME: "PBPKO"
    """fetoplacental volume: A volume parameter representing the total volume of the placental compartment for fetus."""

    PBPKO_00373: "PBPKO"
    """volume of fetus: A volume parameter representing the total volume of the fetus."""

    VOLUME_OF_FETUS: "PBPKO"
    """volume of fetus: A volume parameter representing the total volume of the fetus."""

    PBPKO_00374: "PBPKO"
    """volume of placenta: A volume parameter representing the total volume of the placental compartment."""

    VOLUME_OF_PLACENTA: "PBPKO"
    """volume of placenta: A volume parameter representing the total volume of the placental compartment."""

    PBPKO_00375: "PBPKO"
    """volume of amniotic fluid: A volume parameter representing the total volume of the amniotic fluid compartment."""

    VOLUME_OF_AMNIOTIC_FLUID: "PBPKO"
    """volume of amniotic fluid: A volume parameter representing the total volume of the amniotic fluid compartment."""

    PBPKO_00376: "PBPKO"
    """volume of liver fetus: A volume parameter representing the total volume of the fetal liver compartment."""

    VOLUME_OF_LIVER_FETUS: "PBPKO"
    """volume of liver fetus: A volume parameter representing the total volume of the fetal liver compartment."""

    PBPKO_00377: "PBPKO"
    """volume of brain fetus: A volume parameter representing the total volume of the fetal brain compartment."""

    VOLUME_OF_BRAIN_FETUS: "PBPKO"
    """volume of brain fetus: A volume parameter representing the total volume of the fetal brain compartment."""

    PBPKO_00378: "PBPKO"
    """volume of kidney fetus: A volume parameter representing the total volume of the fetal kidney compartment."""

    VOLUME_OF_KIDNEY_FETUS: "PBPKO"
    """volume of kidney fetus: A volume parameter representing the total volume of the fetal kidney compartment."""

    PBPKO_00379: "PBPKO"
    """volume of rest body fetus: A volume parameter representing the total volume of the rest of body compartment within the fetus."""

    VOLUME_OF_REST_BODY_FETUS: "PBPKO"
    """volume of rest body fetus: A volume parameter representing the total volume of the rest of body compartment within the fetus."""

    PBPKO_00381: "PBPKO"
    """fetoplacental blood flow rate: A blood flow rate parameter representing the rate of blood flow between the fetus and the placenta compartment."""

    FETOPLACENTAL_BLOOD_FLOW_RATE: "PBPKO"
    """fetoplacental blood flow rate: A blood flow rate parameter representing the rate of blood flow between the fetus and the placenta compartment."""

    PBPKO_00382: "PBPKO"
    """fetal cardiac output rate: A blood flow rate parameter representing the volume of blood pumped by the fetal heart compartment per unit time."""

    FETAL_CARDIAC_OUTPUT_RATE: "PBPKO"
    """fetal cardiac output rate: A blood flow rate parameter representing the volume of blood pumped by the fetal heart compartment per unit time."""

    PBPKO_00383: "PBPKO"
    """blood flow rate to liverfetus: A blood flow rate parameter specifically describing the rate to the fetal liver compartment."""

    BLOOD_FLOW_RATE_TO_LIVERFETUS: "PBPKO"
    """blood flow rate to liverfetus: A blood flow rate parameter specifically describing the rate to the fetal liver compartment."""

    PBPKO_00384: "PBPKO"
    """blood flow rate to kidneyfetus: A blood flow rate parameter specifically describing the rate to the fetal kidney compartment."""

    BLOOD_FLOW_RATE_TO_KIDNEYFETUS: "PBPKO"
    """blood flow rate to kidneyfetus: A blood flow rate parameter specifically describing the rate to the fetal kidney compartment."""

    PBPKO_00385: "PBPKO"
    """blood flow rate to brain fetus: A blood flow rate parameter specifically describing the rate to the fetal brain compartment."""

    BLOOD_FLOW_RATE_TO_BRAIN_FETUS: "PBPKO"
    """blood flow rate to brain fetus: A blood flow rate parameter specifically describing the rate to the fetal brain compartment."""

    PBPKO_00386: "PBPKO"
    """blood flow rate to restbody fetus: A blood flow rate parameter specifically describing the rate to the rest of body compartment within the fetus."""

    BLOOD_FLOW_RATE_TO_RESTBODY_FETUS: "PBPKO"
    """blood flow rate to restbody fetus: A blood flow rate parameter specifically describing the rate to the rest of body compartment within the fetus."""

    PBPKO_00387: "PBPKO"
    """gestational age: A physiological parameter representing the age of a pregnancy, typically measured in weeks."""

    GESTATIONAL_AGE: "PBPKO"
    """gestational age: A physiological parameter representing the age of a pregnancy, typically measured in weeks."""

    PBPKO_00388: "PBPKO"
    """gestational week: A physiological parameter representing the specific week of gestation."""

    GESTATIONAL_WEEK: "PBPKO"
    """gestational week: A physiological parameter representing the specific week of gestation."""

    PBPKO_00389: "PBPKO"
    """maximum rate in fetus: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in fetus when the enzyme is saturated with substrate."""

    MAXIMUM_RATE_IN_FETUS: "PBPKO"
    """maximum rate in fetus: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in fetus when the enzyme is saturated with substrate."""

    PBPKO_00390: "PBPKO"
    """amniotic transfer coefficient: A biochemical parameter representing the rate at which a compound transfers from maternal circulation to amniotic fluid."""

    AMNIOTIC_TRANSFER_COEFFICIENT: "PBPKO"
    """amniotic transfer coefficient: A biochemical parameter representing the rate at which a compound transfers from maternal circulation to amniotic fluid."""

    PBPKO_00391: "PBPKO"
    """liverfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal liver to plasma."""

    LIVERFETUS_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """liverfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal liver to plasma."""

    PBPKO_00392: "PBPKO"
    """brainfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal brain to plasma."""

    BRAINFETUS_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """brainfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal brain to plasma."""

    PBPKO_00393: "PBPKO"
    """kidneyfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal kidney to plasma."""

    KIDNEYFETUS_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """kidneyfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal kidney to plasma."""

    PBPKO_00394: "PBPKO"
    """restbodyfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to plasma."""

    RESTBODYFETUS_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """restbodyfetus plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to plasma."""

    PBPKO_00395: "PBPKO"
    """kidney pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the kidney compartments."""

    KIDNEY_PBPK: "PBPKO"
    """kidney pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the kidney compartments."""

    PBPKO_00396: "PBPKO"
    """Bowman's capsule compartment: A kidney compartment representing the Bowman's capsule."""

    BOWMAN_S_CAPSULE_COMPARTMENT: "PBPKO"
    """Bowman's capsule compartment: A kidney compartment representing the Bowman's capsule."""

    PBPKO_00397: "PBPKO"
    """filtrate compartment: A kidney compartment representing the filtrate within the nephron."""

    FILTRATE_COMPARTMENT: "PBPKO"
    """filtrate compartment: A kidney compartment representing the filtrate within the nephron."""

    PBPKO_00398: "PBPKO"
    """proximal tubule compartment: A kidney compartment representing the proximal tubule of the nephron."""

    PROXIMAL_TUBULE_COMPARTMENT: "PBPKO"
    """proximal tubule compartment: A kidney compartment representing the proximal tubule of the nephron."""

    PBPKO_00399: "PBPKO"
    """loop of Henle compartment: A kidney compartment representing the loop of Henle within the nephron."""

    LOOP_OF_HENLE_COMPARTMENT: "PBPKO"
    """loop of Henle compartment: A kidney compartment representing the loop of Henle within the nephron."""

    PBPKO_00400: "PBPKO"
    """distal tubule compartment: A kidney compartment representing the distal tubule of the nephron."""

    DISTAL_TUBULE_COMPARTMENT: "PBPKO"
    """distal tubule compartment: A kidney compartment representing the distal tubule of the nephron."""

    PBPKO_00401: "PBPKO"
    """collecting duct compartment: A kidney compartment representing the collecting duct system."""

    COLLECTING_DUCT_COMPARTMENT: "PBPKO"
    """collecting duct compartment: A kidney compartment representing the collecting duct system."""

    PBPKO_00402: "PBPKO"
    """bladder compartment: A compartment representing the urinary bladder."""

    BLADDER_COMPARTMENT: "PBPKO"
    """bladder compartment: A compartment representing the urinary bladder."""

    PBPKO_00403: "PBPKO"
    """lung pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the lung compartments."""

    LUNG_PBPK: "PBPKO"
    """lung pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the lung compartments."""

    PBPKO_00404: "PBPKO"
    """extrathoracic compartment: A compartment representing the extrathoracic region (head, neck, upper respiratory tract)."""

    EXTRATHORACIC_COMPARTMENT: "PBPKO"
    """extrathoracic compartment: A compartment representing the extrathoracic region (head, neck, upper respiratory tract)."""

    PBPKO_00405: "PBPKO"
    """thoracic compartment: A compartment representing the thoracic region (chest)."""

    THORACIC_COMPARTMENT: "PBPKO"
    """thoracic compartment: A compartment representing the thoracic region (chest)."""

    PBPKO_00406: "PBPKO"
    """bronchiolar compartment: A lung compartment representing the bronchioles."""

    BRONCHIOLAR_COMPARTMENT: "PBPKO"
    """bronchiolar compartment: A lung compartment representing the bronchioles."""

    PBPKO_00407: "PBPKO"
    """alveolar compartment: A lung compartment representing the alveoli."""

    ALVEOLAR_COMPARTMENT: "PBPKO"
    """alveolar compartment: A lung compartment representing the alveoli."""

    PBPKO_00408: "PBPKO"
    """gut pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the gut compartments."""

    GUT_PBPK: "PBPKO"
    """gut pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the gut compartments."""

    PBPKO_00409: "PBPKO"
    """fraction of blood flow to duodenum: The dimensionless fraction of cardiac output delivered to the duodenum compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_DUODENUM: "PBPKO"
    """fraction of blood flow to duodenum: The dimensionless fraction of cardiac output delivered to the duodenum compartment."""

    PBPKO_00410: "PBPKO"
    """fraction of blood flow to jejunum: The dimensionless fraction of cardiac output delivered to the jejunum compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_JEJUNUM: "PBPKO"
    """fraction of blood flow to jejunum: The dimensionless fraction of cardiac output delivered to the jejunum compartment."""

    PBPKO_00411: "PBPKO"
    """fraction of blood flow to ileum: The dimensionless fraction of cardiac output delivered to the ileum compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_ILEUM: "PBPKO"
    """fraction of blood flow to ileum: The dimensionless fraction of cardiac output delivered to the ileum compartment."""

    PBPKO_00412: "PBPKO"
    """fraction of blood flow to colon: The dimensionless fraction of cardiac output delivered to the colon compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_COLON: "PBPKO"
    """fraction of blood flow to colon: The dimensionless fraction of cardiac output delivered to the colon compartment."""

    PBPKO_00413: "PBPKO"
    """fraction of blood flow to cecum: The dimensionless fraction of cardiac output delivered to the cecum compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_CECUM: "PBPKO"
    """fraction of blood flow to cecum: The dimensionless fraction of cardiac output delivered to the cecum compartment."""

    PBPKO_00414: "PBPKO"
    """blood flow rate to duodenum: A blood flow rate parameter specifically describing the rate to the duodenum compartment."""

    BLOOD_FLOW_RATE_TO_DUODENUM: "PBPKO"
    """blood flow rate to duodenum: A blood flow rate parameter specifically describing the rate to the duodenum compartment."""

    PBPKO_00415: "PBPKO"
    """blood flow rate to jejunum: A blood flow rate parameter specifically describing the rate to the jejunum compartment."""

    BLOOD_FLOW_RATE_TO_JEJUNUM: "PBPKO"
    """blood flow rate to jejunum: A blood flow rate parameter specifically describing the rate to the jejunum compartment."""

    PBPKO_00416: "PBPKO"
    """blood flow rate to ileum: A blood flow rate parameter specifically describing the rate to the ileum compartment."""

    BLOOD_FLOW_RATE_TO_ILEUM: "PBPKO"
    """blood flow rate to ileum: A blood flow rate parameter specifically describing the rate to the ileum compartment."""

    PBPKO_00417: "PBPKO"
    """blood flow rate to colon: A blood flow rate parameter specifically describing the rate to the colon compartment."""

    BLOOD_FLOW_RATE_TO_COLON: "PBPKO"
    """blood flow rate to colon: A blood flow rate parameter specifically describing the rate to the colon compartment."""

    PBPKO_00418: "PBPKO"
    """blood flow rate to cecum: A blood flow rate parameter specifically describing the rate to the cecum compartment."""

    BLOOD_FLOW_RATE_TO_CECUM: "PBPKO"
    """blood flow rate to cecum: A blood flow rate parameter specifically describing the rate to the cecum compartment."""

    PBPKO_00419: "PBPKO"
    """fraction of duodenum: A dimensionless fraction of volume defined as the duodenum volume divided per unit of total body weight."""

    FRACTION_OF_DUODENUM: "PBPKO"
    """fraction of duodenum: A dimensionless fraction of volume defined as the duodenum volume divided per unit of total body weight."""

    PBPKO_00420: "PBPKO"
    """fraction of jejunum: A dimensionless fraction of volume defined as the jejunum volume divided per unit of total body weight."""

    FRACTION_OF_JEJUNUM: "PBPKO"
    """fraction of jejunum: A dimensionless fraction of volume defined as the jejunum volume divided per unit of total body weight."""

    PBPKO_00421: "PBPKO"
    """fraction of ileum: A dimensionless fraction of volume defined as the ileum volume divided per unit of total body weight."""

    FRACTION_OF_ILEUM: "PBPKO"
    """fraction of ileum: A dimensionless fraction of volume defined as the ileum volume divided per unit of total body weight."""

    PBPKO_00422: "PBPKO"
    """fraction of colon: A dimensionless fraction of volume defined as the colon volume divided per unit of total body weight."""

    FRACTION_OF_COLON: "PBPKO"
    """fraction of colon: A dimensionless fraction of volume defined as the colon volume divided per unit of total body weight."""

    PBPKO_00423: "PBPKO"
    """fraction of cecum: A dimensionless fraction of volume defined as the cecum volume divided per unit of total body weight."""

    FRACTION_OF_CECUM: "PBPKO"
    """fraction of cecum: A dimensionless fraction of volume defined as the cecum volume divided per unit of total body weight."""

    PBPKO_00424: "PBPKO"
    """volume of duodenum: A volume parameter representing the total volume of the duodenum compartment."""

    VOLUME_OF_DUODENUM: "PBPKO"
    """volume of duodenum: A volume parameter representing the total volume of the duodenum compartment."""

    PBPKO_00425: "PBPKO"
    """volume of jejunum: A volume parameter representing the total volume of the jejunum compartment."""

    VOLUME_OF_JEJUNUM: "PBPKO"
    """volume of jejunum: A volume parameter representing the total volume of the jejunum compartment."""

    PBPKO_00426: "PBPKO"
    """volume of ileum: A volume parameter representing the total volume of the ileum compartment."""

    VOLUME_OF_ILEUM: "PBPKO"
    """volume of ileum: A volume parameter representing the total volume of the ileum compartment."""

    PBPKO_00427: "PBPKO"
    """volume of colon: A volume parameter representing the total volume of the colon compartment."""

    VOLUME_OF_COLON: "PBPKO"
    """volume of colon: A volume parameter representing the total volume of the colon compartment."""

    PBPKO_00428: "PBPKO"
    """volume of cecum: A volume parameter representing the total volume of the cecum compartment."""

    VOLUME_OF_CECUM: "PBPKO"
    """volume of cecum: A volume parameter representing the total volume of the cecum compartment."""

    PBPKO_00429: "PBPKO"
    """bile salt effect solubilization ratio: A biochemical parameter representing the ratio of molecules solubilized due to bile salt presence."""

    BILE_SALT_EFFECT_SOLUBILIZATION_RATIO: "PBPKO"
    """bile salt effect solubilization ratio: A biochemical parameter representing the ratio of molecules solubilized due to bile salt presence."""

    PBPKO_00430: "PBPKO"
    """mean precipitation time: A biochemical parameter representing the average time for a compound to precipitate under specific conditions (e.g., in the GI tract)."""

    MEAN_PRECIPITATION_TIME: "PBPKO"
    """mean precipitation time: A biochemical parameter representing the average time for a compound to precipitate under specific conditions (e.g., in the GI tract)."""

    PBPKO_00431: "PBPKO"
    """diffusion coefficient: A physicochemical parameter representing the amount of substance diffusing across a unit area per unit time under a unit concentration gradient."""

    DIFFUSION_COEFFICIENT: "PBPKO"
    """diffusion coefficient: A physicochemical parameter representing the amount of substance diffusing across a unit area per unit time under a unit concentration gradient."""

    PBPKO_00432: "PBPKO"
    """particle density: A biochemical/physical parameter representing the mass per unit volume of particles (e.g., of the administered compound)."""

    PARTICLE_DENSITY: "PBPKO"
    """particle density: A biochemical/physical parameter representing the mass per unit volume of particles (e.g., of the administered compound)."""

    PBPKO_00433: "PBPKO"
    """particle radius: A biochemical/physical parameter representing the radius of particles (e.g., of the administered compound)."""

    PARTICLE_RADIUS: "PBPKO"
    """particle radius: A biochemical/physical parameter representing the radius of particles (e.g., of the administered compound)."""

    PBPKO_00434: "PBPKO"
    """intestinal transit time: A biochemical parameter representing the time required for a compound to move through the intestine."""

    INTESTINAL_TRANSIT_TIME: "PBPKO"
    """intestinal transit time: A biochemical parameter representing the time required for a compound to move through the intestine."""

    PBPKO_00435: "PBPKO"
    """lactational pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations during lactation, including transfer into milk."""

    LACTATIONAL_PBPK: "PBPKO"
    """lactational pbpk: A physiologically based pharmacokinetic model specifically built to predict compound concentrations during lactation, including transfer into milk."""

    PBPKO_00436: "PBPKO"
    """milk plasma ratio: A biochemical parameter representing the ratio of compound concentration in milk to plasma."""

    MILK_PLASMA_RATIO: "PBPKO"
    """milk plasma ratio: A biochemical parameter representing the ratio of compound concentration in milk to plasma."""

    PBPKO_00437: "PBPKO"
    """fraction unbound milk: An unbound fraction parameter specifically for milk."""

    FRACTION_UNBOUND_MILK: "PBPKO"
    """fraction unbound milk: An unbound fraction parameter specifically for milk."""

    PBPKO_00438: "PBPKO"
    """concentration in milk: The total concentration of compound in the milk compartment."""

    CONCENTRATION_IN_MILK: "PBPKO"
    """concentration in milk: The total concentration of compound in the milk compartment."""

    PBPKO_00439: "PBPKO"
    """daily milk intake: A physiological parameter representing the daily volume of milk ingested (e.g., by an infant)."""

    DAILY_MILK_INTAKE: "PBPKO"
    """daily milk intake: A physiological parameter representing the daily volume of milk ingested (e.g., by an infant)."""

    PBPKO_00440: "PBPKO"
    """phmilk: A biochemical parameter representing the pH of milk."""

    PHMILK: "PBPKO"
    """phmilk: A biochemical parameter representing the pH of milk."""

    PBPKO_00441: "PBPKO"
    """blood milk barrier compartment: A barrier compartment representing the physiological barrier separating blood and milk in lactating species."""

    BLOOD_MILK_BARRIER_COMPARTMENT: "PBPKO"
    """blood milk barrier compartment: A barrier compartment representing the physiological barrier separating blood and milk in lactating species."""

    PBPKO_00442: "PBPKO"
    """milk plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in milk to plasma."""

    MILK_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """milk plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in milk to plasma."""

    PBPKO_00446: "PBPKO"
    """compartment: A data representation model component representing a distinct physiological space (organ, tissue, fluid) where ADME processes occur."""

    COMPARTMENT: "PBPKO"
    """compartment: A data representation model component representing a distinct physiological space (organ, tissue, fluid) where ADME processes occur."""

    PBPKO_00448: "PBPKO"
    """alveolar air compartment: A lung compartment specifically representing the air within the alveoli."""

    ALVEOLAR_AIR_COMPARTMENT: "PBPKO"
    """alveolar air compartment: A lung compartment specifically representing the air within the alveoli."""

    PBPKO_00450: "PBPKO"
    """rest of body compartment: A compartment representing the lumped remainder of the body not explicitly modeled as separate organs/tissues."""

    REST_OF_BODY_COMPARTMENT: "PBPKO"
    """rest of body compartment: A compartment representing the lumped remainder of the body not explicitly modeled as separate organs/tissues."""

    PBPKO_00451: "PBPKO"
    """arterial plasma: A compartment representing the plasma specifically within the arterial blood."""

    ARTERIAL_PLASMA: "PBPKO"
    """arterial plasma: A compartment representing the plasma specifically within the arterial blood."""

    PBPKO_00452: "PBPKO"
    """venous plasma compartment: A compartment representing the plasma specifically within the venous blood."""

    VENOUS_PLASMA_COMPARTMENT: "PBPKO"
    """venous plasma compartment: A compartment representing the plasma specifically within the venous blood."""

    PBPKO_00453: "PBPKO"
    """richly perfused tissue compartment: A compartment representing lumped tissues with high blood flow relative to their volume."""

    RICHLY_PERFUSED_TISSUE_COMPARTMENT: "PBPKO"
    """richly perfused tissue compartment: A compartment representing lumped tissues with high blood flow relative to their volume."""

    PBPKO_00454: "PBPKO"
    """poorly perfused tissue compartment: A compartment representing lumped tissues with low blood flow relative to their volume."""

    POORLY_PERFUSED_TISSUE_COMPARTMENT: "PBPKO"
    """poorly perfused tissue compartment: A compartment representing lumped tissues with low blood flow relative to their volume."""

    PBPKO_00455: "PBPKO"
    """viable unexposed skin compartment: A skin compartment representing the viable layers of skin not directly exposed to the applied compound."""

    VIABLE_UNEXPOSED_SKIN_COMPARTMENT: "PBPKO"
    """viable unexposed skin compartment: A skin compartment representing the viable layers of skin not directly exposed to the applied compound."""

    PBPKO_00456: "PBPKO"
    """viable exposed skin compartment: A skin compartment representing the viable layers of skin directly exposed to the applied compound."""

    VIABLE_EXPOSED_SKIN_COMPARTMENT: "PBPKO"
    """viable exposed skin compartment: A skin compartment representing the viable layers of skin directly exposed to the applied compound."""

    PBPKO_00457: "PBPKO"
    """skin unexposed stratum corneum: A stratum corneum compartment representing the portion not directly exposed to the applied compound."""

    SKIN_UNEXPOSED_STRATUM_CORNEUM: "PBPKO"
    """skin unexposed stratum corneum: A stratum corneum compartment representing the portion not directly exposed to the applied compound."""

    PBPKO_00458: "PBPKO"
    """skin exposed stratum corneum compartment: A stratum corneum compartment representing the portion directly exposed to the applied compound."""

    SKIN_EXPOSED_STRATUM_CORNEUM_COMPARTMENT: "PBPKO"
    """skin exposed stratum corneum compartment: A stratum corneum compartment representing the portion directly exposed to the applied compound."""

    PBPKO_00460: "PBPKO"
    """adipose compartment: A compartment representing adipose (fat) tissue."""

    ADIPOSE_COMPARTMENT: "PBPKO"
    """adipose compartment: A compartment representing adipose (fat) tissue."""

    PBPKO_00461: "PBPKO"
    """anal canal compartment: A large intestine compartment representing the anal canal."""

    ANAL_CANAL_COMPARTMENT: "PBPKO"
    """anal canal compartment: A large intestine compartment representing the anal canal."""

    PBPKO_00462: "PBPKO"
    """appendix compartment: A large intestine compartment representing the appendix."""

    APPENDIX_COMPARTMENT: "PBPKO"
    """appendix compartment: A large intestine compartment representing the appendix."""

    PBPKO_00463: "PBPKO"
    """ascending colon compartment: A large intestine compartment representing the ascending colon."""

    ASCENDING_COLON_COMPARTMENT: "PBPKO"
    """ascending colon compartment: A large intestine compartment representing the ascending colon."""

    PBPKO_00464: "PBPKO"
    """blood compartment: A compartment representing the entirety of the blood (including plasma and cells)."""

    BLOOD_COMPARTMENT: "PBPKO"
    """blood compartment: A compartment representing the entirety of the blood (including plasma and cells)."""

    PBPKO_00465: "PBPKO"
    """bone marrow compartment: A compartment representing the bone marrow."""

    BONE_MARROW_COMPARTMENT: "PBPKO"
    """bone marrow compartment: A compartment representing the bone marrow."""

    PBPKO_00466: "PBPKO"
    """brain compartment: A compartment representing the brain."""

    BRAIN_COMPARTMENT: "PBPKO"
    """brain compartment: A compartment representing the brain."""

    PBPKO_00467: "PBPKO"
    """cecum compartment: A large intestine compartment representing the cecum."""

    CECUM_COMPARTMENT: "PBPKO"
    """cecum compartment: A large intestine compartment representing the cecum."""

    PBPKO_00468: "PBPKO"
    """descending colon compartment: A large intestine compartment representing the descending colon."""

    DESCENDING_COLON_COMPARTMENT: "PBPKO"
    """descending colon compartment: A large intestine compartment representing the descending colon."""

    PBPKO_00469: "PBPKO"
    """dermis compartment: A skin compartment representing the dermis layer."""

    DERMIS_COMPARTMENT: "PBPKO"
    """dermis compartment: A skin compartment representing the dermis layer."""

    PBPKO_00470: "PBPKO"
    """skin compartment: A compartment representing the skin."""

    SKIN_COMPARTMENT: "PBPKO"
    """skin compartment: A compartment representing the skin."""

    PBPKO_00471: "PBPKO"
    """duodenum compartment: A small intestine compartment representing the duodenum."""

    DUODENUM_COMPARTMENT: "PBPKO"
    """duodenum compartment: A small intestine compartment representing the duodenum."""

    PBPKO_00472: "PBPKO"
    """small intestine compartment: A digestive system compartment representing the small intestine."""

    SMALL_INTESTINE_COMPARTMENT: "PBPKO"
    """small intestine compartment: A digestive system compartment representing the small intestine."""

    PBPKO_00473: "PBPKO"
    """endocrine gland compartment: A compartment representing endocrine glands."""

    ENDOCRINE_GLAND_COMPARTMENT: "PBPKO"
    """endocrine gland compartment: A compartment representing endocrine glands."""

    PBPKO_00474: "PBPKO"
    """large intestine compartment: A digestive system compartment representing the large intestine."""

    LARGE_INTESTINE_COMPARTMENT: "PBPKO"
    """large intestine compartment: A digestive system compartment representing the large intestine."""

    PBPKO_00475: "PBPKO"
    """epidermis compartment: A skin compartment representing the epidermis layer."""

    EPIDERMIS_COMPARTMENT: "PBPKO"
    """epidermis compartment: A skin compartment representing the epidermis layer."""

    PBPKO_00476: "PBPKO"
    """gall bladder compartment: A digestive system compartment representing the gall bladder."""

    GALL_BLADDER_COMPARTMENT: "PBPKO"
    """gall bladder compartment: A digestive system compartment representing the gall bladder."""

    PBPKO_00477: "PBPKO"
    """gut compartment: A digestive system compartment representing the gut (general term, often synonymous with intestine or GI tract)."""

    GUT_COMPARTMENT: "PBPKO"
    """gut compartment: A digestive system compartment representing the gut (general term, often synonymous with intestine or GI tract)."""

    PBPKO_00478: "PBPKO"
    """gut lumen compartment: A digestive system compartment representing the lumen (opening) within the gut."""

    GUT_LUMEN_COMPARTMENT: "PBPKO"
    """gut lumen compartment: A digestive system compartment representing the lumen (opening) within the gut."""

    PBPKO_00479: "PBPKO"
    """hair compartment: A compartment representing hair."""

    HAIR_COMPARTMENT: "PBPKO"
    """hair compartment: A compartment representing hair."""

    PBPKO_00480: "PBPKO"
    """heart compartment: A compartment representing the heart."""

    HEART_COMPARTMENT: "PBPKO"
    """heart compartment: A compartment representing the heart."""

    PBPKO_00481: "PBPKO"
    """ileum compartment: A small intestine compartment representing the ileum."""

    ILEUM_COMPARTMENT: "PBPKO"
    """ileum compartment: A small intestine compartment representing the ileum."""

    PBPKO_00482: "PBPKO"
    """jejunum compartment: A small intestine compartment representing the jejunum."""

    JEJUNUM_COMPARTMENT: "PBPKO"
    """jejunum compartment: A small intestine compartment representing the jejunum."""

    PBPKO_00483: "PBPKO"
    """mammary gland compartment: A compartment representing the mammary gland."""

    MAMMARY_GLAND_COMPARTMENT: "PBPKO"
    """mammary gland compartment: A compartment representing the mammary gland."""

    PBPKO_00484: "PBPKO"
    """muscle compartment: A compartment representing muscle tissue."""

    MUSCLE_COMPARTMENT: "PBPKO"
    """muscle compartment: A compartment representing muscle tissue."""

    PBPKO_00485: "PBPKO"
    """nail compartment: A compartment representing nails."""

    NAIL_COMPARTMENT: "PBPKO"
    """nail compartment: A compartment representing nails."""

    PBPKO_00486: "PBPKO"
    """pancreas compartment: A compartment representing the pancreas."""

    PANCREAS_COMPARTMENT: "PBPKO"
    """pancreas compartment: A compartment representing the pancreas."""

    PBPKO_00487: "PBPKO"
    """placental barrier compartment: A barrier compartment representing the placental barrier separating maternal and fetal circulation."""

    PLACENTAL_BARRIER_COMPARTMENT: "PBPKO"
    """placental barrier compartment: A barrier compartment representing the placental barrier separating maternal and fetal circulation."""

    PBPKO_00488: "PBPKO"
    """plasma compartment: A compartment representing blood plasma."""

    PLASMA_COMPARTMENT: "PBPKO"
    """plasma compartment: A compartment representing blood plasma."""

    PBPKO_00489: "PBPKO"
    """rectum compartment: A large intestine compartment representing the rectum."""

    RECTUM_COMPARTMENT: "PBPKO"
    """rectum compartment: A large intestine compartment representing the rectum."""

    PBPKO_00490: "PBPKO"
    """reproductive compartment: A compartment representing reproductive organs (gonads)."""

    REPRODUCTIVE_COMPARTMENT: "PBPKO"
    """reproductive compartment: A compartment representing reproductive organs (gonads)."""

    PBPKO_00491: "PBPKO"
    """sigmoid colon compartment: A large intestine compartment representing the sigmoid colon."""

    SIGMOID_COLON_COMPARTMENT: "PBPKO"
    """sigmoid colon compartment: A large intestine compartment representing the sigmoid colon."""

    PBPKO_00492: "PBPKO"
    """spleen compartment: A compartment representing the spleen."""

    SPLEEN_COMPARTMENT: "PBPKO"
    """spleen compartment: A compartment representing the spleen."""

    PBPKO_00493: "PBPKO"
    """stratum corneum compartment: A skin compartment representing the stratum corneum layer."""

    STRATUM_CORNEUM_COMPARTMENT: "PBPKO"
    """stratum corneum compartment: A skin compartment representing the stratum corneum layer."""

    PBPKO_00494: "PBPKO"
    """transverse colon compartment: A large intestine compartment representing the transverse colon."""

    TRANSVERSE_COLON_COMPARTMENT: "PBPKO"
    """transverse colon compartment: A large intestine compartment representing the transverse colon."""

    PBPKO_00495: "PBPKO"
    """barrier compartment: A compartment representing a physiological barrier limiting compound movement."""

    BARRIER_COMPARTMENT: "PBPKO"
    """barrier compartment: A compartment representing a physiological barrier limiting compound movement."""

    PBPKO_00496: "PBPKO"
    """amount in gut: The amount of compound in the gut compartment."""

    AMOUNT_IN_GUT: "PBPKO"
    """amount in gut: The amount of compound in the gut compartment."""

    PBPKO_00497: "PBPKO"
    """amount in liver: The amount of compound in the liver compartment."""

    AMOUNT_IN_LIVER: "PBPKO"
    """amount in liver: The amount of compound in the liver compartment."""

    PBPKO_00498: "PBPKO"
    """amount in kidney: The amount of compound in the kidney compartment."""

    AMOUNT_IN_KIDNEY: "PBPKO"
    """amount in kidney: The amount of compound in the kidney compartment."""

    PBPKO_00499: "PBPKO"
    """amount in filtrate: The amount of compound in the filtrate compartment."""

    AMOUNT_IN_FILTRATE: "PBPKO"
    """amount in filtrate: The amount of compound in the filtrate compartment."""

    PBPKO_00500: "PBPKO"
    """amount in delay: The amount of compound in the hypothetical delay compartment."""

    AMOUNT_IN_DELAY: "PBPKO"
    """amount in delay: The amount of compound in the hypothetical delay compartment."""

    PBPKO_00501: "PBPKO"
    """amount in restbody: The amount of compound in the rest of the body compartment."""

    AMOUNT_IN_RESTBODY: "PBPKO"
    """amount in restbody: The amount of compound in the rest of the body compartment."""

    PBPKO_00502: "PBPKO"
    """amount in plasma: The amount of compound in the plasma compartment."""

    AMOUNT_IN_PLASMA: "PBPKO"
    """amount in plasma: The amount of compound in the plasma compartment."""

    PBPKO_00503: "PBPKO"
    """amount in brain: The amount of compound in the brain compartment."""

    AMOUNT_IN_BRAIN: "PBPKO"
    """amount in brain: The amount of compound in the brain compartment."""

    PBPKO_00504: "PBPKO"
    """amount in lung: The amount of compound in the lung compartment."""

    AMOUNT_IN_LUNG: "PBPKO"
    """amount in lung: The amount of compound in the lung compartment."""

    PBPKO_00505: "PBPKO"
    """amount in bone marrow: The amount of compound in the bone marrow compartment."""

    AMOUNT_IN_BONE_MARROW: "PBPKO"
    """amount in bone marrow: The amount of compound in the bone marrow compartment."""

    PBPKO_00506: "PBPKO"
    """amount in skin: The amount of compound in the skin compartment."""

    AMOUNT_IN_SKIN: "PBPKO"
    """amount in skin: The amount of compound in the skin compartment."""

    PBPKO_00507: "PBPKO"
    """amount in mammary gland: The amount of compound in the mammary gland compartment."""

    AMOUNT_IN_MAMMARY_GLAND: "PBPKO"
    """amount in mammary gland: The amount of compound in the mammary gland compartment."""

    PBPKO_00508: "PBPKO"
    """fraction of filtrate: A dimensionless fraction of volume defined as the filtrate volume divided per unit of total body weight."""

    FRACTION_OF_FILTRATE: "PBPKO"
    """fraction of filtrate: A dimensionless fraction of volume defined as the filtrate volume divided per unit of total body weight."""

    PBPKO_00509: "PBPKO"
    """fraction of gut: A dimensionless fraction of volume defined as the gut volume divided per unit of total body weight."""

    FRACTION_OF_GUT: "PBPKO"
    """fraction of gut: A dimensionless fraction of volume defined as the gut volume divided per unit of total body weight."""

    PBPKO_00510: "PBPKO"
    """fraction of mammary gland: A dimensionless fraction of volume defined as the mammary gland volume divided per unit of total body weight."""

    FRACTION_OF_MAMMARY_GLAND: "PBPKO"
    """fraction of mammary gland: A dimensionless fraction of volume defined as the mammary gland volume divided per unit of total body weight."""

    PBPKO_00511: "PBPKO"
    """fraction of blood flow to filtrate: The dimensionless fraction of cardiac output delivered to the filtrate compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_FILTRATE: "PBPKO"
    """fraction of blood flow to filtrate: The dimensionless fraction of cardiac output delivered to the filtrate compartment."""

    PBPKO_00512: "PBPKO"
    """fraction of blood flow to bone marrow: The dimensionless fraction of cardiac output delivered to the bone marrow compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_BONE_MARROW: "PBPKO"
    """fraction of blood flow to bone marrow: The dimensionless fraction of cardiac output delivered to the bone marrow compartment."""

    PBPKO_00513: "PBPKO"
    """fraction of blood flow to gut: The dimensionless fraction of cardiac output delivered to the gut compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_GUT: "PBPKO"
    """fraction of blood flow to gut: The dimensionless fraction of cardiac output delivered to the gut compartment."""

    PBPKO_00514: "PBPKO"
    """fraction of blood flow to mammary gland: The dimensionless fraction of cardiac output delivered to the mammary gland compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_MAMMARY_GLAND: "PBPKO"
    """fraction of blood flow to mammary gland: The dimensionless fraction of cardiac output delivered to the mammary gland compartment."""

    PBPKO_00515: "PBPKO"
    """brain plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the brain to plasma."""

    BRAIN_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """brain plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the brain to plasma."""

    PBPKO_00517: "PBPKO"
    """mammary gland plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the mammary gland to plasma."""

    MAMMARY_GLAND_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """mammary gland plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the mammary gland to plasma."""

    PBPKO_00518: "PBPKO"
    """restbody plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the rest of body compartment to plasma."""

    RESTBODY_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """restbody plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in the rest of body compartment to plasma."""

    PBPKO_00519: "PBPKO"
    """tissue plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in a generic tissue to plasma."""

    TISSUE_PLASMA_PARTITION_COEFFICIENT: "PBPKO"
    """tissue plasma partition coefficient: A partition coefficient representing the ratio of compound concentration in a generic tissue to plasma."""

    PBPKO_00520: "PBPKO"
    """urinary rate constant: A biochemical parameter (rate constant) representing the rate at which a compound is cleared via urine, often scaled by body weight."""

    URINARY_RATE_CONSTANT: "PBPKO"
    """urinary rate constant: A biochemical parameter (rate constant) representing the rate at which a compound is cleared via urine, often scaled by body weight."""

    PBPKO_00521: "PBPKO"
    """age in PBPK model: A physiological parameter representing the period of lifespan (typically in years) for which the model is simulated."""

    AGE_IN_PBPK_MODEL: "PBPKO"
    """age in PBPK model: A physiological parameter representing the period of lifespan (typically in years) for which the model is simulated."""

    PBPKO_00522: "PBPKO"
    """volume of filtrate: A volume parameter representing the total volume of the filtrate compartment."""

    VOLUME_OF_FILTRATE: "PBPKO"
    """volume of filtrate: A volume parameter representing the total volume of the filtrate compartment."""

    PBPKO_00523: "PBPKO"
    """volume of bone marrow: A volume parameter representing the total volume of the bone marrow compartment."""

    VOLUME_OF_BONE_MARROW: "PBPKO"
    """volume of bone marrow: A volume parameter representing the total volume of the bone marrow compartment."""

    PBPKO_00524: "PBPKO"
    """volume of gut: A volume parameter representing the total volume of the gut compartment."""

    VOLUME_OF_GUT: "PBPKO"
    """volume of gut: A volume parameter representing the total volume of the gut compartment."""

    PBPKO_00525: "PBPKO"
    """volume of mammary gland: A volume parameter representing the total volume of the mammary gland compartment."""

    VOLUME_OF_MAMMARY_GLAND: "PBPKO"
    """volume of mammary gland: A volume parameter representing the total volume of the mammary gland compartment."""

    PBPKO_00526: "PBPKO"
    """volume of mass balance: A volume parameter representing the check for total mass balance of all compartments (sum of organ volumes should equal body volume/weight equivalent, depending on units)."""

    VOLUME_OF_MASS_BALANCE: "PBPKO"
    """volume of mass balance: A volume parameter representing the check for total mass balance of all compartments (sum of organ volumes should equal body volume/weight equivalent, depending on units)."""

    PBPKO_00527: "PBPKO"
    """hematocrit volume: A volume parameter representing the total volume of red blood cells in whole blood."""

    HEMATOCRIT_VOLUME: "PBPKO"
    """hematocrit volume: A volume parameter representing the total volume of red blood cells in whole blood."""

    PBPKO_00528: "PBPKO"
    """cardiac output rate of plasma: A blood flow rate parameter representing the cardiac output specifically related to plasma flow."""

    CARDIAC_OUTPUT_RATE_OF_PLASMA: "PBPKO"
    """cardiac output rate of plasma: A blood flow rate parameter representing the cardiac output specifically related to plasma flow."""

    PBPKO_00529: "PBPKO"
    """blood flow rate to filtrate: A blood flow rate parameter specifically describing the rate to the filtrate compartment (representing glomerular filtration)."""

    BLOOD_FLOW_RATE_TO_FILTRATE: "PBPKO"
    """blood flow rate to filtrate: A blood flow rate parameter specifically describing the rate to the filtrate compartment (representing glomerular filtration)."""

    PBPKO_00530: "PBPKO"
    """blood flow rate to bone marrow: A blood flow parameter specifically describing the rate to the bone marrow compartment."""

    BLOOD_FLOW_RATE_TO_BONE_MARROW: "PBPKO"
    """blood flow rate to bone marrow: A blood flow parameter specifically describing the rate to the bone marrow compartment."""

    PBPKO_00531: "PBPKO"
    """blood flow rate to gut: A blood flow rate parameter specifically describing the rate to the gut compartment."""

    BLOOD_FLOW_RATE_TO_GUT: "PBPKO"
    """blood flow rate to gut: A blood flow rate parameter specifically describing the rate to the gut compartment."""

    PBPKO_00532: "PBPKO"
    """blood flow rate to mammary gland: A blood flow rate parameter specifically describing the rate to the mammary gland compartment."""

    BLOOD_FLOW_RATE_TO_MAMMARY_GLAND: "PBPKO"
    """blood flow rate to mammary gland: A blood flow rate parameter specifically describing the rate to the mammary gland compartment."""

    PBPKO_00533: "PBPKO"
    """blood flow rate for mass balance: A blood flow rate parameter representing the check for total blood flow mass balance of all the compartments (sum of organ flows should equal cardiac output)."""

    BLOOD_FLOW_RATE_FOR_MASS_BALANCE: "PBPKO"
    """blood flow rate for mass balance: A blood flow rate parameter representing the check for total blood flow mass balance of all the compartments (sum of organ flows should equal cardiac output)."""

    PBPKO_00534: "PBPKO"
    """urinary rate: A biochemical parameter representing the rate at which a compound is cleared via urine."""

    URINARY_RATE: "PBPKO"
    """urinary rate: A biochemical parameter representing the rate at which a compound is cleared via urine."""

    PBPKO_00535: "PBPKO"
    """resorption maximum: A biochemical parameter (Tm) representing the maximum rate of tubular resorption (e.g., in the kidney)."""

    RESORPTION_MAXIMUM: "PBPKO"
    """resorption maximum: A biochemical parameter (Tm) representing the maximum rate of tubular resorption (e.g., in the kidney)."""

    PBPKO_00536: "PBPKO"
    """resorption: A biochemical parameter or process representing the resorption of a compound (e.g., tubular resorption)."""

    RESORPTION: "PBPKO"
    """resorption: A biochemical parameter or process representing the resorption of a compound (e.g., tubular resorption)."""

    PBPKO_00537: "PBPKO"
    """octanol air partition coefficient: A partition coefficient (Koa) representing the ratio of compound concentration in octanol to air at equilibrium."""

    OCTANOL_AIR_PARTITION_COEFFICIENT: "PBPKO"
    """octanol air partition coefficient: A partition coefficient (Koa) representing the ratio of compound concentration in octanol to air at equilibrium."""

    PBPKO_00538: "PBPKO"
    """concentration in gut: The total concentration of compound in the gut compartment."""

    CONCENTRATION_IN_GUT: "PBPKO"
    """concentration in gut: The total concentration of compound in the gut compartment."""

    PBPKO_00539: "PBPKO"
    """concentration in liver: The total concentration of compound in the liver compartment."""

    CONCENTRATION_IN_LIVER: "PBPKO"
    """concentration in liver: The total concentration of compound in the liver compartment."""

    PBPKO_00540: "PBPKO"
    """concentration in brain: The total concentration of compound in the brain compartment."""

    CONCENTRATION_IN_BRAIN: "PBPKO"
    """concentration in brain: The total concentration of compound in the brain compartment."""

    PBPKO_00541: "PBPKO"
    """concentration in kidney: The total concentration of compound in the kidney compartment."""

    CONCENTRATION_IN_KIDNEY: "PBPKO"
    """concentration in kidney: The total concentration of compound in the kidney compartment."""

    PBPKO_00542: "PBPKO"
    """concentration in filtrate: The total concentration of compound in the filtrate compartment."""

    CONCENTRATION_IN_FILTRATE: "PBPKO"
    """concentration in filtrate: The total concentration of compound in the filtrate compartment."""

    PBPKO_00543: "PBPKO"
    """concentration in lung: The total concentration of compound in the lung compartment."""

    CONCENTRATION_IN_LUNG: "PBPKO"
    """concentration in lung: The total concentration of compound in the lung compartment."""

    PBPKO_00544: "PBPKO"
    """concentration in fat: The total concentration of compound in the fat compartment."""

    CONCENTRATION_IN_FAT: "PBPKO"
    """concentration in fat: The total concentration of compound in the fat compartment."""

    PBPKO_00545: "PBPKO"
    """concentration in bone marrow: The total concentration of compound in the bone marrow compartment."""

    CONCENTRATION_IN_BONE_MARROW: "PBPKO"
    """concentration in bone marrow: The total concentration of compound in the bone marrow compartment."""

    PBPKO_00546: "PBPKO"
    """concentration in skin: The total concentration of compound in the skin compartment."""

    CONCENTRATION_IN_SKIN: "PBPKO"
    """concentration in skin: The total concentration of compound in the skin compartment."""

    PBPKO_00547: "PBPKO"
    """concentration in mammary gland: The total concentration of compound in the mammary gland compartment."""

    CONCENTRATION_IN_MAMMARY_GLAND: "PBPKO"
    """concentration in mammary gland: The total concentration of compound in the mammary gland compartment."""

    PBPKO_00548: "PBPKO"
    """concentration in restbody: The total concentration of compound in the rest of body compartment."""

    CONCENTRATION_IN_RESTBODY: "PBPKO"
    """concentration in restbody: The total concentration of compound in the rest of body compartment."""

    PBPKO_00549: "PBPKO"
    """concentration in plasma: The total concentration of compound in the plasma compartment."""

    CONCENTRATION_IN_PLASMA: "PBPKO"
    """concentration in plasma: The total concentration of compound in the plasma compartment."""

    PBPKO_00550: "PBPKO"
    """amount in fat: The amount of compound in the fat compartment."""

    AMOUNT_IN_FAT: "PBPKO"
    """amount in fat: The amount of compound in the fat compartment."""

    PBPKO_00551: "PBPKO"
    """PBPK model simulation time: A parameter representing the time duration over which the model simulation runs."""

    PBPK_MODEL_SIMULATION_TIME: "PBPKO"
    """PBPK model simulation time: A parameter representing the time duration over which the model simulation runs."""

    PBPKO_00552: "PBPKO"
    """arterial blood compartment: A compartment representing the arterial blood."""

    ARTERIAL_BLOOD_COMPARTMENT: "PBPKO"
    """arterial blood compartment: A compartment representing the arterial blood."""

    PBPKO_00553: "PBPKO"
    """digestive system compartment: A compartment representing the digestive system or parts thereof."""

    DIGESTIVE_SYSTEM_COMPARTMENT: "PBPKO"
    """digestive system compartment: A compartment representing the digestive system or parts thereof."""

    PBPKO_00554: "PBPKO"
    """excreta compartment: A compartment representing material eliminated from the body (e.g., urine, feces)."""

    EXCRETA_COMPARTMENT: "PBPKO"
    """excreta compartment: A compartment representing material eliminated from the body (e.g., urine, feces)."""

    PBPKO_00555: "PBPKO"
    """feces compartment: An excreta compartment specifically representing feces."""

    FECES_COMPARTMENT: "PBPKO"
    """feces compartment: An excreta compartment specifically representing feces."""

    PBPKO_00556: "PBPKO"
    """urine compartment: An excreta compartment specifically representing urine."""

    URINE_COMPARTMENT: "PBPKO"
    """urine compartment: An excreta compartment specifically representing urine."""

    PBPKO_00557: "PBPKO"
    """kidney compartment: A compartment representing the kidney(s)."""

    KIDNEY_COMPARTMENT: "PBPKO"
    """kidney compartment: A compartment representing the kidney(s)."""

    PBPKO_00558: "PBPKO"
    """liver compartment: A compartment representing the liver."""

    LIVER_COMPARTMENT: "PBPKO"
    """liver compartment: A compartment representing the liver."""

    PBPKO_00559: "PBPKO"
    """lung compartment: A compartment representing the lung(s)."""

    LUNG_COMPARTMENT: "PBPKO"
    """lung compartment: A compartment representing the lung(s)."""

    PBPKO_00561: "PBPKO"
    """venous blood compartment: A compartment representing the venous blood."""

    VENOUS_BLOOD_COMPARTMENT: "PBPKO"
    """venous blood compartment: A compartment representing the venous blood."""

    PBPKO_00562: "PBPKO"
    """blood flow rate to unexposed skin: A blood flow rate to skin parameter specifically describing the rate to the unexposed portion of the skin compartment."""

    BLOOD_FLOW_RATE_TO_UNEXPOSED_SKIN: "PBPKO"
    """blood flow rate to unexposed skin: A blood flow rate to skin parameter specifically describing the rate to the unexposed portion of the skin compartment."""

    PBPKO_00563: "PBPKO"
    """blood flow rate to exposed skin: A blood flow rate to skin parameter specifically describing the rate to the exposed portion of the skin compartment."""

    BLOOD_FLOW_RATE_TO_EXPOSED_SKIN: "PBPKO"
    """blood flow rate to exposed skin: A blood flow rate to skin parameter specifically describing the rate to the exposed portion of the skin compartment."""

    PBPKO_00564: "PBPKO"
    """blood flow rate to skin stratum corneum unexposed: A blood flow rate to skin parameter specifically describing the rate to the unexposed stratum corneum compartment."""

    BLOOD_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_UNEXPOSED: "PBPKO"
    """blood flow rate to skin stratum corneum unexposed: A blood flow rate to skin parameter specifically describing the rate to the unexposed stratum corneum compartment."""

    PBPKO_00565: "PBPKO"
    """blood flow rate to skin stratum corneum exposed: A blood flow rate to skin parameter specifically describing the rate to the exposed stratum corneum compartment."""

    BLOOD_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_EXPOSED: "PBPKO"
    """blood flow rate to skin stratum corneum exposed: A blood flow rate to skin parameter specifically describing the rate to the exposed stratum corneum compartment."""

    PBPKO_00566: "PBPKO"
    """stomach compartment: A digestive system compartment representing the stomach."""

    STOMACH_COMPARTMENT: "PBPKO"
    """stomach compartment: A digestive system compartment representing the stomach."""

    PBPKO_00567: "PBPKO"
    """bone blood partition coefficient: A partition coefficient representing the ratio of compound concentration in bone to blood."""

    BONE_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """bone blood partition coefficient: A partition coefficient representing the ratio of compound concentration in bone to blood."""

    PBPKO_00568: "PBPKO"
    """air blood partition coefficient: A partition coefficient representing the ratio of compound concentration in air to blood."""

    AIR_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """air blood partition coefficient: A partition coefficient representing the ratio of compound concentration in air to blood."""

    PBPKO_00569: "PBPKO"
    """brain blood partition coefficient: A partition coefficient representing the ratio of compound concentration in brain to blood."""

    BRAIN_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """brain blood partition coefficient: A partition coefficient representing the ratio of compound concentration in brain to blood."""

    PBPKO_00570: "PBPKO"
    """brainfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal brain to blood."""

    BRAINFETUS_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """brainfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal brain to blood."""

    PBPKO_00571: "PBPKO"
    """gonad blood partition coefficient: A partition coefficient representing the ratio of compound concentration in gonads to blood."""

    GONAD_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """gonad blood partition coefficient: A partition coefficient representing the ratio of compound concentration in gonads to blood."""

    PBPKO_00572: "PBPKO"
    """gut blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the gut to blood."""

    GUT_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """gut blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the gut to blood."""

    PBPKO_00573: "PBPKO"
    """heart blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the heart to blood."""

    HEART_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """heart blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the heart to blood."""

    PBPKO_00574: "PBPKO"
    """intestine blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the intestine to blood."""

    INTESTINE_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """intestine blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the intestine to blood."""

    PBPKO_00575: "PBPKO"
    """kidney blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the kidney to blood."""

    KIDNEY_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """kidney blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the kidney to blood."""

    PBPKO_00576: "PBPKO"
    """kidneyfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal kidney to blood."""

    KIDNEYFETUS_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """kidneyfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal kidney to blood."""

    PBPKO_00577: "PBPKO"
    """liver blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the liver to blood."""

    LIVER_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """liver blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the liver to blood."""

    PBPKO_00578: "PBPKO"
    """liverfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal liver to blood."""

    LIVERFETUS_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """liverfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal liver to blood."""

    PBPKO_00579: "PBPKO"
    """lung blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the lung to blood."""

    LUNG_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """lung blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the lung to blood."""

    PBPKO_00580: "PBPKO"
    """mammary gland blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the mammary gland to blood."""

    MAMMARY_GLAND_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """mammary gland blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the mammary gland to blood."""

    PBPKO_00581: "PBPKO"
    """milk blood partition coefficient: A partition coefficient representing the ratio of compound concentration in milk to blood."""

    MILK_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """milk blood partition coefficient: A partition coefficient representing the ratio of compound concentration in milk to blood."""

    PBPKO_00582: "PBPKO"
    """muscle blood partition coefficient: A partition coefficient representing the ratio of compound concentration in muscle to blood."""

    MUSCLE_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """muscle blood partition coefficient: A partition coefficient representing the ratio of compound concentration in muscle to blood."""

    PBPKO_00583: "PBPKO"
    """pancreas blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the pancreas to blood."""

    PANCREAS_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """pancreas blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the pancreas to blood."""

    PBPKO_00584: "PBPKO"
    """poor perfused blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the poorly perfused compartment to blood."""

    POOR_PERFUSED_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """poor perfused blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the poorly perfused compartment to blood."""

    PBPKO_00585: "PBPKO"
    """restbody blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the rest of body compartment to blood."""

    RESTBODY_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """restbody blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the rest of body compartment to blood."""

    PBPKO_00586: "PBPKO"
    """restbodyfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to blood."""

    RESTBODYFETUS_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """restbodyfetus blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to blood."""

    PBPKO_00587: "PBPKO"
    """rich perfused blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the richly perfused compartment to blood."""

    RICH_PERFUSED_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """rich perfused blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the richly perfused compartment to blood."""

    PBPKO_00588: "PBPKO"
    """skin blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the skin to blood."""

    SKIN_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """skin blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the skin to blood."""

    PBPKO_00589: "PBPKO"
    """spleen blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the spleen to blood."""

    SPLEEN_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """spleen blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the spleen to blood."""

    PBPKO_00590: "PBPKO"
    """stomach blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the stomach to blood."""

    STOMACH_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """stomach blood partition coefficient: A partition coefficient representing the ratio of compound concentration in the stomach to blood."""

    PBPKO_00591: "PBPKO"
    """fraction unbound plasma: An unbound fraction parameter specifically for plasma."""

    FRACTION_UNBOUND_PLASMA: "PBPKO"
    """fraction unbound plasma: An unbound fraction parameter specifically for plasma."""

    PBPKO_00592: "PBPKO"
    """maximum rate of apical transporter: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ when the enzyme is saturated with substrate."""

    MAXIMUM_RATE_OF_APICAL_TRANSPORTER: "PBPKO"
    """maximum rate of apical transporter: A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ when the enzyme is saturated with substrate."""

    PBPKO_00593: "PBPKO"
    """maximum rate of basolateral transporter: Maximum rate (Vmax) of transport via a basolateral transporter."""

    MAXIMUM_RATE_OF_BASOLATERAL_TRANSPORTER: "PBPKO"
    """maximum rate of basolateral transporter: Maximum rate (Vmax) of transport via a basolateral transporter."""

    PBPKO_00610: "PBPKO"
    """fraction of volume of compartment: A physiological parameter representing the dimensionless fraction computed by dividing the volume of the compartment by the total body weight."""

    FRACTION_OF_VOLUME_OF_COMPARTMENT: "PBPKO"
    """fraction of volume of compartment: A physiological parameter representing the dimensionless fraction computed by dividing the volume of the compartment by the total body weight."""

    PBPKO_00611: "PBPKO"
    """fraction of blood flow to a compartment: A physiological parameter representing dimensionless fraction of cardiac output delivered to a compartment."""

    FRACTION_OF_BLOOD_FLOW_TO_A_COMPARTMENT: "PBPKO"
    """fraction of blood flow to a compartment: A physiological parameter representing dimensionless fraction of cardiac output delivered to a compartment."""

    PBPKO_00612: "PBPKO"
    """apparent permeability: A biochemical parameter representing the apparent permeability of a compound specifically between the compartments."""

    APPARENT_PERMEABILITY: "PBPKO"
    """apparent permeability: A biochemical parameter representing the apparent permeability of a compound specifically between the compartments."""

    PBPKO_00613: "PBPKO"
    """maximum rate: A biochemical parameter representing Vmax of the enzymatic activity"""

    MAXIMUM_RATE: "PBPKO"
    """maximum rate: A biochemical parameter representing Vmax of the enzymatic activity"""

    PBPKO_00615: "PBPKO"
    """amount of compound in compartment: An output parameter representing the amount of chemical specifically in the compartment"""

    AMOUNT_OF_COMPOUND_IN_COMPARTMENT: "PBPKO"
    """amount of compound in compartment: An output parameter representing the amount of chemical specifically in the compartment"""

    PBPKO_00616: "PBPKO"
    """concentration of compound in compartment: An output parameter representing the total concentration of compound in the compartment."""

    CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT: "PBPKO"
    """concentration of compound in compartment: An output parameter representing the total concentration of compound in the compartment."""

    PBPKO_00617: "PBPKO"
    """hippocampus compartment: A part of brain compartment representing the hippocampus region of the brain"""

    HIPPOCAMPUS_COMPARTMENT: "PBPKO"
    """hippocampus compartment: A part of brain compartment representing the hippocampus region of the brain"""

    PBPKO_00618: "PBPKO"
    """cerebrum compartment: A part of brain compartment representing the cerebrum region of the brain"""

    CEREBRUM_COMPARTMENT: "PBPKO"
    """cerebrum compartment: A part of brain compartment representing the cerebrum region of the brain"""

    PBPKO_00619: "PBPKO"
    """cerebellum compartment: A part of brain compartment representing the cerebellum region of the brain"""

    CEREBELLUM_COMPARTMENT: "PBPKO"
    """cerebellum compartment: A part of brain compartment representing the cerebellum region of the brain"""

    PBPKO_00620: "PBPKO"
    """frontal cortex compartment: A part of brain compartment representing the frontal cortex region of the brain"""

    FRONTAL_CORTEX_COMPARTMENT: "PBPKO"
    """frontal cortex compartment: A part of brain compartment representing the frontal cortex region of the brain"""

    PBPKO_00621: "PBPKO"
    """cerebrospinal fluid compartment: A part of brain compartment representing the cerebrospinal fluid region of the brain"""

    CEREBROSPINAL_FLUID_COMPARTMENT: "PBPKO"
    """cerebrospinal fluid compartment: A part of brain compartment representing the cerebrospinal fluid region of the brain"""

    PBPKO_00622: "PBPKO"
    """fraction unbound blood: An unbound fraction parameter specifically for the blood compartment."""

    FRACTION_UNBOUND_BLOOD: "PBPKO"
    """fraction unbound blood: An unbound fraction parameter specifically for the blood compartment."""

    PBPKO_00623: "PBPKO"
    """amount in blood: The amount of compound in the blood compartment."""

    AMOUNT_IN_BLOOD: "PBPKO"
    """amount in blood: The amount of compound in the blood compartment."""

    PBPKO_00624: "PBPKO"
    """fraction unbound restbody: An unbound fraction parameter specifically for the rest of the body compartment."""

    FRACTION_UNBOUND_RESTBODY: "PBPKO"
    """fraction unbound restbody: An unbound fraction parameter specifically for the rest of the body compartment."""

    PBPKO_00625: "PBPKO"
    """exposed skin compartment: A skin compartment representing the exposed part of the skin to the chemical via dermal contact."""

    EXPOSED_SKIN_COMPARTMENT: "PBPKO"
    """exposed skin compartment: A skin compartment representing the exposed part of the skin to the chemical via dermal contact."""

    PBPKO_00626: "PBPKO"
    """unexposed skin compartment: A skin compartment representing the unexposed part of the skin to the chemical such as regions covered by clothing or occluded areas like the inner arms."""

    UNEXPOSED_SKIN_COMPARTMENT: "PBPKO"
    """unexposed skin compartment: A skin compartment representing the unexposed part of the skin to the chemical such as regions covered by clothing or occluded areas like the inner arms."""

    PBPKO_00627: "PBPKO"
    """fraction of arterial plasma volume: A dimensionless fraction of volume defined as the arterial plasma volume divided per unit of total body weight."""

    FRACTION_OF_ARTERIAL_PLASMA_VOLUME: "PBPKO"
    """fraction of arterial plasma volume: A dimensionless fraction of volume defined as the arterial plasma volume divided per unit of total body weight."""

    PBPKO_00628: "PBPKO"
    """fraction of venous plasma volume: A dimensionless fraction of volume defined as the venous plasma volume divided per unit of total body weight."""

    FRACTION_OF_VENOUS_PLASMA_VOLUME: "PBPKO"
    """fraction of venous plasma volume: A dimensionless fraction of volume defined as the venous plasma volume divided per unit of total body weight."""

    PBPKO_00629: "PBPKO"
    """amount in richly perfused tissue: The amount of compound in the richly perfused tissue compartment."""

    AMOUNT_IN_RICHLY_PERFUSED_TISSUE: "PBPKO"
    """amount in richly perfused tissue: The amount of compound in the richly perfused tissue compartment."""

    PBPKO_00630: "PBPKO"
    """amount in poorly perfused tissue: The amount of compound in the poorly perfused tissue compartment."""

    AMOUNT_IN_POORLY_PERFUSED_TISSUE: "PBPKO"
    """amount in poorly perfused tissue: The amount of compound in the poorly perfused tissue compartment."""

    PBPKO_00631: "PBPKO"
    """amount in arterial blood: The amount of compound in the arterial blood compartment."""

    AMOUNT_IN_ARTERIAL_BLOOD: "PBPKO"
    """amount in arterial blood: The amount of compound in the arterial blood compartment."""

    PBPKO_00632: "PBPKO"
    """amount in venous blood: The amount of compound in the venous blood compartment."""

    AMOUNT_IN_VENOUS_BLOOD: "PBPKO"
    """amount in venous blood: The amount of compound in the venous blood compartment."""

    PBPKO_00633: "PBPKO"
    """amount in alveolar air: The amount of compound in the alveolar air compartment."""

    AMOUNT_IN_ALVEOLAR_AIR: "PBPKO"
    """amount in alveolar air: The amount of compound in the alveolar air compartment."""

    PBPKO_00634: "PBPKO"
    """red blood cell compartment: A compartment representing the red blood cells of the body."""

    RED_BLOOD_CELL_COMPARTMENT: "PBPKO"
    """red blood cell compartment: A compartment representing the red blood cells of the body."""

    PBPKO_00635: "PBPKO"
    """skin thickness: A physiological parameter representing the thickness of the skin compartment"""

    SKIN_THICKNESS: "PBPKO"
    """skin thickness: A physiological parameter representing the thickness of the skin compartment"""

    PBPKO_00636: "PBPKO"
    """bodily fluid flow rate parameter: A physiological parameter representing the rate of fluid flow to a particular compartment."""

    BODILY_FLUID_FLOW_RATE_PARAMETER: "PBPKO"
    """bodily fluid flow rate parameter: A physiological parameter representing the rate of fluid flow to a particular compartment."""

    PBPKO_00637: "PBPKO"
    """amount in viable epidermis of unexposed skin: The amount of chemical in viable epidermis of unexposed skin"""

    AMOUNT_IN_VIABLE_EPIDERMIS_OF_UNEXPOSED_SKIN: "PBPKO"
    """amount in viable epidermis of unexposed skin: The amount of chemical in viable epidermis of unexposed skin"""

    PBPKO_00638: "PBPKO"
    """amount in viable epidermis of exposed skin: The amount of chemical in viable epidermis of exposed skin"""

    AMOUNT_IN_VIABLE_EPIDERMIS_OF_EXPOSED_SKIN: "PBPKO"
    """amount in viable epidermis of exposed skin: The amount of chemical in viable epidermis of exposed skin"""

    PBPKO_00639: "PBPKO"
    """amount in skin stratum corneum of unexposed skin: The amount of chemical in skin stratum corneum of unexposed skin"""

    AMOUNT_IN_SKIN_STRATUM_CORNEUM_OF_UNEXPOSED_SKIN: "PBPKO"
    """amount in skin stratum corneum of unexposed skin: The amount of chemical in skin stratum corneum of unexposed skin"""

    PBPKO_00640: "PBPKO"
    """amount in skin stratum corneum of exposed skin: The amount of chemical in skin stratum corneum of exposed skin"""

    AMOUNT_IN_SKIN_STRATUM_CORNEUM_OF_EXPOSED_SKIN: "PBPKO"
    """amount in skin stratum corneum of exposed skin: The amount of chemical in skin stratum corneum of exposed skin"""

    PBPKO_00641: "PBPKO"
    """dermal absorption rate unexposed skin: An absorption rate constant parameter representing dermal absorption rate flux through unexposed skin"""

    DERMAL_ABSORPTION_RATE_UNEXPOSED_SKIN: "PBPKO"
    """dermal absorption rate unexposed skin: An absorption rate constant parameter representing dermal absorption rate flux through unexposed skin"""

    PBPKO_00642: "PBPKO"
    """dermal absorption rate exposed skin: An absorption rate constant parameter representing dermal absorption rate flux through exposed skin"""

    DERMAL_ABSORPTION_RATE_EXPOSED_SKIN: "PBPKO"
    """dermal absorption rate exposed skin: An absorption rate constant parameter representing dermal absorption rate flux through exposed skin"""

    PBPKO_00643: "PBPKO"
    """thickness stratum corneum: A skin thickness parameter representing the thickness of stratum corneum."""

    THICKNESS_STRATUM_CORNEUM: "PBPKO"
    """thickness stratum corneum: A skin thickness parameter representing the thickness of stratum corneum."""

    PBPKO_00644: "PBPKO"
    """thickness viable epidermis: A skin thickness parameter representing the thickness of viable epidermis."""

    THICKNESS_VIABLE_EPIDERMIS: "PBPKO"
    """thickness viable epidermis: A skin thickness parameter representing the thickness of viable epidermis."""

    PBPKO_00645: "PBPKO"
    """fat blood partition coefficient: A partition coefficient representing the ratio of compound concentration in fat to blood."""

    FAT_BLOOD_PARTITION_COEFFICIENT: "PBPKO"
    """fat blood partition coefficient: A partition coefficient representing the ratio of compound concentration in fat to blood."""

    PBPKO_00646: "PBPKO"
    """diffusion rate: A biochemical parameter representing the diffusion rate of the chemical"""

    DIFFUSION_RATE: "PBPKO"
    """diffusion rate: A biochemical parameter representing the diffusion rate of the chemical"""

    PBPKO_00647: "PBPKO"
    """diffusion rate skin: A diffusion rate parameter representing diffusion rate of the chemical across the skin"""

    DIFFUSION_RATE_SKIN: "PBPKO"
    """diffusion rate skin: A diffusion rate parameter representing diffusion rate of the chemical across the skin"""

    PBPKO_00648: "PBPKO"
    """diffusion rate stratum corneum viable epidermis: A diffusion rate skin parameter representing diffusion rate from stratum corneum to viable epidermis"""

    DIFFUSION_RATE_STRATUM_CORNEUM_VIABLE_EPIDERMIS: "PBPKO"
    """diffusion rate stratum corneum viable epidermis: A diffusion rate skin parameter representing diffusion rate from stratum corneum to viable epidermis"""

    PBPKO_00649: "PBPKO"
    """miscellaneous parameter: A parameter being used in the model but does not belong to specific parameter subclass"""

    MISCELLANEOUS_PARAMETER: "PBPKO"
    """miscellaneous parameter: A parameter being used in the model but does not belong to specific parameter subclass"""

    PBPKO_00650: "PBPKO"
    """Michaelis: A flag indicating for Michaelis-Menten or linear metabolism equation being used in the model"""

    MICHAELIS: "PBPKO"
    """Michaelis: A flag indicating for Michaelis-Menten or linear metabolism equation being used in the model"""

    PBPKO_00651: "PBPKO"
    """fraction of arterial blood volume: A dimensionless fraction of volume defined as the arterial blood volume divided per unit of total body weight."""

    FRACTION_OF_ARTERIAL_BLOOD_VOLUME: "PBPKO"
    """fraction of arterial blood volume: A dimensionless fraction of volume defined as the arterial blood volume divided per unit of total body weight."""

    PBPKO_01501: "PBPKO"
    """pgp."""

    PGP: "PBPKO"
    """pgp."""

    PBPKO_01502: "PBPKO"
    """mrp2."""

    MRP2: "PBPKO"
    """mrp2."""

    PBPKO_01503: "PBPKO"
    """mrp4."""

    MRP4: "PBPKO"
    """mrp4."""

    PBPKO_01504: "PBPKO"
    """bcrp."""

    BCRP: "PBPKO"
    """bcrp."""

    PBPKO_01505: "PBPKO"
    """nctp."""

    NCTP: "PBPKO"
    """nctp."""

    PBPKO_01506: "PBPKO"
    """oct1."""

    OCT1: "PBPKO"
    """oct1."""

    PBPKO_01507: "PBPKO"
    """oat1."""

    OAT1: "PBPKO"
    """oat1."""

    PBPKO_01508: "PBPKO"
    """oat3."""

    OAT3: "PBPKO"
    """oat3."""

    PBPKO_01509: "PBPKO"
    """oat4."""

    OAT4: "PBPKO"
    """oat4."""

    PBPKO_02001: "PBPKO"
    """bile compartment: A compartment representing the bile storage"""

    BILE_COMPARTMENT: "PBPKO"
    """bile compartment: A compartment representing the bile storage"""

    PBPKO_02002: "PBPKO"
    """colon compartment: A compartment representing the colon"""

    COLON_COMPARTMENT: "PBPKO"
    """colon compartment: A compartment representing the colon"""

    PBPKO_02003: "PBPKO"
    """small intestine tissue compartment: A compartment representing the small intestinal tissue"""

    SMALL_INTESTINE_TISSUE_COMPARTMENT: "PBPKO"
    """small intestine tissue compartment: A compartment representing the small intestinal tissue"""

    PBPKO_02004: "PBPKO"
    """intestinal tissue compartment: A compartment representing the whole intestinal tissue"""

    INTESTINAL_TISSUE_COMPARTMENT: "PBPKO"
    """intestinal tissue compartment: A compartment representing the whole intestinal tissue"""

    PBPKO_02005: "PBPKO"
    """portal vein perfused tissue comparment: A compartment with grouped organs that are exclusively perfused via the portal vein (i.e.: Stomach, small and large intestine, spleen)"""

    PORTAL_VEIN_PERFUSED_TISSUE_COMPARMENT: "PBPKO"
    """portal vein perfused tissue comparment: A compartment with grouped organs that are exclusively perfused via the portal vein (i.e.: Stomach, small and large intestine, spleen)"""

    PBPKO_02006: "PBPKO"
    """glomerulus compartment: A part of kidney compartment in the model representing glomerulus in the body"""

    GLOMERULUS_COMPARTMENT: "PBPKO"
    """glomerulus compartment: A part of kidney compartment in the model representing glomerulus in the body"""

    PBPKO_02007: "PBPKO"
    """menstrual plasma compartment: A compartment representing menstrual plasma"""

    MENSTRUAL_PLASMA_COMPARTMENT: "PBPKO"
    """menstrual plasma compartment: A compartment representing menstrual plasma"""

    PBPKO_02008: "PBPKO"
    """kidney rest lumen compartment: A compartment representing rest of the lumen of kidney."""

    KIDNEY_REST_LUMEN_COMPARTMENT: "PBPKO"
    """kidney rest lumen compartment: A compartment representing rest of the lumen of kidney."""

    PBPKO_02009: "PBPKO"
    """kidney proximal tubule tissue compartment: A compartment representing rest of the tissue of kidney."""

    KIDNEY_PROXIMAL_TUBULE_TISSUE_COMPARTMENT: "PBPKO"
    """kidney proximal tubule tissue compartment: A compartment representing rest of the tissue of kidney."""

    PBPKO_02010: "PBPKO"
    """liver extracellular compartment: A compartment representing vascular and interstitial space of the liver."""

    LIVER_EXTRACELLULAR_COMPARTMENT: "PBPKO"
    """liver extracellular compartment: A compartment representing vascular and interstitial space of the liver."""

    PBPKO_02011: "PBPKO"
    """liver intracellular space compartment: A compartment representing intracellular space of the liver."""

    LIVER_INTRACELLULAR_SPACE_COMPARTMENT: "PBPKO"
    """liver intracellular space compartment: A compartment representing intracellular space of the liver."""

    PBPKO_02012: "PBPKO"
    """gastro intestinal tract compartment: A digestive system compartment representing the gastro-intestinal tract"""

    GASTRO_INTESTINAL_TRACT_COMPARTMENT: "PBPKO"
    """gastro intestinal tract compartment: A digestive system compartment representing the gastro-intestinal tract"""

    PBPKO_02013: "PBPKO"
    """gonad compartment: A compartment representing gonads."""

    GONAD_COMPARTMENT: "PBPKO"
    """gonad compartment: A compartment representing gonads."""

    PBPKO_03001: "PBPKO"
    """intrinsic gastric emptying rate: The absorption rate constant parameter representing the intrinsic rate of the chemical release from stomach to lumen or the jejunum segment"""

    INTRINSIC_GASTRIC_EMPTYING_RATE: "PBPKO"
    """intrinsic gastric emptying rate: The absorption rate constant parameter representing the intrinsic rate of the chemical release from stomach to lumen or the jejunum segment"""

    PBPKO_03002: "PBPKO"
    """intrinsic absorption rate: The absorption rate constant parameter representing the intrinsic absorption rate from the gut or any intestinal segment to the liver or the portal vein"""

    INTRINSIC_ABSORPTION_RATE: "PBPKO"
    """intrinsic absorption rate: The absorption rate constant parameter representing the intrinsic absorption rate from the gut or any intestinal segment to the liver or the portal vein"""

    PBPKO_03003: "PBPKO"
    """intrinsic stomach uptake rate: The absorption rate constant parameter representing the intrinsic absorption rate of a chemical from the stomach to the gut tissue or any intestinal segment"""

    INTRINSIC_STOMACH_UPTAKE_RATE: "PBPKO"
    """intrinsic stomach uptake rate: The absorption rate constant parameter representing the intrinsic absorption rate of a chemical from the stomach to the gut tissue or any intestinal segment"""

    PBPKO_03004: "PBPKO"
    """stomach uptake rate: The absorption rate constant parameter representing the absorption rate from stomach to gut tissue or any intestine segment"""

    STOMACH_UPTAKE_RATE: "PBPKO"
    """stomach uptake rate: The absorption rate constant parameter representing the absorption rate from stomach to gut tissue or any intestine segment"""

    PBPKO_03005: "PBPKO"
    """intrinsic fecal excretion rate."""

    INTRINSIC_FECAL_EXCRETION_RATE: "PBPKO"
    """intrinsic fecal excretion rate."""

    PBPKO_03006: "PBPKO"
    """fecal excretion rate."""

    FECAL_EXCRETION_RATE: "PBPKO"
    """fecal excretion rate."""

    PBPKO_03007: "PBPKO"
    """intrinsic biliary clearance rate."""

    INTRINSIC_BILIARY_CLEARANCE_RATE: "PBPKO"
    """intrinsic biliary clearance rate."""

    PBPKO_03008: "PBPKO"
    """kinetic emptying rate from jejunum lumen to ileum lumen."""

    KINETIC_EMPTYING_RATE_FROM_JEJUNUM_LUMEN_TO_ILEUM_LUMEN: "PBPKO"
    """kinetic emptying rate from jejunum lumen to ileum lumen."""

    PBPKO_03009: "PBPKO"
    """kinetic emptying  rate from ileum lumen to large intestine lumen."""

    KINETIC_EMPTYING__RATE_FROM_ILEUM_LUMEN_TO_LARGE_INTESTINE_LUMEN: "PBPKO"
    """kinetic emptying  rate from ileum lumen to large intestine lumen."""

    PBPKO_03010: "PBPKO"
    """kinetic absorption rate from jejunum lumen to intestinal tissue."""

    KINETIC_ABSORPTION_RATE_FROM_JEJUNUM_LUMEN_TO_INTESTINAL_TISSUE: "PBPKO"
    """kinetic absorption rate from jejunum lumen to intestinal tissue."""

    PBPKO_03011: "PBPKO"
    """kinetic absorption rate from ileum lumen to intestinal tissue."""

    KINETIC_ABSORPTION_RATE_FROM_ILEUM_LUMEN_TO_INTESTINAL_TISSUE: "PBPKO"
    """kinetic absorption rate from ileum lumen to intestinal tissue."""

    PBPKO_03012: "PBPKO"
    """kinetic absorption rate from large intestinal lumen to intestinal tissue."""

    KINETIC_ABSORPTION_RATE_FROM_LARGE_INTESTINAL_LUMEN_TO_INTESTINAL_TISSUE: "PBPKO"
    """kinetic absorption rate from large intestinal lumen to intestinal tissue."""

    PBPKO_03013: "PBPKO"
    """effective Caco-2 permeability."""

    EFFECTIVE_CACO_2_PERMEABILITY: "PBPKO"
    """effective Caco-2 permeability."""

    PBPKO_03014: "PBPKO"
    """apparent Caco-2 permeability."""

    APPARENT_CACO_2_PERMEABILITY: "PBPKO"
    """apparent Caco-2 permeability."""

    PBPKO_03015: "PBPKO"
    """kinetic emptying  rate between intestinal segments."""

    KINETIC_EMPTYING__RATE_BETWEEN_INTESTINAL_SEGMENTS: "PBPKO"
    """kinetic emptying  rate between intestinal segments."""

    PBPKO_03016: "PBPKO"
    """Hill dissociation constant."""

    HILL_DISSOCIATION_CONSTANT: "PBPKO"
    """Hill dissociation constant."""

    PBPKO_03017: "PBPKO"
    """Hill coefficient."""

    HILL_COEFFICIENT: "PBPKO"
    """Hill coefficient."""

    PBPKO_03018: "PBPKO"
    """intrinsic absorption rate of metabilite."""

    INTRINSIC_ABSORPTION_RATE_OF_METABILITE: "PBPKO"
    """intrinsic absorption rate of metabilite."""

    PBPKO_03019: "PBPKO"
    """absorption rate of metabolite."""

    ABSORPTION_RATE_OF_METABOLITE: "PBPKO"
    """absorption rate of metabolite."""

    PBPKO_03020: "PBPKO"
    """intrinsic enterohepatic recirculation rate constant."""

    INTRINSIC_ENTEROHEPATIC_RECIRCULATION_RATE_CONSTANT: "PBPKO"
    """intrinsic enterohepatic recirculation rate constant."""

    PBPKO_03021: "PBPKO"
    """enterohepatic recirculation rate constant."""

    ENTEROHEPATIC_RECIRCULATION_RATE_CONSTANT: "PBPKO"
    """enterohepatic recirculation rate constant."""

    PBPKO_03023: "PBPKO"
    """intrinsic reabsorption rate constant."""

    INTRINSIC_REABSORPTION_RATE_CONSTANT: "PBPKO"
    """intrinsic reabsorption rate constant."""

    PBPKO_03024: "PBPKO"
    """reabsorption rate constant."""

    REABSORPTION_RATE_CONSTANT: "PBPKO"
    """reabsorption rate constant."""

    PBPKO_03025: "PBPKO"
    """maximum capacity of binding sites in red cells."""

    MAXIMUM_CAPACITY_OF_BINDING_SITES_IN_RED_CELLS: "PBPKO"
    """maximum capacity of binding sites in red cells."""

    PBPKO_03026: "PBPKO"
    """half-saturation concentration of chemical for binding by sites in red cells."""

    HALF_SATURATION_CONCENTRATION_OF_CHEMICAL_FOR_BINDING_BY_SITES_IN_RED_CELLS: "PBPKO"
    """half-saturation concentration of chemical for binding by sites in red cells."""

    PBPKO_03027: "PBPKO"
    """metabolism rate constant in liver."""

    METABOLISM_RATE_CONSTANT_IN_LIVER: "PBPKO"
    """metabolism rate constant in liver."""

    PBPKO_03028: "PBPKO"
    """metabolism rate constant in intestinal tissue."""

    METABOLISM_RATE_CONSTANT_IN_INTESTINAL_TISSUE: "PBPKO"
    """metabolism rate constant in intestinal tissue."""

    PBPKO_03030: "PBPKO"
    """red blood cells partition coefficient."""

    RED_BLOOD_CELLS_PARTITION_COEFFICIENT: "PBPKO"
    """red blood cells partition coefficient."""

    PBPKO_03031: "PBPKO"
    """follicle permeability coefficient."""

    FOLLICLE_PERMEABILITY_COEFFICIENT: "PBPKO"
    """follicle permeability coefficient."""

    PBPKO_03032: "PBPKO"
    """partition coeffcient of stratum corneum to viable epidermis."""

    PARTITION_COEFFCIENT_OF_STRATUM_CORNEUM_TO_VIABLE_EPIDERMIS: "PBPKO"
    """partition coeffcient of stratum corneum to viable epidermis."""

    PBPKO_03033: "PBPKO"
    """partition coeffcient of viable epidermis to blood."""

    PARTITION_COEFFCIENT_OF_VIABLE_EPIDERMIS_TO_BLOOD: "PBPKO"
    """partition coeffcient of viable epidermis to blood."""

    PBPKO_03034: "PBPKO"
    """partition coeffcient of stratum corneum to skin surface depot."""

    PARTITION_COEFFCIENT_OF_STRATUM_CORNEUM_TO_SKIN_SURFACE_DEPOT: "PBPKO"
    """partition coeffcient of stratum corneum to skin surface depot."""

    PBPKO_03035: "PBPKO"
    """partition coeffcient of follicle to skin surface depot."""

    PARTITION_COEFFCIENT_OF_FOLLICLE_TO_SKIN_SURFACE_DEPOT: "PBPKO"
    """partition coeffcient of follicle to skin surface depot."""

    PBPKO_03036: "PBPKO"
    """octanol water partition coefficient."""

    OCTANOL_WATER_PARTITION_COEFFICIENT: "PBPKO"
    """octanol water partition coefficient."""

    PBPKO_03037: "PBPKO"
    """medium polymer partition coefficient."""

    MEDIUM_POLYMER_PARTITION_COEFFICIENT: "PBPKO"
    """medium polymer partition coefficient."""

    PBPKO_03038: "PBPKO"
    """medium air partition coefficient."""

    MEDIUM_AIR_PARTITION_COEFFICIENT: "PBPKO"
    """medium air partition coefficient."""

    PBPKO_03039: "PBPKO"
    """medium mitochondria partition coefficient."""

    MEDIUM_MITOCHONDRIA_PARTITION_COEFFICIENT: "PBPKO"
    """medium mitochondria partition coefficient."""

    PBPKO_03040: "PBPKO"
    """medium lysosomes partition coefficient."""

    MEDIUM_LYSOSOMES_PARTITION_COEFFICIENT: "PBPKO"
    """medium lysosomes partition coefficient."""

    PBPKO_03041: "PBPKO"
    """medium intracellular water partition coefficient."""

    MEDIUM_INTRACELLULAR_WATER_PARTITION_COEFFICIENT: "PBPKO"
    """medium intracellular water partition coefficient."""

    PBPKO_03042: "PBPKO"
    """medium microsomes partition coefficient."""

    MEDIUM_MICROSOMES_PARTITION_COEFFICIENT: "PBPKO"
    """medium microsomes partition coefficient."""

    PBPKO_03043: "PBPKO"
    """medium other organelles partition coefficient."""

    MEDIUM_OTHER_ORGANELLES_PARTITION_COEFFICIENT: "PBPKO"
    """medium other organelles partition coefficient."""

    PBPKO_03044: "PBPKO"
    """medium albumin partition coefficient."""

    MEDIUM_ALBUMIN_PARTITION_COEFFICIENT: "PBPKO"
    """medium albumin partition coefficient."""

    PBPKO_03045: "PBPKO"
    """abiotic degradation rate in medium."""

    ABIOTIC_DEGRADATION_RATE_IN_MEDIUM: "PBPKO"
    """abiotic degradation rate in medium."""

    PBPKO_03046: "PBPKO"
    """acidic phospholipid association constant."""

    ACIDIC_PHOSPHOLIPID_ASSOCIATION_CONSTANT: "PBPKO"
    """acidic phospholipid association constant."""

    PBPKO_03047: "PBPKO"
    """abiotic degradation rate in air."""

    ABIOTIC_DEGRADATION_RATE_IN_AIR: "PBPKO"
    """abiotic degradation rate in air."""

    PBPKO_03048: "PBPKO"
    """maximum metabolic rate."""

    MAXIMUM_METABOLIC_RATE: "PBPKO"
    """maximum metabolic rate."""

    PBPKO_03049: "PBPKO"
    """linear metabolic rate."""

    LINEAR_METABOLIC_RATE: "PBPKO"
    """linear metabolic rate."""

    PBPKO_03050: "PBPKO"
    """cell radius."""

    CELL_RADIUS: "PBPKO"
    """cell radius."""

    PBPKO_03051: "PBPKO"
    """cell replication time."""

    CELL_REPLICATION_TIME: "PBPKO"
    """cell replication time."""

    PBPKO_03052: "PBPKO"
    """cell fraction of proteins."""

    CELL_FRACTION_OF_PROTEINS: "PBPKO"
    """cell fraction of proteins."""

    PBPKO_03053: "PBPKO"
    """cell fraction of lipids."""

    CELL_FRACTION_OF_LIPIDS: "PBPKO"
    """cell fraction of lipids."""

    PBPKO_03054: "PBPKO"
    """cell fraction of intracellular water."""

    CELL_FRACTION_OF_INTRACELLULAR_WATER: "PBPKO"
    """cell fraction of intracellular water."""

    PBPKO_03055: "PBPKO"
    """cell fraction of mitochondria."""

    CELL_FRACTION_OF_MITOCHONDRIA: "PBPKO"
    """cell fraction of mitochondria."""

    PBPKO_03056: "PBPKO"
    """cell fraction of lysosomes."""

    CELL_FRACTION_OF_LYSOSOMES: "PBPKO"
    """cell fraction of lysosomes."""

    PBPKO_03057: "PBPKO"
    """cell fraction of microsomes."""

    CELL_FRACTION_OF_MICROSOMES: "PBPKO"
    """cell fraction of microsomes."""

    PBPKO_03058: "PBPKO"
    """fraction of neutral lipids in the FBS."""

    FRACTION_OF_NEUTRAL_LIPIDS_IN_THE_FBS: "PBPKO"
    """fraction of neutral lipids in the FBS."""

    PBPKO_03059: "PBPKO"
    """fraction of albumin in the FBS."""

    FRACTION_OF_ALBUMIN_IN_THE_FBS: "PBPKO"
    """fraction of albumin in the FBS."""

    PBPKO_03060: "PBPKO"
    """culture area."""

    CULTURE_AREA: "PBPKO"
    """culture area."""

    PBPKO_03061: "PBPKO"
    """top well diameter."""

    TOP_WELL_DIAMETER: "PBPKO"
    """top well diameter."""

    PBPKO_03062: "PBPKO"
    """well depth."""

    WELL_DEPTH: "PBPKO"
    """well depth."""

    PBPKO_03063: "PBPKO"
    """plate wall thickness."""

    PLATE_WALL_THICKNESS: "PBPKO"
    """plate wall thickness."""

    PBPKO_03064: "PBPKO"
    """culture medium pH."""

    CULTURE_MEDIUM_PH: "PBPKO"
    """culture medium pH."""

    PBPKO_03065: "PBPKO"
    """fraction of serum in total media."""

    FRACTION_OF_SERUM_IN_TOTAL_MEDIA: "PBPKO"
    """fraction of serum in total media."""

    PBPKO_03066: "PBPKO"
    """FBS pH."""

    FBS_PH: "PBPKO"
    """FBS pH."""

    PBPKO_03067: "PBPKO"
    """initial number of cells."""

    INITIAL_NUMBER_OF_CELLS: "PBPKO"
    """initial number of cells."""

    PBPKO_03068: "PBPKO"
    """nominal concentration of medium."""

    NOMINAL_CONCENTRATION_OF_MEDIUM: "PBPKO"
    """nominal concentration of medium."""

    PBPKO_03069: "PBPKO"
    """volume of medium."""

    VOLUME_OF_MEDIUM: "PBPKO"
    """volume of medium."""

    PBPKO_03070: "PBPKO"
    """fraction of FBS iin the medium."""

    FRACTION_OF_FBS_IIN_THE_MEDIUM: "PBPKO"
    """fraction of FBS iin the medium."""

    PBPKO_03071: "PBPKO"
    """ionized fraction in the medium."""

    IONIZED_FRACTION_IN_THE_MEDIUM: "PBPKO"
    """ionized fraction in the medium."""

    PBPKO_03072: "PBPKO"
    """fraction unbound in the medium."""

    FRACTION_UNBOUND_IN_THE_MEDIUM: "PBPKO"
    """fraction unbound in the medium."""

    PBPKO_03073: "PBPKO"
    """fraction unbound in the FBS."""

    FRACTION_UNBOUND_IN_THE_FBS: "PBPKO"
    """fraction unbound in the FBS."""

    PBPKO_03074: "PBPKO"
    """fraction unbound in the cell."""

    FRACTION_UNBOUND_IN_THE_CELL: "PBPKO"
    """fraction unbound in the cell."""

    PBPKO_03075: "PBPKO"
    """absorption rate constant: A biochemical parameter representing the rate constant at which a compound is absorbed into systemic circulation or a target compartment from the site of administration"""

    ABSORPTION_RATE_CONSTANT: "PBPKO"
    """absorption rate constant: A biochemical parameter representing the rate constant at which a compound is absorbed into systemic circulation or a target compartment from the site of administration"""

    PBPKO_03076: "PBPKO"
    """fraction unbound kidney proximal tubule: An unbound fraction parameter specifically for the kidney proximal tubule."""

    FRACTION_UNBOUND_KIDNEY_PROXIMAL_TUBULE: "PBPKO"
    """fraction unbound kidney proximal tubule: An unbound fraction parameter specifically for the kidney proximal tubule."""

    PBPKO_04001: "PBPKO"
    """plasma flow rate: A bodily fluid flow rate parameter specifically describing the flow of plasma to a compartment."""

    PLASMA_FLOW_RATE: "PBPKO"
    """plasma flow rate: A bodily fluid flow rate parameter specifically describing the flow of plasma to a compartment."""

    PBPKO_04002: "PBPKO"
    """plasma flow rate to stomach: A plasma flow rate parameter specifically describing the rate to the stomach compartment."""

    PLASMA_FLOW_RATE_TO_STOMACH: "PBPKO"
    """plasma flow rate to stomach: A plasma flow rate parameter specifically describing the rate to the stomach compartment."""

    PBPKO_04003: "PBPKO"
    """plasma flow rate to intestine: A plasma flow rate parameter specifically describing the rate to the intestine compartment."""

    PLASMA_FLOW_RATE_TO_INTESTINE: "PBPKO"
    """plasma flow rate to intestine: A plasma flow rate parameter specifically describing the rate to the intestine compartment."""

    PBPKO_04004: "PBPKO"
    """plasma flow rate to small intestine: A plasma flow rate parameter specifically describing the rate to the small intestine compartment."""

    PLASMA_FLOW_RATE_TO_SMALL_INTESTINE: "PBPKO"
    """plasma flow rate to small intestine: A plasma flow rate parameter specifically describing the rate to the small intestine compartment."""

    PBPKO_04005: "PBPKO"
    """plasma flow rate to large intestine: A plasma flow rate parameter specifically describing the rate to the large intestine compartment."""

    PLASMA_FLOW_RATE_TO_LARGE_INTESTINE: "PBPKO"
    """plasma flow rate to large intestine: A plasma flow rate parameter specifically describing the rate to the large intestine compartment."""

    PBPKO_04006: "PBPKO"
    """plasma flow rate to pancreas: A plasma flow rate parameter specifically describing the rate to the pancreas compartment."""

    PLASMA_FLOW_RATE_TO_PANCREAS: "PBPKO"
    """plasma flow rate to pancreas: A plasma flow rate parameter specifically describing the rate to the pancreas compartment."""

    PBPKO_04007: "PBPKO"
    """plasma flow rate to liver: A plasma flow rate parameter specifically describing the rate to the liver compartment."""

    PLASMA_FLOW_RATE_TO_LIVER: "PBPKO"
    """plasma flow rate to liver: A plasma flow rate parameter specifically describing the rate to the liver compartment."""

    PBPKO_04008: "PBPKO"
    """plasma flow rate to kidney: A plasma flow rate parameter specifically describing the rate to the kidney compartment."""

    PLASMA_FLOW_RATE_TO_KIDNEY: "PBPKO"
    """plasma flow rate to kidney: A plasma flow rate parameter specifically describing the rate to the kidney compartment."""

    PBPKO_04009: "PBPKO"
    """plasma flow rate to muscle: A plasma flow rate parameter specifically describing the rate to the muscle compartment."""

    PLASMA_FLOW_RATE_TO_MUSCLE: "PBPKO"
    """plasma flow rate to muscle: A plasma flow rate parameter specifically describing the rate to the muscle compartment."""

    PBPKO_04010: "PBPKO"
    """plasma flow rate to heart: A plasma flow rate parameter specifically describing the rate to the heart compartment."""

    PLASMA_FLOW_RATE_TO_HEART: "PBPKO"
    """plasma flow rate to heart: A plasma flow rate parameter specifically describing the rate to the heart compartment."""

    PBPKO_04011: "PBPKO"
    """plasma flow rate to fat: A plasma flow rate parameter specifically describing the rate to the fat compartment."""

    PLASMA_FLOW_RATE_TO_FAT: "PBPKO"
    """plasma flow rate to fat: A plasma flow rate parameter specifically describing the rate to the fat compartment."""

    PBPKO_04012: "PBPKO"
    """plasma flow rate to gonad: A plasma flow rate parameter specifically describing the rate to the gonad compartment."""

    PLASMA_FLOW_RATE_TO_GONAD: "PBPKO"
    """plasma flow rate to gonad: A plasma flow rate parameter specifically describing the rate to the gonad compartment."""

    PBPKO_04013: "PBPKO"
    """plasma flow rate to skin: A plasma flow rate parameter specifically describing the rate to the skin compartment."""

    PLASMA_FLOW_RATE_TO_SKIN: "PBPKO"
    """plasma flow rate to skin: A plasma flow rate parameter specifically describing the rate to the skin compartment."""

    PBPKO_04014: "PBPKO"
    """plasma flow rate to bone: A plasma flow rate parameter specifically describing the rate to the bone compartment."""

    PLASMA_FLOW_RATE_TO_BONE: "PBPKO"
    """plasma flow rate to bone: A plasma flow rate parameter specifically describing the rate to the bone compartment."""

    PBPKO_04015: "PBPKO"
    """plasma flow rate to brain: A plasma flow rate parameter specifically describing the rate to the brain compartment."""

    PLASMA_FLOW_RATE_TO_BRAIN: "PBPKO"
    """plasma flow rate to brain: A plasma flow rate parameter specifically describing the rate to the brain compartment."""

    PBPKO_04016: "PBPKO"
    """plasma flow rate to spleen: A plasma flow rate parameter specifically describing the rate to the spleen compartment."""

    PLASMA_FLOW_RATE_TO_SPLEEN: "PBPKO"
    """plasma flow rate to spleen: A plasma flow rate parameter specifically describing the rate to the spleen compartment."""

    PBPKO_04017: "PBPKO"
    """plasma flow rate to lung: A plasma flow rate parameter specifically describing the rate to the lung compartment."""

    PLASMA_FLOW_RATE_TO_LUNG: "PBPKO"
    """plasma flow rate to lung: A plasma flow rate parameter specifically describing the rate to the lung compartment."""

    PBPKO_04018: "PBPKO"
    """plasma flow rate to poorly perfused: A plasma flow rate parameter specifically describing the rate to the poorly perfused compartment."""

    PLASMA_FLOW_RATE_TO_POORLY_PERFUSED: "PBPKO"
    """plasma flow rate to poorly perfused: A plasma flow rate parameter specifically describing the rate to the poorly perfused compartment."""

    PBPKO_04019: "PBPKO"
    """plasma flow rate to richly perfused: A plasma flow rate parameter specifically describing the rate to the richly perfused compartment."""

    PLASMA_FLOW_RATE_TO_RICHLY_PERFUSED: "PBPKO"
    """plasma flow rate to richly perfused: A plasma flow rate parameter specifically describing the rate to the richly perfused compartment."""

    PBPKO_04020: "PBPKO"
    """plasma flow rate to restbody: A plasma flow rate parameter specifically describing the rate to the rest of the body compartment."""

    PLASMA_FLOW_RATE_TO_RESTBODY: "PBPKO"
    """plasma flow rate to restbody: A plasma flow rate parameter specifically describing the rate to the rest of the body compartment."""

    PBPKO_04021: "PBPKO"
    """plasma flow rate to gall bladder: A plasma flow rate parameter specifically describing the rate to the gall bladder compartment."""

    PLASMA_FLOW_RATE_TO_GALL_BLADDER: "PBPKO"
    """plasma flow rate to gall bladder: A plasma flow rate parameter specifically describing the rate to the gall bladder compartment."""

    PBPKO_04022: "PBPKO"
    """plasma flow rate to portal vein: A plasma flow rate parameter specifically describing the rate to the portal vein compartment."""

    PLASMA_FLOW_RATE_TO_PORTAL_VEIN: "PBPKO"
    """plasma flow rate to portal vein: A plasma flow rate parameter specifically describing the rate to the portal vein compartment."""

    PBPKO_04023: "PBPKO"
    """plasma flow rate to lymph: A plasma flow rate parameter specifically describing the rate to the lymph compartment."""

    PLASMA_FLOW_RATE_TO_LYMPH: "PBPKO"
    """plasma flow rate to lymph: A plasma flow rate parameter specifically describing the rate to the lymph compartment."""

    PBPKO_04024: "PBPKO"
    """plasma flow rate to duodenum: A plasma flow rate parameter specifically describing the rate to the duodenum compartment."""

    PLASMA_FLOW_RATE_TO_DUODENUM: "PBPKO"
    """plasma flow rate to duodenum: A plasma flow rate parameter specifically describing the rate to the duodenum compartment."""

    PBPKO_04025: "PBPKO"
    """plasma flow rate to jejunum: A plasma flow rate parameter specifically describing the rate to the jejunum compartment."""

    PLASMA_FLOW_RATE_TO_JEJUNUM: "PBPKO"
    """plasma flow rate to jejunum: A plasma flow rate parameter specifically describing the rate to the jejunum compartment."""

    PBPKO_04026: "PBPKO"
    """plasma flow rate to ileum: A plasma flow rate parameter specifically describing the rate to the ileum compartment."""

    PLASMA_FLOW_RATE_TO_ILEUM: "PBPKO"
    """plasma flow rate to ileum: A plasma flow rate parameter specifically describing the rate to the ileum compartment."""

    PBPKO_04027: "PBPKO"
    """plasma flow rate to colon: A plasma flow rate parameter specifically describing the rate to the colon compartment."""

    PLASMA_FLOW_RATE_TO_COLON: "PBPKO"
    """plasma flow rate to colon: A plasma flow rate parameter specifically describing the rate to the colon compartment."""

    PBPKO_04028: "PBPKO"
    """plasma flow rate to cecum: A plasma flow rate parameter specifically describing the rate to the cecum compartment."""

    PLASMA_FLOW_RATE_TO_CECUM: "PBPKO"
    """plasma flow rate to cecum: A plasma flow rate parameter specifically describing the rate to the cecum compartment."""

    PBPKO_04029: "PBPKO"
    """plasma flow rate to filtrate: A plasma flow rate parameter specifically describing the rate to the filtrate compartment."""

    PLASMA_FLOW_RATE_TO_FILTRATE: "PBPKO"
    """plasma flow rate to filtrate: A plasma flow rate parameter specifically describing the rate to the filtrate compartment."""

    PBPKO_04030: "PBPKO"
    """plasma flow rate to bone marrow: A plasma flow parameter specifically describing the rate to the bone marrow compartment."""

    PLASMA_FLOW_RATE_TO_BONE_MARROW: "PBPKO"
    """plasma flow rate to bone marrow: A plasma flow parameter specifically describing the rate to the bone marrow compartment."""

    PBPKO_04031: "PBPKO"
    """plasma flow rate to gut: A plasma flow rate parameter specifically describing the rate to the gut compartment."""

    PLASMA_FLOW_RATE_TO_GUT: "PBPKO"
    """plasma flow rate to gut: A plasma flow rate parameter specifically describing the rate to the gut compartment."""

    PBPKO_04032: "PBPKO"
    """plasma flow rate to mammary gland: A plasma flow rate parameter specifically describing the rate to the mammary gland compartment."""

    PLASMA_FLOW_RATE_TO_MAMMARY_GLAND: "PBPKO"
    """plasma flow rate to mammary gland: A plasma flow rate parameter specifically describing the rate to the mammary gland compartment."""

    PBPKO_04033: "PBPKO"
    """plasma flow rate for mass balance: A plasma flow rate parameter representing the check for total plasma flow mass balance of all the compartments (sum of organ flows should equal cardiac output)."""

    PLASMA_FLOW_RATE_FOR_MASS_BALANCE: "PBPKO"
    """plasma flow rate for mass balance: A plasma flow rate parameter representing the check for total plasma flow mass balance of all the compartments (sum of organ flows should equal cardiac output)."""

    PBPKO_04034: "PBPKO"
    """plasma flow rate to unexposed skin: A plasma flow rate parameter specifically describing the rate to the unexposed skin compartment."""

    PLASMA_FLOW_RATE_TO_UNEXPOSED_SKIN: "PBPKO"
    """plasma flow rate to unexposed skin: A plasma flow rate parameter specifically describing the rate to the unexposed skin compartment."""

    PBPKO_04035: "PBPKO"
    """plasma flow rate to exposed skin: A plasma flow rate parameter specifically describing the rate to the exposed skin compartment."""

    PLASMA_FLOW_RATE_TO_EXPOSED_SKIN: "PBPKO"
    """plasma flow rate to exposed skin: A plasma flow rate parameter specifically describing the rate to the exposed skin compartment."""

    PBPKO_04036: "PBPKO"
    """plasma flow rate to skin stratum corneum unexposed: A plasma flow rate parameter specifically describing the rate to the unexposed stratum corneum compartment."""

    PLASMA_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_UNEXPOSED: "PBPKO"
    """plasma flow rate to skin stratum corneum unexposed: A plasma flow rate parameter specifically describing the rate to the unexposed stratum corneum compartment."""

    PBPKO_04037: "PBPKO"
    """plasma flow rate to skin stratum corneum exposed: A plasma flow rate parameter specifically describing the rate to the exposed stratum corneum compartment."""

    PLASMA_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_EXPOSED: "PBPKO"
    """plasma flow rate to skin stratum corneum exposed: A plasma flow rate parameter specifically describing the rate to the exposed stratum corneum compartment."""

    PBPKO_04038: "PBPKO"
    """fraction of blood flow to red blood cells."""

    FRACTION_OF_BLOOD_FLOW_TO_RED_BLOOD_CELLS: "PBPKO"
    """fraction of blood flow to red blood cells."""

    PBPKO_04039: "PBPKO"
    """blood flow rate to red blood cells."""

    BLOOD_FLOW_RATE_TO_RED_BLOOD_CELLS: "PBPKO"
    """blood flow rate to red blood cells."""

    PBPKO_04040: "PBPKO"
    """volumen of lumen."""

    VOLUMEN_OF_LUMEN: "PBPKO"
    """volumen of lumen."""

    PBPKO_04041: "PBPKO"
    """volume of small intestine tissue."""

    VOLUME_OF_SMALL_INTESTINE_TISSUE: "PBPKO"
    """volume of small intestine tissue."""

    PBPKO_04042: "PBPKO"
    """volume of bile."""

    VOLUME_OF_BILE: "PBPKO"
    """volume of bile."""

    PBPKO_04043: "PBPKO"
    """enterocyte volume."""

    ENTEROCYTE_VOLUME: "PBPKO"
    """enterocyte volume."""

    PBPKO_04044: "PBPKO"
    """hepatic vein blood flow."""

    HEPATIC_VEIN_BLOOD_FLOW: "PBPKO"
    """hepatic vein blood flow."""

    PBPKO_04045: "PBPKO"
    """blood flow rate to bile."""

    BLOOD_FLOW_RATE_TO_BILE: "PBPKO"
    """blood flow rate to bile."""

    PBPKO_04046: "PBPKO"
    """diameter of intestinal."""

    DIAMETER_OF_INTESTINAL: "PBPKO"
    """diameter of intestinal."""

    PBPKO_04047: "PBPKO"
    """diameter of the jejunum lumen."""

    DIAMETER_OF_THE_JEJUNUM_LUMEN: "PBPKO"
    """diameter of the jejunum lumen."""

    PBPKO_04048: "PBPKO"
    """diameter of the ileum lumen."""

    DIAMETER_OF_THE_ILEUM_LUMEN: "PBPKO"
    """diameter of the ileum lumen."""

    PBPKO_04049: "PBPKO"
    """diameter of the large intestine lumen."""

    DIAMETER_OF_THE_LARGE_INTESTINE_LUMEN: "PBPKO"
    """diameter of the large intestine lumen."""

    PBPKO_04050: "PBPKO"
    """surface area  of the jejunum lumen."""

    SURFACE_AREA__OF_THE_JEJUNUM_LUMEN: "PBPKO"
    """surface area  of the jejunum lumen."""

    PBPKO_04051: "PBPKO"
    """surface area of the ileum lumen."""

    SURFACE_AREA_OF_THE_ILEUM_LUMEN: "PBPKO"
    """surface area of the ileum lumen."""

    PBPKO_04052: "PBPKO"
    """surface area of the large intestine lumen."""

    SURFACE_AREA_OF_THE_LARGE_INTESTINE_LUMEN: "PBPKO"
    """surface area of the large intestine lumen."""

    PBPKO_04053: "PBPKO"
    """uptake fraction to blood."""

    UPTAKE_FRACTION_TO_BLOOD: "PBPKO"
    """uptake fraction to blood."""

    PBPKO_04054: "PBPKO"
    """fraction of bile in small intestine."""

    FRACTION_OF_BILE_IN_SMALL_INTESTINE: "PBPKO"
    """fraction of bile in small intestine."""

    PBPKO_04055: "PBPKO"
    """fraction of bile in liver."""

    FRACTION_OF_BILE_IN_LIVER: "PBPKO"
    """fraction of bile in liver."""

    PBPKO_04056: "PBPKO"
    """fraction of feces."""

    FRACTION_OF_FECES: "PBPKO"
    """fraction of feces."""

    PBPKO_04057: "PBPKO"
    """volume fraction of blood."""

    VOLUME_FRACTION_OF_BLOOD: "PBPKO"
    """volume fraction of blood."""

    PBPKO_04058: "PBPKO"
    """volume fraction of red blood cells."""

    VOLUME_FRACTION_OF_RED_BLOOD_CELLS: "PBPKO"
    """volume fraction of red blood cells."""

    PBPKO_04059: "PBPKO"
    """skin area."""

    SKIN_AREA: "PBPKO"
    """skin area."""

    PBPKO_04060: "PBPKO"
    """thickness epidermis."""

    THICKNESS_EPIDERMIS: "PBPKO"
    """thickness epidermis."""

    PBPKO_04061: "PBPKO"
    """volume of exposed viable epidermis."""

    VOLUME_OF_EXPOSED_VIABLE_EPIDERMIS: "PBPKO"
    """volume of exposed viable epidermis."""

    PBPKO_04062: "PBPKO"
    """volume of follicle."""

    VOLUME_OF_FOLLICLE: "PBPKO"
    """volume of follicle."""

    PBPKO_04063: "PBPKO"
    """area of exposed skin."""

    AREA_OF_EXPOSED_SKIN: "PBPKO"
    """area of exposed skin."""

    PBPKO_04064: "PBPKO"
    """volume of serum."""

    VOLUME_OF_SERUM: "PBPKO"
    """volume of serum."""

    PBPKO_04065: "PBPKO"
    """volume of adrenals."""

    VOLUME_OF_ADRENALS: "PBPKO"
    """volume of adrenals."""

    PBPKO_04066: "PBPKO"
    """volume of breast."""

    VOLUME_OF_BREAST: "PBPKO"
    """volume of breast."""

    PBPKO_04067: "PBPKO"
    """volume of thyroid."""

    VOLUME_OF_THYROID: "PBPKO"
    """volume of thyroid."""

    PBPKO_04068: "PBPKO"
    """volume of intestinal lumen."""

    VOLUME_OF_INTESTINAL_LUMEN: "PBPKO"
    """volume of intestinal lumen."""

    PBPKO_04069: "PBPKO"
    """volume of small intestinal lumen."""

    VOLUME_OF_SMALL_INTESTINAL_LUMEN: "PBPKO"
    """volume of small intestinal lumen."""

    PBPKO_04070: "PBPKO"
    """volume of large intestinal lumen."""

    VOLUME_OF_LARGE_INTESTINAL_LUMEN: "PBPKO"
    """volume of large intestinal lumen."""

    PBPKO_04071: "PBPKO"
    """volume of stomach lumen."""

    VOLUME_OF_STOMACH_LUMEN: "PBPKO"
    """volume of stomach lumen."""

    PBPKO_04072: "PBPKO"
    """volume of gut intestinal tract."""

    VOLUME_OF_GUT_INTESTINAL_TRACT: "PBPKO"
    """volume of gut intestinal tract."""

    PBPKO_04073: "PBPKO"
    """volume of testis."""

    VOLUME_OF_TESTIS: "PBPKO"
    """volume of testis."""

    PBPKO_04074: "PBPKO"
    """volume of uterus."""

    VOLUME_OF_UTERUS: "PBPKO"
    """volume of uterus."""

    PBPKO_04075: "PBPKO"
    """volume of skeleton."""

    VOLUME_OF_SKELETON: "PBPKO"
    """volume of skeleton."""

    PBPKO_04076: "PBPKO"
    """volume of hair."""

    VOLUME_OF_HAIR: "PBPKO"
    """volume of hair."""

    PBPKO_04077: "PBPKO"
    """volume of urinary tract."""

    VOLUME_OF_URINARY_TRACT: "PBPKO"
    """volume of urinary tract."""

    PBPKO_04078: "PBPKO"
    """volume of skin surface depot."""

    VOLUME_OF_SKIN_SURFACE_DEPOT: "PBPKO"
    """volume of skin surface depot."""

    PBPKO_04079: "PBPKO"
    """volume of cortical bone."""

    VOLUME_OF_CORTICAL_BONE: "PBPKO"
    """volume of cortical bone."""

    PBPKO_04080: "PBPKO"
    """volume of trabecular bone."""

    VOLUME_OF_TRABECULAR_BONE: "PBPKO"
    """volume of trabecular bone."""

    PBPKO_04081: "PBPKO"
    """volume of alveolar compartment."""

    VOLUME_OF_ALVEOLAR_COMPARTMENT: "PBPKO"
    """volume of alveolar compartment."""

    PBPKO_04082: "PBPKO"
    """fraction of serum."""

    FRACTION_OF_SERUM: "PBPKO"
    """fraction of serum."""

    PBPKO_04083: "PBPKO"
    """fraction of adrenals."""

    FRACTION_OF_ADRENALS: "PBPKO"
    """fraction of adrenals."""

    PBPKO_04084: "PBPKO"
    """fraction of breast."""

    FRACTION_OF_BREAST: "PBPKO"
    """fraction of breast."""

    PBPKO_04085: "PBPKO"
    """fraction of thyroid."""

    FRACTION_OF_THYROID: "PBPKO"
    """fraction of thyroid."""

    PBPKO_04086: "PBPKO"
    """fraction of intestinal lumen."""

    FRACTION_OF_INTESTINAL_LUMEN: "PBPKO"
    """fraction of intestinal lumen."""

    PBPKO_04087: "PBPKO"
    """fraction of small intestinal lumen."""

    FRACTION_OF_SMALL_INTESTINAL_LUMEN: "PBPKO"
    """fraction of small intestinal lumen."""

    PBPKO_04088: "PBPKO"
    """fraction of large intestinal lumen."""

    FRACTION_OF_LARGE_INTESTINAL_LUMEN: "PBPKO"
    """fraction of large intestinal lumen."""

    PBPKO_04089: "PBPKO"
    """fraction of stomach lumen."""

    FRACTION_OF_STOMACH_LUMEN: "PBPKO"
    """fraction of stomach lumen."""

    PBPKO_04090: "PBPKO"
    """fraction of gut intestinal tract."""

    FRACTION_OF_GUT_INTESTINAL_TRACT: "PBPKO"
    """fraction of gut intestinal tract."""

    PBPKO_04091: "PBPKO"
    """fraction of testis."""

    FRACTION_OF_TESTIS: "PBPKO"
    """fraction of testis."""

    PBPKO_04092: "PBPKO"
    """fraction of uterus."""

    FRACTION_OF_UTERUS: "PBPKO"
    """fraction of uterus."""

    PBPKO_04093: "PBPKO"
    """fraction of skeleton."""

    FRACTION_OF_SKELETON: "PBPKO"
    """fraction of skeleton."""

    PBPKO_04094: "PBPKO"
    """fraction of hair."""

    FRACTION_OF_HAIR: "PBPKO"
    """fraction of hair."""

    PBPKO_04095: "PBPKO"
    """fraction of amniotic fluid."""

    FRACTION_OF_AMNIOTIC_FLUID: "PBPKO"
    """fraction of amniotic fluid."""

    PBPKO_04096: "PBPKO"
    """fraction of urinary tract."""

    FRACTION_OF_URINARY_TRACT: "PBPKO"
    """fraction of urinary tract."""

    PBPKO_04097: "PBPKO"
    """fraction of cortical bone."""

    FRACTION_OF_CORTICAL_BONE: "PBPKO"
    """fraction of cortical bone."""

    PBPKO_04098: "PBPKO"
    """fraction of trabecular bone."""

    FRACTION_OF_TRABECULAR_BONE: "PBPKO"
    """fraction of trabecular bone."""

    PBPKO_04099: "PBPKO"
    """fraction of the skin surface depot."""

    FRACTION_OF_THE_SKIN_SURFACE_DEPOT: "PBPKO"
    """fraction of the skin surface depot."""

    PBPKO_04100: "PBPKO"
    """fraction of blood: A dimensionless fraction of volume defined as the blood volume divided per unit of total body weight."""

    FRACTION_OF_BLOOD: "PBPKO"
    """fraction of blood: A dimensionless fraction of volume defined as the blood volume divided per unit of total body weight."""

    PBPKO_04101: "PBPKO"
    """fraction of bone marrow: A dimensionless fraction of volume defined as the bone marrow volume divided per unit of total body weight."""

    FRACTION_OF_BONE_MARROW: "PBPKO"
    """fraction of bone marrow: A dimensionless fraction of volume defined as the bone marrow volume divided per unit of total body weight."""

    PBPKO_04102: "PBPKO"
    """fraction of bone non perfused: A dimensionless fraction of volume defined as the bone non perfuse volume divided per unit of total body weight."""

    FRACTION_OF_BONE_NON_PERFUSED: "PBPKO"
    """fraction of bone non perfused: A dimensionless fraction of volume defined as the bone non perfuse volume divided per unit of total body weight."""

    PBPKO_04103: "PBPKO"
    """fraction of adipose mass: A dimensionless fraction of volume defined as the adipose mass volume divided per unit of total body weight."""

    FRACTION_OF_ADIPOSE_MASS: "PBPKO"
    """fraction of adipose mass: A dimensionless fraction of volume defined as the adipose mass volume divided per unit of total body weight."""

    PBPKO_04104: "PBPKO"
    """fraction of intestinal tissue: A dimensionless fraction of volume defined as the intestinal tissue volume divided per unit of total body weight."""

    FRACTION_OF_INTESTINAL_TISSUE: "PBPKO"
    """fraction of intestinal tissue: A dimensionless fraction of volume defined as the intestinal tissue volume divided per unit of total body weight."""

    PBPKO_04105: "PBPKO"
    """volume of kidney rest tissue: A volume parameter representing the total volume of the kidney rest tissue compartment."""

    VOLUME_OF_KIDNEY_REST_TISSUE: "PBPKO"
    """volume of kidney rest tissue: A volume parameter representing the total volume of the kidney rest tissue compartment."""

    PBPKO_04106: "PBPKO"
    """volume of kidney rest lumen: A volume parameter representing the total volume of the kidney rest lumen compartment."""

    VOLUME_OF_KIDNEY_REST_LUMEN: "PBPKO"
    """volume of kidney rest lumen: A volume parameter representing the total volume of the kidney rest lumen compartment."""

    PBPKO_04107: "PBPKO"
    """volume of kidney proximal tubule lumen: A volume parameter representing the total volume of the lumen of kidney proximal tubule compartment."""

    VOLUME_OF_KIDNEY_PROXIMAL_TUBULE_LUMEN: "PBPKO"
    """volume of kidney proximal tubule lumen: A volume parameter representing the total volume of the lumen of kidney proximal tubule compartment."""

    PBPKO_04108: "PBPKO"
    """volume of kidney proximal tubule tissue: A volume parameter representing the total volume of the tissue of kidney proximal tubule compartment."""

    VOLUME_OF_KIDNEY_PROXIMAL_TUBULE_TISSUE: "PBPKO"
    """volume of kidney proximal tubule tissue: A volume parameter representing the total volume of the tissue of kidney proximal tubule compartment."""

    PBPKO_04109: "PBPKO"
    """volume of liver extracellular: A volume parameter representing the total volume of the vascular and interstitial spaces of liver compartment."""

    VOLUME_OF_LIVER_EXTRACELLULAR: "PBPKO"
    """volume of liver extracellular: A volume parameter representing the total volume of the vascular and interstitial spaces of liver compartment."""

    PBPKO_04110: "PBPKO"
    """volume of liver intracellular space: A volume parameter representing the total volume of the hepatocytes in liver compartment."""

    VOLUME_OF_LIVER_INTRACELLULAR_SPACE: "PBPKO"
    """volume of liver intracellular space: A volume parameter representing the total volume of the hepatocytes in liver compartment."""

    PBPKO_04111: "PBPKO"
    """volume of intestine tissue: A volume parameter representing the total volume of the tissue of intestine compartment."""

    VOLUME_OF_INTESTINE_TISSUE: "PBPKO"
    """volume of intestine tissue: A volume parameter representing the total volume of the tissue of intestine compartment."""

    PBPKO_05001: "PBPKO"
    """molar volume: A physicochemical parameter representing the volume of one mole of a molecule."""

    MOLAR_VOLUME: "PBPKO"
    """molar volume: A physicochemical parameter representing the volume of one mole of a molecule."""

    PBPKO_05002: "PBPKO"
    """Henry's law constant: A physicochemical parameter describing the volatily of a compound"""

    HENRY_S_LAW_CONSTANT: "PBPKO"
    """Henry's law constant: A physicochemical parameter describing the volatily of a compound"""

    PBPKO_05003: "PBPKO"
    """vapor pressure: A physicochemical parameter describing the vapor pressure of the compound"""

    VAPOR_PRESSURE: "PBPKO"
    """vapor pressure: A physicochemical parameter describing the vapor pressure of the compound"""

    PBPKO_06002: "PBPKO"
    """unbound venous concentration of compound in compartment."""

    UNBOUND_VENOUS_CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT: "PBPKO"
    """unbound venous concentration of compound in compartment."""

    PBPKO_06003: "PBPKO"
    """unbound concentration of compund in compartment."""

    UNBOUND_CONCENTRATION_OF_COMPUND_IN_COMPARTMENT: "PBPKO"
    """unbound concentration of compund in compartment."""

    PBPKO_06004: "PBPKO"
    """amount in stomach: The amount of chemical in stomach compartment."""

    AMOUNT_IN_STOMACH: "PBPKO"
    """amount in stomach: The amount of chemical in stomach compartment."""

    PBPKO_06005: "PBPKO"
    """amount in small intestine: The amount of chemical in small intestine compartment"""

    AMOUNT_IN_SMALL_INTESTINE: "PBPKO"
    """amount in small intestine: The amount of chemical in small intestine compartment"""

    PBPKO_06006: "PBPKO"
    """amount in jejunum: The amount of chemical in jejunum compartment."""

    AMOUNT_IN_JEJUNUM: "PBPKO"
    """amount in jejunum: The amount of chemical in jejunum compartment."""

    PBPKO_06007: "PBPKO"
    """amount in ileum: The amount of chemical in ileum compartment."""

    AMOUNT_IN_ILEUM: "PBPKO"
    """amount in ileum: The amount of chemical in ileum compartment."""

    PBPKO_06008: "PBPKO"
    """amount in  large intestine: The amount of chemical in large intestine compartment."""

    AMOUNT_IN__LARGE_INTESTINE: "PBPKO"
    """amount in  large intestine: The amount of chemical in large intestine compartment."""

    PBPKO_06009: "PBPKO"
    """amount in lumen: The amount of chemical in lumen of the intestine."""

    AMOUNT_IN_LUMEN: "PBPKO"
    """amount in lumen: The amount of chemical in lumen of the intestine."""

    PBPKO_06010: "PBPKO"
    """amount in small intestine segment: The amount of chemical in segment of small intestine."""

    AMOUNT_IN_SMALL_INTESTINE_SEGMENT: "PBPKO"
    """amount in small intestine segment: The amount of chemical in segment of small intestine."""

    PBPKO_06011: "PBPKO"
    """amount in colon: The amount of chemical in colon compartment."""

    AMOUNT_IN_COLON: "PBPKO"
    """amount in colon: The amount of chemical in colon compartment."""

    PBPKO_06012: "PBPKO"
    """amount in bile: The amount of chemical in bile."""

    AMOUNT_IN_BILE: "PBPKO"
    """amount in bile: The amount of chemical in bile."""

    PBPKO_06013: "PBPKO"
    """amount in spleen: The amount of chemical in spleen compartment"""

    AMOUNT_IN_SPLEEN: "PBPKO"
    """amount in spleen: The amount of chemical in spleen compartment"""

    PBPKO_06014: "PBPKO"
    """amount in duodenum: The amount of chemical in duodenum compartment."""

    AMOUNT_IN_DUODENUM: "PBPKO"
    """amount in duodenum: The amount of chemical in duodenum compartment."""

    PBPKO_06015: "PBPKO"
    """amount in intestinal tissue: The amount of chemical in intestinal tissue"""

    AMOUNT_IN_INTESTINAL_TISSUE: "PBPKO"
    """amount in intestinal tissue: The amount of chemical in intestinal tissue"""

    PBPKO_06016: "PBPKO"
    """amount in portal vein: The amount of chemical in portal vein."""

    AMOUNT_IN_PORTAL_VEIN: "PBPKO"
    """amount in portal vein: The amount of chemical in portal vein."""

    PBPKO_06017: "PBPKO"
    """unbound concentration in plasma: The unbound concentration of compound in the plasma compartment."""

    UNBOUND_CONCENTRATION_IN_PLASMA: "PBPKO"
    """unbound concentration in plasma: The unbound concentration of compound in the plasma compartment."""

    PBPKO_06018: "PBPKO"
    """unbound venous liver concentration: The unbound venous concentration of compound in the liver compartment."""

    UNBOUND_VENOUS_LIVER_CONCENTRATION: "PBPKO"
    """unbound venous liver concentration: The unbound venous concentration of compound in the liver compartment."""

    PBPKO_06019: "PBPKO"
    """unbound venous gut concentration: The unbound venous concentration of compound in the gut compartment."""

    UNBOUND_VENOUS_GUT_CONCENTRATION: "PBPKO"
    """unbound venous gut concentration: The unbound venous concentration of compound in the gut compartment."""

    PBPKO_06020: "PBPKO"
    """unbound venous brain concentration: The unbound venous concentration of compound in the brain compartment."""

    UNBOUND_VENOUS_BRAIN_CONCENTRATION: "PBPKO"
    """unbound venous brain concentration: The unbound venous concentration of compound in the brain compartment."""

    PBPKO_06021: "PBPKO"
    """unbound venous kidney concentration: The unbound venous concentration of compound in the kidney compartment."""

    UNBOUND_VENOUS_KIDNEY_CONCENTRATION: "PBPKO"
    """unbound venous kidney concentration: The unbound venous concentration of compound in the kidney compartment."""

    PBPKO_06022: "PBPKO"
    """unbound venous filtrate concentration: The unbound venous concentration of compound in the filtrate compartment."""

    UNBOUND_VENOUS_FILTRATE_CONCENTRATION: "PBPKO"
    """unbound venous filtrate concentration: The unbound venous concentration of compound in the filtrate compartment."""

    PBPKO_06023: "PBPKO"
    """unbound venous lung concentration: The unbound venous concentration of compound in the lung compartment."""

    UNBOUND_VENOUS_LUNG_CONCENTRATION: "PBPKO"
    """unbound venous lung concentration: The unbound venous concentration of compound in the lung compartment."""

    PBPKO_06024: "PBPKO"
    """unbound venous fat concentration: The unbound venous concentration of compound in the fat compartment."""

    UNBOUND_VENOUS_FAT_CONCENTRATION: "PBPKO"
    """unbound venous fat concentration: The unbound venous concentration of compound in the fat compartment."""

    PBPKO_06025: "PBPKO"
    """unbound venous bone marrow concentration: The unbound venous concentration of compound in the bone marrow compartment."""

    UNBOUND_VENOUS_BONE_MARROW_CONCENTRATION: "PBPKO"
    """unbound venous bone marrow concentration: The unbound venous concentration of compound in the bone marrow compartment."""

    PBPKO_06026: "PBPKO"
    """unbound venous skin concentration: The unbound venous concentration of compound in the skin compartment."""

    UNBOUND_VENOUS_SKIN_CONCENTRATION: "PBPKO"
    """unbound venous skin concentration: The unbound venous concentration of compound in the skin compartment."""

    PBPKO_06027: "PBPKO"
    """unbound venous mammary gland concentration: The unbound venous concentration of compound in the mammary gland compartment."""

    UNBOUND_VENOUS_MAMMARY_GLAND_CONCENTRATION: "PBPKO"
    """unbound venous mammary gland concentration: The unbound venous concentration of compound in the mammary gland compartment."""

    PBPKO_06028: "PBPKO"
    """unbound venous rest body concentration: The unbound venous concentration of compound in the rest body compartment."""

    UNBOUND_VENOUS_REST_BODY_CONCENTRATION: "PBPKO"
    """unbound venous rest body concentration: The unbound venous concentration of compound in the rest body compartment."""

    PBPKO_06029: "PBPKO"
    """total venous concentration of compound in compartment."""

    TOTAL_VENOUS_CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT: "PBPKO"
    """total venous concentration of compound in compartment."""

    PBPKO_06030: "PBPKO"
    """total venous liver concentration: The total venous concentration of compound in the liver compartment."""

    TOTAL_VENOUS_LIVER_CONCENTRATION: "PBPKO"
    """total venous liver concentration: The total venous concentration of compound in the liver compartment."""

    PBPKO_06031: "PBPKO"
    """total venous gut concentration: The total venous concentration of compound in the gut compartment."""

    TOTAL_VENOUS_GUT_CONCENTRATION: "PBPKO"
    """total venous gut concentration: The total venous concentration of compound in the gut compartment."""

    PBPKO_06032: "PBPKO"
    """total venous kidney concentration: The total venous concentration of compound in the kidney compartment."""

    TOTAL_VENOUS_KIDNEY_CONCENTRATION: "PBPKO"
    """total venous kidney concentration: The total venous concentration of compound in the kidney compartment."""

    PBPKO_06033: "PBPKO"
    """total venous brain concentration: The total venous concentration of compound in the brain compartment."""

    TOTAL_VENOUS_BRAIN_CONCENTRATION: "PBPKO"
    """total venous brain concentration: The total venous concentration of compound in the brain compartment."""

    PBPKO_06034: "PBPKO"
    """total venous filtrate concentration: The total venous concentration of compound in the filtrate compartment."""

    TOTAL_VENOUS_FILTRATE_CONCENTRATION: "PBPKO"
    """total venous filtrate concentration: The total venous concentration of compound in the filtrate compartment."""

    PBPKO_06035: "PBPKO"
    """total venous lung concentration: The total venous concentration of compound in the lung compartment."""

    TOTAL_VENOUS_LUNG_CONCENTRATION: "PBPKO"
    """total venous lung concentration: The total venous concentration of compound in the lung compartment."""

    PBPKO_06036: "PBPKO"
    """total venous fat concentration: The total venous concentration of compound in the fat compartment."""

    TOTAL_VENOUS_FAT_CONCENTRATION: "PBPKO"
    """total venous fat concentration: The total venous concentration of compound in the fat compartment."""

    PBPKO_06037: "PBPKO"
    """total venous bone marrow concentration: The total venous concentration of compound in the bone marrow compartment."""

    TOTAL_VENOUS_BONE_MARROW_CONCENTRATION: "PBPKO"
    """total venous bone marrow concentration: The total venous concentration of compound in the bone marrow compartment."""

    PBPKO_06038: "PBPKO"
    """total venous skin concentration: The total venous concentration of compound in the skin compartment."""

    TOTAL_VENOUS_SKIN_CONCENTRATION: "PBPKO"
    """total venous skin concentration: The total venous concentration of compound in the skin compartment."""

    PBPKO_06039: "PBPKO"
    """total venous mammary gland concentration: The total venous concentration of compound in the mammary gland compartment."""

    TOTAL_VENOUS_MAMMARY_GLAND_CONCENTRATION: "PBPKO"
    """total venous mammary gland concentration: The total venous concentration of compound in the mammary gland compartment."""

    PBPKO_06040: "PBPKO"
    """total venous rest body concentration: The total venous concentration of compound in the rest of the body compartment."""

    TOTAL_VENOUS_REST_BODY_CONCENTRATION: "PBPKO"
    """total venous rest body concentration: The total venous concentration of compound in the rest of the body compartment."""

    PBPKO_06041: "PBPKO"
    """concentration in stomach: The concentration of chemical in stomach compartment."""

    CONCENTRATION_IN_STOMACH: "PBPKO"
    """concentration in stomach: The concentration of chemical in stomach compartment."""

    PBPKO_06042: "PBPKO"
    """concentration in small intestine: The concentration of chemical in small intestine compartment."""

    CONCENTRATION_IN_SMALL_INTESTINE: "PBPKO"
    """concentration in small intestine: The concentration of chemical in small intestine compartment."""

    PBPKO_06043: "PBPKO"
    """concentration in jejunum: The concentration of chemical in jejunum compartment."""

    CONCENTRATION_IN_JEJUNUM: "PBPKO"
    """concentration in jejunum: The concentration of chemical in jejunum compartment."""

    PBPKO_06044: "PBPKO"
    """concentration in ileum: The concentration of chemical in ileum compartment."""

    CONCENTRATION_IN_ILEUM: "PBPKO"
    """concentration in ileum: The concentration of chemical in ileum compartment."""

    PBPKO_06045: "PBPKO"
    """concentration in large intestine: The concentration of chemical in large intestine compartment."""

    CONCENTRATION_IN_LARGE_INTESTINE: "PBPKO"
    """concentration in large intestine: The concentration of chemical in large intestine compartment."""

    PBPKO_06046: "PBPKO"
    """concentration in intestinal tissue: The concentration of chemical in tissue of intestine."""

    CONCENTRATION_IN_INTESTINAL_TISSUE: "PBPKO"
    """concentration in intestinal tissue: The concentration of chemical in tissue of intestine."""

    PBPKO_06047: "PBPKO"
    """concentration in lumen: The concentration of chemical in lumen of intestine."""

    CONCENTRATION_IN_LUMEN: "PBPKO"
    """concentration in lumen: The concentration of chemical in lumen of intestine."""

    PBPKO_06048: "PBPKO"
    """concentration in bile: The concentration of chemical in bile."""

    CONCENTRATION_IN_BILE: "PBPKO"
    """concentration in bile: The concentration of chemical in bile."""

    PBPKO_06049: "PBPKO"
    """concentration in spleen: The concentration of chemical in spleen compartment."""

    CONCENTRATION_IN_SPLEEN: "PBPKO"
    """concentration in spleen: The concentration of chemical in spleen compartment."""

    PBPKO_06050: "PBPKO"
    """concentration in feces: The concentration of chemical in feces."""

    CONCENTRATION_IN_FECES: "PBPKO"
    """concentration in feces: The concentration of chemical in feces."""

    PBPKO_06051: "PBPKO"
    """amount in skin surface depot."""

    AMOUNT_IN_SKIN_SURFACE_DEPOT: "PBPKO"
    """amount in skin surface depot."""

    PBPKO_06052: "PBPKO"
    """maximum amount: The maximum amount of chemical in a compartment"""

    MAXIMUM_AMOUNT: "PBPKO"
    """maximum amount: The maximum amount of chemical in a compartment"""

    PBPKO_06053: "PBPKO"
    """amount in follicles."""

    AMOUNT_IN_FOLLICLES: "PBPKO"
    """amount in follicles."""

    PBPKO_06054: "PBPKO"
    """concentration in medium."""

    CONCENTRATION_IN_MEDIUM: "PBPKO"
    """concentration in medium."""

    PBPKO_06055: "PBPKO"
    """concentration in cell."""

    CONCENTRATION_IN_CELL: "PBPKO"
    """concentration in cell."""

    PBPKO_06056: "PBPKO"
    """concentration in mitochondria."""

    CONCENTRATION_IN_MITOCHONDRIA: "PBPKO"
    """concentration in mitochondria."""

    PBPKO_06057: "PBPKO"
    """concentration in lysosomes."""

    CONCENTRATION_IN_LYSOSOMES: "PBPKO"
    """concentration in lysosomes."""

    PBPKO_06058: "PBPKO"
    """concentration in microsomes."""

    CONCENTRATION_IN_MICROSOMES: "PBPKO"
    """concentration in microsomes."""

    PBPKO_06059: "PBPKO"
    """concentration in intracellular water."""

    CONCENTRATION_IN_INTRACELLULAR_WATER: "PBPKO"
    """concentration in intracellular water."""

    PBPKO_06060: "PBPKO"
    """concentration in polymer."""

    CONCENTRATION_IN_POLYMER: "PBPKO"
    """concentration in polymer."""

    PBPKO_06061: "PBPKO"
    """concentration in air."""

    CONCENTRATION_IN_AIR: "PBPKO"
    """concentration in air."""

    PBPKO_06062: "PBPKO"
    """amount in menstrual: The amount of compound in the menstrual compartment."""

    AMOUNT_IN_MENSTRUAL: "PBPKO"
    """amount in menstrual: The amount of compound in the menstrual compartment."""

    PBPKO_06063: "PBPKO"
    """amount in kidney rest tissue: The amount of compound in the kidney rest tissue compartment."""

    AMOUNT_IN_KIDNEY_REST_TISSUE: "PBPKO"
    """amount in kidney rest tissue: The amount of compound in the kidney rest tissue compartment."""

    PBPKO_06064: "PBPKO"
    """amount in kidney rest lumen: The amount of compound in the rest of kidney lumen compartment."""

    AMOUNT_IN_KIDNEY_REST_LUMEN: "PBPKO"
    """amount in kidney rest lumen: The amount of compound in the rest of kidney lumen compartment."""

    PBPKO_06065: "PBPKO"
    """amount in kidney proximal tubule tissue: The amount of compound in the proximal tubule tissue of kidney compartment."""

    AMOUNT_IN_KIDNEY_PROXIMAL_TUBULE_TISSUE: "PBPKO"
    """amount in kidney proximal tubule tissue: The amount of compound in the proximal tubule tissue of kidney compartment."""

    PBPKO_06066: "PBPKO"
    """amount in kidney proximal tubule lumen: The amount of compound in the proximal tubule lumen of kidney compartment."""

    AMOUNT_IN_KIDNEY_PROXIMAL_TUBULE_LUMEN: "PBPKO"
    """amount in kidney proximal tubule lumen: The amount of compound in the proximal tubule lumen of kidney compartment."""

    PBPKO_06067: "PBPKO"
    """amount in liver intracellular: The amount of compound in the intracellular spaceof liver compartment."""

    AMOUNT_IN_LIVER_INTRACELLULAR: "PBPKO"
    """amount in liver intracellular: The amount of compound in the intracellular spaceof liver compartment."""

    PBPKO_06068: "PBPKO"
    """amount in liver extracellular: The amount of compound in the extracellular space of liver compartment."""

    AMOUNT_IN_LIVER_EXTRACELLULAR: "PBPKO"
    """amount in liver extracellular: The amount of compound in the extracellular space of liver compartment."""

    PBPKO_07001: "PBPKO"
    """invitro pbpk."""

    INVITRO_PBPK: "PBPKO"
    """invitro pbpk."""

    PR_000000001: "PBPKO"
    """protein: An amino acid chain that is produced de novo by ribosome-mediated translation of a genetically-encoded mRNA, and any derivatives thereof."""

    PROTEIN: "PBPKO"
    """protein: An amino acid chain that is produced de novo by ribosome-mediated translation of a genetically-encoded mRNA, and any derivatives thereof."""

    PR_000018263: "PBPKO"
    """amino acid chain: An organic amino compound that consists of amino acid residues (unmodified amino-acid residues and/or modified amino-acid residues) linked by peptide bonds or derivatives of such bonds."""

    AMINO_ACID_CHAIN: "PBPKO"
    """amino acid chain: An organic amino compound that consists of amino acid residues (unmodified amino-acid residues and/or modified amino-acid residues) linked by peptide bonds or derivatives of such bonds."""

    RO_0000052: "PBPKO"
    """characteristic of: a relation between a specifically dependent continuant (the characteristic) and any other entity (the bearer), in which the characteristic depends on the bearer for its existence."""

    CHARACTERISTIC_OF: "PBPKO"
    """characteristic of: a relation between a specifically dependent continuant (the characteristic) and any other entity (the bearer), in which the characteristic depends on the bearer for its existence."""

    RO_0000053: "PBPKO"
    """has characteristic: Inverse of characteristic_of"""

    HAS_CHARACTERISTIC: "PBPKO"
    """has characteristic: Inverse of characteristic_of"""

    RO_0000056: "PBPKO"
    """participates in: a relation between a continuant and a process, in which the continuant is somehow involved in the process"""

    PARTICIPATES_IN: "PBPKO"
    """participates in: a relation between a continuant and a process, in which the continuant is somehow involved in the process"""

    RO_0000057: "PBPKO"
    """has participant: a relation between a process and a continuant, in which the continuant is somehow involved in the process"""

    HAS_PARTICIPANT: "PBPKO"
    """has participant: a relation between a process and a continuant, in which the continuant is somehow involved in the process"""

    RO_0000059: "PBPKO"
    """concretizes: A relationship between a specifically dependent continuant and a generically dependent continuant, in which the generically dependent continuant depends on some independent continuant in virtue of the fact that the specifically dependent continuant also depends on that same independent continuant. Multiple specifically dependent continuants can concretize the same generically dependent continuant."""

    CONCRETIZES: "PBPKO"
    """concretizes: A relationship between a specifically dependent continuant and a generically dependent continuant, in which the generically dependent continuant depends on some independent continuant in virtue of the fact that the specifically dependent continuant also depends on that same independent continuant. Multiple specifically dependent continuants can concretize the same generically dependent continuant."""

    RO_0000079: "PBPKO"
    """function of: a relation between a function and an independent continuant (the bearer), in which the function specifically depends on the bearer for its existence"""

    FUNCTION_OF: "PBPKO"
    """function of: a relation between a function and an independent continuant (the bearer), in which the function specifically depends on the bearer for its existence"""

    RO_0000080: "PBPKO"
    """quality of: a relation between a quality and an independent continuant (the bearer), in which the quality specifically depends on the bearer for its existence"""

    QUALITY_OF: "PBPKO"
    """quality of: a relation between a quality and an independent continuant (the bearer), in which the quality specifically depends on the bearer for its existence"""

    RO_0000081: "PBPKO"
    """role of: a relation between a role and an independent continuant (the bearer), in which the role specifically depends on the bearer for its existence"""

    ROLE_OF: "PBPKO"
    """role of: a relation between a role and an independent continuant (the bearer), in which the role specifically depends on the bearer for its existence"""

    RO_0000085: "PBPKO"
    """has function: a relation between an independent continuant (the bearer) and a function, in which the function specifically depends on the bearer for its existence"""

    HAS_FUNCTION: "PBPKO"
    """has function: a relation between an independent continuant (the bearer) and a function, in which the function specifically depends on the bearer for its existence"""

    RO_0000086: "PBPKO"
    """has quality: a relation between an independent continuant (the bearer) and a quality, in which the quality specifically depends on the bearer for its existence"""

    HAS_QUALITY: "PBPKO"
    """has quality: a relation between an independent continuant (the bearer) and a quality, in which the quality specifically depends on the bearer for its existence"""

    RO_0000087: "PBPKO"
    """has role: a relation between an independent continuant (the bearer) and a role, in which the role specifically depends on the bearer for its existence"""

    HAS_ROLE: "PBPKO"
    """has role: a relation between an independent continuant (the bearer) and a role, in which the role specifically depends on the bearer for its existence"""

    RO_0000091: "PBPKO"
    """has disposition: a relation between an independent continuant (the bearer) and a disposition, in which the disposition specifically depends on the bearer for its existence"""

    HAS_DISPOSITION: "PBPKO"
    """has disposition: a relation between an independent continuant (the bearer) and a disposition, in which the disposition specifically depends on the bearer for its existence"""

    RO_0000092: "PBPKO"
    """disposition of: inverse of has disposition"""

    DISPOSITION_OF: "PBPKO"
    """disposition of: inverse of has disposition"""

    RO_0002013: "PBPKO"
    """has regulatory component activity: A 'has regulatory component activity' B if A and B are GO molecular functions (GO_0003674), A has_component B and A is regulated by B."""

    HAS_REGULATORY_COMPONENT_ACTIVITY: "PBPKO"
    """has regulatory component activity: A 'has regulatory component activity' B if A and B are GO molecular functions (GO_0003674), A has_component B and A is regulated by B."""

    RO_0002014: "PBPKO"
    """has negative regulatory component activity: A relationship that holds between a GO molecular function and a component of that molecular function that negatively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is negatively regulated by B."""

    HAS_NEGATIVE_REGULATORY_COMPONENT_ACTIVITY: "PBPKO"
    """has negative regulatory component activity: A relationship that holds between a GO molecular function and a component of that molecular function that negatively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is negatively regulated by B."""

    RO_0002015: "PBPKO"
    """has positive regulatory component activity: A relationship that holds between a GO molecular function and a component of that molecular function that positively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is positively regulated by B."""

    HAS_POSITIVE_REGULATORY_COMPONENT_ACTIVITY: "PBPKO"
    """has positive regulatory component activity: A relationship that holds between a GO molecular function and a component of that molecular function that positively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is positively regulated by B."""

    RO_0002017: "PBPKO"
    """has component activity."""

    HAS_COMPONENT_ACTIVITY: "PBPKO"
    """has component activity."""

    RO_0002018: "PBPKO"
    """has component process: w 'has process component' p if p and w are processes, w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type."""

    HAS_COMPONENT_PROCESS: "PBPKO"
    """has component process: w 'has process component' p if p and w are processes, w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type."""

    RO_0002022: "PBPKO"
    """directly regulated by."""

    DIRECTLY_REGULATED_BY: "PBPKO"
    """directly regulated by."""

    RO_0002023: "PBPKO"
    """directly negatively regulated by."""

    DIRECTLY_NEGATIVELY_REGULATED_BY: "PBPKO"
    """directly negatively regulated by."""

    RO_0002024: "PBPKO"
    """directly positively regulated by."""

    DIRECTLY_POSITIVELY_REGULATED_BY: "PBPKO"
    """directly positively regulated by."""

    RO_0002025: "PBPKO"
    """has effector activity."""

    HAS_EFFECTOR_ACTIVITY: "PBPKO"
    """has effector activity."""

    RO_0002086: "PBPKO"
    """ends after."""

    ENDS_AFTER: "PBPKO"
    """ends after."""

    RO_0002087: "PBPKO"
    """immediately preceded by."""

    IMMEDIATELY_PRECEDED_BY: "PBPKO"
    """immediately preceded by."""

    RO_0002090: "PBPKO"
    """immediately precedes."""

    IMMEDIATELY_PRECEDES: "PBPKO"
    """immediately precedes."""

    RO_0002131: "PBPKO"
    """overlaps: x overlaps y if and only if there exists some z such that x has part z and z part of y"""

    OVERLAPS: "PBPKO"
    """overlaps: x overlaps y if and only if there exists some z such that x has part z and z part of y"""

    RO_0002180: "PBPKO"
    """has component: w 'has component' p if w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type."""

    HAS_COMPONENT: "PBPKO"
    """has component: w 'has component' p if w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type."""

    RO_0002211: "PBPKO"
    """regulates: p regulates q iff p is causally upstream of q, the execution of p is not constant and varies according to specific conditions, and p influences the rate or magnitude of execution of q due to an effect either on some enabler of q or some enabler of a part of q."""

    REGULATES: "PBPKO"
    """regulates: p regulates q iff p is causally upstream of q, the execution of p is not constant and varies according to specific conditions, and p influences the rate or magnitude of execution of q due to an effect either on some enabler of q or some enabler of a part of q."""

    RO_0002212: "PBPKO"
    """negatively regulates: p negatively regulates q iff p regulates q, and p decreases the rate or magnitude of execution of q."""

    NEGATIVELY_REGULATES: "PBPKO"
    """negatively regulates: p negatively regulates q iff p regulates q, and p decreases the rate or magnitude of execution of q."""

    RO_0002213: "PBPKO"
    """positively regulates: p positively regulates q iff p regulates q, and p increases the rate or magnitude of execution of q."""

    POSITIVELY_REGULATES: "PBPKO"
    """positively regulates: p positively regulates q iff p regulates q, and p increases the rate or magnitude of execution of q."""

    RO_0002215: "PBPKO"
    """capable of: A relation between a material entity (such as a cell) and a process, in which the material entity has the ability to carry out the process."""

    CAPABLE_OF: "PBPKO"
    """capable of: A relation between a material entity (such as a cell) and a process, in which the material entity has the ability to carry out the process."""

    RO_0002216: "PBPKO"
    """capable of part of: c stands in this relationship to p if and only if there exists some p' such that c is capable_of p', and p' is part_of p."""

    CAPABLE_OF_PART_OF: "PBPKO"
    """capable of part of: c stands in this relationship to p if and only if there exists some p' such that c is capable_of p', and p' is part_of p."""

    RO_0002222: "PBPKO"
    """temporally related to."""

    TEMPORALLY_RELATED_TO: "PBPKO"
    """temporally related to."""

    RO_0002233: "PBPKO"
    """has input: p has input c iff: p is a process, c is a material entity, c is a participant in p, c is present at the start of p, and the state of c is modified during p."""

    HAS_INPUT: "PBPKO"
    """has input: p has input c iff: p is a process, c is a material entity, c is a participant in p, c is present at the start of p, and the state of c is modified during p."""

    RO_0002263: "PBPKO"
    """acts upstream of: c acts upstream of p if and only if c enables some f that is involved in p' and p' occurs chronologically before p, is not part of p, and affects the execution of p. c is a material entity and f, p, p' are processes."""

    ACTS_UPSTREAM_OF: "PBPKO"
    """acts upstream of: c acts upstream of p if and only if c enables some f that is involved in p' and p' occurs chronologically before p, is not part of p, and affects the execution of p. c is a material entity and f, p, p' are processes."""

    RO_0002264: "PBPKO"
    """acts upstream of or within: c acts upstream of or within p if c is enables f, and f is causally upstream of or within p. c is a material entity and p is an process."""

    ACTS_UPSTREAM_OF_OR_WITHIN: "PBPKO"
    """acts upstream of or within: c acts upstream of or within p if c is enables f, and f is causally upstream of or within p. c is a material entity and p is an process."""

    RO_0002304: "PBPKO"
    """causally upstream of, positive effect: p is causally upstream of, positive effect q iff p is casually upstream of q, and the execution of p is required for the execution of q."""

    CAUSALLY_UPSTREAM_OF__POSITIVE_EFFECT: "PBPKO"
    """causally upstream of, positive effect: p is causally upstream of, positive effect q iff p is casually upstream of q, and the execution of p is required for the execution of q."""

    RO_0002305: "PBPKO"
    """causally upstream of, negative effect: p is causally upstream of, negative effect q iff p is casually upstream of q, and the execution of p decreases the execution of q."""

    CAUSALLY_UPSTREAM_OF__NEGATIVE_EFFECT: "PBPKO"
    """causally upstream of, negative effect: p is causally upstream of, negative effect q iff p is casually upstream of q, and the execution of p decreases the execution of q."""

    RO_0002314: "PBPKO"
    """characteristic of part of: q characteristic of part of w if and only if there exists some p such that q inheres in p and p part of w."""

    CHARACTERISTIC_OF_PART_OF: "PBPKO"
    """characteristic of part of: q characteristic of part of w if and only if there exists some p such that q inheres in p and p part of w."""

    RO_0002323: "PBPKO"
    """mereotopologically related to: A mereological relationship or a topological relationship"""

    MEREOTOPOLOGICALLY_RELATED_TO: "PBPKO"
    """mereotopologically related to: A mereological relationship or a topological relationship"""

    RO_0002327: "PBPKO"
    """enables: c enables p iff c is capable of p and c acts to execute p."""

    ENABLES: "PBPKO"
    """enables: c enables p iff c is capable of p and c acts to execute p."""

    RO_0002328: "PBPKO"
    """functionally related to: A grouping relationship for any relationship directly involving a function, or that holds because of a function of one of the related entities."""

    FUNCTIONALLY_RELATED_TO: "PBPKO"
    """functionally related to: A grouping relationship for any relationship directly involving a function, or that holds because of a function of one of the related entities."""

    RO_0002329: "PBPKO"
    """part of structure that is capable of: this relation holds between c and p when c is part of some c', and c' is capable of p."""

    PART_OF_STRUCTURE_THAT_IS_CAPABLE_OF: "PBPKO"
    """part of structure that is capable of: this relation holds between c and p when c is part of some c', and c' is capable of p."""

    RO_0002331: "PBPKO"
    """involved in: c involved_in p if and only if c enables some process p', and p' is part of p"""

    INVOLVED_IN: "PBPKO"
    """involved in: c involved_in p if and only if c enables some process p', and p' is part of p"""

    RO_0002333: "PBPKO"
    """enabled by: inverse of enables"""

    ENABLED_BY: "PBPKO"
    """enabled by: inverse of enables"""

    RO_0002334: "PBPKO"
    """regulated by: inverse of regulates"""

    REGULATED_BY: "PBPKO"
    """regulated by: inverse of regulates"""

    RO_0002335: "PBPKO"
    """negatively regulated by: inverse of negatively regulates"""

    NEGATIVELY_REGULATED_BY: "PBPKO"
    """negatively regulated by: inverse of negatively regulates"""

    RO_0002336: "PBPKO"
    """positively regulated by: inverse of positively regulates"""

    POSITIVELY_REGULATED_BY: "PBPKO"
    """positively regulated by: inverse of positively regulates"""

    RO_0002351: "PBPKO"
    """has member: has member is a mereological relation between a collection and an item."""

    HAS_MEMBER: "PBPKO"
    """has member: has member is a mereological relation between a collection and an item."""

    RO_0002352: "PBPKO"
    """input of: inverse of has input"""

    INPUT_OF: "PBPKO"
    """input of: inverse of has input"""

    RO_0002404: "PBPKO"
    """causally downstream of: inverse of upstream of"""

    CAUSALLY_DOWNSTREAM_OF: "PBPKO"
    """causally downstream of: inverse of upstream of"""

    RO_0002405: "PBPKO"
    """immediately causally downstream of."""

    IMMEDIATELY_CAUSALLY_DOWNSTREAM_OF: "PBPKO"
    """immediately causally downstream of."""

    RO_0002407: "PBPKO"
    """indirectly positively regulates: p indirectly positively regulates q iff p is indirectly causally upstream of q and p positively regulates q."""

    INDIRECTLY_POSITIVELY_REGULATES: "PBPKO"
    """indirectly positively regulates: p indirectly positively regulates q iff p is indirectly causally upstream of q and p positively regulates q."""

    RO_0002409: "PBPKO"
    """indirectly negatively regulates: p indirectly negatively regulates q iff p is indirectly causally upstream of q and p negatively regulates q."""

    INDIRECTLY_NEGATIVELY_REGULATES: "PBPKO"
    """indirectly negatively regulates: p indirectly negatively regulates q iff p is indirectly causally upstream of q and p negatively regulates q."""

    RO_0002410: "PBPKO"
    """causally related to."""

    CAUSALLY_RELATED_TO: "PBPKO"
    """causally related to."""

    RO_0002411: "PBPKO"
    """causally upstream of: p is causally upstream of q iff p is causally related to q, the end of p precedes the end of q, and p is not an occurrent part of q."""

    CAUSALLY_UPSTREAM_OF: "PBPKO"
    """causally upstream of: p is causally upstream of q iff p is causally related to q, the end of p precedes the end of q, and p is not an occurrent part of q."""

    RO_0002412: "PBPKO"
    """immediately causally upstream of: p is immediately causally upstream of q iff p is causally upstream of q, and the end of p is coincident with the beginning of q."""

    IMMEDIATELY_CAUSALLY_UPSTREAM_OF: "PBPKO"
    """immediately causally upstream of: p is immediately causally upstream of q iff p is causally upstream of q, and the end of p is coincident with the beginning of q."""

    RO_0002418: "PBPKO"
    """causally upstream of or within: p is 'causally upstream or within' q iff p is causally related to q, and the end of p precedes, or is coincident with, the end of q."""

    CAUSALLY_UPSTREAM_OF_OR_WITHIN: "PBPKO"
    """causally upstream of or within: p is 'causally upstream or within' q iff p is causally related to q, and the end of p precedes, or is coincident with, the end of q."""

    RO_0002427: "PBPKO"
    """causally downstream of or within: inverse of causally upstream of or within"""

    CAUSALLY_DOWNSTREAM_OF_OR_WITHIN: "PBPKO"
    """causally downstream of or within: inverse of causally upstream of or within"""

    RO_0002428: "PBPKO"
    """involved in regulation of: c involved in regulation of p if c is involved in some p' and p' regulates some p"""

    INVOLVED_IN_REGULATION_OF: "PBPKO"
    """involved in regulation of: c involved in regulation of p if c is involved in some p' and p' regulates some p"""

    RO_0002429: "PBPKO"
    """involved in positive regulation of: c involved in regulation of p if c is involved in some p' and p' positively regulates some p"""

    INVOLVED_IN_POSITIVE_REGULATION_OF: "PBPKO"
    """involved in positive regulation of: c involved in regulation of p if c is involved in some p' and p' positively regulates some p"""

    RO_0002430: "PBPKO"
    """involved in negative regulation of: c involved in regulation of p if c is involved in some p' and p' negatively regulates some p"""

    INVOLVED_IN_NEGATIVE_REGULATION_OF: "PBPKO"
    """involved in negative regulation of: c involved in regulation of p if c is involved in some p' and p' negatively regulates some p"""

    RO_0002431: "PBPKO"
    """involved in or involved in regulation of: c involved in or regulates p if and only if either (i) c is involved in p or (ii) c is involved in regulation of p"""

    INVOLVED_IN_OR_INVOLVED_IN_REGULATION_OF: "PBPKO"
    """involved in or involved in regulation of: c involved in or regulates p if and only if either (i) c is involved in p or (ii) c is involved in regulation of p"""

    RO_0002434: "PBPKO"
    """interacts with: A relationship that holds between two entities in which the processes executed by the two entities are causally connected."""

    INTERACTS_WITH: "PBPKO"
    """interacts with: A relationship that holds between two entities in which the processes executed by the two entities are causally connected."""

    RO_0002436: "PBPKO"
    """molecularly interacts with: An interaction relationship in which the two partners are molecular entities that directly physically interact with each other for example via a stable binding interaction or a brief interaction during which one modifies the other."""

    MOLECULARLY_INTERACTS_WITH: "PBPKO"
    """molecularly interacts with: An interaction relationship in which the two partners are molecular entities that directly physically interact with each other for example via a stable binding interaction or a brief interaction during which one modifies the other."""

    RO_0002447: "PBPKO"
    """phosphorylates."""

    PHOSPHORYLATES: "PBPKO"
    """phosphorylates."""

    RO_0002448: "PBPKO"
    """directly regulates activity of: The entity A, immediately upstream of the entity B, has an activity that regulates an activity performed by B. For example, A and B may be gene products and binding of B by A regulates the kinase activity of B. A and B can be physically interacting but not necessarily. Immediately upstream means there are no intermediate entity between A and B."""

    DIRECTLY_REGULATES_ACTIVITY_OF: "PBPKO"
    """directly regulates activity of: The entity A, immediately upstream of the entity B, has an activity that regulates an activity performed by B. For example, A and B may be gene products and binding of B by A regulates the kinase activity of B. A and B can be physically interacting but not necessarily. Immediately upstream means there are no intermediate entity between A and B."""

    RO_0002449: "PBPKO"
    """directly negatively regulates activity of: The entity A, immediately upstream of the entity B, has an activity that negatively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A negatively regulates the kinase activity of B."""

    DIRECTLY_NEGATIVELY_REGULATES_ACTIVITY_OF: "PBPKO"
    """directly negatively regulates activity of: The entity A, immediately upstream of the entity B, has an activity that negatively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A negatively regulates the kinase activity of B."""

    RO_0002450: "PBPKO"
    """directly positively regulates activity of: The entity A, immediately upstream of the entity B, has an activity that positively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A positively regulates the kinase activity of B."""

    DIRECTLY_POSITIVELY_REGULATES_ACTIVITY_OF: "PBPKO"
    """directly positively regulates activity of: The entity A, immediately upstream of the entity B, has an activity that positively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A positively regulates the kinase activity of B."""

    RO_0002464: "PBPKO"
    """helper property (not for use in curation)."""

    HELPER_PROPERTY__NOT_FOR_USE_IN_CURATION_: "PBPKO"
    """helper property (not for use in curation)."""

    RO_0002481: "PBPKO"
    """is kinase activity."""

    IS_KINASE_ACTIVITY: "PBPKO"
    """is kinase activity."""

    RO_0002500: "PBPKO"
    """causal agent in process: A relationship between a material entity and a process where the material entity has some causal role that influences the process"""

    CAUSAL_AGENT_IN_PROCESS: "PBPKO"
    """causal agent in process: A relationship between a material entity and a process where the material entity has some causal role that influences the process"""

    RO_0002501: "PBPKO"
    """causal relation between processes: p is causally related to q if and only if p or any part of p and q or any part of q are linked by a chain of events where each event pair is one where the execution of p influences the execution of q. p may be upstream, downstream, part of, or a container of q."""

    CAUSAL_RELATION_BETWEEN_PROCESSES: "PBPKO"
    """causal relation between processes: p is causally related to q if and only if p or any part of p and q or any part of q are linked by a chain of events where each event pair is one where the execution of p influences the execution of q. p may be upstream, downstream, part of, or a container of q."""

    RO_0002502: "PBPKO"
    """depends on."""

    DEPENDS_ON: "PBPKO"
    """depends on."""

    RO_0002506: "PBPKO"
    """causal relation between entities."""

    CAUSAL_RELATION_BETWEEN_ENTITIES: "PBPKO"
    """causal relation between entities."""

    RO_0002559: "PBPKO"
    """causally influenced by."""

    CAUSALLY_INFLUENCED_BY: "PBPKO"
    """causally influenced by."""

    RO_0002563: "PBPKO"
    """interaction relation helper property."""

    INTERACTION_RELATION_HELPER_PROPERTY: "PBPKO"
    """interaction relation helper property."""

    RO_0002564: "PBPKO"
    """molecular interaction relation helper property."""

    MOLECULAR_INTERACTION_RELATION_HELPER_PROPERTY: "PBPKO"
    """molecular interaction relation helper property."""

    RO_0002566: "PBPKO"
    """causally influences: The entity or characteristic A is causally upstream of the entity or characteristic B, A having an effect on B. An entity corresponds to any biological type of entity as long as a mass is measurable. A characteristic corresponds to a particular specificity of an entity (e.g., phenotype, shape, size)."""

    CAUSALLY_INFLUENCES: "PBPKO"
    """causally influences: The entity or characteristic A is causally upstream of the entity or characteristic B, A having an effect on B. An entity corresponds to any biological type of entity as long as a mass is measurable. A characteristic corresponds to a particular specificity of an entity (e.g., phenotype, shape, size)."""

    RO_0002578: "PBPKO"
    """directly regulates: p directly regulates q iff p is immediately causally upstream of q and p regulates q."""

    DIRECTLY_REGULATES: "PBPKO"
    """directly regulates: p directly regulates q iff p is immediately causally upstream of q and p regulates q."""

    RO_0002584: "PBPKO"
    """has part structure that is capable of: s 'has part structure that is capable of' p if and only if there exists some part x such that s 'has part' x and x 'capable of' p"""

    HAS_PART_STRUCTURE_THAT_IS_CAPABLE_OF: "PBPKO"
    """has part structure that is capable of: s 'has part structure that is capable of' p if and only if there exists some part x such that s 'has part' x and x 'capable of' p"""

    RO_0002595: "PBPKO"
    """causal relation between material entity and a process: A relationship that holds between a material entity and a process in which causality is involved, with either the material entity or some part of the material entity exerting some influence over the process, or the process influencing some aspect of the material entity."""

    CAUSAL_RELATION_BETWEEN_MATERIAL_ENTITY_AND_A_PROCESS: "PBPKO"
    """causal relation between material entity and a process: A relationship that holds between a material entity and a process in which causality is involved, with either the material entity or some part of the material entity exerting some influence over the process, or the process influencing some aspect of the material entity."""

    RO_0002596: "PBPKO"
    """capable of regulating: Holds between c and p if and only if c is capable of some activity a, and a regulates p."""

    CAPABLE_OF_REGULATING: "PBPKO"
    """capable of regulating: Holds between c and p if and only if c is capable of some activity a, and a regulates p."""

    RO_0002597: "PBPKO"
    """capable of negatively regulating: Holds between c and p if and only if c is capable of some activity a, and a negatively regulates p."""

    CAPABLE_OF_NEGATIVELY_REGULATING: "PBPKO"
    """capable of negatively regulating: Holds between c and p if and only if c is capable of some activity a, and a negatively regulates p."""

    RO_0002598: "PBPKO"
    """capable of positively regulating: Holds between c and p if and only if c is capable of some activity a, and a positively regulates p."""

    CAPABLE_OF_POSITIVELY_REGULATING: "PBPKO"
    """capable of positively regulating: Holds between c and p if and only if c is capable of some activity a, and a positively regulates p."""

    RO_0002608: "PBPKO"
    """process has causal agent: Inverse of 'causal agent in process'"""

    PROCESS_HAS_CAUSAL_AGENT: "PBPKO"
    """process has causal agent: Inverse of 'causal agent in process'"""

    RO_0002629: "PBPKO"
    """directly positively regulates: p directly positively regulates q iff p is immediately causally upstream of q, and p positively regulates q."""

    DIRECTLY_POSITIVELY_REGULATES: "PBPKO"
    """directly positively regulates: p directly positively regulates q iff p is immediately causally upstream of q, and p positively regulates q."""

    RO_0002630: "PBPKO"
    """directly negatively regulates: p directly negatively regulates q iff p is immediately causally upstream of q, and p negatively regulates q."""

    DIRECTLY_NEGATIVELY_REGULATES: "PBPKO"
    """directly negatively regulates: p directly negatively regulates q iff p is immediately causally upstream of q, and p negatively regulates q."""

    RO_0004031: "PBPKO"
    """enables subfunction: Holds between an entity and an process P where the entity enables some larger compound process, and that larger process has-part P."""

    ENABLES_SUBFUNCTION: "PBPKO"
    """enables subfunction: Holds between an entity and an process P where the entity enables some larger compound process, and that larger process has-part P."""

    RO_0004032: "PBPKO"
    """acts upstream of or within, positive effect."""

    ACTS_UPSTREAM_OF_OR_WITHIN__POSITIVE_EFFECT: "PBPKO"
    """acts upstream of or within, positive effect."""

    RO_0004033: "PBPKO"
    """acts upstream of or within, negative effect."""

    ACTS_UPSTREAM_OF_OR_WITHIN__NEGATIVE_EFFECT: "PBPKO"
    """acts upstream of or within, negative effect."""

    RO_0004034: "PBPKO"
    """acts upstream of, positive effect: c 'acts upstream of, positive effect' p if c is enables f, and f is causally upstream of p, and the direction of f is positive"""

    ACTS_UPSTREAM_OF__POSITIVE_EFFECT: "PBPKO"
    """acts upstream of, positive effect: c 'acts upstream of, positive effect' p if c is enables f, and f is causally upstream of p, and the direction of f is positive"""

    RO_0004035: "PBPKO"
    """acts upstream of, negative effect: c 'acts upstream of, negative effect' p if c is enables f, and f is causally upstream of p, and the direction of f is negative"""

    ACTS_UPSTREAM_OF__NEGATIVE_EFFECT: "PBPKO"
    """acts upstream of, negative effect: c 'acts upstream of, negative effect' p if c is enables f, and f is causally upstream of p, and the direction of f is negative"""

    RO_0004046: "PBPKO"
    """causally upstream of or within, negative effect."""

    CAUSALLY_UPSTREAM_OF_OR_WITHIN__NEGATIVE_EFFECT: "PBPKO"
    """causally upstream of or within, negative effect."""

    RO_0004047: "PBPKO"
    """causally upstream of or within, positive effect."""

    CAUSALLY_UPSTREAM_OF_OR_WITHIN__POSITIVE_EFFECT: "PBPKO"
    """causally upstream of or within, positive effect."""

    RO_0011002: "PBPKO"
    """regulates activity of: The entity A has an activity that regulates an activity of the entity B. For example, A and B are gene products where the catalytic activity of A regulates the kinase activity of B."""

    REGULATES_ACTIVITY_OF: "PBPKO"
    """regulates activity of: The entity A has an activity that regulates an activity of the entity B. For example, A and B are gene products where the catalytic activity of A regulates the kinase activity of B."""

    RO_0012011: "PBPKO"
    """indirectly causally upstream of: p is indirectly causally upstream of q iff p is causally upstream of q and there exists some process r such that p is causally upstream of r and r is causally upstream of q."""

    INDIRECTLY_CAUSALLY_UPSTREAM_OF: "PBPKO"
    """indirectly causally upstream of: p is indirectly causally upstream of q iff p is causally upstream of q and there exists some process r such that p is causally upstream of r and r is causally upstream of q."""

    RO_0012012: "PBPKO"
    """indirectly regulates: p indirectly regulates q iff p is indirectly causally upstream of q and p regulates q."""

    INDIRECTLY_REGULATES: "PBPKO"
    """indirectly regulates: p indirectly regulates q iff p is indirectly causally upstream of q and p regulates q."""

    RO_0017001: "PBPKO"
    """device utilizes material: X device utilizes material Y means X and Y are material entities, and X is capable of some process P that has input Y."""

    DEVICE_UTILIZES_MATERIAL: "PBPKO"
    """device utilizes material: X device utilizes material Y means X and Y are material entities, and X is capable of some process P that has input Y."""

    RO_0019000: "PBPKO"
    """regulates characteristic: A relationship that holds between a process and a characteristic in which process (P) regulates characteristic (C) iff: P results in the existence of C OR affects the intensity or magnitude of C."""

    REGULATES_CHARACTERISTIC: "PBPKO"
    """regulates characteristic: A relationship that holds between a process and a characteristic in which process (P) regulates characteristic (C) iff: P results in the existence of C OR affects the intensity or magnitude of C."""

    RO_0019001: "PBPKO"
    """positively regulates characteristic: A relationship that holds between a process and a characteristic in which process (P) positively regulates characteristic (C) iff: P results in an increase in the intensity or magnitude of C."""

    POSITIVELY_REGULATES_CHARACTERISTIC: "PBPKO"
    """positively regulates characteristic: A relationship that holds between a process and a characteristic in which process (P) positively regulates characteristic (C) iff: P results in an increase in the intensity or magnitude of C."""

    RO_0019002: "PBPKO"
    """negatively regulates characteristic: A relationship that holds between a process and a characteristic in which process (P) negatively regulates characteristic (C) iff: P results in a decrease in the intensity or magnitude of C."""

    NEGATIVELY_REGULATES_CHARACTERISTIC: "PBPKO"
    """negatively regulates characteristic: A relationship that holds between a process and a characteristic in which process (P) negatively regulates characteristic (C) iff: P results in a decrease in the intensity or magnitude of C."""

    UBERON_0000465: "PBPKO"
    """material anatomical entity: Anatomical entity that has mass."""

    MATERIAL_ANATOMICAL_ENTITY: "PBPKO"
    """material anatomical entity: Anatomical entity that has mass."""

    UBERON_0000466: "PBPKO"
    """immaterial anatomical entity: Anatomical entity that has no mass."""

    IMMATERIAL_ANATOMICAL_ENTITY: "PBPKO"
    """immaterial anatomical entity: Anatomical entity that has no mass."""

    UBERON_0000477: "PBPKO"
    """anatomical cluster: Anatomical group whose component anatomical structures lie in close proximity to each other."""

    ANATOMICAL_CLUSTER: "PBPKO"
    """anatomical cluster: Anatomical group whose component anatomical structures lie in close proximity to each other."""

    UBERON_0001062: "PBPKO"
    """anatomical entity: Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species."""

    ANATOMICAL_ENTITY: "PBPKO"
    """anatomical entity: Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species."""

    UO_0000001: "PBPKO"
    """length unit."""

    LENGTH_UNIT: "PBPKO"
    """length unit."""

    UO_0000002: "PBPKO"
    """mass unit."""

    MASS_UNIT: "PBPKO"
    """mass unit."""

    UO_0000003: "PBPKO"
    """time unit."""

    TIME_UNIT: "PBPKO"
    """time unit."""

    UO_0000005: "PBPKO"
    """temperature unit."""

    TEMPERATURE_UNIT: "PBPKO"
    """temperature unit."""

    UO_0000006: "PBPKO"
    """substance unit."""

    SUBSTANCE_UNIT: "PBPKO"
    """substance unit."""

    UO_0000051: "PBPKO"
    """concentration unit."""

    CONCENTRATION_UNIT: "PBPKO"
    """concentration unit."""

    UO_0000095: "PBPKO"
    """volume unit."""

    VOLUME_UNIT: "PBPKO"
    """volume unit."""

    UO_0000105: "PBPKO"
    """frequency unit."""

    FREQUENCY_UNIT: "PBPKO"
    """frequency unit."""

    UO_0000270: "PBPKO"
    """volumetric flow rate unit."""

    VOLUMETRIC_FLOW_RATE_UNIT: "PBPKO"
    """volumetric flow rate unit."""

    UO_0000280: "PBPKO"
    """rate unit."""

    RATE_UNIT: "PBPKO"
    """rate unit."""


PBPKOType = str | PBPKO

#: information of every term, registered on the class below
_terms: list[TermData] = [
    ("BFO_0000001", ("BFO_0000001", "ENTITY"), "entity", None, (), False),
    (
        "BFO_0000002",
        ("BFO_0000002", "CONTINUANT"),
        "continuant",
        "An entity that exists in full at any time in which it exists at all, persists through time while maintaining its identity and has no temporal parts.",
        (),
        False,
    ),
    (
        "BFO_0000003",
        ("BFO_0000003", "OCCURRENT"),
        "occurrent",
        "An entity that has temporal parts and that happens, unfolds or develops through time.",
        (),
        False,
    ),
    (
        "BFO_0000004",
        ("BFO_0000004", "INDEPENDENT_CONTINUANT"),
        "independent continuant",
        "b is an independent continuant = Def. b is a continuant which is such that there is no c and no t such that b s-depends_on c at t. (axiom label in BFO2 Reference: [017-002])",
        (),
        False,
    ),
    (
        "BFO_0000015",
        ("BFO_0000015", "PROCESS"),
        "process",
        "p is a process = Def. p is an occurrent that has temporal proper parts and for some time t, p s-depends_on some material entity at t. (axiom label in BFO2 Reference: [083-003])",
        (),
        False,
    ),
    ("BFO_0000016", ("BFO_0000016", "DISPOSITION"), "disposition", None, (), False),
    (
        "BFO_0000017",
        ("BFO_0000017", "REALIZABLE_ENTITY"),
        "realizable entity",
        "A specifically dependent continuant that inheres in continuant entities and are not exhibited in full at every time in which it inheres in an entity or group of entities. The exhibition or actualization of a realizable entity is a particular manifestation, functioning or process that occurs under certain circumstances.",
        (),
        False,
    ),
    ("BFO_0000019", ("BFO_0000019", "QUALITY"), "quality", None, (), False),
    (
        "BFO_0000020",
        ("BFO_0000020", "SPECIFICALLY_DEPENDENT_CONTINUANT"),
        "specifically dependent continuant",
        "b is a specifically dependent continuant = Def. b is a continuant & there is some independent continuant c which is not a spatial region and which is such that b s-depends_on c at every time t during the course of b’s existence. (axiom label in BFO2 Reference: [050-003])",
        (),
        False,
    ),
    (
        "BFO_0000023",
        ("BFO_0000023", "ROLE"),
        "role",
        "A realizable entity the manifestation of which brings about some result or end that is not essential to a continuant in virtue of the kind of thing that it is but that can be served or participated in by that kind of continuant in some kinds of natural, social or institutional contexts.",
        (),
        False,
    ),
    ("BFO_0000029", ("BFO_0000029", "SITE"), "site", None, (), False),
    (
        "BFO_0000031",
        ("BFO_0000031", "GENERICALLY_DEPENDENT_CONTINUANT"),
        "generically dependent continuant",
        None,
        (),
        False,
    ),
    ("BFO_0000034", ("BFO_0000034", "FUNCTION"), "function", None, (), False),
    (
        "BFO_0000040",
        ("BFO_0000040", "MATERIAL_ENTITY"),
        "material entity",
        "An independent continuant that is spatially extended whose identity is independent of that of other entities and can be maintained through time.",
        (),
        False,
    ),
    (
        "BFO_0000050",
        ("BFO_0000050", "PART_OF"),
        "part of",
        "a core relation that holds between a part and its whole",
        (),
        False,
    ),
    (
        "BFO_0000051",
        ("BFO_0000051", "HAS_PART"),
        "has part",
        "a core relation that holds between a whole and its part",
        (),
        False,
    ),
    (
        "BFO_0000055",
        ("BFO_0000055", "REALIZES"),
        "realizes",
        "Paraphrase of elucidation: a relation between a process and a realizable entity, where there is some material entity that is bearer of the realizable entity and participates in the process, and the realizable entity comes to be realized in the course of the process",
        (),
        False,
    ),
    (
        "BFO_0000062",
        ("BFO_0000062", "PRECEDED_BY"),
        "preceded by",
        "x is preceded by y if and only if the time point at which y ends is before or equivalent to the time point at which x starts. Formally: x preceded by y iff ω(y) <= α(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point.",
        (),
        False,
    ),
    (
        "BFO_0000063",
        ("BFO_0000063", "PRECEDES"),
        "precedes",
        "x precedes y if and only if the time point at which x ends is before or equivalent to the time point at which y starts. Formally: x precedes y iff ω(x) <= α(y), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point.",
        (),
        False,
    ),
    (
        "BFO_0000141",
        ("BFO_0000141", "IMMATERIAL_ENTITY"),
        "immaterial entity",
        None,
        (),
        False,
    ),
    (
        "CHEBI_16670",
        ("CHEBI_16670", "PEPTIDE"),
        "peptide",
        "Amide derived from two or more amino carboxylic acid molecules (the same or different) by formation of a covalent bond from the carbonyl carbon of one to the nitrogen atom of another with formal loss of water. The term is usually applied to structures formed from α-amino acids, but it includes those derived from any amino carboxylic acid. X = OH, OR, NH2, NHR, etc.",
        (),
        False,
    ),
    (
        "CHEBI_24636",
        ("CHEBI_24636", "PROTON"),
        "proton",
        "Nuclear particle of charge number +1, spin ½ and rest mass of 1.007276470(12) u.",
        (),
        False,
    ),
    (
        "CHEBI_33252",
        ("CHEBI_33252", "ATOMIC_NUCLEUS"),
        "atomic nucleus",
        "A nucleus is the positively charged central portion of an atom, excluding the orbital electrons.",
        (),
        False,
    ),
    (
        "CHEBI_33839",
        ("CHEBI_33839", "MACROMOLECULE"),
        "macromolecule",
        "A macromolecule is a molecule of high relative molecular mass, the structure of which essentially comprises the multiple repetition of units derived, actually or conceptually, from molecules of low relative molecular mass.",
        (),
        False,
    ),
    (
        "CHEBI_36342",
        ("CHEBI_36342", "SUBATOMIC_PARTICLE"),
        "subatomic particle",
        "A particle smaller than an atom.",
        (),
        False,
    ),
    (
        "CL_0000000",
        ("CL_0000000", "CELL"),
        "cell",
        "A material entity of anatomical origin (part of or deriving from an organism) that has as its parts a maximally connected cell compartment surrounded by a plasma membrane.",
        (),
        False,
    ),
    (
        "COB_0000011",
        ("COB_0000011", "ATOM"),
        "atom",
        "A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.",
        (),
        False,
    ),
    (
        "COB_0000013",
        ("COB_0000013", "MOLECULE"),
        "molecule",
        "A material entity that consists of two or more atoms that are all connected via covalent bonds such that any atom can be transitively connected with any other atom.",
        (),
        False,
    ),
    (
        "COB_0000021",
        ("COB_0000021", "GROSS_ANATOMICAL_PART"),
        "gross anatomical part",
        "A part of a multicellular organism that is a collection of cell components that are not all contained in one cell.",
        (),
        False,
    ),
    (
        "COB_0000022",
        ("COB_0000022", "ORGANISM"),
        "organism",
        "A material entity that is a maximal functionally integrated unit that develops from a program encoded in a genome",
        (),
        False,
    ),
    (
        "COB_0000035",
        ("COB_0000035", "COMPLETELY_EXECUTED_PLANNED_PROCESS"),
        "completely executed planned process",
        None,
        (),
        False,
    ),
    (
        "COB_0000080",
        ("COB_0000080", "COMPLEX_OF_MOLECULES"),
        "complex of molecules",
        "A complex of two or more molecules that are not covalently bound.",
        (),
        False,
    ),
    (
        "COB_0000082",
        ("COB_0000082", "PLANNED_PROCESS"),
        "planned process",
        "A process that is initiated by an agent who intends to carry out a plan to achieve an objective through one or more actions as described in a plan specification.",
        (),
        False,
    ),
    (
        "COB_0000502",
        ("COB_0000502", "CHARACTERISTIC"),
        "characteristic",
        None,
        (),
        False,
    ),
    ("GO_0003008", ("GO_0003008", "SYSTEM_PROCESS"), "system process", None, (), False),
    (
        "GO_0003674",
        ("GO_0003674", "GENE_PRODUCT_OR_COMPLEX_ACTIVITY"),
        "gene product or complex activity",
        "A molecular process that can be carried out by the action of a single macromolecular machine, usually via direct physical interactions with other molecular entities. Function in this sense denotes an action, or activity, that a gene product (or a complex) performs.",
        (),
        False,
    ),
    (
        "GO_0005575",
        ("GO_0005575", "CELLULAR_COMPONENT"),
        "cellular_component",
        "A location, relative to cellular compartments and structures, occupied by a macromolecular machine. There are three types of cellular components described in the gene ontology: (1) the cellular anatomical entity where a gene product carries out a molecular function (e.g., plasma membrane, cytoskeleton) or membrane-enclosed compartments (e.g., mitochondrion); (2) virion components, where viral proteins act, and (3) the stable macromolecular complexes of which gene product are parts (e.g., the clathrin complex).",
        (),
        False,
    ),
    ("GO_0007588", ("GO_0007588", "EXCRETION"), "excretion", None, (), False),
    (
        "GO_0008150",
        ("GO_0008150", "BIOLOGICAL_PROCESS"),
        "biological process",
        "A biological process is the execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence.",
        (),
        False,
    ),
    (
        "GO_0008152",
        ("GO_0008152", "METABOLIC_PROCESS"),
        "metabolic process",
        None,
        (),
        False,
    ),
    (
        "GO_0009987",
        ("GO_0009987", "CELLULAR_PROCESS"),
        "cellular process",
        None,
        (),
        False,
    ),
    (
        "GO_0016301",
        ("GO_0016301", "KINASE_ACTIVITY"),
        "kinase activity",
        None,
        (),
        False,
    ),
    (
        "GO_0032501",
        ("GO_0032501", "MULTICELLULAR_ORGANISMAL_PROCESS"),
        "multicellular organismal process",
        None,
        (),
        False,
    ),
    (
        "GO_0032991",
        ("GO_0032991", "PROTEIN_CONTAINING_COMPLEX"),
        "protein-containing complex",
        "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.",
        (),
        False,
    ),
    (
        "GO_0044423",
        ("GO_0044423", "VIRION_COMPONENT"),
        "virion component",
        "Any constituent part of a virion, a complete fully infectious extracellular virus particle.",
        (),
        False,
    ),
    (
        "GO_0110165",
        ("GO_0110165", "CELLULAR_ANATOMICAL_ENTITY"),
        "cellular anatomical entity",
        "A part of a cellular organism that is either an immaterial entity or a material entity with granularity above the level of a protein complex but below that of an anatomical system. Or, a substance produced by a cellular organism with granularity above the level of a protein complex.",
        (),
        False,
    ),
    (
        "IAO_0000003",
        ("IAO_0000003", "MEASUREMENT_UNIT_LABEL"),
        "measurement unit label",
        "A measurement unit label is as a label that is part of a scalar measurement datum and denotes a unit of measure.",
        (),
        False,
    ),
    (
        "IAO_0000005",
        ("IAO_0000005", "OBJECTIVE_SPECIFICATION"),
        "objective specification",
        "A directive information entity that describes an intended process endpoint. When part of a plan specification the concretization is realized in a planned process in which the bearer tries to effect the world so that the process endpoint is achieved.",
        (),
        False,
    ),
    (
        "IAO_0000009",
        ("IAO_0000009", "DATUM_LABEL"),
        "datum label",
        "A label is a symbol that is part of some other datum and is used to either partially define the denotation of that datum or to provide a means for identifying the datum as a member of the set of data with the same label",
        (),
        False,
    ),
    (
        "IAO_0000010",
        ("IAO_0000010", "SOFTWARE"),
        "software",
        "Software is a plan specification composed of a series of instructions that can be interpreted by or directly executed by a processing unit.",
        (),
        False,
    ),
    (
        "IAO_0000027",
        ("IAO_0000027", "DATA_ENTITY"),
        "data entity",
        "An information content entity that is intended to be one or more truthful statement(s) about something (modulo, e.g., measurement precision or other systematic errors) and is constructed/acquired by a method which reliably tends to produce (approximately) truthful statements.",
        (),
        False,
    ),
    (
        "IAO_0000030",
        ("IAO_0000030", "INFORMATION_CONTENT_ENTITY"),
        "information content entity",
        "A generically dependent continuant that is about some thing.",
        (),
        False,
    ),
    (
        "IAO_0000033",
        ("IAO_0000033", "DIRECTIVE_INFORMATION_ENTITY"),
        "directive information entity",
        "An information content entity whose concretizations indicate to their bearer how to realize them in a process.",
        (),
        False,
    ),
    (
        "IAO_0000037",
        ("IAO_0000037", "DOT_PLOT"),
        "dot plot",
        "A dot plot is a report graph which is a graphical representation of data where each data point is represented by a single dot placed on coordinates corresponding to data point values in particular dimensions.",
        (),
        False,
    ),
    (
        "IAO_0000038",
        ("IAO_0000038", "GRAPH"),
        "graph",
        "A diagram that presents one or more tuples of information by mapping those tuples in to a two dimensional space in a non arbitrary way.",
        (),
        False,
    ),
    (
        "IAO_0000064",
        ("IAO_0000064", "ALGORITHM"),
        "algorithm",
        "A plan specification which describes the inputs and output of mathematical functions as well as workflow of execution for achieving an predefined objective. Algorithms are realized usually by means of implementation as computer programs for execution by automata.",
        (),
        False,
    ),
    (
        "IAO_0000078",
        ("IAO_0000078", "CURATION_STATUS_SPECIFICATION"),
        "curation status specification",
        "The curation status of the term. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value.",
        (),
        False,
    ),
    (
        "IAO_0000098",
        ("IAO_0000098", "DATA_FORMAT_SPECIFICATION"),
        "data format specification",
        "A data format specification is the information content borne by the document published defining the specification. Example: The ISO document specifying what encompasses an XML document; The instructions in a XSD file",
        (),
        False,
    ),
    (
        "IAO_0000100",
        ("IAO_0000100", "HOMOGENOUS_DATA_COLLECTION"),
        "homogenous data collection",
        "A data item that is an aggregate of other data items of the same type that have something in common. Averages and distributions can be determined for data sets.",
        (),
        False,
    ),
    (
        "IAO_0000101",
        ("IAO_0000101", "IMAGE"),
        "image",
        "An image is an affine projection to a two dimensional surface, of measurements of some quality of an entity or entities repeated at regular intervals across a spatial range, where the measurements are represented as color and luminosity on the projected on surface.",
        (),
        False,
    ),
    (
        "IAO_0000102",
        ("IAO_0000102", "DATA_ABOUT_AN_ONTOLOGY_PART"),
        "data about an ontology part",
        "Data about an ontology part is a data item about a part of an ontology, for example a term",
        (),
        False,
    ),
    (
        "IAO_0000104",
        ("IAO_0000104", "PLAN_SPECIFICATION"),
        "plan specification",
        "A directive information entity with action specifications and objective specifications as parts, and that may be concretized as a realizable entity that, if realized, is realized in a process in which the bearer tries to achieve the objectives by taking the actions specified.",
        (),
        False,
    ),
    (
        "IAO_0000136",
        ("IAO_0000136", "IS_ABOUT"),
        "is about",
        "A (currently) primitive relation that relates an information artifact to an entity.",
        (),
        False,
    ),
    (
        "IAO_0000179",
        ("IAO_0000179", "HISTOGRAM"),
        "histogram",
        "A histogram is a report graph which is a statistical description of a distribution in terms of occurrence frequencies of different event classes.",
        (),
        False,
    ),
    (
        "IAO_0000180",
        ("IAO_0000180", "HEATMAP"),
        "heatmap",
        "A heatmap is a report graph which is a graphical representation of data where the values taken by a variable(s) are shown as colors in a two-dimensional map.",
        (),
        False,
    ),
    (
        "IAO_0000183",
        ("IAO_0000183", "DENDROGRAM"),
        "dendrogram",
        "A dendrogram is a report graph which is a tree diagram frequently used to illustrate the arrangement of the clusters produced by a clustering algorithm.",
        (),
        False,
    ),
    (
        "IAO_0000184",
        ("IAO_0000184", "SCATTER_PLOT"),
        "scatter plot",
        "A scatterplot is a graph which uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.",
        (),
        False,
    ),
    (
        "IAO_0000225",
        ("IAO_0000225", "OBSOLESCENCE_REASON_SPECIFICATION"),
        "obsolescence reason specification",
        "The reason for which a term has been deprecated. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value.",
        (),
        False,
    ),
    (
        "IAO_0000308",
        ("IAO_0000308", "FIGURE"),
        "figure",
        "An information content entity consisting of a two dimensional arrangement of information content entities such that the arrangement itself is about something.",
        (),
        False,
    ),
    (
        "IAO_0000310",
        ("IAO_0000310", "DOCUMENT"),
        "document",
        "A collection of information content entities intended to be understood together as a whole",
        (),
        False,
    ),
    (
        "IAO_0000409",
        ("IAO_0000409", "DENOTATOR_TYPE"),
        "denotator type",
        "A denotator type indicates how a term should be interpreted from an ontological perspective.",
        (),
        False,
    ),
    (
        "IAO_0001000",
        ("IAO_0001000", "DATA_COLLECTION"),
        "data collection",
        "A data entity that consists of multiple data entities.",
        (),
        False,
    ),
    (
        "NCBITaxon_117571",
        ("NCBITaxon_117571", "EUTELEOSTOMI"),
        "Euteleostomi",
        None,
        (),
        False,
    ),
    ("NCBITaxon_2759", ("NCBITaxon_2759", "EUKARYOTA"), "Eukaryota", None, (), False),
    (
        "NCBITaxon_314146",
        ("NCBITaxon_314146", "EUARCHONTOGLIRES"),
        "Euarchontoglires",
        None,
        (),
        False,
    ),
    ("NCBITaxon_32523", ("NCBITaxon_32523", "TETRAPODA"), "Tetrapoda", None, (), False),
    ("NCBITaxon_32524", ("NCBITaxon_32524", "AMNIOTA"), "Amniota", None, (), False),
    (
        "NCBITaxon_33154",
        ("NCBITaxon_33154", "OPISTHOKONTA"),
        "Opisthokonta",
        None,
        (),
        False,
    ),
    ("NCBITaxon_33208", ("NCBITaxon_33208", "METAZOA"), "Metazoa", None, (), False),
    ("NCBITaxon_33213", ("NCBITaxon_33213", "BILATERIA"), "Bilateria", None, (), False),
    ("NCBITaxon_40674", ("NCBITaxon_40674", "MAMMALIA"), "Mammalia", None, (), False),
    (
        "NCBITaxon_7742",
        ("NCBITaxon_7742", "VERTEBRATA__VERTEBRATES_"),
        "Vertebrata <vertebrates>",
        None,
        (),
        False,
    ),
    (
        "NCBITaxon_9606",
        ("NCBITaxon_9606", "HOMO_SAPIENS"),
        "Homo sapiens",
        None,
        (),
        False,
    ),
    (
        "OBI_0000014",
        ("OBI_0000014", "REGULATOR_ROLE"),
        "regulator role",
        "a regulatory role involved with making and/or enforcing relevant legislation and governmental orders",
        (),
        False,
    ),
    (
        "OBI_0000017",
        ("OBI_0000017", "REGULATORY_ROLE"),
        "regulatory role",
        "a role which inheres in material entities and is realized in the processes of making, enforcing or being defined by legislation or orders issued by a governmental body.",
        (),
        False,
    ),
    (
        "OBI_0000018",
        ("OBI_0000018", "MATERIAL_SUPPLIER_ROLE"),
        "material supplier role",
        "a role realized through the process of supplying materials such as animal subjects, reagents or other materials used in an investigation.",
        (),
        False,
    ),
    (
        "OBI_0000023",
        ("OBI_0000023", "CLASSIFIED_DATA_SET"),
        "classified data set",
        "A data set that is produced as the output of a class prediction data transformation and consists of a data set with assigned class labels.",
        (),
        False,
    ),
    (
        "OBI_0000112",
        ("OBI_0000112", "SPECIMEN_ROLE"),
        "specimen role",
        "A role borne by a material entity that is obtained during a specimen collection process and that can be realized by performing measurements or observations on the specimen.",
        (),
        False,
    ),
    (
        "OBI_0000245",
        ("OBI_0000245", "ORGANIZATION"),
        "organization",
        "An entity that can bear roles, has members, and has a set of organization rules. Members of organizations are either organizations themselves or individual people. Members can bear specific organization member roles that are determined in the organization rules. The organization rules also determine how decisions are made on behalf of the organization by the organization members.",
        (),
        False,
    ),
    (
        "OBI_0000260",
        ("OBI_0000260", "PLAN"),
        "plan",
        "A plan is a realizable entity that is the inheres in a bearer who is committed to realizing it as a completely executed planned process.",
        (),
        False,
    ),
    (
        "OBI_0000293",
        ("OBI_0000293", "HAS_SPECIFIED_INPUT"),
        "has specified input",
        "The inverse property of is specified input of",
        (),
        False,
    ),
    (
        "OBI_0000295",
        ("OBI_0000295", "IS_SPECIFIED_INPUT_OF"),
        "is specified input of",
        "A relation between a completely executed planned process and a continuant participating in that process that is not created during the process. The presence of the continuant during the process is explicitly specified in the plan specification which the process realizes the concretization of.",
        (),
        False,
    ),
    (
        "OBI_0000299",
        ("OBI_0000299", "HAS_SPECIFIED_OUTPUT"),
        "has specified output",
        "The inverse property of is specified output of",
        (),
        False,
    ),
    (
        "OBI_0000312",
        ("OBI_0000312", "IS_SPECIFIED_OUTPUT_OF"),
        "is specified output of",
        "A relation between a completely executed planned process and a continuant participating in that process. The presence of the continuant at the end of the process is explicitly specified in the objective specification which the process realizes the concretization of.",
        (),
        False,
    ),
    (
        "OBI_0000417",
        ("OBI_0000417", "ACHIEVES_PLANNED_OBJECTIVE"),
        "achieves_planned_objective",
        "This relation obtains between a planned process and a objective specification when the criteria specified in the objective specification are met at the end of the planned process.",
        (),
        False,
    ),
    (
        "OBI_0000450",
        ("OBI_0000450", "REGULATORY_AGENCY"),
        "regulatory agency",
        "A regulatory agency is a organization that has responsibility over or for the legislation (acts and regulations) for a given sector of the government.",
        (),
        False,
    ),
    (
        "OBI_0000571",
        ("OBI_0000571", "MANUFACTURER_ROLE"),
        "manufacturer role",
        "Manufacturer role is a role which inheres in a person or organization and which is realized by a manufacturing process.",
        (),
        False,
    ),
    (
        "OBI_0000648",
        ("OBI_0000648", "CLUSTERED_DATA_SET"),
        "clustered data set",
        "A data set that is produced as the output of a class discovery data transformation and consists of a data set with assigned discovered class labels.",
        (),
        False,
    ),
    (
        "OBI_0000658",
        ("OBI_0000658", "DATA_REPRESENTATIONAL_MODEL"),
        "data representational model",
        "An information content entity representing the relationships between data items.",
        (),
        False,
    ),
    (
        "OBI_0000659",
        ("OBI_0000659", "SPECIMEN_COLLECTION_PROCESS"),
        "specimen collection process",
        "A planned process with the objective to obtain a material entity for potential use as an input upon which measurements or observations are performed.",
        (),
        False,
    ),
    (
        "OBI_0000663",
        ("OBI_0000663", "CLASS_PREDICTION_DATA_TRANSFORMATION"),
        "class prediction data transformation",
        "A class prediction data transformation (sometimes called supervised classification) is a data transformation that has objective class prediction.",
        (),
        False,
    ),
    (
        "OBI_0000684",
        ("OBI_0000684", "SPECIMEN_COLLECTION_OBJECTIVE"),
        "specimen collection objective",
        "A objective specification that is fulfilled by obtaining a material entity for potential use as an input upon which measurements or observations are performed.",
        (),
        False,
    ),
    (
        "OBI_0000700",
        ("OBI_0000700", "SUPPORT_VECTOR_MACHINE"),
        "support vector machine",
        "A support vector machine is a data transformation with a class prediction objective based on the construction of a separating hyperplane that maximizes the margin between two data sets of vectors in n-dimensional space.",
        (),
        False,
    ),
    (
        "OBI_0000704",
        ("OBI_0000704", "DECISION_TREE_INDUCTION_OBJECTIVE"),
        "decision tree induction objective",
        "A decision tree induction objective is a data transformation objective in which a tree-like graph of edges and nodes is created and from which the selection of each branch requires that some type of logical decision is made.",
        (),
        False,
    ),
    (
        "OBI_0000707",
        ("OBI_0000707", "DECISION_TREE_BUILDING_DATA_TRANSFORMATION"),
        "decision tree building data transformation",
        "A decision tree building data transformation is a data transformation that has objective decision tree induction.",
        (),
        False,
    ),
    (
        "OBI_0000713",
        ("OBI_0000713", "GENEPATTERN_SOFTWARE"),
        "GenePattern software",
        "a software that provides access to more than 100 tools for gene expression analysis, proteomics, SNP analysis and common data processing tasks.",
        (),
        False,
    ),
    (
        "OBI_0000726",
        ("OBI_0000726", "PEAK_MATCHING"),
        "peak matching",
        "Peak matching is a data transformation performed on a dataset of a graph of ordered data points (e.g. a spectrum) with the objective of pattern matching local maxima above a noise threshold",
        (),
        False,
    ),
    (
        "OBI_0000727",
        ("OBI_0000727", "K_NEAREST_NEIGHBORS"),
        "k-nearest neighbors",
        "A k-nearest neighbors is a data transformation which achieves a class discovery or partitioning objective, in which an input data object with vector y is assigned to a class label based upon the k closest training data set points to y; where k is the largest value that class label is assigned.",
        (),
        False,
    ),
    (
        "OBI_0000749",
        ("OBI_0000749", "CART"),
        "CART",
        "A CART (classification and regression trees) is a data transformation method for producing a classification or regression model with a tree-based structure.",
        (),
        False,
    ),
    (
        "OBI_0000792",
        ("OBI_0000792", "STATISTICAL_MODEL_VALIDATION"),
        "statistical model validation",
        "A data transformation which assesses how the results of a statistical analysis will generalize to an independent data set.",
        (),
        False,
    ),
    (
        "OBI_0000833",
        ("OBI_0000833", "OBJECTIVE_ACHIEVED_BY"),
        "objective_achieved_by",
        "This relation obtains between an objective specification and a planned process when the criteria specified in the objective specification are met at the end of the planned process.",
        (),
        False,
    ),
    (
        "OBI_0000835",
        ("OBI_0000835", "MANUFACTURER"),
        "manufacturer",
        "A person or organization that has a manufacturer role.",
        (),
        False,
    ),
    (
        "OBI_0000947",
        ("OBI_0000947", "SERVICE_PROVIDER_ROLE"),
        "service provider role",
        "is a role which inheres in a person or organization and is realized in in a planned process which provides access to training, materials or execution of protocols for an organization or person",
        (),
        False,
    ),
    (
        "OBI_0000963",
        ("OBI_0000963", "CATEGORICAL_LABEL"),
        "categorical label",
        "A label that is part of a categorical datum and that indicates the value of the data item on the categorical scale.",
        (),
        False,
    ),
    (
        "OBI_0001000",
        ("OBI_0001000", "QUESTIONNAIRE"),
        "questionnaire",
        "A document with a set of printed or written questions with a choice of answers, devised for the purposes of a survey or statistical study.",
        (),
        False,
    ),
    (
        "OBI_0001468",
        ("OBI_0001468", "CELL_SPECIMEN"),
        "cell specimen",
        "A specimen primarily composed of a cell or cells collected from a multicellular organism or a cell culture.",
        (),
        False,
    ),
    (
        "OBI_0001479",
        ("OBI_0001479", "SPECIMEN_FROM_ORGANISM"),
        "specimen from organism",
        "A specimen that derives from an anatomical part or substance arising from an organism. Examples of tissue specimen include tissue, organ, physiological system, blood, or body location (arm).",
        (),
        False,
    ),
    (
        "OBI_0001930",
        ("OBI_0001930", "CATEGORICAL_VALUE_SPECIFICATION"),
        "categorical value specification",
        "A value specification that is specifies one category out of a fixed number of nominal categories",
        (),
        False,
    ),
    (
        "OBI_0001933",
        ("OBI_0001933", "VALUE_SPECIFICATION"),
        "value specification",
        "An information content entity that specifies a value within a classification scheme or on a quantitative scale.",
        (),
        False,
    ),
    (
        "OBI_0002076",
        ("OBI_0002076", "COLLECTION_OF_SPECIMENS"),
        "collection of specimens",
        "A material entity that has two or more specimens as its parts.",
        (),
        False,
    ),
    (
        "OBI_0002205",
        ("OBI_0002205", "HISTOLOGIC_GRADE_ACCORDING_TO_AJCC_7TH_EDITION"),
        "histologic grade according to AJCC 7th edition",
        "A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the American Joint Committee on Cancer (AJCC) 7th Edition grading system.",
        (),
        False,
    ),
    (
        "OBI_0002210",
        (
            "OBI_0002210",
            "HISTOLOGIC_GRADE_ACCORDING_TO_THE_FUHRMAN_NUCLEAR_GRADING_SYSTEM",
        ),
        "histologic grade according to the Fuhrman Nuclear Grading System",
        "A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the Fuhrman Nuclear Grading System.",
        (),
        False,
    ),
    (
        "OBI_0002215",
        ("OBI_0002215", "HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR"),
        "histologic grade for ovarian tumor",
        "A categorical value specification that is a histologic grade assigned to a ovarian tumor.",
        (),
        False,
    ),
    (
        "OBI_0002216",
        (
            "OBI_0002216",
            "HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR_ACCORDING_TO_A_TWO_TIER_GRADING_SYSTEM",
        ),
        "histologic grade for ovarian tumor according to a two-tier grading system",
        "A histologic grade for ovarian tumor that is from a two-tier histological classification of tumors.",
        (),
        False,
    ),
    (
        "OBI_0002219",
        (
            "OBI_0002219",
            "HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR_ACCORDING_TO_THE_WORLD_HEALTH_ORGANIZATION",
        ),
        "histologic grade for ovarian tumor according to the World Health Organization",
        "A histologic grade for ovarian tumor that is from a histological classification by the World Health Organization (WHO).",
        (),
        False,
    ),
    (
        "OBI_0002224",
        (
            "OBI_0002224",
            "PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_COLON_AND_RECTUM_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic primary tumor stage for colon and rectum according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002232",
        (
            "OBI_0002232",
            "PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic primary tumor stage for lung according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002243",
        (
            "OBI_0002243",
            "PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic primary tumor stage for kidney according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002256",
        (
            "OBI_0002256",
            "PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic primary tumor stage for ovary according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002270",
        (
            "OBI_0002270",
            "PATHOLOGIC_LYMPH_NODE_STAGE_FOR_COLON_AND_RECTUM_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic lymph node stage for colon and rectum according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    (
        "OBI_0002279",
        (
            "OBI_0002279",
            "PATHOLOGIC_LYMPH_NODE_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic lymph node stage for lung according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    (
        "OBI_0002284",
        (
            "OBI_0002284",
            "PATHOLOGIC_LYMPH_NODE_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic lymph node stage for kidney according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    (
        "OBI_0002287",
        (
            "OBI_0002287",
            "PATHOLOGIC_LYMPH_NODE_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic lymph node stage for ovary according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    (
        "OBI_0002290",
        (
            "OBI_0002290",
            "PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_COLON_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic distant metastases stage for colon according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of colon cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002298",
        (
            "OBI_0002298",
            "PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic distant metastases stage for lung according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002306",
        (
            "OBI_0002306",
            "PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic distant metastases stage for kidney according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002310",
        (
            "OBI_0002310",
            "PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION",
        ),
        "pathologic distant metastases stage for ovary according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    (
        "OBI_0002314",
        ("OBI_0002314", "CLINICAL_TUMOR_STAGE_GROUP_ACCORDING_TO_AJCC_7TH_EDITION"),
        "clinical tumor stage group according to AJCC 7th edition",
        "A categorical value specification that is an assessment of the stage of a cancer according to the American Joint Committee on Cancer (AJCC) v7 staging systems.",
        (),
        False,
    ),
    (
        "OBI_0002326",
        (
            "OBI_0002326",
            "INTERNATIONAL_FEDERATION_OF_GYNECOLOGY_AND_OBSTETRICS_CERVICAL_CANCER_STAGE_VALUE_SPECIFICATION",
        ),
        "International Federation of Gynecology and Obstetrics cervical cancer stage value specification",
        "A categorical value specification that is an assessment of the stage of a gynecologic cancer according to the International Federation of Gynecology and Obstetrics (FIGO) staging systems.",
        (),
        False,
    ),
    (
        "OBI_0002341",
        (
            "OBI_0002341",
            "INTERNATIONAL_FEDERATION_OF_GYNECOLOGY_AND_OBSTETRICS_OVARIAN_CANCER_STAGE_VALUE_SPECIFICATION",
        ),
        "International Federation of Gynecology and Obstetrics ovarian cancer stage value specification",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the FIGO classification system.",
        (),
        False,
    ),
    (
        "OBI_0002356",
        ("OBI_0002356", "PERFORMANCE_STATUS_VALUE_SPECIFICATION"),
        "performance status value specification",
        "A categorical value specification that is an assessment of a participant's performance status (general well-being and activities of daily life).",
        (),
        False,
    ),
    (
        "OBI_0002357",
        ("OBI_0002357", "EASTERN_COOPERATIVE_ONCOLOGY_GROUP_SCORE_VALUE_SPECIFICATION"),
        "Eastern Cooperative Oncology Group score value specification",
        "A performance status value specification designed by the Eastern Cooperative Oncology Group to assess disease progression and its affect on the daily living abilities of the patient.",
        (),
        False,
    ),
    (
        "OBI_0002363",
        ("OBI_0002363", "KARNOFSKY_SCORE_VAUE_SPECIFICATION"),
        "Karnofsky score vaue specification",
        "A performance status value specification designed for classifying patients 16 years of age or older by their functional impairment.",
        (),
        False,
    ),
    (
        "OBI_0002989",
        ("OBI_0002989", "MATERIAL_SUPPLIER"),
        "material supplier",
        "A person or organization that provides material supplies to other people or organizations.",
        (),
        False,
    ),
    (
        "OBI_0100051",
        ("OBI_0100051", "SPECIMEN"),
        "specimen",
        "A material entity that is collected for potential use as an input upon which measurements or observations are performed.",
        (),
        False,
    ),
    (
        "OBI_0200000",
        ("OBI_0200000", "DATA_TRANSFORMATION"),
        "data transformation",
        "A completely executed planned process that produces output data from input data.",
        (),
        False,
    ),
    (
        "OBI_0200033",
        ("OBI_0200033", "LEAVE_ONE_OUT_CROSS_VALIDATION_METHOD"),
        "leave one out cross validation method",
        "is a data transformation : leave-one-out cross-validation (LOOCV) involves using a single observation from the original sample as the validation data, and the remaining observations as the training data. This is repeated such that each observation in the sample is used once as the validation data",
        (),
        False,
    ),
    (
        "OBI_0200041",
        ("OBI_0200041", "K_MEANS_CLUSTERING"),
        "k-means clustering",
        "A k-means clustering is a data transformation which achieves a class discovery or partitioning objective, which takes as input a collection of objects (represented as points in multidimensional space) and which partitions them into a specified number k of clusters. The algorithm attempts to find the centers of natural clusters in the data. The most common form of the algorithm starts by partitioning the input points into k initial sets, either at random or using some heuristic data. It then calculates the mean point, or centroid, of each set. It constructs a new partition by associating each point with the closest centroid. Then the centroids are recalculated for the new clusters, and the algorithm repeated by alternate applications of these two steps until convergence, which is obtained when the points no longer switch clusters (or alternatively centroids are no longer changed).",
        (),
        False,
    ),
    (
        "OBI_0200042",
        ("OBI_0200042", "HIERARCHICAL_CLUSTERING"),
        "hierarchical clustering",
        "A hierarchical clustering is a data transformation which achieves a class discovery objective, which takes as input data item and builds a hierarchy of clusters. The traditional representation of this hierarchy is a tree (visualized by a dendrogram), with the individual input objects at one end (leaves) and a single cluster containing every object at the other (root).",
        (),
        False,
    ),
    (
        "OBI_0200050",
        ("OBI_0200050", "DIMENSIONALITY_REDUCTION"),
        "dimensionality reduction",
        "A dimensionality reduction is data partitioning which transforms each input m-dimensional vector (x_1, x_2, ..., x_m) into an output n-dimensional vector (y_1, y_2, ..., y_n), where n is smaller than m.",
        (),
        False,
    ),
    (
        "OBI_0200051",
        ("OBI_0200051", "PRINCIPAL_COMPONENTS_ANALYSIS_DIMENSIONALITY_REDUCTION"),
        "principal components analysis dimensionality reduction",
        "A principal components analysis dimensionality reduction is a dimensionality reduction achieved by applying principal components analysis and by keeping low-order principal components and excluding higher-order ones.",
        (),
        False,
    ),
    (
        "OBI_0200111",
        ("OBI_0200111", "DATA_VISUALIZATION"),
        "data visualization",
        "A planned process with the objective to graphically represent some data by inputing the data and outputting images, diagrams or animations.",
        (),
        False,
    ),
    (
        "OBI_0200166",
        ("OBI_0200166", "DATA_TRANSFORMATION_OBJECTIVE"),
        "data transformation objective",
        "An objective specification to transformation input data into output data",
        (),
        False,
    ),
    (
        "OBI_0200171",
        ("OBI_0200171", "PARTITIONING_DATA_TRANSFORMATION"),
        "partitioning data transformation",
        "A partitioning data transformation is a data transformation that has objective partitioning.",
        (),
        False,
    ),
    (
        "OBI_0200172",
        ("OBI_0200172", "PARTITIONING_OBJECTIVE"),
        "partitioning objective",
        "A partitioning objective is a data transformation objective where the aim is to generate a collection of disjoint non-empty subsets whose union equals a non-empty input set.",
        (),
        False,
    ),
    (
        "OBI_0200175",
        ("OBI_0200175", "CLASS_DISCOVERY_DATA_TRANSFORMATION"),
        "class discovery data transformation",
        "A class discovery data transformation (sometimes called unsupervised classification) is a data transformation that has objective class discovery.",
        (),
        False,
    ),
    (
        "OBI_0200178",
        ("OBI_0200178", "CLASS_DISCOVERY_OBJECTIVE"),
        "class discovery objective",
        "A class discovery objective (sometimes called unsupervised classification) is a data transformation objective where the aim is to organize input data (typically vectors of attributes) into classes, where the number of classes and their specifications are not known a priori. Depending on usage, the class assignment can be definite or probabilistic.",
        (),
        False,
    ),
    (
        "OBI_0200179",
        ("OBI_0200179", "CLASS_PREDICTION_OBJECTIVE"),
        "class prediction objective",
        "A class prediction objective (sometimes called supervised classification) is a data transformation objective where the aim is to create a predictor from training data through a machine learning technique. The training data consist of pairs of objects (typically vectors of attributes) and class labels for these objects. The resulting predictor can be used to attach class labels to any valid novel input object. Depending on usage, the prediction can be definite or probabilistic. A classification is learned from the training data and can then be tested on test data.",
        (),
        False,
    ),
    (
        "OBI_0200188",
        ("OBI_0200188", "CROSS_VALIDATION_OBJECTIVE"),
        "cross validation objective",
        "A cross validation objective is a data transformation objective in which the aim is to partition a sample of data into subsets such that the analysis is initially performed on a single subset, while the other subset(s) are retained for subsequent use in confirming and validating the initial analysis.",
        (),
        False,
    ),
    (
        "OBI_0200190",
        ("OBI_0200190", "CLUSTERED_DATA_VISUALIZATION"),
        "clustered data visualization",
        "A data visualization which has input of a clustered data set and produces an output of a report graph which is capable of rendering data of this type.",
        (),
        False,
    ),
    ("PATO_0000001", ("PATO_0000001",), "quality", None, (), False),
    (
        "PBPKO_00002",
        ("PBPKO_00002", "PARAMETER"),
        "parameter",
        "A data item involved in PBPK modelling.",
        (),
        False,
    ),
    (
        "PBPKO_00003",
        ("PBPKO_00003", "PHYSIOLOGICALLY_BASED_PHARMACOKINETIC_MODEL"),
        "physiologically based pharmacokinetic model",
        "A data representation model that predicts the absorption, distribution, metabolism, and excretion (ADME) of chemical substances in biological species based on physiological principles using mathematical modelling technique.",
        (),
        False,
    ),
    (
        "PBPKO_00004",
        ("PBPKO_00004", "WHOLE_BODY_PBPK"),
        "whole body pbpk",
        "A physiologically based pharmacokinetic model that contains an explicit representation of the organs most relevant to the ADME of the compound.",
        (),
        False,
    ),
    (
        "PBPKO_00005",
        ("PBPKO_00005", "PERFUSION_LIMITED_MODEL"),
        "perfusion limited model",
        "A physiologically based pharmacokinetic model that assumes tissue concentration reaches equilibrium rapidly and uptake/elimination is limited by blood flow rate.",
        (),
        False,
    ),
    (
        "PBPKO_00006",
        ("PBPKO_00006", "PHYSIOLOGICAL_PARAMETER"),
        "physiological parameter",
        "A parameter that provides the structural framework for a PBPK model and relates to the organism's physiology (e.g., body weight, organ volume, blood flow).",
        (),
        False,
    ),
    (
        "PBPKO_00007",
        ("PBPKO_00007", "BODY_MASS_INDEX"),
        "body mass index",
        "A physiological parameter calculated as an individual's weight (kg) divided by the square of their height (m).",
        (),
        False,
    ),
    (
        "PBPKO_00008",
        ("PBPKO_00008", "BODYWEIGHT"),
        "bodyweight",
        "A physiological parameter representing the mass or quantity of heaviness of an individual.",
        (),
        False,
    ),
    (
        "PBPKO_00009",
        ("PBPKO_00009", "HEIGHT"),
        "height",
        "A physiological parameter describing the distance from the bottom to the top of someone standing upright.",
        (),
        False,
    ),
    (
        "PBPKO_00010",
        ("PBPKO_00010", "SURFACE_AREA"),
        "surface area",
        "A physiological parameter representing the total area that the surface of an object occupies.",
        (),
        False,
    ),
    (
        "PBPKO_00011",
        ("PBPKO_00011", "ASSIGNED_RACE"),
        "assigned race",
        "A parameter representing a geographic ancestral origin category assigned to a population group.",
        (),
        False,
    ),
    (
        "PBPKO_00012",
        ("PBPKO_00012", "BLOOD_FLOW_RATE_TO_COMPARTMENT"),
        "blood flow rate to compartment",
        "A bodily fluid flow rate parameter representing the rate of blood flow in different parts of the body",
        (),
        False,
    ),
    (
        "PBPKO_00013",
        ("PBPKO_00013", "CARDIAC_OUTPUT_RATE"),
        "cardiac output rate",
        "A blood flow rate parameter representing the volume of blood pumped by the heart compartment per unit of time.",
        (),
        False,
    ),
    (
        "PBPKO_00014",
        ("PBPKO_00014", "BLOOD_FLOW_RATE_TO_STOMACH"),
        "blood flow rate to stomach",
        "A blood flow rate parameter specifically describing the rate to the stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00015",
        ("PBPKO_00015", "FRACTION_OF_BLOOD_FLOW_TO_STOMACH"),
        "fraction of blood flow to stomach",
        "The dimensionless fraction of cardiac output delivered to the stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00016",
        ("PBPKO_00016", "BLOOD_FLOW_RATE_TO_INTESTINE"),
        "blood flow rate to intestine",
        "A blood flow parameter specifically describing the rate to the intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00017",
        ("PBPKO_00017", "FRACTION_OF_BLOOD_FLOW_TO_INTESTINE"),
        "fraction of blood flow to intestine",
        "The dimensionless fraction of cardiac output delivered to the intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00018",
        ("PBPKO_00018", "BLOOD_FLOW_RATE_TO_SMALL_INTESTINE"),
        "blood flow rate to small intestine",
        "A blood flow rate parameter specifically describing the rate to the small intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00019",
        ("PBPKO_00019", "FRACTION_OF_BLOOD_FLOW_TO_SMALL_INTESTINE"),
        "fraction of blood flow to small intestine",
        "The dimensionless fraction of cardiac output delivered to the small intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00020",
        ("PBPKO_00020", "BLOOD_FLOW_RATE_TO_LARGE_INTESTINE"),
        "blood flow rate to large intestine",
        "A blood flow rate parameter specifically describing the rate to the large intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00021",
        ("PBPKO_00021", "FRACTION_OF_BLOOD_FLOW_TO_LARGE_INTESTINE"),
        "fraction of blood flow to large intestine",
        "The dimensionless fraction of cardiac output delivered to the large intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00022",
        ("PBPKO_00022", "BLOOD_FLOW_RATE_TO_PANCREAS"),
        "blood flow rate to pancreas",
        "A blood flow rate parameter specifically describing the rate to the pancreas compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00023",
        ("PBPKO_00023", "FRACTION_OF_BLOOD_FLOW_TO_PANCREAS"),
        "fraction of blood flow to pancreas",
        "The dimensionless fraction of cardiac output delivered to the pancreas compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00024",
        ("PBPKO_00024", "BLOOD_FLOW_RATE_TO_LIVER"),
        "blood flow rate to liver",
        "A blood flow rate parameter specifically describing the rate to the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00025",
        ("PBPKO_00025", "FRACTION_OF_BLOOD_FLOW_TO_LIVER"),
        "fraction of blood flow to liver",
        "The dimensionless fraction of cardiac output delivered to the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00026",
        ("PBPKO_00026", "BLOOD_FLOW_RATE_TO_KIDNEY"),
        "blood flow rate to kidney",
        "A blood flow rate parameter specifically describing the rate to the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00027",
        ("PBPKO_00027", "FRACTION_OF_BLOOD_FLOW_TO_KIDNEY"),
        "fraction of blood flow to kidney",
        "The dimensionless fraction of cardiac output delivered to the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00028",
        ("PBPKO_00028", "BLOOD_FLOW_RATE_TO_MUSCLE"),
        "blood flow rate to muscle",
        "A blood flow rate parameter specifically describing the rate to the muscle compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00029",
        ("PBPKO_00029", "FRACTION_OF_BLOOD_FLOW_TO_MUSCLE"),
        "fraction of blood flow to muscle",
        "The dimensionless fraction of cardiac output delivered to the muscle compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00030",
        ("PBPKO_00030", "BLOOD_FLOW_RATE_TO_HEART"),
        "blood flow rate to heart",
        "A blood flow rate parameter specifically describing the rate to the heart compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00031",
        ("PBPKO_00031", "FRACTION_OF_BLOOD_FLOW_TO_HEART"),
        "fraction of blood flow to heart",
        "The dimensionless fraction of cardiac output delivered to the heart compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00032",
        ("PBPKO_00032", "BLOOD_FLOW_RATE_TO_FAT"),
        "blood flow rate to fat",
        "A blood flow rate parameter specifically describing the rate to the fat (adipose tissue) compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00033",
        ("PBPKO_00033", "FRACTION_OF_BLOOD_FLOW_TO_FAT"),
        "fraction of blood flow to fat",
        "The dimensionless fraction of cardiac output delivered to the fat compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00034",
        ("PBPKO_00034", "BLOOD_FLOW_RATE_TO_GONAD"),
        "blood flow rate to gonad",
        "A blood flow parameter specifically describing the rate to the gonads compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00035",
        ("PBPKO_00035", "FRACTION_OF_BLOOD_FLOW_TO_GONAD"),
        "fraction of blood flow to gonad",
        "The dimensionless fraction of cardiac output delivered to the gonad compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00036",
        ("PBPKO_00036", "BLOOD_FLOW_RATE_TO_SKIN"),
        "blood flow rate to skin",
        "A blood flow rate parameter specifically describing the rate to the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00037",
        ("PBPKO_00037", "FRACTION_OF_BLOOD_FLOW_TO_SKIN"),
        "fraction of blood flow to skin",
        "The dimensionless fraction of cardiac output delivered to the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00038",
        ("PBPKO_00038", "BLOOD_FLOW_RATE_TO_BONE"),
        "blood flow rate to bone",
        "A blood flow rate parameter specifically describing the rate to the bone compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00039",
        ("PBPKO_00039", "FRACTION_OF_BLOOD_FLOW_TO_BONE"),
        "fraction of blood flow to bone",
        "The dimensionless fraction of cardiac output delivered to the bone compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00040",
        ("PBPKO_00040", "BLOOD_FLOW_RATE_TO_BRAIN"),
        "blood flow rate to brain",
        "A blood flow rate parameter specifically describing the rate to the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00041",
        ("PBPKO_00041", "FRACTION_OF_BLOOD_FLOW_TO_BRAIN"),
        "fraction of blood flow to brain",
        "The dimensionless fraction of cardiac output delivered to the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00042",
        ("PBPKO_00042", "BLOOD_FLOW_RATE_TO_SPLEEN"),
        "blood flow rate to spleen",
        "A blood flow rate parameter specifically describing the rate to the spleen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00043",
        ("PBPKO_00043", "FRACTION_OF_BLOOD_FLOW_TO_SPLEEN"),
        "fraction of blood flow to spleen",
        "The dimensionless fraction of cardiac output delivered to the spleen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00044",
        ("PBPKO_00044", "BLOOD_FLOW_RATE_TO_LUNG"),
        "blood flow rate to lung",
        "A blood flow rate parameter specifically describing the rate to the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00045",
        ("PBPKO_00045", "FRACTION_OF_BLOOD_FLOW_TO_LUNG"),
        "fraction of blood flow to lung",
        "The dimensionless fraction of cardiac output delivered to the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00046",
        ("PBPKO_00046", "BLOOD_FLOW_RATE_TO_POORLY_PERFUSED"),
        "blood flow rate to poorly perfused",
        "A blood flow rate parameter specifically describing the rate to the poorly perfused organ/tissue compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00047",
        ("PBPKO_00047", "FRACTION_OF_BLOOD_FLOW_TO_POORLY_PERFUSED"),
        "fraction of blood flow to poorly perfused",
        "The dimensionless fraction of cardiac output delivered to the poorly perfused compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00048",
        ("PBPKO_00048", "BLOOD_FLOW_RATE_TO_RICHLY_PERFUSED"),
        "blood flow rate to richly perfused",
        "A blood flow rate parameter specifically describing the rate to the richly perfused organ/tissue compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00049",
        ("PBPKO_00049", "FRACTION_OF_BLOOD_FLOW_TO_RICHLY_PERFUSED"),
        "fraction of blood flow to richly perfused",
        "The dimensionless fraction of cardiac output delivered to the richly perfused compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00050",
        ("PBPKO_00050", "BLOOD_FLOW_RATE_TO_RESTBODY"),
        "blood flow rate to restbody",
        "A blood flow rate parameter specifically describing the rate to the rest of body compartment (total minus specified organs).",
        (),
        False,
    ),
    (
        "PBPKO_00051",
        ("PBPKO_00051", "FRACTION_OF_BLOOD_FLOW_TO_RESTBODY"),
        "fraction of blood flow to restbody",
        "The dimensionless fraction of cardiac output delivered to the rest of the body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00052",
        ("PBPKO_00052", "BLOOD_FLOW_RATE_TO_GALL_BLADDER"),
        "blood flow rate to gall bladder",
        "A blood flow rate parameter specifically describing the rate to the gall bladder compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00053",
        ("PBPKO_00053", "FRACTION_OF_BLOOD_FLOW_TO_GALL_BLADDER"),
        "fraction of blood flow to gall bladder",
        "The dimensionless fraction of cardiac output delivered to the gall bladder compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00054",
        ("PBPKO_00054", "BLOOD_FLOW_RATE_TO_PORTAL_VEIN"),
        "blood flow rate to portal vein",
        "A blood flow rate parameter specifically describing the rate to the portal vein compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00055",
        ("PBPKO_00055", "FRACTION_OF_BLOOD_FLOW_TO_PORTAL_VEIN"),
        "fraction of blood flow to portal vein",
        "The dimensionless fraction of cardiac output delivered to the portal vein compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00056",
        ("PBPKO_00056", "BLOOD_FLOW_RATE_TO_LYMPH"),
        "blood flow rate to lymph",
        "A blood flow rate parameter specifically describing the rate to the lymph compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00057",
        ("PBPKO_00057", "FRACTION_OF_BLOOD_FLOW_TO_LYMPH"),
        "fraction of blood flow to lymph",
        "The dimensionless fraction of cardiac output delivered to the lymph compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00058",
        ("PBPKO_00058", "AMOUNT_OF_METABOLIZED"),
        "amount of metabolized",
        "An output parameter representing the total amount of compound metabolized.",
        (),
        False,
    ),
    (
        "PBPKO_00060",
        ("PBPKO_00060", "FRACTION_OF_BLOOD_FLOW_TO_STRATUM_CORNEUM"),
        "fraction of blood flow to stratum corneum",
        "The dimensionless fraction of cardiac output delivered to the stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00061",
        ("PBPKO_00061", "FRACTION_OF_EXPOSED_SKIN"),
        "fraction of exposed skin",
        "A dimensionless fraction of volume defined as the exposed skin volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00062",
        ("PBPKO_00062", "FRACTION_OF_UNEXPOSED_SKIN"),
        "fraction of unexposed skin",
        "A dimensionless fraction of volume defined as the unexposed skin volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00063",
        ("PBPKO_00063", "ARTERIAL_BLOOD_FLOW_RATE"),
        "arterial blood flow rate",
        "A blood flow rate parameter representing the rate of blood flow through the arterial compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00064",
        ("PBPKO_00064", "VENOUS_BLOOD_FLOW_RATE"),
        "venous blood flow rate",
        "A blood flow rate parameter representing the rate of blood flow returning through the venous compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00065",
        ("PBPKO_00065", "GLOMERULAR_FILTRATION_RATE"),
        "glomerular filtration rate",
        "A bodily fluid flow rate parameter (or physiological process measure) describing the flow rate of filtered fluid through the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00066",
        ("PBPKO_00066", "VOLUME_OF_COMPARTMENT"),
        "volume of compartment",
        "A physiological parameter representing the volume of a specific organ or tissue.",
        (),
        False,
    ),
    (
        "PBPKO_00067",
        ("PBPKO_00067", "VOLUME_OF_STOMACH"),
        "volume of stomach",
        "A volume parameter representing the total volume of the stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00068",
        ("PBPKO_00068", "FRACTION_OF_STOMACH"),
        "fraction of stomach",
        "A dimensionless fraction of volume defined as the stomach volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00069",
        ("PBPKO_00069", "VOLUME_OF_INTESTINE"),
        "volume of intestine",
        "A volume parameter representing the total volume of the intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00070",
        ("PBPKO_00070", "FRACTION_OF_INTESTINE"),
        "fraction of intestine",
        "A dimensionless fraction of volume defined as the intestine volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00071",
        ("PBPKO_00071", "VOLUME_OF_SMALL_INTESTINE"),
        "volume of small intestine",
        "A volume parameter representing the total volume of the small intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00072",
        ("PBPKO_00072", "FRACTION_OF_SMALL_INTESTINE"),
        "fraction of small intestine",
        "A dimensionless fraction of volume defined as the small intestine volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00073",
        ("PBPKO_00073", "VOLUME_OF_LARGE_INTESTINE"),
        "volume of large intestine",
        "A volume parameter representing the total volume of the large intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00074",
        ("PBPKO_00074", "FRACTION_OF_LARGE_INTESTINE"),
        "fraction of large intestine",
        "A dimensionless fraction of volume defined as the large intestine volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00075",
        ("PBPKO_00075", "VOLUME_OF_PANCREAS"),
        "volume of pancreas",
        "A volume parameter representing the total volume of the pancreas compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00076",
        ("PBPKO_00076", "FRACTION_OF_PANCREAS"),
        "fraction of pancreas",
        "A dimensionless fraction of volume defined as the pancreas volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00077",
        ("PBPKO_00077", "VOLUME_OF_LIVER"),
        "volume of liver",
        "A volume parameter representing the total volume of the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00078",
        ("PBPKO_00078", "FRACTION_OF_LIVER"),
        "fraction of liver",
        "A dimensionless fraction of volume defined as the liver volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00079",
        ("PBPKO_00079", "VOLUME_OF_KIDNEY"),
        "volume of kidney",
        "A volume parameter representing the total volume of the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00080",
        ("PBPKO_00080", "FRACTION_OF_KIDNEY"),
        "fraction of kidney",
        "A dimensionless fraction of volume defined as the kidney volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00081",
        ("PBPKO_00081", "VOLUME_OF_MUSCLE"),
        "volume of muscle",
        "A volume parameter representing the total volume of muscle compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00082",
        ("PBPKO_00082", "FRACTION_OF_MUSCLE"),
        "fraction of muscle",
        "A dimensionless fraction of volume defined as the muscle volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00083",
        ("PBPKO_00083", "VOLUME_OF_HEART"),
        "volume of heart",
        "A volume parameter representing the total volume of the heart compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00084",
        ("PBPKO_00084", "FRACTION_OF_HEART"),
        "fraction of heart",
        "A dimensionless fraction of volume defined as the heart volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00085",
        ("PBPKO_00085", "VOLUME_OF_FAT"),
        "volume of fat",
        "A volume parameter representing the total volume of fat (adipose tissue) compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00086",
        ("PBPKO_00086", "FRACTION_OF_FAT"),
        "fraction of fat",
        "A dimensionless fraction of volume defined as the fat volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00087",
        ("PBPKO_00087", "VOLUME_OF_GONAD"),
        "volume of gonad",
        "A volume parameter representing the total volume of the gonad compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00088",
        ("PBPKO_00088", "FRACTION_OF_GONAD"),
        "fraction of gonad",
        "A dimensionless fraction of volume defined as the gonad volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00089",
        ("PBPKO_00089", "VOLUME_OF_SKIN"),
        "volume of skin",
        "A volume parameter representing the total volume of the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00090",
        ("PBPKO_00090", "FRACTION_OF_SKIN"),
        "fraction of skin",
        "A dimensionless fraction of volume defined as the skin volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00091",
        ("PBPKO_00091", "VOLUME_OF_BONE"),
        "volume of bone",
        "A volume parameter representing the total volume of bone compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00092",
        ("PBPKO_00092", "FRACTION_OF_BONE"),
        "fraction of bone",
        "A dimensionless fraction of volume defined as the bone volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00093",
        ("PBPKO_00093", "VOLUME_OF_BRAIN"),
        "volume of brain",
        "A volume parameter representing the total volume of the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00094",
        ("PBPKO_00094", "FRACTION_OF_BRAIN"),
        "fraction of brain",
        "A dimensionless fraction of volume defined as the brain volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00095",
        ("PBPKO_00095", "VOLUME_OF_SPLEEN"),
        "volume of spleen",
        "A volume parameter representing the total volume of the spleen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00096",
        ("PBPKO_00096", "FRACTION_OF_SPLEEN"),
        "fraction of spleen",
        "A dimensionless fraction of volume defined as the spleen volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00097",
        ("PBPKO_00097", "VOLUME_OF_LUNG"),
        "volume of lung",
        "A volume parameter representing the total volume of the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00098",
        ("PBPKO_00098", "FRACTION_OF_LUNG"),
        "fraction of lung",
        "A dimensionless fraction of volume defined as the lung volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00099",
        ("PBPKO_00099", "VOLUME_OF_POORLY_PERFUSED"),
        "volume of poorly perfused",
        "A volume parameter representing the total volume of the poorly perfused compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00100",
        ("PBPKO_00100", "FRACTION_OF_POORLY_PERFUSED"),
        "fraction of poorly perfused",
        "A dimensionless fraction of volume defined as the poorly perfused compartment volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00101",
        ("PBPKO_00101", "VOLUME_OF_RICHLY_PERFUSED"),
        "volume of richly perfused",
        "A volume parameter representing the total volume of the richly perfused compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00102",
        ("PBPKO_00102", "FRACTION_OF_RICHLY_PERFUSED"),
        "fraction of richly perfused",
        "A dimensionless fraction of volume defined as the richly perfused compartment volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00103",
        ("PBPKO_00103", "VOLUME_OF_PLASMA"),
        "volume of plasma",
        "A volume parameter representing the total volume of plasma compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00104",
        ("PBPKO_00104", "FRACTION_OF_PLASMA"),
        "fraction of plasma",
        "A dimensionless fraction of volume defined as the plasma volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00105",
        ("PBPKO_00105", "VOLUME_OF_REST_BODY"),
        "volume of rest body",
        "A volume parameter representing the total volume of the rest of body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00106",
        ("PBPKO_00106", "FRACTION_OF_REST_BODY"),
        "fraction of rest body",
        "A dimensionless fraction of volume defined as the rest of body volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00107",
        ("PBPKO_00107", "VOLUME_OF_STRATUM_CORNEUM_WITH_RESPECT_TO_BLOOD"),
        "volume of stratum corneum with respect to blood",
        "A volume parameter representing the total volume of stratum corneum compartment with respect to blood/plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00108",
        ("PBPKO_00108", "VOLUME_OF_BLOOD"),
        "volume of blood",
        "A volume parameter representing the total volume of blood compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00109",
        ("PBPKO_00109", "VOLUME_OF_EXPOSED_SKIN"),
        "volume of exposed skin",
        "A volume parameter representing the total volume of the exposed skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00110",
        ("PBPKO_00110", "FRACTION_OF_SURFACE_AREA_EXPOSED"),
        "fraction of surface area exposed",
        "A surface area parameter representing the fraction of skin surface area actually exposed.",
        (),
        False,
    ),
    (
        "PBPKO_00111",
        ("PBPKO_00111", "VOLUME_OF_UNEXPOSED_SKIN"),
        "volume of unexposed skin",
        "A volume parameter representing the total volume of the unexposed skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00112",
        ("PBPKO_00112", "VOLUME_OF_STRATUM_CORNEUM_EXPOSED"),
        "volume of stratum corneum exposed",
        "A volume parameter representing the total volume of the exposed stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00113",
        ("PBPKO_00113", "VOLUME_OF_UNEXPOSED_STRATUM_CORNEUM"),
        "volume of unexposed stratum corneum",
        "A volume parameter representing the total volume of the unexposed stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00114",
        ("PBPKO_00114", "FRACTION_ALVEOLAR_VOLUME"),
        "fraction alveolar volume",
        "A dimensionless fraction of volume defined as the alveolar volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00115",
        ("PBPKO_00115", "VOLUME_OF_GALL_BLADDER"),
        "volume of gall bladder",
        "A volume parameter representing the total volume of the gall bladder compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00116",
        ("PBPKO_00116", "FRACTION_OF_GALL_BLADDER"),
        "fraction of gall bladder",
        "A dimensionless fraction of volume defined as the gall bladder volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00117",
        ("PBPKO_00117", "VOLUME_OF_PORTAL_VEIN"),
        "volume of portal vein",
        "A volume parameter representing the total volume of the portal vein compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00118",
        ("PBPKO_00118", "FRACTION_OF_PORTAL_VEIN"),
        "fraction of portal vein",
        "A dimensionless fraction of volume defined as the portal vein volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00119",
        ("PBPKO_00119", "VOLUME_OF_LYMPH"),
        "volume of lymph",
        "A volume parameter representing the total volume of lymph compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00120",
        ("PBPKO_00120", "FRACTION_OF_LYMPH"),
        "fraction of lymph",
        "A dimensionless fraction of volume defined as the lymph volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00121",
        ("PBPKO_00121", "ARTERIAL_VOLUME"),
        "arterial volume",
        "A volume parameter representing the total volume of the arterial compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00122",
        ("PBPKO_00122", "VENOUS_VOLUME"),
        "venous volume",
        "A volume parameter representing the total volume of the venous compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00126",
        ("PBPKO_00126", "PHYSICOCHEMICAL_PARAMETER"),
        "physicochemical parameter",
        "A parameter relating to the physical and chemical properties of a compound (e.g., MW, lipophilicity, solubility, pKa).",
        (),
        False,
    ),
    (
        "PBPKO_00127",
        ("PBPKO_00127", "MOLECULAR_WEIGHT"),
        "molecular weight",
        "A physicochemical parameter representing the sum of the weights of all atoms in a molecule.",
        (),
        False,
    ),
    (
        "PBPKO_00128",
        ("PBPKO_00128", "LIPOPHILLICITY"),
        "lipophillicity",
        "A physicochemical parameter representing the affinity or tendency of a compound to dissolve in lipids or hydrophobic environments.",
        (),
        False,
    ),
    (
        "PBPKO_00129",
        ("PBPKO_00129", "DISTRIBUTION_COEFFICIENT"),
        "distribution coefficient",
        "A physicochemical parameter representing the logarithm of the ratio of concentrations of a compound in a mixture of two immiscible phases at equilibrium, specifically describing lipophilicity (LogD).",
        (),
        False,
    ),
    (
        "PBPKO_00130",
        ("PBPKO_00130", "DISSOLUTION_IN_TWO_PHASE_SYSTEM"),
        "dissolution in two phase system",
        "A physicochemical parameter representing the ratio of a dissolved compound in a two-phase system (often used interchangeably with partition coefficient).",
        (),
        False,
    ),
    (
        "PBPKO_00131",
        ("PBPKO_00131", "LOGARITHMIC_SOLUBILITY"),
        "logarithmic solubility",
        "A physicochemical parameter representing the 10-based logarithm of a compound's solubility (typically in mol/L).",
        (),
        False,
    ),
    (
        "PBPKO_00132",
        ("PBPKO_00132", "WATER_SOLUBILITY"),
        "water solubility",
        "A physicochemical parameter representing the solubility of a compound specifically in water.",
        (),
        False,
    ),
    (
        "PBPKO_00133",
        ("PBPKO_00133", "ACID_DISSOCIATION_CONSTANT"),
        "acid dissociation constant",
        "A physicochemical parameter representing the negative base-10 logarithm (pKa) of the acid dissociation constant (Ka).",
        (),
        False,
    ),
    (
        "PBPKO_00134",
        ("PBPKO_00134", "BASIC_DISSOCIATION_CONSTANT"),
        "basic dissociation constant",
        "A physicochemical parameter representing the negative base-10 logarithm (pKb) of the base dissociation constant (Kb).",
        (),
        False,
    ),
    (
        "PBPKO_00135",
        ("PBPKO_00135", "PHYSIOLOGICAL_CHARGE"),
        "physiological charge",
        "A physicochemical parameter representing the electrical charge of a molecule at physiological pH.",
        (),
        False,
    ),
    (
        "PBPKO_00136",
        ("PBPKO_00136", "HYDROGEN_ACCEPTOR_COUNT"),
        "hydrogen acceptor count",
        "A physicochemical parameter representing the integer number of hydrogen bond acceptors in a molecular entity.",
        (),
        False,
    ),
    (
        "PBPKO_00137",
        ("PBPKO_00137", "HYDROGEN_DONOR_COUNT"),
        "hydrogen donor count",
        "A physicochemical parameter representing the integer number of hydrogen bond donors in a molecular entity.",
        (),
        False,
    ),
    (
        "PBPKO_00138",
        ("PBPKO_00138", "ROTATABLE_BOND_COUNT"),
        "rotatable bond count",
        "A physicochemical parameter representing the integer count of rotatable bonds in a molecular entity.",
        (),
        False,
    ),
    (
        "PBPKO_00139",
        ("PBPKO_00139", "BIOCHEMICAL_PARAMETER"),
        "biochemical parameter",
        "A parameter that is compound-dependent and relates to biological interactions or transformations (e.g., clearance, binding, partition coefficients).",
        (),
        False,
    ),
    (
        "PBPKO_00140",
        ("PBPKO_00140", "ABSORPTION"),
        "absorption",
        "A biological process by which a compound moves from its site of administration into the systemic circulation or a target tissue.",
        (),
        False,
    ),
    (
        "PBPKO_00141",
        ("PBPKO_00141", "ABSORPTION_RATE_CONSTANT_GUT"),
        "absorption rate constant gut",
        "An absorption rate constant parameter representing the rate constant for the movement of a compound from the gut to systemic circulation or another compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00142",
        ("PBPKO_00142", "ABSORPTION_RATE_CONSTANT_INTESTINE"),
        "absorption rate constant intestine",
        "An absorption rate constant parameter representing the movement of a compound from the intestine to systemic circulation or another compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00143",
        ("PBPKO_00143", "GASTRIC_EMPTYING_RATE"),
        "gastric emptying rate",
        "A biochemical parameter representing the rate at which the stomach empties its contents into the small intestine.",
        (),
        False,
    ),
    (
        "PBPKO_00144",
        ("PBPKO_00144", "ENTEROHEPATIC_RECIRCULATION"),
        "enterohepatic recirculation",
        "A biological process involving recycling of compounds through the liver via biliary excretion, intestinal reabsorption, portal circulation return, and re-excretion.",
        (),
        False,
    ),
    (
        "PBPKO_00145",
        ("PBPKO_00145", "SPECIFIC_INTESTINAL_PERMEABILITY"),
        "specific intestinal permeability",
        "A biochemical parameter representing the surface area-normalized transcellular permeability of the intestinal wall for a compound.",
        (),
        False,
    ),
    (
        "PBPKO_00146",
        ("PBPKO_00146", "DISTRIBUTION_PROCESS"),
        "distribution process",
        "A biological process describing the movement of a compound from systemic circulation to various organs/tissues.",
        (),
        False,
    ),
    (
        "PBPKO_00147",
        ("PBPKO_00147", "VOLUME_OF_DISTRIBUTION"),
        "volume of distribution",
        "A biochemical parameter representing the apparent volume into which a compound distributes in the body relative to its plasma concentration.",
        (),
        False,
    ),
    (
        "PBPKO_00148",
        ("PBPKO_00148", "PROTEIN_BINDING_MEDIATED_DISTRIBUTIION_PROCESS"),
        "protein binding mediated distributiion process",
        "A distribution process (or molecular function) where substances bind to proteins or related compounds.",
        (),
        False,
    ),
    (
        "PBPKO_00149",
        ("PBPKO_00149", "UNBOUND_FRACTION"),
        "unbound fraction",
        "A biochemical parameter representing the fraction of a compound that is not bound (e.g., to proteins).",
        (),
        False,
    ),
    (
        "PBPKO_00150",
        ("PBPKO_00150", "FRACTION_UNBOUND_GUT"),
        "fraction unbound gut",
        "An unbound fraction parameter specifically for the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00151",
        ("PBPKO_00151", "FRACTION_UNBOUND_STOMACH"),
        "fraction unbound stomach",
        "An unbound fraction parameter specifically for the stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00152",
        ("PBPKO_00152", "FRACTION_UNBOUND_INTESTINE"),
        "fraction unbound intestine",
        "An unbound fraction parameter specifically for the intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00153",
        ("PBPKO_00153", "FRACTION_UNBOUND_PANCREAS"),
        "fraction unbound pancreas",
        "An unbound fraction parameter specifically for the pancreas compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00154",
        ("PBPKO_00154", "FRACTION_UNBOUND_LIVER"),
        "fraction unbound liver",
        "An unbound fraction parameter specifically for the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00155",
        ("PBPKO_00155", "FRACTION_UNBOUND_KIDNEY"),
        "fraction unbound kidney",
        "An unbound fraction parameter specifically for the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00156",
        ("PBPKO_00156", "FRACTION_UNBOUND_MUSCLE"),
        "fraction unbound muscle",
        "An unbound fraction parameter specifically for the muscle compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00157",
        ("PBPKO_00157", "FRACTION_UNBOUND_HEART"),
        "fraction unbound heart",
        "An unbound fraction parameter specifically for the heart compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00158",
        ("PBPKO_00158", "FRACTION_UNBOUND_FAT"),
        "fraction unbound fat",
        "An unbound fraction parameter specifically for the fat (adipose) compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00159",
        ("PBPKO_00159", "FRACTION_UNBOUND_GONAD"),
        "fraction unbound gonad",
        "An unbound fraction parameter specifically for the gonad compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00160",
        ("PBPKO_00160", "FRACTION_UNBOUND_SKIN"),
        "fraction unbound skin",
        "An unbound fraction parameter specifically for the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00161",
        ("PBPKO_00161", "FRACTION_UNBOUND_BONE"),
        "fraction unbound bone",
        "An unbound fraction parameter specifically for the bone compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00162",
        ("PBPKO_00162", "FRACTION_UNBOUND_SPLEEN"),
        "fraction unbound spleen",
        "An unbound fraction parameter specifically for the spleen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00163",
        ("PBPKO_00163", "FRACTION_UNBOUND_LUNG"),
        "fraction unbound lung",
        "An unbound fraction parameter specifically for the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00164",
        ("PBPKO_00164", "FRACTION_UNBOUND_ENTEROCYTES"),
        "fraction unbound enterocytes",
        "An unbound fraction parameter specifically within enterocytes.",
        (),
        False,
    ),
    (
        "PBPKO_00165",
        ("PBPKO_00165", "PARTITION_COEFFICIENT"),
        "partition coefficient",
        "A biochemical parameter representing the ratio of the concentration of a compound in a particular tissue to its concentration in plasma/blood at equilibrium.",
        (),
        False,
    ),
    (
        "PBPKO_00166",
        ("PBPKO_00166", "GUT_PLASMA_PARTITION_COEFFICIENT"),
        "gut plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in gut to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00167",
        ("PBPKO_00167", "STOMACH_PLASMA_PARTITION_COEFFICIENT"),
        "stomach plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in stomach to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00168",
        ("PBPKO_00168", "INTESTINE_PLASMA_PARTITION_COEFFICIENT"),
        "intestine plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in intestine to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00169",
        ("PBPKO_00169", "PANCREAS_PLASMA_PARTITION_COEFFICIENT"),
        "pancreas plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in pancreas to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00170",
        ("PBPKO_00170", "LIVER_PLASMA_PARTITION_COEFFICIENT"),
        "liver plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in liver to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00171",
        ("PBPKO_00171", "KIDNEY_PLASMA_PARTITION_COEFFICIENT"),
        "kidney plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in kidney to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00172",
        ("PBPKO_00172", "MUSCLE_PLASMA_PARTITION_COEFFICIENT"),
        "muscle plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in muscle to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00173",
        ("PBPKO_00173", "HEART_PLASMA_PARTITION_COEFFICIENT"),
        "heart plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in heart to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00174",
        ("PBPKO_00174", "FAT_PLASMA_PARTITION_COEFFICIENT"),
        "fat plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in fat (adipose tissue) to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00175",
        ("PBPKO_00175", "GONAD_PLASMA_PARTITION_COEFFICIENT"),
        "gonad plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in gonads to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00176",
        ("PBPKO_00176", "SKIN_PLASMA_PARTITION_COEFFICIENT"),
        "skin plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in skin to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00177",
        ("PBPKO_00177", "BONE_PLASMA_PARTITION_COEFFICIENT"),
        "bone plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in bone to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00178",
        ("PBPKO_00178", "SPLEEN_PLASMA_PARTITION_COEFFICIENT"),
        "spleen plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in spleen to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00179",
        ("PBPKO_00179", "LUNG_PLASMA_PARTITION_COEFFICIENT"),
        "lung plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in lung to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00180",
        ("PBPKO_00180", "RICH_PERFUSED_PLASMA_PARTITION_COEFFICIENT"),
        "rich perfused plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the lumped richly perfused compartment to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00181",
        ("PBPKO_00181", "POOR_PERFUSED_PLASMA_PARTITION_COEFFICIENT"),
        "poor perfused plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the lumped poorly perfused compartment to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00182",
        ("PBPKO_00182", "SKIN_STRATUM_CORNEUM_PARTITION_COEFFICIENT"),
        "skin stratum corneum partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the stratum corneum to the rest of the skin.",
        (),
        False,
    ),
    (
        "PBPKO_00183",
        ("PBPKO_00183", "AIR_PLASMA_PARTITION_COEFFICIENT"),
        "air plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in air to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00184",
        ("PBPKO_00184", "SKIN_DIFFUSION_COEFFICIENT"),
        "skin diffusion coefficient",
        "A diffusion coefficient representing the diffusion of a compound across the skin.",
        (),
        False,
    ),
    (
        "PBPKO_00185",
        ("PBPKO_00185", "HUMAN_SERUM_ALBUMIN"),
        "human serum albumin",
        "A material entity representing distribution-related protein (most abundant in human plasma) that binds various compounds.",
        (),
        False,
    ),
    (
        "PBPKO_00187",
        ("PBPKO_00187", "BLOOD_PLASMA_RATIO"),
        "blood:plasma ratio",
        "A biochemical parameter representing the ratio of compound concentration in whole blood to that in plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00189",
        ("PBPKO_00189", "CATALYTIC_RATE_CONSTANT"),
        "catalytic rate constant",
        "A biochemical parameter quantifying enzymatic reaction velocity (kcat), representing the maximum number of substrate molecules converted per active site per unit time.",
        (),
        False,
    ),
    (
        "PBPKO_00191",
        ("PBPKO_00191", "PHASE_I_METABOLISM"),
        "phase I metabolism",
        "A metabolism process involving the conversion of exogenous substances to more polar metabolites, often via oxidation, reduction, or hydrolysis (e.g., by CYPs).",
        (),
        False,
    ),
    (
        "PBPKO_00200",
        ("PBPKO_00200", "PHASE_II"),
        "phase II",
        "A metabolism process involving the conjugation of phase I products (or parent compounds) to hydrophilic moieties to facilitate excretion.",
        (),
        False,
    ),
    (
        "PBPKO_00209",
        ("PBPKO_00209", "PHASE_III"),
        "phase III",
        "A metabolism/transport process involving the further processing and excretion of conjugated metabolites (often involving efflux transporters).",
        (),
        False,
    ),
    (
        "PBPKO_00210",
        ("PBPKO_00210", "FIRST_PASS_METABOLISM"),
        "first pass metabolism",
        "A metabolism process occurring at a specific location (e.g., liver, gut wall) after administration but before reaching systemic circulation, reducing the concentration of active compound.",
        (),
        False,
    ),
    (
        "PBPKO_00211",
        ("PBPKO_00211", "MAXIMUM_RATE_IN_INTESTINE"),
        "maximum rate in intestine",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the intestine when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    (
        "PBPKO_00212",
        ("PBPKO_00212", "MICHAELIS_CONSTANT__INTESTINE"),
        "Michaelis constant  intestine",
        "Michaelis constant representing the substrate concentration at which the reaction rate in the intestine is half of Vmax (Km).",
        (),
        False,
    ),
    (
        "PBPKO_00213",
        ("PBPKO_00213", "MAXIMUM_RATE_IN_LIVER"),
        "maximum rate in liver",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the liver when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    (
        "PBPKO_00214",
        ("PBPKO_00214", "MICHAELIS_CONSTANT__LIVER"),
        "Michaelis constant  liver",
        "Michaelis constant representing the substrate concentration at which the reaction rate in the liver is half of Vmax (Km).",
        (),
        False,
    ),
    (
        "PBPKO_00215",
        ("PBPKO_00215", "GUT_METABOLISM"),
        "gut metabolism",
        "A metabolism process specifically occurring within the gut.",
        (),
        False,
    ),
    (
        "PBPKO_00216",
        ("PBPKO_00216", "DISSOCIATION_CONSTANT"),
        "dissociation constant",
        "A biochemical parameter (Kd) measuring the affinity of a compound for its binding partner (e.g., receptor, protein).",
        (),
        False,
    ),
    (
        "PBPKO_00217",
        ("PBPKO_00217", "TRANSPORTER"),
        "transporter",
        "A material entity representing protein responsible for the import or export of compounds across cell membranes.",
        (),
        False,
    ),
    (
        "PBPKO_00218",
        ("PBPKO_00218", "OATP"),
        "oatp",
        "A transporter family (Organic Anion Transporting Polypeptides) involved in transporting organic anions.",
        (),
        False,
    ),
    (
        "PBPKO_00219",
        ("PBPKO_00219", "ABCC3"),
        "abcc3",
        "A transporter (ATP-binding cassette subfamily C member 3) involved in bile metabolism and transport.",
        (),
        False,
    ),
    (
        "PBPKO_00220",
        ("PBPKO_00220", "ABCC2"),
        "abcc2",
        "A transporter (ATP-binding cassette subfamily C member 2) involved in transporting various molecules across cell membranes.",
        (),
        False,
    ),
    (
        "PBPKO_00221",
        ("PBPKO_00221", "DEGRADATION_RATE_CONSTANT"),
        "degradation rate constant",
        "A biochemical parameter (kdeg) representing the rate constant for the degradation of a metabolizing enzyme or transporter.",
        (),
        False,
    ),
    (
        "PBPKO_00222",
        ("PBPKO_00222", "INHIBITION_CONSTANT"),
        "inhibition constant",
        "A biochemical parameter (Ki) representing the inhibition constant for a specific enzyme or transporter interaction.",
        (),
        False,
    ),
    (
        "PBPKO_00223",
        ("PBPKO_00223", "RENAL_EXCRETION"),
        "renal excretion",
        "An excretion process involving the elimination of compounds and metabolites primarily through urine via the kidneys.",
        (),
        False,
    ),
    (
        "PBPKO_00224",
        ("PBPKO_00224", "HEPATIC_EXCRETION"),
        "hepatic excretion",
        "An excretion process involving the elimination of compounds and metabolites via the liver (often into bile).",
        (),
        False,
    ),
    (
        "PBPKO_00225",
        ("PBPKO_00225", "FECAL_EXCRETION"),
        "fecal excretion",
        "An excretion process involving the elimination of compounds and metabolites through feces.",
        (),
        False,
    ),
    (
        "PBPKO_00226",
        ("PBPKO_00226", "EXHALATION"),
        "exhalation",
        "An excretion process involving the elimination of volatile compounds and metabolites through respiration.",
        (),
        False,
    ),
    (
        "PBPKO_00227",
        ("PBPKO_00227", "SWEAT_EXCRETION"),
        "sweat excretion",
        "An excretion process involving the elimination of compounds and metabolites through sweat.",
        (),
        False,
    ),
    (
        "PBPKO_00228",
        ("PBPKO_00228", "HAIR_EXCRETION"),
        "hair excretion",
        "An excretion process involving the elimination and deposition of compounds and metabolites into hair.",
        (),
        False,
    ),
    (
        "PBPKO_00229",
        ("PBPKO_00229", "CLEARANCE_RATE"),
        "clearance rate",
        "A biochemical parameter representing the volume of biological fluid cleared of a compound per unit time.",
        (),
        False,
    ),
    (
        "PBPKO_00230",
        ("PBPKO_00230", "FECAL_CLEARANCE_RATE"),
        "fecal clearance rate",
        "A clearance rate specifically quantifying elimination via feces.",
        (),
        False,
    ),
    (
        "PBPKO_00231",
        ("PBPKO_00231", "SWEAT_CLEARANCE_RATE"),
        "sweat clearance rate",
        "A clearance rate specifically quantifying elimination via sweat.",
        (),
        False,
    ),
    (
        "PBPKO_00232",
        ("PBPKO_00232", "URINARY_CLEARANCE_RATE"),
        "urinary clearance rate",
        "A clearance rate specifically quantifying elimination via urine.",
        (),
        False,
    ),
    (
        "PBPKO_00233",
        ("PBPKO_00233", "BILIARY_CLEARANCE_RATE"),
        "biliary clearance rate",
        "A clearance rate specifically quantifying elimination via bile.",
        (),
        False,
    ),
    (
        "PBPKO_00234",
        ("PBPKO_00234", "HEPATIC_CLEARANCE_RATE"),
        "hepatic clearance rate",
        "A clearance rate specifically quantifying elimination via the liver (metabolism and/or biliary excretion).",
        (),
        False,
    ),
    (
        "PBPKO_00235",
        ("PBPKO_00235", "INTRINSIC_CLEARANCE_RATE"),
        "intrinsic clearance rate",
        "A clearance rate representing the inherent ability of an organ or tissue to eliminate a compound, independent of blood flow or binding.",
        (),
        False,
    ),
    (
        "PBPKO_00236",
        ("PBPKO_00236", "FECAL_ELIMINATION_RATE_CONSTANT"),
        "fecal elimination rate constant",
        "A biochemical parameter representing the rate constant for elimination via fecal excretion.",
        (),
        False,
    ),
    (
        "PBPKO_00237",
        ("PBPKO_00237", "RENAL_ELIMINATION_RATE_CONSTANT"),
        "renal elimination rate constant",
        "A biochemical parameter representing the rate constant for elimination via renal (urinary) excretion.",
        (),
        False,
    ),
    (
        "PBPKO_00238",
        ("PBPKO_00238", "BILIARY_ELIMINATION"),
        "biliary elimination",
        "An elimination process involving the irreversible transfer of compound or metabolites from plasma to bile via hepatocytes.",
        (),
        False,
    ),
    (
        "PBPKO_00239",
        ("PBPKO_00239", "ROUTE_OF_EXPOSURE"),
        "route of exposure",
        "A parameter designating the body part or method through which exposure is introduced.",
        (),
        False,
    ),
    (
        "PBPKO_00240",
        ("PBPKO_00240", "ORAL_EXPOSURE"),
        "oral exposure",
        "A route of exposure via the mouth.",
        (),
        False,
    ),
    (
        "PBPKO_00241",
        ("PBPKO_00241", "DERMAL_EXPOSURE"),
        "dermal exposure",
        "A route of exposure via the skin.",
        (),
        False,
    ),
    (
        "PBPKO_00242",
        ("PBPKO_00242", "INHALATION_EXPOSURE"),
        "inhalation exposure",
        "A route of exposure via inhalation into the lungs.",
        (),
        False,
    ),
    (
        "PBPKO_00243",
        ("PBPKO_00243", "INTRAVENOUS_BOLUS_EXPOSURE"),
        "intravenous bolus exposure",
        "A route of exposure involving rapid injection directly into a vein.",
        (),
        False,
    ),
    (
        "PBPKO_00244",
        ("PBPKO_00244", "INTRAVENOUS_INFUSION_EXPOSURE"),
        "intravenous infusion exposure",
        "A route of exposure involving continuous administration directly into a vein over time.",
        (),
        False,
    ),
    (
        "PBPKO_00245",
        ("PBPKO_00245", "INTRAMUSCULAR_EXPOSURE"),
        "intramuscular exposure",
        "A route of exposure involving injection into a muscle.",
        (),
        False,
    ),
    (
        "PBPKO_00246",
        ("PBPKO_00246", "INTRAARTERIAL_EXPOSURE"),
        "intraarterial exposure",
        "A route of exposure involving administration directly into an artery.",
        (),
        False,
    ),
    (
        "PBPKO_00247",
        ("PBPKO_00247", "INTRATHECAL_EXPOSURE"),
        "intrathecal exposure",
        "A route of exposure involving administration into the spinal canal.",
        (),
        False,
    ),
    (
        "PBPKO_00248",
        ("PBPKO_00248", "SUBCUTANEOUS_EXPOSURE"),
        "subcutaneous exposure",
        "A route of exposure involving administration under the skin.",
        (),
        False,
    ),
    (
        "PBPKO_00249",
        ("PBPKO_00249", "NASAL_EXPOSURE"),
        "nasal exposure",
        "A route of exposure via the nasal passages.",
        (),
        False,
    ),
    (
        "PBPKO_00250",
        ("PBPKO_00250", "TRANSDERMAL_EXPOSURE"),
        "transdermal exposure",
        "A route of exposure involving absorption through the skin, typically from a patch.",
        (),
        False,
    ),
    (
        "PBPKO_00251",
        ("PBPKO_00251", "OCULAR_EXPOSURE"),
        "ocular exposure",
        "A route of exposure via the eye.",
        (),
        False,
    ),
    (
        "PBPKO_00252",
        ("PBPKO_00252", "OUTPUT_PARAMETER"),
        "output parameter",
        "A parameter representing a result or prediction generated by the PBPK model.",
        (),
        False,
    ),
    (
        "PBPKO_00253",
        ("PBPKO_00253", "PEAK_CONCENTRATION"),
        "peak concentration",
        "An output parameter representing the highest concentration (Cmax) of a compound achieved after exposure.",
        (),
        False,
    ),
    (
        "PBPKO_00254",
        ("PBPKO_00254", "MAXIMUM_STEADY_STATE_CONCENTRATION"),
        "maximum steady state concentration",
        "An output parameter representing the maximum concentration (Cmax,ss) achieved at steady state during repeated dosing.",
        (),
        False,
    ),
    (
        "PBPKO_00255",
        ("PBPKO_00255", "MAXIMUM_TIME"),
        "maximum time",
        "An output parameter representing the time (Tmax) required to reach the peak concentration.",
        (),
        False,
    ),
    (
        "PBPKO_00256",
        ("PBPKO_00256", "AREA_UNDER_CURVE"),
        "area under curve",
        "An output parameter representing the integral of the concentration-time curve (AUC), indicating total exposure.",
        (),
        False,
    ),
    (
        "PBPKO_00257",
        ("PBPKO_00257", "AREA_UNDER_CURVE_0_TO_T"),
        "area under curve 0 to t",
        "An area under curve parameter calculated from time zero to a specific time point t (AUC0-t).",
        (),
        False,
    ),
    (
        "PBPKO_00258",
        ("PBPKO_00258", "AREA_UNDER_CURVE_LAST"),
        "area under curve last",
        "An area under curve parameter calculated from time zero to the time of the last measurable concentration (AUClast).",
        (),
        False,
    ),
    (
        "PBPKO_00259",
        ("PBPKO_00259", "AREA_UNDER_CURVE_0_TO_INFINITY"),
        "area under curve 0 to infinity",
        "An area under curve parameter extrapolated from time zero to infinity (AUC0-inf), representing total exposure after a single dose.",
        (),
        False,
    ),
    (
        "PBPKO_00260",
        ("PBPKO_00260", "AREA_UNDER_MOMENT_CURVE"),
        "area under moment curve",
        "An output parameter calculated as the integral of the product of time and concentration versus time (AUMC).",
        (),
        False,
    ),
    (
        "PBPKO_00261",
        ("PBPKO_00261", "MEAN_RESIDENCE_TIME"),
        "mean residence time",
        "An output parameter representing the average time a compound resides in the body (MRT).",
        (),
        False,
    ),
    (
        "PBPKO_00262",
        ("PBPKO_00262", "HALF_LIFE"),
        "half-life",
        "An output parameter representing the time required for the compound concentration to decrease by half (t1/2).",
        (),
        False,
    ),
    (
        "PBPKO_00263",
        ("PBPKO_00263", "BIOAVAILABILITY"),
        "bioavailability",
        "An output parameter representing the rate and extent to which an active compound is absorbed and becomes available at the site of action or systemic circulation.",
        (),
        False,
    ),
    (
        "PBPKO_00264",
        ("PBPKO_00264", "RELATIVE_BIOAVAILABILITY"),
        "relative bioavailability",
        "A bioavailability parameter comparing the rate and extent of absorption of a test compound to a reference compound.",
        (),
        False,
    ),
    (
        "PBPKO_00265",
        ("PBPKO_00265", "MEAN_ABSORPTION_TIME"),
        "mean absorption time",
        "An output parameter representing the average time for a compound to be absorbed into systemic circulation (MAT).",
        (),
        False,
    ),
    (
        "PBPKO_00266",
        ("PBPKO_00266", "MEAN_DISSOLUTION_TIME"),
        "mean dissolution time",
        "An output parameter representing the average time for a compound to dissolve in the body (MDT).",
        (),
        False,
    ),
    (
        "PBPKO_00267",
        ("PBPKO_00267", "BIOEQUIVALENCE"),
        "bioequivalence",
        "An output parameter indicating comparable bioavailability between test and reference formulations under similar conditions.",
        (),
        False,
    ),
    (
        "PBPKO_00268",
        ("PBPKO_00268", "ABSOLUTE_BIOAVAILABILITY"),
        "absolute bioavailability",
        "A bioavailability parameter comparing the amount reaching systemic circulation after non-IV administration to the amount available after IV administration.",
        (),
        False,
    ),
    (
        "PBPKO_00269",
        ("PBPKO_00269", "ELIMINATION_PHASE"),
        "elimination phase",
        "An elimination process phase describing the period where removal of the compound from the body predominates.",
        (),
        False,
    ),
    (
        "PBPKO_00270",
        ("PBPKO_00270", "ABSORPTION_PHASE"),
        "absorption phase",
        "An absorption process phase describing the period where the compound moves from the administration site into systemic circulation.",
        (),
        False,
    ),
    (
        "PBPKO_00272",
        ("PBPKO_00272", "AMOUNT_IN_URINE"),
        "amount in urine",
        "The amount of compound in the urine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00273",
        ("PBPKO_00273", "AMOUNT_IN_FECES"),
        "amount in feces",
        "The amount of compound in the feces compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00274",
        ("PBPKO_00274", "CUMULATIVE_AMOUNT_IN_URINE"),
        "cumulative amount in urine",
        "An output parameter representing the total amount of compound excreted in urine over a specific time period.",
        (),
        False,
    ),
    (
        "PBPKO_00275",
        ("PBPKO_00275", "CUMULATIVE_AMOUNT_IN_FECES"),
        "cumulative amount in feces",
        "An output parameter representing the total amount of compound excreted in feces over a specific time period.",
        (),
        False,
    ),
    (
        "PBPKO_00277",
        ("PBPKO_00277", "STEADY_STATE_AREA_UNDER_CURVE"),
        "steady state area under curve",
        "An area under curve parameter calculated over a dosing interval at steady state (AUCss).",
        (),
        False,
    ),
    (
        "PBPKO_00279",
        ("PBPKO_00279", "MIN_ORGAN_CONCENTRATION"),
        "min organ concentration",
        "An output parameter representing the minimum concentration of a compound in a specific organ after exposure.",
        (),
        False,
    ),
    (
        "PBPKO_00280",
        ("PBPKO_00280", "MAX_ORGAN_CONCENTRATION"),
        "max organ concentration",
        "An output parameter representing the maximum concentration of a compound in a specific organ after exposure.",
        (),
        False,
    ),
    (
        "PBPKO_00281",
        ("PBPKO_00281", "MEDIAN_ORGAN_CONCENTRATION"),
        "median organ concentration",
        "An output parameter representing the median concentration of a compound in a specific organ after exposure.",
        (),
        False,
    ),
    (
        "PBPKO_00282",
        ("PBPKO_00282", "PERCENTILE_2_5_CPLASMA"),
        "percentile 2.5 cplasma",
        "A plasma concentration parameter representing the 2.5th percentile of the plasma concentration distribution in a population simulation.",
        (),
        False,
    ),
    (
        "PBPKO_00283",
        ("PBPKO_00283", "PERCENTILE_97_5_CPLASMA"),
        "percentile 97.5 cplasma",
        "A plasma concentration parameter representing the 97.5th percentile of the plasma concentration distribution in a population simulation.",
        (),
        False,
    ),
    (
        "PBPKO_00284",
        ("PBPKO_00284", "TOLERABLE_DAILY_INTAKE"),
        "tolerable daily intake",
        "An output parameter (or exposure limit) estimating the amount of a substance that can be ingested daily over a lifetime without appreciable health risk (TDI).",
        (),
        False,
    ),
    (
        "PBPKO_00285",
        ("PBPKO_00285", "RECONSTRUCTED_EXPOSURE"),
        "reconstructed exposure",
        "An output parameter estimating the amount of compound exposure based on internal body measurements.",
        (),
        False,
    ),
    (
        "PBPKO_00286",
        ("PBPKO_00286", "ESTIMATED_DAILY_INTAKE"),
        "estimated daily intake",
        "An output parameter estimating the amount of a compound consumed daily (EDI).",
        (),
        False,
    ),
    (
        "PBPKO_00287",
        ("PBPKO_00287", "BIOMONITORING_EQUIVALENT"),
        "biomonitoring equivalent",
        "An output parameter representing the concentration of a chemical (or metabolite) in a biological medium consistent with exposure guidance values (BE).",
        (),
        False,
    ),
    (
        "PBPKO_00289",
        ("PBPKO_00289", "REFERENCE_DOSE"),
        "reference dose",
        "An output parameter (or exposure limit) estimating the daily oral or dermal exposure likely to be without appreciable risk over a lifetime (RfD).",
        (),
        False,
    ),
    (
        "PBPKO_00290",
        ("PBPKO_00290", "ACCEPTABLE_DAILY_INTAKE"),
        "acceptable daily intake",
        "An output parameter (or exposure limit) estimating the amount of a substance in food/water that can be consumed daily without appreciable health risk (ADI).",
        (),
        False,
    ),
    (
        "PBPKO_00296",
        ("PBPKO_00296", "REFERENCE_HUMAN_DATA_SET"),
        "reference human data set",
        "A data set containing the physiological parameters representing a standard human, often defined by specific characteristics like 70 kg body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00297",
        ("PBPKO_00297", "BIOLOGICAL_MATRIX_CONCENTRATION"),
        "biological matrix concentration",
        "An output parameter representing the total concentration of a compound in a specified biological matrix.",
        (),
        False,
    ),
    (
        "PBPKO_00298",
        ("PBPKO_00298", "CONCENTRATION_IN_HAIR"),
        "concentration in hair",
        "The total concentration of compound in the hair compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00299",
        ("PBPKO_00299", "CONCENTRATION_IN_NAIL"),
        "concentration in nail",
        "A biological matrix concentration specifically representing the total concentration of compound in the nail compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00300",
        ("PBPKO_00300", "CONCENTRATION_IN_TEETH"),
        "concentration in teeth",
        "A biological matrix concentration specifically representing the total concentration of compound in the teeth compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00301",
        ("PBPKO_00301", "CONCENTRATION_IN_BLOOD"),
        "concentration in blood",
        "The total concentration of compound in the blood compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00302",
        ("PBPKO_00302", "CONCENTRATION_IN_URINE"),
        "concentration in urine",
        "A biological matrix concentration specifically representing the total concentration of compound in the urine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00303",
        ("PBPKO_00303", "PERMEABILITY_LIMITED_PBPK"),
        "permeability limited pbpk",
        "A physiologically based pharmacokinetic model that considers the permeability across membranes as a limiting factor for compound distribution.",
        (),
        False,
    ),
    (
        "PBPKO_00304",
        ("PBPKO_00304", "MAXIMUM_RATE_OF_BASOLATERAL_TRANSPORTER_IN_VITRO"),
        "maximum rate of basolateral transporter in vitro",
        "Maximum rate (Vmax) of transport via a basolateral transporter, measured in vitro.",
        (),
        False,
    ),
    (
        "PBPKO_00305",
        ("PBPKO_00305", "MICHAELIS_CONSTANT_BASO"),
        "Michaelis constant baso",
        "Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for a basolateral transporter.",
        (),
        False,
    ),
    (
        "PBPKO_00306",
        ("PBPKO_00306", "MAXIMUM_RATE_OF_APICAL_TRANSPORTER_IN_VITRO"),
        "maximum rate of apical transporter in vitro",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ, measured in vitro, when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    (
        "PBPKO_00307",
        ("PBPKO_00307", "MICHAELIS_CONSTANT_APICAL"),
        "Michaelis constant apical",
        "Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for an apical transporter.",
        (),
        False,
    ),
    (
        "PBPKO_00310",
        ("PBPKO_00310", "INFLUX_CONSTANT"),
        "influx constant",
        "A biochemical parameter (kin) describing the rate constant for compound movement into a cell or compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00311",
        ("PBPKO_00311", "EFFLUX_RATE_CONSTANT"),
        "efflux rate constant",
        "A biochemical parameter (kefflux) describing the rate constant for compound movement out of a cell or compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00312",
        ("PBPKO_00312", "PLASMA_SPACE"),
        "plasma space",
        "A physiological parameter representing the volume occupied by plasma within a tissue or the body.",
        (),
        False,
    ),
    (
        "PBPKO_00313",
        ("PBPKO_00313", "ENDOSOMAL_SPACE_COMPARTMENT"),
        "endosomal space compartment",
        "A compartment representing the endosomal space within cells.",
        (),
        False,
    ),
    (
        "PBPKO_00314",
        ("PBPKO_00314", "INTERSTITIAL_SPACE"),
        "interstitial space",
        "A physiological parameter representing the fluid-filled space between blood vessels and cells.",
        (),
        False,
    ),
    (
        "PBPKO_00315",
        ("PBPKO_00315", "EFFECTIVE_PERMEABILITY"),
        "effective permeability",
        "A biochemical parameter (Peff) representing the rate at which a compound passes through a biological barrier (e.g., intestinal wall).",
        (),
        False,
    ),
    (
        "PBPKO_00316",
        ("PBPKO_00316", "POPULATION_PBPK"),
        "population pbpk",
        "A physiologically based pharmacokinetic model approach used to characterize interindividual variability within a population.",
        (),
        False,
    ),
    (
        "PBPKO_00317",
        ("PBPKO_00317", "TOP_DOWN_PBPK"),
        "top-down pbpk",
        "A physiologically based pharmacokinetic model approach primarily based on fitting observed clinical data, often empirical.",
        (),
        False,
    ),
    (
        "PBPKO_00318",
        ("PBPKO_00318", "BOTTOM_UP_PBPK"),
        "bottom-up pbpk",
        "A physiologically based pharmacokinetic model approach built mechanistically using in vitro and physiological data.",
        (),
        False,
    ),
    (
        "PBPKO_00319",
        ("PBPKO_00319", "ONE_COMPARTMENT_PBPK"),
        "one-compartment pbpk",
        "A physiologically based pharmacokinetic model that treats the entire body as a single, kinetically homogenous unit (central compartment).",
        (),
        False,
    ),
    (
        "PBPKO_00320",
        ("PBPKO_00320", "CENTRAL_COMPARTMENT"),
        "central compartment",
        "A compartment in a multi-compartment model representing plasma and highly perfused tissues where distribution is rapid.",
        (),
        False,
    ),
    (
        "PBPKO_00321",
        ("PBPKO_00321", "PERIPHERAL_COMPARTMENT"),
        "peripheral compartment",
        "A compartment in a multi-compartment model representing tissues where compound distribution is slower compared to the central compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00322",
        ("PBPKO_00322", "ELIMINATION"),
        "elimination",
        "A biological process involving the irreversible removal of a compound from the body, encompassing metabolism and excretion.",
        (),
        False,
    ),
    (
        "PBPKO_00323",
        ("PBPKO_00323", "LINEAR_ELIMINATION"),
        "linear elimination",
        "An elimination process that follows first-order kinetics (rate proportional to concentration).",
        (),
        False,
    ),
    (
        "PBPKO_00324",
        ("PBPKO_00324", "NON_LINEAR_ELIMINATION"),
        "non-linear elimination",
        "An elimination process that does not follow first-order kinetics (e.g., saturable processes).",
        (),
        False,
    ),
    (
        "PBPKO_00332",
        ("PBPKO_00332", "LIFESTAGE"),
        "lifestage",
        "A physiological parameter representing distinct phases of an individual's life (e.g., infant, adult, geriatric).",
        (),
        False,
    ),
    (
        "PBPKO_00333",
        ("PBPKO_00333", "FETUS_LIFESTAGE"),
        "fetus lifestage",
        "A lifestage parameter representing the unborn offspring from the postembryonic stage until birth.",
        (),
        False,
    ),
    (
        "PBPKO_00334",
        ("PBPKO_00334", "INFANT_LIFESTAGE"),
        "infant lifestage",
        "A lifestage parameter representing a very young child, typically under one year of age.",
        (),
        False,
    ),
    (
        "PBPKO_00335",
        ("PBPKO_00335", "TODDLER_LIFESTAGE"),
        "toddler lifestage",
        "A lifestage parameter representing a young child, typically between one and three years old.",
        (),
        False,
    ),
    (
        "PBPKO_00336",
        ("PBPKO_00336", "CHILD_LIFESTAGE"),
        "child lifestage",
        "A lifestage parameter representing individuals typically between 3 and 11 years old.",
        (),
        False,
    ),
    (
        "PBPKO_00337",
        ("PBPKO_00337", "TEENAGER_LIFESTAGE"),
        "teenager lifestage",
        "A lifestage parameter representing individuals typically between eleven and fifteen years old.",
        (),
        False,
    ),
    (
        "PBPKO_00338",
        ("PBPKO_00338", "ADOLESCENT_LIFESTAGE"),
        "adolescent lifestage",
        "A lifestage parameter representing the transitional stage between teenager and adulthood (approx. 15-18 years).",
        (),
        False,
    ),
    (
        "PBPKO_00339",
        ("PBPKO_00339", "ADULT_LIFESTAGE"),
        "adult lifestage",
        "A lifestage parameter representing individuals typically from eighteen to thirty years old.",
        (),
        False,
    ),
    (
        "PBPKO_00340",
        ("PBPKO_00340", "MIDDLE_AGE_LIFESTAGE"),
        "middle age lifestage",
        "A lifestage parameter representing individuals typically from thirty to forty-five years old.",
        (),
        False,
    ),
    (
        "PBPKO_00341",
        ("PBPKO_00341", "OLD_AGE_LIFESTAGE"),
        "old age lifestage",
        "A lifestage parameter representing individuals typically from forty-five to sixty years old (or older, definitions vary).",
        (),
        False,
    ),
    (
        "PBPKO_00342",
        ("PBPKO_00342", "PEDIATRIC_LIFESTAGE"),
        "pediatric lifestage",
        "A lifestage parameter representing individuals typically below fifteen years of age.",
        (),
        False,
    ),
    (
        "PBPKO_00343",
        ("PBPKO_00343", "GERIATRIC_LIFESTAGE"),
        "geriatric lifestage",
        "A lifestage parameter representing older adults, often considered 60/65 years and older.",
        (),
        False,
    ),
    (
        "PBPKO_00347",
        ("PBPKO_00347", "BRAIN_PBPK"),
        "brain pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations in the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00348",
        ("PBPKO_00348", "CEREBROSPINAL_FLUID_VOLUME"),
        "cerebrospinal fluid volume",
        "A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the spinal region.",
        (),
        False,
    ),
    (
        "PBPKO_00349",
        ("PBPKO_00349", "CRANIAL_CEREBROSPINAL_FLUID_VOLUME"),
        "cranial cerebrospinal fluid volume",
        "A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the cranial region.",
        (),
        False,
    ),
    (
        "PBPKO_00350",
        ("PBPKO_00350", "BRAIN_MASS"),
        "brain mass",
        "A physiological parameter representing the mass of the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00351",
        ("PBPKO_00351", "BLOOD_BRAIN_BARRIER_COMPARTMENT"),
        "blood brain barrier compartment",
        "A barrier compartment representing the blood-brain barrier (BBB).",
        (),
        False,
    ),
    (
        "PBPKO_00352",
        ("PBPKO_00352", "SPINAL_CEREBROSPINAL_FLUID_FLOW_RATE"),
        "spinal cerebrospinal fluid flow rate",
        "A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the spinal region.",
        (),
        False,
    ),
    (
        "PBPKO_00353",
        ("PBPKO_00353", "CRANIAL_CEREBROSPINAL_FLUID_FLOW_RATE"),
        "cranial cerebrospinal fluid flow rate",
        "A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the cranial region.",
        (),
        False,
    ),
    (
        "PBPKO_00354",
        ("PBPKO_00354", "BLOOD_CEREBROSPINAL_FLUID_COMPARTMENT"),
        "blood cerebrospinal fluid compartment",
        "A barrier compartment representing the blood-cerebrospinal fluid barrier (BCSFB).",
        (),
        False,
    ),
    (
        "PBPKO_00355",
        ("PBPKO_00355", "VOLUME_OF_HIPPOCAMPUS"),
        "volume of hippocampus",
        "A volume parameter representing the total volume of the hippocampus compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00356",
        ("PBPKO_00356", "VOLUME_OF_FRONTAL_CORTEX"),
        "volume of frontal cortex",
        "A volume parameter representing the total volume of the frontal cortex compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00357",
        ("PBPKO_00357", "VOLUME_OF_CEREBRUM"),
        "volume of cerebrum",
        "A volume parameter representing the total volume of the cerebrum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00358",
        ("PBPKO_00358", "VOLUME_OF_CEREBELLUM"),
        "volume of cerebellum",
        "A volume parameter representing the total volume of the cerebellum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00359",
        ("PBPKO_00359", "BLOOD_FLOW_RATE_TO_HIPPOCAMPUS"),
        "blood flow rate to hippocampus",
        "A blood flow rate parameter specifically describing the rate to the hippocampus compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00360",
        ("PBPKO_00360", "BLOOD_FLOW_RATE_TO_FRONTAL_CORTEX"),
        "blood flow rate to frontal cortex",
        "A blood flow rate parameter specifically describing the rate to the frontal cortex compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00361",
        ("PBPKO_00361", "BLOOD_FLOW_RATE_TO_CEREBRUM"),
        "blood flow rate to cerebrum",
        "A blood flow rate parameter specifically describing the rate to the cerebrum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00362",
        ("PBPKO_00362", "BLOOD_FLOW_RATE_TO_CEREBELLUM"),
        "blood flow rate to cerebellum",
        "A blood flow rate parameter specifically describing the rate to the cerebellum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00363",
        ("PBPKO_00363", "HIPPOCAMPUS_BRAIN_PARTITION_COEFFICIENT"),
        "hippocampus brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the hippocampus to the overall brain.",
        (),
        False,
    ),
    (
        "PBPKO_00364",
        ("PBPKO_00364", "CEREBRUM_BRAIN_PARTITION_COEFFICIENT"),
        "cerebrum brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the cerebrum to the overall brain.",
        (),
        False,
    ),
    (
        "PBPKO_00365",
        ("PBPKO_00365", "CEREBELLUM_BRAIN_PARTITION_COEFFICIENT"),
        "cerebellum brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the cerebellum to the overall brain.",
        (),
        False,
    ),
    (
        "PBPKO_00366",
        ("PBPKO_00366", "FRONTALCORTEX_BRAIN_PARTITION_COEFFICIENT"),
        "frontalcortex brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the frontal cortex to the overall brain.",
        (),
        False,
    ),
    (
        "PBPKO_00367",
        ("PBPKO_00367", "APPARENT_PERMEABILITY_CEREBRUM_TO_REST_OF_BRAIN"),
        "apparent permeability cerebrum to rest of brain",
        "Apparent permeability of a compound specifically between the cerebrum and the rest of the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00368",
        ("PBPKO_00368", "APPARENT_PERMEABILITY_CEREBELLUM_TO_REST_OF_BRAIN"),
        "apparent permeability cerebellum to rest of brain",
        "Apparent permeability of a compound specifically between the cerebellum and the rest of the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00369",
        ("PBPKO_00369", "APPARENT_PERMEABILITY_HIPPOCAMPUS_TO_REST_OF_BRAIN"),
        "apparent permeability hippocampus to rest of brain",
        "Apparent permeability of a compound specifically between the hippocampus and the rest of the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00370",
        ("PBPKO_00370", "APPARENT_PERMEABILITY_CORTEX_TO_REST_OF_BRAIN"),
        "apparent permeability cortex to rest of brain",
        "Apparent permeability of a compound specifically between the cortex and the rest of the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00371",
        ("PBPKO_00371", "PREGNANT_PBPK"),
        "pregnant pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations during pregnancy.",
        (),
        False,
    ),
    (
        "PBPKO_00372",
        ("PBPKO_00372", "FETOPLACENTAL_VOLUME"),
        "fetoplacental volume",
        "A volume parameter representing the total volume of the placental compartment for fetus.",
        (),
        False,
    ),
    (
        "PBPKO_00373",
        ("PBPKO_00373", "VOLUME_OF_FETUS"),
        "volume of fetus",
        "A volume parameter representing the total volume of the fetus.",
        (),
        False,
    ),
    (
        "PBPKO_00374",
        ("PBPKO_00374", "VOLUME_OF_PLACENTA"),
        "volume of placenta",
        "A volume parameter representing the total volume of the placental compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00375",
        ("PBPKO_00375", "VOLUME_OF_AMNIOTIC_FLUID"),
        "volume of amniotic fluid",
        "A volume parameter representing the total volume of the amniotic fluid compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00376",
        ("PBPKO_00376", "VOLUME_OF_LIVER_FETUS"),
        "volume of liver fetus",
        "A volume parameter representing the total volume of the fetal liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00377",
        ("PBPKO_00377", "VOLUME_OF_BRAIN_FETUS"),
        "volume of brain fetus",
        "A volume parameter representing the total volume of the fetal brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00378",
        ("PBPKO_00378", "VOLUME_OF_KIDNEY_FETUS"),
        "volume of kidney fetus",
        "A volume parameter representing the total volume of the fetal kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00379",
        ("PBPKO_00379", "VOLUME_OF_REST_BODY_FETUS"),
        "volume of rest body fetus",
        "A volume parameter representing the total volume of the rest of body compartment within the fetus.",
        (),
        False,
    ),
    (
        "PBPKO_00381",
        ("PBPKO_00381", "FETOPLACENTAL_BLOOD_FLOW_RATE"),
        "fetoplacental blood flow rate",
        "A blood flow rate parameter representing the rate of blood flow between the fetus and the placenta compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00382",
        ("PBPKO_00382", "FETAL_CARDIAC_OUTPUT_RATE"),
        "fetal cardiac output rate",
        "A blood flow rate parameter representing the volume of blood pumped by the fetal heart compartment per unit time.",
        (),
        False,
    ),
    (
        "PBPKO_00383",
        ("PBPKO_00383", "BLOOD_FLOW_RATE_TO_LIVERFETUS"),
        "blood flow rate to liverfetus",
        "A blood flow rate parameter specifically describing the rate to the fetal liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00384",
        ("PBPKO_00384", "BLOOD_FLOW_RATE_TO_KIDNEYFETUS"),
        "blood flow rate to kidneyfetus",
        "A blood flow rate parameter specifically describing the rate to the fetal kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00385",
        ("PBPKO_00385", "BLOOD_FLOW_RATE_TO_BRAIN_FETUS"),
        "blood flow rate to brain fetus",
        "A blood flow rate parameter specifically describing the rate to the fetal brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00386",
        ("PBPKO_00386", "BLOOD_FLOW_RATE_TO_RESTBODY_FETUS"),
        "blood flow rate to restbody fetus",
        "A blood flow rate parameter specifically describing the rate to the rest of body compartment within the fetus.",
        (),
        False,
    ),
    (
        "PBPKO_00387",
        ("PBPKO_00387", "GESTATIONAL_AGE"),
        "gestational age",
        "A physiological parameter representing the age of a pregnancy, typically measured in weeks.",
        (),
        False,
    ),
    (
        "PBPKO_00388",
        ("PBPKO_00388", "GESTATIONAL_WEEK"),
        "gestational week",
        "A physiological parameter representing the specific week of gestation.",
        (),
        False,
    ),
    (
        "PBPKO_00389",
        ("PBPKO_00389", "MAXIMUM_RATE_IN_FETUS"),
        "maximum rate in fetus",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in fetus when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    (
        "PBPKO_00390",
        ("PBPKO_00390", "AMNIOTIC_TRANSFER_COEFFICIENT"),
        "amniotic transfer coefficient",
        "A biochemical parameter representing the rate at which a compound transfers from maternal circulation to amniotic fluid.",
        (),
        False,
    ),
    (
        "PBPKO_00391",
        ("PBPKO_00391", "LIVERFETUS_PLASMA_PARTITION_COEFFICIENT"),
        "liverfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal liver to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00392",
        ("PBPKO_00392", "BRAINFETUS_PLASMA_PARTITION_COEFFICIENT"),
        "brainfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal brain to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00393",
        ("PBPKO_00393", "KIDNEYFETUS_PLASMA_PARTITION_COEFFICIENT"),
        "kidneyfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal kidney to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00394",
        ("PBPKO_00394", "RESTBODYFETUS_PLASMA_PARTITION_COEFFICIENT"),
        "restbodyfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00395",
        ("PBPKO_00395", "KIDNEY_PBPK"),
        "kidney pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the kidney compartments.",
        (),
        False,
    ),
    (
        "PBPKO_00396",
        ("PBPKO_00396", "BOWMAN_S_CAPSULE_COMPARTMENT"),
        "Bowman's capsule compartment",
        "A kidney compartment representing the Bowman's capsule.",
        (),
        False,
    ),
    (
        "PBPKO_00397",
        ("PBPKO_00397", "FILTRATE_COMPARTMENT"),
        "filtrate compartment",
        "A kidney compartment representing the filtrate within the nephron.",
        (),
        False,
    ),
    (
        "PBPKO_00398",
        ("PBPKO_00398", "PROXIMAL_TUBULE_COMPARTMENT"),
        "proximal tubule compartment",
        "A kidney compartment representing the proximal tubule of the nephron.",
        (),
        False,
    ),
    (
        "PBPKO_00399",
        ("PBPKO_00399", "LOOP_OF_HENLE_COMPARTMENT"),
        "loop of Henle compartment",
        "A kidney compartment representing the loop of Henle within the nephron.",
        (),
        False,
    ),
    (
        "PBPKO_00400",
        ("PBPKO_00400", "DISTAL_TUBULE_COMPARTMENT"),
        "distal tubule compartment",
        "A kidney compartment representing the distal tubule of the nephron.",
        (),
        False,
    ),
    (
        "PBPKO_00401",
        ("PBPKO_00401", "COLLECTING_DUCT_COMPARTMENT"),
        "collecting duct compartment",
        "A kidney compartment representing the collecting duct system.",
        (),
        False,
    ),
    (
        "PBPKO_00402",
        ("PBPKO_00402", "BLADDER_COMPARTMENT"),
        "bladder compartment",
        "A compartment representing the urinary bladder.",
        (),
        False,
    ),
    (
        "PBPKO_00403",
        ("PBPKO_00403", "LUNG_PBPK"),
        "lung pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the lung compartments.",
        (),
        False,
    ),
    (
        "PBPKO_00404",
        ("PBPKO_00404", "EXTRATHORACIC_COMPARTMENT"),
        "extrathoracic compartment",
        "A compartment representing the extrathoracic region (head, neck, upper respiratory tract).",
        (),
        False,
    ),
    (
        "PBPKO_00405",
        ("PBPKO_00405", "THORACIC_COMPARTMENT"),
        "thoracic compartment",
        "A compartment representing the thoracic region (chest).",
        (),
        False,
    ),
    (
        "PBPKO_00406",
        ("PBPKO_00406", "BRONCHIOLAR_COMPARTMENT"),
        "bronchiolar compartment",
        "A lung compartment representing the bronchioles.",
        (),
        False,
    ),
    (
        "PBPKO_00407",
        ("PBPKO_00407", "ALVEOLAR_COMPARTMENT"),
        "alveolar compartment",
        "A lung compartment representing the alveoli.",
        (),
        False,
    ),
    (
        "PBPKO_00408",
        ("PBPKO_00408", "GUT_PBPK"),
        "gut pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the gut compartments.",
        (),
        False,
    ),
    (
        "PBPKO_00409",
        ("PBPKO_00409", "FRACTION_OF_BLOOD_FLOW_TO_DUODENUM"),
        "fraction of blood flow to duodenum",
        "The dimensionless fraction of cardiac output delivered to the duodenum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00410",
        ("PBPKO_00410", "FRACTION_OF_BLOOD_FLOW_TO_JEJUNUM"),
        "fraction of blood flow to jejunum",
        "The dimensionless fraction of cardiac output delivered to the jejunum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00411",
        ("PBPKO_00411", "FRACTION_OF_BLOOD_FLOW_TO_ILEUM"),
        "fraction of blood flow to ileum",
        "The dimensionless fraction of cardiac output delivered to the ileum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00412",
        ("PBPKO_00412", "FRACTION_OF_BLOOD_FLOW_TO_COLON"),
        "fraction of blood flow to colon",
        "The dimensionless fraction of cardiac output delivered to the colon compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00413",
        ("PBPKO_00413", "FRACTION_OF_BLOOD_FLOW_TO_CECUM"),
        "fraction of blood flow to cecum",
        "The dimensionless fraction of cardiac output delivered to the cecum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00414",
        ("PBPKO_00414", "BLOOD_FLOW_RATE_TO_DUODENUM"),
        "blood flow rate to duodenum",
        "A blood flow rate parameter specifically describing the rate to the duodenum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00415",
        ("PBPKO_00415", "BLOOD_FLOW_RATE_TO_JEJUNUM"),
        "blood flow rate to jejunum",
        "A blood flow rate parameter specifically describing the rate to the jejunum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00416",
        ("PBPKO_00416", "BLOOD_FLOW_RATE_TO_ILEUM"),
        "blood flow rate to ileum",
        "A blood flow rate parameter specifically describing the rate to the ileum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00417",
        ("PBPKO_00417", "BLOOD_FLOW_RATE_TO_COLON"),
        "blood flow rate to colon",
        "A blood flow rate parameter specifically describing the rate to the colon compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00418",
        ("PBPKO_00418", "BLOOD_FLOW_RATE_TO_CECUM"),
        "blood flow rate to cecum",
        "A blood flow rate parameter specifically describing the rate to the cecum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00419",
        ("PBPKO_00419", "FRACTION_OF_DUODENUM"),
        "fraction of duodenum",
        "A dimensionless fraction of volume defined as the duodenum volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00420",
        ("PBPKO_00420", "FRACTION_OF_JEJUNUM"),
        "fraction of jejunum",
        "A dimensionless fraction of volume defined as the jejunum volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00421",
        ("PBPKO_00421", "FRACTION_OF_ILEUM"),
        "fraction of ileum",
        "A dimensionless fraction of volume defined as the ileum volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00422",
        ("PBPKO_00422", "FRACTION_OF_COLON"),
        "fraction of colon",
        "A dimensionless fraction of volume defined as the colon volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00423",
        ("PBPKO_00423", "FRACTION_OF_CECUM"),
        "fraction of cecum",
        "A dimensionless fraction of volume defined as the cecum volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00424",
        ("PBPKO_00424", "VOLUME_OF_DUODENUM"),
        "volume of duodenum",
        "A volume parameter representing the total volume of the duodenum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00425",
        ("PBPKO_00425", "VOLUME_OF_JEJUNUM"),
        "volume of jejunum",
        "A volume parameter representing the total volume of the jejunum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00426",
        ("PBPKO_00426", "VOLUME_OF_ILEUM"),
        "volume of ileum",
        "A volume parameter representing the total volume of the ileum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00427",
        ("PBPKO_00427", "VOLUME_OF_COLON"),
        "volume of colon",
        "A volume parameter representing the total volume of the colon compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00428",
        ("PBPKO_00428", "VOLUME_OF_CECUM"),
        "volume of cecum",
        "A volume parameter representing the total volume of the cecum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00429",
        ("PBPKO_00429", "BILE_SALT_EFFECT_SOLUBILIZATION_RATIO"),
        "bile salt effect solubilization ratio",
        "A biochemical parameter representing the ratio of molecules solubilized due to bile salt presence.",
        (),
        False,
    ),
    (
        "PBPKO_00430",
        ("PBPKO_00430", "MEAN_PRECIPITATION_TIME"),
        "mean precipitation time",
        "A biochemical parameter representing the average time for a compound to precipitate under specific conditions (e.g., in the GI tract).",
        (),
        False,
    ),
    (
        "PBPKO_00431",
        ("PBPKO_00431", "DIFFUSION_COEFFICIENT"),
        "diffusion coefficient",
        "A physicochemical parameter representing the amount of substance diffusing across a unit area per unit time under a unit concentration gradient.",
        (),
        False,
    ),
    (
        "PBPKO_00432",
        ("PBPKO_00432", "PARTICLE_DENSITY"),
        "particle density",
        "A biochemical/physical parameter representing the mass per unit volume of particles (e.g., of the administered compound).",
        (),
        False,
    ),
    (
        "PBPKO_00433",
        ("PBPKO_00433", "PARTICLE_RADIUS"),
        "particle radius",
        "A biochemical/physical parameter representing the radius of particles (e.g., of the administered compound).",
        (),
        False,
    ),
    (
        "PBPKO_00434",
        ("PBPKO_00434", "INTESTINAL_TRANSIT_TIME"),
        "intestinal transit time",
        "A biochemical parameter representing the time required for a compound to move through the intestine.",
        (),
        False,
    ),
    (
        "PBPKO_00435",
        ("PBPKO_00435", "LACTATIONAL_PBPK"),
        "lactational pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations during lactation, including transfer into milk.",
        (),
        False,
    ),
    (
        "PBPKO_00436",
        ("PBPKO_00436", "MILK_PLASMA_RATIO"),
        "milk plasma ratio",
        "A biochemical parameter representing the ratio of compound concentration in milk to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00437",
        ("PBPKO_00437", "FRACTION_UNBOUND_MILK"),
        "fraction unbound milk",
        "An unbound fraction parameter specifically for milk.",
        (),
        False,
    ),
    (
        "PBPKO_00438",
        ("PBPKO_00438", "CONCENTRATION_IN_MILK"),
        "concentration in milk",
        "The total concentration of compound in the milk compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00439",
        ("PBPKO_00439", "DAILY_MILK_INTAKE"),
        "daily milk intake",
        "A physiological parameter representing the daily volume of milk ingested (e.g., by an infant).",
        (),
        False,
    ),
    (
        "PBPKO_00440",
        ("PBPKO_00440", "PHMILK"),
        "phmilk",
        "A biochemical parameter representing the pH of milk.",
        (),
        False,
    ),
    (
        "PBPKO_00441",
        ("PBPKO_00441", "BLOOD_MILK_BARRIER_COMPARTMENT"),
        "blood milk barrier compartment",
        "A barrier compartment representing the physiological barrier separating blood and milk in lactating species.",
        (),
        False,
    ),
    (
        "PBPKO_00442",
        ("PBPKO_00442", "MILK_PLASMA_PARTITION_COEFFICIENT"),
        "milk plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in milk to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00446",
        ("PBPKO_00446", "COMPARTMENT"),
        "compartment",
        "A data representation model component representing a distinct physiological space (organ, tissue, fluid) where ADME processes occur.",
        (),
        False,
    ),
    (
        "PBPKO_00448",
        ("PBPKO_00448", "ALVEOLAR_AIR_COMPARTMENT"),
        "alveolar air compartment",
        "A lung compartment specifically representing the air within the alveoli.",
        (),
        False,
    ),
    (
        "PBPKO_00450",
        ("PBPKO_00450", "REST_OF_BODY_COMPARTMENT"),
        "rest of body compartment",
        "A compartment representing the lumped remainder of the body not explicitly modeled as separate organs/tissues.",
        (),
        False,
    ),
    (
        "PBPKO_00451",
        ("PBPKO_00451", "ARTERIAL_PLASMA"),
        "arterial plasma",
        "A compartment representing the plasma specifically within the arterial blood.",
        (),
        False,
    ),
    (
        "PBPKO_00452",
        ("PBPKO_00452", "VENOUS_PLASMA_COMPARTMENT"),
        "venous plasma compartment",
        "A compartment representing the plasma specifically within the venous blood.",
        (),
        False,
    ),
    (
        "PBPKO_00453",
        ("PBPKO_00453", "RICHLY_PERFUSED_TISSUE_COMPARTMENT"),
        "richly perfused tissue compartment",
        "A compartment representing lumped tissues with high blood flow relative to their volume.",
        (),
        False,
    ),
    (
        "PBPKO_00454",
        ("PBPKO_00454", "POORLY_PERFUSED_TISSUE_COMPARTMENT"),
        "poorly perfused tissue compartment",
        "A compartment representing lumped tissues with low blood flow relative to their volume.",
        (),
        False,
    ),
    (
        "PBPKO_00455",
        ("PBPKO_00455", "VIABLE_UNEXPOSED_SKIN_COMPARTMENT"),
        "viable unexposed skin compartment",
        "A skin compartment representing the viable layers of skin not directly exposed to the applied compound.",
        (),
        False,
    ),
    (
        "PBPKO_00456",
        ("PBPKO_00456", "VIABLE_EXPOSED_SKIN_COMPARTMENT"),
        "viable exposed skin compartment",
        "A skin compartment representing the viable layers of skin directly exposed to the applied compound.",
        (),
        False,
    ),
    (
        "PBPKO_00457",
        ("PBPKO_00457", "SKIN_UNEXPOSED_STRATUM_CORNEUM"),
        "skin unexposed stratum corneum",
        "A stratum corneum compartment representing the portion not directly exposed to the applied compound.",
        (),
        False,
    ),
    (
        "PBPKO_00458",
        ("PBPKO_00458", "SKIN_EXPOSED_STRATUM_CORNEUM_COMPARTMENT"),
        "skin exposed stratum corneum compartment",
        "A stratum corneum compartment representing the portion directly exposed to the applied compound.",
        (),
        False,
    ),
    (
        "PBPKO_00460",
        ("PBPKO_00460", "ADIPOSE_COMPARTMENT"),
        "adipose compartment",
        "A compartment representing adipose (fat) tissue.",
        (),
        False,
    ),
    (
        "PBPKO_00461",
        ("PBPKO_00461", "ANAL_CANAL_COMPARTMENT"),
        "anal canal compartment",
        "A large intestine compartment representing the anal canal.",
        (),
        False,
    ),
    (
        "PBPKO_00462",
        ("PBPKO_00462", "APPENDIX_COMPARTMENT"),
        "appendix compartment",
        "A large intestine compartment representing the appendix.",
        (),
        False,
    ),
    (
        "PBPKO_00463",
        ("PBPKO_00463", "ASCENDING_COLON_COMPARTMENT"),
        "ascending colon compartment",
        "A large intestine compartment representing the ascending colon.",
        (),
        False,
    ),
    (
        "PBPKO_00464",
        ("PBPKO_00464", "BLOOD_COMPARTMENT"),
        "blood compartment",
        "A compartment representing the entirety of the blood (including plasma and cells).",
        (),
        False,
    ),
    (
        "PBPKO_00465",
        ("PBPKO_00465", "BONE_MARROW_COMPARTMENT"),
        "bone marrow compartment",
        "A compartment representing the bone marrow.",
        (),
        False,
    ),
    (
        "PBPKO_00466",
        ("PBPKO_00466", "BRAIN_COMPARTMENT"),
        "brain compartment",
        "A compartment representing the brain.",
        (),
        False,
    ),
    (
        "PBPKO_00467",
        ("PBPKO_00467", "CECUM_COMPARTMENT"),
        "cecum compartment",
        "A large intestine compartment representing the cecum.",
        (),
        False,
    ),
    (
        "PBPKO_00468",
        ("PBPKO_00468", "DESCENDING_COLON_COMPARTMENT"),
        "descending colon compartment",
        "A large intestine compartment representing the descending colon.",
        (),
        False,
    ),
    (
        "PBPKO_00469",
        ("PBPKO_00469", "DERMIS_COMPARTMENT"),
        "dermis compartment",
        "A skin compartment representing the dermis layer.",
        (),
        False,
    ),
    (
        "PBPKO_00470",
        ("PBPKO_00470", "SKIN_COMPARTMENT"),
        "skin compartment",
        "A compartment representing the skin.",
        (),
        False,
    ),
    (
        "PBPKO_00471",
        ("PBPKO_00471", "DUODENUM_COMPARTMENT"),
        "duodenum compartment",
        "A small intestine compartment representing the duodenum.",
        (),
        False,
    ),
    (
        "PBPKO_00472",
        ("PBPKO_00472", "SMALL_INTESTINE_COMPARTMENT"),
        "small intestine compartment",
        "A digestive system compartment representing the small intestine.",
        (),
        False,
    ),
    (
        "PBPKO_00473",
        ("PBPKO_00473", "ENDOCRINE_GLAND_COMPARTMENT"),
        "endocrine gland compartment",
        "A compartment representing endocrine glands.",
        (),
        False,
    ),
    (
        "PBPKO_00474",
        ("PBPKO_00474", "LARGE_INTESTINE_COMPARTMENT"),
        "large intestine compartment",
        "A digestive system compartment representing the large intestine.",
        (),
        False,
    ),
    (
        "PBPKO_00475",
        ("PBPKO_00475", "EPIDERMIS_COMPARTMENT"),
        "epidermis compartment",
        "A skin compartment representing the epidermis layer.",
        (),
        False,
    ),
    (
        "PBPKO_00476",
        ("PBPKO_00476", "GALL_BLADDER_COMPARTMENT"),
        "gall bladder compartment",
        "A digestive system compartment representing the gall bladder.",
        (),
        False,
    ),
    (
        "PBPKO_00477",
        ("PBPKO_00477", "GUT_COMPARTMENT"),
        "gut compartment",
        "A digestive system compartment representing the gut (general term, often synonymous with intestine or GI tract).",
        (),
        False,
    ),
    (
        "PBPKO_00478",
        ("PBPKO_00478", "GUT_LUMEN_COMPARTMENT"),
        "gut lumen compartment",
        "A digestive system compartment representing the lumen (opening) within the gut.",
        (),
        False,
    ),
    (
        "PBPKO_00479",
        ("PBPKO_00479", "HAIR_COMPARTMENT"),
        "hair compartment",
        "A compartment representing hair.",
        (),
        False,
    ),
    (
        "PBPKO_00480",
        ("PBPKO_00480", "HEART_COMPARTMENT"),
        "heart compartment",
        "A compartment representing the heart.",
        (),
        False,
    ),
    (
        "PBPKO_00481",
        ("PBPKO_00481", "ILEUM_COMPARTMENT"),
        "ileum compartment",
        "A small intestine compartment representing the ileum.",
        (),
        False,
    ),
    (
        "PBPKO_00482",
        ("PBPKO_00482", "JEJUNUM_COMPARTMENT"),
        "jejunum compartment",
        "A small intestine compartment representing the jejunum.",
        (),
        False,
    ),
    (
        "PBPKO_00483",
        ("PBPKO_00483", "MAMMARY_GLAND_COMPARTMENT"),
        "mammary gland compartment",
        "A compartment representing the mammary gland.",
        (),
        False,
    ),
    (
        "PBPKO_00484",
        ("PBPKO_00484", "MUSCLE_COMPARTMENT"),
        "muscle compartment",
        "A compartment representing muscle tissue.",
        (),
        False,
    ),
    (
        "PBPKO_00485",
        ("PBPKO_00485", "NAIL_COMPARTMENT"),
        "nail compartment",
        "A compartment representing nails.",
        (),
        False,
    ),
    (
        "PBPKO_00486",
        ("PBPKO_00486", "PANCREAS_COMPARTMENT"),
        "pancreas compartment",
        "A compartment representing the pancreas.",
        (),
        False,
    ),
    (
        "PBPKO_00487",
        ("PBPKO_00487", "PLACENTAL_BARRIER_COMPARTMENT"),
        "placental barrier compartment",
        "A barrier compartment representing the placental barrier separating maternal and fetal circulation.",
        (),
        False,
    ),
    (
        "PBPKO_00488",
        ("PBPKO_00488", "PLASMA_COMPARTMENT"),
        "plasma compartment",
        "A compartment representing blood plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00489",
        ("PBPKO_00489", "RECTUM_COMPARTMENT"),
        "rectum compartment",
        "A large intestine compartment representing the rectum.",
        (),
        False,
    ),
    (
        "PBPKO_00490",
        ("PBPKO_00490", "REPRODUCTIVE_COMPARTMENT"),
        "reproductive compartment",
        "A compartment representing reproductive organs (gonads).",
        (),
        False,
    ),
    (
        "PBPKO_00491",
        ("PBPKO_00491", "SIGMOID_COLON_COMPARTMENT"),
        "sigmoid colon compartment",
        "A large intestine compartment representing the sigmoid colon.",
        (),
        False,
    ),
    (
        "PBPKO_00492",
        ("PBPKO_00492", "SPLEEN_COMPARTMENT"),
        "spleen compartment",
        "A compartment representing the spleen.",
        (),
        False,
    ),
    (
        "PBPKO_00493",
        ("PBPKO_00493", "STRATUM_CORNEUM_COMPARTMENT"),
        "stratum corneum compartment",
        "A skin compartment representing the stratum corneum layer.",
        (),
        False,
    ),
    (
        "PBPKO_00494",
        ("PBPKO_00494", "TRANSVERSE_COLON_COMPARTMENT"),
        "transverse colon compartment",
        "A large intestine compartment representing the transverse colon.",
        (),
        False,
    ),
    (
        "PBPKO_00495",
        ("PBPKO_00495", "BARRIER_COMPARTMENT"),
        "barrier compartment",
        "A compartment representing a physiological barrier limiting compound movement.",
        (),
        False,
    ),
    (
        "PBPKO_00496",
        ("PBPKO_00496", "AMOUNT_IN_GUT"),
        "amount in gut",
        "The amount of compound in the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00497",
        ("PBPKO_00497", "AMOUNT_IN_LIVER"),
        "amount in liver",
        "The amount of compound in the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00498",
        ("PBPKO_00498", "AMOUNT_IN_KIDNEY"),
        "amount in kidney",
        "The amount of compound in the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00499",
        ("PBPKO_00499", "AMOUNT_IN_FILTRATE"),
        "amount in filtrate",
        "The amount of compound in the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00500",
        ("PBPKO_00500", "AMOUNT_IN_DELAY"),
        "amount in delay",
        "The amount of compound in the hypothetical delay compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00501",
        ("PBPKO_00501", "AMOUNT_IN_RESTBODY"),
        "amount in restbody",
        "The amount of compound in the rest of the body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00502",
        ("PBPKO_00502", "AMOUNT_IN_PLASMA"),
        "amount in plasma",
        "The amount of compound in the plasma compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00503",
        ("PBPKO_00503", "AMOUNT_IN_BRAIN"),
        "amount in brain",
        "The amount of compound in the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00504",
        ("PBPKO_00504", "AMOUNT_IN_LUNG"),
        "amount in lung",
        "The amount of compound in the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00505",
        ("PBPKO_00505", "AMOUNT_IN_BONE_MARROW"),
        "amount in bone marrow",
        "The amount of compound in the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00506",
        ("PBPKO_00506", "AMOUNT_IN_SKIN"),
        "amount in skin",
        "The amount of compound in the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00507",
        ("PBPKO_00507", "AMOUNT_IN_MAMMARY_GLAND"),
        "amount in mammary gland",
        "The amount of compound in the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00508",
        ("PBPKO_00508", "FRACTION_OF_FILTRATE"),
        "fraction of filtrate",
        "A dimensionless fraction of volume defined as the filtrate volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00509",
        ("PBPKO_00509", "FRACTION_OF_GUT"),
        "fraction of gut",
        "A dimensionless fraction of volume defined as the gut volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00510",
        ("PBPKO_00510", "FRACTION_OF_MAMMARY_GLAND"),
        "fraction of mammary gland",
        "A dimensionless fraction of volume defined as the mammary gland volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00511",
        ("PBPKO_00511", "FRACTION_OF_BLOOD_FLOW_TO_FILTRATE"),
        "fraction of blood flow to filtrate",
        "The dimensionless fraction of cardiac output delivered to the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00512",
        ("PBPKO_00512", "FRACTION_OF_BLOOD_FLOW_TO_BONE_MARROW"),
        "fraction of blood flow to bone marrow",
        "The dimensionless fraction of cardiac output delivered to the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00513",
        ("PBPKO_00513", "FRACTION_OF_BLOOD_FLOW_TO_GUT"),
        "fraction of blood flow to gut",
        "The dimensionless fraction of cardiac output delivered to the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00514",
        ("PBPKO_00514", "FRACTION_OF_BLOOD_FLOW_TO_MAMMARY_GLAND"),
        "fraction of blood flow to mammary gland",
        "The dimensionless fraction of cardiac output delivered to the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00515",
        ("PBPKO_00515", "BRAIN_PLASMA_PARTITION_COEFFICIENT"),
        "brain plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the brain to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00517",
        ("PBPKO_00517", "MAMMARY_GLAND_PLASMA_PARTITION_COEFFICIENT"),
        "mammary gland plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the mammary gland to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00518",
        ("PBPKO_00518", "RESTBODY_PLASMA_PARTITION_COEFFICIENT"),
        "restbody plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the rest of body compartment to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00519",
        ("PBPKO_00519", "TISSUE_PLASMA_PARTITION_COEFFICIENT"),
        "tissue plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in a generic tissue to plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00520",
        ("PBPKO_00520", "URINARY_RATE_CONSTANT"),
        "urinary rate constant",
        "A biochemical parameter (rate constant) representing the rate at which a compound is cleared via urine, often scaled by body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00521",
        ("PBPKO_00521", "AGE_IN_PBPK_MODEL"),
        "age in PBPK model",
        "A physiological parameter representing the period of lifespan (typically in years) for which the model is simulated.",
        (),
        False,
    ),
    (
        "PBPKO_00522",
        ("PBPKO_00522", "VOLUME_OF_FILTRATE"),
        "volume of filtrate",
        "A volume parameter representing the total volume of the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00523",
        ("PBPKO_00523", "VOLUME_OF_BONE_MARROW"),
        "volume of bone marrow",
        "A volume parameter representing the total volume of the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00524",
        ("PBPKO_00524", "VOLUME_OF_GUT"),
        "volume of gut",
        "A volume parameter representing the total volume of the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00525",
        ("PBPKO_00525", "VOLUME_OF_MAMMARY_GLAND"),
        "volume of mammary gland",
        "A volume parameter representing the total volume of the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00526",
        ("PBPKO_00526", "VOLUME_OF_MASS_BALANCE"),
        "volume of mass balance",
        "A volume parameter representing the check for total mass balance of all compartments (sum of organ volumes should equal body volume/weight equivalent, depending on units).",
        (),
        False,
    ),
    (
        "PBPKO_00527",
        ("PBPKO_00527", "HEMATOCRIT_VOLUME"),
        "hematocrit volume",
        "A volume parameter representing the total volume of red blood cells in whole blood.",
        (),
        False,
    ),
    (
        "PBPKO_00528",
        ("PBPKO_00528", "CARDIAC_OUTPUT_RATE_OF_PLASMA"),
        "cardiac output rate of plasma",
        "A blood flow rate parameter representing the cardiac output specifically related to plasma flow.",
        (),
        False,
    ),
    (
        "PBPKO_00529",
        ("PBPKO_00529", "BLOOD_FLOW_RATE_TO_FILTRATE"),
        "blood flow rate to filtrate",
        "A blood flow rate parameter specifically describing the rate to the filtrate compartment (representing glomerular filtration).",
        (),
        False,
    ),
    (
        "PBPKO_00530",
        ("PBPKO_00530", "BLOOD_FLOW_RATE_TO_BONE_MARROW"),
        "blood flow rate to bone marrow",
        "A blood flow parameter specifically describing the rate to the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00531",
        ("PBPKO_00531", "BLOOD_FLOW_RATE_TO_GUT"),
        "blood flow rate to gut",
        "A blood flow rate parameter specifically describing the rate to the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00532",
        ("PBPKO_00532", "BLOOD_FLOW_RATE_TO_MAMMARY_GLAND"),
        "blood flow rate to mammary gland",
        "A blood flow rate parameter specifically describing the rate to the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00533",
        ("PBPKO_00533", "BLOOD_FLOW_RATE_FOR_MASS_BALANCE"),
        "blood flow rate for mass balance",
        "A blood flow rate parameter representing the check for total blood flow mass balance of all the compartments (sum of organ flows should equal cardiac output).",
        (),
        False,
    ),
    (
        "PBPKO_00534",
        ("PBPKO_00534", "URINARY_RATE"),
        "urinary rate",
        "A biochemical parameter representing the rate at which a compound is cleared via urine.",
        (),
        False,
    ),
    (
        "PBPKO_00535",
        ("PBPKO_00535", "RESORPTION_MAXIMUM"),
        "resorption maximum",
        "A biochemical parameter (Tm) representing the maximum rate of tubular resorption (e.g., in the kidney).",
        (),
        False,
    ),
    (
        "PBPKO_00536",
        ("PBPKO_00536", "RESORPTION"),
        "resorption",
        "A biochemical parameter or process representing the resorption of a compound (e.g., tubular resorption).",
        (),
        False,
    ),
    (
        "PBPKO_00537",
        ("PBPKO_00537", "OCTANOL_AIR_PARTITION_COEFFICIENT"),
        "octanol air partition coefficient",
        "A partition coefficient (Koa) representing the ratio of compound concentration in octanol to air at equilibrium.",
        (),
        False,
    ),
    (
        "PBPKO_00538",
        ("PBPKO_00538", "CONCENTRATION_IN_GUT"),
        "concentration in gut",
        "The total concentration of compound in the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00539",
        ("PBPKO_00539", "CONCENTRATION_IN_LIVER"),
        "concentration in liver",
        "The total concentration of compound in the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00540",
        ("PBPKO_00540", "CONCENTRATION_IN_BRAIN"),
        "concentration in brain",
        "The total concentration of compound in the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00541",
        ("PBPKO_00541", "CONCENTRATION_IN_KIDNEY"),
        "concentration in kidney",
        "The total concentration of compound in the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00542",
        ("PBPKO_00542", "CONCENTRATION_IN_FILTRATE"),
        "concentration in filtrate",
        "The total concentration of compound in the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00543",
        ("PBPKO_00543", "CONCENTRATION_IN_LUNG"),
        "concentration in lung",
        "The total concentration of compound in the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00544",
        ("PBPKO_00544", "CONCENTRATION_IN_FAT"),
        "concentration in fat",
        "The total concentration of compound in the fat compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00545",
        ("PBPKO_00545", "CONCENTRATION_IN_BONE_MARROW"),
        "concentration in bone marrow",
        "The total concentration of compound in the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00546",
        ("PBPKO_00546", "CONCENTRATION_IN_SKIN"),
        "concentration in skin",
        "The total concentration of compound in the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00547",
        ("PBPKO_00547", "CONCENTRATION_IN_MAMMARY_GLAND"),
        "concentration in mammary gland",
        "The total concentration of compound in the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00548",
        ("PBPKO_00548", "CONCENTRATION_IN_RESTBODY"),
        "concentration in restbody",
        "The total concentration of compound in the rest of body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00549",
        ("PBPKO_00549", "CONCENTRATION_IN_PLASMA"),
        "concentration in plasma",
        "The total concentration of compound in the plasma compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00550",
        ("PBPKO_00550", "AMOUNT_IN_FAT"),
        "amount in fat",
        "The amount of compound in the fat compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00551",
        ("PBPKO_00551", "PBPK_MODEL_SIMULATION_TIME"),
        "PBPK model simulation time",
        "A parameter representing the time duration over which the model simulation runs.",
        (),
        False,
    ),
    (
        "PBPKO_00552",
        ("PBPKO_00552", "ARTERIAL_BLOOD_COMPARTMENT"),
        "arterial blood compartment",
        "A compartment representing the arterial blood.",
        (),
        False,
    ),
    (
        "PBPKO_00553",
        ("PBPKO_00553", "DIGESTIVE_SYSTEM_COMPARTMENT"),
        "digestive system compartment",
        "A compartment representing the digestive system or parts thereof.",
        (),
        False,
    ),
    (
        "PBPKO_00554",
        ("PBPKO_00554", "EXCRETA_COMPARTMENT"),
        "excreta compartment",
        "A compartment representing material eliminated from the body (e.g., urine, feces).",
        (),
        False,
    ),
    (
        "PBPKO_00555",
        ("PBPKO_00555", "FECES_COMPARTMENT"),
        "feces compartment",
        "An excreta compartment specifically representing feces.",
        (),
        False,
    ),
    (
        "PBPKO_00556",
        ("PBPKO_00556", "URINE_COMPARTMENT"),
        "urine compartment",
        "An excreta compartment specifically representing urine.",
        (),
        False,
    ),
    (
        "PBPKO_00557",
        ("PBPKO_00557", "KIDNEY_COMPARTMENT"),
        "kidney compartment",
        "A compartment representing the kidney(s).",
        (),
        False,
    ),
    (
        "PBPKO_00558",
        ("PBPKO_00558", "LIVER_COMPARTMENT"),
        "liver compartment",
        "A compartment representing the liver.",
        (),
        False,
    ),
    (
        "PBPKO_00559",
        ("PBPKO_00559", "LUNG_COMPARTMENT"),
        "lung compartment",
        "A compartment representing the lung(s).",
        (),
        False,
    ),
    (
        "PBPKO_00561",
        ("PBPKO_00561", "VENOUS_BLOOD_COMPARTMENT"),
        "venous blood compartment",
        "A compartment representing the venous blood.",
        (),
        False,
    ),
    (
        "PBPKO_00562",
        ("PBPKO_00562", "BLOOD_FLOW_RATE_TO_UNEXPOSED_SKIN"),
        "blood flow rate to unexposed skin",
        "A blood flow rate to skin parameter specifically describing the rate to the unexposed portion of the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00563",
        ("PBPKO_00563", "BLOOD_FLOW_RATE_TO_EXPOSED_SKIN"),
        "blood flow rate to exposed skin",
        "A blood flow rate to skin parameter specifically describing the rate to the exposed portion of the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00564",
        ("PBPKO_00564", "BLOOD_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_UNEXPOSED"),
        "blood flow rate to skin stratum corneum unexposed",
        "A blood flow rate to skin parameter specifically describing the rate to the unexposed stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00565",
        ("PBPKO_00565", "BLOOD_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_EXPOSED"),
        "blood flow rate to skin stratum corneum exposed",
        "A blood flow rate to skin parameter specifically describing the rate to the exposed stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00566",
        ("PBPKO_00566", "STOMACH_COMPARTMENT"),
        "stomach compartment",
        "A digestive system compartment representing the stomach.",
        (),
        False,
    ),
    (
        "PBPKO_00567",
        ("PBPKO_00567", "BONE_BLOOD_PARTITION_COEFFICIENT"),
        "bone blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in bone to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00568",
        ("PBPKO_00568", "AIR_BLOOD_PARTITION_COEFFICIENT"),
        "air blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in air to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00569",
        ("PBPKO_00569", "BRAIN_BLOOD_PARTITION_COEFFICIENT"),
        "brain blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in brain to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00570",
        ("PBPKO_00570", "BRAINFETUS_BLOOD_PARTITION_COEFFICIENT"),
        "brainfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal brain to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00571",
        ("PBPKO_00571", "GONAD_BLOOD_PARTITION_COEFFICIENT"),
        "gonad blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in gonads to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00572",
        ("PBPKO_00572", "GUT_BLOOD_PARTITION_COEFFICIENT"),
        "gut blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the gut to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00573",
        ("PBPKO_00573", "HEART_BLOOD_PARTITION_COEFFICIENT"),
        "heart blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the heart to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00574",
        ("PBPKO_00574", "INTESTINE_BLOOD_PARTITION_COEFFICIENT"),
        "intestine blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the intestine to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00575",
        ("PBPKO_00575", "KIDNEY_BLOOD_PARTITION_COEFFICIENT"),
        "kidney blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the kidney to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00576",
        ("PBPKO_00576", "KIDNEYFETUS_BLOOD_PARTITION_COEFFICIENT"),
        "kidneyfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal kidney to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00577",
        ("PBPKO_00577", "LIVER_BLOOD_PARTITION_COEFFICIENT"),
        "liver blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the liver to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00578",
        ("PBPKO_00578", "LIVERFETUS_BLOOD_PARTITION_COEFFICIENT"),
        "liverfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal liver to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00579",
        ("PBPKO_00579", "LUNG_BLOOD_PARTITION_COEFFICIENT"),
        "lung blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the lung to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00580",
        ("PBPKO_00580", "MAMMARY_GLAND_BLOOD_PARTITION_COEFFICIENT"),
        "mammary gland blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the mammary gland to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00581",
        ("PBPKO_00581", "MILK_BLOOD_PARTITION_COEFFICIENT"),
        "milk blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in milk to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00582",
        ("PBPKO_00582", "MUSCLE_BLOOD_PARTITION_COEFFICIENT"),
        "muscle blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in muscle to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00583",
        ("PBPKO_00583", "PANCREAS_BLOOD_PARTITION_COEFFICIENT"),
        "pancreas blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the pancreas to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00584",
        ("PBPKO_00584", "POOR_PERFUSED_BLOOD_PARTITION_COEFFICIENT"),
        "poor perfused blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the poorly perfused compartment to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00585",
        ("PBPKO_00585", "RESTBODY_BLOOD_PARTITION_COEFFICIENT"),
        "restbody blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the rest of body compartment to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00586",
        ("PBPKO_00586", "RESTBODYFETUS_BLOOD_PARTITION_COEFFICIENT"),
        "restbodyfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00587",
        ("PBPKO_00587", "RICH_PERFUSED_BLOOD_PARTITION_COEFFICIENT"),
        "rich perfused blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the richly perfused compartment to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00588",
        ("PBPKO_00588", "SKIN_BLOOD_PARTITION_COEFFICIENT"),
        "skin blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the skin to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00589",
        ("PBPKO_00589", "SPLEEN_BLOOD_PARTITION_COEFFICIENT"),
        "spleen blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the spleen to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00590",
        ("PBPKO_00590", "STOMACH_BLOOD_PARTITION_COEFFICIENT"),
        "stomach blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the stomach to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00591",
        ("PBPKO_00591", "FRACTION_UNBOUND_PLASMA"),
        "fraction unbound plasma",
        "An unbound fraction parameter specifically for plasma.",
        (),
        False,
    ),
    (
        "PBPKO_00592",
        ("PBPKO_00592", "MAXIMUM_RATE_OF_APICAL_TRANSPORTER"),
        "maximum rate of apical transporter",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    (
        "PBPKO_00593",
        ("PBPKO_00593", "MAXIMUM_RATE_OF_BASOLATERAL_TRANSPORTER"),
        "maximum rate of basolateral transporter",
        "Maximum rate (Vmax) of transport via a basolateral transporter.",
        (),
        False,
    ),
    (
        "PBPKO_00610",
        ("PBPKO_00610", "FRACTION_OF_VOLUME_OF_COMPARTMENT"),
        "fraction of volume of compartment",
        "A physiological parameter representing the dimensionless fraction computed by dividing the volume of the compartment by the total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00611",
        ("PBPKO_00611", "FRACTION_OF_BLOOD_FLOW_TO_A_COMPARTMENT"),
        "fraction of blood flow to a compartment",
        "A physiological parameter representing dimensionless fraction of cardiac output delivered to a compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00612",
        ("PBPKO_00612", "APPARENT_PERMEABILITY"),
        "apparent permeability",
        "A biochemical parameter representing the apparent permeability of a compound specifically between the compartments.",
        (),
        False,
    ),
    (
        "PBPKO_00613",
        ("PBPKO_00613", "MAXIMUM_RATE"),
        "maximum rate",
        "A biochemical parameter representing Vmax of the enzymatic activity",
        (),
        False,
    ),
    (
        "PBPKO_00615",
        ("PBPKO_00615", "AMOUNT_OF_COMPOUND_IN_COMPARTMENT"),
        "amount of compound in compartment",
        "An output parameter representing the amount of chemical specifically in the compartment",
        (),
        False,
    ),
    (
        "PBPKO_00616",
        ("PBPKO_00616", "CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT"),
        "concentration of compound in compartment",
        "An output parameter representing the total concentration of compound in the compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00617",
        ("PBPKO_00617", "HIPPOCAMPUS_COMPARTMENT"),
        "hippocampus compartment",
        "A part of brain compartment representing the hippocampus region of the brain",
        (),
        False,
    ),
    (
        "PBPKO_00618",
        ("PBPKO_00618", "CEREBRUM_COMPARTMENT"),
        "cerebrum compartment",
        "A part of brain compartment representing the cerebrum region of the brain",
        (),
        False,
    ),
    (
        "PBPKO_00619",
        ("PBPKO_00619", "CEREBELLUM_COMPARTMENT"),
        "cerebellum compartment",
        "A part of brain compartment representing the cerebellum region of the brain",
        (),
        False,
    ),
    (
        "PBPKO_00620",
        ("PBPKO_00620", "FRONTAL_CORTEX_COMPARTMENT"),
        "frontal cortex compartment",
        "A part of brain compartment representing the frontal cortex region of the brain",
        (),
        False,
    ),
    (
        "PBPKO_00621",
        ("PBPKO_00621", "CEREBROSPINAL_FLUID_COMPARTMENT"),
        "cerebrospinal fluid compartment",
        "A part of brain compartment representing the cerebrospinal fluid region of the brain",
        (),
        False,
    ),
    (
        "PBPKO_00622",
        ("PBPKO_00622", "FRACTION_UNBOUND_BLOOD"),
        "fraction unbound blood",
        "An unbound fraction parameter specifically for the blood compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00623",
        ("PBPKO_00623", "AMOUNT_IN_BLOOD"),
        "amount in blood",
        "The amount of compound in the blood compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00624",
        ("PBPKO_00624", "FRACTION_UNBOUND_RESTBODY"),
        "fraction unbound restbody",
        "An unbound fraction parameter specifically for the rest of the body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00625",
        ("PBPKO_00625", "EXPOSED_SKIN_COMPARTMENT"),
        "exposed skin compartment",
        "A skin compartment representing the exposed part of the skin to the chemical via dermal contact.",
        (),
        False,
    ),
    (
        "PBPKO_00626",
        ("PBPKO_00626", "UNEXPOSED_SKIN_COMPARTMENT"),
        "unexposed skin compartment",
        "A skin compartment representing the unexposed part of the skin to the chemical such as regions covered by clothing or occluded areas like the inner arms.",
        (),
        False,
    ),
    (
        "PBPKO_00627",
        ("PBPKO_00627", "FRACTION_OF_ARTERIAL_PLASMA_VOLUME"),
        "fraction of arterial plasma volume",
        "A dimensionless fraction of volume defined as the arterial plasma volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00628",
        ("PBPKO_00628", "FRACTION_OF_VENOUS_PLASMA_VOLUME"),
        "fraction of venous plasma volume",
        "A dimensionless fraction of volume defined as the venous plasma volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_00629",
        ("PBPKO_00629", "AMOUNT_IN_RICHLY_PERFUSED_TISSUE"),
        "amount in richly perfused tissue",
        "The amount of compound in the richly perfused tissue compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00630",
        ("PBPKO_00630", "AMOUNT_IN_POORLY_PERFUSED_TISSUE"),
        "amount in poorly perfused tissue",
        "The amount of compound in the poorly perfused tissue compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00631",
        ("PBPKO_00631", "AMOUNT_IN_ARTERIAL_BLOOD"),
        "amount in arterial blood",
        "The amount of compound in the arterial blood compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00632",
        ("PBPKO_00632", "AMOUNT_IN_VENOUS_BLOOD"),
        "amount in venous blood",
        "The amount of compound in the venous blood compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00633",
        ("PBPKO_00633", "AMOUNT_IN_ALVEOLAR_AIR"),
        "amount in alveolar air",
        "The amount of compound in the alveolar air compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00634",
        ("PBPKO_00634", "RED_BLOOD_CELL_COMPARTMENT"),
        "red blood cell compartment",
        "A compartment representing the red blood cells of the body.",
        (),
        False,
    ),
    (
        "PBPKO_00635",
        ("PBPKO_00635", "SKIN_THICKNESS"),
        "skin thickness",
        "A physiological parameter representing the thickness of the skin compartment",
        (),
        False,
    ),
    (
        "PBPKO_00636",
        ("PBPKO_00636", "BODILY_FLUID_FLOW_RATE_PARAMETER"),
        "bodily fluid flow rate parameter",
        "A physiological parameter representing the rate of fluid flow to a particular compartment.",
        (),
        False,
    ),
    (
        "PBPKO_00637",
        ("PBPKO_00637", "AMOUNT_IN_VIABLE_EPIDERMIS_OF_UNEXPOSED_SKIN"),
        "amount in viable epidermis of unexposed skin",
        "The amount of chemical in viable epidermis of unexposed skin",
        (),
        False,
    ),
    (
        "PBPKO_00638",
        ("PBPKO_00638", "AMOUNT_IN_VIABLE_EPIDERMIS_OF_EXPOSED_SKIN"),
        "amount\xa0in viable epidermis of exposed skin",
        "The amount of chemical in viable epidermis of exposed skin",
        (),
        False,
    ),
    (
        "PBPKO_00639",
        ("PBPKO_00639", "AMOUNT_IN_SKIN_STRATUM_CORNEUM_OF_UNEXPOSED_SKIN"),
        "amount\xa0in skin stratum\xa0corneum of unexposed skin",
        "The amount of chemical in skin stratum corneum of unexposed skin",
        (),
        False,
    ),
    (
        "PBPKO_00640",
        ("PBPKO_00640", "AMOUNT_IN_SKIN_STRATUM_CORNEUM_OF_EXPOSED_SKIN"),
        "amount\xa0in skin stratum\xa0corneum of exposed skin",
        "The amount of chemical in skin stratum corneum of exposed skin",
        (),
        False,
    ),
    (
        "PBPKO_00641",
        ("PBPKO_00641", "DERMAL_ABSORPTION_RATE_UNEXPOSED_SKIN"),
        "dermal absorption\xa0rate\xa0unexposed skin",
        "An absorption rate constant parameter representing dermal absorption rate flux through unexposed skin",
        (),
        False,
    ),
    (
        "PBPKO_00642",
        ("PBPKO_00642", "DERMAL_ABSORPTION_RATE_EXPOSED_SKIN"),
        "dermal absorption\xa0rate\xa0exposed skin",
        "An absorption rate constant parameter representing dermal absorption rate flux through exposed skin",
        (),
        False,
    ),
    (
        "PBPKO_00643",
        ("PBPKO_00643", "THICKNESS_STRATUM_CORNEUM"),
        "thickness stratum corneum",
        "A skin thickness parameter representing the thickness of stratum corneum.",
        (),
        False,
    ),
    (
        "PBPKO_00644",
        ("PBPKO_00644", "THICKNESS_VIABLE_EPIDERMIS"),
        "thickness viable epidermis",
        "A skin thickness parameter representing the thickness of viable epidermis.",
        (),
        False,
    ),
    (
        "PBPKO_00645",
        ("PBPKO_00645", "FAT_BLOOD_PARTITION_COEFFICIENT"),
        "fat blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in fat to blood.",
        (),
        False,
    ),
    (
        "PBPKO_00646",
        ("PBPKO_00646", "DIFFUSION_RATE"),
        "diffusion rate",
        "A biochemical parameter representing the diffusion rate of the chemical",
        (),
        False,
    ),
    (
        "PBPKO_00647",
        ("PBPKO_00647", "DIFFUSION_RATE_SKIN"),
        "diffusion rate skin",
        "A diffusion rate parameter representing diffusion rate of the chemical across the skin",
        (),
        False,
    ),
    (
        "PBPKO_00648",
        ("PBPKO_00648", "DIFFUSION_RATE_STRATUM_CORNEUM_VIABLE_EPIDERMIS"),
        "diffusion\xa0rate stratum\xa0corneum\xa0viable epidermis",
        "A diffusion rate skin parameter representing diffusion rate from stratum corneum to viable epidermis",
        (),
        False,
    ),
    (
        "PBPKO_00649",
        ("PBPKO_00649", "MISCELLANEOUS_PARAMETER"),
        "miscellaneous parameter",
        "A parameter being used in the model but does not belong to specific parameter subclass",
        (),
        False,
    ),
    (
        "PBPKO_00650",
        ("PBPKO_00650", "MICHAELIS"),
        "Michaelis",
        "A flag indicating for Michaelis-Menten or linear metabolism equation being used in the model",
        (),
        False,
    ),
    (
        "PBPKO_00651",
        ("PBPKO_00651", "FRACTION_OF_ARTERIAL_BLOOD_VOLUME"),
        "fraction of arterial\xa0blood\xa0volume",
        "A dimensionless fraction of volume defined as the arterial blood volume divided per unit of total body weight.",
        (),
        False,
    ),
    ("PBPKO_01501", ("PBPKO_01501", "PGP"), "pgp", None, (), False),
    ("PBPKO_01502", ("PBPKO_01502", "MRP2"), "mrp2", None, (), False),
    ("PBPKO_01503", ("PBPKO_01503", "MRP4"), "mrp4", None, (), False),
    ("PBPKO_01504", ("PBPKO_01504", "BCRP"), "bcrp", None, (), False),
    ("PBPKO_01505", ("PBPKO_01505", "NCTP"), "nctp", None, (), False),
    ("PBPKO_01506", ("PBPKO_01506", "OCT1"), "oct1", None, (), False),
    ("PBPKO_01507", ("PBPKO_01507", "OAT1"), "oat1", None, (), False),
    ("PBPKO_01508", ("PBPKO_01508", "OAT3"), "oat3", None, (), False),
    ("PBPKO_01509", ("PBPKO_01509", "OAT4"), "oat4", None, (), False),
    (
        "PBPKO_02001",
        ("PBPKO_02001", "BILE_COMPARTMENT"),
        "bile compartment",
        "A compartment representing the bile storage",
        (),
        False,
    ),
    (
        "PBPKO_02002",
        ("PBPKO_02002", "COLON_COMPARTMENT"),
        "colon compartment",
        "A compartment representing the colon",
        (),
        False,
    ),
    (
        "PBPKO_02003",
        ("PBPKO_02003", "SMALL_INTESTINE_TISSUE_COMPARTMENT"),
        "small intestine tissue compartment",
        "A compartment representing the small intestinal tissue",
        (),
        False,
    ),
    (
        "PBPKO_02004",
        ("PBPKO_02004", "INTESTINAL_TISSUE_COMPARTMENT"),
        "intestinal tissue compartment",
        "A compartment representing the whole intestinal tissue",
        (),
        False,
    ),
    (
        "PBPKO_02005",
        ("PBPKO_02005", "PORTAL_VEIN_PERFUSED_TISSUE_COMPARMENT"),
        "portal vein perfused tissue comparment",
        "A compartment with grouped organs that are exclusively perfused via the portal vein (i.e.: Stomach, small and large intestine, spleen)",
        (),
        False,
    ),
    (
        "PBPKO_02006",
        ("PBPKO_02006", "GLOMERULUS_COMPARTMENT"),
        "glomerulus compartment",
        "A part of kidney compartment in the model representing glomerulus in the body",
        (),
        False,
    ),
    (
        "PBPKO_02007",
        ("PBPKO_02007", "MENSTRUAL_PLASMA_COMPARTMENT"),
        "menstrual plasma compartment",
        "A compartment representing menstrual plasma",
        (),
        False,
    ),
    (
        "PBPKO_02008",
        ("PBPKO_02008", "KIDNEY_REST_LUMEN_COMPARTMENT"),
        "kidney rest lumen compartment",
        "A compartment representing rest of the lumen of kidney.",
        (),
        False,
    ),
    (
        "PBPKO_02009",
        ("PBPKO_02009", "KIDNEY_PROXIMAL_TUBULE_TISSUE_COMPARTMENT"),
        "kidney proximal tubule tissue compartment",
        "A compartment representing rest of the tissue of kidney.",
        (),
        False,
    ),
    (
        "PBPKO_02010",
        ("PBPKO_02010", "LIVER_EXTRACELLULAR_COMPARTMENT"),
        "liver extracellular compartment",
        "A compartment representing vascular and interstitial space of the liver.",
        (),
        False,
    ),
    (
        "PBPKO_02011",
        ("PBPKO_02011", "LIVER_INTRACELLULAR_SPACE_COMPARTMENT"),
        "liver intracellular space compartment",
        "A compartment representing intracellular space of the liver.",
        (),
        False,
    ),
    (
        "PBPKO_02012",
        ("PBPKO_02012", "GASTRO_INTESTINAL_TRACT_COMPARTMENT"),
        "gastro intestinal tract compartment",
        "A digestive system compartment representing the gastro-intestinal tract",
        (),
        False,
    ),
    (
        "PBPKO_02013",
        ("PBPKO_02013", "GONAD_COMPARTMENT"),
        "gonad compartment",
        "A compartment representing gonads.",
        (),
        False,
    ),
    (
        "PBPKO_03001",
        ("PBPKO_03001", "INTRINSIC_GASTRIC_EMPTYING_RATE"),
        "intrinsic gastric emptying rate",
        "The absorption rate constant parameter representing the intrinsic rate of the chemical release from stomach to lumen or the jejunum segment",
        (),
        False,
    ),
    (
        "PBPKO_03002",
        ("PBPKO_03002", "INTRINSIC_ABSORPTION_RATE"),
        "intrinsic absorption rate",
        "The absorption rate constant parameter representing the intrinsic absorption rate from the gut or any intestinal segment to the liver or the portal vein",
        (),
        False,
    ),
    (
        "PBPKO_03003",
        ("PBPKO_03003", "INTRINSIC_STOMACH_UPTAKE_RATE"),
        "intrinsic stomach uptake rate",
        "The absorption rate constant parameter representing the intrinsic absorption rate of a chemical from the stomach to the gut tissue or any intestinal segment",
        (),
        False,
    ),
    (
        "PBPKO_03004",
        ("PBPKO_03004", "STOMACH_UPTAKE_RATE"),
        "stomach uptake rate",
        "The absorption rate constant parameter representing the absorption rate from stomach to gut tissue or any intestine segment",
        (),
        False,
    ),
    (
        "PBPKO_03005",
        ("PBPKO_03005", "INTRINSIC_FECAL_EXCRETION_RATE"),
        "intrinsic fecal excretion rate",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03006",
        ("PBPKO_03006", "FECAL_EXCRETION_RATE"),
        "fecal excretion rate",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03007",
        ("PBPKO_03007", "INTRINSIC_BILIARY_CLEARANCE_RATE"),
        "intrinsic biliary clearance rate",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03008",
        ("PBPKO_03008", "KINETIC_EMPTYING_RATE_FROM_JEJUNUM_LUMEN_TO_ILEUM_LUMEN"),
        "kinetic emptying rate from jejunum lumen to ileum lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03009",
        (
            "PBPKO_03009",
            "KINETIC_EMPTYING__RATE_FROM_ILEUM_LUMEN_TO_LARGE_INTESTINE_LUMEN",
        ),
        "kinetic emptying  rate from ileum lumen to large intestine lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03010",
        (
            "PBPKO_03010",
            "KINETIC_ABSORPTION_RATE_FROM_JEJUNUM_LUMEN_TO_INTESTINAL_TISSUE",
        ),
        "kinetic absorption rate from jejunum lumen to intestinal tissue",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03011",
        (
            "PBPKO_03011",
            "KINETIC_ABSORPTION_RATE_FROM_ILEUM_LUMEN_TO_INTESTINAL_TISSUE",
        ),
        "kinetic absorption rate from ileum lumen to intestinal tissue",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03012",
        (
            "PBPKO_03012",
            "KINETIC_ABSORPTION_RATE_FROM_LARGE_INTESTINAL_LUMEN_TO_INTESTINAL_TISSUE",
        ),
        "kinetic absorption rate from large intestinal lumen to intestinal tissue",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03013",
        ("PBPKO_03013", "EFFECTIVE_CACO_2_PERMEABILITY"),
        "effective Caco-2 permeability",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03014",
        ("PBPKO_03014", "APPARENT_CACO_2_PERMEABILITY"),
        "apparent Caco-2 permeability",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03015",
        ("PBPKO_03015", "KINETIC_EMPTYING__RATE_BETWEEN_INTESTINAL_SEGMENTS"),
        "kinetic emptying  rate between intestinal segments",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03016",
        ("PBPKO_03016", "HILL_DISSOCIATION_CONSTANT"),
        "Hill dissociation constant",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03017",
        ("PBPKO_03017", "HILL_COEFFICIENT"),
        "Hill coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03018",
        ("PBPKO_03018", "INTRINSIC_ABSORPTION_RATE_OF_METABILITE"),
        "intrinsic absorption rate of metabilite",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03019",
        ("PBPKO_03019", "ABSORPTION_RATE_OF_METABOLITE"),
        "absorption rate of metabolite",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03020",
        ("PBPKO_03020", "INTRINSIC_ENTEROHEPATIC_RECIRCULATION_RATE_CONSTANT"),
        "intrinsic enterohepatic recirculation rate constant",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03021",
        ("PBPKO_03021", "ENTEROHEPATIC_RECIRCULATION_RATE_CONSTANT"),
        "enterohepatic recirculation rate constant",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03023",
        ("PBPKO_03023", "INTRINSIC_REABSORPTION_RATE_CONSTANT"),
        "intrinsic reabsorption rate constant",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03024",
        ("PBPKO_03024", "REABSORPTION_RATE_CONSTANT"),
        "reabsorption rate constant",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03025",
        ("PBPKO_03025", "MAXIMUM_CAPACITY_OF_BINDING_SITES_IN_RED_CELLS"),
        "maximum capacity of binding sites in red cells",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03026",
        (
            "PBPKO_03026",
            "HALF_SATURATION_CONCENTRATION_OF_CHEMICAL_FOR_BINDING_BY_SITES_IN_RED_CELLS",
        ),
        "half-saturation concentration of chemical for binding by sites in red cells",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03027",
        ("PBPKO_03027", "METABOLISM_RATE_CONSTANT_IN_LIVER"),
        "metabolism rate constant in liver",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03028",
        ("PBPKO_03028", "METABOLISM_RATE_CONSTANT_IN_INTESTINAL_TISSUE"),
        "metabolism rate constant in intestinal tissue",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03030",
        ("PBPKO_03030", "RED_BLOOD_CELLS_PARTITION_COEFFICIENT"),
        "red blood cells partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03031",
        ("PBPKO_03031", "FOLLICLE_PERMEABILITY_COEFFICIENT"),
        "follicle permeability coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03032",
        ("PBPKO_03032", "PARTITION_COEFFCIENT_OF_STRATUM_CORNEUM_TO_VIABLE_EPIDERMIS"),
        "partition coeffcient of stratum corneum to viable epidermis",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03033",
        ("PBPKO_03033", "PARTITION_COEFFCIENT_OF_VIABLE_EPIDERMIS_TO_BLOOD"),
        "partition coeffcient of viable epidermis to blood",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03034",
        (
            "PBPKO_03034",
            "PARTITION_COEFFCIENT_OF_STRATUM_CORNEUM_TO_SKIN_SURFACE_DEPOT",
        ),
        "partition coeffcient of stratum corneum to skin surface depot",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03035",
        ("PBPKO_03035", "PARTITION_COEFFCIENT_OF_FOLLICLE_TO_SKIN_SURFACE_DEPOT"),
        "partition coeffcient of follicle to skin surface depot",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03036",
        ("PBPKO_03036", "OCTANOL_WATER_PARTITION_COEFFICIENT"),
        "octanol water partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03037",
        ("PBPKO_03037", "MEDIUM_POLYMER_PARTITION_COEFFICIENT"),
        "medium polymer partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03038",
        ("PBPKO_03038", "MEDIUM_AIR_PARTITION_COEFFICIENT"),
        "medium air partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03039",
        ("PBPKO_03039", "MEDIUM_MITOCHONDRIA_PARTITION_COEFFICIENT"),
        "medium mitochondria partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03040",
        ("PBPKO_03040", "MEDIUM_LYSOSOMES_PARTITION_COEFFICIENT"),
        "medium lysosomes partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03041",
        ("PBPKO_03041", "MEDIUM_INTRACELLULAR_WATER_PARTITION_COEFFICIENT"),
        "medium intracellular water partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03042",
        ("PBPKO_03042", "MEDIUM_MICROSOMES_PARTITION_COEFFICIENT"),
        "medium microsomes partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03043",
        ("PBPKO_03043", "MEDIUM_OTHER_ORGANELLES_PARTITION_COEFFICIENT"),
        "medium other organelles partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03044",
        ("PBPKO_03044", "MEDIUM_ALBUMIN_PARTITION_COEFFICIENT"),
        "medium albumin partition coefficient",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03045",
        ("PBPKO_03045", "ABIOTIC_DEGRADATION_RATE_IN_MEDIUM"),
        "abiotic degradation rate in medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03046",
        ("PBPKO_03046", "ACIDIC_PHOSPHOLIPID_ASSOCIATION_CONSTANT"),
        "acidic phospholipid association constant",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03047",
        ("PBPKO_03047", "ABIOTIC_DEGRADATION_RATE_IN_AIR"),
        "abiotic degradation rate in air",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03048",
        ("PBPKO_03048", "MAXIMUM_METABOLIC_RATE"),
        "maximum metabolic rate",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03049",
        ("PBPKO_03049", "LINEAR_METABOLIC_RATE"),
        "linear metabolic rate",
        None,
        (),
        False,
    ),
    ("PBPKO_03050", ("PBPKO_03050", "CELL_RADIUS"), "cell radius", None, (), False),
    (
        "PBPKO_03051",
        ("PBPKO_03051", "CELL_REPLICATION_TIME"),
        "cell replication time",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03052",
        ("PBPKO_03052", "CELL_FRACTION_OF_PROTEINS"),
        "cell fraction of proteins",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03053",
        ("PBPKO_03053", "CELL_FRACTION_OF_LIPIDS"),
        "cell fraction of lipids",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03054",
        ("PBPKO_03054", "CELL_FRACTION_OF_INTRACELLULAR_WATER"),
        "cell fraction of intracellular water",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03055",
        ("PBPKO_03055", "CELL_FRACTION_OF_MITOCHONDRIA"),
        "cell fraction of mitochondria",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03056",
        ("PBPKO_03056", "CELL_FRACTION_OF_LYSOSOMES"),
        "cell fraction of lysosomes",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03057",
        ("PBPKO_03057", "CELL_FRACTION_OF_MICROSOMES"),
        "cell fraction of microsomes",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03058",
        ("PBPKO_03058", "FRACTION_OF_NEUTRAL_LIPIDS_IN_THE_FBS"),
        "fraction of neutral lipids in the FBS",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03059",
        ("PBPKO_03059", "FRACTION_OF_ALBUMIN_IN_THE_FBS"),
        "fraction of albumin in the FBS",
        None,
        (),
        False,
    ),
    ("PBPKO_03060", ("PBPKO_03060", "CULTURE_AREA"), "culture area", None, (), False),
    (
        "PBPKO_03061",
        ("PBPKO_03061", "TOP_WELL_DIAMETER"),
        "top well diameter",
        None,
        (),
        False,
    ),
    ("PBPKO_03062", ("PBPKO_03062", "WELL_DEPTH"), "well depth", None, (), False),
    (
        "PBPKO_03063",
        ("PBPKO_03063", "PLATE_WALL_THICKNESS"),
        "plate wall thickness",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03064",
        ("PBPKO_03064", "CULTURE_MEDIUM_PH"),
        "culture medium pH",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03065",
        ("PBPKO_03065", "FRACTION_OF_SERUM_IN_TOTAL_MEDIA"),
        "fraction of serum in total media",
        None,
        (),
        False,
    ),
    ("PBPKO_03066", ("PBPKO_03066", "FBS_PH"), "FBS pH", None, (), False),
    (
        "PBPKO_03067",
        ("PBPKO_03067", "INITIAL_NUMBER_OF_CELLS"),
        "initial number of cells",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03068",
        ("PBPKO_03068", "NOMINAL_CONCENTRATION_OF_MEDIUM"),
        "nominal concentration of medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03069",
        ("PBPKO_03069", "VOLUME_OF_MEDIUM"),
        "volume of medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03070",
        ("PBPKO_03070", "FRACTION_OF_FBS_IIN_THE_MEDIUM"),
        "fraction of FBS iin the medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03071",
        ("PBPKO_03071", "IONIZED_FRACTION_IN_THE_MEDIUM"),
        "ionized fraction in the medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03072",
        ("PBPKO_03072", "FRACTION_UNBOUND_IN_THE_MEDIUM"),
        "fraction unbound in the medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03073",
        ("PBPKO_03073", "FRACTION_UNBOUND_IN_THE_FBS"),
        "fraction unbound in the FBS",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03074",
        ("PBPKO_03074", "FRACTION_UNBOUND_IN_THE_CELL"),
        "fraction unbound in the cell",
        None,
        (),
        False,
    ),
    (
        "PBPKO_03075",
        ("PBPKO_03075", "ABSORPTION_RATE_CONSTANT"),
        "absorption rate constant",
        "A biochemical parameter representing the rate constant at which a compound is absorbed into systemic circulation or a target compartment from the site of administration",
        (),
        False,
    ),
    (
        "PBPKO_03076",
        ("PBPKO_03076", "FRACTION_UNBOUND_KIDNEY_PROXIMAL_TUBULE"),
        "fraction unbound kidney proximal tubule",
        "An unbound fraction parameter specifically for the kidney proximal tubule.",
        (),
        False,
    ),
    (
        "PBPKO_04001",
        ("PBPKO_04001", "PLASMA_FLOW_RATE"),
        "plasma flow rate",
        "A bodily fluid flow rate parameter specifically describing the flow of plasma to a compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04002",
        ("PBPKO_04002", "PLASMA_FLOW_RATE_TO_STOMACH"),
        "plasma flow rate to stomach",
        "A plasma flow rate parameter specifically describing the rate to the stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04003",
        ("PBPKO_04003", "PLASMA_FLOW_RATE_TO_INTESTINE"),
        "plasma flow rate to intestine",
        "A plasma flow rate parameter specifically describing the rate to the intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04004",
        ("PBPKO_04004", "PLASMA_FLOW_RATE_TO_SMALL_INTESTINE"),
        "plasma flow rate to small intestine",
        "A plasma flow rate parameter specifically describing the rate to the small intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04005",
        ("PBPKO_04005", "PLASMA_FLOW_RATE_TO_LARGE_INTESTINE"),
        "plasma flow rate to large intestine",
        "A plasma flow rate parameter specifically describing the rate to the large intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04006",
        ("PBPKO_04006", "PLASMA_FLOW_RATE_TO_PANCREAS"),
        "plasma flow rate to pancreas",
        "A plasma flow rate parameter specifically describing the rate to the pancreas compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04007",
        ("PBPKO_04007", "PLASMA_FLOW_RATE_TO_LIVER"),
        "plasma flow rate to liver",
        "A plasma flow rate parameter specifically describing the rate to the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04008",
        ("PBPKO_04008", "PLASMA_FLOW_RATE_TO_KIDNEY"),
        "plasma flow rate to kidney",
        "A plasma flow rate parameter specifically describing the rate to the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04009",
        ("PBPKO_04009", "PLASMA_FLOW_RATE_TO_MUSCLE"),
        "plasma flow rate to muscle",
        "A plasma flow rate parameter specifically describing the rate to the muscle compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04010",
        ("PBPKO_04010", "PLASMA_FLOW_RATE_TO_HEART"),
        "plasma flow rate to heart",
        "A plasma flow rate parameter specifically describing the rate to the heart compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04011",
        ("PBPKO_04011", "PLASMA_FLOW_RATE_TO_FAT"),
        "plasma flow rate to fat",
        "A plasma flow rate parameter specifically describing the rate to the fat compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04012",
        ("PBPKO_04012", "PLASMA_FLOW_RATE_TO_GONAD"),
        "plasma flow rate to gonad",
        "A plasma flow rate parameter specifically describing the rate to the gonad compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04013",
        ("PBPKO_04013", "PLASMA_FLOW_RATE_TO_SKIN"),
        "plasma flow rate to skin",
        "A plasma flow rate parameter specifically describing the rate to the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04014",
        ("PBPKO_04014", "PLASMA_FLOW_RATE_TO_BONE"),
        "plasma flow rate to bone",
        "A plasma flow rate parameter specifically describing the rate to the bone compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04015",
        ("PBPKO_04015", "PLASMA_FLOW_RATE_TO_BRAIN"),
        "plasma flow rate to brain",
        "A plasma flow rate parameter specifically describing the rate to the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04016",
        ("PBPKO_04016", "PLASMA_FLOW_RATE_TO_SPLEEN"),
        "plasma flow rate to spleen",
        "A plasma flow rate parameter specifically describing the rate to the spleen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04017",
        ("PBPKO_04017", "PLASMA_FLOW_RATE_TO_LUNG"),
        "plasma flow rate to lung",
        "A plasma flow rate parameter specifically describing the rate to the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04018",
        ("PBPKO_04018", "PLASMA_FLOW_RATE_TO_POORLY_PERFUSED"),
        "plasma flow rate to poorly perfused",
        "A plasma flow rate parameter specifically describing the rate to the poorly perfused compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04019",
        ("PBPKO_04019", "PLASMA_FLOW_RATE_TO_RICHLY_PERFUSED"),
        "plasma flow rate to richly perfused",
        "A plasma flow rate parameter specifically describing the rate to the richly perfused compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04020",
        ("PBPKO_04020", "PLASMA_FLOW_RATE_TO_RESTBODY"),
        "plasma flow rate to restbody",
        "A plasma flow rate parameter specifically describing the rate to the rest of the body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04021",
        ("PBPKO_04021", "PLASMA_FLOW_RATE_TO_GALL_BLADDER"),
        "plasma flow rate to gall bladder",
        "A plasma flow rate parameter specifically describing the rate to the gall bladder compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04022",
        ("PBPKO_04022", "PLASMA_FLOW_RATE_TO_PORTAL_VEIN"),
        "plasma flow rate to portal vein",
        "A plasma flow rate parameter specifically describing the rate to the portal vein compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04023",
        ("PBPKO_04023", "PLASMA_FLOW_RATE_TO_LYMPH"),
        "plasma flow rate to lymph",
        "A plasma flow rate parameter specifically describing the rate to the lymph compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04024",
        ("PBPKO_04024", "PLASMA_FLOW_RATE_TO_DUODENUM"),
        "plasma flow rate to duodenum",
        "A plasma flow rate parameter specifically describing the rate to the duodenum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04025",
        ("PBPKO_04025", "PLASMA_FLOW_RATE_TO_JEJUNUM"),
        "plasma flow rate to jejunum",
        "A plasma flow rate parameter specifically describing the rate to the jejunum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04026",
        ("PBPKO_04026", "PLASMA_FLOW_RATE_TO_ILEUM"),
        "plasma flow rate to ileum",
        "A plasma flow rate parameter specifically describing the rate to the ileum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04027",
        ("PBPKO_04027", "PLASMA_FLOW_RATE_TO_COLON"),
        "plasma flow rate to colon",
        "A plasma flow rate parameter specifically describing the rate to the colon compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04028",
        ("PBPKO_04028", "PLASMA_FLOW_RATE_TO_CECUM"),
        "plasma flow rate to cecum",
        "A plasma flow rate parameter specifically describing the rate to the cecum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04029",
        ("PBPKO_04029", "PLASMA_FLOW_RATE_TO_FILTRATE"),
        "plasma flow rate to filtrate",
        "A plasma flow rate parameter specifically describing the rate to the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04030",
        ("PBPKO_04030", "PLASMA_FLOW_RATE_TO_BONE_MARROW"),
        "plasma flow rate to bone marrow",
        "A plasma flow parameter specifically describing the rate to the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04031",
        ("PBPKO_04031", "PLASMA_FLOW_RATE_TO_GUT"),
        "plasma flow rate to gut",
        "A plasma flow rate parameter specifically describing the rate to the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04032",
        ("PBPKO_04032", "PLASMA_FLOW_RATE_TO_MAMMARY_GLAND"),
        "plasma flow rate to mammary gland",
        "A plasma flow rate parameter specifically describing the rate to the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04033",
        ("PBPKO_04033", "PLASMA_FLOW_RATE_FOR_MASS_BALANCE"),
        "plasma flow rate for mass balance",
        "A plasma flow rate parameter representing the check for total plasma flow mass balance of all the compartments (sum of organ flows should equal cardiac output).",
        (),
        False,
    ),
    (
        "PBPKO_04034",
        ("PBPKO_04034", "PLASMA_FLOW_RATE_TO_UNEXPOSED_SKIN"),
        "plasma flow rate to unexposed skin",
        "A plasma flow rate parameter specifically describing the rate to the unexposed skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04035",
        ("PBPKO_04035", "PLASMA_FLOW_RATE_TO_EXPOSED_SKIN"),
        "plasma flow rate to exposed skin",
        "A plasma flow rate parameter specifically describing the rate to the exposed skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04036",
        ("PBPKO_04036", "PLASMA_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_UNEXPOSED"),
        "plasma flow rate to skin stratum corneum unexposed",
        "A plasma flow rate parameter specifically describing the rate to the unexposed stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04037",
        ("PBPKO_04037", "PLASMA_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_EXPOSED"),
        "plasma flow rate to skin stratum corneum exposed",
        "A plasma flow rate parameter specifically describing the rate to the exposed stratum corneum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04038",
        ("PBPKO_04038", "FRACTION_OF_BLOOD_FLOW_TO_RED_BLOOD_CELLS"),
        "fraction of blood flow to red blood cells",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04039",
        ("PBPKO_04039", "BLOOD_FLOW_RATE_TO_RED_BLOOD_CELLS"),
        "blood flow rate to red blood cells",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04040",
        ("PBPKO_04040", "VOLUMEN_OF_LUMEN"),
        "volumen of lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04041",
        ("PBPKO_04041", "VOLUME_OF_SMALL_INTESTINE_TISSUE"),
        "volume of small intestine tissue",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04042",
        ("PBPKO_04042", "VOLUME_OF_BILE"),
        "volume of bile",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04043",
        ("PBPKO_04043", "ENTEROCYTE_VOLUME"),
        "enterocyte volume",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04044",
        ("PBPKO_04044", "HEPATIC_VEIN_BLOOD_FLOW"),
        "hepatic vein blood flow",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04045",
        ("PBPKO_04045", "BLOOD_FLOW_RATE_TO_BILE"),
        "blood flow rate to bile",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04046",
        ("PBPKO_04046", "DIAMETER_OF_INTESTINAL"),
        "diameter of intestinal",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04047",
        ("PBPKO_04047", "DIAMETER_OF_THE_JEJUNUM_LUMEN"),
        "diameter of the jejunum lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04048",
        ("PBPKO_04048", "DIAMETER_OF_THE_ILEUM_LUMEN"),
        "diameter of the ileum lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04049",
        ("PBPKO_04049", "DIAMETER_OF_THE_LARGE_INTESTINE_LUMEN"),
        "diameter of the large intestine lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04050",
        ("PBPKO_04050", "SURFACE_AREA__OF_THE_JEJUNUM_LUMEN"),
        "surface area  of the jejunum lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04051",
        ("PBPKO_04051", "SURFACE_AREA_OF_THE_ILEUM_LUMEN"),
        "surface area of the ileum lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04052",
        ("PBPKO_04052", "SURFACE_AREA_OF_THE_LARGE_INTESTINE_LUMEN"),
        "surface area of the large intestine lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04053",
        ("PBPKO_04053", "UPTAKE_FRACTION_TO_BLOOD"),
        "uptake fraction to blood",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04054",
        ("PBPKO_04054", "FRACTION_OF_BILE_IN_SMALL_INTESTINE"),
        "fraction of bile in small intestine",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04055",
        ("PBPKO_04055", "FRACTION_OF_BILE_IN_LIVER"),
        "fraction of bile in liver",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04056",
        ("PBPKO_04056", "FRACTION_OF_FECES"),
        "fraction of feces",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04057",
        ("PBPKO_04057", "VOLUME_FRACTION_OF_BLOOD"),
        "volume fraction of blood",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04058",
        ("PBPKO_04058", "VOLUME_FRACTION_OF_RED_BLOOD_CELLS"),
        "volume fraction of red blood cells",
        None,
        (),
        False,
    ),
    ("PBPKO_04059", ("PBPKO_04059", "SKIN_AREA"), "skin area", None, (), False),
    (
        "PBPKO_04060",
        ("PBPKO_04060", "THICKNESS_EPIDERMIS"),
        "thickness epidermis",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04061",
        ("PBPKO_04061", "VOLUME_OF_EXPOSED_VIABLE_EPIDERMIS"),
        "volume of exposed viable epidermis",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04062",
        ("PBPKO_04062", "VOLUME_OF_FOLLICLE"),
        "volume of follicle",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04063",
        ("PBPKO_04063", "AREA_OF_EXPOSED_SKIN"),
        "area of exposed skin",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04064",
        ("PBPKO_04064", "VOLUME_OF_SERUM"),
        "volume of serum",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04065",
        ("PBPKO_04065", "VOLUME_OF_ADRENALS"),
        "volume of adrenals",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04066",
        ("PBPKO_04066", "VOLUME_OF_BREAST"),
        "volume of breast",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04067",
        ("PBPKO_04067", "VOLUME_OF_THYROID"),
        "volume of thyroid",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04068",
        ("PBPKO_04068", "VOLUME_OF_INTESTINAL_LUMEN"),
        "volume of intestinal lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04069",
        ("PBPKO_04069", "VOLUME_OF_SMALL_INTESTINAL_LUMEN"),
        "volume of small intestinal lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04070",
        ("PBPKO_04070", "VOLUME_OF_LARGE_INTESTINAL_LUMEN"),
        "volume of large intestinal lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04071",
        ("PBPKO_04071", "VOLUME_OF_STOMACH_LUMEN"),
        "volume of stomach lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04072",
        ("PBPKO_04072", "VOLUME_OF_GUT_INTESTINAL_TRACT"),
        "volume of gut intestinal tract",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04073",
        ("PBPKO_04073", "VOLUME_OF_TESTIS"),
        "volume of testis",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04074",
        ("PBPKO_04074", "VOLUME_OF_UTERUS"),
        "volume of uterus",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04075",
        ("PBPKO_04075", "VOLUME_OF_SKELETON"),
        "volume of skeleton",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04076",
        ("PBPKO_04076", "VOLUME_OF_HAIR"),
        "volume of hair",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04077",
        ("PBPKO_04077", "VOLUME_OF_URINARY_TRACT"),
        "volume of urinary tract",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04078",
        ("PBPKO_04078", "VOLUME_OF_SKIN_SURFACE_DEPOT"),
        "volume of skin surface depot",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04079",
        ("PBPKO_04079", "VOLUME_OF_CORTICAL_BONE"),
        "volume of cortical bone",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04080",
        ("PBPKO_04080", "VOLUME_OF_TRABECULAR_BONE"),
        "volume of trabecular bone",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04081",
        ("PBPKO_04081", "VOLUME_OF_ALVEOLAR_COMPARTMENT"),
        "volume of alveolar compartment",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04082",
        ("PBPKO_04082", "FRACTION_OF_SERUM"),
        "fraction of serum",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04083",
        ("PBPKO_04083", "FRACTION_OF_ADRENALS"),
        "fraction of adrenals",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04084",
        ("PBPKO_04084", "FRACTION_OF_BREAST"),
        "fraction of breast",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04085",
        ("PBPKO_04085", "FRACTION_OF_THYROID"),
        "fraction of thyroid",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04086",
        ("PBPKO_04086", "FRACTION_OF_INTESTINAL_LUMEN"),
        "fraction of intestinal lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04087",
        ("PBPKO_04087", "FRACTION_OF_SMALL_INTESTINAL_LUMEN"),
        "fraction of small intestinal lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04088",
        ("PBPKO_04088", "FRACTION_OF_LARGE_INTESTINAL_LUMEN"),
        "fraction of large intestinal lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04089",
        ("PBPKO_04089", "FRACTION_OF_STOMACH_LUMEN"),
        "fraction of stomach lumen",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04090",
        ("PBPKO_04090", "FRACTION_OF_GUT_INTESTINAL_TRACT"),
        "fraction of gut intestinal tract",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04091",
        ("PBPKO_04091", "FRACTION_OF_TESTIS"),
        "fraction of testis",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04092",
        ("PBPKO_04092", "FRACTION_OF_UTERUS"),
        "fraction of uterus",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04093",
        ("PBPKO_04093", "FRACTION_OF_SKELETON"),
        "fraction of skeleton",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04094",
        ("PBPKO_04094", "FRACTION_OF_HAIR"),
        "fraction of hair",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04095",
        ("PBPKO_04095", "FRACTION_OF_AMNIOTIC_FLUID"),
        "fraction of amniotic fluid",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04096",
        ("PBPKO_04096", "FRACTION_OF_URINARY_TRACT"),
        "fraction of urinary tract",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04097",
        ("PBPKO_04097", "FRACTION_OF_CORTICAL_BONE"),
        "fraction of cortical bone",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04098",
        ("PBPKO_04098", "FRACTION_OF_TRABECULAR_BONE"),
        "fraction of trabecular bone",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04099",
        ("PBPKO_04099", "FRACTION_OF_THE_SKIN_SURFACE_DEPOT"),
        "fraction of the skin surface depot",
        None,
        (),
        False,
    ),
    (
        "PBPKO_04100",
        ("PBPKO_04100", "FRACTION_OF_BLOOD"),
        "fraction of blood",
        "A dimensionless fraction of volume defined as the blood volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_04101",
        ("PBPKO_04101", "FRACTION_OF_BONE_MARROW"),
        "fraction of bone marrow",
        "A dimensionless fraction of volume defined as the bone marrow volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_04102",
        ("PBPKO_04102", "FRACTION_OF_BONE_NON_PERFUSED"),
        "fraction of bone non perfused",
        "A dimensionless fraction of volume defined as the bone non perfuse volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_04103",
        ("PBPKO_04103", "FRACTION_OF_ADIPOSE_MASS"),
        "fraction of adipose mass",
        "A dimensionless fraction of volume defined as the adipose mass volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_04104",
        ("PBPKO_04104", "FRACTION_OF_INTESTINAL_TISSUE"),
        "fraction of intestinal tissue",
        "A dimensionless fraction of volume defined as the intestinal tissue volume divided per unit of total body weight.",
        (),
        False,
    ),
    (
        "PBPKO_04105",
        ("PBPKO_04105", "VOLUME_OF_KIDNEY_REST_TISSUE"),
        "volume of kidney rest tissue",
        "A volume parameter representing the total volume of the kidney rest tissue compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04106",
        ("PBPKO_04106", "VOLUME_OF_KIDNEY_REST_LUMEN"),
        "volume of kidney rest lumen",
        "A volume parameter representing the total volume of the kidney rest lumen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04107",
        ("PBPKO_04107", "VOLUME_OF_KIDNEY_PROXIMAL_TUBULE_LUMEN"),
        "volume of kidney proximal tubule lumen",
        "A volume parameter representing the total volume of the lumen of kidney proximal tubule compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04108",
        ("PBPKO_04108", "VOLUME_OF_KIDNEY_PROXIMAL_TUBULE_TISSUE"),
        "volume of kidney proximal tubule tissue",
        "A volume parameter representing the total volume of the tissue of kidney proximal tubule compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04109",
        ("PBPKO_04109", "VOLUME_OF_LIVER_EXTRACELLULAR"),
        "volume of liver extracellular",
        "A volume parameter representing the total volume of the vascular and interstitial spaces of liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04110",
        ("PBPKO_04110", "VOLUME_OF_LIVER_INTRACELLULAR_SPACE"),
        "volume of liver intracellular space",
        "A volume parameter representing the total volume of the hepatocytes in liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_04111",
        ("PBPKO_04111", "VOLUME_OF_INTESTINE_TISSUE"),
        "volume of intestine tissue",
        "A volume parameter representing the total volume of the tissue of intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_05001",
        ("PBPKO_05001", "MOLAR_VOLUME"),
        "molar volume",
        "A physicochemical parameter representing the volume of one mole of a molecule.",
        (),
        False,
    ),
    (
        "PBPKO_05002",
        ("PBPKO_05002", "HENRY_S_LAW_CONSTANT"),
        "Henry's law constant",
        "A physicochemical parameter describing the volatily of a compound",
        (),
        False,
    ),
    (
        "PBPKO_05003",
        ("PBPKO_05003", "VAPOR_PRESSURE"),
        "vapor pressure",
        "A physicochemical parameter describing the vapor pressure of the compound",
        (),
        False,
    ),
    (
        "PBPKO_06002",
        ("PBPKO_06002", "UNBOUND_VENOUS_CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT"),
        "unbound venous concentration of compound in compartment",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06003",
        ("PBPKO_06003", "UNBOUND_CONCENTRATION_OF_COMPUND_IN_COMPARTMENT"),
        "unbound concentration of compund in compartment",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06004",
        ("PBPKO_06004", "AMOUNT_IN_STOMACH"),
        "amount in stomach",
        "The amount of chemical in stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06005",
        ("PBPKO_06005", "AMOUNT_IN_SMALL_INTESTINE"),
        "amount in small intestine",
        "The amount of chemical in small intestine compartment",
        (),
        False,
    ),
    (
        "PBPKO_06006",
        ("PBPKO_06006", "AMOUNT_IN_JEJUNUM"),
        "amount in jejunum",
        "The amount of chemical in jejunum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06007",
        ("PBPKO_06007", "AMOUNT_IN_ILEUM"),
        "amount in ileum",
        "The amount of chemical in ileum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06008",
        ("PBPKO_06008", "AMOUNT_IN__LARGE_INTESTINE"),
        "amount in  large intestine",
        "The amount of chemical in large intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06009",
        ("PBPKO_06009", "AMOUNT_IN_LUMEN"),
        "amount in lumen",
        "The amount of chemical in lumen of the intestine.",
        (),
        False,
    ),
    (
        "PBPKO_06010",
        ("PBPKO_06010", "AMOUNT_IN_SMALL_INTESTINE_SEGMENT"),
        "amount in small intestine segment",
        "The amount of chemical in segment of small intestine.",
        (),
        False,
    ),
    (
        "PBPKO_06011",
        ("PBPKO_06011", "AMOUNT_IN_COLON"),
        "amount in colon",
        "The amount of chemical in colon compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06012",
        ("PBPKO_06012", "AMOUNT_IN_BILE"),
        "amount in bile",
        "The amount of chemical in bile.",
        (),
        False,
    ),
    (
        "PBPKO_06013",
        ("PBPKO_06013", "AMOUNT_IN_SPLEEN"),
        "amount in spleen",
        "The amount of chemical in spleen compartment",
        (),
        False,
    ),
    (
        "PBPKO_06014",
        ("PBPKO_06014", "AMOUNT_IN_DUODENUM"),
        "amount in duodenum",
        "The amount of chemical in duodenum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06015",
        ("PBPKO_06015", "AMOUNT_IN_INTESTINAL_TISSUE"),
        "amount in intestinal tissue",
        "The amount of chemical in intestinal tissue",
        (),
        False,
    ),
    (
        "PBPKO_06016",
        ("PBPKO_06016", "AMOUNT_IN_PORTAL_VEIN"),
        "amount in portal vein",
        "The amount of chemical in portal vein.",
        (),
        False,
    ),
    (
        "PBPKO_06017",
        ("PBPKO_06017", "UNBOUND_CONCENTRATION_IN_PLASMA"),
        "unbound concentration in plasma",
        "The unbound concentration of compound in the plasma compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06018",
        ("PBPKO_06018", "UNBOUND_VENOUS_LIVER_CONCENTRATION"),
        "unbound venous liver concentration",
        "The unbound venous concentration of compound in the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06019",
        ("PBPKO_06019", "UNBOUND_VENOUS_GUT_CONCENTRATION"),
        "unbound venous gut concentration",
        "The unbound venous concentration of compound in the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06020",
        ("PBPKO_06020", "UNBOUND_VENOUS_BRAIN_CONCENTRATION"),
        "unbound venous brain concentration",
        "The unbound venous concentration of compound in the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06021",
        ("PBPKO_06021", "UNBOUND_VENOUS_KIDNEY_CONCENTRATION"),
        "unbound venous kidney concentration",
        "The unbound venous concentration of compound in the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06022",
        ("PBPKO_06022", "UNBOUND_VENOUS_FILTRATE_CONCENTRATION"),
        "unbound venous filtrate concentration",
        "The unbound venous concentration of compound in the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06023",
        ("PBPKO_06023", "UNBOUND_VENOUS_LUNG_CONCENTRATION"),
        "unbound venous lung concentration",
        "The unbound venous concentration of compound in the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06024",
        ("PBPKO_06024", "UNBOUND_VENOUS_FAT_CONCENTRATION"),
        "unbound venous fat concentration",
        "The unbound venous concentration of compound in the fat compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06025",
        ("PBPKO_06025", "UNBOUND_VENOUS_BONE_MARROW_CONCENTRATION"),
        "unbound venous bone marrow concentration",
        "The unbound venous concentration of compound in the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06026",
        ("PBPKO_06026", "UNBOUND_VENOUS_SKIN_CONCENTRATION"),
        "unbound venous skin concentration",
        "The unbound venous concentration of compound in the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06027",
        ("PBPKO_06027", "UNBOUND_VENOUS_MAMMARY_GLAND_CONCENTRATION"),
        "unbound venous mammary gland concentration",
        "The unbound venous concentration of compound in the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06028",
        ("PBPKO_06028", "UNBOUND_VENOUS_REST_BODY_CONCENTRATION"),
        "unbound venous rest body concentration",
        "The unbound venous concentration of compound in the rest body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06029",
        ("PBPKO_06029", "TOTAL_VENOUS_CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT"),
        "total venous concentration of compound in compartment",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06030",
        ("PBPKO_06030", "TOTAL_VENOUS_LIVER_CONCENTRATION"),
        "total venous liver concentration",
        "The total venous concentration of compound in the liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06031",
        ("PBPKO_06031", "TOTAL_VENOUS_GUT_CONCENTRATION"),
        "total venous gut concentration",
        "The total venous concentration of compound in the gut compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06032",
        ("PBPKO_06032", "TOTAL_VENOUS_KIDNEY_CONCENTRATION"),
        "total venous kidney concentration",
        "The total venous concentration of compound in the kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06033",
        ("PBPKO_06033", "TOTAL_VENOUS_BRAIN_CONCENTRATION"),
        "total venous brain concentration",
        "The total venous concentration of compound in the brain compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06034",
        ("PBPKO_06034", "TOTAL_VENOUS_FILTRATE_CONCENTRATION"),
        "total venous filtrate concentration",
        "The total venous concentration of compound in the filtrate compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06035",
        ("PBPKO_06035", "TOTAL_VENOUS_LUNG_CONCENTRATION"),
        "total venous lung concentration",
        "The total venous concentration of compound in the lung compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06036",
        ("PBPKO_06036", "TOTAL_VENOUS_FAT_CONCENTRATION"),
        "total venous fat concentration",
        "The total venous concentration of compound in the fat compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06037",
        ("PBPKO_06037", "TOTAL_VENOUS_BONE_MARROW_CONCENTRATION"),
        "total venous bone marrow concentration",
        "The total venous concentration of compound in the bone marrow compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06038",
        ("PBPKO_06038", "TOTAL_VENOUS_SKIN_CONCENTRATION"),
        "total venous skin concentration",
        "The total venous concentration of compound in the skin compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06039",
        ("PBPKO_06039", "TOTAL_VENOUS_MAMMARY_GLAND_CONCENTRATION"),
        "total venous mammary gland concentration",
        "The total venous concentration of compound in the mammary gland compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06040",
        ("PBPKO_06040", "TOTAL_VENOUS_REST_BODY_CONCENTRATION"),
        "total venous rest body concentration",
        "The total venous concentration of compound in the rest of the body compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06041",
        ("PBPKO_06041", "CONCENTRATION_IN_STOMACH"),
        "concentration in stomach",
        "The concentration of chemical in stomach compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06042",
        ("PBPKO_06042", "CONCENTRATION_IN_SMALL_INTESTINE"),
        "concentration in small intestine",
        "The concentration of chemical in small intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06043",
        ("PBPKO_06043", "CONCENTRATION_IN_JEJUNUM"),
        "concentration in jejunum",
        "The concentration of chemical in jejunum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06044",
        ("PBPKO_06044", "CONCENTRATION_IN_ILEUM"),
        "concentration in ileum",
        "The concentration of chemical in ileum compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06045",
        ("PBPKO_06045", "CONCENTRATION_IN_LARGE_INTESTINE"),
        "concentration in large intestine",
        "The concentration of chemical in large intestine compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06046",
        ("PBPKO_06046", "CONCENTRATION_IN_INTESTINAL_TISSUE"),
        "concentration in intestinal tissue",
        "The concentration of chemical in tissue of intestine.",
        (),
        False,
    ),
    (
        "PBPKO_06047",
        ("PBPKO_06047", "CONCENTRATION_IN_LUMEN"),
        "concentration in lumen",
        "The concentration of chemical in lumen of intestine.",
        (),
        False,
    ),
    (
        "PBPKO_06048",
        ("PBPKO_06048", "CONCENTRATION_IN_BILE"),
        "concentration in bile",
        "The concentration of chemical in bile.",
        (),
        False,
    ),
    (
        "PBPKO_06049",
        ("PBPKO_06049", "CONCENTRATION_IN_SPLEEN"),
        "concentration in spleen",
        "The concentration of chemical in spleen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06050",
        ("PBPKO_06050", "CONCENTRATION_IN_FECES"),
        "concentration in feces",
        "The concentration of chemical in feces.",
        (),
        False,
    ),
    (
        "PBPKO_06051",
        ("PBPKO_06051", "AMOUNT_IN_SKIN_SURFACE_DEPOT"),
        "amount in skin surface depot",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06052",
        ("PBPKO_06052", "MAXIMUM_AMOUNT"),
        "maximum amount",
        "The maximum amount of chemical in a compartment",
        (),
        False,
    ),
    (
        "PBPKO_06053",
        ("PBPKO_06053", "AMOUNT_IN_FOLLICLES"),
        "amount in follicles",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06054",
        ("PBPKO_06054", "CONCENTRATION_IN_MEDIUM"),
        "concentration in medium",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06055",
        ("PBPKO_06055", "CONCENTRATION_IN_CELL"),
        "concentration in cell",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06056",
        ("PBPKO_06056", "CONCENTRATION_IN_MITOCHONDRIA"),
        "concentration in mitochondria",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06057",
        ("PBPKO_06057", "CONCENTRATION_IN_LYSOSOMES"),
        "concentration in lysosomes",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06058",
        ("PBPKO_06058", "CONCENTRATION_IN_MICROSOMES"),
        "concentration in microsomes",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06059",
        ("PBPKO_06059", "CONCENTRATION_IN_INTRACELLULAR_WATER"),
        "concentration in intracellular water",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06060",
        ("PBPKO_06060", "CONCENTRATION_IN_POLYMER"),
        "concentration in polymer",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06061",
        ("PBPKO_06061", "CONCENTRATION_IN_AIR"),
        "concentration in air",
        None,
        (),
        False,
    ),
    (
        "PBPKO_06062",
        ("PBPKO_06062", "AMOUNT_IN_MENSTRUAL"),
        "amount in menstrual",
        "The amount of compound in the menstrual compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06063",
        ("PBPKO_06063", "AMOUNT_IN_KIDNEY_REST_TISSUE"),
        "amount in kidney rest tissue",
        "The amount of compound in the kidney rest tissue compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06064",
        ("PBPKO_06064", "AMOUNT_IN_KIDNEY_REST_LUMEN"),
        "amount in kidney rest lumen",
        "The amount of compound in the rest of kidney lumen compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06065",
        ("PBPKO_06065", "AMOUNT_IN_KIDNEY_PROXIMAL_TUBULE_TISSUE"),
        "amount in kidney proximal tubule tissue",
        "The amount of compound in the proximal tubule tissue of kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06066",
        ("PBPKO_06066", "AMOUNT_IN_KIDNEY_PROXIMAL_TUBULE_LUMEN"),
        "amount in kidney proximal tubule lumen",
        "The amount of compound in the proximal tubule lumen of kidney compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06067",
        ("PBPKO_06067", "AMOUNT_IN_LIVER_INTRACELLULAR"),
        "amount in liver intracellular",
        "The amount of compound in the intracellular spaceof liver compartment.",
        (),
        False,
    ),
    (
        "PBPKO_06068",
        ("PBPKO_06068", "AMOUNT_IN_LIVER_EXTRACELLULAR"),
        "amount in liver extracellular",
        "The amount of compound in the extracellular space of liver compartment.",
        (),
        False,
    ),
    ("PBPKO_07001", ("PBPKO_07001", "INVITRO_PBPK"), "invitro pbpk", None, (), False),
    (
        "PR_000000001",
        ("PR_000000001", "PROTEIN"),
        "protein",
        "An amino acid chain that is produced de novo by ribosome-mediated translation of a genetically-encoded mRNA, and any derivatives thereof.",
        (),
        False,
    ),
    (
        "PR_000018263",
        ("PR_000018263", "AMINO_ACID_CHAIN"),
        "amino acid chain",
        "An organic amino compound that consists of amino acid residues (unmodified amino-acid residues and/or modified amino-acid residues) linked by peptide bonds or derivatives of such bonds.",
        (),
        False,
    ),
    (
        "RO_0000052",
        ("RO_0000052", "CHARACTERISTIC_OF"),
        "characteristic of",
        "a relation between a specifically dependent continuant (the characteristic) and any other entity (the bearer), in which the characteristic depends on the bearer for its existence.",
        (),
        False,
    ),
    (
        "RO_0000053",
        ("RO_0000053", "HAS_CHARACTERISTIC"),
        "has characteristic",
        "Inverse of characteristic_of",
        (),
        False,
    ),
    (
        "RO_0000056",
        ("RO_0000056", "PARTICIPATES_IN"),
        "participates in",
        "a relation between a continuant and a process, in which the continuant is somehow involved in the process",
        (),
        False,
    ),
    (
        "RO_0000057",
        ("RO_0000057", "HAS_PARTICIPANT"),
        "has participant",
        "a relation between a process and a continuant, in which the continuant is somehow involved in the process",
        (),
        False,
    ),
    (
        "RO_0000059",
        ("RO_0000059", "CONCRETIZES"),
        "concretizes",
        "A relationship between a specifically dependent continuant and a generically dependent continuant, in which the generically dependent continuant depends on some independent continuant in virtue of the fact that the specifically dependent continuant also depends on that same independent continuant. Multiple specifically dependent continuants can concretize the same generically dependent continuant.",
        (),
        False,
    ),
    (
        "RO_0000079",
        ("RO_0000079", "FUNCTION_OF"),
        "function of",
        "a relation between a function and an independent continuant (the bearer), in which the function specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000080",
        ("RO_0000080", "QUALITY_OF"),
        "quality of",
        "a relation between a quality and an independent continuant (the bearer), in which the quality specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000081",
        ("RO_0000081", "ROLE_OF"),
        "role of",
        "a relation between a role and an independent continuant (the bearer), in which the role specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000085",
        ("RO_0000085", "HAS_FUNCTION"),
        "has function",
        "a relation between an independent continuant (the bearer) and a function, in which the function specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000086",
        ("RO_0000086", "HAS_QUALITY"),
        "has quality",
        "a relation between an independent continuant (the bearer) and a quality, in which the quality specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000087",
        ("RO_0000087", "HAS_ROLE"),
        "has role",
        "a relation between an independent continuant (the bearer) and a role, in which the role specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000091",
        ("RO_0000091", "HAS_DISPOSITION"),
        "has disposition",
        "a relation between an independent continuant (the bearer) and a disposition, in which the disposition specifically depends on the bearer for its existence",
        (),
        False,
    ),
    (
        "RO_0000092",
        ("RO_0000092", "DISPOSITION_OF"),
        "disposition of",
        "inverse of has disposition",
        (),
        False,
    ),
    (
        "RO_0002013",
        ("RO_0002013", "HAS_REGULATORY_COMPONENT_ACTIVITY"),
        "has regulatory component activity",
        "A 'has regulatory component activity' B if A and B are GO molecular functions (GO_0003674), A has_component B and A is regulated by B.",
        (),
        False,
    ),
    (
        "RO_0002014",
        ("RO_0002014", "HAS_NEGATIVE_REGULATORY_COMPONENT_ACTIVITY"),
        "has negative regulatory component activity",
        "A relationship that holds between a GO molecular function and a component of that molecular function that negatively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is negatively regulated by B.",
        (),
        False,
    ),
    (
        "RO_0002015",
        ("RO_0002015", "HAS_POSITIVE_REGULATORY_COMPONENT_ACTIVITY"),
        "has positive regulatory component activity",
        "A relationship that holds between a GO molecular function and a component of that molecular function that positively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is positively regulated by B.",
        (),
        False,
    ),
    (
        "RO_0002017",
        ("RO_0002017", "HAS_COMPONENT_ACTIVITY"),
        "has component activity",
        None,
        (),
        False,
    ),
    (
        "RO_0002018",
        ("RO_0002018", "HAS_COMPONENT_PROCESS"),
        "has component process",
        "w 'has process component' p if p and w are processes, w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type.",
        (),
        False,
    ),
    (
        "RO_0002022",
        ("RO_0002022", "DIRECTLY_REGULATED_BY"),
        "directly regulated by",
        None,
        (),
        False,
    ),
    (
        "RO_0002023",
        ("RO_0002023", "DIRECTLY_NEGATIVELY_REGULATED_BY"),
        "directly negatively regulated by",
        None,
        (),
        False,
    ),
    (
        "RO_0002024",
        ("RO_0002024", "DIRECTLY_POSITIVELY_REGULATED_BY"),
        "directly positively regulated by",
        None,
        (),
        False,
    ),
    (
        "RO_0002025",
        ("RO_0002025", "HAS_EFFECTOR_ACTIVITY"),
        "has effector activity",
        None,
        (),
        False,
    ),
    ("RO_0002086", ("RO_0002086", "ENDS_AFTER"), "ends after", None, (), False),
    (
        "RO_0002087",
        ("RO_0002087", "IMMEDIATELY_PRECEDED_BY"),
        "immediately preceded by",
        None,
        (),
        False,
    ),
    (
        "RO_0002090",
        ("RO_0002090", "IMMEDIATELY_PRECEDES"),
        "immediately precedes",
        None,
        (),
        False,
    ),
    (
        "RO_0002131",
        ("RO_0002131", "OVERLAPS"),
        "overlaps",
        "x overlaps y if and only if there exists some z such that x has part z and z part of y",
        (),
        False,
    ),
    (
        "RO_0002180",
        ("RO_0002180", "HAS_COMPONENT"),
        "has component",
        "w 'has component' p if w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type.",
        (),
        False,
    ),
    (
        "RO_0002211",
        ("RO_0002211", "REGULATES"),
        "regulates",
        "p regulates q iff p is causally upstream of q, the execution of p is not constant and varies according to specific conditions, and p influences the rate or magnitude of execution of q due to an effect either on some enabler of q or some enabler of a part of q.",
        (),
        False,
    ),
    (
        "RO_0002212",
        ("RO_0002212", "NEGATIVELY_REGULATES"),
        "negatively regulates",
        "p negatively regulates q iff p regulates q, and p decreases the rate or magnitude of execution of q.",
        (),
        False,
    ),
    (
        "RO_0002213",
        ("RO_0002213", "POSITIVELY_REGULATES"),
        "positively regulates",
        "p positively regulates q iff p regulates q, and p increases the rate or magnitude of execution of q.",
        (),
        False,
    ),
    (
        "RO_0002215",
        ("RO_0002215", "CAPABLE_OF"),
        "capable of",
        "A relation between a material entity (such as a cell) and a process, in which the material entity has the ability to carry out the process.",
        (),
        False,
    ),
    (
        "RO_0002216",
        ("RO_0002216", "CAPABLE_OF_PART_OF"),
        "capable of part of",
        "c stands in this relationship to p if and only if there exists some p' such that c is capable_of p', and p' is part_of p.",
        (),
        False,
    ),
    (
        "RO_0002222",
        ("RO_0002222", "TEMPORALLY_RELATED_TO"),
        "temporally related to",
        None,
        (),
        False,
    ),
    (
        "RO_0002233",
        ("RO_0002233", "HAS_INPUT"),
        "has input",
        "p has input c iff: p is a process, c is a material entity, c is a participant in p, c is present at the start of p, and the state of c is modified during p.",
        (),
        False,
    ),
    (
        "RO_0002263",
        ("RO_0002263", "ACTS_UPSTREAM_OF"),
        "acts upstream of",
        "c acts upstream of p if and only if c enables some f that is involved in p' and p' occurs chronologically before p, is not part of p, and affects the execution of p. c is a material entity and f, p, p' are processes.",
        (),
        False,
    ),
    (
        "RO_0002264",
        ("RO_0002264", "ACTS_UPSTREAM_OF_OR_WITHIN"),
        "acts upstream of or within",
        "c acts upstream of or within p if c is enables f, and f is causally upstream of or within p. c is a material entity and p is an process.",
        (),
        False,
    ),
    (
        "RO_0002304",
        ("RO_0002304", "CAUSALLY_UPSTREAM_OF__POSITIVE_EFFECT"),
        "causally upstream of, positive effect",
        "p is causally upstream of, positive effect q iff p is casually upstream of q, and the execution of p is required for the execution of q.",
        (),
        False,
    ),
    (
        "RO_0002305",
        ("RO_0002305", "CAUSALLY_UPSTREAM_OF__NEGATIVE_EFFECT"),
        "causally upstream of, negative effect",
        "p is causally upstream of, negative effect q iff p is casually upstream of q, and the execution of p decreases the execution of q.",
        (),
        False,
    ),
    (
        "RO_0002314",
        ("RO_0002314", "CHARACTERISTIC_OF_PART_OF"),
        "characteristic of part of",
        "q characteristic of part of w if and only if there exists some p such that q inheres in p and p part of w.",
        (),
        False,
    ),
    (
        "RO_0002323",
        ("RO_0002323", "MEREOTOPOLOGICALLY_RELATED_TO"),
        "mereotopologically related to",
        "A mereological relationship or a topological relationship",
        (),
        False,
    ),
    (
        "RO_0002327",
        ("RO_0002327", "ENABLES"),
        "enables",
        "c enables p iff c is capable of p and c acts to execute p.",
        (),
        False,
    ),
    (
        "RO_0002328",
        ("RO_0002328", "FUNCTIONALLY_RELATED_TO"),
        "functionally related to",
        "A grouping relationship for any relationship directly involving a function, or that holds because of a function of one of the related entities.",
        (),
        False,
    ),
    (
        "RO_0002329",
        ("RO_0002329", "PART_OF_STRUCTURE_THAT_IS_CAPABLE_OF"),
        "part of structure that is capable of",
        "this relation holds between c and p when c is part of some c', and c' is capable of p.",
        (),
        False,
    ),
    (
        "RO_0002331",
        ("RO_0002331", "INVOLVED_IN"),
        "involved in",
        "c involved_in p if and only if c enables some process p', and p' is part of p",
        (),
        False,
    ),
    (
        "RO_0002333",
        ("RO_0002333", "ENABLED_BY"),
        "enabled by",
        "inverse of enables",
        (),
        False,
    ),
    (
        "RO_0002334",
        ("RO_0002334", "REGULATED_BY"),
        "regulated by",
        "inverse of regulates",
        (),
        False,
    ),
    (
        "RO_0002335",
        ("RO_0002335", "NEGATIVELY_REGULATED_BY"),
        "negatively regulated by",
        "inverse of negatively regulates",
        (),
        False,
    ),
    (
        "RO_0002336",
        ("RO_0002336", "POSITIVELY_REGULATED_BY"),
        "positively regulated by",
        "inverse of positively regulates",
        (),
        False,
    ),
    (
        "RO_0002351",
        ("RO_0002351", "HAS_MEMBER"),
        "has member",
        "has member is a mereological relation between a collection and an item.",
        (),
        False,
    ),
    (
        "RO_0002352",
        ("RO_0002352", "INPUT_OF"),
        "input of",
        "inverse of has input",
        (),
        False,
    ),
    (
        "RO_0002404",
        ("RO_0002404", "CAUSALLY_DOWNSTREAM_OF"),
        "causally downstream of",
        "inverse of upstream of",
        (),
        False,
    ),
    (
        "RO_0002405",
        ("RO_0002405", "IMMEDIATELY_CAUSALLY_DOWNSTREAM_OF"),
        "immediately causally downstream of",
        None,
        (),
        False,
    ),
    (
        "RO_0002407",
        ("RO_0002407", "INDIRECTLY_POSITIVELY_REGULATES"),
        "indirectly positively regulates",
        "p indirectly positively regulates q iff p is indirectly causally upstream of q and p positively regulates q.",
        (),
        False,
    ),
    (
        "RO_0002409",
        ("RO_0002409", "INDIRECTLY_NEGATIVELY_REGULATES"),
        "indirectly negatively regulates",
        "p indirectly negatively regulates q iff p is indirectly causally upstream of q and p negatively regulates q.",
        (),
        False,
    ),
    (
        "RO_0002410",
        ("RO_0002410", "CAUSALLY_RELATED_TO"),
        "causally related to",
        None,
        (),
        False,
    ),
    (
        "RO_0002411",
        ("RO_0002411", "CAUSALLY_UPSTREAM_OF"),
        "causally upstream of",
        "p is causally upstream of q iff p is causally related to q, the end of p precedes the end of q, and p is not an occurrent part of q.",
        (),
        False,
    ),
    (
        "RO_0002412",
        ("RO_0002412", "IMMEDIATELY_CAUSALLY_UPSTREAM_OF"),
        "immediately causally upstream of",
        "p is immediately causally upstream of q iff p is causally upstream of q, and the end of p is coincident with the beginning of q.",
        (),
        False,
    ),
    (
        "RO_0002418",
        ("RO_0002418", "CAUSALLY_UPSTREAM_OF_OR_WITHIN"),
        "causally upstream of or within",
        "p is 'causally upstream or within' q iff p is causally related to q, and the end of p precedes, or is coincident with, the end of q.",
        (),
        False,
    ),
    (
        "RO_0002427",
        ("RO_0002427", "CAUSALLY_DOWNSTREAM_OF_OR_WITHIN"),
        "causally downstream of or within",
        "inverse of causally upstream of or within",
        (),
        False,
    ),
    (
        "RO_0002428",
        ("RO_0002428", "INVOLVED_IN_REGULATION_OF"),
        "involved in regulation of",
        "c involved in regulation of p if c is involved in some p' and p' regulates some p",
        (),
        False,
    ),
    (
        "RO_0002429",
        ("RO_0002429", "INVOLVED_IN_POSITIVE_REGULATION_OF"),
        "involved in positive regulation of",
        "c involved in regulation of p if c is involved in some p' and p' positively regulates some p",
        (),
        False,
    ),
    (
        "RO_0002430",
        ("RO_0002430", "INVOLVED_IN_NEGATIVE_REGULATION_OF"),
        "involved in negative regulation of",
        "c involved in regulation of p if c is involved in some p' and p' negatively regulates some p",
        (),
        False,
    ),
    (
        "RO_0002431",
        ("RO_0002431", "INVOLVED_IN_OR_INVOLVED_IN_REGULATION_OF"),
        "involved in or involved in regulation of",
        "c involved in or regulates p if and only if either (i) c is involved in p or (ii) c is involved in regulation of p",
        (),
        False,
    ),
    (
        "RO_0002434",
        ("RO_0002434", "INTERACTS_WITH"),
        "interacts with",
        "A relationship that holds between two entities in which the processes executed by the two entities are causally connected.",
        (),
        False,
    ),
    (
        "RO_0002436",
        ("RO_0002436", "MOLECULARLY_INTERACTS_WITH"),
        "molecularly interacts with",
        "An interaction relationship in which the two partners are molecular entities that directly physically interact with each other for example via a stable binding interaction or a brief interaction during which one modifies the other.",
        (),
        False,
    ),
    ("RO_0002447", ("RO_0002447", "PHOSPHORYLATES"), "phosphorylates", None, (), False),
    (
        "RO_0002448",
        ("RO_0002448", "DIRECTLY_REGULATES_ACTIVITY_OF"),
        "directly regulates activity of",
        "The entity A, immediately upstream of the entity B, has an activity that regulates an activity performed by B. For example, A and B may be gene products and binding of B by A regulates the kinase activity of B. A and B can be physically interacting but not necessarily. Immediately upstream means there are no intermediate entity between A and B.",
        (),
        False,
    ),
    (
        "RO_0002449",
        ("RO_0002449", "DIRECTLY_NEGATIVELY_REGULATES_ACTIVITY_OF"),
        "directly negatively regulates activity of",
        "The entity A, immediately upstream of the entity B, has an activity that negatively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A negatively regulates the kinase activity of B.",
        (),
        False,
    ),
    (
        "RO_0002450",
        ("RO_0002450", "DIRECTLY_POSITIVELY_REGULATES_ACTIVITY_OF"),
        "directly positively regulates activity of",
        "The entity A, immediately upstream of the entity B, has an activity that positively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A positively regulates the kinase activity of B.",
        (),
        False,
    ),
    (
        "RO_0002464",
        ("RO_0002464", "HELPER_PROPERTY__NOT_FOR_USE_IN_CURATION_"),
        "helper property (not for use in curation)",
        None,
        (),
        False,
    ),
    (
        "RO_0002481",
        ("RO_0002481", "IS_KINASE_ACTIVITY"),
        "is kinase activity",
        None,
        (),
        False,
    ),
    (
        "RO_0002500",
        ("RO_0002500", "CAUSAL_AGENT_IN_PROCESS"),
        "causal agent in process",
        "A relationship between a material entity and a process where the material entity has some causal role that influences the process",
        (),
        False,
    ),
    (
        "RO_0002501",
        ("RO_0002501", "CAUSAL_RELATION_BETWEEN_PROCESSES"),
        "causal relation between processes",
        "p is causally related to q if and only if p or any part of p and q or any part of q are linked by a chain of events where each event pair is one where the execution of p influences the execution of q. p may be upstream, downstream, part of, or a container of q.",
        (),
        False,
    ),
    ("RO_0002502", ("RO_0002502", "DEPENDS_ON"), "depends on", None, (), False),
    (
        "RO_0002506",
        ("RO_0002506", "CAUSAL_RELATION_BETWEEN_ENTITIES"),
        "causal relation between entities",
        None,
        (),
        False,
    ),
    (
        "RO_0002559",
        ("RO_0002559", "CAUSALLY_INFLUENCED_BY"),
        "causally influenced by",
        None,
        (),
        False,
    ),
    (
        "RO_0002563",
        ("RO_0002563", "INTERACTION_RELATION_HELPER_PROPERTY"),
        "interaction relation helper property",
        None,
        (),
        False,
    ),
    (
        "RO_0002564",
        ("RO_0002564", "MOLECULAR_INTERACTION_RELATION_HELPER_PROPERTY"),
        "molecular interaction relation helper property",
        None,
        (),
        False,
    ),
    (
        "RO_0002566",
        ("RO_0002566", "CAUSALLY_INFLUENCES"),
        "causally influences",
        "The entity or characteristic A is causally upstream of the entity or characteristic B, A having an effect on B. An entity corresponds to any biological type of entity as long as a mass is measurable. A characteristic corresponds to a particular specificity of an entity (e.g., phenotype, shape, size).",
        (),
        False,
    ),
    (
        "RO_0002578",
        ("RO_0002578", "DIRECTLY_REGULATES"),
        "directly regulates",
        "p directly regulates q iff p is immediately causally upstream of q and p regulates q.",
        (),
        False,
    ),
    (
        "RO_0002584",
        ("RO_0002584", "HAS_PART_STRUCTURE_THAT_IS_CAPABLE_OF"),
        "has part structure that is capable of",
        "s 'has part structure that is capable of' p if and only if there exists some part x such that s 'has part' x and x 'capable of' p",
        (),
        False,
    ),
    (
        "RO_0002595",
        ("RO_0002595", "CAUSAL_RELATION_BETWEEN_MATERIAL_ENTITY_AND_A_PROCESS"),
        "causal relation between material entity and a process",
        "A relationship that holds between a material entity and a process in which causality is involved, with either the material entity or some part of the material entity exerting some influence over the process, or the process influencing some aspect of the material entity.",
        (),
        False,
    ),
    (
        "RO_0002596",
        ("RO_0002596", "CAPABLE_OF_REGULATING"),
        "capable of regulating",
        "Holds between c and p if and only if c is capable of some activity a, and a regulates p.",
        (),
        False,
    ),
    (
        "RO_0002597",
        ("RO_0002597", "CAPABLE_OF_NEGATIVELY_REGULATING"),
        "capable of negatively regulating",
        "Holds between c and p if and only if c is capable of some activity a, and a negatively regulates p.",
        (),
        False,
    ),
    (
        "RO_0002598",
        ("RO_0002598", "CAPABLE_OF_POSITIVELY_REGULATING"),
        "capable of positively regulating",
        "Holds between c and p if and only if c is capable of some activity a, and a positively regulates p.",
        (),
        False,
    ),
    (
        "RO_0002608",
        ("RO_0002608", "PROCESS_HAS_CAUSAL_AGENT"),
        "process has causal agent",
        "Inverse of 'causal agent in process'",
        (),
        False,
    ),
    (
        "RO_0002629",
        ("RO_0002629", "DIRECTLY_POSITIVELY_REGULATES"),
        "directly positively regulates",
        "p directly positively regulates q iff p is immediately causally upstream of q, and p positively regulates q.",
        (),
        False,
    ),
    (
        "RO_0002630",
        ("RO_0002630", "DIRECTLY_NEGATIVELY_REGULATES"),
        "directly negatively regulates",
        "p directly negatively regulates q iff p is immediately causally upstream of q, and p negatively regulates q.",
        (),
        False,
    ),
    (
        "RO_0004031",
        ("RO_0004031", "ENABLES_SUBFUNCTION"),
        "enables subfunction",
        "Holds between an entity and an process P where the entity enables some larger compound process, and that larger process has-part P.",
        (),
        False,
    ),
    (
        "RO_0004032",
        ("RO_0004032", "ACTS_UPSTREAM_OF_OR_WITHIN__POSITIVE_EFFECT"),
        "acts upstream of or within, positive effect",
        None,
        (),
        False,
    ),
    (
        "RO_0004033",
        ("RO_0004033", "ACTS_UPSTREAM_OF_OR_WITHIN__NEGATIVE_EFFECT"),
        "acts upstream of or within, negative effect",
        None,
        (),
        False,
    ),
    (
        "RO_0004034",
        ("RO_0004034", "ACTS_UPSTREAM_OF__POSITIVE_EFFECT"),
        "acts upstream of, positive effect",
        "c 'acts upstream of, positive effect' p if c is enables f, and f is causally upstream of p, and the direction of f is positive",
        (),
        False,
    ),
    (
        "RO_0004035",
        ("RO_0004035", "ACTS_UPSTREAM_OF__NEGATIVE_EFFECT"),
        "acts upstream of, negative effect",
        "c 'acts upstream of, negative effect' p if c is enables f, and f is causally upstream of p, and the direction of f is negative",
        (),
        False,
    ),
    (
        "RO_0004046",
        ("RO_0004046", "CAUSALLY_UPSTREAM_OF_OR_WITHIN__NEGATIVE_EFFECT"),
        "causally upstream of or within, negative effect",
        None,
        (),
        False,
    ),
    (
        "RO_0004047",
        ("RO_0004047", "CAUSALLY_UPSTREAM_OF_OR_WITHIN__POSITIVE_EFFECT"),
        "causally upstream of or within, positive effect",
        None,
        (),
        False,
    ),
    (
        "RO_0011002",
        ("RO_0011002", "REGULATES_ACTIVITY_OF"),
        "regulates activity of",
        "The entity A has an activity that regulates an activity of the entity B. For example, A and B are gene products where the catalytic activity of A regulates the kinase activity of B.",
        (),
        False,
    ),
    (
        "RO_0012011",
        ("RO_0012011", "INDIRECTLY_CAUSALLY_UPSTREAM_OF"),
        "indirectly causally upstream of",
        "p is indirectly causally upstream of q iff p is causally upstream of q and there exists some process r such that p is causally upstream of r and r is causally upstream of q.",
        (),
        False,
    ),
    (
        "RO_0012012",
        ("RO_0012012", "INDIRECTLY_REGULATES"),
        "indirectly regulates",
        "p indirectly regulates q iff p is indirectly causally upstream of q and p regulates q.",
        (),
        False,
    ),
    (
        "RO_0017001",
        ("RO_0017001", "DEVICE_UTILIZES_MATERIAL"),
        "device utilizes material",
        "X device utilizes material Y means X and Y are material entities, and X is capable of some process P that has input Y.",
        (),
        False,
    ),
    (
        "RO_0019000",
        ("RO_0019000", "REGULATES_CHARACTERISTIC"),
        "regulates characteristic",
        "A relationship that holds between a process and a characteristic in which process (P) regulates characteristic (C) iff: P results in the existence of C OR affects the intensity or magnitude of C.",
        (),
        False,
    ),
    (
        "RO_0019001",
        ("RO_0019001", "POSITIVELY_REGULATES_CHARACTERISTIC"),
        "positively regulates characteristic",
        "A relationship that holds between a process and a characteristic in which process (P) positively regulates characteristic (C) iff: P results in an increase in the intensity or magnitude of C.",
        (),
        False,
    ),
    (
        "RO_0019002",
        ("RO_0019002", "NEGATIVELY_REGULATES_CHARACTERISTIC"),
        "negatively regulates characteristic",
        "A relationship that holds between a process and a characteristic in which process (P) negatively regulates characteristic (C) iff: P results in a decrease in the intensity or magnitude of C.",
        (),
        False,
    ),
    (
        "UBERON_0000465",
        ("UBERON_0000465", "MATERIAL_ANATOMICAL_ENTITY"),
        "material anatomical entity",
        "Anatomical entity that has mass.",
        (),
        False,
    ),
    (
        "UBERON_0000466",
        ("UBERON_0000466", "IMMATERIAL_ANATOMICAL_ENTITY"),
        "immaterial anatomical entity",
        "Anatomical entity that has no mass.",
        (),
        False,
    ),
    (
        "UBERON_0000477",
        ("UBERON_0000477", "ANATOMICAL_CLUSTER"),
        "anatomical cluster",
        "Anatomical group whose component anatomical structures lie in close proximity to each other.",
        (),
        False,
    ),
    (
        "UBERON_0001062",
        ("UBERON_0001062", "ANATOMICAL_ENTITY"),
        "anatomical entity",
        "Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.",
        (),
        False,
    ),
    ("UO_0000001", ("UO_0000001", "LENGTH_UNIT"), "length unit", None, (), False),
    ("UO_0000002", ("UO_0000002", "MASS_UNIT"), "mass unit", None, (), False),
    ("UO_0000003", ("UO_0000003", "TIME_UNIT"), "time unit", None, (), False),
    (
        "UO_0000005",
        ("UO_0000005", "TEMPERATURE_UNIT"),
        "temperature unit",
        None,
        (),
        False,
    ),
    ("UO_0000006", ("UO_0000006", "SUBSTANCE_UNIT"), "substance unit", None, (), False),
    (
        "UO_0000051",
        ("UO_0000051", "CONCENTRATION_UNIT"),
        "concentration unit",
        None,
        (),
        False,
    ),
    ("UO_0000095", ("UO_0000095", "VOLUME_UNIT"), "volume unit", None, (), False),
    ("UO_0000105", ("UO_0000105", "FREQUENCY_UNIT"), "frequency unit", None, (), False),
    (
        "UO_0000270",
        ("UO_0000270", "VOLUMETRIC_FLOW_RATE_UNIT"),
        "volumetric flow rate unit",
        None,
        (),
        False,
    ),
    ("UO_0000280", ("UO_0000280", "RATE_UNIT"), "rate unit", None, (), False),
]

PBPKO._register(_terms)

__all__ = [
    "PBPKO",
    "PBPKOType",
]
