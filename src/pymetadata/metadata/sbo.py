"""SBO ontology."""

from enum import Enum


class SBO(str, Enum):
    """Enum for SBO ontology."""

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
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_UNIREACTANT_ENZYMES = (
        "SBO_0000028"
    )

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

    # mass action rate law for second order irreversible reactions, one reactant, continuous scheme
    SBO_0000052 = "SBO_0000052"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = (
        "SBO_0000052"
    )

    # mass action rate law for second order irreversible reactions, two reactants
    SBO_0000053 = "SBO_0000053"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000053"
    )

    # mass action rate law for second order irreversible reactions, two reactants, continuous scheme
    SBO_0000054 = "SBO_0000054"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000054"
    )

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
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = (
        "SBO_0000057"
    )

    # mass action rate law for third order irreversible reactions, two reactants
    SBO_0000058 = "SBO_0000058"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000058"
    )

    # mass action rate law for third order irreversible reactions, two reactants, continuous scheme
    SBO_0000059 = "SBO_0000059"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000059"
    )

    # mass action rate law for third order irreversible reactions, three reactants
    SBO_0000060 = "SBO_0000060"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__THREE_REACTANTS = (
        "SBO_0000060"
    )

    # mass action rate law for third order irreversible reactions, three reactants, continuous scheme
    SBO_0000061 = "SBO_0000061"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__THREE_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000061"
    )

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
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000070"
    )

    # mass action rate law for zeroth order forward, second order reverse, reversible reactions, continuous scheme
    SBO_0000071 = "SBO_0000071"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000071"
    )

    # mass action rate law for zeroth order forward, second order reverse, reversible reactions, one product, continuous scheme
    SBO_0000072 = "SBO_0000072"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000072"
    )

    # mass action rate law for zeroth order forward, second order reverse, reversible reactions, two products, continuous scheme
    SBO_0000073 = "SBO_0000073"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000073"
    )

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, continuous scheme
    SBO_0000074 = "SBO_0000074"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000074"
    )

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, one product, continuous scheme
    SBO_0000075 = "SBO_0000075"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000075"
    )

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, two products, continuous scheme
    SBO_0000076 = "SBO_0000076"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000076"
    )

    # mass action rate law for zeroth order forward, third order reverse, reversible reactions, three products, continuous scheme
    SBO_0000077 = "SBO_0000077"
    MASS_ACTION_RATE_LAW_FOR_ZEROTH_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000077"
    )

    # mass action rate law for first order reversible reactions
    SBO_0000078 = "SBO_0000078"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_REVERSIBLE_REACTIONS = "SBO_0000078"

    # mass action rate law for first order forward, zeroth order reverse, reversible reactions, continuous scheme
    SBO_0000079 = "SBO_0000079"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000079"
    )

    # mass action rate law for first order forward, first order reverse, reversible reactions, continuous scheme
    SBO_0000080 = "SBO_0000080"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__CONTINUOUS_SCHEME = (
        "SBO_0000080"
    )

    # mass action rate law for first order forward, second order reverse, reversible reactions
    SBO_0000081 = "SBO_0000081"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS = (
        "SBO_0000081"
    )

    # mass action rate law for first order forward, second order reverse, reversible reactions, one product, continuous scheme
    SBO_0000082 = "SBO_0000082"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000082"
    )

    # mass action rate law for first order forward, second order reverse, reversible reactions, two products, continuous scheme
    SBO_0000083 = "SBO_0000083"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000083"
    )

    # mass action rate law for first order forward, third order reverse, reversible reactions
    SBO_0000084 = "SBO_0000084"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS = (
        "SBO_0000084"
    )

    # mass action rate law for first order forward, third order reverse, reversible reactions, one product, continuous scheme
    SBO_0000085 = "SBO_0000085"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000085"
    )

    # mass action rate law for first order forward, third order reverse, reversible reactions, two products, continuous scheme
    SBO_0000086 = "SBO_0000086"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000086"
    )

    # mass action rate law for first order forward, third order reverse, reversible reactions, three products, continuous scheme
    SBO_0000087 = "SBO_0000087"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000087"
    )

    # mass action rate law for second order reversible reactions
    SBO_0000088 = "SBO_0000088"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_REVERSIBLE_REACTIONS = "SBO_0000088"

    # mass action rate law for second order forward, reversible reactions, one reactant
    SBO_0000089 = "SBO_0000089"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000089"
    )

    # mass action rate law for second order forward, zeroth order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000090 = "SBO_0000090"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = (
        "SBO_0000090"
    )

    # mass action rate law for second order forward, first order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000091 = "SBO_0000091"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = (
        "SBO_0000091"
    )

    # mass action rate law for second order forward, second order reverse, reversible reactions, one reactant
    SBO_0000092 = "SBO_0000092"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000092"
    )

    # mass action rate law for second order forward, second order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000093 = "SBO_0000093"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000093"
    )

    # mass action rate law for second order forward, second order reverse, reversible reactions, two products, continuous scheme
    SBO_0000094 = "SBO_0000094"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000094"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant
    SBO_0000095 = "SBO_0000095"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000095"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000096 = "SBO_0000096"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000096"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, two products, continuous scheme
    SBO_0000097 = "SBO_0000097"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000097"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, one reactant, three products, continuous scheme
    SBO_0000098 = "SBO_0000098"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000098"
    )

    # mass action rate law for second order forward, reversible reactions, two reactants
    SBO_0000099 = "SBO_0000099"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__REVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000099"
    )

    # mass action rate law for second order forward, zeroth order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000100 = "SBO_0000100"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000100"
    )

    # mass action rate law for second order forward, first order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000101 = "SBO_0000101"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000101"
    )

    # mass action rate law for second order forward, second order reverse, reversible reactions, two reactants
    SBO_0000102 = "SBO_0000102"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000102"
    )

    # mass action rate law for second order forward, second order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000103 = "SBO_0000103"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000103"
    )

    # mass action rate law for second order forward, second order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000104 = "SBO_0000104"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000104"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants
    SBO_0000105 = "SBO_0000105"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000105"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000106 = "SBO_0000106"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000106"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000107 = "SBO_0000107"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000107"
    )

    # mass action rate law for second order forward, third order reverse, reversible reactions, two reactants, three products, continuous scheme
    SBO_0000108 = "SBO_0000108"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000108"
    )

    # mass action rate law for third order reversible reactions
    SBO_0000109 = "SBO_0000109"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_REVERSIBLE_REACTIONS = "SBO_0000109"

    # mass action rate law for third order forward, reversible reactions, two reactants
    SBO_0000110 = "SBO_0000110"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__REVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000110"
    )

    # mass action rate law for third order forward, zeroth order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000111 = "SBO_0000111"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000111"
    )

    # mass action rate law for third order forward, first order reverse, reversible reactions, two reactants, continuous scheme
    SBO_0000112 = "SBO_0000112"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000112"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, two reactants
    SBO_0000113 = "SBO_0000113"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000113"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000114 = "SBO_0000114"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000114"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000115 = "SBO_0000115"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000115"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants
    SBO_0000116 = "SBO_0000116"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS = (
        "SBO_0000116"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, one product, continuous scheme
    SBO_0000117 = "SBO_0000117"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000117"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, two products, continuous scheme
    SBO_0000118 = "SBO_0000118"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000118"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, two reactants, three products, continuous scheme
    SBO_0000119 = "SBO_0000119"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__TWO_REACTANTS__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000119"
    )

    # mass action rate law for third order forward, reversible reactions, three reactants
    SBO_0000120 = "SBO_0000120"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__REVERSIBLE_REACTIONS__THREE_REACTANTS = (
        "SBO_0000120"
    )

    # mass action rate law for third order forward, zeroth order reverse, reversible reactions, three reactants, continuous scheme
    SBO_0000121 = "SBO_0000121"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000121"
    )

    # mass action rate law for third order forward, first order reverse, reversible reactions, three reactants, continuous scheme
    SBO_0000122 = "SBO_0000122"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__CONTINUOUS_SCHEME = (
        "SBO_0000122"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, three reactants
    SBO_0000123 = "SBO_0000123"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS = (
        "SBO_0000123"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, three reactants, one product, continuous scheme
    SBO_0000124 = "SBO_0000124"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000124"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, three reactants, two products, continuous scheme
    SBO_0000125 = "SBO_0000125"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000125"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants
    SBO_0000126 = "SBO_0000126"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS = (
        "SBO_0000126"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, one product, continuous scheme
    SBO_0000127 = "SBO_0000127"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000127"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, two products, continuous scheme
    SBO_0000128 = "SBO_0000128"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000128"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, three reactants, three products, continuous scheme
    SBO_0000129 = "SBO_0000129"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__THREE_REACTANTS__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000129"
    )

    # mass action rate law for third order forward, reversible reactions, one reactant
    SBO_0000130 = "SBO_0000130"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000130"
    )

    # mass action rate law for third order forward, zeroth order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000131 = "SBO_0000131"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__ZEROTH_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = (
        "SBO_0000131"
    )

    # mass action rate law for third order forward, first order reverse, reversible reactions, one reactant, continuous scheme
    SBO_0000132 = "SBO_0000132"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__FIRST_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__CONTINUOUS_SCHEME = (
        "SBO_0000132"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, one reactant
    SBO_0000133 = "SBO_0000133"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000133"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000134 = "SBO_0000134"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000134"
    )

    # mass action rate law for third order forward, second order reverse, reversible reactions, one reactant, two products, continuous scheme
    SBO_0000135 = "SBO_0000135"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__SECOND_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000135"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant
    SBO_0000136 = "SBO_0000136"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT = (
        "SBO_0000136"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, one product, continuous scheme
    SBO_0000137 = "SBO_0000137"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__ONE_PRODUCT__CONTINUOUS_SCHEME = (
        "SBO_0000137"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, two products, continuous scheme
    SBO_0000138 = "SBO_0000138"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__TWO_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000138"
    )

    # mass action rate law for third order forward, third order reverse, reversible reactions, one reactant, three products, continuous scheme
    SBO_0000139 = "SBO_0000139"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_FORWARD__THIRD_ORDER_REVERSE__REVERSIBLE_REACTIONS__ONE_REACTANT__THREE_PRODUCTS__CONTINUOUS_SCHEME = (
        "SBO_0000139"
    )

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
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__DISCRETE_SCHEME = (
        "SBO_0000142"
    )

    # mass action rate law for second order irreversible reactions, two reactants, discrete scheme
    SBO_0000143 = "SBO_0000143"
    MASS_ACTION_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__DISCRETE_SCHEME = (
        "SBO_0000143"
    )

    # mass action rate law for third order irreversible reactions, one reactant, discrete scheme
    SBO_0000144 = "SBO_0000144"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__DISCRETE_SCHEME = (
        "SBO_0000144"
    )

    # mass action rate law for third order irreversible reactions, two reactants, discrete scheme
    SBO_0000145 = "SBO_0000145"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__TWO_REACTANTS__DISCRETE_SCHEME = (
        "SBO_0000145"
    )

    # mass action rate law for third order irreversible reactions, three reactants, discrete scheme
    SBO_0000146 = "SBO_0000146"
    MASS_ACTION_RATE_LAW_FOR_THIRD_ORDER_IRREVERSIBLE_REACTIONS__THREE_REACTANTS__DISCRETE_SCHEME = (
        "SBO_0000146"
    )

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
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_REACTANT_ENZYMES = (
        "SBO_0000150"
    )

    # enzymatic rate law for irreversible non-modulated non-interacting bireactant enzymes
    SBO_0000151 = "SBO_0000151"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_BIREACTANT_ENZYMES = (
        "SBO_0000151"
    )

    # enzymatic rate law for irreversible non-modulated non-interacting trireactant enzymes
    SBO_0000152 = "SBO_0000152"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_NON_MODULATED_NON_INTERACTING_TRIREACTANT_ENZYMES = (
        "SBO_0000152"
    )

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
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_ONE_INHIBITOR = (
        "SBO_0000260"
    )

    # inhibitory constant
    SBO_0000261 = "SBO_0000261"
    INHIBITORY_CONSTANT = "SBO_0000261"

    # enzymatic rate law for simple uncompetitive inhibition of irreversible unireactant enzymes
    SBO_0000262 = "SBO_0000262"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_UNCOMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES = (
        "SBO_0000262"
    )

    # relative equilibrium constant
    SBO_0000263 = "SBO_0000263"
    RELATIVE_EQUILIBRIUM_CONSTANT = "SBO_0000263"

    # relative inhibition constant
    SBO_0000264 = "SBO_0000264"
    RELATIVE_INHIBITION_CONSTANT = "SBO_0000264"

    # enzymatic rate law for simple mixed-type inhibition of irreversible unireactant enzymes
    SBO_0000265 = "SBO_0000265"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_MIXED_TYPE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES = (
        "SBO_0000265"
    )

    # enzymatic rate law for simple irreversible non-competitive inhibition of unireactant enzymes
    SBO_0000266 = "SBO_0000266"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_IRREVERSIBLE_NON_COMPETITIVE_INHIBITION_OF_UNIREACTANT_ENZYMES = (
        "SBO_0000266"
    )

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by one inhibitor
    SBO_0000267 = "SBO_0000267"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_ONE_INHIBITOR = (
        "SBO_0000267"
    )

    # enzymatic rate law
    SBO_0000268 = "SBO_0000268"
    ENZYMATIC_RATE_LAW = "SBO_0000268"

    # enzymatic rate law for unireactant enzymes
    SBO_0000269 = "SBO_0000269"
    ENZYMATIC_RATE_LAW_FOR_UNIREACTANT_ENZYMES = "SBO_0000269"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by exclusive inhibitors
    SBO_0000270 = "SBO_0000270"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_EXCLUSIVE_INHIBITORS = (
        "SBO_0000270"
    )

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by two exclusive inhibitors
    SBO_0000271 = "SBO_0000271"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_EXCLUSIVE_INHIBITORS = (
        "SBO_0000271"
    )

    # number of inhibitors
    SBO_0000272 = "SBO_0000272"
    NUMBER_OF_INHIBITORS = "SBO_0000272"

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzymes by non-exclusive non-cooperative inhibitors
    SBO_0000273 = "SBO_0000273"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_NON_EXCLUSIVE_NON_COOPERATIVE_INHIBITORS = (
        "SBO_0000273"
    )

    # enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by two non-exclusive, non-cooperative inhibitors
    SBO_0000274 = "SBO_0000274"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_NON_EXCLUSIVE__NON_COOPERATIVE_INHIBITORS = (
        "SBO_0000274"
    )

    # enzymatic rate law for mixed-type inhibition of irreversible enzymes by mutually exclusive inhibitors
    SBO_0000275 = "SBO_0000275"
    ENZYMATIC_RATE_LAW_FOR_MIXED_TYPE_INHIBITION_OF_IRREVERSIBLE_ENZYMES_BY_MUTUALLY_EXCLUSIVE_INHIBITORS = (
        "SBO_0000275"
    )

    # enzymatic rate law for mixed-type inhibition of irreversible unireactant enzymes by two inhibitors
    SBO_0000276 = "SBO_0000276"
    ENZYMATIC_RATE_LAW_FOR_MIXED_TYPE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_INHIBITORS = (
        "SBO_0000276"
    )

    # enzymatic rate law for non-competitive inhibition of irreversible unireactant enzymes by two exclusively binding inhibitors
    SBO_0000277 = "SBO_0000277"
    ENZYMATIC_RATE_LAW_FOR_NON_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_EXCLUSIVELY_BINDING_INHIBITORS = (
        "SBO_0000277"
    )

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
    ENZYMATIC_RATE_LAW_FOR_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_COMPETING_SUBSTRATES = (
        "SBO_0000378"
    )

    # enzymatic rate law for simple competitive inhibition of irreversible unireactant enzymes by two non-exclusive inhibitors
    SBO_0000379 = "SBO_0000379"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_TWO_NON_EXCLUSIVE_INHIBITORS = (
        "SBO_0000379"
    )

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
    ENZYMATIC_RATE_LAW_FOR_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_SINGLE_COMPETING_SUBSTRATE = (
        "SBO_0000386"
    )

    # enzymatic rate law for competitive inhibition of irreversible unireactant enzyme by product
    SBO_0000387 = "SBO_0000387"
    ENZYMATIC_RATE_LAW_FOR_COMPETITIVE_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYME_BY_PRODUCT = (
        "SBO_0000387"
    )

    # enzymatic rate law for inhibition of irreversible unireactant enzymes by single competing substrate with product inhibition
    SBO_0000388 = "SBO_0000388"
    ENZYMATIC_RATE_LAW_FOR_INHIBITION_OF_IRREVERSIBLE_UNIREACTANT_ENZYMES_BY_SINGLE_COMPETING_SUBSTRATE_WITH_PRODUCT_INHIBITION = (
        "SBO_0000388"
    )

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
    ENZYMATIC_RATE_LAW_FOR_MIXED_TYPE_INHIBITION_OF_REVERSIBLE_ENZYMES_BY_MUTUALLY_EXCLUSIVE_INHIBITORS = (
        "SBO_0000441"
    )

    # enzymatic rate law for simple reversible non-competitive inhibition of unireactant enzymes
    SBO_0000442 = "SBO_0000442"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_REVERSIBLE_NON_COMPETITIVE_INHIBITION_OF_UNIREACTANT_ENZYMES = (
        "SBO_0000442"
    )

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
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_EMPIRICAL_ALLOSTERIC_INHIBITION_BY_ONE_INHIBITOR = (
        "SBO_0000453"
    )

    # enzymatic rate law for reversible substrate inhibition
    SBO_0000454 = "SBO_0000454"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_SUBSTRATE_INHIBITION = "SBO_0000454"

    # enzymatic rate law for irreversible substrate inhibition
    SBO_0000455 = "SBO_0000455"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_SUBSTRATE_INHIBITION = "SBO_0000455"

    # enzymatic rate law for reversible unireactant enzyme with a single hyperbolic modulator
    SBO_0000456 = "SBO_0000456"
    ENZYMATIC_RATE_LAW_FOR_REVERSIBLE_UNIREACTANT_ENZYME_WITH_A_SINGLE_HYPERBOLIC_MODULATOR = (
        "SBO_0000456"
    )

    # enzymatic rate law for irreversible unireactant enzyme with a single hyperbolic modulator
    SBO_0000457 = "SBO_0000457"
    ENZYMATIC_RATE_LAW_FOR_IRREVERSIBLE_UNIREACTANT_ENZYME_WITH_A_SINGLE_HYPERBOLIC_MODULATOR = (
        "SBO_0000457"
    )

    # enzymatic rate law for simple uncompetitive inhibition of reversible unireactant enzymes
    SBO_0000458 = "SBO_0000458"
    ENZYMATIC_RATE_LAW_FOR_SIMPLE_UNCOMPETITIVE_INHIBITION_OF_REVERSIBLE_UNIREACTANT_ENZYMES = (
        "SBO_0000458"
    )

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
    GENETIC_INTERACTION = "SBO_0000499"

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
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS__SINGLE_ESSENTIAL_STIMULATOR__CONTINUOUS_SCHEME = (
        "SBO_0000560"
    )

    # mass action rate law for first order irreversible reactions, single essential stimulator, discrete scheme
    SBO_0000561 = "SBO_0000561"
    MASS_ACTION_RATE_LAW_FOR_FIRST_ORDER_IRREVERSIBLE_REACTIONS__SINGLE_ESSENTIAL_STIMULATOR__DISCRETE_SCHEME = (
        "SBO_0000561"
    )

    # mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator
    SBO_0000562 = "SBO_0000562"
    MASS_ACTION_LIKE_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__ONE_ESSENTIAL_STIMULATOR = (
        "SBO_0000562"
    )

    # mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator, continuous scheme
    SBO_0000563 = "SBO_0000563"
    MASS_ACTION_LIKE_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__ONE_ESSENTIAL_STIMULATOR__CONTINUOUS_SCHEME = (
        "SBO_0000563"
    )

    # mass action like rate law for second order irreversible reactions, one reactant, one essential stimulator, discrete scheme
    SBO_0000564 = "SBO_0000564"
    MASS_ACTION_LIKE_RATE_LAW_FOR_SECOND_ORDER_IRREVERSIBLE_REACTIONS__ONE_REACTANT__ONE_ESSENTIAL_STIMULATOR__DISCRETE_SCHEME = (
        "SBO_0000564"
    )

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
    PROMOTER = "SBO_0000598"

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


__all__ = [
    "SBO",
]
