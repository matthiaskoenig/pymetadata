"""SBO ontology.

Generated from the ontology release by
`pymetadata.ontologies._ontology_builder`, do not edit.
"""

from pymetadata.ontologies.term import OntologyEnum, TermData

pattern = r"^SBO_\d{7}$"


class SBO(OntologyEnum):
    """SBO ontology."""

    # systems biology representation
    SBO_0000000 = "SBO_0000000"
    SYSTEMS_BIOLOGY_REPRESENTATION = "SBO_0000000"

    # rate law
    SBO_0000001 = "SBO_0000001"
    RATE_LAW = "SBO_0000001"

    # quantitative systems description parameter
    SBO_0000002 = "SBO_0000002"
    QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER = "SBO_0000002"

    # participant role
    SBO_0000003 = "SBO_0000003"
    PARTICIPANT_ROLE = "SBO_0000003"

    # modelling framework
    SBO_0000004 = "SBO_0000004"
    MODELLING_FRAMEWORK = "SBO_0000004"

    # obsolete mathematical expression
    SBO_0000005 = "SBO_0000005"
    OBSOLETE_MATHEMATICAL_EXPRESSION = "SBO_0000005"

    # obsolete parameter
    SBO_0000006 = "SBO_0000006"
    OBSOLETE_PARAMETER = "SBO_0000006"

    # obsolete participant type
    SBO_0000007 = "SBO_0000007"
    OBSOLETE_PARTICIPANT_TYPE = "SBO_0000007"

    # obsolete modelling framework
    SBO_0000008 = "SBO_0000008"
    OBSOLETE_MODELLING_FRAMEWORK = "SBO_0000008"

    # kinetic constant
    SBO_0000009 = "SBO_0000009"
    KINETIC_CONSTANT = "SBO_0000009"

    # reactant
    SBO_0000010 = "SBO_0000010"
    REACTANT = "SBO_0000010"

    # product
    SBO_0000011 = "SBO_0000011"
    PRODUCT = "SBO_0000011"

    # mass action rate law
    SBO_0000012 = "SBO_0000012"
    MASS_ACTION_RATE_LAW = "SBO_0000012"

    # catalyst
    SBO_0000013 = "SBO_0000013"
    CATALYST = "SBO_0000013"

    # enzyme
    SBO_0000014 = "SBO_0000014"
    ENZYME = "SBO_0000014"

    # substrate
    SBO_0000015 = "SBO_0000015"
    SUBSTRATE = "SBO_0000015"

    # unimolecular rate constant
    SBO_0000016 = "SBO_0000016"
    UNIMOLECULAR_RATE_CONSTANT = "SBO_0000016"

    # bimolecular rate constant
    SBO_0000017 = "SBO_0000017"
    BIMOLECULAR_RATE_CONSTANT = "SBO_0000017"

    # trimolecular rate constant
    SBO_0000018 = "SBO_0000018"
    TRIMOLECULAR_RATE_CONSTANT = "SBO_0000018"

    # modifier
    SBO_0000019 = "SBO_0000019"
    MODIFIER = "SBO_0000019"

    # inhibitor
    SBO_0000020 = "SBO_0000020"
    INHIBITOR = "SBO_0000020"

    # potentiator
    SBO_0000021 = "SBO_0000021"
    POTENTIATOR = "SBO_0000021"

    # forward unimolecular rate constant
    SBO_0000022 = "SBO_0000022"
    FORWARD_UNIMOLECULAR_RATE_CONSTANT = "SBO_0000022"

    # forward bimolecular rate constant
    SBO_0000023 = "SBO_0000023"
    FORWARD_BIMOLECULAR_RATE_CONSTANT = "SBO_0000023"

    # forward trimolecular rate constant
    SBO_0000024 = "SBO_0000024"
    FORWARD_TRIMOLECULAR_RATE_CONSTANT = "SBO_0000024"

    # catalytic rate constant
    SBO_0000025 = "SBO_0000025"
    CATALYTIC_RATE_CONSTANT = "SBO_0000025"

    # new term name
    SBO_0000026 = "SBO_0000026"
    NEW_TERM_NAME = "SBO_0000026"

    # Michaelis constant
    SBO_0000027 = "SBO_0000027"
    MICHAELIS_CONSTANT = "SBO_0000027"

    # enzymatic rate law for irreversible non-modulated non-interacting unireactant enzymes
    SBO_0000028 = "SBO_0000028"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_UNIREACTANT_ENZYMES = "SBO_0000028"

    # Henri-Michaelis-Menten rate law
    SBO_0000029 = "SBO_0000029"
    HENRI_MICHAELIS_MENTEN_RATE_LAW = "SBO_0000029"

    # Van Slyke-Cullen rate law
    SBO_0000030 = "SBO_0000030"
    VAN_SLYKE_CULLEN_RATE_LAW = "SBO_0000030"

    # Briggs-Haldane rate law
    SBO_0000031 = "SBO_0000031"
    BRIGGS_HALDANE_RATE_LAW = "SBO_0000031"

    # reverse unimolecular rate constant
    SBO_0000032 = "SBO_0000032"
    REVERSE_UNIMOLECULAR_RATE_CONSTANT = "SBO_0000032"

    # reverse bimolecular rate constant
    SBO_0000033 = "SBO_0000033"
    REVERSE_BIMOLECULAR_RATE_CONSTANT = "SBO_0000033"

    # reverse trimolecular rate constant
    SBO_0000034 = "SBO_0000034"
    REVERSE_TRIMOLECULAR_RATE_CONSTANT = "SBO_0000034"

    # forward unimolecular rate constant, continuous case
    SBO_0000035 = "SBO_0000035"
    FORWARD_UNIMOLECULAR_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000035"

    # forward bimolecular rate constant, continuous case
    SBO_0000036 = "SBO_0000036"
    FORWARD_BIMOLECULAR_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000036"

    # forward trimolecular rate constant, continuous case
    SBO_0000037 = "SBO_0000037"
    FORWARD_TRIMOLECULAR_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000037"

    # reverse unimolecular rate constant, continuous case
    SBO_0000038 = "SBO_0000038"
    REVERSE_UNIMOLECULAR_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000038"

    # reverse bimolecular rate constant, continuous case
    SBO_0000039 = "SBO_0000039"
    REVERSE_BIMOLECULAR_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000039"

    # reverse trimolecular rate constant, continuous case
    SBO_0000040 = "SBO_0000040"
    REVERSE_TRIMOLECULAR_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000040"

    # mass action rate law for irreversible reactions
    SBO_0000041 = "SBO_0000041"
    MASS_ACTION_RATE_LAW_FOR_IRREVERSIBLE_REACTIONS = "SBO_0000041"

    # mass action rate law for reversible reactions
    SBO_0000042 = "SBO_0000042"
    MASS_ACTION_RATE_LAW_FOR_REVERSIBLE_REACTIONS = "SBO_0000042"

    # mass action rate law for zeroth order irreversible reactions
    SBO_0000043 = "SBO_0000043"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_IRREVERSIBLE_REACTIONS = "SBO_0000043"

    # mass action rate law for first order irreversible reactions
    SBO_0000044 = "SBO_0000044"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS = "SBO_0000044"

    # mass action rate law for second order irreversible reactions
    SBO_0000045 = "SBO_0000045"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS = "SBO_0000045"

    # zeroth order rate constant
    SBO_0000046 = "SBO_0000046"
    ZEROTH_ORDER_RATE_CONSTANT = "SBO_0000046"

    # mass action rate law for zeroth order irreversible reactions, continuous scheme
    SBO_0000047 = "SBO_0000047"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_IRREVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000047"
    )

    # forward zeroth order rate constant, continuous case
    SBO_0000048 = "SBO_0000048"
    FORWARD_ZEROTH_ORDER_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000048"

    # mass action rate law for first order irreversible reactions, continuous scheme
    SBO_0000049 = "SBO_0000049"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000049"
    )

    # mass action rate law for second order irreversible reactions, one reactant
    SBO_0000050 = "SBO_0000050"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000050"
    )

    # new term name
    SBO_0000051 = "SBO_0000051"

    # mass action rate law for second order irreversible reactions, one reactant, continuous scheme
    SBO_0000052 = "SBO_0000052"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = "SBO_0000052"

    # mass action rate law for second order irreversible reactions, two reactants
    SBO_0000053 = "SBO_0000053"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000053"
    )

    # mass action rate law for second order irreversible reactions, two reactants, continuous scheme
    SBO_0000054 = "SBO_0000054"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000054"

    # mass action rate law for third order irreversible reactions
    SBO_0000055 = "SBO_0000055"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS = "SBO_0000055"

    # mass action rate law for third order irreversible reactions, one reactant
    SBO_0000056 = "SBO_0000056"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000056"
    )

    # mass action rate law for third order irreversible reactions, one reactant, continuous scheme
    SBO_0000057 = "SBO_0000057"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = "SBO_0000057"

    # mass action rate law for third order irreversible reactions, two reactants
    SBO_0000058 = "SBO_0000058"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000058"
    )

    # mass action rate law for third order irreversible reactions, two reactants, continuous scheme
    SBO_0000059 = "SBO_0000059"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000059"

    # mass action rate law for third order irreversible reactions, three reactants
    SBO_0000060 = "SBO_0000060"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__THREE_REACTANTS = (
        "SBO_0000060"
    )

    # mass action rate law for third order irreversible reactions, three reactants, continuous scheme
    SBO_0000061 = "SBO_0000061"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__THREE_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000061"

    # continuous framework
    SBO_0000062 = "SBO_0000062"
    CONTINUOUS_FRAMEWORK = "SBO_0000062"

    # discrete framework
    SBO_0000063 = "SBO_0000063"
    DISCRETE_FRAMEWORK = "SBO_0000063"

    # mathematical expression
    SBO_0000064 = "SBO_0000064"
    MATHEMATICAL_EXPRESSION = "SBO_0000064"

    # forward zeroth order rate constant, discrete case
    SBO_0000065 = "SBO_0000065"
    FORWARD_ZEROTH_ORDER_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000065"

    # forward unimolecular rate constant, discrete case
    SBO_0000066 = "SBO_0000066"
    FORWARD_UNIMOLECULAR_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000066"

    # forward bimolecular rate constant, discrete case
    SBO_0000067 = "SBO_0000067"
    FORWARD_BIMOLECULAR_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000067"

    # forward trimolecular rate constant, discrete case
    SBO_0000068 = "SBO_0000068"
    FORWARD_TRIMOLECULAR_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000068"

    # mass action rate law for zeroth order reversible reactions
    SBO_0000069 = "SBO_0000069"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_REVERSIBLE_REACTIONS = "SBO_0000069"

    # mass action rate law for zeroth order forward, first order reverse, reversible reactions, continuous scheme
    SBO_0000070 = "SBO_0000070"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = "SBO_0000070"

    # mass action rate law for zeroth order forward, second order reverse, reversible reactions, continuous scheme
    SBO_0000071 = "SBO_0000071"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = "SBO_0000071"

    # mass action rate law for zeroth order forward, second order reverse, reversible reactions, one product, continuous scheme
    SBO_0000072 = "SBO_0000072"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000072"

    # mass action rate law for zeroth order forward, second order reverse, reversible reactions, two products, continuous scheme
    SBO_0000073 = "SBO_0000073"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000073"

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, continuous scheme
    SBO_0000074 = "SBO_0000074"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = "SBO_0000074"

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, one product, continuous scheme
    SBO_0000075 = "SBO_0000075"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000075"

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, two products, continuous scheme
    SBO_0000076 = "SBO_0000076"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000076"

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, three products, continuous scheme
    SBO_0000077 = "SBO_0000077"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000077"

    # mass action rate law for first order reversible reactions
    SBO_0000078 = "SBO_0000078"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_REVERSIBLE_REACTIONS = "SBO_0000078"

    # mass action rate law for first order forward, zeroth order reverse, reversible reactions, continuous scheme
    SBO_0000079 = "SBO_0000079"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = "SBO_0000079"

    # mass action rate law for first order forward, first order reverse, reversible reactions, continuous scheme
    SBO_0000080 = "SBO_0000080"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = "SBO_0000080"

    # mass action rate law for first order forward, second order reverse, reversible reactions
    SBO_0000081 = "SBO_0000081"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS = "SBO_0000081"

    # mass action rate law for first order forward, second order reverse, reversible reactions, one product, continuous scheme
    SBO_0000082 = "SBO_0000082"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000082"

    # mass action rate law for first order forward, second order reverse, reversible reactions, two products, continuous scheme
    SBO_0000083 = "SBO_0000083"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000083"

    # mass action rate law for first order forward, third order reverse, reversible reactions
    SBO_0000084 = "SBO_0000084"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS = "SBO_0000084"

    # mass action rate law for first order forward, third order reverse, reversible reactions, one product, continuous scheme
    SBO_0000085 = "SBO_0000085"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000085"

    # mass action rate law for first order forward, third order reverse, reversible reactions, two products, continuous scheme
    SBO_0000086 = "SBO_0000086"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000086"

    # mass action rate law for first order forward, third order reverse, reversible reactions, three products, continuous scheme
    SBO_0000087 = "SBO_0000087"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000087"

    # mass action rate law for second order reversible reactions
    SBO_0000088 = "SBO_0000088"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_REVERSIBLE_REACTIONS = "SBO_0000088"

    # mass action rate law for second order forward, reversible reactions, one reactant
    SBO_0000089 = "SBO_0000089"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__REVERSIBLE_REACTIONS__ONE_REACTANT = "SBO_0000089"

    # mass action rate law for second order forward, zeroth order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000090 = "SBO_0000090"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = "SBO_0000090"

    # mass action rate law for second order forward, first order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000091 = "SBO_0000091"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = "SBO_0000091"

    # mass action rate law for second order forward, second order reverse, reversible reactions, one reactant
    SBO_0000092 = "SBO_0000092"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = "SBO_0000092"

    # mass action rate law for second order forward, second order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000093 = "SBO_0000093"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000093"

    # mass action rate law for second order forward, second order reverse, reversible reactions, two products, continuous scheme
    SBO_0000094 = "SBO_0000094"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000094"

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant
    SBO_0000095 = "SBO_0000095"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = "SBO_0000095"

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000096 = "SBO_0000096"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000096"

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, two products, continuous scheme
    SBO_0000097 = "SBO_0000097"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000097"

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, three products, continuous scheme
    SBO_0000098 = "SBO_0000098"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000098"

    # mass action rate law for second order forward, reversible reactions, two reactants
    SBO_0000099 = "SBO_0000099"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__REVERSIBLE_REACTIONS__TWO_REACTANTS = "SBO_0000099"

    # mass action rate law for second order forward, zeroth order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000100 = "SBO_0000100"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000100"

    # mass action rate law for second order forward, first order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000101 = "SBO_0000101"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000101"

    # mass action rate law for second order forward, second order reverse, reversible reactions, two reactants
    SBO_0000102 = "SBO_0000102"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = "SBO_0000102"

    # mass action rate law for second order forward, second order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000103 = "SBO_0000103"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000103"

    # mass action rate law for second order forward, second order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000104 = "SBO_0000104"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000104"

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants
    SBO_0000105 = "SBO_0000105"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = "SBO_0000105"

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000106 = "SBO_0000106"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000106"

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000107 = "SBO_0000107"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000107"

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, three products, continuous scheme
    SBO_0000108 = "SBO_0000108"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000108"

    # mass action rate law for third order reversible reactions
    SBO_0000109 = "SBO_0000109"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_REVERSIBLE_REACTIONS = "SBO_0000109"

    # mass action rate law for third order forward, reversible reactions, two reactants
    SBO_0000110 = "SBO_0000110"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__REVERSIBLE_REACTIONS__TWO_REACTANTS = "SBO_0000110"

    # mass action rate law for third order forward, zeroth order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000111 = "SBO_0000111"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000111"

    # mass action rate law for third order forward, first order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000112 = "SBO_0000112"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000112"

    # mass action rate law for third order forward, second order reverse, reversible reactions, two reactants
    SBO_0000113 = "SBO_0000113"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = "SBO_0000113"

    # mass action rate law for third order forward, second order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000114 = "SBO_0000114"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000114"

    # mass action rate law for third order forward, second order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000115 = "SBO_0000115"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000115"

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants
    SBO_0000116 = "SBO_0000116"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = "SBO_0000116"

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000117 = "SBO_0000117"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000117"

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000118 = "SBO_0000118"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000118"

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, three products, continuous scheme
    SBO_0000119 = "SBO_0000119"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000119"

    # mass action rate law for third order forward, reversible reactions, three reactants
    SBO_0000120 = "SBO_0000120"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__REVERSIBLE_REACTIONS__THREE_REACTANTS = "SBO_0000120"

    # mass action rate law for third order forward, zeroth order reverse, reversible reactions, three reactants, continuous scheme
    SBO_0000121 = "SBO_0000121"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000121"

    # mass action rate law for third order forward, first order reverse, reversible reactions, three reactants, continuous scheme
    SBO_0000122 = "SBO_0000122"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__CONTINUOUS_SCHEME = "SBO_0000122"

    # mass action rate law for third order forward, second order reverse, reversible reactions, three reactants
    SBO_0000123 = "SBO_0000123"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS = "SBO_0000123"

    # mass action rate law for third order forward, second order reverse, reversible reactions, three reactants, one product, continuous scheme
    SBO_0000124 = "SBO_0000124"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000124"

    # mass action rate law for third order forward, second order reverse, reversible reactions, three reactants, two products, continuous scheme
    SBO_0000125 = "SBO_0000125"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000125"

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants
    SBO_0000126 = "SBO_0000126"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS = "SBO_0000126"

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, one product, continuous scheme
    SBO_0000127 = "SBO_0000127"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000127"

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, two products, continuous scheme
    SBO_0000128 = "SBO_0000128"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000128"

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, three products, continuous scheme
    SBO_0000129 = "SBO_0000129"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000129"

    # mass action rate law for third order forward, reversible reactions, one reactant
    SBO_0000130 = "SBO_0000130"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000130"
    )

    # mass action rate law for third order forward, zeroth order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000131 = "SBO_0000131"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = "SBO_0000131"

    # mass action rate law for third order forward, first order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000132 = "SBO_0000132"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = "SBO_0000132"

    # mass action rate law for third order forward, second order reverse, reversible reactions, one reactant
    SBO_0000133 = "SBO_0000133"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = "SBO_0000133"

    # mass action rate law for third order forward, second order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000134 = "SBO_0000134"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000134"

    # mass action rate law for third order forward, second order reverse, reversible reactions, one reactant, two products, continuous scheme
    SBO_0000135 = "SBO_0000135"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000135"

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant
    SBO_0000136 = "SBO_0000136"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = "SBO_0000136"

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000137 = "SBO_0000137"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = "SBO_0000137"

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, two products, continuous scheme
    SBO_0000138 = "SBO_0000138"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__TWO_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000138"

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, three products, continuous scheme
    SBO_0000139 = "SBO_0000139"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__THREE_PRODUCTS__CONTINUOUS_SCHEME = "SBO_0000139"

    # mass action rate law for zeroth order irreversible reactions, discrete scheme
    SBO_0000140 = "SBO_0000140"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_IRREVERSIBLE_REACTIONS__DISCRETE_SCHEME = (
        "SBO_0000140"
    )

    # mass action rate law for first order irreversible reactions, discrete scheme
    SBO_0000141 = "SBO_0000141"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS__DISCRETE_SCHEME = (
        "SBO_0000141"
    )

    # mass action rate law for second order irreversible reactions, one reactant, discrete scheme
    SBO_0000142 = "SBO_0000142"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__DISCRETE_SCHEME = "SBO_0000142"

    # mass action rate law for second order irreversible reactions, two reactants, discrete scheme
    SBO_0000143 = "SBO_0000143"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__DISCRETE_SCHEME = "SBO_0000143"

    # mass action rate law for third order irreversible reactions, one reactant, discrete scheme
    SBO_0000144 = "SBO_0000144"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__DISCRETE_SCHEME = "SBO_0000144"

    # mass action rate law for third order irreversible reactions, two reactants, discrete scheme
    SBO_0000145 = "SBO_0000145"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__DISCRETE_SCHEME = "SBO_0000145"

    # mass action rate law for third order irreversible reactions, three reactants, discrete scheme
    SBO_0000146 = "SBO_0000146"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__THREE_REACTANTS__DISCRETE_SCHEME = "SBO_0000146"

    # thermodynamic temperature
    SBO_0000147 = "SBO_0000147"
    THERMODYNAMIC_TEMPERATURE = "SBO_0000147"

    # temperature difference
    SBO_0000148 = "SBO_0000148"
    TEMPERATURE_DIFFERENCE = "SBO_0000148"

    # number of substrates
    SBO_0000149 = "SBO_0000149"
    NUMBER_OF_SUBSTRATES = "SBO_0000149"

    # enzymatic rate law for irreversible non-modulated non-interacting reactant enzymes
    SBO_0000150 = "SBO_0000150"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_REACTANT_ENZYMES = "SBO_0000150"

    # enzymatic rate law for irreversible non-modulated non-interacting bireactant enzymes
    SBO_0000151 = "SBO_0000151"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_BIREACTANT_ENZYMES = "SBO_0000151"

    # enzymatic rate law for irreversible non-modulated non-interacting trireactant enzymes
    SBO_0000152 = "SBO_0000152"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_TRIREACTANT_ENZYMES = "SBO_0000152"

    # forward rate constant
    SBO_0000153 = "SBO_0000153"
    FORWARD_RATE_CONSTANT = "SBO_0000153"

    # forward rate constant, continuous case
    SBO_0000154 = "SBO_0000154"
    FORWARD_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000154"

    # forward rate constant, discrete case
    SBO_0000155 = "SBO_0000155"
    FORWARD_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000155"

    # reverse rate constant
    SBO_0000156 = "SBO_0000156"
    REVERSE_RATE_CONSTANT = "SBO_0000156"

    # number of reactants
    SBO_0000157 = "SBO_0000157"
    NUMBER_OF_REACTANTS = "SBO_0000157"

    # order of a reaction with respect to a reactant
    SBO_0000158 = "SBO_0000158"
    ORDER_OF_A_REACTION_WITH_RESPECT_TO_A_REACTANT = "SBO_0000158"

    # non-integral order rate constant
    SBO_0000159 = "SBO_0000159"
    NON_INTEGRAL_ORDER_RATE_CONSTANT = "SBO_0000159"

    # forward non-integral order rate constant
    SBO_0000160 = "SBO_0000160"
    FORWARD_NON_INTEGRAL_ORDER_RATE_CONSTANT = "SBO_0000160"

    # reverse non-integral order rate constant
    SBO_0000161 = "SBO_0000161"
    REVERSE_NON_INTEGRAL_ORDER_RATE_CONSTANT = "SBO_0000161"

    # forward zeroth order rate constant
    SBO_0000162 = "SBO_0000162"
    FORWARD_ZEROTH_ORDER_RATE_CONSTANT = "SBO_0000162"

    # mass action rate law for irreversible reactions, continuous scheme
    SBO_0000163 = "SBO_0000163"
    MASS_ACTION_RATE_LAW_FOR_IRREVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = "SBO_0000163"

    # second order irreversible mass action kinetics, continuous scheme
    SBO_0000164 = "SBO_0000164"
    SECOND_ORDER_IRREVERSIBLE_MASS_ACTION_KINETICS__CONTINUOUS_SCHEME = "SBO_0000164"

    # third order irreversible mass action kinetics, continuous scheme
    SBO_0000165 = "SBO_0000165"
    THIRD_ORDER_IRREVERSIBLE_MASS_ACTION_KINETICS__CONTINUOUS_SCHEME = "SBO_0000165"

    # mass action rate law for irreversible reactions, discrete scheme
    SBO_0000166 = "SBO_0000166"
    MASS_ACTION_RATE_LAW_FOR_IRREVERSIBLE_REACTIONS__DISCRETE_SCHEME = "SBO_0000166"

    # biochemical or transport reaction
    SBO_0000167 = "SBO_0000167"
    BIOCHEMICAL_OR_TRANSPORT_REACTION = "SBO_0000167"

    # control
    SBO_0000168 = "SBO_0000168"
    CONTROL = "SBO_0000168"

    # inhibition
    SBO_0000169 = "SBO_0000169"
    INHIBITION = "SBO_0000169"

    # stimulation
    SBO_0000170 = "SBO_0000170"
    STIMULATION = "SBO_0000170"

    # necessary stimulation
    SBO_0000171 = "SBO_0000171"
    NECESSARY_STIMULATION = "SBO_0000171"

    # catalysis
    SBO_0000172 = "SBO_0000172"
    CATALYSIS = "SBO_0000172"

    # and
    SBO_0000173 = "SBO_0000173"
    AND = "SBO_0000173"

    # or
    SBO_0000174 = "SBO_0000174"
    OR = "SBO_0000174"

    # xor
    SBO_0000175 = "SBO_0000175"
    XOR = "SBO_0000175"

    # biochemical reaction
    SBO_0000176 = "SBO_0000176"
    BIOCHEMICAL_REACTION = "SBO_0000176"

    # non-covalent binding
    SBO_0000177 = "SBO_0000177"
    NON_COVALENT_BINDING = "SBO_0000177"

    # cleavage
    SBO_0000178 = "SBO_0000178"
    CLEAVAGE = "SBO_0000178"

    # degradation
    SBO_0000179 = "SBO_0000179"
    DEGRADATION = "SBO_0000179"

    # dissociation
    SBO_0000180 = "SBO_0000180"
    DISSOCIATION = "SBO_0000180"

    # conformational transition
    SBO_0000181 = "SBO_0000181"
    CONFORMATIONAL_TRANSITION = "SBO_0000181"

    # conversion
    SBO_0000182 = "SBO_0000182"
    CONVERSION = "SBO_0000182"

    # transcription
    SBO_0000183 = "SBO_0000183"
    TRANSCRIPTION = "SBO_0000183"

    # translation
    SBO_0000184 = "SBO_0000184"
    TRANSLATION = "SBO_0000184"

    # translocation reaction
    SBO_0000185 = "SBO_0000185"
    TRANSLOCATION_REACTION = "SBO_0000185"

    # maximal velocity
    SBO_0000186 = "SBO_0000186"
    MAXIMAL_VELOCITY = "SBO_0000186"

    # Henri-Michaelis-Menten equation, Vmax form
    SBO_0000187 = "SBO_0000187"
    HENRI_MICHAELIS_MENTEN_EQUATION__VMAX_FORM = "SBO_0000187"

    # number of biochemical items
    SBO_0000188 = "SBO_0000188"
    NUMBER_OF_BIOCHEMICAL_ITEMS = "SBO_0000188"

    # number of binding sites
    SBO_0000189 = "SBO_0000189"
    NUMBER_OF_BINDING_SITES = "SBO_0000189"

    # Hill coefficient
    SBO_0000190 = "SBO_0000190"
    HILL_COEFFICIENT = "SBO_0000190"

    # Hill constant
    SBO_0000191 = "SBO_0000191"
    HILL_CONSTANT = "SBO_0000191"

    # Hill-type rate law, generalised form
    SBO_0000192 = "SBO_0000192"
    HILL_TYPE_RATE_LAW__GENERALISED_FORM = "SBO_0000192"

    # equilibrium or steady-state constant
    SBO_0000193 = "SBO_0000193"
    EQUILIBRIUM_OR_STEADY_STATE_CONSTANT = "SBO_0000193"

    # pseudo-dissociation constant
    SBO_0000194 = "SBO_0000194"
    PSEUDO_DISSOCIATION_CONSTANT = "SBO_0000194"

    # Hill-type rate law, microscopic form
    SBO_0000195 = "SBO_0000195"
    HILL_TYPE_RATE_LAW__MICROSCOPIC_FORM = "SBO_0000195"

    # concentration of an entity pool
    SBO_0000196 = "SBO_0000196"
    CONCENTRATION_OF_AN_ENTITY_POOL = "SBO_0000196"

    # specific concentration of an entity
    SBO_0000197 = "SBO_0000197"
    SPECIFIC_CONCENTRATION_OF_AN_ENTITY = "SBO_0000197"

    # Hill-type rate law, reduced form
    SBO_0000198 = "SBO_0000198"
    HILL_TYPE_RATE_LAW__REDUCED_FORM = "SBO_0000198"

    # normalised enzymatic rate law for unireactant enzymes
    SBO_0000199 = "SBO_0000199"
    NORMALISED_ENZYMATIC_RATE_LAW_FOR_UNIREACTANT_ENZYMES = "SBO_0000199"

    # redox reaction
    SBO_0000200 = "SBO_0000200"
    REDOX_REACTION = "SBO_0000200"

    # oxidation
    SBO_0000201 = "SBO_0000201"
    OXIDATION = "SBO_0000201"

    # reduction
    SBO_0000202 = "SBO_0000202"
    REDUCTION = "SBO_0000202"

    # duplication
    SBO_0000203 = "SBO_0000203"
    DUPLICATION = "SBO_0000203"

    # DNA replication
    SBO_0000204 = "SBO_0000204"
    DNA_REPLICATION = "SBO_0000204"

    # composite biochemical process
    SBO_0000205 = "SBO_0000205"
    COMPOSITE_BIOCHEMICAL_PROCESS = "SBO_0000205"

    # competitive inhibitor
    SBO_0000206 = "SBO_0000206"
    COMPETITIVE_INHIBITOR = "SBO_0000206"

    # non-competitive inhibitor
    SBO_0000207 = "SBO_0000207"
    NON_COMPETITIVE_INHIBITOR = "SBO_0000207"

    # acid-base reaction
    SBO_0000208 = "SBO_0000208"
    ACID_BASE_REACTION = "SBO_0000208"

    # ionisation
    SBO_0000209 = "SBO_0000209"
    IONISATION = "SBO_0000209"

    # addition of a chemical group
    SBO_0000210 = "SBO_0000210"
    ADDITION_OF_A_CHEMICAL_GROUP = "SBO_0000210"

    # removal of a chemical group
    SBO_0000211 = "SBO_0000211"
    REMOVAL_OF_A_CHEMICAL_GROUP = "SBO_0000211"

    # protonation
    SBO_0000212 = "SBO_0000212"
    PROTONATION = "SBO_0000212"

    # deprotonation
    SBO_0000213 = "SBO_0000213"
    DEPROTONATION = "SBO_0000213"

    # methylation
    SBO_0000214 = "SBO_0000214"
    METHYLATION = "SBO_0000214"

    # acetylation
    SBO_0000215 = "SBO_0000215"
    ACETYLATION = "SBO_0000215"

    # phosphorylation
    SBO_0000216 = "SBO_0000216"
    PHOSPHORYLATION = "SBO_0000216"

    # glycosylation
    SBO_0000217 = "SBO_0000217"
    GLYCOSYLATION = "SBO_0000217"

    # palmitoylation
    SBO_0000218 = "SBO_0000218"
    PALMITOYLATION = "SBO_0000218"

    # myristoylation
    SBO_0000219 = "SBO_0000219"
    MYRISTOYLATION = "SBO_0000219"

    # sulfation
    SBO_0000220 = "SBO_0000220"
    SULFATION = "SBO_0000220"

    # prenylation
    SBO_0000221 = "SBO_0000221"
    PRENYLATION = "SBO_0000221"

    # farnesylation
    SBO_0000222 = "SBO_0000222"
    FARNESYLATION = "SBO_0000222"

    # geranylgeranylation
    SBO_0000223 = "SBO_0000223"
    GERANYLGERANYLATION = "SBO_0000223"

    # ubiquitination
    SBO_0000224 = "SBO_0000224"
    UBIQUITINATION = "SBO_0000224"

    # delay
    SBO_0000225 = "SBO_0000225"
    DELAY = "SBO_0000225"

    # density of an entity pool
    SBO_0000226 = "SBO_0000226"
    DENSITY_OF_AN_ENTITY_POOL = "SBO_0000226"

    # mass density of an entity
    SBO_0000227 = "SBO_0000227"
    MASS_DENSITY_OF_AN_ENTITY = "SBO_0000227"

    # volume density of an entity
    SBO_0000228 = "SBO_0000228"
    VOLUME_DENSITY_OF_AN_ENTITY = "SBO_0000228"

    # area density of an entity
    SBO_0000229 = "SBO_0000229"
    AREA_DENSITY_OF_AN_ENTITY = "SBO_0000229"

    # linear density of an entity
    SBO_0000230 = "SBO_0000230"
    LINEAR_DENSITY_OF_AN_ENTITY = "SBO_0000230"

    # occurring entity representation
    SBO_0000231 = "SBO_0000231"
    OCCURRING_ENTITY_REPRESENTATION = "SBO_0000231"

    # obsolete event
    SBO_0000232 = "SBO_0000232"
    OBSOLETE_EVENT = "SBO_0000232"

    # hydroxylation
    SBO_0000233 = "SBO_0000233"
    HYDROXYLATION = "SBO_0000233"

    # logical framework
    SBO_0000234 = "SBO_0000234"
    LOGICAL_FRAMEWORK = "SBO_0000234"

    # participant
    SBO_0000235 = "SBO_0000235"
    PARTICIPANT = "SBO_0000235"

    # physical entity representation
    SBO_0000236 = "SBO_0000236"
    PHYSICAL_ENTITY_REPRESENTATION = "SBO_0000236"

    # logical combination
    SBO_0000237 = "SBO_0000237"
    LOGICAL_COMBINATION = "SBO_0000237"

    # not
    SBO_0000238 = "SBO_0000238"
    NOT = "SBO_0000238"

    # allosteric control
    SBO_0000239 = "SBO_0000239"
    ALLOSTERIC_CONTROL = "SBO_0000239"

    # material entity
    SBO_0000240 = "SBO_0000240"
    MATERIAL_ENTITY = "SBO_0000240"

    # functional entity
    SBO_0000241 = "SBO_0000241"
    FUNCTIONAL_ENTITY = "SBO_0000241"

    # channel
    SBO_0000242 = "SBO_0000242"
    CHANNEL = "SBO_0000242"

    # gene
    SBO_0000243 = "SBO_0000243"
    GENE = "SBO_0000243"

    # receptor
    SBO_0000244 = "SBO_0000244"
    RECEPTOR = "SBO_0000244"

    # macromolecule
    SBO_0000245 = "SBO_0000245"
    MACROMOLECULE = "SBO_0000245"

    # information macromolecule
    SBO_0000246 = "SBO_0000246"
    INFORMATION_MACROMOLECULE = "SBO_0000246"

    # simple chemical
    SBO_0000247 = "SBO_0000247"
    SIMPLE_CHEMICAL = "SBO_0000247"

    # chemical macromolecule
    SBO_0000248 = "SBO_0000248"
    CHEMICAL_MACROMOLECULE = "SBO_0000248"

    # polysaccharide
    SBO_0000249 = "SBO_0000249"
    POLYSACCHARIDE = "SBO_0000249"

    # ribonucleic acid
    SBO_0000250 = "SBO_0000250"
    RIBONUCLEIC_ACID = "SBO_0000250"

    # deoxyribonucleic acid
    SBO_0000251 = "SBO_0000251"
    DEOXYRIBONUCLEIC_ACID = "SBO_0000251"

    # polypeptide chain
    SBO_0000252 = "SBO_0000252"
    POLYPEPTIDE_CHAIN = "SBO_0000252"

    # non-covalent complex
    SBO_0000253 = "SBO_0000253"
    NON_COVALENT_COMPLEX = "SBO_0000253"

    # electrical resistance
    SBO_0000254 = "SBO_0000254"
    ELECTRICAL_RESISTANCE = "SBO_0000254"

    # physical characteristic
    SBO_0000255 = "SBO_0000255"
    PHYSICAL_CHARACTERISTIC = "SBO_0000255"

    # biochemical parameter
    SBO_0000256 = "SBO_0000256"
    BIOCHEMICAL_PARAMETER = "SBO_0000256"

    # conductance
    SBO_0000257 = "SBO_0000257"
    CONDUCTANCE = "SBO_0000257"

    # capacitance
    SBO_0000258 = "SBO_0000258"
    CAPACITANCE = "SBO_0000258"

    # voltage
    SBO_0000259 = "SBO_0000259"
    VOLTAGE = "SBO_0000259"

    # enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by one inhibitor
    SBO_0000260 = "SBO_0000260"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_ONE_INHIBITOR = "SBO_0000260"

    # inhibitory constant
    SBO_0000261 = "SBO_0000261"
    INHIBITORY_CONSTANT = "SBO_0000261"

    # enzymatic rate law for simple uncompetitive inhibition of irreversible unireactant enzymes
    SBO_0000262 = "SBO_0000262"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_UNCOMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES = "SBO_0000262"

    # relative equilibrium constant
    SBO_0000263 = "SBO_0000263"
    RELATIVE_EQUILIBRIUM_CONSTANT = "SBO_0000263"

    # relative inhibition constant
    SBO_0000264 = "SBO_0000264"
    RELATIVE_INHIBITION_CONSTANT = "SBO_0000264"

    # enzymatic rate law for simple mixed-type inhibition of irreversible unireactant enzymes
    SBO_0000265 = "SBO_0000265"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_MIXED_TYPE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES = "SBO_0000265"

    # enzymatic rate law for simple irreversible non-competitive inhibition of unireactant enzymes
    SBO_0000266 = "SBO_0000266"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_IRREVERSIBLE_NON_COMPETITIVE_INHIBITION_OF_UNIREACTANT_ENZYMES = "SBO_0000266"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by one inhibitor
    SBO_0000267 = "SBO_0000267"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_ONE_INHIBITOR = "SBO_0000267"

    # enzymatic rate law
    SBO_0000268 = "SBO_0000268"
    ENZYMATIC_RATE_LAW = "SBO_0000268"

    # enzymatic rate law for unireactant enzymes
    SBO_0000269 = "SBO_0000269"
    ENZYMATIC_RATE_LAW_FOR_UNIREACTANT_ENZYMES = "SBO_0000269"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by exclusive inhibitors
    SBO_0000270 = "SBO_0000270"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_EXCLUSIVE_INHIBITORS = "SBO_0000270"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by two exclusive inhibitors
    SBO_0000271 = "SBO_0000271"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_EXCLUSIVE_INHIBITORS = "SBO_0000271"

    # number of inhibitors
    SBO_0000272 = "SBO_0000272"
    NUMBER_OF_INHIBITORS = "SBO_0000272"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by non-exclusive non-cooperative inhibitors
    SBO_0000273 = "SBO_0000273"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_NON_EXCLUSIVE_NON_COOPERATIVE_INHIBITORS = "SBO_0000273"

    # enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by two non-exclusive, non-cooperative inhibitors
    SBO_0000274 = "SBO_0000274"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_NON_EXCLUSIVE__NON_COOPERATIVE_INHIBITORS = "SBO_0000274"

    # enzymatic rate law for mixed-type inhibition of irreversible enzymes by mutually exclusive inhibitors
    SBO_0000275 = "SBO_0000275"
    ENZYMATIC_RATE_LAW_FOR_MIXED_TYPE_INHIBITION_OF_IRREVERSIBLE_ENZYMES_BY_MUTUALLY_EXCLUSIVE_INHIBITORS = "SBO_0000275"

    # enzymatic rate law for mixed-type inhibition of irreversible unireactant enzymes by two inhibitors
    SBO_0000276 = "SBO_0000276"
    ENZYMATIC_RATE_LAW_FOR_MIXED_TYPE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_INHIBITORS = "SBO_0000276"

    # enzymatic rate law for non-competitive inhibition of irreversible unireactant enzymes by two exclusively binding inhibitors
    SBO_0000277 = "SBO_0000277"
    ENZYMATIC_RATE_LAW_FOR_NON_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_EXCLUSIVELY_BINDING_INHIBITORS = "SBO_0000277"

    # messenger RNA
    SBO_0000278 = "SBO_0000278"
    MESSENGER_RNA = "SBO_0000278"

    # pressure
    SBO_0000279 = "SBO_0000279"
    PRESSURE = "SBO_0000279"

    # ligand
    SBO_0000280 = "SBO_0000280"
    LIGAND = "SBO_0000280"

    # equilibrium constant
    SBO_0000281 = "SBO_0000281"
    EQUILIBRIUM_CONSTANT = "SBO_0000281"

    # dissociation constant
    SBO_0000282 = "SBO_0000282"
    DISSOCIATION_CONSTANT = "SBO_0000282"

    # acid dissociation constant
    SBO_0000283 = "SBO_0000283"
    ACID_DISSOCIATION_CONSTANT = "SBO_0000283"

    # transporter
    SBO_0000284 = "SBO_0000284"
    TRANSPORTER = "SBO_0000284"

    # material entity of unspecified nature
    SBO_0000285 = "SBO_0000285"
    MATERIAL_ENTITY_OF_UNSPECIFIED_NATURE = "SBO_0000285"

    # multimer
    SBO_0000286 = "SBO_0000286"
    MULTIMER = "SBO_0000286"

    # EC50
    SBO_0000287 = "SBO_0000287"
    EC50 = "SBO_0000287"

    # IC50
    SBO_0000288 = "SBO_0000288"
    IC50 = "SBO_0000288"

    # functional compartment
    SBO_0000289 = "SBO_0000289"
    FUNCTIONAL_COMPARTMENT = "SBO_0000289"

    # physical compartment
    SBO_0000290 = "SBO_0000290"
    PHYSICAL_COMPARTMENT = "SBO_0000290"

    # empty set
    SBO_0000291 = "SBO_0000291"
    EMPTY_SET = "SBO_0000291"

    # spatial continuous framework
    SBO_0000292 = "SBO_0000292"
    SPATIAL_CONTINUOUS_FRAMEWORK = "SBO_0000292"

    # non-spatial continuous framework
    SBO_0000293 = "SBO_0000293"
    NON_SPATIAL_CONTINUOUS_FRAMEWORK = "SBO_0000293"

    # spatial discrete framework
    SBO_0000294 = "SBO_0000294"
    SPATIAL_DISCRETE_FRAMEWORK = "SBO_0000294"

    # non-spatial discrete framework
    SBO_0000295 = "SBO_0000295"
    NON_SPATIAL_DISCRETE_FRAMEWORK = "SBO_0000295"

    # macromolecular complex
    SBO_0000296 = "SBO_0000296"
    MACROMOLECULAR_COMPLEX = "SBO_0000296"

    # protein complex
    SBO_0000297 = "SBO_0000297"
    PROTEIN_COMPLEX = "SBO_0000297"

    # synthetic chemical compound
    SBO_0000298 = "SBO_0000298"
    SYNTHETIC_CHEMICAL_COMPOUND = "SBO_0000298"

    # metabolite
    SBO_0000299 = "SBO_0000299"
    METABOLITE = "SBO_0000299"

    # total concentration of enzyme
    SBO_0000300 = "SBO_0000300"
    TOTAL_CONCENTRATION_OF_ENZYME = "SBO_0000300"

    # total catalytic efficiency
    SBO_0000301 = "SBO_0000301"
    TOTAL_CATALYTIC_EFFICIENCY = "SBO_0000301"

    # catalytic efficiency
    SBO_0000302 = "SBO_0000302"
    CATALYTIC_EFFICIENCY = "SBO_0000302"

    # biochemical potential
    SBO_0000303 = "SBO_0000303"
    BIOCHEMICAL_POTENTIAL = "SBO_0000303"

    # pH
    SBO_0000304 = "SBO_0000304"
    PH = "SBO_0000304"

    # pOH
    SBO_0000305 = "SBO_0000305"
    POH = "SBO_0000305"

    # pK
    SBO_0000306 = "SBO_0000306"
    PK = "SBO_0000306"

    # pKa
    SBO_0000307 = "SBO_0000307"
    PKA = "SBO_0000307"

    # equilibrium or steady-state characteristic
    SBO_0000308 = "SBO_0000308"
    EQUILIBRIUM_OR_STEADY_STATE_CHARACTERISTIC = "SBO_0000308"

    # dissociation characteristic
    SBO_0000309 = "SBO_0000309"
    DISSOCIATION_CHARACTERISTIC = "SBO_0000309"

    # acid dissociation characteristic
    SBO_0000310 = "SBO_0000310"
    ACID_DISSOCIATION_CHARACTERISTIC = "SBO_0000310"

    # heterogeneous nuclear RNA
    SBO_0000311 = "SBO_0000311"
    HETEROGENEOUS_NUCLEAR_RNA = "SBO_0000311"

    # mature messenger RNA
    SBO_0000312 = "SBO_0000312"
    MATURE_MESSENGER_RNA = "SBO_0000312"

    # transfer RNA
    SBO_0000313 = "SBO_0000313"
    TRANSFER_RNA = "SBO_0000313"

    # ribosomal RNA
    SBO_0000314 = "SBO_0000314"
    RIBOSOMAL_RNA = "SBO_0000314"

    # ribozyme
    SBO_0000315 = "SBO_0000315"
    RIBOZYME = "SBO_0000315"

    # microRNA
    SBO_0000316 = "SBO_0000316"
    MICRORNA = "SBO_0000316"

    # small interfering RNA
    SBO_0000317 = "SBO_0000317"
    SMALL_INTERFERING_RNA = "SBO_0000317"

    # small nuclear RNA
    SBO_0000318 = "SBO_0000318"
    SMALL_NUCLEAR_RNA = "SBO_0000318"

    # small nucleolar RNA
    SBO_0000319 = "SBO_0000319"
    SMALL_NUCLEOLAR_RNA = "SBO_0000319"

    # product catalytic rate constant
    SBO_0000320 = "SBO_0000320"
    PRODUCT_CATALYTIC_RATE_CONSTANT = "SBO_0000320"

    # substrate catalytic rate constant
    SBO_0000321 = "SBO_0000321"
    SUBSTRATE_CATALYTIC_RATE_CONSTANT = "SBO_0000321"

    # Michaelis constant for substrate
    SBO_0000322 = "SBO_0000322"
    MICHAELIS_CONSTANT_FOR_SUBSTRATE = "SBO_0000322"

    # Michaelis constant for product
    SBO_0000323 = "SBO_0000323"
    MICHAELIS_CONSTANT_FOR_PRODUCT = "SBO_0000323"

    # forward maximal velocity
    SBO_0000324 = "SBO_0000324"
    FORWARD_MAXIMAL_VELOCITY = "SBO_0000324"

    # reverse maximal velocity
    SBO_0000325 = "SBO_0000325"
    REVERSE_MAXIMAL_VELOCITY = "SBO_0000325"

    # enzymatic rate law for non-modulated unireactant enzymes
    SBO_0000326 = "SBO_0000326"
    ENZYMATIC_RATE_LAW_FOR_NON_MODULATED_UNIREACTANT_ENZYMES = "SBO_0000326"

    # non-macromolecular ion
    SBO_0000327 = "SBO_0000327"
    NON_MACROMOLECULAR_ION = "SBO_0000327"

    # non-macromolecular radical
    SBO_0000328 = "SBO_0000328"
    NON_MACROMOLECULAR_RADICAL = "SBO_0000328"

    # transcription start site
    SBO_0000329 = "SBO_0000329"
    TRANSCRIPTION_START_SITE = "SBO_0000329"

    # dephosphorylation
    SBO_0000330 = "SBO_0000330"
    DEPHOSPHORYLATION = "SBO_0000330"

    # half-life
    SBO_0000331 = "SBO_0000331"
    HALF_LIFE = "SBO_0000331"

    # half-life of an exponential decay
    SBO_0000332 = "SBO_0000332"
    HALF_LIFE_OF_AN_EXPONENTIAL_DECAY = "SBO_0000332"

    # monoexponential decay rate law
    SBO_0000333 = "SBO_0000333"
    MONOEXPONENTIAL_DECAY_RATE_LAW = "SBO_0000333"

    # non-coding RNA
    SBO_0000334 = "SBO_0000334"
    NON_CODING_RNA = "SBO_0000334"

    # gene coding region
    SBO_0000335 = "SBO_0000335"
    GENE_CODING_REGION = "SBO_0000335"

    # interactor
    SBO_0000336 = "SBO_0000336"
    INTERACTOR = "SBO_0000336"

    # association constant
    SBO_0000337 = "SBO_0000337"
    ASSOCIATION_CONSTANT = "SBO_0000337"

    # dissociation rate constant
    SBO_0000338 = "SBO_0000338"
    DISSOCIATION_RATE_CONSTANT = "SBO_0000338"

    # bimolecular association rate constant
    SBO_0000339 = "SBO_0000339"
    BIMOLECULAR_ASSOCIATION_RATE_CONSTANT = "SBO_0000339"

    # trimolecular association rate constant
    SBO_0000340 = "SBO_0000340"
    TRIMOLECULAR_ASSOCIATION_RATE_CONSTANT = "SBO_0000340"

    # association rate constant
    SBO_0000341 = "SBO_0000341"
    ASSOCIATION_RATE_CONSTANT = "SBO_0000341"

    # molecular or genetic interaction
    SBO_0000342 = "SBO_0000342"
    MOLECULAR_OR_GENETIC_INTERACTION = "SBO_0000342"

    # genetic interaction
    SBO_0000343 = "SBO_0000343"
    GENETIC_INTERACTION = "SBO_0000343"

    # molecular interaction
    SBO_0000344 = "SBO_0000344"
    MOLECULAR_INTERACTION = "SBO_0000344"

    # time
    SBO_0000345 = "SBO_0000345"
    TIME = "SBO_0000345"

    # temporal measure
    SBO_0000346 = "SBO_0000346"
    TEMPORAL_MEASURE = "SBO_0000346"

    # duration
    SBO_0000347 = "SBO_0000347"
    DURATION = "SBO_0000347"

    # exponential time constant
    SBO_0000348 = "SBO_0000348"
    EXPONENTIAL_TIME_CONSTANT = "SBO_0000348"

    # inactivation rate constant
    SBO_0000349 = "SBO_0000349"
    INACTIVATION_RATE_CONSTANT = "SBO_0000349"

    # forward reaction velocity
    SBO_0000350 = "SBO_0000350"
    FORWARD_REACTION_VELOCITY = "SBO_0000350"

    # reverse zeroth order rate constant
    SBO_0000352 = "SBO_0000352"
    REVERSE_ZEROTH_ORDER_RATE_CONSTANT = "SBO_0000352"

    # reverse reaction velocity
    SBO_0000353 = "SBO_0000353"
    REVERSE_REACTION_VELOCITY = "SBO_0000353"

    # informational molecule segment
    SBO_0000354 = "SBO_0000354"
    INFORMATIONAL_MOLECULE_SEGMENT = "SBO_0000354"

    # conservation law
    SBO_0000355 = "SBO_0000355"
    CONSERVATION_LAW = "SBO_0000355"

    # decay constant
    SBO_0000356 = "SBO_0000356"
    DECAY_CONSTANT = "SBO_0000356"

    # biological effect of a perturbation
    SBO_0000357 = "SBO_0000357"
    BIOLOGICAL_EFFECT_OF_A_PERTURBATION = "SBO_0000357"

    # phenotype
    SBO_0000358 = "SBO_0000358"
    PHENOTYPE = "SBO_0000358"

    # mass conservation law
    SBO_0000359 = "SBO_0000359"
    MASS_CONSERVATION_LAW = "SBO_0000359"

    # quantity of an entity pool
    SBO_0000360 = "SBO_0000360"
    QUANTITY_OF_AN_ENTITY_POOL = "SBO_0000360"

    # amount of an entity pool
    SBO_0000361 = "SBO_0000361"
    AMOUNT_OF_AN_ENTITY_POOL = "SBO_0000361"

    # concentration conservation law
    SBO_0000362 = "SBO_0000362"
    CONCENTRATION_CONSERVATION_LAW = "SBO_0000362"

    # activation constant
    SBO_0000363 = "SBO_0000363"
    ACTIVATION_CONSTANT = "SBO_0000363"

    # multimer cardinality
    SBO_0000364 = "SBO_0000364"
    MULTIMER_CARDINALITY = "SBO_0000364"

    # forward non-integral order rate constant, continuous case
    SBO_0000365 = "SBO_0000365"
    FORWARD_NON_INTEGRAL_ORDER_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000365"

    # forward non-integral order rate constant, discrete case
    SBO_0000366 = "SBO_0000366"
    FORWARD_NON_INTEGRAL_ORDER_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000366"

    # reverse non-integral order rate constant, discrete case
    SBO_0000367 = "SBO_0000367"
    REVERSE_NON_INTEGRAL_ORDER_RATE_CONSTANT__DISCRETE_CASE = "SBO_0000367"

    # reverse non-integral order rate constant, continuous case
    SBO_0000368 = "SBO_0000368"
    REVERSE_NON_INTEGRAL_ORDER_RATE_CONSTANT__CONTINUOUS_CASE = "SBO_0000368"

    # gene regulatory region
    SBO_0000369 = "SBO_0000369"
    GENE_REGULATORY_REGION = "SBO_0000369"

    # Michaelis constant in non-equilibrium situation
    SBO_0000370 = "SBO_0000370"
    MICHAELIS_CONSTANT_IN_NON_EQUILIBRIUM_SITUATION = "SBO_0000370"

    # Michaelis constant in quasi-steady state situation
    SBO_0000371 = "SBO_0000371"
    MICHAELIS_CONSTANT_IN_QUASI_STEADY_STATE_SITUATION = "SBO_0000371"

    # Michaelis constant in irreversible situation
    SBO_0000372 = "SBO_0000372"
    MICHAELIS_CONSTANT_IN_IRREVERSIBLE_SITUATION = "SBO_0000372"

    # Michaelis constant in fast equilibrium situation
    SBO_0000373 = "SBO_0000373"
    MICHAELIS_CONSTANT_IN_FAST_EQUILIBRIUM_SITUATION = "SBO_0000373"

    # relationship
    SBO_0000374 = "SBO_0000374"
    RELATIONSHIP = "SBO_0000374"

    # process
    SBO_0000375 = "SBO_0000375"
    PROCESS = "SBO_0000375"

    # hydrolysis
    SBO_0000376 = "SBO_0000376"
    HYDROLYSIS = "SBO_0000376"

    # isomerisation
    SBO_0000377 = "SBO_0000377"
    ISOMERISATION = "SBO_0000377"

    # enzymatic rate law for inhibition of irreversible unireactant enzymes by competing substrates
    SBO_0000378 = "SBO_0000378"
    ENZYMATIC_RATE_LAW_FOR_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_COMPETING_SUBSTRATES = "SBO_0000378"

    # enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by two non-exclusive inhibitors
    SBO_0000379 = "SBO_0000379"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_NON_EXCLUSIVE_INHIBITORS = "SBO_0000379"

    # biochemical coefficient
    SBO_0000380 = "SBO_0000380"
    BIOCHEMICAL_COEFFICIENT = "SBO_0000380"

    # biochemical proportionality coefficient
    SBO_0000381 = "SBO_0000381"
    BIOCHEMICAL_PROPORTIONALITY_COEFFICIENT = "SBO_0000381"

    # biochemical exponential coefficient
    SBO_0000382 = "SBO_0000382"
    BIOCHEMICAL_EXPONENTIAL_COEFFICIENT = "SBO_0000382"

    # biochemical cooperative inhibition coefficient
    SBO_0000383 = "SBO_0000383"
    BIOCHEMICAL_COOPERATIVE_INHIBITION_COEFFICIENT = "SBO_0000383"

    # biochemical inhibitory proportionality coefficient
    SBO_0000384 = "SBO_0000384"
    BIOCHEMICAL_INHIBITORY_PROPORTIONALITY_COEFFICIENT = "SBO_0000384"

    # biochemical cooperative inhibitor substrate coefficient
    SBO_0000385 = "SBO_0000385"
    BIOCHEMICAL_COOPERATIVE_INHIBITOR_SUBSTRATE_COEFFICIENT = "SBO_0000385"

    # enzymatic rate law for inhibition of irreversible unireactant enzymes by single competing substrate
    SBO_0000386 = "SBO_0000386"
    ENZYMATIC_RATE_LAW_FOR_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_SINGLE_COMPETING_SUBSTRATE = "SBO_0000386"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzyme by product
    SBO_0000387 = "SBO_0000387"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYME_BY_PRODUCT = "SBO_0000387"

    # enzymatic rate law for inhibition of irreversible unireactant enzymes by single competing substrate with product inhibition
    SBO_0000388 = "SBO_0000388"
    ENZYMATIC_RATE_LAW_FOR_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_SINGLE_COMPETING_SUBSTRATE_WITH_PRODUCT_INHIBITION = "SBO_0000388"

    # switch value
    SBO_0000389 = "SBO_0000389"
    SWITCH_VALUE = "SBO_0000389"

    # boolean switch
    SBO_0000390 = "SBO_0000390"
    BOOLEAN_SWITCH = "SBO_0000390"

    # steady state expression
    SBO_0000391 = "SBO_0000391"
    STEADY_STATE_EXPRESSION = "SBO_0000391"

    # equivalence
    SBO_0000392 = "SBO_0000392"
    EQUIVALENCE = "SBO_0000392"

    # production
    SBO_0000393 = "SBO_0000393"
    PRODUCTION = "SBO_0000393"

    # consumption
    SBO_0000394 = "SBO_0000394"
    CONSUMPTION = "SBO_0000394"

    # encapsulating process
    SBO_0000395 = "SBO_0000395"
    ENCAPSULATING_PROCESS = "SBO_0000395"

    # uncertain process
    SBO_0000396 = "SBO_0000396"
    UNCERTAIN_PROCESS = "SBO_0000396"

    # omitted process
    SBO_0000397 = "SBO_0000397"
    OMITTED_PROCESS = "SBO_0000397"

    # logical relationship
    SBO_0000398 = "SBO_0000398"
    LOGICAL_RELATIONSHIP = "SBO_0000398"

    # decarboxylation
    SBO_0000399 = "SBO_0000399"
    DECARBOXYLATION = "SBO_0000399"

    # decarbonylation
    SBO_0000400 = "SBO_0000400"
    DECARBONYLATION = "SBO_0000400"

    # deamination
    SBO_0000401 = "SBO_0000401"
    DEAMINATION = "SBO_0000401"

    # transfer of a chemical group
    SBO_0000402 = "SBO_0000402"
    TRANSFER_OF_A_CHEMICAL_GROUP = "SBO_0000402"

    # transamination
    SBO_0000403 = "SBO_0000403"
    TRANSAMINATION = "SBO_0000403"

    # unit of genetic information
    SBO_0000404 = "SBO_0000404"
    UNIT_OF_GENETIC_INFORMATION = "SBO_0000404"

    # perturbing agent
    SBO_0000405 = "SBO_0000405"
    PERTURBING_AGENT = "SBO_0000405"

    # observable
    SBO_0000406 = "SBO_0000406"
    OBSERVABLE = "SBO_0000406"

    # absolute inhibition
    SBO_0000407 = "SBO_0000407"
    ABSOLUTE_INHIBITION = "SBO_0000407"

    # biological activity
    SBO_0000408 = "SBO_0000408"
    BIOLOGICAL_ACTIVITY = "SBO_0000408"

    # interaction outcome
    SBO_0000409 = "SBO_0000409"
    INTERACTION_OUTCOME = "SBO_0000409"

    # implicit compartment
    SBO_0000410 = "SBO_0000410"
    IMPLICIT_COMPARTMENT = "SBO_0000410"

    # absolute stimulation
    SBO_0000411 = "SBO_0000411"
    ABSOLUTE_STIMULATION = "SBO_0000411"

    # biological activity
    SBO_0000412 = "SBO_0000412"

    # positional relationship
    SBO_0000413 = "SBO_0000413"
    POSITIONAL_RELATIONSHIP = "SBO_0000413"

    # cis
    SBO_0000414 = "SBO_0000414"
    CIS = "SBO_0000414"

    # trans
    SBO_0000415 = "SBO_0000415"
    TRANS = "SBO_0000415"

    # true
    SBO_0000416 = "SBO_0000416"
    TRUE = "SBO_0000416"

    # false
    SBO_0000417 = "SBO_0000417"
    FALSE = "SBO_0000417"

    # multimer of complexes
    SBO_0000418 = "SBO_0000418"
    MULTIMER_OF_COMPLEXES = "SBO_0000418"

    # multimer of informational molecule segment
    SBO_0000419 = "SBO_0000419"
    MULTIMER_OF_INFORMATIONAL_MOLECULE_SEGMENT = "SBO_0000419"

    # multimer of macromolecules
    SBO_0000420 = "SBO_0000420"
    MULTIMER_OF_MACROMOLECULES = "SBO_0000420"

    # multimer of simple chemicals
    SBO_0000421 = "SBO_0000421"
    MULTIMER_OF_SIMPLE_CHEMICALS = "SBO_0000421"

    # isoinhibition constant
    SBO_0000422 = "SBO_0000422"
    ISOINHIBITION_CONSTANT = "SBO_0000422"

    # pseudo-dissociation constant for product
    SBO_0000423 = "SBO_0000423"
    PSEUDO_DISSOCIATION_CONSTANT_FOR_PRODUCT = "SBO_0000423"

    # pseudo-dissociation constant for substrate
    SBO_0000424 = "SBO_0000424"
    PSEUDO_DISSOCIATION_CONSTANT_FOR_SUBSTRATE = "SBO_0000424"

    # reversible Hill-type enzymatic rate law
    SBO_0000425 = "SBO_0000425"
    REVERSIBLE_HILL_TYPE_ENZYMATIC_RATE_LAW = "SBO_0000425"

    # modulated reversible Hill-type rate law
    SBO_0000426 = "SBO_0000426"
    MODULATED_REVERSIBLE_HILL_TYPE_RATE_LAW = "SBO_0000426"

    # modulated reversible Hill-type rate law with one modifier
    SBO_0000427 = "SBO_0000427"
    MODULATED_REVERSIBLE_HILL_TYPE_RATE_LAW_WITH_ONE_MODIFIER = "SBO_0000427"

    # modulated reversible Hill-type rate law with two modifiers
    SBO_0000428 = "SBO_0000428"
    MODULATED_REVERSIBLE_HILL_TYPE_RATE_LAW_WITH_TWO_MODIFIERS = "SBO_0000428"

    # enzymatic rate law for multireactant enzymes
    SBO_0000429 = "SBO_0000429"
    ENZYMATIC_RATE_LAW_FOR_MULTIREACTANT_ENZYMES = "SBO_0000429"

    # enzymatic rate law for modulated unireactant enzymes
    SBO_0000430 = "SBO_0000430"
    ENZYMATIC_RATE_LAW_FOR_MODULATED_UNIREACTANT_ENZYMES = "SBO_0000430"

    # unmodulated reversible Hill-type rate law
    SBO_0000431 = "SBO_0000431"
    UNMODULATED_REVERSIBLE_HILL_TYPE_RATE_LAW = "SBO_0000431"

    # irreversible Michaelis Menten rate law for two substrates
    SBO_0000432 = "SBO_0000432"
    IRREVERSIBLE_MICHAELIS_MENTEN_RATE_LAW_FOR_TWO_SUBSTRATES = "SBO_0000432"

    # Ordered Bi-Bi mechanism rate law
    SBO_0000433 = "SBO_0000433"
    ORDERED_BI_BI_MECHANISM_RATE_LAW = "SBO_0000433"

    # Ordered Bi-Uni mechanism rate law
    SBO_0000434 = "SBO_0000434"
    ORDERED_BI_UNI_MECHANISM_RATE_LAW = "SBO_0000434"

    # Ordered Uni-Bi mechanism rate law
    SBO_0000435 = "SBO_0000435"
    ORDERED_UNI_BI_MECHANISM_RATE_LAW = "SBO_0000435"

    # Ping Pong Bi-Bi mechanism rate law
    SBO_0000436 = "SBO_0000436"
    PING_PONG_BI_BI_MECHANISM_RATE_LAW = "SBO_0000436"

    # reversible Iso Uni-Uni
    SBO_0000437 = "SBO_0000437"
    REVERSIBLE_ISO_UNI_UNI = "SBO_0000437"

    # reversible Uni-Uni
    SBO_0000438 = "SBO_0000438"
    REVERSIBLE_UNI_UNI = "SBO_0000438"

    # Uni-Uni Reversible using Haldane relationship
    SBO_0000439 = "SBO_0000439"
    UNI_UNI_REVERSIBLE_USING_HALDANE_RELATIONSHIP = "SBO_0000439"

    # enzymatic rate law for irreversible allosteric inhibition
    SBO_0000440 = "SBO_0000440"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_ALLOSTERIC_INHIBITION = "SBO_0000440"

    # enzymatic rate law for mixed-type inhibition of reversible enzymes by mutually exclusive inhibitors
    SBO_0000441 = "SBO_0000441"
    ENZYMATIC_RATE_LAW_FOR_MIXED_TYPE_INHIBITION_OF_REVERSIBLE_ENZYMES_BY_MUTUALLY_EXCLUSIVE_INHIBITORS = "SBO_0000441"

    # enzymatic rate law for simple reversible non-competitive inhibition of unireactant enzymes
    SBO_0000442 = "SBO_0000442"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_REVERSIBLE_NON_COMPETITIVE_INHIBITION_OF_UNIREACTANT_ENZYMES = "SBO_0000442"

    # enzymatic rate law for reversible essential activation
    SBO_0000443 = "SBO_0000443"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_ESSENTIAL_ACTIVATION = "SBO_0000443"

    # enzymatic rate law for reversible mixed activation
    SBO_0000444 = "SBO_0000444"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_MIXED_ACTIVATION = "SBO_0000444"

    # enzymatic rate law for irreversible substrate activation
    SBO_0000445 = "SBO_0000445"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_SUBSTRATE_ACTIVATION = "SBO_0000445"

    # enzymatic rate law for irrreversible mixed activation
    SBO_0000446 = "SBO_0000446"
    ENZYMATIC_RATE_LAW_FOR_IRRREVERSIBLE_MIXED_ACTIVATION = "SBO_0000446"

    # enzymatic rate law for reversible catalytic activation with one activator
    SBO_0000447 = "SBO_0000447"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_CATALYTIC_ACTIVATION_WITH_ONE_ACTIVATOR = (
        "SBO_0000447"
    )

    # enzymatic rate law for reversible specific activation
    SBO_0000448 = "SBO_0000448"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_SPECIFIC_ACTIVATION = "SBO_0000448"

    # enzymatic rate law for irreversible catalytic activation with one activator
    SBO_0000449 = "SBO_0000449"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_CATALYTIC_ACTIVATION_WITH_ONE_ACTIVATOR = (
        "SBO_0000449"
    )

    # enzymatic rate law for irreversible specific activation
    SBO_0000450 = "SBO_0000450"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_SPECIFIC_ACTIVATION = "SBO_0000450"

    # enzymatic rate law for reversible reactions with competitive inhibition
    SBO_0000451 = "SBO_0000451"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_REACTIONS_WITH_COMPETITIVE_INHIBITION = (
        "SBO_0000451"
    )

    # enzymatic rate law for reversible competitive inhibition by one inhibitor
    SBO_0000452 = "SBO_0000452"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_COMPETITIVE_INHIBITION_BY_ONE_INHIBITOR = (
        "SBO_0000452"
    )

    # enzymatic rate law for reversible empirical allosteric inhibition by one inhibitor
    SBO_0000453 = "SBO_0000453"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_EMPIRICAL_ALLOSTERIC_INHIBITION_BY_ONE_INHIBITOR = "SBO_0000453"

    # enzymatic rate law for reversible substrate inhibition
    SBO_0000454 = "SBO_0000454"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_SUBSTRATE_INHIBITION = "SBO_0000454"

    # enzymatic rate law for irreversible substrate inhibition
    SBO_0000455 = "SBO_0000455"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_SUBSTRATE_INHIBITION = "SBO_0000455"

    # enzymatic rate law for reversible unireactant enzyme with a single hyperbolic modulator
    SBO_0000456 = "SBO_0000456"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_UNIREACTANT_ENZYME_WITH_A_SINGLE_HYPERBOLIC_MODULATOR = "SBO_0000456"

    # enzymatic rate law for irreversible unireactant enzyme with a single hyperbolic modulator
    SBO_0000457 = "SBO_0000457"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_UNIREACTANT_ENZYME_WITH_A_SINGLE_HYPERBOLIC_MODULATOR = "SBO_0000457"

    # enzymatic rate law for simple uncompetitive inhibition of reversible unireactant enzymes
    SBO_0000458 = "SBO_0000458"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_UNCOMPETITIVE_INHIBITION_OF_REVERSIBLE_UNIREACTANT_ENZYMES = "SBO_0000458"

    # stimulator
    SBO_0000459 = "SBO_0000459"
    STIMULATOR = "SBO_0000459"

    # enzymatic catalyst
    SBO_0000460 = "SBO_0000460"
    ENZYMATIC_CATALYST = "SBO_0000460"

    # essential activator
    SBO_0000461 = "SBO_0000461"
    ESSENTIAL_ACTIVATOR = "SBO_0000461"

    # non-essential activator
    SBO_0000462 = "SBO_0000462"
    NON_ESSENTIAL_ACTIVATOR = "SBO_0000462"

    # standard biochemical potential
    SBO_0000463 = "SBO_0000463"
    STANDARD_BIOCHEMICAL_POTENTIAL = "SBO_0000463"

    # state variable assignment
    SBO_0000464 = "SBO_0000464"
    STATE_VARIABLE_ASSIGNMENT = "SBO_0000464"

    # spatial measure
    SBO_0000465 = "SBO_0000465"
    SPATIAL_MEASURE = "SBO_0000465"

    # length
    SBO_0000466 = "SBO_0000466"
    LENGTH = "SBO_0000466"

    # area
    SBO_0000467 = "SBO_0000467"
    AREA = "SBO_0000467"

    # volume
    SBO_0000468 = "SBO_0000468"
    VOLUME = "SBO_0000468"

    # containment
    SBO_0000469 = "SBO_0000469"
    CONTAINMENT = "SBO_0000469"

    # mass fraction
    SBO_0000470 = "SBO_0000470"
    MASS_FRACTION = "SBO_0000470"

    # molal concentration of an entity
    SBO_0000471 = "SBO_0000471"
    MOLAL_CONCENTRATION_OF_AN_ENTITY = "SBO_0000471"

    # molar concentration of an entity
    SBO_0000472 = "SBO_0000472"
    MOLAR_CONCENTRATION_OF_AN_ENTITY = "SBO_0000472"

    # denotement
    SBO_0000473 = "SBO_0000473"
    DENOTEMENT = "SBO_0000473"

    # convenience function
    SBO_0000474 = "SBO_0000474"
    CONVENIENCE_FUNCTION = "SBO_0000474"

    # periodic forcing function
    SBO_0000475 = "SBO_0000475"
    PERIODIC_FORCING_FUNCTION = "SBO_0000475"

    # period
    SBO_0000476 = "SBO_0000476"
    PERIOD = "SBO_0000476"

    # phase shift
    SBO_0000477 = "SBO_0000477"
    PHASE_SHIFT = "SBO_0000477"

    # powered product of Michaelis constant
    SBO_0000478 = "SBO_0000478"
    POWERED_PRODUCT_OF_MICHAELIS_CONSTANT = "SBO_0000478"

    # powered product of substrate Michaelis constants
    SBO_0000479 = "SBO_0000479"
    POWERED_PRODUCT_OF_SUBSTRATE_MICHAELIS_CONSTANTS = "SBO_0000479"

    # powered product of product Michaelis constants
    SBO_0000480 = "SBO_0000480"
    POWERED_PRODUCT_OF_PRODUCT_MICHAELIS_CONSTANTS = "SBO_0000480"

    # stoichiometric coefficient
    SBO_0000481 = "SBO_0000481"
    STOICHIOMETRIC_COEFFICIENT = "SBO_0000481"

    # geometric mean rate constant
    SBO_0000482 = "SBO_0000482"
    GEOMETRIC_MEAN_RATE_CONSTANT = "SBO_0000482"

    # forward geometric mean rate constant
    SBO_0000483 = "SBO_0000483"
    FORWARD_GEOMETRIC_MEAN_RATE_CONSTANT = "SBO_0000483"

    # reverse geometric mean rate constant
    SBO_0000484 = "SBO_0000484"
    REVERSE_GEOMETRIC_MEAN_RATE_CONSTANT = "SBO_0000484"

    # basal rate constant
    SBO_0000485 = "SBO_0000485"
    BASAL_RATE_CONSTANT = "SBO_0000485"

    # relative basal rate constant
    SBO_0000486 = "SBO_0000486"
    RELATIVE_BASAL_RATE_CONSTANT = "SBO_0000486"

    # relative activity function
    SBO_0000487 = "SBO_0000487"
    RELATIVE_ACTIVITY_FUNCTION = "SBO_0000487"

    # relative activation function
    SBO_0000488 = "SBO_0000488"
    RELATIVE_ACTIVATION_FUNCTION = "SBO_0000488"

    # relative inhibition function
    SBO_0000489 = "SBO_0000489"
    RELATIVE_INHIBITION_FUNCTION = "SBO_0000489"

    # number of products
    SBO_0000490 = "SBO_0000490"
    NUMBER_OF_PRODUCTS = "SBO_0000490"

    # diffusion coefficient
    SBO_0000491 = "SBO_0000491"
    DIFFUSION_COEFFICIENT = "SBO_0000491"

    # amplitude
    SBO_0000492 = "SBO_0000492"
    AMPLITUDE = "SBO_0000492"

    # functional domain
    SBO_0000493 = "SBO_0000493"
    FUNCTIONAL_DOMAIN = "SBO_0000493"

    # binding site
    SBO_0000494 = "SBO_0000494"
    BINDING_SITE = "SBO_0000494"

    # catalytic site
    SBO_0000495 = "SBO_0000495"
    CATALYTIC_SITE = "SBO_0000495"

    # transmembrane domain
    SBO_0000496 = "SBO_0000496"
    TRANSMEMBRANE_DOMAIN = "SBO_0000496"

    # ternary switch
    SBO_0000497 = "SBO_0000497"
    TERNARY_SWITCH = "SBO_0000497"

    # relative activity
    SBO_0000498 = "SBO_0000498"
    RELATIVE_ACTIVITY = "SBO_0000498"

    # genetic interaction
    SBO_0000499 = "SBO_0000499"

    # genetic suppression
    SBO_0000500 = "SBO_0000500"
    GENETIC_SUPPRESSION = "SBO_0000500"

    # genetic enhancement
    SBO_0000501 = "SBO_0000501"
    GENETIC_ENHANCEMENT = "SBO_0000501"

    # synthetic lethality
    SBO_0000502 = "SBO_0000502"
    SYNTHETIC_LETHALITY = "SBO_0000502"

    # number of entity pool constituents
    SBO_0000503 = "SBO_0000503"
    NUMBER_OF_ENTITY_POOL_CONSTITUENTS = "SBO_0000503"

    # mass of an entity pool
    SBO_0000504 = "SBO_0000504"
    MASS_OF_AN_ENTITY_POOL = "SBO_0000504"

    # concentration of enzyme
    SBO_0000505 = "SBO_0000505"
    CONCENTRATION_OF_ENZYME = "SBO_0000505"

    # mass of enzyme
    SBO_0000506 = "SBO_0000506"
    MASS_OF_ENZYME = "SBO_0000506"

    # number of an enzyme
    SBO_0000507 = "SBO_0000507"
    NUMBER_OF_AN_ENZYME = "SBO_0000507"

    # number of a reactant
    SBO_0000508 = "SBO_0000508"
    NUMBER_OF_A_REACTANT = "SBO_0000508"

    # concentration of reactant
    SBO_0000509 = "SBO_0000509"
    CONCENTRATION_OF_REACTANT = "SBO_0000509"

    # mass of reactant
    SBO_0000510 = "SBO_0000510"
    MASS_OF_REACTANT = "SBO_0000510"

    # number of a product
    SBO_0000511 = "SBO_0000511"
    NUMBER_OF_A_PRODUCT = "SBO_0000511"

    # concentration of product
    SBO_0000512 = "SBO_0000512"
    CONCENTRATION_OF_PRODUCT = "SBO_0000512"

    # mass of product
    SBO_0000513 = "SBO_0000513"
    MASS_OF_PRODUCT = "SBO_0000513"

    # number of a substrate
    SBO_0000514 = "SBO_0000514"
    NUMBER_OF_A_SUBSTRATE = "SBO_0000514"

    # concentration of substrate
    SBO_0000515 = "SBO_0000515"
    CONCENTRATION_OF_SUBSTRATE = "SBO_0000515"

    # mass of substrate
    SBO_0000516 = "SBO_0000516"
    MASS_OF_SUBSTRATE = "SBO_0000516"

    # number of a modifier
    SBO_0000517 = "SBO_0000517"
    NUMBER_OF_A_MODIFIER = "SBO_0000517"

    # concentration of modifier
    SBO_0000518 = "SBO_0000518"
    CONCENTRATION_OF_MODIFIER = "SBO_0000518"

    # mass of modifier
    SBO_0000519 = "SBO_0000519"
    MASS_OF_MODIFIER = "SBO_0000519"

    # number of an inhibitor
    SBO_0000520 = "SBO_0000520"
    NUMBER_OF_AN_INHIBITOR = "SBO_0000520"

    # concentration of inhibitor
    SBO_0000521 = "SBO_0000521"
    CONCENTRATION_OF_INHIBITOR = "SBO_0000521"

    # mass of inhibitor
    SBO_0000522 = "SBO_0000522"
    MASS_OF_INHIBITOR = "SBO_0000522"

    # number of an activator
    SBO_0000523 = "SBO_0000523"
    NUMBER_OF_AN_ACTIVATOR = "SBO_0000523"

    # concentration of activator
    SBO_0000524 = "SBO_0000524"
    CONCENTRATION_OF_ACTIVATOR = "SBO_0000524"

    # mass of activator
    SBO_0000525 = "SBO_0000525"
    MASS_OF_ACTIVATOR = "SBO_0000525"

    # protein complex formation
    SBO_0000526 = "SBO_0000526"
    PROTEIN_COMPLEX_FORMATION = "SBO_0000526"

    # modular rate law
    SBO_0000527 = "SBO_0000527"
    MODULAR_RATE_LAW = "SBO_0000527"

    # common modular rate law
    SBO_0000528 = "SBO_0000528"
    COMMON_MODULAR_RATE_LAW = "SBO_0000528"

    # direct binding modular rate law
    SBO_0000529 = "SBO_0000529"
    DIRECT_BINDING_MODULAR_RATE_LAW = "SBO_0000529"

    # simultaneous binding modular rate law
    SBO_0000530 = "SBO_0000530"
    SIMULTANEOUS_BINDING_MODULAR_RATE_LAW = "SBO_0000530"

    # power-law modular rate law
    SBO_0000531 = "SBO_0000531"
    POWER_LAW_MODULAR_RATE_LAW = "SBO_0000531"

    # force-dependent modular rate law
    SBO_0000532 = "SBO_0000532"
    FORCE_DEPENDENT_MODULAR_RATE_LAW = "SBO_0000532"

    # specific activator
    SBO_0000533 = "SBO_0000533"
    SPECIFIC_ACTIVATOR = "SBO_0000533"

    # catalytic activator
    SBO_0000534 = "SBO_0000534"
    CATALYTIC_ACTIVATOR = "SBO_0000534"

    # binding activator
    SBO_0000535 = "SBO_0000535"
    BINDING_ACTIVATOR = "SBO_0000535"

    # partial inhibitor
    SBO_0000536 = "SBO_0000536"
    PARTIAL_INHIBITOR = "SBO_0000536"

    # complete inhibitor
    SBO_0000537 = "SBO_0000537"
    COMPLETE_INHIBITOR = "SBO_0000537"

    # ionic permeability
    SBO_0000538 = "SBO_0000538"
    IONIC_PERMEABILITY = "SBO_0000538"

    # probabilistic parameter
    SBO_0000539 = "SBO_0000539"
    PROBABILISTIC_PARAMETER = "SBO_0000539"

    # fraction of an entity pool
    SBO_0000540 = "SBO_0000540"
    FRACTION_OF_AN_ENTITY_POOL = "SBO_0000540"

    # mole fraction
    SBO_0000541 = "SBO_0000541"
    MOLE_FRACTION = "SBO_0000541"

    # basic reproductive ratio
    SBO_0000542 = "SBO_0000542"
    BASIC_REPRODUCTIVE_RATIO = "SBO_0000542"

    # protein aggregate
    SBO_0000543 = "SBO_0000543"
    PROTEIN_AGGREGATE = "SBO_0000543"

    # metadata representation
    SBO_0000544 = "SBO_0000544"
    METADATA_REPRESENTATION = "SBO_0000544"

    # systems description parameter
    SBO_0000545 = "SBO_0000545"
    SYSTEMS_DESCRIPTION_PARAMETER = "SBO_0000545"

    # qualitative systems description parameter
    SBO_0000546 = "SBO_0000546"
    QUALITATIVE_SYSTEMS_DESCRIPTION_PARAMETER = "SBO_0000546"

    # boolean logical framework
    SBO_0000547 = "SBO_0000547"
    BOOLEAN_LOGICAL_FRAMEWORK = "SBO_0000547"

    # multi-valued logical framework
    SBO_0000548 = "SBO_0000548"
    MULTI_VALUED_LOGICAL_FRAMEWORK = "SBO_0000548"

    # fuzzy logical framework
    SBO_0000549 = "SBO_0000549"
    FUZZY_LOGICAL_FRAMEWORK = "SBO_0000549"

    # annotation
    SBO_0000550 = "SBO_0000550"
    ANNOTATION = "SBO_0000550"

    # controlled short label
    SBO_0000551 = "SBO_0000551"
    CONTROLLED_SHORT_LABEL = "SBO_0000551"

    # reference annotation
    SBO_0000552 = "SBO_0000552"
    REFERENCE_ANNOTATION = "SBO_0000552"

    # bibliographical reference
    SBO_0000553 = "SBO_0000553"
    BIBLIOGRAPHICAL_REFERENCE = "SBO_0000553"

    # database cross reference
    SBO_0000554 = "SBO_0000554"
    DATABASE_CROSS_REFERENCE = "SBO_0000554"

    # controlled annotation
    SBO_0000555 = "SBO_0000555"
    CONTROLLED_ANNOTATION = "SBO_0000555"

    # uncontrolled annotation
    SBO_0000556 = "SBO_0000556"
    UNCONTROLLED_ANNOTATION = "SBO_0000556"

    # embedded annotation
    SBO_0000557 = "SBO_0000557"
    EMBEDDED_ANNOTATION = "SBO_0000557"

    # specific activity
    SBO_0000558 = "SBO_0000558"
    SPECIFIC_ACTIVITY = "SBO_0000558"

    # enzyme activity
    SBO_0000559 = "SBO_0000559"
    ENZYME_ACTIVITY = "SBO_0000559"

    # mass action rate law for first order irreversible reactions, single essential stimulator, continuous scheme
    SBO_0000560 = "SBO_0000560"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS__SINGLE_ESSENTIAL_STIMULATOR__CONTINUOUS_SCHEME = "SBO_0000560"

    # mass action rate law for first order irreversible reactions, single essential stimulator, discrete scheme
    SBO_0000561 = "SBO_0000561"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS__SINGLE_ESSENTIAL_STIMULATOR__DISCRETE_SCHEME = "SBO_0000561"

    # mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator
    SBO_0000562 = "SBO_0000562"
    MASS_ACTION_LIKE_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__ONE_ESSENTIAL_STIMULATOR = "SBO_0000562"

    # mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator, continuous scheme
    SBO_0000563 = "SBO_0000563"
    MASS_ACTION_LIKE_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__ONE_ESSENTIAL_STIMULATOR__CONTINUOUS_SCHEME = "SBO_0000563"

    # mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator, discrete scheme
    SBO_0000564 = "SBO_0000564"
    MASS_ACTION_LIKE_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__ONE_ESSENTIAL_STIMULATOR__DISCRETE_SCHEME = "SBO_0000564"

    # systems description constant
    SBO_0000565 = "SBO_0000565"
    SYSTEMS_DESCRIPTION_CONSTANT = "SBO_0000565"

    # relative permeability
    SBO_0000566 = "SBO_0000566"
    RELATIVE_PERMEABILITY = "SBO_0000566"

    # universal gas constant
    SBO_0000567 = "SBO_0000567"
    UNIVERSAL_GAS_CONSTANT = "SBO_0000567"

    # Faraday constant
    SBO_0000568 = "SBO_0000568"
    FARADAY_CONSTANT = "SBO_0000568"

    # Goldman equation
    SBO_0000569 = "SBO_0000569"
    GOLDMAN_EQUATION = "SBO_0000569"

    # Nernst potential
    SBO_0000570 = "SBO_0000570"
    NERNST_POTENTIAL = "SBO_0000570"

    # thermodynamic parameter
    SBO_0000571 = "SBO_0000571"
    THERMODYNAMIC_PARAMETER = "SBO_0000571"

    # enthalpy
    SBO_0000572 = "SBO_0000572"
    ENTHALPY = "SBO_0000572"

    # enthalpy change
    SBO_0000573 = "SBO_0000573"
    ENTHALPY_CHANGE = "SBO_0000573"

    # standard enthalpy of formation
    SBO_0000574 = "SBO_0000574"
    STANDARD_ENTHALPY_OF_FORMATION = "SBO_0000574"

    # standard enthalpy of reaction
    SBO_0000575 = "SBO_0000575"
    STANDARD_ENTHALPY_OF_REACTION = "SBO_0000575"

    # entropy
    SBO_0000576 = "SBO_0000576"
    ENTROPY = "SBO_0000576"

    # entropy change
    SBO_0000577 = "SBO_0000577"
    ENTROPY_CHANGE = "SBO_0000577"

    # standard entropy of reaction
    SBO_0000578 = "SBO_0000578"
    STANDARD_ENTROPY_OF_REACTION_ = "SBO_0000578"

    # standard entropy of formation
    SBO_0000579 = "SBO_0000579"
    STANDARD_ENTROPY_OF_FORMATION = "SBO_0000579"

    # Gibbs free energy
    SBO_0000580 = "SBO_0000580"
    GIBBS_FREE_ENERGY = "SBO_0000580"

    # Gibbs free energy change
    SBO_0000581 = "SBO_0000581"
    GIBBS_FREE_ENERGY_CHANGE = "SBO_0000581"

    # standard Gibbs free energy of formation
    SBO_0000582 = "SBO_0000582"
    STANDARD_GIBBS_FREE_ENERGY_OF_FORMATION = "SBO_0000582"

    # standard Gibbs free energy of reaction
    SBO_0000583 = "SBO_0000583"
    STANDARD_GIBBS_FREE_ENERGY_OF_REACTION = "SBO_0000583"

    # temporal offset
    SBO_0000584 = "SBO_0000584"
    TEMPORAL_OFFSET = "SBO_0000584"

    # simulation duration
    SBO_0000585 = "SBO_0000585"
    SIMULATION_DURATION = "SBO_0000585"

    # model time
    SBO_0000586 = "SBO_0000586"
    MODEL_TIME = "SBO_0000586"

    # transcellular membrane influx reaction
    SBO_0000587 = "SBO_0000587"
    TRANSCELLULAR_MEMBRANE_INFLUX_REACTION = "SBO_0000587"

    # transcellular membrane efflux reaction
    SBO_0000588 = "SBO_0000588"
    TRANSCELLULAR_MEMBRANE_EFFLUX_REACTION = "SBO_0000588"

    # genetic production
    SBO_0000589 = "SBO_0000589"
    GENETIC_PRODUCTION = "SBO_0000589"

    # promoter
    SBO_0000590 = "SBO_0000590"
    PROMOTER = "SBO_0000590"

    # petri net transition
    SBO_0000591 = "SBO_0000591"
    PETRI_NET_TRANSITION = "SBO_0000591"

    # discrete amount of an entity pool
    SBO_0000592 = "SBO_0000592"
    DISCRETE_AMOUNT_OF_AN_ENTITY_POOL = "SBO_0000592"

    # petri net place
    SBO_0000593 = "SBO_0000593"
    PETRI_NET_PLACE = "SBO_0000593"

    # neutral participant
    SBO_0000594 = "SBO_0000594"
    NEUTRAL_PARTICIPANT = "SBO_0000594"

    # dual-activity modifier
    SBO_0000595 = "SBO_0000595"
    DUAL_ACTIVITY_MODIFIER = "SBO_0000595"

    # modifier of unknown activity
    SBO_0000596 = "SBO_0000596"
    MODIFIER_OF_UNKNOWN_ACTIVITY = "SBO_0000596"

    # silencer
    SBO_0000597 = "SBO_0000597"
    SILENCER = "SBO_0000597"

    # promoter
    SBO_0000598 = "SBO_0000598"

    # port
    SBO_0000599 = "SBO_0000599"
    PORT = "SBO_0000599"

    # input port
    SBO_0000600 = "SBO_0000600"
    INPUT_PORT = "SBO_0000600"

    # output port
    SBO_0000601 = "SBO_0000601"
    OUTPUT_PORT = "SBO_0000601"

    # logical parameter
    SBO_0000602 = "SBO_0000602"
    LOGICAL_PARAMETER = "SBO_0000602"

    # side product
    SBO_0000603 = "SBO_0000603"
    SIDE_PRODUCT = "SBO_0000603"

    # side substrate
    SBO_0000604 = "SBO_0000604"
    SIDE_SUBSTRATE = "SBO_0000604"

    # high affinity receptor
    SBO_0000605 = "SBO_0000605"
    HIGH_AFFINITY_RECEPTOR = "SBO_0000605"

    # low affinity receptor
    SBO_0000606 = "SBO_0000606"
    LOW_AFFINITY_RECEPTOR = "SBO_0000606"

    # dimer
    SBO_0000607 = "SBO_0000607"
    DIMER = "SBO_0000607"

    # homodimer
    SBO_0000608 = "SBO_0000608"
    HOMODIMER = "SBO_0000608"

    # heterodimer
    SBO_0000609 = "SBO_0000609"
    HETERODIMER = "SBO_0000609"

    # growth rate
    SBO_0000610 = "SBO_0000610"
    GROWTH_RATE = "SBO_0000610"

    # effective catalytic rate
    SBO_0000611 = "SBO_0000611"
    EFFECTIVE_CATALYTIC_RATE = "SBO_0000611"

    # rate of reaction
    SBO_0000612 = "SBO_0000612"
    RATE_OF_REACTION = "SBO_0000612"

    # reaction parameter
    SBO_0000613 = "SBO_0000613"
    REACTION_PARAMETER = "SBO_0000613"

    # rate of reaction (concentration)
    SBO_0000614 = "SBO_0000614"
    RATE_OF_REACTION__CONCENTRATION_ = "SBO_0000614"

    # rate of reaction (amount)
    SBO_0000615 = "SBO_0000615"
    RATE_OF_REACTION__AMOUNT_ = "SBO_0000615"

    # extent of reaction
    SBO_0000616 = "SBO_0000616"
    EXTENT_OF_REACTION = "SBO_0000616"

    # Gibbs free energy of reaction
    SBO_0000617 = "SBO_0000617"
    GIBBS_FREE_ENERGY_OF_REACTION = "SBO_0000617"

    # reaction affinity
    SBO_0000618 = "SBO_0000618"
    REACTION_AFFINITY = "SBO_0000618"

    # transformed Gibbs free energy change
    SBO_0000619 = "SBO_0000619"
    TRANSFORMED_GIBBS_FREE_ENERGY_CHANGE = "SBO_0000619"

    # transformed standard Gibbs free energy of reaction
    SBO_0000620 = "SBO_0000620"
    TRANSFORMED_STANDARD_GIBBS_FREE_ENERGY_OF_REACTION = "SBO_0000620"

    # transformed standard Gibbs free energy of formation
    SBO_0000621 = "SBO_0000621"
    TRANSFORMED_STANDARD_GIBBS_FREE_ENERGY_OF_FORMATION = "SBO_0000621"

    # transformed Gibbs free energy of reaction
    SBO_0000622 = "SBO_0000622"
    TRANSFORMED_GIBBS_FREE_ENERGY_OF_REACTION = "SBO_0000622"

    # ionic strength
    SBO_0000623 = "SBO_0000623"
    IONIC_STRENGTH = "SBO_0000623"

    # flux balance framework
    SBO_0000624 = "SBO_0000624"
    FLUX_BALANCE_FRAMEWORK = "SBO_0000624"

    # flux bound
    SBO_0000625 = "SBO_0000625"
    FLUX_BOUND = "SBO_0000625"

    # default flux bound
    SBO_0000626 = "SBO_0000626"
    DEFAULT_FLUX_BOUND = "SBO_0000626"

    # exchange reaction
    SBO_0000627 = "SBO_0000627"
    EXCHANGE_REACTION = "SBO_0000627"

    # demand reaction
    SBO_0000628 = "SBO_0000628"
    DEMAND_REACTION = "SBO_0000628"

    # biomass production
    SBO_0000629 = "SBO_0000629"
    BIOMASS_PRODUCTION = "SBO_0000629"

    # ATP maintenance
    SBO_0000630 = "SBO_0000630"
    ATP_MAINTENANCE = "SBO_0000630"

    # pseudoreaction
    SBO_0000631 = "SBO_0000631"
    PSEUDOREACTION = "SBO_0000631"

    # sink reaction
    SBO_0000632 = "SBO_0000632"
    SINK_REACTION = "SBO_0000632"

    # subsystem
    SBO_0000633 = "SBO_0000633"
    SUBSYSTEM = "SBO_0000633"

    # DNA segment
    SBO_0000634 = "SBO_0000634"
    DNA_SEGMENT = "SBO_0000634"

    # RNA segment
    SBO_0000635 = "SBO_0000635"
    RNA_SEGMENT = "SBO_0000635"

    # allosteric activator
    SBO_0000636 = "SBO_0000636"
    ALLOSTERIC_ACTIVATOR = "SBO_0000636"

    # non-allosteric activator
    SBO_0000637 = "SBO_0000637"
    NON_ALLOSTERIC_ACTIVATOR = "SBO_0000637"

    # irreversible inhibitor
    SBO_0000638 = "SBO_0000638"
    IRREVERSIBLE_INHIBITOR = "SBO_0000638"

    # allosteric inhibitor
    SBO_0000639 = "SBO_0000639"
    ALLOSTERIC_INHIBITOR = "SBO_0000639"

    # uncompetitive inhibitor
    SBO_0000640 = "SBO_0000640"
    UNCOMPETITIVE_INHIBITOR = "SBO_0000640"

    # pMg
    SBO_0000641 = "SBO_0000641"
    PMG = "SBO_0000641"

    # inhibited
    SBO_0000642 = "SBO_0000642"
    INHIBITED = "SBO_0000642"

    # stimulated
    SBO_0000643 = "SBO_0000643"
    STIMULATED = "SBO_0000643"

    # modified
    SBO_0000644 = "SBO_0000644"
    MODIFIED = "SBO_0000644"

    # template
    SBO_0000645 = "SBO_0000645"
    TEMPLATE = "SBO_0000645"

    # mass action rate law for reversible reactions, continuous schema
    SBO_0000646 = "SBO_0000646"
    MASS_ACTION_RATE_LAW_FOR_REVERSIBLE_REACTIONS__CONTINUOUS_SCHEMA = "SBO_0000646"

    # molecular mass
    SBO_0000647 = "SBO_0000647"
    MOLECULAR_MASS = "SBO_0000647"

    # protein molecular mass
    SBO_0000648 = "SBO_0000648"
    PROTEIN_MOLECULAR_MASS = "SBO_0000648"

    # biomass
    SBO_0000649 = "SBO_0000649"
    BIOMASS = "SBO_0000649"

    # reversible process
    SBO_0000650 = "SBO_0000650"
    REVERSIBLE_PROCESS = "SBO_0000650"

    # irreversible process
    SBO_0000651 = "SBO_0000651"
    IRREVERSIBLE_PROCESS = "SBO_0000651"

    # polymerization
    SBO_0000652 = "SBO_0000652"
    POLYMERIZATION = "SBO_0000652"

    # depolymerization
    SBO_0000653 = "SBO_0000653"
    DEPOLYMERIZATION = "SBO_0000653"

    # co-transport reaction
    SBO_0000654 = "SBO_0000654"
    CO_TRANSPORT_REACTION = "SBO_0000654"

    # transport reaction
    SBO_0000655 = "SBO_0000655"
    TRANSPORT_REACTION = "SBO_0000655"

    # activation
    SBO_0000656 = "SBO_0000656"
    ACTIVATION = "SBO_0000656"

    # active transport
    SBO_0000657 = "SBO_0000657"
    ACTIVE_TRANSPORT = "SBO_0000657"

    # passive transport
    SBO_0000658 = "SBO_0000658"
    PASSIVE_TRANSPORT = "SBO_0000658"

    # symporter-mediated transport
    SBO_0000659 = "SBO_0000659"
    SYMPORTER_MEDIATED_TRANSPORT = "SBO_0000659"

    # antiporter-mediated transport
    SBO_0000660 = "SBO_0000660"
    ANTIPORTER_MEDIATED_TRANSPORT = "SBO_0000660"

    # capacity
    SBO_0000661 = "SBO_0000661"
    CAPACITY = "SBO_0000661"

    # occupancy
    SBO_0000662 = "SBO_0000662"
    OCCUPANCY = "SBO_0000662"

    # fractional occupancy
    SBO_0000663 = "SBO_0000663"
    FRACTIONAL_OCCUPANCY = "SBO_0000663"

    # contained entity
    SBO_0000664 = "SBO_0000664"
    CONTAINED_ENTITY = "SBO_0000664"

    # inactivation
    SBO_0000665 = "SBO_0000665"
    INACTIVATION = "SBO_0000665"

    # chain length
    SBO_0000666 = "SBO_0000666"
    CHAIN_LENGTH = "SBO_0000666"

    # protein chain length
    SBO_0000667 = "SBO_0000667"
    PROTEIN_CHAIN_LENGTH = "SBO_0000667"

    # yield
    SBO_0000668 = "SBO_0000668"
    YIELD = "SBO_0000668"

    # biomass yield on substrate
    SBO_0000669 = "SBO_0000669"
    BIOMASS_YIELD_ON_SUBSTRATE = "SBO_0000669"

    # product yield on substrate
    SBO_0000670 = "SBO_0000670"
    PRODUCT_YIELD_ON_SUBSTRATE = "SBO_0000670"

    # non-enzymatic catalyst
    SBO_0000671 = "SBO_0000671"
    NON_ENZYMATIC_CATALYST = "SBO_0000671"

    # spontaneous reaction
    SBO_0000672 = "SBO_0000672"
    SPONTANEOUS_REACTION = "SBO_0000672"

    # forward effective catalytic rate
    SBO_0000673 = "SBO_0000673"
    FORWARD_EFFECTIVE_CATALYTIC_RATE = "SBO_0000673"

    # reverse effective catalytic rate
    SBO_0000674 = "SBO_0000674"
    REVERSE_EFFECTIVE_CATALYTIC_RATE = "SBO_0000674"

    # deterministic non-spatial continuous framework
    SBO_0000675 = "SBO_0000675"
    DETERMINISTIC_NON_SPATIAL_CONTINUOUS_FRAMEWORK = "SBO_0000675"

    # stochastic non-spatial continuous framework
    SBO_0000676 = "SBO_0000676"
    STOCHASTIC_NON_SPATIAL_CONTINUOUS_FRAMEWORK = "SBO_0000676"

    # population-based discrete spatial simulation
    SBO_0000677 = "SBO_0000677"
    POPULATION_BASED_DISCRETE_SPATIAL_SIMULATION = "SBO_0000677"

    # particle-based discrete spatial simulation
    SBO_0000678 = "SBO_0000678"
    PARTICLE_BASED_DISCRETE_SPATIAL_SIMULATION = "SBO_0000678"

    # population-based discrete non-spatial simulation
    SBO_0000679 = "SBO_0000679"
    POPULATION_BASED_DISCRETE_NON_SPATIAL_SIMULATION = "SBO_0000679"

    # particle-based discrete non-spatial simulation
    SBO_0000680 = "SBO_0000680"
    PARTICLE_BASED_DISCRETE_NON_SPATIAL_SIMULATION = "SBO_0000680"

    # hybrid framework
    SBO_0000681 = "SBO_0000681"
    HYBRID_FRAMEWORK = "SBO_0000681"

    # hybrid spatial framework
    SBO_0000682 = "SBO_0000682"
    HYBRID_SPATIAL_FRAMEWORK = "SBO_0000682"

    # hybrid non-spatial framework
    SBO_0000683 = "SBO_0000683"
    HYBRID_NON_SPATIAL_FRAMEWORK = "SBO_0000683"

    # hybrid flux balance-deterministic continuous non-spatial framework
    SBO_0000684 = "SBO_0000684"
    HYBRID_FLUX_BALANCE_DETERMINISTIC_CONTINUOUS_NON_SPATIAL_FRAMEWORK = "SBO_0000684"

    # hybrid flux balance-discrete non-spatial framework
    SBO_0000685 = "SBO_0000685"
    HYBRID_FLUX_BALANCE_DISCRETE_NON_SPATIAL_FRAMEWORK = "SBO_0000685"

    # hybrid flux balance-logical-deterministic continuous non-spatial framework
    SBO_0000686 = "SBO_0000686"
    HYBRID_FLUX_BALANCE_LOGICAL_DETERMINISTIC_CONTINUOUS_NON_SPATIAL_FRAMEWORK = (
        "SBO_0000686"
    )

    # hybrid flux balance-logical non-spatial framework
    SBO_0000687 = "SBO_0000687"
    HYBRID_FLUX_BALANCE_LOGICAL_NON_SPATIAL_FRAMEWORK = "SBO_0000687"

    # hybrid flux logical-discrete non-spatial framework
    SBO_0000688 = "SBO_0000688"
    HYBRID_FLUX_LOGICAL_DISCRETE_NON_SPATIAL_FRAMEWORK = "SBO_0000688"

    # hybrid continuous-discrete non-spatial framework
    SBO_0000689 = "SBO_0000689"
    HYBRID_CONTINUOUS_DISCRETE_NON_SPATIAL_FRAMEWORK = "SBO_0000689"

    # hybrid deterministic continuous-discrete non-spatial framework
    SBO_0000690 = "SBO_0000690"
    HYBRID_DETERMINISTIC_CONTINUOUS_DISCRETE_NON_SPATIAL_FRAMEWORK = "SBO_0000690"

    # hybrid stochastic continuous-discrete non-spatial framework
    SBO_0000691 = "SBO_0000691"
    HYBRID_STOCHASTIC_CONTINUOUS_DISCRETE_NON_SPATIAL_FRAMEWORK = "SBO_0000691"

    # resource balance framework
    SBO_0000692 = "SBO_0000692"
    RESOURCE_BALANCE_FRAMEWORK = "SBO_0000692"

    # constraint-based framework
    SBO_0000693 = "SBO_0000693"
    CONSTRAINT_BASED_FRAMEWORK = "SBO_0000693"

    # optimization framework
    SBO_0000694 = "SBO_0000694"
    OPTIMIZATION_FRAMEWORK = "SBO_0000694"

    # ligation
    SBO_0000695 = "SBO_0000695"
    LIGATION = "SBO_0000695"

    # part of
    part_of = "part_of"
    PART_OF = "part_of"


SBOType = str | SBO

#: information of every term, assigned to the enum below
_terms: dict[str, TermData] = {
    "SBO_0000000": (
        "systems biology representation",
        "Representation of an entity used in a systems biology knowledge reconstruction, such as a model, pathway, network.",
        (),
        False,
    ),
    "SBO_0000001": (
        "rate law",
        "mathematical description that relates quantities of reactants to the reaction velocity.",
        (),
        False,
    ),
    "SBO_0000002": (
        "quantitative systems description parameter",
        "A numerical value that defines certain characteristics of systems or system functions. It may be part of a calculation, but its value is not determined by the form of the equation itself, and may be arbitrarily assigned.",
        (),
        False,
    ),
    "SBO_0000003": (
        "participant role",
        "The function of a physical or conceptual entity, that is its role, in the execution of an event or process.",
        (),
        False,
    ),
    "SBO_0000004": (
        "modelling framework",
        "Set of assumptions that underlay a mathematical description.",
        (),
        False,
    ),
    "SBO_0000005": (
        "obsolete mathematical expression",
        "The description of a system in mathematical terms.",
        (),
        False,
    ),
    "SBO_0000006": (
        "obsolete parameter",
        "A numerical value that represents the amount of some entity, process or mathematical function of the system.",
        (),
        False,
    ),
    "SBO_0000007": (
        "obsolete participant type",
        "The 'kind' of entity involved in some process, action or reaction in the system. This may be enzyme, simple chemical, etc..",
        (),
        False,
    ),
    "SBO_0000008": (
        "obsolete modelling framework",
        "Basic assumptions that underlie a mathematical model.",
        (),
        False,
    ),
    "SBO_0000009": ("kinetic constant", "Synonym: reaction rate constant", (), False),
    "SBO_0000010": (
        "reactant",
        "Substance consumed by a chemical reaction. Reactants react with each other to form the products of a chemical reaction. In a chemical equation the Reactants are the elements or compounds on the left hand side of the reaction equation. A reactant can be consumed and produced by the same reaction, its global quantity remaining unchanged.",
        (),
        False,
    ),
    "SBO_0000011": (
        "product",
        "Substance that is produced in a reaction. In a chemical equation the Products are the elements or compounds on the right hand side of the reaction equation. A product can be produced and consumed by the same reaction, its global quantity remaining unchanged.",
        (),
        False,
    ),
    "SBO_0000012": (
        "mass action rate law",
        "The Law of Mass Action, first expressed by Waage and Guldberg in 1864 (Waage, P.; Guldberg, C. M. Forhandlinger: Videnskabs-Selskabet i Christiana 1864, 35) states that the speed of a chemical reaction is proportional to the quantity of the reacting substances. More formally, the change of a product quantity is proportional to the product of reactant activities. In the case of a reaction occurring in a gas phase, the activities are equal to the partial pressures. In the case of a well-stirred aqueous medium, the activities are equal to the concentrations. In the case of discrete kinetic description, the quantity are expressed in number of molecules and the relevant volume are implicitely embedded in the kinetic constant.",
        (),
        False,
    ),
    "SBO_0000013": (
        "catalyst",
        "Substance that accelerates the velocity of a chemical reaction without itself being consumed or transformed. This effect is achieved by lowering the free energy of the transition state.",
        (),
        False,
    ),
    "SBO_0000014": (
        "enzyme",
        'A protein that catalyzes a chemical reaction. The word comes from en ("at" or "in") and simo ("leaven" or "yeast").',
        (),
        False,
    ),
    "SBO_0000015": (
        "substrate",
        "Molecule which is acted upon by an enzyme. The substrate binds with the enzyme's active site, and the enzyme catalyzes a chemical reaction involving the substrate.",
        (),
        False,
    ),
    "SBO_0000016": (
        "unimolecular rate constant",
        "Numerical parameter that quantifies the velocity of a chemical reaction involving only one reactant.",
        (),
        False,
    ),
    "SBO_0000017": (
        "bimolecular rate constant",
        "Numerical parameter that quantifies the velocity of a chemical reaction involving two reactants.",
        (),
        False,
    ),
    "SBO_0000018": (
        "trimolecular rate constant",
        "Numerical parameter that quantifies the velocity of a chemical reaction involving three reactants.",
        (),
        False,
    ),
    "SBO_0000019": (
        "modifier",
        "Substance that changes the velocity of a process without itself being consumed or transformed by the reaction.",
        (),
        False,
    ),
    "SBO_0000020": (
        "inhibitor",
        "Substance that decreases the probability of a chemical reaction without itself being consumed or transformed by the reaction.",
        (),
        False,
    ),
    "SBO_0000021": ("potentiator", "Synonym: activator", (), False),
    "SBO_0000022": (
        "forward unimolecular rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving only one reactant. This parameter encompasses all the contributions to the velocity except the quantity of the reactant.",
        (),
        False,
    ),
    "SBO_0000023": (
        "forward bimolecular rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving two reactants. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.",
        (),
        False,
    ),
    "SBO_0000024": (
        "forward trimolecular rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving three reactants. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.",
        (),
        False,
    ),
    "SBO_0000025": ("catalytic rate constant", "Synonym: turnover number", (), False),
    "SBO_0000026": ("new term name", "none", (), False),
    "SBO_0000027": (
        "Michaelis constant",
        "Synonym: Michaelis-Menten constant",
        (),
        False,
    ),
    "SBO_0000028": (
        "enzymatic rate law for irreversible non-modulated non-interacting unireactant enzymes",
        "Kinetics of enzymes that react only with one substance, their substrate. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000029": (
        "Henri-Michaelis-Menten rate law",
        'First general rate equation for reactions involving enzymes, it was presented in "Victor Henri. Lois Générales de l\'Action des Diastases. Paris, Hermann, 1903.". The reaction is assumed to be made of a reversible of the binding of the substrate to the enzyme, followed by the breakdown of the complex generating the product. Ten years after Henri, Michaelis and Menten presented a variant of his equation, based on the hypothesis that the dissociation rate of the substrate was much larger than the rate of the product generation. Leonor Michaelis, Maud Menten (1913). Die Kinetik der Invertinwirkung, Biochem. Z. 49:333-369.',
        (),
        False,
    ),
    "SBO_0000030": (
        "Van Slyke-Cullen rate law",
        'Rate-law presented in "Donald D. Van Slyke and Glenn E. Cullen. The mode of action of urease and of enzymes in general. J. Biol. Chem., Oct 1914; 19: 141-180". It assumes that the enzymatic reaction occurs as two irreversible steps.E+S -> ES -> E+P. Although of the same form than the Henri-Michaelis-Menten equation, it is semantically different since K now represents the ratio between the production rate and the association rate of the enzyme and the substrate.',
        (),
        False,
    ),
    "SBO_0000031": (
        "Briggs-Haldane rate law",
        "The Briggs-Haldane rate law is a general rate equation that does not require the restriction of equilibrium of Henri-Michaelis-Menten or irreversible reactions of Van Slyke, but instead make the hypothesis that the complex enzyme-substrate is in quasi-steady-state. Although of the same form than the Henri-Michaelis-Menten equation, it is semantically different since Km now represents a pseudo-equilibrium constant, and is equal to the ratio between the rate of consumption of the complex (sum of dissociation of substrate and generation of product) and the association rate of the enzyme and the substrate.",
        (),
        False,
    ),
    "SBO_0000032": (
        "reverse unimolecular rate constant",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction involving only one product. This parameter encompasses all the contributions to the velocity except the quantity of the product.",
        (),
        False,
    ),
    "SBO_0000033": (
        "reverse bimolecular rate constant",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction involving only one product. This parameter encompasses all the contributions to the velocity except the quantity of the product.",
        (),
        False,
    ),
    "SBO_0000034": (
        "reverse trimolecular rate constant",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction involving three products. This parameter encompasses all the contributions to the velocity except the quantity of the products.",
        (),
        False,
    ),
    "SBO_0000035": (
        "forward unimolecular rate constant, continuous case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving only one reactant. This parameter encompasses all the contributions to the velocity except the quantity of the reactant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000036": (
        "forward bimolecular rate constant, continuous case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving two reactants. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000037": (
        "forward trimolecular rate constant, continuous case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving three reactants. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000038": (
        "reverse unimolecular rate constant, continuous case",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction involving only one product. This parameter encompasses all the contributions to the velocity except the quantity of the product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000039": (
        "reverse bimolecular rate constant, continuous case",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction involving only one product. This parameter encompasses all the contributions to the velocity except the quantity of the product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000040": (
        "reverse trimolecular rate constant, continuous case",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction involving three products. This parameter encompasses all the contributions to the velocity except the quantity of the products. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000041": (
        "mass action rate law for irreversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products.",
        (),
        False,
    ),
    "SBO_0000042": (
        "mass action rate law for reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products.",
        (),
        False,
    ),
    "SBO_0000043": (
        "mass action rate law for zeroth order irreversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is constant.",
        (),
        False,
    ),
    "SBO_0000044": (
        "mass action rate law for first order irreversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant.",
        (),
        False,
    ),
    "SBO_0000045": (
        "mass action rate law for second order irreversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to two reactant quantity.",
        (),
        False,
    ),
    "SBO_0000046": (
        "zeroth order rate constant",
        "Numerical parameter that quantifies the velocity of a chemical reaction independant of the reactant quantities. This parameter encompasses all the contributions to the velocity.",
        (),
        False,
    ),
    "SBO_0000047": (
        "mass action rate law for zeroth order irreversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000048": (
        "forward zeroth order rate constant, continuous case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction independant of the reactant quantities. This parameter encompasses all the contributions to the velocity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000049": (
        "mass action rate law for first order irreversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000050": (
        "mass action rate law for second order irreversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products, and the change of a product quantity is proportional to the square of one reactant quantity.",
        (),
        False,
    ),
    "SBO_0000051": ("new term name", None, (), False),
    "SBO_0000052": (
        "mass action rate law for second order irreversible reactions, one reactant, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the square of one reactant quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000053": (
        "mass action rate law for second order irreversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of two reactants.",
        (),
        False,
    ),
    "SBO_0000054": (
        "mass action rate law for second order irreversible reactions, two reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the product of two reactant quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000055": (
        "mass action rate law for third order irreversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to three reactant quantities.",
        (),
        False,
    ),
    "SBO_0000056": (
        "mass action rate law for third order irreversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the cube of one reactant quantity.",
        (),
        False,
    ),
    "SBO_0000057": (
        "mass action rate law for third order irreversible reactions, one reactant, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products, and the change of a product quantity is proportional to the cube of one reactant quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000058": (
        "mass action rate law for third order irreversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant and the square of the quantity of the other reactant.",
        (),
        False,
    ),
    "SBO_0000059": (
        "mass action rate law for third order irreversible reactions, two reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant and the square of the quantity of the other reactant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000060": (
        "mass action rate law for third order irreversible reactions, three reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of three reactants.",
        (),
        False,
    ),
    "SBO_0000061": (
        "mass action rate law for third order irreversible reactions, three reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products, and the change of a product quantity is proportional to the product of three reactant quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000062": (
        "continuous framework",
        "Modelling approach where the quantities of participants are considered continuous, and represented by real values. The associated simulation methods make use of differential equations.",
        (),
        False,
    ),
    "SBO_0000063": (
        "discrete framework",
        "Modelling approach where the quantities of participants are considered discrete, and represented by integer values. The associated simulation methods can be deterministic or stochastic.",
        (),
        False,
    ),
    "SBO_0000064": (
        "mathematical expression",
        "Formal representation of a calculus linking parameters and variables of a model.",
        (),
        False,
    ),
    "SBO_0000065": (
        "forward zeroth order rate constant, discrete case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction independant of the reactant quantities. This parameter encompasses all the contributions to the velocity. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000066": (
        "forward unimolecular rate constant, discrete case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving only one reactant. This parameter encompasses all the contributions to the velocity except the quantity of the reactant. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000067": (
        "forward bimolecular rate constant, discrete case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving two reactants. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000068": (
        "forward trimolecular rate constant, discrete case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction involving three reactants. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000069": (
        "mass action rate law for zeroth order reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant.",
        (),
        False,
    ),
    "SBO_0000070": (
        "mass action rate law for zeroth order forward, first order reverse, reversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000071": (
        "mass action rate law for zeroth order forward, second order reverse, reversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional totwo product quantities.",
        (),
        False,
    ),
    "SBO_0000072": (
        "mass action rate law for zeroth order forward, second order reverse, reversible reactions, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000073": (
        "mass action rate law for zeroth order forward, second order reverse, reversible reactions, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000074": (
        "mass action rate law for zeroth order forward, third order reverse, reversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to three product quantities.",
        (),
        False,
    ),
    "SBO_0000075": (
        "mass action rate law for zeroth order forward, third order reverse, reversible reactions, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000076": (
        "mass action rate law for zeroth order forward, third order reverse, reversible reactions, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000077": (
        "mass action rate law for zeroth order forward, third order reverse, reversible reactions, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is constant. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000078": (
        "mass action rate law for first order reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant.",
        (),
        False,
    ),
    "SBO_0000079": (
        "mass action rate law for first order forward, zeroth order reverse, reversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000080": (
        "mass action rate law for first order forward, first order reverse, reversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000081": (
        "mass action rate law for first order forward, second order reverse, reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to two product quantities.",
        (),
        False,
    ),
    "SBO_0000082": (
        "mass action rate law for first order forward, second order reverse, reversible reactions, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000083": (
        "mass action rate law for first order forward, second order reverse, reversible reactions, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000084": (
        "mass action rate law for first order forward, third order reverse, reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to three product quantities.",
        (),
        False,
    ),
    "SBO_0000085": (
        "mass action rate law for first order forward, third order reverse, reversible reactions, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000086": (
        "mass action rate law for first order forward, third order reverse, reversible reactions, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000087": (
        "mass action rate law for first order forward, third order reverse, reversible reactions, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000088": (
        "mass action rate law for second order reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to two reactant quantities.",
        (),
        False,
    ),
    "SBO_0000089": (
        "mass action rate law for second order forward, reversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity.",
        (),
        False,
    ),
    "SBO_0000090": (
        "mass action rate law for second order forward, zeroth order reverse, reversible reactions, one reactant, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000091": (
        "mass action rate law for second order forward, first order reverse, reversible reactions, one reactant, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000092": (
        "mass action rate law for second order forward, second order reverse, reversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the quantity of two products.",
        (),
        False,
    ),
    "SBO_0000093": (
        "mass action rate law for second order forward, second order reverse, reversible reactions, one reactant, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000094": (
        "mass action rate law for second order forward, second order reverse, reversible reactions, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000095": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the quantity of three products.",
        (),
        False,
    ),
    "SBO_0000096": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000097": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000098": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the square of one reactant quantity. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000099": (
        "mass action rate law for second order forward, reversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities.",
        (),
        False,
    ),
    "SBO_0000100": (
        "mass action rate law for second order forward, zeroth order reverse, reversible reactions, two reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000101": (
        "mass action rate law for second order forward, first order reverse, reversible reactions, two reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000102": (
        "mass action rate law for second order forward, second order reverse, reversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the quantity of two products.",
        (),
        False,
    ),
    "SBO_0000103": (
        "mass action rate law for second order forward, second order reverse, reversible reactions, two reactants, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000104": (
        "mass action rate law for second order forward, second order reverse, reversible reactions, two reactants, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000105": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the quantity of three products.",
        (),
        False,
    ),
    "SBO_0000106": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000107": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000108": (
        "mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of two reactant quantities. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000109": (
        "mass action rate law for third order reversible reactions",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of a reactant quantity.",
        (),
        False,
    ),
    "SBO_0000110": (
        "mass action rate law for third order forward, reversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant.",
        (),
        False,
    ),
    "SBO_0000111": (
        "mass action rate law for third order forward, zeroth order reverse, reversible reactions, two reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000112": (
        "mass action rate law for third order forward, first order reverse, reversible reactions, two reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000113": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the quantity of two products.",
        (),
        False,
    ),
    "SBO_0000114": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, two reactants, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000115": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, two reactants, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000116": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, two reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the quantity of three products.",
        (),
        False,
    ),
    "SBO_0000117": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000118": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000119": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the quantity of one reactant and the square of quantity of the other reactant. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000120": (
        "mass action rate law for third order forward, reversible reactions, three reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities.",
        (),
        False,
    ),
    "SBO_0000121": (
        "mass action rate law for third order forward, zeroth order reverse, reversible reactions, three reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000122": (
        "mass action rate law for third order forward, first order reverse, reversible reactions, three reactants, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000123": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, three reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the quantity of two products.",
        (),
        False,
    ),
    "SBO_0000124": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, three reactants, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000125": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, three reactants, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000126": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, three reactants",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the quantity of three products.",
        (),
        False,
    ),
    "SBO_0000127": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000128": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000129": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the product of three reactant quantities. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000130": (
        "mass action rate law for third order forward, reversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity.",
        (),
        False,
    ),
    "SBO_0000131": (
        "mass action rate law for third order forward, zeroth order reverse, reversible reactions, one reactant, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is constant. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000132": (
        "mass action rate law for third order forward, first order reverse, reversible reactions, one reactant, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the quantity of one product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000133": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the quantity of two products.",
        (),
        False,
    ),
    "SBO_0000134": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, one reactant, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the square of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000135": (
        "mass action rate law for third order forward, second order reverse, reversible reactions, one reactant, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the product of two product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000136": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, one reactant",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the quantity of three products.",
        (),
        False,
    ),
    "SBO_0000137": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, one product, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the cube of one product quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000138": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, two products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the quantity of one product and the square of the quantity of the other product. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000139": (
        "mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, three products, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does include a reverse process that creates the reactants from the products. The rate of the forward process is proportional to the cube of one reactant quantity. The rate of the reverse process is proportional to the product of three product quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000140": (
        "mass action rate law for zeroth order irreversible reactions, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is constant. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000141": (
        "mass action rate law for first order irreversible reactions, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000142": (
        "mass action rate law for second order irreversible reactions, one reactant, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the square of one reactant quantity. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000143": (
        "mass action rate law for second order irreversible reactions, two reactants, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of two reactants. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000144": (
        "mass action rate law for third order irreversible reactions, one reactant, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the cube of one reactant quantity. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000145": (
        "mass action rate law for third order irreversible reactions, two reactants, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant and the square of the quantity of the other reactant. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000146": (
        "mass action rate law for third order irreversible reactions, three reactants, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of three reactants. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000147": (
        "thermodynamic temperature",
        'Temperature is the physical property of a system which underlies the common notions of "hot" and "cold"; the material with the higher temperature is said to be hotter. Temperature is a quantity related to the average kinetic energy of the particles in a substance. The 10th Conference Generale des Poids et Mesures decided to define the thermodynamic temperature scale by choosing the triple point of water as the fundamental fixed point, and assigning to it the temperature 273,16 degrees Kelvin, exactly (0.01 degree Celsius).',
        (),
        False,
    ),
    "SBO_0000148": (
        "temperature difference",
        "Quantity resulting from the difference between two thermodynamic temperatures. A difference or interval of temperature may be expressed in Kelvins or in degrees Celsius.",
        (),
        False,
    ),
    "SBO_0000149": (
        "number of substrates",
        "Number of molecules which are acted upon by an enzyme.",
        (),
        False,
    ),
    "SBO_0000150": (
        "enzymatic rate law for irreversible non-modulated non-interacting reactant enzymes",
        "Kinetics of enzymes that react with one or several substances, their substrates, that bind independently. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000151": (
        "enzymatic rate law for irreversible non-modulated non-interacting bireactant enzymes",
        "Kinetics of enzymes that react with two substances, their substrates, that bind independently. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000152": (
        "enzymatic rate law for irreversible non-modulated non-interacting trireactant enzymes",
        "Kinetics of enzymes that react with three substances, their substrates, that bind independently. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000153": (
        "forward rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.",
        (),
        False,
    ),
    "SBO_0000154": (
        "forward rate constant, continuous case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000155": (
        "forward rate constant, discrete case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000156": (
        "reverse rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.",
        (),
        False,
    ),
    "SBO_0000157": (
        "number of reactants",
        "Number of different substances consumed by a chemical reaction.",
        (),
        False,
    ),
    "SBO_0000158": (
        "order of a reaction with respect to a reactant",
        "The order of a reaction with respect to a certain reactant is defined as the power to which its concentration term in the rate equation is raised.",
        (),
        False,
    ),
    "SBO_0000159": (
        "non-integral order rate constant",
        "Numerical parameter that quantifies the velocity of a chemical reaction where reactants have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.",
        (),
        False,
    ),
    "SBO_0000160": (
        "forward non-integral order rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction where reactants have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.",
        (),
        False,
    ),
    "SBO_0000161": (
        "reverse non-integral order rate constant",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction where products have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the products.",
        (),
        False,
    ),
    "SBO_0000162": (
        "forward zeroth order rate constant",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction independant of the reactant quantities. This parameter encompasses all the contributions to the velocity.",
        (),
        False,
    ),
    "SBO_0000163": (
        "mass action rate law for irreversible reactions, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000164": (
        "second order irreversible mass action kinetics, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to two reactant quantity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000165": (
        "third order irreversible mass action kinetics, continuous scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to three reactant quantities. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000166": (
        "mass action rate law for irreversible reactions, discrete scheme",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000167": (
        "biochemical or transport reaction",
        "An event involving one or more physical entities that modifies the structure, location or free energy of at least one of the participants.",
        (),
        False,
    ),
    "SBO_0000168": ("control", "Synonym: regulation", (), False),
    "SBO_0000169": (
        "inhibition",
        "Negative modulation of the execution of a process.",
        (),
        False,
    ),
    "SBO_0000170": (
        "stimulation",
        "Positive modulation of the execution of a process.",
        (),
        False,
    ),
    "SBO_0000171": ("necessary stimulation", "Synonym: trigger", (), False),
    "SBO_0000172": (
        "catalysis",
        "Modification of the velocity of a reaction by lowering the energy of the transition state.",
        (),
        False,
    ),
    "SBO_0000173": (
        "and",
        "All the preceding events or participating entities are necessary to perform the control.",
        (),
        False,
    ),
    "SBO_0000174": (
        "or",
        "Any of the preceding events or participating entities are necessary to perform the control.",
        (),
        False,
    ),
    "SBO_0000175": ("xor", "Synonym: exclusive or", (), False),
    "SBO_0000176": (
        "biochemical reaction",
        "An event involving one or more chemical entities that modifies the electrochemical structure of at least one of the participants.",
        (),
        False,
    ),
    "SBO_0000177": ("non-covalent binding", "Synonym: association", (), False),
    "SBO_0000178": (
        "cleavage",
        "Rupture of a covalent bond resulting in the conversion of one physical entity into several physical entities or into a physical entity of a different topological class.",
        (),
        False,
    ),
    "SBO_0000179": (
        "degradation",
        "Complete disappearance of a physical entity.",
        (),
        False,
    ),
    "SBO_0000180": (
        "dissociation",
        "Transformation of a non-covalent complex that results in the formation of several independent biochemical entities",
        (),
        False,
    ),
    "SBO_0000181": (
        "conformational transition",
        "Biochemical reaction that does not result in the modification of covalent bonds of reactants, but rather modifies the conformation of some reactants, that is the relative position of their atoms in space.",
        (),
        False,
    ),
    "SBO_0000182": (
        "conversion",
        "Biochemical reaction that results in the modification of some covalent bonds.",
        (),
        False,
    ),
    "SBO_0000183": (
        "transcription",
        "Process through which a DNA sequence is copied to produce a complementary RNA.",
        (),
        False,
    ),
    "SBO_0000184": (
        "translation",
        "Process in which a polypeptide chain is produced from a messenger RNA.",
        (),
        False,
    ),
    "SBO_0000185": (
        "translocation reaction",
        "Movement of a physical entity without modification of the structure of the entity.",
        (),
        False,
    ),
    "SBO_0000186": ("maximal velocity", "Synonym: Vmax", (), False),
    "SBO_0000187": (
        "Henri-Michaelis-Menten equation, Vmax form",
        "Version of Henri-Michaelis-Menten equation where kp*[E]t is replaced by the maximal velocity, Vmax, reached when all the enzyme is active.",
        (),
        False,
    ),
    "SBO_0000188": (
        "number of biochemical items",
        "A number of objects of the same type, identical or different, involved in a biochemical event.",
        (),
        False,
    ),
    "SBO_0000189": (
        "number of binding sites",
        "Number of regions on a reactant to which specific other reactants, in this context collectively called ligands, form a chemical bond.",
        (),
        False,
    ),
    "SBO_0000190": (
        "Hill coefficient",
        "Empirical parameter created by Archibald Vivian Hill to describe the cooperative binding of oxygen on hemoglobine (Hill (1910). The possible effects of the aggregation of the molecules of haemoglobin on its dissociation curves. J Physiol 40: iv-vii).",
        (),
        False,
    ),
    "SBO_0000191": (
        "Hill constant",
        "Empirical constant created by Archibald Vivian Hill to describe the cooperative binding of oxygen on hemoglobine (Hill (1910). The possible effects of the aggregation of the molecules of haemoglobin on its dissociation curves. J Physiol 40: iv-vii). Different from a microscopic dissociation constant, it has the dimension of concentration to the power of the Hill coefficient.",
        (),
        False,
    ),
    "SBO_0000192": (
        "Hill-type rate law, generalised form",
        "Empirical equation created by Archibald Vivian Hill to describe the cooperative binding of oxygen on hemoglobine (Hill (1910). The possible effects of the aggregation of the molecules of haemoglobin on its dissociation curves. J Physiol 40: iv-vii).",
        (),
        False,
    ),
    "SBO_0000193": (
        "equilibrium or steady-state constant",
        "Constant with the dimension of a powered concentration. It is determined at half-saturation, half-activity etc.",
        (),
        False,
    ),
    "SBO_0000194": (
        "pseudo-dissociation constant",
        "Dissociation constant equivalent to an intrinsic microscopic dissociation constant, but obtained from an averaging process, for instance by extracting the root of a Hill constant.",
        (),
        False,
    ),
    "SBO_0000195": (
        "Hill-type rate law, microscopic form",
        "Hill equation rewritten by creating a pseudo-microscopic constant, equal to the Hill constant powered to the opposite of the Hill coefficient.",
        (),
        False,
    ),
    "SBO_0000196": ("concentration of an entity pool", "Synonym: [X]", (), False),
    "SBO_0000197": (
        "specific concentration of an entity",
        "Concentration of an object divided by the value of another parameter having the dimension of a concentration.",
        (),
        False,
    ),
    "SBO_0000198": (
        "Hill-type rate law, reduced form",
        "Hill equation rewritten by replacing the concentration of reactant with its reduced form, that is the concentration divide by a pseudo-microscopic constant, equal to the Hill constant powered to the opposite of the Hill coefficient.",
        (),
        False,
    ),
    "SBO_0000199": (
        "normalised enzymatic rate law for unireactant enzymes",
        "Kinetics of enzymes that react only with one substance, their substrate. The total enzyme concentration is considered to be equal to 1, therefore the maximal velocity equals the catalytic constant.",
        (),
        False,
    ),
    "SBO_0000200": (
        "redox reaction",
        "Chemical process in which atoms have their oxidation number (oxidation state) changed.",
        (),
        False,
    ),
    "SBO_0000201": (
        "oxidation",
        "Chemical process during which a molecular entity loses electrons.",
        (),
        False,
    ),
    "SBO_0000202": (
        "reduction",
        "Chemical process in which a molecular entity gain electrons.",
        (),
        False,
    ),
    "SBO_0000203": (
        "duplication",
        "Reaction in which a reactant gives birth to two products identical to itself.",
        (),
        False,
    ),
    "SBO_0000204": (
        "DNA replication",
        "Process in which a DNA duplex is transformed into two identical DNA duplexes.",
        (),
        False,
    ),
    "SBO_0000205": (
        "composite biochemical process",
        "Process that involves the participation of chemical or biological entities and is composed of several elementary steps or reactions.",
        (),
        False,
    ),
    "SBO_0000206": (
        "competitive inhibitor",
        "Substance that decreases the probability of a chemical reaction, without itself being consumed or transformed by the reaction, by stericaly hindering the interaction between reactants.",
        (),
        False,
    ),
    "SBO_0000207": (
        "non-competitive inhibitor",
        "Substance that decreases the probability of a chemical reaction, without itself being consumed or transformed by the reaction, and without sterically hindering the interaction between reactants.",
        (),
        False,
    ),
    "SBO_0000208": (
        "acid-base reaction",
        "Chemical reaction where a proton is given by a compound, the acid, to another one, the base (Brønsted-Lowry definition). An alternative, more general, definition is a reaction where a compound, the base, gives a pair of electrons to another, the acid (Lewis definition).",
        (),
        False,
    ),
    "SBO_0000209": (
        "ionisation",
        "Ionization is the physical process of converting an atom or molecule into an ion by changing the difference between the number of protons and electrons.",
        (),
        False,
    ),
    "SBO_0000210": (
        "addition of a chemical group",
        "Covalent reaction that results in the addition of a chemical group on a molecule.",
        (),
        False,
    ),
    "SBO_0000211": (
        "removal of a chemical group",
        "Covalent reaction that results in the removal of a chemical group from a molecule.",
        (),
        False,
    ),
    "SBO_0000212": (
        "protonation",
        "Addition of a proton (H+) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000213": (
        "deprotonation",
        "Removal of a proton (hydrogen ion H+) from a chemical entity.",
        (),
        False,
    ),
    "SBO_0000214": (
        "methylation",
        "Addition of a methyl group (-CH3) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000215": (
        "acetylation",
        "Addition of an acetyl group (-COCH3) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000216": (
        "phosphorylation",
        "Addition of a phosphate group (-H2PO4) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000217": (
        "glycosylation",
        "Addition of a saccharide group to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000218": (
        "palmitoylation",
        "Addition of a palmitoyl group (CH3-[CH2]14-CO-) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000219": (
        "myristoylation",
        "Addition of a myristoyl (CH3-[CH2]12-CO-) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000220": ("sulfation", "Synonym: sulphation", (), False),
    "SBO_0000221": ("prenylation", "Synonym: isoprenylation", (), False),
    "SBO_0000222": (
        "farnesylation",
        "Addition of a farnesyl group (CH2-CH=C(CH3)-CH2-CH2-CH=C(CH3)-CH2-CH2-CH=C(CH3)2) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000223": (
        "geranylgeranylation",
        "Addition of a geranylgeranyl group (CH2-CH=C(CH3)-CH2-CH2-CH=C(CH3)-CH2-CH2-CH=C(CH3)-CH2-CH2-CH=C(CH3)2) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000224": (
        "ubiquitination",
        "Covalent linkage to the protein ubiquitin.",
        (),
        False,
    ),
    "SBO_0000225": ("delay", "Time during which some action is awaited.", (), False),
    "SBO_0000226": (
        "density of an entity pool",
        "A quantitative measure of an amount or property of an entity expressed in terms of another dimension, such as unit length, area or volume.",
        (),
        False,
    ),
    "SBO_0000227": (
        "mass density of an entity",
        "The mass of an entity expressed with reference to another dimension, such as unit length, area or volume.",
        (),
        False,
    ),
    "SBO_0000228": (
        "volume density of an entity",
        "Mass of an entity per unit volume.",
        (),
        False,
    ),
    "SBO_0000229": (
        "area density of an entity",
        "The mass of an entity per unit of surface area.",
        (),
        False,
    ),
    "SBO_0000230": (
        "linear density of an entity",
        "Mass of an entity per unit length.",
        (),
        False,
    ),
    "SBO_0000231": (
        "occurring entity representation",
        "Representation of an entity that manifests, unfolds or develops through time, such as a discrete event, or a mutual or reciprocal action or influence that happens between participating physical entities, and/or other occurring entities.",
        (),
        False,
    ),
    "SBO_0000232": (
        "obsolete event",
        "A phenomenon that takes place and which may be observable, or may be determined to have occurred as the result of an action or process.",
        (),
        False,
    ),
    "SBO_0000233": (
        "hydroxylation",
        "Addition of an hydroxyl group (-OH) to a chemical entity.",
        (),
        False,
    ),
    "SBO_0000234": (
        "logical framework",
        'Modelling approach, pioneered by Rene Thomas and Stuart Kaufman, where the evolution of a system is described by the transitions between discrete activity states of "genes" that control each other.',
        (),
        False,
    ),
    "SBO_0000235": (
        "participant",
        "Entity that affects or is affected by an event.",
        (),
        False,
    ),
    "SBO_0000236": (
        "physical entity representation",
        "Synonym: new synonym",
        (),
        False,
    ),
    "SBO_0000237": (
        "logical combination",
        "Combining the influence of several entities or events in a unique influence.",
        (),
        False,
    ),
    "SBO_0000238": (
        "not",
        "The preceding event or participating entity cannot participate to the control.",
        (),
        False,
    ),
    "SBO_0000239": (
        "allosteric control",
        "Regulation of the influence of a reaction participant by binding an effector to a binding site of the participant different of the site of the participant conveying the influence.",
        (),
        False,
    ),
    "SBO_0000240": (
        "material entity",
        "A real thing that is defined by its physico-chemical structure.",
        (),
        False,
    ),
    "SBO_0000241": (
        "functional entity",
        "A real thing, defined by its properties or the actions it performs, rather than it physico-chemical structure.",
        (),
        False,
    ),
    "SBO_0000242": (
        "channel",
        "A component that allows another component to pass through itself, possibly connecting different compartments.",
        (),
        False,
    ),
    "SBO_0000243": (
        "gene",
        "A locatable region of genomic sequence, corresponding to a unit of inheritance, which is associated with regulatory regions, transcribed regions and/or other functional sequence regions. Sequence Ontology SO:0000704",
        (),
        False,
    ),
    "SBO_0000244": (
        "receptor",
        "Participating entity that binds to a specific physical entity and initiates the response to that physical entity.The original concept of the receptor was introduced independently at the end of the 19th century by John Newport Langley (1852-1925) and Paul Ehrlich (1854-1915). Langley JN.On the reaction of cells and of nerve-endings to certain poisons, chiefly as regards the reaction of striated muscle to nicotine and to curari. J Physiol. 1905 Dec 30;33(4-5):374-413.",
        (),
        False,
    ),
    "SBO_0000245": (
        "macromolecule",
        "Molecular entity mainly built-up by the repetition of pseudo-identical units. CHEBI:33839",
        (),
        False,
    ),
    "SBO_0000246": (
        "information macromolecule",
        "Macromolecule whose sequence is encoded in the genome of living organisms.",
        (),
        False,
    ),
    "SBO_0000247": (
        "simple chemical",
        "Simple, non-repetitive chemical entity.",
        (),
        False,
    ),
    "SBO_0000248": (
        "chemical macromolecule",
        "Macromolecule whose sequence is not directly encoded in the genome.",
        (),
        False,
    ),
    "SBO_0000249": (
        "polysaccharide",
        "Macromolecule consisting of a large number of monosaccharide residues linked by glycosidic bonds. CHEBI:18154",
        (),
        False,
    ),
    "SBO_0000250": ("ribonucleic acid", "Synonym: RNA", (), False),
    "SBO_0000251": ("deoxyribonucleic acid", "Synonym: DNA", (), False),
    "SBO_0000252": (
        "polypeptide chain",
        "Naturally occurring macromolecule formed by the repetition of amino-acid residues linked by peptidic bonds. A polypeptide chain is synthesized by the ribosome. CHEBI:16541",
        (),
        False,
    ),
    "SBO_0000253": (
        "non-covalent complex",
        "Entity composed of several independant components that are not linked by covalent bonds.",
        (),
        False,
    ),
    "SBO_0000254": (
        "electrical resistance",
        "Measure of the degree to which an object opposes the passage of an electric current. The SI unit of electrical resistance is the ohm.",
        (),
        False,
    ),
    "SBO_0000255": (
        "physical characteristic",
        "Parameter characterising a physical system or the environment, and independent of life's influence.",
        (),
        False,
    ),
    "SBO_0000256": (
        "biochemical parameter",
        "Parameter that depends on the biochemical properties of a system.",
        (),
        False,
    ),
    "SBO_0000257": (
        "conductance",
        "Measure of how easily electricity flows along a certain path through an electrical element. The SI derived unit of conductance is the Siemens.",
        (),
        False,
    ),
    "SBO_0000258": (
        "capacitance",
        "Measure of the amount of electric charge stored (or separated) for a given electric potential. The unit of capacitance id the Farad.",
        (),
        False,
    ),
    "SBO_0000259": ("voltage", "Synonym: electrical potential difference", (), False),
    "SBO_0000260": (
        "enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by one inhibitor",
        "Synonym: simple intersecting linear competitive inhibition of unireactant enzymes",
        (),
        False,
    ),
    "SBO_0000261": ("inhibitory constant", "Synonym: Ki", (), False),
    "SBO_0000262": (
        "enzymatic rate law for simple uncompetitive inhibition of irreversible unireactant enzymes",
        "Synonym: simple linear uncompetitive inhibition",
        (),
        False,
    ),
    "SBO_0000263": (
        "relative equilibrium constant",
        "Ratio of an equilibrium constant in a given condition by the same equilibrium constant is not fullfilled.",
        (),
        False,
    ),
    "SBO_0000264": (
        "relative inhibition constant",
        "Ratio of the dissociation constant of an inhibitor from the complex enzyme-substrate on the dissociation constant of an inhibitor from the free enzyme.",
        (),
        False,
    ),
    "SBO_0000265": (
        "enzymatic rate law for simple mixed-type inhibition of irreversible unireactant enzymes",
        "Synonym: simple intersecting linear mixed-type competitive inhibition",
        (),
        False,
    ),
    "SBO_0000266": (
        "enzymatic rate law for simple irreversible non-competitive inhibition of unireactant enzymes",
        "Inhibition of a unireactant enzyme by one inhibitor that can bind to the complex enzyme-substrate and the free enzyme with the same equilibrium constant, and totally prevent the catalysis.",
        (),
        False,
    ),
    "SBO_0000267": (
        "enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by one inhibitor",
        "Synonym: multiple competitive inhibition by one inhibitor of unireactant enzymes",
        (),
        False,
    ),
    "SBO_0000268": (
        "enzymatic rate law",
        "Enzyme kinetics is the study of the rates of chemical reactions that are catalysed by enzymes, how this rate is controlled, and how drugs and poisons can inhibit its activity.",
        (),
        False,
    ),
    "SBO_0000269": (
        "enzymatic rate law for unireactant enzymes",
        "Kinetics of enzymes that catalyse the transformation of only one substrate.",
        (),
        False,
    ),
    "SBO_0000270": (
        "enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by exclusive inhibitors",
        "Inhibition of a unireactant enzyme by inhibitors that bind to the free enzyme on the same binding site than the substrate. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000271": (
        "enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by two exclusive inhibitors",
        "Inhibition of a unireactant enzyme by two inhibitors that bind to the free enzyme on the same binding site than the substrate. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000272": (
        "number of inhibitors",
        "Number of entities that inhibit a reaction.",
        (),
        False,
    ),
    "SBO_0000273": (
        "enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by non-exclusive non-cooperative inhibitors",
        "Inhibition of a unireactant enzyme by inhibitors that bind independently to the free enzyme and preclude the binding of the substrate. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000274": (
        "enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by two non-exclusive, non-cooperative inhibitors",
        "Inhibition of a unireactant enzyme by two inhibitors that can bind independently once to the free enzyme and preclude the binding of the substrate. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000275": (
        "enzymatic rate law for mixed-type inhibition of irreversible enzymes by mutually exclusive inhibitors",
        "Inhibition of a unireactant enzyme by inhibitors that can bind to the complex enzyme-substrate and the free enzyme, possibly with different equilibrium constants, and totally prevent the catalysis. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000276": (
        "enzymatic rate law for mixed-type inhibition of irreversible unireactant enzymes by two inhibitors",
        "Inhibition of unireactant enzymes by two inhibitors that can bind to the complex enzyme-substrate and the free enzyme, possibly with different equilibrium constant, and totally prevent the catalysis. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000277": (
        "enzymatic rate law for non-competitive inhibition of irreversible unireactant enzymes by two exclusively binding inhibitors",
        "Inhibition of unireactant enzymes by two inhibitors that can bind to the complex enzyme-substrate and the free enzyme with the same equilibrium constant and totally prevent the catalysis.",
        (),
        False,
    ),
    "SBO_0000278": ("messenger RNA", "Synonym: mRNA", (), False),
    "SBO_0000279": (
        "pressure",
        "Pressure (symbol: p) is the force per unit area applied on a surface in a direction perpendicular to that surface. The unit of pressure is the Pascal (Pa), that is equal to 1 Newton per square meter.",
        (),
        False,
    ),
    "SBO_0000280": (
        "ligand",
        "In biochemistry, a ligand is an effector, a physical entity that binds to a site on a receptor's surface by intermolecular forces.",
        (),
        False,
    ),
    "SBO_0000281": ("equilibrium constant", "Synonym: Keq", (), False),
    "SBO_0000282": ("dissociation constant", "Synonym: Kd", (), False),
    "SBO_0000283": ("acid dissociation constant", "Synonym: Ka", (), False),
    "SBO_0000284": (
        "transporter",
        "Participating entity that facilitates the movement of another physical entity from a defined subset of the physical environment (for instance a cellular compartment) to another.",
        (),
        False,
    ),
    "SBO_0000285": (
        "material entity of unspecified nature",
        "Material entity whose nature is unknown or irrelevant.",
        (),
        False,
    ),
    "SBO_0000286": (
        "multimer",
        "Non-covalent association of identical, or pseudo-identical, entities. By pseudo-identical entities, we mean biochemical elements that differ chemically, although remaining globally identical in structure and/or function. Examples are homologous subunits in an hetero-oligomeric receptor.",
        (),
        False,
    ),
    "SBO_0000287": (
        "EC50",
        "Concentration of an active compound at which 50% of its maximal effect is observed. The EC50 is not a pure characteristic of the compound but depends on the conditions or the measurement.",
        (),
        False,
    ),
    "SBO_0000288": (
        "IC50",
        "Also called half maximal inhibitory concentration, it represents the concentration of an inhibitor substance that is required to suppress 50% of an effect.",
        (),
        False,
    ),
    "SBO_0000289": (
        "functional compartment",
        "Logical or physical subset of the event space that contains pools, that is sets of participants considered identical when it comes to the event they are involved into. A compartment can have any number of dimensions, including 0, and be of any size including null.",
        (),
        False,
    ),
    "SBO_0000290": (
        "physical compartment",
        "Specific location of space, that can be bounded or not. A physical compartment can have 1, 2 or 3 dimensions.",
        (),
        False,
    ),
    "SBO_0000291": (
        "empty set",
        "Entity defined by the absence of any actual object. An empty set is often used to represent the source of a creation process or the result of a degradation process.",
        (),
        False,
    ),
    "SBO_0000292": (
        "spatial continuous framework",
        "Modelling approach where the quantities of participants are considered continuous, and represented by real values. The associated simulation methods make use of differential equations. The models take into account the distribution of the entities and describe the spatial fluxes.",
        (),
        False,
    ),
    "SBO_0000293": (
        "non-spatial continuous framework",
        "Modelling approach where the quantities of participants are considered continuous, and represented by real values. The associated simulation methods make use of differential equations. The models do not take into account the distribution of the entities and describe only the temporal fluxes.",
        (),
        False,
    ),
    "SBO_0000294": (
        "spatial discrete framework",
        "Modelling approach where the quantities of participants are considered discrete, and represented by integer values. The associated simulation methods can be deterministic or stochastic. The models take into account the distribution of the entities and describe the spatial fluxes.",
        (),
        False,
    ),
    "SBO_0000295": (
        "non-spatial discrete framework",
        "Modelling approach where the quantities of participants are considered discrete, and represented by integer values. The associated simulation methods can be deterministic or stochastic.The models do not take into account the distribution of the entities and describe only the temporal fluxes.",
        (),
        False,
    ),
    "SBO_0000296": (
        "macromolecular complex",
        "Non-covalent complex of one or more macromolecules and zero or more simple chemicals.",
        (),
        False,
    ),
    "SBO_0000297": (
        "protein complex",
        "Macromolecular complex containing one or more polypeptide chains possibly associated with simple chemicals. CHEBI:36080",
        (),
        False,
    ),
    "SBO_0000298": (
        "synthetic chemical compound",
        "Chemical entity that is engineered by a human-designed process ex-vivo rather than a produced by a living entity.",
        (),
        False,
    ),
    "SBO_0000299": (
        "metabolite",
        "Substance produced by metabolism or by a metabolic process.",
        (),
        False,
    ),
    "SBO_0000300": ("total concentration of enzyme", "Synonym: Et", (), False),
    "SBO_0000301": (
        "total catalytic efficiency",
        "Constant representing the actual efficiency of an enzyme at a given concentration, taking into account its microscopic catalytic activity and the rates of substrate binding and dissociation. NB. The symbol Vmax and the names maximum rate and maximum velocity are in widespread use although under normal circumstances there is no finite substrate concentration at which v = V and hence no maximum in the mathematical sense (Eur. J. Biochem. 128:281-291).",
        (),
        False,
    ),
    "SBO_0000302": (
        "catalytic efficiency",
        "Constant representing the actual efficiency of an enzyme, taking into account its microscopic catalytic activity and the rates of substrate binding and dissociation.",
        (),
        False,
    ),
    "SBO_0000303": ("biochemical potential", "Synonym: chemical potential", (), False),
    "SBO_0000304": ("pH", "Synonym: potential of hydrogen", (), False),
    "SBO_0000305": (
        "pOH",
        "Negative logarithm (base 10) of the activity of hydroxyde in a solution. In a diluted solution, this activity is equal to the concentration of ions HO-.",
        (),
        False,
    ),
    "SBO_0000306": ("pK", "Synonym: dissociation potential", (), False),
    "SBO_0000307": ("pKa", "Synonym: potential of acid", (), False),
    "SBO_0000308": (
        "equilibrium or steady-state characteristic",
        "Quantitative parameter that characterises a biochemical equilibrium.",
        (),
        False,
    ),
    "SBO_0000309": (
        "dissociation characteristic",
        "Quantitative parameter that characterises a dissociation.",
        (),
        False,
    ),
    "SBO_0000310": (
        "acid dissociation characteristic",
        "Quantitative parameter that characterises an acid-base reaction.",
        (),
        False,
    ),
    "SBO_0000311": ("heterogeneous nuclear RNA", "Synonym: Precursor mRNA", (), False),
    "SBO_0000312": (
        "mature messenger RNA",
        "Completely processed single strand of messenger ribonucleic acid (mRNA), synthesized from a DNA template in the nucleus of a cell by transcription and containing copies of only the exons of a gene.",
        (),
        False,
    ),
    "SBO_0000313": ("transfer RNA", "Synonym: tRNA", (), False),
    "SBO_0000314": ("ribosomal RNA", "Synonym: rRNA", (), False),
    "SBO_0000315": ("ribozyme", "Synonym: ribonucleic acid enzyme", (), False),
    "SBO_0000316": ("microRNA", "Synonym: miRNA", (), False),
    "SBO_0000317": ("small interfering RNA", "Synonym: siRNA", (), False),
    "SBO_0000318": ("small nuclear RNA", "Synonym: snRNA", (), False),
    "SBO_0000319": ("small nucleolar RNA", "Synonym: snoRNA", (), False),
    "SBO_0000320": ("product catalytic rate constant", "Synonym: kcatp", (), False),
    "SBO_0000321": (
        "substrate catalytic rate constant",
        "Synonym: reverse catalytic rate constant",
        (),
        False,
    ),
    "SBO_0000322": ("Michaelis constant for substrate", "Synonym: Kms", (), False),
    "SBO_0000323": ("Michaelis constant for product", "Synonym: Kmp", (), False),
    "SBO_0000324": ("forward maximal velocity", "Synonym: Vmaxf", (), False),
    "SBO_0000325": ("reverse maximal velocity", "Synonym: Vmaxr", (), False),
    "SBO_0000326": (
        "enzymatic rate law for non-modulated unireactant enzymes",
        "Kinetics of enzymes that react only with one substance, their substrate, and are not modulated by other compounds.",
        (),
        False,
    ),
    "SBO_0000327": (
        "non-macromolecular ion",
        "Chemical entity having a net electric charge.",
        (),
        False,
    ),
    "SBO_0000328": (
        "non-macromolecular radical",
        "chemical entity possessing an unpaired electron.",
        (),
        False,
    ),
    "SBO_0000329": ("transcription start site", "Synonym: TSS", (), False),
    "SBO_0000330": (
        "dephosphorylation",
        "Removal of a phosphate group (-H2PO4) from a chemical entity.",
        (),
        False,
    ),
    "SBO_0000331": (
        "half-life",
        "Time interval over which a quantified entity is reduced to half its original value.",
        (),
        False,
    ),
    "SBO_0000332": (
        "half-life of an exponential decay",
        "Time taken by a quantity decreasing according to a mono-exponential decay to be divided by two. Sometimes called t1/2.",
        (),
        False,
    ),
    "SBO_0000333": (
        "monoexponential decay rate law",
        "Monotonic decrease of a quantity proportionally to its value.",
        (),
        False,
    ),
    "SBO_0000334": (
        "non-coding RNA",
        "RNA molecule that is not translated into a protein. Sequence Ontology SO:0000655",
        (),
        False,
    ),
    "SBO_0000335": (
        "gene coding region",
        "Portion of DNA or RNA that is transcribed into another RNA, such as a messenger RNA or a non-coding RNA (for instance a transfert RNA or a ribosomal RNA).",
        (),
        False,
    ),
    "SBO_0000336": (
        "interactor",
        "Entity participating in a physical or functional interaction.",
        (),
        False,
    ),
    "SBO_0000337": ("association constant", "Synonym: Ka", (), False),
    "SBO_0000338": ("dissociation rate constant", "Synonym: kd", (), False),
    "SBO_0000339": (
        "bimolecular association rate constant",
        "Rate with which two components associate into a complex.",
        (),
        False,
    ),
    "SBO_0000340": (
        "trimolecular association rate constant",
        "Rate with which three components associate into a complex.",
        (),
        False,
    ),
    "SBO_0000341": (
        "association rate constant",
        "Rate with which components associate into a complex.",
        (),
        False,
    ),
    "SBO_0000342": (
        "molecular or genetic interaction",
        "Mutual or reciprocal action or influence between molecular entities.",
        (),
        False,
    ),
    "SBO_0000343": (
        "genetic interaction",
        "A phenomenon whereby an observed phenotype, qualitative or quantative, is not explainable by the simple additive effects of the individual gene pertubations alone. Genetic interaction between perturbed genes is usually expected to generate a 'defective' phenotype. The level of defectiveness is often used to sub-classify this phenomenon.",
        (),
        False,
    ),
    "SBO_0000344": (
        "molecular interaction",
        "Relationship between molecular entities, based on contacts, direct or indirect.",
        (),
        False,
    ),
    "SBO_0000345": (
        "time",
        "Fundmental quantity of the measuring system used to sequence events, to compare the durations of events and the intervals between them, and to quantify the motions or the transformation of entities. The SI base unit for time is the SI second. The second is the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium 133 atom.",
        (),
        False,
    ),
    "SBO_0000346": (
        "temporal measure",
        "Fundamental quantity of the measuring system used to sequence events, to compare the durations of events and the intervals between them, and to quantify the motions or the transformation of entities. The SI base unit for time is the SI second. The second is the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium 133 atom.",
        (),
        False,
    ),
    "SBO_0000347": (
        "duration",
        "Amount of time during which an event persists.",
        (),
        False,
    ),
    "SBO_0000348": ("exponential time constant", "Synonym: mean lifetime", (), False),
    "SBO_0000349": ("inactivation rate constant", "Synonym: kinact", (), False),
    "SBO_0000350": (
        "forward reaction velocity",
        "The speed of an enzymatic reaction at a defined concentration of substrate(s) and enzyme.",
        (),
        False,
    ),
    "SBO_0000352": (
        "reverse zeroth order rate constant",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction independant of the reactant quantities. This parameter encompasses all the contributions to the velocity. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000353": (
        "reverse reaction velocity",
        "The speed of an enzymatic reaction at a defined concentration of substrate(s) and enzyme.",
        (),
        False,
    ),
    "SBO_0000354": (
        "informational molecule segment",
        "Fragment of a macromolecule that carries genetic information.",
        (),
        False,
    ),
    "SBO_0000355": (
        "conservation law",
        "Mathematical expression stating that a quantity is conserved in a system, whatever happens within the boundaries of that system.",
        (),
        False,
    ),
    "SBO_0000356": (
        "decay constant",
        'Kinetic constant characterising a mono-exponential decay. It is the inverse of the mean lifetime of the continuant being decayed. Its unit is "per time".',
        (),
        False,
    ),
    "SBO_0000357": (
        "biological effect of a perturbation",
        "Biochemical networks can be affected by external influences. Those influences can be well-defined physical perturbations, such as a light pulse, or a change in temperature but also more complex of not well defined phenomena, for instance a biological process, an experimental setup, or a mutation.",
        (),
        False,
    ),
    "SBO_0000358": (
        "phenotype",
        "A biochemical network can generate phenotypes or affects biological processes. Such processes can take place at different levels and are independent of the biochemical network itself.",
        (),
        False,
    ),
    "SBO_0000359": (
        "mass conservation law",
        "A chemical moiety that exists under different forms but is not created nor destroyed in a biochemical system. In any given system such a conserved moiety is characterized by a finite number of particles that exist in the system and is invariant.",
        (),
        False,
    ),
    "SBO_0000360": (
        "quantity of an entity pool",
        "The enumeration of co-localised, identical biochemical entities of a specific state, which constitute a pool. The form of enumeration may be purely numerical, or may be given in relation to another dimension such as length or volume.",
        (),
        False,
    ),
    "SBO_0000361": (
        "amount of an entity pool",
        "A numerical measure of the quantity, or of some property, of the entities that constitute the entity pool.",
        (),
        False,
    ),
    "SBO_0000362": (
        "concentration conservation law",
        "If all forms of a moiety exist in a single compartment and the size of that compartment is fixed then the Mass Conservation is also a Concentration Conservation.",
        (),
        False,
    ),
    "SBO_0000363": ("activation constant", "Synonym: Kx", (), False),
    "SBO_0000364": (
        "multimer cardinality",
        "Number of monomers composing a multimeric entity.",
        (),
        False,
    ),
    "SBO_0000365": (
        "forward non-integral order rate constant, continuous case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction where reactants have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the reactants.It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000366": (
        "forward non-integral order rate constant, discrete case",
        "Numerical parameter that quantifies the forward velocity of a chemical reaction where reactants have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the reactants. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000367": (
        "reverse non-integral order rate constant, discrete case",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction where products have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the products. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000368": (
        "reverse non-integral order rate constant, continuous case",
        "Numerical parameter that quantifies the reverse velocity of a chemical reaction where products have non-integral orders. This parameter encompasses all the contributions to the velocity except the quantity of the products. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000369": (
        "gene regulatory region",
        "Region of a gene that is involved in the modulation of the expression of the gene.",
        (),
        False,
    ),
    "SBO_0000370": (
        "Michaelis constant in non-equilibrium situation",
        "Michaelis constant derived or experimentally measured under non-equilibrium conditions.",
        (),
        False,
    ),
    "SBO_0000371": (
        "Michaelis constant in quasi-steady state situation",
        "Michaelis constant derived using a steady-state assumption for enzyme-substrate and enzyme-product intermediates. For example see Briggs-Haldane equation (SBO:0000031).",
        (),
        False,
    ),
    "SBO_0000372": (
        "Michaelis constant in irreversible situation",
        "Michaelis constant derived assuming enzyme-substrate and enzyme-product intermediates are formed in consecutive irreversible reactions. The constant K is the ratio of the forward rate constants. For example see Van Slyke-Cullen equation (SBO:0000030).",
        (),
        False,
    ),
    "SBO_0000373": (
        "Michaelis constant in fast equilibrium situation",
        "Michaelis constant as determined in a reaction where the formation of the enzyme-substrate complex occurs at a much faster rate than subsequent steps, and so are assumed to be in a quasi-equilibrium situation. K is equivalent to an equilibrium constant. For example see Henri-Michaelis-Menten equation (SBO:0000029).",
        (),
        False,
    ),
    "SBO_0000374": (
        "relationship",
        "connectedness between entities and/or interactions representing their relatedness or influence.",
        (),
        False,
    ),
    "SBO_0000375": (
        "process",
        "A sequential series of actions, motions, or occurrences, such as chemical reactions, that affect one or more entities in a phenomenologically characteristic manner.",
        (),
        False,
    ),
    "SBO_0000376": (
        "hydrolysis",
        "Decomposition of a compound by reaction with water, where the hydroxyl and H groups are incorporated into different products",
        (),
        False,
    ),
    "SBO_0000377": (
        "isomerisation",
        "A reaction in which the principal reactant and principal product are isomers of each other",
        (),
        False,
    ),
    "SBO_0000378": (
        "enzymatic rate law for inhibition of irreversible unireactant enzymes by competing substrates",
        "Inhibition of a unireactant enzyme by competing substrates (Sa) that bind to the free enzyme on the same binding site. The enzyme does not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000379": (
        "enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by two non-exclusive inhibitors",
        "Inhibition of a unireactant enzyme by two inhibitors that can bind once to the free enzyme and preclude the binding of the substrate. Binding of one inhibitor may affect binding of the other, or not. The enzymes do not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000380": (
        "biochemical coefficient",
        "number used as a multiplicative or exponential factor for quantities, expressions or functions",
        (),
        False,
    ),
    "SBO_0000381": (
        "biochemical proportionality coefficient",
        "A multiplicative factor for quantities, expressions or functions",
        (),
        False,
    ),
    "SBO_0000382": (
        "biochemical exponential coefficient",
        "number used as an exponential factor for quantities, expressions or functions",
        (),
        False,
    ),
    "SBO_0000383": (
        "biochemical cooperative inhibition coefficient",
        "The coefficient used to quantify the effect on inhibition constants of multiple inhibitors binding non-exclusively to the enzyme.",
        (),
        False,
    ),
    "SBO_0000384": (
        "biochemical inhibitory proportionality coefficient",
        "Coefficient that quantifies the effect on inhibition constants of either binding of multiple substrates or inhibitors.",
        (),
        False,
    ),
    "SBO_0000385": (
        "biochemical cooperative inhibitor substrate coefficient",
        "The coefficient that describes the proportional change of Ks or Ki when inhibitor or substrate is bound, respectively, to the enzyme.",
        (),
        False,
    ),
    "SBO_0000386": (
        "enzymatic rate law for inhibition of irreversible unireactant enzymes by single competing substrate",
        "Inhibition of a unireactant enzyme by a competing substrate (Sa) that binds to the free enzyme on the same binding site. The enzyme does not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000387": (
        "enzymatic rate law for competitive inhibition of irreversible unireactant enzyme by product",
        "Inhibition of a unireactant enzyme by a competing product (P) that binds to the free enzyme on the same binding site. The enzyme does not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000388": (
        "enzymatic rate law for inhibition of irreversible unireactant enzymes by single competing substrate with product inhibition",
        "Inhibition of a unireactant enzyme by a competing substrate (Sa) that binds to the free enzyme on the same binding site, and competitive inhibition by a product (P) and an alternative product (Pa). The enzyme does not catalyse the reactions in both directions.",
        (),
        False,
    ),
    "SBO_0000389": (
        "switch value",
        "A parameter value taken by a switch, which has a discrete set of values which can be alternated or switched between.",
        (),
        False,
    ),
    "SBO_0000390": ("boolean switch", "Synonym: binary switch", (), False),
    "SBO_0000391": (
        "steady state expression",
        "A mathematical expression that describes a steady state situation",
        (),
        False,
    ),
    "SBO_0000392": (
        "equivalence",
        "Term to signify those material or conceptual entities that are identical in some respect within a frame of reference",
        (),
        False,
    ),
    "SBO_0000393": (
        "production",
        "Generation of a material or conceptual entity.",
        (),
        False,
    ),
    "SBO_0000394": (
        "consumption",
        "Decrease in amount of a material or conceptual entity.",
        (),
        False,
    ),
    "SBO_0000395": (
        "encapsulating process",
        "An aggregation of interactions and entities into a single process.",
        (),
        False,
    ),
    "SBO_0000396": (
        "uncertain process",
        "An equivocal or conjectural process, whose existence is assumed but not proven.",
        (),
        False,
    ),
    "SBO_0000397": (
        "omitted process",
        "One or more processes that are not represented in certain representations or interpretations of a model.",
        (),
        False,
    ),
    "SBO_0000398": (
        "logical relationship",
        "Relationship between entities (material or conceptual) and logical operators, or between logical operators themselves.",
        (),
        False,
    ),
    "SBO_0000399": (
        "decarboxylation",
        "A process in which a carboxyl group (COOH) is removed from a molecule as carbon dioxide.",
        (),
        False,
    ),
    "SBO_0000400": (
        "decarbonylation",
        "Removal of a carbonyl group (-C-O-) from a molecule, usually as carbon monoxide",
        (),
        False,
    ),
    "SBO_0000401": (
        "deamination",
        "Removal of an amine group from a molecule, often under the addition of water",
        (),
        False,
    ),
    "SBO_0000402": (
        "transfer of a chemical group",
        "Covalent reaction that results in the transfer of a chemical group from one molecule to another.",
        (),
        False,
    ),
    "SBO_0000403": (
        "transamination",
        "The transfer of an amino group between two molecules. Commonly in biology this is restricted to reactions between an amino acid and an alpha-keto carbonic acid, whereby the reacting amino acid is converted into an alpha-keto acid, and the alpha-keto acid reactant into an amino acid.",
        (),
        False,
    ),
    "SBO_0000404": (
        "unit of genetic information",
        "Functional entity associated with or derived from a unit of inheritance.",
        (),
        False,
    ),
    "SBO_0000405": (
        "perturbing agent",
        "A material entity that is responsible for a perturbing effect",
        (),
        False,
    ),
    "SBO_0000406": (
        "observable",
        "An entity that can be measured quantitatively",
        (),
        False,
    ),
    "SBO_0000407": (
        "absolute inhibition",
        "Control that precludes the execution of a process.",
        (),
        False,
    ),
    "SBO_0000408": (
        "biological activity",
        "Effect of a biological entity on biological structures or processes.",
        (),
        False,
    ),
    "SBO_0000409": (
        "interaction outcome",
        "Entity that results from the interaction between other entities.",
        (),
        False,
    ),
    "SBO_0000410": (
        "implicit compartment",
        "A compartment whose existence is inferred due to the presence of known material entities which must be bounded, allowing the creation of material entity pools.",
        (),
        False,
    ),
    "SBO_0000411": (
        "absolute stimulation",
        "Control that always triggers the controlled process.",
        (),
        False,
    ),
    "SBO_0000412": (
        "biological activity",
        "The potential action that a biological entity has on other entities. Example are enzymatic activity, binding activity etc.",
        (),
        False,
    ),
    "SBO_0000413": (
        "positional relationship",
        "The connectedness between entities as related by their position",
        (),
        False,
    ),
    "SBO_0000414": (
        "cis",
        "Positional relationship between entities on the same strand (e.g. in DNA), or on the same side.",
        (),
        False,
    ),
    "SBO_0000415": (
        "trans",
        "Positional relationship between entities on different sides, or strands",
        (),
        False,
    ),
    "SBO_0000416": (
        "true",
        "One of the two values possible from a boolean switch, which equates to '1', 'on' or 'input'.",
        (),
        False,
    ),
    "SBO_0000417": (
        "false",
        "One of the two values possible from a boolean switch, which equates to '0', 'off' or 'no input'.",
        (),
        False,
    ),
    "SBO_0000418": (
        "multimer of complexes",
        "Non-covalent association between several independant complexes",
        (),
        False,
    ),
    "SBO_0000419": (
        "multimer of informational molecule segment",
        "Non-covalent association between portions of macromolecules that carry genetic information",
        (),
        False,
    ),
    "SBO_0000420": (
        "multimer of macromolecules",
        "Non-covalent association between several macromolecules",
        (),
        False,
    ),
    "SBO_0000421": (
        "multimer of simple chemicals",
        "Non-covalent association between several simple chemicals",
        (),
        False,
    ),
    "SBO_0000422": (
        "isoinhibition constant",
        "Inhibitory constant for the binding of a given ligand with an isomeric form of an enzyme.",
        (),
        False,
    ),
    "SBO_0000423": (
        "pseudo-dissociation constant for product",
        "In reversible reactions this is the concentration of product that is required to achieve half activation or inhibition in Hill-type kinetics, in the absence of the substrate.",
        (),
        False,
    ),
    "SBO_0000424": (
        "pseudo-dissociation constant for substrate",
        "In reversible reactions this is the concentration of substrate that is required to achieve half activation or inhibition in Hill-type kinetics, in the absence of the product.",
        (),
        False,
    ),
    "SBO_0000425": (
        "reversible Hill-type enzymatic rate law",
        "Reversible Hill-type kinetics represents the situation where a single substrate and product bind cooperatively and reversibly to the enzyme. Co-operativity is seen if the Hill coefficient (h) is greater than 1, indicating that the binding of one substrate (or product) molecule facilitates the binding of the next. The opposite effect is evident with a coefficient less than 1.",
        (),
        False,
    ),
    "SBO_0000426": (
        "modulated reversible Hill-type rate law",
        "Reversible Hill-type kinetics in the presence of at least one modifier whose binding is affected by the presence of the substrate or product.",
        (),
        False,
    ),
    "SBO_0000427": (
        "modulated reversible Hill-type rate law with one modifier",
        "The modifier can be either an activator or inhibitor depending on the value of alpha (activator for values larger than 1, inhibitor for values smaller than 1; no effect if exactly 1). This reflects the effect of the presence of substrate and product on the binding of the modifier. The equation, derived by Hofmeyr and Cornish-Bowden (Comput. Appl. Biosci. 13, 377 - 385 (1997)",
        (),
        False,
    ),
    "SBO_0000428": (
        "modulated reversible Hill-type rate law with two modifiers",
        "The modifiers can be either activators or inhibitors depending on the values of and alpha (activators for values larger than 1, inhibitors for values smaller than 1; no effect if exactly 1). The assumption is that the binding of one modifier affects the binding of the second. Modifiers are assumed to bind at different sites. The synergetic effects of the two modifiers depend on the parameter alpha (if unity then they are independent; if zero they compete for the same binding site). and reflect the effect of the presence of substrate and product on the binding of modifier A or modifier B. alphaA and alphaB factors account for the effect of substrate and product binding on the binding of modifier A and modifier B respectively. alphaAB accounts for the interaction of the modifiers on each others binding. (if < 1 Ma is inhibitor, if > 1 activator) alpha_2 : factor accounting for the effect of S and P on the binding of Mb (if < 1 Mb is inhibitor, if > 1 activator) alpha_3 : factor accounting for interaction of Ma to Mb binding to the enzyme (and v. v.).",
        (),
        False,
    ),
    "SBO_0000429": (
        "enzymatic rate law for multireactant enzymes",
        "Kinetics of enzyme-catalysed reactions with 2 or more substrates or products",
        (),
        False,
    ),
    "SBO_0000430": (
        "enzymatic rate law for modulated unireactant enzymes",
        "Kinetics of enzymes that react with one substance, and whose activity may be positively or negatively modulated.",
        (),
        False,
    ),
    "SBO_0000431": (
        "unmodulated reversible Hill-type rate law",
        "Reversible equivalent of Hill kinetics, where substrate and product bind co-operatively to the enzyme. A Hill coefficient (h) of greater than 1 indicates positive co-operativity between substrate and product, while h values below 1 indicate negative co-operativity.",
        (),
        False,
    ),
    "SBO_0000432": (
        "irreversible Michaelis Menten rate law for two substrates",
        "Enzymatic rate law for an irreversible reaction involving two substrates and one product.",
        (),
        False,
    ),
    "SBO_0000433": (
        "Ordered Bi-Bi mechanism rate law",
        "Enzymatic rate law for a reaction involving two substrates and two products. The products P and then Q are released strictly in order, while the substrates are bound strictly in the order A and then B.",
        (),
        False,
    ),
    "SBO_0000434": (
        "Ordered Bi-Uni mechanism rate law",
        "Enzymatic rate for a reaction involving two substrates and one product. The substrates A and then B are bound strictly in order.",
        (),
        False,
    ),
    "SBO_0000435": (
        "Ordered Uni-Bi mechanism rate law",
        "Enzymatic rate law for a reaction with one substrate and two products. The products P and then Q are released in the strict order P and then Q.",
        (),
        False,
    ),
    "SBO_0000436": (
        "Ping Pong Bi-Bi mechanism rate law",
        "Enzymatic rate law for a reaction involving two substrates and two products. The first product (P) is released after the first substrate (A) has been bound. The second product (Q) is released after the second substrate (B) has been bound.",
        (),
        False,
    ),
    "SBO_0000437": (
        "reversible Iso Uni-Uni",
        "Enzyme catalysed reaction involving one substrate and one product. Unlike the reversible uni-uni mechanism (SBO:0000326), the mechanism assumes an enzyme intermediate. Therefore, the free enzyme generated after the release of product from enzyme-product complex is not the same form as that which bind the substrate to form enzyme-substrate complex. Some permeases are thought to follow this mechanism, such that isomerization in the membrane may be accomplished through re-orientation in the membrane.",
        (),
        False,
    ),
    "SBO_0000438": (
        "reversible Uni-Uni",
        "Synonym: Uni-Uni Reversible Simple Michaelis-Menten",
        (),
        False,
    ),
    "SBO_0000439": (
        "Uni-Uni Reversible using Haldane relationship",
        "Synonym: Uni-Uni",
        (),
        False,
    ),
    "SBO_0000440": (
        "enzymatic rate law for irreversible allosteric inhibition",
        "Enzymatic rate law which follows from the allosteric concerted model (symmetry model or MWC model).This states that enzyme subunits can assume one of two conformational states (relaxed or tense), and that the state of one subunit is shared or enforced on the others. The binding of a ligand to a site other than that bound by the substrate (active site) can shift the conformation from one state to the other. L represents the equilibrium constant between active and inactive states of the enzyme, and n represents the number of binding sites for the substrate and inhibitor.",
        (),
        False,
    ),
    "SBO_0000441": (
        "enzymatic rate law for mixed-type inhibition of reversible enzymes by mutually exclusive inhibitors",
        "Reversible inhibition of a unireactant enzyme by inhibitors that can bind to the enzyme-substrate complex and to the free enzyme with the same equilibrium constant. The inhibitor is noncompetitive with the substrate.",
        (),
        False,
    ),
    "SBO_0000442": (
        "enzymatic rate law for simple reversible non-competitive inhibition of unireactant enzymes",
        "Reversible inhibition of a unireactant enzyme by one inhibitor that can bind to the enzyme-substrate complex and to the free enzyme with the same equilibrium constant. The inhibitor is noncompetitive with the substrate.",
        (),
        False,
    ),
    "SBO_0000443": (
        "enzymatic rate law for reversible essential activation",
        "Synonym: specific activation",
        (),
        False,
    ),
    "SBO_0000444": (
        "enzymatic rate law for reversible mixed activation",
        "Enzymatic rate law where the activator enhances the rate of reaction through specific and catalytic effects, which increase the apparent limiting rate and decrease apparent Michaelis constant. The activator can bind reversibly both the free enzyme and enzyme-substrate complex, while the substrate can bind only to enzyme-activator complex. Catalytic activity is seen only when enzyme, substrate and activator are complexed.",
        (),
        False,
    ),
    "SBO_0000445": (
        "enzymatic rate law for irreversible substrate activation",
        "This enzymatic rate law is available only for irreversible reactions, with one substrate and one product. There is a second binding site for the enzyme which, when occupied, activates the enzyme. Substrate binding at either site can occur at random.",
        (),
        False,
    ),
    "SBO_0000446": (
        "enzymatic rate law for irrreversible mixed activation",
        "Enzymatic rate law where the activator enhances the rate of reaction through specific and catalytic effects, which increase the apparent limiting rate and decrease apparent Michaelis constant. The activator can bind irreversibly both free enzyme and enzyme-substrate complex, while the substrate can bind only to enzyme-activator complex. Catalytic activity is seen only when enzyme, substrate and activator are complexed.",
        (),
        False,
    ),
    "SBO_0000447": (
        "enzymatic rate law for reversible catalytic activation with one activator",
        "Enzymatic rate law where an activator enhances the rate of reaction by increasing the apparent limiting rate; The reversible binding of the activator to the enzyme-substrate complex is required for enzyme catalytic activity (to generate the product).",
        (),
        False,
    ),
    "SBO_0000448": (
        "enzymatic rate law for reversible specific activation",
        "Enzymatic rate law for one substrate, one product and one modifier which acts as an activator. The activator enhances the rate of reaction by decreasing the apparent Michaelis constant. The activator reversibly binds to the enzyme before the enzyme can bind the substrate.",
        (),
        False,
    ),
    "SBO_0000449": (
        "enzymatic rate law for irreversible catalytic activation with one activator",
        "Enzymatic rate law where an activator enhances the rate of reaction by increasing the apparent limiting rate; The activator binding to the enzyme-substrate complex (irreversibly) is required for enzyme catalytic activity (to generate the product).",
        (),
        False,
    ),
    "SBO_0000450": (
        "enzymatic rate law for irreversible specific activation",
        "Enzymatic rate law for one substrate, one product and one modifier which acts as an activator. The activator enhances the rate of reaction by decreasing the apparent Michaelis constant. The activator must bind to the enzyme before the enzyme can bind the substrate.",
        (),
        False,
    ),
    "SBO_0000451": (
        "enzymatic rate law for reversible reactions with competitive inhibition",
        "This enzymatic rate law involves one substrate, one product and one or more modifiers. The modifiers act as competitive inhibitors of the substrate at the enzyme binding site; The modifiers (inhibitors) reversibly bound to the enzyme block access to the substrate. The inhibitors have the effect of increasing the apparent Km, and bind exclusively to the enzymes.",
        (),
        False,
    ),
    "SBO_0000452": (
        "enzymatic rate law for reversible competitive inhibition by one inhibitor",
        "This enzymatic rate law involves one substrate, one product and one modifier. The modifier acts as a competitive inhibitor with the substrate at the enzyme binding site; The modifier (inhibitor) reversibly bound to the enzyme blocks access to the substrate. The inhibitor has the effect of increasing the apparent Km.",
        (),
        False,
    ),
    "SBO_0000453": (
        "enzymatic rate law for reversible empirical allosteric inhibition by one inhibitor",
        "Enzymatic rate law where the reversible binding of one ligand decreases the affinity for substrate at other active sites. The ligand does not bind the same site as the substrate on the enzyme. This is an empirical equation, where n represents the Hill coefficient.",
        (),
        False,
    ),
    "SBO_0000454": (
        "enzymatic rate law for reversible substrate inhibition",
        "Enzymatic rate law where the substrate for an enzyme also acts as a reversible inhibitor. This may entail a second (non-active) binding site for the enzyme. The inhibition constant is then the dissociation constant for the substrate from this second site.",
        (),
        False,
    ),
    "SBO_0000455": (
        "enzymatic rate law for irreversible substrate inhibition",
        "Enzymatic rate law where the substrate for an enzyme also acts as an irreversible inhibitor. This may entail a second (non-active) binding site for the enzyme. The inhibition constant is then the dissociation constant for the substrate from this second site.",
        (),
        False,
    ),
    "SBO_0000456": (
        "enzymatic rate law for reversible unireactant enzyme with a single hyperbolic modulator",
        "Enzymatic rate law where the modifier can act as an activator or inhibitor, depending upon the values of the kinetic constants. The modifier can bind reversibly to all forms of the enzyme and all enzyme-substrate complexes are reactive. 'a' represents the ratio of dissociation constant of the elementary step Enzyme-Substrate complex + Modifier = Enzyme-Substrate-Modifier complex over that of Enzyme + Modifier = Enzyme-Modifier complex. 'b' represents ratio of the rate constant of elementary step Enzyme-Substrate-Modifier complex -> Enzyme-Modifier complex + Product over that of Enzyme-Substrate complex -> Enzyme + Product.",
        (),
        False,
    ),
    "SBO_0000457": (
        "enzymatic rate law for irreversible unireactant enzyme with a single hyperbolic modulator",
        "Enzymatic rate law where the modifier can act as an activator or inhibitor, depending upon the values of the kinetic constants. The modifier can bind irreversibly to all forms of the enzyme and all enzyme-substrate complexes are reactive. 'a' represents the ratio of dissociation constant of the elementary step Enzyme-Substrate complex + Modifier = Enzyme-Substrate-Modifier complex) over that of Enzyme + Modifier = Enzyme-Modifier complex. 'b' represents ratio of the rate constant of elementary step Enzyme-Substrate-Modifier complex -> Enzyme-Modifier complex + Product over that of Enzyme-Substrate complex -> Enzyme + Product.",
        (),
        False,
    ),
    "SBO_0000458": (
        "enzymatic rate law for simple uncompetitive inhibition of reversible unireactant enzymes",
        "Reversible inhibition of a unireactant enzyme by one inhibitor, which binds to the enzyme-substrate complex. The inhibitor is uncompetitive with the substrate.",
        (),
        False,
    ),
    "SBO_0000459": ("stimulator", "Synonym: activator", (), False),
    "SBO_0000460": (
        "enzymatic catalyst",
        "A substance that accelerates the velocity of a chemical reaction without itself being consumed or transformed, by lowering the free energy of the transition state. The substance acting as a catalyst is an enzyme.",
        (),
        False,
    ),
    "SBO_0000461": ("essential activator", "Synonym: necessary stimulator", (), False),
    "SBO_0000462": (
        "non-essential activator",
        "An activator which is not necessary for an enzymatic reaction, but whose presence will further increase enzymatic activity.",
        (),
        False,
    ),
    "SBO_0000463": (
        "standard biochemical potential",
        "Synonym: standard chemical potential",
        (),
        False,
    ),
    "SBO_0000464": (
        "state variable assignment",
        "Assignment of a state or a value to a state variable, characteristic or property, of a biological entity.",
        (),
        False,
    ),
    "SBO_0000465": (
        "spatial measure",
        "The measurable dimensions of an object which are minimally required to define the space that an object occupies.",
        (),
        False,
    ),
    "SBO_0000466": (
        "length",
        "The length of an object is the longest measurable distance between its extremities.",
        (),
        False,
    ),
    "SBO_0000467": (
        "area",
        "The area of an object is a quantity expressing its two-dimensional size, usually part or all of its surface.",
        (),
        False,
    ),
    "SBO_0000468": (
        "volume",
        "A quantity representing the three-dimensional space occupied by all or part of an object.",
        (),
        False,
    ),
    "SBO_0000469": ("containment", "Synonym: inclusion", (), False),
    "SBO_0000470": (
        "mass fraction",
        "For a given substance, A, its mass fraction (x A) is defined as the ratio of its mass (m A) to the total mass (m total) in which it is present, where the sum of all mass fractions is equal to 1. This provides a means to express concentration in a dimensionless size.",
        (),
        False,
    ),
    "SBO_0000471": (
        "molal concentration of an entity",
        'Molality denotes the number of moles of solute per kilogram of solvent (not solution). The term molal solution is used as a shorthand for a "one molal solution", i.e. a solution which contains one mole of the solute per kilogram of the solvent. The SI unit for molality is mol/kg.',
        (),
        False,
    ),
    "SBO_0000472": (
        "molar concentration of an entity",
        "Molarity, or molar concentration, denotes the number of moles of a given substance per litre of solution. The unit of measure of molarity is mol/L, molar, or the capital letter M as an abbreviated form.",
        (),
        False,
    ),
    "SBO_0000473": (
        "denotement",
        "Term to signify where a material or conceptual entity is represented or denoted by a symbol or by some other abbreviated form.",
        (),
        False,
    ),
    "SBO_0000474": (
        "convenience function",
        "Mathematical function commonly used in biological modeling, which enable simplification of more complex expressions",
        (),
        False,
    ),
    "SBO_0000475": (
        "periodic forcing function",
        "Synonym: input signal step function",
        (),
        False,
    ),
    "SBO_0000476": (
        "period",
        "The period is the duration of one cycle in a repeating event. [wikipedia]",
        (),
        False,
    ),
    "SBO_0000477": ("phase shift", "Synonym: temporal offset", (), False),
    "SBO_0000478": (
        "powered product of Michaelis constant",
        "The product of the Michaelis constants, to the power of their respective stoichiometric coefficients, for either substrates or products.",
        (),
        False,
    ),
    "SBO_0000479": (
        "powered product of substrate Michaelis constants",
        "The product of the substrate Michaelis constants, to the power of their respective stoichiometric coefficients.",
        (),
        False,
    ),
    "SBO_0000480": (
        "powered product of product Michaelis constants",
        "The product of the product Michaelis constants, to the power of their respective stoichiometric coefficients.",
        (),
        False,
    ),
    "SBO_0000481": (
        "stoichiometric coefficient",
        "The stoichiometric coefficient represents the degree to which a chemical species participates in a reaction. It corresponds to the number of molecules of a reactant that are consumed or produced with each occurrence of a reaction event.",
        (),
        False,
    ),
    "SBO_0000482": (
        "geometric mean rate constant",
        "The geometric mean turnover rate of an enzyme in either forward or backward direction for a reaction, measured per second.",
        (),
        False,
    ),
    "SBO_0000483": (
        "forward geometric mean rate constant",
        "The geometric mean turnover rate of an enzyme in the forward direction for a reaction, measured per second.",
        (),
        False,
    ),
    "SBO_0000484": (
        "reverse geometric mean rate constant",
        "The geometric mean turnover rate of an enzyme in the reverse direction for a reaction, measured per second.",
        (),
        False,
    ),
    "SBO_0000485": (
        "basal rate constant",
        "The minimal velocity observed under defined conditions, which may or may not include the presence of an effector. For example in an inhibitory system, this would be the residual velocity observed under full inhibition. In non-essential activation, this would be the velocity in the absence of any activator.",
        (),
        False,
    ),
    "SBO_0000486": (
        "relative basal rate constant",
        "The ratio of the basal activity to the maximal velocity of a reaction. The values range between 0 and 1.",
        (),
        False,
    ),
    "SBO_0000487": (
        "relative activity function",
        "Function which ranges from 0 to 1, to describe the relative activation or inhibition of a reaction or process, actual or conceptual.",
        (),
        False,
    ),
    "SBO_0000488": (
        "relative activation function",
        "Function which ranges from 0 to 1, to describe the relative activation of a reaction or process, actual or conceptual.",
        (),
        False,
    ),
    "SBO_0000489": (
        "relative inhibition function",
        "Function which ranges from 0 to 1, to describe the relative inhibition of a reaction or process, actual or conceptual.",
        (),
        False,
    ),
    "SBO_0000490": (
        "number of products",
        "Number of molecules which are generated by an enzyme.",
        (),
        False,
    ),
    "SBO_0000491": ("diffusion coefficient", "Synonym: diffusivity", (), False),
    "SBO_0000492": (
        "amplitude",
        "Amplitude is the magnitude of change in the oscillating variable, with each oscillation, within an oscillating system.",
        (),
        False,
    ),
    "SBO_0000493": (
        "functional domain",
        "A spatial region of an entity that confers a function",
        (),
        False,
    ),
    "SBO_0000494": (
        "binding site",
        "A specific domain of a spatio-temporal entity to which another spatio-temporal entity is able to bind, forming chemical bonds.",
        (),
        False,
    ),
    "SBO_0000495": (
        "catalytic site",
        "A catalytic site is the region which confers specificity of a substrate for the binding entity, and where specific reactions take place in the conversion of the substrate to the product.",
        (),
        False,
    ),
    "SBO_0000496": (
        "transmembrane domain",
        "A transmembrane domain is any three-dimensional protein structure which is thermodynamically stable in a membrane. This may be a single alpha helix, a stable complex of several transmembrane alpha helices, a transmembrane beta barrel, a beta-helix of gramicidin A, or any other structure.",
        (),
        False,
    ),
    "SBO_0000497": (
        "ternary switch",
        "A parameter that has three discrete values which may be alternated between.",
        (),
        False,
    ),
    "SBO_0000498": (
        "relative activity",
        "Value which ranges from 0 to 1, to describe the relative activity of a process or reaction.",
        (),
        False,
    ),
    "SBO_0000499": (
        "genetic interaction",
        "A phenomenon whereby an observed phenotype, qualitative or quantative, is not explainable by the simple additive effects of the individual gene pertubations alone. Genetic interaction between perturbed genes is usually expected to generate a 'defective' phenotype. The level of defectiveness is often used to sub-classify this phenomenon.",
        (),
        False,
    ),
    "SBO_0000500": (
        "genetic suppression",
        "Genetic suppression is said to have occurred when the phenotypic effect of an initial mutation in a gene is less severe, or entirely negated, by a subsequent mutation.",
        (),
        False,
    ),
    "SBO_0000501": (
        "genetic enhancement",
        "Genetic enhancement is said to have occurred when the phenotypic effect of an initial mutation in a gene is made increasingly severe by a subsequent mutation.",
        (),
        False,
    ),
    "SBO_0000502": (
        "synthetic lethality",
        "Synthetic lethality is said to have occurred where gene mutations, each of which map to a separate locus, fail to complement in an offspring to correct a phenotype, as would be expected.",
        (),
        False,
    ),
    "SBO_0000503": (
        "number of entity pool constituents",
        "The numerical quantification of an entity pool. This may be expressed as, for example, the number of molecules or the number of moles of identical entities of which an specific entity pool is comprised.",
        (),
        False,
    ),
    "SBO_0000504": (
        "mass of an entity pool",
        "The mass that comprises an entity pool.",
        (),
        False,
    ),
    "SBO_0000505": (
        "concentration of enzyme",
        "Amount of enzyme present per unit of volume. The participant role 'enzymatic catalyst' is defined in SBO:0000460.",
        (),
        False,
    ),
    "SBO_0000506": (
        "mass of enzyme",
        "Amount, expressed as a mass, of an enzyme. The participant role 'enzymatic catalyst' is defined in SBO:0000460.",
        (),
        False,
    ),
    "SBO_0000507": (
        "number of an enzyme",
        "Amount, expressed as a number, of a specific enzyme comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'enzymatic catalyst' is defined in SBO:0000460.",
        (),
        False,
    ),
    "SBO_0000508": (
        "number of a reactant",
        "The amount, expressed as a number, of a specific reactant comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'reactant' is defined in SBO:0000010.",
        (),
        False,
    ),
    "SBO_0000509": (
        "concentration of reactant",
        "The amount of a specific entity pool reactant present per unit of volume. The participant role 'reactant' is defined in SBO:0000010.",
        (),
        False,
    ),
    "SBO_0000510": (
        "mass of reactant",
        "The amount, expressed as a mass, of a specific reactant entity pool. The participant role 'reactant' is defined in SBO:0000010.",
        (),
        False,
    ),
    "SBO_0000511": (
        "number of a product",
        "The amount, expressed as a number, of a specific product comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'product' is defined in SBO:0000011.",
        (),
        False,
    ),
    "SBO_0000512": (
        "concentration of product",
        "The amount of a specific entity pool product present per unit of volume. The participant role 'product' is defined in SBO:0000011.",
        (),
        False,
    ),
    "SBO_0000513": (
        "mass of product",
        "The amount, expressed as a mass, of a specific product entity pool. The participant role 'product' is defined in SBO:0000011.",
        (),
        False,
    ),
    "SBO_0000514": (
        "number of a substrate",
        "The amount, expressed as a number, of a specific substrate comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'substrate' is defined in SBO:0000015.",
        (),
        False,
    ),
    "SBO_0000515": (
        "concentration of substrate",
        "The amount of a specific entity pool substrate present per unit of volume. The participant role 'substrate' is defined in SBO:0000015.",
        (),
        False,
    ),
    "SBO_0000516": (
        "mass of substrate",
        "The amount, expressed as a mass, of a specific substrate entity pool. The participant role 'substrate' is defined in SBO:0000015.",
        (),
        False,
    ),
    "SBO_0000517": (
        "number of a modifier",
        "The amount, expressed as a number, of a specific modifier comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'modifier' is defined in SBO:0000019.",
        (),
        False,
    ),
    "SBO_0000518": (
        "concentration of modifier",
        "The amount of a specific modifier entity pool present per unit of volume. The participant role 'modifier' is defined in SBO:0000019.",
        (),
        False,
    ),
    "SBO_0000519": (
        "mass of modifier",
        "The amount, expressed as a mass, of a specific modifier entity pool. The participant role 'modifier' is defined in SBO:0000019.",
        (),
        False,
    ),
    "SBO_0000520": (
        "number of an inhibitor",
        "The amount, expressed as a number, of a specific inhibitor comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'inhibitor' is defined in SBO:0000020.",
        (),
        False,
    ),
    "SBO_0000521": (
        "concentration of inhibitor",
        "The amount of a specific inhibitor entity pool present per unit of volume. The participant role 'inhibitor' is defined in SBO:0000020.",
        (),
        False,
    ),
    "SBO_0000522": (
        "mass of inhibitor",
        "The amount, expressed as a mass, of a specific inhibitor entity pool. The participant role 'inhibitor' is defined in SBO:0000020.",
        (),
        False,
    ),
    "SBO_0000523": (
        "number of an activator",
        "The amount, expressed as a number, of a specific activator comprising an entity pool. This may be expressed, for example, as the number of molecules, or the number of moles. The participant role 'activator' is defined in SBO:0000459.",
        (),
        False,
    ),
    "SBO_0000524": (
        "concentration of activator",
        "The amount of a specific activator entity pool present per unit of volume. The participant role 'activator' is defined in SBO:0000459.",
        (),
        False,
    ),
    "SBO_0000525": (
        "mass of activator",
        "The amount, expressed as a mass, of a specific activator entity pool. The participant role 'activator' is defined in SBO:0000459.",
        (),
        False,
    ),
    "SBO_0000526": (
        "protein complex formation",
        "The process by which two or more proteins interact non-covalently to form a protein complex (SBO:0000297).",
        (),
        False,
    ),
    "SBO_0000527": (
        "modular rate law",
        "Modular rate laws are a set of rate laws that provide a means to parameterise a system in a manner that is a compromise between mathematical abstraction and biochemical detail. They share the same common form: v = u f (T/(D + Dreg)) The individual numerator and denominator terms can substituted with alternative forms, depending on reaction details and model formulation, to generate specific modular rate laws. The terms represented are; v, reaction rate; u, enzyme amount; T, modular term derived from stoichiometries, metabolite concentrations and reactant constants; D, modular term for polynomial of scaled concentrations; Dreg, competitive regulation binding states term; f, modular term for regulation factor.",
        (),
        False,
    ),
    "SBO_0000528": (
        "common modular rate law",
        "The common modular rate law is a generalised form of reversible Michaelis Menten kinetics, using a denominator where each binding state of the enzyme is represented. It is assumed that substrates and products bind independently and randomly, and that substrates and products cannot be bound at the same time.",
        (),
        False,
    ),
    "SBO_0000529": (
        "direct binding modular rate law",
        "The direct binding modular rate law makes the assumption that both substrates and products bind simultaneously and in a single step, hence the total binding states possible enumerate to 3; nothing bound, substrates bound, and products bound. Substrates and products cannot be bound at the same time.",
        (),
        False,
    ),
    "SBO_0000530": (
        "simultaneous binding modular rate law",
        "The simultaneous binding modular rate law makes the assumption that substrates and products can be bound simultaneously, and in any combination.",
        (),
        False,
    ),
    "SBO_0000531": (
        "power-law modular rate law",
        "For the power-law rate law, the denominator is set to be a constant, and the rate law does not saturate.",
        (),
        False,
    ),
    "SBO_0000532": (
        "force-dependent modular rate law",
        "Modular rate law where the D term is given by the square root of the product of terms (c/KM)^m where c, KM, and m denote the concentrations, Michaelis constants, and molecularities, respectively, and the product is taken over all reactants and products involved in the reaction.",
        (),
        False,
    ),
    "SBO_0000533": (
        "specific activator",
        "An essential activator that affects the apparent value of the specificity constant. Mechanistically, the activator would need to be bound before reactant and product binding can take place.",
        (),
        False,
    ),
    "SBO_0000534": (
        "catalytic activator",
        "An essential activator that affects the apparent value of the catalytic constant.",
        (),
        False,
    ),
    "SBO_0000535": (
        "binding activator",
        "An essential activator that affects the apparent value of the Michaelis constant(s).",
        (),
        False,
    ),
    "SBO_0000536": (
        "partial inhibitor",
        "Substance that, when bound, decreases enzymatic activity to a lower, nonzero value, without itself being consumed or transformed by the reaction, and without sterically hindering the interaction between reactants. The enzyme-inhibitor complex does retain some basal level of activity.",
        (),
        False,
    ),
    "SBO_0000537": (
        "complete inhibitor",
        "Substance that, when bound, completely negates enzymatic activity, without itself being consumed or transformed by the reaction, and without sterically hindering the interaction between reactants. The inhibitor binds to all enzyme species independently and with the same affinity, completely inhibiting any enzymatic activity.",
        (),
        False,
    ),
    "SBO_0000538": ("ionic permeability", "Synonym: membrane permeability", (), False),
    "SBO_0000539": (
        "probabilistic parameter",
        "A quantitative parameter that represents a probability value, assigned to a specific event.",
        (),
        False,
    ),
    "SBO_0000540": (
        "fraction of an entity pool",
        "A ratio that represents the quantity of a defined constituent entity over the total number of all constituent entities present.",
        (),
        False,
    ),
    "SBO_0000541": (
        "mole fraction",
        "The number of moles of a constituent entity, divided by the total number of all constituent entities present in a system.",
        (),
        False,
    ),
    "SBO_0000542": ("basic reproductive ratio", "Synonym: R0", (), False),
    "SBO_0000543": (
        "protein aggregate",
        "A nonspecific coalescence of misfolded proteins which may or may not form a precipitate, depending upon particle size.",
        (),
        False,
    ),
    "SBO_0000544": (
        "metadata representation",
        "Supplementary information relating to a primary item of data, traditionally termed 'data about data'. It can describe, for example, the location or type of the data, or its relationship to other data.",
        (),
        False,
    ),
    "SBO_0000545": (
        "systems description parameter",
        "A value, numerical or symbolic, that defines certain characteristics of systems or system functions, or is necessary in their derivation.",
        (),
        False,
    ),
    "SBO_0000546": (
        "qualitative systems description parameter",
        "A non-numerical value that defines certain characteristics of systems or system functions.",
        (),
        False,
    ),
    "SBO_0000547": (
        "boolean logical framework",
        "Equationally defined algebraic framework usually interpreted as a two-valued logic using the basic Boolean operations (conjunction, disjunction and negation), together with the constants '0' and '1' denoting false and true values, respectively.",
        (),
        False,
    ),
    "SBO_0000548": (
        "multi-valued logical framework",
        "Extension of the boolean logical framework which associates a defined number of possible integer values (states) with the variables.",
        (),
        False,
    ),
    "SBO_0000549": (
        "fuzzy logical framework",
        "Extension of the Boolean logical framework which allows intermediate or undetermined values for the logical variables.",
        (),
        False,
    ),
    "SBO_0000550": (
        "annotation",
        "Supplementary information that does not modify the semantics of the presented information.",
        (),
        False,
    ),
    "SBO_0000551": (
        "controlled short label",
        "The use of an abbreviated name, taken from a controlled vocabulary of terms, which is used to represent some information about the entity to which it is attached.",
        (),
        False,
    ),
    "SBO_0000552": (
        "reference annotation",
        "Additional information that supplements existing data, usually in a document, by providing a link to more detailed information, which is held externally, or elsewhere.",
        (),
        False,
    ),
    "SBO_0000553": (
        "bibliographical reference",
        "An annotation which directs one to information contained within a published body of knowledge, usually a book or scientific journal.",
        (),
        False,
    ),
    "SBO_0000554": ("database cross reference", "Synonym: db xref", (), False),
    "SBO_0000555": (
        "controlled annotation",
        "Annotation which complies with the full set of defined rules in its construction.",
        (),
        False,
    ),
    "SBO_0000556": (
        "uncontrolled annotation",
        "Annotation which does not comply with, or is not restricted by, any rules in its construction. Examples would include free text annotations.",
        (),
        False,
    ),
    "SBO_0000557": (
        "embedded annotation",
        "Annotation that directly incorporates information into the body of a document.",
        (),
        False,
    ),
    "SBO_0000558": (
        "specific activity",
        "A measure of enzyme activity under standard conditions, at a specific substrate concentration (usually saturation), expressed as the amount of product formed per unit time, per amount of enzyme. This is often expressed as micromol per min per mg, rather than the less practical official unit, Katal (1 mol per second).",
        (),
        False,
    ),
    "SBO_0000559": (
        "enzyme activity",
        "A measure of the amount of active enzyme present, expressed under specified conditions. This is often expressed as micromol per min (also known as enzyme unit, U), rather than the less practical official SI unit, Katal (1 mol per second). Enzyme activity normally refers to the natural substrate for the enzyme, but can also be given for standardised substrates such as gelatin, where it is then referred to as GDU (Gelatin Digesting Units).",
        (),
        False,
    ),
    "SBO_0000560": (
        "mass action rate law for first order irreversible reactions, single essential stimulator, continuous scheme",
        "Reaction scheme in which the reaction velocity is direct proportional to the activity or concentration of a single molecular species. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of the stimulator. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000561": (
        "mass action rate law for first order irreversible reactions, single essential stimulator, discrete scheme",
        "Reaction scheme in which the reaction velocity is direct proportional to the activity or quantity of a single molecular species. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of the stimulator. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000562": (
        "mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator",
        "Reaction scheme where the products are created from a reactant and the change of a product quantity is proportional to the product of the reactant and the stimulator activities. The reaction scheme does not include any reverse process that creates the reactant from the products. The change of a product quantity is proportional to the quantity of the reactant and the stimulator.",
        (),
        False,
    ),
    "SBO_0000563": (
        "mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator, continuous scheme",
        "Reaction scheme where the products are created from a reactant and the change of a product quantity is proportional to the product of the reactant and the stimulator activities. The reaction scheme does not include any reverse process that creates the reactant from the products. The change of a product quantity is proportional to the quantity of the reactant and the stimulator. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000564": (
        "mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator, discrete scheme",
        "Reaction scheme where the products are created from a reactant and the change of a product quantity is proportional to the product of the reactant and the stimulator quantities. The reaction scheme does not include any reverse process that creates the reactant from the products. The change of a product quantity is proportional to the quantity of the reactant and the stimulator. It is to be used in a reaction modelled using a discrete framework.",
        (),
        False,
    ),
    "SBO_0000565": (
        "systems description constant",
        "A physical constant that is required in the calculation of a system parameter.",
        (),
        False,
    ),
    "SBO_0000566": (
        "relative permeability",
        "The permeability of an ion through a channel or membrane expressed in relation to the reference ion, which is given the value 1. For example, if a membrane is most permeable to K+, then that is assigned the reference permeability value of 1, and the value for Na+ may be 0.05.",
        (),
        False,
    ),
    "SBO_0000567": ("universal gas constant", "Synonym: molar gas constant", (), False),
    "SBO_0000568": (
        "Faraday constant",
        "Named after Michael Faraday, it is the magnitude of electric charge per mole of electrons. It has the value 96,485.3365 C/mol (Coulombs per Mole), and the symbol F.",
        (),
        False,
    ),
    "SBO_0000569": (
        "Goldman equation",
        "Synonym: Goldman-Hodgkin-Katz voltage equation",
        (),
        False,
    ),
    "SBO_0000570": ("Nernst potential", "Synonym: reversal potential", (), False),
    "SBO_0000571": (
        "thermodynamic parameter",
        "Parameters used in the study of thermodynamics, a physical science that pertains to the relationship between heat and other forms of energy such as 'work done' in material bodies.",
        (),
        False,
    ),
    "SBO_0000572": (
        "enthalpy",
        "A thermodynamic potential whose natural variables are entropy (S) and pressure (p). The enthalpy of a system, measured in Joules (J), is defined as H = U + pV (where H is enthalpy, U is the internal energy, p is the pressure at the system boundary, and V is the system volume). symbol: H",
        (),
        False,
    ),
    "SBO_0000573": (
        "enthalpy change",
        "Change in enthalpy observed in the constituents of a thermodynamic system when undergoing a transformation or chemical reaction. This is the preferred way of expressing the energy changes to a system at constant pressure, since enthalpy itself cannot be directly measured. The enthalpy change is positive in endothermic reactions, negative in exothermic reactions, and is defined as the difference between the final and initial enthalpy of the system under study: ΔH = Hf - Hi. The standard unit of measure is J. Symbol: ΔH",
        (),
        False,
    ),
    "SBO_0000574": (
        "standard enthalpy of formation",
        "The enthalpy change observed in a constituent of a thermodynamic system when one mole of a compound, in its standard state, is formed from its elementary antecedents, in their standard state(s), under standard conditions (1 bar). The standard unit of measure is kJ/mol. Symbol: DeltaHf0, DeltafH0",
        (),
        False,
    ),
    "SBO_0000575": (
        "standard enthalpy of reaction",
        "The enthalpy change observed in a constituent of a thermodynamic system when one mole of substance reacts completely, under standard conditions (1 bar). The standard unit of measure is kJ/mol. Symbol: DeltaHr0, DeltarH0",
        (),
        False,
    ),
    "SBO_0000576": (
        "entropy",
        "A thermodynamic property which acts as a measure of the state of disorder of a system. Its natural variables are the internal energy (U) and the volume (V). It is defined by dS = (1/T)dU + (p/T)dV. The second law of thermodynamics states that in an isolated system, natural processes tend to increase in disorder or entropy. The standard unit of measure is Joules per Kelvin (J/K). symbol: S",
        (),
        False,
    ),
    "SBO_0000577": (
        "entropy change",
        "The increase or decrease of the entropy of a system. For values greater than zero, there is an implied increase in the disorder of a system, for example during a reaction, and decreased disorder where the values are less than zero. The entropy change of a process is defined as the initial system entropy value minus the final entropy value: DeltaS = Sf - Si. The standard unit of measure is J/K. symbol: DeltaS",
        (),
        False,
    ),
    "SBO_0000578": (
        "standard entropy of reaction ",
        "The entropy change observed in a thermodynamic system when one mole of substance reacts completely, under standard conditions (1 bar). The standard unit of measure is kJ/(mol K). This can be calculated using the entropies for products and reactants: DeltaS(reaction)=sum DeltaS (products) - sum DeltaS reactants. The standard unit of measure is kJ/(mol K). symbol: DeltaSro",
        (),
        False,
    ),
    "SBO_0000579": (
        "standard entropy of formation",
        "The change in entropy associated with the formation of one mole of a substance from its elements in their standard states under standard conditions (1 bar). The standard unit of measure is kJ/(mol K). symbol: DeltaSfo",
        (),
        False,
    ),
    "SBO_0000580": ("Gibbs free energy", "Synonym: Gibbs function", (), False),
    "SBO_0000581": (
        "Gibbs free energy change",
        "The increase or decrease of the Gibbs free energy of a system. During a reaction, this is equal to the change in enthalpy of the system minus the change in the product of the temperature times the entropy of the system: ΔG = ΔH - T ΔS. A negative value indicates that the reaction will be favoured and will release energy. The magnitude of the value indicates how far the reaction is from equilibrium, where there will be no free energy change. The standard unit of measure is kJ/mol. Symbol: ΔG.",
        (),
        False,
    ),
    "SBO_0000582": (
        "standard Gibbs free energy of formation",
        "The change in Gibbs free energy associated with the formation of 1 mole of substance from elements in their standard states under standard conditions (1 bar). For aqueous solutions, each solute must be present in 1M concentration. The standard unit of measure is kJ/mol. Symbol: ΔGf°.",
        (),
        False,
    ),
    "SBO_0000583": (
        "standard Gibbs free energy of reaction",
        "The Gibbs free energy change observed in a thermodynamic system when one mole of substance reacts completely, under standard conditions (1 bar). For aqueous solutions, each solute must be present in 1M concentration. The standard unit of measure is kJ/mol. Symbol: ΔG°.",
        (),
        False,
    ),
    "SBO_0000584": (
        "temporal offset",
        "A duration of time after which a phase shift occurs.",
        (),
        False,
    ),
    "SBO_0000585": (
        "simulation duration",
        "The total length of time over which a model is simulated, where the time scale is indicated within the model simulation.",
        (),
        False,
    ),
    "SBO_0000586": (
        "model time",
        "A conceptualisation of time which is intrinsic to a mathematical model, and which can be used to describe other variables or parameters of the model.",
        (),
        False,
    ),
    "SBO_0000587": (
        "transcellular membrane influx reaction",
        "A transport reaction which results in the entry of the transported entity, into the cell.",
        (),
        False,
    ),
    "SBO_0000588": (
        "transcellular membrane efflux reaction",
        "A transport reaction which results in the removal of the transported entity from the cell.",
        (),
        False,
    ),
    "SBO_0000589": (
        "genetic production",
        "A composite biochemical process through which a gene sequence is fully converted into mature gene products. These gene products may include RNA species as well as proteins, and the process encompasses all intermediate steps required to generate the active form of the gene product.",
        (),
        False,
    ),
    "SBO_0000590": (
        "promoter",
        "A stretch of DNA upstream of a transcription start site, to which a promoter and other transcription factors may bind to initiate or regulate expression.",
        (),
        False,
    ),
    "SBO_0000591": (
        "petri net transition",
        "A process that can modify the state of petri net 'places'[SBO:0000593].",
        (),
        False,
    ),
    "SBO_0000592": (
        "discrete amount of an entity pool",
        "A discrete value attributed to an entity pool.",
        (),
        False,
    ),
    "SBO_0000593": (
        "petri net place",
        "A defined entity pool state which can be modified by a petri net transition [SBO:0000591].",
        (),
        False,
    ),
    "SBO_0000594": (
        "neutral participant",
        "A participant whose presence does not alter the velocity of a process or event.",
        (),
        False,
    ),
    "SBO_0000595": (
        "dual-activity modifier",
        "A modifier that can exhibit either inhibitory or stimulatory effects on a process depending on the context in which it occurs. For example, the observed effect may be dependent upon the concentration of the modifier.",
        (),
        False,
    ),
    "SBO_0000596": (
        "modifier of unknown activity",
        "A modifier whose activity is not known or has not been specified.",
        (),
        False,
    ),
    "SBO_0000597": (
        "silencer",
        "A silencer is a modifier which acts in a manner that completely prevents an event or process from occurring. For example, a silencer in gene expression is usually a transcription factor that binds a DNA sequence in such a way as to completely prevent the binding of RNA polymerase, and thus fully suppresses transcription.",
        (),
        False,
    ),
    "SBO_0000598": (
        "promoter",
        "A region of DNA to which various transcription factors and RNA polymerase must bind in order to initiate transcription for a gene.",
        (),
        False,
    ),
    "SBO_0000599": (
        "port",
        "A denotement that specifies a point of contact between variables or submodels in a hierarchical model.",
        (),
        False,
    ),
    "SBO_0000600": (
        "input port",
        "A connection point to an element in a model that indicates that the element's mathematical interpretation is defined outside the model.",
        (),
        False,
    ),
    "SBO_0000601": (
        "output port",
        "A connection point to an element in a model that indicates that the element's mathematical interpretation is defined within the model.",
        (),
        False,
    ),
    "SBO_0000602": (
        "logical parameter",
        "A parameter that takes only logical values.",
        (),
        False,
    ),
    "SBO_0000603": (
        "side product",
        "A substance that is produced in a chemical reaction but is not itself the primary product or focus of that reaction. Examples include, but are not limited to, currency compounds such as ATP, NADPH and protons.",
        (),
        False,
    ),
    "SBO_0000604": (
        "side substrate",
        "A substance that is consumed in a chemical reaction but is not itself the primary substrate or focus of that reaction. Examples include, but are not limited to, currency compounds such as ATP, NADPH and protons.",
        (),
        False,
    ),
    "SBO_0000605": (
        "high affinity receptor",
        "A receptor where binding occurs through strong intermolecular forces such as Van der Waals, hydrogen bonds or ionic bonds.",
        (),
        False,
    ),
    "SBO_0000606": (
        "low affinity receptor",
        "A receptor where binding occurs through weak intermolecular forces.",
        (),
        False,
    ),
    "SBO_0000607": (
        "dimer",
        "A macromolecular complex composed of two monomeric units, which may or may not be identical. Monomers are usually non-covalently bound.",
        (),
        False,
    ),
    "SBO_0000608": (
        "homodimer",
        "A macromolecular complex composed of precisely two identical monomeric units, which are usually non-covalently bound.",
        (),
        False,
    ),
    "SBO_0000609": (
        "heterodimer",
        "A macromolecular complex composed of precisely two non-identical monomeric units, which are usually non-covalently bound.",
        (),
        False,
    ),
    "SBO_0000610": (
        "growth rate",
        "A measure of the rate of growth of an organism, usually in culture. This can be expressed as increase in cell number or, more usually as an increase in dry weight of cells (grams), measured over a unit time period. Usually expressed as hour -1.",
        (),
        False,
    ),
    "SBO_0000611": (
        "effective catalytic rate",
        "Under nutrient limited conditions, it may be assumed that enzymes are operating below their maximal capacity (Kcat). Keff represents the lumped turnover rate of a reaction, expressed in units per time.",
        (),
        False,
    ),
    "SBO_0000612": (
        "rate of reaction",
        "The velocity at which a reaction occurs. This may be calculated through the accumulation of a product or consumption of a reactant, and expressed using entity concentrations or amounts per time interval. The rate of reaction may be influenced by temperature, pressure and other factors. Rate of reaction is often referred to as reaction rate or metabolic flux.",
        (),
        False,
    ),
    "SBO_0000613": (
        "reaction parameter",
        "Parameters that pertain to chemical reactions.",
        (),
        False,
    ),
    "SBO_0000614": (
        "rate of reaction (concentration)",
        "Rate of reaction expressed as a change in concentration over time.",
        (),
        False,
    ),
    "SBO_0000615": (
        "rate of reaction (amount)",
        "Rate of reaction expressed as a change in enumerated quantity over time.",
        (),
        False,
    ),
    "SBO_0000616": (
        "extent of reaction",
        "The extent of a reaction is a measure of how far a reaction has proceeded towards equilibrium. It is denoted by the Greek letter Î¾ and is expressed in moles.",
        (),
        False,
    ),
    "SBO_0000617": (
        "Gibbs free energy of reaction",
        "The Gibbs free energy change observed in a thermodynamic system when a substance undergoes a reaction under non standard conditions. The unit of measure is kJ/mol. Symbol: ΔG.",
        (),
        False,
    ),
    "SBO_0000618": (
        "reaction affinity",
        "Synonym: thermodynamic driving force",
        (),
        False,
    ),
    "SBO_0000619": (
        "transformed Gibbs free energy change",
        "A Gibbs free energy that is calculated from the standard Gibbs value (at 298K), and extrapolated to a desired pH and ionic strength, and may be determined at a different temperature. Symbol: ΔG´.",
        (),
        False,
    ),
    "SBO_0000620": (
        "transformed standard Gibbs free energy of reaction",
        "A Gibbs free energy of reaction that is calculated from the standard Gibbs value (at 298K), and extrapolated to a desired pH and ionic strength, and may be determined at a different temperature. Symbol ΔG´.",
        (),
        False,
    ),
    "SBO_0000621": (
        "transformed standard Gibbs free energy of formation",
        "A Gibbs free energy of formation that is calculated from the standard Gibbs value (at 298K), and extrapolated to a desired pH and ionic strength, and may be determined at a different temperature. Symbol ΔGf´.",
        (),
        False,
    ),
    "SBO_0000622": (
        "transformed Gibbs free energy of reaction",
        "The Gibbs free energy change observed in a thermodynamic system when a substance undergoes a reaction under non standard conditions, which is extrapolated to a desired pH and ionic strength, and may be determined at a different temperature. Symbol: ΔG´.",
        (),
        False,
    ),
    "SBO_0000623": (
        "ionic strength",
        "A combined (weighted) measure of the concentration of all electrolytes present in a solution. It is calculated as a half of the sum over all the ions in the solution multiplied by the square of individual ionic valencies. Monovalent electrolytes have a concentration equal to their ionic strength while multivalent electrolytes have greater ionic strength, directly proportional to ionic valency. Symbol: I",
        (),
        False,
    ),
    "SBO_0000624": (
        "flux balance framework",
        "Modelling approach, typically used for metabolic models, where the flow of metabolites (flux) through a network can be calculated. This approach will generally produce a set of solutions (solution space), which may be reduced using objective functions and constraints on individual fluxes.",
        (),
        False,
    ),
    "SBO_0000625": (
        "flux bound",
        "A parameter that limits the upper or lower value that a flux may assume. This parameter may be determined experimentally, or may be the result of theoretical investigation.",
        (),
        False,
    ),
    "SBO_0000626": (
        "default flux bound",
        "A value used for flux bound in cases where a precise value, supported experimentally or theoretically, is not available.",
        (),
        False,
    ),
    "SBO_0000627": (
        "exchange reaction",
        "A modeling process to provide matter influx or efflux to a model, for example to replenish a metabolic network with raw materials (eg carbon / energy sources). Such reactions are conceptual, created solely for modeling purposes, and do not have a physical correspondence. Exchange reactions, often represented as 'R_EX_', can operate in the negative (uptake) direction or positive (secretion) direction. By convention, a negative flux through an exchange reaction represents uptake of the corresponding metabolite, and a positive flux represent discharge.",
        (),
        False,
    ),
    "SBO_0000628": (
        "demand reaction",
        "A modeling process analogous to exchange reaction, but which operates upon \"internal\" metabolites. Metabolites that are consumed by these reactions are assumed to be used in intra-cellular processes that are not part of the model. Demand reactions, often represented 'R_DM_', can also deliver metabolites (from intra-cellular processes that are not considered in the model).",
        (),
        False,
    ),
    "SBO_0000629": (
        "biomass production",
        "Biomass production, often represented 'R_BIOMASS_', is usually the optimization target reaction of constraint-based models, and can consume multiple reactants to produce multiple products. It is also assumed that parts of the reactants are also consumed in unrepresented processes and hence products do not have to reflect all the atom composition of the reactants. Formulation of a biomass production process entails definition of the macromolecular content (eg. cellular protein fraction), metabolic constitution of each fraction (eg. amino acids), and subsequently the atomic composition (eg. nitrogen atoms). More complex biomass functions can additionally incorporate details of essential vitamins and cofactors required for growth.",
        (),
        False,
    ),
    "SBO_0000630": ("ATP maintenance", "Synonym: maintenance energy", (), False),
    "SBO_0000631": (
        "pseudoreaction",
        "A conceptual process used for modeling purposes, often created solely to complete model structure, with respect to providing inflow or outflow of matter or material. Unlike other reactions, pseudoreactions are not usually subjected to mass balance considerations.",
        (),
        False,
    ),
    "SBO_0000632": ("sink reaction", "Synonym: source/sink", (), False),
    "SBO_0000633": (
        "subsystem",
        "Term used to indicate the grouping of model components, largely reactions, by some criterion, often processual. This can be used to indicate, for example, the subsystem of a model that is concerned with 'transport'. A designated subsystem includes reactions annotated with the term, as well as reactions participants such as enzymes, modifiers and genes encoding these subsystem components.",
        (),
        False,
    ),
    "SBO_0000634": (
        "DNA segment",
        "Fragment or region of a DNA macromolecule.",
        (),
        False,
    ),
    "SBO_0000635": (
        "RNA segment",
        "Fragment or region of an RNA macromolecule.",
        (),
        False,
    ),
    "SBO_0000636": (
        "allosteric activator",
        "Synonym: positive allosteric modulation",
        (),
        False,
    ),
    "SBO_0000637": (
        "non-allosteric activator",
        "Describes an activator (ligand) which binds to the enzyme, which does not result in a conformational change, but which enhances the enzyme's activity.",
        (),
        False,
    ),
    "SBO_0000638": (
        "irreversible inhibitor",
        "An inhibitor which binds irreversibly with the enzyme such that it cannot be removed, and abolishes enzymatic function.",
        (),
        False,
    ),
    "SBO_0000639": (
        "allosteric inhibitor",
        "An inhibitor whose binding to an enzyme results in a conformational change, resulting in a loss of enzymatic activity. This activity can be restored upon removal of the inhibitor.",
        (),
        False,
    ),
    "SBO_0000640": (
        "uncompetitive inhibitor",
        "Synonym: anti-competitive inhibitor",
        (),
        False,
    ),
    "SBO_0000641": (
        "pMg",
        "An enumeration of the concentration of magnesium (Mg) in solution (pMg = -log10[Mg2+]).",
        (),
        False,
    ),
    "SBO_0000642": (
        "inhibited",
        "Conceptual or material entity that is the object of an inhibition process, and is acted upon by an inhibitor.",
        (),
        False,
    ),
    "SBO_0000643": (
        "stimulated",
        "Conceptual or material entity that is the object of a stimulation process, and is acted upon by a stimulator.",
        (),
        False,
    ),
    "SBO_0000644": (
        "modified",
        "Conceptual or material entity that is the object of a modification process, and is acted upon by a modifier.",
        (),
        False,
    ),
    "SBO_0000645": (
        "template",
        "An entity that acts as the starting material for genetic production (http://identifiers.org/biomodels.sbo/SBO:0000589).",
        (),
        False,
    ),
    "SBO_0000646": (
        "mass action rate law for reversible reactions, continuous schema",
        "Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme includes a reverse process that creates the reactants from the products. It is to be used in a reaction modelled using a continuous framework.",
        (),
        False,
    ),
    "SBO_0000647": ("molecular mass", "Synonym: molecular weight", (), False),
    "SBO_0000648": (
        "protein molecular mass",
        "Synonym: protein molecular weight",
        (),
        False,
    ),
    "SBO_0000649": (
        "biomass",
        "A composite representation of material entities required for organismal growth. It includes macromolecular content (eg. cellular protein fraction), metabolic constitution of each fraction (eg. amino acids), and atomic composition (eg. nitrogen atoms).",
        (),
        False,
    ),
    "SBO_0000650": (
        "reversible process",
        "A sequential series of actions, motions, or occurrences, such as chemical reactions, where a reversal of states that bring the system back to its original state in a characteristic manner occurs.",
        (),
        False,
    ),
    "SBO_0000651": (
        "irreversible process",
        "A sequential series of actions, motions, or occurrences, such as chemical reactions, where a reversal of states that bring the system back to its original state in a characteristic manner does not occur.",
        (),
        False,
    ),
    "SBO_0000652": (
        "polymerization",
        "A chemical reaction in which one or more monomer molecules combine to form a larger polymer molecule with repeated structural units.",
        (),
        False,
    ),
    "SBO_0000653": (
        "depolymerization",
        "A chemical reaction in which a large polymer breaks into its constituent monomers (or mixture of monomers).",
        (),
        False,
    ),
    "SBO_0000654": (
        "co-transport reaction",
        "A biochemical process involving the simultaneous transport of two or more substances across a membrane via a protein or protein complex.",
        (),
        False,
    ),
    "SBO_0000655": (
        "transport reaction",
        "The movement of an entity/entities across a biological membrane mediated by a transporter protein.",
        (),
        False,
    ),
    "SBO_0000656": (
        "activation",
        "A conformational change in a protein resulting in its activation.",
        (),
        False,
    ),
    "SBO_0000657": (
        "active transport",
        "Protein assisted movement of molecules across a membrane from a region of low concentration to high concentration involving the consumption of cellular energy (ATP molecules).",
        (),
        False,
    ),
    "SBO_0000658": (
        "passive transport",
        "Movement of molecules without the need for external energy, and usually from a region of high concentration to low concentration.",
        (),
        False,
    ),
    "SBO_0000659": (
        "symporter-mediated transport",
        "A membrane protein mediated transport of two ore more molecules in the same relative direction across a membrane.",
        (),
        False,
    ),
    "SBO_0000660": (
        "antiporter-mediated transport",
        "A membrane protein mediated transport of two or more molecules in opposite directions across a membrane.",
        (),
        False,
    ),
    "SBO_0000661": (
        "capacity",
        "Total amount that can be contained or produced by a specific entity. This can refer to diverse items, such as the carrying capacity of a membrane with respect to proteins, the capacity of high-energy phosphate bonds, or the maximal count of bacteria in the gut, etc.",
        (),
        False,
    ),
    "SBO_0000662": (
        "occupancy",
        "Occopancy is a quantitative systemic property that indicates which number of available places is occupied. This can refer to diverse things, such as the number of occupied high-energy phosphate bonds in ATP, the number of bacteria in the gut, or the number of electrons loaded onto redox carriers, etc.",
        (),
        False,
    ),
    "SBO_0000663": (
        "fractional occupancy",
        "Fractional occupancy is a quantitative dynamic property of a system that can be calculated as the fraction of occupancy over capacity.",
        (),
        False,
    ),
    "SBO_0000664": (
        "contained entity",
        "an entity which physical constituents are partially or totally contained in a defined compartment.",
        (),
        False,
    ),
    "SBO_0000665": (
        "inactivation",
        "a conformation changes to a protein leading to its inactivation",
        (),
        False,
    ),
    "SBO_0000666": (
        "chain length",
        "describes the number of amino acids,nucleic acid in a protein/DNA/RNA chain",
        (),
        False,
    ),
    "SBO_0000667": (
        "protein chain length",
        "length of amino acid sequence in a protein",
        (),
        False,
    ),
    "SBO_0000668": (
        "yield",
        "output generated as biomass or product from a/set of chemical reaction/s.",
        (),
        False,
    ),
    "SBO_0000669": (
        "biomass yield on substrate",
        "generation of biomass for an substrate through a defined reaction/s.",
        (),
        False,
    ),
    "SBO_0000670": (
        "product yield on substrate",
        "generation of product from substrate in a defined chemical reaction.",
        (),
        False,
    ),
    "SBO_0000671": (
        "non-enzymatic catalyst",
        "agent driving non-enzymatic reaction. Non-enzymatic reactions resemble catalytic mechanisms as found in all major enzyme classes and occur spontaneously, small molecule (e.g. metal-) catalyzed or light-induced.",
        (),
        False,
    ),
    "SBO_0000672": (
        "spontaneous reaction",
        "Reaction with no catalyst (no enzyme in particular) is needed to proceed.",
        (),
        False,
    ),
    "SBO_0000673": (
        "forward effective catalytic rate",
        "it represent the catalytic rate driving the reaction in forward direction.",
        (),
        False,
    ),
    "SBO_0000674": (
        "reverse effective catalytic rate",
        "it represent the catalytic rate driving the reaction in backward direction.",
        (),
        False,
    ),
    "SBO_0000675": (
        "deterministic non-spatial continuous framework",
        "Modeling approach where the quantities of participants are considered deterministic continuous variables, and represented by real values. The associated simulation methods make use of ordinary differential equations.",
        (),
        False,
    ),
    "SBO_0000676": (
        "stochastic non-spatial continuous framework",
        "Modeling approach where the quantities of participants are considered stochastic continuous variables, and represented by real values. The associated simulation methods make use of stochastic differential equations. The models do take into account the distribution of the entities.",
        (),
        False,
    ),
    "SBO_0000677": (
        "population-based discrete spatial simulation",
        "Modeling approach which tracks the sizes of populations of participants in each spatial localization. For biochemical simulations, such populations could represent types of molecular species.",
        (),
        False,
    ),
    "SBO_0000678": (
        "particle-based discrete spatial simulation",
        "Modeling approach which tracks the state of individual particles in each spatial localization. For biochemical simulations, such particles could represent individual molecules.",
        (),
        False,
    ),
    "SBO_0000679": (
        "population-based discrete non-spatial simulation",
        "Modeling approach which tracks the sizes of populations of participants with minimal or no spatial resolution. For biochemical simulations, such populations could represent types of molecular species.",
        (),
        False,
    ),
    "SBO_0000680": (
        "particle-based discrete non-spatial simulation",
        "Modeling approach which tracks the state of individual particles with miimal or no spatial resolution. For biochemical simulations, such particles could represent individual molecules.",
        (),
        False,
    ),
    "SBO_0000681": (
        "hybrid framework",
        "Modeling approach which combines multiple canonical modeling frameworks. For example, a hybrid model could consider both continuous (represented by real values) and discrete (represented by integers) participants. Hybrid models are executed with hybrid simulation algorithms. For example, a hybrid continuous-discrete model may be simulation using a combination of stochastic simulation and ordinary differential equations.",
        (),
        False,
    ),
    "SBO_0000682": (
        "hybrid spatial framework",
        "Modeling approach which combines multiple canonical spatial modeling frameworks. For example, a hybrid model could consider both continuous (represented by real values) and discrete (represented by integers) participants. Hybrid models are executed with hybrid simulation algorithms. For example, a hybrid continuous-discrete model may be simulation using a combination of stochastic simulation and partial differential equations.",
        (),
        False,
    ),
    "SBO_0000683": (
        "hybrid non-spatial framework",
        "Modeling approach which combines multiple canonical non-spatial modeling frameworks. For example, a hybrid model could consider both continuous (represented by real values) and discrete (represented by integers) participants. Hybrid models are executed with hybrid simulation algorithms. For example, a hybrid continuous-discrete model may be simulation using a combination of stochastic simulation and ordinary differential equations.",
        (),
        False,
    ),
    "SBO_0000684": (
        "hybrid flux balance-deterministic continuous non-spatial framework",
        "Modeling approach which combines flux-balance [SBO:0000624] and deterministic continuous non-spatial [SBO:0000675] simulation. For example, a metabolic network could be simulated using flux balance analysis, while a signaling network could be co-simulated with a method for integrating ordinary differential equations.",
        (),
        False,
    ),
    "SBO_0000685": (
        "hybrid flux balance-discrete non-spatial framework",
        "Modeling approach which combines flux-balance [SBO:0000624] and discrete non-spatial [SBO:0000295] simulation. For example, a metabolic network could be simulated using flux balance analysis, while the synthesis and turnover of enzymes could be co-simulated with a discrete simulation method such as Gillespie's algorithm.",
        (),
        False,
    ),
    "SBO_0000686": (
        "hybrid flux balance-logical-deterministic continuous non-spatial framework",
        "Modeling approach which combines flux-balance [SBO:0000624], non-spatial deterministic continuous [SBO:0000675], and logical [SBO:0000234] simulation. For example, a metabolic network could be simulated using flux balance analysis, while the expression metabolic enzymes could be co-simulated with a logical simulation method and a signaling network could be co-simulated with a method for integrating ordinary differential equations such as CVODE.",
        (),
        False,
    ),
    "SBO_0000687": (
        "hybrid flux balance-logical non-spatial framework",
        "Modeling approach which combines flux-balance [SBO:0000624] and logical [SBO:0000234] simulation. For example, a metabolic network could be simulated using flux balance analysis, while the expression metabolic enzymes could be co-simulated with a logical simulation method.",
        (),
        False,
    ),
    "SBO_0000688": (
        "hybrid flux logical-discrete non-spatial framework",
        "Modeling approach which combines logical [SBO:0000234] and non-spatial discrete [SBO:0000295] simulation. For example, the MaBoSS simulation method simulates logical regulatory graphs with an algorithm that is similar to Gillespie's algorithm.",
        (),
        False,
    ),
    "SBO_0000689": (
        "hybrid continuous-discrete non-spatial framework",
        "Modeling approach which combines continuous [SBO:0000293] and discrete [SBO:0000295] simulation, where some participants are represented as continuous variables and others are represented as discrete variables, without a detailed spatial representation of each participant. For example, a model may be simulated using a combination of a discrete simulation method such as Gillespie's algorithm and an ordinary differential equations integration method such as CVODE.",
        (),
        False,
    ),
    "SBO_0000690": (
        "hybrid deterministic continuous-discrete non-spatial framework",
        "Modeling approach which combines deterministic continuous [SBO:0000675] and discrete [SBO:0000295] simulation, where some participants are represented as deterministic, continuous variables and others are represented as discrete variables, without a detailed spatial representation of each participant. For example, a model may be simulated using a combination of a discrete simulation method such as Gillespie's algorithm and an ordinary differential equations integration method such as CVODE.",
        (),
        False,
    ),
    "SBO_0000691": (
        "hybrid stochastic continuous-discrete non-spatial framework",
        "Modeling approach which combines stochastic continuous [SBO:0000676] and discrete [SBO:0000295] simulation, where some participants are represented as stochastic, continuous variables and others are represented as discrete variables, without a detailed spatial representation of each participant. For example, a model may be simulated using a combination of a discrete simulation method such as Gillespie's algorithm and an stochastic differential equations integration method.",
        (),
        False,
    ),
    "SBO_0000692": (
        "resource balance framework",
        "Modeling approach where the flow of resources (flux) through a network can be calculated. This approach will generally produce a set of solutions (solution space), which may be reduced using objective functions and constraints on individual fluxes.",
        (),
        False,
    ),
    "SBO_0000693": (
        "constraint-based framework",
        "Modelling approach which captures bounds on the possible behavior of a system, which may be further reduced using an objective function.",
        (),
        False,
    ),
    "SBO_0000694": (
        "optimization framework",
        "Modelling approach for finding the optimal state of a system.",
        (),
        False,
    ),
    "SBO_0000695": (
        "ligation",
        "Formation of a covalent bond resulting in the creation of a link between the ends of one or more linear polymer molecules.",
        (),
        False,
    ),
    "part_of": ("part of", None, (), False),
}

SBO._terms = _terms

__all__ = [
    "SBO",
    "SBOType",
]
