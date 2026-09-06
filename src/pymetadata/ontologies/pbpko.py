"""PBPKO ontology.

Generated from the ontology release by
`pymetadata.ontologies._ontology_builder`, do not edit.
"""

from pymetadata.ontologies.term import OntologyEnum, TermData

pattern = r"^PBPKO_\d{5}$"


class PBPKO(OntologyEnum):
    """PBPKO ontology."""

    # entity
    BFO_0000001 = "BFO_0000001"
    ENTITY = "BFO_0000001"

    # continuant
    BFO_0000002 = "BFO_0000002"
    CONTINUANT = "BFO_0000002"

    # occurrent
    BFO_0000003 = "BFO_0000003"
    OCCURRENT = "BFO_0000003"

    # independent continuant
    BFO_0000004 = "BFO_0000004"
    INDEPENDENT_CONTINUANT = "BFO_0000004"

    # process
    BFO_0000015 = "BFO_0000015"
    PROCESS = "BFO_0000015"

    # disposition
    BFO_0000016 = "BFO_0000016"
    DISPOSITION = "BFO_0000016"

    # realizable entity
    BFO_0000017 = "BFO_0000017"
    REALIZABLE_ENTITY = "BFO_0000017"

    # quality
    BFO_0000019 = "BFO_0000019"
    QUALITY = "BFO_0000019"

    # specifically dependent continuant
    BFO_0000020 = "BFO_0000020"
    SPECIFICALLY_DEPENDENT_CONTINUANT = "BFO_0000020"

    # role
    BFO_0000023 = "BFO_0000023"
    ROLE = "BFO_0000023"

    # site
    BFO_0000029 = "BFO_0000029"
    SITE = "BFO_0000029"

    # generically dependent continuant
    BFO_0000031 = "BFO_0000031"
    GENERICALLY_DEPENDENT_CONTINUANT = "BFO_0000031"

    # function
    BFO_0000034 = "BFO_0000034"
    FUNCTION = "BFO_0000034"

    # material entity
    BFO_0000040 = "BFO_0000040"
    MATERIAL_ENTITY = "BFO_0000040"

    # part of
    BFO_0000050 = "BFO_0000050"
    PART_OF = "BFO_0000050"

    # has part
    BFO_0000051 = "BFO_0000051"
    HAS_PART = "BFO_0000051"

    # realizes
    BFO_0000055 = "BFO_0000055"
    REALIZES = "BFO_0000055"

    # preceded by
    BFO_0000062 = "BFO_0000062"
    PRECEDED_BY = "BFO_0000062"

    # precedes
    BFO_0000063 = "BFO_0000063"
    PRECEDES = "BFO_0000063"

    # immaterial entity
    BFO_0000141 = "BFO_0000141"
    IMMATERIAL_ENTITY = "BFO_0000141"

    # peptide
    CHEBI_16670 = "CHEBI_16670"
    PEPTIDE = "CHEBI_16670"

    # proton
    CHEBI_24636 = "CHEBI_24636"
    PROTON = "CHEBI_24636"

    # atomic nucleus
    CHEBI_33252 = "CHEBI_33252"
    ATOMIC_NUCLEUS = "CHEBI_33252"

    # macromolecule
    CHEBI_33839 = "CHEBI_33839"
    MACROMOLECULE = "CHEBI_33839"

    # subatomic particle
    CHEBI_36342 = "CHEBI_36342"
    SUBATOMIC_PARTICLE = "CHEBI_36342"

    # cell
    CL_0000000 = "CL_0000000"
    CELL = "CL_0000000"

    # atom
    COB_0000011 = "COB_0000011"
    ATOM = "COB_0000011"

    # molecule
    COB_0000013 = "COB_0000013"
    MOLECULE = "COB_0000013"

    # gross anatomical part
    COB_0000021 = "COB_0000021"
    GROSS_ANATOMICAL_PART = "COB_0000021"

    # organism
    COB_0000022 = "COB_0000022"
    ORGANISM = "COB_0000022"

    # completely executed planned process
    COB_0000035 = "COB_0000035"
    COMPLETELY_EXECUTED_PLANNED_PROCESS = "COB_0000035"

    # complex of molecules
    COB_0000080 = "COB_0000080"
    COMPLEX_OF_MOLECULES = "COB_0000080"

    # planned process
    COB_0000082 = "COB_0000082"
    PLANNED_PROCESS = "COB_0000082"

    # characteristic
    COB_0000502 = "COB_0000502"
    CHARACTERISTIC = "COB_0000502"

    # system process
    GO_0003008 = "GO_0003008"
    SYSTEM_PROCESS = "GO_0003008"

    # gene product or complex activity
    GO_0003674 = "GO_0003674"
    GENE_PRODUCT_OR_COMPLEX_ACTIVITY = "GO_0003674"

    # cellular_component
    GO_0005575 = "GO_0005575"
    CELLULAR_COMPONENT = "GO_0005575"

    # excretion
    GO_0007588 = "GO_0007588"
    EXCRETION = "GO_0007588"

    # biological process
    GO_0008150 = "GO_0008150"
    BIOLOGICAL_PROCESS = "GO_0008150"

    # metabolic process
    GO_0008152 = "GO_0008152"
    METABOLIC_PROCESS = "GO_0008152"

    # cellular process
    GO_0009987 = "GO_0009987"
    CELLULAR_PROCESS = "GO_0009987"

    # kinase activity
    GO_0016301 = "GO_0016301"
    KINASE_ACTIVITY = "GO_0016301"

    # multicellular organismal process
    GO_0032501 = "GO_0032501"
    MULTICELLULAR_ORGANISMAL_PROCESS = "GO_0032501"

    # protein-containing complex
    GO_0032991 = "GO_0032991"
    PROTEIN_CONTAINING_COMPLEX = "GO_0032991"

    # virion component
    GO_0044423 = "GO_0044423"
    VIRION_COMPONENT = "GO_0044423"

    # cellular anatomical entity
    GO_0110165 = "GO_0110165"
    CELLULAR_ANATOMICAL_ENTITY = "GO_0110165"

    # measurement unit label
    IAO_0000003 = "IAO_0000003"
    MEASUREMENT_UNIT_LABEL = "IAO_0000003"

    # objective specification
    IAO_0000005 = "IAO_0000005"
    OBJECTIVE_SPECIFICATION = "IAO_0000005"

    # datum label
    IAO_0000009 = "IAO_0000009"
    DATUM_LABEL = "IAO_0000009"

    # software
    IAO_0000010 = "IAO_0000010"
    SOFTWARE = "IAO_0000010"

    # data entity
    IAO_0000027 = "IAO_0000027"
    DATA_ENTITY = "IAO_0000027"

    # information content entity
    IAO_0000030 = "IAO_0000030"
    INFORMATION_CONTENT_ENTITY = "IAO_0000030"

    # directive information entity
    IAO_0000033 = "IAO_0000033"
    DIRECTIVE_INFORMATION_ENTITY = "IAO_0000033"

    # dot plot
    IAO_0000037 = "IAO_0000037"
    DOT_PLOT = "IAO_0000037"

    # graph
    IAO_0000038 = "IAO_0000038"
    GRAPH = "IAO_0000038"

    # algorithm
    IAO_0000064 = "IAO_0000064"
    ALGORITHM = "IAO_0000064"

    # curation status specification
    IAO_0000078 = "IAO_0000078"
    CURATION_STATUS_SPECIFICATION = "IAO_0000078"

    # data format specification
    IAO_0000098 = "IAO_0000098"
    DATA_FORMAT_SPECIFICATION = "IAO_0000098"

    # homogenous data collection
    IAO_0000100 = "IAO_0000100"
    HOMOGENOUS_DATA_COLLECTION = "IAO_0000100"

    # image
    IAO_0000101 = "IAO_0000101"
    IMAGE = "IAO_0000101"

    # data about an ontology part
    IAO_0000102 = "IAO_0000102"
    DATA_ABOUT_AN_ONTOLOGY_PART = "IAO_0000102"

    # plan specification
    IAO_0000104 = "IAO_0000104"
    PLAN_SPECIFICATION = "IAO_0000104"

    # is about
    IAO_0000136 = "IAO_0000136"
    IS_ABOUT = "IAO_0000136"

    # histogram
    IAO_0000179 = "IAO_0000179"
    HISTOGRAM = "IAO_0000179"

    # heatmap
    IAO_0000180 = "IAO_0000180"
    HEATMAP = "IAO_0000180"

    # dendrogram
    IAO_0000183 = "IAO_0000183"
    DENDROGRAM = "IAO_0000183"

    # scatter plot
    IAO_0000184 = "IAO_0000184"
    SCATTER_PLOT = "IAO_0000184"

    # obsolescence reason specification
    IAO_0000225 = "IAO_0000225"
    OBSOLESCENCE_REASON_SPECIFICATION = "IAO_0000225"

    # figure
    IAO_0000308 = "IAO_0000308"
    FIGURE = "IAO_0000308"

    # document
    IAO_0000310 = "IAO_0000310"
    DOCUMENT = "IAO_0000310"

    # denotator type
    IAO_0000409 = "IAO_0000409"
    DENOTATOR_TYPE = "IAO_0000409"

    # data collection
    IAO_0001000 = "IAO_0001000"
    DATA_COLLECTION = "IAO_0001000"

    # Euteleostomi
    NCBITaxon_117571 = "NCBITaxon_117571"
    EUTELEOSTOMI = "NCBITaxon_117571"

    # Eukaryota
    NCBITaxon_2759 = "NCBITaxon_2759"
    EUKARYOTA = "NCBITaxon_2759"

    # Euarchontoglires
    NCBITaxon_314146 = "NCBITaxon_314146"
    EUARCHONTOGLIRES = "NCBITaxon_314146"

    # Tetrapoda
    NCBITaxon_32523 = "NCBITaxon_32523"
    TETRAPODA = "NCBITaxon_32523"

    # Amniota
    NCBITaxon_32524 = "NCBITaxon_32524"
    AMNIOTA = "NCBITaxon_32524"

    # Opisthokonta
    NCBITaxon_33154 = "NCBITaxon_33154"
    OPISTHOKONTA = "NCBITaxon_33154"

    # Metazoa
    NCBITaxon_33208 = "NCBITaxon_33208"
    METAZOA = "NCBITaxon_33208"

    # Bilateria
    NCBITaxon_33213 = "NCBITaxon_33213"
    BILATERIA = "NCBITaxon_33213"

    # Mammalia
    NCBITaxon_40674 = "NCBITaxon_40674"
    MAMMALIA = "NCBITaxon_40674"

    # Vertebrata <vertebrates>
    NCBITaxon_7742 = "NCBITaxon_7742"
    VERTEBRATA__VERTEBRATES_ = "NCBITaxon_7742"

    # Homo sapiens
    NCBITaxon_9606 = "NCBITaxon_9606"
    HOMO_SAPIENS = "NCBITaxon_9606"

    # regulator role
    OBI_0000014 = "OBI_0000014"
    REGULATOR_ROLE = "OBI_0000014"

    # regulatory role
    OBI_0000017 = "OBI_0000017"
    REGULATORY_ROLE = "OBI_0000017"

    # material supplier role
    OBI_0000018 = "OBI_0000018"
    MATERIAL_SUPPLIER_ROLE = "OBI_0000018"

    # classified data set
    OBI_0000023 = "OBI_0000023"
    CLASSIFIED_DATA_SET = "OBI_0000023"

    # specimen role
    OBI_0000112 = "OBI_0000112"
    SPECIMEN_ROLE = "OBI_0000112"

    # organization
    OBI_0000245 = "OBI_0000245"
    ORGANIZATION = "OBI_0000245"

    # plan
    OBI_0000260 = "OBI_0000260"
    PLAN = "OBI_0000260"

    # has specified input
    OBI_0000293 = "OBI_0000293"
    HAS_SPECIFIED_INPUT = "OBI_0000293"

    # is specified input of
    OBI_0000295 = "OBI_0000295"
    IS_SPECIFIED_INPUT_OF = "OBI_0000295"

    # has specified output
    OBI_0000299 = "OBI_0000299"
    HAS_SPECIFIED_OUTPUT = "OBI_0000299"

    # is specified output of
    OBI_0000312 = "OBI_0000312"
    IS_SPECIFIED_OUTPUT_OF = "OBI_0000312"

    # achieves_planned_objective
    OBI_0000417 = "OBI_0000417"
    ACHIEVES_PLANNED_OBJECTIVE = "OBI_0000417"

    # regulatory agency
    OBI_0000450 = "OBI_0000450"
    REGULATORY_AGENCY = "OBI_0000450"

    # manufacturer role
    OBI_0000571 = "OBI_0000571"
    MANUFACTURER_ROLE = "OBI_0000571"

    # clustered data set
    OBI_0000648 = "OBI_0000648"
    CLUSTERED_DATA_SET = "OBI_0000648"

    # data representational model
    OBI_0000658 = "OBI_0000658"
    DATA_REPRESENTATIONAL_MODEL = "OBI_0000658"

    # specimen collection process
    OBI_0000659 = "OBI_0000659"
    SPECIMEN_COLLECTION_PROCESS = "OBI_0000659"

    # class prediction data transformation
    OBI_0000663 = "OBI_0000663"
    CLASS_PREDICTION_DATA_TRANSFORMATION = "OBI_0000663"

    # specimen collection objective
    OBI_0000684 = "OBI_0000684"
    SPECIMEN_COLLECTION_OBJECTIVE = "OBI_0000684"

    # support vector machine
    OBI_0000700 = "OBI_0000700"
    SUPPORT_VECTOR_MACHINE = "OBI_0000700"

    # decision tree induction objective
    OBI_0000704 = "OBI_0000704"
    DECISION_TREE_INDUCTION_OBJECTIVE = "OBI_0000704"

    # decision tree building data transformation
    OBI_0000707 = "OBI_0000707"
    DECISION_TREE_BUILDING_DATA_TRANSFORMATION = "OBI_0000707"

    # GenePattern software
    OBI_0000713 = "OBI_0000713"
    GENEPATTERN_SOFTWARE = "OBI_0000713"

    # peak matching
    OBI_0000726 = "OBI_0000726"
    PEAK_MATCHING = "OBI_0000726"

    # k-nearest neighbors
    OBI_0000727 = "OBI_0000727"
    K_NEAREST_NEIGHBORS = "OBI_0000727"

    # CART
    OBI_0000749 = "OBI_0000749"
    CART = "OBI_0000749"

    # statistical model validation
    OBI_0000792 = "OBI_0000792"
    STATISTICAL_MODEL_VALIDATION = "OBI_0000792"

    # objective_achieved_by
    OBI_0000833 = "OBI_0000833"
    OBJECTIVE_ACHIEVED_BY = "OBI_0000833"

    # manufacturer
    OBI_0000835 = "OBI_0000835"
    MANUFACTURER = "OBI_0000835"

    # service provider role
    OBI_0000947 = "OBI_0000947"
    SERVICE_PROVIDER_ROLE = "OBI_0000947"

    # categorical label
    OBI_0000963 = "OBI_0000963"
    CATEGORICAL_LABEL = "OBI_0000963"

    # questionnaire
    OBI_0001000 = "OBI_0001000"
    QUESTIONNAIRE = "OBI_0001000"

    # cell specimen
    OBI_0001468 = "OBI_0001468"
    CELL_SPECIMEN = "OBI_0001468"

    # specimen from organism
    OBI_0001479 = "OBI_0001479"
    SPECIMEN_FROM_ORGANISM = "OBI_0001479"

    # categorical value specification
    OBI_0001930 = "OBI_0001930"
    CATEGORICAL_VALUE_SPECIFICATION = "OBI_0001930"

    # value specification
    OBI_0001933 = "OBI_0001933"
    VALUE_SPECIFICATION = "OBI_0001933"

    # collection of specimens
    OBI_0002076 = "OBI_0002076"
    COLLECTION_OF_SPECIMENS = "OBI_0002076"

    # histologic grade according to AJCC 7th edition
    OBI_0002205 = "OBI_0002205"
    HISTOLOGIC_GRADE_ACCORDING_TO_AJCC_7TH_EDITION = "OBI_0002205"

    # histologic grade according to the Fuhrman Nuclear Grading System
    OBI_0002210 = "OBI_0002210"
    HISTOLOGIC_GRADE_ACCORDING_TO_THE_FUHRMAN_NUCLEAR_GRADING_SYSTEM = "OBI_0002210"

    # histologic grade for ovarian tumor
    OBI_0002215 = "OBI_0002215"
    HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR = "OBI_0002215"

    # histologic grade for ovarian tumor according to a two-tier grading system
    OBI_0002216 = "OBI_0002216"
    HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR_ACCORDING_TO_A_TWO_TIER_GRADING_SYSTEM = (
        "OBI_0002216"
    )

    # histologic grade for ovarian tumor according to the World Health Organization
    OBI_0002219 = "OBI_0002219"
    HISTOLOGIC_GRADE_FOR_OVARIAN_TUMOR_ACCORDING_TO_THE_WORLD_HEALTH_ORGANIZATION = (
        "OBI_0002219"
    )

    # pathologic primary tumor stage for colon and rectum according to AJCC 7th edition
    OBI_0002224 = "OBI_0002224"
    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_COLON_AND_RECTUM_ACCORDING_TO_AJCC_7TH_EDITION = "OBI_0002224"

    # pathologic primary tumor stage for lung according to AJCC 7th edition
    OBI_0002232 = "OBI_0002232"
    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002232"
    )

    # pathologic primary tumor stage for kidney according to AJCC 7th edition
    OBI_0002243 = "OBI_0002243"
    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002243"
    )

    # pathologic primary tumor stage for ovary according to AJCC 7th edition
    OBI_0002256 = "OBI_0002256"
    PATHOLOGIC_PRIMARY_TUMOR_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002256"
    )

    # pathologic lymph node stage for colon and rectum according to AJCC 7th edition
    OBI_0002270 = "OBI_0002270"
    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_COLON_AND_RECTUM_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002270"
    )

    # pathologic lymph node stage for lung according to AJCC 7th edition
    OBI_0002279 = "OBI_0002279"
    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION = "OBI_0002279"

    # pathologic lymph node stage for kidney according to AJCC 7th edition
    OBI_0002284 = "OBI_0002284"
    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION = "OBI_0002284"

    # pathologic lymph node stage for ovary according to AJCC 7th edition
    OBI_0002287 = "OBI_0002287"
    PATHOLOGIC_LYMPH_NODE_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION = "OBI_0002287"

    # pathologic distant metastases stage for colon according to AJCC 7th edition
    OBI_0002290 = "OBI_0002290"
    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_COLON_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002290"
    )

    # pathologic distant metastases stage for lung according to AJCC 7th edition
    OBI_0002298 = "OBI_0002298"
    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_LUNG_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002298"
    )

    # pathologic distant metastases stage for kidney according to AJCC 7th edition
    OBI_0002306 = "OBI_0002306"
    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_KIDNEY_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002306"
    )

    # pathologic distant metastases stage for ovary according to AJCC 7th edition
    OBI_0002310 = "OBI_0002310"
    PATHOLOGIC_DISTANT_METASTASES_STAGE_FOR_OVARY_ACCORDING_TO_AJCC_7TH_EDITION = (
        "OBI_0002310"
    )

    # clinical tumor stage group according to AJCC 7th edition
    OBI_0002314 = "OBI_0002314"
    CLINICAL_TUMOR_STAGE_GROUP_ACCORDING_TO_AJCC_7TH_EDITION = "OBI_0002314"

    # International Federation of Gynecology and Obstetrics cervical cancer stage value specification
    OBI_0002326 = "OBI_0002326"
    INTERNATIONAL_FEDERATION_OF_GYNECOLOGY_AND_OBSTETRICS_CERVICAL_CANCER_STAGE_VALUE_SPECIFICATION = "OBI_0002326"

    # International Federation of Gynecology and Obstetrics ovarian cancer stage value specification
    OBI_0002341 = "OBI_0002341"
    INTERNATIONAL_FEDERATION_OF_GYNECOLOGY_AND_OBSTETRICS_OVARIAN_CANCER_STAGE_VALUE_SPECIFICATION = "OBI_0002341"

    # performance status value specification
    OBI_0002356 = "OBI_0002356"
    PERFORMANCE_STATUS_VALUE_SPECIFICATION = "OBI_0002356"

    # Eastern Cooperative Oncology Group score value specification
    OBI_0002357 = "OBI_0002357"
    EASTERN_COOPERATIVE_ONCOLOGY_GROUP_SCORE_VALUE_SPECIFICATION = "OBI_0002357"

    # Karnofsky score vaue specification
    OBI_0002363 = "OBI_0002363"
    KARNOFSKY_SCORE_VAUE_SPECIFICATION = "OBI_0002363"

    # material supplier
    OBI_0002989 = "OBI_0002989"
    MATERIAL_SUPPLIER = "OBI_0002989"

    # specimen
    OBI_0100051 = "OBI_0100051"
    SPECIMEN = "OBI_0100051"

    # data transformation
    OBI_0200000 = "OBI_0200000"
    DATA_TRANSFORMATION = "OBI_0200000"

    # leave one out cross validation method
    OBI_0200033 = "OBI_0200033"
    LEAVE_ONE_OUT_CROSS_VALIDATION_METHOD = "OBI_0200033"

    # k-means clustering
    OBI_0200041 = "OBI_0200041"
    K_MEANS_CLUSTERING = "OBI_0200041"

    # hierarchical clustering
    OBI_0200042 = "OBI_0200042"
    HIERARCHICAL_CLUSTERING = "OBI_0200042"

    # dimensionality reduction
    OBI_0200050 = "OBI_0200050"
    DIMENSIONALITY_REDUCTION = "OBI_0200050"

    # principal components analysis dimensionality reduction
    OBI_0200051 = "OBI_0200051"
    PRINCIPAL_COMPONENTS_ANALYSIS_DIMENSIONALITY_REDUCTION = "OBI_0200051"

    # data visualization
    OBI_0200111 = "OBI_0200111"
    DATA_VISUALIZATION = "OBI_0200111"

    # data transformation objective
    OBI_0200166 = "OBI_0200166"
    DATA_TRANSFORMATION_OBJECTIVE = "OBI_0200166"

    # partitioning data transformation
    OBI_0200171 = "OBI_0200171"
    PARTITIONING_DATA_TRANSFORMATION = "OBI_0200171"

    # partitioning objective
    OBI_0200172 = "OBI_0200172"
    PARTITIONING_OBJECTIVE = "OBI_0200172"

    # class discovery data transformation
    OBI_0200175 = "OBI_0200175"
    CLASS_DISCOVERY_DATA_TRANSFORMATION = "OBI_0200175"

    # class discovery objective
    OBI_0200178 = "OBI_0200178"
    CLASS_DISCOVERY_OBJECTIVE = "OBI_0200178"

    # class prediction objective
    OBI_0200179 = "OBI_0200179"
    CLASS_PREDICTION_OBJECTIVE = "OBI_0200179"

    # cross validation objective
    OBI_0200188 = "OBI_0200188"
    CROSS_VALIDATION_OBJECTIVE = "OBI_0200188"

    # clustered data visualization
    OBI_0200190 = "OBI_0200190"
    CLUSTERED_DATA_VISUALIZATION = "OBI_0200190"

    # quality
    PATO_0000001 = "PATO_0000001"

    # parameter
    PBPKO_00002 = "PBPKO_00002"
    PARAMETER = "PBPKO_00002"

    # physiologically based pharmacokinetic model
    PBPKO_00003 = "PBPKO_00003"
    PHYSIOLOGICALLY_BASED_PHARMACOKINETIC_MODEL = "PBPKO_00003"

    # whole body pbpk
    PBPKO_00004 = "PBPKO_00004"
    WHOLE_BODY_PBPK = "PBPKO_00004"

    # perfusion limited model
    PBPKO_00005 = "PBPKO_00005"
    PERFUSION_LIMITED_MODEL = "PBPKO_00005"

    # physiological parameter
    PBPKO_00006 = "PBPKO_00006"
    PHYSIOLOGICAL_PARAMETER = "PBPKO_00006"

    # body mass index
    PBPKO_00007 = "PBPKO_00007"
    BODY_MASS_INDEX = "PBPKO_00007"

    # bodyweight
    PBPKO_00008 = "PBPKO_00008"
    BODYWEIGHT = "PBPKO_00008"

    # height
    PBPKO_00009 = "PBPKO_00009"
    HEIGHT = "PBPKO_00009"

    # surface area
    PBPKO_00010 = "PBPKO_00010"
    SURFACE_AREA = "PBPKO_00010"

    # assigned race
    PBPKO_00011 = "PBPKO_00011"
    ASSIGNED_RACE = "PBPKO_00011"

    # blood flow rate to compartment
    PBPKO_00012 = "PBPKO_00012"
    BLOOD_FLOW_RATE_TO_COMPARTMENT = "PBPKO_00012"

    # cardiac output rate
    PBPKO_00013 = "PBPKO_00013"
    CARDIAC_OUTPUT_RATE = "PBPKO_00013"

    # blood flow rate to stomach
    PBPKO_00014 = "PBPKO_00014"
    BLOOD_FLOW_RATE_TO_STOMACH = "PBPKO_00014"

    # fraction of blood flow to stomach
    PBPKO_00015 = "PBPKO_00015"
    FRACTION_OF_BLOOD_FLOW_TO_STOMACH = "PBPKO_00015"

    # blood flow rate to intestine
    PBPKO_00016 = "PBPKO_00016"
    BLOOD_FLOW_RATE_TO_INTESTINE = "PBPKO_00016"

    # fraction of blood flow to intestine
    PBPKO_00017 = "PBPKO_00017"
    FRACTION_OF_BLOOD_FLOW_TO_INTESTINE = "PBPKO_00017"

    # blood flow rate to small intestine
    PBPKO_00018 = "PBPKO_00018"
    BLOOD_FLOW_RATE_TO_SMALL_INTESTINE = "PBPKO_00018"

    # fraction of blood flow to small intestine
    PBPKO_00019 = "PBPKO_00019"
    FRACTION_OF_BLOOD_FLOW_TO_SMALL_INTESTINE = "PBPKO_00019"

    # blood flow rate to large intestine
    PBPKO_00020 = "PBPKO_00020"
    BLOOD_FLOW_RATE_TO_LARGE_INTESTINE = "PBPKO_00020"

    # fraction of blood flow to large intestine
    PBPKO_00021 = "PBPKO_00021"
    FRACTION_OF_BLOOD_FLOW_TO_LARGE_INTESTINE = "PBPKO_00021"

    # blood flow rate to pancreas
    PBPKO_00022 = "PBPKO_00022"
    BLOOD_FLOW_RATE_TO_PANCREAS = "PBPKO_00022"

    # fraction of blood flow to pancreas
    PBPKO_00023 = "PBPKO_00023"
    FRACTION_OF_BLOOD_FLOW_TO_PANCREAS = "PBPKO_00023"

    # blood flow rate to liver
    PBPKO_00024 = "PBPKO_00024"
    BLOOD_FLOW_RATE_TO_LIVER = "PBPKO_00024"

    # fraction of blood flow to liver
    PBPKO_00025 = "PBPKO_00025"
    FRACTION_OF_BLOOD_FLOW_TO_LIVER = "PBPKO_00025"

    # blood flow rate to kidney
    PBPKO_00026 = "PBPKO_00026"
    BLOOD_FLOW_RATE_TO_KIDNEY = "PBPKO_00026"

    # fraction of blood flow to kidney
    PBPKO_00027 = "PBPKO_00027"
    FRACTION_OF_BLOOD_FLOW_TO_KIDNEY = "PBPKO_00027"

    # blood flow rate to muscle
    PBPKO_00028 = "PBPKO_00028"
    BLOOD_FLOW_RATE_TO_MUSCLE = "PBPKO_00028"

    # fraction of blood flow to muscle
    PBPKO_00029 = "PBPKO_00029"
    FRACTION_OF_BLOOD_FLOW_TO_MUSCLE = "PBPKO_00029"

    # blood flow rate to heart
    PBPKO_00030 = "PBPKO_00030"
    BLOOD_FLOW_RATE_TO_HEART = "PBPKO_00030"

    # fraction of blood flow to heart
    PBPKO_00031 = "PBPKO_00031"
    FRACTION_OF_BLOOD_FLOW_TO_HEART = "PBPKO_00031"

    # blood flow rate to fat
    PBPKO_00032 = "PBPKO_00032"
    BLOOD_FLOW_RATE_TO_FAT = "PBPKO_00032"

    # fraction of blood flow to fat
    PBPKO_00033 = "PBPKO_00033"
    FRACTION_OF_BLOOD_FLOW_TO_FAT = "PBPKO_00033"

    # blood flow rate to gonad
    PBPKO_00034 = "PBPKO_00034"
    BLOOD_FLOW_RATE_TO_GONAD = "PBPKO_00034"

    # fraction of blood flow to gonad
    PBPKO_00035 = "PBPKO_00035"
    FRACTION_OF_BLOOD_FLOW_TO_GONAD = "PBPKO_00035"

    # blood flow rate to skin
    PBPKO_00036 = "PBPKO_00036"
    BLOOD_FLOW_RATE_TO_SKIN = "PBPKO_00036"

    # fraction of blood flow to skin
    PBPKO_00037 = "PBPKO_00037"
    FRACTION_OF_BLOOD_FLOW_TO_SKIN = "PBPKO_00037"

    # blood flow rate to bone
    PBPKO_00038 = "PBPKO_00038"
    BLOOD_FLOW_RATE_TO_BONE = "PBPKO_00038"

    # fraction of blood flow to bone
    PBPKO_00039 = "PBPKO_00039"
    FRACTION_OF_BLOOD_FLOW_TO_BONE = "PBPKO_00039"

    # blood flow rate to brain
    PBPKO_00040 = "PBPKO_00040"
    BLOOD_FLOW_RATE_TO_BRAIN = "PBPKO_00040"

    # fraction of blood flow to brain
    PBPKO_00041 = "PBPKO_00041"
    FRACTION_OF_BLOOD_FLOW_TO_BRAIN = "PBPKO_00041"

    # blood flow rate to spleen
    PBPKO_00042 = "PBPKO_00042"
    BLOOD_FLOW_RATE_TO_SPLEEN = "PBPKO_00042"

    # fraction of blood flow to spleen
    PBPKO_00043 = "PBPKO_00043"
    FRACTION_OF_BLOOD_FLOW_TO_SPLEEN = "PBPKO_00043"

    # blood flow rate to lung
    PBPKO_00044 = "PBPKO_00044"
    BLOOD_FLOW_RATE_TO_LUNG = "PBPKO_00044"

    # fraction of blood flow to lung
    PBPKO_00045 = "PBPKO_00045"
    FRACTION_OF_BLOOD_FLOW_TO_LUNG = "PBPKO_00045"

    # blood flow rate to poorly perfused
    PBPKO_00046 = "PBPKO_00046"
    BLOOD_FLOW_RATE_TO_POORLY_PERFUSED = "PBPKO_00046"

    # fraction of blood flow to poorly perfused
    PBPKO_00047 = "PBPKO_00047"
    FRACTION_OF_BLOOD_FLOW_TO_POORLY_PERFUSED = "PBPKO_00047"

    # blood flow rate to richly perfused
    PBPKO_00048 = "PBPKO_00048"
    BLOOD_FLOW_RATE_TO_RICHLY_PERFUSED = "PBPKO_00048"

    # fraction of blood flow to richly perfused
    PBPKO_00049 = "PBPKO_00049"
    FRACTION_OF_BLOOD_FLOW_TO_RICHLY_PERFUSED = "PBPKO_00049"

    # blood flow rate to restbody
    PBPKO_00050 = "PBPKO_00050"
    BLOOD_FLOW_RATE_TO_RESTBODY = "PBPKO_00050"

    # fraction of blood flow to restbody
    PBPKO_00051 = "PBPKO_00051"
    FRACTION_OF_BLOOD_FLOW_TO_RESTBODY = "PBPKO_00051"

    # blood flow rate to gall bladder
    PBPKO_00052 = "PBPKO_00052"
    BLOOD_FLOW_RATE_TO_GALL_BLADDER = "PBPKO_00052"

    # fraction of blood flow to gall bladder
    PBPKO_00053 = "PBPKO_00053"
    FRACTION_OF_BLOOD_FLOW_TO_GALL_BLADDER = "PBPKO_00053"

    # blood flow rate to portal vein
    PBPKO_00054 = "PBPKO_00054"
    BLOOD_FLOW_RATE_TO_PORTAL_VEIN = "PBPKO_00054"

    # fraction of blood flow to portal vein
    PBPKO_00055 = "PBPKO_00055"
    FRACTION_OF_BLOOD_FLOW_TO_PORTAL_VEIN = "PBPKO_00055"

    # blood flow rate to lymph
    PBPKO_00056 = "PBPKO_00056"
    BLOOD_FLOW_RATE_TO_LYMPH = "PBPKO_00056"

    # fraction of blood flow to lymph
    PBPKO_00057 = "PBPKO_00057"
    FRACTION_OF_BLOOD_FLOW_TO_LYMPH = "PBPKO_00057"

    # amount of metabolized
    PBPKO_00058 = "PBPKO_00058"
    AMOUNT_OF_METABOLIZED = "PBPKO_00058"

    # fraction of blood flow to stratum corneum
    PBPKO_00060 = "PBPKO_00060"
    FRACTION_OF_BLOOD_FLOW_TO_STRATUM_CORNEUM = "PBPKO_00060"

    # fraction of exposed skin
    PBPKO_00061 = "PBPKO_00061"
    FRACTION_OF_EXPOSED_SKIN = "PBPKO_00061"

    # fraction of unexposed skin
    PBPKO_00062 = "PBPKO_00062"
    FRACTION_OF_UNEXPOSED_SKIN = "PBPKO_00062"

    # arterial blood flow rate
    PBPKO_00063 = "PBPKO_00063"
    ARTERIAL_BLOOD_FLOW_RATE = "PBPKO_00063"

    # venous blood flow rate
    PBPKO_00064 = "PBPKO_00064"
    VENOUS_BLOOD_FLOW_RATE = "PBPKO_00064"

    # glomerular filtration rate
    PBPKO_00065 = "PBPKO_00065"
    GLOMERULAR_FILTRATION_RATE = "PBPKO_00065"

    # volume of compartment
    PBPKO_00066 = "PBPKO_00066"
    VOLUME_OF_COMPARTMENT = "PBPKO_00066"

    # volume of stomach
    PBPKO_00067 = "PBPKO_00067"
    VOLUME_OF_STOMACH = "PBPKO_00067"

    # fraction of stomach
    PBPKO_00068 = "PBPKO_00068"
    FRACTION_OF_STOMACH = "PBPKO_00068"

    # volume of intestine
    PBPKO_00069 = "PBPKO_00069"
    VOLUME_OF_INTESTINE = "PBPKO_00069"

    # fraction of intestine
    PBPKO_00070 = "PBPKO_00070"
    FRACTION_OF_INTESTINE = "PBPKO_00070"

    # volume of small intestine
    PBPKO_00071 = "PBPKO_00071"
    VOLUME_OF_SMALL_INTESTINE = "PBPKO_00071"

    # fraction of small intestine
    PBPKO_00072 = "PBPKO_00072"
    FRACTION_OF_SMALL_INTESTINE = "PBPKO_00072"

    # volume of large intestine
    PBPKO_00073 = "PBPKO_00073"
    VOLUME_OF_LARGE_INTESTINE = "PBPKO_00073"

    # fraction of large intestine
    PBPKO_00074 = "PBPKO_00074"
    FRACTION_OF_LARGE_INTESTINE = "PBPKO_00074"

    # volume of pancreas
    PBPKO_00075 = "PBPKO_00075"
    VOLUME_OF_PANCREAS = "PBPKO_00075"

    # fraction of pancreas
    PBPKO_00076 = "PBPKO_00076"
    FRACTION_OF_PANCREAS = "PBPKO_00076"

    # volume of liver
    PBPKO_00077 = "PBPKO_00077"
    VOLUME_OF_LIVER = "PBPKO_00077"

    # fraction of liver
    PBPKO_00078 = "PBPKO_00078"
    FRACTION_OF_LIVER = "PBPKO_00078"

    # volume of kidney
    PBPKO_00079 = "PBPKO_00079"
    VOLUME_OF_KIDNEY = "PBPKO_00079"

    # fraction of kidney
    PBPKO_00080 = "PBPKO_00080"
    FRACTION_OF_KIDNEY = "PBPKO_00080"

    # volume of muscle
    PBPKO_00081 = "PBPKO_00081"
    VOLUME_OF_MUSCLE = "PBPKO_00081"

    # fraction of muscle
    PBPKO_00082 = "PBPKO_00082"
    FRACTION_OF_MUSCLE = "PBPKO_00082"

    # volume of heart
    PBPKO_00083 = "PBPKO_00083"
    VOLUME_OF_HEART = "PBPKO_00083"

    # fraction of heart
    PBPKO_00084 = "PBPKO_00084"
    FRACTION_OF_HEART = "PBPKO_00084"

    # volume of fat
    PBPKO_00085 = "PBPKO_00085"
    VOLUME_OF_FAT = "PBPKO_00085"

    # fraction of fat
    PBPKO_00086 = "PBPKO_00086"
    FRACTION_OF_FAT = "PBPKO_00086"

    # volume of gonad
    PBPKO_00087 = "PBPKO_00087"
    VOLUME_OF_GONAD = "PBPKO_00087"

    # fraction of gonad
    PBPKO_00088 = "PBPKO_00088"
    FRACTION_OF_GONAD = "PBPKO_00088"

    # volume of skin
    PBPKO_00089 = "PBPKO_00089"
    VOLUME_OF_SKIN = "PBPKO_00089"

    # fraction of skin
    PBPKO_00090 = "PBPKO_00090"
    FRACTION_OF_SKIN = "PBPKO_00090"

    # volume of bone
    PBPKO_00091 = "PBPKO_00091"
    VOLUME_OF_BONE = "PBPKO_00091"

    # fraction of bone
    PBPKO_00092 = "PBPKO_00092"
    FRACTION_OF_BONE = "PBPKO_00092"

    # volume of brain
    PBPKO_00093 = "PBPKO_00093"
    VOLUME_OF_BRAIN = "PBPKO_00093"

    # fraction of brain
    PBPKO_00094 = "PBPKO_00094"
    FRACTION_OF_BRAIN = "PBPKO_00094"

    # volume of spleen
    PBPKO_00095 = "PBPKO_00095"
    VOLUME_OF_SPLEEN = "PBPKO_00095"

    # fraction of spleen
    PBPKO_00096 = "PBPKO_00096"
    FRACTION_OF_SPLEEN = "PBPKO_00096"

    # volume of lung
    PBPKO_00097 = "PBPKO_00097"
    VOLUME_OF_LUNG = "PBPKO_00097"

    # fraction of lung
    PBPKO_00098 = "PBPKO_00098"
    FRACTION_OF_LUNG = "PBPKO_00098"

    # volume of poorly perfused
    PBPKO_00099 = "PBPKO_00099"
    VOLUME_OF_POORLY_PERFUSED = "PBPKO_00099"

    # fraction of poorly perfused
    PBPKO_00100 = "PBPKO_00100"
    FRACTION_OF_POORLY_PERFUSED = "PBPKO_00100"

    # volume of richly perfused
    PBPKO_00101 = "PBPKO_00101"
    VOLUME_OF_RICHLY_PERFUSED = "PBPKO_00101"

    # fraction of richly perfused
    PBPKO_00102 = "PBPKO_00102"
    FRACTION_OF_RICHLY_PERFUSED = "PBPKO_00102"

    # volume of plasma
    PBPKO_00103 = "PBPKO_00103"
    VOLUME_OF_PLASMA = "PBPKO_00103"

    # fraction of plasma
    PBPKO_00104 = "PBPKO_00104"
    FRACTION_OF_PLASMA = "PBPKO_00104"

    # volume of rest body
    PBPKO_00105 = "PBPKO_00105"
    VOLUME_OF_REST_BODY = "PBPKO_00105"

    # fraction of rest body
    PBPKO_00106 = "PBPKO_00106"
    FRACTION_OF_REST_BODY = "PBPKO_00106"

    # volume of stratum corneum with respect to blood
    PBPKO_00107 = "PBPKO_00107"
    VOLUME_OF_STRATUM_CORNEUM_WITH_RESPECT_TO_BLOOD = "PBPKO_00107"

    # volume of blood
    PBPKO_00108 = "PBPKO_00108"
    VOLUME_OF_BLOOD = "PBPKO_00108"

    # volume of exposed skin
    PBPKO_00109 = "PBPKO_00109"
    VOLUME_OF_EXPOSED_SKIN = "PBPKO_00109"

    # fraction of surface area exposed
    PBPKO_00110 = "PBPKO_00110"
    FRACTION_OF_SURFACE_AREA_EXPOSED = "PBPKO_00110"

    # volume of unexposed skin
    PBPKO_00111 = "PBPKO_00111"
    VOLUME_OF_UNEXPOSED_SKIN = "PBPKO_00111"

    # volume of stratum corneum exposed
    PBPKO_00112 = "PBPKO_00112"
    VOLUME_OF_STRATUM_CORNEUM_EXPOSED = "PBPKO_00112"

    # volume of unexposed stratum corneum
    PBPKO_00113 = "PBPKO_00113"
    VOLUME_OF_UNEXPOSED_STRATUM_CORNEUM = "PBPKO_00113"

    # fraction alveolar volume
    PBPKO_00114 = "PBPKO_00114"
    FRACTION_ALVEOLAR_VOLUME = "PBPKO_00114"

    # volume of gall bladder
    PBPKO_00115 = "PBPKO_00115"
    VOLUME_OF_GALL_BLADDER = "PBPKO_00115"

    # fraction of gall bladder
    PBPKO_00116 = "PBPKO_00116"
    FRACTION_OF_GALL_BLADDER = "PBPKO_00116"

    # volume of portal vein
    PBPKO_00117 = "PBPKO_00117"
    VOLUME_OF_PORTAL_VEIN = "PBPKO_00117"

    # fraction of portal vein
    PBPKO_00118 = "PBPKO_00118"
    FRACTION_OF_PORTAL_VEIN = "PBPKO_00118"

    # volume of lymph
    PBPKO_00119 = "PBPKO_00119"
    VOLUME_OF_LYMPH = "PBPKO_00119"

    # fraction of lymph
    PBPKO_00120 = "PBPKO_00120"
    FRACTION_OF_LYMPH = "PBPKO_00120"

    # arterial volume
    PBPKO_00121 = "PBPKO_00121"
    ARTERIAL_VOLUME = "PBPKO_00121"

    # venous volume
    PBPKO_00122 = "PBPKO_00122"
    VENOUS_VOLUME = "PBPKO_00122"

    # physicochemical parameter
    PBPKO_00126 = "PBPKO_00126"
    PHYSICOCHEMICAL_PARAMETER = "PBPKO_00126"

    # molecular weight
    PBPKO_00127 = "PBPKO_00127"
    MOLECULAR_WEIGHT = "PBPKO_00127"

    # lipophillicity
    PBPKO_00128 = "PBPKO_00128"
    LIPOPHILLICITY = "PBPKO_00128"

    # distribution coefficient
    PBPKO_00129 = "PBPKO_00129"
    DISTRIBUTION_COEFFICIENT = "PBPKO_00129"

    # dissolution in two phase system
    PBPKO_00130 = "PBPKO_00130"
    DISSOLUTION_IN_TWO_PHASE_SYSTEM = "PBPKO_00130"

    # logarithmic solubility
    PBPKO_00131 = "PBPKO_00131"
    LOGARITHMIC_SOLUBILITY = "PBPKO_00131"

    # water solubility
    PBPKO_00132 = "PBPKO_00132"
    WATER_SOLUBILITY = "PBPKO_00132"

    # acid dissociation constant
    PBPKO_00133 = "PBPKO_00133"
    ACID_DISSOCIATION_CONSTANT = "PBPKO_00133"

    # basic dissociation constant
    PBPKO_00134 = "PBPKO_00134"
    BASIC_DISSOCIATION_CONSTANT = "PBPKO_00134"

    # physiological charge
    PBPKO_00135 = "PBPKO_00135"
    PHYSIOLOGICAL_CHARGE = "PBPKO_00135"

    # hydrogen acceptor count
    PBPKO_00136 = "PBPKO_00136"
    HYDROGEN_ACCEPTOR_COUNT = "PBPKO_00136"

    # hydrogen donor count
    PBPKO_00137 = "PBPKO_00137"
    HYDROGEN_DONOR_COUNT = "PBPKO_00137"

    # rotatable bond count
    PBPKO_00138 = "PBPKO_00138"
    ROTATABLE_BOND_COUNT = "PBPKO_00138"

    # biochemical parameter
    PBPKO_00139 = "PBPKO_00139"
    BIOCHEMICAL_PARAMETER = "PBPKO_00139"

    # absorption
    PBPKO_00140 = "PBPKO_00140"
    ABSORPTION = "PBPKO_00140"

    # absorption rate constant gut
    PBPKO_00141 = "PBPKO_00141"
    ABSORPTION_RATE_CONSTANT_GUT = "PBPKO_00141"

    # absorption rate constant intestine
    PBPKO_00142 = "PBPKO_00142"
    ABSORPTION_RATE_CONSTANT_INTESTINE = "PBPKO_00142"

    # gastric emptying rate
    PBPKO_00143 = "PBPKO_00143"
    GASTRIC_EMPTYING_RATE = "PBPKO_00143"

    # enterohepatic recirculation
    PBPKO_00144 = "PBPKO_00144"
    ENTEROHEPATIC_RECIRCULATION = "PBPKO_00144"

    # specific intestinal permeability
    PBPKO_00145 = "PBPKO_00145"
    SPECIFIC_INTESTINAL_PERMEABILITY = "PBPKO_00145"

    # distribution process
    PBPKO_00146 = "PBPKO_00146"
    DISTRIBUTION_PROCESS = "PBPKO_00146"

    # volume of distribution
    PBPKO_00147 = "PBPKO_00147"
    VOLUME_OF_DISTRIBUTION = "PBPKO_00147"

    # protein binding mediated distributiion process
    PBPKO_00148 = "PBPKO_00148"
    PROTEIN_BINDING_MEDIATED_DISTRIBUTIION_PROCESS = "PBPKO_00148"

    # unbound fraction
    PBPKO_00149 = "PBPKO_00149"
    UNBOUND_FRACTION = "PBPKO_00149"

    # fraction unbound gut
    PBPKO_00150 = "PBPKO_00150"
    FRACTION_UNBOUND_GUT = "PBPKO_00150"

    # fraction unbound stomach
    PBPKO_00151 = "PBPKO_00151"
    FRACTION_UNBOUND_STOMACH = "PBPKO_00151"

    # fraction unbound intestine
    PBPKO_00152 = "PBPKO_00152"
    FRACTION_UNBOUND_INTESTINE = "PBPKO_00152"

    # fraction unbound pancreas
    PBPKO_00153 = "PBPKO_00153"
    FRACTION_UNBOUND_PANCREAS = "PBPKO_00153"

    # fraction unbound liver
    PBPKO_00154 = "PBPKO_00154"
    FRACTION_UNBOUND_LIVER = "PBPKO_00154"

    # fraction unbound kidney
    PBPKO_00155 = "PBPKO_00155"
    FRACTION_UNBOUND_KIDNEY = "PBPKO_00155"

    # fraction unbound muscle
    PBPKO_00156 = "PBPKO_00156"
    FRACTION_UNBOUND_MUSCLE = "PBPKO_00156"

    # fraction unbound heart
    PBPKO_00157 = "PBPKO_00157"
    FRACTION_UNBOUND_HEART = "PBPKO_00157"

    # fraction unbound fat
    PBPKO_00158 = "PBPKO_00158"
    FRACTION_UNBOUND_FAT = "PBPKO_00158"

    # fraction unbound gonad
    PBPKO_00159 = "PBPKO_00159"
    FRACTION_UNBOUND_GONAD = "PBPKO_00159"

    # fraction unbound skin
    PBPKO_00160 = "PBPKO_00160"
    FRACTION_UNBOUND_SKIN = "PBPKO_00160"

    # fraction unbound bone
    PBPKO_00161 = "PBPKO_00161"
    FRACTION_UNBOUND_BONE = "PBPKO_00161"

    # fraction unbound spleen
    PBPKO_00162 = "PBPKO_00162"
    FRACTION_UNBOUND_SPLEEN = "PBPKO_00162"

    # fraction unbound lung
    PBPKO_00163 = "PBPKO_00163"
    FRACTION_UNBOUND_LUNG = "PBPKO_00163"

    # fraction unbound enterocytes
    PBPKO_00164 = "PBPKO_00164"
    FRACTION_UNBOUND_ENTEROCYTES = "PBPKO_00164"

    # partition coefficient
    PBPKO_00165 = "PBPKO_00165"
    PARTITION_COEFFICIENT = "PBPKO_00165"

    # gut plasma partition coefficient
    PBPKO_00166 = "PBPKO_00166"
    GUT_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00166"

    # stomach plasma partition coefficient
    PBPKO_00167 = "PBPKO_00167"
    STOMACH_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00167"

    # intestine plasma partition coefficient
    PBPKO_00168 = "PBPKO_00168"
    INTESTINE_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00168"

    # pancreas plasma partition coefficient
    PBPKO_00169 = "PBPKO_00169"
    PANCREAS_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00169"

    # liver plasma partition coefficient
    PBPKO_00170 = "PBPKO_00170"
    LIVER_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00170"

    # kidney plasma partition coefficient
    PBPKO_00171 = "PBPKO_00171"
    KIDNEY_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00171"

    # muscle plasma partition coefficient
    PBPKO_00172 = "PBPKO_00172"
    MUSCLE_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00172"

    # heart plasma partition coefficient
    PBPKO_00173 = "PBPKO_00173"
    HEART_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00173"

    # fat plasma partition coefficient
    PBPKO_00174 = "PBPKO_00174"
    FAT_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00174"

    # gonad plasma partition coefficient
    PBPKO_00175 = "PBPKO_00175"
    GONAD_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00175"

    # skin plasma partition coefficient
    PBPKO_00176 = "PBPKO_00176"
    SKIN_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00176"

    # bone plasma partition coefficient
    PBPKO_00177 = "PBPKO_00177"
    BONE_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00177"

    # spleen plasma partition coefficient
    PBPKO_00178 = "PBPKO_00178"
    SPLEEN_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00178"

    # lung plasma partition coefficient
    PBPKO_00179 = "PBPKO_00179"
    LUNG_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00179"

    # rich perfused plasma partition coefficient
    PBPKO_00180 = "PBPKO_00180"
    RICH_PERFUSED_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00180"

    # poor perfused plasma partition coefficient
    PBPKO_00181 = "PBPKO_00181"
    POOR_PERFUSED_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00181"

    # skin stratum corneum partition coefficient
    PBPKO_00182 = "PBPKO_00182"
    SKIN_STRATUM_CORNEUM_PARTITION_COEFFICIENT = "PBPKO_00182"

    # air plasma partition coefficient
    PBPKO_00183 = "PBPKO_00183"
    AIR_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00183"

    # skin diffusion coefficient
    PBPKO_00184 = "PBPKO_00184"
    SKIN_DIFFUSION_COEFFICIENT = "PBPKO_00184"

    # human serum albumin
    PBPKO_00185 = "PBPKO_00185"
    HUMAN_SERUM_ALBUMIN = "PBPKO_00185"

    # blood:plasma ratio
    PBPKO_00187 = "PBPKO_00187"
    BLOOD_PLASMA_RATIO = "PBPKO_00187"

    # catalytic rate constant
    PBPKO_00189 = "PBPKO_00189"
    CATALYTIC_RATE_CONSTANT = "PBPKO_00189"

    # phase I metabolism
    PBPKO_00191 = "PBPKO_00191"
    PHASE_I_METABOLISM = "PBPKO_00191"

    # phase II
    PBPKO_00200 = "PBPKO_00200"
    PHASE_II = "PBPKO_00200"

    # phase III
    PBPKO_00209 = "PBPKO_00209"
    PHASE_III = "PBPKO_00209"

    # first pass metabolism
    PBPKO_00210 = "PBPKO_00210"
    FIRST_PASS_METABOLISM = "PBPKO_00210"

    # maximum rate in intestine
    PBPKO_00211 = "PBPKO_00211"
    MAXIMUM_RATE_IN_INTESTINE = "PBPKO_00211"

    # Michaelis constant  intestine
    PBPKO_00212 = "PBPKO_00212"
    MICHAELIS_CONSTANT__INTESTINE = "PBPKO_00212"

    # maximum rate in liver
    PBPKO_00213 = "PBPKO_00213"
    MAXIMUM_RATE_IN_LIVER = "PBPKO_00213"

    # Michaelis constant  liver
    PBPKO_00214 = "PBPKO_00214"
    MICHAELIS_CONSTANT__LIVER = "PBPKO_00214"

    # gut metabolism
    PBPKO_00215 = "PBPKO_00215"
    GUT_METABOLISM = "PBPKO_00215"

    # dissociation constant
    PBPKO_00216 = "PBPKO_00216"
    DISSOCIATION_CONSTANT = "PBPKO_00216"

    # transporter
    PBPKO_00217 = "PBPKO_00217"
    TRANSPORTER = "PBPKO_00217"

    # oatp
    PBPKO_00218 = "PBPKO_00218"
    OATP = "PBPKO_00218"

    # abcc3
    PBPKO_00219 = "PBPKO_00219"
    ABCC3 = "PBPKO_00219"

    # abcc2
    PBPKO_00220 = "PBPKO_00220"
    ABCC2 = "PBPKO_00220"

    # degradation rate constant
    PBPKO_00221 = "PBPKO_00221"
    DEGRADATION_RATE_CONSTANT = "PBPKO_00221"

    # inhibition constant
    PBPKO_00222 = "PBPKO_00222"
    INHIBITION_CONSTANT = "PBPKO_00222"

    # renal excretion
    PBPKO_00223 = "PBPKO_00223"
    RENAL_EXCRETION = "PBPKO_00223"

    # hepatic excretion
    PBPKO_00224 = "PBPKO_00224"
    HEPATIC_EXCRETION = "PBPKO_00224"

    # fecal excretion
    PBPKO_00225 = "PBPKO_00225"
    FECAL_EXCRETION = "PBPKO_00225"

    # exhalation
    PBPKO_00226 = "PBPKO_00226"
    EXHALATION = "PBPKO_00226"

    # sweat excretion
    PBPKO_00227 = "PBPKO_00227"
    SWEAT_EXCRETION = "PBPKO_00227"

    # hair excretion
    PBPKO_00228 = "PBPKO_00228"
    HAIR_EXCRETION = "PBPKO_00228"

    # clearance rate
    PBPKO_00229 = "PBPKO_00229"
    CLEARANCE_RATE = "PBPKO_00229"

    # fecal clearance rate
    PBPKO_00230 = "PBPKO_00230"
    FECAL_CLEARANCE_RATE = "PBPKO_00230"

    # sweat clearance rate
    PBPKO_00231 = "PBPKO_00231"
    SWEAT_CLEARANCE_RATE = "PBPKO_00231"

    # urinary clearance rate
    PBPKO_00232 = "PBPKO_00232"
    URINARY_CLEARANCE_RATE = "PBPKO_00232"

    # biliary clearance rate
    PBPKO_00233 = "PBPKO_00233"
    BILIARY_CLEARANCE_RATE = "PBPKO_00233"

    # hepatic clearance rate
    PBPKO_00234 = "PBPKO_00234"
    HEPATIC_CLEARANCE_RATE = "PBPKO_00234"

    # intrinsic clearance rate
    PBPKO_00235 = "PBPKO_00235"
    INTRINSIC_CLEARANCE_RATE = "PBPKO_00235"

    # fecal elimination rate constant
    PBPKO_00236 = "PBPKO_00236"
    FECAL_ELIMINATION_RATE_CONSTANT = "PBPKO_00236"

    # renal elimination rate constant
    PBPKO_00237 = "PBPKO_00237"
    RENAL_ELIMINATION_RATE_CONSTANT = "PBPKO_00237"

    # biliary elimination
    PBPKO_00238 = "PBPKO_00238"
    BILIARY_ELIMINATION = "PBPKO_00238"

    # route of exposure
    PBPKO_00239 = "PBPKO_00239"
    ROUTE_OF_EXPOSURE = "PBPKO_00239"

    # oral exposure
    PBPKO_00240 = "PBPKO_00240"
    ORAL_EXPOSURE = "PBPKO_00240"

    # dermal exposure
    PBPKO_00241 = "PBPKO_00241"
    DERMAL_EXPOSURE = "PBPKO_00241"

    # inhalation exposure
    PBPKO_00242 = "PBPKO_00242"
    INHALATION_EXPOSURE = "PBPKO_00242"

    # intravenous bolus exposure
    PBPKO_00243 = "PBPKO_00243"
    INTRAVENOUS_BOLUS_EXPOSURE = "PBPKO_00243"

    # intravenous infusion exposure
    PBPKO_00244 = "PBPKO_00244"
    INTRAVENOUS_INFUSION_EXPOSURE = "PBPKO_00244"

    # intramuscular exposure
    PBPKO_00245 = "PBPKO_00245"
    INTRAMUSCULAR_EXPOSURE = "PBPKO_00245"

    # intraarterial exposure
    PBPKO_00246 = "PBPKO_00246"
    INTRAARTERIAL_EXPOSURE = "PBPKO_00246"

    # intrathecal exposure
    PBPKO_00247 = "PBPKO_00247"
    INTRATHECAL_EXPOSURE = "PBPKO_00247"

    # subcutaneous exposure
    PBPKO_00248 = "PBPKO_00248"
    SUBCUTANEOUS_EXPOSURE = "PBPKO_00248"

    # nasal exposure
    PBPKO_00249 = "PBPKO_00249"
    NASAL_EXPOSURE = "PBPKO_00249"

    # transdermal exposure
    PBPKO_00250 = "PBPKO_00250"
    TRANSDERMAL_EXPOSURE = "PBPKO_00250"

    # ocular exposure
    PBPKO_00251 = "PBPKO_00251"
    OCULAR_EXPOSURE = "PBPKO_00251"

    # output parameter
    PBPKO_00252 = "PBPKO_00252"
    OUTPUT_PARAMETER = "PBPKO_00252"

    # peak concentration
    PBPKO_00253 = "PBPKO_00253"
    PEAK_CONCENTRATION = "PBPKO_00253"

    # maximum steady state concentration
    PBPKO_00254 = "PBPKO_00254"
    MAXIMUM_STEADY_STATE_CONCENTRATION = "PBPKO_00254"

    # maximum time
    PBPKO_00255 = "PBPKO_00255"
    MAXIMUM_TIME = "PBPKO_00255"

    # area under curve
    PBPKO_00256 = "PBPKO_00256"
    AREA_UNDER_CURVE = "PBPKO_00256"

    # area under curve 0 to t
    PBPKO_00257 = "PBPKO_00257"
    AREA_UNDER_CURVE_0_TO_T = "PBPKO_00257"

    # area under curve last
    PBPKO_00258 = "PBPKO_00258"
    AREA_UNDER_CURVE_LAST = "PBPKO_00258"

    # area under curve 0 to infinity
    PBPKO_00259 = "PBPKO_00259"
    AREA_UNDER_CURVE_0_TO_INFINITY = "PBPKO_00259"

    # area under moment curve
    PBPKO_00260 = "PBPKO_00260"
    AREA_UNDER_MOMENT_CURVE = "PBPKO_00260"

    # mean residence time
    PBPKO_00261 = "PBPKO_00261"
    MEAN_RESIDENCE_TIME = "PBPKO_00261"

    # half-life
    PBPKO_00262 = "PBPKO_00262"
    HALF_LIFE = "PBPKO_00262"

    # bioavailability
    PBPKO_00263 = "PBPKO_00263"
    BIOAVAILABILITY = "PBPKO_00263"

    # relative bioavailability
    PBPKO_00264 = "PBPKO_00264"
    RELATIVE_BIOAVAILABILITY = "PBPKO_00264"

    # mean absorption time
    PBPKO_00265 = "PBPKO_00265"
    MEAN_ABSORPTION_TIME = "PBPKO_00265"

    # mean dissolution time
    PBPKO_00266 = "PBPKO_00266"
    MEAN_DISSOLUTION_TIME = "PBPKO_00266"

    # bioequivalence
    PBPKO_00267 = "PBPKO_00267"
    BIOEQUIVALENCE = "PBPKO_00267"

    # absolute bioavailability
    PBPKO_00268 = "PBPKO_00268"
    ABSOLUTE_BIOAVAILABILITY = "PBPKO_00268"

    # elimination phase
    PBPKO_00269 = "PBPKO_00269"
    ELIMINATION_PHASE = "PBPKO_00269"

    # absorption phase
    PBPKO_00270 = "PBPKO_00270"
    ABSORPTION_PHASE = "PBPKO_00270"

    # amount in urine
    PBPKO_00272 = "PBPKO_00272"
    AMOUNT_IN_URINE = "PBPKO_00272"

    # amount in feces
    PBPKO_00273 = "PBPKO_00273"
    AMOUNT_IN_FECES = "PBPKO_00273"

    # cumulative amount in urine
    PBPKO_00274 = "PBPKO_00274"
    CUMULATIVE_AMOUNT_IN_URINE = "PBPKO_00274"

    # cumulative amount in feces
    PBPKO_00275 = "PBPKO_00275"
    CUMULATIVE_AMOUNT_IN_FECES = "PBPKO_00275"

    # steady state area under curve
    PBPKO_00277 = "PBPKO_00277"
    STEADY_STATE_AREA_UNDER_CURVE = "PBPKO_00277"

    # min organ concentration
    PBPKO_00279 = "PBPKO_00279"
    MIN_ORGAN_CONCENTRATION = "PBPKO_00279"

    # max organ concentration
    PBPKO_00280 = "PBPKO_00280"
    MAX_ORGAN_CONCENTRATION = "PBPKO_00280"

    # median organ concentration
    PBPKO_00281 = "PBPKO_00281"
    MEDIAN_ORGAN_CONCENTRATION = "PBPKO_00281"

    # percentile 2.5 cplasma
    PBPKO_00282 = "PBPKO_00282"
    PERCENTILE_2_5_CPLASMA = "PBPKO_00282"

    # percentile 97.5 cplasma
    PBPKO_00283 = "PBPKO_00283"
    PERCENTILE_97_5_CPLASMA = "PBPKO_00283"

    # tolerable daily intake
    PBPKO_00284 = "PBPKO_00284"
    TOLERABLE_DAILY_INTAKE = "PBPKO_00284"

    # reconstructed exposure
    PBPKO_00285 = "PBPKO_00285"
    RECONSTRUCTED_EXPOSURE = "PBPKO_00285"

    # estimated daily intake
    PBPKO_00286 = "PBPKO_00286"
    ESTIMATED_DAILY_INTAKE = "PBPKO_00286"

    # biomonitoring equivalent
    PBPKO_00287 = "PBPKO_00287"
    BIOMONITORING_EQUIVALENT = "PBPKO_00287"

    # reference dose
    PBPKO_00289 = "PBPKO_00289"
    REFERENCE_DOSE = "PBPKO_00289"

    # acceptable daily intake
    PBPKO_00290 = "PBPKO_00290"
    ACCEPTABLE_DAILY_INTAKE = "PBPKO_00290"

    # reference human data set
    PBPKO_00296 = "PBPKO_00296"
    REFERENCE_HUMAN_DATA_SET = "PBPKO_00296"

    # biological matrix concentration
    PBPKO_00297 = "PBPKO_00297"
    BIOLOGICAL_MATRIX_CONCENTRATION = "PBPKO_00297"

    # concentration in hair
    PBPKO_00298 = "PBPKO_00298"
    CONCENTRATION_IN_HAIR = "PBPKO_00298"

    # concentration in nail
    PBPKO_00299 = "PBPKO_00299"
    CONCENTRATION_IN_NAIL = "PBPKO_00299"

    # concentration in teeth
    PBPKO_00300 = "PBPKO_00300"
    CONCENTRATION_IN_TEETH = "PBPKO_00300"

    # concentration in blood
    PBPKO_00301 = "PBPKO_00301"
    CONCENTRATION_IN_BLOOD = "PBPKO_00301"

    # concentration in urine
    PBPKO_00302 = "PBPKO_00302"
    CONCENTRATION_IN_URINE = "PBPKO_00302"

    # permeability limited pbpk
    PBPKO_00303 = "PBPKO_00303"
    PERMEABILITY_LIMITED_PBPK = "PBPKO_00303"

    # maximum rate of basolateral transporter in vitro
    PBPKO_00304 = "PBPKO_00304"
    MAXIMUM_RATE_OF_BASOLATERAL_TRANSPORTER_IN_VITRO = "PBPKO_00304"

    # Michaelis constant baso
    PBPKO_00305 = "PBPKO_00305"
    MICHAELIS_CONSTANT_BASO = "PBPKO_00305"

    # maximum rate of apical transporter in vitro
    PBPKO_00306 = "PBPKO_00306"
    MAXIMUM_RATE_OF_APICAL_TRANSPORTER_IN_VITRO = "PBPKO_00306"

    # Michaelis constant apical
    PBPKO_00307 = "PBPKO_00307"
    MICHAELIS_CONSTANT_APICAL = "PBPKO_00307"

    # influx constant
    PBPKO_00310 = "PBPKO_00310"
    INFLUX_CONSTANT = "PBPKO_00310"

    # efflux rate constant
    PBPKO_00311 = "PBPKO_00311"
    EFFLUX_RATE_CONSTANT = "PBPKO_00311"

    # plasma space
    PBPKO_00312 = "PBPKO_00312"
    PLASMA_SPACE = "PBPKO_00312"

    # endosomal space compartment
    PBPKO_00313 = "PBPKO_00313"
    ENDOSOMAL_SPACE_COMPARTMENT = "PBPKO_00313"

    # interstitial space
    PBPKO_00314 = "PBPKO_00314"
    INTERSTITIAL_SPACE = "PBPKO_00314"

    # effective permeability
    PBPKO_00315 = "PBPKO_00315"
    EFFECTIVE_PERMEABILITY = "PBPKO_00315"

    # population pbpk
    PBPKO_00316 = "PBPKO_00316"
    POPULATION_PBPK = "PBPKO_00316"

    # top-down pbpk
    PBPKO_00317 = "PBPKO_00317"
    TOP_DOWN_PBPK = "PBPKO_00317"

    # bottom-up pbpk
    PBPKO_00318 = "PBPKO_00318"
    BOTTOM_UP_PBPK = "PBPKO_00318"

    # one-compartment pbpk
    PBPKO_00319 = "PBPKO_00319"
    ONE_COMPARTMENT_PBPK = "PBPKO_00319"

    # central compartment
    PBPKO_00320 = "PBPKO_00320"
    CENTRAL_COMPARTMENT = "PBPKO_00320"

    # peripheral compartment
    PBPKO_00321 = "PBPKO_00321"
    PERIPHERAL_COMPARTMENT = "PBPKO_00321"

    # elimination
    PBPKO_00322 = "PBPKO_00322"
    ELIMINATION = "PBPKO_00322"

    # linear elimination
    PBPKO_00323 = "PBPKO_00323"
    LINEAR_ELIMINATION = "PBPKO_00323"

    # non-linear elimination
    PBPKO_00324 = "PBPKO_00324"
    NON_LINEAR_ELIMINATION = "PBPKO_00324"

    # lifestage
    PBPKO_00332 = "PBPKO_00332"
    LIFESTAGE = "PBPKO_00332"

    # fetus lifestage
    PBPKO_00333 = "PBPKO_00333"
    FETUS_LIFESTAGE = "PBPKO_00333"

    # infant lifestage
    PBPKO_00334 = "PBPKO_00334"
    INFANT_LIFESTAGE = "PBPKO_00334"

    # toddler lifestage
    PBPKO_00335 = "PBPKO_00335"
    TODDLER_LIFESTAGE = "PBPKO_00335"

    # child lifestage
    PBPKO_00336 = "PBPKO_00336"
    CHILD_LIFESTAGE = "PBPKO_00336"

    # teenager lifestage
    PBPKO_00337 = "PBPKO_00337"
    TEENAGER_LIFESTAGE = "PBPKO_00337"

    # adolescent lifestage
    PBPKO_00338 = "PBPKO_00338"
    ADOLESCENT_LIFESTAGE = "PBPKO_00338"

    # adult lifestage
    PBPKO_00339 = "PBPKO_00339"
    ADULT_LIFESTAGE = "PBPKO_00339"

    # middle age lifestage
    PBPKO_00340 = "PBPKO_00340"
    MIDDLE_AGE_LIFESTAGE = "PBPKO_00340"

    # old age lifestage
    PBPKO_00341 = "PBPKO_00341"
    OLD_AGE_LIFESTAGE = "PBPKO_00341"

    # pediatric lifestage
    PBPKO_00342 = "PBPKO_00342"
    PEDIATRIC_LIFESTAGE = "PBPKO_00342"

    # geriatric lifestage
    PBPKO_00343 = "PBPKO_00343"
    GERIATRIC_LIFESTAGE = "PBPKO_00343"

    # brain pbpk
    PBPKO_00347 = "PBPKO_00347"
    BRAIN_PBPK = "PBPKO_00347"

    # cerebrospinal fluid volume
    PBPKO_00348 = "PBPKO_00348"
    CEREBROSPINAL_FLUID_VOLUME = "PBPKO_00348"

    # cranial cerebrospinal fluid volume
    PBPKO_00349 = "PBPKO_00349"
    CRANIAL_CEREBROSPINAL_FLUID_VOLUME = "PBPKO_00349"

    # brain mass
    PBPKO_00350 = "PBPKO_00350"
    BRAIN_MASS = "PBPKO_00350"

    # blood brain barrier compartment
    PBPKO_00351 = "PBPKO_00351"
    BLOOD_BRAIN_BARRIER_COMPARTMENT = "PBPKO_00351"

    # spinal cerebrospinal fluid flow rate
    PBPKO_00352 = "PBPKO_00352"
    SPINAL_CEREBROSPINAL_FLUID_FLOW_RATE = "PBPKO_00352"

    # cranial cerebrospinal fluid flow rate
    PBPKO_00353 = "PBPKO_00353"
    CRANIAL_CEREBROSPINAL_FLUID_FLOW_RATE = "PBPKO_00353"

    # blood cerebrospinal fluid compartment
    PBPKO_00354 = "PBPKO_00354"
    BLOOD_CEREBROSPINAL_FLUID_COMPARTMENT = "PBPKO_00354"

    # volume of hippocampus
    PBPKO_00355 = "PBPKO_00355"
    VOLUME_OF_HIPPOCAMPUS = "PBPKO_00355"

    # volume of frontal cortex
    PBPKO_00356 = "PBPKO_00356"
    VOLUME_OF_FRONTAL_CORTEX = "PBPKO_00356"

    # volume of cerebrum
    PBPKO_00357 = "PBPKO_00357"
    VOLUME_OF_CEREBRUM = "PBPKO_00357"

    # volume of cerebellum
    PBPKO_00358 = "PBPKO_00358"
    VOLUME_OF_CEREBELLUM = "PBPKO_00358"

    # blood flow rate to hippocampus
    PBPKO_00359 = "PBPKO_00359"
    BLOOD_FLOW_RATE_TO_HIPPOCAMPUS = "PBPKO_00359"

    # blood flow rate to frontal cortex
    PBPKO_00360 = "PBPKO_00360"
    BLOOD_FLOW_RATE_TO_FRONTAL_CORTEX = "PBPKO_00360"

    # blood flow rate to cerebrum
    PBPKO_00361 = "PBPKO_00361"
    BLOOD_FLOW_RATE_TO_CEREBRUM = "PBPKO_00361"

    # blood flow rate to cerebellum
    PBPKO_00362 = "PBPKO_00362"
    BLOOD_FLOW_RATE_TO_CEREBELLUM = "PBPKO_00362"

    # hippocampus brain partition coefficient
    PBPKO_00363 = "PBPKO_00363"
    HIPPOCAMPUS_BRAIN_PARTITION_COEFFICIENT = "PBPKO_00363"

    # cerebrum brain partition coefficient
    PBPKO_00364 = "PBPKO_00364"
    CEREBRUM_BRAIN_PARTITION_COEFFICIENT = "PBPKO_00364"

    # cerebellum brain partition coefficient
    PBPKO_00365 = "PBPKO_00365"
    CEREBELLUM_BRAIN_PARTITION_COEFFICIENT = "PBPKO_00365"

    # frontalcortex brain partition coefficient
    PBPKO_00366 = "PBPKO_00366"
    FRONTALCORTEX_BRAIN_PARTITION_COEFFICIENT = "PBPKO_00366"

    # apparent permeability cerebrum to rest of brain
    PBPKO_00367 = "PBPKO_00367"
    APPARENT_PERMEABILITY_CEREBRUM_TO_REST_OF_BRAIN = "PBPKO_00367"

    # apparent permeability cerebellum to rest of brain
    PBPKO_00368 = "PBPKO_00368"
    APPARENT_PERMEABILITY_CEREBELLUM_TO_REST_OF_BRAIN = "PBPKO_00368"

    # apparent permeability hippocampus to rest of brain
    PBPKO_00369 = "PBPKO_00369"
    APPARENT_PERMEABILITY_HIPPOCAMPUS_TO_REST_OF_BRAIN = "PBPKO_00369"

    # apparent permeability cortex to rest of brain
    PBPKO_00370 = "PBPKO_00370"
    APPARENT_PERMEABILITY_CORTEX_TO_REST_OF_BRAIN = "PBPKO_00370"

    # pregnant pbpk
    PBPKO_00371 = "PBPKO_00371"
    PREGNANT_PBPK = "PBPKO_00371"

    # fetoplacental volume
    PBPKO_00372 = "PBPKO_00372"
    FETOPLACENTAL_VOLUME = "PBPKO_00372"

    # volume of fetus
    PBPKO_00373 = "PBPKO_00373"
    VOLUME_OF_FETUS = "PBPKO_00373"

    # volume of placenta
    PBPKO_00374 = "PBPKO_00374"
    VOLUME_OF_PLACENTA = "PBPKO_00374"

    # volume of amniotic fluid
    PBPKO_00375 = "PBPKO_00375"
    VOLUME_OF_AMNIOTIC_FLUID = "PBPKO_00375"

    # volume of liver fetus
    PBPKO_00376 = "PBPKO_00376"
    VOLUME_OF_LIVER_FETUS = "PBPKO_00376"

    # volume of brain fetus
    PBPKO_00377 = "PBPKO_00377"
    VOLUME_OF_BRAIN_FETUS = "PBPKO_00377"

    # volume of kidney fetus
    PBPKO_00378 = "PBPKO_00378"
    VOLUME_OF_KIDNEY_FETUS = "PBPKO_00378"

    # volume of rest body fetus
    PBPKO_00379 = "PBPKO_00379"
    VOLUME_OF_REST_BODY_FETUS = "PBPKO_00379"

    # fetoplacental blood flow rate
    PBPKO_00381 = "PBPKO_00381"
    FETOPLACENTAL_BLOOD_FLOW_RATE = "PBPKO_00381"

    # fetal cardiac output rate
    PBPKO_00382 = "PBPKO_00382"
    FETAL_CARDIAC_OUTPUT_RATE = "PBPKO_00382"

    # blood flow rate to liverfetus
    PBPKO_00383 = "PBPKO_00383"
    BLOOD_FLOW_RATE_TO_LIVERFETUS = "PBPKO_00383"

    # blood flow rate to kidneyfetus
    PBPKO_00384 = "PBPKO_00384"
    BLOOD_FLOW_RATE_TO_KIDNEYFETUS = "PBPKO_00384"

    # blood flow rate to brain fetus
    PBPKO_00385 = "PBPKO_00385"
    BLOOD_FLOW_RATE_TO_BRAIN_FETUS = "PBPKO_00385"

    # blood flow rate to restbody fetus
    PBPKO_00386 = "PBPKO_00386"
    BLOOD_FLOW_RATE_TO_RESTBODY_FETUS = "PBPKO_00386"

    # gestational age
    PBPKO_00387 = "PBPKO_00387"
    GESTATIONAL_AGE = "PBPKO_00387"

    # gestational week
    PBPKO_00388 = "PBPKO_00388"
    GESTATIONAL_WEEK = "PBPKO_00388"

    # maximum rate in fetus
    PBPKO_00389 = "PBPKO_00389"
    MAXIMUM_RATE_IN_FETUS = "PBPKO_00389"

    # amniotic transfer coefficient
    PBPKO_00390 = "PBPKO_00390"
    AMNIOTIC_TRANSFER_COEFFICIENT = "PBPKO_00390"

    # liverfetus plasma partition coefficient
    PBPKO_00391 = "PBPKO_00391"
    LIVERFETUS_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00391"

    # brainfetus plasma partition coefficient
    PBPKO_00392 = "PBPKO_00392"
    BRAINFETUS_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00392"

    # kidneyfetus plasma partition coefficient
    PBPKO_00393 = "PBPKO_00393"
    KIDNEYFETUS_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00393"

    # restbodyfetus plasma partition coefficient
    PBPKO_00394 = "PBPKO_00394"
    RESTBODYFETUS_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00394"

    # kidney pbpk
    PBPKO_00395 = "PBPKO_00395"
    KIDNEY_PBPK = "PBPKO_00395"

    # Bowman's capsule compartment
    PBPKO_00396 = "PBPKO_00396"
    BOWMAN_S_CAPSULE_COMPARTMENT = "PBPKO_00396"

    # filtrate compartment
    PBPKO_00397 = "PBPKO_00397"
    FILTRATE_COMPARTMENT = "PBPKO_00397"

    # proximal tubule compartment
    PBPKO_00398 = "PBPKO_00398"
    PROXIMAL_TUBULE_COMPARTMENT = "PBPKO_00398"

    # loop of Henle compartment
    PBPKO_00399 = "PBPKO_00399"
    LOOP_OF_HENLE_COMPARTMENT = "PBPKO_00399"

    # distal tubule compartment
    PBPKO_00400 = "PBPKO_00400"
    DISTAL_TUBULE_COMPARTMENT = "PBPKO_00400"

    # collecting duct compartment
    PBPKO_00401 = "PBPKO_00401"
    COLLECTING_DUCT_COMPARTMENT = "PBPKO_00401"

    # bladder compartment
    PBPKO_00402 = "PBPKO_00402"
    BLADDER_COMPARTMENT = "PBPKO_00402"

    # lung pbpk
    PBPKO_00403 = "PBPKO_00403"
    LUNG_PBPK = "PBPKO_00403"

    # extrathoracic compartment
    PBPKO_00404 = "PBPKO_00404"
    EXTRATHORACIC_COMPARTMENT = "PBPKO_00404"

    # thoracic compartment
    PBPKO_00405 = "PBPKO_00405"
    THORACIC_COMPARTMENT = "PBPKO_00405"

    # bronchiolar compartment
    PBPKO_00406 = "PBPKO_00406"
    BRONCHIOLAR_COMPARTMENT = "PBPKO_00406"

    # alveolar compartment
    PBPKO_00407 = "PBPKO_00407"
    ALVEOLAR_COMPARTMENT = "PBPKO_00407"

    # gut pbpk
    PBPKO_00408 = "PBPKO_00408"
    GUT_PBPK = "PBPKO_00408"

    # fraction of blood flow to duodenum
    PBPKO_00409 = "PBPKO_00409"
    FRACTION_OF_BLOOD_FLOW_TO_DUODENUM = "PBPKO_00409"

    # fraction of blood flow to jejunum
    PBPKO_00410 = "PBPKO_00410"
    FRACTION_OF_BLOOD_FLOW_TO_JEJUNUM = "PBPKO_00410"

    # fraction of blood flow to ileum
    PBPKO_00411 = "PBPKO_00411"
    FRACTION_OF_BLOOD_FLOW_TO_ILEUM = "PBPKO_00411"

    # fraction of blood flow to colon
    PBPKO_00412 = "PBPKO_00412"
    FRACTION_OF_BLOOD_FLOW_TO_COLON = "PBPKO_00412"

    # fraction of blood flow to cecum
    PBPKO_00413 = "PBPKO_00413"
    FRACTION_OF_BLOOD_FLOW_TO_CECUM = "PBPKO_00413"

    # blood flow rate to duodenum
    PBPKO_00414 = "PBPKO_00414"
    BLOOD_FLOW_RATE_TO_DUODENUM = "PBPKO_00414"

    # blood flow rate to jejunum
    PBPKO_00415 = "PBPKO_00415"
    BLOOD_FLOW_RATE_TO_JEJUNUM = "PBPKO_00415"

    # blood flow rate to ileum
    PBPKO_00416 = "PBPKO_00416"
    BLOOD_FLOW_RATE_TO_ILEUM = "PBPKO_00416"

    # blood flow rate to colon
    PBPKO_00417 = "PBPKO_00417"
    BLOOD_FLOW_RATE_TO_COLON = "PBPKO_00417"

    # blood flow rate to cecum
    PBPKO_00418 = "PBPKO_00418"
    BLOOD_FLOW_RATE_TO_CECUM = "PBPKO_00418"

    # fraction of duodenum
    PBPKO_00419 = "PBPKO_00419"
    FRACTION_OF_DUODENUM = "PBPKO_00419"

    # fraction of jejunum
    PBPKO_00420 = "PBPKO_00420"
    FRACTION_OF_JEJUNUM = "PBPKO_00420"

    # fraction of ileum
    PBPKO_00421 = "PBPKO_00421"
    FRACTION_OF_ILEUM = "PBPKO_00421"

    # fraction of colon
    PBPKO_00422 = "PBPKO_00422"
    FRACTION_OF_COLON = "PBPKO_00422"

    # fraction of cecum
    PBPKO_00423 = "PBPKO_00423"
    FRACTION_OF_CECUM = "PBPKO_00423"

    # volume of duodenum
    PBPKO_00424 = "PBPKO_00424"
    VOLUME_OF_DUODENUM = "PBPKO_00424"

    # volume of jejunum
    PBPKO_00425 = "PBPKO_00425"
    VOLUME_OF_JEJUNUM = "PBPKO_00425"

    # volume of ileum
    PBPKO_00426 = "PBPKO_00426"
    VOLUME_OF_ILEUM = "PBPKO_00426"

    # volume of colon
    PBPKO_00427 = "PBPKO_00427"
    VOLUME_OF_COLON = "PBPKO_00427"

    # volume of cecum
    PBPKO_00428 = "PBPKO_00428"
    VOLUME_OF_CECUM = "PBPKO_00428"

    # bile salt effect solubilization ratio
    PBPKO_00429 = "PBPKO_00429"
    BILE_SALT_EFFECT_SOLUBILIZATION_RATIO = "PBPKO_00429"

    # mean precipitation time
    PBPKO_00430 = "PBPKO_00430"
    MEAN_PRECIPITATION_TIME = "PBPKO_00430"

    # diffusion coefficient
    PBPKO_00431 = "PBPKO_00431"
    DIFFUSION_COEFFICIENT = "PBPKO_00431"

    # particle density
    PBPKO_00432 = "PBPKO_00432"
    PARTICLE_DENSITY = "PBPKO_00432"

    # particle radius
    PBPKO_00433 = "PBPKO_00433"
    PARTICLE_RADIUS = "PBPKO_00433"

    # intestinal transit time
    PBPKO_00434 = "PBPKO_00434"
    INTESTINAL_TRANSIT_TIME = "PBPKO_00434"

    # lactational pbpk
    PBPKO_00435 = "PBPKO_00435"
    LACTATIONAL_PBPK = "PBPKO_00435"

    # milk plasma ratio
    PBPKO_00436 = "PBPKO_00436"
    MILK_PLASMA_RATIO = "PBPKO_00436"

    # fraction unbound milk
    PBPKO_00437 = "PBPKO_00437"
    FRACTION_UNBOUND_MILK = "PBPKO_00437"

    # concentration in milk
    PBPKO_00438 = "PBPKO_00438"
    CONCENTRATION_IN_MILK = "PBPKO_00438"

    # daily milk intake
    PBPKO_00439 = "PBPKO_00439"
    DAILY_MILK_INTAKE = "PBPKO_00439"

    # phmilk
    PBPKO_00440 = "PBPKO_00440"
    PHMILK = "PBPKO_00440"

    # blood milk barrier compartment
    PBPKO_00441 = "PBPKO_00441"
    BLOOD_MILK_BARRIER_COMPARTMENT = "PBPKO_00441"

    # milk plasma partition coefficient
    PBPKO_00442 = "PBPKO_00442"
    MILK_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00442"

    # compartment
    PBPKO_00446 = "PBPKO_00446"
    COMPARTMENT = "PBPKO_00446"

    # alveolar air compartment
    PBPKO_00448 = "PBPKO_00448"
    ALVEOLAR_AIR_COMPARTMENT = "PBPKO_00448"

    # rest of body compartment
    PBPKO_00450 = "PBPKO_00450"
    REST_OF_BODY_COMPARTMENT = "PBPKO_00450"

    # arterial plasma
    PBPKO_00451 = "PBPKO_00451"
    ARTERIAL_PLASMA = "PBPKO_00451"

    # venous plasma compartment
    PBPKO_00452 = "PBPKO_00452"
    VENOUS_PLASMA_COMPARTMENT = "PBPKO_00452"

    # richly perfused tissue compartment
    PBPKO_00453 = "PBPKO_00453"
    RICHLY_PERFUSED_TISSUE_COMPARTMENT = "PBPKO_00453"

    # poorly perfused tissue compartment
    PBPKO_00454 = "PBPKO_00454"
    POORLY_PERFUSED_TISSUE_COMPARTMENT = "PBPKO_00454"

    # viable unexposed skin compartment
    PBPKO_00455 = "PBPKO_00455"
    VIABLE_UNEXPOSED_SKIN_COMPARTMENT = "PBPKO_00455"

    # viable exposed skin compartment
    PBPKO_00456 = "PBPKO_00456"
    VIABLE_EXPOSED_SKIN_COMPARTMENT = "PBPKO_00456"

    # skin unexposed stratum corneum
    PBPKO_00457 = "PBPKO_00457"
    SKIN_UNEXPOSED_STRATUM_CORNEUM = "PBPKO_00457"

    # skin exposed stratum corneum compartment
    PBPKO_00458 = "PBPKO_00458"
    SKIN_EXPOSED_STRATUM_CORNEUM_COMPARTMENT = "PBPKO_00458"

    # adipose compartment
    PBPKO_00460 = "PBPKO_00460"
    ADIPOSE_COMPARTMENT = "PBPKO_00460"

    # anal canal compartment
    PBPKO_00461 = "PBPKO_00461"
    ANAL_CANAL_COMPARTMENT = "PBPKO_00461"

    # appendix compartment
    PBPKO_00462 = "PBPKO_00462"
    APPENDIX_COMPARTMENT = "PBPKO_00462"

    # ascending colon compartment
    PBPKO_00463 = "PBPKO_00463"
    ASCENDING_COLON_COMPARTMENT = "PBPKO_00463"

    # blood compartment
    PBPKO_00464 = "PBPKO_00464"
    BLOOD_COMPARTMENT = "PBPKO_00464"

    # bone marrow compartment
    PBPKO_00465 = "PBPKO_00465"
    BONE_MARROW_COMPARTMENT = "PBPKO_00465"

    # brain compartment
    PBPKO_00466 = "PBPKO_00466"
    BRAIN_COMPARTMENT = "PBPKO_00466"

    # cecum compartment
    PBPKO_00467 = "PBPKO_00467"
    CECUM_COMPARTMENT = "PBPKO_00467"

    # descending colon compartment
    PBPKO_00468 = "PBPKO_00468"
    DESCENDING_COLON_COMPARTMENT = "PBPKO_00468"

    # dermis compartment
    PBPKO_00469 = "PBPKO_00469"
    DERMIS_COMPARTMENT = "PBPKO_00469"

    # skin compartment
    PBPKO_00470 = "PBPKO_00470"
    SKIN_COMPARTMENT = "PBPKO_00470"

    # duodenum compartment
    PBPKO_00471 = "PBPKO_00471"
    DUODENUM_COMPARTMENT = "PBPKO_00471"

    # small intestine compartment
    PBPKO_00472 = "PBPKO_00472"
    SMALL_INTESTINE_COMPARTMENT = "PBPKO_00472"

    # endocrine gland compartment
    PBPKO_00473 = "PBPKO_00473"
    ENDOCRINE_GLAND_COMPARTMENT = "PBPKO_00473"

    # large intestine compartment
    PBPKO_00474 = "PBPKO_00474"
    LARGE_INTESTINE_COMPARTMENT = "PBPKO_00474"

    # epidermis compartment
    PBPKO_00475 = "PBPKO_00475"
    EPIDERMIS_COMPARTMENT = "PBPKO_00475"

    # gall bladder compartment
    PBPKO_00476 = "PBPKO_00476"
    GALL_BLADDER_COMPARTMENT = "PBPKO_00476"

    # gut compartment
    PBPKO_00477 = "PBPKO_00477"
    GUT_COMPARTMENT = "PBPKO_00477"

    # gut lumen compartment
    PBPKO_00478 = "PBPKO_00478"
    GUT_LUMEN_COMPARTMENT = "PBPKO_00478"

    # hair compartment
    PBPKO_00479 = "PBPKO_00479"
    HAIR_COMPARTMENT = "PBPKO_00479"

    # heart compartment
    PBPKO_00480 = "PBPKO_00480"
    HEART_COMPARTMENT = "PBPKO_00480"

    # ileum compartment
    PBPKO_00481 = "PBPKO_00481"
    ILEUM_COMPARTMENT = "PBPKO_00481"

    # jejunum compartment
    PBPKO_00482 = "PBPKO_00482"
    JEJUNUM_COMPARTMENT = "PBPKO_00482"

    # mammary gland compartment
    PBPKO_00483 = "PBPKO_00483"
    MAMMARY_GLAND_COMPARTMENT = "PBPKO_00483"

    # muscle compartment
    PBPKO_00484 = "PBPKO_00484"
    MUSCLE_COMPARTMENT = "PBPKO_00484"

    # nail compartment
    PBPKO_00485 = "PBPKO_00485"
    NAIL_COMPARTMENT = "PBPKO_00485"

    # pancreas compartment
    PBPKO_00486 = "PBPKO_00486"
    PANCREAS_COMPARTMENT = "PBPKO_00486"

    # placental barrier compartment
    PBPKO_00487 = "PBPKO_00487"
    PLACENTAL_BARRIER_COMPARTMENT = "PBPKO_00487"

    # plasma compartment
    PBPKO_00488 = "PBPKO_00488"
    PLASMA_COMPARTMENT = "PBPKO_00488"

    # rectum compartment
    PBPKO_00489 = "PBPKO_00489"
    RECTUM_COMPARTMENT = "PBPKO_00489"

    # reproductive compartment
    PBPKO_00490 = "PBPKO_00490"
    REPRODUCTIVE_COMPARTMENT = "PBPKO_00490"

    # sigmoid colon compartment
    PBPKO_00491 = "PBPKO_00491"
    SIGMOID_COLON_COMPARTMENT = "PBPKO_00491"

    # spleen compartment
    PBPKO_00492 = "PBPKO_00492"
    SPLEEN_COMPARTMENT = "PBPKO_00492"

    # stratum corneum compartment
    PBPKO_00493 = "PBPKO_00493"
    STRATUM_CORNEUM_COMPARTMENT = "PBPKO_00493"

    # transverse colon compartment
    PBPKO_00494 = "PBPKO_00494"
    TRANSVERSE_COLON_COMPARTMENT = "PBPKO_00494"

    # barrier compartment
    PBPKO_00495 = "PBPKO_00495"
    BARRIER_COMPARTMENT = "PBPKO_00495"

    # amount in gut
    PBPKO_00496 = "PBPKO_00496"
    AMOUNT_IN_GUT = "PBPKO_00496"

    # amount in liver
    PBPKO_00497 = "PBPKO_00497"
    AMOUNT_IN_LIVER = "PBPKO_00497"

    # amount in kidney
    PBPKO_00498 = "PBPKO_00498"
    AMOUNT_IN_KIDNEY = "PBPKO_00498"

    # amount in filtrate
    PBPKO_00499 = "PBPKO_00499"
    AMOUNT_IN_FILTRATE = "PBPKO_00499"

    # amount in delay
    PBPKO_00500 = "PBPKO_00500"
    AMOUNT_IN_DELAY = "PBPKO_00500"

    # amount in restbody
    PBPKO_00501 = "PBPKO_00501"
    AMOUNT_IN_RESTBODY = "PBPKO_00501"

    # amount in plasma
    PBPKO_00502 = "PBPKO_00502"
    AMOUNT_IN_PLASMA = "PBPKO_00502"

    # amount in brain
    PBPKO_00503 = "PBPKO_00503"
    AMOUNT_IN_BRAIN = "PBPKO_00503"

    # amount in lung
    PBPKO_00504 = "PBPKO_00504"
    AMOUNT_IN_LUNG = "PBPKO_00504"

    # amount in bone marrow
    PBPKO_00505 = "PBPKO_00505"
    AMOUNT_IN_BONE_MARROW = "PBPKO_00505"

    # amount in skin
    PBPKO_00506 = "PBPKO_00506"
    AMOUNT_IN_SKIN = "PBPKO_00506"

    # amount in mammary gland
    PBPKO_00507 = "PBPKO_00507"
    AMOUNT_IN_MAMMARY_GLAND = "PBPKO_00507"

    # fraction of filtrate
    PBPKO_00508 = "PBPKO_00508"
    FRACTION_OF_FILTRATE = "PBPKO_00508"

    # fraction of gut
    PBPKO_00509 = "PBPKO_00509"
    FRACTION_OF_GUT = "PBPKO_00509"

    # fraction of mammary gland
    PBPKO_00510 = "PBPKO_00510"
    FRACTION_OF_MAMMARY_GLAND = "PBPKO_00510"

    # fraction of blood flow to filtrate
    PBPKO_00511 = "PBPKO_00511"
    FRACTION_OF_BLOOD_FLOW_TO_FILTRATE = "PBPKO_00511"

    # fraction of blood flow to bone marrow
    PBPKO_00512 = "PBPKO_00512"
    FRACTION_OF_BLOOD_FLOW_TO_BONE_MARROW = "PBPKO_00512"

    # fraction of blood flow to gut
    PBPKO_00513 = "PBPKO_00513"
    FRACTION_OF_BLOOD_FLOW_TO_GUT = "PBPKO_00513"

    # fraction of blood flow to mammary gland
    PBPKO_00514 = "PBPKO_00514"
    FRACTION_OF_BLOOD_FLOW_TO_MAMMARY_GLAND = "PBPKO_00514"

    # brain plasma partition coefficient
    PBPKO_00515 = "PBPKO_00515"
    BRAIN_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00515"

    # mammary gland plasma partition coefficient
    PBPKO_00517 = "PBPKO_00517"
    MAMMARY_GLAND_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00517"

    # restbody plasma partition coefficient
    PBPKO_00518 = "PBPKO_00518"
    RESTBODY_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00518"

    # tissue plasma partition coefficient
    PBPKO_00519 = "PBPKO_00519"
    TISSUE_PLASMA_PARTITION_COEFFICIENT = "PBPKO_00519"

    # urinary rate constant
    PBPKO_00520 = "PBPKO_00520"
    URINARY_RATE_CONSTANT = "PBPKO_00520"

    # age in PBPK model
    PBPKO_00521 = "PBPKO_00521"
    AGE_IN_PBPK_MODEL = "PBPKO_00521"

    # volume of filtrate
    PBPKO_00522 = "PBPKO_00522"
    VOLUME_OF_FILTRATE = "PBPKO_00522"

    # volume of bone marrow
    PBPKO_00523 = "PBPKO_00523"
    VOLUME_OF_BONE_MARROW = "PBPKO_00523"

    # volume of gut
    PBPKO_00524 = "PBPKO_00524"
    VOLUME_OF_GUT = "PBPKO_00524"

    # volume of mammary gland
    PBPKO_00525 = "PBPKO_00525"
    VOLUME_OF_MAMMARY_GLAND = "PBPKO_00525"

    # volume of mass balance
    PBPKO_00526 = "PBPKO_00526"
    VOLUME_OF_MASS_BALANCE = "PBPKO_00526"

    # hematocrit volume
    PBPKO_00527 = "PBPKO_00527"
    HEMATOCRIT_VOLUME = "PBPKO_00527"

    # cardiac output rate of plasma
    PBPKO_00528 = "PBPKO_00528"
    CARDIAC_OUTPUT_RATE_OF_PLASMA = "PBPKO_00528"

    # blood flow rate to filtrate
    PBPKO_00529 = "PBPKO_00529"
    BLOOD_FLOW_RATE_TO_FILTRATE = "PBPKO_00529"

    # blood flow rate to bone marrow
    PBPKO_00530 = "PBPKO_00530"
    BLOOD_FLOW_RATE_TO_BONE_MARROW = "PBPKO_00530"

    # blood flow rate to gut
    PBPKO_00531 = "PBPKO_00531"
    BLOOD_FLOW_RATE_TO_GUT = "PBPKO_00531"

    # blood flow rate to mammary gland
    PBPKO_00532 = "PBPKO_00532"
    BLOOD_FLOW_RATE_TO_MAMMARY_GLAND = "PBPKO_00532"

    # blood flow rate for mass balance
    PBPKO_00533 = "PBPKO_00533"
    BLOOD_FLOW_RATE_FOR_MASS_BALANCE = "PBPKO_00533"

    # urinary rate
    PBPKO_00534 = "PBPKO_00534"
    URINARY_RATE = "PBPKO_00534"

    # resorption maximum
    PBPKO_00535 = "PBPKO_00535"
    RESORPTION_MAXIMUM = "PBPKO_00535"

    # resorption
    PBPKO_00536 = "PBPKO_00536"
    RESORPTION = "PBPKO_00536"

    # octanol air partition coefficient
    PBPKO_00537 = "PBPKO_00537"
    OCTANOL_AIR_PARTITION_COEFFICIENT = "PBPKO_00537"

    # concentration in gut
    PBPKO_00538 = "PBPKO_00538"
    CONCENTRATION_IN_GUT = "PBPKO_00538"

    # concentration in liver
    PBPKO_00539 = "PBPKO_00539"
    CONCENTRATION_IN_LIVER = "PBPKO_00539"

    # concentration in brain
    PBPKO_00540 = "PBPKO_00540"
    CONCENTRATION_IN_BRAIN = "PBPKO_00540"

    # concentration in kidney
    PBPKO_00541 = "PBPKO_00541"
    CONCENTRATION_IN_KIDNEY = "PBPKO_00541"

    # concentration in filtrate
    PBPKO_00542 = "PBPKO_00542"
    CONCENTRATION_IN_FILTRATE = "PBPKO_00542"

    # concentration in lung
    PBPKO_00543 = "PBPKO_00543"
    CONCENTRATION_IN_LUNG = "PBPKO_00543"

    # concentration in fat
    PBPKO_00544 = "PBPKO_00544"
    CONCENTRATION_IN_FAT = "PBPKO_00544"

    # concentration in bone marrow
    PBPKO_00545 = "PBPKO_00545"
    CONCENTRATION_IN_BONE_MARROW = "PBPKO_00545"

    # concentration in skin
    PBPKO_00546 = "PBPKO_00546"
    CONCENTRATION_IN_SKIN = "PBPKO_00546"

    # concentration in mammary gland
    PBPKO_00547 = "PBPKO_00547"
    CONCENTRATION_IN_MAMMARY_GLAND = "PBPKO_00547"

    # concentration in restbody
    PBPKO_00548 = "PBPKO_00548"
    CONCENTRATION_IN_RESTBODY = "PBPKO_00548"

    # concentration in plasma
    PBPKO_00549 = "PBPKO_00549"
    CONCENTRATION_IN_PLASMA = "PBPKO_00549"

    # amount in fat
    PBPKO_00550 = "PBPKO_00550"
    AMOUNT_IN_FAT = "PBPKO_00550"

    # PBPK model simulation time
    PBPKO_00551 = "PBPKO_00551"
    PBPK_MODEL_SIMULATION_TIME = "PBPKO_00551"

    # arterial blood compartment
    PBPKO_00552 = "PBPKO_00552"
    ARTERIAL_BLOOD_COMPARTMENT = "PBPKO_00552"

    # digestive system compartment
    PBPKO_00553 = "PBPKO_00553"
    DIGESTIVE_SYSTEM_COMPARTMENT = "PBPKO_00553"

    # excreta compartment
    PBPKO_00554 = "PBPKO_00554"
    EXCRETA_COMPARTMENT = "PBPKO_00554"

    # feces compartment
    PBPKO_00555 = "PBPKO_00555"
    FECES_COMPARTMENT = "PBPKO_00555"

    # urine compartment
    PBPKO_00556 = "PBPKO_00556"
    URINE_COMPARTMENT = "PBPKO_00556"

    # kidney compartment
    PBPKO_00557 = "PBPKO_00557"
    KIDNEY_COMPARTMENT = "PBPKO_00557"

    # liver compartment
    PBPKO_00558 = "PBPKO_00558"
    LIVER_COMPARTMENT = "PBPKO_00558"

    # lung compartment
    PBPKO_00559 = "PBPKO_00559"
    LUNG_COMPARTMENT = "PBPKO_00559"

    # venous blood compartment
    PBPKO_00561 = "PBPKO_00561"
    VENOUS_BLOOD_COMPARTMENT = "PBPKO_00561"

    # blood flow rate to unexposed skin
    PBPKO_00562 = "PBPKO_00562"
    BLOOD_FLOW_RATE_TO_UNEXPOSED_SKIN = "PBPKO_00562"

    # blood flow rate to exposed skin
    PBPKO_00563 = "PBPKO_00563"
    BLOOD_FLOW_RATE_TO_EXPOSED_SKIN = "PBPKO_00563"

    # blood flow rate to skin stratum corneum unexposed
    PBPKO_00564 = "PBPKO_00564"
    BLOOD_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_UNEXPOSED = "PBPKO_00564"

    # blood flow rate to skin stratum corneum exposed
    PBPKO_00565 = "PBPKO_00565"
    BLOOD_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_EXPOSED = "PBPKO_00565"

    # stomach compartment
    PBPKO_00566 = "PBPKO_00566"
    STOMACH_COMPARTMENT = "PBPKO_00566"

    # bone blood partition coefficient
    PBPKO_00567 = "PBPKO_00567"
    BONE_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00567"

    # air blood partition coefficient
    PBPKO_00568 = "PBPKO_00568"
    AIR_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00568"

    # brain blood partition coefficient
    PBPKO_00569 = "PBPKO_00569"
    BRAIN_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00569"

    # brainfetus blood partition coefficient
    PBPKO_00570 = "PBPKO_00570"
    BRAINFETUS_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00570"

    # gonad blood partition coefficient
    PBPKO_00571 = "PBPKO_00571"
    GONAD_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00571"

    # gut blood partition coefficient
    PBPKO_00572 = "PBPKO_00572"
    GUT_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00572"

    # heart blood partition coefficient
    PBPKO_00573 = "PBPKO_00573"
    HEART_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00573"

    # intestine blood partition coefficient
    PBPKO_00574 = "PBPKO_00574"
    INTESTINE_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00574"

    # kidney blood partition coefficient
    PBPKO_00575 = "PBPKO_00575"
    KIDNEY_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00575"

    # kidneyfetus blood partition coefficient
    PBPKO_00576 = "PBPKO_00576"
    KIDNEYFETUS_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00576"

    # liver blood partition coefficient
    PBPKO_00577 = "PBPKO_00577"
    LIVER_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00577"

    # liverfetus blood partition coefficient
    PBPKO_00578 = "PBPKO_00578"
    LIVERFETUS_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00578"

    # lung blood partition coefficient
    PBPKO_00579 = "PBPKO_00579"
    LUNG_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00579"

    # mammary gland blood partition coefficient
    PBPKO_00580 = "PBPKO_00580"
    MAMMARY_GLAND_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00580"

    # milk blood partition coefficient
    PBPKO_00581 = "PBPKO_00581"
    MILK_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00581"

    # muscle blood partition coefficient
    PBPKO_00582 = "PBPKO_00582"
    MUSCLE_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00582"

    # pancreas blood partition coefficient
    PBPKO_00583 = "PBPKO_00583"
    PANCREAS_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00583"

    # poor perfused blood partition coefficient
    PBPKO_00584 = "PBPKO_00584"
    POOR_PERFUSED_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00584"

    # restbody blood partition coefficient
    PBPKO_00585 = "PBPKO_00585"
    RESTBODY_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00585"

    # restbodyfetus blood partition coefficient
    PBPKO_00586 = "PBPKO_00586"
    RESTBODYFETUS_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00586"

    # rich perfused blood partition coefficient
    PBPKO_00587 = "PBPKO_00587"
    RICH_PERFUSED_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00587"

    # skin blood partition coefficient
    PBPKO_00588 = "PBPKO_00588"
    SKIN_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00588"

    # spleen blood partition coefficient
    PBPKO_00589 = "PBPKO_00589"
    SPLEEN_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00589"

    # stomach blood partition coefficient
    PBPKO_00590 = "PBPKO_00590"
    STOMACH_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00590"

    # fraction unbound plasma
    PBPKO_00591 = "PBPKO_00591"
    FRACTION_UNBOUND_PLASMA = "PBPKO_00591"

    # maximum rate of apical transporter
    PBPKO_00592 = "PBPKO_00592"
    MAXIMUM_RATE_OF_APICAL_TRANSPORTER = "PBPKO_00592"

    # maximum rate of basolateral transporter
    PBPKO_00593 = "PBPKO_00593"
    MAXIMUM_RATE_OF_BASOLATERAL_TRANSPORTER = "PBPKO_00593"

    # fraction of volume of compartment
    PBPKO_00610 = "PBPKO_00610"
    FRACTION_OF_VOLUME_OF_COMPARTMENT = "PBPKO_00610"

    # fraction of blood flow to a compartment
    PBPKO_00611 = "PBPKO_00611"
    FRACTION_OF_BLOOD_FLOW_TO_A_COMPARTMENT = "PBPKO_00611"

    # apparent permeability
    PBPKO_00612 = "PBPKO_00612"
    APPARENT_PERMEABILITY = "PBPKO_00612"

    # maximum rate
    PBPKO_00613 = "PBPKO_00613"
    MAXIMUM_RATE = "PBPKO_00613"

    # amount of compound in compartment
    PBPKO_00615 = "PBPKO_00615"
    AMOUNT_OF_COMPOUND_IN_COMPARTMENT = "PBPKO_00615"

    # concentration of compound in compartment
    PBPKO_00616 = "PBPKO_00616"
    CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT = "PBPKO_00616"

    # hippocampus compartment
    PBPKO_00617 = "PBPKO_00617"
    HIPPOCAMPUS_COMPARTMENT = "PBPKO_00617"

    # cerebrum compartment
    PBPKO_00618 = "PBPKO_00618"
    CEREBRUM_COMPARTMENT = "PBPKO_00618"

    # cerebellum compartment
    PBPKO_00619 = "PBPKO_00619"
    CEREBELLUM_COMPARTMENT = "PBPKO_00619"

    # frontal cortex compartment
    PBPKO_00620 = "PBPKO_00620"
    FRONTAL_CORTEX_COMPARTMENT = "PBPKO_00620"

    # cerebrospinal fluid compartment
    PBPKO_00621 = "PBPKO_00621"
    CEREBROSPINAL_FLUID_COMPARTMENT = "PBPKO_00621"

    # fraction unbound blood
    PBPKO_00622 = "PBPKO_00622"
    FRACTION_UNBOUND_BLOOD = "PBPKO_00622"

    # amount in blood
    PBPKO_00623 = "PBPKO_00623"
    AMOUNT_IN_BLOOD = "PBPKO_00623"

    # fraction unbound restbody
    PBPKO_00624 = "PBPKO_00624"
    FRACTION_UNBOUND_RESTBODY = "PBPKO_00624"

    # exposed skin compartment
    PBPKO_00625 = "PBPKO_00625"
    EXPOSED_SKIN_COMPARTMENT = "PBPKO_00625"

    # unexposed skin compartment
    PBPKO_00626 = "PBPKO_00626"
    UNEXPOSED_SKIN_COMPARTMENT = "PBPKO_00626"

    # fraction of arterial plasma volume
    PBPKO_00627 = "PBPKO_00627"
    FRACTION_OF_ARTERIAL_PLASMA_VOLUME = "PBPKO_00627"

    # fraction of venous plasma volume
    PBPKO_00628 = "PBPKO_00628"
    FRACTION_OF_VENOUS_PLASMA_VOLUME = "PBPKO_00628"

    # amount in richly perfused tissue
    PBPKO_00629 = "PBPKO_00629"
    AMOUNT_IN_RICHLY_PERFUSED_TISSUE = "PBPKO_00629"

    # amount in poorly perfused tissue
    PBPKO_00630 = "PBPKO_00630"
    AMOUNT_IN_POORLY_PERFUSED_TISSUE = "PBPKO_00630"

    # amount in arterial blood
    PBPKO_00631 = "PBPKO_00631"
    AMOUNT_IN_ARTERIAL_BLOOD = "PBPKO_00631"

    # amount in venous blood
    PBPKO_00632 = "PBPKO_00632"
    AMOUNT_IN_VENOUS_BLOOD = "PBPKO_00632"

    # amount in alveolar air
    PBPKO_00633 = "PBPKO_00633"
    AMOUNT_IN_ALVEOLAR_AIR = "PBPKO_00633"

    # red blood cell compartment
    PBPKO_00634 = "PBPKO_00634"
    RED_BLOOD_CELL_COMPARTMENT = "PBPKO_00634"

    # skin thickness
    PBPKO_00635 = "PBPKO_00635"
    SKIN_THICKNESS = "PBPKO_00635"

    # bodily fluid flow rate parameter
    PBPKO_00636 = "PBPKO_00636"
    BODILY_FLUID_FLOW_RATE_PARAMETER = "PBPKO_00636"

    # amount in viable epidermis of unexposed skin
    PBPKO_00637 = "PBPKO_00637"
    AMOUNT_IN_VIABLE_EPIDERMIS_OF_UNEXPOSED_SKIN = "PBPKO_00637"

    # amount in viable epidermis of exposed skin
    PBPKO_00638 = "PBPKO_00638"
    AMOUNT_IN_VIABLE_EPIDERMIS_OF_EXPOSED_SKIN = "PBPKO_00638"

    # amount in skin stratum corneum of unexposed skin
    PBPKO_00639 = "PBPKO_00639"
    AMOUNT_IN_SKIN_STRATUM_CORNEUM_OF_UNEXPOSED_SKIN = "PBPKO_00639"

    # amount in skin stratum corneum of exposed skin
    PBPKO_00640 = "PBPKO_00640"
    AMOUNT_IN_SKIN_STRATUM_CORNEUM_OF_EXPOSED_SKIN = "PBPKO_00640"

    # dermal absorption rate unexposed skin
    PBPKO_00641 = "PBPKO_00641"
    DERMAL_ABSORPTION_RATE_UNEXPOSED_SKIN = "PBPKO_00641"

    # dermal absorption rate exposed skin
    PBPKO_00642 = "PBPKO_00642"
    DERMAL_ABSORPTION_RATE_EXPOSED_SKIN = "PBPKO_00642"

    # thickness stratum corneum
    PBPKO_00643 = "PBPKO_00643"
    THICKNESS_STRATUM_CORNEUM = "PBPKO_00643"

    # thickness viable epidermis
    PBPKO_00644 = "PBPKO_00644"
    THICKNESS_VIABLE_EPIDERMIS = "PBPKO_00644"

    # fat blood partition coefficient
    PBPKO_00645 = "PBPKO_00645"
    FAT_BLOOD_PARTITION_COEFFICIENT = "PBPKO_00645"

    # diffusion rate
    PBPKO_00646 = "PBPKO_00646"
    DIFFUSION_RATE = "PBPKO_00646"

    # diffusion rate skin
    PBPKO_00647 = "PBPKO_00647"
    DIFFUSION_RATE_SKIN = "PBPKO_00647"

    # diffusion rate stratum corneum viable epidermis
    PBPKO_00648 = "PBPKO_00648"
    DIFFUSION_RATE_STRATUM_CORNEUM_VIABLE_EPIDERMIS = "PBPKO_00648"

    # miscellaneous parameter
    PBPKO_00649 = "PBPKO_00649"
    MISCELLANEOUS_PARAMETER = "PBPKO_00649"

    # Michaelis
    PBPKO_00650 = "PBPKO_00650"
    MICHAELIS = "PBPKO_00650"

    # fraction of arterial blood volume
    PBPKO_00651 = "PBPKO_00651"
    FRACTION_OF_ARTERIAL_BLOOD_VOLUME = "PBPKO_00651"

    # pgp
    PBPKO_01501 = "PBPKO_01501"
    PGP = "PBPKO_01501"

    # mrp2
    PBPKO_01502 = "PBPKO_01502"
    MRP2 = "PBPKO_01502"

    # mrp4
    PBPKO_01503 = "PBPKO_01503"
    MRP4 = "PBPKO_01503"

    # bcrp
    PBPKO_01504 = "PBPKO_01504"
    BCRP = "PBPKO_01504"

    # nctp
    PBPKO_01505 = "PBPKO_01505"
    NCTP = "PBPKO_01505"

    # oct1
    PBPKO_01506 = "PBPKO_01506"
    OCT1 = "PBPKO_01506"

    # oat1
    PBPKO_01507 = "PBPKO_01507"
    OAT1 = "PBPKO_01507"

    # oat3
    PBPKO_01508 = "PBPKO_01508"
    OAT3 = "PBPKO_01508"

    # oat4
    PBPKO_01509 = "PBPKO_01509"
    OAT4 = "PBPKO_01509"

    # bile compartment
    PBPKO_02001 = "PBPKO_02001"
    BILE_COMPARTMENT = "PBPKO_02001"

    # colon compartment
    PBPKO_02002 = "PBPKO_02002"
    COLON_COMPARTMENT = "PBPKO_02002"

    # small intestine tissue compartment
    PBPKO_02003 = "PBPKO_02003"
    SMALL_INTESTINE_TISSUE_COMPARTMENT = "PBPKO_02003"

    # intestinal tissue compartment
    PBPKO_02004 = "PBPKO_02004"
    INTESTINAL_TISSUE_COMPARTMENT = "PBPKO_02004"

    # portal vein perfused tissue comparment
    PBPKO_02005 = "PBPKO_02005"
    PORTAL_VEIN_PERFUSED_TISSUE_COMPARMENT = "PBPKO_02005"

    # glomerulus compartment
    PBPKO_02006 = "PBPKO_02006"
    GLOMERULUS_COMPARTMENT = "PBPKO_02006"

    # menstrual plasma compartment
    PBPKO_02007 = "PBPKO_02007"
    MENSTRUAL_PLASMA_COMPARTMENT = "PBPKO_02007"

    # kidney rest lumen compartment
    PBPKO_02008 = "PBPKO_02008"
    KIDNEY_REST_LUMEN_COMPARTMENT = "PBPKO_02008"

    # kidney proximal tubule tissue compartment
    PBPKO_02009 = "PBPKO_02009"
    KIDNEY_PROXIMAL_TUBULE_TISSUE_COMPARTMENT = "PBPKO_02009"

    # liver extracellular compartment
    PBPKO_02010 = "PBPKO_02010"
    LIVER_EXTRACELLULAR_COMPARTMENT = "PBPKO_02010"

    # liver intracellular space compartment
    PBPKO_02011 = "PBPKO_02011"
    LIVER_INTRACELLULAR_SPACE_COMPARTMENT = "PBPKO_02011"

    # gastro intestinal tract compartment
    PBPKO_02012 = "PBPKO_02012"
    GASTRO_INTESTINAL_TRACT_COMPARTMENT = "PBPKO_02012"

    # gonad compartment
    PBPKO_02013 = "PBPKO_02013"
    GONAD_COMPARTMENT = "PBPKO_02013"

    # intrinsic gastric emptying rate
    PBPKO_03001 = "PBPKO_03001"
    INTRINSIC_GASTRIC_EMPTYING_RATE = "PBPKO_03001"

    # intrinsic absorption rate
    PBPKO_03002 = "PBPKO_03002"
    INTRINSIC_ABSORPTION_RATE = "PBPKO_03002"

    # intrinsic stomach uptake rate
    PBPKO_03003 = "PBPKO_03003"
    INTRINSIC_STOMACH_UPTAKE_RATE = "PBPKO_03003"

    # stomach uptake rate
    PBPKO_03004 = "PBPKO_03004"
    STOMACH_UPTAKE_RATE = "PBPKO_03004"

    # intrinsic fecal excretion rate
    PBPKO_03005 = "PBPKO_03005"
    INTRINSIC_FECAL_EXCRETION_RATE = "PBPKO_03005"

    # fecal excretion rate
    PBPKO_03006 = "PBPKO_03006"
    FECAL_EXCRETION_RATE = "PBPKO_03006"

    # intrinsic biliary clearance rate
    PBPKO_03007 = "PBPKO_03007"
    INTRINSIC_BILIARY_CLEARANCE_RATE = "PBPKO_03007"

    # kinetic emptying rate from jejunum lumen to ileum lumen
    PBPKO_03008 = "PBPKO_03008"
    KINETIC_EMPTYING_RATE_FROM_JEJUNUM_LUMEN_TO_ILEUM_LUMEN = "PBPKO_03008"

    # kinetic emptying  rate from ileum lumen to large intestine lumen
    PBPKO_03009 = "PBPKO_03009"
    KINETIC_EMPTYING__RATE_FROM_ILEUM_LUMEN_TO_LARGE_INTESTINE_LUMEN = "PBPKO_03009"

    # kinetic absorption rate from jejunum lumen to intestinal tissue
    PBPKO_03010 = "PBPKO_03010"
    KINETIC_ABSORPTION_RATE_FROM_JEJUNUM_LUMEN_TO_INTESTINAL_TISSUE = "PBPKO_03010"

    # kinetic absorption rate from ileum lumen to intestinal tissue
    PBPKO_03011 = "PBPKO_03011"
    KINETIC_ABSORPTION_RATE_FROM_ILEUM_LUMEN_TO_INTESTINAL_TISSUE = "PBPKO_03011"

    # kinetic absorption rate from large intestinal lumen to intestinal tissue
    PBPKO_03012 = "PBPKO_03012"
    KINETIC_ABSORPTION_RATE_FROM_LARGE_INTESTINAL_LUMEN_TO_INTESTINAL_TISSUE = (
        "PBPKO_03012"
    )

    # effective Caco-2 permeability
    PBPKO_03013 = "PBPKO_03013"
    EFFECTIVE_CACO_2_PERMEABILITY = "PBPKO_03013"

    # apparent Caco-2 permeability
    PBPKO_03014 = "PBPKO_03014"
    APPARENT_CACO_2_PERMEABILITY = "PBPKO_03014"

    # kinetic emptying  rate between intestinal segments
    PBPKO_03015 = "PBPKO_03015"
    KINETIC_EMPTYING__RATE_BETWEEN_INTESTINAL_SEGMENTS = "PBPKO_03015"

    # Hill dissociation constant
    PBPKO_03016 = "PBPKO_03016"
    HILL_DISSOCIATION_CONSTANT = "PBPKO_03016"

    # Hill coefficient
    PBPKO_03017 = "PBPKO_03017"
    HILL_COEFFICIENT = "PBPKO_03017"

    # intrinsic absorption rate of metabilite
    PBPKO_03018 = "PBPKO_03018"
    INTRINSIC_ABSORPTION_RATE_OF_METABILITE = "PBPKO_03018"

    # absorption rate of metabolite
    PBPKO_03019 = "PBPKO_03019"
    ABSORPTION_RATE_OF_METABOLITE = "PBPKO_03019"

    # intrinsic enterohepatic recirculation rate constant
    PBPKO_03020 = "PBPKO_03020"
    INTRINSIC_ENTEROHEPATIC_RECIRCULATION_RATE_CONSTANT = "PBPKO_03020"

    # enterohepatic recirculation rate constant
    PBPKO_03021 = "PBPKO_03021"
    ENTEROHEPATIC_RECIRCULATION_RATE_CONSTANT = "PBPKO_03021"

    # intrinsic reabsorption rate constant
    PBPKO_03023 = "PBPKO_03023"
    INTRINSIC_REABSORPTION_RATE_CONSTANT = "PBPKO_03023"

    # reabsorption rate constant
    PBPKO_03024 = "PBPKO_03024"
    REABSORPTION_RATE_CONSTANT = "PBPKO_03024"

    # maximum capacity of binding sites in red cells
    PBPKO_03025 = "PBPKO_03025"
    MAXIMUM_CAPACITY_OF_BINDING_SITES_IN_RED_CELLS = "PBPKO_03025"

    # half-saturation concentration of chemical for binding by sites in red cells
    PBPKO_03026 = "PBPKO_03026"
    HALF_SATURATION_CONCENTRATION_OF_CHEMICAL_FOR_BINDING_BY_SITES_IN_RED_CELLS = (
        "PBPKO_03026"
    )

    # metabolism rate constant in liver
    PBPKO_03027 = "PBPKO_03027"
    METABOLISM_RATE_CONSTANT_IN_LIVER = "PBPKO_03027"

    # metabolism rate constant in intestinal tissue
    PBPKO_03028 = "PBPKO_03028"
    METABOLISM_RATE_CONSTANT_IN_INTESTINAL_TISSUE = "PBPKO_03028"

    # red blood cells partition coefficient
    PBPKO_03030 = "PBPKO_03030"
    RED_BLOOD_CELLS_PARTITION_COEFFICIENT = "PBPKO_03030"

    # follicle permeability coefficient
    PBPKO_03031 = "PBPKO_03031"
    FOLLICLE_PERMEABILITY_COEFFICIENT = "PBPKO_03031"

    # partition coeffcient of stratum corneum to viable epidermis
    PBPKO_03032 = "PBPKO_03032"
    PARTITION_COEFFCIENT_OF_STRATUM_CORNEUM_TO_VIABLE_EPIDERMIS = "PBPKO_03032"

    # partition coeffcient of viable epidermis to blood
    PBPKO_03033 = "PBPKO_03033"
    PARTITION_COEFFCIENT_OF_VIABLE_EPIDERMIS_TO_BLOOD = "PBPKO_03033"

    # partition coeffcient of stratum corneum to skin surface depot
    PBPKO_03034 = "PBPKO_03034"
    PARTITION_COEFFCIENT_OF_STRATUM_CORNEUM_TO_SKIN_SURFACE_DEPOT = "PBPKO_03034"

    # partition coeffcient of follicle to skin surface depot
    PBPKO_03035 = "PBPKO_03035"
    PARTITION_COEFFCIENT_OF_FOLLICLE_TO_SKIN_SURFACE_DEPOT = "PBPKO_03035"

    # octanol water partition coefficient
    PBPKO_03036 = "PBPKO_03036"
    OCTANOL_WATER_PARTITION_COEFFICIENT = "PBPKO_03036"

    # medium polymer partition coefficient
    PBPKO_03037 = "PBPKO_03037"
    MEDIUM_POLYMER_PARTITION_COEFFICIENT = "PBPKO_03037"

    # medium air partition coefficient
    PBPKO_03038 = "PBPKO_03038"
    MEDIUM_AIR_PARTITION_COEFFICIENT = "PBPKO_03038"

    # medium mitochondria partition coefficient
    PBPKO_03039 = "PBPKO_03039"
    MEDIUM_MITOCHONDRIA_PARTITION_COEFFICIENT = "PBPKO_03039"

    # medium lysosomes partition coefficient
    PBPKO_03040 = "PBPKO_03040"
    MEDIUM_LYSOSOMES_PARTITION_COEFFICIENT = "PBPKO_03040"

    # medium intracellular water partition coefficient
    PBPKO_03041 = "PBPKO_03041"
    MEDIUM_INTRACELLULAR_WATER_PARTITION_COEFFICIENT = "PBPKO_03041"

    # medium microsomes partition coefficient
    PBPKO_03042 = "PBPKO_03042"
    MEDIUM_MICROSOMES_PARTITION_COEFFICIENT = "PBPKO_03042"

    # medium other organelles partition coefficient
    PBPKO_03043 = "PBPKO_03043"
    MEDIUM_OTHER_ORGANELLES_PARTITION_COEFFICIENT = "PBPKO_03043"

    # medium albumin partition coefficient
    PBPKO_03044 = "PBPKO_03044"
    MEDIUM_ALBUMIN_PARTITION_COEFFICIENT = "PBPKO_03044"

    # abiotic degradation rate in medium
    PBPKO_03045 = "PBPKO_03045"
    ABIOTIC_DEGRADATION_RATE_IN_MEDIUM = "PBPKO_03045"

    # acidic phospholipid association constant
    PBPKO_03046 = "PBPKO_03046"
    ACIDIC_PHOSPHOLIPID_ASSOCIATION_CONSTANT = "PBPKO_03046"

    # abiotic degradation rate in air
    PBPKO_03047 = "PBPKO_03047"
    ABIOTIC_DEGRADATION_RATE_IN_AIR = "PBPKO_03047"

    # maximum metabolic rate
    PBPKO_03048 = "PBPKO_03048"
    MAXIMUM_METABOLIC_RATE = "PBPKO_03048"

    # linear metabolic rate
    PBPKO_03049 = "PBPKO_03049"
    LINEAR_METABOLIC_RATE = "PBPKO_03049"

    # cell radius
    PBPKO_03050 = "PBPKO_03050"
    CELL_RADIUS = "PBPKO_03050"

    # cell replication time
    PBPKO_03051 = "PBPKO_03051"
    CELL_REPLICATION_TIME = "PBPKO_03051"

    # cell fraction of proteins
    PBPKO_03052 = "PBPKO_03052"
    CELL_FRACTION_OF_PROTEINS = "PBPKO_03052"

    # cell fraction of lipids
    PBPKO_03053 = "PBPKO_03053"
    CELL_FRACTION_OF_LIPIDS = "PBPKO_03053"

    # cell fraction of intracellular water
    PBPKO_03054 = "PBPKO_03054"
    CELL_FRACTION_OF_INTRACELLULAR_WATER = "PBPKO_03054"

    # cell fraction of mitochondria
    PBPKO_03055 = "PBPKO_03055"
    CELL_FRACTION_OF_MITOCHONDRIA = "PBPKO_03055"

    # cell fraction of lysosomes
    PBPKO_03056 = "PBPKO_03056"
    CELL_FRACTION_OF_LYSOSOMES = "PBPKO_03056"

    # cell fraction of microsomes
    PBPKO_03057 = "PBPKO_03057"
    CELL_FRACTION_OF_MICROSOMES = "PBPKO_03057"

    # fraction of neutral lipids in the FBS
    PBPKO_03058 = "PBPKO_03058"
    FRACTION_OF_NEUTRAL_LIPIDS_IN_THE_FBS = "PBPKO_03058"

    # fraction of albumin in the FBS
    PBPKO_03059 = "PBPKO_03059"
    FRACTION_OF_ALBUMIN_IN_THE_FBS = "PBPKO_03059"

    # culture area
    PBPKO_03060 = "PBPKO_03060"
    CULTURE_AREA = "PBPKO_03060"

    # top well diameter
    PBPKO_03061 = "PBPKO_03061"
    TOP_WELL_DIAMETER = "PBPKO_03061"

    # well depth
    PBPKO_03062 = "PBPKO_03062"
    WELL_DEPTH = "PBPKO_03062"

    # plate wall thickness
    PBPKO_03063 = "PBPKO_03063"
    PLATE_WALL_THICKNESS = "PBPKO_03063"

    # culture medium pH
    PBPKO_03064 = "PBPKO_03064"
    CULTURE_MEDIUM_PH = "PBPKO_03064"

    # fraction of serum in total media
    PBPKO_03065 = "PBPKO_03065"
    FRACTION_OF_SERUM_IN_TOTAL_MEDIA = "PBPKO_03065"

    # FBS pH
    PBPKO_03066 = "PBPKO_03066"
    FBS_PH = "PBPKO_03066"

    # initial number of cells
    PBPKO_03067 = "PBPKO_03067"
    INITIAL_NUMBER_OF_CELLS = "PBPKO_03067"

    # nominal concentration of medium
    PBPKO_03068 = "PBPKO_03068"
    NOMINAL_CONCENTRATION_OF_MEDIUM = "PBPKO_03068"

    # volume of medium
    PBPKO_03069 = "PBPKO_03069"
    VOLUME_OF_MEDIUM = "PBPKO_03069"

    # fraction of FBS iin the medium
    PBPKO_03070 = "PBPKO_03070"
    FRACTION_OF_FBS_IIN_THE_MEDIUM = "PBPKO_03070"

    # ionized fraction in the medium
    PBPKO_03071 = "PBPKO_03071"
    IONIZED_FRACTION_IN_THE_MEDIUM = "PBPKO_03071"

    # fraction unbound in the medium
    PBPKO_03072 = "PBPKO_03072"
    FRACTION_UNBOUND_IN_THE_MEDIUM = "PBPKO_03072"

    # fraction unbound in the FBS
    PBPKO_03073 = "PBPKO_03073"
    FRACTION_UNBOUND_IN_THE_FBS = "PBPKO_03073"

    # fraction unbound in the cell
    PBPKO_03074 = "PBPKO_03074"
    FRACTION_UNBOUND_IN_THE_CELL = "PBPKO_03074"

    # absorption rate constant
    PBPKO_03075 = "PBPKO_03075"
    ABSORPTION_RATE_CONSTANT = "PBPKO_03075"

    # fraction unbound kidney proximal tubule
    PBPKO_03076 = "PBPKO_03076"
    FRACTION_UNBOUND_KIDNEY_PROXIMAL_TUBULE = "PBPKO_03076"

    # plasma flow rate
    PBPKO_04001 = "PBPKO_04001"
    PLASMA_FLOW_RATE = "PBPKO_04001"

    # plasma flow rate to stomach
    PBPKO_04002 = "PBPKO_04002"
    PLASMA_FLOW_RATE_TO_STOMACH = "PBPKO_04002"

    # plasma flow rate to intestine
    PBPKO_04003 = "PBPKO_04003"
    PLASMA_FLOW_RATE_TO_INTESTINE = "PBPKO_04003"

    # plasma flow rate to small intestine
    PBPKO_04004 = "PBPKO_04004"
    PLASMA_FLOW_RATE_TO_SMALL_INTESTINE = "PBPKO_04004"

    # plasma flow rate to large intestine
    PBPKO_04005 = "PBPKO_04005"
    PLASMA_FLOW_RATE_TO_LARGE_INTESTINE = "PBPKO_04005"

    # plasma flow rate to pancreas
    PBPKO_04006 = "PBPKO_04006"
    PLASMA_FLOW_RATE_TO_PANCREAS = "PBPKO_04006"

    # plasma flow rate to liver
    PBPKO_04007 = "PBPKO_04007"
    PLASMA_FLOW_RATE_TO_LIVER = "PBPKO_04007"

    # plasma flow rate to kidney
    PBPKO_04008 = "PBPKO_04008"
    PLASMA_FLOW_RATE_TO_KIDNEY = "PBPKO_04008"

    # plasma flow rate to muscle
    PBPKO_04009 = "PBPKO_04009"
    PLASMA_FLOW_RATE_TO_MUSCLE = "PBPKO_04009"

    # plasma flow rate to heart
    PBPKO_04010 = "PBPKO_04010"
    PLASMA_FLOW_RATE_TO_HEART = "PBPKO_04010"

    # plasma flow rate to fat
    PBPKO_04011 = "PBPKO_04011"
    PLASMA_FLOW_RATE_TO_FAT = "PBPKO_04011"

    # plasma flow rate to gonad
    PBPKO_04012 = "PBPKO_04012"
    PLASMA_FLOW_RATE_TO_GONAD = "PBPKO_04012"

    # plasma flow rate to skin
    PBPKO_04013 = "PBPKO_04013"
    PLASMA_FLOW_RATE_TO_SKIN = "PBPKO_04013"

    # plasma flow rate to bone
    PBPKO_04014 = "PBPKO_04014"
    PLASMA_FLOW_RATE_TO_BONE = "PBPKO_04014"

    # plasma flow rate to brain
    PBPKO_04015 = "PBPKO_04015"
    PLASMA_FLOW_RATE_TO_BRAIN = "PBPKO_04015"

    # plasma flow rate to spleen
    PBPKO_04016 = "PBPKO_04016"
    PLASMA_FLOW_RATE_TO_SPLEEN = "PBPKO_04016"

    # plasma flow rate to lung
    PBPKO_04017 = "PBPKO_04017"
    PLASMA_FLOW_RATE_TO_LUNG = "PBPKO_04017"

    # plasma flow rate to poorly perfused
    PBPKO_04018 = "PBPKO_04018"
    PLASMA_FLOW_RATE_TO_POORLY_PERFUSED = "PBPKO_04018"

    # plasma flow rate to richly perfused
    PBPKO_04019 = "PBPKO_04019"
    PLASMA_FLOW_RATE_TO_RICHLY_PERFUSED = "PBPKO_04019"

    # plasma flow rate to restbody
    PBPKO_04020 = "PBPKO_04020"
    PLASMA_FLOW_RATE_TO_RESTBODY = "PBPKO_04020"

    # plasma flow rate to gall bladder
    PBPKO_04021 = "PBPKO_04021"
    PLASMA_FLOW_RATE_TO_GALL_BLADDER = "PBPKO_04021"

    # plasma flow rate to portal vein
    PBPKO_04022 = "PBPKO_04022"
    PLASMA_FLOW_RATE_TO_PORTAL_VEIN = "PBPKO_04022"

    # plasma flow rate to lymph
    PBPKO_04023 = "PBPKO_04023"
    PLASMA_FLOW_RATE_TO_LYMPH = "PBPKO_04023"

    # plasma flow rate to duodenum
    PBPKO_04024 = "PBPKO_04024"
    PLASMA_FLOW_RATE_TO_DUODENUM = "PBPKO_04024"

    # plasma flow rate to jejunum
    PBPKO_04025 = "PBPKO_04025"
    PLASMA_FLOW_RATE_TO_JEJUNUM = "PBPKO_04025"

    # plasma flow rate to ileum
    PBPKO_04026 = "PBPKO_04026"
    PLASMA_FLOW_RATE_TO_ILEUM = "PBPKO_04026"

    # plasma flow rate to colon
    PBPKO_04027 = "PBPKO_04027"
    PLASMA_FLOW_RATE_TO_COLON = "PBPKO_04027"

    # plasma flow rate to cecum
    PBPKO_04028 = "PBPKO_04028"
    PLASMA_FLOW_RATE_TO_CECUM = "PBPKO_04028"

    # plasma flow rate to filtrate
    PBPKO_04029 = "PBPKO_04029"
    PLASMA_FLOW_RATE_TO_FILTRATE = "PBPKO_04029"

    # plasma flow rate to bone marrow
    PBPKO_04030 = "PBPKO_04030"
    PLASMA_FLOW_RATE_TO_BONE_MARROW = "PBPKO_04030"

    # plasma flow rate to gut
    PBPKO_04031 = "PBPKO_04031"
    PLASMA_FLOW_RATE_TO_GUT = "PBPKO_04031"

    # plasma flow rate to mammary gland
    PBPKO_04032 = "PBPKO_04032"
    PLASMA_FLOW_RATE_TO_MAMMARY_GLAND = "PBPKO_04032"

    # plasma flow rate for mass balance
    PBPKO_04033 = "PBPKO_04033"
    PLASMA_FLOW_RATE_FOR_MASS_BALANCE = "PBPKO_04033"

    # plasma flow rate to unexposed skin
    PBPKO_04034 = "PBPKO_04034"
    PLASMA_FLOW_RATE_TO_UNEXPOSED_SKIN = "PBPKO_04034"

    # plasma flow rate to exposed skin
    PBPKO_04035 = "PBPKO_04035"
    PLASMA_FLOW_RATE_TO_EXPOSED_SKIN = "PBPKO_04035"

    # plasma flow rate to skin stratum corneum unexposed
    PBPKO_04036 = "PBPKO_04036"
    PLASMA_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_UNEXPOSED = "PBPKO_04036"

    # plasma flow rate to skin stratum corneum exposed
    PBPKO_04037 = "PBPKO_04037"
    PLASMA_FLOW_RATE_TO_SKIN_STRATUM_CORNEUM_EXPOSED = "PBPKO_04037"

    # fraction of blood flow to red blood cells
    PBPKO_04038 = "PBPKO_04038"
    FRACTION_OF_BLOOD_FLOW_TO_RED_BLOOD_CELLS = "PBPKO_04038"

    # blood flow rate to red blood cells
    PBPKO_04039 = "PBPKO_04039"
    BLOOD_FLOW_RATE_TO_RED_BLOOD_CELLS = "PBPKO_04039"

    # volumen of lumen
    PBPKO_04040 = "PBPKO_04040"
    VOLUMEN_OF_LUMEN = "PBPKO_04040"

    # volume of small intestine tissue
    PBPKO_04041 = "PBPKO_04041"
    VOLUME_OF_SMALL_INTESTINE_TISSUE = "PBPKO_04041"

    # volume of bile
    PBPKO_04042 = "PBPKO_04042"
    VOLUME_OF_BILE = "PBPKO_04042"

    # enterocyte volume
    PBPKO_04043 = "PBPKO_04043"
    ENTEROCYTE_VOLUME = "PBPKO_04043"

    # hepatic vein blood flow
    PBPKO_04044 = "PBPKO_04044"
    HEPATIC_VEIN_BLOOD_FLOW = "PBPKO_04044"

    # blood flow rate to bile
    PBPKO_04045 = "PBPKO_04045"
    BLOOD_FLOW_RATE_TO_BILE = "PBPKO_04045"

    # diameter of intestinal
    PBPKO_04046 = "PBPKO_04046"
    DIAMETER_OF_INTESTINAL = "PBPKO_04046"

    # diameter of the jejunum lumen
    PBPKO_04047 = "PBPKO_04047"
    DIAMETER_OF_THE_JEJUNUM_LUMEN = "PBPKO_04047"

    # diameter of the ileum lumen
    PBPKO_04048 = "PBPKO_04048"
    DIAMETER_OF_THE_ILEUM_LUMEN = "PBPKO_04048"

    # diameter of the large intestine lumen
    PBPKO_04049 = "PBPKO_04049"
    DIAMETER_OF_THE_LARGE_INTESTINE_LUMEN = "PBPKO_04049"

    # surface area  of the jejunum lumen
    PBPKO_04050 = "PBPKO_04050"
    SURFACE_AREA__OF_THE_JEJUNUM_LUMEN = "PBPKO_04050"

    # surface area of the ileum lumen
    PBPKO_04051 = "PBPKO_04051"
    SURFACE_AREA_OF_THE_ILEUM_LUMEN = "PBPKO_04051"

    # surface area of the large intestine lumen
    PBPKO_04052 = "PBPKO_04052"
    SURFACE_AREA_OF_THE_LARGE_INTESTINE_LUMEN = "PBPKO_04052"

    # uptake fraction to blood
    PBPKO_04053 = "PBPKO_04053"
    UPTAKE_FRACTION_TO_BLOOD = "PBPKO_04053"

    # fraction of bile in small intestine
    PBPKO_04054 = "PBPKO_04054"
    FRACTION_OF_BILE_IN_SMALL_INTESTINE = "PBPKO_04054"

    # fraction of bile in liver
    PBPKO_04055 = "PBPKO_04055"
    FRACTION_OF_BILE_IN_LIVER = "PBPKO_04055"

    # fraction of feces
    PBPKO_04056 = "PBPKO_04056"
    FRACTION_OF_FECES = "PBPKO_04056"

    # volume fraction of blood
    PBPKO_04057 = "PBPKO_04057"
    VOLUME_FRACTION_OF_BLOOD = "PBPKO_04057"

    # volume fraction of red blood cells
    PBPKO_04058 = "PBPKO_04058"
    VOLUME_FRACTION_OF_RED_BLOOD_CELLS = "PBPKO_04058"

    # skin area
    PBPKO_04059 = "PBPKO_04059"
    SKIN_AREA = "PBPKO_04059"

    # thickness epidermis
    PBPKO_04060 = "PBPKO_04060"
    THICKNESS_EPIDERMIS = "PBPKO_04060"

    # volume of exposed viable epidermis
    PBPKO_04061 = "PBPKO_04061"
    VOLUME_OF_EXPOSED_VIABLE_EPIDERMIS = "PBPKO_04061"

    # volume of follicle
    PBPKO_04062 = "PBPKO_04062"
    VOLUME_OF_FOLLICLE = "PBPKO_04062"

    # area of exposed skin
    PBPKO_04063 = "PBPKO_04063"
    AREA_OF_EXPOSED_SKIN = "PBPKO_04063"

    # volume of serum
    PBPKO_04064 = "PBPKO_04064"
    VOLUME_OF_SERUM = "PBPKO_04064"

    # volume of adrenals
    PBPKO_04065 = "PBPKO_04065"
    VOLUME_OF_ADRENALS = "PBPKO_04065"

    # volume of breast
    PBPKO_04066 = "PBPKO_04066"
    VOLUME_OF_BREAST = "PBPKO_04066"

    # volume of thyroid
    PBPKO_04067 = "PBPKO_04067"
    VOLUME_OF_THYROID = "PBPKO_04067"

    # volume of intestinal lumen
    PBPKO_04068 = "PBPKO_04068"
    VOLUME_OF_INTESTINAL_LUMEN = "PBPKO_04068"

    # volume of small intestinal lumen
    PBPKO_04069 = "PBPKO_04069"
    VOLUME_OF_SMALL_INTESTINAL_LUMEN = "PBPKO_04069"

    # volume of large intestinal lumen
    PBPKO_04070 = "PBPKO_04070"
    VOLUME_OF_LARGE_INTESTINAL_LUMEN = "PBPKO_04070"

    # volume of stomach lumen
    PBPKO_04071 = "PBPKO_04071"
    VOLUME_OF_STOMACH_LUMEN = "PBPKO_04071"

    # volume of gut intestinal tract
    PBPKO_04072 = "PBPKO_04072"
    VOLUME_OF_GUT_INTESTINAL_TRACT = "PBPKO_04072"

    # volume of testis
    PBPKO_04073 = "PBPKO_04073"
    VOLUME_OF_TESTIS = "PBPKO_04073"

    # volume of uterus
    PBPKO_04074 = "PBPKO_04074"
    VOLUME_OF_UTERUS = "PBPKO_04074"

    # volume of skeleton
    PBPKO_04075 = "PBPKO_04075"
    VOLUME_OF_SKELETON = "PBPKO_04075"

    # volume of hair
    PBPKO_04076 = "PBPKO_04076"
    VOLUME_OF_HAIR = "PBPKO_04076"

    # volume of urinary tract
    PBPKO_04077 = "PBPKO_04077"
    VOLUME_OF_URINARY_TRACT = "PBPKO_04077"

    # volume of skin surface depot
    PBPKO_04078 = "PBPKO_04078"
    VOLUME_OF_SKIN_SURFACE_DEPOT = "PBPKO_04078"

    # volume of cortical bone
    PBPKO_04079 = "PBPKO_04079"
    VOLUME_OF_CORTICAL_BONE = "PBPKO_04079"

    # volume of trabecular bone
    PBPKO_04080 = "PBPKO_04080"
    VOLUME_OF_TRABECULAR_BONE = "PBPKO_04080"

    # volume of alveolar compartment
    PBPKO_04081 = "PBPKO_04081"
    VOLUME_OF_ALVEOLAR_COMPARTMENT = "PBPKO_04081"

    # fraction of serum
    PBPKO_04082 = "PBPKO_04082"
    FRACTION_OF_SERUM = "PBPKO_04082"

    # fraction of adrenals
    PBPKO_04083 = "PBPKO_04083"
    FRACTION_OF_ADRENALS = "PBPKO_04083"

    # fraction of breast
    PBPKO_04084 = "PBPKO_04084"
    FRACTION_OF_BREAST = "PBPKO_04084"

    # fraction of thyroid
    PBPKO_04085 = "PBPKO_04085"
    FRACTION_OF_THYROID = "PBPKO_04085"

    # fraction of intestinal lumen
    PBPKO_04086 = "PBPKO_04086"
    FRACTION_OF_INTESTINAL_LUMEN = "PBPKO_04086"

    # fraction of small intestinal lumen
    PBPKO_04087 = "PBPKO_04087"
    FRACTION_OF_SMALL_INTESTINAL_LUMEN = "PBPKO_04087"

    # fraction of large intestinal lumen
    PBPKO_04088 = "PBPKO_04088"
    FRACTION_OF_LARGE_INTESTINAL_LUMEN = "PBPKO_04088"

    # fraction of stomach lumen
    PBPKO_04089 = "PBPKO_04089"
    FRACTION_OF_STOMACH_LUMEN = "PBPKO_04089"

    # fraction of gut intestinal tract
    PBPKO_04090 = "PBPKO_04090"
    FRACTION_OF_GUT_INTESTINAL_TRACT = "PBPKO_04090"

    # fraction of testis
    PBPKO_04091 = "PBPKO_04091"
    FRACTION_OF_TESTIS = "PBPKO_04091"

    # fraction of uterus
    PBPKO_04092 = "PBPKO_04092"
    FRACTION_OF_UTERUS = "PBPKO_04092"

    # fraction of skeleton
    PBPKO_04093 = "PBPKO_04093"
    FRACTION_OF_SKELETON = "PBPKO_04093"

    # fraction of hair
    PBPKO_04094 = "PBPKO_04094"
    FRACTION_OF_HAIR = "PBPKO_04094"

    # fraction of amniotic fluid
    PBPKO_04095 = "PBPKO_04095"
    FRACTION_OF_AMNIOTIC_FLUID = "PBPKO_04095"

    # fraction of urinary tract
    PBPKO_04096 = "PBPKO_04096"
    FRACTION_OF_URINARY_TRACT = "PBPKO_04096"

    # fraction of cortical bone
    PBPKO_04097 = "PBPKO_04097"
    FRACTION_OF_CORTICAL_BONE = "PBPKO_04097"

    # fraction of trabecular bone
    PBPKO_04098 = "PBPKO_04098"
    FRACTION_OF_TRABECULAR_BONE = "PBPKO_04098"

    # fraction of the skin surface depot
    PBPKO_04099 = "PBPKO_04099"
    FRACTION_OF_THE_SKIN_SURFACE_DEPOT = "PBPKO_04099"

    # fraction of blood
    PBPKO_04100 = "PBPKO_04100"
    FRACTION_OF_BLOOD = "PBPKO_04100"

    # fraction of bone marrow
    PBPKO_04101 = "PBPKO_04101"
    FRACTION_OF_BONE_MARROW = "PBPKO_04101"

    # fraction of bone non perfused
    PBPKO_04102 = "PBPKO_04102"
    FRACTION_OF_BONE_NON_PERFUSED = "PBPKO_04102"

    # fraction of adipose mass
    PBPKO_04103 = "PBPKO_04103"
    FRACTION_OF_ADIPOSE_MASS = "PBPKO_04103"

    # fraction of intestinal tissue
    PBPKO_04104 = "PBPKO_04104"
    FRACTION_OF_INTESTINAL_TISSUE = "PBPKO_04104"

    # volume of kidney rest tissue
    PBPKO_04105 = "PBPKO_04105"
    VOLUME_OF_KIDNEY_REST_TISSUE = "PBPKO_04105"

    # volume of kidney rest lumen
    PBPKO_04106 = "PBPKO_04106"
    VOLUME_OF_KIDNEY_REST_LUMEN = "PBPKO_04106"

    # volume of kidney proximal tubule lumen
    PBPKO_04107 = "PBPKO_04107"
    VOLUME_OF_KIDNEY_PROXIMAL_TUBULE_LUMEN = "PBPKO_04107"

    # volume of kidney proximal tubule tissue
    PBPKO_04108 = "PBPKO_04108"
    VOLUME_OF_KIDNEY_PROXIMAL_TUBULE_TISSUE = "PBPKO_04108"

    # volume of liver extracellular
    PBPKO_04109 = "PBPKO_04109"
    VOLUME_OF_LIVER_EXTRACELLULAR = "PBPKO_04109"

    # volume of liver intracellular space
    PBPKO_04110 = "PBPKO_04110"
    VOLUME_OF_LIVER_INTRACELLULAR_SPACE = "PBPKO_04110"

    # volume of intestine tissue
    PBPKO_04111 = "PBPKO_04111"
    VOLUME_OF_INTESTINE_TISSUE = "PBPKO_04111"

    # molar volume
    PBPKO_05001 = "PBPKO_05001"
    MOLAR_VOLUME = "PBPKO_05001"

    # Henry's law constant
    PBPKO_05002 = "PBPKO_05002"
    HENRY_S_LAW_CONSTANT = "PBPKO_05002"

    # vapor pressure
    PBPKO_05003 = "PBPKO_05003"
    VAPOR_PRESSURE = "PBPKO_05003"

    # unbound venous concentration of compound in compartment
    PBPKO_06002 = "PBPKO_06002"
    UNBOUND_VENOUS_CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT = "PBPKO_06002"

    # unbound concentration of compund in compartment
    PBPKO_06003 = "PBPKO_06003"
    UNBOUND_CONCENTRATION_OF_COMPUND_IN_COMPARTMENT = "PBPKO_06003"

    # amount in stomach
    PBPKO_06004 = "PBPKO_06004"
    AMOUNT_IN_STOMACH = "PBPKO_06004"

    # amount in small intestine
    PBPKO_06005 = "PBPKO_06005"
    AMOUNT_IN_SMALL_INTESTINE = "PBPKO_06005"

    # amount in jejunum
    PBPKO_06006 = "PBPKO_06006"
    AMOUNT_IN_JEJUNUM = "PBPKO_06006"

    # amount in ileum
    PBPKO_06007 = "PBPKO_06007"
    AMOUNT_IN_ILEUM = "PBPKO_06007"

    # amount in  large intestine
    PBPKO_06008 = "PBPKO_06008"
    AMOUNT_IN__LARGE_INTESTINE = "PBPKO_06008"

    # amount in lumen
    PBPKO_06009 = "PBPKO_06009"
    AMOUNT_IN_LUMEN = "PBPKO_06009"

    # amount in small intestine segment
    PBPKO_06010 = "PBPKO_06010"
    AMOUNT_IN_SMALL_INTESTINE_SEGMENT = "PBPKO_06010"

    # amount in colon
    PBPKO_06011 = "PBPKO_06011"
    AMOUNT_IN_COLON = "PBPKO_06011"

    # amount in bile
    PBPKO_06012 = "PBPKO_06012"
    AMOUNT_IN_BILE = "PBPKO_06012"

    # amount in spleen
    PBPKO_06013 = "PBPKO_06013"
    AMOUNT_IN_SPLEEN = "PBPKO_06013"

    # amount in duodenum
    PBPKO_06014 = "PBPKO_06014"
    AMOUNT_IN_DUODENUM = "PBPKO_06014"

    # amount in intestinal tissue
    PBPKO_06015 = "PBPKO_06015"
    AMOUNT_IN_INTESTINAL_TISSUE = "PBPKO_06015"

    # amount in portal vein
    PBPKO_06016 = "PBPKO_06016"
    AMOUNT_IN_PORTAL_VEIN = "PBPKO_06016"

    # unbound concentration in plasma
    PBPKO_06017 = "PBPKO_06017"
    UNBOUND_CONCENTRATION_IN_PLASMA = "PBPKO_06017"

    # unbound venous liver concentration
    PBPKO_06018 = "PBPKO_06018"
    UNBOUND_VENOUS_LIVER_CONCENTRATION = "PBPKO_06018"

    # unbound venous gut concentration
    PBPKO_06019 = "PBPKO_06019"
    UNBOUND_VENOUS_GUT_CONCENTRATION = "PBPKO_06019"

    # unbound venous brain concentration
    PBPKO_06020 = "PBPKO_06020"
    UNBOUND_VENOUS_BRAIN_CONCENTRATION = "PBPKO_06020"

    # unbound venous kidney concentration
    PBPKO_06021 = "PBPKO_06021"
    UNBOUND_VENOUS_KIDNEY_CONCENTRATION = "PBPKO_06021"

    # unbound venous filtrate concentration
    PBPKO_06022 = "PBPKO_06022"
    UNBOUND_VENOUS_FILTRATE_CONCENTRATION = "PBPKO_06022"

    # unbound venous lung concentration
    PBPKO_06023 = "PBPKO_06023"
    UNBOUND_VENOUS_LUNG_CONCENTRATION = "PBPKO_06023"

    # unbound venous fat concentration
    PBPKO_06024 = "PBPKO_06024"
    UNBOUND_VENOUS_FAT_CONCENTRATION = "PBPKO_06024"

    # unbound venous bone marrow concentration
    PBPKO_06025 = "PBPKO_06025"
    UNBOUND_VENOUS_BONE_MARROW_CONCENTRATION = "PBPKO_06025"

    # unbound venous skin concentration
    PBPKO_06026 = "PBPKO_06026"
    UNBOUND_VENOUS_SKIN_CONCENTRATION = "PBPKO_06026"

    # unbound venous mammary gland concentration
    PBPKO_06027 = "PBPKO_06027"
    UNBOUND_VENOUS_MAMMARY_GLAND_CONCENTRATION = "PBPKO_06027"

    # unbound venous rest body concentration
    PBPKO_06028 = "PBPKO_06028"
    UNBOUND_VENOUS_REST_BODY_CONCENTRATION = "PBPKO_06028"

    # total venous concentration of compound in compartment
    PBPKO_06029 = "PBPKO_06029"
    TOTAL_VENOUS_CONCENTRATION_OF_COMPOUND_IN_COMPARTMENT = "PBPKO_06029"

    # total venous liver concentration
    PBPKO_06030 = "PBPKO_06030"
    TOTAL_VENOUS_LIVER_CONCENTRATION = "PBPKO_06030"

    # total venous gut concentration
    PBPKO_06031 = "PBPKO_06031"
    TOTAL_VENOUS_GUT_CONCENTRATION = "PBPKO_06031"

    # total venous kidney concentration
    PBPKO_06032 = "PBPKO_06032"
    TOTAL_VENOUS_KIDNEY_CONCENTRATION = "PBPKO_06032"

    # total venous brain concentration
    PBPKO_06033 = "PBPKO_06033"
    TOTAL_VENOUS_BRAIN_CONCENTRATION = "PBPKO_06033"

    # total venous filtrate concentration
    PBPKO_06034 = "PBPKO_06034"
    TOTAL_VENOUS_FILTRATE_CONCENTRATION = "PBPKO_06034"

    # total venous lung concentration
    PBPKO_06035 = "PBPKO_06035"
    TOTAL_VENOUS_LUNG_CONCENTRATION = "PBPKO_06035"

    # total venous fat concentration
    PBPKO_06036 = "PBPKO_06036"
    TOTAL_VENOUS_FAT_CONCENTRATION = "PBPKO_06036"

    # total venous bone marrow concentration
    PBPKO_06037 = "PBPKO_06037"
    TOTAL_VENOUS_BONE_MARROW_CONCENTRATION = "PBPKO_06037"

    # total venous skin concentration
    PBPKO_06038 = "PBPKO_06038"
    TOTAL_VENOUS_SKIN_CONCENTRATION = "PBPKO_06038"

    # total venous mammary gland concentration
    PBPKO_06039 = "PBPKO_06039"
    TOTAL_VENOUS_MAMMARY_GLAND_CONCENTRATION = "PBPKO_06039"

    # total venous rest body concentration
    PBPKO_06040 = "PBPKO_06040"
    TOTAL_VENOUS_REST_BODY_CONCENTRATION = "PBPKO_06040"

    # concentration in stomach
    PBPKO_06041 = "PBPKO_06041"
    CONCENTRATION_IN_STOMACH = "PBPKO_06041"

    # concentration in small intestine
    PBPKO_06042 = "PBPKO_06042"
    CONCENTRATION_IN_SMALL_INTESTINE = "PBPKO_06042"

    # concentration in jejunum
    PBPKO_06043 = "PBPKO_06043"
    CONCENTRATION_IN_JEJUNUM = "PBPKO_06043"

    # concentration in ileum
    PBPKO_06044 = "PBPKO_06044"
    CONCENTRATION_IN_ILEUM = "PBPKO_06044"

    # concentration in large intestine
    PBPKO_06045 = "PBPKO_06045"
    CONCENTRATION_IN_LARGE_INTESTINE = "PBPKO_06045"

    # concentration in intestinal tissue
    PBPKO_06046 = "PBPKO_06046"
    CONCENTRATION_IN_INTESTINAL_TISSUE = "PBPKO_06046"

    # concentration in lumen
    PBPKO_06047 = "PBPKO_06047"
    CONCENTRATION_IN_LUMEN = "PBPKO_06047"

    # concentration in bile
    PBPKO_06048 = "PBPKO_06048"
    CONCENTRATION_IN_BILE = "PBPKO_06048"

    # concentration in spleen
    PBPKO_06049 = "PBPKO_06049"
    CONCENTRATION_IN_SPLEEN = "PBPKO_06049"

    # concentration in feces
    PBPKO_06050 = "PBPKO_06050"
    CONCENTRATION_IN_FECES = "PBPKO_06050"

    # amount in skin surface depot
    PBPKO_06051 = "PBPKO_06051"
    AMOUNT_IN_SKIN_SURFACE_DEPOT = "PBPKO_06051"

    # maximum amount
    PBPKO_06052 = "PBPKO_06052"
    MAXIMUM_AMOUNT = "PBPKO_06052"

    # amount in follicles
    PBPKO_06053 = "PBPKO_06053"
    AMOUNT_IN_FOLLICLES = "PBPKO_06053"

    # concentration in medium
    PBPKO_06054 = "PBPKO_06054"
    CONCENTRATION_IN_MEDIUM = "PBPKO_06054"

    # concentration in cell
    PBPKO_06055 = "PBPKO_06055"
    CONCENTRATION_IN_CELL = "PBPKO_06055"

    # concentration in mitochondria
    PBPKO_06056 = "PBPKO_06056"
    CONCENTRATION_IN_MITOCHONDRIA = "PBPKO_06056"

    # concentration in lysosomes
    PBPKO_06057 = "PBPKO_06057"
    CONCENTRATION_IN_LYSOSOMES = "PBPKO_06057"

    # concentration in microsomes
    PBPKO_06058 = "PBPKO_06058"
    CONCENTRATION_IN_MICROSOMES = "PBPKO_06058"

    # concentration in intracellular water
    PBPKO_06059 = "PBPKO_06059"
    CONCENTRATION_IN_INTRACELLULAR_WATER = "PBPKO_06059"

    # concentration in polymer
    PBPKO_06060 = "PBPKO_06060"
    CONCENTRATION_IN_POLYMER = "PBPKO_06060"

    # concentration in air
    PBPKO_06061 = "PBPKO_06061"
    CONCENTRATION_IN_AIR = "PBPKO_06061"

    # amount in menstrual
    PBPKO_06062 = "PBPKO_06062"
    AMOUNT_IN_MENSTRUAL = "PBPKO_06062"

    # amount in kidney rest tissue
    PBPKO_06063 = "PBPKO_06063"
    AMOUNT_IN_KIDNEY_REST_TISSUE = "PBPKO_06063"

    # amount in kidney rest lumen
    PBPKO_06064 = "PBPKO_06064"
    AMOUNT_IN_KIDNEY_REST_LUMEN = "PBPKO_06064"

    # amount in kidney proximal tubule tissue
    PBPKO_06065 = "PBPKO_06065"
    AMOUNT_IN_KIDNEY_PROXIMAL_TUBULE_TISSUE = "PBPKO_06065"

    # amount in kidney proximal tubule lumen
    PBPKO_06066 = "PBPKO_06066"
    AMOUNT_IN_KIDNEY_PROXIMAL_TUBULE_LUMEN = "PBPKO_06066"

    # amount in liver intracellular
    PBPKO_06067 = "PBPKO_06067"
    AMOUNT_IN_LIVER_INTRACELLULAR = "PBPKO_06067"

    # amount in liver extracellular
    PBPKO_06068 = "PBPKO_06068"
    AMOUNT_IN_LIVER_EXTRACELLULAR = "PBPKO_06068"

    # invitro pbpk
    PBPKO_07001 = "PBPKO_07001"
    INVITRO_PBPK = "PBPKO_07001"

    # protein
    PR_000000001 = "PR_000000001"
    PROTEIN = "PR_000000001"

    # amino acid chain
    PR_000018263 = "PR_000018263"
    AMINO_ACID_CHAIN = "PR_000018263"

    # characteristic of
    RO_0000052 = "RO_0000052"
    CHARACTERISTIC_OF = "RO_0000052"

    # has characteristic
    RO_0000053 = "RO_0000053"
    HAS_CHARACTERISTIC = "RO_0000053"

    # participates in
    RO_0000056 = "RO_0000056"
    PARTICIPATES_IN = "RO_0000056"

    # has participant
    RO_0000057 = "RO_0000057"
    HAS_PARTICIPANT = "RO_0000057"

    # concretizes
    RO_0000059 = "RO_0000059"
    CONCRETIZES = "RO_0000059"

    # function of
    RO_0000079 = "RO_0000079"
    FUNCTION_OF = "RO_0000079"

    # quality of
    RO_0000080 = "RO_0000080"
    QUALITY_OF = "RO_0000080"

    # role of
    RO_0000081 = "RO_0000081"
    ROLE_OF = "RO_0000081"

    # has function
    RO_0000085 = "RO_0000085"
    HAS_FUNCTION = "RO_0000085"

    # has quality
    RO_0000086 = "RO_0000086"
    HAS_QUALITY = "RO_0000086"

    # has role
    RO_0000087 = "RO_0000087"
    HAS_ROLE = "RO_0000087"

    # has disposition
    RO_0000091 = "RO_0000091"
    HAS_DISPOSITION = "RO_0000091"

    # disposition of
    RO_0000092 = "RO_0000092"
    DISPOSITION_OF = "RO_0000092"

    # has regulatory component activity
    RO_0002013 = "RO_0002013"
    HAS_REGULATORY_COMPONENT_ACTIVITY = "RO_0002013"

    # has negative regulatory component activity
    RO_0002014 = "RO_0002014"
    HAS_NEGATIVE_REGULATORY_COMPONENT_ACTIVITY = "RO_0002014"

    # has positive regulatory component activity
    RO_0002015 = "RO_0002015"
    HAS_POSITIVE_REGULATORY_COMPONENT_ACTIVITY = "RO_0002015"

    # has component activity
    RO_0002017 = "RO_0002017"
    HAS_COMPONENT_ACTIVITY = "RO_0002017"

    # has component process
    RO_0002018 = "RO_0002018"
    HAS_COMPONENT_PROCESS = "RO_0002018"

    # directly regulated by
    RO_0002022 = "RO_0002022"
    DIRECTLY_REGULATED_BY = "RO_0002022"

    # directly negatively regulated by
    RO_0002023 = "RO_0002023"
    DIRECTLY_NEGATIVELY_REGULATED_BY = "RO_0002023"

    # directly positively regulated by
    RO_0002024 = "RO_0002024"
    DIRECTLY_POSITIVELY_REGULATED_BY = "RO_0002024"

    # has effector activity
    RO_0002025 = "RO_0002025"
    HAS_EFFECTOR_ACTIVITY = "RO_0002025"

    # ends after
    RO_0002086 = "RO_0002086"
    ENDS_AFTER = "RO_0002086"

    # immediately preceded by
    RO_0002087 = "RO_0002087"
    IMMEDIATELY_PRECEDED_BY = "RO_0002087"

    # immediately precedes
    RO_0002090 = "RO_0002090"
    IMMEDIATELY_PRECEDES = "RO_0002090"

    # overlaps
    RO_0002131 = "RO_0002131"
    OVERLAPS = "RO_0002131"

    # has component
    RO_0002180 = "RO_0002180"
    HAS_COMPONENT = "RO_0002180"

    # regulates
    RO_0002211 = "RO_0002211"
    REGULATES = "RO_0002211"

    # negatively regulates
    RO_0002212 = "RO_0002212"
    NEGATIVELY_REGULATES = "RO_0002212"

    # positively regulates
    RO_0002213 = "RO_0002213"
    POSITIVELY_REGULATES = "RO_0002213"

    # capable of
    RO_0002215 = "RO_0002215"
    CAPABLE_OF = "RO_0002215"

    # capable of part of
    RO_0002216 = "RO_0002216"
    CAPABLE_OF_PART_OF = "RO_0002216"

    # temporally related to
    RO_0002222 = "RO_0002222"
    TEMPORALLY_RELATED_TO = "RO_0002222"

    # has input
    RO_0002233 = "RO_0002233"
    HAS_INPUT = "RO_0002233"

    # acts upstream of
    RO_0002263 = "RO_0002263"
    ACTS_UPSTREAM_OF = "RO_0002263"

    # acts upstream of or within
    RO_0002264 = "RO_0002264"
    ACTS_UPSTREAM_OF_OR_WITHIN = "RO_0002264"

    # causally upstream of, positive effect
    RO_0002304 = "RO_0002304"
    CAUSALLY_UPSTREAM_OF__POSITIVE_EFFECT = "RO_0002304"

    # causally upstream of, negative effect
    RO_0002305 = "RO_0002305"
    CAUSALLY_UPSTREAM_OF__NEGATIVE_EFFECT = "RO_0002305"

    # characteristic of part of
    RO_0002314 = "RO_0002314"
    CHARACTERISTIC_OF_PART_OF = "RO_0002314"

    # mereotopologically related to
    RO_0002323 = "RO_0002323"
    MEREOTOPOLOGICALLY_RELATED_TO = "RO_0002323"

    # enables
    RO_0002327 = "RO_0002327"
    ENABLES = "RO_0002327"

    # functionally related to
    RO_0002328 = "RO_0002328"
    FUNCTIONALLY_RELATED_TO = "RO_0002328"

    # part of structure that is capable of
    RO_0002329 = "RO_0002329"
    PART_OF_STRUCTURE_THAT_IS_CAPABLE_OF = "RO_0002329"

    # involved in
    RO_0002331 = "RO_0002331"
    INVOLVED_IN = "RO_0002331"

    # enabled by
    RO_0002333 = "RO_0002333"
    ENABLED_BY = "RO_0002333"

    # regulated by
    RO_0002334 = "RO_0002334"
    REGULATED_BY = "RO_0002334"

    # negatively regulated by
    RO_0002335 = "RO_0002335"
    NEGATIVELY_REGULATED_BY = "RO_0002335"

    # positively regulated by
    RO_0002336 = "RO_0002336"
    POSITIVELY_REGULATED_BY = "RO_0002336"

    # has member
    RO_0002351 = "RO_0002351"
    HAS_MEMBER = "RO_0002351"

    # input of
    RO_0002352 = "RO_0002352"
    INPUT_OF = "RO_0002352"

    # causally downstream of
    RO_0002404 = "RO_0002404"
    CAUSALLY_DOWNSTREAM_OF = "RO_0002404"

    # immediately causally downstream of
    RO_0002405 = "RO_0002405"
    IMMEDIATELY_CAUSALLY_DOWNSTREAM_OF = "RO_0002405"

    # indirectly positively regulates
    RO_0002407 = "RO_0002407"
    INDIRECTLY_POSITIVELY_REGULATES = "RO_0002407"

    # indirectly negatively regulates
    RO_0002409 = "RO_0002409"
    INDIRECTLY_NEGATIVELY_REGULATES = "RO_0002409"

    # causally related to
    RO_0002410 = "RO_0002410"
    CAUSALLY_RELATED_TO = "RO_0002410"

    # causally upstream of
    RO_0002411 = "RO_0002411"
    CAUSALLY_UPSTREAM_OF = "RO_0002411"

    # immediately causally upstream of
    RO_0002412 = "RO_0002412"
    IMMEDIATELY_CAUSALLY_UPSTREAM_OF = "RO_0002412"

    # causally upstream of or within
    RO_0002418 = "RO_0002418"
    CAUSALLY_UPSTREAM_OF_OR_WITHIN = "RO_0002418"

    # causally downstream of or within
    RO_0002427 = "RO_0002427"
    CAUSALLY_DOWNSTREAM_OF_OR_WITHIN = "RO_0002427"

    # involved in regulation of
    RO_0002428 = "RO_0002428"
    INVOLVED_IN_REGULATION_OF = "RO_0002428"

    # involved in positive regulation of
    RO_0002429 = "RO_0002429"
    INVOLVED_IN_POSITIVE_REGULATION_OF = "RO_0002429"

    # involved in negative regulation of
    RO_0002430 = "RO_0002430"
    INVOLVED_IN_NEGATIVE_REGULATION_OF = "RO_0002430"

    # involved in or involved in regulation of
    RO_0002431 = "RO_0002431"
    INVOLVED_IN_OR_INVOLVED_IN_REGULATION_OF = "RO_0002431"

    # interacts with
    RO_0002434 = "RO_0002434"
    INTERACTS_WITH = "RO_0002434"

    # molecularly interacts with
    RO_0002436 = "RO_0002436"
    MOLECULARLY_INTERACTS_WITH = "RO_0002436"

    # phosphorylates
    RO_0002447 = "RO_0002447"
    PHOSPHORYLATES = "RO_0002447"

    # directly regulates activity of
    RO_0002448 = "RO_0002448"
    DIRECTLY_REGULATES_ACTIVITY_OF = "RO_0002448"

    # directly negatively regulates activity of
    RO_0002449 = "RO_0002449"
    DIRECTLY_NEGATIVELY_REGULATES_ACTIVITY_OF = "RO_0002449"

    # directly positively regulates activity of
    RO_0002450 = "RO_0002450"
    DIRECTLY_POSITIVELY_REGULATES_ACTIVITY_OF = "RO_0002450"

    # helper property (not for use in curation)
    RO_0002464 = "RO_0002464"
    HELPER_PROPERTY__NOT_FOR_USE_IN_CURATION_ = "RO_0002464"

    # is kinase activity
    RO_0002481 = "RO_0002481"
    IS_KINASE_ACTIVITY = "RO_0002481"

    # causal agent in process
    RO_0002500 = "RO_0002500"
    CAUSAL_AGENT_IN_PROCESS = "RO_0002500"

    # causal relation between processes
    RO_0002501 = "RO_0002501"
    CAUSAL_RELATION_BETWEEN_PROCESSES = "RO_0002501"

    # depends on
    RO_0002502 = "RO_0002502"
    DEPENDS_ON = "RO_0002502"

    # causal relation between entities
    RO_0002506 = "RO_0002506"
    CAUSAL_RELATION_BETWEEN_ENTITIES = "RO_0002506"

    # causally influenced by
    RO_0002559 = "RO_0002559"
    CAUSALLY_INFLUENCED_BY = "RO_0002559"

    # interaction relation helper property
    RO_0002563 = "RO_0002563"
    INTERACTION_RELATION_HELPER_PROPERTY = "RO_0002563"

    # molecular interaction relation helper property
    RO_0002564 = "RO_0002564"
    MOLECULAR_INTERACTION_RELATION_HELPER_PROPERTY = "RO_0002564"

    # causally influences
    RO_0002566 = "RO_0002566"
    CAUSALLY_INFLUENCES = "RO_0002566"

    # directly regulates
    RO_0002578 = "RO_0002578"
    DIRECTLY_REGULATES = "RO_0002578"

    # has part structure that is capable of
    RO_0002584 = "RO_0002584"
    HAS_PART_STRUCTURE_THAT_IS_CAPABLE_OF = "RO_0002584"

    # causal relation between material entity and a process
    RO_0002595 = "RO_0002595"
    CAUSAL_RELATION_BETWEEN_MATERIAL_ENTITY_AND_A_PROCESS = "RO_0002595"

    # capable of regulating
    RO_0002596 = "RO_0002596"
    CAPABLE_OF_REGULATING = "RO_0002596"

    # capable of negatively regulating
    RO_0002597 = "RO_0002597"
    CAPABLE_OF_NEGATIVELY_REGULATING = "RO_0002597"

    # capable of positively regulating
    RO_0002598 = "RO_0002598"
    CAPABLE_OF_POSITIVELY_REGULATING = "RO_0002598"

    # process has causal agent
    RO_0002608 = "RO_0002608"
    PROCESS_HAS_CAUSAL_AGENT = "RO_0002608"

    # directly positively regulates
    RO_0002629 = "RO_0002629"
    DIRECTLY_POSITIVELY_REGULATES = "RO_0002629"

    # directly negatively regulates
    RO_0002630 = "RO_0002630"
    DIRECTLY_NEGATIVELY_REGULATES = "RO_0002630"

    # enables subfunction
    RO_0004031 = "RO_0004031"
    ENABLES_SUBFUNCTION = "RO_0004031"

    # acts upstream of or within, positive effect
    RO_0004032 = "RO_0004032"
    ACTS_UPSTREAM_OF_OR_WITHIN__POSITIVE_EFFECT = "RO_0004032"

    # acts upstream of or within, negative effect
    RO_0004033 = "RO_0004033"
    ACTS_UPSTREAM_OF_OR_WITHIN__NEGATIVE_EFFECT = "RO_0004033"

    # acts upstream of, positive effect
    RO_0004034 = "RO_0004034"
    ACTS_UPSTREAM_OF__POSITIVE_EFFECT = "RO_0004034"

    # acts upstream of, negative effect
    RO_0004035 = "RO_0004035"
    ACTS_UPSTREAM_OF__NEGATIVE_EFFECT = "RO_0004035"

    # causally upstream of or within, negative effect
    RO_0004046 = "RO_0004046"
    CAUSALLY_UPSTREAM_OF_OR_WITHIN__NEGATIVE_EFFECT = "RO_0004046"

    # causally upstream of or within, positive effect
    RO_0004047 = "RO_0004047"
    CAUSALLY_UPSTREAM_OF_OR_WITHIN__POSITIVE_EFFECT = "RO_0004047"

    # regulates activity of
    RO_0011002 = "RO_0011002"
    REGULATES_ACTIVITY_OF = "RO_0011002"

    # indirectly causally upstream of
    RO_0012011 = "RO_0012011"
    INDIRECTLY_CAUSALLY_UPSTREAM_OF = "RO_0012011"

    # indirectly regulates
    RO_0012012 = "RO_0012012"
    INDIRECTLY_REGULATES = "RO_0012012"

    # device utilizes material
    RO_0017001 = "RO_0017001"
    DEVICE_UTILIZES_MATERIAL = "RO_0017001"

    # regulates characteristic
    RO_0019000 = "RO_0019000"
    REGULATES_CHARACTERISTIC = "RO_0019000"

    # positively regulates characteristic
    RO_0019001 = "RO_0019001"
    POSITIVELY_REGULATES_CHARACTERISTIC = "RO_0019001"

    # negatively regulates characteristic
    RO_0019002 = "RO_0019002"
    NEGATIVELY_REGULATES_CHARACTERISTIC = "RO_0019002"

    # material anatomical entity
    UBERON_0000465 = "UBERON_0000465"
    MATERIAL_ANATOMICAL_ENTITY = "UBERON_0000465"

    # immaterial anatomical entity
    UBERON_0000466 = "UBERON_0000466"
    IMMATERIAL_ANATOMICAL_ENTITY = "UBERON_0000466"

    # anatomical cluster
    UBERON_0000477 = "UBERON_0000477"
    ANATOMICAL_CLUSTER = "UBERON_0000477"

    # anatomical entity
    UBERON_0001062 = "UBERON_0001062"
    ANATOMICAL_ENTITY = "UBERON_0001062"

    # length unit
    UO_0000001 = "UO_0000001"
    LENGTH_UNIT = "UO_0000001"

    # mass unit
    UO_0000002 = "UO_0000002"
    MASS_UNIT = "UO_0000002"

    # time unit
    UO_0000003 = "UO_0000003"
    TIME_UNIT = "UO_0000003"

    # temperature unit
    UO_0000005 = "UO_0000005"
    TEMPERATURE_UNIT = "UO_0000005"

    # substance unit
    UO_0000006 = "UO_0000006"
    SUBSTANCE_UNIT = "UO_0000006"

    # concentration unit
    UO_0000051 = "UO_0000051"
    CONCENTRATION_UNIT = "UO_0000051"

    # volume unit
    UO_0000095 = "UO_0000095"
    VOLUME_UNIT = "UO_0000095"

    # frequency unit
    UO_0000105 = "UO_0000105"
    FREQUENCY_UNIT = "UO_0000105"

    # volumetric flow rate unit
    UO_0000270 = "UO_0000270"
    VOLUMETRIC_FLOW_RATE_UNIT = "UO_0000270"

    # rate unit
    UO_0000280 = "UO_0000280"
    RATE_UNIT = "UO_0000280"


PBPKOType = str | PBPKO

#: information of every term, assigned to the enum below
_terms: dict[str, TermData] = {
    "BFO_0000001": ("entity", None, (), False),
    "BFO_0000002": (
        "continuant",
        "An entity that exists in full at any time in which it exists at all, persists through time while maintaining its identity and has no temporal parts.",
        (),
        False,
    ),
    "BFO_0000003": (
        "occurrent",
        "An entity that has temporal parts and that happens, unfolds or develops through time.",
        (),
        False,
    ),
    "BFO_0000004": (
        "independent continuant",
        "b is an independent continuant = Def. b is a continuant which is such that there is no c and no t such that b s-depends_on c at t. (axiom label in BFO2 Reference: [017-002])",
        (),
        False,
    ),
    "BFO_0000015": (
        "process",
        "p is a process = Def. p is an occurrent that has temporal proper parts and for some time t, p s-depends_on some material entity at t. (axiom label in BFO2 Reference: [083-003])",
        (),
        False,
    ),
    "BFO_0000016": ("disposition", None, (), False),
    "BFO_0000017": (
        "realizable entity",
        "A specifically dependent continuant that inheres in continuant entities and are not exhibited in full at every time in which it inheres in an entity or group of entities. The exhibition or actualization of a realizable entity is a particular manifestation, functioning or process that occurs under certain circumstances.",
        (),
        False,
    ),
    "BFO_0000019": ("quality", None, (), False),
    "BFO_0000020": (
        "specifically dependent continuant",
        "b is a specifically dependent continuant = Def. b is a continuant & there is some independent continuant c which is not a spatial region and which is such that b s-depends_on c at every time t during the course of b’s existence. (axiom label in BFO2 Reference: [050-003])",
        (),
        False,
    ),
    "BFO_0000023": (
        "role",
        "A realizable entity the manifestation of which brings about some result or end that is not essential to a continuant in virtue of the kind of thing that it is but that can be served or participated in by that kind of continuant in some kinds of natural, social or institutional contexts.",
        (),
        False,
    ),
    "BFO_0000029": ("site", None, (), False),
    "BFO_0000031": ("generically dependent continuant", None, (), False),
    "BFO_0000034": ("function", None, (), False),
    "BFO_0000040": (
        "material entity",
        "An independent continuant that is spatially extended whose identity is independent of that of other entities and can be maintained through time.",
        (),
        False,
    ),
    "BFO_0000050": (
        "part of",
        "a core relation that holds between a part and its whole",
        (),
        False,
    ),
    "BFO_0000051": (
        "has part",
        "a core relation that holds between a whole and its part",
        (),
        False,
    ),
    "BFO_0000055": (
        "realizes",
        "Paraphrase of elucidation: a relation between a process and a realizable entity, where there is some material entity that is bearer of the realizable entity and participates in the process, and the realizable entity comes to be realized in the course of the process",
        (),
        False,
    ),
    "BFO_0000062": (
        "preceded by",
        "x is preceded by y if and only if the time point at which y ends is before or equivalent to the time point at which x starts. Formally: x preceded by y iff ω(y) <= α(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point.",
        (),
        False,
    ),
    "BFO_0000063": (
        "precedes",
        "x precedes y if and only if the time point at which x ends is before or equivalent to the time point at which y starts. Formally: x precedes y iff ω(x) <= α(y), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point.",
        (),
        False,
    ),
    "BFO_0000141": ("immaterial entity", None, (), False),
    "CHEBI_16670": (
        "peptide",
        "Amide derived from two or more amino carboxylic acid molecules (the same or different) by formation of a covalent bond from the carbonyl carbon of one to the nitrogen atom of another with formal loss of water. The term is usually applied to structures formed from α-amino acids, but it includes those derived from any amino carboxylic acid. X = OH, OR, NH2, NHR, etc.",
        (),
        False,
    ),
    "CHEBI_24636": (
        "proton",
        "Nuclear particle of charge number +1, spin ½ and rest mass of 1.007276470(12) u.",
        (),
        False,
    ),
    "CHEBI_33252": (
        "atomic nucleus",
        "A nucleus is the positively charged central portion of an atom, excluding the orbital electrons.",
        (),
        False,
    ),
    "CHEBI_33839": (
        "macromolecule",
        "A macromolecule is a molecule of high relative molecular mass, the structure of which essentially comprises the multiple repetition of units derived, actually or conceptually, from molecules of low relative molecular mass.",
        (),
        False,
    ),
    "CHEBI_36342": (
        "subatomic particle",
        "A particle smaller than an atom.",
        (),
        False,
    ),
    "CL_0000000": (
        "cell",
        "A material entity of anatomical origin (part of or deriving from an organism) that has as its parts a maximally connected cell compartment surrounded by a plasma membrane.",
        (),
        False,
    ),
    "COB_0000011": (
        "atom",
        "A material entity consisting of exactly one atomic nucleus and the electron(s) orbiting it.",
        (),
        False,
    ),
    "COB_0000013": (
        "molecule",
        "A material entity that consists of two or more atoms that are all connected via covalent bonds such that any atom can be transitively connected with any other atom.",
        (),
        False,
    ),
    "COB_0000021": (
        "gross anatomical part",
        "A part of a multicellular organism that is a collection of cell components that are not all contained in one cell.",
        (),
        False,
    ),
    "COB_0000022": (
        "organism",
        "A material entity that is a maximal functionally integrated unit that develops from a program encoded in a genome",
        (),
        False,
    ),
    "COB_0000035": ("completely executed planned process", None, (), False),
    "COB_0000080": (
        "complex of molecules",
        "A complex of two or more molecules that are not covalently bound.",
        (),
        False,
    ),
    "COB_0000082": (
        "planned process",
        "A process that is initiated by an agent who intends to carry out a plan to achieve an objective through one or more actions as described in a plan specification.",
        (),
        False,
    ),
    "COB_0000502": ("characteristic", None, (), False),
    "GO_0003008": ("system process", None, (), False),
    "GO_0003674": (
        "gene product or complex activity",
        "A molecular process that can be carried out by the action of a single macromolecular machine, usually via direct physical interactions with other molecular entities. Function in this sense denotes an action, or activity, that a gene product (or a complex) performs.",
        (),
        False,
    ),
    "GO_0005575": (
        "cellular_component",
        "A location, relative to cellular compartments and structures, occupied by a macromolecular machine. There are three types of cellular components described in the gene ontology: (1) the cellular anatomical entity where a gene product carries out a molecular function (e.g., plasma membrane, cytoskeleton) or membrane-enclosed compartments (e.g., mitochondrion); (2) virion components, where viral proteins act, and (3) the stable macromolecular complexes of which gene product are parts (e.g., the clathrin complex).",
        (),
        False,
    ),
    "GO_0007588": ("excretion", None, (), False),
    "GO_0008150": (
        "biological process",
        "A biological process is the execution of a genetically-encoded biological module or program. It consists of all the steps required to achieve the specific biological objective of the module. A biological process is accomplished by a particular set of molecular functions carried out by specific gene products (or macromolecular complexes), often in a highly regulated manner and in a particular temporal sequence.",
        (),
        False,
    ),
    "GO_0008152": ("metabolic process", None, (), False),
    "GO_0009987": ("cellular process", None, (), False),
    "GO_0016301": ("kinase activity", None, (), False),
    "GO_0032501": ("multicellular organismal process", None, (), False),
    "GO_0032991": (
        "protein-containing complex",
        "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.",
        (),
        False,
    ),
    "GO_0044423": (
        "virion component",
        "Any constituent part of a virion, a complete fully infectious extracellular virus particle.",
        (),
        False,
    ),
    "GO_0110165": (
        "cellular anatomical entity",
        "A part of a cellular organism that is either an immaterial entity or a material entity with granularity above the level of a protein complex but below that of an anatomical system. Or, a substance produced by a cellular organism with granularity above the level of a protein complex.",
        (),
        False,
    ),
    "IAO_0000003": (
        "measurement unit label",
        "A measurement unit label is as a label that is part of a scalar measurement datum and denotes a unit of measure.",
        (),
        False,
    ),
    "IAO_0000005": (
        "objective specification",
        "A directive information entity that describes an intended process endpoint. When part of a plan specification the concretization is realized in a planned process in which the bearer tries to effect the world so that the process endpoint is achieved.",
        (),
        False,
    ),
    "IAO_0000009": (
        "datum label",
        "A label is a symbol that is part of some other datum and is used to either partially define the denotation of that datum or to provide a means for identifying the datum as a member of the set of data with the same label",
        (),
        False,
    ),
    "IAO_0000010": (
        "software",
        "Software is a plan specification composed of a series of instructions that can be interpreted by or directly executed by a processing unit.",
        (),
        False,
    ),
    "IAO_0000027": (
        "data entity",
        "An information content entity that is intended to be one or more truthful statement(s) about something (modulo, e.g., measurement precision or other systematic errors) and is constructed/acquired by a method which reliably tends to produce (approximately) truthful statements.",
        (),
        False,
    ),
    "IAO_0000030": (
        "information content entity",
        "A generically dependent continuant that is about some thing.",
        (),
        False,
    ),
    "IAO_0000033": (
        "directive information entity",
        "An information content entity whose concretizations indicate to their bearer how to realize them in a process.",
        (),
        False,
    ),
    "IAO_0000037": (
        "dot plot",
        "A dot plot is a report graph which is a graphical representation of data where each data point is represented by a single dot placed on coordinates corresponding to data point values in particular dimensions.",
        (),
        False,
    ),
    "IAO_0000038": (
        "graph",
        "A diagram that presents one or more tuples of information by mapping those tuples in to a two dimensional space in a non arbitrary way.",
        (),
        False,
    ),
    "IAO_0000064": (
        "algorithm",
        "A plan specification which describes the inputs and output of mathematical functions as well as workflow of execution for achieving an predefined objective. Algorithms are realized usually by means of implementation as computer programs for execution by automata.",
        (),
        False,
    ),
    "IAO_0000078": (
        "curation status specification",
        "The curation status of the term. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value.",
        (),
        False,
    ),
    "IAO_0000098": (
        "data format specification",
        "A data format specification is the information content borne by the document published defining the specification. Example: The ISO document specifying what encompasses an XML document; The instructions in a XSD file",
        (),
        False,
    ),
    "IAO_0000100": (
        "homogenous data collection",
        "A data item that is an aggregate of other data items of the same type that have something in common. Averages and distributions can be determined for data sets.",
        (),
        False,
    ),
    "IAO_0000101": (
        "image",
        "An image is an affine projection to a two dimensional surface, of measurements of some quality of an entity or entities repeated at regular intervals across a spatial range, where the measurements are represented as color and luminosity on the projected on surface.",
        (),
        False,
    ),
    "IAO_0000102": (
        "data about an ontology part",
        "Data about an ontology part is a data item about a part of an ontology, for example a term",
        (),
        False,
    ),
    "IAO_0000104": (
        "plan specification",
        "A directive information entity with action specifications and objective specifications as parts, and that may be concretized as a realizable entity that, if realized, is realized in a process in which the bearer tries to achieve the objectives by taking the actions specified.",
        (),
        False,
    ),
    "IAO_0000136": (
        "is about",
        "A (currently) primitive relation that relates an information artifact to an entity.",
        (),
        False,
    ),
    "IAO_0000179": (
        "histogram",
        "A histogram is a report graph which is a statistical description of a distribution in terms of occurrence frequencies of different event classes.",
        (),
        False,
    ),
    "IAO_0000180": (
        "heatmap",
        "A heatmap is a report graph which is a graphical representation of data where the values taken by a variable(s) are shown as colors in a two-dimensional map.",
        (),
        False,
    ),
    "IAO_0000183": (
        "dendrogram",
        "A dendrogram is a report graph which is a tree diagram frequently used to illustrate the arrangement of the clusters produced by a clustering algorithm.",
        (),
        False,
    ),
    "IAO_0000184": (
        "scatter plot",
        "A scatterplot is a graph which uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points, each having the value of one variable determining the position on the horizontal axis and the value of the other variable determining the position on the vertical axis.",
        (),
        False,
    ),
    "IAO_0000225": (
        "obsolescence reason specification",
        "The reason for which a term has been deprecated. The allowed values come from an enumerated list of predefined terms. See the specification of these instances for more detailed definitions of each enumerated value.",
        (),
        False,
    ),
    "IAO_0000308": (
        "figure",
        "An information content entity consisting of a two dimensional arrangement of information content entities such that the arrangement itself is about something.",
        (),
        False,
    ),
    "IAO_0000310": (
        "document",
        "A collection of information content entities intended to be understood together as a whole",
        (),
        False,
    ),
    "IAO_0000409": (
        "denotator type",
        "A denotator type indicates how a term should be interpreted from an ontological perspective.",
        (),
        False,
    ),
    "IAO_0001000": (
        "data collection",
        "A data entity that consists of multiple data entities.",
        (),
        False,
    ),
    "NCBITaxon_117571": ("Euteleostomi", None, (), False),
    "NCBITaxon_2759": ("Eukaryota", None, (), False),
    "NCBITaxon_314146": ("Euarchontoglires", None, (), False),
    "NCBITaxon_32523": ("Tetrapoda", None, (), False),
    "NCBITaxon_32524": ("Amniota", None, (), False),
    "NCBITaxon_33154": ("Opisthokonta", None, (), False),
    "NCBITaxon_33208": ("Metazoa", None, (), False),
    "NCBITaxon_33213": ("Bilateria", None, (), False),
    "NCBITaxon_40674": ("Mammalia", None, (), False),
    "NCBITaxon_7742": ("Vertebrata <vertebrates>", None, (), False),
    "NCBITaxon_9606": ("Homo sapiens", None, (), False),
    "OBI_0000014": (
        "regulator role",
        "a regulatory role involved with making and/or enforcing relevant legislation and governmental orders",
        (),
        False,
    ),
    "OBI_0000017": (
        "regulatory role",
        "a role which inheres in material entities and is realized in the processes of making, enforcing or being defined by legislation or orders issued by a governmental body.",
        (),
        False,
    ),
    "OBI_0000018": (
        "material supplier role",
        "a role realized through the process of supplying materials such as animal subjects, reagents or other materials used in an investigation.",
        (),
        False,
    ),
    "OBI_0000023": (
        "classified data set",
        "A data set that is produced as the output of a class prediction data transformation and consists of a data set with assigned class labels.",
        (),
        False,
    ),
    "OBI_0000112": (
        "specimen role",
        "A role borne by a material entity that is obtained during a specimen collection process and that can be realized by performing measurements or observations on the specimen.",
        (),
        False,
    ),
    "OBI_0000245": (
        "organization",
        "An entity that can bear roles, has members, and has a set of organization rules. Members of organizations are either organizations themselves or individual people. Members can bear specific organization member roles that are determined in the organization rules. The organization rules also determine how decisions are made on behalf of the organization by the organization members.",
        (),
        False,
    ),
    "OBI_0000260": (
        "plan",
        "A plan is a realizable entity that is the inheres in a bearer who is committed to realizing it as a completely executed planned process.",
        (),
        False,
    ),
    "OBI_0000293": (
        "has specified input",
        "The inverse property of is specified input of",
        (),
        False,
    ),
    "OBI_0000295": (
        "is specified input of",
        "A relation between a completely executed planned process and a continuant participating in that process that is not created during the process. The presence of the continuant during the process is explicitly specified in the plan specification which the process realizes the concretization of.",
        (),
        False,
    ),
    "OBI_0000299": (
        "has specified output",
        "The inverse property of is specified output of",
        (),
        False,
    ),
    "OBI_0000312": (
        "is specified output of",
        "A relation between a completely executed planned process and a continuant participating in that process. The presence of the continuant at the end of the process is explicitly specified in the objective specification which the process realizes the concretization of.",
        (),
        False,
    ),
    "OBI_0000417": (
        "achieves_planned_objective",
        "This relation obtains between a planned process and a objective specification when the criteria specified in the objective specification are met at the end of the planned process.",
        (),
        False,
    ),
    "OBI_0000450": (
        "regulatory agency",
        "A regulatory agency is a organization that has responsibility over or for the legislation (acts and regulations) for a given sector of the government.",
        (),
        False,
    ),
    "OBI_0000571": (
        "manufacturer role",
        "Manufacturer role is a role which inheres in a person or organization and which is realized by a manufacturing process.",
        (),
        False,
    ),
    "OBI_0000648": (
        "clustered data set",
        "A data set that is produced as the output of a class discovery data transformation and consists of a data set with assigned discovered class labels.",
        (),
        False,
    ),
    "OBI_0000658": (
        "data representational model",
        "An information content entity representing the relationships between data items.",
        (),
        False,
    ),
    "OBI_0000659": (
        "specimen collection process",
        "A planned process with the objective to obtain a material entity for potential use as an input upon which measurements or observations are performed.",
        (),
        False,
    ),
    "OBI_0000663": (
        "class prediction data transformation",
        "A class prediction data transformation (sometimes called supervised classification) is a data transformation that has objective class prediction.",
        (),
        False,
    ),
    "OBI_0000684": (
        "specimen collection objective",
        "A objective specification that is fulfilled by obtaining a material entity for potential use as an input upon which measurements or observations are performed.",
        (),
        False,
    ),
    "OBI_0000700": (
        "support vector machine",
        "A support vector machine is a data transformation with a class prediction objective based on the construction of a separating hyperplane that maximizes the margin between two data sets of vectors in n-dimensional space.",
        (),
        False,
    ),
    "OBI_0000704": (
        "decision tree induction objective",
        "A decision tree induction objective is a data transformation objective in which a tree-like graph of edges and nodes is created and from which the selection of each branch requires that some type of logical decision is made.",
        (),
        False,
    ),
    "OBI_0000707": (
        "decision tree building data transformation",
        "A decision tree building data transformation is a data transformation that has objective decision tree induction.",
        (),
        False,
    ),
    "OBI_0000713": (
        "GenePattern software",
        "a software that provides access to more than 100 tools for gene expression analysis, proteomics, SNP analysis and common data processing tasks.",
        (),
        False,
    ),
    "OBI_0000726": (
        "peak matching",
        "Peak matching is a data transformation performed on a dataset of a graph of ordered data points (e.g. a spectrum) with the objective of pattern matching local maxima above a noise threshold",
        (),
        False,
    ),
    "OBI_0000727": (
        "k-nearest neighbors",
        "A k-nearest neighbors is a data transformation which achieves a class discovery or partitioning objective, in which an input data object with vector y is assigned to a class label based upon the k closest training data set points to y; where k is the largest value that class label is assigned.",
        (),
        False,
    ),
    "OBI_0000749": (
        "CART",
        "A CART (classification and regression trees) is a data transformation method for producing a classification or regression model with a tree-based structure.",
        (),
        False,
    ),
    "OBI_0000792": (
        "statistical model validation",
        "A data transformation which assesses how the results of a statistical analysis will generalize to an independent data set.",
        (),
        False,
    ),
    "OBI_0000833": (
        "objective_achieved_by",
        "This relation obtains between an objective specification and a planned process when the criteria specified in the objective specification are met at the end of the planned process.",
        (),
        False,
    ),
    "OBI_0000835": (
        "manufacturer",
        "A person or organization that has a manufacturer role.",
        (),
        False,
    ),
    "OBI_0000947": (
        "service provider role",
        "is a role which inheres in a person or organization and is realized in in a planned process which provides access to training, materials or execution of protocols for an organization or person",
        (),
        False,
    ),
    "OBI_0000963": (
        "categorical label",
        "A label that is part of a categorical datum and that indicates the value of the data item on the categorical scale.",
        (),
        False,
    ),
    "OBI_0001000": (
        "questionnaire",
        "A document with a set of printed or written questions with a choice of answers, devised for the purposes of a survey or statistical study.",
        (),
        False,
    ),
    "OBI_0001468": (
        "cell specimen",
        "A specimen primarily composed of a cell or cells collected from a multicellular organism or a cell culture.",
        (),
        False,
    ),
    "OBI_0001479": (
        "specimen from organism",
        "A specimen that derives from an anatomical part or substance arising from an organism. Examples of tissue specimen include tissue, organ, physiological system, blood, or body location (arm).",
        (),
        False,
    ),
    "OBI_0001930": (
        "categorical value specification",
        "A value specification that is specifies one category out of a fixed number of nominal categories",
        (),
        False,
    ),
    "OBI_0001933": (
        "value specification",
        "An information content entity that specifies a value within a classification scheme or on a quantitative scale.",
        (),
        False,
    ),
    "OBI_0002076": (
        "collection of specimens",
        "A material entity that has two or more specimens as its parts.",
        (),
        False,
    ),
    "OBI_0002205": (
        "histologic grade according to AJCC 7th edition",
        "A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the American Joint Committee on Cancer (AJCC) 7th Edition grading system.",
        (),
        False,
    ),
    "OBI_0002210": (
        "histologic grade according to the Fuhrman Nuclear Grading System",
        "A categorical value specification that is a histologic grade assigned to a tumor slide specimen according to the Fuhrman Nuclear Grading System.",
        (),
        False,
    ),
    "OBI_0002215": (
        "histologic grade for ovarian tumor",
        "A categorical value specification that is a histologic grade assigned to a ovarian tumor.",
        (),
        False,
    ),
    "OBI_0002216": (
        "histologic grade for ovarian tumor according to a two-tier grading system",
        "A histologic grade for ovarian tumor that is from a two-tier histological classification of tumors.",
        (),
        False,
    ),
    "OBI_0002219": (
        "histologic grade for ovarian tumor according to the World Health Organization",
        "A histologic grade for ovarian tumor that is from a histological classification by the World Health Organization (WHO).",
        (),
        False,
    ),
    "OBI_0002224": (
        "pathologic primary tumor stage for colon and rectum according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002232": (
        "pathologic primary tumor stage for lung according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM American Joint Committee on Cancer (AJCC) version 7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002243": (
        "pathologic primary tumor stage for kidney according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002256": (
        "pathologic primary tumor stage for ovary according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of the primary tumor. TNM pathologic primary tumor findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002270": (
        "pathologic lymph node stage for colon and rectum according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of colorectal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    "OBI_0002279": (
        "pathologic lymph node stage for lung according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    "OBI_0002284": (
        "pathologic lymph node stage for kidney according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    "OBI_0002287": (
        "pathologic lymph node stage for ovary according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to staging of regional lymph nodes.",
        (),
        False,
    ),
    "OBI_0002290": (
        "pathologic distant metastases stage for colon according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of colon cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002298": (
        "pathologic distant metastases stage for lung according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of lung cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002306": (
        "pathologic distant metastases stage for kidney according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of renal cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002310": (
        "pathologic distant metastases stage for ovary according to AJCC 7th edition",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the TNM AJCC v7 classification system as they pertain to distant metastases. TNM pathologic distant metastasis findings are based on clinical findings supplemented by histopathologic examination of one or more tissue specimens acquired during surgery.",
        (),
        False,
    ),
    "OBI_0002314": (
        "clinical tumor stage group according to AJCC 7th edition",
        "A categorical value specification that is an assessment of the stage of a cancer according to the American Joint Committee on Cancer (AJCC) v7 staging systems.",
        (),
        False,
    ),
    "OBI_0002326": (
        "International Federation of Gynecology and Obstetrics cervical cancer stage value specification",
        "A categorical value specification that is an assessment of the stage of a gynecologic cancer according to the International Federation of Gynecology and Obstetrics (FIGO) staging systems.",
        (),
        False,
    ),
    "OBI_0002341": (
        "International Federation of Gynecology and Obstetrics ovarian cancer stage value specification",
        "A categorical value specification that is a pathologic finding about one or more characteristics of ovarian cancer following the rules of the FIGO classification system.",
        (),
        False,
    ),
    "OBI_0002356": (
        "performance status value specification",
        "A categorical value specification that is an assessment of a participant's performance status (general well-being and activities of daily life).",
        (),
        False,
    ),
    "OBI_0002357": (
        "Eastern Cooperative Oncology Group score value specification",
        "A performance status value specification designed by the Eastern Cooperative Oncology Group to assess disease progression and its affect on the daily living abilities of the patient.",
        (),
        False,
    ),
    "OBI_0002363": (
        "Karnofsky score vaue specification",
        "A performance status value specification designed for classifying patients 16 years of age or older by their functional impairment.",
        (),
        False,
    ),
    "OBI_0002989": (
        "material supplier",
        "A person or organization that provides material supplies to other people or organizations.",
        (),
        False,
    ),
    "OBI_0100051": (
        "specimen",
        "A material entity that is collected for potential use as an input upon which measurements or observations are performed.",
        (),
        False,
    ),
    "OBI_0200000": (
        "data transformation",
        "A completely executed planned process that produces output data from input data.",
        (),
        False,
    ),
    "OBI_0200033": (
        "leave one out cross validation method",
        "is a data transformation : leave-one-out cross-validation (LOOCV) involves using a single observation from the original sample as the validation data, and the remaining observations as the training data. This is repeated such that each observation in the sample is used once as the validation data",
        (),
        False,
    ),
    "OBI_0200041": (
        "k-means clustering",
        "A k-means clustering is a data transformation which achieves a class discovery or partitioning objective, which takes as input a collection of objects (represented as points in multidimensional space) and which partitions them into a specified number k of clusters. The algorithm attempts to find the centers of natural clusters in the data. The most common form of the algorithm starts by partitioning the input points into k initial sets, either at random or using some heuristic data. It then calculates the mean point, or centroid, of each set. It constructs a new partition by associating each point with the closest centroid. Then the centroids are recalculated for the new clusters, and the algorithm repeated by alternate applications of these two steps until convergence, which is obtained when the points no longer switch clusters (or alternatively centroids are no longer changed).",
        (),
        False,
    ),
    "OBI_0200042": (
        "hierarchical clustering",
        "A hierarchical clustering is a data transformation which achieves a class discovery objective, which takes as input data item and builds a hierarchy of clusters. The traditional representation of this hierarchy is a tree (visualized by a dendrogram), with the individual input objects at one end (leaves) and a single cluster containing every object at the other (root).",
        (),
        False,
    ),
    "OBI_0200050": (
        "dimensionality reduction",
        "A dimensionality reduction is data partitioning which transforms each input m-dimensional vector (x_1, x_2, ..., x_m) into an output n-dimensional vector (y_1, y_2, ..., y_n), where n is smaller than m.",
        (),
        False,
    ),
    "OBI_0200051": (
        "principal components analysis dimensionality reduction",
        "A principal components analysis dimensionality reduction is a dimensionality reduction achieved by applying principal components analysis and by keeping low-order principal components and excluding higher-order ones.",
        (),
        False,
    ),
    "OBI_0200111": (
        "data visualization",
        "A planned process with the objective to graphically represent some data by inputing the data and outputting images, diagrams or animations.",
        (),
        False,
    ),
    "OBI_0200166": (
        "data transformation objective",
        "An objective specification to transformation input data into output data",
        (),
        False,
    ),
    "OBI_0200171": (
        "partitioning data transformation",
        "A partitioning data transformation is a data transformation that has objective partitioning.",
        (),
        False,
    ),
    "OBI_0200172": (
        "partitioning objective",
        "A partitioning objective is a data transformation objective where the aim is to generate a collection of disjoint non-empty subsets whose union equals a non-empty input set.",
        (),
        False,
    ),
    "OBI_0200175": (
        "class discovery data transformation",
        "A class discovery data transformation (sometimes called unsupervised classification) is a data transformation that has objective class discovery.",
        (),
        False,
    ),
    "OBI_0200178": (
        "class discovery objective",
        "A class discovery objective (sometimes called unsupervised classification) is a data transformation objective where the aim is to organize input data (typically vectors of attributes) into classes, where the number of classes and their specifications are not known a priori. Depending on usage, the class assignment can be definite or probabilistic.",
        (),
        False,
    ),
    "OBI_0200179": (
        "class prediction objective",
        "A class prediction objective (sometimes called supervised classification) is a data transformation objective where the aim is to create a predictor from training data through a machine learning technique. The training data consist of pairs of objects (typically vectors of attributes) and class labels for these objects. The resulting predictor can be used to attach class labels to any valid novel input object. Depending on usage, the prediction can be definite or probabilistic. A classification is learned from the training data and can then be tested on test data.",
        (),
        False,
    ),
    "OBI_0200188": (
        "cross validation objective",
        "A cross validation objective is a data transformation objective in which the aim is to partition a sample of data into subsets such that the analysis is initially performed on a single subset, while the other subset(s) are retained for subsequent use in confirming and validating the initial analysis.",
        (),
        False,
    ),
    "OBI_0200190": (
        "clustered data visualization",
        "A data visualization which has input of a clustered data set and produces an output of a report graph which is capable of rendering data of this type.",
        (),
        False,
    ),
    "PATO_0000001": ("quality", None, (), False),
    "PBPKO_00002": ("parameter", "A data item involved in PBPK modelling.", (), False),
    "PBPKO_00003": (
        "physiologically based pharmacokinetic model",
        "A data representation model that predicts the absorption, distribution, metabolism, and excretion (ADME) of chemical substances in biological species based on physiological principles using mathematical modelling technique.",
        (),
        False,
    ),
    "PBPKO_00004": (
        "whole body pbpk",
        "A physiologically based pharmacokinetic model that contains an explicit representation of the organs most relevant to the ADME of the compound.",
        (),
        False,
    ),
    "PBPKO_00005": (
        "perfusion limited model",
        "A physiologically based pharmacokinetic model that assumes tissue concentration reaches equilibrium rapidly and uptake/elimination is limited by blood flow rate.",
        (),
        False,
    ),
    "PBPKO_00006": (
        "physiological parameter",
        "A parameter that provides the structural framework for a PBPK model and relates to the organism's physiology (e.g., body weight, organ volume, blood flow).",
        (),
        False,
    ),
    "PBPKO_00007": (
        "body mass index",
        "A physiological parameter calculated as an individual's weight (kg) divided by the square of their height (m).",
        (),
        False,
    ),
    "PBPKO_00008": (
        "bodyweight",
        "A physiological parameter representing the mass or quantity of heaviness of an individual.",
        (),
        False,
    ),
    "PBPKO_00009": (
        "height",
        "A physiological parameter describing the distance from the bottom to the top of someone standing upright.",
        (),
        False,
    ),
    "PBPKO_00010": (
        "surface area",
        "A physiological parameter representing the total area that the surface of an object occupies.",
        (),
        False,
    ),
    "PBPKO_00011": (
        "assigned race",
        "A parameter representing a geographic ancestral origin category assigned to a population group.",
        (),
        False,
    ),
    "PBPKO_00012": (
        "blood flow rate to compartment",
        "A bodily fluid flow rate parameter representing the rate of blood flow in different parts of the body",
        (),
        False,
    ),
    "PBPKO_00013": (
        "cardiac output rate",
        "A blood flow rate parameter representing the volume of blood pumped by the heart compartment per unit of time.",
        (),
        False,
    ),
    "PBPKO_00014": (
        "blood flow rate to stomach",
        "A blood flow rate parameter specifically describing the rate to the stomach compartment.",
        (),
        False,
    ),
    "PBPKO_00015": (
        "fraction of blood flow to stomach",
        "The dimensionless fraction of cardiac output delivered to the stomach compartment.",
        (),
        False,
    ),
    "PBPKO_00016": (
        "blood flow rate to intestine",
        "A blood flow parameter specifically describing the rate to the intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00017": (
        "fraction of blood flow to intestine",
        "The dimensionless fraction of cardiac output delivered to the intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00018": (
        "blood flow rate to small intestine",
        "A blood flow rate parameter specifically describing the rate to the small intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00019": (
        "fraction of blood flow to small intestine",
        "The dimensionless fraction of cardiac output delivered to the small intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00020": (
        "blood flow rate to large intestine",
        "A blood flow rate parameter specifically describing the rate to the large intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00021": (
        "fraction of blood flow to large intestine",
        "The dimensionless fraction of cardiac output delivered to the large intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00022": (
        "blood flow rate to pancreas",
        "A blood flow rate parameter specifically describing the rate to the pancreas compartment.",
        (),
        False,
    ),
    "PBPKO_00023": (
        "fraction of blood flow to pancreas",
        "The dimensionless fraction of cardiac output delivered to the pancreas compartment.",
        (),
        False,
    ),
    "PBPKO_00024": (
        "blood flow rate to liver",
        "A blood flow rate parameter specifically describing the rate to the liver compartment.",
        (),
        False,
    ),
    "PBPKO_00025": (
        "fraction of blood flow to liver",
        "The dimensionless fraction of cardiac output delivered to the liver compartment.",
        (),
        False,
    ),
    "PBPKO_00026": (
        "blood flow rate to kidney",
        "A blood flow rate parameter specifically describing the rate to the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00027": (
        "fraction of blood flow to kidney",
        "The dimensionless fraction of cardiac output delivered to the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00028": (
        "blood flow rate to muscle",
        "A blood flow rate parameter specifically describing the rate to the muscle compartment.",
        (),
        False,
    ),
    "PBPKO_00029": (
        "fraction of blood flow to muscle",
        "The dimensionless fraction of cardiac output delivered to the muscle compartment.",
        (),
        False,
    ),
    "PBPKO_00030": (
        "blood flow rate to heart",
        "A blood flow rate parameter specifically describing the rate to the heart compartment.",
        (),
        False,
    ),
    "PBPKO_00031": (
        "fraction of blood flow to heart",
        "The dimensionless fraction of cardiac output delivered to the heart compartment.",
        (),
        False,
    ),
    "PBPKO_00032": (
        "blood flow rate to fat",
        "A blood flow rate parameter specifically describing the rate to the fat (adipose tissue) compartment.",
        (),
        False,
    ),
    "PBPKO_00033": (
        "fraction of blood flow to fat",
        "The dimensionless fraction of cardiac output delivered to the fat compartment.",
        (),
        False,
    ),
    "PBPKO_00034": (
        "blood flow rate to gonad",
        "A blood flow parameter specifically describing the rate to the gonads compartment.",
        (),
        False,
    ),
    "PBPKO_00035": (
        "fraction of blood flow to gonad",
        "The dimensionless fraction of cardiac output delivered to the gonad compartment.",
        (),
        False,
    ),
    "PBPKO_00036": (
        "blood flow rate to skin",
        "A blood flow rate parameter specifically describing the rate to the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00037": (
        "fraction of blood flow to skin",
        "The dimensionless fraction of cardiac output delivered to the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00038": (
        "blood flow rate to bone",
        "A blood flow rate parameter specifically describing the rate to the bone compartment.",
        (),
        False,
    ),
    "PBPKO_00039": (
        "fraction of blood flow to bone",
        "The dimensionless fraction of cardiac output delivered to the bone compartment.",
        (),
        False,
    ),
    "PBPKO_00040": (
        "blood flow rate to brain",
        "A blood flow rate parameter specifically describing the rate to the brain compartment.",
        (),
        False,
    ),
    "PBPKO_00041": (
        "fraction of blood flow to brain",
        "The dimensionless fraction of cardiac output delivered to the brain compartment.",
        (),
        False,
    ),
    "PBPKO_00042": (
        "blood flow rate to spleen",
        "A blood flow rate parameter specifically describing the rate to the spleen compartment.",
        (),
        False,
    ),
    "PBPKO_00043": (
        "fraction of blood flow to spleen",
        "The dimensionless fraction of cardiac output delivered to the spleen compartment.",
        (),
        False,
    ),
    "PBPKO_00044": (
        "blood flow rate to lung",
        "A blood flow rate parameter specifically describing the rate to the lung compartment.",
        (),
        False,
    ),
    "PBPKO_00045": (
        "fraction of blood flow to lung",
        "The dimensionless fraction of cardiac output delivered to the lung compartment.",
        (),
        False,
    ),
    "PBPKO_00046": (
        "blood flow rate to poorly perfused",
        "A blood flow rate parameter specifically describing the rate to the poorly perfused organ/tissue compartment.",
        (),
        False,
    ),
    "PBPKO_00047": (
        "fraction of blood flow to poorly perfused",
        "The dimensionless fraction of cardiac output delivered to the poorly perfused compartment.",
        (),
        False,
    ),
    "PBPKO_00048": (
        "blood flow rate to richly perfused",
        "A blood flow rate parameter specifically describing the rate to the richly perfused organ/tissue compartment.",
        (),
        False,
    ),
    "PBPKO_00049": (
        "fraction of blood flow to richly perfused",
        "The dimensionless fraction of cardiac output delivered to the richly perfused compartment.",
        (),
        False,
    ),
    "PBPKO_00050": (
        "blood flow rate to restbody",
        "A blood flow rate parameter specifically describing the rate to the rest of body compartment (total minus specified organs).",
        (),
        False,
    ),
    "PBPKO_00051": (
        "fraction of blood flow to restbody",
        "The dimensionless fraction of cardiac output delivered to the rest of the body compartment.",
        (),
        False,
    ),
    "PBPKO_00052": (
        "blood flow rate to gall bladder",
        "A blood flow rate parameter specifically describing the rate to the gall bladder compartment.",
        (),
        False,
    ),
    "PBPKO_00053": (
        "fraction of blood flow to gall bladder",
        "The dimensionless fraction of cardiac output delivered to the gall bladder compartment.",
        (),
        False,
    ),
    "PBPKO_00054": (
        "blood flow rate to portal vein",
        "A blood flow rate parameter specifically describing the rate to the portal vein compartment.",
        (),
        False,
    ),
    "PBPKO_00055": (
        "fraction of blood flow to portal vein",
        "The dimensionless fraction of cardiac output delivered to the portal vein compartment.",
        (),
        False,
    ),
    "PBPKO_00056": (
        "blood flow rate to lymph",
        "A blood flow rate parameter specifically describing the rate to the lymph compartment.",
        (),
        False,
    ),
    "PBPKO_00057": (
        "fraction of blood flow to lymph",
        "The dimensionless fraction of cardiac output delivered to the lymph compartment.",
        (),
        False,
    ),
    "PBPKO_00058": (
        "amount of metabolized",
        "An output parameter representing the total amount of compound metabolized.",
        (),
        False,
    ),
    "PBPKO_00060": (
        "fraction of blood flow to stratum corneum",
        "The dimensionless fraction of cardiac output delivered to the stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_00061": (
        "fraction of exposed skin",
        "A dimensionless fraction of volume defined as the exposed skin volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00062": (
        "fraction of unexposed skin",
        "A dimensionless fraction of volume defined as the unexposed skin volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00063": (
        "arterial blood flow rate",
        "A blood flow rate parameter representing the rate of blood flow through the arterial compartment.",
        (),
        False,
    ),
    "PBPKO_00064": (
        "venous blood flow rate",
        "A blood flow rate parameter representing the rate of blood flow returning through the venous compartment.",
        (),
        False,
    ),
    "PBPKO_00065": (
        "glomerular filtration rate",
        "A bodily fluid flow rate parameter (or physiological process measure) describing the flow rate of filtered fluid through the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00066": (
        "volume of compartment",
        "A physiological parameter representing the volume of a specific organ or tissue.",
        (),
        False,
    ),
    "PBPKO_00067": (
        "volume of stomach",
        "A volume parameter representing the total volume of the stomach compartment.",
        (),
        False,
    ),
    "PBPKO_00068": (
        "fraction of stomach",
        "A dimensionless fraction of volume defined as the stomach volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00069": (
        "volume of intestine",
        "A volume parameter representing the total volume of the intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00070": (
        "fraction of intestine",
        "A dimensionless fraction of volume defined as the intestine volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00071": (
        "volume of small intestine",
        "A volume parameter representing the total volume of the small intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00072": (
        "fraction of small intestine",
        "A dimensionless fraction of volume defined as the small intestine volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00073": (
        "volume of large intestine",
        "A volume parameter representing the total volume of the large intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00074": (
        "fraction of large intestine",
        "A dimensionless fraction of volume defined as the large intestine volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00075": (
        "volume of pancreas",
        "A volume parameter representing the total volume of the pancreas compartment.",
        (),
        False,
    ),
    "PBPKO_00076": (
        "fraction of pancreas",
        "A dimensionless fraction of volume defined as the pancreas volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00077": (
        "volume of liver",
        "A volume parameter representing the total volume of the liver compartment.",
        (),
        False,
    ),
    "PBPKO_00078": (
        "fraction of liver",
        "A dimensionless fraction of volume defined as the liver volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00079": (
        "volume of kidney",
        "A volume parameter representing the total volume of the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00080": (
        "fraction of kidney",
        "A dimensionless fraction of volume defined as the kidney volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00081": (
        "volume of muscle",
        "A volume parameter representing the total volume of muscle compartment.",
        (),
        False,
    ),
    "PBPKO_00082": (
        "fraction of muscle",
        "A dimensionless fraction of volume defined as the muscle volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00083": (
        "volume of heart",
        "A volume parameter representing the total volume of the heart compartment.",
        (),
        False,
    ),
    "PBPKO_00084": (
        "fraction of heart",
        "A dimensionless fraction of volume defined as the heart volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00085": (
        "volume of fat",
        "A volume parameter representing the total volume of fat (adipose tissue) compartment.",
        (),
        False,
    ),
    "PBPKO_00086": (
        "fraction of fat",
        "A dimensionless fraction of volume defined as the fat volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00087": (
        "volume of gonad",
        "A volume parameter representing the total volume of the gonad compartment.",
        (),
        False,
    ),
    "PBPKO_00088": (
        "fraction of gonad",
        "A dimensionless fraction of volume defined as the gonad volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00089": (
        "volume of skin",
        "A volume parameter representing the total volume of the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00090": (
        "fraction of skin",
        "A dimensionless fraction of volume defined as the skin volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00091": (
        "volume of bone",
        "A volume parameter representing the total volume of bone compartment.",
        (),
        False,
    ),
    "PBPKO_00092": (
        "fraction of bone",
        "A dimensionless fraction of volume defined as the bone volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00093": (
        "volume of brain",
        "A volume parameter representing the total volume of the brain compartment.",
        (),
        False,
    ),
    "PBPKO_00094": (
        "fraction of brain",
        "A dimensionless fraction of volume defined as the brain volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00095": (
        "volume of spleen",
        "A volume parameter representing the total volume of the spleen compartment.",
        (),
        False,
    ),
    "PBPKO_00096": (
        "fraction of spleen",
        "A dimensionless fraction of volume defined as the spleen volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00097": (
        "volume of lung",
        "A volume parameter representing the total volume of the lung compartment.",
        (),
        False,
    ),
    "PBPKO_00098": (
        "fraction of lung",
        "A dimensionless fraction of volume defined as the lung volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00099": (
        "volume of poorly perfused",
        "A volume parameter representing the total volume of the poorly perfused compartment.",
        (),
        False,
    ),
    "PBPKO_00100": (
        "fraction of poorly perfused",
        "A dimensionless fraction of volume defined as the poorly perfused compartment volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00101": (
        "volume of richly perfused",
        "A volume parameter representing the total volume of the richly perfused compartment.",
        (),
        False,
    ),
    "PBPKO_00102": (
        "fraction of richly perfused",
        "A dimensionless fraction of volume defined as the richly perfused compartment volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00103": (
        "volume of plasma",
        "A volume parameter representing the total volume of plasma compartment.",
        (),
        False,
    ),
    "PBPKO_00104": (
        "fraction of plasma",
        "A dimensionless fraction of volume defined as the plasma volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00105": (
        "volume of rest body",
        "A volume parameter representing the total volume of the rest of body compartment.",
        (),
        False,
    ),
    "PBPKO_00106": (
        "fraction of rest body",
        "A dimensionless fraction of volume defined as the rest of body volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00107": (
        "volume of stratum corneum with respect to blood",
        "A volume parameter representing the total volume of stratum corneum compartment with respect to blood/plasma.",
        (),
        False,
    ),
    "PBPKO_00108": (
        "volume of blood",
        "A volume parameter representing the total volume of blood compartment.",
        (),
        False,
    ),
    "PBPKO_00109": (
        "volume of exposed skin",
        "A volume parameter representing the total volume of the exposed skin compartment.",
        (),
        False,
    ),
    "PBPKO_00110": (
        "fraction of surface area exposed",
        "A surface area parameter representing the fraction of skin surface area actually exposed.",
        (),
        False,
    ),
    "PBPKO_00111": (
        "volume of unexposed skin",
        "A volume parameter representing the total volume of the unexposed skin compartment.",
        (),
        False,
    ),
    "PBPKO_00112": (
        "volume of stratum corneum exposed",
        "A volume parameter representing the total volume of the exposed stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_00113": (
        "volume of unexposed stratum corneum",
        "A volume parameter representing the total volume of the unexposed stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_00114": (
        "fraction alveolar volume",
        "A dimensionless fraction of volume defined as the alveolar volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00115": (
        "volume of gall bladder",
        "A volume parameter representing the total volume of the gall bladder compartment.",
        (),
        False,
    ),
    "PBPKO_00116": (
        "fraction of gall bladder",
        "A dimensionless fraction of volume defined as the gall bladder volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00117": (
        "volume of portal vein",
        "A volume parameter representing the total volume of the portal vein compartment.",
        (),
        False,
    ),
    "PBPKO_00118": (
        "fraction of portal vein",
        "A dimensionless fraction of volume defined as the portal vein volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00119": (
        "volume of lymph",
        "A volume parameter representing the total volume of lymph compartment.",
        (),
        False,
    ),
    "PBPKO_00120": (
        "fraction of lymph",
        "A dimensionless fraction of volume defined as the lymph volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00121": (
        "arterial volume",
        "A volume parameter representing the total volume of the arterial compartment.",
        (),
        False,
    ),
    "PBPKO_00122": (
        "venous volume",
        "A volume parameter representing the total volume of the venous compartment.",
        (),
        False,
    ),
    "PBPKO_00126": (
        "physicochemical parameter",
        "A parameter relating to the physical and chemical properties of a compound (e.g., MW, lipophilicity, solubility, pKa).",
        (),
        False,
    ),
    "PBPKO_00127": (
        "molecular weight",
        "A physicochemical parameter representing the sum of the weights of all atoms in a molecule.",
        (),
        False,
    ),
    "PBPKO_00128": (
        "lipophillicity",
        "A physicochemical parameter representing the affinity or tendency of a compound to dissolve in lipids or hydrophobic environments.",
        (),
        False,
    ),
    "PBPKO_00129": (
        "distribution coefficient",
        "A physicochemical parameter representing the logarithm of the ratio of concentrations of a compound in a mixture of two immiscible phases at equilibrium, specifically describing lipophilicity (LogD).",
        (),
        False,
    ),
    "PBPKO_00130": (
        "dissolution in two phase system",
        "A physicochemical parameter representing the ratio of a dissolved compound in a two-phase system (often used interchangeably with partition coefficient).",
        (),
        False,
    ),
    "PBPKO_00131": (
        "logarithmic solubility",
        "A physicochemical parameter representing the 10-based logarithm of a compound's solubility (typically in mol/L).",
        (),
        False,
    ),
    "PBPKO_00132": (
        "water solubility",
        "A physicochemical parameter representing the solubility of a compound specifically in water.",
        (),
        False,
    ),
    "PBPKO_00133": (
        "acid dissociation constant",
        "A physicochemical parameter representing the negative base-10 logarithm (pKa) of the acid dissociation constant (Ka).",
        (),
        False,
    ),
    "PBPKO_00134": (
        "basic dissociation constant",
        "A physicochemical parameter representing the negative base-10 logarithm (pKb) of the base dissociation constant (Kb).",
        (),
        False,
    ),
    "PBPKO_00135": (
        "physiological charge",
        "A physicochemical parameter representing the electrical charge of a molecule at physiological pH.",
        (),
        False,
    ),
    "PBPKO_00136": (
        "hydrogen acceptor count",
        "A physicochemical parameter representing the integer number of hydrogen bond acceptors in a molecular entity.",
        (),
        False,
    ),
    "PBPKO_00137": (
        "hydrogen donor count",
        "A physicochemical parameter representing the integer number of hydrogen bond donors in a molecular entity.",
        (),
        False,
    ),
    "PBPKO_00138": (
        "rotatable bond count",
        "A physicochemical parameter representing the integer count of rotatable bonds in a molecular entity.",
        (),
        False,
    ),
    "PBPKO_00139": (
        "biochemical parameter",
        "A parameter that is compound-dependent and relates to biological interactions or transformations (e.g., clearance, binding, partition coefficients).",
        (),
        False,
    ),
    "PBPKO_00140": (
        "absorption",
        "A biological process by which a compound moves from its site of administration into the systemic circulation or a target tissue.",
        (),
        False,
    ),
    "PBPKO_00141": (
        "absorption rate constant gut",
        "An absorption rate constant parameter representing the rate constant for the movement of a compound from the gut to systemic circulation or another compartment.",
        (),
        False,
    ),
    "PBPKO_00142": (
        "absorption rate constant intestine",
        "An absorption rate constant parameter representing the movement of a compound from the intestine to systemic circulation or another compartment.",
        (),
        False,
    ),
    "PBPKO_00143": (
        "gastric emptying rate",
        "A biochemical parameter representing the rate at which the stomach empties its contents into the small intestine.",
        (),
        False,
    ),
    "PBPKO_00144": (
        "enterohepatic recirculation",
        "A biological process involving recycling of compounds through the liver via biliary excretion, intestinal reabsorption, portal circulation return, and re-excretion.",
        (),
        False,
    ),
    "PBPKO_00145": (
        "specific intestinal permeability",
        "A biochemical parameter representing the surface area-normalized transcellular permeability of the intestinal wall for a compound.",
        (),
        False,
    ),
    "PBPKO_00146": (
        "distribution process",
        "A biological process describing the movement of a compound from systemic circulation to various organs/tissues.",
        (),
        False,
    ),
    "PBPKO_00147": (
        "volume of distribution",
        "A biochemical parameter representing the apparent volume into which a compound distributes in the body relative to its plasma concentration.",
        (),
        False,
    ),
    "PBPKO_00148": (
        "protein binding mediated distributiion process",
        "A distribution process (or molecular function) where substances bind to proteins or related compounds.",
        (),
        False,
    ),
    "PBPKO_00149": (
        "unbound fraction",
        "A biochemical parameter representing the fraction of a compound that is not bound (e.g., to proteins).",
        (),
        False,
    ),
    "PBPKO_00150": (
        "fraction unbound gut",
        "An unbound fraction parameter specifically for the gut compartment.",
        (),
        False,
    ),
    "PBPKO_00151": (
        "fraction unbound stomach",
        "An unbound fraction parameter specifically for the stomach compartment.",
        (),
        False,
    ),
    "PBPKO_00152": (
        "fraction unbound intestine",
        "An unbound fraction parameter specifically for the intestine compartment.",
        (),
        False,
    ),
    "PBPKO_00153": (
        "fraction unbound pancreas",
        "An unbound fraction parameter specifically for the pancreas compartment.",
        (),
        False,
    ),
    "PBPKO_00154": (
        "fraction unbound liver",
        "An unbound fraction parameter specifically for the liver compartment.",
        (),
        False,
    ),
    "PBPKO_00155": (
        "fraction unbound kidney",
        "An unbound fraction parameter specifically for the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00156": (
        "fraction unbound muscle",
        "An unbound fraction parameter specifically for the muscle compartment.",
        (),
        False,
    ),
    "PBPKO_00157": (
        "fraction unbound heart",
        "An unbound fraction parameter specifically for the heart compartment.",
        (),
        False,
    ),
    "PBPKO_00158": (
        "fraction unbound fat",
        "An unbound fraction parameter specifically for the fat (adipose) compartment.",
        (),
        False,
    ),
    "PBPKO_00159": (
        "fraction unbound gonad",
        "An unbound fraction parameter specifically for the gonad compartment.",
        (),
        False,
    ),
    "PBPKO_00160": (
        "fraction unbound skin",
        "An unbound fraction parameter specifically for the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00161": (
        "fraction unbound bone",
        "An unbound fraction parameter specifically for the bone compartment.",
        (),
        False,
    ),
    "PBPKO_00162": (
        "fraction unbound spleen",
        "An unbound fraction parameter specifically for the spleen compartment.",
        (),
        False,
    ),
    "PBPKO_00163": (
        "fraction unbound lung",
        "An unbound fraction parameter specifically for the lung compartment.",
        (),
        False,
    ),
    "PBPKO_00164": (
        "fraction unbound enterocytes",
        "An unbound fraction parameter specifically within enterocytes.",
        (),
        False,
    ),
    "PBPKO_00165": (
        "partition coefficient",
        "A biochemical parameter representing the ratio of the concentration of a compound in a particular tissue to its concentration in plasma/blood at equilibrium.",
        (),
        False,
    ),
    "PBPKO_00166": (
        "gut plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in gut to plasma.",
        (),
        False,
    ),
    "PBPKO_00167": (
        "stomach plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in stomach to plasma.",
        (),
        False,
    ),
    "PBPKO_00168": (
        "intestine plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in intestine to plasma.",
        (),
        False,
    ),
    "PBPKO_00169": (
        "pancreas plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in pancreas to plasma.",
        (),
        False,
    ),
    "PBPKO_00170": (
        "liver plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in liver to plasma.",
        (),
        False,
    ),
    "PBPKO_00171": (
        "kidney plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in kidney to plasma.",
        (),
        False,
    ),
    "PBPKO_00172": (
        "muscle plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in muscle to plasma.",
        (),
        False,
    ),
    "PBPKO_00173": (
        "heart plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in heart to plasma.",
        (),
        False,
    ),
    "PBPKO_00174": (
        "fat plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in fat (adipose tissue) to plasma.",
        (),
        False,
    ),
    "PBPKO_00175": (
        "gonad plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in gonads to plasma.",
        (),
        False,
    ),
    "PBPKO_00176": (
        "skin plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in skin to plasma.",
        (),
        False,
    ),
    "PBPKO_00177": (
        "bone plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in bone to plasma.",
        (),
        False,
    ),
    "PBPKO_00178": (
        "spleen plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in spleen to plasma.",
        (),
        False,
    ),
    "PBPKO_00179": (
        "lung plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in lung to plasma.",
        (),
        False,
    ),
    "PBPKO_00180": (
        "rich perfused plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the lumped richly perfused compartment to plasma.",
        (),
        False,
    ),
    "PBPKO_00181": (
        "poor perfused plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the lumped poorly perfused compartment to plasma.",
        (),
        False,
    ),
    "PBPKO_00182": (
        "skin stratum corneum partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the stratum corneum to the rest of the skin.",
        (),
        False,
    ),
    "PBPKO_00183": (
        "air plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in air to plasma.",
        (),
        False,
    ),
    "PBPKO_00184": (
        "skin diffusion coefficient",
        "A diffusion coefficient representing the diffusion of a compound across the skin.",
        (),
        False,
    ),
    "PBPKO_00185": (
        "human serum albumin",
        "A material entity representing distribution-related protein (most abundant in human plasma) that binds various compounds.",
        (),
        False,
    ),
    "PBPKO_00187": (
        "blood:plasma ratio",
        "A biochemical parameter representing the ratio of compound concentration in whole blood to that in plasma.",
        (),
        False,
    ),
    "PBPKO_00189": (
        "catalytic rate constant",
        "A biochemical parameter quantifying enzymatic reaction velocity (kcat), representing the maximum number of substrate molecules converted per active site per unit time.",
        (),
        False,
    ),
    "PBPKO_00191": (
        "phase I metabolism",
        "A metabolism process involving the conversion of exogenous substances to more polar metabolites, often via oxidation, reduction, or hydrolysis (e.g., by CYPs).",
        (),
        False,
    ),
    "PBPKO_00200": (
        "phase II",
        "A metabolism process involving the conjugation of phase I products (or parent compounds) to hydrophilic moieties to facilitate excretion.",
        (),
        False,
    ),
    "PBPKO_00209": (
        "phase III",
        "A metabolism/transport process involving the further processing and excretion of conjugated metabolites (often involving efflux transporters).",
        (),
        False,
    ),
    "PBPKO_00210": (
        "first pass metabolism",
        "A metabolism process occurring at a specific location (e.g., liver, gut wall) after administration but before reaching systemic circulation, reducing the concentration of active compound.",
        (),
        False,
    ),
    "PBPKO_00211": (
        "maximum rate in intestine",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the intestine when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    "PBPKO_00212": (
        "Michaelis constant  intestine",
        "Michaelis constant representing the substrate concentration at which the reaction rate in the intestine is half of Vmax (Km).",
        (),
        False,
    ),
    "PBPKO_00213": (
        "maximum rate in liver",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in the liver when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    "PBPKO_00214": (
        "Michaelis constant  liver",
        "Michaelis constant representing the substrate concentration at which the reaction rate in the liver is half of Vmax (Km).",
        (),
        False,
    ),
    "PBPKO_00215": (
        "gut metabolism",
        "A metabolism process specifically occurring within the gut.",
        (),
        False,
    ),
    "PBPKO_00216": (
        "dissociation constant",
        "A biochemical parameter (Kd) measuring the affinity of a compound for its binding partner (e.g., receptor, protein).",
        (),
        False,
    ),
    "PBPKO_00217": (
        "transporter",
        "A material entity representing protein responsible for the import or export of compounds across cell membranes.",
        (),
        False,
    ),
    "PBPKO_00218": (
        "oatp",
        "A transporter family (Organic Anion Transporting Polypeptides) involved in transporting organic anions.",
        (),
        False,
    ),
    "PBPKO_00219": (
        "abcc3",
        "A transporter (ATP-binding cassette subfamily C member 3) involved in bile metabolism and transport.",
        (),
        False,
    ),
    "PBPKO_00220": (
        "abcc2",
        "A transporter (ATP-binding cassette subfamily C member 2) involved in transporting various molecules across cell membranes.",
        (),
        False,
    ),
    "PBPKO_00221": (
        "degradation rate constant",
        "A biochemical parameter (kdeg) representing the rate constant for the degradation of a metabolizing enzyme or transporter.",
        (),
        False,
    ),
    "PBPKO_00222": (
        "inhibition constant",
        "A biochemical parameter (Ki) representing the inhibition constant for a specific enzyme or transporter interaction.",
        (),
        False,
    ),
    "PBPKO_00223": (
        "renal excretion",
        "An excretion process involving the elimination of compounds and metabolites primarily through urine via the kidneys.",
        (),
        False,
    ),
    "PBPKO_00224": (
        "hepatic excretion",
        "An excretion process involving the elimination of compounds and metabolites via the liver (often into bile).",
        (),
        False,
    ),
    "PBPKO_00225": (
        "fecal excretion",
        "An excretion process involving the elimination of compounds and metabolites through feces.",
        (),
        False,
    ),
    "PBPKO_00226": (
        "exhalation",
        "An excretion process involving the elimination of volatile compounds and metabolites through respiration.",
        (),
        False,
    ),
    "PBPKO_00227": (
        "sweat excretion",
        "An excretion process involving the elimination of compounds and metabolites through sweat.",
        (),
        False,
    ),
    "PBPKO_00228": (
        "hair excretion",
        "An excretion process involving the elimination and deposition of compounds and metabolites into hair.",
        (),
        False,
    ),
    "PBPKO_00229": (
        "clearance rate",
        "A biochemical parameter representing the volume of biological fluid cleared of a compound per unit time.",
        (),
        False,
    ),
    "PBPKO_00230": (
        "fecal clearance rate",
        "A clearance rate specifically quantifying elimination via feces.",
        (),
        False,
    ),
    "PBPKO_00231": (
        "sweat clearance rate",
        "A clearance rate specifically quantifying elimination via sweat.",
        (),
        False,
    ),
    "PBPKO_00232": (
        "urinary clearance rate",
        "A clearance rate specifically quantifying elimination via urine.",
        (),
        False,
    ),
    "PBPKO_00233": (
        "biliary clearance rate",
        "A clearance rate specifically quantifying elimination via bile.",
        (),
        False,
    ),
    "PBPKO_00234": (
        "hepatic clearance rate",
        "A clearance rate specifically quantifying elimination via the liver (metabolism and/or biliary excretion).",
        (),
        False,
    ),
    "PBPKO_00235": (
        "intrinsic clearance rate",
        "A clearance rate representing the inherent ability of an organ or tissue to eliminate a compound, independent of blood flow or binding.",
        (),
        False,
    ),
    "PBPKO_00236": (
        "fecal elimination rate constant",
        "A biochemical parameter representing the rate constant for elimination via fecal excretion.",
        (),
        False,
    ),
    "PBPKO_00237": (
        "renal elimination rate constant",
        "A biochemical parameter representing the rate constant for elimination via renal (urinary) excretion.",
        (),
        False,
    ),
    "PBPKO_00238": (
        "biliary elimination",
        "An elimination process involving the irreversible transfer of compound or metabolites from plasma to bile via hepatocytes.",
        (),
        False,
    ),
    "PBPKO_00239": (
        "route of exposure",
        "A parameter designating the body part or method through which exposure is introduced.",
        (),
        False,
    ),
    "PBPKO_00240": ("oral exposure", "A route of exposure via the mouth.", (), False),
    "PBPKO_00241": ("dermal exposure", "A route of exposure via the skin.", (), False),
    "PBPKO_00242": (
        "inhalation exposure",
        "A route of exposure via inhalation into the lungs.",
        (),
        False,
    ),
    "PBPKO_00243": (
        "intravenous bolus exposure",
        "A route of exposure involving rapid injection directly into a vein.",
        (),
        False,
    ),
    "PBPKO_00244": (
        "intravenous infusion exposure",
        "A route of exposure involving continuous administration directly into a vein over time.",
        (),
        False,
    ),
    "PBPKO_00245": (
        "intramuscular exposure",
        "A route of exposure involving injection into a muscle.",
        (),
        False,
    ),
    "PBPKO_00246": (
        "intraarterial exposure",
        "A route of exposure involving administration directly into an artery.",
        (),
        False,
    ),
    "PBPKO_00247": (
        "intrathecal exposure",
        "A route of exposure involving administration into the spinal canal.",
        (),
        False,
    ),
    "PBPKO_00248": (
        "subcutaneous exposure",
        "A route of exposure involving administration under the skin.",
        (),
        False,
    ),
    "PBPKO_00249": (
        "nasal exposure",
        "A route of exposure via the nasal passages.",
        (),
        False,
    ),
    "PBPKO_00250": (
        "transdermal exposure",
        "A route of exposure involving absorption through the skin, typically from a patch.",
        (),
        False,
    ),
    "PBPKO_00251": ("ocular exposure", "A route of exposure via the eye.", (), False),
    "PBPKO_00252": (
        "output parameter",
        "A parameter representing a result or prediction generated by the PBPK model.",
        (),
        False,
    ),
    "PBPKO_00253": (
        "peak concentration",
        "An output parameter representing the highest concentration (Cmax) of a compound achieved after exposure.",
        (),
        False,
    ),
    "PBPKO_00254": (
        "maximum steady state concentration",
        "An output parameter representing the maximum concentration (Cmax,ss) achieved at steady state during repeated dosing.",
        (),
        False,
    ),
    "PBPKO_00255": (
        "maximum time",
        "An output parameter representing the time (Tmax) required to reach the peak concentration.",
        (),
        False,
    ),
    "PBPKO_00256": (
        "area under curve",
        "An output parameter representing the integral of the concentration-time curve (AUC), indicating total exposure.",
        (),
        False,
    ),
    "PBPKO_00257": (
        "area under curve 0 to t",
        "An area under curve parameter calculated from time zero to a specific time point t (AUC0-t).",
        (),
        False,
    ),
    "PBPKO_00258": (
        "area under curve last",
        "An area under curve parameter calculated from time zero to the time of the last measurable concentration (AUClast).",
        (),
        False,
    ),
    "PBPKO_00259": (
        "area under curve 0 to infinity",
        "An area under curve parameter extrapolated from time zero to infinity (AUC0-inf), representing total exposure after a single dose.",
        (),
        False,
    ),
    "PBPKO_00260": (
        "area under moment curve",
        "An output parameter calculated as the integral of the product of time and concentration versus time (AUMC).",
        (),
        False,
    ),
    "PBPKO_00261": (
        "mean residence time",
        "An output parameter representing the average time a compound resides in the body (MRT).",
        (),
        False,
    ),
    "PBPKO_00262": (
        "half-life",
        "An output parameter representing the time required for the compound concentration to decrease by half (t1/2).",
        (),
        False,
    ),
    "PBPKO_00263": (
        "bioavailability",
        "An output parameter representing the rate and extent to which an active compound is absorbed and becomes available at the site of action or systemic circulation.",
        (),
        False,
    ),
    "PBPKO_00264": (
        "relative bioavailability",
        "A bioavailability parameter comparing the rate and extent of absorption of a test compound to a reference compound.",
        (),
        False,
    ),
    "PBPKO_00265": (
        "mean absorption time",
        "An output parameter representing the average time for a compound to be absorbed into systemic circulation (MAT).",
        (),
        False,
    ),
    "PBPKO_00266": (
        "mean dissolution time",
        "An output parameter representing the average time for a compound to dissolve in the body (MDT).",
        (),
        False,
    ),
    "PBPKO_00267": (
        "bioequivalence",
        "An output parameter indicating comparable bioavailability between test and reference formulations under similar conditions.",
        (),
        False,
    ),
    "PBPKO_00268": (
        "absolute bioavailability",
        "A bioavailability parameter comparing the amount reaching systemic circulation after non-IV administration to the amount available after IV administration.",
        (),
        False,
    ),
    "PBPKO_00269": (
        "elimination phase",
        "An elimination process phase describing the period where removal of the compound from the body predominates.",
        (),
        False,
    ),
    "PBPKO_00270": (
        "absorption phase",
        "An absorption process phase describing the period where the compound moves from the administration site into systemic circulation.",
        (),
        False,
    ),
    "PBPKO_00272": (
        "amount in urine",
        "The amount of compound in the urine compartment.",
        (),
        False,
    ),
    "PBPKO_00273": (
        "amount in feces",
        "The amount of compound in the feces compartment.",
        (),
        False,
    ),
    "PBPKO_00274": (
        "cumulative amount in urine",
        "An output parameter representing the total amount of compound excreted in urine over a specific time period.",
        (),
        False,
    ),
    "PBPKO_00275": (
        "cumulative amount in feces",
        "An output parameter representing the total amount of compound excreted in feces over a specific time period.",
        (),
        False,
    ),
    "PBPKO_00277": (
        "steady state area under curve",
        "An area under curve parameter calculated over a dosing interval at steady state (AUCss).",
        (),
        False,
    ),
    "PBPKO_00279": (
        "min organ concentration",
        "An output parameter representing the minimum concentration of a compound in a specific organ after exposure.",
        (),
        False,
    ),
    "PBPKO_00280": (
        "max organ concentration",
        "An output parameter representing the maximum concentration of a compound in a specific organ after exposure.",
        (),
        False,
    ),
    "PBPKO_00281": (
        "median organ concentration",
        "An output parameter representing the median concentration of a compound in a specific organ after exposure.",
        (),
        False,
    ),
    "PBPKO_00282": (
        "percentile 2.5 cplasma",
        "A plasma concentration parameter representing the 2.5th percentile of the plasma concentration distribution in a population simulation.",
        (),
        False,
    ),
    "PBPKO_00283": (
        "percentile 97.5 cplasma",
        "A plasma concentration parameter representing the 97.5th percentile of the plasma concentration distribution in a population simulation.",
        (),
        False,
    ),
    "PBPKO_00284": (
        "tolerable daily intake",
        "An output parameter (or exposure limit) estimating the amount of a substance that can be ingested daily over a lifetime without appreciable health risk (TDI).",
        (),
        False,
    ),
    "PBPKO_00285": (
        "reconstructed exposure",
        "An output parameter estimating the amount of compound exposure based on internal body measurements.",
        (),
        False,
    ),
    "PBPKO_00286": (
        "estimated daily intake",
        "An output parameter estimating the amount of a compound consumed daily (EDI).",
        (),
        False,
    ),
    "PBPKO_00287": (
        "biomonitoring equivalent",
        "An output parameter representing the concentration of a chemical (or metabolite) in a biological medium consistent with exposure guidance values (BE).",
        (),
        False,
    ),
    "PBPKO_00289": (
        "reference dose",
        "An output parameter (or exposure limit) estimating the daily oral or dermal exposure likely to be without appreciable risk over a lifetime (RfD).",
        (),
        False,
    ),
    "PBPKO_00290": (
        "acceptable daily intake",
        "An output parameter (or exposure limit) estimating the amount of a substance in food/water that can be consumed daily without appreciable health risk (ADI).",
        (),
        False,
    ),
    "PBPKO_00296": (
        "reference human data set",
        "A data set containing the physiological parameters representing a standard human, often defined by specific characteristics like 70 kg body weight.",
        (),
        False,
    ),
    "PBPKO_00297": (
        "biological matrix concentration",
        "An output parameter representing the total concentration of a compound in a specified biological matrix.",
        (),
        False,
    ),
    "PBPKO_00298": (
        "concentration in hair",
        "The total concentration of compound in the hair compartment.",
        (),
        False,
    ),
    "PBPKO_00299": (
        "concentration in nail",
        "A biological matrix concentration specifically representing the total concentration of compound in the nail compartment.",
        (),
        False,
    ),
    "PBPKO_00300": (
        "concentration in teeth",
        "A biological matrix concentration specifically representing the total concentration of compound in the teeth compartment.",
        (),
        False,
    ),
    "PBPKO_00301": (
        "concentration in blood",
        "The total concentration of compound in the blood compartment.",
        (),
        False,
    ),
    "PBPKO_00302": (
        "concentration in urine",
        "A biological matrix concentration specifically representing the total concentration of compound in the urine compartment.",
        (),
        False,
    ),
    "PBPKO_00303": (
        "permeability limited pbpk",
        "A physiologically based pharmacokinetic model that considers the permeability across membranes as a limiting factor for compound distribution.",
        (),
        False,
    ),
    "PBPKO_00304": (
        "maximum rate of basolateral transporter in vitro",
        "Maximum rate (Vmax) of transport via a basolateral transporter, measured in vitro.",
        (),
        False,
    ),
    "PBPKO_00305": (
        "Michaelis constant baso",
        "Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for a basolateral transporter.",
        (),
        False,
    ),
    "PBPKO_00306": (
        "maximum rate of apical transporter in vitro",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ, measured in vitro, when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    "PBPKO_00307": (
        "Michaelis constant apical",
        "Michaelis constant representing the substrate concentration at half-maximal velocity (Km) for an apical transporter.",
        (),
        False,
    ),
    "PBPKO_00310": (
        "influx constant",
        "A biochemical parameter (kin) describing the rate constant for compound movement into a cell or compartment.",
        (),
        False,
    ),
    "PBPKO_00311": (
        "efflux rate constant",
        "A biochemical parameter (kefflux) describing the rate constant for compound movement out of a cell or compartment.",
        (),
        False,
    ),
    "PBPKO_00312": (
        "plasma space",
        "A physiological parameter representing the volume occupied by plasma within a tissue or the body.",
        (),
        False,
    ),
    "PBPKO_00313": (
        "endosomal space compartment",
        "A compartment representing the endosomal space within cells.",
        (),
        False,
    ),
    "PBPKO_00314": (
        "interstitial space",
        "A physiological parameter representing the fluid-filled space between blood vessels and cells.",
        (),
        False,
    ),
    "PBPKO_00315": (
        "effective permeability",
        "A biochemical parameter (Peff) representing the rate at which a compound passes through a biological barrier (e.g., intestinal wall).",
        (),
        False,
    ),
    "PBPKO_00316": (
        "population pbpk",
        "A physiologically based pharmacokinetic model approach used to characterize interindividual variability within a population.",
        (),
        False,
    ),
    "PBPKO_00317": (
        "top-down pbpk",
        "A physiologically based pharmacokinetic model approach primarily based on fitting observed clinical data, often empirical.",
        (),
        False,
    ),
    "PBPKO_00318": (
        "bottom-up pbpk",
        "A physiologically based pharmacokinetic model approach built mechanistically using in vitro and physiological data.",
        (),
        False,
    ),
    "PBPKO_00319": (
        "one-compartment pbpk",
        "A physiologically based pharmacokinetic model that treats the entire body as a single, kinetically homogenous unit (central compartment).",
        (),
        False,
    ),
    "PBPKO_00320": (
        "central compartment",
        "A compartment in a multi-compartment model representing plasma and highly perfused tissues where distribution is rapid.",
        (),
        False,
    ),
    "PBPKO_00321": (
        "peripheral compartment",
        "A compartment in a multi-compartment model representing tissues where compound distribution is slower compared to the central compartment.",
        (),
        False,
    ),
    "PBPKO_00322": (
        "elimination",
        "A biological process involving the irreversible removal of a compound from the body, encompassing metabolism and excretion.",
        (),
        False,
    ),
    "PBPKO_00323": (
        "linear elimination",
        "An elimination process that follows first-order kinetics (rate proportional to concentration).",
        (),
        False,
    ),
    "PBPKO_00324": (
        "non-linear elimination",
        "An elimination process that does not follow first-order kinetics (e.g., saturable processes).",
        (),
        False,
    ),
    "PBPKO_00332": (
        "lifestage",
        "A physiological parameter representing distinct phases of an individual's life (e.g., infant, adult, geriatric).",
        (),
        False,
    ),
    "PBPKO_00333": (
        "fetus lifestage",
        "A lifestage parameter representing the unborn offspring from the postembryonic stage until birth.",
        (),
        False,
    ),
    "PBPKO_00334": (
        "infant lifestage",
        "A lifestage parameter representing a very young child, typically under one year of age.",
        (),
        False,
    ),
    "PBPKO_00335": (
        "toddler lifestage",
        "A lifestage parameter representing a young child, typically between one and three years old.",
        (),
        False,
    ),
    "PBPKO_00336": (
        "child lifestage",
        "A lifestage parameter representing individuals typically between 3 and 11 years old.",
        (),
        False,
    ),
    "PBPKO_00337": (
        "teenager lifestage",
        "A lifestage parameter representing individuals typically between eleven and fifteen years old.",
        (),
        False,
    ),
    "PBPKO_00338": (
        "adolescent lifestage",
        "A lifestage parameter representing the transitional stage between teenager and adulthood (approx. 15-18 years).",
        (),
        False,
    ),
    "PBPKO_00339": (
        "adult lifestage",
        "A lifestage parameter representing individuals typically from eighteen to thirty years old.",
        (),
        False,
    ),
    "PBPKO_00340": (
        "middle age lifestage",
        "A lifestage parameter representing individuals typically from thirty to forty-five years old.",
        (),
        False,
    ),
    "PBPKO_00341": (
        "old age lifestage",
        "A lifestage parameter representing individuals typically from forty-five to sixty years old (or older, definitions vary).",
        (),
        False,
    ),
    "PBPKO_00342": (
        "pediatric lifestage",
        "A lifestage parameter representing individuals typically below fifteen years of age.",
        (),
        False,
    ),
    "PBPKO_00343": (
        "geriatric lifestage",
        "A lifestage parameter representing older adults, often considered 60/65 years and older.",
        (),
        False,
    ),
    "PBPKO_00347": (
        "brain pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations in the brain.",
        (),
        False,
    ),
    "PBPKO_00348": (
        "cerebrospinal fluid volume",
        "A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the spinal region.",
        (),
        False,
    ),
    "PBPKO_00349": (
        "cranial cerebrospinal fluid volume",
        "A volume parameter representing the total volume of cerebrospinal fluid (CSF) compartment in the cranial region.",
        (),
        False,
    ),
    "PBPKO_00350": (
        "brain mass",
        "A physiological parameter representing the mass of the brain.",
        (),
        False,
    ),
    "PBPKO_00351": (
        "blood brain barrier compartment",
        "A barrier compartment representing the blood-brain barrier (BBB).",
        (),
        False,
    ),
    "PBPKO_00352": (
        "spinal cerebrospinal fluid flow rate",
        "A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the spinal region.",
        (),
        False,
    ),
    "PBPKO_00353": (
        "cranial cerebrospinal fluid flow rate",
        "A bodily fluid flow rate parameter representing the flow rate of cerebrospinal fluid (CSF) compartment in the cranial region.",
        (),
        False,
    ),
    "PBPKO_00354": (
        "blood cerebrospinal fluid compartment",
        "A barrier compartment representing the blood-cerebrospinal fluid barrier (BCSFB).",
        (),
        False,
    ),
    "PBPKO_00355": (
        "volume of hippocampus",
        "A volume parameter representing the total volume of the hippocampus compartment.",
        (),
        False,
    ),
    "PBPKO_00356": (
        "volume of frontal cortex",
        "A volume parameter representing the total volume of the frontal cortex compartment.",
        (),
        False,
    ),
    "PBPKO_00357": (
        "volume of cerebrum",
        "A volume parameter representing the total volume of the cerebrum compartment.",
        (),
        False,
    ),
    "PBPKO_00358": (
        "volume of cerebellum",
        "A volume parameter representing the total volume of the cerebellum compartment.",
        (),
        False,
    ),
    "PBPKO_00359": (
        "blood flow rate to hippocampus",
        "A blood flow rate parameter specifically describing the rate to the hippocampus compartment.",
        (),
        False,
    ),
    "PBPKO_00360": (
        "blood flow rate to frontal cortex",
        "A blood flow rate parameter specifically describing the rate to the frontal cortex compartment.",
        (),
        False,
    ),
    "PBPKO_00361": (
        "blood flow rate to cerebrum",
        "A blood flow rate parameter specifically describing the rate to the cerebrum compartment.",
        (),
        False,
    ),
    "PBPKO_00362": (
        "blood flow rate to cerebellum",
        "A blood flow rate parameter specifically describing the rate to the cerebellum compartment.",
        (),
        False,
    ),
    "PBPKO_00363": (
        "hippocampus brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the hippocampus to the overall brain.",
        (),
        False,
    ),
    "PBPKO_00364": (
        "cerebrum brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the cerebrum to the overall brain.",
        (),
        False,
    ),
    "PBPKO_00365": (
        "cerebellum brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the cerebellum to the overall brain.",
        (),
        False,
    ),
    "PBPKO_00366": (
        "frontalcortex brain partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the frontal cortex to the overall brain.",
        (),
        False,
    ),
    "PBPKO_00367": (
        "apparent permeability cerebrum to rest of brain",
        "Apparent permeability of a compound specifically between the cerebrum and the rest of the brain.",
        (),
        False,
    ),
    "PBPKO_00368": (
        "apparent permeability cerebellum to rest of brain",
        "Apparent permeability of a compound specifically between the cerebellum and the rest of the brain.",
        (),
        False,
    ),
    "PBPKO_00369": (
        "apparent permeability hippocampus to rest of brain",
        "Apparent permeability of a compound specifically between the hippocampus and the rest of the brain.",
        (),
        False,
    ),
    "PBPKO_00370": (
        "apparent permeability cortex to rest of brain",
        "Apparent permeability of a compound specifically between the cortex and the rest of the brain.",
        (),
        False,
    ),
    "PBPKO_00371": (
        "pregnant pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations during pregnancy.",
        (),
        False,
    ),
    "PBPKO_00372": (
        "fetoplacental volume",
        "A volume parameter representing the total volume of the placental compartment for fetus.",
        (),
        False,
    ),
    "PBPKO_00373": (
        "volume of fetus",
        "A volume parameter representing the total volume of the fetus.",
        (),
        False,
    ),
    "PBPKO_00374": (
        "volume of placenta",
        "A volume parameter representing the total volume of the placental compartment.",
        (),
        False,
    ),
    "PBPKO_00375": (
        "volume of amniotic fluid",
        "A volume parameter representing the total volume of the amniotic fluid compartment.",
        (),
        False,
    ),
    "PBPKO_00376": (
        "volume of liver fetus",
        "A volume parameter representing the total volume of the fetal liver compartment.",
        (),
        False,
    ),
    "PBPKO_00377": (
        "volume of brain fetus",
        "A volume parameter representing the total volume of the fetal brain compartment.",
        (),
        False,
    ),
    "PBPKO_00378": (
        "volume of kidney fetus",
        "A volume parameter representing the total volume of the fetal kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00379": (
        "volume of rest body fetus",
        "A volume parameter representing the total volume of the rest of body compartment within the fetus.",
        (),
        False,
    ),
    "PBPKO_00381": (
        "fetoplacental blood flow rate",
        "A blood flow rate parameter representing the rate of blood flow between the fetus and the placenta compartment.",
        (),
        False,
    ),
    "PBPKO_00382": (
        "fetal cardiac output rate",
        "A blood flow rate parameter representing the volume of blood pumped by the fetal heart compartment per unit time.",
        (),
        False,
    ),
    "PBPKO_00383": (
        "blood flow rate to liverfetus",
        "A blood flow rate parameter specifically describing the rate to the fetal liver compartment.",
        (),
        False,
    ),
    "PBPKO_00384": (
        "blood flow rate to kidneyfetus",
        "A blood flow rate parameter specifically describing the rate to the fetal kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00385": (
        "blood flow rate to brain fetus",
        "A blood flow rate parameter specifically describing the rate to the fetal brain compartment.",
        (),
        False,
    ),
    "PBPKO_00386": (
        "blood flow rate to restbody fetus",
        "A blood flow rate parameter specifically describing the rate to the rest of body compartment within the fetus.",
        (),
        False,
    ),
    "PBPKO_00387": (
        "gestational age",
        "A physiological parameter representing the age of a pregnancy, typically measured in weeks.",
        (),
        False,
    ),
    "PBPKO_00388": (
        "gestational week",
        "A physiological parameter representing the specific week of gestation.",
        (),
        False,
    ),
    "PBPKO_00389": (
        "maximum rate in fetus",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound in fetus when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    "PBPKO_00390": (
        "amniotic transfer coefficient",
        "A biochemical parameter representing the rate at which a compound transfers from maternal circulation to amniotic fluid.",
        (),
        False,
    ),
    "PBPKO_00391": (
        "liverfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal liver to plasma.",
        (),
        False,
    ),
    "PBPKO_00392": (
        "brainfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal brain to plasma.",
        (),
        False,
    ),
    "PBPKO_00393": (
        "kidneyfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal kidney to plasma.",
        (),
        False,
    ),
    "PBPKO_00394": (
        "restbodyfetus plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to plasma.",
        (),
        False,
    ),
    "PBPKO_00395": (
        "kidney pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the kidney compartments.",
        (),
        False,
    ),
    "PBPKO_00396": (
        "Bowman's capsule compartment",
        "A kidney compartment representing the Bowman's capsule.",
        (),
        False,
    ),
    "PBPKO_00397": (
        "filtrate compartment",
        "A kidney compartment representing the filtrate within the nephron.",
        (),
        False,
    ),
    "PBPKO_00398": (
        "proximal tubule compartment",
        "A kidney compartment representing the proximal tubule of the nephron.",
        (),
        False,
    ),
    "PBPKO_00399": (
        "loop of Henle compartment",
        "A kidney compartment representing the loop of Henle within the nephron.",
        (),
        False,
    ),
    "PBPKO_00400": (
        "distal tubule compartment",
        "A kidney compartment representing the distal tubule of the nephron.",
        (),
        False,
    ),
    "PBPKO_00401": (
        "collecting duct compartment",
        "A kidney compartment representing the collecting duct system.",
        (),
        False,
    ),
    "PBPKO_00402": (
        "bladder compartment",
        "A compartment representing the urinary bladder.",
        (),
        False,
    ),
    "PBPKO_00403": (
        "lung pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the lung compartments.",
        (),
        False,
    ),
    "PBPKO_00404": (
        "extrathoracic compartment",
        "A compartment representing the extrathoracic region (head, neck, upper respiratory tract).",
        (),
        False,
    ),
    "PBPKO_00405": (
        "thoracic compartment",
        "A compartment representing the thoracic region (chest).",
        (),
        False,
    ),
    "PBPKO_00406": (
        "bronchiolar compartment",
        "A lung compartment representing the bronchioles.",
        (),
        False,
    ),
    "PBPKO_00407": (
        "alveolar compartment",
        "A lung compartment representing the alveoli.",
        (),
        False,
    ),
    "PBPKO_00408": (
        "gut pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations within the gut compartments.",
        (),
        False,
    ),
    "PBPKO_00409": (
        "fraction of blood flow to duodenum",
        "The dimensionless fraction of cardiac output delivered to the duodenum compartment.",
        (),
        False,
    ),
    "PBPKO_00410": (
        "fraction of blood flow to jejunum",
        "The dimensionless fraction of cardiac output delivered to the jejunum compartment.",
        (),
        False,
    ),
    "PBPKO_00411": (
        "fraction of blood flow to ileum",
        "The dimensionless fraction of cardiac output delivered to the ileum compartment.",
        (),
        False,
    ),
    "PBPKO_00412": (
        "fraction of blood flow to colon",
        "The dimensionless fraction of cardiac output delivered to the colon compartment.",
        (),
        False,
    ),
    "PBPKO_00413": (
        "fraction of blood flow to cecum",
        "The dimensionless fraction of cardiac output delivered to the cecum compartment.",
        (),
        False,
    ),
    "PBPKO_00414": (
        "blood flow rate to duodenum",
        "A blood flow rate parameter specifically describing the rate to the duodenum compartment.",
        (),
        False,
    ),
    "PBPKO_00415": (
        "blood flow rate to jejunum",
        "A blood flow rate parameter specifically describing the rate to the jejunum compartment.",
        (),
        False,
    ),
    "PBPKO_00416": (
        "blood flow rate to ileum",
        "A blood flow rate parameter specifically describing the rate to the ileum compartment.",
        (),
        False,
    ),
    "PBPKO_00417": (
        "blood flow rate to colon",
        "A blood flow rate parameter specifically describing the rate to the colon compartment.",
        (),
        False,
    ),
    "PBPKO_00418": (
        "blood flow rate to cecum",
        "A blood flow rate parameter specifically describing the rate to the cecum compartment.",
        (),
        False,
    ),
    "PBPKO_00419": (
        "fraction of duodenum",
        "A dimensionless fraction of volume defined as the duodenum volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00420": (
        "fraction of jejunum",
        "A dimensionless fraction of volume defined as the jejunum volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00421": (
        "fraction of ileum",
        "A dimensionless fraction of volume defined as the ileum volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00422": (
        "fraction of colon",
        "A dimensionless fraction of volume defined as the colon volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00423": (
        "fraction of cecum",
        "A dimensionless fraction of volume defined as the cecum volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00424": (
        "volume of duodenum",
        "A volume parameter representing the total volume of the duodenum compartment.",
        (),
        False,
    ),
    "PBPKO_00425": (
        "volume of jejunum",
        "A volume parameter representing the total volume of the jejunum compartment.",
        (),
        False,
    ),
    "PBPKO_00426": (
        "volume of ileum",
        "A volume parameter representing the total volume of the ileum compartment.",
        (),
        False,
    ),
    "PBPKO_00427": (
        "volume of colon",
        "A volume parameter representing the total volume of the colon compartment.",
        (),
        False,
    ),
    "PBPKO_00428": (
        "volume of cecum",
        "A volume parameter representing the total volume of the cecum compartment.",
        (),
        False,
    ),
    "PBPKO_00429": (
        "bile salt effect solubilization ratio",
        "A biochemical parameter representing the ratio of molecules solubilized due to bile salt presence.",
        (),
        False,
    ),
    "PBPKO_00430": (
        "mean precipitation time",
        "A biochemical parameter representing the average time for a compound to precipitate under specific conditions (e.g., in the GI tract).",
        (),
        False,
    ),
    "PBPKO_00431": (
        "diffusion coefficient",
        "A physicochemical parameter representing the amount of substance diffusing across a unit area per unit time under a unit concentration gradient.",
        (),
        False,
    ),
    "PBPKO_00432": (
        "particle density",
        "A biochemical/physical parameter representing the mass per unit volume of particles (e.g., of the administered compound).",
        (),
        False,
    ),
    "PBPKO_00433": (
        "particle radius",
        "A biochemical/physical parameter representing the radius of particles (e.g., of the administered compound).",
        (),
        False,
    ),
    "PBPKO_00434": (
        "intestinal transit time",
        "A biochemical parameter representing the time required for a compound to move through the intestine.",
        (),
        False,
    ),
    "PBPKO_00435": (
        "lactational pbpk",
        "A physiologically based pharmacokinetic model specifically built to predict compound concentrations during lactation, including transfer into milk.",
        (),
        False,
    ),
    "PBPKO_00436": (
        "milk plasma ratio",
        "A biochemical parameter representing the ratio of compound concentration in milk to plasma.",
        (),
        False,
    ),
    "PBPKO_00437": (
        "fraction unbound milk",
        "An unbound fraction parameter specifically for milk.",
        (),
        False,
    ),
    "PBPKO_00438": (
        "concentration in milk",
        "The total concentration of compound in the milk compartment.",
        (),
        False,
    ),
    "PBPKO_00439": (
        "daily milk intake",
        "A physiological parameter representing the daily volume of milk ingested (e.g., by an infant).",
        (),
        False,
    ),
    "PBPKO_00440": (
        "phmilk",
        "A biochemical parameter representing the pH of milk.",
        (),
        False,
    ),
    "PBPKO_00441": (
        "blood milk barrier compartment",
        "A barrier compartment representing the physiological barrier separating blood and milk in lactating species.",
        (),
        False,
    ),
    "PBPKO_00442": (
        "milk plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in milk to plasma.",
        (),
        False,
    ),
    "PBPKO_00446": (
        "compartment",
        "A data representation model component representing a distinct physiological space (organ, tissue, fluid) where ADME processes occur.",
        (),
        False,
    ),
    "PBPKO_00448": (
        "alveolar air compartment",
        "A lung compartment specifically representing the air within the alveoli.",
        (),
        False,
    ),
    "PBPKO_00450": (
        "rest of body compartment",
        "A compartment representing the lumped remainder of the body not explicitly modeled as separate organs/tissues.",
        (),
        False,
    ),
    "PBPKO_00451": (
        "arterial plasma",
        "A compartment representing the plasma specifically within the arterial blood.",
        (),
        False,
    ),
    "PBPKO_00452": (
        "venous plasma compartment",
        "A compartment representing the plasma specifically within the venous blood.",
        (),
        False,
    ),
    "PBPKO_00453": (
        "richly perfused tissue compartment",
        "A compartment representing lumped tissues with high blood flow relative to their volume.",
        (),
        False,
    ),
    "PBPKO_00454": (
        "poorly perfused tissue compartment",
        "A compartment representing lumped tissues with low blood flow relative to their volume.",
        (),
        False,
    ),
    "PBPKO_00455": (
        "viable unexposed skin compartment",
        "A skin compartment representing the viable layers of skin not directly exposed to the applied compound.",
        (),
        False,
    ),
    "PBPKO_00456": (
        "viable exposed skin compartment",
        "A skin compartment representing the viable layers of skin directly exposed to the applied compound.",
        (),
        False,
    ),
    "PBPKO_00457": (
        "skin unexposed stratum corneum",
        "A stratum corneum compartment representing the portion not directly exposed to the applied compound.",
        (),
        False,
    ),
    "PBPKO_00458": (
        "skin exposed stratum corneum compartment",
        "A stratum corneum compartment representing the portion directly exposed to the applied compound.",
        (),
        False,
    ),
    "PBPKO_00460": (
        "adipose compartment",
        "A compartment representing adipose (fat) tissue.",
        (),
        False,
    ),
    "PBPKO_00461": (
        "anal canal compartment",
        "A large intestine compartment representing the anal canal.",
        (),
        False,
    ),
    "PBPKO_00462": (
        "appendix compartment",
        "A large intestine compartment representing the appendix.",
        (),
        False,
    ),
    "PBPKO_00463": (
        "ascending colon compartment",
        "A large intestine compartment representing the ascending colon.",
        (),
        False,
    ),
    "PBPKO_00464": (
        "blood compartment",
        "A compartment representing the entirety of the blood (including plasma and cells).",
        (),
        False,
    ),
    "PBPKO_00465": (
        "bone marrow compartment",
        "A compartment representing the bone marrow.",
        (),
        False,
    ),
    "PBPKO_00466": (
        "brain compartment",
        "A compartment representing the brain.",
        (),
        False,
    ),
    "PBPKO_00467": (
        "cecum compartment",
        "A large intestine compartment representing the cecum.",
        (),
        False,
    ),
    "PBPKO_00468": (
        "descending colon compartment",
        "A large intestine compartment representing the descending colon.",
        (),
        False,
    ),
    "PBPKO_00469": (
        "dermis compartment",
        "A skin compartment representing the dermis layer.",
        (),
        False,
    ),
    "PBPKO_00470": (
        "skin compartment",
        "A compartment representing the skin.",
        (),
        False,
    ),
    "PBPKO_00471": (
        "duodenum compartment",
        "A small intestine compartment representing the duodenum.",
        (),
        False,
    ),
    "PBPKO_00472": (
        "small intestine compartment",
        "A digestive system compartment representing the small intestine.",
        (),
        False,
    ),
    "PBPKO_00473": (
        "endocrine gland compartment",
        "A compartment representing endocrine glands.",
        (),
        False,
    ),
    "PBPKO_00474": (
        "large intestine compartment",
        "A digestive system compartment representing the large intestine.",
        (),
        False,
    ),
    "PBPKO_00475": (
        "epidermis compartment",
        "A skin compartment representing the epidermis layer.",
        (),
        False,
    ),
    "PBPKO_00476": (
        "gall bladder compartment",
        "A digestive system compartment representing the gall bladder.",
        (),
        False,
    ),
    "PBPKO_00477": (
        "gut compartment",
        "A digestive system compartment representing the gut (general term, often synonymous with intestine or GI tract).",
        (),
        False,
    ),
    "PBPKO_00478": (
        "gut lumen compartment",
        "A digestive system compartment representing the lumen (opening) within the gut.",
        (),
        False,
    ),
    "PBPKO_00479": ("hair compartment", "A compartment representing hair.", (), False),
    "PBPKO_00480": (
        "heart compartment",
        "A compartment representing the heart.",
        (),
        False,
    ),
    "PBPKO_00481": (
        "ileum compartment",
        "A small intestine compartment representing the ileum.",
        (),
        False,
    ),
    "PBPKO_00482": (
        "jejunum compartment",
        "A small intestine compartment representing the jejunum.",
        (),
        False,
    ),
    "PBPKO_00483": (
        "mammary gland compartment",
        "A compartment representing the mammary gland.",
        (),
        False,
    ),
    "PBPKO_00484": (
        "muscle compartment",
        "A compartment representing muscle tissue.",
        (),
        False,
    ),
    "PBPKO_00485": ("nail compartment", "A compartment representing nails.", (), False),
    "PBPKO_00486": (
        "pancreas compartment",
        "A compartment representing the pancreas.",
        (),
        False,
    ),
    "PBPKO_00487": (
        "placental barrier compartment",
        "A barrier compartment representing the placental barrier separating maternal and fetal circulation.",
        (),
        False,
    ),
    "PBPKO_00488": (
        "plasma compartment",
        "A compartment representing blood plasma.",
        (),
        False,
    ),
    "PBPKO_00489": (
        "rectum compartment",
        "A large intestine compartment representing the rectum.",
        (),
        False,
    ),
    "PBPKO_00490": (
        "reproductive compartment",
        "A compartment representing reproductive organs (gonads).",
        (),
        False,
    ),
    "PBPKO_00491": (
        "sigmoid colon compartment",
        "A large intestine compartment representing the sigmoid colon.",
        (),
        False,
    ),
    "PBPKO_00492": (
        "spleen compartment",
        "A compartment representing the spleen.",
        (),
        False,
    ),
    "PBPKO_00493": (
        "stratum corneum compartment",
        "A skin compartment representing the stratum corneum layer.",
        (),
        False,
    ),
    "PBPKO_00494": (
        "transverse colon compartment",
        "A large intestine compartment representing the transverse colon.",
        (),
        False,
    ),
    "PBPKO_00495": (
        "barrier compartment",
        "A compartment representing a physiological barrier limiting compound movement.",
        (),
        False,
    ),
    "PBPKO_00496": (
        "amount in gut",
        "The amount of compound in the gut compartment.",
        (),
        False,
    ),
    "PBPKO_00497": (
        "amount in liver",
        "The amount of compound in the liver compartment.",
        (),
        False,
    ),
    "PBPKO_00498": (
        "amount in kidney",
        "The amount of compound in the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00499": (
        "amount in filtrate",
        "The amount of compound in the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_00500": (
        "amount in delay",
        "The amount of compound in the hypothetical delay compartment.",
        (),
        False,
    ),
    "PBPKO_00501": (
        "amount in restbody",
        "The amount of compound in the rest of the body compartment.",
        (),
        False,
    ),
    "PBPKO_00502": (
        "amount in plasma",
        "The amount of compound in the plasma compartment.",
        (),
        False,
    ),
    "PBPKO_00503": (
        "amount in brain",
        "The amount of compound in the brain compartment.",
        (),
        False,
    ),
    "PBPKO_00504": (
        "amount in lung",
        "The amount of compound in the lung compartment.",
        (),
        False,
    ),
    "PBPKO_00505": (
        "amount in bone marrow",
        "The amount of compound in the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_00506": (
        "amount in skin",
        "The amount of compound in the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00507": (
        "amount in mammary gland",
        "The amount of compound in the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_00508": (
        "fraction of filtrate",
        "A dimensionless fraction of volume defined as the filtrate volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00509": (
        "fraction of gut",
        "A dimensionless fraction of volume defined as the gut volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00510": (
        "fraction of mammary gland",
        "A dimensionless fraction of volume defined as the mammary gland volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00511": (
        "fraction of blood flow to filtrate",
        "The dimensionless fraction of cardiac output delivered to the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_00512": (
        "fraction of blood flow to bone marrow",
        "The dimensionless fraction of cardiac output delivered to the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_00513": (
        "fraction of blood flow to gut",
        "The dimensionless fraction of cardiac output delivered to the gut compartment.",
        (),
        False,
    ),
    "PBPKO_00514": (
        "fraction of blood flow to mammary gland",
        "The dimensionless fraction of cardiac output delivered to the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_00515": (
        "brain plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the brain to plasma.",
        (),
        False,
    ),
    "PBPKO_00517": (
        "mammary gland plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the mammary gland to plasma.",
        (),
        False,
    ),
    "PBPKO_00518": (
        "restbody plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the rest of body compartment to plasma.",
        (),
        False,
    ),
    "PBPKO_00519": (
        "tissue plasma partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in a generic tissue to plasma.",
        (),
        False,
    ),
    "PBPKO_00520": (
        "urinary rate constant",
        "A biochemical parameter (rate constant) representing the rate at which a compound is cleared via urine, often scaled by body weight.",
        (),
        False,
    ),
    "PBPKO_00521": (
        "age in PBPK model",
        "A physiological parameter representing the period of lifespan (typically in years) for which the model is simulated.",
        (),
        False,
    ),
    "PBPKO_00522": (
        "volume of filtrate",
        "A volume parameter representing the total volume of the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_00523": (
        "volume of bone marrow",
        "A volume parameter representing the total volume of the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_00524": (
        "volume of gut",
        "A volume parameter representing the total volume of the gut compartment.",
        (),
        False,
    ),
    "PBPKO_00525": (
        "volume of mammary gland",
        "A volume parameter representing the total volume of the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_00526": (
        "volume of mass balance",
        "A volume parameter representing the check for total mass balance of all compartments (sum of organ volumes should equal body volume/weight equivalent, depending on units).",
        (),
        False,
    ),
    "PBPKO_00527": (
        "hematocrit volume",
        "A volume parameter representing the total volume of red blood cells in whole blood.",
        (),
        False,
    ),
    "PBPKO_00528": (
        "cardiac output rate of plasma",
        "A blood flow rate parameter representing the cardiac output specifically related to plasma flow.",
        (),
        False,
    ),
    "PBPKO_00529": (
        "blood flow rate to filtrate",
        "A blood flow rate parameter specifically describing the rate to the filtrate compartment (representing glomerular filtration).",
        (),
        False,
    ),
    "PBPKO_00530": (
        "blood flow rate to bone marrow",
        "A blood flow parameter specifically describing the rate to the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_00531": (
        "blood flow rate to gut",
        "A blood flow rate parameter specifically describing the rate to the gut compartment.",
        (),
        False,
    ),
    "PBPKO_00532": (
        "blood flow rate to mammary gland",
        "A blood flow rate parameter specifically describing the rate to the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_00533": (
        "blood flow rate for mass balance",
        "A blood flow rate parameter representing the check for total blood flow mass balance of all the compartments (sum of organ flows should equal cardiac output).",
        (),
        False,
    ),
    "PBPKO_00534": (
        "urinary rate",
        "A biochemical parameter representing the rate at which a compound is cleared via urine.",
        (),
        False,
    ),
    "PBPKO_00535": (
        "resorption maximum",
        "A biochemical parameter (Tm) representing the maximum rate of tubular resorption (e.g., in the kidney).",
        (),
        False,
    ),
    "PBPKO_00536": (
        "resorption",
        "A biochemical parameter or process representing the resorption of a compound (e.g., tubular resorption).",
        (),
        False,
    ),
    "PBPKO_00537": (
        "octanol air partition coefficient",
        "A partition coefficient (Koa) representing the ratio of compound concentration in octanol to air at equilibrium.",
        (),
        False,
    ),
    "PBPKO_00538": (
        "concentration in gut",
        "The total concentration of compound in the gut compartment.",
        (),
        False,
    ),
    "PBPKO_00539": (
        "concentration in liver",
        "The total concentration of compound in the liver compartment.",
        (),
        False,
    ),
    "PBPKO_00540": (
        "concentration in brain",
        "The total concentration of compound in the brain compartment.",
        (),
        False,
    ),
    "PBPKO_00541": (
        "concentration in kidney",
        "The total concentration of compound in the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_00542": (
        "concentration in filtrate",
        "The total concentration of compound in the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_00543": (
        "concentration in lung",
        "The total concentration of compound in the lung compartment.",
        (),
        False,
    ),
    "PBPKO_00544": (
        "concentration in fat",
        "The total concentration of compound in the fat compartment.",
        (),
        False,
    ),
    "PBPKO_00545": (
        "concentration in bone marrow",
        "The total concentration of compound in the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_00546": (
        "concentration in skin",
        "The total concentration of compound in the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00547": (
        "concentration in mammary gland",
        "The total concentration of compound in the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_00548": (
        "concentration in restbody",
        "The total concentration of compound in the rest of body compartment.",
        (),
        False,
    ),
    "PBPKO_00549": (
        "concentration in plasma",
        "The total concentration of compound in the plasma compartment.",
        (),
        False,
    ),
    "PBPKO_00550": (
        "amount in fat",
        "The amount of compound in the fat compartment.",
        (),
        False,
    ),
    "PBPKO_00551": (
        "PBPK model simulation time",
        "A parameter representing the time duration over which the model simulation runs.",
        (),
        False,
    ),
    "PBPKO_00552": (
        "arterial blood compartment",
        "A compartment representing the arterial blood.",
        (),
        False,
    ),
    "PBPKO_00553": (
        "digestive system compartment",
        "A compartment representing the digestive system or parts thereof.",
        (),
        False,
    ),
    "PBPKO_00554": (
        "excreta compartment",
        "A compartment representing material eliminated from the body (e.g., urine, feces).",
        (),
        False,
    ),
    "PBPKO_00555": (
        "feces compartment",
        "An excreta compartment specifically representing feces.",
        (),
        False,
    ),
    "PBPKO_00556": (
        "urine compartment",
        "An excreta compartment specifically representing urine.",
        (),
        False,
    ),
    "PBPKO_00557": (
        "kidney compartment",
        "A compartment representing the kidney(s).",
        (),
        False,
    ),
    "PBPKO_00558": (
        "liver compartment",
        "A compartment representing the liver.",
        (),
        False,
    ),
    "PBPKO_00559": (
        "lung compartment",
        "A compartment representing the lung(s).",
        (),
        False,
    ),
    "PBPKO_00561": (
        "venous blood compartment",
        "A compartment representing the venous blood.",
        (),
        False,
    ),
    "PBPKO_00562": (
        "blood flow rate to unexposed skin",
        "A blood flow rate to skin parameter specifically describing the rate to the unexposed portion of the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00563": (
        "blood flow rate to exposed skin",
        "A blood flow rate to skin parameter specifically describing the rate to the exposed portion of the skin compartment.",
        (),
        False,
    ),
    "PBPKO_00564": (
        "blood flow rate to skin stratum corneum unexposed",
        "A blood flow rate to skin parameter specifically describing the rate to the unexposed stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_00565": (
        "blood flow rate to skin stratum corneum exposed",
        "A blood flow rate to skin parameter specifically describing the rate to the exposed stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_00566": (
        "stomach compartment",
        "A digestive system compartment representing the stomach.",
        (),
        False,
    ),
    "PBPKO_00567": (
        "bone blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in bone to blood.",
        (),
        False,
    ),
    "PBPKO_00568": (
        "air blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in air to blood.",
        (),
        False,
    ),
    "PBPKO_00569": (
        "brain blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in brain to blood.",
        (),
        False,
    ),
    "PBPKO_00570": (
        "brainfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal brain to blood.",
        (),
        False,
    ),
    "PBPKO_00571": (
        "gonad blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in gonads to blood.",
        (),
        False,
    ),
    "PBPKO_00572": (
        "gut blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the gut to blood.",
        (),
        False,
    ),
    "PBPKO_00573": (
        "heart blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the heart to blood.",
        (),
        False,
    ),
    "PBPKO_00574": (
        "intestine blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the intestine to blood.",
        (),
        False,
    ),
    "PBPKO_00575": (
        "kidney blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the kidney to blood.",
        (),
        False,
    ),
    "PBPKO_00576": (
        "kidneyfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal kidney to blood.",
        (),
        False,
    ),
    "PBPKO_00577": (
        "liver blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the liver to blood.",
        (),
        False,
    ),
    "PBPKO_00578": (
        "liverfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal liver to blood.",
        (),
        False,
    ),
    "PBPKO_00579": (
        "lung blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the lung to blood.",
        (),
        False,
    ),
    "PBPKO_00580": (
        "mammary gland blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the mammary gland to blood.",
        (),
        False,
    ),
    "PBPKO_00581": (
        "milk blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in milk to blood.",
        (),
        False,
    ),
    "PBPKO_00582": (
        "muscle blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in muscle to blood.",
        (),
        False,
    ),
    "PBPKO_00583": (
        "pancreas blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the pancreas to blood.",
        (),
        False,
    ),
    "PBPKO_00584": (
        "poor perfused blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the poorly perfused compartment to blood.",
        (),
        False,
    ),
    "PBPKO_00585": (
        "restbody blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the rest of body compartment to blood.",
        (),
        False,
    ),
    "PBPKO_00586": (
        "restbodyfetus blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the fetal rest of body compartment to blood.",
        (),
        False,
    ),
    "PBPKO_00587": (
        "rich perfused blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the richly perfused compartment to blood.",
        (),
        False,
    ),
    "PBPKO_00588": (
        "skin blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the skin to blood.",
        (),
        False,
    ),
    "PBPKO_00589": (
        "spleen blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the spleen to blood.",
        (),
        False,
    ),
    "PBPKO_00590": (
        "stomach blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in the stomach to blood.",
        (),
        False,
    ),
    "PBPKO_00591": (
        "fraction unbound plasma",
        "An unbound fraction parameter specifically for plasma.",
        (),
        False,
    ),
    "PBPKO_00592": (
        "maximum rate of apical transporter",
        "A maximum rate (Vmax) of an enzyme catalysed reaction for a compound across the apical membrane of an organ when the enzyme is saturated with substrate.",
        (),
        False,
    ),
    "PBPKO_00593": (
        "maximum rate of basolateral transporter",
        "Maximum rate (Vmax) of transport via a basolateral transporter.",
        (),
        False,
    ),
    "PBPKO_00610": (
        "fraction of volume of compartment",
        "A physiological parameter representing the dimensionless fraction computed by dividing the volume of the compartment by the total body weight.",
        (),
        False,
    ),
    "PBPKO_00611": (
        "fraction of blood flow to a compartment",
        "A physiological parameter representing dimensionless fraction of cardiac output delivered to a compartment.",
        (),
        False,
    ),
    "PBPKO_00612": (
        "apparent permeability",
        "A biochemical parameter representing the apparent permeability of a compound specifically between the compartments.",
        (),
        False,
    ),
    "PBPKO_00613": (
        "maximum rate",
        "A biochemical parameter representing Vmax of the enzymatic activity",
        (),
        False,
    ),
    "PBPKO_00615": (
        "amount of compound in compartment",
        "An output parameter representing the amount of chemical specifically in the compartment",
        (),
        False,
    ),
    "PBPKO_00616": (
        "concentration of compound in compartment",
        "An output parameter representing the total concentration of compound in the compartment.",
        (),
        False,
    ),
    "PBPKO_00617": (
        "hippocampus compartment",
        "A part of brain compartment representing the hippocampus region of the brain",
        (),
        False,
    ),
    "PBPKO_00618": (
        "cerebrum compartment",
        "A part of brain compartment representing the cerebrum region of the brain",
        (),
        False,
    ),
    "PBPKO_00619": (
        "cerebellum compartment",
        "A part of brain compartment representing the cerebellum region of the brain",
        (),
        False,
    ),
    "PBPKO_00620": (
        "frontal cortex compartment",
        "A part of brain compartment representing the frontal cortex region of the brain",
        (),
        False,
    ),
    "PBPKO_00621": (
        "cerebrospinal fluid compartment",
        "A part of brain compartment representing the cerebrospinal fluid region of the brain",
        (),
        False,
    ),
    "PBPKO_00622": (
        "fraction unbound blood",
        "An unbound fraction parameter specifically for the blood compartment.",
        (),
        False,
    ),
    "PBPKO_00623": (
        "amount in blood",
        "The amount of compound in the blood compartment.",
        (),
        False,
    ),
    "PBPKO_00624": (
        "fraction unbound restbody",
        "An unbound fraction parameter specifically for the rest of the body compartment.",
        (),
        False,
    ),
    "PBPKO_00625": (
        "exposed skin compartment",
        "A skin compartment representing the exposed part of the skin to the chemical via dermal contact.",
        (),
        False,
    ),
    "PBPKO_00626": (
        "unexposed skin compartment",
        "A skin compartment representing the unexposed part of the skin to the chemical such as regions covered by clothing or occluded areas like the inner arms.",
        (),
        False,
    ),
    "PBPKO_00627": (
        "fraction of arterial plasma volume",
        "A dimensionless fraction of volume defined as the arterial plasma volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00628": (
        "fraction of venous plasma volume",
        "A dimensionless fraction of volume defined as the venous plasma volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_00629": (
        "amount in richly perfused tissue",
        "The amount of compound in the richly perfused tissue compartment.",
        (),
        False,
    ),
    "PBPKO_00630": (
        "amount in poorly perfused tissue",
        "The amount of compound in the poorly perfused tissue compartment.",
        (),
        False,
    ),
    "PBPKO_00631": (
        "amount in arterial blood",
        "The amount of compound in the arterial blood compartment.",
        (),
        False,
    ),
    "PBPKO_00632": (
        "amount in venous blood",
        "The amount of compound in the venous blood compartment.",
        (),
        False,
    ),
    "PBPKO_00633": (
        "amount in alveolar air",
        "The amount of compound in the alveolar air compartment.",
        (),
        False,
    ),
    "PBPKO_00634": (
        "red blood cell compartment",
        "A compartment representing the red blood cells of the body.",
        (),
        False,
    ),
    "PBPKO_00635": (
        "skin thickness",
        "A physiological parameter representing the thickness of the skin compartment",
        (),
        False,
    ),
    "PBPKO_00636": (
        "bodily fluid flow rate parameter",
        "A physiological parameter representing the rate of fluid flow to a particular compartment.",
        (),
        False,
    ),
    "PBPKO_00637": (
        "amount in viable epidermis of unexposed skin",
        "The amount of chemical in viable epidermis of unexposed skin",
        (),
        False,
    ),
    "PBPKO_00638": (
        "amount\xa0in viable epidermis of exposed skin",
        "The amount of chemical in viable epidermis of exposed skin",
        (),
        False,
    ),
    "PBPKO_00639": (
        "amount\xa0in skin stratum\xa0corneum of unexposed skin",
        "The amount of chemical in skin stratum corneum of unexposed skin",
        (),
        False,
    ),
    "PBPKO_00640": (
        "amount\xa0in skin stratum\xa0corneum of exposed skin",
        "The amount of chemical in skin stratum corneum of exposed skin",
        (),
        False,
    ),
    "PBPKO_00641": (
        "dermal absorption\xa0rate\xa0unexposed skin",
        "An absorption rate constant parameter representing dermal absorption rate flux through unexposed skin",
        (),
        False,
    ),
    "PBPKO_00642": (
        "dermal absorption\xa0rate\xa0exposed skin",
        "An absorption rate constant parameter representing dermal absorption rate flux through exposed skin",
        (),
        False,
    ),
    "PBPKO_00643": (
        "thickness stratum corneum",
        "A skin thickness parameter representing the thickness of stratum corneum.",
        (),
        False,
    ),
    "PBPKO_00644": (
        "thickness viable epidermis",
        "A skin thickness parameter representing the thickness of viable epidermis.",
        (),
        False,
    ),
    "PBPKO_00645": (
        "fat blood partition coefficient",
        "A partition coefficient representing the ratio of compound concentration in fat to blood.",
        (),
        False,
    ),
    "PBPKO_00646": (
        "diffusion rate",
        "A biochemical parameter representing the diffusion rate of the chemical",
        (),
        False,
    ),
    "PBPKO_00647": (
        "diffusion rate skin",
        "A diffusion rate parameter representing diffusion rate of the chemical across the skin",
        (),
        False,
    ),
    "PBPKO_00648": (
        "diffusion\xa0rate stratum\xa0corneum\xa0viable epidermis",
        "A diffusion rate skin parameter representing diffusion rate from stratum corneum to viable epidermis",
        (),
        False,
    ),
    "PBPKO_00649": (
        "miscellaneous parameter",
        "A parameter being used in the model but does not belong to specific parameter subclass",
        (),
        False,
    ),
    "PBPKO_00650": (
        "Michaelis",
        "A flag indicating for Michaelis-Menten or linear metabolism equation being used in the model",
        (),
        False,
    ),
    "PBPKO_00651": (
        "fraction of arterial\xa0blood\xa0volume",
        "A dimensionless fraction of volume defined as the arterial blood volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_01501": ("pgp", None, (), False),
    "PBPKO_01502": ("mrp2", None, (), False),
    "PBPKO_01503": ("mrp4", None, (), False),
    "PBPKO_01504": ("bcrp", None, (), False),
    "PBPKO_01505": ("nctp", None, (), False),
    "PBPKO_01506": ("oct1", None, (), False),
    "PBPKO_01507": ("oat1", None, (), False),
    "PBPKO_01508": ("oat3", None, (), False),
    "PBPKO_01509": ("oat4", None, (), False),
    "PBPKO_02001": (
        "bile compartment",
        "A compartment representing the bile storage",
        (),
        False,
    ),
    "PBPKO_02002": (
        "colon compartment",
        "A compartment representing the colon",
        (),
        False,
    ),
    "PBPKO_02003": (
        "small intestine tissue compartment",
        "A compartment representing the small intestinal tissue",
        (),
        False,
    ),
    "PBPKO_02004": (
        "intestinal tissue compartment",
        "A compartment representing the whole intestinal tissue",
        (),
        False,
    ),
    "PBPKO_02005": (
        "portal vein perfused tissue comparment",
        "A compartment with grouped organs that are exclusively perfused via the portal vein (i.e.: Stomach, small and large intestine, spleen)",
        (),
        False,
    ),
    "PBPKO_02006": (
        "glomerulus compartment",
        "A part of kidney compartment in the model representing glomerulus in the body",
        (),
        False,
    ),
    "PBPKO_02007": (
        "menstrual plasma compartment",
        "A compartment representing menstrual plasma",
        (),
        False,
    ),
    "PBPKO_02008": (
        "kidney rest lumen compartment",
        "A compartment representing rest of the lumen of kidney.",
        (),
        False,
    ),
    "PBPKO_02009": (
        "kidney proximal tubule tissue compartment",
        "A compartment representing rest of the tissue of kidney.",
        (),
        False,
    ),
    "PBPKO_02010": (
        "liver extracellular compartment",
        "A compartment representing vascular and interstitial space of the liver.",
        (),
        False,
    ),
    "PBPKO_02011": (
        "liver intracellular space compartment",
        "A compartment representing intracellular space of the liver.",
        (),
        False,
    ),
    "PBPKO_02012": (
        "gastro intestinal tract compartment",
        "A digestive system compartment representing the gastro-intestinal tract",
        (),
        False,
    ),
    "PBPKO_02013": (
        "gonad compartment",
        "A compartment representing gonads.",
        (),
        False,
    ),
    "PBPKO_03001": (
        "intrinsic gastric emptying rate",
        "The absorption rate constant parameter representing the intrinsic rate of the chemical release from stomach to lumen or the jejunum segment",
        (),
        False,
    ),
    "PBPKO_03002": (
        "intrinsic absorption rate",
        "The absorption rate constant parameter representing the intrinsic absorption rate from the gut or any intestinal segment to the liver or the portal vein",
        (),
        False,
    ),
    "PBPKO_03003": (
        "intrinsic stomach uptake rate",
        "The absorption rate constant parameter representing the intrinsic absorption rate of a chemical from the stomach to the gut tissue or any intestinal segment",
        (),
        False,
    ),
    "PBPKO_03004": (
        "stomach uptake rate",
        "The absorption rate constant parameter representing the absorption rate from stomach to gut tissue or any intestine segment",
        (),
        False,
    ),
    "PBPKO_03005": ("intrinsic fecal excretion rate", None, (), False),
    "PBPKO_03006": ("fecal excretion rate", None, (), False),
    "PBPKO_03007": ("intrinsic biliary clearance rate", None, (), False),
    "PBPKO_03008": (
        "kinetic emptying rate from jejunum lumen to ileum lumen",
        None,
        (),
        False,
    ),
    "PBPKO_03009": (
        "kinetic emptying  rate from ileum lumen to large intestine lumen",
        None,
        (),
        False,
    ),
    "PBPKO_03010": (
        "kinetic absorption rate from jejunum lumen to intestinal tissue",
        None,
        (),
        False,
    ),
    "PBPKO_03011": (
        "kinetic absorption rate from ileum lumen to intestinal tissue",
        None,
        (),
        False,
    ),
    "PBPKO_03012": (
        "kinetic absorption rate from large intestinal lumen to intestinal tissue",
        None,
        (),
        False,
    ),
    "PBPKO_03013": ("effective Caco-2 permeability", None, (), False),
    "PBPKO_03014": ("apparent Caco-2 permeability", None, (), False),
    "PBPKO_03015": (
        "kinetic emptying  rate between intestinal segments",
        None,
        (),
        False,
    ),
    "PBPKO_03016": ("Hill dissociation constant", None, (), False),
    "PBPKO_03017": ("Hill coefficient", None, (), False),
    "PBPKO_03018": ("intrinsic absorption rate of metabilite", None, (), False),
    "PBPKO_03019": ("absorption rate of metabolite", None, (), False),
    "PBPKO_03020": (
        "intrinsic enterohepatic recirculation rate constant",
        None,
        (),
        False,
    ),
    "PBPKO_03021": ("enterohepatic recirculation rate constant", None, (), False),
    "PBPKO_03023": ("intrinsic reabsorption rate constant", None, (), False),
    "PBPKO_03024": ("reabsorption rate constant", None, (), False),
    "PBPKO_03025": ("maximum capacity of binding sites in red cells", None, (), False),
    "PBPKO_03026": (
        "half-saturation concentration of chemical for binding by sites in red cells",
        None,
        (),
        False,
    ),
    "PBPKO_03027": ("metabolism rate constant in liver", None, (), False),
    "PBPKO_03028": ("metabolism rate constant in intestinal tissue", None, (), False),
    "PBPKO_03030": ("red blood cells partition coefficient", None, (), False),
    "PBPKO_03031": ("follicle permeability coefficient", None, (), False),
    "PBPKO_03032": (
        "partition coeffcient of stratum corneum to viable epidermis",
        None,
        (),
        False,
    ),
    "PBPKO_03033": (
        "partition coeffcient of viable epidermis to blood",
        None,
        (),
        False,
    ),
    "PBPKO_03034": (
        "partition coeffcient of stratum corneum to skin surface depot",
        None,
        (),
        False,
    ),
    "PBPKO_03035": (
        "partition coeffcient of follicle to skin surface depot",
        None,
        (),
        False,
    ),
    "PBPKO_03036": ("octanol water partition coefficient", None, (), False),
    "PBPKO_03037": ("medium polymer partition coefficient", None, (), False),
    "PBPKO_03038": ("medium air partition coefficient", None, (), False),
    "PBPKO_03039": ("medium mitochondria partition coefficient", None, (), False),
    "PBPKO_03040": ("medium lysosomes partition coefficient", None, (), False),
    "PBPKO_03041": (
        "medium intracellular water partition coefficient",
        None,
        (),
        False,
    ),
    "PBPKO_03042": ("medium microsomes partition coefficient", None, (), False),
    "PBPKO_03043": ("medium other organelles partition coefficient", None, (), False),
    "PBPKO_03044": ("medium albumin partition coefficient", None, (), False),
    "PBPKO_03045": ("abiotic degradation rate in medium", None, (), False),
    "PBPKO_03046": ("acidic phospholipid association constant", None, (), False),
    "PBPKO_03047": ("abiotic degradation rate in air", None, (), False),
    "PBPKO_03048": ("maximum metabolic rate", None, (), False),
    "PBPKO_03049": ("linear metabolic rate", None, (), False),
    "PBPKO_03050": ("cell radius", None, (), False),
    "PBPKO_03051": ("cell replication time", None, (), False),
    "PBPKO_03052": ("cell fraction of proteins", None, (), False),
    "PBPKO_03053": ("cell fraction of lipids", None, (), False),
    "PBPKO_03054": ("cell fraction of intracellular water", None, (), False),
    "PBPKO_03055": ("cell fraction of mitochondria", None, (), False),
    "PBPKO_03056": ("cell fraction of lysosomes", None, (), False),
    "PBPKO_03057": ("cell fraction of microsomes", None, (), False),
    "PBPKO_03058": ("fraction of neutral lipids in the FBS", None, (), False),
    "PBPKO_03059": ("fraction of albumin in the FBS", None, (), False),
    "PBPKO_03060": ("culture area", None, (), False),
    "PBPKO_03061": ("top well diameter", None, (), False),
    "PBPKO_03062": ("well depth", None, (), False),
    "PBPKO_03063": ("plate wall thickness", None, (), False),
    "PBPKO_03064": ("culture medium pH", None, (), False),
    "PBPKO_03065": ("fraction of serum in total media", None, (), False),
    "PBPKO_03066": ("FBS pH", None, (), False),
    "PBPKO_03067": ("initial number of cells", None, (), False),
    "PBPKO_03068": ("nominal concentration of medium", None, (), False),
    "PBPKO_03069": ("volume of medium", None, (), False),
    "PBPKO_03070": ("fraction of FBS iin the medium", None, (), False),
    "PBPKO_03071": ("ionized fraction in the medium", None, (), False),
    "PBPKO_03072": ("fraction unbound in the medium", None, (), False),
    "PBPKO_03073": ("fraction unbound in the FBS", None, (), False),
    "PBPKO_03074": ("fraction unbound in the cell", None, (), False),
    "PBPKO_03075": (
        "absorption rate constant",
        "A biochemical parameter representing the rate constant at which a compound is absorbed into systemic circulation or a target compartment from the site of administration",
        (),
        False,
    ),
    "PBPKO_03076": (
        "fraction unbound kidney proximal tubule",
        "An unbound fraction parameter specifically for the kidney proximal tubule.",
        (),
        False,
    ),
    "PBPKO_04001": (
        "plasma flow rate",
        "A bodily fluid flow rate parameter specifically describing the flow of plasma to a compartment.",
        (),
        False,
    ),
    "PBPKO_04002": (
        "plasma flow rate to stomach",
        "A plasma flow rate parameter specifically describing the rate to the stomach compartment.",
        (),
        False,
    ),
    "PBPKO_04003": (
        "plasma flow rate to intestine",
        "A plasma flow rate parameter specifically describing the rate to the intestine compartment.",
        (),
        False,
    ),
    "PBPKO_04004": (
        "plasma flow rate to small intestine",
        "A plasma flow rate parameter specifically describing the rate to the small intestine compartment.",
        (),
        False,
    ),
    "PBPKO_04005": (
        "plasma flow rate to large intestine",
        "A plasma flow rate parameter specifically describing the rate to the large intestine compartment.",
        (),
        False,
    ),
    "PBPKO_04006": (
        "plasma flow rate to pancreas",
        "A plasma flow rate parameter specifically describing the rate to the pancreas compartment.",
        (),
        False,
    ),
    "PBPKO_04007": (
        "plasma flow rate to liver",
        "A plasma flow rate parameter specifically describing the rate to the liver compartment.",
        (),
        False,
    ),
    "PBPKO_04008": (
        "plasma flow rate to kidney",
        "A plasma flow rate parameter specifically describing the rate to the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_04009": (
        "plasma flow rate to muscle",
        "A plasma flow rate parameter specifically describing the rate to the muscle compartment.",
        (),
        False,
    ),
    "PBPKO_04010": (
        "plasma flow rate to heart",
        "A plasma flow rate parameter specifically describing the rate to the heart compartment.",
        (),
        False,
    ),
    "PBPKO_04011": (
        "plasma flow rate to fat",
        "A plasma flow rate parameter specifically describing the rate to the fat compartment.",
        (),
        False,
    ),
    "PBPKO_04012": (
        "plasma flow rate to gonad",
        "A plasma flow rate parameter specifically describing the rate to the gonad compartment.",
        (),
        False,
    ),
    "PBPKO_04013": (
        "plasma flow rate to skin",
        "A plasma flow rate parameter specifically describing the rate to the skin compartment.",
        (),
        False,
    ),
    "PBPKO_04014": (
        "plasma flow rate to bone",
        "A plasma flow rate parameter specifically describing the rate to the bone compartment.",
        (),
        False,
    ),
    "PBPKO_04015": (
        "plasma flow rate to brain",
        "A plasma flow rate parameter specifically describing the rate to the brain compartment.",
        (),
        False,
    ),
    "PBPKO_04016": (
        "plasma flow rate to spleen",
        "A plasma flow rate parameter specifically describing the rate to the spleen compartment.",
        (),
        False,
    ),
    "PBPKO_04017": (
        "plasma flow rate to lung",
        "A plasma flow rate parameter specifically describing the rate to the lung compartment.",
        (),
        False,
    ),
    "PBPKO_04018": (
        "plasma flow rate to poorly perfused",
        "A plasma flow rate parameter specifically describing the rate to the poorly perfused compartment.",
        (),
        False,
    ),
    "PBPKO_04019": (
        "plasma flow rate to richly perfused",
        "A plasma flow rate parameter specifically describing the rate to the richly perfused compartment.",
        (),
        False,
    ),
    "PBPKO_04020": (
        "plasma flow rate to restbody",
        "A plasma flow rate parameter specifically describing the rate to the rest of the body compartment.",
        (),
        False,
    ),
    "PBPKO_04021": (
        "plasma flow rate to gall bladder",
        "A plasma flow rate parameter specifically describing the rate to the gall bladder compartment.",
        (),
        False,
    ),
    "PBPKO_04022": (
        "plasma flow rate to portal vein",
        "A plasma flow rate parameter specifically describing the rate to the portal vein compartment.",
        (),
        False,
    ),
    "PBPKO_04023": (
        "plasma flow rate to lymph",
        "A plasma flow rate parameter specifically describing the rate to the lymph compartment.",
        (),
        False,
    ),
    "PBPKO_04024": (
        "plasma flow rate to duodenum",
        "A plasma flow rate parameter specifically describing the rate to the duodenum compartment.",
        (),
        False,
    ),
    "PBPKO_04025": (
        "plasma flow rate to jejunum",
        "A plasma flow rate parameter specifically describing the rate to the jejunum compartment.",
        (),
        False,
    ),
    "PBPKO_04026": (
        "plasma flow rate to ileum",
        "A plasma flow rate parameter specifically describing the rate to the ileum compartment.",
        (),
        False,
    ),
    "PBPKO_04027": (
        "plasma flow rate to colon",
        "A plasma flow rate parameter specifically describing the rate to the colon compartment.",
        (),
        False,
    ),
    "PBPKO_04028": (
        "plasma flow rate to cecum",
        "A plasma flow rate parameter specifically describing the rate to the cecum compartment.",
        (),
        False,
    ),
    "PBPKO_04029": (
        "plasma flow rate to filtrate",
        "A plasma flow rate parameter specifically describing the rate to the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_04030": (
        "plasma flow rate to bone marrow",
        "A plasma flow parameter specifically describing the rate to the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_04031": (
        "plasma flow rate to gut",
        "A plasma flow rate parameter specifically describing the rate to the gut compartment.",
        (),
        False,
    ),
    "PBPKO_04032": (
        "plasma flow rate to mammary gland",
        "A plasma flow rate parameter specifically describing the rate to the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_04033": (
        "plasma flow rate for mass balance",
        "A plasma flow rate parameter representing the check for total plasma flow mass balance of all the compartments (sum of organ flows should equal cardiac output).",
        (),
        False,
    ),
    "PBPKO_04034": (
        "plasma flow rate to unexposed skin",
        "A plasma flow rate parameter specifically describing the rate to the unexposed skin compartment.",
        (),
        False,
    ),
    "PBPKO_04035": (
        "plasma flow rate to exposed skin",
        "A plasma flow rate parameter specifically describing the rate to the exposed skin compartment.",
        (),
        False,
    ),
    "PBPKO_04036": (
        "plasma flow rate to skin stratum corneum unexposed",
        "A plasma flow rate parameter specifically describing the rate to the unexposed stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_04037": (
        "plasma flow rate to skin stratum corneum exposed",
        "A plasma flow rate parameter specifically describing the rate to the exposed stratum corneum compartment.",
        (),
        False,
    ),
    "PBPKO_04038": ("fraction of blood flow to red blood cells", None, (), False),
    "PBPKO_04039": ("blood flow rate to red blood cells", None, (), False),
    "PBPKO_04040": ("volumen of lumen", None, (), False),
    "PBPKO_04041": ("volume of small intestine tissue", None, (), False),
    "PBPKO_04042": ("volume of bile", None, (), False),
    "PBPKO_04043": ("enterocyte volume", None, (), False),
    "PBPKO_04044": ("hepatic vein blood flow", None, (), False),
    "PBPKO_04045": ("blood flow rate to bile", None, (), False),
    "PBPKO_04046": ("diameter of intestinal", None, (), False),
    "PBPKO_04047": ("diameter of the jejunum lumen", None, (), False),
    "PBPKO_04048": ("diameter of the ileum lumen", None, (), False),
    "PBPKO_04049": ("diameter of the large intestine lumen", None, (), False),
    "PBPKO_04050": ("surface area  of the jejunum lumen", None, (), False),
    "PBPKO_04051": ("surface area of the ileum lumen", None, (), False),
    "PBPKO_04052": ("surface area of the large intestine lumen", None, (), False),
    "PBPKO_04053": ("uptake fraction to blood", None, (), False),
    "PBPKO_04054": ("fraction of bile in small intestine", None, (), False),
    "PBPKO_04055": ("fraction of bile in liver", None, (), False),
    "PBPKO_04056": ("fraction of feces", None, (), False),
    "PBPKO_04057": ("volume fraction of blood", None, (), False),
    "PBPKO_04058": ("volume fraction of red blood cells", None, (), False),
    "PBPKO_04059": ("skin area", None, (), False),
    "PBPKO_04060": ("thickness epidermis", None, (), False),
    "PBPKO_04061": ("volume of exposed viable epidermis", None, (), False),
    "PBPKO_04062": ("volume of follicle", None, (), False),
    "PBPKO_04063": ("area of exposed skin", None, (), False),
    "PBPKO_04064": ("volume of serum", None, (), False),
    "PBPKO_04065": ("volume of adrenals", None, (), False),
    "PBPKO_04066": ("volume of breast", None, (), False),
    "PBPKO_04067": ("volume of thyroid", None, (), False),
    "PBPKO_04068": ("volume of intestinal lumen", None, (), False),
    "PBPKO_04069": ("volume of small intestinal lumen", None, (), False),
    "PBPKO_04070": ("volume of large intestinal lumen", None, (), False),
    "PBPKO_04071": ("volume of stomach lumen", None, (), False),
    "PBPKO_04072": ("volume of gut intestinal tract", None, (), False),
    "PBPKO_04073": ("volume of testis", None, (), False),
    "PBPKO_04074": ("volume of uterus", None, (), False),
    "PBPKO_04075": ("volume of skeleton", None, (), False),
    "PBPKO_04076": ("volume of hair", None, (), False),
    "PBPKO_04077": ("volume of urinary tract", None, (), False),
    "PBPKO_04078": ("volume of skin surface depot", None, (), False),
    "PBPKO_04079": ("volume of cortical bone", None, (), False),
    "PBPKO_04080": ("volume of trabecular bone", None, (), False),
    "PBPKO_04081": ("volume of alveolar compartment", None, (), False),
    "PBPKO_04082": ("fraction of serum", None, (), False),
    "PBPKO_04083": ("fraction of adrenals", None, (), False),
    "PBPKO_04084": ("fraction of breast", None, (), False),
    "PBPKO_04085": ("fraction of thyroid", None, (), False),
    "PBPKO_04086": ("fraction of intestinal lumen", None, (), False),
    "PBPKO_04087": ("fraction of small intestinal lumen", None, (), False),
    "PBPKO_04088": ("fraction of large intestinal lumen", None, (), False),
    "PBPKO_04089": ("fraction of stomach lumen", None, (), False),
    "PBPKO_04090": ("fraction of gut intestinal tract", None, (), False),
    "PBPKO_04091": ("fraction of testis", None, (), False),
    "PBPKO_04092": ("fraction of uterus", None, (), False),
    "PBPKO_04093": ("fraction of skeleton", None, (), False),
    "PBPKO_04094": ("fraction of hair", None, (), False),
    "PBPKO_04095": ("fraction of amniotic fluid", None, (), False),
    "PBPKO_04096": ("fraction of urinary tract", None, (), False),
    "PBPKO_04097": ("fraction of cortical bone", None, (), False),
    "PBPKO_04098": ("fraction of trabecular bone", None, (), False),
    "PBPKO_04099": ("fraction of the skin surface depot", None, (), False),
    "PBPKO_04100": (
        "fraction of blood",
        "A dimensionless fraction of volume defined as the blood volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_04101": (
        "fraction of bone marrow",
        "A dimensionless fraction of volume defined as the bone marrow volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_04102": (
        "fraction of bone non perfused",
        "A dimensionless fraction of volume defined as the bone non perfuse volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_04103": (
        "fraction of adipose mass",
        "A dimensionless fraction of volume defined as the adipose mass volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_04104": (
        "fraction of intestinal tissue",
        "A dimensionless fraction of volume defined as the intestinal tissue volume divided per unit of total body weight.",
        (),
        False,
    ),
    "PBPKO_04105": (
        "volume of kidney rest tissue",
        "A volume parameter representing the total volume of the kidney rest tissue compartment.",
        (),
        False,
    ),
    "PBPKO_04106": (
        "volume of kidney rest lumen",
        "A volume parameter representing the total volume of the kidney rest lumen compartment.",
        (),
        False,
    ),
    "PBPKO_04107": (
        "volume of kidney proximal tubule lumen",
        "A volume parameter representing the total volume of the lumen of kidney proximal tubule compartment.",
        (),
        False,
    ),
    "PBPKO_04108": (
        "volume of kidney proximal tubule tissue",
        "A volume parameter representing the total volume of the tissue of kidney proximal tubule compartment.",
        (),
        False,
    ),
    "PBPKO_04109": (
        "volume of liver extracellular",
        "A volume parameter representing the total volume of the vascular and interstitial spaces of liver compartment.",
        (),
        False,
    ),
    "PBPKO_04110": (
        "volume of liver intracellular space",
        "A volume parameter representing the total volume of the hepatocytes in liver compartment.",
        (),
        False,
    ),
    "PBPKO_04111": (
        "volume of intestine tissue",
        "A volume parameter representing the total volume of the tissue of intestine compartment.",
        (),
        False,
    ),
    "PBPKO_05001": (
        "molar volume",
        "A physicochemical parameter representing the volume of one mole of a molecule.",
        (),
        False,
    ),
    "PBPKO_05002": (
        "Henry's law constant",
        "A physicochemical parameter describing the volatily of a compound",
        (),
        False,
    ),
    "PBPKO_05003": (
        "vapor pressure",
        "A physicochemical parameter describing the vapor pressure of the compound",
        (),
        False,
    ),
    "PBPKO_06002": (
        "unbound venous concentration of compound in compartment",
        None,
        (),
        False,
    ),
    "PBPKO_06003": ("unbound concentration of compund in compartment", None, (), False),
    "PBPKO_06004": (
        "amount in stomach",
        "The amount of chemical in stomach compartment.",
        (),
        False,
    ),
    "PBPKO_06005": (
        "amount in small intestine",
        "The amount of chemical in small intestine compartment",
        (),
        False,
    ),
    "PBPKO_06006": (
        "amount in jejunum",
        "The amount of chemical in jejunum compartment.",
        (),
        False,
    ),
    "PBPKO_06007": (
        "amount in ileum",
        "The amount of chemical in ileum compartment.",
        (),
        False,
    ),
    "PBPKO_06008": (
        "amount in  large intestine",
        "The amount of chemical in large intestine compartment.",
        (),
        False,
    ),
    "PBPKO_06009": (
        "amount in lumen",
        "The amount of chemical in lumen of the intestine.",
        (),
        False,
    ),
    "PBPKO_06010": (
        "amount in small intestine segment",
        "The amount of chemical in segment of small intestine.",
        (),
        False,
    ),
    "PBPKO_06011": (
        "amount in colon",
        "The amount of chemical in colon compartment.",
        (),
        False,
    ),
    "PBPKO_06012": ("amount in bile", "The amount of chemical in bile.", (), False),
    "PBPKO_06013": (
        "amount in spleen",
        "The amount of chemical in spleen compartment",
        (),
        False,
    ),
    "PBPKO_06014": (
        "amount in duodenum",
        "The amount of chemical in duodenum compartment.",
        (),
        False,
    ),
    "PBPKO_06015": (
        "amount in intestinal tissue",
        "The amount of chemical in intestinal tissue",
        (),
        False,
    ),
    "PBPKO_06016": (
        "amount in portal vein",
        "The amount of chemical in portal vein.",
        (),
        False,
    ),
    "PBPKO_06017": (
        "unbound concentration in plasma",
        "The unbound concentration of compound in the plasma compartment.",
        (),
        False,
    ),
    "PBPKO_06018": (
        "unbound venous liver concentration",
        "The unbound venous concentration of compound in the liver compartment.",
        (),
        False,
    ),
    "PBPKO_06019": (
        "unbound venous gut concentration",
        "The unbound venous concentration of compound in the gut compartment.",
        (),
        False,
    ),
    "PBPKO_06020": (
        "unbound venous brain concentration",
        "The unbound venous concentration of compound in the brain compartment.",
        (),
        False,
    ),
    "PBPKO_06021": (
        "unbound venous kidney concentration",
        "The unbound venous concentration of compound in the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_06022": (
        "unbound venous filtrate concentration",
        "The unbound venous concentration of compound in the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_06023": (
        "unbound venous lung concentration",
        "The unbound venous concentration of compound in the lung compartment.",
        (),
        False,
    ),
    "PBPKO_06024": (
        "unbound venous fat concentration",
        "The unbound venous concentration of compound in the fat compartment.",
        (),
        False,
    ),
    "PBPKO_06025": (
        "unbound venous bone marrow concentration",
        "The unbound venous concentration of compound in the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_06026": (
        "unbound venous skin concentration",
        "The unbound venous concentration of compound in the skin compartment.",
        (),
        False,
    ),
    "PBPKO_06027": (
        "unbound venous mammary gland concentration",
        "The unbound venous concentration of compound in the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_06028": (
        "unbound venous rest body concentration",
        "The unbound venous concentration of compound in the rest body compartment.",
        (),
        False,
    ),
    "PBPKO_06029": (
        "total venous concentration of compound in compartment",
        None,
        (),
        False,
    ),
    "PBPKO_06030": (
        "total venous liver concentration",
        "The total venous concentration of compound in the liver compartment.",
        (),
        False,
    ),
    "PBPKO_06031": (
        "total venous gut concentration",
        "The total venous concentration of compound in the gut compartment.",
        (),
        False,
    ),
    "PBPKO_06032": (
        "total venous kidney concentration",
        "The total venous concentration of compound in the kidney compartment.",
        (),
        False,
    ),
    "PBPKO_06033": (
        "total venous brain concentration",
        "The total venous concentration of compound in the brain compartment.",
        (),
        False,
    ),
    "PBPKO_06034": (
        "total venous filtrate concentration",
        "The total venous concentration of compound in the filtrate compartment.",
        (),
        False,
    ),
    "PBPKO_06035": (
        "total venous lung concentration",
        "The total venous concentration of compound in the lung compartment.",
        (),
        False,
    ),
    "PBPKO_06036": (
        "total venous fat concentration",
        "The total venous concentration of compound in the fat compartment.",
        (),
        False,
    ),
    "PBPKO_06037": (
        "total venous bone marrow concentration",
        "The total venous concentration of compound in the bone marrow compartment.",
        (),
        False,
    ),
    "PBPKO_06038": (
        "total venous skin concentration",
        "The total venous concentration of compound in the skin compartment.",
        (),
        False,
    ),
    "PBPKO_06039": (
        "total venous mammary gland concentration",
        "The total venous concentration of compound in the mammary gland compartment.",
        (),
        False,
    ),
    "PBPKO_06040": (
        "total venous rest body concentration",
        "The total venous concentration of compound in the rest of the body compartment.",
        (),
        False,
    ),
    "PBPKO_06041": (
        "concentration in stomach",
        "The concentration of chemical in stomach compartment.",
        (),
        False,
    ),
    "PBPKO_06042": (
        "concentration in small intestine",
        "The concentration of chemical in small intestine compartment.",
        (),
        False,
    ),
    "PBPKO_06043": (
        "concentration in jejunum",
        "The concentration of chemical in jejunum compartment.",
        (),
        False,
    ),
    "PBPKO_06044": (
        "concentration in ileum",
        "The concentration of chemical in ileum compartment.",
        (),
        False,
    ),
    "PBPKO_06045": (
        "concentration in large intestine",
        "The concentration of chemical in large intestine compartment.",
        (),
        False,
    ),
    "PBPKO_06046": (
        "concentration in intestinal tissue",
        "The concentration of chemical in tissue of intestine.",
        (),
        False,
    ),
    "PBPKO_06047": (
        "concentration in lumen",
        "The concentration of chemical in lumen of intestine.",
        (),
        False,
    ),
    "PBPKO_06048": (
        "concentration in bile",
        "The concentration of chemical in bile.",
        (),
        False,
    ),
    "PBPKO_06049": (
        "concentration in spleen",
        "The concentration of chemical in spleen compartment.",
        (),
        False,
    ),
    "PBPKO_06050": (
        "concentration in feces",
        "The concentration of chemical in feces.",
        (),
        False,
    ),
    "PBPKO_06051": ("amount in skin surface depot", None, (), False),
    "PBPKO_06052": (
        "maximum amount",
        "The maximum amount of chemical in a compartment",
        (),
        False,
    ),
    "PBPKO_06053": ("amount in follicles", None, (), False),
    "PBPKO_06054": ("concentration in medium", None, (), False),
    "PBPKO_06055": ("concentration in cell", None, (), False),
    "PBPKO_06056": ("concentration in mitochondria", None, (), False),
    "PBPKO_06057": ("concentration in lysosomes", None, (), False),
    "PBPKO_06058": ("concentration in microsomes", None, (), False),
    "PBPKO_06059": ("concentration in intracellular water", None, (), False),
    "PBPKO_06060": ("concentration in polymer", None, (), False),
    "PBPKO_06061": ("concentration in air", None, (), False),
    "PBPKO_06062": (
        "amount in menstrual",
        "The amount of compound in the menstrual compartment.",
        (),
        False,
    ),
    "PBPKO_06063": (
        "amount in kidney rest tissue",
        "The amount of compound in the kidney rest tissue compartment.",
        (),
        False,
    ),
    "PBPKO_06064": (
        "amount in kidney rest lumen",
        "The amount of compound in the rest of kidney lumen compartment.",
        (),
        False,
    ),
    "PBPKO_06065": (
        "amount in kidney proximal tubule tissue",
        "The amount of compound in the proximal tubule tissue of kidney compartment.",
        (),
        False,
    ),
    "PBPKO_06066": (
        "amount in kidney proximal tubule lumen",
        "The amount of compound in the proximal tubule lumen of kidney compartment.",
        (),
        False,
    ),
    "PBPKO_06067": (
        "amount in liver intracellular",
        "The amount of compound in the intracellular spaceof liver compartment.",
        (),
        False,
    ),
    "PBPKO_06068": (
        "amount in liver extracellular",
        "The amount of compound in the extracellular space of liver compartment.",
        (),
        False,
    ),
    "PBPKO_07001": ("invitro pbpk", None, (), False),
    "PR_000000001": (
        "protein",
        "An amino acid chain that is produced de novo by ribosome-mediated translation of a genetically-encoded mRNA, and any derivatives thereof.",
        (),
        False,
    ),
    "PR_000018263": (
        "amino acid chain",
        "An organic amino compound that consists of amino acid residues (unmodified amino-acid residues and/or modified amino-acid residues) linked by peptide bonds or derivatives of such bonds.",
        (),
        False,
    ),
    "RO_0000052": (
        "characteristic of",
        "a relation between a specifically dependent continuant (the characteristic) and any other entity (the bearer), in which the characteristic depends on the bearer for its existence.",
        (),
        False,
    ),
    "RO_0000053": ("has characteristic", "Inverse of characteristic_of", (), False),
    "RO_0000056": (
        "participates in",
        "a relation between a continuant and a process, in which the continuant is somehow involved in the process",
        (),
        False,
    ),
    "RO_0000057": (
        "has participant",
        "a relation between a process and a continuant, in which the continuant is somehow involved in the process",
        (),
        False,
    ),
    "RO_0000059": (
        "concretizes",
        "A relationship between a specifically dependent continuant and a generically dependent continuant, in which the generically dependent continuant depends on some independent continuant in virtue of the fact that the specifically dependent continuant also depends on that same independent continuant. Multiple specifically dependent continuants can concretize the same generically dependent continuant.",
        (),
        False,
    ),
    "RO_0000079": (
        "function of",
        "a relation between a function and an independent continuant (the bearer), in which the function specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000080": (
        "quality of",
        "a relation between a quality and an independent continuant (the bearer), in which the quality specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000081": (
        "role of",
        "a relation between a role and an independent continuant (the bearer), in which the role specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000085": (
        "has function",
        "a relation between an independent continuant (the bearer) and a function, in which the function specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000086": (
        "has quality",
        "a relation between an independent continuant (the bearer) and a quality, in which the quality specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000087": (
        "has role",
        "a relation between an independent continuant (the bearer) and a role, in which the role specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000091": (
        "has disposition",
        "a relation between an independent continuant (the bearer) and a disposition, in which the disposition specifically depends on the bearer for its existence",
        (),
        False,
    ),
    "RO_0000092": ("disposition of", "inverse of has disposition", (), False),
    "RO_0002013": (
        "has regulatory component activity",
        "A 'has regulatory component activity' B if A and B are GO molecular functions (GO_0003674), A has_component B and A is regulated by B.",
        (),
        False,
    ),
    "RO_0002014": (
        "has negative regulatory component activity",
        "A relationship that holds between a GO molecular function and a component of that molecular function that negatively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is negatively regulated by B.",
        (),
        False,
    ),
    "RO_0002015": (
        "has positive regulatory component activity",
        "A relationship that holds between a GO molecular function and a component of that molecular function that positively regulates the activity of the whole. More formally, A 'has regulatory component activity' B iff :A and B are GO molecular functions (GO_0003674), A has_component B and A is positively regulated by B.",
        (),
        False,
    ),
    "RO_0002017": ("has component activity", None, (), False),
    "RO_0002018": (
        "has component process",
        "w 'has process component' p if p and w are processes, w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type.",
        (),
        False,
    ),
    "RO_0002022": ("directly regulated by", None, (), False),
    "RO_0002023": ("directly negatively regulated by", None, (), False),
    "RO_0002024": ("directly positively regulated by", None, (), False),
    "RO_0002025": ("has effector activity", None, (), False),
    "RO_0002086": ("ends after", None, (), False),
    "RO_0002087": ("immediately preceded by", None, (), False),
    "RO_0002090": ("immediately precedes", None, (), False),
    "RO_0002131": (
        "overlaps",
        "x overlaps y if and only if there exists some z such that x has part z and z part of y",
        (),
        False,
    ),
    "RO_0002180": (
        "has component",
        "w 'has component' p if w 'has part' p and w is such that it can be directly disassembled into into n parts p, p2, p3, ..., pn, where these parts are of similar type.",
        (),
        False,
    ),
    "RO_0002211": (
        "regulates",
        "p regulates q iff p is causally upstream of q, the execution of p is not constant and varies according to specific conditions, and p influences the rate or magnitude of execution of q due to an effect either on some enabler of q or some enabler of a part of q.",
        (),
        False,
    ),
    "RO_0002212": (
        "negatively regulates",
        "p negatively regulates q iff p regulates q, and p decreases the rate or magnitude of execution of q.",
        (),
        False,
    ),
    "RO_0002213": (
        "positively regulates",
        "p positively regulates q iff p regulates q, and p increases the rate or magnitude of execution of q.",
        (),
        False,
    ),
    "RO_0002215": (
        "capable of",
        "A relation between a material entity (such as a cell) and a process, in which the material entity has the ability to carry out the process.",
        (),
        False,
    ),
    "RO_0002216": (
        "capable of part of",
        "c stands in this relationship to p if and only if there exists some p' such that c is capable_of p', and p' is part_of p.",
        (),
        False,
    ),
    "RO_0002222": ("temporally related to", None, (), False),
    "RO_0002233": (
        "has input",
        "p has input c iff: p is a process, c is a material entity, c is a participant in p, c is present at the start of p, and the state of c is modified during p.",
        (),
        False,
    ),
    "RO_0002263": (
        "acts upstream of",
        "c acts upstream of p if and only if c enables some f that is involved in p' and p' occurs chronologically before p, is not part of p, and affects the execution of p. c is a material entity and f, p, p' are processes.",
        (),
        False,
    ),
    "RO_0002264": (
        "acts upstream of or within",
        "c acts upstream of or within p if c is enables f, and f is causally upstream of or within p. c is a material entity and p is an process.",
        (),
        False,
    ),
    "RO_0002304": (
        "causally upstream of, positive effect",
        "p is causally upstream of, positive effect q iff p is casually upstream of q, and the execution of p is required for the execution of q.",
        (),
        False,
    ),
    "RO_0002305": (
        "causally upstream of, negative effect",
        "p is causally upstream of, negative effect q iff p is casually upstream of q, and the execution of p decreases the execution of q.",
        (),
        False,
    ),
    "RO_0002314": (
        "characteristic of part of",
        "q characteristic of part of w if and only if there exists some p such that q inheres in p and p part of w.",
        (),
        False,
    ),
    "RO_0002323": (
        "mereotopologically related to",
        "A mereological relationship or a topological relationship",
        (),
        False,
    ),
    "RO_0002327": (
        "enables",
        "c enables p iff c is capable of p and c acts to execute p.",
        (),
        False,
    ),
    "RO_0002328": (
        "functionally related to",
        "A grouping relationship for any relationship directly involving a function, or that holds because of a function of one of the related entities.",
        (),
        False,
    ),
    "RO_0002329": (
        "part of structure that is capable of",
        "this relation holds between c and p when c is part of some c', and c' is capable of p.",
        (),
        False,
    ),
    "RO_0002331": (
        "involved in",
        "c involved_in p if and only if c enables some process p', and p' is part of p",
        (),
        False,
    ),
    "RO_0002333": ("enabled by", "inverse of enables", (), False),
    "RO_0002334": ("regulated by", "inverse of regulates", (), False),
    "RO_0002335": (
        "negatively regulated by",
        "inverse of negatively regulates",
        (),
        False,
    ),
    "RO_0002336": (
        "positively regulated by",
        "inverse of positively regulates",
        (),
        False,
    ),
    "RO_0002351": (
        "has member",
        "has member is a mereological relation between a collection and an item.",
        (),
        False,
    ),
    "RO_0002352": ("input of", "inverse of has input", (), False),
    "RO_0002404": ("causally downstream of", "inverse of upstream of", (), False),
    "RO_0002405": ("immediately causally downstream of", None, (), False),
    "RO_0002407": (
        "indirectly positively regulates",
        "p indirectly positively regulates q iff p is indirectly causally upstream of q and p positively regulates q.",
        (),
        False,
    ),
    "RO_0002409": (
        "indirectly negatively regulates",
        "p indirectly negatively regulates q iff p is indirectly causally upstream of q and p negatively regulates q.",
        (),
        False,
    ),
    "RO_0002410": ("causally related to", None, (), False),
    "RO_0002411": (
        "causally upstream of",
        "p is causally upstream of q iff p is causally related to q, the end of p precedes the end of q, and p is not an occurrent part of q.",
        (),
        False,
    ),
    "RO_0002412": (
        "immediately causally upstream of",
        "p is immediately causally upstream of q iff p is causally upstream of q, and the end of p is coincident with the beginning of q.",
        (),
        False,
    ),
    "RO_0002418": (
        "causally upstream of or within",
        "p is 'causally upstream or within' q iff p is causally related to q, and the end of p precedes, or is coincident with, the end of q.",
        (),
        False,
    ),
    "RO_0002427": (
        "causally downstream of or within",
        "inverse of causally upstream of or within",
        (),
        False,
    ),
    "RO_0002428": (
        "involved in regulation of",
        "c involved in regulation of p if c is involved in some p' and p' regulates some p",
        (),
        False,
    ),
    "RO_0002429": (
        "involved in positive regulation of",
        "c involved in regulation of p if c is involved in some p' and p' positively regulates some p",
        (),
        False,
    ),
    "RO_0002430": (
        "involved in negative regulation of",
        "c involved in regulation of p if c is involved in some p' and p' negatively regulates some p",
        (),
        False,
    ),
    "RO_0002431": (
        "involved in or involved in regulation of",
        "c involved in or regulates p if and only if either (i) c is involved in p or (ii) c is involved in regulation of p",
        (),
        False,
    ),
    "RO_0002434": (
        "interacts with",
        "A relationship that holds between two entities in which the processes executed by the two entities are causally connected.",
        (),
        False,
    ),
    "RO_0002436": (
        "molecularly interacts with",
        "An interaction relationship in which the two partners are molecular entities that directly physically interact with each other for example via a stable binding interaction or a brief interaction during which one modifies the other.",
        (),
        False,
    ),
    "RO_0002447": ("phosphorylates", None, (), False),
    "RO_0002448": (
        "directly regulates activity of",
        "The entity A, immediately upstream of the entity B, has an activity that regulates an activity performed by B. For example, A and B may be gene products and binding of B by A regulates the kinase activity of B. A and B can be physically interacting but not necessarily. Immediately upstream means there are no intermediate entity between A and B.",
        (),
        False,
    ),
    "RO_0002449": (
        "directly negatively regulates activity of",
        "The entity A, immediately upstream of the entity B, has an activity that negatively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A negatively regulates the kinase activity of B.",
        (),
        False,
    ),
    "RO_0002450": (
        "directly positively regulates activity of",
        "The entity A, immediately upstream of the entity B, has an activity that positively regulates an activity performed by B. For example, A and B may be gene products and binding of B by A positively regulates the kinase activity of B.",
        (),
        False,
    ),
    "RO_0002464": ("helper property (not for use in curation)", None, (), False),
    "RO_0002481": ("is kinase activity", None, (), False),
    "RO_0002500": (
        "causal agent in process",
        "A relationship between a material entity and a process where the material entity has some causal role that influences the process",
        (),
        False,
    ),
    "RO_0002501": (
        "causal relation between processes",
        "p is causally related to q if and only if p or any part of p and q or any part of q are linked by a chain of events where each event pair is one where the execution of p influences the execution of q. p may be upstream, downstream, part of, or a container of q.",
        (),
        False,
    ),
    "RO_0002502": ("depends on", None, (), False),
    "RO_0002506": ("causal relation between entities", None, (), False),
    "RO_0002559": ("causally influenced by", None, (), False),
    "RO_0002563": ("interaction relation helper property", None, (), False),
    "RO_0002564": ("molecular interaction relation helper property", None, (), False),
    "RO_0002566": (
        "causally influences",
        "The entity or characteristic A is causally upstream of the entity or characteristic B, A having an effect on B. An entity corresponds to any biological type of entity as long as a mass is measurable. A characteristic corresponds to a particular specificity of an entity (e.g., phenotype, shape, size).",
        (),
        False,
    ),
    "RO_0002578": (
        "directly regulates",
        "p directly regulates q iff p is immediately causally upstream of q and p regulates q.",
        (),
        False,
    ),
    "RO_0002584": (
        "has part structure that is capable of",
        "s 'has part structure that is capable of' p if and only if there exists some part x such that s 'has part' x and x 'capable of' p",
        (),
        False,
    ),
    "RO_0002595": (
        "causal relation between material entity and a process",
        "A relationship that holds between a material entity and a process in which causality is involved, with either the material entity or some part of the material entity exerting some influence over the process, or the process influencing some aspect of the material entity.",
        (),
        False,
    ),
    "RO_0002596": (
        "capable of regulating",
        "Holds between c and p if and only if c is capable of some activity a, and a regulates p.",
        (),
        False,
    ),
    "RO_0002597": (
        "capable of negatively regulating",
        "Holds between c and p if and only if c is capable of some activity a, and a negatively regulates p.",
        (),
        False,
    ),
    "RO_0002598": (
        "capable of positively regulating",
        "Holds between c and p if and only if c is capable of some activity a, and a positively regulates p.",
        (),
        False,
    ),
    "RO_0002608": (
        "process has causal agent",
        "Inverse of 'causal agent in process'",
        (),
        False,
    ),
    "RO_0002629": (
        "directly positively regulates",
        "p directly positively regulates q iff p is immediately causally upstream of q, and p positively regulates q.",
        (),
        False,
    ),
    "RO_0002630": (
        "directly negatively regulates",
        "p directly negatively regulates q iff p is immediately causally upstream of q, and p negatively regulates q.",
        (),
        False,
    ),
    "RO_0004031": (
        "enables subfunction",
        "Holds between an entity and an process P where the entity enables some larger compound process, and that larger process has-part P.",
        (),
        False,
    ),
    "RO_0004032": ("acts upstream of or within, positive effect", None, (), False),
    "RO_0004033": ("acts upstream of or within, negative effect", None, (), False),
    "RO_0004034": (
        "acts upstream of, positive effect",
        "c 'acts upstream of, positive effect' p if c is enables f, and f is causally upstream of p, and the direction of f is positive",
        (),
        False,
    ),
    "RO_0004035": (
        "acts upstream of, negative effect",
        "c 'acts upstream of, negative effect' p if c is enables f, and f is causally upstream of p, and the direction of f is negative",
        (),
        False,
    ),
    "RO_0004046": ("causally upstream of or within, negative effect", None, (), False),
    "RO_0004047": ("causally upstream of or within, positive effect", None, (), False),
    "RO_0011002": (
        "regulates activity of",
        "The entity A has an activity that regulates an activity of the entity B. For example, A and B are gene products where the catalytic activity of A regulates the kinase activity of B.",
        (),
        False,
    ),
    "RO_0012011": (
        "indirectly causally upstream of",
        "p is indirectly causally upstream of q iff p is causally upstream of q and there exists some process r such that p is causally upstream of r and r is causally upstream of q.",
        (),
        False,
    ),
    "RO_0012012": (
        "indirectly regulates",
        "p indirectly regulates q iff p is indirectly causally upstream of q and p regulates q.",
        (),
        False,
    ),
    "RO_0017001": (
        "device utilizes material",
        "X device utilizes material Y means X and Y are material entities, and X is capable of some process P that has input Y.",
        (),
        False,
    ),
    "RO_0019000": (
        "regulates characteristic",
        "A relationship that holds between a process and a characteristic in which process (P) regulates characteristic (C) iff: P results in the existence of C OR affects the intensity or magnitude of C.",
        (),
        False,
    ),
    "RO_0019001": (
        "positively regulates characteristic",
        "A relationship that holds between a process and a characteristic in which process (P) positively regulates characteristic (C) iff: P results in an increase in the intensity or magnitude of C.",
        (),
        False,
    ),
    "RO_0019002": (
        "negatively regulates characteristic",
        "A relationship that holds between a process and a characteristic in which process (P) negatively regulates characteristic (C) iff: P results in a decrease in the intensity or magnitude of C.",
        (),
        False,
    ),
    "UBERON_0000465": (
        "material anatomical entity",
        "Anatomical entity that has mass.",
        (),
        False,
    ),
    "UBERON_0000466": (
        "immaterial anatomical entity",
        "Anatomical entity that has no mass.",
        (),
        False,
    ),
    "UBERON_0000477": (
        "anatomical cluster",
        "Anatomical group whose component anatomical structures lie in close proximity to each other.",
        (),
        False,
    ),
    "UBERON_0001062": (
        "anatomical entity",
        "Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.",
        (),
        False,
    ),
    "UO_0000001": ("length unit", None, (), False),
    "UO_0000002": ("mass unit", None, (), False),
    "UO_0000003": ("time unit", None, (), False),
    "UO_0000005": ("temperature unit", None, (), False),
    "UO_0000006": ("substance unit", None, (), False),
    "UO_0000051": ("concentration unit", None, (), False),
    "UO_0000095": ("volume unit", None, (), False),
    "UO_0000105": ("frequency unit", None, (), False),
    "UO_0000270": ("volumetric flow rate unit", None, (), False),
    "UO_0000280": ("rate unit", None, (), False),
}

PBPKO._terms = _terms

__all__ = [
    "PBPKO",
    "PBPKOType",
]
