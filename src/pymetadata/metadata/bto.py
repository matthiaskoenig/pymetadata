"""BTO ontology."""

from enum import Enum


class BTO(str, Enum):
    """Enum for BTO ontology."""

    # tissues, cell types and enzyme sources
    BTO_0000000 = "BTO_0000000"
    TISSUES__CELL_TYPES_AND_ENZYME_SOURCES = "BTO_0000000"

    # culture condition:-induced cell
    BTO_0000001 = "BTO_0000001"
    CULTURE_CONDITION__INDUCED_CELL = "BTO_0000001"

    # culture condition:1,4-dichlorobenzene-grown cell
    BTO_0000002 = "BTO_0000002"
    CULTURE_CONDITION_1_4_DICHLOROBENZENE_GROWN_CELL = "BTO_0000002"

    # intestinal cell line
    BTO_0000003 = "BTO_0000003"
    INTESTINAL_CELL_LINE = "BTO_0000003"

    # culture condition:2,5-dihydroxybenzoate-grown cell
    BTO_0000004 = "BTO_0000004"
    CULTURE_CONDITION_2_5_DIHYDROXYBENZOATE_GROWN_CELL = "BTO_0000004"

    # culture condition:2-aminobenzenesulfonate-grown cell
    BTO_0000005 = "BTO_0000005"
    CULTURE_CONDITION_2_AMINOBENZENESULFONATE_GROWN_CELL = "BTO_0000005"

    # osteoblastoma cell
    BTO_0000006 = "BTO_0000006"
    OSTEOBLASTOMA_CELL = "BTO_0000006"

    # HEK-293 cell
    BTO_0000007 = "BTO_0000007"
    HEK_293_CELL = "BTO_0000007"

    # culture condition:3-chlorobenzoate-grown cell
    BTO_0000008 = "BTO_0000008"
    CULTURE_CONDITION_3_CHLOROBENZOATE_GROWN_CELL = "BTO_0000008"

    # culture condition:3-hydroxybenzoate-grown cell
    BTO_0000009 = "BTO_0000009"
    CULTURE_CONDITION_3_HYDROXYBENZOATE_GROWN_CELL = "BTO_0000009"

    # culture condition:3-methylcrotonoyl-CoA-grown cell
    BTO_0000010 = "BTO_0000010"
    CULTURE_CONDITION_3_METHYLCROTONOYL_COA_GROWN_CELL = "BTO_0000010"

    # 3T3-L1 cell
    BTO_0000011 = "BTO_0000011"
    _3T3_L1_CELL = "BTO_0000011"

    # culture condition:4-(methoxymethyl)phenol-grown cell
    BTO_0000012 = "BTO_0000012"
    CULTURE_CONDITION_4__METHOXYMETHYL_PHENOL_GROWN_CELL = "BTO_0000012"

    # culture condition:4-chlorophenol-grown cell
    BTO_0000013 = "BTO_0000013"
    CULTURE_CONDITION_4_CHLOROPHENOL_GROWN_CELL = "BTO_0000013"

    # culture condition:4-hydroxybenzoate-grown cell
    BTO_0000014 = "BTO_0000014"
    CULTURE_CONDITION_4_HYDROXYBENZOATE_GROWN_CELL = "BTO_0000014"

    # culture condition:4-methylmuconolactone-grown cell
    BTO_0000015 = "BTO_0000015"
    CULTURE_CONDITION_4_METHYLMUCONOLACTONE_GROWN_CELL = "BTO_0000015"

    # A-172 cell
    BTO_0000016 = "BTO_0000016"
    A_172_CELL = "BTO_0000016"

    # A-431 cell
    BTO_0000017 = "BTO_0000017"
    A_431_CELL = "BTO_0000017"

    # A-549 cell
    BTO_0000018 = "BTO_0000018"
    A_549_CELL = "BTO_0000018"

    # A7r5 cell
    BTO_0000019 = "BTO_0000019"
    A7R5_CELL = "BTO_0000019"

    # abdomen
    BTO_0000020 = "BTO_0000020"
    ABDOMEN = "BTO_0000020"

    # head muscle
    BTO_0000021 = "BTO_0000021"
    HEAD_MUSCLE = "BTO_0000021"

    # abdominal ganglion
    BTO_0000022 = "BTO_0000022"
    ABDOMINAL_GANGLION = "BTO_0000022"

    # pectoral muscle
    BTO_0000023 = "BTO_0000023"
    PECTORAL_MUSCLE = "BTO_0000023"

    # abomasum
    BTO_0000024 = "BTO_0000024"
    ABOMASUM = "BTO_0000024"

    # amniotic cavity
    BTO_0000025 = "BTO_0000025"
    AMNIOTIC_CAVITY = "BTO_0000025"

    # culture condition:galactose-grown cell
    BTO_0000026 = "BTO_0000026"
    CULTURE_CONDITION_GALACTOSE_GROWN_CELL = "BTO_0000026"

    # achene
    BTO_0000027 = "BTO_0000027"
    ACHENE = "BTO_0000027"

    # pancreatic acinar cell
    BTO_0000028 = "BTO_0000028"
    PANCREATIC_ACINAR_CELL = "BTO_0000028"

    # adductor longus
    BTO_0000029 = "BTO_0000029"
    ADDUCTOR_LONGUS = "BTO_0000029"

    # adductor
    BTO_0000030 = "BTO_0000030"
    ADDUCTOR = "BTO_0000030"

    # fruit peduncle
    BTO_0000031 = "BTO_0000031"
    FRUIT_PEDUNCLE = "BTO_0000031"

    # colonic adenocarcinoma cell
    BTO_0000032 = "BTO_0000032"
    COLONIC_ADENOCARCINOMA_CELL = "BTO_0000032"

    # SW-403 cell
    BTO_0000033 = "BTO_0000033"
    SW_403_CELL = "BTO_0000033"

    # apical meristem
    BTO_0000034 = "BTO_0000034"
    APICAL_MERISTEM = "BTO_0000034"

    # colorectal adenocarcinoma cell
    BTO_0000035 = "BTO_0000035"
    COLORECTAL_ADENOCARCINOMA_CELL = "BTO_0000035"

    # gastric adenocarcinoma cell
    BTO_0000036 = "BTO_0000036"
    GASTRIC_ADENOCARCINOMA_CELL = "BTO_0000036"

    # renal cell carcinoma cell
    BTO_0000037 = "BTO_0000037"
    RENAL_CELL_CARCINOMA_CELL = "BTO_0000037"

    # SW-480 cell
    BTO_0000038 = "BTO_0000038"
    SW_480_CELL = "BTO_0000038"

    # root cap
    BTO_0000039 = "BTO_0000039"
    ROOT_CAP = "BTO_0000039"

    # adenohypophysis
    BTO_0000040 = "BTO_0000040"
    ADENOHYPOPHYSIS = "BTO_0000040"

    # medulla oblongata
    BTO_0000041 = "BTO_0000041"
    MEDULLA_OBLONGATA = "BTO_0000041"

    # animal
    BTO_0000042 = "BTO_0000042"
    ANIMAL = "BTO_0000042"

    # cerebellar cortex
    BTO_0000043 = "BTO_0000043"
    CEREBELLAR_CORTEX = "BTO_0000043"

    # tear gland
    BTO_0000044 = "BTO_0000044"
    TEAR_GLAND = "BTO_0000044"

    # adrenal cortex
    BTO_0000045 = "BTO_0000045"
    ADRENAL_CORTEX = "BTO_0000045"

    # Y-1 cell
    BTO_0000046 = "BTO_0000046"
    Y_1_CELL = "BTO_0000046"

    # adrenal gland
    BTO_0000047 = "BTO_0000047"
    ADRENAL_GLAND = "BTO_0000047"

    # zona glomerulosa
    BTO_0000048 = "BTO_0000048"
    ZONA_GLOMERULOSA = "BTO_0000048"

    # adrenal medulla
    BTO_0000049 = "BTO_0000049"
    ADRENAL_MEDULLA = "BTO_0000049"

    # zona fasciculata
    BTO_0000050 = "BTO_0000050"
    ZONA_FASCICULATA = "BTO_0000050"

    # tendon sheath
    BTO_0000051 = "BTO_0000051"
    TENDON_SHEATH = "BTO_0000051"

    # stoma
    BTO_0000052 = "BTO_0000052"
    STOMA = "BTO_0000052"

    # albedo
    BTO_0000053 = "BTO_0000053"
    ALBEDO = "BTO_0000053"

    # albumen gland
    BTO_0000054 = "BTO_0000054"
    ALBUMEN_GLAND = "BTO_0000054"

    # pars recta
    BTO_0000055 = "BTO_0000055"
    PARS_RECTA = "BTO_0000055"

    # zona reticulata
    BTO_0000056 = "BTO_0000056"
    ZONA_RETICULATA = "BTO_0000056"

    # aleurone layer
    BTO_0000057 = "BTO_0000057"
    ALEURONE_LAYER = "BTO_0000057"

    # alimentary canal
    BTO_0000058 = "BTO_0000058"
    ALIMENTARY_CANAL = "BTO_0000058"

    # renal epithelium
    BTO_0000059 = "BTO_0000059"
    RENAL_EPITHELIUM = "BTO_0000059"

    # alveolus
    BTO_0000060 = "BTO_0000060"
    ALVEOLUS = "BTO_0000060"

    # alveolar sac
    BTO_0000061 = "BTO_0000061"
    ALVEOLAR_SAC = "BTO_0000061"

    # amastigote
    BTO_0000062 = "BTO_0000062"
    AMASTIGOTE = "BTO_0000062"

    # culture condition:ammonium malate-grown cell
    BTO_0000063 = "BTO_0000063"
    CULTURE_CONDITION_AMMONIUM_MALATE_GROWN_CELL = "BTO_0000063"

    # amniochorion
    BTO_0000064 = "BTO_0000064"
    AMNIOCHORION = "BTO_0000064"

    # amnion
    BTO_0000065 = "BTO_0000065"
    AMNION = "BTO_0000065"

    # amniocyte
    BTO_0000066 = "BTO_0000066"
    AMNIOCYTE = "BTO_0000066"

    # kidney cell line
    BTO_0000067 = "BTO_0000067"
    KIDNEY_CELL_LINE = "BTO_0000067"

    # amniotic fluid
    BTO_0000068 = "BTO_0000068"
    AMNIOTIC_FLUID = "BTO_0000068"

    # WISH cell
    BTO_0000069 = "BTO_0000069"
    WISH_CELL = "BTO_0000069"

    # fungal cell line
    BTO_0000070 = "BTO_0000070"
    FUNGAL_CELL_LINE = "BTO_0000070"

    # amoebocyte
    BTO_0000071 = "BTO_0000071"
    AMOEBOCYTE = "BTO_0000071"

    # carpel
    BTO_0000072 = "BTO_0000072"
    CARPEL = "BTO_0000072"

    # culture condition:aniline-grown cell
    BTO_0000073 = "BTO_0000073"
    CULTURE_CONDITION_ANILINE_GROWN_CELL = "BTO_0000073"

    # antenna
    BTO_0000074 = "BTO_0000074"
    ANTENNA = "BTO_0000074"

    # antennal gland
    BTO_0000075 = "BTO_0000075"
    ANTENNAL_GLAND = "BTO_0000075"

    # anterior midgut
    BTO_0000076 = "BTO_0000076"
    ANTERIOR_MIDGUT = "BTO_0000076"

    # posterior midgut
    BTO_0000077 = "BTO_0000077"
    POSTERIOR_MIDGUT = "BTO_0000077"

    # microglia
    BTO_0000078 = "BTO_0000078"
    MICROGLIA = "BTO_0000078"

    # anther
    BTO_0000079 = "BTO_0000079"
    ANTHER = "BTO_0000079"

    # male reproductive gland
    BTO_0000080 = "BTO_0000080"
    MALE_REPRODUCTIVE_GLAND = "BTO_0000080"

    # reproductive system
    BTO_0000081 = "BTO_0000081"
    REPRODUCTIVE_SYSTEM = "BTO_0000081"

    # male reproductive system
    BTO_0000082 = "BTO_0000082"
    MALE_REPRODUCTIVE_SYSTEM = "BTO_0000082"

    # female reproductive system
    BTO_0000083 = "BTO_0000083"
    FEMALE_REPRODUCTIVE_SYSTEM = "BTO_0000083"

    # vermiform appendix
    BTO_0000084 = "BTO_0000084"
    VERMIFORM_APPENDIX = "BTO_0000084"

    # appressorium
    BTO_0000085 = "BTO_0000085"
    APPRESSORIUM = "BTO_0000085"

    # culture condition:arabinose-grown cell
    BTO_0000086 = "BTO_0000086"
    CULTURE_CONDITION_ARABINOSE_GROWN_CELL = "BTO_0000086"

    # arterial smooth muscle
    BTO_0000087 = "BTO_0000087"
    ARTERIAL_SMOOTH_MUSCLE = "BTO_0000087"

    # cardiovascular system
    BTO_0000088 = "BTO_0000088"
    CARDIOVASCULAR_SYSTEM = "BTO_0000088"

    # blood
    BTO_0000089 = "BTO_0000089"
    BLOOD = "BTO_0000089"

    # ascidian
    BTO_0000090 = "BTO_0000090"
    ASCIDIAN = "BTO_0000090"

    # ascites
    BTO_0000091 = "BTO_0000091"
    ASCITES = "BTO_0000091"

    # trypanosomoid form
    BTO_0000092 = "BTO_0000092"
    TRYPANOSOMOID_FORM = "BTO_0000092"

    # MCF-7 cell
    BTO_0000093 = "BTO_0000093"
    MCF_7_CELL = "BTO_0000093"

    # ascites tumor cell
    BTO_0000094 = "BTO_0000094"
    ASCITES_TUMOR_CELL = "BTO_0000094"

    # F-9 cell
    BTO_0000095 = "BTO_0000095"
    F_9_CELL = "BTO_0000095"

    # urinary bladder cell line
    BTO_0000096 = "BTO_0000096"
    URINARY_BLADDER_CELL_LINE = "BTO_0000096"

    # ascospore
    BTO_0000097 = "BTO_0000097"
    ASCOSPORE = "BTO_0000097"

    # astroblast
    BTO_0000098 = "BTO_0000098"
    ASTROBLAST = "BTO_0000098"

    # astrocyte
    BTO_0000099 = "BTO_0000099"
    ASTROCYTE = "BTO_0000099"

    # astrocytoma cell
    BTO_0000100 = "BTO_0000100"
    ASTROCYTOMA_CELL = "BTO_0000100"

    # astrocytoma cell line
    BTO_0000101 = "BTO_0000101"
    ASTROCYTOMA_CELL_LINE = "BTO_0000101"

    # blood clot
    BTO_0000102 = "BTO_0000102"
    BLOOD_CLOT = "BTO_0000102"

    # Colon 26-L5 cell
    BTO_0000103 = "BTO_0000103"
    COLON_26_L5_CELL = "BTO_0000103"

    # lymphoma cell line
    BTO_0000104 = "BTO_0000104"
    LYMPHOMA_CELL_LINE = "BTO_0000104"

    # upper epidermis
    BTO_0000105 = "BTO_0000105"
    UPPER_EPIDERMIS = "BTO_0000105"

    # cranial ganglion
    BTO_0000106 = "BTO_0000106"
    CRANIAL_GANGLION = "BTO_0000106"

    # B95-8 cell
    BTO_0000107 = "BTO_0000107"
    B95_8_CELL = "BTO_0000107"

    # olfactory epithelium
    BTO_0000108 = "BTO_0000108"
    OLFACTORY_EPITHELIUM = "BTO_0000108"

    # bacteroid
    BTO_0000109 = "BTO_0000109"
    BACTEROID = "BTO_0000109"

    # amniotic cell line
    BTO_0000110 = "BTO_0000110"
    AMNIOTIC_CELL_LINE = "BTO_0000110"

    # BALB/3T12-3 cell
    BTO_0000111 = "BTO_0000111"
    BALB_3T12_3_CELL = "BTO_0000111"

    # sieve cell
    BTO_0000112 = "BTO_0000112"
    SIEVE_CELL = "BTO_0000112"

    # cervical ganglion
    BTO_0000113 = "BTO_0000113"
    CERVICAL_GANGLION = "BTO_0000113"

    # basidiocarp
    BTO_0000114 = "BTO_0000114"
    BASIDIOCARP = "BTO_0000114"

    # BC3H1 cell
    BTO_0000115 = "BTO_0000115"
    BC3H1_CELL = "BTO_0000115"

    # plant epidermis
    BTO_0000116 = "BTO_0000116"
    PLANT_EPIDERMIS = "BTO_0000116"

    # culture condition:benzoate-grown cell
    BTO_0000117 = "BTO_0000117"
    CULTURE_CONDITION_BENZOATE_GROWN_CELL = "BTO_0000117"

    # culture condition:benzoylformate-grown cell
    BTO_0000118 = "BTO_0000118"
    CULTURE_CONDITION_BENZOYLFORMATE_GROWN_CELL = "BTO_0000118"

    # berry
    BTO_0000119 = "BTO_0000119"
    BERRY = "BTO_0000119"

    # BHK-21 cell
    BTO_0000120 = "BTO_0000120"
    BHK_21_CELL = "BTO_0000120"

    # bile
    BTO_0000121 = "BTO_0000121"
    BILE = "BTO_0000121"

    # bile duct
    BTO_0000122 = "BTO_0000122"
    BILE_DUCT = "BTO_0000122"

    # bladder
    BTO_0000123 = "BTO_0000123"
    BLADDER = "BTO_0000123"

    # microspore
    BTO_0000124 = "BTO_0000124"
    MICROSPORE = "BTO_0000124"

    # blast cell
    BTO_0000125 = "BTO_0000125"
    BLAST_CELL = "BTO_0000125"

    # blastoderm
    BTO_0000126 = "BTO_0000126"
    BLASTODERM = "BTO_0000126"

    # blastospore
    BTO_0000127 = "BTO_0000127"
    BLASTOSPORE = "BTO_0000127"

    # blastula
    BTO_0000128 = "BTO_0000128"
    BLASTULA = "BTO_0000128"

    # basophil
    BTO_0000129 = "BTO_0000129"
    BASOPHIL = "BTO_0000129"

    # neutrophil
    BTO_0000130 = "BTO_0000130"
    NEUTROPHIL = "BTO_0000130"

    # blood plasma
    BTO_0000131 = "BTO_0000131"
    BLOOD_PLASMA = "BTO_0000131"

    # blood platelet
    BTO_0000132 = "BTO_0000132"
    BLOOD_PLATELET = "BTO_0000132"

    # blood serum
    BTO_0000133 = "BTO_0000133"
    BLOOD_SERUM = "BTO_0000133"

    # bloodstream form
    BTO_0000134 = "BTO_0000134"
    BLOODSTREAM_FORM = "BTO_0000134"

    # aorta
    BTO_0000135 = "BTO_0000135"
    AORTA = "BTO_0000135"

    # bronchoalveolar system
    BTO_0000136 = "BTO_0000136"
    BRONCHOALVEOLAR_SYSTEM = "BTO_0000136"

    # pulmonary artery endothelium
    BTO_0000137 = "BTO_0000137"
    PULMONARY_ARTERY_ENDOTHELIUM = "BTO_0000137"

    # midbrain
    BTO_0000138 = "BTO_0000138"
    MIDBRAIN = "BTO_0000138"

    # body wall
    BTO_0000139 = "BTO_0000139"
    BODY_WALL = "BTO_0000139"

    # bone
    BTO_0000140 = "BTO_0000140"
    BONE = "BTO_0000140"

    # bone marrow
    BTO_0000141 = "BTO_0000141"
    BONE_MARROW = "BTO_0000141"

    # brain
    BTO_0000142 = "BTO_0000142"
    BRAIN = "BTO_0000142"

    # substantia nigra
    BTO_0000143 = "BTO_0000143"
    SUBSTANTIA_NIGRA = "BTO_0000143"

    # meninx
    BTO_0000144 = "BTO_0000144"
    MENINX = "BTO_0000144"

    # brain myelin
    BTO_0000145 = "BTO_0000145"
    BRAIN_MYELIN = "BTO_0000145"

    # brain stem
    BTO_0000146 = "BTO_0000146"
    BRAIN_STEM = "BTO_0000146"

    # microgametophyte
    BTO_0000147 = "BTO_0000147"
    MICROGAMETOPHYTE = "BTO_0000147"

    # branch
    BTO_0000148 = "BTO_0000148"
    BRANCH = "BTO_0000148"

    # breast
    BTO_0000149 = "BTO_0000149"
    BREAST = "BTO_0000149"

    # breast cancer cell
    BTO_0000150 = "BTO_0000150"
    BREAST_CANCER_CELL = "BTO_0000150"

    # extensor
    BTO_0000151 = "BTO_0000151"
    EXTENSOR = "BTO_0000151"

    # infected cell
    BTO_0000152 = "BTO_0000152"
    INFECTED_CELL = "BTO_0000152"

    # Walker carcinoma 256 cell
    BTO_0000153 = "BTO_0000153"
    WALKER_CARCINOMA_256_CELL = "BTO_0000153"

    # BRL-3A cell
    BTO_0000154 = "BTO_0000154"
    BRL_3A_CELL = "BTO_0000154"

    # bronchoalveolar lavage fluid
    BTO_0000155 = "BTO_0000155"
    BRONCHOALVEOLAR_LAVAGE_FLUID = "BTO_0000155"

    # brown adipose tissue
    BTO_0000156 = "BTO_0000156"
    BROWN_ADIPOSE_TISSUE = "BTO_0000156"

    # aorta thoracica
    BTO_0000157 = "BTO_0000157"
    AORTA_THORACICA = "BTO_0000157"

    # plant bud
    BTO_0000158 = "BTO_0000158"
    PLANT_BUD = "BTO_0000158"

    # bulb
    BTO_0000159 = "BTO_0000159"
    BULB = "BTO_0000159"

    # bundle sheath
    BTO_0000160 = "BTO_0000160"
    BUNDLE_SHEATH = "BTO_0000160"

    # lung fibroblast cell line
    BTO_0000161 = "BTO_0000161"
    LUNG_FIBROBLAST_CELL_LINE = "BTO_0000161"

    # culture condition:butyrate-grown cell
    BTO_0000162 = "BTO_0000162"
    CULTURE_CONDITION_BUTYRATE_GROWN_CELL = "BTO_0000162"

    # corolla
    BTO_0000163 = "BTO_0000163"
    COROLLA = "BTO_0000163"

    # Burkitt lymphoma cell
    BTO_0000164 = "BTO_0000164"
    BURKITT_LYMPHOMA_CELL = "BTO_0000164"

    # C2C12 cell
    BTO_0000165 = "BTO_0000165"
    C2C12_CELL = "BTO_0000165"

    # cecum
    BTO_0000166 = "BTO_0000166"
    CECUM = "BTO_0000166"

    # adenocarcinoma cell line
    BTO_0000167 = "BTO_0000167"
    ADENOCARCINOMA_CELL_LINE = "BTO_0000167"

    # carotid artery
    BTO_0000168 = "BTO_0000168"
    CAROTID_ARTERY = "BTO_0000168"

    # calyx
    BTO_0000169 = "BTO_0000169"
    CALYX = "BTO_0000169"

    # cambium
    BTO_0000170 = "BTO_0000170"
    CAMBIUM = "BTO_0000170"

    # NCI-H226Br cell
    BTO_0000171 = "BTO_0000171"
    NCI_H226BR_CELL = "BTO_0000171"

    # pileus
    BTO_0000172 = "BTO_0000172"
    PILEUS = "BTO_0000172"

    # fruit capsule
    BTO_0000173 = "BTO_0000173"
    FRUIT_CAPSULE = "BTO_0000173"

    # embryonic structure
    BTO_0000174 = "BTO_0000174"
    EMBRYONIC_STRUCTURE = "BTO_0000174"

    # epithalamus
    BTO_0000175 = "BTO_0000175"
    EPITHALAMUS = "BTO_0000175"

    # carcinoma cell
    BTO_0000176 = "BTO_0000176"
    CARCINOMA_CELL = "BTO_0000176"

    # BG-1 cell
    BTO_0000177 = "BTO_0000177"
    BG_1_CELL = "BTO_0000177"

    # adenoma cell
    BTO_0000178 = "BTO_0000178"
    ADENOMA_CELL = "BTO_0000178"

    # Colo-205 cell
    BTO_0000179 = "BTO_0000179"
    COLO_205_CELL = "BTO_0000179"

    # cervical carcinoma cell
    BTO_0000180 = "BTO_0000180"
    CERVICAL_CARCINOMA_CELL = "BTO_0000180"

    # Lewis lung carcinoma cell line
    BTO_0000181 = "BTO_0000181"
    LEWIS_LUNG_CARCINOMA_CELL_LINE = "BTO_0000181"

    # HT-29 cell
    BTO_0000182 = "BTO_0000182"
    HT_29_CELL = "BTO_0000182"

    # pancreatic cell line
    BTO_0000183 = "BTO_0000183"
    PANCREATIC_CELL_LINE = "BTO_0000183"

    # medullary thyroid carcinoma cell
    BTO_0000184 = "BTO_0000184"
    MEDULLARY_THYROID_CARCINOMA_CELL = "BTO_0000184"

    # medullary breast carcinoma cell
    BTO_0000185 = "BTO_0000185"
    MEDULLARY_BREAST_CARCINOMA_CELL = "BTO_0000185"

    # lobular carcinoma cell
    BTO_0000186 = "BTO_0000186"
    LOBULAR_CARCINOMA_CELL = "BTO_0000186"

    # myeloblast
    BTO_0000187 = "BTO_0000187"
    MYELOBLAST = "BTO_0000187"

    # colonic cell line
    BTO_0000188 = "BTO_0000188"
    COLONIC_CELL_LINE = "BTO_0000188"

    # small cell lung cancer cell
    BTO_0000189 = "BTO_0000189"
    SMALL_CELL_LUNG_CANCER_CELL = "BTO_0000189"

    # Ehrlich tumor carcinoma cell
    BTO_0000190 = "BTO_0000190"
    EHRLICH_TUMOR_CARCINOMA_CELL = "BTO_0000190"

    # medullary carcinoma cell
    BTO_0000191 = "BTO_0000191"
    MEDULLARY_CARCINOMA_CELL = "BTO_0000191"

    # nasopharyngeal carcinoma cell
    BTO_0000192 = "BTO_0000192"
    NASOPHARYNGEAL_CARCINOMA_CELL = "BTO_0000192"

    # rectal cancer cell
    BTO_0000193 = "BTO_0000193"
    RECTAL_CANCER_CELL = "BTO_0000193"

    # endometrioid carcinoma cell
    BTO_0000194 = "BTO_0000194"
    ENDOMETRIOID_CARCINOMA_CELL = "BTO_0000194"

    # CACO-2 cell
    BTO_0000195 = "BTO_0000195"
    CACO_2_CELL = "BTO_0000195"

    # thyroid cancer cell
    BTO_0000196 = "BTO_0000196"
    THYROID_CANCER_CELL = "BTO_0000196"

    # carcinosarcoma cell
    BTO_0000197 = "BTO_0000197"
    CARCINOSARCOMA_CELL = "BTO_0000197"

    # cardia
    BTO_0000198 = "BTO_0000198"
    CARDIA = "BTO_0000198"

    # cardiac muscle
    BTO_0000199 = "BTO_0000199"
    CARDIAC_MUSCLE = "BTO_0000199"

    # culture condition:2-chloropropionate-grown cell
    BTO_0000200 = "BTO_0000200"
    CULTURE_CONDITION_2_CHLOROPROPIONATE_GROWN_CELL = "BTO_0000200"

    # pheochromocytoma cell line
    BTO_0000201 = "BTO_0000201"
    PHEOCHROMOCYTOMA_CELL_LINE = "BTO_0000201"

    # sense organ
    BTO_0000202 = "BTO_0000202"
    SENSE_ORGAN = "BTO_0000202"

    # respiratory system
    BTO_0000203 = "BTO_0000203"
    RESPIRATORY_SYSTEM = "BTO_0000203"

    # carotid body
    BTO_0000204 = "BTO_0000204"
    CAROTID_BODY = "BTO_0000204"

    # nerve plexus
    BTO_0000205 = "BTO_0000205"
    NERVE_PLEXUS = "BTO_0000205"

    # cartilage
    BTO_0000206 = "BTO_0000206"
    CARTILAGE = "BTO_0000206"

    # tibial cartilage
    BTO_0000207 = "BTO_0000207"
    TIBIAL_CARTILAGE = "BTO_0000207"

    # caryopsis
    BTO_0000208 = "BTO_0000208"
    CARYOPSIS = "BTO_0000208"

    # corpus epididymis
    BTO_0000209 = "BTO_0000209"
    CORPUS_EPIDIDYMIS = "BTO_0000209"

    # cauda epididymis
    BTO_0000210 = "BTO_0000210"
    CAUDA_EPIDIDYMIS = "BTO_0000210"

    # caudate nucleus
    BTO_0000211 = "BTO_0000211"
    CAUDATE_NUCLEUS = "BTO_0000211"

    # caudate putamen
    BTO_0000212 = "BTO_0000212"
    CAUDATE_PUTAMEN = "BTO_0000212"

    # cecum mucosa
    BTO_0000213 = "BTO_0000213"
    CECUM_MUCOSA = "BTO_0000213"

    # cell culture
    BTO_0000214 = "BTO_0000214"
    CELL_CULTURE = "BTO_0000214"

    # culture condition:galactonate-grown cell
    BTO_0000215 = "BTO_0000215"
    CULTURE_CONDITION_GALACTONATE_GROWN_CELL = "BTO_0000215"

    # culture condition
    BTO_0000216 = "BTO_0000216"
    CULTURE_CONDITION = "BTO_0000216"

    # MH-7777A cell
    BTO_0000217 = "BTO_0000217"
    MH_7777A_CELL = "BTO_0000217"

    # BALB/3T3 cell
    BTO_0000218 = "BTO_0000218"
    BALB_3T3_CELL = "BTO_0000218"

    # plastron
    BTO_0000219 = "BTO_0000219"
    PLASTRON = "BTO_0000219"

    # MH1C1 cell
    BTO_0000220 = "BTO_0000220"
    MH1C1_CELL = "BTO_0000220"

    # cell suspension culture
    BTO_0000221 = "BTO_0000221"
    CELL_SUSPENSION_CULTURE = "BTO_0000221"

    # myoblast
    BTO_0000222 = "BTO_0000222"
    MYOBLAST = "BTO_0000222"

    # teratocarcinoma cell
    BTO_0000223 = "BTO_0000223"
    TERATOCARCINOMA_CELL = "BTO_0000223"

    # liver cell line
    BTO_0000224 = "BTO_0000224"
    LIVER_CELL_LINE = "BTO_0000224"

    # CEM-C1 cell
    BTO_0000225 = "BTO_0000225"
    CEM_C1_CELL = "BTO_0000225"

    # gitter cell
    BTO_0000226 = "BTO_0000226"
    GITTER_CELL = "BTO_0000226"

    # central nervous system
    BTO_0000227 = "BTO_0000227"
    CENTRAL_NERVOUS_SYSTEM = "BTO_0000227"

    # C-1300 cell
    BTO_0000228 = "BTO_0000228"
    C_1300_CELL = "BTO_0000228"

    # centrum semiovale
    BTO_0000229 = "BTO_0000229"
    CENTRUM_SEMIOVALE = "BTO_0000229"

    # subarachnoid space
    BTO_0000230 = "BTO_0000230"
    SUBARACHNOID_SPACE = "BTO_0000230"

    # cerebral hemisphere
    BTO_0000231 = "BTO_0000231"
    CEREBRAL_HEMISPHERE = "BTO_0000231"

    # cerebellum
    BTO_0000232 = "BTO_0000232"
    CEREBELLUM = "BTO_0000232"

    # cerebral cortex
    BTO_0000233 = "BTO_0000233"
    CEREBRAL_CORTEX = "BTO_0000233"

    # vein
    BTO_0000234 = "BTO_0000234"
    VEIN = "BTO_0000234"

    # basal ganglion
    BTO_0000235 = "BTO_0000235"
    BASAL_GANGLION = "BTO_0000235"

    # cerebral white matter
    BTO_0000236 = "BTO_0000236"
    CEREBRAL_WHITE_MATTER = "BTO_0000236"

    # cerebrospinal fluid
    BTO_0000237 = "BTO_0000237"
    CEREBROSPINAL_FLUID = "BTO_0000237"

    # cerebrovascular endothelial cell
    BTO_0000238 = "BTO_0000238"
    CEREBROVASCULAR_ENDOTHELIAL_CELL = "BTO_0000238"

    # telencephalon
    BTO_0000239 = "BTO_0000239"
    TELENCEPHALON = "BTO_0000239"

    # inferior cervical ganglion
    BTO_0000240 = "BTO_0000240"
    INFERIOR_CERVICAL_GANGLION = "BTO_0000240"

    # cervical epithelium
    BTO_0000241 = "BTO_0000241"
    CERVICAL_EPITHELIUM = "BTO_0000241"

    # cervical mucus
    BTO_0000242 = "BTO_0000242"
    CERVICAL_MUCUS = "BTO_0000242"

    # vagina
    BTO_0000243 = "BTO_0000243"
    VAGINA = "BTO_0000243"

    # culture condition:chlorobenzene-induced cell
    BTO_0000244 = "BTO_0000244"
    CULTURE_CONDITION_CHLOROBENZENE_INDUCED_CELL = "BTO_0000244"

    # culture condition:chlorobenzoate-grown cell
    BTO_0000245 = "BTO_0000245"
    CULTURE_CONDITION_CHLOROBENZOATE_GROWN_CELL = "BTO_0000245"

    # CHO cell
    BTO_0000246 = "BTO_0000246"
    CHO_CELL = "BTO_0000246"

    # shoot tip
    BTO_0000247 = "BTO_0000247"
    SHOOT_TIP = "BTO_0000247"

    # chondroclast
    BTO_0000248 = "BTO_0000248"
    CHONDROCLAST = "BTO_0000248"

    # chondrocyte
    BTO_0000249 = "BTO_0000249"
    CHONDROCYTE = "BTO_0000249"

    # chondrosarcoma cell
    BTO_0000250 = "BTO_0000250"
    CHONDROSARCOMA_CELL = "BTO_0000250"

    # chorioallantois
    BTO_0000251 = "BTO_0000251"
    CHORIOALLANTOIS = "BTO_0000251"

    # chorion
    BTO_0000252 = "BTO_0000252"
    CHORION = "BTO_0000252"

    # BEN cell
    BTO_0000253 = "BTO_0000253"
    BEN_CELL = "BTO_0000253"

    # female reproductive gland
    BTO_0000254 = "BTO_0000254"
    FEMALE_REPRODUCTIVE_GLAND = "BTO_0000254"

    # brain cell line
    BTO_0000255 = "BTO_0000255"
    BRAIN_CELL_LINE = "BTO_0000255"

    # myoblast cell line
    BTO_0000256 = "BTO_0000256"
    MYOBLAST_CELL_LINE = "BTO_0000256"

    # uterine cancer cell
    BTO_0000257 = "BTO_0000257"
    UTERINE_CANCER_CELL = "BTO_0000257"

    # choroid plexus
    BTO_0000258 = "BTO_0000258"
    CHOROID_PLEXUS = "BTO_0000258"

    # chromaffin cell
    BTO_0000259 = "BTO_0000259"
    CHROMAFFIN_CELL = "BTO_0000259"

    # ciliary body
    BTO_0000260 = "BTO_0000260"
    CILIARY_BODY = "BTO_0000260"

    # culture condition:mannitol-grown cell
    BTO_0000261 = "BTO_0000261"
    CULTURE_CONDITION_MANNITOL_GROWN_CELL = "BTO_0000261"

    # clove
    BTO_0000262 = "BTO_0000262"
    CLOVE = "BTO_0000262"

    # P-388D1(IL-1) cell
    BTO_0000263 = "BTO_0000263"
    P_388D1_IL_1__CELL = "BTO_0000263"

    # bone marrow cell line
    BTO_0000264 = "BTO_0000264"
    BONE_MARROW_CELL_LINE = "BTO_0000264"

    # coagulating gland
    BTO_0000265 = "BTO_0000265"
    COAGULATING_GLAND = "BTO_0000265"

    # cob
    BTO_0000266 = "BTO_0000266"
    COB = "BTO_0000266"

    # cochlea
    BTO_0000267 = "BTO_0000267"
    COCHLEA = "BTO_0000267"

    # coleoptile
    BTO_0000268 = "BTO_0000268"
    COLEOPTILE = "BTO_0000268"

    # colon
    BTO_0000269 = "BTO_0000269"
    COLON = "BTO_0000269"

    # colon ascendens
    BTO_0000270 = "BTO_0000270"
    COLON_ASCENDENS = "BTO_0000270"

    # colonic mucosa
    BTO_0000271 = "BTO_0000271"
    COLONIC_MUCOSA = "BTO_0000271"

    # colon transversum
    BTO_0000272 = "BTO_0000272"
    COLON_TRANSVERSUM = "BTO_0000272"

    # ink gland
    BTO_0000273 = "BTO_0000273"
    INK_GLAND = "BTO_0000273"

    # apical bud
    BTO_0000274 = "BTO_0000274"
    APICAL_BUD = "BTO_0000274"

    # colonocyte
    BTO_0000275 = "BTO_0000275"
    COLONOCYTE = "BTO_0000275"

    # colostrum
    BTO_0000276 = "BTO_0000276"
    COLOSTRUM = "BTO_0000276"

    # columnella muscle
    BTO_0000277 = "BTO_0000277"
    COLUMNELLA_MUSCLE = "BTO_0000277"

    # commercial preparation
    BTO_0000278 = "BTO_0000278"
    COMMERCIAL_PREPARATION = "BTO_0000278"

    # testicular cancer cell
    BTO_0000279 = "BTO_0000279"
    TESTICULAR_CANCER_CELL = "BTO_0000279"

    # cone
    BTO_0000280 = "BTO_0000280"
    CONE = "BTO_0000280"

    # conidiophore
    BTO_0000281 = "BTO_0000281"
    CONIDIOPHORE = "BTO_0000281"

    # head
    BTO_0000282 = "BTO_0000282"
    HEAD = "BTO_0000282"

    # conidium
    BTO_0000283 = "BTO_0000283"
    CONIDIUM = "BTO_0000283"

    # organism form
    BTO_0000284 = "BTO_0000284"
    ORGANISM_FORM = "BTO_0000284"

    # corm
    BTO_0000285 = "BTO_0000285"
    CORM = "BTO_0000285"

    # cornea
    BTO_0000286 = "BTO_0000286"
    CORNEA = "BTO_0000286"

    # corneal epithelium
    BTO_0000287 = "BTO_0000287"
    CORNEAL_EPITHELIUM = "BTO_0000287"

    # corona
    BTO_0000288 = "BTO_0000288"
    CORONA = "BTO_0000288"

    # cytotoxic T-lymphocyte
    BTO_0000289 = "BTO_0000289"
    CYTOTOXIC_T_LYMPHOCYTE = "BTO_0000289"

    # coronary artery
    BTO_0000290 = "BTO_0000290"
    CORONARY_ARTERY = "BTO_0000290"

    # corpus allatum
    BTO_0000291 = "BTO_0000291"
    CORPUS_ALLATUM = "BTO_0000291"

    # corpus luteum
    BTO_0000292 = "BTO_0000292"
    CORPUS_LUTEUM = "BTO_0000292"

    # occipital lobe
    BTO_0000293 = "BTO_0000293"
    OCCIPITAL_LOBE = "BTO_0000293"

    # dermis
    BTO_0000294 = "BTO_0000294"
    DERMIS = "BTO_0000294"

    # WEHI-3 cell
    BTO_0000295 = "BTO_0000295"
    WEHI_3_CELL = "BTO_0000295"

    # SW-1088 cell
    BTO_0000296 = "BTO_0000296"
    SW_1088_CELL = "BTO_0000296"

    # carcinoma cell line
    BTO_0000297 = "BTO_0000297"
    CARCINOMA_CELL_LINE = "BTO_0000297"

    # COS-7 cell
    BTO_0000298 = "BTO_0000298"
    COS_7_CELL = "BTO_0000298"

    # cotton fibre
    BTO_0000299 = "BTO_0000299"
    COTTON_FIBRE = "BTO_0000299"

    # cotyledon
    BTO_0000300 = "BTO_0000300"
    COTYLEDON = "BTO_0000300"

    # crop
    BTO_0000301 = "BTO_0000301"
    CROP = "BTO_0000301"

    # ring gland
    BTO_0000302 = "BTO_0000302"
    RING_GLAND = "BTO_0000302"

    # crown gall
    BTO_0000303 = "BTO_0000303"
    CROWN_GALL = "BTO_0000303"

    # PANC-1 cell
    BTO_0000304 = "BTO_0000304"
    PANC_1_CELL = "BTO_0000304"

    # crypt
    BTO_0000305 = "BTO_0000305"
    CRYPT = "BTO_0000305"

    # teratocarcinoma cell line
    BTO_0000306 = "BTO_0000306"
    TERATOCARCINOMA_CELL_LINE = "BTO_0000306"

    # crystalline style
    BTO_0000307 = "BTO_0000307"
    CRYSTALLINE_STYLE = "BTO_0000307"

    # cytotoxic T-lymphocyte cell line
    BTO_0000308 = "BTO_0000308"
    CYTOTOXIC_T_LYMPHOCYTE_CELL_LINE = "BTO_0000308"

    # bundle sheath cell
    BTO_0000309 = "BTO_0000309"
    BUNDLE_SHEATH_CELL = "BTO_0000309"

    # protophloem
    BTO_0000310 = "BTO_0000310"
    PROTOPHLOEM = "BTO_0000310"

    # culture filtrate
    BTO_0000311 = "BTO_0000311"
    CULTURE_FILTRATE = "BTO_0000311"

    # motoneuron
    BTO_0000312 = "BTO_0000312"
    MOTONEURON = "BTO_0000312"

    # hypodermis
    BTO_0000313 = "BTO_0000313"
    HYPODERMIS = "BTO_0000313"

    # neuroepithelium
    BTO_0000314 = "BTO_0000314"
    NEUROEPITHELIUM = "BTO_0000314"

    # ectoderm
    BTO_0000315 = "BTO_0000315"
    ECTODERM = "BTO_0000315"

    # culture medium
    BTO_0000316 = "BTO_0000316"
    CULTURE_MEDIUM = "BTO_0000316"

    # caulonema
    BTO_0000317 = "BTO_0000317"
    CAULONEMA = "BTO_0000317"

    # CV-1 cell
    BTO_0000318 = "BTO_0000318"
    CV_1_CELL = "BTO_0000318"

    # culture condition:cyclohexanol-grown cell
    BTO_0000319 = "BTO_0000319"
    CULTURE_CONDITION_CYCLOHEXANOL_GROWN_CELL = "BTO_0000319"

    # cyst
    BTO_0000320 = "BTO_0000320"
    CYST = "BTO_0000320"

    # plant cuticle
    BTO_0000321 = "BTO_0000321"
    PLANT_CUTICLE = "BTO_0000321"

    # cytotrophoblast
    BTO_0000322 = "BTO_0000322"
    CYTOTROPHOBLAST = "BTO_0000322"

    # culture condition:D-mandelate-grown cell
    BTO_0000323 = "BTO_0000323"
    CULTURE_CONDITION_D_MANDELATE_GROWN_CELL = "BTO_0000323"

    # culture condition:D-arabinose-induced cell
    BTO_0000324 = "BTO_0000324"
    CULTURE_CONDITION_D_ARABINOSE_INDUCED_CELL = "BTO_0000324"

    # culture condition:D-galactose-grown cell
    BTO_0000325 = "BTO_0000325"
    CULTURE_CONDITION_D_GALACTOSE_GROWN_CELL = "BTO_0000325"

    # culture condition:D-lyxose-grown cell
    BTO_0000326 = "BTO_0000326"
    CULTURE_CONDITION_D_LYXOSE_GROWN_CELL = "BTO_0000326"

    # culture condition:D-mannose-grown cell
    BTO_0000327 = "BTO_0000327"
    CULTURE_CONDITION_D_MANNOSE_GROWN_CELL = "BTO_0000327"

    # culture condition:D-phenylglycine-grown cell
    BTO_0000328 = "BTO_0000328"
    CULTURE_CONDITION_D_PHENYLGLYCINE_GROWN_CELL = "BTO_0000328"

    # culture condition:D-ribose-grown cell
    BTO_0000329 = "BTO_0000329"
    CULTURE_CONDITION_D_RIBOSE_GROWN_CELL = "BTO_0000329"

    # culture condition:D-ribose-induced cell
    BTO_0000330 = "BTO_0000330"
    CULTURE_CONDITION_D_RIBOSE_INDUCED_CELL = "BTO_0000330"

    # L-929 cell
    BTO_0000331 = "BTO_0000331"
    L_929_CELL = "BTO_0000331"

    # culture condition:dark-grown cell
    BTO_0000332 = "BTO_0000332"
    CULTURE_CONDITION_DARK_GROWN_CELL = "BTO_0000332"

    # renal corpuscle
    BTO_0000333 = "BTO_0000333"
    RENAL_CORPUSCLE = "BTO_0000333"

    # decidua parietalis
    BTO_0000334 = "BTO_0000334"
    DECIDUA_PARIETALIS = "BTO_0000334"

    # deciduoma cell
    BTO_0000335 = "BTO_0000335"
    DECIDUOMA_CELL = "BTO_0000335"

    # caput epididymis
    BTO_0000336 = "BTO_0000336"
    CAPUT_EPIDIDYMIS = "BTO_0000336"

    # dental follicle
    BTO_0000337 = "BTO_0000337"
    DENTAL_FOLLICLE = "BTO_0000337"

    # dental plaque
    BTO_0000338 = "BTO_0000338"
    DENTAL_PLAQUE = "BTO_0000338"

    # dental pulp
    BTO_0000339 = "BTO_0000339"
    DENTAL_PULP = "BTO_0000339"

    # culture condition:deoxyribonucleoside-induced cell
    BTO_0000340 = "BTO_0000340"
    CULTURE_CONDITION_DEOXYRIBONUCLEOSIDE_INDUCED_CELL = "BTO_0000340"

    # diaphragm
    BTO_0000341 = "BTO_0000341"
    DIAPHRAGM = "BTO_0000341"

    # diencephalon
    BTO_0000342 = "BTO_0000342"
    DIENCEPHALON = "BTO_0000342"

    # renal tubule
    BTO_0000343 = "BTO_0000343"
    RENAL_TUBULE = "BTO_0000343"

    # stratum corneum
    BTO_0000344 = "BTO_0000344"
    STRATUM_CORNEUM = "BTO_0000344"

    # digestive gland
    BTO_0000345 = "BTO_0000345"
    DIGESTIVE_GLAND = "BTO_0000345"

    # digestive juice
    BTO_0000346 = "BTO_0000346"
    DIGESTIVE_JUICE = "BTO_0000346"

    # reticulum
    BTO_0000347 = "BTO_0000347"
    RETICULUM = "BTO_0000347"

    # omasum
    BTO_0000348 = "BTO_0000348"
    OMASUM = "BTO_0000348"

    # gut cavity
    BTO_0000349 = "BTO_0000349"
    GUT_CAVITY = "BTO_0000349"

    # culture condition:dimethylamine-grown cell
    BTO_0000350 = "BTO_0000350"
    CULTURE_CONDITION_DIMETHYLAMINE_GROWN_CELL = "BTO_0000350"

    # disc
    BTO_0000351 = "BTO_0000351"
    DISC = "BTO_0000351"

    # culture condition:DL-mandelate-grown cell
    BTO_0000352 = "BTO_0000352"
    CULTURE_CONDITION_DL_MANDELATE_GROWN_CELL = "BTO_0000352"

    # lung cell line
    BTO_0000353 = "BTO_0000353"
    LUNG_CELL_LINE = "BTO_0000353"

    # DON cell
    BTO_0000354 = "BTO_0000354"
    DON_CELL = "BTO_0000354"

    # dormant eye
    BTO_0000355 = "BTO_0000355"
    DORMANT_EYE = "BTO_0000355"

    # breast cancer cell line
    BTO_0000356 = "BTO_0000356"
    BREAST_CANCER_CELL_LINE = "BTO_0000356"

    # nectary
    BTO_0000357 = "BTO_0000357"
    NECTARY = "BTO_0000357"

    # McA-RH7777 cell
    BTO_0000358 = "BTO_0000358"
    MCA_RH7777_CELL = "BTO_0000358"

    # middle cervical ganglion
    BTO_0000359 = "BTO_0000359"
    MIDDLE_CERVICAL_GANGLION = "BTO_0000359"

    # posterior spinal root
    BTO_0000360 = "BTO_0000360"
    POSTERIOR_SPINAL_ROOT = "BTO_0000360"

    # stratum granulosum
    BTO_0000361 = "BTO_0000361"
    STRATUM_GRANULOSUM = "BTO_0000361"

    # urinary bladder cancer cell
    BTO_0000362 = "BTO_0000362"
    URINARY_BLADDER_CANCER_CELL = "BTO_0000362"

    # culture condition:dulcitol-grown cell
    BTO_0000363 = "BTO_0000363"
    CULTURE_CONDITION_DULCITOL_GROWN_CELL = "BTO_0000363"

    # stratum lucidum
    BTO_0000364 = "BTO_0000364"
    STRATUM_LUCIDUM = "BTO_0000364"

    # duodenum
    BTO_0000365 = "BTO_0000365"
    DUODENUM = "BTO_0000365"

    # duodenal juice
    BTO_0000366 = "BTO_0000366"
    DUODENAL_JUICE = "BTO_0000366"

    # duodenal mucosa
    BTO_0000367 = "BTO_0000367"
    DUODENAL_MUCOSA = "BTO_0000367"

    # ear
    BTO_0000368 = "BTO_0000368"
    EAR = "BTO_0000368"

    # egg
    BTO_0000369 = "BTO_0000369"
    EGG = "BTO_0000369"

    # egg white
    BTO_0000370 = "BTO_0000370"
    EGG_WHITE = "BTO_0000370"

    # egg yolk
    BTO_0000371 = "BTO_0000371"
    EGG_YOLK = "BTO_0000371"

    # bone cancer cell
    BTO_0000372 = "BTO_0000372"
    BONE_CANCER_CELL = "BTO_0000372"

    # Ehrlich ascites carcinoma cell
    BTO_0000373 = "BTO_0000373"
    EHRLICH_ASCITES_CARCINOMA_CELL = "BTO_0000373"

    # bone cell line
    BTO_0000374 = "BTO_0000374"
    BONE_CELL_LINE = "BTO_0000374"

    # keratinocyte cell line
    BTO_0000375 = "BTO_0000375"
    KERATINOCYTE_CELL_LINE = "BTO_0000375"

    # electric organ
    BTO_0000376 = "BTO_0000376"
    ELECTRIC_ORGAN = "BTO_0000376"

    # elementary body
    BTO_0000377 = "BTO_0000377"
    ELEMENTARY_BODY = "BTO_0000377"

    # elytron
    BTO_0000378 = "BTO_0000378"
    ELYTRON = "BTO_0000378"

    # embryo
    BTO_0000379 = "BTO_0000379"
    EMBRYO = "BTO_0000379"

    # embryonic axis
    BTO_0000380 = "BTO_0000380"
    EMBRYONIC_AXIS = "BTO_0000380"

    # embryonic blood
    BTO_0000381 = "BTO_0000381"
    EMBRYONIC_BLOOD = "BTO_0000381"

    # Kc cell
    BTO_0000382 = "BTO_0000382"
    KC_CELL = "BTO_0000382"

    # renal cell carcinoma cell line
    BTO_0000383 = "BTO_0000383"
    RENAL_CELL_CARCINOMA_CELL_LINE = "BTO_0000383"

    # emulsin
    BTO_0000384 = "BTO_0000384"
    EMULSIN = "BTO_0000384"

    # bone cancer cell line
    BTO_0000385 = "BTO_0000385"
    BONE_CANCER_CELL_LINE = "BTO_0000385"

    # culture condition:(NH4)2SO4-grown cell
    BTO_0000386 = "BTO_0000386"
    CULTURE_CONDITION__NH4_2SO4_GROWN_CELL = "BTO_0000386"

    # endocardium
    BTO_0000387 = "BTO_0000387"
    ENDOCARDIUM = "BTO_0000387"

    # endodermis
    BTO_0000388 = "BTO_0000388"
    ENDODERMIS = "BTO_0000388"

    # mature ovarian follicle
    BTO_0000389 = "BTO_0000389"
    MATURE_OVARIAN_FOLLICLE = "BTO_0000389"

    # endosperm
    BTO_0000390 = "BTO_0000390"
    ENDOSPERM = "BTO_0000390"

    # DLD-1 cell
    BTO_0000391 = "BTO_0000391"
    DLD_1_CELL = "BTO_0000391"

    # plasma cell
    BTO_0000392 = "BTO_0000392"
    PLASMA_CELL = "BTO_0000392"

    # endothelium
    BTO_0000393 = "BTO_0000393"
    ENDOTHELIUM = "BTO_0000393"

    # aorta endothelium
    BTO_0000394 = "BTO_0000394"
    AORTA_ENDOTHELIUM = "BTO_0000394"

    # alveolar cell
    BTO_0000395 = "BTO_0000395"
    ALVEOLAR_CELL = "BTO_0000395"

    # EAhy 926 cell
    BTO_0000396 = "BTO_0000396"
    EAHY_926_CELL = "BTO_0000396"

    # tooth
    BTO_0000397 = "BTO_0000397"
    TOOTH = "BTO_0000397"

    # enterocyte
    BTO_0000398 = "BTO_0000398"
    ENTEROCYTE = "BTO_0000398"

    # eosinophil
    BTO_0000399 = "BTO_0000399"
    EOSINOPHIL = "BTO_0000399"

    # sarcoma cell line
    BTO_0000400 = "BTO_0000400"
    SARCOMA_CELL_LINE = "BTO_0000400"

    # ependymal epithelium
    BTO_0000401 = "BTO_0000401"
    EPENDYMAL_EPITHELIUM = "BTO_0000401"

    # epicotyl
    BTO_0000402 = "BTO_0000402"
    EPICOTYL = "BTO_0000402"

    # mastocytoma cell line
    BTO_0000403 = "BTO_0000403"
    MASTOCYTOMA_CELL_LINE = "BTO_0000403"

    # epidermis
    BTO_0000404 = "BTO_0000404"
    EPIDERMIS = "BTO_0000404"

    # penis
    BTO_0000405 = "BTO_0000405"
    PENIS = "BTO_0000405"

    # L-428 cell
    BTO_0000406 = "BTO_0000406"
    L_428_CELL = "BTO_0000406"

    # osteosarcoma cell line
    BTO_0000407 = "BTO_0000407"
    OSTEOSARCOMA_CELL_LINE = "BTO_0000407"

    # epididymis
    BTO_0000408 = "BTO_0000408"
    EPIDIDYMIS = "BTO_0000408"

    # epimastigote
    BTO_0000409 = "BTO_0000409"
    EPIMASTIGOTE = "BTO_0000409"

    # immature ovarian follicle
    BTO_0000410 = "BTO_0000410"
    IMMATURE_OVARIAN_FOLLICLE = "BTO_0000410"

    # cervical mucosa
    BTO_0000411 = "BTO_0000411"
    CERVICAL_MUCOSA = "BTO_0000411"

    # epiphyseal growth plate
    BTO_0000412 = "BTO_0000412"
    EPIPHYSEAL_GROWTH_PLATE = "BTO_0000412"

    # epiphysis
    BTO_0000413 = "BTO_0000413"
    EPIPHYSIS = "BTO_0000413"

    # epithelial cell
    BTO_0000414 = "BTO_0000414"
    EPITHELIAL_CELL = "BTO_0000414"

    # epithelioma cell
    BTO_0000415 = "BTO_0000415"
    EPITHELIOMA_CELL = "BTO_0000415"

    # epithelium
    BTO_0000416 = "BTO_0000416"
    EPITHELIUM = "BTO_0000416"

    # bile duct epithelium
    BTO_0000417 = "BTO_0000417"
    BILE_DUCT_EPITHELIUM = "BTO_0000417"

    # neostriatum
    BTO_0000418 = "BTO_0000418"
    NEOSTRIATUM = "BTO_0000418"

    # respiratory epithelium
    BTO_0000419 = "BTO_0000419"
    RESPIRATORY_EPITHELIUM = "BTO_0000419"

    # neck
    BTO_0000420 = "BTO_0000420"
    NECK = "BTO_0000420"

    # connective tissue
    BTO_0000421 = "BTO_0000421"
    CONNECTIVE_TISSUE = "BTO_0000421"

    # vaginal epithelium
    BTO_0000422 = "BTO_0000422"
    VAGINAL_EPITHELIUM = "BTO_0000422"

    # epitrochlearis
    BTO_0000423 = "BTO_0000423"
    EPITROCHLEARIS = "BTO_0000423"

    # erythrocyte
    BTO_0000424 = "BTO_0000424"
    ERYTHROCYTE = "BTO_0000424"

    # erythrocytic stage
    BTO_0000425 = "BTO_0000425"
    ERYTHROCYTIC_STAGE = "BTO_0000425"

    # erythroleukemia cell
    BTO_0000426 = "BTO_0000426"
    ERYTHROLEUKEMIA_CELL = "BTO_0000426"

    # pituitary gland cell line
    BTO_0000427 = "BTO_0000427"
    PITUITARY_GLAND_CELL_LINE = "BTO_0000427"

    # culture condition:ethanol-grown cell
    BTO_0000428 = "BTO_0000428"
    CULTURE_CONDITION_ETHANOL_GROWN_CELL = "BTO_0000428"

    # H69AR cell
    BTO_0000429 = "BTO_0000429"
    H69AR_CELL = "BTO_0000429"

    # EUE cell
    BTO_0000430 = "BTO_0000430"
    EUE_CELL = "BTO_0000430"

    # excretory gland
    BTO_0000431 = "BTO_0000431"
    EXCRETORY_GLAND = "BTO_0000431"

    # corpus cardiacum
    BTO_0000432 = "BTO_0000432"
    CORPUS_CARDIACUM = "BTO_0000432"

    # exocrine acinar cell
    BTO_0000433 = "BTO_0000433"
    EXOCRINE_ACINAR_CELL = "BTO_0000433"

    # exocrine pancreas
    BTO_0000434 = "BTO_0000434"
    EXOCRINE_PANCREAS = "BTO_0000434"

    # stratum spinosum
    BTO_0000435 = "BTO_0000435"
    STRATUM_SPINOSUM = "BTO_0000435"

    # extensor digitorum longus
    BTO_0000436 = "BTO_0000436"
    EXTENSOR_DIGITORUM_LONGUS = "BTO_0000436"

    # culture condition:glycerol-grown cell
    BTO_0000437 = "BTO_0000437"
    CULTURE_CONDITION_GLYCEROL_GROWN_CELL = "BTO_0000437"

    # stratum germinativum
    BTO_0000438 = "BTO_0000438"
    STRATUM_GERMINATIVUM = "BTO_0000438"

    # eye
    BTO_0000439 = "BTO_0000439"
    EYE = "BTO_0000439"

    # feces
    BTO_0000440 = "BTO_0000440"
    FECES = "BTO_0000440"

    # fat body
    BTO_0000442 = "BTO_0000442"
    FAT_BODY = "BTO_0000442"

    # adipocyte
    BTO_0000443 = "BTO_0000443"
    ADIPOCYTE = "BTO_0000443"

    # fat pad
    BTO_0000444 = "BTO_0000444"
    FAT_PAD = "BTO_0000444"

    # cerebral lobe
    BTO_0000445 = "BTO_0000445"
    CEREBRAL_LOBE = "BTO_0000445"

    # FDCP-Mix cl.A4 cell
    BTO_0000446 = "BTO_0000446"
    FDCP_MIX_CL_A4_CELL = "BTO_0000446"

    # feather
    BTO_0000447 = "BTO_0000447"
    FEATHER = "BTO_0000447"

    # fetal serum
    BTO_0000448 = "BTO_0000448"
    FETAL_SERUM = "BTO_0000448"

    # fetus
    BTO_0000449 = "BTO_0000449"
    FETUS = "BTO_0000449"

    # fiber
    BTO_0000450 = "BTO_0000450"
    FIBER = "BTO_0000450"

    # fibrillar flight muscle
    BTO_0000451 = "BTO_0000451"
    FIBRILLAR_FLIGHT_MUSCLE = "BTO_0000451"

    # fibroblast
    BTO_0000452 = "BTO_0000452"
    FIBROBLAST = "BTO_0000452"

    # fibroblast cell line
    BTO_0000453 = "BTO_0000453"
    FIBROBLAST_CELL_LINE = "BTO_0000453"

    # 3T6-Swiss albino cell
    BTO_0000454 = "BTO_0000454"
    _3T6_SWISS_ALBINO_CELL = "BTO_0000454"

    # JTC-15 cell
    BTO_0000455 = "BTO_0000455"
    JTC_15_CELL = "BTO_0000455"

    # plasmacytoma cell line
    BTO_0000456 = "BTO_0000456"
    PLASMACYTOMA_CELL_LINE = "BTO_0000456"

    # CHO-K1 cell
    BTO_0000457 = "BTO_0000457"
    CHO_K1_CELL = "BTO_0000457"

    # WI-38 cell
    BTO_0000458 = "BTO_0000458"
    WI_38_CELL = "BTO_0000458"

    # fibrosarcoma cell
    BTO_0000459 = "BTO_0000459"
    FIBROSARCOMA_CELL = "BTO_0000459"

    # fibrosarcoma cell line
    BTO_0000460 = "BTO_0000460"
    FIBROSARCOMA_CELL_LINE = "BTO_0000460"

    # HSDM1C1 cell
    BTO_0000461 = "BTO_0000461"
    HSDM1C1_CELL = "BTO_0000461"

    # fiddlehead
    BTO_0000462 = "BTO_0000462"
    FIDDLEHEAD = "BTO_0000462"

    # filament
    BTO_0000463 = "BTO_0000463"
    FILAMENT = "BTO_0000463"

    # flagellate
    BTO_0000464 = "BTO_0000464"
    FLAGELLATE = "BTO_0000464"

    # flavedo
    BTO_0000465 = "BTO_0000465"
    FLAVEDO = "BTO_0000465"

    # flexor digitorum longus
    BTO_0000466 = "BTO_0000466"
    FLEXOR_DIGITORUM_LONGUS = "BTO_0000466"

    # flight muscle
    BTO_0000467 = "BTO_0000467"
    FLIGHT_MUSCLE = "BTO_0000467"

    # floret
    BTO_0000468 = "BTO_0000468"
    FLORET = "BTO_0000468"

    # flower
    BTO_0000469 = "BTO_0000469"
    FLOWER = "BTO_0000469"

    # flower bud
    BTO_0000470 = "BTO_0000470"
    FLOWER_BUD = "BTO_0000470"

    # culture condition:fluorene-grown cell
    BTO_0000471 = "BTO_0000471"
    CULTURE_CONDITION_FLUORENE_GROWN_CELL = "BTO_0000471"

    # FM3A cell
    BTO_0000472 = "BTO_0000472"
    FM3A_CELL = "BTO_0000472"

    # fetal membrane
    BTO_0000473 = "BTO_0000473"
    FETAL_MEMBRANE = "BTO_0000473"

    # allantois
    BTO_0000474 = "BTO_0000474"
    ALLANTOIS = "BTO_0000474"

    # ovarian follicle
    BTO_0000475 = "BTO_0000475"
    OVARIAN_FOLLICLE = "BTO_0000475"

    # foot
    BTO_0000476 = "BTO_0000476"
    FOOT = "BTO_0000476"

    # foot muscle
    BTO_0000477 = "BTO_0000477"
    FOOT_MUSCLE = "BTO_0000477"

    # forebrain
    BTO_0000478 = "BTO_0000478"
    FOREBRAIN = "BTO_0000478"

    # forelimb muscle
    BTO_0000479 = "BTO_0000479"
    FORELIMB_MUSCLE = "BTO_0000479"

    # forestomach
    BTO_0000480 = "BTO_0000480"
    FORESTOMACH = "BTO_0000480"

    # culture condition:formate-grown cell
    BTO_0000481 = "BTO_0000481"
    CULTURE_CONDITION_FORMATE_GROWN_CELL = "BTO_0000481"

    # renal distal tubule
    BTO_0000482 = "BTO_0000482"
    RENAL_DISTAL_TUBULE = "BTO_0000482"

    # frond
    BTO_0000483 = "BTO_0000483"
    FROND = "BTO_0000483"

    # frontal lobe
    BTO_0000484 = "BTO_0000484"
    FRONTAL_LOBE = "BTO_0000484"

    # culture condition:fructose-grown cell
    BTO_0000485 = "BTO_0000485"
    CULTURE_CONDITION_FRUCTOSE_GROWN_CELL = "BTO_0000485"

    # fruit
    BTO_0000486 = "BTO_0000486"
    FRUIT = "BTO_0000486"

    # fruit body
    BTO_0000487 = "BTO_0000487"
    FRUIT_BODY = "BTO_0000487"

    # lower epidermis
    BTO_0000488 = "BTO_0000488"
    LOWER_EPIDERMIS = "BTO_0000488"

    # intestinal cancer cell
    BTO_0000489 = "BTO_0000489"
    INTESTINAL_CANCER_CELL = "BTO_0000489"

    # prostate gland ventral lobe
    BTO_0000490 = "BTO_0000490"
    PROSTATE_GLAND_VENTRAL_LOBE = "BTO_0000490"

    # excretion
    BTO_0000491 = "BTO_0000491"
    EXCRETION = "BTO_0000491"

    # MST cell
    BTO_0000492 = "BTO_0000492"
    MST_CELL = "BTO_0000492"

    # gall bladder
    BTO_0000493 = "BTO_0000493"
    GALL_BLADDER = "BTO_0000493"

    # germinal disc
    BTO_0000494 = "BTO_0000494"
    GERMINAL_DISC = "BTO_0000494"

    # gametophyte
    BTO_0000495 = "BTO_0000495"
    GAMETOPHYTE = "BTO_0000495"

    # anterior lobe
    BTO_0000496 = "BTO_0000496"
    ANTERIOR_LOBE = "BTO_0000496"

    # ganglion
    BTO_0000497 = "BTO_0000497"
    GANGLION = "BTO_0000497"

    # gastric cancer cell
    BTO_0000498 = "BTO_0000498"
    GASTRIC_CANCER_CELL = "BTO_0000498"

    # gastric corpus mucosa
    BTO_0000499 = "BTO_0000499"
    GASTRIC_CORPUS_MUCOSA = "BTO_0000499"

    # gastric epithelium
    BTO_0000500 = "BTO_0000500"
    GASTRIC_EPITHELIUM = "BTO_0000500"

    # gastric juice
    BTO_0000501 = "BTO_0000501"
    GASTRIC_JUICE = "BTO_0000501"

    # gastric fundus
    BTO_0000502 = "BTO_0000502"
    GASTRIC_FUNDUS = "BTO_0000502"

    # gastric gland
    BTO_0000503 = "BTO_0000503"
    GASTRIC_GLAND = "BTO_0000503"

    # pancreatic juice
    BTO_0000504 = "BTO_0000504"
    PANCREATIC_JUICE = "BTO_0000504"

    # gastric corpus
    BTO_0000505 = "BTO_0000505"
    GASTRIC_CORPUS = "BTO_0000505"

    # gastrocnemius
    BTO_0000506 = "BTO_0000506"
    GASTROCNEMIUS = "BTO_0000506"

    # foregut
    BTO_0000507 = "BTO_0000507"
    FOREGUT = "BTO_0000507"

    # thorax muscle
    BTO_0000508 = "BTO_0000508"
    THORAX_MUSCLE = "BTO_0000508"

    # gastrodermis
    BTO_0000509 = "BTO_0000509"
    GASTRODERMIS = "BTO_0000509"

    # hindgut
    BTO_0000510 = "BTO_0000510"
    HINDGUT = "BTO_0000510"

    # gastrointestinal tract
    BTO_0000511 = "BTO_0000511"
    GASTROINTESTINAL_TRACT = "BTO_0000511"

    # primary oocyte
    BTO_0000512 = "BTO_0000512"
    PRIMARY_OOCYTE = "BTO_0000512"

    # culture condition:geranoic acid-induced cell
    BTO_0000513 = "BTO_0000513"
    CULTURE_CONDITION_GERANOIC_ACID_INDUCED_CELL = "BTO_0000513"

    # germ
    BTO_0000514 = "BTO_0000514"
    GERM = "BTO_0000514"

    # haustorium
    BTO_0000515 = "BTO_0000515"
    HAUSTORIUM = "BTO_0000515"

    # ghost
    BTO_0000516 = "BTO_0000516"
    GHOST = "BTO_0000516"

    # culture condition:5-methylcytosine-grown cell
    BTO_0000517 = "BTO_0000517"
    CULTURE_CONDITION_5_METHYLCYTOSINE_GROWN_CELL = "BTO_0000517"

    # gill
    BTO_0000518 = "BTO_0000518"
    GILL = "BTO_0000518"

    # gingiva
    BTO_0000519 = "BTO_0000519"
    GINGIVA = "BTO_0000519"

    # gizzard
    BTO_0000520 = "BTO_0000520"
    GIZZARD = "BTO_0000520"

    # gizzard smooth muscle
    BTO_0000521 = "BTO_0000521"
    GIZZARD_SMOOTH_MUSCLE = "BTO_0000521"

    # gland
    BTO_0000522 = "BTO_0000522"
    GLAND = "BTO_0000522"

    # gleba
    BTO_0000523 = "BTO_0000523"
    GLEBA = "BTO_0000523"

    # glia
    BTO_0000524 = "BTO_0000524"
    GLIA = "BTO_0000524"

    # A-875 cell
    BTO_0000525 = "BTO_0000525"
    A_875_CELL = "BTO_0000525"

    # glioma cell
    BTO_0000526 = "BTO_0000526"
    GLIOMA_CELL = "BTO_0000526"

    # glioblastoma cell
    BTO_0000527 = "BTO_0000527"
    GLIOBLASTOMA_CELL = "BTO_0000527"

    # JTC-27 cell
    BTO_0000528 = "BTO_0000528"
    JTC_27_CELL = "BTO_0000528"

    # C6 glioma cell
    BTO_0000529 = "BTO_0000529"
    C6_GLIOMA_CELL = "BTO_0000529"

    # renal glomerulus
    BTO_0000530 = "BTO_0000530"
    RENAL_GLOMERULUS = "BTO_0000530"

    # gluteal muscle
    BTO_0000531 = "BTO_0000531"
    GLUTEAL_MUSCLE = "BTO_0000531"

    # culture condition:glycine-grown cell
    BTO_0000532 = "BTO_0000532"
    CULTURE_CONDITION_GLYCINE_GROWN_CELL = "BTO_0000532"

    # culture condition:dihydroxyacetone-grown cell
    BTO_0000533 = "BTO_0000533"
    CULTURE_CONDITION_DIHYDROXYACETONE_GROWN_CELL = "BTO_0000533"

    # gonad
    BTO_0000534 = "BTO_0000534"
    GONAD = "BTO_0000534"

    # germ cell
    BTO_0000535 = "BTO_0000535"
    GERM_CELL = "BTO_0000535"

    # gracilis muscle
    BTO_0000536 = "BTO_0000536"
    GRACILIS_MUSCLE = "BTO_0000536"

    # nectar
    BTO_0000537 = "BTO_0000537"
    NECTAR = "BTO_0000537"

    # alveolar cell type II
    BTO_0000538 = "BTO_0000538"
    ALVEOLAR_CELL_TYPE_II = "BTO_0000538"

    # granulocyte
    BTO_0000539 = "BTO_0000539"
    GRANULOCYTE = "BTO_0000539"

    # pollen mother cell
    BTO_0000540 = "BTO_0000540"
    POLLEN_MOTHER_CELL = "BTO_0000540"

    # prostate gland dorsolateral lobe
    BTO_0000541 = "BTO_0000541"
    PROSTATE_GLAND_DORSOLATERAL_LOBE = "BTO_0000541"

    # granulosa cell
    BTO_0000542 = "BTO_0000542"
    GRANULOSA_CELL = "BTO_0000542"

    # ground meristem
    BTO_0000543 = "BTO_0000543"
    GROUND_MERISTEM = "BTO_0000543"

    # guard cell
    BTO_0000544 = "BTO_0000544"
    GUARD_CELL = "BTO_0000544"

    # gut
    BTO_0000545 = "BTO_0000545"
    GUT = "BTO_0000545"

    # gut mucosa
    BTO_0000546 = "BTO_0000546"
    GUT_MUCOSA = "BTO_0000546"

    # gut wall
    BTO_0000547 = "BTO_0000547"
    GUT_WALL = "BTO_0000547"

    # prostate gland lobe
    BTO_0000548 = "BTO_0000548"
    PROSTATE_GLAND_LOBE = "BTO_0000548"

    # culture condition:H2/CO2-grown cell
    BTO_0000549 = "BTO_0000549"
    CULTURE_CONDITION_H2_CO2_GROWN_CELL = "BTO_0000549"

    # anal plate
    BTO_0000550 = "BTO_0000550"
    ANAL_PLATE = "BTO_0000550"

    # lung cancer cell
    BTO_0000551 = "BTO_0000551"
    LUNG_CANCER_CELL = "BTO_0000551"

    # HaCaT cell
    BTO_0000552 = "BTO_0000552"
    HACAT_CELL = "BTO_0000552"

    # peripheral blood
    BTO_0000553 = "BTO_0000553"
    PERIPHERAL_BLOOD = "BTO_0000553"

    # hair follicle
    BTO_0000554 = "BTO_0000554"
    HAIR_FOLLICLE = "BTO_0000554"

    # hair root
    BTO_0000555 = "BTO_0000555"
    HAIR_ROOT = "BTO_0000555"

    # germ layer
    BTO_0000556 = "BTO_0000556"
    GERM_LAYER = "BTO_0000556"

    # harderian gland
    BTO_0000557 = "BTO_0000557"
    HARDERIAN_GLAND = "BTO_0000557"

    # hatching gland
    BTO_0000558 = "BTO_0000558"
    HATCHING_GLAND = "BTO_0000558"

    # hatching liquid
    BTO_0000559 = "BTO_0000559"
    HATCHING_LIQUID = "BTO_0000559"

    # haustorial mother cell
    BTO_0000560 = "BTO_0000560"
    HAUSTORIAL_MOTHER_CELL = "BTO_0000560"

    # posterior lobe
    BTO_0000561 = "BTO_0000561"
    POSTERIOR_LOBE = "BTO_0000561"

    # heart
    BTO_0000562 = "BTO_0000562"
    HEART = "BTO_0000562"

    # culture condition:aerobically-grown cell
    BTO_0000563 = "BTO_0000563"
    CULTURE_CONDITION_AEROBICALLY_GROWN_CELL = "BTO_0000563"

    # heart valve
    BTO_0000564 = "BTO_0000564"
    HEART_VALVE = "BTO_0000564"

    # HEL cell
    BTO_0000565 = "BTO_0000565"
    HEL_CELL = "BTO_0000565"

    # pancreatic islet cancer cell
    BTO_0000566 = "BTO_0000566"
    PANCREATIC_ISLET_CANCER_CELL = "BTO_0000566"

    # HeLa cell
    BTO_0000567 = "BTO_0000567"
    HELA_CELL = "BTO_0000567"

    # HeLa-S3 cell
    BTO_0000568 = "BTO_0000568"
    HELA_S3_CELL = "BTO_0000568"

    # exoerythrocytic stage
    BTO_0000569 = "BTO_0000569"
    EXOERYTHROCYTIC_STAGE = "BTO_0000569"

    # hematopoietic system
    BTO_0000570 = "BTO_0000570"
    HEMATOPOIETIC_SYSTEM = "BTO_0000570"

    # hemocyte
    BTO_0000571 = "BTO_0000571"
    HEMOCYTE = "BTO_0000571"

    # hemolymph
    BTO_0000572 = "BTO_0000572"
    HEMOLYMPH = "BTO_0000572"

    # artery
    BTO_0000573 = "BTO_0000573"
    ARTERY = "BTO_0000573"

    # hematopoietic cell
    BTO_0000574 = "BTO_0000574"
    HEMATOPOIETIC_CELL = "BTO_0000574"

    # hepatocyte
    BTO_0000575 = "BTO_0000575"
    HEPATOCYTE = "BTO_0000575"

    # B-16 cell
    BTO_0000576 = "BTO_0000576"
    B_16_CELL = "BTO_0000576"

    # Morris hepatoma 3924A cell
    BTO_0000577 = "BTO_0000577"
    MORRIS_HEPATOMA_3924A_CELL = "BTO_0000577"

    # hepatoma cell line
    BTO_0000578 = "BTO_0000578"
    HEPATOMA_CELL_LINE = "BTO_0000578"

    # eye cancer cell
    BTO_0000579 = "BTO_0000579"
    EYE_CANCER_CELL = "BTO_0000579"

    # blood cancer cell
    BTO_0000580 = "BTO_0000580"
    BLOOD_CANCER_CELL = "BTO_0000580"

    # MOPC-315 cell
    BTO_0000581 = "BTO_0000581"
    MOPC_315_CELL = "BTO_0000581"

    # hepatoma ascites cell line
    BTO_0000582 = "BTO_0000582"
    HEPATOMA_ASCITES_CELL_LINE = "BTO_0000582"

    # bone marrow cancer cell
    BTO_0000583 = "BTO_0000583"
    BONE_MARROW_CANCER_CELL = "BTO_0000583"

    # pancreatic cancer cell
    BTO_0000584 = "BTO_0000584"
    PANCREATIC_CANCER_CELL = "BTO_0000584"

    # intraocular melanoma cell
    BTO_0000585 = "BTO_0000585"
    INTRAOCULAR_MELANOMA_CELL = "BTO_0000585"

    # colonic cancer cell
    BTO_0000586 = "BTO_0000586"
    COLONIC_CANCER_CELL = "BTO_0000586"

    # C 108 cell
    BTO_0000587 = "BTO_0000587"
    C_108_CELL = "BTO_0000587"

    # LL/2 (LLC1) cell
    BTO_0000588 = "BTO_0000588"
    LL_2__LLC1__CELL = "BTO_0000588"

    # primary meristem
    BTO_0000589 = "BTO_0000589"
    PRIMARY_MERISTEM = "BTO_0000589"

    # Alzheimer disease specific cell type
    BTO_0000590 = "BTO_0000590"
    ALZHEIMER_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0000590"

    # N1-S1 cell
    BTO_0000591 = "BTO_0000591"
    N1_S1_CELL = "BTO_0000591"

    # adrenal gland cancer cell
    BTO_0000592 = "BTO_0000592"
    ADRENAL_GLAND_CANCER_CELL = "BTO_0000592"

    # Yoshida AH-130 cell
    BTO_0000593 = "BTO_0000593"
    YOSHIDA_AH_130_CELL = "BTO_0000593"

    # liver cancer cell
    BTO_0000594 = "BTO_0000594"
    LIVER_CANCER_CELL = "BTO_0000594"

    # FDCP-1 cell
    BTO_0000595 = "BTO_0000595"
    FDCP_1_CELL = "BTO_0000595"

    # P-19 cell
    BTO_0000596 = "BTO_0000596"
    P_19_CELL = "BTO_0000596"

    # hepatopancreas
    BTO_0000597 = "BTO_0000597"
    HEPATOPANCREAS = "BTO_0000597"

    # B5/589 cell
    BTO_0000598 = "BTO_0000598"
    B5_589_CELL = "BTO_0000598"

    # Hep-G2 cell
    BTO_0000599 = "BTO_0000599"
    HEP_G2_CELL = "BTO_0000599"

    # heterocyst
    BTO_0000600 = "BTO_0000600"
    HETEROCYST = "BTO_0000600"

    # hippocampus
    BTO_0000601 = "BTO_0000601"
    HIPPOCAMPUS = "BTO_0000601"

    # histiocyte
    BTO_0000602 = "BTO_0000602"
    HISTIOCYTE = "BTO_0000602"

    # pre-B acute lymphoblastic leukemia cell line
    BTO_0000603 = "BTO_0000603"
    PRE_B_ACUTE_LYMPHOBLASTIC_LEUKEMIA_CELL_LINE = "BTO_0000603"

    # adenocarcinoma cell
    BTO_0000604 = "BTO_0000604"
    ADENOCARCINOMA_CELL = "BTO_0000604"

    # honey
    BTO_0000605 = "BTO_0000605"
    HONEY = "BTO_0000605"

    # LK-63 cell
    BTO_0000606 = "BTO_0000606"
    LK_63_CELL = "BTO_0000606"

    # HTC cell
    BTO_0000607 = "BTO_0000607"
    HTC_CELL = "BTO_0000607"

    # hepatoma cell
    BTO_0000608 = "BTO_0000608"
    HEPATOMA_CELL = "BTO_0000608"

    # husk
    BTO_0000609 = "BTO_0000609"
    HUSK = "BTO_0000609"

    # hybridoma cell
    BTO_0000610 = "BTO_0000610"
    HYBRIDOMA_CELL = "BTO_0000610"

    # culture condition:hydroxyproline-induced cell
    BTO_0000611 = "BTO_0000611"
    CULTURE_CONDITION_HYDROXYPROLINE_INDUCED_CELL = "BTO_0000611"

    # hypha
    BTO_0000612 = "BTO_0000612"
    HYPHA = "BTO_0000612"

    # hypocotyl
    BTO_0000613 = "BTO_0000613"
    HYPOCOTYL = "BTO_0000613"

    # hypothalamus
    BTO_0000614 = "BTO_0000614"
    HYPOTHALAMUS = "BTO_0000614"

    # corpus callosum
    BTO_0000615 = "BTO_0000615"
    CORPUS_CALLOSUM = "BTO_0000615"

    # I-cell
    BTO_0000616 = "BTO_0000616"
    I_CELL = "BTO_0000616"

    # ileal carcinoid cell
    BTO_0000617 = "BTO_0000617"
    ILEAL_CARCINOID_CELL = "BTO_0000617"

    # ileal lavage fluid
    BTO_0000618 = "BTO_0000618"
    ILEAL_LAVAGE_FLUID = "BTO_0000618"

    # ileal mucosa
    BTO_0000619 = "BTO_0000619"
    ILEAL_MUCOSA = "BTO_0000619"

    # ileum
    BTO_0000620 = "BTO_0000620"
    ILEUM = "BTO_0000620"

    # iliopsoas muscle
    BTO_0000621 = "BTO_0000621"
    ILIOPSOAS_MUSCLE = "BTO_0000621"

    # culture condition:cyclopentanol-grown cell
    BTO_0000622 = "BTO_0000622"
    CULTURE_CONDITION_CYCLOPENTANOL_GROWN_CELL = "BTO_0000622"

    # culture condition:2-butyne-1,4-diol-grown cell
    BTO_0000623 = "BTO_0000623"
    CULTURE_CONDITION_2_BUTYNE_1_4_DIOL_GROWN_CELL = "BTO_0000623"

    # culture condition:cyclohexane-1,2-diol-induced cell
    BTO_0000624 = "BTO_0000624"
    CULTURE_CONDITION_CYCLOHEXANE_1_2_DIOL_INDUCED_CELL = "BTO_0000624"

    # culture condition:D-xylose-grown cell
    BTO_0000625 = "BTO_0000625"
    CULTURE_CONDITION_D_XYLOSE_GROWN_CELL = "BTO_0000625"

    # culture condition:DL-5-methyltryptophan-grown cell
    BTO_0000626 = "BTO_0000626"
    CULTURE_CONDITION_DL_5_METHYLTRYPTOPHAN_GROWN_CELL = "BTO_0000626"

    # HIT-T15 cell
    BTO_0000627 = "BTO_0000627"
    HIT_T15_CELL = "BTO_0000627"

    # inflorescence
    BTO_0000628 = "BTO_0000628"
    INFLORESCENCE = "BTO_0000628"

    # ink
    BTO_0000629 = "BTO_0000629"
    INK = "BTO_0000629"

    # inner ear
    BTO_0000630 = "BTO_0000630"
    INNER_EAR = "BTO_0000630"

    # culture condition:inositol-deficient-grown cell
    BTO_0000631 = "BTO_0000631"
    CULTURE_CONDITION_INOSITOL_DEFICIENT_GROWN_CELL = "BTO_0000631"

    # insulinoma cell
    BTO_0000632 = "BTO_0000632"
    INSULINOMA_CELL = "BTO_0000632"

    # intestine-407 cell
    BTO_0000633 = "BTO_0000633"
    INTESTINE_407_CELL = "BTO_0000633"

    # integument
    BTO_0000634 = "BTO_0000634"
    INTEGUMENT = "BTO_0000634"

    # yellow bone marrow
    BTO_0000635 = "BTO_0000635"
    YELLOW_BONE_MARROW = "BTO_0000635"

    # internode
    BTO_0000636 = "BTO_0000636"
    INTERNODE = "BTO_0000636"

    # interphotoreceptor matrix
    BTO_0000637 = "BTO_0000637"
    INTERPHOTORECEPTOR_MATRIX = "BTO_0000637"

    # interrenal cell
    BTO_0000638 = "BTO_0000638"
    INTERRENAL_CELL = "BTO_0000638"

    # intersegmental muscle
    BTO_0000639 = "BTO_0000639"
    INTERSEGMENTAL_MUSCLE = "BTO_0000639"

    # intestinal gland
    BTO_0000640 = "BTO_0000640"
    INTESTINAL_GLAND = "BTO_0000640"

    # colon descendens
    BTO_0000641 = "BTO_0000641"
    COLON_DESCENDENS = "BTO_0000641"

    # intestinal mucosa
    BTO_0000642 = "BTO_0000642"
    INTESTINAL_MUCOSA = "BTO_0000642"

    # intestinal muscle
    BTO_0000643 = "BTO_0000643"
    INTESTINAL_MUSCLE = "BTO_0000643"

    # intestinal juice
    BTO_0000644 = "BTO_0000644"
    INTESTINAL_JUICE = "BTO_0000644"

    # colon sigmoideum
    BTO_0000645 = "BTO_0000645"
    COLON_SIGMOIDEUM = "BTO_0000645"

    # left colon
    BTO_0000646 = "BTO_0000646"
    LEFT_COLON = "BTO_0000646"

    # intestinal wall
    BTO_0000647 = "BTO_0000647"
    INTESTINAL_WALL = "BTO_0000647"

    # intestine
    BTO_0000648 = "BTO_0000648"
    INTESTINE = "BTO_0000648"

    # right colon
    BTO_0000649 = "BTO_0000649"
    RIGHT_COLON = "BTO_0000649"

    # endocrine pancreas
    BTO_0000650 = "BTO_0000650"
    ENDOCRINE_PANCREAS = "BTO_0000650"

    # small intestine
    BTO_0000651 = "BTO_0000651"
    SMALL_INTESTINE = "BTO_0000651"

    # culture condition:mannuronate-grown cell
    BTO_0000652 = "BTO_0000652"
    CULTURE_CONDITION_MANNURONATE_GROWN_CELL = "BTO_0000652"

    # iris
    BTO_0000653 = "BTO_0000653"
    IRIS = "BTO_0000653"

    # ciliary muscle
    BTO_0000654 = "BTO_0000654"
    CILIARY_MUSCLE = "BTO_0000654"

    # iris smooth muscle
    BTO_0000655 = "BTO_0000655"
    IRIS_SMOOTH_MUSCLE = "BTO_0000655"

    # iris sphincter muscle
    BTO_0000656 = "BTO_0000656"
    IRIS_SPHINCTER_MUSCLE = "BTO_0000656"

    # jejunum
    BTO_0000657 = "BTO_0000657"
    JEJUNUM = "BTO_0000657"

    # uterine adenocarcinoma cell
    BTO_0000658 = "BTO_0000658"
    UTERINE_ADENOCARCINOMA_CELL = "BTO_0000658"

    # juice
    BTO_0000659 = "BTO_0000659"
    JUICE = "BTO_0000659"

    # mycelial cord
    BTO_0000660 = "BTO_0000660"
    MYCELIAL_CORD = "BTO_0000660"

    # JURKAT cell
    BTO_0000661 = "BTO_0000661"
    JURKAT_CELL = "BTO_0000661"

    # nasopharynx
    BTO_0000662 = "BTO_0000662"
    NASOPHARYNX = "BTO_0000662"

    # juxtaglomerular tumor cell
    BTO_0000663 = "BTO_0000663"
    JUXTAGLOMERULAR_TUMOR_CELL = "BTO_0000663"

    # K-562 cell
    BTO_0000664 = "BTO_0000664"
    K_562_CELL = "BTO_0000664"

    # KB cell
    BTO_0000665 = "BTO_0000665"
    KB_CELL = "BTO_0000665"

    # LoVo cell
    BTO_0000666 = "BTO_0000666"
    LOVO_CELL = "BTO_0000666"

    # keratinocyte
    BTO_0000667 = "BTO_0000667"
    KERATINOCYTE = "BTO_0000667"

    # kernel
    BTO_0000668 = "BTO_0000668"
    KERNEL = "BTO_0000668"

    # embryonic cell line
    BTO_0000669 = "BTO_0000669"
    EMBRYONIC_CELL_LINE = "BTO_0000669"

    # KG-1 cell
    BTO_0000670 = "BTO_0000670"
    KG_1_CELL = "BTO_0000670"

    # kidney
    BTO_0000671 = "BTO_0000671"
    KIDNEY = "BTO_0000671"

    # hindbrain
    BTO_0000672 = "BTO_0000672"
    HINDBRAIN = "BTO_0000672"

    # metencephalon
    BTO_0000673 = "BTO_0000673"
    METENCEPHALON = "BTO_0000673"

    # BHK 165-23 cell
    BTO_0000674 = "BTO_0000674"
    BHK_165_23_CELL = "BTO_0000674"

    # SW-620 cell
    BTO_0000675 = "BTO_0000675"
    SW_620_CELL = "BTO_0000675"

    # fibroadenoma cell
    BTO_0000676 = "BTO_0000676"
    FIBROADENOMA_CELL = "BTO_0000676"

    # plant tumor tissue
    BTO_0000677 = "BTO_0000677"
    PLANT_TUMOR_TISSUE = "BTO_0000677"

    # G-402 cell
    BTO_0000678 = "BTO_0000678"
    G_402_CELL = "BTO_0000678"

    # blood-lymph
    BTO_0000679 = "BTO_0000679"
    BLOOD_LYMPH = "BTO_0000679"

    # kidney cancer cell
    BTO_0000680 = "BTO_0000680"
    KIDNEY_CANCER_CELL = "BTO_0000680"

    # KM-3 cell
    BTO_0000681 = "BTO_0000681"
    KM_3_CELL = "BTO_0000681"

    # Koji culture
    BTO_0000682 = "BTO_0000682"
    KOJI_CULTURE = "BTO_0000682"

    # Krebs ascites cell
    BTO_0000683 = "BTO_0000683"
    KREBS_ASCITES_CELL = "BTO_0000683"

    # Krebs II ascites cell
    BTO_0000684 = "BTO_0000684"
    KREBS_II_ASCITES_CELL = "BTO_0000684"

    # Kupffer cell
    BTO_0000685 = "BTO_0000685"
    KUPFFER_CELL = "BTO_0000685"

    # Kurloff cell
    BTO_0000686 = "BTO_0000686"
    KURLOFF_CELL = "BTO_0000686"

    # culture condition:L-mandelate-grown cell
    BTO_0000687 = "BTO_0000687"
    CULTURE_CONDITION_L_MANDELATE_GROWN_CELL = "BTO_0000687"

    # culture condition:acetate-grown cell
    BTO_0000688 = "BTO_0000688"
    CULTURE_CONDITION_ACETATE_GROWN_CELL = "BTO_0000688"

    # culture condition:L-allo-threonine-grown cell
    BTO_0000689 = "BTO_0000689"
    CULTURE_CONDITION_L_ALLO_THREONINE_GROWN_CELL = "BTO_0000689"

    # brain cancer cell line
    BTO_0000690 = "BTO_0000690"
    BRAIN_CANCER_CELL_LINE = "BTO_0000690"

    # culture condition:L-fucose-induced cell
    BTO_0000691 = "BTO_0000691"
    CULTURE_CONDITION_L_FUCOSE_INDUCED_CELL = "BTO_0000691"

    # culture condition:L-glucose-grown cell
    BTO_0000692 = "BTO_0000692"
    CULTURE_CONDITION_L_GLUCOSE_GROWN_CELL = "BTO_0000692"

    # culture condition:L-lyxose-induced cell
    BTO_0000693 = "BTO_0000693"
    CULTURE_CONDITION_L_LYXOSE_INDUCED_CELL = "BTO_0000693"

    # culture condition:L-phenylalanine-grown cell
    BTO_0000694 = "BTO_0000694"
    CULTURE_CONDITION_L_PHENYLALANINE_GROWN_CELL = "BTO_0000694"

    # culture condition:L-phenylglycine-grown cell
    BTO_0000695 = "BTO_0000695"
    CULTURE_CONDITION_L_PHENYLGLYCINE_GROWN_CELL = "BTO_0000695"

    # culture condition:L-rhamnose-grown cell
    BTO_0000696 = "BTO_0000696"
    CULTURE_CONDITION_L_RHAMNOSE_GROWN_CELL = "BTO_0000696"

    # culture condition:L-rhamnose-induced cell
    BTO_0000697 = "BTO_0000697"
    CULTURE_CONDITION_L_RHAMNOSE_INDUCED_CELL = "BTO_0000697"

    # culture condition:L-ribose-grown cell
    BTO_0000698 = "BTO_0000698"
    CULTURE_CONDITION_L_RIBOSE_GROWN_CELL = "BTO_0000698"

    # culture condition:L-serine-grown cell
    BTO_0000699 = "BTO_0000699"
    CULTURE_CONDITION_L_SERINE_GROWN_CELL = "BTO_0000699"

    # culture condition:L-threonine-grown cell
    BTO_0000700 = "BTO_0000700"
    CULTURE_CONDITION_L_THREONINE_GROWN_CELL = "BTO_0000700"

    # culture condition:L-tyrosine-grown cell
    BTO_0000701 = "BTO_0000701"
    CULTURE_CONDITION_L_TYROSINE_GROWN_CELL = "BTO_0000701"

    # L-1210 cell
    BTO_0000702 = "BTO_0000702"
    L_1210_CELL = "BTO_0000702"

    # lacquer
    BTO_0000703 = "BTO_0000703"
    LACQUER = "BTO_0000703"

    # culture condition:D-lactate-grown cell
    BTO_0000704 = "BTO_0000704"
    CULTURE_CONDITION_D_LACTATE_GROWN_CELL = "BTO_0000704"

    # Langerhans cell
    BTO_0000705 = "BTO_0000705"
    LANGERHANS_CELL = "BTO_0000705"

    # large intestine
    BTO_0000706 = "BTO_0000706"
    LARGE_INTESTINE = "BTO_0000706"

    # larva
    BTO_0000707 = "BTO_0000707"
    LARVA = "BTO_0000707"

    # larval integument
    BTO_0000708 = "BTO_0000708"
    LARVAL_INTEGUMENT = "BTO_0000708"

    # secondary spermatocyte
    BTO_0000709 = "BTO_0000709"
    SECONDARY_SPERMATOCYTE = "BTO_0000709"

    # latex
    BTO_0000710 = "BTO_0000710"
    LATEX = "BTO_0000710"

    # glioma cell line
    BTO_0000711 = "BTO_0000711"
    GLIOMA_CELL_LINE = "BTO_0000711"

    # laticifer
    BTO_0000712 = "BTO_0000712"
    LATICIFER = "BTO_0000712"

    # leaf
    BTO_0000713 = "BTO_0000713"
    LEAF = "BTO_0000713"

    # leaf axil
    BTO_0000714 = "BTO_0000714"
    LEAF_AXIL = "BTO_0000714"

    # leaf base
    BTO_0000715 = "BTO_0000715"
    LEAF_BASE = "BTO_0000715"

    # pancreatic beta cell line
    BTO_0000716 = "BTO_0000716"
    PANCREATIC_BETA_CELL_LINE = "BTO_0000716"

    # pericardium
    BTO_0000717 = "BTO_0000717"
    PERICARDIUM = "BTO_0000717"

    # leaf epidermis
    BTO_0000718 = "BTO_0000718"
    LEAF_EPIDERMIS = "BTO_0000718"

    # leaf lamina
    BTO_0000719 = "BTO_0000719"
    LEAF_LAMINA = "BTO_0000719"

    # plant form
    BTO_0000720 = "BTO_0000720"
    PLANT_FORM = "BTO_0000720"

    # leg
    BTO_0000721 = "BTO_0000721"
    LEG = "BTO_0000721"

    # leg muscle
    BTO_0000722 = "BTO_0000722"
    LEG_MUSCLE = "BTO_0000722"

    # lens
    BTO_0000723 = "BTO_0000723"
    LENS = "BTO_0000723"

    # lens fiber
    BTO_0000724 = "BTO_0000724"
    LENS_FIBER = "BTO_0000724"

    # hematopoietic stem cell
    BTO_0000725 = "BTO_0000725"
    HEMATOPOIETIC_STEM_CELL = "BTO_0000725"

    # RPMI-8226 cell
    BTO_0000726 = "BTO_0000726"
    RPMI_8226_CELL = "BTO_0000726"

    # multiple myeloma cell line
    BTO_0000727 = "BTO_0000727"
    MULTIPLE_MYELOMA_CELL_LINE = "BTO_0000727"

    # Brown Pearce carcinoma cell
    BTO_0000728 = "BTO_0000728"
    BROWN_PEARCE_CARCINOMA_CELL = "BTO_0000728"

    # carcinoid cell
    BTO_0000729 = "BTO_0000729"
    CARCINOID_CELL = "BTO_0000729"

    # endocarp
    BTO_0000730 = "BTO_0000730"
    ENDOCARP = "BTO_0000730"

    # acute lymphoblastic leukemia cell
    BTO_0000731 = "BTO_0000731"
    ACUTE_LYMPHOBLASTIC_LEUKEMIA_CELL = "BTO_0000731"

    # KU-812 cell
    BTO_0000732 = "BTO_0000732"
    KU_812_CELL = "BTO_0000732"

    # exocarp
    BTO_0000733 = "BTO_0000733"
    EXOCARP = "BTO_0000733"

    # myelocyte
    BTO_0000734 = "BTO_0000734"
    MYELOCYTE = "BTO_0000734"

    # sporophyte
    BTO_0000735 = "BTO_0000735"
    SPOROPHYTE = "BTO_0000735"

    # CCRF-CEM cell
    BTO_0000736 = "BTO_0000736"
    CCRF_CEM_CELL = "BTO_0000736"

    # leukemia cell line
    BTO_0000737 = "BTO_0000737"
    LEUKEMIA_CELL_LINE = "BTO_0000737"

    # HL-60 cell
    BTO_0000738 = "BTO_0000738"
    HL_60_CELL = "BTO_0000738"

    # lymphoblastic leukemia cell line
    BTO_0000739 = "BTO_0000739"
    LYMPHOBLASTIC_LEUKEMIA_CELL_LINE = "BTO_0000739"

    # myeloid leukemia cell line
    BTO_0000740 = "BTO_0000740"
    MYELOID_LEUKEMIA_CELL_LINE = "BTO_0000740"

    # lymphocytic leukemia cell line
    BTO_0000741 = "BTO_0000741"
    LYMPHOCYTIC_LEUKEMIA_CELL_LINE = "BTO_0000741"

    # myotome
    BTO_0000742 = "BTO_0000742"
    MYOTOME = "BTO_0000742"

    # pre-B-lymphocyte cell line
    BTO_0000743 = "BTO_0000743"
    PRE_B_LYMPHOCYTE_CELL_LINE = "BTO_0000743"

    # lymphocytic leukemia cell
    BTO_0000744 = "BTO_0000744"
    LYMPHOCYTIC_LEUKEMIA_CELL = "BTO_0000744"

    # Lewis lung carcinoma cell
    BTO_0000745 = "BTO_0000745"
    LEWIS_LUNG_CARCINOMA_CELL = "BTO_0000745"

    # preadipocyte cell line
    BTO_0000746 = "BTO_0000746"
    PREADIPOCYTE_CELL_LINE = "BTO_0000746"

    # sporangiospore
    BTO_0000747 = "BTO_0000747"
    SPORANGIOSPORE = "BTO_0000747"

    # P-388 cell
    BTO_0000748 = "BTO_0000748"
    P_388_CELL = "BTO_0000748"

    # sporozoan form
    BTO_0000749 = "BTO_0000749"
    SPOROZOAN_FORM = "BTO_0000749"

    # plant ovary
    BTO_0000750 = "BTO_0000750"
    PLANT_OVARY = "BTO_0000750"

    # leukocyte
    BTO_0000751 = "BTO_0000751"
    LEUKOCYTE = "BTO_0000751"

    # lymph vessel
    BTO_0000752 = "BTO_0000752"
    LYMPH_VESSEL = "BTO_0000752"

    # lymphoid tissue
    BTO_0000753 = "BTO_0000753"
    LYMPHOID_TISSUE = "BTO_0000753"

    # lewy body
    BTO_0000754 = "BTO_0000754"
    LEWY_BODY = "BTO_0000754"

    # Leydig cell
    BTO_0000755 = "BTO_0000755"
    LEYDIG_CELL = "BTO_0000755"

    # pituitary gland tumor cell line
    BTO_0000756 = "BTO_0000756"
    PITUITARY_GLAND_TUMOR_CELL_LINE = "BTO_0000756"

    # plasmodium
    BTO_0000757 = "BTO_0000757"
    PLASMODIUM = "BTO_0000757"

    # myelencephalon
    BTO_0000758 = "BTO_0000758"
    MYELENCEPHALON = "BTO_0000758"

    # liver
    BTO_0000759 = "BTO_0000759"
    LIVER = "BTO_0000759"

    # LLC-PK1 cell
    BTO_0000760 = "BTO_0000760"
    LLC_PK1_CELL = "BTO_0000760"

    # collecting duct
    BTO_0000761 = "BTO_0000761"
    COLLECTING_DUCT = "BTO_0000761"

    # lung cancer cell line
    BTO_0000762 = "BTO_0000762"
    LUNG_CANCER_CELL_LINE = "BTO_0000762"

    # lung
    BTO_0000763 = "BTO_0000763"
    LUNG = "BTO_0000763"

    # lung fibroblast
    BTO_0000764 = "BTO_0000764"
    LUNG_FIBROBLAST = "BTO_0000764"

    # exocrine gland
    BTO_0000765 = "BTO_0000765"
    EXOCRINE_GLAND = "BTO_0000765"

    # blood vessel endothelium
    BTO_0000766 = "BTO_0000766"
    BLOOD_VESSEL_ENDOTHELIUM = "BTO_0000766"

    # mesenteric lymph node
    BTO_0000767 = "BTO_0000767"
    MESENTERIC_LYMPH_NODE = "BTO_0000767"

    # infundibulum
    BTO_0000768 = "BTO_0000768"
    INFUNDIBULUM = "BTO_0000768"

    # submandibular lymph node
    BTO_0000769 = "BTO_0000769"
    SUBMANDIBULAR_LYMPH_NODE = "BTO_0000769"

    # oligodendroglia
    BTO_0000770 = "BTO_0000770"
    OLIGODENDROGLIA = "BTO_0000770"

    # macroglia
    BTO_0000771 = "BTO_0000771"
    MACROGLIA = "BTO_0000771"

    # lymphoblast
    BTO_0000772 = "BTO_0000772"
    LYMPHOBLAST = "BTO_0000772"

    # lymphoblastoid cell line
    BTO_0000773 = "BTO_0000773"
    LYMPHOBLASTOID_CELL_LINE = "BTO_0000773"

    # lymphoblastoma cell
    BTO_0000774 = "BTO_0000774"
    LYMPHOBLASTOMA_CELL = "BTO_0000774"

    # lymphocyte
    BTO_0000775 = "BTO_0000775"
    LYMPHOCYTE = "BTO_0000775"

    # B-lymphocyte
    BTO_0000776 = "BTO_0000776"
    B_LYMPHOCYTE = "BTO_0000776"

    # adenoid
    BTO_0000777 = "BTO_0000777"
    ADENOID = "BTO_0000777"

    # pulmonary artery
    BTO_0000778 = "BTO_0000778"
    PULMONARY_ARTERY = "BTO_0000778"

    # mesenteric artery
    BTO_0000779 = "BTO_0000779"
    MESENTERIC_ARTERY = "BTO_0000779"

    # alveolar cell type I
    BTO_0000780 = "BTO_0000780"
    ALVEOLAR_CELL_TYPE_I = "BTO_0000780"

    # intestinal epithelium
    BTO_0000781 = "BTO_0000781"
    INTESTINAL_EPITHELIUM = "BTO_0000781"

    # T-lymphocyte
    BTO_0000782 = "BTO_0000782"
    T_LYMPHOCYTE = "BTO_0000782"

    # pancreatic beta cell
    BTO_0000783 = "BTO_0000783"
    PANCREATIC_BETA_CELL = "BTO_0000783"

    # lymph node
    BTO_0000784 = "BTO_0000784"
    LYMPH_NODE = "BTO_0000784"

    # lymphoma cell
    BTO_0000785 = "BTO_0000785"
    LYMPHOMA_CELL = "BTO_0000785"

    # tongue cancer cell line
    BTO_0000786 = "BTO_0000786"
    TONGUE_CANCER_CELL_LINE = "BTO_0000786"

    # gastric cancer cell line
    BTO_0000787 = "BTO_0000787"
    GASTRIC_CANCER_CELL_LINE = "BTO_0000787"

    # 70Z/3 cell
    BTO_0000788 = "BTO_0000788"
    _70Z_3_CELL = "BTO_0000788"

    # CA-46 cell
    BTO_0000789 = "BTO_0000789"
    CA_46_CELL = "BTO_0000789"

    # pharyngeal cancer cell line
    BTO_0000790 = "BTO_0000790"
    PHARYNGEAL_CANCER_CELL_LINE = "BTO_0000790"

    # BW-5147 cell
    BTO_0000791 = "BTO_0000791"
    BW_5147_CELL = "BTO_0000791"

    # urinary bladder carcinoma cell line
    BTO_0000792 = "BTO_0000792"
    URINARY_BLADDER_CARCINOMA_CELL_LINE = "BTO_0000792"

    # SH-SY5Y cell
    BTO_0000793 = "BTO_0000793"
    SH_SY5Y_CELL = "BTO_0000793"

    # pancreatic cancer cell line
    BTO_0000794 = "BTO_0000794"
    PANCREATIC_CANCER_CELL_LINE = "BTO_0000794"

    # L-5178-Y cell
    BTO_0000795 = "BTO_0000795"
    L_5178_Y_CELL = "BTO_0000795"

    # P-1798 cell
    BTO_0000796 = "BTO_0000796"
    P_1798_CELL = "BTO_0000796"

    # colonic cancer cell line
    BTO_0000797 = "BTO_0000797"
    COLONIC_CANCER_CELL_LINE = "BTO_0000797"

    # BeWo cell
    BTO_0000798 = "BTO_0000798"
    BEWO_CELL = "BTO_0000798"

    # lymphosarcoma cell
    BTO_0000799 = "BTO_0000799"
    LYMPHOSARCOMA_CELL = "BTO_0000799"

    # endoderm
    BTO_0000800 = "BTO_0000800"
    ENDODERM = "BTO_0000800"

    # macrophage
    BTO_0000801 = "BTO_0000801"
    MACROPHAGE = "BTO_0000801"

    # alveolar macrophage
    BTO_0000802 = "BTO_0000802"
    ALVEOLAR_MACROPHAGE = "BTO_0000802"

    # pancreatic delta cell
    BTO_0000803 = "BTO_0000803"
    PANCREATIC_DELTA_CELL = "BTO_0000803"

    # J-774A.1 cell
    BTO_0000804 = "BTO_0000804"
    J_774A_1_CELL = "BTO_0000804"

    # pancreatic PP cell
    BTO_0000805 = "BTO_0000805"
    PANCREATIC_PP_CELL = "BTO_0000805"

    # IC-21 cell
    BTO_0000806 = "BTO_0000806"
    IC_21_CELL = "BTO_0000806"

    # chorionic cell line
    BTO_0000807 = "BTO_0000807"
    CHORIONIC_CELL_LINE = "BTO_0000807"

    # interrenal gland
    BTO_0000808 = "BTO_0000808"
    INTERRENAL_GLAND = "BTO_0000808"

    # germ cell cancer cell
    BTO_0000809 = "BTO_0000809"
    GERM_CELL_CANCER_CELL = "BTO_0000809"

    # malpighian tubule
    BTO_0000810 = "BTO_0000810"
    MALPIGHIAN_TUBULE = "BTO_0000810"

    # ovary cancer cell line
    BTO_0000811 = "BTO_0000811"
    OVARY_CANCER_CELL_LINE = "BTO_0000811"

    # OVCAR-3 cell
    BTO_0000812 = "BTO_0000812"
    OVCAR_3_CELL = "BTO_0000812"

    # Pt-K1 cell
    BTO_0000813 = "BTO_0000813"
    PT_K1_CELL = "BTO_0000813"

    # CAOV-3 cell
    BTO_0000814 = "BTO_0000814"
    CAOV_3_CELL = "BTO_0000814"

    # MDA-MB-231 cell
    BTO_0000815 = "BTO_0000815"
    MDA_MB_231_CELL = "BTO_0000815"

    # breast cell line
    BTO_0000816 = "BTO_0000816"
    BREAST_CELL_LINE = "BTO_0000816"

    # mammary gland
    BTO_0000817 = "BTO_0000817"
    MAMMARY_GLAND = "BTO_0000817"

    # spinal column
    BTO_0000818 = "BTO_0000818"
    SPINAL_COLUMN = "BTO_0000818"

    # pharyngeal cell line
    BTO_0000819 = "BTO_0000819"
    PHARYNGEAL_CELL_LINE = "BTO_0000819"

    # C127I cell
    BTO_0000820 = "BTO_0000820"
    C127I_CELL = "BTO_0000820"

    # nipple
    BTO_0000821 = "BTO_0000821"
    NIPPLE = "BTO_0000821"

    # culture condition:mandelate-grown cell
    BTO_0000822 = "BTO_0000822"
    CULTURE_CONDITION_MANDELATE_GROWN_CELL = "BTO_0000822"

    # cerebral gray matter
    BTO_0000823 = "BTO_0000823"
    CEREBRAL_GRAY_MATTER = "BTO_0000823"

    # culture condition:mannose-grown cell
    BTO_0000824 = "BTO_0000824"
    CULTURE_CONDITION_MANNOSE_GROWN_CELL = "BTO_0000824"

    # mantle
    BTO_0000825 = "BTO_0000825"
    MANTLE = "BTO_0000825"

    # mantle cavity
    BTO_0000826 = "BTO_0000826"
    MANTLE_CAVITY = "BTO_0000826"

    # mantle muscle
    BTO_0000827 = "BTO_0000827"
    MANTLE_MUSCLE = "BTO_0000827"

    # throat
    BTO_0000828 = "BTO_0000828"
    THROAT = "BTO_0000828"

    # marrow
    BTO_0000829 = "BTO_0000829"
    MARROW = "BTO_0000829"

    # mast cell
    BTO_0000830 = "BTO_0000830"
    MAST_CELL = "BTO_0000830"

    # liver reticuloendothelial system
    BTO_0000831 = "BTO_0000831"
    LIVER_RETICULOENDOTHELIAL_SYSTEM = "BTO_0000831"

    # mastocytoma cell
    BTO_0000832 = "BTO_0000832"
    MASTOCYTOMA_CELL = "BTO_0000832"

    # RBL-2H3 cell
    BTO_0000833 = "BTO_0000833"
    RBL_2H3_CELL = "BTO_0000833"

    # Detroit-562 cell
    BTO_0000834 = "BTO_0000834"
    DETROIT_562_CELL = "BTO_0000834"

    # culture condition:L-idonate-grown cell
    BTO_0000835 = "BTO_0000835"
    CULTURE_CONDITION_L_IDONATE_GROWN_CELL = "BTO_0000835"

    # MDBK cell
    BTO_0000836 = "BTO_0000836"
    MDBK_CELL = "BTO_0000836"

    # MDCK cell
    BTO_0000837 = "BTO_0000837"
    MDCK_CELL = "BTO_0000837"

    # meconium
    BTO_0000838 = "BTO_0000838"
    MECONIUM = "BTO_0000838"

    # mesoderm
    BTO_0000839 = "BTO_0000839"
    MESODERM = "BTO_0000839"

    # nose
    BTO_0000840 = "BTO_0000840"
    NOSE = "BTO_0000840"

    # umbilical artery
    BTO_0000841 = "BTO_0000841"
    UMBILICAL_ARTERY = "BTO_0000841"

    # megagametophyte
    BTO_0000842 = "BTO_0000842"
    MEGAGAMETOPHYTE = "BTO_0000842"

    # megakaryocyte
    BTO_0000843 = "BTO_0000843"
    MEGAKARYOCYTE = "BTO_0000843"

    # megakaryotic cell line
    BTO_0000844 = "BTO_0000844"
    MEGAKARYOTIC_CELL_LINE = "BTO_0000844"

    # meiotic cell
    BTO_0000845 = "BTO_0000845"
    MEIOTIC_CELL = "BTO_0000845"

    # erythroleukemia cell line
    BTO_0000846 = "BTO_0000846"
    ERYTHROLEUKEMIA_CELL_LINE = "BTO_0000846"

    # melanocyte
    BTO_0000847 = "BTO_0000847"
    MELANOCYTE = "BTO_0000847"

    # melanoma cell
    BTO_0000848 = "BTO_0000848"
    MELANOMA_CELL = "BTO_0000848"

    # melanoma cell line
    BTO_0000849 = "BTO_0000849"
    MELANOMA_CELL_LINE = "BTO_0000849"

    # amelanotic melanoma cell
    BTO_0000850 = "BTO_0000850"
    AMELANOTIC_MELANOMA_CELL = "BTO_0000850"

    # adrenal cortex cell line
    BTO_0000851 = "BTO_0000851"
    ADRENAL_CORTEX_CELL_LINE = "BTO_0000851"

    # meristem
    BTO_0000852 = "BTO_0000852"
    MERISTEM = "BTO_0000852"

    # mesangial cell
    BTO_0000853 = "BTO_0000853"
    MESANGIAL_CELL = "BTO_0000853"

    # zygote
    BTO_0000854 = "BTO_0000854"
    ZYGOTE = "BTO_0000854"

    # lymph
    BTO_0000855 = "BTO_0000855"
    LYMPH = "BTO_0000855"

    # mesocarp
    BTO_0000856 = "BTO_0000856"
    MESOCARP = "BTO_0000856"

    # umbilical artery endothelium
    BTO_0000857 = "BTO_0000857"
    UMBILICAL_ARTERY_ENDOTHELIUM = "BTO_0000857"

    # mesophyll
    BTO_0000858 = "BTO_0000858"
    MESOPHYLL = "BTO_0000858"

    # metacestode
    BTO_0000859 = "BTO_0000859"
    METACESTODE = "BTO_0000859"

    # CHRB-30 cell
    BTO_0000860 = "BTO_0000860"
    CHRB_30_CELL = "BTO_0000860"

    # culture condition:methanol-grown cell
    BTO_0000861 = "BTO_0000861"
    CULTURE_CONDITION_METHANOL_GROWN_CELL = "BTO_0000861"

    # heart ventricle
    BTO_0000862 = "BTO_0000862"
    HEART_VENTRICLE = "BTO_0000862"

    # midgut
    BTO_0000863 = "BTO_0000863"
    MIDGUT = "BTO_0000863"

    # tibialis
    BTO_0000864 = "BTO_0000864"
    TIBIALIS = "BTO_0000864"

    # anterior spinal root
    BTO_0000865 = "BTO_0000865"
    ANTERIOR_SPINAL_ROOT = "BTO_0000865"

    # midgut secretion
    BTO_0000866 = "BTO_0000866"
    MIDGUT_SECRETION = "BTO_0000866"

    # tibialis posterior
    BTO_0000867 = "BTO_0000867"
    TIBIALIS_POSTERIOR = "BTO_0000867"

    # milk
    BTO_0000868 = "BTO_0000868"
    MILK = "BTO_0000868"

    # milk fat
    BTO_0000869 = "BTO_0000869"
    MILK_FAT = "BTO_0000869"

    # spinal nerve
    BTO_0000870 = "BTO_0000870"
    SPINAL_NERVE = "BTO_0000870"

    # RAG cell
    BTO_0000871 = "BTO_0000871"
    RAG_CELL = "BTO_0000871"

    # oligodendrocytic cell line
    BTO_0000872 = "BTO_0000872"
    OLIGODENDROCYTIC_CELL_LINE = "BTO_0000872"

    # MOLT-4 cell
    BTO_0000873 = "BTO_0000873"
    MOLT_4_CELL = "BTO_0000873"

    # molting gland
    BTO_0000874 = "BTO_0000874"
    MOLTING_GLAND = "BTO_0000874"

    # N20.1 cell
    BTO_0000875 = "BTO_0000875"
    N20_1_CELL = "BTO_0000875"

    # monocyte
    BTO_0000876 = "BTO_0000876"
    MONOCYTE = "BTO_0000876"

    # culture condition:trehalose-grown cell
    BTO_0000877 = "BTO_0000877"
    CULTURE_CONDITION_TREHALOSE_GROWN_CELL = "BTO_0000877"

    # mononuclear cell
    BTO_0000878 = "BTO_0000878"
    MONONUCLEAR_CELL = "BTO_0000878"

    # lateral ventricle
    BTO_0000879 = "BTO_0000879"
    LATERAL_VENTRICLE = "BTO_0000879"

    # culture condition:alkane-grown cell
    BTO_0000880 = "BTO_0000880"
    CULTURE_CONDITION_ALKANE_GROWN_CELL = "BTO_0000880"

    # Morris hepatoma 7777 cell
    BTO_0000881 = "BTO_0000881"
    MORRIS_HEPATOMA_7777_CELL = "BTO_0000881"

    # culture condition:p-hydroxyphenylacetic acid-grown cell
    BTO_0000882 = "BTO_0000882"
    CULTURE_CONDITION_P_HYDROXYPHENYLACETIC_ACID_GROWN_CELL = "BTO_0000882"

    # spinal root
    BTO_0000883 = "BTO_0000883"
    SPINAL_ROOT = "BTO_0000883"

    # molting fluid
    BTO_0000884 = "BTO_0000884"
    MOLTING_FLUID = "BTO_0000884"

    # tongue cell line
    BTO_0000885 = "BTO_0000885"
    TONGUE_CELL_LINE = "BTO_0000885"

    # mucosa
    BTO_0000886 = "BTO_0000886"
    MUCOSA = "BTO_0000886"

    # muscle
    BTO_0000887 = "BTO_0000887"
    MUSCLE = "BTO_0000887"

    # muscle fibre
    BTO_0000888 = "BTO_0000888"
    MUSCLE_FIBRE = "BTO_0000888"

    # Burkitt lymphoma cell line
    BTO_0000889 = "BTO_0000889"
    BURKITT_LYMPHOMA_CELL_LINE = "BTO_0000889"

    # mycelial felt
    BTO_0000890 = "BTO_0000890"
    MYCELIAL_FELT = "BTO_0000890"

    # NTERA-2 cell
    BTO_0000891 = "BTO_0000891"
    NTERA_2_CELL = "BTO_0000891"

    # mycobiont
    BTO_0000892 = "BTO_0000892"
    MYCOBIONT = "BTO_0000892"

    # mycorrhiza
    BTO_0000893 = "BTO_0000893"
    MYCORRHIZA = "BTO_0000893"

    # myelin
    BTO_0000894 = "BTO_0000894"
    MYELIN = "BTO_0000894"

    # myelin membrane
    BTO_0000895 = "BTO_0000895"
    MYELIN_MEMBRANE = "BTO_0000895"

    # bag cell neuron
    BTO_0000896 = "BTO_0000896"
    BAG_CELL_NEURON = "BTO_0000896"

    # amnion epithelium
    BTO_0000897 = "BTO_0000897"
    AMNION_EPITHELIUM = "BTO_0000897"

    # myeloma cell
    BTO_0000898 = "BTO_0000898"
    MYELOMA_CELL = "BTO_0000898"

    # myeloma cell line
    BTO_0000899 = "BTO_0000899"
    MYELOMA_CELL_LINE = "BTO_0000899"

    # myelin sheath
    BTO_0000900 = "BTO_0000900"
    MYELIN_SHEATH = "BTO_0000900"

    # myocardium
    BTO_0000901 = "BTO_0000901"
    MYOCARDIUM = "BTO_0000901"

    # plant vessel
    BTO_0000902 = "BTO_0000902"
    PLANT_VESSEL = "BTO_0000902"

    # atrium
    BTO_0000903 = "BTO_0000903"
    ATRIUM = "BTO_0000903"

    # culture condition:beta-aminoisobutyrate-grown cell
    BTO_0000904 = "BTO_0000904"
    CULTURE_CONDITION_BETA_AMINOISOBUTYRATE_GROWN_CELL = "BTO_0000904"

    # culture condition:myoinositol-grown cell
    BTO_0000905 = "BTO_0000905"
    CULTURE_CONDITION_MYOINOSITOL_GROWN_CELL = "BTO_0000905"

    # myeloid cell line
    BTO_0000906 = "BTO_0000906"
    MYELOID_CELL_LINE = "BTO_0000906"

    # myometrium
    BTO_0000907 = "BTO_0000907"
    MYOMETRIUM = "BTO_0000907"

    # myrosin cell
    BTO_0000908 = "BTO_0000908"
    MYROSIN_CELL = "BTO_0000908"

    # myxospore
    BTO_0000909 = "BTO_0000909"
    MYXOSPORE = "BTO_0000909"

    # culture condition:N-acetyl-D-glucosamine-grown cell
    BTO_0000910 = "BTO_0000910"
    CULTURE_CONDITION_N_ACETYL_D_GLUCOSAMINE_GROWN_CELL = "BTO_0000910"

    # culture condition:N-acetyl-D-mannosamine-grown cell
    BTO_0000911 = "BTO_0000911"
    CULTURE_CONDITION_N_ACETYL_D_MANNOSAMINE_GROWN_CELL = "BTO_0000911"

    # nasal mucosa
    BTO_0000912 = "BTO_0000912"
    NASAL_MUCOSA = "BTO_0000912"

    # nasal polyp
    BTO_0000913 = "BTO_0000913"
    NASAL_POLYP = "BTO_0000913"

    # natural killer cell
    BTO_0000914 = "BTO_0000914"
    NATURAL_KILLER_CELL = "BTO_0000914"

    # nauplius
    BTO_0000915 = "BTO_0000915"
    NAUPLIUS = "BTO_0000915"

    # NC37 cell
    BTO_0000916 = "BTO_0000916"
    NC37_CELL = "BTO_0000916"

    # needle
    BTO_0000917 = "BTO_0000917"
    NEEDLE = "BTO_0000917"

    # nematocyst
    BTO_0000918 = "BTO_0000918"
    NEMATOCYST = "BTO_0000918"

    # 8305C cell
    BTO_0000919 = "BTO_0000919"
    _8305C_CELL = "BTO_0000919"

    # neocortex
    BTO_0000920 = "BTO_0000920"
    NEOCORTEX = "BTO_0000920"

    # CAL-27 cell
    BTO_0000921 = "BTO_0000921"
    CAL_27_CELL = "BTO_0000921"

    # neostriatal neuron
    BTO_0000922 = "BTO_0000922"
    NEOSTRIATAL_NEURON = "BTO_0000922"

    # nephridium
    BTO_0000923 = "BTO_0000923"
    NEPHRIDIUM = "BTO_0000923"

    # nephron
    BTO_0000924 = "BTO_0000924"
    NEPHRON = "BTO_0000924"

    # nerve
    BTO_0000925 = "BTO_0000925"
    NERVE = "BTO_0000925"

    # ophthalmic nerve
    BTO_0000926 = "BTO_0000926"
    OPHTHALMIC_NERVE = "BTO_0000926"

    # nerve trunk
    BTO_0000927 = "BTO_0000927"
    NERVE_TRUNK = "BTO_0000927"

    # limbic system
    BTO_0000928 = "BTO_0000928"
    LIMBIC_SYSTEM = "BTO_0000928"

    # neural retina
    BTO_0000929 = "BTO_0000929"
    NEURAL_RETINA = "BTO_0000929"

    # neuroblast
    BTO_0000930 = "BTO_0000930"
    NEUROBLAST = "BTO_0000930"

    # neuroblastoma cell
    BTO_0000931 = "BTO_0000931"
    NEUROBLASTOMA_CELL = "BTO_0000931"

    # neuroblastoma cell line
    BTO_0000932 = "BTO_0000932"
    NEUROBLASTOMA_CELL_LINE = "BTO_0000932"

    # N18TG2 cell
    BTO_0000933 = "BTO_0000933"
    N18TG2_CELL = "BTO_0000933"

    # IMR-32 cell
    BTO_0000934 = "BTO_0000934"
    IMR_32_CELL = "BTO_0000934"

    # LAN-5 cell
    BTO_0000935 = "BTO_0000935"
    LAN_5_CELL = "BTO_0000935"

    # neurofibrillary tangle
    BTO_0000936 = "BTO_0000936"
    NEUROFIBRILLARY_TANGLE = "BTO_0000936"

    # neurohypophysis
    BTO_0000937 = "BTO_0000937"
    NEUROHYPOPHYSIS = "BTO_0000937"

    # neuron
    BTO_0000938 = "BTO_0000938"
    NEURON = "BTO_0000938"

    # basal cell
    BTO_0000939 = "BTO_0000939"
    BASAL_CELL = "BTO_0000939"

    # juice vesicle
    BTO_0000940 = "BTO_0000940"
    JUICE_VESICLE = "BTO_0000940"

    # CAL-33 cell
    BTO_0000941 = "BTO_0000941"
    CAL_33_CELL = "BTO_0000941"

    # NG-108-15 cell
    BTO_0000942 = "BTO_0000942"
    NG_108_15_CELL = "BTO_0000942"

    # culture condition:nicotinic acid-grown cell
    BTO_0000943 = "BTO_0000943"
    CULTURE_CONDITION_NICOTINIC_ACID_GROWN_CELL = "BTO_0000943"

    # NIH-3T3 cell
    BTO_0000944 = "BTO_0000944"
    NIH_3T3_CELL = "BTO_0000944"

    # CAL-51 cell
    BTO_0000945 = "BTO_0000945"
    CAL_51_CELL = "BTO_0000945"

    # NT2/D1 cell
    BTO_0000946 = "BTO_0000946"
    NT2_D1_CELL = "BTO_0000946"

    # neuronal cell line
    BTO_0000947 = "BTO_0000947"
    NEURONAL_CELL_LINE = "BTO_0000947"

    # SKOV-3 cell
    BTO_0000948 = "BTO_0000948"
    SKOV_3_CELL = "BTO_0000948"

    # Novikoff ascites tumor cell
    BTO_0000949 = "BTO_0000949"
    NOVIKOFF_ASCITES_TUMOR_CELL = "BTO_0000949"

    # Novikoff hepatoma cell
    BTO_0000950 = "BTO_0000950"
    NOVIKOFF_HEPATOMA_CELL = "BTO_0000950"

    # NRK cell
    BTO_0000951 = "BTO_0000951"
    NRK_CELL = "BTO_0000951"

    # nuchal ligament
    BTO_0000952 = "BTO_0000952"
    NUCHAL_LIGAMENT = "BTO_0000952"

    # nurse cell
    BTO_0000953 = "BTO_0000953"
    NURSE_CELL = "BTO_0000953"

    # nymph
    BTO_0000954 = "BTO_0000954"
    NYMPH = "BTO_0000954"

    # laryngeal cell line
    BTO_0000955 = "BTO_0000955"
    LARYNGEAL_CELL_LINE = "BTO_0000955"

    # gut epithelium
    BTO_0000956 = "BTO_0000956"
    GUT_EPITHELIUM = "BTO_0000956"

    # nape
    BTO_0000957 = "BTO_0000957"
    NAPE = "BTO_0000957"

    # spermatogonium
    BTO_0000958 = "BTO_0000958"
    SPERMATOGONIUM = "BTO_0000958"

    # esophagus
    BTO_0000959 = "BTO_0000959"
    ESOPHAGUS = "BTO_0000959"

    # UT-7 cell
    BTO_0000960 = "BTO_0000960"
    UT_7_CELL = "BTO_0000960"

    # olfactory bulb
    BTO_0000961 = "BTO_0000961"
    OLFACTORY_BULB = "BTO_0000961"

    # oligodendrocyte
    BTO_0000962 = "BTO_0000962"
    OLIGODENDROCYTE = "BTO_0000962"

    # oligodendroglioma cell
    BTO_0000963 = "BTO_0000963"
    OLIGODENDROGLIOMA_CELL = "BTO_0000963"

    # oocyte
    BTO_0000964 = "BTO_0000964"
    OOCYTE = "BTO_0000964"

    # optic lobe
    BTO_0000965 = "BTO_0000965"
    OPTIC_LOBE = "BTO_0000965"

    # optic nerve
    BTO_0000966 = "BTO_0000966"
    OPTIC_NERVE = "BTO_0000966"

    # osseous plate
    BTO_0000967 = "BTO_0000967"
    OSSEOUS_PLATE = "BTO_0000967"

    # osteoclast
    BTO_0000968 = "BTO_0000968"
    OSTEOCLAST = "BTO_0000968"

    # osteoclastoma cell
    BTO_0000969 = "BTO_0000969"
    OSTEOCLASTOMA_CELL = "BTO_0000969"

    # osteosarcoma cell
    BTO_0000970 = "BTO_0000970"
    OSTEOSARCOMA_CELL = "BTO_0000970"

    # SAOS-2 cell
    BTO_0000971 = "BTO_0000971"
    SAOS_2_CELL = "BTO_0000971"

    # HEP-3B cell
    BTO_0000972 = "BTO_0000972"
    HEP_3B_CELL = "BTO_0000972"

    # respiratory mucosa
    BTO_0000973 = "BTO_0000973"
    RESPIRATORY_MUCOSA = "BTO_0000973"

    # culture condition:sulfite-grown cell
    BTO_0000974 = "BTO_0000974"
    CULTURE_CONDITION_SULFITE_GROWN_CELL = "BTO_0000974"

    # ovary
    BTO_0000975 = "BTO_0000975"
    OVARY = "BTO_0000975"

    # HEp-2 cell
    BTO_0000976 = "BTO_0000976"
    HEP_2_CELL = "BTO_0000976"

    # ovary cell line
    BTO_0000977 = "BTO_0000977"
    OVARY_CELL_LINE = "BTO_0000977"

    # CMK cell
    BTO_0000978 = "BTO_0000978"
    CMK_CELL = "BTO_0000978"

    # PANC-3 cell
    BTO_0000979 = "BTO_0000979"
    PANC_3_CELL = "BTO_0000979"

    # oviduct
    BTO_0000980 = "BTO_0000980"
    OVIDUCT = "BTO_0000980"

    # ovotestis
    BTO_0000981 = "BTO_0000981"
    OVOTESTIS = "BTO_0000981"

    # culture condition:p-cresol-grown cell
    BTO_0000982 = "BTO_0000982"
    CULTURE_CONDITION_P_CRESOL_GROWN_CELL = "BTO_0000982"

    # culture condition:p-toluate-grown cell
    BTO_0000983 = "BTO_0000983"
    CULTURE_CONDITION_P_TOLUATE_GROWN_CELL = "BTO_0000983"

    # P-388D1 cell
    BTO_0000984 = "BTO_0000984"
    P_388D1_CELL = "BTO_0000984"

    # P-815 cell
    BTO_0000985 = "BTO_0000985"
    P_815_CELL = "BTO_0000985"

    # pachytene cell
    BTO_0000986 = "BTO_0000986"
    PACHYTENE_CELL = "BTO_0000986"

    # palisade parenchyma
    BTO_0000987 = "BTO_0000987"
    PALISADE_PARENCHYMA = "BTO_0000987"

    # pancreas
    BTO_0000988 = "BTO_0000988"
    PANCREAS = "BTO_0000988"

    # taste bud
    BTO_0000989 = "BTO_0000989"
    TASTE_BUD = "BTO_0000989"

    # pancreatic alpha cell
    BTO_0000990 = "BTO_0000990"
    PANCREATIC_ALPHA_CELL = "BTO_0000990"

    # pancreatic islet
    BTO_0000991 = "BTO_0000991"
    PANCREATIC_ISLET = "BTO_0000991"

    # tongue epithelium
    BTO_0000992 = "BTO_0000992"
    TONGUE_EPITHELIUM = "BTO_0000992"

    # paneth cell
    BTO_0000993 = "BTO_0000993"
    PANETH_CELL = "BTO_0000993"

    # RBL-1 cell
    BTO_0000994 = "BTO_0000994"
    RBL_1_CELL = "BTO_0000994"

    # paramyeloblast
    BTO_0000995 = "BTO_0000995"
    PARAMYELOBLAST = "BTO_0000995"

    # gametocyte
    BTO_0000996 = "BTO_0000996"
    GAMETOCYTE = "BTO_0000996"

    # parathyroid gland
    BTO_0000997 = "BTO_0000997"
    PARATHYROID_GLAND = "BTO_0000997"

    # paraveinal mesophyll
    BTO_0000998 = "BTO_0000998"
    PARAVEINAL_MESOPHYLL = "BTO_0000998"

    # plant parenchyma
    BTO_0000999 = "BTO_0000999"
    PLANT_PARENCHYMA = "BTO_0000999"

    # acute megakaryocytic leukemia cell line
    BTO_0001000 = "BTO_0001000"
    ACUTE_MEGAKARYOCYTIC_LEUKEMIA_CELL_LINE = "BTO_0001000"

    # parietal lobe
    BTO_0001001 = "BTO_0001001"
    PARIETAL_LOBE = "BTO_0001001"

    # schizont
    BTO_0001002 = "BTO_0001002"
    SCHIZONT = "BTO_0001002"

    # parotid acinar cell
    BTO_0001003 = "BTO_0001003"
    PAROTID_ACINAR_CELL = "BTO_0001003"

    # parotid gland
    BTO_0001004 = "BTO_0001004"
    PAROTID_GLAND = "BTO_0001004"

    # amnion epithelial cell
    BTO_0001005 = "BTO_0001005"
    AMNION_EPITHELIAL_CELL = "BTO_0001005"

    # pelvis
    BTO_0001006 = "BTO_0001006"
    PELVIS = "BTO_0001006"

    # AGS cell
    BTO_0001007 = "BTO_0001007"
    AGS_CELL = "BTO_0001007"

    # PBMC cell line
    BTO_0001008 = "BTO_0001008"
    PBMC_CELL_LINE = "BTO_0001008"

    # PC-12 cell
    BTO_0001009 = "BTO_0001009"
    PC_12_CELL = "BTO_0001009"

    # callus
    BTO_0001010 = "BTO_0001010"
    CALLUS = "BTO_0001010"

    # cerebellar Purkinje cell
    BTO_0001011 = "BTO_0001011"
    CEREBELLAR_PURKINJE_CELL = "BTO_0001011"

    # pedal ganglion
    BTO_0001012 = "BTO_0001012"
    PEDAL_GANGLION = "BTO_0001012"

    # pedal muscle
    BTO_0001013 = "BTO_0001013"
    PEDAL_MUSCLE = "BTO_0001013"

    # Mo-T cell
    BTO_0001014 = "BTO_0001014"
    MO_T_CELL = "BTO_0001014"

    # culture condition:pentanoate-grown cell
    BTO_0001015 = "BTO_0001015"
    CULTURE_CONDITION_PENTANOATE_GROWN_CELL = "BTO_0001015"

    # pericardial fluid
    BTO_0001016 = "BTO_0001016"
    PERICARDIAL_FLUID = "BTO_0001016"

    # pericarp
    BTO_0001017 = "BTO_0001017"
    PERICARP = "BTO_0001017"

    # basophilic leukemia cell line
    BTO_0001018 = "BTO_0001018"
    BASOPHILIC_LEUKEMIA_CELL_LINE = "BTO_0001018"

    # prostate gland cell line
    BTO_0001019 = "BTO_0001019"
    PROSTATE_GLAND_CELL_LINE = "BTO_0001019"

    # periodontal ligament
    BTO_0001020 = "BTO_0001020"
    PERIODONTAL_LIGAMENT = "BTO_0001020"

    # periodontium
    BTO_0001021 = "BTO_0001021"
    PERIODONTIUM = "BTO_0001021"

    # periosteum
    BTO_0001022 = "BTO_0001022"
    PERIOSTEUM = "BTO_0001022"

    # ovary cancer cell
    BTO_0001023 = "BTO_0001023"
    OVARY_CANCER_CELL = "BTO_0001023"

    # retinal rod
    BTO_0001024 = "BTO_0001024"
    RETINAL_ROD = "BTO_0001024"

    # peripheral blood mononuclear cell
    BTO_0001025 = "BTO_0001025"
    PERIPHERAL_BLOOD_MONONUCLEAR_CELL = "BTO_0001025"

    # polymorphonuclear leukocyte
    BTO_0001026 = "BTO_0001026"
    POLYMORPHONUCLEAR_LEUKOCYTE = "BTO_0001026"

    # peripheral nerve
    BTO_0001027 = "BTO_0001027"
    PERIPHERAL_NERVE = "BTO_0001027"

    # peripheral nervous system
    BTO_0001028 = "BTO_0001028"
    PERIPHERAL_NERVOUS_SYSTEM = "BTO_0001028"

    # perisperm
    BTO_0001029 = "BTO_0001029"
    PERISPERM = "BTO_0001029"

    # J774.2 cell
    BTO_0001030 = "BTO_0001030"
    J774_2_CELL = "BTO_0001030"

    # peritoneal fluid
    BTO_0001031 = "BTO_0001031"
    PERITONEAL_FLUID = "BTO_0001031"

    # cardiac Purkinje cell
    BTO_0001032 = "BTO_0001032"
    CARDIAC_PURKINJE_CELL = "BTO_0001032"

    # prostate cancer cell line
    BTO_0001033 = "BTO_0001033"
    PROSTATE_CANCER_CELL_LINE = "BTO_0001033"

    # peritoneal macrophage
    BTO_0001034 = "BTO_0001034"
    PERITONEAL_MACROPHAGE = "BTO_0001034"

    # hematopoietic cell line
    BTO_0001035 = "BTO_0001035"
    HEMATOPOIETIC_CELL_LINE = "BTO_0001035"

    # retinal cone
    BTO_0001036 = "BTO_0001036"
    RETINAL_CONE = "BTO_0001036"

    # sensory cell
    BTO_0001037 = "BTO_0001037"
    SENSORY_CELL = "BTO_0001037"

    # peritrophic membrane
    BTO_0001038 = "BTO_0001038"
    PERITROPHIC_MEMBRANE = "BTO_0001038"

    # peritubular cell
    BTO_0001039 = "BTO_0001039"
    PERITUBULAR_CELL = "BTO_0001039"

    # petal
    BTO_0001040 = "BTO_0001040"
    PETAL = "BTO_0001040"

    # petiole
    BTO_0001041 = "BTO_0001041"
    PETIOLE = "BTO_0001041"

    # amygdala
    BTO_0001042 = "BTO_0001042"
    AMYGDALA = "BTO_0001042"

    # adult
    BTO_0001043 = "BTO_0001043"
    ADULT = "BTO_0001043"

    # phagocyte
    BTO_0001044 = "BTO_0001044"
    PHAGOCYTE = "BTO_0001044"

    # T-lymphocyte cell line
    BTO_0001045 = "BTO_0001045"
    T_LYMPHOCYTE_CELL_LINE = "BTO_0001045"

    # pharate pupa
    BTO_0001046 = "BTO_0001046"
    PHARATE_PUPA = "BTO_0001046"

    # pharyngeal mucosa
    BTO_0001047 = "BTO_0001047"
    PHARYNGEAL_MUCOSA = "BTO_0001047"

    # pharyngeal muscle
    BTO_0001048 = "BTO_0001048"
    PHARYNGEAL_MUSCLE = "BTO_0001048"

    # pharynx
    BTO_0001049 = "BTO_0001049"
    PHARYNX = "BTO_0001049"

    # culture condition:phenol-grown cell
    BTO_0001050 = "BTO_0001050"
    CULTURE_CONDITION_PHENOL_GROWN_CELL = "BTO_0001050"

    # culture condition:phenylacetic acid-grown cell
    BTO_0001051 = "BTO_0001051"
    CULTURE_CONDITION_PHENYLACETIC_ACID_GROWN_CELL = "BTO_0001051"

    # ND-1 cell
    BTO_0001052 = "BTO_0001052"
    ND_1_CELL = "BTO_0001052"

    # culture condition:phenylglyoxylate-grown cell
    BTO_0001053 = "BTO_0001053"
    CULTURE_CONDITION_PHENYLGLYOXYLATE_GROWN_CELL = "BTO_0001053"

    # pheochromocytoma cell
    BTO_0001054 = "BTO_0001054"
    PHEOCHROMOCYTOMA_CELL = "BTO_0001054"

    # ovarian epithelial cell
    BTO_0001055 = "BTO_0001055"
    OVARIAN_EPITHELIAL_CELL = "BTO_0001055"

    # myeloid leukemia cell
    BTO_0001056 = "BTO_0001056"
    MYELOID_LEUKEMIA_CELL = "BTO_0001056"

    # neural tube
    BTO_0001057 = "BTO_0001057"
    NEURAL_TUBE = "BTO_0001057"

    # phloem
    BTO_0001058 = "BTO_0001058"
    PHLOEM = "BTO_0001058"

    # culture condition:phosphonoacetate-grown cell
    BTO_0001059 = "BTO_0001059"
    CULTURE_CONDITION_PHOSPHONOACETATE_GROWN_CELL = "BTO_0001059"

    # photoreceptor cell
    BTO_0001060 = "BTO_0001060"
    PHOTORECEPTOR_CELL = "BTO_0001060"

    # PC-3 cell
    BTO_0001061 = "BTO_0001061"
    PC_3_CELL = "BTO_0001061"

    # PPC-1 cell
    BTO_0001062 = "BTO_0001062"
    PPC_1_CELL = "BTO_0001062"

    # phrenic nerve
    BTO_0001063 = "BTO_0001063"
    PHRENIC_NERVE = "BTO_0001063"

    # phycobiont
    BTO_0001064 = "BTO_0001064"
    PHYCOBIONT = "BTO_0001064"

    # Tsu-Pr1 cell
    BTO_0001065 = "BTO_0001065"
    TSU_PR1_CELL = "BTO_0001065"

    # hippocampal pyramidal layer
    BTO_0001066 = "BTO_0001066"
    HIPPOCAMPAL_PYRAMIDAL_LAYER = "BTO_0001066"

    # pineal gland
    BTO_0001067 = "BTO_0001067"
    PINEAL_GLAND = "BTO_0001067"

    # pinealocyte
    BTO_0001068 = "BTO_0001068"
    PINEALOCYTE = "BTO_0001068"

    # pitcher
    BTO_0001069 = "BTO_0001069"
    PITCHER = "BTO_0001069"

    # pitcher secretion
    BTO_0001070 = "BTO_0001070"
    PITCHER_SECRETION = "BTO_0001070"

    # pith
    BTO_0001071 = "BTO_0001071"
    PITH = "BTO_0001071"

    # trigeminal nerve
    BTO_0001072 = "BTO_0001072"
    TRIGEMINAL_NERVE = "BTO_0001072"

    # hypophysis
    BTO_0001073 = "BTO_0001073"
    HYPOPHYSIS = "BTO_0001073"

    # trigeminal nucleus
    BTO_0001074 = "BTO_0001074"
    TRIGEMINAL_NUCLEUS = "BTO_0001074"

    # motor trigeminal nucleus
    BTO_0001075 = "BTO_0001075"
    MOTOR_TRIGEMINAL_NUCLEUS = "BTO_0001075"

    # pituitary gland tumor cell
    BTO_0001076 = "BTO_0001076"
    PITUITARY_GLAND_TUMOR_CELL = "BTO_0001076"

    # AtT-20 cell
    BTO_0001077 = "BTO_0001077"
    ATT_20_CELL = "BTO_0001077"

    # placenta
    BTO_0001078 = "BTO_0001078"
    PLACENTA = "BTO_0001078"

    # trophoblast
    BTO_0001079 = "BTO_0001079"
    TROPHOBLAST = "BTO_0001079"

    # Morris hepatoma cell
    BTO_0001080 = "BTO_0001080"
    MORRIS_HEPATOMA_CELL = "BTO_0001080"

    # MOLT-3 cell
    BTO_0001081 = "BTO_0001081"
    MOLT_3_CELL = "BTO_0001081"

    # MM46 cell
    BTO_0001082 = "BTO_0001082"
    MM46_CELL = "BTO_0001082"

    # MH134 cell
    BTO_0001083 = "BTO_0001083"
    MH134_CELL = "BTO_0001083"

    # plantlet
    BTO_0001084 = "BTO_0001084"
    PLANTLET = "BTO_0001084"

    # vascular system
    BTO_0001085 = "BTO_0001085"
    VASCULAR_SYSTEM = "BTO_0001085"

    # embryonic stem cell
    BTO_0001086 = "BTO_0001086"
    EMBRYONIC_STEM_CELL = "BTO_0001086"

    # plasmacytoma cell
    BTO_0001087 = "BTO_0001087"
    PLASMACYTOMA_CELL = "BTO_0001087"

    # gastric cell line
    BTO_0001088 = "BTO_0001088"
    GASTRIC_CELL_LINE = "BTO_0001088"

    # MPC-11 cell
    BTO_0001089 = "BTO_0001089"
    MPC_11_CELL = "BTO_0001089"

    # mouth
    BTO_0001090 = "BTO_0001090"
    MOUTH = "BTO_0001090"

    # axenic culture
    BTO_0001091 = "BTO_0001091"
    AXENIC_CULTURE = "BTO_0001091"

    # KATO-III cell
    BTO_0001092 = "BTO_0001092"
    KATO_III_CELL = "BTO_0001092"

    # WEHI-231 cell
    BTO_0001093 = "BTO_0001093"
    WEHI_231_CELL = "BTO_0001093"

    # pre-B acute lymphoblastic leukemia cell
    BTO_0001094 = "BTO_0001094"
    PRE_B_ACUTE_LYMPHOBLASTIC_LEUKEMIA_CELL = "BTO_0001094"

    # pod
    BTO_0001095 = "BTO_0001095"
    POD = "BTO_0001095"

    # lymphoid cell
    BTO_0001096 = "BTO_0001096"
    LYMPHOID_CELL = "BTO_0001096"

    # pollen
    BTO_0001097 = "BTO_0001097"
    POLLEN = "BTO_0001097"

    # sorocarp
    BTO_0001098 = "BTO_0001098"
    SOROCARP = "BTO_0001098"

    # blastocyst
    BTO_0001099 = "BTO_0001099"
    BLASTOCYST = "BTO_0001099"

    # B-cell acute lymphoblastic leukemia cell
    BTO_0001100 = "BTO_0001100"
    B_CELL_ACUTE_LYMPHOBLASTIC_LEUKEMIA_CELL = "BTO_0001100"

    # pons
    BTO_0001101 = "BTO_0001101"
    PONS = "BTO_0001101"

    # blood vessel
    BTO_0001102 = "BTO_0001102"
    BLOOD_VESSEL = "BTO_0001102"

    # skeletal muscle
    BTO_0001103 = "BTO_0001103"
    SKELETAL_MUSCLE = "BTO_0001103"

    # cranial nerve
    BTO_0001104 = "BTO_0001104"
    CRANIAL_NERVE = "BTO_0001104"

    # insular cortex
    BTO_0001105 = "BTO_0001105"
    INSULAR_CORTEX = "BTO_0001105"

    # T-cell acute lymphoblastic leukemia cell
    BTO_0001106 = "BTO_0001106"
    T_CELL_ACUTE_LYMPHOBLASTIC_LEUKEMIA_CELL = "BTO_0001106"

    # preadipocyte
    BTO_0001107 = "BTO_0001107"
    PREADIPOCYTE = "BTO_0001107"

    # mitral cell layer
    BTO_0001108 = "BTO_0001108"
    MITRAL_CELL_LAYER = "BTO_0001108"

    # HCT-116 cell
    BTO_0001109 = "BTO_0001109"
    HCT_116_CELL = "BTO_0001109"

    # prepupa
    BTO_0001110 = "BTO_0001110"
    PREPUPA = "BTO_0001110"

    # preputial gland
    BTO_0001111 = "BTO_0001111"
    PREPUTIAL_GLAND = "BTO_0001111"

    # preputial gland tumor cell
    BTO_0001112 = "BTO_0001112"
    PREPUTIAL_GLAND_TUMOR_CELL = "BTO_0001112"

    # prepuce
    BTO_0001113 = "BTO_0001113"
    PREPUCE = "BTO_0001113"

    # primary leaf
    BTO_0001114 = "BTO_0001114"
    PRIMARY_LEAF = "BTO_0001114"

    # primary spermatocyte
    BTO_0001115 = "BTO_0001115"
    PRIMARY_SPERMATOCYTE = "BTO_0001115"

    # floral primordium
    BTO_0001116 = "BTO_0001116"
    FLORAL_PRIMORDIUM = "BTO_0001116"

    # proboscis
    BTO_0001117 = "BTO_0001117"
    PROBOSCIS = "BTO_0001117"

    # P3X63Ag8 cell
    BTO_0001118 = "BTO_0001118"
    P3X63AG8_CELL = "BTO_0001118"

    # procambium
    BTO_0001119 = "BTO_0001119"
    PROCAMBIUM = "BTO_0001119"

    # epithelial cell line
    BTO_0001120 = "BTO_0001120"
    EPITHELIAL_CELL_LINE = "BTO_0001120"

    # cauline leaf
    BTO_0001121 = "BTO_0001121"
    CAULINE_LEAF = "BTO_0001121"

    # procyclic form
    BTO_0001122 = "BTO_0001122"
    PROCYCLIC_FORM = "BTO_0001122"

    # peripheral ganglion
    BTO_0001123 = "BTO_0001123"
    PERIPHERAL_GANGLION = "BTO_0001123"

    # promastigote
    BTO_0001124 = "BTO_0001124"
    PROMASTIGOTE = "BTO_0001124"

    # culture condition:propanediol-grown cell
    BTO_0001125 = "BTO_0001125"
    CULTURE_CONDITION_PROPANEDIOL_GROWN_CELL = "BTO_0001125"

    # culture condition:propionate-grown cell
    BTO_0001126 = "BTO_0001126"
    CULTURE_CONDITION_PROPIONATE_GROWN_CELL = "BTO_0001126"

    # primary culture
    BTO_0001127 = "BTO_0001127"
    PRIMARY_CULTURE = "BTO_0001127"

    # prostasome
    BTO_0001128 = "BTO_0001128"
    PROSTASOME = "BTO_0001128"

    # prostate gland
    BTO_0001129 = "BTO_0001129"
    PROSTATE_GLAND = "BTO_0001129"

    # prostate gland cancer cell
    BTO_0001130 = "BTO_0001130"
    PROSTATE_GLAND_CANCER_CELL = "BTO_0001130"

    # BHK cell
    BTO_0001131 = "BTO_0001131"
    BHK_CELL = "BTO_0001131"

    # shoot base
    BTO_0001132 = "BTO_0001132"
    SHOOT_BASE = "BTO_0001132"

    # pre-B-lymphocyte
    BTO_0001133 = "BTO_0001133"
    PRE_B_LYMPHOCYTE = "BTO_0001133"

    # protonema
    BTO_0001134 = "BTO_0001134"
    PROTONEMA = "BTO_0001134"

    # protoxylem
    BTO_0001135 = "BTO_0001135"
    PROTOXYLEM = "BTO_0001135"

    # proventriculus
    BTO_0001136 = "BTO_0001136"
    PROVENTRICULUS = "BTO_0001136"

    # right colon mucosa
    BTO_0001137 = "BTO_0001137"
    RIGHT_COLON_MUCOSA = "BTO_0001137"

    # somatic embryo
    BTO_0001138 = "BTO_0001138"
    SOMATIC_EMBRYO = "BTO_0001138"

    # pseudoplasmodium
    BTO_0001139 = "BTO_0001139"
    PSEUDOPLASMODIUM = "BTO_0001139"

    # psoas
    BTO_0001140 = "BTO_0001140"
    PSOAS = "BTO_0001140"

    # pulmonary artery endothelial cell
    BTO_0001141 = "BTO_0001141"
    PULMONARY_ARTERY_ENDOTHELIAL_CELL = "BTO_0001141"

    # pulp
    BTO_0001142 = "BTO_0001142"
    PULP = "BTO_0001142"

    # pupa
    BTO_0001143 = "BTO_0001143"
    PUPA = "BTO_0001143"

    # chloronema
    BTO_0001144 = "BTO_0001144"
    CHLORONEMA = "BTO_0001144"

    # pre-T-lymphocyte
    BTO_0001145 = "BTO_0001145"
    PRE_T_LYMPHOCYTE = "BTO_0001145"

    # pyloric region
    BTO_0001146 = "BTO_0001146"
    PYLORIC_REGION = "BTO_0001146"

    # culture condition:pyridoxine-grown cell
    BTO_0001147 = "BTO_0001147"
    CULTURE_CONDITION_PYRIDOXINE_GROWN_CELL = "BTO_0001147"

    # BALL-1 cell
    BTO_0001148 = "BTO_0001148"
    BALL_1_CELL = "BTO_0001148"

    # quadriceps
    BTO_0001149 = "BTO_0001149"
    QUADRICEPS = "BTO_0001149"

    # culture condition:quinaldine-grown cell
    BTO_0001150 = "BTO_0001150"
    CULTURE_CONDITION_QUINALDINE_GROWN_CELL = "BTO_0001150"

    # MOLT-4F cell
    BTO_0001151 = "BTO_0001151"
    MOLT_4F_CELL = "BTO_0001151"

    # radicle
    BTO_0001152 = "BTO_0001152"
    RADICLE = "BTO_0001152"

    # radular muscle
    BTO_0001153 = "BTO_0001153"
    RADULAR_MUSCLE = "BTO_0001153"

    # RAJI cell
    BTO_0001154 = "BTO_0001154"
    RAJI_CELL = "BTO_0001154"

    # ray cell
    BTO_0001155 = "BTO_0001155"
    RAY_CELL = "BTO_0001155"

    # node
    BTO_0001156 = "BTO_0001156"
    NODE = "BTO_0001156"

    # rectal gland
    BTO_0001157 = "BTO_0001157"
    RECTAL_GLAND = "BTO_0001157"

    # rectum
    BTO_0001158 = "BTO_0001158"
    RECTUM = "BTO_0001158"

    # aorta thoracica smooth muscle
    BTO_0001159 = "BTO_0001159"
    AORTA_THORACICA_SMOOTH_MUSCLE = "BTO_0001159"

    # red bone marrow
    BTO_0001160 = "BTO_0001160"
    RED_BONE_MARROW = "BTO_0001160"

    # chorionic villus
    BTO_0001161 = "BTO_0001161"
    CHORIONIC_VILLUS = "BTO_0001161"

    # apocrine gland
    BTO_0001162 = "BTO_0001162"
    APOCRINE_GLAND = "BTO_0001162"

    # REH cell
    BTO_0001163 = "BTO_0001163"
    REH_CELL = "BTO_0001163"

    # megakaryoblast
    BTO_0001164 = "BTO_0001164"
    MEGAKARYOBLAST = "BTO_0001164"

    # renal artery
    BTO_0001165 = "BTO_0001165"
    RENAL_ARTERY = "BTO_0001165"

    # renal cortex
    BTO_0001166 = "BTO_0001166"
    RENAL_CORTEX = "BTO_0001166"

    # renal medulla
    BTO_0001167 = "BTO_0001167"
    RENAL_MEDULLA = "BTO_0001167"

    # rennet
    BTO_0001168 = "BTO_0001168"
    RENNET = "BTO_0001168"

    # 3T3-F442A cell
    BTO_0001169 = "BTO_0001169"
    _3T3_F442A_CELL = "BTO_0001169"

    # resting cell
    BTO_0001170 = "BTO_0001170"
    RESTING_CELL = "BTO_0001170"

    # spore
    BTO_0001171 = "BTO_0001171"
    SPORE = "BTO_0001171"

    # reticulate body
    BTO_0001172 = "BTO_0001172"
    RETICULATE_BODY = "BTO_0001172"

    # reticulocyte
    BTO_0001173 = "BTO_0001173"
    RETICULOCYTE = "BTO_0001173"

    # reticuloendothelial system
    BTO_0001174 = "BTO_0001174"
    RETICULOENDOTHELIAL_SYSTEM = "BTO_0001174"

    # retina
    BTO_0001175 = "BTO_0001175"
    RETINA = "BTO_0001175"

    # endothelial cell
    BTO_0001176 = "BTO_0001176"
    ENDOTHELIAL_CELL = "BTO_0001176"

    # retinal pigment epithelium
    BTO_0001177 = "BTO_0001177"
    RETINAL_PIGMENT_EPITHELIUM = "BTO_0001177"

    # retinoblastoma cell
    BTO_0001178 = "BTO_0001178"
    RETINOBLASTOMA_CELL = "BTO_0001178"

    # rhizophore
    BTO_0001179 = "BTO_0001179"
    RHIZOPHORE = "BTO_0001179"

    # idioblast
    BTO_0001180 = "BTO_0001180"
    IDIOBLAST = "BTO_0001180"

    # rhizome
    BTO_0001181 = "BTO_0001181"
    RHIZOME = "BTO_0001181"

    # primary root
    BTO_0001182 = "BTO_0001182"
    PRIMARY_ROOT = "BTO_0001182"

    # secondary root
    BTO_0001183 = "BTO_0001183"
    SECONDARY_ROOT = "BTO_0001183"

    # rind
    BTO_0001184 = "BTO_0001184"
    RIND = "BTO_0001184"

    # RINm5F cell
    BTO_0001185 = "BTO_0001185"
    RINM5F_CELL = "BTO_0001185"

    # receptacle
    BTO_0001186 = "BTO_0001186"
    RECEPTACLE = "BTO_0001186"

    # roe
    BTO_0001187 = "BTO_0001187"
    ROE = "BTO_0001187"

    # root
    BTO_0001188 = "BTO_0001188"
    ROOT = "BTO_0001188"

    # FAZA cell
    BTO_0001189 = "BTO_0001189"
    FAZA_CELL = "BTO_0001189"

    # root nodule
    BTO_0001190 = "BTO_0001190"
    ROOT_NODULE = "BTO_0001190"

    # root tip
    BTO_0001191 = "BTO_0001191"
    ROOT_TIP = "BTO_0001191"

    # rootlet
    BTO_0001192 = "BTO_0001192"
    ROOTLET = "BTO_0001192"

    # C-127 cell
    BTO_0001193 = "BTO_0001193"
    C_127_CELL = "BTO_0001193"

    # rumen
    BTO_0001194 = "BTO_0001194"
    RUMEN = "BTO_0001194"

    # rumen epithelium
    BTO_0001195 = "BTO_0001195"
    RUMEN_EPITHELIUM = "BTO_0001195"

    # SF-21 cell
    BTO_0001196 = "BTO_0001196"
    SF_21_CELL = "BTO_0001196"

    # S-180 cell
    BTO_0001197 = "BTO_0001197"
    S_180_CELL = "BTO_0001197"

    # atrial gland
    BTO_0001198 = "BTO_0001198"
    ATRIAL_GLAND = "BTO_0001198"

    # EBTr (NBL-4) cell
    BTO_0001199 = "BTO_0001199"
    EBTR__NBL_4__CELL = "BTO_0001199"

    # aorta thoracica smooth muscle cell line
    BTO_0001200 = "BTO_0001200"
    AORTA_THORACICA_SMOOTH_MUSCLE_CELL_LINE = "BTO_0001200"

    # rosette
    BTO_0001201 = "BTO_0001201"
    ROSETTE = "BTO_0001201"

    # saliva
    BTO_0001202 = "BTO_0001202"
    SALIVA = "BTO_0001202"

    # salivary gland
    BTO_0001203 = "BTO_0001203"
    SALIVARY_GLAND = "BTO_0001203"

    # salt gland
    BTO_0001204 = "BTO_0001204"
    SALT_GLAND = "BTO_0001204"

    # RT4-D6P2T cell
    BTO_0001205 = "BTO_0001205"
    RT4_D6P2T_CELL = "BTO_0001205"

    # sarcocarp
    BTO_0001206 = "BTO_0001206"
    SARCOCARP = "BTO_0001206"

    # sarcoma cell
    BTO_0001207 = "BTO_0001207"
    SARCOMA_CELL = "BTO_0001207"

    # larynx
    BTO_0001208 = "BTO_0001208"
    LARYNX = "BTO_0001208"

    # umbilical cord cell line
    BTO_0001209 = "BTO_0001209"
    UMBILICAL_CORD_CELL_LINE = "BTO_0001209"

    # SGS cell
    BTO_0001210 = "BTO_0001210"
    SGS_CELL = "BTO_0001210"

    # breast epithelial cell
    BTO_0001211 = "BTO_0001211"
    BREAST_EPITHELIAL_CELL = "BTO_0001211"

    # Rous sarcoma cell
    BTO_0001212 = "BTO_0001212"
    ROUS_SARCOMA_CELL = "BTO_0001212"

    # Yoshida ascites sarcoma cell
    BTO_0001213 = "BTO_0001213"
    YOSHIDA_ASCITES_SARCOMA_CELL = "BTO_0001213"

    # Yoshida sarcoma cell
    BTO_0001214 = "BTO_0001214"
    YOSHIDA_SARCOMA_CELL = "BTO_0001214"

    # sartorius
    BTO_0001215 = "BTO_0001215"
    SARTORIUS = "BTO_0001215"

    # Schwann cell line
    BTO_0001216 = "BTO_0001216"
    SCHWANN_CELL_LINE = "BTO_0001216"

    # scape
    BTO_0001217 = "BTO_0001217"
    SCAPE = "BTO_0001217"

    # scapula
    BTO_0001218 = "BTO_0001218"
    SCAPULA = "BTO_0001218"

    # MEB-4 cell
    BTO_0001219 = "BTO_0001219"
    MEB_4_CELL = "BTO_0001219"

    # Schwann cell
    BTO_0001220 = "BTO_0001220"
    SCHWANN_CELL = "BTO_0001220"

    # sciatic nerve
    BTO_0001221 = "BTO_0001221"
    SCIATIC_NERVE = "BTO_0001221"

    # sclerenchyma
    BTO_0001222 = "BTO_0001222"
    SCLERENCHYMA = "BTO_0001222"

    # scutellum
    BTO_0001223 = "BTO_0001223"
    SCUTELLUM = "BTO_0001223"

    # second instar larva
    BTO_0001224 = "BTO_0001224"
    SECOND_INSTAR_LARVA = "BTO_0001224"

    # MKN-45 cell
    BTO_0001225 = "BTO_0001225"
    MKN_45_CELL = "BTO_0001225"

    # seed
    BTO_0001226 = "BTO_0001226"
    SEED = "BTO_0001226"

    # seed coat
    BTO_0001227 = "BTO_0001227"
    SEED_COAT = "BTO_0001227"

    # seedling
    BTO_0001228 = "BTO_0001228"
    SEEDLING = "BTO_0001228"

    # IMR-90 cell
    BTO_0001229 = "BTO_0001229"
    IMR_90_CELL = "BTO_0001229"

    # semen
    BTO_0001230 = "BTO_0001230"
    SEMEN = "BTO_0001230"

    # trigeminal ganglion
    BTO_0001231 = "BTO_0001231"
    TRIGEMINAL_GANGLION = "BTO_0001231"

    # seminal plasma
    BTO_0001232 = "BTO_0001232"
    SEMINAL_PLASMA = "BTO_0001232"

    # plant embryo
    BTO_0001233 = "BTO_0001233"
    PLANT_EMBRYO = "BTO_0001233"

    # seminal vesicle
    BTO_0001234 = "BTO_0001234"
    SEMINAL_VESICLE = "BTO_0001234"

    # seminiferous tubule
    BTO_0001235 = "BTO_0001235"
    SEMINIFEROUS_TUBULE = "BTO_0001235"

    # semitendinosus
    BTO_0001236 = "BTO_0001236"
    SEMITENDINOSUS = "BTO_0001236"

    # sensillum
    BTO_0001237 = "BTO_0001237"
    SENSILLUM = "BTO_0001237"

    # Sertoli cell
    BTO_0001238 = "BTO_0001238"
    SERTOLI_CELL = "BTO_0001238"

    # serum
    BTO_0001239 = "BTO_0001239"
    SERUM = "BTO_0001239"

    # SF-9 cell
    BTO_0001240 = "BTO_0001240"
    SF_9_CELL = "BTO_0001240"

    # shell gland
    BTO_0001241 = "BTO_0001241"
    SHELL_GLAND = "BTO_0001241"

    # fetal cell line
    BTO_0001242 = "BTO_0001242"
    FETAL_CELL_LINE = "BTO_0001242"

    # shoot
    BTO_0001243 = "BTO_0001243"
    SHOOT = "BTO_0001243"

    # urinary tract
    BTO_0001244 = "BTO_0001244"
    URINARY_TRACT = "BTO_0001244"

    # bronchoalveolar stem cell
    BTO_0001245 = "BTO_0001245"
    BRONCHOALVEOLAR_STEM_CELL = "BTO_0001245"

    # flexor digitorum profundus
    BTO_0001246 = "BTO_0001246"
    FLEXOR_DIGITORUM_PROFUNDUS = "BTO_0001246"

    # sieve tube
    BTO_0001247 = "BTO_0001247"
    SIEVE_TUBE = "BTO_0001247"

    # T-47D cell
    BTO_0001248 = "BTO_0001248"
    T_47D_CELL = "BTO_0001248"

    # silique
    BTO_0001249 = "BTO_0001249"
    SILIQUE = "BTO_0001249"

    # silk gland
    BTO_0001250 = "BTO_0001250"
    SILK_GLAND = "BTO_0001250"

    # liver sinusoidal endothelial cell
    BTO_0001251 = "BTO_0001251"
    LIVER_SINUSOIDAL_ENDOTHELIAL_CELL = "BTO_0001251"

    # tibia
    BTO_0001252 = "BTO_0001252"
    TIBIA = "BTO_0001252"

    # skin
    BTO_0001253 = "BTO_0001253"
    SKIN = "BTO_0001253"

    # sweat
    BTO_0001254 = "BTO_0001254"
    SWEAT = "BTO_0001254"

    # skin fibroblast
    BTO_0001255 = "BTO_0001255"
    SKIN_FIBROBLAST = "BTO_0001255"

    # parasympathetic ganglion
    BTO_0001256 = "BTO_0001256"
    PARASYMPATHETIC_GANGLION = "BTO_0001256"

    # flexor
    BTO_0001257 = "BTO_0001257"
    FLEXOR = "BTO_0001257"

    # small intestine epithelium
    BTO_0001258 = "BTO_0001258"
    SMALL_INTESTINE_EPITHELIUM = "BTO_0001258"

    # small intestine mucosa
    BTO_0001259 = "BTO_0001259"
    SMALL_INTESTINE_MUCOSA = "BTO_0001259"

    # smooth muscle
    BTO_0001260 = "BTO_0001260"
    SMOOTH_MUSCLE = "BTO_0001260"

    # abdominal muscle
    BTO_0001261 = "BTO_0001261"
    ABDOMINAL_MUSCLE = "BTO_0001261"

    # soft body part
    BTO_0001262 = "BTO_0001262"
    SOFT_BODY_PART = "BTO_0001262"

    # Friend erythroleukemia cell line
    BTO_0001263 = "BTO_0001263"
    FRIEND_ERYTHROLEUKEMIA_CELL_LINE = "BTO_0001263"

    # spinal ganglion
    BTO_0001264 = "BTO_0001264"
    SPINAL_GANGLION = "BTO_0001264"

    # soleus
    BTO_0001265 = "BTO_0001265"
    SOLEUS = "BTO_0001265"

    # invertebrate muscular system
    BTO_0001266 = "BTO_0001266"
    INVERTEBRATE_MUSCULAR_SYSTEM = "BTO_0001266"

    # BmN cell
    BTO_0001267 = "BTO_0001267"
    BMN_CELL = "BTO_0001267"

    # somatic cell
    BTO_0001268 = "BTO_0001268"
    SOMATIC_CELL = "BTO_0001268"

    # spadix
    BTO_0001269 = "BTO_0001269"
    SPADIX = "BTO_0001269"

    # spear
    BTO_0001270 = "BTO_0001270"
    SPEAR = "BTO_0001270"

    # leukemia cell
    BTO_0001271 = "BTO_0001271"
    LEUKEMIA_CELL = "BTO_0001271"

    # sperm flagellum
    BTO_0001272 = "BTO_0001272"
    SPERM_FLAGELLUM = "BTO_0001272"

    # spermatheca
    BTO_0001273 = "BTO_0001273"
    SPERMATHECA = "BTO_0001273"

    # spermatid
    BTO_0001274 = "BTO_0001274"
    SPERMATID = "BTO_0001274"

    # spermatocyte
    BTO_0001275 = "BTO_0001275"
    SPERMATOCYTE = "BTO_0001275"

    # pollen tube
    BTO_0001276 = "BTO_0001276"
    POLLEN_TUBE = "BTO_0001276"

    # spermatozoon
    BTO_0001277 = "BTO_0001277"
    SPERMATOZOON = "BTO_0001277"

    # spike
    BTO_0001278 = "BTO_0001278"
    SPIKE = "BTO_0001278"

    # spinal cord
    BTO_0001279 = "BTO_0001279"
    SPINAL_CORD = "BTO_0001279"

    # BmN4-IR cell
    BTO_0001280 = "BTO_0001280"
    BMN4_IR_CELL = "BTO_0001280"

    # spleen
    BTO_0001281 = "BTO_0001281"
    SPLEEN = "BTO_0001281"

    # HT-1080 cell
    BTO_0001282 = "BTO_0001282"
    HT_1080_CELL = "BTO_0001282"

    # mitral cell
    BTO_0001283 = "BTO_0001283"
    MITRAL_CELL = "BTO_0001283"

    # femur
    BTO_0001284 = "BTO_0001284"
    FEMUR = "BTO_0001284"

    # sporangiophore
    BTO_0001285 = "BTO_0001285"
    SPORANGIOPHORE = "BTO_0001285"

    # skin cancer cell
    BTO_0001286 = "BTO_0001286"
    SKIN_CANCER_CELL = "BTO_0001286"

    # sporangium
    BTO_0001287 = "BTO_0001287"
    SPORANGIUM = "BTO_0001287"

    # adductor brevis
    BTO_0001288 = "BTO_0001288"
    ADDUCTOR_BREVIS = "BTO_0001288"

    # squamous cell carcinoma cell
    BTO_0001289 = "BTO_0001289"
    SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0001289"

    # sporocarp
    BTO_0001290 = "BTO_0001290"
    SPOROCARP = "BTO_0001290"

    # sporophore
    BTO_0001291 = "BTO_0001291"
    SPOROPHORE = "BTO_0001291"

    # sporozoite
    BTO_0001292 = "BTO_0001292"
    SPOROZOITE = "BTO_0001292"

    # sporulated oocyst
    BTO_0001293 = "BTO_0001293"
    SPORULATED_OOCYST = "BTO_0001293"

    # sporulating cell
    BTO_0001294 = "BTO_0001294"
    SPORULATING_CELL = "BTO_0001294"

    # cranium
    BTO_0001295 = "BTO_0001295"
    CRANIUM = "BTO_0001295"

    # sprout
    BTO_0001296 = "BTO_0001296"
    SPROUT = "BTO_0001296"

    # sputum
    BTO_0001297 = "BTO_0001297"
    SPUTUM = "BTO_0001297"

    # basal cell carcinoma cell
    BTO_0001298 = "BTO_0001298"
    BASAL_CELL_CARCINOMA_CELL = "BTO_0001298"

    # stele
    BTO_0001299 = "BTO_0001299"
    STELE = "BTO_0001299"

    # stem
    BTO_0001300 = "BTO_0001300"
    STEM = "BTO_0001300"

    # bark
    BTO_0001301 = "BTO_0001301"
    BARK = "BTO_0001301"

    # sternum
    BTO_0001302 = "BTO_0001302"
    STERNUM = "BTO_0001302"

    # stigma
    BTO_0001303 = "BTO_0001303"
    STIGMA = "BTO_0001303"

    # stipe
    BTO_0001304 = "BTO_0001304"
    STIPE = "BTO_0001304"

    # stipule
    BTO_0001305 = "BTO_0001305"
    STIPULE = "BTO_0001305"

    # stolon
    BTO_0001306 = "BTO_0001306"
    STOLON = "BTO_0001306"

    # stomach
    BTO_0001307 = "BTO_0001307"
    STOMACH = "BTO_0001307"

    # gastric mucosa
    BTO_0001308 = "BTO_0001308"
    GASTRIC_MUCOSA = "BTO_0001308"

    # tuberous root
    BTO_0001309 = "BTO_0001309"
    TUBEROUS_ROOT = "BTO_0001309"

    # storage tissue
    BTO_0001310 = "BTO_0001310"
    STORAGE_TISSUE = "BTO_0001310"

    # corpus striatum
    BTO_0001311 = "BTO_0001311"
    CORPUS_STRIATUM = "BTO_0001311"

    # adductor magnus
    BTO_0001312 = "BTO_0001312"
    ADDUCTOR_MAGNUS = "BTO_0001312"

    # style
    BTO_0001313 = "BTO_0001313"
    STYLE = "BTO_0001313"

    # subcutis
    BTO_0001314 = "BTO_0001314"
    SUBCUTIS = "BTO_0001314"

    # sublingual gland
    BTO_0001315 = "BTO_0001315"
    SUBLINGUAL_GLAND = "BTO_0001315"

    # submandibular gland
    BTO_0001316 = "BTO_0001316"
    SUBMANDIBULAR_GLAND = "BTO_0001316"

    # glomerular layer
    BTO_0001317 = "BTO_0001317"
    GLOMERULAR_LAYER = "BTO_0001317"

    # submandibular ganglion
    BTO_0001318 = "BTO_0001318"
    SUBMANDIBULAR_GANGLION = "BTO_0001318"

    # external plexiform layer
    BTO_0001319 = "BTO_0001319"
    EXTERNAL_PLEXIFORM_LAYER = "BTO_0001319"

    # internal plexiform layer
    BTO_0001320 = "BTO_0001320"
    INTERNAL_PLEXIFORM_LAYER = "BTO_0001320"

    # LNCaP cell
    BTO_0001321 = "BTO_0001321"
    LNCAP_CELL = "BTO_0001321"

    # culture condition:succinate-grown cell
    BTO_0001322 = "BTO_0001322"
    CULTURE_CONDITION_SUCCINATE_GROWN_CELL = "BTO_0001322"

    # BPH-1 cell
    BTO_0001323 = "BTO_0001323"
    BPH_1_CELL = "BTO_0001323"

    # culture condition:sulfate-grown cell
    BTO_0001324 = "BTO_0001324"
    CULTURE_CONDITION_SULFATE_GROWN_CELL = "BTO_0001324"

    # superior cervical ganglion
    BTO_0001325 = "BTO_0001325"
    SUPERIOR_CERVICAL_GANGLION = "BTO_0001325"

    # cholangiocarcinoma cell
    BTO_0001326 = "BTO_0001326"
    CHOLANGIOCARCINOMA_CELL = "BTO_0001326"

    # granule cell layer
    BTO_0001327 = "BTO_0001327"
    GRANULE_CELL_LAYER = "BTO_0001327"

    # calvarium
    BTO_0001328 = "BTO_0001328"
    CALVARIUM = "BTO_0001328"

    # gastrinoma cell
    BTO_0001329 = "BTO_0001329"
    GASTRINOMA_CELL = "BTO_0001329"

    # hepatoma ascites cell
    BTO_0001330 = "BTO_0001330"
    HEPATOMA_ASCITES_CELL = "BTO_0001330"

    # sweat gland
    BTO_0001331 = "BTO_0001331"
    SWEAT_GLAND = "BTO_0001331"

    # DU-145 cell
    BTO_0001332 = "BTO_0001332"
    DU_145_CELL = "BTO_0001332"

    # sympathetic ganglion
    BTO_0001333 = "BTO_0001333"
    SYMPATHETIC_GANGLION = "BTO_0001333"

    # papilloma cell
    BTO_0001334 = "BTO_0001334"
    PAPILLOMA_CELL = "BTO_0001334"

    # syncytiotrophoblast
    BTO_0001335 = "BTO_0001335"
    SYNCYTIOTROPHOBLAST = "BTO_0001335"

    # synovial fibroblast
    BTO_0001336 = "BTO_0001336"
    SYNOVIAL_FIBROBLAST = "BTO_0001336"

    # extensor digitorum brevis
    BTO_0001337 = "BTO_0001337"
    EXTENSOR_DIGITORUM_BREVIS = "BTO_0001337"

    # synovial tissue
    BTO_0001338 = "BTO_0001338"
    SYNOVIAL_TISSUE = "BTO_0001338"

    # synovia
    BTO_0001339 = "BTO_0001339"
    SYNOVIA = "BTO_0001339"

    # bronchus
    BTO_0001340 = "BTO_0001340"
    BRONCHUS = "BTO_0001340"

    # S-49 cell
    BTO_0001341 = "BTO_0001341"
    S_49_CELL = "BTO_0001341"

    # A3 cell
    BTO_0001342 = "BTO_0001342"
    A3_CELL = "BTO_0001342"

    # extensor digitorum communis
    BTO_0001343 = "BTO_0001343"
    EXTENSOR_DIGITORUM_COMMUNIS = "BTO_0001343"

    # adult T-cell lymphoma cell
    BTO_0001344 = "BTO_0001344"
    ADULT_T_CELL_LYMPHOMA_CELL = "BTO_0001344"

    # T-24 cell
    BTO_0001345 = "BTO_0001345"
    T_24_CELL = "BTO_0001345"

    # tachyzoite
    BTO_0001346 = "BTO_0001346"
    TACHYZOITE = "BTO_0001346"

    # tadpole
    BTO_0001347 = "BTO_0001347"
    TADPOLE = "BTO_0001347"

    # tail
    BTO_0001348 = "BTO_0001348"
    TAIL = "BTO_0001348"

    # NRP-152 cell
    BTO_0001349 = "BTO_0001349"
    NRP_152_CELL = "BTO_0001349"

    # tapetum
    BTO_0001350 = "BTO_0001350"
    TAPETUM = "BTO_0001350"

    # vomeronasal nerve
    BTO_0001351 = "BTO_0001351"
    VOMERONASAL_NERVE = "BTO_0001351"

    # NRP-154 cell
    BTO_0001352 = "BTO_0001352"
    NRP_154_CELL = "BTO_0001352"

    # telson
    BTO_0001353 = "BTO_0001353"
    TELSON = "BTO_0001353"

    # telson muscle
    BTO_0001354 = "BTO_0001354"
    TELSON_MUSCLE = "BTO_0001354"

    # temporal lobe
    BTO_0001355 = "BTO_0001355"
    TEMPORAL_LOBE = "BTO_0001355"

    # tendon
    BTO_0001356 = "BTO_0001356"
    TENDON = "BTO_0001356"

    # tentacle
    BTO_0001357 = "BTO_0001357"
    TENTACLE = "BTO_0001357"

    # culture condition:terephthalate-grown cell
    BTO_0001358 = "BTO_0001358"
    CULTURE_CONDITION_TEREPHTHALATE_GROWN_CELL = "BTO_0001358"

    # medulloblastoma cell line
    BTO_0001359 = "BTO_0001359"
    MEDULLOBLASTOMA_CELL_LINE = "BTO_0001359"

    # decidua
    BTO_0001360 = "BTO_0001360"
    DECIDUA = "BTO_0001360"

    # CMT93/69 cell
    BTO_0001361 = "BTO_0001361"
    CMT93_69_CELL = "BTO_0001361"

    # olfactory lobe
    BTO_0001362 = "BTO_0001362"
    OLFACTORY_LOBE = "BTO_0001362"

    # testis
    BTO_0001363 = "BTO_0001363"
    TESTIS = "BTO_0001363"

    # testis sheath
    BTO_0001364 = "BTO_0001364"
    TESTIS_SHEATH = "BTO_0001364"

    # thalamus
    BTO_0001365 = "BTO_0001365"
    THALAMUS = "BTO_0001365"

    # thallus
    BTO_0001366 = "BTO_0001366"
    THALLUS = "BTO_0001366"

    # thigh muscle
    BTO_0001367 = "BTO_0001367"
    THIGH_MUSCLE = "BTO_0001367"

    # thorax
    BTO_0001368 = "BTO_0001368"
    THORAX = "BTO_0001368"

    # vertebrate muscular system
    BTO_0001369 = "BTO_0001369"
    VERTEBRATE_MUSCULAR_SYSTEM = "BTO_0001369"

    # THP-1 cell
    BTO_0001370 = "BTO_0001370"
    THP_1_CELL = "BTO_0001370"

    # iris dilator muscle
    BTO_0001371 = "BTO_0001371"
    IRIS_DILATOR_MUSCLE = "BTO_0001371"

    # thymocyte
    BTO_0001372 = "BTO_0001372"
    THYMOCYTE = "BTO_0001372"

    # amnion epithelial cell line
    BTO_0001373 = "BTO_0001373"
    AMNION_EPITHELIAL_CELL_LINE = "BTO_0001373"

    # thymus
    BTO_0001374 = "BTO_0001374"
    THYMUS = "BTO_0001374"

    # mandibular nerve
    BTO_0001375 = "BTO_0001375"
    MANDIBULAR_NERVE = "BTO_0001375"

    # thigh
    BTO_0001376 = "BTO_0001376"
    THIGH = "BTO_0001376"

    # thymus lymphoma cell line
    BTO_0001377 = "BTO_0001377"
    THYMUS_LYMPHOMA_CELL_LINE = "BTO_0001377"

    # maxillary nerve
    BTO_0001378 = "BTO_0001378"
    MAXILLARY_NERVE = "BTO_0001378"

    # thyroid gland
    BTO_0001379 = "BTO_0001379"
    THYROID_GLAND = "BTO_0001379"

    # mesentery
    BTO_0001380 = "BTO_0001380"
    MESENTERY = "BTO_0001380"

    # tibial chondrocyte
    BTO_0001381 = "BTO_0001381"
    TIBIAL_CHONDROCYTE = "BTO_0001381"

    # tibialis anterior
    BTO_0001382 = "BTO_0001382"
    TIBIALIS_ANTERIOR = "BTO_0001382"

    # alveolar bone
    BTO_0001383 = "BTO_0001383"
    ALVEOLAR_BONE = "BTO_0001383"

    # culture condition:tissue culture
    BTO_0001384 = "BTO_0001384"
    CULTURE_CONDITION_TISSUE_CULTURE = "BTO_0001384"

    # tongue
    BTO_0001385 = "BTO_0001385"
    TONGUE = "BTO_0001385"

    # tongue muscle
    BTO_0001386 = "BTO_0001386"
    TONGUE_MUSCLE = "BTO_0001386"

    # tonsil
    BTO_0001387 = "BTO_0001387"
    TONSIL = "BTO_0001387"

    # trachea
    BTO_0001388 = "BTO_0001388"
    TRACHEA = "BTO_0001388"

    # tracheal epithelium
    BTO_0001389 = "BTO_0001389"
    TRACHEAL_EPITHELIUM = "BTO_0001389"

    # tracheal mucosa
    BTO_0001390 = "BTO_0001390"
    TRACHEAL_MUCOSA = "BTO_0001390"

    # tracheal smooth muscle
    BTO_0001391 = "BTO_0001391"
    TRACHEAL_SMOOTH_MUSCLE = "BTO_0001391"

    # culture condition:trans-aconitate-grown cell
    BTO_0001392 = "BTO_0001392"
    CULTURE_CONDITION_TRANS_ACONITATE_GROWN_CELL = "BTO_0001392"

    # mesenchyme
    BTO_0001393 = "BTO_0001393"
    MESENCHYME = "BTO_0001393"

    # trapping leaf
    BTO_0001394 = "BTO_0001394"
    TRAPPING_LEAF = "BTO_0001394"

    # trichome
    BTO_0001395 = "BTO_0001395"
    TRICHOME = "BTO_0001395"

    # trophosome tissue
    BTO_0001396 = "BTO_0001396"
    TROPHOSOME_TISSUE = "BTO_0001396"

    # trophozoite
    BTO_0001397 = "BTO_0001397"
    TROPHOZOITE = "BTO_0001397"

    # trypomastigote
    BTO_0001398 = "BTO_0001398"
    TRYPOMASTIGOTE = "BTO_0001398"

    # Tay-Sachs disease specific cell type
    BTO_0001399 = "BTO_0001399"
    TAY_SACHS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0001399"

    # tuber
    BTO_0001400 = "BTO_0001400"
    TUBER = "BTO_0001400"

    # tuber cortex
    BTO_0001401 = "BTO_0001401"
    TUBER_CORTEX = "BTO_0001401"

    # urogenital ridge
    BTO_0001402 = "BTO_0001402"
    UROGENITAL_RIDGE = "BTO_0001402"

    # gastrula
    BTO_0001403 = "BTO_0001403"
    GASTRULA = "BTO_0001403"

    # Yoshida ascites hepatoma cell line
    BTO_0001404 = "BTO_0001404"
    YOSHIDA_ASCITES_HEPATOMA_CELL_LINE = "BTO_0001404"

    # bronchial cancer cell
    BTO_0001405 = "BTO_0001405"
    BRONCHIAL_CANCER_CELL = "BTO_0001405"

    # HT-144 cell
    BTO_0001406 = "BTO_0001406"
    HT_144_CELL = "BTO_0001406"

    # neuroendocrine tumor cell
    BTO_0001407 = "BTO_0001407"
    NEUROENDOCRINE_TUMOR_CELL = "BTO_0001407"

    # locus ceruleus
    BTO_0001408 = "BTO_0001408"
    LOCUS_CERULEUS = "BTO_0001408"

    # ureter
    BTO_0001409 = "BTO_0001409"
    URETER = "BTO_0001409"

    # GH3 cell
    BTO_0001410 = "BTO_0001410"
    GH3_CELL = "BTO_0001410"

    # twig
    BTO_0001411 = "BTO_0001411"
    TWIG = "BTO_0001411"

    # U-937 cell
    BTO_0001412 = "BTO_0001412"
    U_937_CELL = "BTO_0001412"

    # primary cell
    BTO_0001413 = "BTO_0001413"
    PRIMARY_CELL = "BTO_0001413"

    # umbilical cord
    BTO_0001415 = "BTO_0001415"
    UMBILICAL_CORD = "BTO_0001415"

    # umbilical vein endothelium
    BTO_0001416 = "BTO_0001416"
    UMBILICAL_VEIN_ENDOTHELIUM = "BTO_0001416"

    # uredospore
    BTO_0001417 = "BTO_0001417"
    UREDOSPORE = "BTO_0001417"

    # urinary bladder
    BTO_0001418 = "BTO_0001418"
    URINARY_BLADDER = "BTO_0001418"

    # urine
    BTO_0001419 = "BTO_0001419"
    URINE = "BTO_0001419"

    # uropygial gland
    BTO_0001420 = "BTO_0001420"
    UROPYGIAL_GLAND = "BTO_0001420"

    # uterine cervix
    BTO_0001421 = "BTO_0001421"
    UTERINE_CERVIX = "BTO_0001421"

    # uterine endometrium
    BTO_0001422 = "BTO_0001422"
    UTERINE_ENDOMETRIUM = "BTO_0001422"

    # uterine lavage
    BTO_0001423 = "BTO_0001423"
    UTERINE_LAVAGE = "BTO_0001423"

    # uterus
    BTO_0001424 = "BTO_0001424"
    UTERUS = "BTO_0001424"

    # V-79 cell
    BTO_0001425 = "BTO_0001425"
    V_79_CELL = "BTO_0001425"

    # urethra
    BTO_0001426 = "BTO_0001426"
    URETHRA = "BTO_0001426"

    # vas deferens
    BTO_0001427 = "BTO_0001427"
    VAS_DEFERENS = "BTO_0001427"

    # breast epithelium
    BTO_0001428 = "BTO_0001428"
    BREAST_EPITHELIUM = "BTO_0001428"

    # vascular bundle
    BTO_0001429 = "BTO_0001429"
    VASCULAR_BUNDLE = "BTO_0001429"

    # mammary epithelium
    BTO_0001430 = "BTO_0001430"
    MAMMARY_EPITHELIUM = "BTO_0001430"

    # vascular smooth muscle
    BTO_0001431 = "BTO_0001431"
    VASCULAR_SMOOTH_MUSCLE = "BTO_0001431"

    # vascular tissue
    BTO_0001432 = "BTO_0001432"
    VASCULAR_TISSUE = "BTO_0001432"

    # mononuclear phagocyte
    BTO_0001433 = "BTO_0001433"
    MONONUCLEAR_PHAGOCYTE = "BTO_0001433"

    # vegetative cell
    BTO_0001434 = "BTO_0001434"
    VEGETATIVE_CELL = "BTO_0001434"

    # arm
    BTO_0001435 = "BTO_0001435"
    ARM = "BTO_0001435"

    # mycelium
    BTO_0001436 = "BTO_0001436"
    MYCELIUM = "BTO_0001436"

    # embryonic carcinoma cell line
    BTO_0001437 = "BTO_0001437"
    EMBRYONIC_CARCINOMA_CELL_LINE = "BTO_0001437"

    # vena cava
    BTO_0001438 = "BTO_0001438"
    VENA_CAVA = "BTO_0001438"

    # venom
    BTO_0001439 = "BTO_0001439"
    VENOM = "BTO_0001439"

    # venom gland
    BTO_0001440 = "BTO_0001440"
    VENOM_GLAND = "BTO_0001440"

    # marrow cell
    BTO_0001441 = "BTO_0001441"
    MARROW_CELL = "BTO_0001441"

    # brain ventricle
    BTO_0001442 = "BTO_0001442"
    BRAIN_VENTRICLE = "BTO_0001442"

    # culture condition:veratryl alcohol-grown cell
    BTO_0001443 = "BTO_0001443"
    CULTURE_CONDITION_VERATRYL_ALCOHOL_GROWN_CELL = "BTO_0001443"

    # Vero cell
    BTO_0001444 = "BTO_0001444"
    VERO_CELL = "BTO_0001444"

    # tail bud
    BTO_0001445 = "BTO_0001445"
    TAIL_BUD = "BTO_0001445"

    # olfactory cortex
    BTO_0001446 = "BTO_0001446"
    OLFACTORY_CORTEX = "BTO_0001446"

    # forearm
    BTO_0001447 = "BTO_0001447"
    FOREARM = "BTO_0001447"

    # visceral hump
    BTO_0001448 = "BTO_0001448"
    VISCERAL_HUMP = "BTO_0001448"

    # gall bladder epithelium
    BTO_0001449 = "BTO_0001449"
    GALL_BLADDER_EPITHELIUM = "BTO_0001449"

    # vitelline membrane
    BTO_0001450 = "BTO_0001450"
    VITELLINE_MEMBRANE = "BTO_0001450"

    # vitreous humor
    BTO_0001451 = "BTO_0001451"
    VITREOUS_HUMOR = "BTO_0001451"

    # nasal nerve
    BTO_0001452 = "BTO_0001452"
    NASAL_NERVE = "BTO_0001452"

    # detrusor
    BTO_0001453 = "BTO_0001453"
    DETRUSOR = "BTO_0001453"

    # thymoma cell
    BTO_0001454 = "BTO_0001454"
    THYMOMA_CELL = "BTO_0001454"

    # thymic carcinoma cell
    BTO_0001455 = "BTO_0001455"
    THYMIC_CARCINOMA_CELL = "BTO_0001455"

    # white adipose tissue
    BTO_0001456 = "BTO_0001456"
    WHITE_ADIPOSE_TISSUE = "BTO_0001456"

    # hip
    BTO_0001457 = "BTO_0001457"
    HIP = "BTO_0001457"

    # apocrine sweat gland
    BTO_0001458 = "BTO_0001458"
    APOCRINE_SWEAT_GLAND = "BTO_0001458"

    # white prepupa
    BTO_0001459 = "BTO_0001459"
    WHITE_PREPUPA = "BTO_0001459"

    # thymic cancer cell
    BTO_0001460 = "BTO_0001460"
    THYMIC_CANCER_CELL = "BTO_0001460"

    # whole plant
    BTO_0001461 = "BTO_0001461"
    WHOLE_PLANT = "BTO_0001461"

    # bladder wall
    BTO_0001462 = "BTO_0001462"
    BLADDER_WALL = "BTO_0001462"

    # wing
    BTO_0001463 = "BTO_0001463"
    WING = "BTO_0001463"

    # wing disc
    BTO_0001464 = "BTO_0001464"
    WING_DISC = "BTO_0001464"

    # pericycle
    BTO_0001465 = "BTO_0001465"
    PERICYCLE = "BTO_0001465"

    # BT-20 cell
    BTO_0001466 = "BTO_0001466"
    BT_20_CELL = "BTO_0001466"

    # mesocotyl
    BTO_0001467 = "BTO_0001467"
    MESOCOTYL = "BTO_0001467"

    # xylem
    BTO_0001468 = "BTO_0001468"
    XYLEM = "BTO_0001468"

    # culture condition:xylose-grown cell
    BTO_0001469 = "BTO_0001469"
    CULTURE_CONDITION_XYLOSE_GROWN_CELL = "BTO_0001469"

    # epidermal cell
    BTO_0001470 = "BTO_0001470"
    EPIDERMAL_CELL = "BTO_0001470"

    # yolk sac
    BTO_0001471 = "BTO_0001471"
    YOLK_SAC = "BTO_0001471"

    # peritoneum
    BTO_0001472 = "BTO_0001472"
    PERITONEUM = "BTO_0001472"

    # blastomere
    BTO_0001473 = "BTO_0001473"
    BLASTOMERE = "BTO_0001473"

    # yolk sac erythroid cell
    BTO_0001474 = "BTO_0001474"
    YOLK_SAC_ERYTHROID_CELL = "BTO_0001474"

    # zoospore
    BTO_0001475 = "BTO_0001475"
    ZOOSPORE = "BTO_0001475"

    # mitotic cell
    BTO_0001476 = "BTO_0001476"
    MITOTIC_CELL = "BTO_0001476"

    # photophore
    BTO_0001477 = "BTO_0001477"
    PHOTOPHORE = "BTO_0001477"

    # zygotene cell
    BTO_0001478 = "BTO_0001478"
    ZYGOTENE_CELL = "BTO_0001478"

    # culture condition:-grown cell
    BTO_0001479 = "BTO_0001479"
    CULTURE_CONDITION__GROWN_CELL = "BTO_0001479"

    # Meynert's basal nucleus
    BTO_0001480 = "BTO_0001480"
    MEYNERT_S_BASAL_NUCLEUS = "BTO_0001480"

    # plant
    BTO_0001481 = "BTO_0001481"
    PLANT = "BTO_0001481"

    # CTLL-2 cell
    BTO_0001482 = "BTO_0001482"
    CTLL_2_CELL = "BTO_0001482"

    # WiDr cell
    BTO_0001483 = "BTO_0001483"
    WIDR_CELL = "BTO_0001483"

    # nervous system
    BTO_0001484 = "BTO_0001484"
    NERVOUS_SYSTEM = "BTO_0001484"

    # muscular system
    BTO_0001485 = "BTO_0001485"
    MUSCULAR_SYSTEM = "BTO_0001485"

    # skeletal system
    BTO_0001486 = "BTO_0001486"
    SKELETAL_SYSTEM = "BTO_0001486"

    # adipose tissue
    BTO_0001487 = "BTO_0001487"
    ADIPOSE_TISSUE = "BTO_0001487"

    # endocrine gland
    BTO_0001488 = "BTO_0001488"
    ENDOCRINE_GLAND = "BTO_0001488"

    # whole body
    BTO_0001489 = "BTO_0001489"
    WHOLE_BODY = "BTO_0001489"

    # other source
    BTO_0001490 = "BTO_0001490"
    OTHER_SOURCE = "BTO_0001490"

    # viscus
    BTO_0001491 = "BTO_0001491"
    VISCUS = "BTO_0001491"

    # limb
    BTO_0001492 = "BTO_0001492"
    LIMB = "BTO_0001492"

    # trunk
    BTO_0001493 = "BTO_0001493"
    TRUNK = "BTO_0001493"

    # fungus
    BTO_0001494 = "BTO_0001494"
    FUNGUS = "BTO_0001494"

    # plumule
    BTO_0001495 = "BTO_0001495"
    PLUMULE = "BTO_0001495"

    # perivascular astrocyte
    BTO_0001496 = "BTO_0001496"
    PERIVASCULAR_ASTROCYTE = "BTO_0001496"

    # IEC-6 cell
    BTO_0001497 = "BTO_0001497"
    IEC_6_CELL = "BTO_0001497"

    # renal proximal tubule
    BTO_0001498 = "BTO_0001498"
    RENAL_PROXIMAL_TUBULE = "BTO_0001498"

    # tear
    BTO_0001499 = "BTO_0001499"
    TEAR = "BTO_0001499"

    # tendril
    BTO_0001500 = "BTO_0001500"
    TENDRIL = "BTO_0001500"

    # hair
    BTO_0001501 = "BTO_0001501"
    HAIR = "BTO_0001501"

    # hip joint
    BTO_0001502 = "BTO_0001502"
    HIP_JOINT = "BTO_0001502"

    # thoracic leg
    BTO_0001503 = "BTO_0001503"
    THORACIC_LEG = "BTO_0001503"

    # blastodisc
    BTO_0001504 = "BTO_0001504"
    BLASTODISC = "BTO_0001504"

    # loin
    BTO_0001505 = "BTO_0001505"
    LOIN = "BTO_0001505"

    # radula
    BTO_0001506 = "BTO_0001506"
    RADULA = "BTO_0001506"

    # pes anserinus
    BTO_0001507 = "BTO_0001507"
    PES_ANSERINUS = "BTO_0001507"

    # morula
    BTO_0001508 = "BTO_0001508"
    MORULA = "BTO_0001508"

    # umbilical vein
    BTO_0001509 = "BTO_0001509"
    UMBILICAL_VEIN = "BTO_0001509"

    # rectal cell line
    BTO_0001510 = "BTO_0001510"
    RECTAL_CELL_LINE = "BTO_0001510"

    # tooth germ
    BTO_0001511 = "BTO_0001511"
    TOOTH_GERM = "BTO_0001511"

    # imago
    BTO_0001512 = "BTO_0001512"
    IMAGO = "BTO_0001512"

    # biliary epithelium
    BTO_0001513 = "BTO_0001513"
    BILIARY_EPITHELIUM = "BTO_0001513"

    # biliary epithelial cell
    BTO_0001514 = "BTO_0001514"
    BILIARY_EPITHELIAL_CELL = "BTO_0001514"

    # glomerular epithelium
    BTO_0001515 = "BTO_0001515"
    GLOMERULAR_EPITHELIUM = "BTO_0001515"

    # BA/F3 cell
    BTO_0001516 = "BTO_0001516"
    BA_F3_CELL = "BTO_0001516"

    # FAO cell
    BTO_0001517 = "BTO_0001517"
    FAO_CELL = "BTO_0001517"

    # B-cell lymphoma cell line
    BTO_0001518 = "BTO_0001518"
    B_CELL_LYMPHOMA_CELL_LINE = "BTO_0001518"

    # endothelial cell line
    BTO_0001519 = "BTO_0001519"
    ENDOTHELIAL_CELL_LINE = "BTO_0001519"

    # umbilical vein endothelial cell line
    BTO_0001520 = "BTO_0001520"
    UMBILICAL_VEIN_ENDOTHELIAL_CELL_LINE = "BTO_0001520"

    # pancreatic adenocarcinoma cell line
    BTO_0001521 = "BTO_0001521"
    PANCREATIC_ADENOCARCINOMA_CELL_LINE = "BTO_0001521"

    # B-lymphocyte cell line
    BTO_0001522 = "BTO_0001522"
    B_LYMPHOCYTE_CELL_LINE = "BTO_0001522"

    # WIL-2 cell
    BTO_0001523 = "BTO_0001523"
    WIL_2_CELL = "BTO_0001523"

    # WIL2-NS cell
    BTO_0001524 = "BTO_0001524"
    WIL2_NS_CELL = "BTO_0001524"

    # WIL2-S cell
    BTO_0001525 = "BTO_0001525"
    WIL2_S_CELL = "BTO_0001525"

    # renal medulla cell line
    BTO_0001526 = "BTO_0001526"
    RENAL_MEDULLA_CELL_LINE = "BTO_0001526"

    # PAP-HT25 cell
    BTO_0001527 = "BTO_0001527"
    PAP_HT25_CELL = "BTO_0001527"

    # B-lymphoblast
    BTO_0001528 = "BTO_0001528"
    B_LYMPHOBLAST = "BTO_0001528"

    # BSC-40 cell
    BTO_0001529 = "BTO_0001529"
    BSC_40_CELL = "BTO_0001529"

    # glioblastoma cell line
    BTO_0001530 = "BTO_0001530"
    GLIOBLASTOMA_CELL_LINE = "BTO_0001530"

    # glial cell line
    BTO_0001531 = "BTO_0001531"
    GLIAL_CELL_LINE = "BTO_0001531"

    # rectal cancer cell line
    BTO_0001532 = "BTO_0001532"
    RECTAL_CANCER_CELL_LINE = "BTO_0001532"

    # gastrointestinal cancer cell
    BTO_0001533 = "BTO_0001533"
    GASTROINTESTINAL_CANCER_CELL = "BTO_0001533"

    # SW-948 cell
    BTO_0001534 = "BTO_0001534"
    SW_948_CELL = "BTO_0001534"

    # SW-48 cell
    BTO_0001535 = "BTO_0001535"
    SW_48_CELL = "BTO_0001535"

    # SW-1417 cell
    BTO_0001536 = "BTO_0001536"
    SW_1417_CELL = "BTO_0001536"

    # small intestine cell line
    BTO_0001537 = "BTO_0001537"
    SMALL_INTESTINE_CELL_LINE = "BTO_0001537"

    # COS-1 cell
    BTO_0001538 = "BTO_0001538"
    COS_1_CELL = "BTO_0001538"

    # parenchyma
    BTO_0001539 = "BTO_0001539"
    PARENCHYMA = "BTO_0001539"

    # goblet cell
    BTO_0001540 = "BTO_0001540"
    GOBLET_CELL = "BTO_0001540"

    # pronephros
    BTO_0001541 = "BTO_0001541"
    PRONEPHROS = "BTO_0001541"

    # mesonephron
    BTO_0001542 = "BTO_0001542"
    MESONEPHRON = "BTO_0001542"

    # metanephron
    BTO_0001543 = "BTO_0001543"
    METANEPHRON = "BTO_0001543"

    # chronic myeloid leukemia cell
    BTO_0001544 = "BTO_0001544"
    CHRONIC_MYELOID_LEUKEMIA_CELL = "BTO_0001544"

    # acute myeloid leukemia cell
    BTO_0001545 = "BTO_0001545"
    ACUTE_MYELOID_LEUKEMIA_CELL = "BTO_0001545"

    # chronic lymphocytic leukemia cell
    BTO_0001546 = "BTO_0001546"
    CHRONIC_LYMPHOCYTIC_LEUKEMIA_CELL = "BTO_0001546"

    # sepal
    BTO_0001547 = "BTO_0001547"
    SEPAL = "BTO_0001547"

    # labial gland
    BTO_0001548 = "BTO_0001548"
    LABIAL_GLAND = "BTO_0001548"

    # megakaryocyte cell line
    BTO_0001549 = "BTO_0001549"
    MEGAKARYOCYTE_CELL_LINE = "BTO_0001549"

    # Dami cell
    BTO_0001550 = "BTO_0001550"
    DAMI_CELL = "BTO_0001550"

    # free-living state
    BTO_0001551 = "BTO_0001551"
    FREE_LIVING_STATE = "BTO_0001551"

    # Yoshida AH-66 cell
    BTO_0001552 = "BTO_0001552"
    YOSHIDA_AH_66_CELL = "BTO_0001552"

    # LS-174T cell
    BTO_0001553 = "BTO_0001553"
    LS_174T_CELL = "BTO_0001553"

    # 661W cell
    BTO_0001554 = "BTO_0001554"
    _661W_CELL = "BTO_0001554"

    # endometrial cancer cell line
    BTO_0001555 = "BTO_0001555"
    ENDOMETRIAL_CANCER_CELL_LINE = "BTO_0001555"

    # Rcho-1 cell
    BTO_0001556 = "BTO_0001556"
    RCHO_1_CELL = "BTO_0001556"

    # SF-767 cell
    BTO_0001557 = "BTO_0001557"
    SF_767_CELL = "BTO_0001557"

    # somite
    BTO_0001558 = "BTO_0001558"
    SOMITE = "BTO_0001558"

    # stamen
    BTO_0001559 = "BTO_0001559"
    STAMEN = "BTO_0001559"

    # testicular cancer cell line
    BTO_0001560 = "BTO_0001560"
    TESTICULAR_CANCER_CELL_LINE = "BTO_0001560"

    # DAUDI cell
    BTO_0001561 = "BTO_0001561"
    DAUDI_CELL = "BTO_0001561"

    # aerial mycelium
    BTO_0001562 = "BTO_0001562"
    AERIAL_MYCELIUM = "BTO_0001562"

    # vastus lateralis
    BTO_0001563 = "BTO_0001563"
    VASTUS_LATERALIS = "BTO_0001563"

    # rectus femoris
    BTO_0001564 = "BTO_0001564"
    RECTUS_FEMORIS = "BTO_0001564"

    # HT-29-MTX cell
    BTO_0001565 = "BTO_0001565"
    HT_29_MTX_CELL = "BTO_0001565"

    # HT-29 G cell
    BTO_0001566 = "BTO_0001566"
    HT_29_G_CELL = "BTO_0001566"

    # MDA-MB-435 cell
    BTO_0001567 = "BTO_0001567"
    MDA_MB_435_CELL = "BTO_0001567"

    # MDA-MB-436 cell
    BTO_0001568 = "BTO_0001568"
    MDA_MB_436_CELL = "BTO_0001568"

    # MDA-MB-361 cell
    BTO_0001569 = "BTO_0001569"
    MDA_MB_361_CELL = "BTO_0001569"

    # MDA-MB-468 cell
    BTO_0001570 = "BTO_0001570"
    MDA_MB_468_CELL = "BTO_0001570"

    # erythroblast
    BTO_0001571 = "BTO_0001571"
    ERYTHROBLAST = "BTO_0001571"

    # articular cartilage
    BTO_0001572 = "BTO_0001572"
    ARTICULAR_CARTILAGE = "BTO_0001572"

    # brain cancer cell
    BTO_0001573 = "BTO_0001573"
    BRAIN_CANCER_CELL = "BTO_0001573"

    # chondrosarcoma cell line
    BTO_0001574 = "BTO_0001574"
    CHONDROSARCOMA_CELL_LINE = "BTO_0001574"

    # choriocarcinoma cell line
    BTO_0001575 = "BTO_0001575"
    CHORIOCARCINOMA_CELL_LINE = "BTO_0001575"

    # choriocarcinoma cell
    BTO_0001576 = "BTO_0001576"
    CHORIOCARCINOMA_CELL = "BTO_0001576"

    # esophageal cancer cell
    BTO_0001577 = "BTO_0001577"
    ESOPHAGEAL_CANCER_CELL = "BTO_0001577"

    # esophageal epithelium
    BTO_0001578 = "BTO_0001578"
    ESOPHAGEAL_EPITHELIUM = "BTO_0001578"

    # extraocular muscle
    BTO_0001579 = "BTO_0001579"
    EXTRAOCULAR_MUSCLE = "BTO_0001579"

    # ejaculatory duct
    BTO_0001580 = "BTO_0001580"
    EJACULATORY_DUCT = "BTO_0001580"

    # embryonic stem cell line
    BTO_0001581 = "BTO_0001581"
    EMBRYONIC_STEM_CELL_LINE = "BTO_0001581"

    # ES-D3 cell
    BTO_0001582 = "BTO_0001582"
    ES_D3_CELL = "BTO_0001582"

    # T-98G cell
    BTO_0001583 = "BTO_0001583"
    T_98G_CELL = "BTO_0001583"

    # G-361 cell
    BTO_0001584 = "BTO_0001584"
    G_361_CELL = "BTO_0001584"

    # JAR cell
    BTO_0001585 = "BTO_0001585"
    JAR_CELL = "BTO_0001585"

    # lymphoid cell line
    BTO_0001586 = "BTO_0001586"
    LYMPHOID_CELL_LINE = "BTO_0001586"

    # MEL-HO cell
    BTO_0001587 = "BTO_0001587"
    MEL_HO_CELL = "BTO_0001587"

    # MEL-JUSO cell
    BTO_0001588 = "BTO_0001588"
    MEL_JUSO_CELL = "BTO_0001588"

    # KLN205 cell
    BTO_0001589 = "BTO_0001589"
    KLN205_CELL = "BTO_0001589"

    # MRC-5 cell
    BTO_0001590 = "BTO_0001590"
    MRC_5_CELL = "BTO_0001590"

    # PA-1 cell
    BTO_0001591 = "BTO_0001591"
    PA_1_CELL = "BTO_0001591"

    # meniscus
    BTO_0001592 = "BTO_0001592"
    MENISCUS = "BTO_0001592"

    # osteoblast
    BTO_0001593 = "BTO_0001593"
    OSTEOBLAST = "BTO_0001593"

    # U-266 cell
    BTO_0001594 = "BTO_0001594"
    U_266_CELL = "BTO_0001594"

    # WM-266-4 cell
    BTO_0001595 = "BTO_0001595"
    WM_266_4_CELL = "BTO_0001595"

    # MG-63 cell
    BTO_0001596 = "BTO_0001596"
    MG_63_CELL = "BTO_0001596"

    # sapling
    BTO_0001597 = "BTO_0001597"
    SAPLING = "BTO_0001597"

    # splenocyte
    BTO_0001598 = "BTO_0001598"
    SPLENOCYTE = "BTO_0001598"

    # SW-1116 cell
    BTO_0001599 = "BTO_0001599"
    SW_1116_CELL = "BTO_0001599"

    # cuticle
    BTO_0001600 = "BTO_0001600"
    CUTICLE = "BTO_0001600"

    # epicuticle
    BTO_0001601 = "BTO_0001601"
    EPICUTICLE = "BTO_0001601"

    # exocuticle
    BTO_0001602 = "BTO_0001602"
    EXOCUTICLE = "BTO_0001602"

    # endocuticle
    BTO_0001603 = "BTO_0001603"
    ENDOCUTICLE = "BTO_0001603"

    # eyestalk
    BTO_0001604 = "BTO_0001604"
    EYESTALK = "BTO_0001604"

    # reticulum trabeculare
    BTO_0001605 = "BTO_0001605"
    RETICULUM_TRABECULARE = "BTO_0001605"

    # sclera
    BTO_0001606 = "BTO_0001606"
    SCLERA = "BTO_0001606"

    # swim bladder
    BTO_0001607 = "BTO_0001607"
    SWIM_BLADDER = "BTO_0001607"

    # feather calamus
    BTO_0001608 = "BTO_0001608"
    FEATHER_CALAMUS = "BTO_0001608"

    # LS-180 cell
    BTO_0001609 = "BTO_0001609"
    LS_180_CELL = "BTO_0001609"

    # thyroid cancer cell line
    BTO_0001610 = "BTO_0001610"
    THYROID_CANCER_CELL_LINE = "BTO_0001610"

    # SW-1736 cell
    BTO_0001611 = "BTO_0001611"
    SW_1736_CELL = "BTO_0001611"

    # colorectal adenoma cell
    BTO_0001612 = "BTO_0001612"
    COLORECTAL_ADENOMA_CELL = "BTO_0001612"

    # colorectum
    BTO_0001613 = "BTO_0001613"
    COLORECTUM = "BTO_0001613"

    # colorectal cell line
    BTO_0001614 = "BTO_0001614"
    COLORECTAL_CELL_LINE = "BTO_0001614"

    # colorectal cancer cell
    BTO_0001615 = "BTO_0001615"
    COLORECTAL_CANCER_CELL = "BTO_0001615"

    # colorectal cancer cell line
    BTO_0001616 = "BTO_0001616"
    COLORECTAL_CANCER_CELL_LINE = "BTO_0001616"

    # DHL-9 cell
    BTO_0001617 = "BTO_0001617"
    DHL_9_CELL = "BTO_0001617"

    # F28-7 cell
    BTO_0001618 = "BTO_0001618"
    F28_7_CELL = "BTO_0001618"

    # skin fibroblast cell line
    BTO_0001619 = "BTO_0001619"
    SKIN_FIBROBLAST_CELL_LINE = "BTO_0001619"

    # SK-N-SH cell
    BTO_0001620 = "BTO_0001620"
    SK_N_SH_CELL = "BTO_0001620"

    # intestinal cancer cell line
    BTO_0001621 = "BTO_0001621"
    INTESTINAL_CANCER_CELL_LINE = "BTO_0001621"

    # fibroblastoma cell
    BTO_0001622 = "BTO_0001622"
    FIBROBLASTOMA_CELL = "BTO_0001622"

    # fibroma cell
    BTO_0001623 = "BTO_0001623"
    FIBROMA_CELL = "BTO_0001623"

    # femoral artery
    BTO_0001624 = "BTO_0001624"
    FEMORAL_ARTERY = "BTO_0001624"

    # laryngeal cancer cell
    BTO_0001625 = "BTO_0001625"
    LARYNGEAL_CANCER_CELL = "BTO_0001625"

    # laryngeal muscle
    BTO_0001626 = "BTO_0001626"
    LARYNGEAL_MUSCLE = "BTO_0001626"

    # glottis
    BTO_0001627 = "BTO_0001627"
    GLOTTIS = "BTO_0001627"

    # epiglottis
    BTO_0001628 = "BTO_0001628"
    EPIGLOTTIS = "BTO_0001628"

    # left ventricle
    BTO_0001629 = "BTO_0001629"
    LEFT_VENTRICLE = "BTO_0001629"

    # right ventricle
    BTO_0001630 = "BTO_0001630"
    RIGHT_VENTRICLE = "BTO_0001630"

    # leiomyosarcoma cell
    BTO_0001631 = "BTO_0001631"
    LEIOMYOSARCOMA_CELL = "BTO_0001631"

    # lens cortex
    BTO_0001632 = "BTO_0001632"
    LENS_CORTEX = "BTO_0001632"

    # lens nucleus
    BTO_0001633 = "BTO_0001633"
    LENS_NUCLEUS = "BTO_0001633"

    # leptomeninx
    BTO_0001634 = "BTO_0001634"
    LEPTOMENINX = "BTO_0001634"

    # pia mater
    BTO_0001635 = "BTO_0001635"
    PIA_MATER = "BTO_0001635"

    # arachnoid mater
    BTO_0001636 = "BTO_0001636"
    ARACHNOID_MATER = "BTO_0001636"

    # dura mater
    BTO_0001637 = "BTO_0001637"
    DURA_MATER = "BTO_0001637"

    # blastema
    BTO_0001638 = "BTO_0001638"
    BLASTEMA = "BTO_0001638"

    # bud
    BTO_0001639 = "BTO_0001639"
    BUD = "BTO_0001639"

    # limb bud
    BTO_0001640 = "BTO_0001640"
    LIMB_BUD = "BTO_0001640"

    # bronchial bud
    BTO_0001641 = "BTO_0001641"
    BRONCHIAL_BUD = "BTO_0001641"

    # liver bud
    BTO_0001642 = "BTO_0001642"
    LIVER_BUD = "BTO_0001642"

    # lung bud
    BTO_0001643 = "BTO_0001643"
    LUNG_BUD = "BTO_0001643"

    # vascular bud
    BTO_0001644 = "BTO_0001644"
    VASCULAR_BUD = "BTO_0001644"

    # wing bud
    BTO_0001645 = "BTO_0001645"
    WING_BUD = "BTO_0001645"

    # ureteric bud
    BTO_0001646 = "BTO_0001646"
    URETERIC_BUD = "BTO_0001646"

    # lip
    BTO_0001647 = "BTO_0001647"
    LIP = "BTO_0001647"

    # longissimus
    BTO_0001648 = "BTO_0001648"
    LONGISSIMUS = "BTO_0001648"

    # longissimus capitis
    BTO_0001649 = "BTO_0001649"
    LONGISSIMUS_CAPITIS = "BTO_0001649"

    # longissimus cervicis
    BTO_0001650 = "BTO_0001650"
    LONGISSIMUS_CERVICIS = "BTO_0001650"

    # longissimus thoracis
    BTO_0001651 = "BTO_0001651"
    LONGISSIMUS_THORACIS = "BTO_0001651"

    # sacrospinalis
    BTO_0001652 = "BTO_0001652"
    SACROSPINALIS = "BTO_0001652"

    # lung epithelium
    BTO_0001653 = "BTO_0001653"
    LUNG_EPITHELIUM = "BTO_0001653"

    # female cone
    BTO_0001654 = "BTO_0001654"
    FEMALE_CONE = "BTO_0001654"

    # male cone
    BTO_0001655 = "BTO_0001655"
    MALE_CONE = "BTO_0001655"

    # nerve cord
    BTO_0001656 = "BTO_0001656"
    NERVE_CORD = "BTO_0001656"

    # abscission zone
    BTO_0001657 = "BTO_0001657"
    ABSCISSION_ZONE = "BTO_0001657"

    # aerial part
    BTO_0001658 = "BTO_0001658"
    AERIAL_PART = "BTO_0001658"

    # aerial root
    BTO_0001659 = "BTO_0001659"
    AERIAL_ROOT = "BTO_0001659"

    # respiratory smooth muscle
    BTO_0001660 = "BTO_0001660"
    RESPIRATORY_SMOOTH_MUSCLE = "BTO_0001660"

    # alkaline gland
    BTO_0001661 = "BTO_0001661"
    ALKALINE_GLAND = "BTO_0001661"

    # allantoic fluid
    BTO_0001662 = "BTO_0001662"
    ALLANTOIC_FLUID = "BTO_0001662"

    # ameloblast
    BTO_0001663 = "BTO_0001663"
    AMELOBLAST = "BTO_0001663"

    # hepatoblastoma cell line
    BTO_0001664 = "BTO_0001664"
    HEPATOBLASTOMA_CELL_LINE = "BTO_0001664"

    # HB611 cell
    BTO_0001665 = "BTO_0001665"
    HB611_CELL = "BTO_0001665"

    # hepatoblastoma cell
    BTO_0001666 = "BTO_0001666"
    HEPATOBLASTOMA_CELL = "BTO_0001666"

    # HMB-2 cell
    BTO_0001667 = "BTO_0001667"
    HMB_2_CELL = "BTO_0001667"

    # mast cell line
    BTO_0001668 = "BTO_0001668"
    MAST_CELL_LINE = "BTO_0001668"

    # HMC-1 cell
    BTO_0001669 = "BTO_0001669"
    HMC_1_CELL = "BTO_0001669"

    # HuH-6 cell
    BTO_0001670 = "BTO_0001670"
    HUH_6_CELL = "BTO_0001670"

    # J-82 cell
    BTO_0001671 = "BTO_0001671"
    J_82_CELL = "BTO_0001671"

    # Mel Ei cell
    BTO_0001672 = "BTO_0001672"
    MEL_EI_CELL = "BTO_0001672"

    # Mel Ju cell
    BTO_0001673 = "BTO_0001673"
    MEL_JU_CELL = "BTO_0001673"

    # Mel Im cell
    BTO_0001674 = "BTO_0001674"
    MEL_IM_CELL = "BTO_0001674"

    # Mel Wei cell
    BTO_0001675 = "BTO_0001675"
    MEL_WEI_CELL = "BTO_0001675"

    # PC-12D cell
    BTO_0001676 = "BTO_0001676"
    PC_12D_CELL = "BTO_0001676"

    # SCHNEIDER-2 cell
    BTO_0001677 = "BTO_0001677"
    SCHNEIDER_2_CELL = "BTO_0001677"

    # Th1 cell
    BTO_0001678 = "BTO_0001678"
    TH1_CELL = "BTO_0001678"

    # Th2 cell
    BTO_0001679 = "BTO_0001679"
    TH2_CELL = "BTO_0001679"

    # anus
    BTO_0001680 = "BTO_0001680"
    ANUS = "BTO_0001680"

    # anal sac
    BTO_0001681 = "BTO_0001681"
    ANAL_SAC = "BTO_0001681"

    # byssus
    BTO_0001682 = "BTO_0001682"
    BYSSUS = "BTO_0001682"

    # adenohypophysis tumor cell
    BTO_0001683 = "BTO_0001683"
    ADENOHYPOPHYSIS_TUMOR_CELL = "BTO_0001683"

    # antler
    BTO_0001684 = "BTO_0001684"
    ANTLER = "BTO_0001684"

    # aortic smooth muscle
    BTO_0001685 = "BTO_0001685"
    AORTIC_SMOOTH_MUSCLE = "BTO_0001685"

    # joint
    BTO_0001686 = "BTO_0001686"
    JOINT = "BTO_0001686"

    # asynchronous muscle
    BTO_0001687 = "BTO_0001687"
    ASYNCHRONOUS_MUSCLE = "BTO_0001687"

    # cochlear ganglion
    BTO_0001688 = "BTO_0001688"
    COCHLEAR_GANGLION = "BTO_0001688"

    # axillary bud
    BTO_0001689 = "BTO_0001689"
    AXILLARY_BUD = "BTO_0001689"

    # B-cell lymphoma cell
    BTO_0001690 = "BTO_0001690"
    B_CELL_LYMPHOMA_CELL = "BTO_0001690"

    # spiral organ
    BTO_0001691 = "BTO_0001691"
    SPIRAL_ORGAN = "BTO_0001691"

    # cochlear duct
    BTO_0001692 = "BTO_0001692"
    COCHLEAR_DUCT = "BTO_0001692"

    # modiolus
    BTO_0001693 = "BTO_0001693"
    MODIOLUS = "BTO_0001693"

    # urinary bladder epithelium
    BTO_0001694 = "BTO_0001694"
    URINARY_BLADDER_EPITHELIUM = "BTO_0001694"

    # blastopore
    BTO_0001695 = "BTO_0001695"
    BLASTOPORE = "BTO_0001695"

    # archenteron
    BTO_0001696 = "BTO_0001696"
    ARCHENTERON = "BTO_0001696"

    # olfactory gland
    BTO_0001697 = "BTO_0001697"
    OLFACTORY_GLAND = "BTO_0001697"

    # bulbourethral gland
    BTO_0001698 = "BTO_0001698"
    BULBOURETHRAL_GLAND = "BTO_0001698"

    # bursa of Fabricius
    BTO_0001699 = "BTO_0001699"
    BURSA_OF_FABRICIUS = "BTO_0001699"

    # cancellous bone
    BTO_0001700 = "BTO_0001700"
    CANCELLOUS_BONE = "BTO_0001700"

    # carapace
    BTO_0001701 = "BTO_0001701"
    CARAPACE = "BTO_0001701"

    # left atrium
    BTO_0001702 = "BTO_0001702"
    LEFT_ATRIUM = "BTO_0001702"

    # right atrium
    BTO_0001703 = "BTO_0001703"
    RIGHT_ATRIUM = "BTO_0001703"

    # twitch muscle
    BTO_0001704 = "BTO_0001704"
    TWITCH_MUSCLE = "BTO_0001704"

    # vallate papilla
    BTO_0001705 = "BTO_0001705"
    VALLATE_PAPILLA = "BTO_0001705"

    # cnidoblast
    BTO_0001706 = "BTO_0001706"
    CNIDOBLAST = "BTO_0001706"

    # coelom
    BTO_0001707 = "BTO_0001707"
    COELOM = "BTO_0001707"

    # coelomic fluid
    BTO_0001708 = "BTO_0001708"
    COELOMIC_FLUID = "BTO_0001708"

    # colonic epithelium
    BTO_0001709 = "BTO_0001709"
    COLONIC_EPITHELIUM = "BTO_0001709"

    # corpora quadrigemina
    BTO_0001710 = "BTO_0001710"
    CORPORA_QUADRIGEMINA = "BTO_0001710"

    # melanophore
    BTO_0001711 = "BTO_0001711"
    MELANOPHORE = "BTO_0001711"

    # dorsal lip
    BTO_0001712 = "BTO_0001712"
    DORSAL_LIP = "BTO_0001712"

    # dorsum
    BTO_0001713 = "BTO_0001713"
    DORSUM = "BTO_0001713"

    # duodenal adenocarcinoma cell
    BTO_0001714 = "BTO_0001714"
    DUODENAL_ADENOCARCINOMA_CELL = "BTO_0001714"

    # ectoplacental cone
    BTO_0001715 = "BTO_0001715"
    ECTOPLACENTAL_CONE = "BTO_0001715"

    # eggshell
    BTO_0001716 = "BTO_0001716"
    EGGSHELL = "BTO_0001716"

    # BmN4-DR cell
    BTO_0001717 = "BTO_0001717"
    BMN4_DR_CELL = "BTO_0001717"

    # embryoid body
    BTO_0001718 = "BTO_0001718"
    EMBRYOID_BODY = "BTO_0001718"

    # claw
    BTO_0001719 = "BTO_0001719"
    CLAW = "BTO_0001719"

    # floor plate
    BTO_0001720 = "BTO_0001720"
    FLOOR_PLATE = "BTO_0001720"

    # sternal cartilage
    BTO_0001721 = "BTO_0001721"
    STERNAL_CARTILAGE = "BTO_0001721"

    # enamel organ
    BTO_0001722 = "BTO_0001722"
    ENAMEL_ORGAN = "BTO_0001722"

    # enamel epithelium
    BTO_0001723 = "BTO_0001723"
    ENAMEL_EPITHELIUM = "BTO_0001723"

    # ependymocyte
    BTO_0001724 = "BTO_0001724"
    EPENDYMOCYTE = "BTO_0001724"

    # floral meristem
    BTO_0001725 = "BTO_0001725"
    FLORAL_MERISTEM = "BTO_0001725"

    # inflorescence meristem
    BTO_0001726 = "BTO_0001726"
    INFLORESCENCE_MERISTEM = "BTO_0001726"

    # perianth
    BTO_0001727 = "BTO_0001727"
    PERIANTH = "BTO_0001727"

    # tepal
    BTO_0001728 = "BTO_0001728"
    TEPAL = "BTO_0001728"

    # forelimb
    BTO_0001729 = "BTO_0001729"
    FORELIMB = "BTO_0001729"

    # mesosperm
    BTO_0001730 = "BTO_0001730"
    MESOSPERM = "BTO_0001730"

    # glucagonoma cell
    BTO_0001731 = "BTO_0001731"
    GLUCAGONOMA_CELL = "BTO_0001731"

    # gastric antrum
    BTO_0001732 = "BTO_0001732"
    GASTRIC_ANTRUM = "BTO_0001732"

    # gynoecium
    BTO_0001733 = "BTO_0001733"
    GYNOECIUM = "BTO_0001733"

    # gut juice
    BTO_0001734 = "BTO_0001734"
    GUT_JUICE = "BTO_0001734"

    # cardiac Purkinje fiber
    BTO_0001735 = "BTO_0001735"
    CARDIAC_PURKINJE_FIBER = "BTO_0001735"

    # vascular cancer cell
    BTO_0001736 = "BTO_0001736"
    VASCULAR_CANCER_CELL = "BTO_0001736"

    # hemangioendothelioma cell
    BTO_0001737 = "BTO_0001737"
    HEMANGIOENDOTHELIOMA_CELL = "BTO_0001737"

    # histiocytic lymphoma cell
    BTO_0001738 = "BTO_0001738"
    HISTIOCYTIC_LYMPHOMA_CELL = "BTO_0001738"

    # pars tuberalis
    BTO_0001739 = "BTO_0001739"
    PARS_TUBERALIS = "BTO_0001739"

    # hypopharynx
    BTO_0001740 = "BTO_0001740"
    HYPOPHARYNX = "BTO_0001740"

    # incisor
    BTO_0001741 = "BTO_0001741"
    INCISOR = "BTO_0001741"

    # jejunal mucosa
    BTO_0001742 = "BTO_0001742"
    JEJUNAL_MUCOSA = "BTO_0001742"

    # jejunal epithelium
    BTO_0001743 = "BTO_0001743"
    JEJUNAL_EPITHELIUM = "BTO_0001743"

    # jugular vein
    BTO_0001744 = "BTO_0001744"
    JUGULAR_VEIN = "BTO_0001744"

    # renal inner medulla
    BTO_0001745 = "BTO_0001745"
    RENAL_INNER_MEDULLA = "BTO_0001745"

    # renal outer medulla
    BTO_0001746 = "BTO_0001746"
    RENAL_OUTER_MEDULLA = "BTO_0001746"

    # palpus
    BTO_0001747 = "BTO_0001747"
    PALPUS = "BTO_0001747"

    # mandible
    BTO_0001748 = "BTO_0001748"
    MANDIBLE = "BTO_0001748"

    # jaw
    BTO_0001749 = "BTO_0001749"
    JAW = "BTO_0001749"

    # mandibular condyle
    BTO_0001750 = "BTO_0001750"
    MANDIBULAR_CONDYLE = "BTO_0001750"

    # mandibular ramus
    BTO_0001751 = "BTO_0001751"
    MANDIBULAR_RAMUS = "BTO_0001751"

    # invertebrate mandible
    BTO_0001752 = "BTO_0001752"
    INVERTEBRATE_MANDIBLE = "BTO_0001752"

    # mandibular organ
    BTO_0001753 = "BTO_0001753"
    MANDIBULAR_ORGAN = "BTO_0001753"

    # cheek
    BTO_0001754 = "BTO_0001754"
    CHEEK = "BTO_0001754"

    # masseter
    BTO_0001755 = "BTO_0001755"
    MASSETER = "BTO_0001755"

    # meningioma cell
    BTO_0001756 = "BTO_0001756"
    MENINGIOMA_CELL = "BTO_0001756"

    # medulloblastoma cell
    BTO_0001757 = "BTO_0001757"
    MEDULLOBLASTOMA_CELL = "BTO_0001757"

    # ocellus
    BTO_0001758 = "BTO_0001758"
    OCELLUS = "BTO_0001758"

    # molaris
    BTO_0001759 = "BTO_0001759"
    MOLARIS = "BTO_0001759"

    # myotube
    BTO_0001760 = "BTO_0001760"
    MYOTUBE = "BTO_0001760"

    # nasal vestibule
    BTO_0001761 = "BTO_0001761"
    NASAL_VESTIBULE = "BTO_0001761"

    # neonate
    BTO_0001762 = "BTO_0001762"
    NEONATE = "BTO_0001762"

    # neural arch
    BTO_0001763 = "BTO_0001763"
    NEURAL_ARCH = "BTO_0001763"

    # neural crest
    BTO_0001764 = "BTO_0001764"
    NEURAL_CREST = "BTO_0001764"

    # neural plate
    BTO_0001765 = "BTO_0001765"
    NEURAL_PLATE = "BTO_0001765"

    # neurula
    BTO_0001766 = "BTO_0001766"
    NEURULA = "BTO_0001766"

    # neurosecretory cell
    BTO_0001767 = "BTO_0001767"
    NEUROSECRETORY_CELL = "BTO_0001767"

    # notochord
    BTO_0001768 = "BTO_0001768"
    NOTOCHORD = "BTO_0001768"

    # odontoblast
    BTO_0001769 = "BTO_0001769"
    ODONTOBLAST = "BTO_0001769"

    # ciliary epithelium
    BTO_0001770 = "BTO_0001770"
    CILIARY_EPITHELIUM = "BTO_0001770"

    # AN3CA cell
    BTO_0001771 = "BTO_0001771"
    AN3CA_CELL = "BTO_0001771"

    # olfactory organ
    BTO_0001772 = "BTO_0001772"
    OLFACTORY_ORGAN = "BTO_0001772"

    # oocyst
    BTO_0001773 = "BTO_0001773"
    OOCYST = "BTO_0001773"

    # oral cancer cell
    BTO_0001774 = "BTO_0001774"
    ORAL_CANCER_CELL = "BTO_0001774"

    # oral epithelium
    BTO_0001775 = "BTO_0001775"
    ORAL_EPITHELIUM = "BTO_0001775"

    # plant ovule
    BTO_0001776 = "BTO_0001776"
    PLANT_OVULE = "BTO_0001776"

    # megasporangium
    BTO_0001777 = "BTO_0001777"
    MEGASPORANGIUM = "BTO_0001777"

    # microsporangium
    BTO_0001778 = "BTO_0001778"
    MICROSPORANGIUM = "BTO_0001778"

    # palate
    BTO_0001779 = "BTO_0001779"
    PALATE = "BTO_0001779"

    # oxyntic cell
    BTO_0001780 = "BTO_0001780"
    OXYNTIC_CELL = "BTO_0001780"

    # parathyroid gland cancer cell
    BTO_0001781 = "BTO_0001781"
    PARATHYROID_GLAND_CANCER_CELL = "BTO_0001781"

    # peritoneal cavity
    BTO_0001782 = "BTO_0001782"
    PERITONEAL_CAVITY = "BTO_0001782"

    # pulvinus
    BTO_0001783 = "BTO_0001783"
    PULVINUS = "BTO_0001783"

    # Peyer's gland
    BTO_0001784 = "BTO_0001784"
    PEYER_S_GLAND = "BTO_0001784"

    # branchial arch
    BTO_0001785 = "BTO_0001785"
    BRANCHIAL_ARCH = "BTO_0001785"

    # pheromone gland
    BTO_0001786 = "BTO_0001786"
    PHEROMONE_GLAND = "BTO_0001786"

    # pars distalis
    BTO_0001787 = "BTO_0001787"
    PARS_DISTALIS = "BTO_0001787"

    # pars intermedia
    BTO_0001788 = "BTO_0001788"
    PARS_INTERMEDIA = "BTO_0001788"

    # neural lobe
    BTO_0001789 = "BTO_0001789"
    NEURAL_LOBE = "BTO_0001789"

    # pleopod
    BTO_0001790 = "BTO_0001790"
    PLEOPOD = "BTO_0001790"

    # pleura
    BTO_0001791 = "BTO_0001791"
    PLEURA = "BTO_0001791"

    # portal vein
    BTO_0001792 = "BTO_0001792"
    PORTAL_VEIN = "BTO_0001792"

    # tectum mesencephali
    BTO_0001793 = "BTO_0001793"
    TECTUM_MESENCEPHALI = "BTO_0001793"

    # posterior silk gland
    BTO_0001794 = "BTO_0001794"
    POSTERIOR_SILK_GLAND = "BTO_0001794"

    # anterior silk gland
    BTO_0001795 = "BTO_0001795"
    ANTERIOR_SILK_GLAND = "BTO_0001795"

    # preoptic area
    BTO_0001796 = "BTO_0001796"
    PREOPTIC_AREA = "BTO_0001796"

    # promyelocytic leukemia cell
    BTO_0001797 = "BTO_0001797"
    PROMYELOCYTIC_LEUKEMIA_CELL = "BTO_0001797"

    # prothallium
    BTO_0001798 = "BTO_0001798"
    PROTHALLIUM = "BTO_0001798"

    # pulmonary vein
    BTO_0001799 = "BTO_0001799"
    PULMONARY_VEIN = "BTO_0001799"

    # retinal ganglion cell
    BTO_0001800 = "BTO_0001800"
    RETINAL_GANGLION_CELL = "BTO_0001800"

    # skeletal muscle cancer cell
    BTO_0001801 = "BTO_0001801"
    SKELETAL_MUSCLE_CANCER_CELL = "BTO_0001801"

    # rhabdomyosarcoma cell
    BTO_0001802 = "BTO_0001802"
    RHABDOMYOSARCOMA_CELL = "BTO_0001802"

    # retrocerebral complex
    BTO_0001803 = "BTO_0001803"
    RETROCEREBRAL_COMPLEX = "BTO_0001803"

    # root hair
    BTO_0001804 = "BTO_0001804"
    ROOT_HAIR = "BTO_0001804"

    # saccule
    BTO_0001805 = "BTO_0001805"
    SACCULE = "BTO_0001805"

    # visceral mass
    BTO_0001806 = "BTO_0001806"
    VISCERAL_MASS = "BTO_0001806"

    # utricle
    BTO_0001807 = "BTO_0001807"
    UTRICLE = "BTO_0001807"

    # saphenous vein
    BTO_0001808 = "BTO_0001808"
    SAPHENOUS_VEIN = "BTO_0001808"

    # scalp
    BTO_0001809 = "BTO_0001809"
    SCALP = "BTO_0001809"

    # sclerotium
    BTO_0001810 = "BTO_0001810"
    SCLEROTIUM = "BTO_0001810"

    # seminiferous epithelium
    BTO_0001811 = "BTO_0001811"
    SEMINIFEROUS_EPITHELIUM = "BTO_0001811"

    # slow twitch muscle fiber
    BTO_0001812 = "BTO_0001812"
    SLOW_TWITCH_MUSCLE_FIBER = "BTO_0001812"

    # fast twitch muscle fiber
    BTO_0001813 = "BTO_0001813"
    FAST_TWITCH_MUSCLE_FIBER = "BTO_0001813"

    # leaf tip
    BTO_0001814 = "BTO_0001814"
    LEAF_TIP = "BTO_0001814"

    # stellate ganglion
    BTO_0001815 = "BTO_0001815"
    STELLATE_GANGLION = "BTO_0001815"

    # stem nodule
    BTO_0001816 = "BTO_0001816"
    STEM_NODULE = "BTO_0001816"

    # stolon tip
    BTO_0001817 = "BTO_0001817"
    STOLON_TIP = "BTO_0001817"

    # stomach smooth muscle
    BTO_0001818 = "BTO_0001818"
    STOMACH_SMOOTH_MUSCLE = "BTO_0001818"

    # stria vascularis
    BTO_0001819 = "BTO_0001819"
    STRIA_VASCULARIS = "BTO_0001819"

    # subcommissural organ
    BTO_0001820 = "BTO_0001820"
    SUBCOMMISSURAL_ORGAN = "BTO_0001820"

    # subesophageal ganglion
    BTO_0001821 = "BTO_0001821"
    SUBESOPHAGEAL_GANGLION = "BTO_0001821"

    # suprachiasmatic nucleus
    BTO_0001822 = "BTO_0001822"
    SUPRACHIASMATIC_NUCLEUS = "BTO_0001822"

    # synovium
    BTO_0001823 = "BTO_0001823"
    SYNOVIUM = "BTO_0001823"

    # synovial sarcoma cell
    BTO_0001824 = "BTO_0001824"
    SYNOVIAL_SARCOMA_CELL = "BTO_0001824"

    # T-cell lymphoma cell
    BTO_0001825 = "BTO_0001825"
    T_CELL_LYMPHOMA_CELL = "BTO_0001825"

    # T-lymphoblast
    BTO_0001826 = "BTO_0001826"
    T_LYMPHOBLAST = "BTO_0001826"

    # tail fin
    BTO_0001827 = "BTO_0001827"
    TAIL_FIN = "BTO_0001827"

    # tapetum lucidum
    BTO_0001828 = "BTO_0001828"
    TAPETUM_LUCIDUM = "BTO_0001828"

    # choroid
    BTO_0001829 = "BTO_0001829"
    CHOROID = "BTO_0001829"

    # tassel
    BTO_0001830 = "BTO_0001830"
    TASSEL = "BTO_0001830"

    # thoracic ganglion
    BTO_0001831 = "BTO_0001831"
    THORACIC_GANGLION = "BTO_0001831"

    # sympathetic nervous system
    BTO_0001832 = "BTO_0001832"
    SYMPATHETIC_NERVOUS_SYSTEM = "BTO_0001832"

    # parasympathetic nervous system
    BTO_0001833 = "BTO_0001833"
    PARASYMPATHETIC_NERVOUS_SYSTEM = "BTO_0001833"

    # sympathetic chain
    BTO_0001834 = "BTO_0001834"
    SYMPATHETIC_CHAIN = "BTO_0001834"

    # vertebral ganglion
    BTO_0001835 = "BTO_0001835"
    VERTEBRAL_GANGLION = "BTO_0001835"

    # thymic epithelium
    BTO_0001836 = "BTO_0001836"
    THYMIC_EPITHELIUM = "BTO_0001836"

    # serous gland
    BTO_0001837 = "BTO_0001837"
    SEROUS_GLAND = "BTO_0001837"

    # tooth bud
    BTO_0001838 = "BTO_0001838"
    TOOTH_BUD = "BTO_0001838"

    # dental papilla
    BTO_0001839 = "BTO_0001839"
    DENTAL_PAPILLA = "BTO_0001839"

    # trophectoderm
    BTO_0001840 = "BTO_0001840"
    TROPHECTODERM = "BTO_0001840"

    # parietal ganglion
    BTO_0001841 = "BTO_0001841"
    PARIETAL_GANGLION = "BTO_0001841"

    # pleural ganglion
    BTO_0001842 = "BTO_0001842"
    PLEURAL_GANGLION = "BTO_0001842"

    # cerebral ganglion
    BTO_0001843 = "BTO_0001843"
    CEREBRAL_GANGLION = "BTO_0001843"

    # tooth enamel
    BTO_0001844 = "BTO_0001844"
    TOOTH_ENAMEL = "BTO_0001844"

    # bronchial epithelium
    BTO_0001845 = "BTO_0001845"
    BRONCHIAL_EPITHELIUM = "BTO_0001845"

    # bronchial mucosa
    BTO_0001846 = "BTO_0001846"
    BRONCHIAL_MUCOSA = "BTO_0001846"

    # umbilical smooth muscle
    BTO_0001847 = "BTO_0001847"
    UMBILICAL_SMOOTH_MUSCLE = "BTO_0001847"

    # urophysis
    BTO_0001848 = "BTO_0001848"
    UROPHYSIS = "BTO_0001848"

    # urinary bladder smooth muscle
    BTO_0001849 = "BTO_0001849"
    URINARY_BLADDER_SMOOTH_MUSCLE = "BTO_0001849"

    # portio vaginalis cervicis
    BTO_0001850 = "BTO_0001850"
    PORTIO_VAGINALIS_CERVICIS = "BTO_0001850"

    # portio supravaginalis cervicis
    BTO_0001851 = "BTO_0001851"
    PORTIO_SUPRAVAGINALIS_CERVICIS = "BTO_0001851"

    # cerebrovascular endothelium
    BTO_0001852 = "BTO_0001852"
    CEREBROVASCULAR_ENDOTHELIUM = "BTO_0001852"

    # vascular endothelium
    BTO_0001853 = "BTO_0001853"
    VASCULAR_ENDOTHELIUM = "BTO_0001853"

    # vascular endothelial cell
    BTO_0001854 = "BTO_0001854"
    VASCULAR_ENDOTHELIAL_CELL = "BTO_0001854"

    # venom duct
    BTO_0001855 = "BTO_0001855"
    VENOM_DUCT = "BTO_0001855"

    # vestibular labyrinth
    BTO_0001856 = "BTO_0001856"
    VESTIBULAR_LABYRINTH = "BTO_0001856"

    # visual cortex
    BTO_0001857 = "BTO_0001857"
    VISUAL_CORTEX = "BTO_0001857"

    # dermal papilla
    BTO_0001858 = "BTO_0001858"
    DERMAL_PAPILLA = "BTO_0001858"

    # wart
    BTO_0001859 = "BTO_0001859"
    WART = "BTO_0001859"

    # yolk sac cancer cell
    BTO_0001860 = "BTO_0001860"
    YOLK_SAC_CANCER_CELL = "BTO_0001860"

    # BxPC-3 cell
    BTO_0001861 = "BTO_0001861"
    BXPC_3_CELL = "BTO_0001861"

    # nucleus accumbens
    BTO_0001862 = "BTO_0001862"
    NUCLEUS_ACCUMBENS = "BTO_0001862"

    # body wall muscle
    BTO_0001863 = "BTO_0001863"
    BODY_WALL_MUSCLE = "BTO_0001863"

    # AsPC-1 cell
    BTO_0001864 = "BTO_0001864"
    ASPC_1_CELL = "BTO_0001864"

    # PK-15 cell
    BTO_0001865 = "BTO_0001865"
    PK_15_CELL = "BTO_0001865"

    # bronchiolar epithelium
    BTO_0001866 = "BTO_0001866"
    BRONCHIOLAR_EPITHELIUM = "BTO_0001866"

    # NR-6 cell
    BTO_0001867 = "BTO_0001867"
    NR_6_CELL = "BTO_0001867"

    # occipital pole
    BTO_0001868 = "BTO_0001868"
    OCCIPITAL_POLE = "BTO_0001868"

    # olfactory tubercle
    BTO_0001869 = "BTO_0001869"
    OLFACTORY_TUBERCLE = "BTO_0001869"

    # OVCA-5 cell
    BTO_0001870 = "BTO_0001870"
    OVCA_5_CELL = "BTO_0001870"

    # synganglion
    BTO_0001871 = "BTO_0001871"
    SYNGANGLION = "BTO_0001871"

    # alphaTN4-1 cell
    BTO_0001872 = "BTO_0001872"
    ALPHATN4_1_CELL = "BTO_0001872"

    # lens epithelium
    BTO_0001873 = "BTO_0001873"
    LENS_EPITHELIUM = "BTO_0001873"

    # lens epithelial cell line
    BTO_0001874 = "BTO_0001874"
    LENS_EPITHELIAL_CELL_LINE = "BTO_0001874"

    # FRTL-5 cell
    BTO_0001875 = "BTO_0001875"
    FRTL_5_CELL = "BTO_0001875"

    # thyroid cell line
    BTO_0001876 = "BTO_0001876"
    THYROID_CELL_LINE = "BTO_0001876"

    # psoas major
    BTO_0001877 = "BTO_0001877"
    PSOAS_MAJOR = "BTO_0001877"

    # psoas minor
    BTO_0001878 = "BTO_0001878"
    PSOAS_MINOR = "BTO_0001878"

    # H9c2 cell
    BTO_0001879 = "BTO_0001879"
    H9C2_CELL = "BTO_0001879"

    # RPMI-8402 cell
    BTO_0001880 = "BTO_0001880"
    RPMI_8402_CELL = "BTO_0001880"

    # SW-626 cell
    BTO_0001881 = "BTO_0001881"
    SW_626_CELL = "BTO_0001881"

    # ovary adenocarcinoma cell line
    BTO_0001882 = "BTO_0001882"
    OVARY_ADENOCARCINOMA_CELL_LINE = "BTO_0001882"

    # acute myeloid leukemia cell line
    BTO_0001883 = "BTO_0001883"
    ACUTE_MYELOID_LEUKEMIA_CELL_LINE = "BTO_0001883"

    # ML-1 cell
    BTO_0001884 = "BTO_0001884"
    ML_1_CELL = "BTO_0001884"

    # ML-2 cell
    BTO_0001885 = "BTO_0001885"
    ML_2_CELL = "BTO_0001885"

    # primordium
    BTO_0001886 = "BTO_0001886"
    PRIMORDIUM = "BTO_0001886"

    # heart primordium
    BTO_0001887 = "BTO_0001887"
    HEART_PRIMORDIUM = "BTO_0001887"

    # follicular thyroid cancer cell
    BTO_0001888 = "BTO_0001888"
    FOLLICULAR_THYROID_CANCER_CELL = "BTO_0001888"

    # FTC-133 cell
    BTO_0001889 = "BTO_0001889"
    FTC_133_CELL = "BTO_0001889"

    # RKO cell
    BTO_0001890 = "BTO_0001890"
    RKO_CELL = "BTO_0001890"

    # RKO-E6 cell
    BTO_0001891 = "BTO_0001891"
    RKO_E6_CELL = "BTO_0001891"

    # RKO-AS-45-1 cell
    BTO_0001892 = "BTO_0001892"
    RKO_AS_45_1_CELL = "BTO_0001892"

    # ring stage
    BTO_0001893 = "BTO_0001893"
    RING_STAGE = "BTO_0001893"

    # IIC9 cell
    BTO_0001894 = "BTO_0001894"
    IIC9_CELL = "BTO_0001894"

    # gastrointestinal endocrine cell
    BTO_0001895 = "BTO_0001895"
    GASTROINTESTINAL_ENDOCRINE_CELL = "BTO_0001895"

    # IDH4 cell
    BTO_0001896 = "BTO_0001896"
    IDH4_CELL = "BTO_0001896"

    # hemocyte cell line
    BTO_0001897 = "BTO_0001897"
    HEMOCYTE_CELL_LINE = "BTO_0001897"

    # mbn-2 cell
    BTO_0001898 = "BTO_0001898"
    MBN_2_CELL = "BTO_0001898"

    # stationary phase culture
    BTO_0001899 = "BTO_0001899"
    STATIONARY_PHASE_CULTURE = "BTO_0001899"

    # growth phase culture
    BTO_0001900 = "BTO_0001900"
    GROWTH_PHASE_CULTURE = "BTO_0001900"

    # death phase culture
    BTO_0001901 = "BTO_0001901"
    DEATH_PHASE_CULTURE = "BTO_0001901"

    # lag phase culture
    BTO_0001902 = "BTO_0001902"
    LAG_PHASE_CULTURE = "BTO_0001902"

    # logarithmic phase culture
    BTO_0001903 = "BTO_0001903"
    LOGARITHMIC_PHASE_CULTURE = "BTO_0001903"

    # SU.86.86 cell
    BTO_0001904 = "BTO_0001904"
    SU_86_86_CELL = "BTO_0001904"

    # tail muscle
    BTO_0001905 = "BTO_0001905"
    TAIL_MUSCLE = "BTO_0001905"

    # cephalothorax
    BTO_0001906 = "BTO_0001906"
    CEPHALOTHORAX = "BTO_0001906"

    # NS-1 cell
    BTO_0001907 = "BTO_0001907"
    NS_1_CELL = "BTO_0001907"

    # MDA-MB-453 cell
    BTO_0001908 = "BTO_0001908"
    MDA_MB_453_CELL = "BTO_0001908"

    # N1E-115 cell
    BTO_0001909 = "BTO_0001909"
    N1E_115_CELL = "BTO_0001909"

    # NCI-H441 cell
    BTO_0001910 = "BTO_0001910"
    NCI_H441_CELL = "BTO_0001910"

    # lung adenocarcinoma cell line
    BTO_0001911 = "BTO_0001911"
    LUNG_ADENOCARCINOMA_CELL_LINE = "BTO_0001911"

    # breast adenocarcinoma cell line
    BTO_0001912 = "BTO_0001912"
    BREAST_ADENOCARCINOMA_CELL_LINE = "BTO_0001912"

    # colonic adenocarcinoma cell line
    BTO_0001913 = "BTO_0001913"
    COLONIC_ADENOCARCINOMA_CELL_LINE = "BTO_0001913"

    # colorectal adenocarcinoma cell line
    BTO_0001914 = "BTO_0001914"
    COLORECTAL_ADENOCARCINOMA_CELL_LINE = "BTO_0001914"

    # M5076 cell
    BTO_0001915 = "BTO_0001915"
    M5076_CELL = "BTO_0001915"

    # LIM1215 cell
    BTO_0001916 = "BTO_0001916"
    LIM1215_CELL = "BTO_0001916"

    # LIM2412 cell
    BTO_0001917 = "BTO_0001917"
    LIM2412_CELL = "BTO_0001917"

    # LIM1863 cell
    BTO_0001918 = "BTO_0001918"
    LIM1863_CELL = "BTO_0001918"

    # tube foot
    BTO_0001919 = "BTO_0001919"
    TUBE_FOOT = "BTO_0001919"

    # Ehrlich Lettre ascites carcinoma cell
    BTO_0001920 = "BTO_0001920"
    EHRLICH_LETTRE_ASCITES_CARCINOMA_CELL = "BTO_0001920"

    # compound eye
    BTO_0001921 = "BTO_0001921"
    COMPOUND_EYE = "BTO_0001921"

    # ommatidium
    BTO_0001922 = "BTO_0001922"
    OMMATIDIUM = "BTO_0001922"

    # Aristotles lantern
    BTO_0001923 = "BTO_0001923"
    ARISTOTLES_LANTERN = "BTO_0001923"

    # lantern muscle
    BTO_0001924 = "BTO_0001924"
    LANTERN_MUSCLE = "BTO_0001924"

    # longissimus lumborum
    BTO_0001925 = "BTO_0001925"
    LONGISSIMUS_LUMBORUM = "BTO_0001925"

    # hybridoma cell line
    BTO_0001926 = "BTO_0001926"
    HYBRIDOMA_CELL_LINE = "BTO_0001926"

    # WEGLI18 cell
    BTO_0001927 = "BTO_0001927"
    WEGLI18_CELL = "BTO_0001927"

    # AR4-2J cell
    BTO_0001928 = "BTO_0001928"
    AR4_2J_CELL = "BTO_0001928"

    # ATDC-5 cell
    BTO_0001929 = "BTO_0001929"
    ATDC_5_CELL = "BTO_0001929"

    # A20 cell
    BTO_0001930 = "BTO_0001930"
    A20_CELL = "BTO_0001930"

    # BJAB cell
    BTO_0001931 = "BTO_0001931"
    BJAB_CELL = "BTO_0001931"

    # BT-474 cell
    BTO_0001932 = "BTO_0001932"
    BT_474_CELL = "BTO_0001932"

    # BRL cell
    BTO_0001933 = "BTO_0001933"
    BRL_CELL = "BTO_0001933"

    # BL-60 cell
    BTO_0001934 = "BTO_0001934"
    BL_60_CELL = "BTO_0001934"

    # BW-5147.3 cell
    BTO_0001935 = "BTO_0001935"
    BW_5147_3_CELL = "BTO_0001935"

    # SKW6.4 cell
    BTO_0001936 = "BTO_0001936"
    SKW6_4_CELL = "BTO_0001936"

    # RL-19 cell
    BTO_0001937 = "BTO_0001937"
    RL_19_CELL = "BTO_0001937"

    # U2-OS cell
    BTO_0001938 = "BTO_0001938"
    U2_OS_CELL = "BTO_0001938"

    # MCF-10A cell
    BTO_0001939 = "BTO_0001939"
    MCF_10A_CELL = "BTO_0001939"

    # cardiomyoblast
    BTO_0001940 = "BTO_0001940"
    CARDIOMYOBLAST = "BTO_0001940"

    # Morris hepatoma 7316A cell
    BTO_0001941 = "BTO_0001941"
    MORRIS_HEPATOMA_7316A_CELL = "BTO_0001941"

    # mandibular incisor
    BTO_0001942 = "BTO_0001942"
    MANDIBULAR_INCISOR = "BTO_0001942"

    # corneocyte
    BTO_0001943 = "BTO_0001943"
    CORNEOCYTE = "BTO_0001943"

    # H9 cell
    BTO_0001944 = "BTO_0001944"
    H9_CELL = "BTO_0001944"

    # HUT-78 cell
    BTO_0001945 = "BTO_0001945"
    HUT_78_CELL = "BTO_0001945"

    # myofibroblast
    BTO_0001946 = "BTO_0001946"
    MYOFIBROBLAST = "BTO_0001946"

    # HRT-18 cell
    BTO_0001947 = "BTO_0001947"
    HRT_18_CELL = "BTO_0001947"

    # JURKAT E-6.1 cell
    BTO_0001948 = "BTO_0001948"
    JURKAT_E_6_1_CELL = "BTO_0001948"

    # HUVEC cell
    BTO_0001949 = "BTO_0001949"
    HUVEC_CELL = "BTO_0001949"

    # HuH-7 cell
    BTO_0001950 = "BTO_0001950"
    HUH_7_CELL = "BTO_0001950"

    # HOS-TE85 cell
    BTO_0001951 = "BTO_0001951"
    HOS_TE85_CELL = "BTO_0001951"

    # HPB-ALL cell
    BTO_0001952 = "BTO_0001952"
    HPB_ALL_CELL = "BTO_0001952"

    # tanycyte
    BTO_0001953 = "BTO_0001953"
    TANYCYTE = "BTO_0001953"

    # median eminence
    BTO_0001954 = "BTO_0001954"
    MEDIAN_EMINENCE = "BTO_0001954"

    # REF-52 cell
    BTO_0001955 = "BTO_0001955"
    REF_52_CELL = "BTO_0001955"

    # XLT-15 cell
    BTO_0001956 = "BTO_0001956"
    XLT_15_CELL = "BTO_0001956"

    # MC3T3-E1 cell
    BTO_0001957 = "BTO_0001957"
    MC3T3_E1_CELL = "BTO_0001957"

    # embryonic fibroblast cell line
    BTO_0001958 = "BTO_0001958"
    EMBRYONIC_FIBROBLAST_CELL_LINE = "BTO_0001958"

    # PEER cell
    BTO_0001959 = "BTO_0001959"
    PEER_CELL = "BTO_0001959"

    # HuMMEC cell
    BTO_0001960 = "BTO_0001960"
    HUMMEC_CELL = "BTO_0001960"

    # MFM-223 cell
    BTO_0001961 = "BTO_0001961"
    MFM_223_CELL = "BTO_0001961"

    # T/G HA-VSMC cell
    BTO_0001962 = "BTO_0001962"
    T_G_HA_VSMC_CELL = "BTO_0001962"

    # aorta cell line
    BTO_0001963 = "BTO_0001963"
    AORTA_CELL_LINE = "BTO_0001963"

    # aorta smooth muscle cell line
    BTO_0001964 = "BTO_0001964"
    AORTA_SMOOTH_MUSCLE_CELL_LINE = "BTO_0001964"

    # carcass
    BTO_0001965 = "BTO_0001965"
    CARCASS = "BTO_0001965"

    # cervical cell line
    BTO_0001966 = "BTO_0001966"
    CERVICAL_CELL_LINE = "BTO_0001966"

    # cervical cancer cell line
    BTO_0001967 = "BTO_0001967"
    CERVICAL_CANCER_CELL_LINE = "BTO_0001967"

    # C-33A cell
    BTO_0001968 = "BTO_0001968"
    C_33A_CELL = "BTO_0001968"

    # 697 cell
    BTO_0001969 = "BTO_0001969"
    _697_CELL = "BTO_0001969"

    # NCI-H660 cell
    BTO_0001970 = "BTO_0001970"
    NCI_H660_CELL = "BTO_0001970"

    # plant cell line
    BTO_0001971 = "BTO_0001971"
    PLANT_CELL_LINE = "BTO_0001971"

    # TBY-2 cell
    BTO_0001972 = "BTO_0001972"
    TBY_2_CELL = "BTO_0001972"

    # vascular endothelial cell line
    BTO_0001973 = "BTO_0001973"
    VASCULAR_ENDOTHELIAL_CELL_LINE = "BTO_0001973"

    # HPEC cell
    BTO_0001974 = "BTO_0001974"
    HPEC_CELL = "BTO_0001974"

    # placental cell line
    BTO_0001975 = "BTO_0001975"
    PLACENTAL_CELL_LINE = "BTO_0001975"

    # Neuro-2a cell
    BTO_0001976 = "BTO_0001976"
    NEURO_2A_CELL = "BTO_0001976"

    # Oc cell
    BTO_0001977 = "BTO_0001977"
    OC_CELL = "BTO_0001977"

    # anal canal
    BTO_0001978 = "BTO_0001978"
    ANAL_CANAL = "BTO_0001978"

    # mucous gland
    BTO_0001979 = "BTO_0001979"
    MUCOUS_GLAND = "BTO_0001979"

    # sebaceous gland
    BTO_0001980 = "BTO_0001980"
    SEBACEOUS_GLAND = "BTO_0001980"

    # sebum
    BTO_0001981 = "BTO_0001981"
    SEBUM = "BTO_0001981"

    # chemostat culture
    BTO_0001982 = "BTO_0001982"
    CHEMOSTAT_CULTURE = "BTO_0001982"

    # peptic chief cell
    BTO_0001983 = "BTO_0001983"
    PEPTIC_CHIEF_CELL = "BTO_0001983"

    # culture condition:beta-L-alanine-grown cell
    BTO_0001984 = "BTO_0001984"
    CULTURE_CONDITION_BETA_L_ALANINE_GROWN_CELL = "BTO_0001984"

    # culture condition:cytosine-grown cell
    BTO_0001985 = "BTO_0001985"
    CULTURE_CONDITION_CYTOSINE_GROWN_CELL = "BTO_0001985"

    # culture condition:cyclohexane-1,2-diol grown cell
    BTO_0001986 = "BTO_0001986"
    CULTURE_CONDITION_CYCLOHEXANE_1_2_DIOL_GROWN_CELL = "BTO_0001986"

    # culture condition:dihydrothymine-grown cell
    BTO_0001987 = "BTO_0001987"
    CULTURE_CONDITION_DIHYDROTHYMINE_GROWN_CELL = "BTO_0001987"

    # culture condition:dihyrouracil-grown cell
    BTO_0001988 = "BTO_0001988"
    CULTURE_CONDITION_DIHYROURACIL_GROWN_CELL = "BTO_0001988"

    # culture condition:long-chain fatty acid-grown cell
    BTO_0001989 = "BTO_0001989"
    CULTURE_CONDITION_LONG_CHAIN_FATTY_ACID_GROWN_CELL = "BTO_0001989"

    # culture condition:oleate-grown cell
    BTO_0001990 = "BTO_0001990"
    CULTURE_CONDITION_OLEATE_GROWN_CELL = "BTO_0001990"

    # culture condition:phthalate-grown cell
    BTO_0001991 = "BTO_0001991"
    CULTURE_CONDITION_PHTHALATE_GROWN_CELL = "BTO_0001991"

    # culture condition:selenium-grown cell
    BTO_0001992 = "BTO_0001992"
    CULTURE_CONDITION_SELENIUM_GROWN_CELL = "BTO_0001992"

    # culture condition:thymine-grown cell
    BTO_0001993 = "BTO_0001993"
    CULTURE_CONDITION_THYMINE_GROWN_CELL = "BTO_0001993"

    # culture condition:uracil-grown cell
    BTO_0001994 = "BTO_0001994"
    CULTURE_CONDITION_URACIL_GROWN_CELL = "BTO_0001994"

    # myocytoma cell
    BTO_0001995 = "BTO_0001995"
    MYOCYTOMA_CELL = "BTO_0001995"

    # endometrial cell line
    BTO_0001996 = "BTO_0001996"
    ENDOMETRIAL_CELL_LINE = "BTO_0001996"

    # arteriole
    BTO_0001997 = "BTO_0001997"
    ARTERIOLE = "BTO_0001997"

    # HMCB cell
    BTO_0001998 = "BTO_0001998"
    HMCB_CELL = "BTO_0001998"

    # culture condition:gene expression
    BTO_0001999 = "BTO_0001999"
    CULTURE_CONDITION_GENE_EXPRESSION = "BTO_0001999"

    # CCP-2 cell
    BTO_0002000 = "BTO_0002000"
    CCP_2_CELL = "BTO_0002000"

    # CCP-8 cell
    BTO_0002001 = "BTO_0002001"
    CCP_8_CELL = "BTO_0002001"

    # CCP-7 cell
    BTO_0002002 = "BTO_0002002"
    CCP_7_CELL = "BTO_0002002"

    # SW-1353 cell
    BTO_0002003 = "BTO_0002003"
    SW_1353_CELL = "BTO_0002003"

    # LN-229 cell
    BTO_0002004 = "BTO_0002004"
    LN_229_CELL = "BTO_0002004"

    # LN-18 cell
    BTO_0002005 = "BTO_0002005"
    LN_18_CELL = "BTO_0002005"

    # ALVA-41 cell
    BTO_0002006 = "BTO_0002006"
    ALVA_41_CELL = "BTO_0002006"

    # aggregation stage
    BTO_0002007 = "BTO_0002007"
    AGGREGATION_STAGE = "BTO_0002007"

    # culture condition:antigen-presenting cell
    BTO_0002008 = "BTO_0002008"
    CULTURE_CONDITION_ANTIGEN_PRESENTING_CELL = "BTO_0002008"

    # artery wall
    BTO_0002009 = "BTO_0002009"
    ARTERY_WALL = "BTO_0002009"

    # tunica externa vasorum
    BTO_0002010 = "BTO_0002010"
    TUNICA_EXTERNA_VASORUM = "BTO_0002010"

    # tunica media vasorum
    BTO_0002011 = "BTO_0002011"
    TUNICA_MEDIA_VASORUM = "BTO_0002011"

    # tunica intima vasorum
    BTO_0002012 = "BTO_0002012"
    TUNICA_INTIMA_VASORUM = "BTO_0002012"

    # AS-30D cell
    BTO_0002013 = "BTO_0002013"
    AS_30D_CELL = "BTO_0002013"

    # B16-F10 cell
    BTO_0002014 = "BTO_0002014"
    B16_F10_CELL = "BTO_0002014"

    # BM-1604 cell
    BTO_0002015 = "BTO_0002015"
    BM_1604_CELL = "BTO_0002015"

    # C81-61 cell
    BTO_0002016 = "BTO_0002016"
    C81_61_CELL = "BTO_0002016"

    # plant reproductive system
    BTO_0002017 = "BTO_0002017"
    PLANT_REPRODUCTIVE_SYSTEM = "BTO_0002017"

    # corpus cavernosum clitoridis
    BTO_0002018 = "BTO_0002018"
    CORPUS_CAVERNOSUM_CLITORIDIS = "BTO_0002018"

    # corpus cavernosum penis
    BTO_0002019 = "BTO_0002019"
    CORPUS_CAVERNOSUM_PENIS = "BTO_0002019"

    # clitoris
    BTO_0002020 = "BTO_0002020"
    CLITORIS = "BTO_0002020"

    # prostate adenocarcinoma cell
    BTO_0002021 = "BTO_0002021"
    PROSTATE_ADENOCARCINOMA_CELL = "BTO_0002021"

    # bronchial epithelial cell line
    BTO_0002022 = "BTO_0002022"
    BRONCHIAL_EPITHELIAL_CELL_LINE = "BTO_0002022"

    # HBE-1 cell
    BTO_0002023 = "BTO_0002023"
    HBE_1_CELL = "BTO_0002023"

    # squamous cell carcinoma cell line
    BTO_0002024 = "BTO_0002024"
    SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0002024"

    # HSC-3 cell
    BTO_0002025 = "BTO_0002025"
    HSC_3_CELL = "BTO_0002025"

    # HSC-4 cell
    BTO_0002026 = "BTO_0002026"
    HSC_4_CELL = "BTO_0002026"

    # oral cancer cell line
    BTO_0002027 = "BTO_0002027"
    ORAL_CANCER_CELL_LINE = "BTO_0002027"

    # J-96 cell
    BTO_0002028 = "BTO_0002028"
    J_96_CELL = "BTO_0002028"

    # myoma cell
    BTO_0002029 = "BTO_0002029"
    MYOMA_CELL = "BTO_0002029"

    # natural killer cell line
    BTO_0002030 = "BTO_0002030"
    NATURAL_KILLER_CELL_LINE = "BTO_0002030"

    # RNK-16 cell
    BTO_0002031 = "BTO_0002031"
    RNK_16_CELL = "BTO_0002031"

    # T-84 cell
    BTO_0002032 = "BTO_0002032"
    T_84_CELL = "BTO_0002032"

    # EFO-27 cell
    BTO_0002033 = "BTO_0002033"
    EFO_27_CELL = "BTO_0002033"

    # SK-UT-1 cell
    BTO_0002034 = "BTO_0002034"
    SK_UT_1_CELL = "BTO_0002034"

    # U-251MG cell
    BTO_0002035 = "BTO_0002035"
    U_251MG_CELL = "BTO_0002035"

    # U-87MG cell
    BTO_0002036 = "BTO_0002036"
    U_87MG_CELL = "BTO_0002036"

    # M-1 myeloid leukemia cell
    BTO_0002037 = "BTO_0002037"
    M_1_MYELOID_LEUKEMIA_CELL = "BTO_0002037"

    # osteocyte
    BTO_0002038 = "BTO_0002038"
    OSTEOCYTE = "BTO_0002038"

    # KMST-6 cell
    BTO_0002039 = "BTO_0002039"
    KMST_6_CELL = "BTO_0002039"

    # KMST-6/T cell
    BTO_0002040 = "BTO_0002040"
    KMST_6_T_CELL = "BTO_0002040"

    # KMS-6 cell
    BTO_0002041 = "BTO_0002041"
    KMS_6_CELL = "BTO_0002041"

    # dendritic cell
    BTO_0002042 = "BTO_0002042"
    DENDRITIC_CELL = "BTO_0002042"

    # ECV-304 cell
    BTO_0002043 = "BTO_0002043"
    ECV_304_CELL = "BTO_0002043"

    # frond tip
    BTO_0002044 = "BTO_0002044"
    FROND_TIP = "BTO_0002044"

    # capillary
    BTO_0002045 = "BTO_0002045"
    CAPILLARY = "BTO_0002045"

    # spermatozoid
    BTO_0002046 = "BTO_0002046"
    SPERMATOZOID = "BTO_0002046"

    # Colo-320 cell
    BTO_0002047 = "BTO_0002047"
    COLO_320_CELL = "BTO_0002047"

    # slug stage
    BTO_0002048 = "BTO_0002048"
    SLUG_STAGE = "BTO_0002048"

    # Chang cell
    BTO_0002049 = "BTO_0002049"
    CHANG_CELL = "BTO_0002049"

    # osteogenic cell
    BTO_0002050 = "BTO_0002050"
    OSTEOGENIC_CELL = "BTO_0002050"

    # preosteoblast
    BTO_0002051 = "BTO_0002051"
    PREOSTEOBLAST = "BTO_0002051"

    # osteogenic cell line
    BTO_0002052 = "BTO_0002052"
    OSTEOGENIC_CELL_LINE = "BTO_0002052"

    # seminal vesicle fluid
    BTO_0002053 = "BTO_0002053"
    SEMINAL_VESICLE_FLUID = "BTO_0002053"

    # Dunn cell
    BTO_0002054 = "BTO_0002054"
    DUNN_CELL = "BTO_0002054"

    # XD-6 cell
    BTO_0002055 = "BTO_0002055"
    XD_6_CELL = "BTO_0002055"

    # siphon
    BTO_0002056 = "BTO_0002056"
    SIPHON = "BTO_0002056"

    # lung adenocarcinoma cell
    BTO_0002057 = "BTO_0002057"
    LUNG_ADENOCARCINOMA_CELL = "BTO_0002057"

    # non-small cell lung cancer cell
    BTO_0002058 = "BTO_0002058"
    NON_SMALL_CELL_LUNG_CANCER_CELL = "BTO_0002058"

    # large cell carcinoma cell
    BTO_0002059 = "BTO_0002059"
    LARGE_CELL_CARCINOMA_CELL = "BTO_0002059"

    # bronchioalveolar carcinoma cell
    BTO_0002060 = "BTO_0002060"
    BRONCHIOALVEOLAR_CARCINOMA_CELL = "BTO_0002060"

    # bronchogenic carcinoma cell
    BTO_0002061 = "BTO_0002061"
    BRONCHOGENIC_CARCINOMA_CELL = "BTO_0002061"

    # B-lymphoblastoid cell line
    BTO_0002062 = "BTO_0002062"
    B_LYMPHOBLASTOID_CELL_LINE = "BTO_0002062"

    # Colo-720L cell
    BTO_0002063 = "BTO_0002063"
    COLO_720L_CELL = "BTO_0002063"

    # stromal cell
    BTO_0002064 = "BTO_0002064"
    STROMAL_CELL = "BTO_0002064"

    # venom apparatus
    BTO_0002065 = "BTO_0002065"
    VENOM_APPARATUS = "BTO_0002065"

    # venom sac
    BTO_0002066 = "BTO_0002066"
    VENOM_SAC = "BTO_0002066"

    # stinger
    BTO_0002067 = "BTO_0002067"
    STINGER = "BTO_0002067"

    # scent gland
    BTO_0002068 = "BTO_0002068"
    SCENT_GLAND = "BTO_0002068"

    # wax gland
    BTO_0002069 = "BTO_0002069"
    WAX_GLAND = "BTO_0002069"

    # KS-IMM cell
    BTO_0002070 = "BTO_0002070"
    KS_IMM_CELL = "BTO_0002070"

    # Kaposi's sarcoma cell
    BTO_0002071 = "BTO_0002071"
    KAPOSI_S_SARCOMA_CELL = "BTO_0002071"

    # squamous epithelium
    BTO_0002072 = "BTO_0002072"
    SQUAMOUS_EPITHELIUM = "BTO_0002072"

    # pavement epithelium
    BTO_0002073 = "BTO_0002073"
    PAVEMENT_EPITHELIUM = "BTO_0002073"

    # stratified epithelium
    BTO_0002074 = "BTO_0002074"
    STRATIFIED_EPITHELIUM = "BTO_0002074"

    # mesenchymal epithelium
    BTO_0002075 = "BTO_0002075"
    MESENCHYMAL_EPITHELIUM = "BTO_0002075"

    # osteomalacia cell
    BTO_0002076 = "BTO_0002076"
    OSTEOMALACIA_CELL = "BTO_0002076"

    # oncogenic osteomalacia cell
    BTO_0002077 = "BTO_0002077"
    ONCOGENIC_OSTEOMALACIA_CELL = "BTO_0002077"

    # hepatic osteomalacia cell
    BTO_0002078 = "BTO_0002078"
    HEPATIC_OSTEOMALACIA_CELL = "BTO_0002078"

    # puerperal osteomalacia cell
    BTO_0002079 = "BTO_0002079"
    PUERPERAL_OSTEOMALACIA_CELL = "BTO_0002079"

    # renal tubular osteomalacia cell
    BTO_0002080 = "BTO_0002080"
    RENAL_TUBULAR_OSTEOMALACIA_CELL = "BTO_0002080"

    # senile osteomalacia cell
    BTO_0002081 = "BTO_0002081"
    SENILE_OSTEOMALACIA_CELL = "BTO_0002081"

    # subdural space
    BTO_0002082 = "BTO_0002082"
    SUBDURAL_SPACE = "BTO_0002082"

    # perilymphatic space
    BTO_0002083 = "BTO_0002083"
    PERILYMPHATIC_SPACE = "BTO_0002083"

    # anterior chamber of the eye
    BTO_0002084 = "BTO_0002084"
    ANTERIOR_CHAMBER_OF_THE_EYE = "BTO_0002084"

    # chamber of the eye
    BTO_0002085 = "BTO_0002085"
    CHAMBER_OF_THE_EYE = "BTO_0002085"

    # posterior chamber of the eye
    BTO_0002086 = "BTO_0002086"
    POSTERIOR_CHAMBER_OF_THE_EYE = "BTO_0002086"

    # vitreous chamber of the eye
    BTO_0002087 = "BTO_0002087"
    VITREOUS_CHAMBER_OF_THE_EYE = "BTO_0002087"

    # ependymoma cell
    BTO_0002088 = "BTO_0002088"
    EPENDYMOMA_CELL = "BTO_0002088"

    # CAL-72 cell
    BTO_0002089 = "BTO_0002089"
    CAL_72_CELL = "BTO_0002089"

    # endophytic retinoblastoma cell
    BTO_0002090 = "BTO_0002090"
    ENDOPHYTIC_RETINOBLASTOMA_CELL = "BTO_0002090"

    # exophytic retinoblastoma cell
    BTO_0002091 = "BTO_0002091"
    EXOPHYTIC_RETINOBLASTOMA_CELL = "BTO_0002091"

    # ganglioglioma cell
    BTO_0002092 = "BTO_0002092"
    GANGLIOGLIOMA_CELL = "BTO_0002092"

    # ganglioneuroma cell
    BTO_0002093 = "BTO_0002093"
    GANGLIONEUROMA_CELL = "BTO_0002093"

    # ganglioneurofibroma cell
    BTO_0002094 = "BTO_0002094"
    GANGLIONEUROFIBROMA_CELL = "BTO_0002094"

    # nasal glioma cell
    BTO_0002095 = "BTO_0002095"
    NASAL_GLIOMA_CELL = "BTO_0002095"

    # nasal cavity
    BTO_0002096 = "BTO_0002096"
    NASAL_CAVITY = "BTO_0002096"

    # pharyngeal cavity
    BTO_0002097 = "BTO_0002097"
    PHARYNGEAL_CAVITY = "BTO_0002097"

    # tympanum
    BTO_0002098 = "BTO_0002098"
    TYMPANUM = "BTO_0002098"

    # middle ear
    BTO_0002099 = "BTO_0002099"
    MIDDLE_EAR = "BTO_0002099"

    # outer ear
    BTO_0002100 = "BTO_0002100"
    OUTER_EAR = "BTO_0002100"

    # multiple myeloma cell
    BTO_0002101 = "BTO_0002101"
    MULTIPLE_MYELOMA_CELL = "BTO_0002101"

    # MOPC-104E cell
    BTO_0002102 = "BTO_0002102"
    MOPC_104E_CELL = "BTO_0002102"

    # MOPC-173 cell
    BTO_0002103 = "BTO_0002103"
    MOPC_173_CELL = "BTO_0002103"

    # BE(2)-M17 cell
    BTO_0002104 = "BTO_0002104"
    BE_2__M17_CELL = "BTO_0002104"

    # perisympathetic organ
    BTO_0002105 = "BTO_0002105"
    PERISYMPATHETIC_ORGAN = "BTO_0002105"

    # neurohemal organ
    BTO_0002106 = "BTO_0002106"
    NEUROHEMAL_ORGAN = "BTO_0002106"

    # submucosa
    BTO_0002107 = "BTO_0002107"
    SUBMUCOSA = "BTO_0002107"

    # tela submucosa bronchiorum
    BTO_0002108 = "BTO_0002108"
    TELA_SUBMUCOSA_BRONCHIORUM = "BTO_0002108"

    # tela submucosa esophagi
    BTO_0002109 = "BTO_0002109"
    TELA_SUBMUCOSA_ESOPHAGI = "BTO_0002109"

    # tela submucosa gastris
    BTO_0002110 = "BTO_0002110"
    TELA_SUBMUCOSA_GASTRIS = "BTO_0002110"

    # tela submucosa intestini crassi
    BTO_0002111 = "BTO_0002111"
    TELA_SUBMUCOSA_INTESTINI_CRASSI = "BTO_0002111"

    # tela submucosa intestini tenuis
    BTO_0002112 = "BTO_0002112"
    TELA_SUBMUCOSA_INTESTINI_TENUIS = "BTO_0002112"

    # tela submucosa pharyngis
    BTO_0002113 = "BTO_0002113"
    TELA_SUBMUCOSA_PHARYNGIS = "BTO_0002113"

    # tela submucosa recti
    BTO_0002114 = "BTO_0002114"
    TELA_SUBMUCOSA_RECTI = "BTO_0002114"

    # tela submucosa tracheae
    BTO_0002115 = "BTO_0002115"
    TELA_SUBMUCOSA_TRACHEAE = "BTO_0002115"

    # tela submucosa tubae uterinae
    BTO_0002116 = "BTO_0002116"
    TELA_SUBMUCOSA_TUBAE_UTERINAE = "BTO_0002116"

    # tela submucosa vesicae urinariae
    BTO_0002117 = "BTO_0002117"
    TELA_SUBMUCOSA_VESICAE_URINARIAE = "BTO_0002117"

    # culture condition:collagen-grown cell
    BTO_0002118 = "BTO_0002118"
    CULTURE_CONDITION_COLLAGEN_GROWN_CELL = "BTO_0002118"

    # spikelet
    BTO_0002119 = "BTO_0002119"
    SPIKELET = "BTO_0002119"

    # pyloric cecum
    BTO_0002120 = "BTO_0002120"
    PYLORIC_CECUM = "BTO_0002120"

    # pyloric stomach
    BTO_0002121 = "BTO_0002121"
    PYLORIC_STOMACH = "BTO_0002121"

    # cardiac stomach
    BTO_0002122 = "BTO_0002122"
    CARDIAC_STOMACH = "BTO_0002122"

    # primitive endoderm
    BTO_0002123 = "BTO_0002123"
    PRIMITIVE_ENDODERM = "BTO_0002123"

    # ampulla
    BTO_0002124 = "BTO_0002124"
    AMPULLA = "BTO_0002124"

    # water vascular system
    BTO_0002125 = "BTO_0002125"
    WATER_VASCULAR_SYSTEM = "BTO_0002125"

    # U-373MG cell
    BTO_0002126 = "BTO_0002126"
    U_373MG_CELL = "BTO_0002126"

    # U-138MG cell
    BTO_0002127 = "BTO_0002127"
    U_138MG_CELL = "BTO_0002127"

    # TX3868 cell
    BTO_0002128 = "BTO_0002128"
    TX3868_CELL = "BTO_0002128"

    # SK-MEL-1 cell
    BTO_0002129 = "BTO_0002129"
    SK_MEL_1_CELL = "BTO_0002129"

    # SK-MEL cell
    BTO_0002130 = "BTO_0002130"
    SK_MEL_CELL = "BTO_0002130"

    # SK-MEL-28 cell
    BTO_0002131 = "BTO_0002131"
    SK_MEL_28_CELL = "BTO_0002131"

    # SK-MEL-3 cell
    BTO_0002132 = "BTO_0002132"
    SK_MEL_3_CELL = "BTO_0002132"

    # SK-MEL-30 cell
    BTO_0002133 = "BTO_0002133"
    SK_MEL_30_CELL = "BTO_0002133"

    # SK-MEL-5 cell
    BTO_0002134 = "BTO_0002134"
    SK_MEL_5_CELL = "BTO_0002134"

    # INS-1 cell
    BTO_0002135 = "BTO_0002135"
    INS_1_CELL = "BTO_0002135"

    # NB-4 cell
    BTO_0002136 = "BTO_0002136"
    NB_4_CELL = "BTO_0002136"

    # MiaPaCa-2 cell
    BTO_0002137 = "BTO_0002137"
    MIAPACA_2_CELL = "BTO_0002137"

    # MiaPaCa cell
    BTO_0002138 = "BTO_0002138"
    MIAPACA_CELL = "BTO_0002138"

    # HS-683 cell
    BTO_0002139 = "BTO_0002139"
    HS_683_CELL = "BTO_0002139"

    # RPMI-7931 cell
    BTO_0002140 = "BTO_0002140"
    RPMI_7931_CELL = "BTO_0002140"

    # BCS-TC2 cell
    BTO_0002141 = "BTO_0002141"
    BCS_TC2_CELL = "BTO_0002141"

    # BRIN-BD11 cell
    BTO_0002142 = "BTO_0002142"
    BRIN_BD11_CELL = "BTO_0002142"

    # CEM-VCR R cell
    BTO_0002143 = "BTO_0002143"
    CEM_VCR_R_CELL = "BTO_0002143"

    # acute lymphoblastic leukemia cell line
    BTO_0002144 = "BTO_0002144"
    ACUTE_LYMPHOBLASTIC_LEUKEMIA_CELL_LINE = "BTO_0002144"

    # midgut cell line
    BTO_0002145 = "BTO_0002145"
    MIDGUT_CELL_LINE = "BTO_0002145"

    # CAL-62 cell
    BTO_0002146 = "BTO_0002146"
    CAL_62_CELL = "BTO_0002146"

    # type II intestinal metaplasia disease specific cell type
    BTO_0002147 = "BTO_0002147"
    TYPE_II_INTESTINAL_METAPLASIA_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0002147"

    # gas bladder
    BTO_0002148 = "BTO_0002148"
    GAS_BLADDER = "BTO_0002148"

    # gill raker
    BTO_0002149 = "BTO_0002149"
    GILL_RAKER = "BTO_0002149"

    # gill filament
    BTO_0002150 = "BTO_0002150"
    GILL_FILAMENT = "BTO_0002150"

    # gill raker sieve
    BTO_0002151 = "BTO_0002151"
    GILL_RAKER_SIEVE = "BTO_0002151"

    # gill arch
    BTO_0002152 = "BTO_0002152"
    GILL_ARCH = "BTO_0002152"

    # pharyngobranchial
    BTO_0002153 = "BTO_0002153"
    PHARYNGOBRANCHIAL = "BTO_0002153"

    # epibranchial
    BTO_0002154 = "BTO_0002154"
    EPIBRANCHIAL = "BTO_0002154"

    # ceratobranchial
    BTO_0002155 = "BTO_0002155"
    CERATOBRANCHIAL = "BTO_0002155"

    # hypobranchial
    BTO_0002156 = "BTO_0002156"
    HYPOBRANCHIAL = "BTO_0002156"

    # endochondral bone
    BTO_0002157 = "BTO_0002157"
    ENDOCHONDRAL_BONE = "BTO_0002157"

    # huelle cell
    BTO_0002158 = "BTO_0002158"
    HUELLE_CELL = "BTO_0002158"

    # cleistothecium
    BTO_0002159 = "BTO_0002159"
    CLEISTOTHECIUM = "BTO_0002159"

    # apothecium
    BTO_0002160 = "BTO_0002160"
    APOTHECIUM = "BTO_0002160"

    # ascocarp
    BTO_0002161 = "BTO_0002161"
    ASCOCARP = "BTO_0002161"

    # ascus
    BTO_0002162 = "BTO_0002162"
    ASCUS = "BTO_0002162"

    # gymnothecium
    BTO_0002163 = "BTO_0002163"
    GYMNOTHECIUM = "BTO_0002163"

    # perithecium
    BTO_0002164 = "BTO_0002164"
    PERITHECIUM = "BTO_0002164"

    # basidium
    BTO_0002165 = "BTO_0002165"
    BASIDIUM = "BTO_0002165"

    # basidiospore
    BTO_0002166 = "BTO_0002166"
    BASIDIOSPORE = "BTO_0002166"

    # mushroom
    BTO_0002167 = "BTO_0002167"
    MUSHROOM = "BTO_0002167"

    # juvenile
    BTO_0002168 = "BTO_0002168"
    JUVENILE = "BTO_0002168"

    # anterior commissure
    BTO_0002169 = "BTO_0002169"
    ANTERIOR_COMMISSURE = "BTO_0002169"

    # LOX cell
    BTO_0002170 = "BTO_0002170"
    LOX_CELL = "BTO_0002170"

    # amelanotic melanoma cell line
    BTO_0002171 = "BTO_0002171"
    AMELANOTIC_MELANOMA_CELL_LINE = "BTO_0002171"

    # ABFTL-6 cell
    BTO_0002172 = "BTO_0002172"
    ABFTL_6_CELL = "BTO_0002172"

    # tubercle
    BTO_0002173 = "BTO_0002173"
    TUBERCLE = "BTO_0002173"

    # parenchymal cell
    BTO_0002174 = "BTO_0002174"
    PARENCHYMAL_CELL = "BTO_0002174"

    # LLC-RK1 cell
    BTO_0002175 = "BTO_0002175"
    LLC_RK1_CELL = "BTO_0002175"

    # Pro-5 cell
    BTO_0002176 = "BTO_0002176"
    PRO_5_CELL = "BTO_0002176"

    # PR cell
    BTO_0002177 = "BTO_0002177"
    PR_CELL = "BTO_0002177"

    # HMEpC cell
    BTO_0002178 = "BTO_0002178"
    HMEPC_CELL = "BTO_0002178"

    # 184A1N4 cell
    BTO_0002179 = "BTO_0002179"
    _184A1N4_CELL = "BTO_0002179"

    # 184-B5 cell
    BTO_0002180 = "BTO_0002180"
    _184_B5_CELL = "BTO_0002180"

    # HEK-293T cell
    BTO_0002181 = "BTO_0002181"
    HEK_293T_CELL = "BTO_0002181"

    # 95D cell
    BTO_0002182 = "BTO_0002182"
    _95D_CELL = "BTO_0002182"

    # 95C cell
    BTO_0002183 = "BTO_0002183"
    _95C_CELL = "BTO_0002183"

    # culture condition:2,4-dichlorophenoxyacetate-grown cell
    BTO_0002184 = "BTO_0002184"
    CULTURE_CONDITION_2_4_DICHLOROPHENOXYACETATE_GROWN_CELL = "BTO_0002184"

    # culture condition:2-aminobenzoate-grown cell
    BTO_0002185 = "BTO_0002185"
    CULTURE_CONDITION_2_AMINOBENZOATE_GROWN_CELL = "BTO_0002185"

    # culture condition:2-chloroacrylate-grown cell
    BTO_0002186 = "BTO_0002186"
    CULTURE_CONDITION_2_CHLOROACRYLATE_GROWN_CELL = "BTO_0002186"

    # culture condition:3-nitrophenol grown-cell
    BTO_0002187 = "BTO_0002187"
    CULTURE_CONDITION_3_NITROPHENOL_GROWN_CELL = "BTO_0002187"

    # culture condition:alpha-pinene-grown cell
    BTO_0002188 = "BTO_0002188"
    CULTURE_CONDITION_ALPHA_PINENE_GROWN_CELL = "BTO_0002188"

    # culture condition:pullulan-grown cell
    BTO_0002189 = "BTO_0002189"
    CULTURE_CONDITION_PULLULAN_GROWN_CELL = "BTO_0002189"

    # culture condition:xylan-grown cell
    BTO_0002190 = "BTO_0002190"
    CULTURE_CONDITION_XYLAN_GROWN_CELL = "BTO_0002190"

    # fibre tract
    BTO_0002191 = "BTO_0002191"
    FIBRE_TRACT = "BTO_0002191"

    # SCC12b cell
    BTO_0002192 = "BTO_0002192"
    SCC12B_CELL = "BTO_0002192"

    # SCC-13 cell
    BTO_0002193 = "BTO_0002193"
    SCC_13_CELL = "BTO_0002193"

    # NHK cell
    BTO_0002194 = "BTO_0002194"
    NHK_CELL = "BTO_0002194"

    # vascular smooth muscle cell line
    BTO_0002195 = "BTO_0002195"
    VASCULAR_SMOOTH_MUSCLE_CELL_LINE = "BTO_0002195"

    # A10 cell
    BTO_0002196 = "BTO_0002196"
    A10_CELL = "BTO_0002196"

    # M22 cell
    BTO_0002197 = "BTO_0002197"
    M22_CELL = "BTO_0002197"

    # OC/CDE22 cell
    BTO_0002198 = "BTO_0002198"
    OC_CDE22_CELL = "BTO_0002198"

    # Colo-206F cell
    BTO_0002199 = "BTO_0002199"
    COLO_206F_CELL = "BTO_0002199"

    # Colo-678 cell
    BTO_0002200 = "BTO_0002200"
    COLO_678_CELL = "BTO_0002200"

    # HCT-15 cell
    BTO_0002201 = "BTO_0002201"
    HCT_15_CELL = "BTO_0002201"

    # lung squamous cell carcinoma cell line
    BTO_0002202 = "BTO_0002202"
    LUNG_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0002202"

    # SK-MES-1 cell
    BTO_0002203 = "BTO_0002203"
    SK_MES_1_CELL = "BTO_0002203"

    # palatine uvula
    BTO_0002204 = "BTO_0002204"
    PALATINE_UVULA = "BTO_0002204"

    # large cell lung cancer cell line
    BTO_0002205 = "BTO_0002205"
    LARGE_CELL_LUNG_CANCER_CELL_LINE = "BTO_0002205"

    # small cell lung cancer cell line
    BTO_0002206 = "BTO_0002206"
    SMALL_CELL_LUNG_CANCER_CELL_LINE = "BTO_0002206"

    # NCI-H460 cell
    BTO_0002207 = "BTO_0002207"
    NCI_H460_CELL = "BTO_0002207"

    # K6H6/B5 cell
    BTO_0002208 = "BTO_0002208"
    K6H6_B5_CELL = "BTO_0002208"

    # NCI-H596 cell
    BTO_0002209 = "BTO_0002209"
    NCI_H596_CELL = "BTO_0002209"

    # SiHa cell
    BTO_0002210 = "BTO_0002210"
    SIHA_CELL = "BTO_0002210"

    # oral squamous cell carcinoma cell line
    BTO_0002211 = "BTO_0002211"
    ORAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0002211"

    # cervical squamous cell carcinoma cell line
    BTO_0002212 = "BTO_0002212"
    CERVICAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0002212"

    # A-1207 cell
    BTO_0002213 = "BTO_0002213"
    A_1207_CELL = "BTO_0002213"

    # A-1235 cell
    BTO_0002214 = "BTO_0002214"
    A_1235_CELL = "BTO_0002214"

    # LN-319 cell
    BTO_0002215 = "BTO_0002215"
    LN_319_CELL = "BTO_0002215"

    # LN-428 cell
    BTO_0002216 = "BTO_0002216"
    LN_428_CELL = "BTO_0002216"

    # culture supernatant
    BTO_0002217 = "BTO_0002217"
    CULTURE_SUPERNATANT = "BTO_0002217"

    # chalazal cell
    BTO_0002218 = "BTO_0002218"
    CHALAZAL_CELL = "BTO_0002218"

    # adrenocortical carcinoma cell
    BTO_0002219 = "BTO_0002219"
    ADRENOCORTICAL_CARCINOMA_CELL = "BTO_0002219"

    # 15PC3 cell
    BTO_0002220 = "BTO_0002220"
    _15PC3_CELL = "BTO_0002220"

    # HLE-B3 cell
    BTO_0002221 = "BTO_0002221"
    HLE_B3_CELL = "BTO_0002221"

    # bract
    BTO_0002222 = "BTO_0002222"
    BRACT = "BTO_0002222"

    # BW/T200- cell
    BTO_0002223 = "BTO_0002223"
    BW_T200__CELL = "BTO_0002223"

    # cheek pouch
    BTO_0002224 = "BTO_0002224"
    CHEEK_POUCH = "BTO_0002224"

    # digestive gland cell line
    BTO_0002225 = "BTO_0002225"
    DIGESTIVE_GLAND_CELL_LINE = "BTO_0002225"

    # abalone digestive gland cell line
    BTO_0002226 = "BTO_0002226"
    ABALONE_DIGESTIVE_GLAND_CELL_LINE = "BTO_0002226"

    # culture condition:citrate-grown cell
    BTO_0002227 = "BTO_0002227"
    CULTURE_CONDITION_CITRATE_GROWN_CELL = "BTO_0002227"

    # culture condition:light-grown cell
    BTO_0002228 = "BTO_0002228"
    CULTURE_CONDITION_LIGHT_GROWN_CELL = "BTO_0002228"

    # culture condition:heme-grown cell
    BTO_0002229 = "BTO_0002229"
    CULTURE_CONDITION_HEME_GROWN_CELL = "BTO_0002229"

    # culture condition:naphthalene-grown cell
    BTO_0002230 = "BTO_0002230"
    CULTURE_CONDITION_NAPHTHALENE_GROWN_CELL = "BTO_0002230"

    # culture condition:porcine gastric mucin-grown cell
    BTO_0002231 = "BTO_0002231"
    CULTURE_CONDITION_PORCINE_GASTRIC_MUCIN_GROWN_CELL = "BTO_0002231"

    # culture condition:taurine-grown cell
    BTO_0002232 = "BTO_0002232"
    CULTURE_CONDITION_TAURINE_GROWN_CELL = "BTO_0002232"

    # culture fluid
    BTO_0002233 = "BTO_0002233"
    CULTURE_FLUID = "BTO_0002233"

    # culture-condition:L-arginine-grown cell
    BTO_0002234 = "BTO_0002234"
    CULTURE_CONDITION_L_ARGININE_GROWN_CELL = "BTO_0002234"

    # Calu-6 cell
    BTO_0002235 = "BTO_0002235"
    CALU_6_CELL = "BTO_0002235"

    # ovarian cumulus cell
    BTO_0002236 = "BTO_0002236"
    OVARIAN_CUMULUS_CELL = "BTO_0002236"

    # ectomycorrhiza
    BTO_0002237 = "BTO_0002237"
    ECTOMYCORRHIZA = "BTO_0002237"

    # endomycorrhiza
    BTO_0002238 = "BTO_0002238"
    ENDOMYCORRHIZA = "BTO_0002238"

    # endectomycorrhiza
    BTO_0002239 = "BTO_0002239"
    ENDECTOMYCORRHIZA = "BTO_0002239"

    # exodermis
    BTO_0002240 = "BTO_0002240"
    EXODERMIS = "BTO_0002240"

    # eyelid
    BTO_0002241 = "BTO_0002241"
    EYELID = "BTO_0002241"

    # oral epithelial cell
    BTO_0002242 = "BTO_0002242"
    ORAL_EPITHELIAL_CELL = "BTO_0002242"

    # hypanthium
    BTO_0002243 = "BTO_0002243"
    HYPANTHIUM = "BTO_0002243"

    # flower stalk
    BTO_0002244 = "BTO_0002244"
    FLOWER_STALK = "BTO_0002244"

    # foreskin fibroblast cell line
    BTO_0002245 = "BTO_0002245"
    FORESKIN_FIBROBLAST_CELL_LINE = "BTO_0002245"

    # globus pallidus
    BTO_0002246 = "BTO_0002246"
    GLOBUS_PALLIDUS = "BTO_0002246"

    # globus pallidus lateralis
    BTO_0002247 = "BTO_0002247"
    GLOBUS_PALLIDUS_LATERALIS = "BTO_0002247"

    # globus pallidus medialis
    BTO_0002248 = "BTO_0002248"
    GLOBUS_PALLIDUS_MEDIALIS = "BTO_0002248"

    # cervical canal
    BTO_0002249 = "BTO_0002249"
    CERVICAL_CANAL = "BTO_0002249"

    # nucleus lentiformis
    BTO_0002250 = "BTO_0002250"
    NUCLEUS_LENTIFORMIS = "BTO_0002250"

    # lamina medullaris medialis corporis striati
    BTO_0002251 = "BTO_0002251"
    LAMINA_MEDULLARIS_MEDIALIS_CORPORIS_STRIATI = "BTO_0002251"

    # subthalamic nucleus
    BTO_0002252 = "BTO_0002252"
    SUBTHALAMIC_NUCLEUS = "BTO_0002252"

    # GOTO cell
    BTO_0002253 = "BTO_0002253"
    GOTO_CELL = "BTO_0002253"

    # vas efferens
    BTO_0002254 = "BTO_0002254"
    VAS_EFFERENS = "BTO_0002254"

    # HCT-8 cell
    BTO_0002255 = "BTO_0002255"
    HCT_8_CELL = "BTO_0002255"

    # heterotroph
    BTO_0002256 = "BTO_0002256"
    HETEROTROPH = "BTO_0002256"

    # heterotrophic cell
    BTO_0002257 = "BTO_0002257"
    HETEROTROPHIC_CELL = "BTO_0002257"

    # autotroph
    BTO_0002258 = "BTO_0002258"
    AUTOTROPH = "BTO_0002258"

    # autotrophic cell
    BTO_0002259 = "BTO_0002259"
    AUTOTROPHIC_CELL = "BTO_0002259"

    # HS-68 cell
    BTO_0002260 = "BTO_0002260"
    HS_68_CELL = "BTO_0002260"

    # fungus form
    BTO_0002261 = "BTO_0002261"
    FUNGUS_FORM = "BTO_0002261"

    # plant pedicel
    BTO_0002262 = "BTO_0002262"
    PLANT_PEDICEL = "BTO_0002262"

    # ventriculus
    BTO_0002263 = "BTO_0002263"
    VENTRICULUS = "BTO_0002263"

    # dried cell
    BTO_0002264 = "BTO_0002264"
    DRIED_CELL = "BTO_0002264"

    # microplasmodium
    BTO_0002265 = "BTO_0002265"
    MICROPLASMODIUM = "BTO_0002265"

    # honey sac
    BTO_0002266 = "BTO_0002266"
    HONEY_SAC = "BTO_0002266"

    # rhabdomyosarcoma cell line
    BTO_0002267 = "BTO_0002267"
    RHABDOMYOSARCOMA_CELL_LINE = "BTO_0002267"

    # MLE-12 cell
    BTO_0002268 = "BTO_0002268"
    MLE_12_CELL = "BTO_0002268"

    # JEG-3 cell
    BTO_0002269 = "BTO_0002269"
    JEG_3_CELL = "BTO_0002269"

    # MCF-7/2a cell
    BTO_0002270 = "BTO_0002270"
    MCF_7_2A_CELL = "BTO_0002270"

    # MCS-2 cell
    BTO_0002271 = "BTO_0002271"
    MCS_2_CELL = "BTO_0002271"

    # merozoite
    BTO_0002272 = "BTO_0002272"
    MEROZOITE = "BTO_0002272"

    # ileocecum
    BTO_0002273 = "BTO_0002273"
    ILEOCECUM = "BTO_0002273"

    # BHT-101 cell
    BTO_0002274 = "BTO_0002274"
    BHT_101_CELL = "BTO_0002274"

    # lateral hypodermal chord
    BTO_0002275 = "BTO_0002275"
    LATERAL_HYPODERMAL_CHORD = "BTO_0002275"

    # immobilized cell
    BTO_0002276 = "BTO_0002276"
    IMMOBILIZED_CELL = "BTO_0002276"

    # melanotroph
    BTO_0002277 = "BTO_0002277"
    MELANOTROPH = "BTO_0002277"

    # macrophage cell line
    BTO_0002278 = "BTO_0002278"
    MACROPHAGE_CELL_LINE = "BTO_0002278"

    # J-774 cell
    BTO_0002279 = "BTO_0002279"
    J_774_CELL = "BTO_0002279"

    # lignifying cell
    BTO_0002280 = "BTO_0002280"
    LIGNIFYING_CELL = "BTO_0002280"

    # YZI-1S cell
    BTO_0002281 = "BTO_0002281"
    YZI_1S_CELL = "BTO_0002281"

    # Pt-K2 cell
    BTO_0002282 = "BTO_0002282"
    PT_K2_CELL = "BTO_0002282"

    # NCI-H157 cell
    BTO_0002283 = "BTO_0002283"
    NCI_H157_CELL = "BTO_0002283"

    # MIN-6 cell
    BTO_0002284 = "BTO_0002284"
    MIN_6_CELL = "BTO_0002284"

    # granulosa cell line
    BTO_0002285 = "BTO_0002285"
    GRANULOSA_CELL_LINE = "BTO_0002285"

    # POGS-5 cell
    BTO_0002286 = "BTO_0002286"
    POGS_5_CELL = "BTO_0002286"

    # POGRS-1 cell
    BTO_0002287 = "BTO_0002287"
    POGRS_1_CELL = "BTO_0002287"

    # GLHR-15 cell
    BTO_0002288 = "BTO_0002288"
    GLHR_15_CELL = "BTO_0002288"

    # GFSHR-17 cell
    BTO_0002289 = "BTO_0002289"
    GFSHR_17_CELL = "BTO_0002289"

    # primary cell line
    BTO_0002290 = "BTO_0002290"
    PRIMARY_CELL_LINE = "BTO_0002290"

    # SP2/0-AG14 cell
    BTO_0002291 = "BTO_0002291"
    SP2_0_AG14_CELL = "BTO_0002291"

    # flagellum
    BTO_0002292 = "BTO_0002292"
    FLAGELLUM = "BTO_0002292"

    # SAKRTLS 12.1 cell
    BTO_0002293 = "BTO_0002293"
    SAKRTLS_12_1_CELL = "BTO_0002293"

    # solid substrate culture
    BTO_0002294 = "BTO_0002294"
    SOLID_SUBSTRATE_CULTURE = "BTO_0002294"

    # podocyte
    BTO_0002295 = "BTO_0002295"
    PODOCYTE = "BTO_0002295"

    # capsular epithelium
    BTO_0002296 = "BTO_0002296"
    CAPSULAR_EPITHELIUM = "BTO_0002296"

    # renal glomerular capsule
    BTO_0002297 = "BTO_0002297"
    RENAL_GLOMERULAR_CAPSULE = "BTO_0002297"

    # inferior olivary complex
    BTO_0002298 = "BTO_0002298"
    INFERIOR_OLIVARY_COMPLEX = "BTO_0002298"

    # oliva
    BTO_0002299 = "BTO_0002299"
    OLIVA = "BTO_0002299"

    # hilum nuclei olivaris inferioris
    BTO_0002300 = "BTO_0002300"
    HILUM_NUCLEI_OLIVARIS_INFERIORIS = "BTO_0002300"

    # mucinous cystadenoma cell
    BTO_0002301 = "BTO_0002301"
    MUCINOUS_CYSTADENOMA_CELL = "BTO_0002301"

    # inferior mesenteric artery
    BTO_0002302 = "BTO_0002302"
    INFERIOR_MESENTERIC_ARTERY = "BTO_0002302"

    # superior mesenteric artery
    BTO_0002303 = "BTO_0002303"
    SUPERIOR_MESENTERIC_ARTERY = "BTO_0002303"

    # protoscolex
    BTO_0002304 = "BTO_0002304"
    PROTOSCOLEX = "BTO_0002304"

    # scolex
    BTO_0002305 = "BTO_0002305"
    SCOLEX = "BTO_0002305"

    # ARO cell
    BTO_0002306 = "BTO_0002306"
    ARO_CELL = "BTO_0002306"

    # yeast form
    BTO_0002307 = "BTO_0002307"
    YEAST_FORM = "BTO_0002307"

    # myoepithelium
    BTO_0002308 = "BTO_0002308"
    MYOEPITHELIUM = "BTO_0002308"

    # myoepithelial cell
    BTO_0002309 = "BTO_0002309"
    MYOEPITHELIAL_CELL = "BTO_0002309"

    # mammary myoepithelium
    BTO_0002310 = "BTO_0002310"
    MAMMARY_MYOEPITHELIUM = "BTO_0002310"

    # mammary myoepithelial cell
    BTO_0002311 = "BTO_0002311"
    MAMMARY_MYOEPITHELIAL_CELL = "BTO_0002311"

    # mature cell
    BTO_0002312 = "BTO_0002312"
    MATURE_CELL = "BTO_0002312"

    # immature cell
    BTO_0002313 = "BTO_0002313"
    IMMATURE_CELL = "BTO_0002313"

    # satellite cell
    BTO_0002314 = "BTO_0002314"
    SATELLITE_CELL = "BTO_0002314"

    # supporting cell
    BTO_0002315 = "BTO_0002315"
    SUPPORTING_CELL = "BTO_0002315"

    # stellate cell
    BTO_0002316 = "BTO_0002316"
    STELLATE_CELL = "BTO_0002316"

    # slow muscle
    BTO_0002317 = "BTO_0002317"
    SLOW_MUSCLE = "BTO_0002317"

    # fast muscle
    BTO_0002318 = "BTO_0002318"
    FAST_MUSCLE = "BTO_0002318"

    # skeletal muscle fiber
    BTO_0002319 = "BTO_0002319"
    SKELETAL_MUSCLE_FIBER = "BTO_0002319"

    # cardiac muscle fiber
    BTO_0002320 = "BTO_0002320"
    CARDIAC_MUSCLE_FIBER = "BTO_0002320"

    # intermediate muscle fiber
    BTO_0002321 = "BTO_0002321"
    INTERMEDIATE_MUSCLE_FIBER = "BTO_0002321"

    # cell property
    BTO_0002322 = "BTO_0002322"
    CELL_PROPERTY = "BTO_0002322"

    # eccrine sweat gland
    BTO_0002323 = "BTO_0002323"
    ECCRINE_SWEAT_GLAND = "BTO_0002323"

    # merocrine gland
    BTO_0002324 = "BTO_0002324"
    MEROCRINE_GLAND = "BTO_0002324"

    # holocrine gland
    BTO_0002325 = "BTO_0002325"
    HOLOCRINE_GLAND = "BTO_0002325"

    # breast apocrine carcinoma cell
    BTO_0002326 = "BTO_0002326"
    BREAST_APOCRINE_CARCINOMA_CELL = "BTO_0002326"

    # stem cortex
    BTO_0002327 = "BTO_0002327"
    STEM_CORTEX = "BTO_0002327"

    # ventral nerve cord
    BTO_0002328 = "BTO_0002328"
    VENTRAL_NERVE_CORD = "BTO_0002328"

    # dorsal nerve cord
    BTO_0002329 = "BTO_0002329"
    DORSAL_NERVE_CORD = "BTO_0002329"

    # lamina propria
    BTO_0002330 = "BTO_0002330"
    LAMINA_PROPRIA = "BTO_0002330"

    # PLHC-1 cell
    BTO_0002331 = "BTO_0002331"
    PLHC_1_CELL = "BTO_0002331"

    # monocytic leukemia cell line
    BTO_0002332 = "BTO_0002332"
    MONOCYTIC_LEUKEMIA_CELL_LINE = "BTO_0002332"

    # Mono-Mac-6 cell
    BTO_0002333 = "BTO_0002333"
    MONO_MAC_6_CELL = "BTO_0002333"

    # retinal pigment epithelium cell line
    BTO_0002334 = "BTO_0002334"
    RETINAL_PIGMENT_EPITHELIUM_CELL_LINE = "BTO_0002334"

    # ARPE-19 cell
    BTO_0002335 = "BTO_0002335"
    ARPE_19_CELL = "BTO_0002335"

    # culture condition:arabitol-grown cell
    BTO_0002336 = "BTO_0002336"
    CULTURE_CONDITION_ARABITOL_GROWN_CELL = "BTO_0002336"

    # culture condition:cellobiose-grown cell
    BTO_0002337 = "BTO_0002337"
    CULTURE_CONDITION_CELLOBIOSE_GROWN_CELL = "BTO_0002337"

    # culture condition:cellulose-grown cell
    BTO_0002338 = "BTO_0002338"
    CULTURE_CONDITION_CELLULOSE_GROWN_CELL = "BTO_0002338"

    # culture condition:fluoride-grown cell
    BTO_0002339 = "BTO_0002339"
    CULTURE_CONDITION_FLUORIDE_GROWN_CELL = "BTO_0002339"

    # plant collar
    BTO_0002340 = "BTO_0002340"
    PLANT_COLLAR = "BTO_0002340"

    # leaf collar
    BTO_0002341 = "BTO_0002341"
    LEAF_COLLAR = "BTO_0002341"

    # bradyzoite
    BTO_0002342 = "BTO_0002342"
    BRADYZOITE = "BTO_0002342"

    # tarsal bone
    BTO_0002343 = "BTO_0002343"
    TARSAL_BONE = "BTO_0002343"

    # electrocyte
    BTO_0002344 = "BTO_0002344"
    ELECTROCYTE = "BTO_0002344"

    # hindlimb
    BTO_0002345 = "BTO_0002345"
    HINDLIMB = "BTO_0002345"

    # fibula
    BTO_0002346 = "BTO_0002346"
    FIBULA = "BTO_0002346"

    # metatarsal bone
    BTO_0002347 = "BTO_0002347"
    METATARSAL_BONE = "BTO_0002347"

    # toe
    BTO_0002348 = "BTO_0002348"
    TOE = "BTO_0002348"

    # hallux
    BTO_0002349 = "BTO_0002349"
    HALLUX = "BTO_0002349"

    # digitus secundus pedis
    BTO_0002350 = "BTO_0002350"
    DIGITUS_SECUNDUS_PEDIS = "BTO_0002350"

    # digitus tertius pedis
    BTO_0002351 = "BTO_0002351"
    DIGITUS_TERTIUS_PEDIS = "BTO_0002351"

    # digitus quartis pedis
    BTO_0002352 = "BTO_0002352"
    DIGITUS_QUARTIS_PEDIS = "BTO_0002352"

    # digitum minimus pedis
    BTO_0002353 = "BTO_0002353"
    DIGITUM_MINIMUS_PEDIS = "BTO_0002353"

    # talus
    BTO_0002354 = "BTO_0002354"
    TALUS = "BTO_0002354"

    # calcaneal bone
    BTO_0002355 = "BTO_0002355"
    CALCANEAL_BONE = "BTO_0002355"

    # navicular bone
    BTO_0002356 = "BTO_0002356"
    NAVICULAR_BONE = "BTO_0002356"

    # cuboid bone
    BTO_0002357 = "BTO_0002357"
    CUBOID_BONE = "BTO_0002357"

    # lateral cuneiform bone
    BTO_0002358 = "BTO_0002358"
    LATERAL_CUNEIFORM_BONE = "BTO_0002358"

    # intermediate cuneiform bone
    BTO_0002359 = "BTO_0002359"
    INTERMEDIATE_CUNEIFORM_BONE = "BTO_0002359"

    # medial cuneiform bone
    BTO_0002360 = "BTO_0002360"
    MEDIAL_CUNEIFORM_BONE = "BTO_0002360"

    # osteochondroma cell
    BTO_0002361 = "BTO_0002361"
    OSTEOCHONDROMA_CELL = "BTO_0002361"

    # pancreatic duct
    BTO_0002362 = "BTO_0002362"
    PANCREATIC_DUCT = "BTO_0002362"

    # pancreatic ductal carcinoma cell
    BTO_0002363 = "BTO_0002363"
    PANCREATIC_DUCTAL_CARCINOMA_CELL = "BTO_0002363"

    # gastric pit
    BTO_0002364 = "BTO_0002364"
    GASTRIC_PIT = "BTO_0002364"

    # chondroblastoma cell
    BTO_0002365 = "BTO_0002365"
    CHONDROBLASTOMA_CELL = "BTO_0002365"

    # extravillous trophoblast
    BTO_0002366 = "BTO_0002366"
    EXTRAVILLOUS_TROPHOBLAST = "BTO_0002366"

    # cytotrophoblastic cell
    BTO_0002367 = "BTO_0002367"
    CYTOTROPHOBLASTIC_CELL = "BTO_0002367"

    # 3Y1-B clone 1 cell
    BTO_0002368 = "BTO_0002368"
    _3Y1_B_CLONE_1_CELL = "BTO_0002368"

    # HR-3Y1 cell
    BTO_0002369 = "BTO_0002369"
    HR_3Y1_CELL = "BTO_0002369"

    # colleterial gland
    BTO_0002370 = "BTO_0002370"
    COLLETERIAL_GLAND = "BTO_0002370"

    # macroplasmodium
    BTO_0002371 = "BTO_0002371"
    MACROPLASMODIUM = "BTO_0002371"

    # neuroepithelioma cell
    BTO_0002372 = "BTO_0002372"
    NEUROEPITHELIOMA_CELL = "BTO_0002372"

    # glioblastoma multiforme cell
    BTO_0002373 = "BTO_0002373"
    GLIOBLASTOMA_MULTIFORME_CELL = "BTO_0002373"

    # anaplastic astrocytoma cell
    BTO_0002374 = "BTO_0002374"
    ANAPLASTIC_ASTROCYTOMA_CELL = "BTO_0002374"

    # bronchiole
    BTO_0002375 = "BTO_0002375"
    BRONCHIOLE = "BTO_0002375"

    # duodenal gland
    BTO_0002376 = "BTO_0002376"
    DUODENAL_GLAND = "BTO_0002376"

    # SR-3Y1 cell
    BTO_0002377 = "BTO_0002377"
    SR_3Y1_CELL = "BTO_0002377"

    # pilocytic astrocytoma cell
    BTO_0002378 = "BTO_0002378"
    PILOCYTIC_ASTROCYTOMA_CELL = "BTO_0002378"

    # juvenile pilocytic astrocytoma cell
    BTO_0002379 = "BTO_0002379"
    JUVENILE_PILOCYTIC_ASTROCYTOMA_CELL = "BTO_0002379"

    # gastric adenocarcinoma cell line
    BTO_0002380 = "BTO_0002380"
    GASTRIC_ADENOCARCINOMA_CELL_LINE = "BTO_0002380"

    # MKN-28 cell
    BTO_0002381 = "BTO_0002381"
    MKN_28_CELL = "BTO_0002381"

    # MKN-7 cell
    BTO_0002382 = "BTO_0002382"
    MKN_7_CELL = "BTO_0002382"

    # MKN-74 cell
    BTO_0002383 = "BTO_0002383"
    MKN_74_CELL = "BTO_0002383"

    # MKN-1 cell
    BTO_0002384 = "BTO_0002384"
    MKN_1_CELL = "BTO_0002384"

    # GLC-4 cell
    BTO_0002385 = "BTO_0002385"
    GLC_4_CELL = "BTO_0002385"

    # GLC-4/ADR cell
    BTO_0002386 = "BTO_0002386"
    GLC_4_ADR_CELL = "BTO_0002386"

    # GLC-4/MITO cell
    BTO_0002387 = "BTO_0002387"
    GLC_4_MITO_CELL = "BTO_0002387"

    # GLC-4/CDDP cell
    BTO_0002388 = "BTO_0002388"
    GLC_4_CDDP_CELL = "BTO_0002388"

    # U-1285 cell
    BTO_0002389 = "BTO_0002389"
    U_1285_CELL = "BTO_0002389"

    # U-1568 cell
    BTO_0002390 = "BTO_0002390"
    U_1568_CELL = "BTO_0002390"

    # U-1285dox cell
    BTO_0002391 = "BTO_0002391"
    U_1285DOX_CELL = "BTO_0002391"

    # SGC-7901 cell
    BTO_0002392 = "BTO_0002392"
    SGC_7901_CELL = "BTO_0002392"

    # N-27 cell
    BTO_0002393 = "BTO_0002393"
    N_27_CELL = "BTO_0002393"

    # DC-3F cell
    BTO_0002394 = "BTO_0002394"
    DC_3F_CELL = "BTO_0002394"

    # DC-3F/ADX cell
    BTO_0002395 = "BTO_0002395"
    DC_3F_ADX_CELL = "BTO_0002395"

    # NIH-3T3-G185 cell
    BTO_0002396 = "BTO_0002396"
    NIH_3T3_G185_CELL = "BTO_0002396"

    # prostate gland epithelium
    BTO_0002397 = "BTO_0002397"
    PROSTATE_GLAND_EPITHELIUM = "BTO_0002397"

    # prostate epithelium cell line
    BTO_0002398 = "BTO_0002398"
    PROSTATE_EPITHELIUM_CELL_LINE = "BTO_0002398"

    # PNT-2 cell
    BTO_0002399 = "BTO_0002399"
    PNT_2_CELL = "BTO_0002399"

    # OLN-93 cell
    BTO_0002400 = "BTO_0002400"
    OLN_93_CELL = "BTO_0002400"

    # feather rachis
    BTO_0002401 = "BTO_0002401"
    FEATHER_RACHIS = "BTO_0002401"

    # oviduct epithelium
    BTO_0002402 = "BTO_0002402"
    OVIDUCT_EPITHELIUM = "BTO_0002402"

    # OS-RC-2 cell
    BTO_0002403 = "BTO_0002403"
    OS_RC_2_CELL = "BTO_0002403"

    # YMB-1 cell
    BTO_0002404 = "BTO_0002404"
    YMB_1_CELL = "BTO_0002404"

    # EoL-1 cell
    BTO_0002405 = "BTO_0002405"
    EOL_1_CELL = "BTO_0002405"

    # eosinophilic leukemia cell line
    BTO_0002406 = "BTO_0002406"
    EOSINOPHILIC_LEUKEMIA_CELL_LINE = "BTO_0002406"

    # spermary
    BTO_0002407 = "BTO_0002407"
    SPERMARY = "BTO_0002407"

    # NRK-52E cell
    BTO_0002408 = "BTO_0002408"
    NRK_52E_CELL = "BTO_0002408"

    # NRK-49F cell
    BTO_0002409 = "BTO_0002409"
    NRK_49F_CELL = "BTO_0002409"

    # giant cell carcinoma cell
    BTO_0002410 = "BTO_0002410"
    GIANT_CELL_CARCINOMA_CELL = "BTO_0002410"

    # giant cell carcinoma cell line
    BTO_0002411 = "BTO_0002411"
    GIANT_CELL_CARCINOMA_CELL_LINE = "BTO_0002411"

    # PG cell
    BTO_0002412 = "BTO_0002412"
    PG_CELL = "BTO_0002412"

    # PG-BE1 cell
    BTO_0002413 = "BTO_0002413"
    PG_BE1_CELL = "BTO_0002413"

    # PG-CL3 cell
    BTO_0002414 = "BTO_0002414"
    PG_CL3_CELL = "BTO_0002414"

    # PG-LH7 cell
    BTO_0002415 = "BTO_0002415"
    PG_LH7_CELL = "BTO_0002415"

    # NCI-H929 cell
    BTO_0002416 = "BTO_0002416"
    NCI_H929_CELL = "BTO_0002416"

    # helper T-lymphocyte
    BTO_0002417 = "BTO_0002417"
    HELPER_T_LYMPHOCYTE = "BTO_0002417"

    # NCI-H292 cell
    BTO_0002418 = "BTO_0002418"
    NCI_H292_CELL = "BTO_0002418"

    # SK-BR-3 cell
    BTO_0002419 = "BTO_0002419"
    SK_BR_3_CELL = "BTO_0002419"

    # monocytic leukemia cell
    BTO_0002420 = "BTO_0002420"
    MONOCYTIC_LEUKEMIA_CELL = "BTO_0002420"

    # eosinophilic leukemia cell
    BTO_0002421 = "BTO_0002421"
    EOSINOPHILIC_LEUKEMIA_CELL = "BTO_0002421"

    # mesothelium
    BTO_0002422 = "BTO_0002422"
    MESOTHELIUM = "BTO_0002422"

    # mesothelioma cell
    BTO_0002423 = "BTO_0002423"
    MESOTHELIOMA_CELL = "BTO_0002423"

    # mesothelioma cell line
    BTO_0002424 = "BTO_0002424"
    MESOTHELIOMA_CELL_LINE = "BTO_0002424"

    # MSTO-211H cell
    BTO_0002425 = "BTO_0002425"
    MSTO_211H_CELL = "BTO_0002425"

    # CHOP cell
    BTO_0002426 = "BTO_0002426"
    CHOP_CELL = "BTO_0002426"

    # KYSE-150 cell
    BTO_0002427 = "BTO_0002427"
    KYSE_150_CELL = "BTO_0002427"

    # esophageal squamous cell carcinoma cell line
    BTO_0002428 = "BTO_0002428"
    ESOPHAGEAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0002428"

    # HA22T/VGH cell
    BTO_0002429 = "BTO_0002429"
    HA22T_VGH_CELL = "BTO_0002429"

    # Lec15.1 CHO cell
    BTO_0002430 = "BTO_0002430"
    LEC15_1_CHO_CELL = "BTO_0002430"

    # HuO-3N1 cell
    BTO_0002431 = "BTO_0002431"
    HUO_3N1_CELL = "BTO_0002431"

    # prespore
    BTO_0002432 = "BTO_0002432"
    PRESPORE = "BTO_0002432"

    # genital primordium
    BTO_0002433 = "BTO_0002433"
    GENITAL_PRIMORDIUM = "BTO_0002433"

    # dorsal raphe nucleus
    BTO_0002434 = "BTO_0002434"
    DORSAL_RAPHE_NUCLEUS = "BTO_0002434"

    # colorectal mucosa
    BTO_0002435 = "BTO_0002435"
    COLORECTAL_MUCOSA = "BTO_0002435"

    # myenteric plexus
    BTO_0002436 = "BTO_0002436"
    MYENTERIC_PLEXUS = "BTO_0002436"

    # enteric plexus
    BTO_0002437 = "BTO_0002437"
    ENTERIC_PLEXUS = "BTO_0002437"

    # Dogiel's corpuscle
    BTO_0002438 = "BTO_0002438"
    DOGIEL_S_CORPUSCLE = "BTO_0002438"

    # genital mucosa
    BTO_0002439 = "BTO_0002439"
    GENITAL_MUCOSA = "BTO_0002439"

    # CX-1 cell
    BTO_0002440 = "BTO_0002440"
    CX_1_CELL = "BTO_0002440"

    # pericyte
    BTO_0002441 = "BTO_0002441"
    PERICYTE = "BTO_0002441"

    # tetrad of microspores
    BTO_0002442 = "BTO_0002442"
    TETRAD_OF_MICROSPORES = "BTO_0002442"

    # tetrad of pollen
    BTO_0002443 = "BTO_0002443"
    TETRAD_OF_POLLEN = "BTO_0002443"

    # basal forebrain
    BTO_0002444 = "BTO_0002444"
    BASAL_FOREBRAIN = "BTO_0002444"

    # diagonal band
    BTO_0002445 = "BTO_0002445"
    DIAGONAL_BAND = "BTO_0002445"

    # medial septum
    BTO_0002446 = "BTO_0002446"
    MEDIAL_SEPTUM = "BTO_0002446"

    # substantia innominata
    BTO_0002447 = "BTO_0002447"
    SUBSTANTIA_INNOMINATA = "BTO_0002447"

    # basal telencephalon
    BTO_0002448 = "BTO_0002448"
    BASAL_TELENCEPHALON = "BTO_0002448"

    # hypothalamic nucleus
    BTO_0002449 = "BTO_0002449"
    HYPOTHALAMIC_NUCLEUS = "BTO_0002449"

    # anterior hypothalamic nucleus
    BTO_0002450 = "BTO_0002450"
    ANTERIOR_HYPOTHALAMIC_NUCLEUS = "BTO_0002450"

    # dorsal hypothalamic nucleus
    BTO_0002451 = "BTO_0002451"
    DORSAL_HYPOTHALAMIC_NUCLEUS = "BTO_0002451"

    # thalamic nucleus
    BTO_0002452 = "BTO_0002452"
    THALAMIC_NUCLEUS = "BTO_0002452"

    # medial dorsal nucleus of thalamus
    BTO_0002453 = "BTO_0002453"
    MEDIAL_DORSAL_NUCLEUS_OF_THALAMUS = "BTO_0002453"

    # median nucleus of thalamus
    BTO_0002454 = "BTO_0002454"
    MEDIAN_NUCLEUS_OF_THALAMUS = "BTO_0002454"

    # anterior paraventricular nucleus
    BTO_0002455 = "BTO_0002455"
    ANTERIOR_PARAVENTRICULAR_NUCLEUS = "BTO_0002455"

    # posterior paraventricular nucleus
    BTO_0002456 = "BTO_0002456"
    POSTERIOR_PARAVENTRICULAR_NUCLEUS = "BTO_0002456"

    # nucleus parataenialis
    BTO_0002457 = "BTO_0002457"
    NUCLEUS_PARATAENIALIS = "BTO_0002457"

    # rhomboid nucleus
    BTO_0002458 = "BTO_0002458"
    RHOMBOID_NUCLEUS = "BTO_0002458"

    # nucleus reuniens
    BTO_0002459 = "BTO_0002459"
    NUCLEUS_REUNIENS = "BTO_0002459"

    # paraventricular nucleus
    BTO_0002460 = "BTO_0002460"
    PARAVENTRICULAR_NUCLEUS = "BTO_0002460"

    # posterior hypothalamic nucleus
    BTO_0002461 = "BTO_0002461"
    POSTERIOR_HYPOTHALAMIC_NUCLEUS = "BTO_0002461"

    # posterior nuclear complex of thalamus
    BTO_0002462 = "BTO_0002462"
    POSTERIOR_NUCLEAR_COMPLEX_OF_THALAMUS = "BTO_0002462"

    # ventral lateral complex of thalamus
    BTO_0002463 = "BTO_0002463"
    VENTRAL_LATERAL_COMPLEX_OF_THALAMUS = "BTO_0002463"

    # ventrobasal complex of thalamus
    BTO_0002464 = "BTO_0002464"
    VENTROBASAL_COMPLEX_OF_THALAMUS = "BTO_0002464"

    # nucleus ventralis posterolateralis thalamus
    BTO_0002465 = "BTO_0002465"
    NUCLEUS_VENTRALIS_POSTEROLATERALIS_THALAMUS = "BTO_0002465"

    # nucleus ventralis posteromedialis thalamus
    BTO_0002466 = "BTO_0002466"
    NUCLEUS_VENTRALIS_POSTEROMEDIALIS_THALAMUS = "BTO_0002466"

    # ventral nucleus of thalamus
    BTO_0002467 = "BTO_0002467"
    VENTRAL_NUCLEUS_OF_THALAMUS = "BTO_0002467"

    # ventral anterior nucleus of thalamus
    BTO_0002468 = "BTO_0002468"
    VENTRAL_ANTERIOR_NUCLEUS_OF_THALAMUS = "BTO_0002468"

    # ventral intermediate nucleus of thalamus
    BTO_0002469 = "BTO_0002469"
    VENTRAL_INTERMEDIATE_NUCLEUS_OF_THALAMUS = "BTO_0002469"

    # ventral medial complex of thalamus
    BTO_0002470 = "BTO_0002470"
    VENTRAL_MEDIAL_COMPLEX_OF_THALAMUS = "BTO_0002470"

    # culture condition:anaerobically-grown cell
    BTO_0002471 = "BTO_0002471"
    CULTURE_CONDITION_ANAEROBICALLY_GROWN_CELL = "BTO_0002471"

    # ventromedial hypothalamic nucleus
    BTO_0002472 = "BTO_0002472"
    VENTROMEDIAL_HYPOTHALAMIC_NUCLEUS = "BTO_0002472"

    # infundibular nucleus
    BTO_0002473 = "BTO_0002473"
    INFUNDIBULAR_NUCLEUS = "BTO_0002473"

    # dorsomedial nucleus of intermediate hypothalamus
    BTO_0002474 = "BTO_0002474"
    DORSOMEDIAL_NUCLEUS_OF_INTERMEDIATE_HYPOTHALAMUS = "BTO_0002474"

    # endopeduncular nucleus
    BTO_0002475 = "BTO_0002475"
    ENDOPEDUNCULAR_NUCLEUS = "BTO_0002475"

    # paraventricular nucleus of hypothalamus
    BTO_0002476 = "BTO_0002476"
    PARAVENTRICULAR_NUCLEUS_OF_HYPOTHALAMUS = "BTO_0002476"

    # cecal epithelium
    BTO_0002477 = "BTO_0002477"
    CECAL_EPITHELIUM = "BTO_0002477"

    # cervical epithelial cell
    BTO_0002478 = "BTO_0002478"
    CERVICAL_EPITHELIAL_CELL = "BTO_0002478"

    # posterior periventricular nucleus
    BTO_0002479 = "BTO_0002479"
    POSTERIOR_PERIVENTRICULAR_NUCLEUS = "BTO_0002479"

    # plume
    BTO_0002480 = "BTO_0002480"
    PLUME = "BTO_0002480"

    # lateral tuberal nucleus
    BTO_0002481 = "BTO_0002481"
    LATERAL_TUBERAL_NUCLEUS = "BTO_0002481"

    # gonadotrophic cell
    BTO_0002482 = "BTO_0002482"
    GONADOTROPHIC_CELL = "BTO_0002482"

    # interventricular septum
    BTO_0002483 = "BTO_0002483"
    INTERVENTRICULAR_SEPTUM = "BTO_0002483"

    # columnar cell
    BTO_0002484 = "BTO_0002484"
    COLUMNAR_CELL = "BTO_0002484"

    # atrial appendage
    BTO_0002485 = "BTO_0002485"
    ATRIAL_APPENDAGE = "BTO_0002485"

    # lupulin gland
    BTO_0002486 = "BTO_0002486"
    LUPULIN_GLAND = "BTO_0002486"

    # metacyclic form
    BTO_0002487 = "BTO_0002487"
    METACYCLIC_FORM = "BTO_0002487"

    # uterine leiomyosarcoma cell line
    BTO_0002488 = "BTO_0002488"
    UTERINE_LEIOMYOSARCOMA_CELL_LINE = "BTO_0002488"

    # promyelocytic leukemia cell line
    BTO_0002489 = "BTO_0002489"
    PROMYELOCYTIC_LEUKEMIA_CELL_LINE = "BTO_0002489"

    # culture condition:acetylacetone-grown cell
    BTO_0002490 = "BTO_0002490"
    CULTURE_CONDITION_ACETYLACETONE_GROWN_CELL = "BTO_0002490"

    # culture condition:4-hydroxyphenylacetate-grown cell
    BTO_0002491 = "BTO_0002491"
    CULTURE_CONDITION_4_HYDROXYPHENYLACETATE_GROWN_CELL = "BTO_0002491"

    # vestimentum
    BTO_0002492 = "BTO_0002492"
    VESTIMENTUM = "BTO_0002492"

    # CH12.LX cell
    BTO_0002493 = "BTO_0002493"
    CH12_LX_CELL = "BTO_0002493"

    # mesangium
    BTO_0002494 = "BTO_0002494"
    MESANGIUM = "BTO_0002494"

    # cerebral gyrus
    BTO_0002495 = "BTO_0002495"
    CEREBRAL_GYRUS = "BTO_0002495"

    # dentate gyrus
    BTO_0002496 = "BTO_0002496"
    DENTATE_GYRUS = "BTO_0002496"

    # fasciolar gyrus
    BTO_0002497 = "BTO_0002497"
    FASCIOLAR_GYRUS = "BTO_0002497"

    # arachnoid barrier layer
    BTO_0002498 = "BTO_0002498"
    ARACHNOID_BARRIER_LAYER = "BTO_0002498"

    # companion cell
    BTO_0002499 = "BTO_0002499"
    COMPANION_CELL = "BTO_0002499"

    # arachnoid trabecula
    BTO_0002500 = "BTO_0002500"
    ARACHNOID_TRABECULA = "BTO_0002500"

    # trabecula
    BTO_0002501 = "BTO_0002501"
    TRABECULA = "BTO_0002501"

    # kinetoplastid
    BTO_0002502 = "BTO_0002502"
    KINETOPLASTID = "BTO_0002502"

    # protozoan form
    BTO_0002503 = "BTO_0002503"
    PROTOZOAN_FORM = "BTO_0002503"

    # T-lymphoblastic leukemia cell line
    BTO_0002504 = "BTO_0002504"
    T_LYMPHOBLASTIC_LEUKEMIA_CELL_LINE = "BTO_0002504"

    # anaplastic large cell lymphoma cell
    BTO_0002505 = "BTO_0002505"
    ANAPLASTIC_LARGE_CELL_LYMPHOMA_CELL = "BTO_0002505"

    # enteric nervous system
    BTO_0002506 = "BTO_0002506"
    ENTERIC_NERVOUS_SYSTEM = "BTO_0002506"

    # autonomic nervous system
    BTO_0002507 = "BTO_0002507"
    AUTONOMIC_NERVOUS_SYSTEM = "BTO_0002507"

    # myenteron
    BTO_0002508 = "BTO_0002508"
    MYENTERON = "BTO_0002508"

    # corticotropic cell
    BTO_0002509 = "BTO_0002509"
    CORTICOTROPIC_CELL = "BTO_0002509"

    # myelomonocytic leukemia cell
    BTO_0002510 = "BTO_0002510"
    MYELOMONOCYTIC_LEUKEMIA_CELL = "BTO_0002510"

    # pinnule
    BTO_0002511 = "BTO_0002511"
    PINNULE = "BTO_0002511"

    # leaflet
    BTO_0002512 = "BTO_0002512"
    LEAFLET = "BTO_0002512"

    # Ewing's sarcoma cell
    BTO_0002513 = "BTO_0002513"
    EWING_S_SARCOMA_CELL = "BTO_0002513"

    # CN1.4 cell
    BTO_0002514 = "BTO_0002514"
    CN1_4_CELL = "BTO_0002514"

    # brain cortex cell line
    BTO_0002515 = "BTO_0002515"
    BRAIN_CORTEX_CELL_LINE = "BTO_0002515"

    # odontoclast
    BTO_0002516 = "BTO_0002516"
    ODONTOCLAST = "BTO_0002516"

    # follicular lymphoma cell line
    BTO_0002517 = "BTO_0002517"
    FOLLICULAR_LYMPHOMA_CELL_LINE = "BTO_0002517"

    # FL-18 cell
    BTO_0002518 = "BTO_0002518"
    FL_18_CELL = "BTO_0002518"

    # FL-218 cell
    BTO_0002519 = "BTO_0002519"
    FL_218_CELL = "BTO_0002519"

    # FL-318 cell
    BTO_0002520 = "BTO_0002520"
    FL_318_CELL = "BTO_0002520"

    # diffuse large B-cell lymphoma cell
    BTO_0002521 = "BTO_0002521"
    DIFFUSE_LARGE_B_CELL_LYMPHOMA_CELL = "BTO_0002521"

    # HBL-1 cell
    BTO_0002522 = "BTO_0002522"
    HBL_1_CELL = "BTO_0002522"

    # HBL-2 cell
    BTO_0002523 = "BTO_0002523"
    HBL_2_CELL = "BTO_0002523"

    # HEK-293A cell
    BTO_0002524 = "BTO_0002524"
    HEK_293A_CELL = "BTO_0002524"

    # cementum
    BTO_0002525 = "BTO_0002525"
    CEMENTUM = "BTO_0002525"

    # HBL-4 cell
    BTO_0002526 = "BTO_0002526"
    HBL_4_CELL = "BTO_0002526"

    # HBL-5 cell
    BTO_0002527 = "BTO_0002527"
    HBL_5_CELL = "BTO_0002527"

    # HBL-7 cell
    BTO_0002528 = "BTO_0002528"
    HBL_7_CELL = "BTO_0002528"

    # HBL-8 cell
    BTO_0002529 = "BTO_0002529"
    HBL_8_CELL = "BTO_0002529"

    # HBL-9 cell
    BTO_0002530 = "BTO_0002530"
    HBL_9_CELL = "BTO_0002530"

    # HBL-10 cell
    BTO_0002531 = "BTO_0002531"
    HBL_10_CELL = "BTO_0002531"

    # Kobayashi cell
    BTO_0002532 = "BTO_0002532"
    KOBAYASHI_CELL = "BTO_0002532"

    # HBL-11 cell
    BTO_0002533 = "BTO_0002533"
    HBL_11_CELL = "BTO_0002533"

    # HBL-3 cell
    BTO_0002534 = "BTO_0002534"
    HBL_3_CELL = "BTO_0002534"

    # Morris hepatoma 7800C1 cell
    BTO_0002535 = "BTO_0002535"
    MORRIS_HEPATOMA_7800C1_CELL = "BTO_0002535"

    # feather vane
    BTO_0002536 = "BTO_0002536"
    FEATHER_VANE = "BTO_0002536"

    # BNL CL.2 cell
    BTO_0002537 = "BTO_0002537"
    BNL_CL_2_CELL = "BTO_0002537"

    # LLC-PK-1-GR101 cell
    BTO_0002538 = "BTO_0002538"
    LLC_PK_1_GR101_CELL = "BTO_0002538"

    # culture condition:styrene-grown cell
    BTO_0002539 = "BTO_0002539"
    CULTURE_CONDITION_STYRENE_GROWN_CELL = "BTO_0002539"

    # culture condition:styrene oxide-grown cell
    BTO_0002540 = "BTO_0002540"
    CULTURE_CONDITION_STYRENE_OXIDE_GROWN_CELL = "BTO_0002540"

    # culture condition:(R)-cysteate-grown cell
    BTO_0002541 = "BTO_0002541"
    CULTURE_CONDITION__R__CYSTEATE_GROWN_CELL = "BTO_0002541"

    # femoral muscle
    BTO_0002542 = "BTO_0002542"
    FEMORAL_MUSCLE = "BTO_0002542"

    # alveolar wall
    BTO_0002543 = "BTO_0002543"
    ALVEOLAR_WALL = "BTO_0002543"

    # MCF-12A cell
    BTO_0002544 = "BTO_0002544"
    MCF_12A_CELL = "BTO_0002544"

    # MCF-12F cell
    BTO_0002545 = "BTO_0002545"
    MCF_12F_CELL = "BTO_0002545"

    # KBM-5 cell
    BTO_0002546 = "BTO_0002546"
    KBM_5_CELL = "BTO_0002546"

    # KE-37 cell
    BTO_0002547 = "BTO_0002547"
    KE_37_CELL = "BTO_0002547"

    # BT-549 cell
    BTO_0002548 = "BTO_0002548"
    BT_549_CELL = "BTO_0002548"

    # A-2780 cell
    BTO_0002549 = "BTO_0002549"
    A_2780_CELL = "BTO_0002549"

    # CH-1 cell
    BTO_0002550 = "BTO_0002550"
    CH_1_CELL = "BTO_0002550"

    # ACH-2 cell
    BTO_0002551 = "BTO_0002551"
    ACH_2_CELL = "BTO_0002551"

    # NCI-H1299 cell
    BTO_0002552 = "BTO_0002552"
    NCI_H1299_CELL = "BTO_0002552"

    # non-small cell lung cancer cell line
    BTO_0002553 = "BTO_0002553"
    NON_SMALL_CELL_LUNG_CANCER_CELL_LINE = "BTO_0002553"

    # K-562adr cell
    BTO_0002554 = "BTO_0002554"
    K_562ADR_CELL = "BTO_0002554"

    # HOSE cell
    BTO_0002555 = "BTO_0002555"
    HOSE_CELL = "BTO_0002555"

    # HOSE-A cell
    BTO_0002556 = "BTO_0002556"
    HOSE_A_CELL = "BTO_0002556"

    # HOSE-B cell
    BTO_0002557 = "BTO_0002557"
    HOSE_B_CELL = "BTO_0002557"

    # INER-37 cell
    BTO_0002558 = "BTO_0002558"
    INER_37_CELL = "BTO_0002558"

    # INER-51 cell
    BTO_0002559 = "BTO_0002559"
    INER_51_CELL = "BTO_0002559"

    # OVCA-2 cell
    BTO_0002560 = "BTO_0002560"
    OVCA_2_CELL = "BTO_0002560"

    # OVCA-4 cell
    BTO_0002561 = "BTO_0002561"
    OVCA_4_CELL = "BTO_0002561"

    # A-1847 cell
    BTO_0002562 = "BTO_0002562"
    A_1847_CELL = "BTO_0002562"

    # OVCA-420 cell
    BTO_0002563 = "BTO_0002563"
    OVCA_420_CELL = "BTO_0002563"

    # OVCA-429 cell
    BTO_0002564 = "BTO_0002564"
    OVCA_429_CELL = "BTO_0002564"

    # OVCA-432 cell
    BTO_0002565 = "BTO_0002565"
    OVCA_432_CELL = "BTO_0002565"

    # OVCA-433 cell
    BTO_0002566 = "BTO_0002566"
    OVCA_433_CELL = "BTO_0002566"

    # INER-51/PSC-1 cell
    BTO_0002567 = "BTO_0002567"
    INER_51_PSC_1_CELL = "BTO_0002567"

    # Colo-201 cell
    BTO_0002568 = "BTO_0002568"
    COLO_201_CELL = "BTO_0002568"

    # Co-403 cell
    BTO_0002569 = "BTO_0002569"
    CO_403_CELL = "BTO_0002569"

    # coronary artery smooth muscle cell line
    BTO_0002570 = "BTO_0002570"
    CORONARY_ARTERY_SMOOTH_MUSCLE_CELL_LINE = "BTO_0002570"

    # Caco-2/TC7 cell
    BTO_0002571 = "BTO_0002571"
    CACO_2_TC7_CELL = "BTO_0002571"

    # MEF cell
    BTO_0002572 = "BTO_0002572"
    MEF_CELL = "BTO_0002572"

    # TERA-2 cell
    BTO_0002573 = "BTO_0002573"
    TERA_2_CELL = "BTO_0002573"

    # NT2-N cell
    BTO_0002574 = "BTO_0002574"
    NT2_N_CELL = "BTO_0002574"

    # IGROV-1 cell
    BTO_0002575 = "BTO_0002575"
    IGROV_1_CELL = "BTO_0002575"

    # UMR-106 cell
    BTO_0002576 = "BTO_0002576"
    UMR_106_CELL = "BTO_0002576"

    # UMR-108 cell
    BTO_0002577 = "BTO_0002577"
    UMR_108_CELL = "BTO_0002577"

    # feather barbs
    BTO_0002578 = "BTO_0002578"
    FEATHER_BARBS = "BTO_0002578"

    # IEC-CF7 cell
    BTO_0002579 = "BTO_0002579"
    IEC_CF7_CELL = "BTO_0002579"

    # chronic myeloid leukemia cell line
    BTO_0002580 = "BTO_0002580"
    CHRONIC_MYELOID_LEUKEMIA_CELL_LINE = "BTO_0002580"

    # MEG-01 cell
    BTO_0002581 = "BTO_0002581"
    MEG_01_CELL = "BTO_0002581"

    # HFL-1 cell
    BTO_0002582 = "BTO_0002582"
    HFL_1_CELL = "BTO_0002582"

    # YMB-1-E cell
    BTO_0002583 = "BTO_0002583"
    YMB_1_E_CELL = "BTO_0002583"

    # WRL-68 cell
    BTO_0002584 = "BTO_0002584"
    WRL_68_CELL = "BTO_0002584"

    # WE-480 cell
    BTO_0002585 = "BTO_0002585"
    WE_480_CELL = "BTO_0002585"

    # G-401 cell
    BTO_0002586 = "BTO_0002586"
    G_401_CELL = "BTO_0002586"

    # NCI-H295 cell
    BTO_0002587 = "BTO_0002587"
    NCI_H295_CELL = "BTO_0002587"

    # NCI-H295R cell
    BTO_0002588 = "BTO_0002588"
    NCI_H295R_CELL = "BTO_0002588"

    # H-7721 cell
    BTO_0002589 = "BTO_0002589"
    H_7721_CELL = "BTO_0002589"

    # HEY cell
    BTO_0002590 = "BTO_0002590"
    HEY_CELL = "BTO_0002590"

    # HL-60/Vinc cell
    BTO_0002591 = "BTO_0002591"
    HL_60_VINC_CELL = "BTO_0002591"

    # DC-3F/S16 cell
    BTO_0002592 = "BTO_0002592"
    DC_3F_S16_CELL = "BTO_0002592"

    # DC-3F/9-OH-E cell
    BTO_0002593 = "BTO_0002593"
    DC_3F_9_OH_E_CELL = "BTO_0002593"

    # DDT1-MF-2 cell
    BTO_0002594 = "BTO_0002594"
    DDT1_MF_2_CELL = "BTO_0002594"

    # leiomyosarcoma cell line
    BTO_0002595 = "BTO_0002595"
    LEIOMYOSARCOMA_CELL_LINE = "BTO_0002595"

    # NUGC-2 cell
    BTO_0002596 = "BTO_0002596"
    NUGC_2_CELL = "BTO_0002596"

    # NUGC-3 cell
    BTO_0002597 = "BTO_0002597"
    NUGC_3_CELL = "BTO_0002597"

    # RBA cell
    BTO_0002598 = "BTO_0002598"
    RBA_CELL = "BTO_0002598"

    # RBA-2 cell
    BTO_0002599 = "BTO_0002599"
    RBA_2_CELL = "BTO_0002599"

    # astrocyte cell line
    BTO_0002600 = "BTO_0002600"
    ASTROCYTE_CELL_LINE = "BTO_0002600"

    # RAW/LR5 cell
    BTO_0002601 = "BTO_0002601"
    RAW_LR5_CELL = "BTO_0002601"

    # RTH-149 cell
    BTO_0002602 = "BTO_0002602"
    RTH_149_CELL = "BTO_0002602"

    # 11-9-1-4 cell
    BTO_0002603 = "BTO_0002603"
    _11_9_1_4_CELL = "BTO_0002603"

    # TC-71 cell
    BTO_0002604 = "BTO_0002604"
    TC_71_CELL = "BTO_0002604"

    # TE-671 cell
    BTO_0002605 = "BTO_0002605"
    TE_671_CELL = "BTO_0002605"

    # glial cell
    BTO_0002606 = "BTO_0002606"
    GLIAL_CELL = "BTO_0002606"

    # SK-LMS-1 cell
    BTO_0002607 = "BTO_0002607"
    SK_LMS_1_CELL = "BTO_0002607"

    # vomeronasal organ
    BTO_0002608 = "BTO_0002608"
    VOMERONASAL_ORGAN = "BTO_0002608"

    # astroglial cell
    BTO_0002609 = "BTO_0002609"
    ASTROGLIAL_CELL = "BTO_0002609"

    # pseudopodium
    BTO_0002610 = "BTO_0002610"
    PSEUDOPODIUM = "BTO_0002610"

    # axopodium
    BTO_0002611 = "BTO_0002611"
    AXOPODIUM = "BTO_0002611"

    # filopodium
    BTO_0002612 = "BTO_0002612"
    FILOPODIUM = "BTO_0002612"

    # lobopodium
    BTO_0002613 = "BTO_0002613"
    LOBOPODIUM = "BTO_0002613"

    # reticulopodium
    BTO_0002614 = "BTO_0002614"
    RETICULOPODIUM = "BTO_0002614"

    # fascia dentata
    BTO_0002615 = "BTO_0002615"
    FASCIA_DENTATA = "BTO_0002615"

    # turion
    BTO_0002616 = "BTO_0002616"
    TURION = "BTO_0002616"

    # thyroid nodule
    BTO_0002617 = "BTO_0002617"
    THYROID_NODULE = "BTO_0002617"

    # ejaculatory duct epithelium
    BTO_0002618 = "BTO_0002618"
    EJACULATORY_DUCT_EPITHELIUM = "BTO_0002618"

    # posterior adductor muscle
    BTO_0002619 = "BTO_0002619"
    POSTERIOR_ADDUCTOR_MUSCLE = "BTO_0002619"

    # anterior adductor muscle
    BTO_0002620 = "BTO_0002620"
    ANTERIOR_ADDUCTOR_MUSCLE = "BTO_0002620"

    # spinal muscle
    BTO_0002621 = "BTO_0002621"
    SPINAL_MUSCLE = "BTO_0002621"

    # spinal muscle of head
    BTO_0002622 = "BTO_0002622"
    SPINAL_MUSCLE_OF_HEAD = "BTO_0002622"

    # spinal muscle of neck
    BTO_0002623 = "BTO_0002623"
    SPINAL_MUSCLE_OF_NECK = "BTO_0002623"

    # spinal muscle of thorax
    BTO_0002624 = "BTO_0002624"
    SPINAL_MUSCLE_OF_THORAX = "BTO_0002624"

    # mesenchymal cell
    BTO_0002625 = "BTO_0002625"
    MESENCHYMAL_CELL = "BTO_0002625"

    # venule
    BTO_0002626 = "BTO_0002626"
    VENULE = "BTO_0002626"

    # T-lymphoblastoma cell
    BTO_0002627 = "BTO_0002627"
    T_LYMPHOBLASTOMA_CELL = "BTO_0002627"

    # B-lymphoblastoma cell
    BTO_0002628 = "BTO_0002628"
    B_LYMPHOBLASTOMA_CELL = "BTO_0002628"

    # T-lymphoblastoid cell line
    BTO_0002629 = "BTO_0002629"
    T_LYMPHOBLASTOID_CELL_LINE = "BTO_0002629"

    # UCI-101 cell
    BTO_0002630 = "BTO_0002630"
    UCI_101_CELL = "BTO_0002630"

    # glume
    BTO_0002631 = "BTO_0002631"
    GLUME = "BTO_0002631"

    # larval cell line
    BTO_0002632 = "BTO_0002632"
    LARVAL_CELL_LINE = "BTO_0002632"

    # 4a-2s4 cell
    BTO_0002633 = "BTO_0002633"
    _4A_2S4_CELL = "BTO_0002633"

    # L3-5-3 cell
    BTO_0002634 = "BTO_0002634"
    L3_5_3_CELL = "BTO_0002634"

    # Sua1.1 cell
    BTO_0002635 = "BTO_0002635"
    SUA1_1_CELL = "BTO_0002635"

    # 1HAEo cell
    BTO_0002636 = "BTO_0002636"
    _1HAEO_CELL = "BTO_0002636"

    # respiratory epithelium cell line
    BTO_0002637 = "BTO_0002637"
    RESPIRATORY_EPITHELIUM_CELL_LINE = "BTO_0002637"

    # Hs 925.T cell
    BTO_0002638 = "BTO_0002638"
    HS_925_T_CELL = "BTO_0002638"

    # NS20Y cell
    BTO_0002639 = "BTO_0002639"
    NS20Y_CELL = "BTO_0002639"

    # CHO-EM9 cell
    BTO_0002640 = "BTO_0002640"
    CHO_EM9_CELL = "BTO_0002640"

    # CHO-AA8 cell
    BTO_0002641 = "BTO_0002641"
    CHO_AA8_CELL = "BTO_0002641"

    # A2780/DX3 cell
    BTO_0002642 = "BTO_0002642"
    A2780_DX3_CELL = "BTO_0002642"

    # cortical collecting duct
    BTO_0002643 = "BTO_0002643"
    CORTICAL_COLLECTING_DUCT = "BTO_0002643"

    # CCD-13Lu cell
    BTO_0002644 = "BTO_0002644"
    CCD_13LU_CELL = "BTO_0002644"

    # CCD-8Lu cell
    BTO_0002645 = "BTO_0002645"
    CCD_8LU_CELL = "BTO_0002645"

    # CCD-25Lu cell
    BTO_0002646 = "BTO_0002646"
    CCD_25LU_CELL = "BTO_0002646"

    # CCD-27Sk cell
    BTO_0002647 = "BTO_0002647"
    CCD_27SK_CELL = "BTO_0002647"

    # ROS-17/2.8 cell
    BTO_0002648 = "BTO_0002648"
    ROS_17_2_8_CELL = "BTO_0002648"

    # B35 cell
    BTO_0002649 = "BTO_0002649"
    B35_CELL = "BTO_0002649"

    # entorhinal area
    BTO_0002650 = "BTO_0002650"
    ENTORHINAL_AREA = "BTO_0002650"

    # piriform area
    BTO_0002651 = "BTO_0002651"
    PIRIFORM_AREA = "BTO_0002651"

    # hemangioendothelioma cell line
    BTO_0002652 = "BTO_0002652"
    HEMANGIOENDOTHELIOMA_CELL_LINE = "BTO_0002652"

    # N2aEGFP cell
    BTO_0002653 = "BTO_0002653"
    N2AEGFP_CELL = "BTO_0002653"

    # hippocampal mossy fiber
    BTO_0002654 = "BTO_0002654"
    HIPPOCAMPAL_MOSSY_FIBER = "BTO_0002654"

    # postlarva
    BTO_0002655 = "BTO_0002655"
    POSTLARVA = "BTO_0002655"

    # sickle cell
    BTO_0002656 = "BTO_0002656"
    SICKLE_CELL = "BTO_0002656"

    # mpkCCDc14 cell
    BTO_0002657 = "BTO_0002657"
    MPKCCDC14_CELL = "BTO_0002657"

    # collecting duct cell line
    BTO_0002658 = "BTO_0002658"
    COLLECTING_DUCT_CELL_LINE = "BTO_0002658"

    # embryonic brain cortex cell line
    BTO_0002659 = "BTO_0002659"
    EMBRYONIC_BRAIN_CORTEX_CELL_LINE = "BTO_0002659"

    # inflorescence stalk
    BTO_0002660 = "BTO_0002660"
    INFLORESCENCE_STALK = "BTO_0002660"

    # auditory vesicle
    BTO_0002661 = "BTO_0002661"
    AUDITORY_VESICLE = "BTO_0002661"

    # skeletal muscle cell line
    BTO_0002662 = "BTO_0002662"
    SKELETAL_MUSCLE_CELL_LINE = "BTO_0002662"

    # N2aSW cell
    BTO_0002663 = "BTO_0002663"
    N2ASW_CELL = "BTO_0002663"

    # HTAU cell
    BTO_0002664 = "BTO_0002664"
    HTAU_CELL = "BTO_0002664"

    # B-50 cell
    BTO_0002665 = "BTO_0002665"
    B_50_CELL = "BTO_0002665"

    # adult stem cell
    BTO_0002666 = "BTO_0002666"
    ADULT_STEM_CELL = "BTO_0002666"

    # cord blood stem cell
    BTO_0002667 = "BTO_0002667"
    CORD_BLOOD_STEM_CELL = "BTO_0002667"

    # bone marrow stromal stem cell
    BTO_0002668 = "BTO_0002668"
    BONE_MARROW_STROMAL_STEM_CELL = "BTO_0002668"

    # peripheral blood stem cell
    BTO_0002669 = "BTO_0002669"
    PERIPHERAL_BLOOD_STEM_CELL = "BTO_0002669"

    # medial geniculate nucleus
    BTO_0002670 = "BTO_0002670"
    MEDIAL_GENICULATE_NUCLEUS = "BTO_0002670"

    # ventral principal nucleus of medial geniculate body
    BTO_0002671 = "BTO_0002671"
    VENTRAL_PRINCIPAL_NUCLEUS_OF_MEDIAL_GENICULATE_BODY = "BTO_0002671"

    # medial nucleus of medial geniculate body
    BTO_0002672 = "BTO_0002672"
    MEDIAL_NUCLEUS_OF_MEDIAL_GENICULATE_BODY = "BTO_0002672"

    # dorsal nucleus of medial geniculate body
    BTO_0002673 = "BTO_0002673"
    DORSAL_NUCLEUS_OF_MEDIAL_GENICULATE_BODY = "BTO_0002673"

    # medial geniculate body
    BTO_0002674 = "BTO_0002674"
    MEDIAL_GENICULATE_BODY = "BTO_0002674"

    # mushroom body
    BTO_0002675 = "BTO_0002675"
    MUSHROOM_BODY = "BTO_0002675"

    # vertical lobe of mushroom body
    BTO_0002676 = "BTO_0002676"
    VERTICAL_LOBE_OF_MUSHROOM_BODY = "BTO_0002676"

    # medial lobe of mushroom body
    BTO_0002677 = "BTO_0002677"
    MEDIAL_LOBE_OF_MUSHROOM_BODY = "BTO_0002677"

    # testicular vein
    BTO_0002678 = "BTO_0002678"
    TESTICULAR_VEIN = "BTO_0002678"

    # right testicular vein
    BTO_0002679 = "BTO_0002679"
    RIGHT_TESTICULAR_VEIN = "BTO_0002679"

    # left testicular vein
    BTO_0002680 = "BTO_0002680"
    LEFT_TESTICULAR_VEIN = "BTO_0002680"

    # renal vein
    BTO_0002681 = "BTO_0002681"
    RENAL_VEIN = "BTO_0002681"

    # inferior vena cava
    BTO_0002682 = "BTO_0002682"
    INFERIOR_VENA_CAVA = "BTO_0002682"

    # superior vena cava
    BTO_0002683 = "BTO_0002683"
    SUPERIOR_VENA_CAVA = "BTO_0002683"

    # lymphoid follicle
    BTO_0002684 = "BTO_0002684"
    LYMPHOID_FOLLICLE = "BTO_0002684"

    # EOMA cell
    BTO_0002685 = "BTO_0002685"
    EOMA_CELL = "BTO_0002685"

    # central amygdaloid nucleus
    BTO_0002686 = "BTO_0002686"
    CENTRAL_AMYGDALOID_NUCLEUS = "BTO_0002686"

    # Leydig cell tumor cell
    BTO_0002687 = "BTO_0002687"
    LEYDIG_CELL_TUMOR_CELL = "BTO_0002687"

    # vascular cell
    BTO_0002688 = "BTO_0002688"
    VASCULAR_CELL = "BTO_0002688"

    # oviductal fluid
    BTO_0002689 = "BTO_0002689"
    OVIDUCTAL_FLUID = "BTO_0002689"

    # biofilm
    BTO_0002690 = "BTO_0002690"
    BIOFILM = "BTO_0002690"

    # neuroendocrine cell
    BTO_0002691 = "BTO_0002691"
    NEUROENDOCRINE_CELL = "BTO_0002691"

    # enterochromaffin-like cell
    BTO_0002692 = "BTO_0002692"
    ENTEROCHROMAFFIN_LIKE_CELL = "BTO_0002692"

    # culture condition:toluene-grown cell
    BTO_0002693 = "BTO_0002693"
    CULTURE_CONDITION_TOLUENE_GROWN_CELL = "BTO_0002693"

    # leiomyoma cell
    BTO_0002694 = "BTO_0002694"
    LEIOMYOMA_CELL = "BTO_0002694"

    # uterine leiomyoma cell
    BTO_0002695 = "BTO_0002695"
    UTERINE_LEIOMYOMA_CELL = "BTO_0002695"

    # SK-N-BE(2) cell
    BTO_0002696 = "BTO_0002696"
    SK_N_BE_2__CELL = "BTO_0002696"

    # supraoptic nucleus
    BTO_0002697 = "BTO_0002697"
    SUPRAOPTIC_NUCLEUS = "BTO_0002697"

    # bed nucleus of stria terminalis
    BTO_0002698 = "BTO_0002698"
    BED_NUCLEUS_OF_STRIA_TERMINALIS = "BTO_0002698"

    # lateral habenular nucleus
    BTO_0002699 = "BTO_0002699"
    LATERAL_HABENULAR_NUCLEUS = "BTO_0002699"

    # habenular trigone
    BTO_0002700 = "BTO_0002700"
    HABENULAR_TRIGONE = "BTO_0002700"

    # midbrain central gray
    BTO_0002701 = "BTO_0002701"
    MIDBRAIN_CENTRAL_GRAY = "BTO_0002701"

    # medial amygdaloid nucleus
    BTO_0002702 = "BTO_0002702"
    MEDIAL_AMYGDALOID_NUCLEUS = "BTO_0002702"

    # cortical amygdaloid nucleus
    BTO_0002703 = "BTO_0002703"
    CORTICAL_AMYGDALOID_NUCLEUS = "BTO_0002703"

    # lateral amygdaloid nucleus
    BTO_0002704 = "BTO_0002704"
    LATERAL_AMYGDALOID_NUCLEUS = "BTO_0002704"

    # septal area
    BTO_0002705 = "BTO_0002705"
    SEPTAL_AREA = "BTO_0002705"

    # ventral septal area
    BTO_0002706 = "BTO_0002706"
    VENTRAL_SEPTAL_AREA = "BTO_0002706"

    # culture condition:ornithine-grown cell
    BTO_0002707 = "BTO_0002707"
    CULTURE_CONDITION_ORNITHINE_GROWN_CELL = "BTO_0002707"

    # GT1-7 cell
    BTO_0002708 = "BTO_0002708"
    GT1_7_CELL = "BTO_0002708"

    # head and neck squamous cell carcinoma cell line
    BTO_0002709 = "BTO_0002709"
    HEAD_AND_NECK_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0002709"

    # UM-SCC-14B cell
    BTO_0002710 = "BTO_0002710"
    UM_SCC_14B_CELL = "BTO_0002710"

    # UM-SCC-17B cell
    BTO_0002711 = "BTO_0002711"
    UM_SCC_17B_CELL = "BTO_0002711"

    # UM-SCC-22B cell
    BTO_0002712 = "BTO_0002712"
    UM_SCC_22B_CELL = "BTO_0002712"

    # UM-SCC-21A cell
    BTO_0002713 = "BTO_0002713"
    UM_SCC_21A_CELL = "BTO_0002713"

    # UM-SCC-22A cell
    BTO_0002714 = "BTO_0002714"
    UM_SCC_22A_CELL = "BTO_0002714"

    # UM-SCC-38 cell
    BTO_0002715 = "BTO_0002715"
    UM_SCC_38_CELL = "BTO_0002715"

    # MDA-1186 cell
    BTO_0002716 = "BTO_0002716"
    MDA_1186_CELL = "BTO_0002716"

    # MDA-886 cell
    BTO_0002717 = "BTO_0002717"
    MDA_886_CELL = "BTO_0002717"

    # TR-146 cell
    BTO_0002718 = "BTO_0002718"
    TR_146_CELL = "BTO_0002718"

    # primary effusion lymphoma cell line
    BTO_0002719 = "BTO_0002719"
    PRIMARY_EFFUSION_LYMPHOMA_CELL_LINE = "BTO_0002719"

    # BC-1 cell
    BTO_0002720 = "BTO_0002720"
    BC_1_CELL = "BTO_0002720"

    # BC-2 cell
    BTO_0002721 = "BTO_0002721"
    BC_2_CELL = "BTO_0002721"

    # BC-3 cell
    BTO_0002722 = "BTO_0002722"
    BC_3_CELL = "BTO_0002722"

    # HBL-6 cell
    BTO_0002723 = "BTO_0002723"
    HBL_6_CELL = "BTO_0002723"

    # CRO-AP/2 cell
    BTO_0002724 = "BTO_0002724"
    CRO_AP_2_CELL = "BTO_0002724"

    # CRO-AP/3 cell
    BTO_0002725 = "BTO_0002725"
    CRO_AP_3_CELL = "BTO_0002725"

    # CRO-AP/5 cell
    BTO_0002726 = "BTO_0002726"
    CRO_AP_5_CELL = "BTO_0002726"

    # BCBL-1 cell
    BTO_0002727 = "BTO_0002727"
    BCBL_1_CELL = "BTO_0002727"

    # BCP-1 cell
    BTO_0002728 = "BTO_0002728"
    BCP_1_CELL = "BTO_0002728"

    # ovarian serous carcinoma cell
    BTO_0002729 = "BTO_0002729"
    OVARIAN_SEROUS_CARCINOMA_CELL = "BTO_0002729"

    # uterine serous carcinoma cell
    BTO_0002730 = "BTO_0002730"
    UTERINE_SEROUS_CARCINOMA_CELL = "BTO_0002730"

    # erythroid cell
    BTO_0002731 = "BTO_0002731"
    ERYTHROID_CELL = "BTO_0002731"

    # HEK-293CymR cell
    BTO_0002732 = "BTO_0002732"
    HEK_293CYMR_CELL = "BTO_0002732"

    # embryonic kidney cell line
    BTO_0002733 = "BTO_0002733"
    EMBRYONIC_KIDNEY_CELL_LINE = "BTO_0002733"

    # 16-HBE14o cell
    BTO_0002734 = "BTO_0002734"
    _16_HBE14O_CELL = "BTO_0002734"

    # MKT-BR cell
    BTO_0002735 = "BTO_0002735"
    MKT_BR_CELL = "BTO_0002735"

    # OCM-1 cell
    BTO_0002736 = "BTO_0002736"
    OCM_1_CELL = "BTO_0002736"

    # SP-6.5 cell
    BTO_0002737 = "BTO_0002737"
    SP_6_5_CELL = "BTO_0002737"

    # cement gland
    BTO_0002738 = "BTO_0002738"
    CEMENT_GLAND = "BTO_0002738"

    # VACO cell
    BTO_0002739 = "BTO_0002739"
    VACO_CELL = "BTO_0002739"

    # INR1G9 cell
    BTO_0002740 = "BTO_0002740"
    INR1G9_CELL = "BTO_0002740"

    # hepatic stellate cell
    BTO_0002741 = "BTO_0002741"
    HEPATIC_STELLATE_CELL = "BTO_0002741"

    # gynecophoral canal
    BTO_0002742 = "BTO_0002742"
    GYNECOPHORAL_CANAL = "BTO_0002742"

    # schistosomulum
    BTO_0002743 = "BTO_0002743"
    SCHISTOSOMULUM = "BTO_0002743"

    # CAPAN-1 cell
    BTO_0002744 = "BTO_0002744"
    CAPAN_1_CELL = "BTO_0002744"

    # CAPAN-2 cell
    BTO_0002745 = "BTO_0002745"
    CAPAN_2_CELL = "BTO_0002745"

    # PC-1.0 cell
    BTO_0002746 = "BTO_0002746"
    PC_1_0_CELL = "BTO_0002746"

    # PC-1 cell
    BTO_0002747 = "BTO_0002747"
    PC_1_CELL = "BTO_0002747"

    # BL-2 cell
    BTO_0002748 = "BTO_0002748"
    BL_2_CELL = "BTO_0002748"

    # HS-74 cell
    BTO_0002749 = "BTO_0002749"
    HS_74_CELL = "BTO_0002749"

    # Calu-3 cell
    BTO_0002750 = "BTO_0002750"
    CALU_3_CELL = "BTO_0002750"

    # PC6-3 cell
    BTO_0002751 = "BTO_0002751"
    PC6_3_CELL = "BTO_0002751"

    # PC-6 cell
    BTO_0002752 = "BTO_0002752"
    PC_6_CELL = "BTO_0002752"

    # PC6-1 cell
    BTO_0002753 = "BTO_0002753"
    PC6_1_CELL = "BTO_0002753"

    # PC6-2 cell
    BTO_0002754 = "BTO_0002754"
    PC6_2_CELL = "BTO_0002754"

    # PC6-16 cell
    BTO_0002755 = "BTO_0002755"
    PC6_16_CELL = "BTO_0002755"

    # PC6-4 cell
    BTO_0002756 = "BTO_0002756"
    PC6_4_CELL = "BTO_0002756"

    # PC6-5 cell
    BTO_0002757 = "BTO_0002757"
    PC6_5_CELL = "BTO_0002757"

    # PC6-6 cell
    BTO_0002758 = "BTO_0002758"
    PC6_6_CELL = "BTO_0002758"

    # PC6-7 cell
    BTO_0002759 = "BTO_0002759"
    PC6_7_CELL = "BTO_0002759"

    # PC6-8 cell
    BTO_0002760 = "BTO_0002760"
    PC6_8_CELL = "BTO_0002760"

    # PC6-9 cell
    BTO_0002761 = "BTO_0002761"
    PC6_9_CELL = "BTO_0002761"

    # PC6-10 cell
    BTO_0002762 = "BTO_0002762"
    PC6_10_CELL = "BTO_0002762"

    # PC6-11 cell
    BTO_0002763 = "BTO_0002763"
    PC6_11_CELL = "BTO_0002763"

    # PC6-13 cell
    BTO_0002764 = "BTO_0002764"
    PC6_13_CELL = "BTO_0002764"

    # PC6-14 cell
    BTO_0002765 = "BTO_0002765"
    PC6_14_CELL = "BTO_0002765"

    # PC6-15 cell
    BTO_0002766 = "BTO_0002766"
    PC6_15_CELL = "BTO_0002766"

    # GH4-C1 cell
    BTO_0002767 = "BTO_0002767"
    GH4_C1_CELL = "BTO_0002767"

    # mammary epithelial cell line
    BTO_0002768 = "BTO_0002768"
    MAMMARY_EPITHELIAL_CELL_LINE = "BTO_0002768"

    # HME cell
    BTO_0002769 = "BTO_0002769"
    HME_CELL = "BTO_0002769"

    # decidual cell
    BTO_0002770 = "BTO_0002770"
    DECIDUAL_CELL = "BTO_0002770"

    # olfactory ensheathing cell
    BTO_0002771 = "BTO_0002771"
    OLFACTORY_ENSHEATHING_CELL = "BTO_0002771"

    # chela
    BTO_0002772 = "BTO_0002772"
    CHELA = "BTO_0002772"

    # salivary gland cancer cell
    BTO_0002773 = "BTO_0002773"
    SALIVARY_GLAND_CANCER_CELL = "BTO_0002773"

    # amyloid plaque
    BTO_0002774 = "BTO_0002774"
    AMYLOID_PLAQUE = "BTO_0002774"

    # ANA-1 cell
    BTO_0002775 = "BTO_0002775"
    ANA_1_CELL = "BTO_0002775"

    # inflorescence apex
    BTO_0002776 = "BTO_0002776"
    INFLORESCENCE_APEX = "BTO_0002776"

    # anterolateral sulcus of medulla oblongata
    BTO_0002777 = "BTO_0002777"
    ANTEROLATERAL_SULCUS_OF_MEDULLA_OBLONGATA = "BTO_0002777"

    # rostral ventrolateral medulla
    BTO_0002778 = "BTO_0002778"
    ROSTRAL_VENTROLATERAL_MEDULLA = "BTO_0002778"

    # endospore
    BTO_0002779 = "BTO_0002779"
    ENDOSPORE = "BTO_0002779"

    # visceral muscle
    BTO_0002780 = "BTO_0002780"
    VISCERAL_MUSCLE = "BTO_0002780"

    # mesenteric vein
    BTO_0002781 = "BTO_0002781"
    MESENTERIC_VEIN = "BTO_0002781"

    # inferior mesenteric vein
    BTO_0002782 = "BTO_0002782"
    INFERIOR_MESENTERIC_VEIN = "BTO_0002782"

    # superior mesenteric vein
    BTO_0002783 = "BTO_0002783"
    SUPERIOR_MESENTERIC_VEIN = "BTO_0002783"

    # corpus albicans
    BTO_0002784 = "BTO_0002784"
    CORPUS_ALBICANS = "BTO_0002784"

    # rhinencephalon
    BTO_0002785 = "BTO_0002785"
    RHINENCEPHALON = "BTO_0002785"

    # cystadenoma cell
    BTO_0002786 = "BTO_0002786"
    CYSTADENOMA_CELL = "BTO_0002786"

    # clear cell adenocarcinoma cell
    BTO_0002787 = "BTO_0002787"
    CLEAR_CELL_ADENOCARCINOMA_CELL = "BTO_0002787"

    # mucinous adenocarcinoma cell
    BTO_0002788 = "BTO_0002788"
    MUCINOUS_ADENOCARCINOMA_CELL = "BTO_0002788"

    # ovarian low malignant potential tumor cell
    BTO_0002789 = "BTO_0002789"
    OVARIAN_LOW_MALIGNANT_POTENTIAL_TUMOR_CELL = "BTO_0002789"

    # phloem parenchyma cell
    BTO_0002790 = "BTO_0002790"
    PHLOEM_PARENCHYMA_CELL = "BTO_0002790"

    # culture condition:arginine-grown cell
    BTO_0002791 = "BTO_0002791"
    CULTURE_CONDITION_ARGININE_GROWN_CELL = "BTO_0002791"

    # culture condition:citrulline-grown cell
    BTO_0002792 = "BTO_0002792"
    CULTURE_CONDITION_CITRULLINE_GROWN_CELL = "BTO_0002792"

    # culture condition:glucose/ammonium-grown cell
    BTO_0002793 = "BTO_0002793"
    CULTURE_CONDITION_GLUCOSE_AMMONIUM_GROWN_CELL = "BTO_0002793"

    # culture condition:glucose/arginine-grown cell
    BTO_0002794 = "BTO_0002794"
    CULTURE_CONDITION_GLUCOSE_ARGININE_GROWN_CELL = "BTO_0002794"

    # culture condition:glucose-grown cell
    BTO_0002795 = "BTO_0002795"
    CULTURE_CONDITION_GLUCOSE_GROWN_CELL = "BTO_0002795"

    # culture condition:glutamate-grown cell
    BTO_0002796 = "BTO_0002796"
    CULTURE_CONDITION_GLUTAMATE_GROWN_CELL = "BTO_0002796"

    # culture condition:N-3-oxododecanoyl-L-homoserine lactone/ammonium chloride-grown cell
    BTO_0002797 = "BTO_0002797"
    CULTURE_CONDITION_N_3_OXODODECANOYL_L_HOMOSERINE_LACTONE_AMMONIUM_CHLORIDE_GROWN_CELL = (
        "BTO_0002797"
    )

    # culture condition:N-decanoyl-L-homoserine lactone-grown cell
    BTO_0002798 = "BTO_0002798"
    CULTURE_CONDITION_N_DECANOYL_L_HOMOSERINE_LACTONE_GROWN_CELL = "BTO_0002798"

    # culture condition:raffinose-grown cell
    BTO_0002799 = "BTO_0002799"
    CULTURE_CONDITION_RAFFINOSE_GROWN_CELL = "BTO_0002799"

    # culture condition:succinate/ammonium-grown cell
    BTO_0002800 = "BTO_0002800"
    CULTURE_CONDITION_SUCCINATE_AMMONIUM_GROWN_CELL = "BTO_0002800"

    # culture condition:tributyrin-grown cell
    BTO_0002801 = "BTO_0002801"
    CULTURE_CONDITION_TRIBUTYRIN_GROWN_CELL = "BTO_0002801"

    # 1F6 cell
    BTO_0002802 = "BTO_0002802"
    _1F6_CELL = "BTO_0002802"

    # BLM cell
    BTO_0002803 = "BTO_0002803"
    BLM_CELL = "BTO_0002803"

    # Mel57 cell
    BTO_0002804 = "BTO_0002804"
    MEL57_CELL = "BTO_0002804"

    # M14 melanoma cell
    BTO_0002805 = "BTO_0002805"
    M14_MELANOMA_CELL = "BTO_0002805"

    # A-375 cell
    BTO_0002806 = "BTO_0002806"
    A_375_CELL = "BTO_0002806"

    # prefrontal cortex
    BTO_0002807 = "BTO_0002807"
    PREFRONTAL_CORTEX = "BTO_0002807"

    # B16-BL6 cell
    BTO_0002808 = "BTO_0002808"
    B16_BL6_CELL = "BTO_0002808"

    # L-6 myoblast cell
    BTO_0002809 = "BTO_0002809"
    L_6_MYOBLAST_CELL = "BTO_0002809"

    # L8 cell
    BTO_0002810 = "BTO_0002810"
    L8_CELL = "BTO_0002810"

    # flag leaf
    BTO_0002811 = "BTO_0002811"
    FLAG_LEAF = "BTO_0002811"

    # final leaf
    BTO_0002812 = "BTO_0002812"
    FINAL_LEAF = "BTO_0002812"

    # gubernaculum testis
    BTO_0002813 = "BTO_0002813"
    GUBERNACULUM_TESTIS = "BTO_0002813"

    # chorda gubernaculum
    BTO_0002814 = "BTO_0002814"
    CHORDA_GUBERNACULUM = "BTO_0002814"

    # transitional cell carcinoma cell
    BTO_0002815 = "BTO_0002815"
    TRANSITIONAL_CELL_CARCINOMA_CELL = "BTO_0002815"

    # bladder transitional cell carcinoma cell
    BTO_0002816 = "BTO_0002816"
    BLADDER_TRANSITIONAL_CELL_CARCINOMA_CELL = "BTO_0002816"

    # esophageal cancer cell line
    BTO_0002817 = "BTO_0002817"
    ESOPHAGEAL_CANCER_CELL_LINE = "BTO_0002817"

    # HCE-7 cell
    BTO_0002818 = "BTO_0002818"
    HCE_7_CELL = "BTO_0002818"

    # decidua basalis
    BTO_0002819 = "BTO_0002819"
    DECIDUA_BASALIS = "BTO_0002819"

    # oligodendroglioma cell line
    BTO_0002820 = "BTO_0002820"
    OLIGODENDROGLIOMA_CELL_LINE = "BTO_0002820"

    # HOG cell
    BTO_0002821 = "BTO_0002821"
    HOG_CELL = "BTO_0002821"

    # NCI-HUT 125 cell
    BTO_0002822 = "BTO_0002822"
    NCI_HUT_125_CELL = "BTO_0002822"

    # SK-PC-1 cell
    BTO_0002823 = "BTO_0002823"
    SK_PC_1_CELL = "BTO_0002823"

    # SF-188 cell
    BTO_0002824 = "BTO_0002824"
    SF_188_CELL = "BTO_0002824"

    # SW-742 cell
    BTO_0002825 = "BTO_0002825"
    SW_742_CELL = "BTO_0002825"

    # SVEC4-10 cell
    BTO_0002826 = "BTO_0002826"
    SVEC4_10_CELL = "BTO_0002826"

    # SK-N-AS cell
    BTO_0002827 = "BTO_0002827"
    SK_N_AS_CELL = "BTO_0002827"

    # HMEC-1 cell
    BTO_0002828 = "BTO_0002828"
    HMEC_1_CELL = "BTO_0002828"

    # KARPAS-299 cell
    BTO_0002829 = "BTO_0002829"
    KARPAS_299_CELL = "BTO_0002829"

    # DB-1 cell
    BTO_0002830 = "BTO_0002830"
    DB_1_CELL = "BTO_0002830"

    # PC-346C cell
    BTO_0002831 = "BTO_0002831"
    PC_346C_CELL = "BTO_0002831"

    # PEA-13 cell
    BTO_0002832 = "BTO_0002832"
    PEA_13_CELL = "BTO_0002832"

    # NB-1643 cell
    BTO_0002833 = "BTO_0002833"
    NB_1643_CELL = "BTO_0002833"

    # NB-1691 cell
    BTO_0002834 = "BTO_0002834"
    NB_1691_CELL = "BTO_0002834"

    # NCI-H358 cell
    BTO_0002835 = "BTO_0002835"
    NCI_H358_CELL = "BTO_0002835"

    # NCI-H460M cell
    BTO_0002836 = "BTO_0002836"
    NCI_H460M_CELL = "BTO_0002836"

    # PY-41 cell
    BTO_0002837 = "BTO_0002837"
    PY_41_CELL = "BTO_0002837"

    # HT-29/219 cell
    BTO_0002838 = "BTO_0002838"
    HT_29_219_CELL = "BTO_0002838"

    # P12-ICHIKAWA cell
    BTO_0002839 = "BTO_0002839"
    P12_ICHIKAWA_CELL = "BTO_0002839"

    # bile ductule
    BTO_0002840 = "BTO_0002840"
    BILE_DUCTULE = "BTO_0002840"

    # bile canaliculus
    BTO_0002841 = "BTO_0002841"
    BILE_CANALICULUS = "BTO_0002841"

    # cholangioma cell
    BTO_0002842 = "BTO_0002842"
    CHOLANGIOMA_CELL = "BTO_0002842"

    # breast fibroadenoma cell
    BTO_0002843 = "BTO_0002843"
    BREAST_FIBROADENOMA_CELL = "BTO_0002843"

    # breast invasive ductal carcinoma cell
    BTO_0002844 = "BTO_0002844"
    BREAST_INVASIVE_DUCTAL_CARCINOMA_CELL = "BTO_0002844"

    # mammary duct
    BTO_0002845 = "BTO_0002845"
    MAMMARY_DUCT = "BTO_0002845"

    # non-Hodgkin lymphoma cell
    BTO_0002846 = "BTO_0002846"
    NON_HODGKIN_LYMPHOMA_CELL = "BTO_0002846"

    # thecoma cell
    BTO_0002847 = "BTO_0002847"
    THECOMA_CELL = "BTO_0002847"

    # granulosa-theca cell tumor cell
    BTO_0002848 = "BTO_0002848"
    GRANULOSA_THECA_CELL_TUMOR_CELL = "BTO_0002848"

    # luteoma cell
    BTO_0002849 = "BTO_0002849"
    LUTEOMA_CELL = "BTO_0002849"

    # theca cell
    BTO_0002850 = "BTO_0002850"
    THECA_CELL = "BTO_0002850"

    # theca interna
    BTO_0002851 = "BTO_0002851"
    THECA_INTERNA = "BTO_0002851"

    # theca externa
    BTO_0002852 = "BTO_0002852"
    THECA_EXTERNA = "BTO_0002852"

    # theca folliculi
    BTO_0002853 = "BTO_0002853"
    THECA_FOLLICULI = "BTO_0002853"

    # corn silk
    BTO_0002854 = "BTO_0002854"
    CORN_SILK = "BTO_0002854"

    # hepatic cecum
    BTO_0002855 = "BTO_0002855"
    HEPATIC_CECUM = "BTO_0002855"

    # coelomocyte
    BTO_0002856 = "BTO_0002856"
    COELOMOCYTE = "BTO_0002856"

    # eleocyte
    BTO_0002857 = "BTO_0002857"
    ELEOCYTE = "BTO_0002857"

    # cerebral subcortex
    BTO_0002858 = "BTO_0002858"
    CEREBRAL_SUBCORTEX = "BTO_0002858"

    # esophageal mucosa
    BTO_0002859 = "BTO_0002859"
    ESOPHAGEAL_MUCOSA = "BTO_0002859"

    # oral mucosa
    BTO_0002860 = "BTO_0002860"
    ORAL_MUCOSA = "BTO_0002860"

    # esophageal squamous cell carcinoma cell
    BTO_0002861 = "BTO_0002861"
    ESOPHAGEAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0002861"

    # HBEpC cell
    BTO_0002862 = "BTO_0002862"
    HBEPC_CELL = "BTO_0002862"

    # MSS-31 cell
    BTO_0002863 = "BTO_0002863"
    MSS_31_CELL = "BTO_0002863"

    # T3M4 cell
    BTO_0002864 = "BTO_0002864"
    T3M4_CELL = "BTO_0002864"

    # GER cell
    BTO_0002865 = "BTO_0002865"
    GER_CELL = "BTO_0002865"

    # TE-2 cell
    BTO_0002866 = "BTO_0002866"
    TE_2_CELL = "BTO_0002866"

    # TE-6 cell
    BTO_0002867 = "BTO_0002867"
    TE_6_CELL = "BTO_0002867"

    # urinary bladder transitional cell carcinoma cell line
    BTO_0002868 = "BTO_0002868"
    URINARY_BLADDER_TRANSITIONAL_CELL_CARCINOMA_CELL_LINE = "BTO_0002868"

    # transitional cell carcinoma cell line
    BTO_0002869 = "BTO_0002869"
    TRANSITIONAL_CELL_CARCINOMA_CELL_LINE = "BTO_0002869"

    # RT-4 cell
    BTO_0002870 = "BTO_0002870"
    RT_4_CELL = "BTO_0002870"

    # embryonic brain cell line
    BTO_0002871 = "BTO_0002871"
    EMBRYONIC_BRAIN_CELL_LINE = "BTO_0002871"

    # embryonic hippocampal cell line
    BTO_0002872 = "BTO_0002872"
    EMBRYONIC_HIPPOCAMPAL_CELL_LINE = "BTO_0002872"

    # HN9.10e cell
    BTO_0002873 = "BTO_0002873"
    HN9_10E_CELL = "BTO_0002873"

    # Rat-2 cell
    BTO_0002874 = "BTO_0002874"
    RAT_2_CELL = "BTO_0002874"

    # CL1-0 cell
    BTO_0002875 = "BTO_0002875"
    CL1_0_CELL = "BTO_0002875"

    # CL1-5 cell
    BTO_0002876 = "BTO_0002876"
    CL1_5_CELL = "BTO_0002876"

    # PC-14 cell
    BTO_0002877 = "BTO_0002877"
    PC_14_CELL = "BTO_0002877"

    # B-lymphoblastoid cell
    BTO_0002878 = "BTO_0002878"
    B_LYMPHOBLASTOID_CELL = "BTO_0002878"

    # chorionic plate
    BTO_0002879 = "BTO_0002879"
    CHORIONIC_PLATE = "BTO_0002879"

    # ingluvial ganglion
    BTO_0002880 = "BTO_0002880"
    INGLUVIAL_GANGLION = "BTO_0002880"

    # neural stem cell
    BTO_0002881 = "BTO_0002881"
    NEURAL_STEM_CELL = "BTO_0002881"

    # 32D cell
    BTO_0002882 = "BTO_0002882"
    _32D_CELL = "BTO_0002882"

    # 32D clone3 cell
    BTO_0002883 = "BTO_0002883"
    _32D_CLONE3_CELL = "BTO_0002883"

    # 416B cell
    BTO_0002884 = "BTO_0002884"
    _416B_CELL = "BTO_0002884"

    # MEL-745A cell
    BTO_0002885 = "BTO_0002885"
    MEL_745A_CELL = "BTO_0002885"

    # renal epithelium cell line
    BTO_0002886 = "BTO_0002886"
    RENAL_EPITHELIUM_CELL_LINE = "BTO_0002886"

    # A-9 cell
    BTO_0002887 = "BTO_0002887"
    A_9_CELL = "BTO_0002887"

    # Th-1 cell line
    BTO_0002888 = "BTO_0002888"
    TH_1_CELL_LINE = "BTO_0002888"

    # alveolar macrophage cell line
    BTO_0002889 = "BTO_0002889"
    ALVEOLAR_MACROPHAGE_CELL_LINE = "BTO_0002889"

    # CA-77 cell
    BTO_0002890 = "BTO_0002890"
    CA_77_CELL = "BTO_0002890"

    # neural stem cell line
    BTO_0002891 = "BTO_0002891"
    NEURAL_STEM_CELL_LINE = "BTO_0002891"

    # GEO cell
    BTO_0002892 = "BTO_0002892"
    GEO_CELL = "BTO_0002892"

    # HB1.F3 cell
    BTO_0002893 = "BTO_0002893"
    HB1_F3_CELL = "BTO_0002893"

    # Hepa-1c1c7 cell
    BTO_0002894 = "BTO_0002894"
    HEPA_1C1C7_CELL = "BTO_0002894"

    # HEPA 1-6 cell
    BTO_0002895 = "BTO_0002895"
    HEPA_1_6_CELL = "BTO_0002895"

    # HM-1 ES cell
    BTO_0002896 = "BTO_0002896"
    HM_1_ES_CELL = "BTO_0002896"

    # IM-9 cell
    BTO_0002897 = "BTO_0002897"
    IM_9_CELL = "BTO_0002897"

    # J558L cell
    BTO_0002898 = "BTO_0002898"
    J558L_CELL = "BTO_0002898"

    # K-1034 RPE cell
    BTO_0002899 = "BTO_0002899"
    K_1034_RPE_CELL = "BTO_0002899"

    # monocyte-derived dendritic cell
    BTO_0002900 = "BTO_0002900"
    MONOCYTE_DERIVED_DENDRITIC_CELL = "BTO_0002900"

    # neural crest cell line
    BTO_0002901 = "BTO_0002901"
    NEURAL_CREST_CELL_LINE = "BTO_0002901"

    # NC14.9.1 cell
    BTO_0002902 = "BTO_0002902"
    NC14_9_1_CELL = "BTO_0002902"

    # NC14.4.6E cell
    BTO_0002903 = "BTO_0002903"
    NC14_4_6E_CELL = "BTO_0002903"

    # non-Hodgkin lymphoma cell line
    BTO_0002904 = "BTO_0002904"
    NON_HODGKIN_LYMPHOMA_CELL_LINE = "BTO_0002904"

    # NHL-B cell
    BTO_0002905 = "BTO_0002905"
    NHL_B_CELL = "BTO_0002905"

    # NPLC/PRF/5 cell
    BTO_0002906 = "BTO_0002906"
    NPLC_PRF_5_CELL = "BTO_0002906"

    # NR-8383 cell
    BTO_0002907 = "BTO_0002907"
    NR_8383_CELL = "BTO_0002907"

    # PLB-985 cell
    BTO_0002908 = "BTO_0002908"
    PLB_985_CELL = "BTO_0002908"

    # RK-13 cell
    BTO_0002909 = "BTO_0002909"
    RK_13_CELL = "BTO_0002909"

    # S194/5.XXO-1 cell
    BTO_0002910 = "BTO_0002910"
    S194_5_XXO_1_CELL = "BTO_0002910"

    # S194/5.XXO.BU.1 cell
    BTO_0002911 = "BTO_0002911"
    S194_5_XXO_BU_1_CELL = "BTO_0002911"

    # neuroepithelioma cell line
    BTO_0002912 = "BTO_0002912"
    NEUROEPITHELIOMA_CELL_LINE = "BTO_0002912"

    # epithelioma cell line
    BTO_0002913 = "BTO_0002913"
    EPITHELIOMA_CELL_LINE = "BTO_0002913"

    # SK-N-MC cell
    BTO_0002914 = "BTO_0002914"
    SK_N_MC_CELL = "BTO_0002914"

    # rhabdomyocyte
    BTO_0002915 = "BTO_0002915"
    RHABDOMYOCYTE = "BTO_0002915"

    # striated muscle cell
    BTO_0002916 = "BTO_0002916"
    STRIATED_MUSCLE_CELL = "BTO_0002916"

    # rhabdomyocyte cell line
    BTO_0002917 = "BTO_0002917"
    RHABDOMYOCYTE_CELL_LINE = "BTO_0002917"

    # HMV-II cell
    BTO_0002918 = "BTO_0002918"
    HMV_II_CELL = "BTO_0002918"

    # retinoblastoma cell line
    BTO_0002919 = "BTO_0002919"
    RETINOBLASTOMA_CELL_LINE = "BTO_0002919"

    # Y-79 cell
    BTO_0002920 = "BTO_0002920"
    Y_79_CELL = "BTO_0002920"

    # LS174T-HM7 cell
    BTO_0002921 = "BTO_0002921"
    LS174T_HM7_CELL = "BTO_0002921"

    # bronchial epithelial cell
    BTO_0002922 = "BTO_0002922"
    BRONCHIAL_EPITHELIAL_CELL = "BTO_0002922"

    # BEAS-2B cell
    BTO_0002923 = "BTO_0002923"
    BEAS_2B_CELL = "BTO_0002923"

    # NHBE cell
    BTO_0002924 = "BTO_0002924"
    NHBE_CELL = "BTO_0002924"

    # tracheobronchial epithelium
    BTO_0002925 = "BTO_0002925"
    TRACHEOBRONCHIAL_EPITHELIUM = "BTO_0002925"

    # tracheobronchial epithelial cell line
    BTO_0002926 = "BTO_0002926"
    TRACHEOBRONCHIAL_EPITHELIAL_CELL_LINE = "BTO_0002926"

    # tracheobronchial epithelial cell
    BTO_0002927 = "BTO_0002927"
    TRACHEOBRONCHIAL_EPITHELIAL_CELL = "BTO_0002927"

    # adult stem cell line
    BTO_0002928 = "BTO_0002928"
    ADULT_STEM_CELL_LINE = "BTO_0002928"

    # adult liver stem cell line
    BTO_0002929 = "BTO_0002929"
    ADULT_LIVER_STEM_CELL_LINE = "BTO_0002929"

    # fascia
    BTO_0002930 = "BTO_0002930"
    FASCIA = "BTO_0002930"

    # liver epithelial cell line
    BTO_0002931 = "BTO_0002931"
    LIVER_EPITHELIAL_CELL_LINE = "BTO_0002931"

    # cholangiocarcinoma cell line
    BTO_0002932 = "BTO_0002932"
    CHOLANGIOCARCINOMA_CELL_LINE = "BTO_0002932"

    # CCLP-1 cell
    BTO_0002933 = "BTO_0002933"
    CCLP_1_CELL = "BTO_0002933"

    # thymic cortex
    BTO_0002934 = "BTO_0002934"
    THYMIC_CORTEX = "BTO_0002934"

    # SG231 cell
    BTO_0002935 = "BTO_0002935"
    SG231_CELL = "BTO_0002935"

    # vaginal cell line
    BTO_0002936 = "BTO_0002936"
    VAGINAL_CELL_LINE = "BTO_0002936"

    # S-16 cell
    BTO_0002937 = "BTO_0002937"
    S_16_CELL = "BTO_0002937"

    # 33B cell
    BTO_0002938 = "BTO_0002938"
    _33B_CELL = "BTO_0002938"

    # serous adenocarcinoma cell
    BTO_0002939 = "BTO_0002939"
    SEROUS_ADENOCARCINOMA_CELL = "BTO_0002939"

    # Calu-1 cell
    BTO_0002940 = "BTO_0002940"
    CALU_1_CELL = "BTO_0002940"

    # Colo-38 cell
    BTO_0002941 = "BTO_0002941"
    COLO_38_CELL = "BTO_0002941"

    # HO-1 cell
    BTO_0002942 = "BTO_0002942"
    HO_1_CELL = "BTO_0002942"

    # FO-1 cell
    BTO_0002943 = "BTO_0002943"
    FO_1_CELL = "BTO_0002943"

    # DU-2 cell
    BTO_0002944 = "BTO_0002944"
    DU_2_CELL = "BTO_0002944"

    # MRN-1 cell
    BTO_0002945 = "BTO_0002945"
    MRN_1_CELL = "BTO_0002945"

    # MNT-1 cell
    BTO_0002946 = "BTO_0002946"
    MNT_1_CELL = "BTO_0002946"

    # 1102 cell
    BTO_0002947 = "BTO_0002947"
    _1102_CELL = "BTO_0002947"

    # 1383 cell
    BTO_0002948 = "BTO_0002948"
    _1383_CELL = "BTO_0002948"

    # 938 cell
    BTO_0002949 = "BTO_0002949"
    _938_CELL = "BTO_0002949"

    # Mel888 cell
    BTO_0002950 = "BTO_0002950"
    MEL888_CELL = "BTO_0002950"

    # 624 cell
    BTO_0002951 = "BTO_0002951"
    _624_CELL = "BTO_0002951"

    # Mel249 cell
    BTO_0002952 = "BTO_0002952"
    MEL249_CELL = "BTO_0002952"

    # Mel499 cell
    BTO_0002953 = "BTO_0002953"
    MEL499_CELL = "BTO_0002953"

    # Mel505 cell
    BTO_0002954 = "BTO_0002954"
    MEL505_CELL = "BTO_0002954"

    # Mel592 cell
    BTO_0002955 = "BTO_0002955"
    MEL592_CELL = "BTO_0002955"

    # Mel501 cell
    BTO_0002956 = "BTO_0002956"
    MEL501_CELL = "BTO_0002956"

    # DM6 cell
    BTO_0002957 = "BTO_0002957"
    DM6_CELL = "BTO_0002957"

    # DM93 cell
    BTO_0002958 = "BTO_0002958"
    DM93_CELL = "BTO_0002958"

    # TP17 cell
    BTO_0002959 = "BTO_0002959"
    TP17_CELL = "BTO_0002959"

    # HEC-1-A cell
    BTO_0002960 = "BTO_0002960"
    HEC_1_A_CELL = "BTO_0002960"

    # STP-1 cell
    BTO_0002961 = "BTO_0002961"
    STP_1_CELL = "BTO_0002961"

    # 1290-2 cell
    BTO_0002962 = "BTO_0002962"
    _1290_2_CELL = "BTO_0002962"

    # 1704 cell
    BTO_0002963 = "BTO_0002963"
    _1704_CELL = "BTO_0002963"

    # 1182 cell
    BTO_0002964 = "BTO_0002964"
    _1182_CELL = "BTO_0002964"

    # M10 melanoma cell
    BTO_0002965 = "BTO_0002965"
    M10_MELANOMA_CELL = "BTO_0002965"

    # SK-MEL-21 cell
    BTO_0002966 = "BTO_0002966"
    SK_MEL_21_CELL = "BTO_0002966"

    # SK-MEL-37 cell
    BTO_0002967 = "BTO_0002967"
    SK_MEL_37_CELL = "BTO_0002967"

    # SK-MEL-93 cell
    BTO_0002968 = "BTO_0002968"
    SK_MEL_93_CELL = "BTO_0002968"

    # IR-8 cell
    BTO_0002969 = "BTO_0002969"
    IR_8_CELL = "BTO_0002969"

    # H494 cell
    BTO_0002970 = "BTO_0002970"
    H494_CELL = "BTO_0002970"

    # KJ29 cell
    BTO_0002971 = "BTO_0002971"
    KJ29_CELL = "BTO_0002971"

    # 164T2 cell
    BTO_0002972 = "BTO_0002972"
    _164T2_CELL = "BTO_0002972"

    # 267T2 cell
    BTO_0002973 = "BTO_0002973"
    _267T2_CELL = "BTO_0002973"

    # HEK-293-EBNA cell
    BTO_0002974 = "BTO_0002974"
    HEK_293_EBNA_CELL = "BTO_0002974"

    # A-2058 cell
    BTO_0002975 = "BTO_0002975"
    A_2058_CELL = "BTO_0002975"

    # abdominal aorta
    BTO_0002976 = "BTO_0002976"
    ABDOMINAL_AORTA = "BTO_0002976"

    # exocrine glandular secretion
    BTO_0002977 = "BTO_0002977"
    EXOCRINE_GLANDULAR_SECRETION = "BTO_0002977"

    # internal secretion
    BTO_0002978 = "BTO_0002978"
    INTERNAL_SECRETION = "BTO_0002978"

    # secretion
    BTO_0002979 = "BTO_0002979"
    SECRETION = "BTO_0002979"

    # pancreatic alpha cell line
    BTO_0002980 = "BTO_0002980"
    PANCREATIC_ALPHA_CELL_LINE = "BTO_0002980"

    # alpha-TC1.9 cell
    BTO_0002981 = "BTO_0002981"
    ALPHA_TC1_9_CELL = "BTO_0002981"

    # alpha-TC1.6 cell
    BTO_0002982 = "BTO_0002982"
    ALPHA_TC1_6_CELL = "BTO_0002982"

    # anaplastic oligodendroglioma cell
    BTO_0002983 = "BTO_0002983"
    ANAPLASTIC_OLIGODENDROGLIOMA_CELL = "BTO_0002983"

    # antropyloric mucosa
    BTO_0002984 = "BTO_0002984"
    ANTROPYLORIC_MUCOSA = "BTO_0002984"

    # coronary artery smooth muscle
    BTO_0002985 = "BTO_0002985"
    CORONARY_ARTERY_SMOOTH_MUSCLE = "BTO_0002985"

    # culture condition:molybdate-grown cell
    BTO_0002986 = "BTO_0002986"
    CULTURE_CONDITION_MOLYBDATE_GROWN_CELL = "BTO_0002986"

    # culture condition:tungstate-grown cell
    BTO_0002987 = "BTO_0002987"
    CULTURE_CONDITION_TUNGSTATE_GROWN_CELL = "BTO_0002987"

    # CHO-7 cell
    BTO_0002988 = "BTO_0002988"
    CHO_7_CELL = "BTO_0002988"

    # CHP-134 cell
    BTO_0002989 = "BTO_0002989"
    CHP_134_CELL = "BTO_0002989"

    # gastric ulcer
    BTO_0002990 = "BTO_0002990"
    GASTRIC_ULCER = "BTO_0002990"

    # glandular epithelium
    BTO_0002991 = "BTO_0002991"
    GLANDULAR_EPITHELIUM = "BTO_0002991"

    # ARH-77 cell
    BTO_0002992 = "BTO_0002992"
    ARH_77_CELL = "BTO_0002992"

    # beta-TC3 cell
    BTO_0002993 = "BTO_0002993"
    BETA_TC3_CELL = "BTO_0002993"

    # lacteal cyst
    BTO_0002994 = "BTO_0002994"
    LACTEAL_CYST = "BTO_0002994"

    # CCL-39 cell
    BTO_0002995 = "BTO_0002995"
    CCL_39_CELL = "BTO_0002995"

    # cavernous artery
    BTO_0002996 = "BTO_0002996"
    CAVERNOUS_ARTERY = "BTO_0002996"

    # LAPC-4 cell
    BTO_0002997 = "BTO_0002997"
    LAPC_4_CELL = "BTO_0002997"

    # LNCaP-C4-2B4 cell
    BTO_0002998 = "BTO_0002998"
    LNCAP_C4_2B4_CELL = "BTO_0002998"

    # CWR22-Rv1 cell
    BTO_0002999 = "BTO_0002999"
    CWR22_RV1_CELL = "BTO_0002999"

    # EB-1 cell
    BTO_0003000 = "BTO_0003000"
    EB_1_CELL = "BTO_0003000"

    # EBC-1 cell
    BTO_0003001 = "BTO_0003001"
    EBC_1_CELL = "BTO_0003001"

    # endocervix
    BTO_0003002 = "BTO_0003002"
    ENDOCERVIX = "BTO_0003002"

    # epididymal fluid
    BTO_0003003 = "BTO_0003003"
    EPIDIDYMAL_FLUID = "BTO_0003003"

    # NCI-H1435 cell
    BTO_0003004 = "BTO_0003004"
    NCI_H1435_CELL = "BTO_0003004"

    # NCI-H324 cell
    BTO_0003005 = "BTO_0003005"
    NCI_H324_CELL = "BTO_0003005"

    # NCI-H2122 cell
    BTO_0003006 = "BTO_0003006"
    NCI_H2122_CELL = "BTO_0003006"

    # NCI-H322 cell
    BTO_0003007 = "BTO_0003007"
    NCI_H322_CELL = "BTO_0003007"

    # NCI-H226 cell
    BTO_0003008 = "BTO_0003008"
    NCI_H226_CELL = "BTO_0003008"

    # NCI-H1703 cell
    BTO_0003009 = "BTO_0003009"
    NCI_H1703_CELL = "BTO_0003009"

    # NCI-H125 cell
    BTO_0003010 = "BTO_0003010"
    NCI_H125_CELL = "BTO_0003010"

    # NCI-H1334 cell
    BTO_0003011 = "BTO_0003011"
    NCI_H1334_CELL = "BTO_0003011"

    # NCI-H1264 cell
    BTO_0003012 = "BTO_0003012"
    NCI_H1264_CELL = "BTO_0003012"

    # NCI-H661 cell
    BTO_0003013 = "BTO_0003013"
    NCI_H661_CELL = "BTO_0003013"

    # NCI-H520 cell
    BTO_0003014 = "BTO_0003014"
    NCI_H520_CELL = "BTO_0003014"

    # macula lutea
    BTO_0003015 = "BTO_0003015"
    MACULA_LUTEA = "BTO_0003015"

    # SW-1573 cell
    BTO_0003016 = "BTO_0003016"
    SW_1573_CELL = "BTO_0003016"

    # COLO-699 cell
    BTO_0003017 = "BTO_0003017"
    COLO_699_CELL = "BTO_0003017"

    # NE-18 cell
    BTO_0003018 = "BTO_0003018"
    NE_18_CELL = "BTO_0003018"

    # NCI-H345 cell
    BTO_0003019 = "BTO_0003019"
    NCI_H345_CELL = "BTO_0003019"

    # NCI-H209 cell
    BTO_0003020 = "BTO_0003020"
    NCI_H209_CELL = "BTO_0003020"

    # NCI-H187 cell
    BTO_0003021 = "BTO_0003021"
    NCI_H187_CELL = "BTO_0003021"

    # NCI-H69 cell
    BTO_0003022 = "BTO_0003022"
    NCI_H69_CELL = "BTO_0003022"

    # NCI-H510 cell
    BTO_0003023 = "BTO_0003023"
    NCI_H510_CELL = "BTO_0003023"

    # NCI-H146 cell
    BTO_0003024 = "BTO_0003024"
    NCI_H146_CELL = "BTO_0003024"

    # NCI-H128 cell
    BTO_0003025 = "BTO_0003025"
    NCI_H128_CELL = "BTO_0003025"

    # NCI-H82 cell
    BTO_0003026 = "BTO_0003026"
    NCI_H82_CELL = "BTO_0003026"

    # NCI-H196 cell
    BTO_0003027 = "BTO_0003027"
    NCI_H196_CELL = "BTO_0003027"

    # NCI-N417 cell
    BTO_0003028 = "BTO_0003028"
    NCI_N417_CELL = "BTO_0003028"

    # SKLU-1 cell
    BTO_0003029 = "BTO_0003029"
    SKLU_1_CELL = "BTO_0003029"

    # MT-4 cell
    BTO_0003030 = "BTO_0003030"
    MT_4_CELL = "BTO_0003030"

    # HCA-7 cell
    BTO_0003031 = "BTO_0003031"
    HCA_7_CELL = "BTO_0003031"

    # HEK-293F cell
    BTO_0003032 = "BTO_0003032"
    HEK_293F_CELL = "BTO_0003032"

    # HEK-293H cell
    BTO_0003033 = "BTO_0003033"
    HEK_293H_CELL = "BTO_0003033"

    # HELF cell
    BTO_0003034 = "BTO_0003034"
    HELF_CELL = "BTO_0003034"

    # HS-Sultan cell
    BTO_0003035 = "BTO_0003035"
    HS_SULTAN_CELL = "BTO_0003035"

    # hippocampal cell line
    BTO_0003036 = "BTO_0003036"
    HIPPOCAMPAL_CELL_LINE = "BTO_0003036"

    # HT-22 cell
    BTO_0003037 = "BTO_0003037"
    HT_22_CELL = "BTO_0003037"

    # HEC-1-B cell
    BTO_0003038 = "BTO_0003038"
    HEC_1_B_CELL = "BTO_0003038"

    # hypodermal seam cell
    BTO_0003039 = "BTO_0003039"
    HYPODERMAL_SEAM_CELL = "BTO_0003039"

    # uterine adenocarcinoma cell line
    BTO_0003040 = "BTO_0003040"
    UTERINE_ADENOCARCINOMA_CELL_LINE = "BTO_0003040"

    # Ishikawa cell
    BTO_0003041 = "BTO_0003041"
    ISHIKAWA_CELL = "BTO_0003041"

    # J-774.1 cell
    BTO_0003042 = "BTO_0003042"
    J_774_1_CELL = "BTO_0003042"

    # JJ012-TS4 cell
    BTO_0003043 = "BTO_0003043"
    JJ012_TS4_CELL = "BTO_0003043"

    # JY cell
    BTO_0003044 = "BTO_0003044"
    JY_CELL = "BTO_0003044"

    # neuroma cell
    BTO_0003045 = "BTO_0003045"
    NEUROMA_CELL = "BTO_0003045"

    # neurofibroma cell
    BTO_0003046 = "BTO_0003046"
    NEUROFIBROMA_CELL = "BTO_0003046"

    # neurilemoma cell
    BTO_0003047 = "BTO_0003047"
    NEURILEMOMA_CELL = "BTO_0003047"

    # neurolemma
    BTO_0003048 = "BTO_0003048"
    NEUROLEMMA = "BTO_0003048"

    # kerathoacanthoma cell
    BTO_0003049 = "BTO_0003049"
    KERATHOACANTHOMA_CELL = "BTO_0003049"

    # MA-10 cell
    BTO_0003050 = "BTO_0003050"
    MA_10_CELL = "BTO_0003050"

    # MBA-15 cell
    BTO_0003051 = "BTO_0003051"
    MBA_15_CELL = "BTO_0003051"

    # MDA-686Ln cell
    BTO_0003052 = "BTO_0003052"
    MDA_686LN_CELL = "BTO_0003052"

    # NCI-N87 cell
    BTO_0003053 = "BTO_0003053"
    NCI_N87_CELL = "BTO_0003053"

    # OVCA-8 cell
    BTO_0003054 = "BTO_0003054"
    OVCA_8_CELL = "BTO_0003054"

    # NW-16 cell
    BTO_0003055 = "BTO_0003055"
    NW_16_CELL = "BTO_0003055"

    # NB-2 cell
    BTO_0003056 = "BTO_0003056"
    NB_2_CELL = "BTO_0003056"

    # NB2-Sp cell
    BTO_0003057 = "BTO_0003057"
    NB2_SP_CELL = "BTO_0003057"

    # NB2a/d1 cell
    BTO_0003058 = "BTO_0003058"
    NB2A_D1_CELL = "BTO_0003058"

    # oviduct epithelial cell line
    BTO_0003059 = "BTO_0003059"
    OVIDUCT_EPITHELIAL_CELL_LINE = "BTO_0003059"

    # PC12-AC cell
    BTO_0003060 = "BTO_0003060"
    PC12_AC_CELL = "BTO_0003060"

    # retinal cell line
    BTO_0003061 = "BTO_0003061"
    RETINAL_CELL_LINE = "BTO_0003061"

    # MIO-M1 cell
    BTO_0003062 = "BTO_0003062"
    MIO_M1_CELL = "BTO_0003062"

    # Mueller cell line
    BTO_0003063 = "BTO_0003063"
    MUELLER_CELL_LINE = "BTO_0003063"

    # Mueller cell
    BTO_0003064 = "BTO_0003064"
    MUELLER_CELL = "BTO_0003064"

    # VA13-TS4 cell
    BTO_0003065 = "BTO_0003065"
    VA13_TS4_CELL = "BTO_0003065"

    # WI38-VA13 subline 2RA cell
    BTO_0003066 = "BTO_0003066"
    WI38_VA13_SUBLINE_2RA_CELL = "BTO_0003066"

    # OE-E6/E7 cell
    BTO_0003067 = "BTO_0003067"
    OE_E6_E7_CELL = "BTO_0003067"

    # PNT-1A cell
    BTO_0003068 = "BTO_0003068"
    PNT_1A_CELL = "BTO_0003068"

    # OK cell
    BTO_0003069 = "BTO_0003069"
    OK_CELL = "BTO_0003069"

    # S2 cell
    BTO_0003070 = "BTO_0003070"
    S2_CELL = "BTO_0003070"

    # HLEC-SRA 01/04 cell
    BTO_0003071 = "BTO_0003071"
    HLEC_SRA_01_04_CELL = "BTO_0003071"

    # human lens epithelial cell line
    BTO_0003072 = "BTO_0003072"
    HUMAN_LENS_EPITHELIAL_CELL_LINE = "BTO_0003072"

    # medullary thyroid carcinoma cell line
    BTO_0003073 = "BTO_0003073"
    MEDULLARY_THYROID_CARCINOMA_CELL_LINE = "BTO_0003073"

    # TT cell
    BTO_0003074 = "BTO_0003074"
    TT_CELL = "BTO_0003074"

    # WM-115 cell
    BTO_0003075 = "BTO_0003075"
    WM_115_CELL = "BTO_0003075"

    # RAMOS cell
    BTO_0003076 = "BTO_0003076"
    RAMOS_CELL = "BTO_0003076"

    # RAMOS-AW cell
    BTO_0003077 = "BTO_0003077"
    RAMOS_AW_CELL = "BTO_0003077"

    # RAMOS-EHRB cell
    BTO_0003078 = "BTO_0003078"
    RAMOS_EHRB_CELL = "BTO_0003078"

    # RAMOS (RA.1) cell
    BTO_0003079 = "BTO_0003079"
    RAMOS__RA_1__CELL = "BTO_0003079"

    # pleural fluid
    BTO_0003080 = "BTO_0003080"
    PLEURAL_FLUID = "BTO_0003080"

    # pancreatic ductal adenocarcinoma cell
    BTO_0003081 = "BTO_0003081"
    PANCREATIC_DUCTAL_ADENOCARCINOMA_CELL = "BTO_0003081"

    # uterine epithelium
    BTO_0003082 = "BTO_0003082"
    UTERINE_EPITHELIUM = "BTO_0003082"

    # uterine wall
    BTO_0003083 = "BTO_0003083"
    UTERINE_WALL = "BTO_0003083"

    # vaginal fluid
    BTO_0003084 = "BTO_0003084"
    VAGINAL_FLUID = "BTO_0003084"

    # uterine anchor cell
    BTO_0003085 = "BTO_0003085"
    UTERINE_ANCHOR_CELL = "BTO_0003085"

    # rosette leaf
    BTO_0003086 = "BTO_0003086"
    ROSETTE_LEAF = "BTO_0003086"

    # subiculum
    BTO_0003087 = "BTO_0003087"
    SUBICULUM = "BTO_0003087"

    # subiculum promontorii
    BTO_0003088 = "BTO_0003088"
    SUBICULUM_PROMONTORII = "BTO_0003088"

    # promontorium tympani
    BTO_0003089 = "BTO_0003089"
    PROMONTORIUM_TYMPANI = "BTO_0003089"

    # subventricular zone
    BTO_0003090 = "BTO_0003090"
    SUBVENTRICULAR_ZONE = "BTO_0003090"

    # urogenital system
    BTO_0003091 = "BTO_0003091"
    UROGENITAL_SYSTEM = "BTO_0003091"

    # urinary system
    BTO_0003092 = "BTO_0003092"
    URINARY_SYSTEM = "BTO_0003092"

    # cardiofibroblast
    BTO_0003093 = "BTO_0003093"
    CARDIOFIBROBLAST = "BTO_0003093"

    # secondary oocyte
    BTO_0003094 = "BTO_0003094"
    SECONDARY_OOCYTE = "BTO_0003094"

    # normoblast
    BTO_0003095 = "BTO_0003095"
    NORMOBLAST = "BTO_0003095"

    # internal male genital organ
    BTO_0003096 = "BTO_0003096"
    INTERNAL_MALE_GENITAL_ORGAN = "BTO_0003096"

    # external male genital organ
    BTO_0003097 = "BTO_0003097"
    EXTERNAL_MALE_GENITAL_ORGAN = "BTO_0003097"

    # scrotum
    BTO_0003098 = "BTO_0003098"
    SCROTUM = "BTO_0003098"

    # internal female genital organ
    BTO_0003099 = "BTO_0003099"
    INTERNAL_FEMALE_GENITAL_ORGAN = "BTO_0003099"

    # external female genital organ
    BTO_0003100 = "BTO_0003100"
    EXTERNAL_FEMALE_GENITAL_ORGAN = "BTO_0003100"

    # female pudendum
    BTO_0003101 = "BTO_0003101"
    FEMALE_PUDENDUM = "BTO_0003101"

    # pyramidal neuron
    BTO_0003102 = "BTO_0003102"
    PYRAMIDAL_NEURON = "BTO_0003102"

    # pro-B-lymphocyte cell line
    BTO_0003103 = "BTO_0003103"
    PRO_B_LYMPHOCYTE_CELL_LINE = "BTO_0003103"

    # pro-B-lymphocyte
    BTO_0003104 = "BTO_0003104"
    PRO_B_LYMPHOCYTE = "BTO_0003104"

    # SW-1222 cell
    BTO_0003105 = "BTO_0003105"
    SW_1222_CELL = "BTO_0003105"

    # HOM-2 cell
    BTO_0003106 = "BTO_0003106"
    HOM_2_CELL = "BTO_0003106"

    # foreign-body giant cell
    BTO_0003107 = "BTO_0003107"
    FOREIGN_BODY_GIANT_CELL = "BTO_0003107"

    # ChaGo-K-1 cell
    BTO_0003108 = "BTO_0003108"
    CHAGO_K_1_CELL = "BTO_0003108"

    # CaSki cell
    BTO_0003109 = "BTO_0003109"
    CASKI_CELL = "BTO_0003109"

    # CALO cell
    BTO_0003110 = "BTO_0003110"
    CALO_CELL = "BTO_0003110"

    # VIPA cell
    BTO_0003111 = "BTO_0003111"
    VIPA_CELL = "BTO_0003111"

    # INBL cell
    BTO_0003112 = "BTO_0003112"
    INBL_CELL = "BTO_0003112"

    # ROVA cell
    BTO_0003113 = "BTO_0003113"
    ROVA_CELL = "BTO_0003113"

    # wound fluid
    BTO_0003114 = "BTO_0003114"
    WOUND_FLUID = "BTO_0003114"

    # major vestibular gland
    BTO_0003115 = "BTO_0003115"
    MAJOR_VESTIBULAR_GLAND = "BTO_0003115"

    # minor vestibular gland
    BTO_0003116 = "BTO_0003116"
    MINOR_VESTIBULAR_GLAND = "BTO_0003116"

    # glans clitoridis
    BTO_0003117 = "BTO_0003117"
    GLANS_CLITORIDIS = "BTO_0003117"

    # glans penis
    BTO_0003118 = "BTO_0003118"
    GLANS_PENIS = "BTO_0003118"

    # clitoral gland
    BTO_0003119 = "BTO_0003119"
    CLITORAL_GLAND = "BTO_0003119"

    # atherosclerotic plaque
    BTO_0003120 = "BTO_0003120"
    ATHEROSCLEROTIC_PLAQUE = "BTO_0003120"

    # villus
    BTO_0003121 = "BTO_0003121"
    VILLUS = "BTO_0003121"

    # microvascular endothelium
    BTO_0003122 = "BTO_0003122"
    MICROVASCULAR_ENDOTHELIUM = "BTO_0003122"

    # microvascular endothelial cell
    BTO_0003123 = "BTO_0003123"
    MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0003123"

    # microvascular endothelial cell line
    BTO_0003124 = "BTO_0003124"
    MICROVASCULAR_ENDOTHELIAL_CELL_LINE = "BTO_0003124"

    # HBMEC cell
    BTO_0003125 = "BTO_0003125"
    HBMEC_CELL = "BTO_0003125"

    # bone marrow endothelial cell line
    BTO_0003126 = "BTO_0003126"
    BONE_MARROW_ENDOTHELIAL_CELL_LINE = "BTO_0003126"

    # human bone marrow endothelial cell line
    BTO_0003127 = "BTO_0003127"
    HUMAN_BONE_MARROW_ENDOTHELIAL_CELL_LINE = "BTO_0003127"

    # brain microvascular endothelial cell line
    BTO_0003128 = "BTO_0003128"
    BRAIN_MICROVASCULAR_ENDOTHELIAL_CELL_LINE = "BTO_0003128"

    # human brain microvascular endothelial cell
    BTO_0003129 = "BTO_0003129"
    HUMAN_BRAIN_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0003129"

    # FL cell
    BTO_0003130 = "BTO_0003130"
    FL_CELL = "BTO_0003130"

    # CaR-1 cell
    BTO_0003131 = "BTO_0003131"
    CAR_1_CELL = "BTO_0003131"

    # microsporidian
    BTO_0003132 = "BTO_0003132"
    MICROSPORIDIAN = "BTO_0003132"

    # culture condition:acetylene-grown cell
    BTO_0003133 = "BTO_0003133"
    CULTURE_CONDITION_ACETYLENE_GROWN_CELL = "BTO_0003133"

    # culture condition:quinate-grown cell
    BTO_0003134 = "BTO_0003134"
    CULTURE_CONDITION_QUINATE_GROWN_CELL = "BTO_0003134"

    # zona pellucida
    BTO_0003135 = "BTO_0003135"
    ZONA_PELLUCIDA = "BTO_0003135"

    # ZR-75-1 cell
    BTO_0003136 = "BTO_0003136"
    ZR_75_1_CELL = "BTO_0003136"

    # 5637 cell
    BTO_0003137 = "BTO_0003137"
    _5637_CELL = "BTO_0003137"

    # UM-SCC-1 cell
    BTO_0003138 = "BTO_0003138"
    UM_SCC_1_CELL = "BTO_0003138"

    # UM-SCC-12 cell
    BTO_0003139 = "BTO_0003139"
    UM_SCC_12_CELL = "BTO_0003139"

    # UM-SCC-14A cell
    BTO_0003140 = "BTO_0003140"
    UM_SCC_14A_CELL = "BTO_0003140"

    # true leaf
    BTO_0003141 = "BTO_0003141"
    TRUE_LEAF = "BTO_0003141"

    # KU-812F cell
    BTO_0003142 = "BTO_0003142"
    KU_812F_CELL = "BTO_0003142"

    # coculture
    BTO_0003143 = "BTO_0003143"
    COCULTURE = "BTO_0003143"

    # neuron-oligodendrocyte coculture
    BTO_0003144 = "BTO_0003144"
    NEURON_OLIGODENDROCYTE_COCULTURE = "BTO_0003144"

    # vestibulum vaginae
    BTO_0003145 = "BTO_0003145"
    VESTIBULUM_VAGINAE = "BTO_0003145"

    # zona incerta
    BTO_0003146 = "BTO_0003146"
    ZONA_INCERTA = "BTO_0003146"

    # juvenile leaf
    BTO_0003147 = "BTO_0003147"
    JUVENILE_LEAF = "BTO_0003147"

    # culture condition:milk-grown cell
    BTO_0003148 = "BTO_0003148"
    CULTURE_CONDITION_MILK_GROWN_CELL = "BTO_0003148"

    # interalveolar septum
    BTO_0003149 = "BTO_0003149"
    INTERALVEOLAR_SEPTUM = "BTO_0003149"

    # pulmonary artery endothelial cell line
    BTO_0003150 = "BTO_0003150"
    PULMONARY_ARTERY_ENDOTHELIAL_CELL_LINE = "BTO_0003150"

    # HPAEC cell
    BTO_0003151 = "BTO_0003151"
    HPAEC_CELL = "BTO_0003151"

    # papillary thyroid cancer cell
    BTO_0003152 = "BTO_0003152"
    PAPILLARY_THYROID_CANCER_CELL = "BTO_0003152"

    # perineurium
    BTO_0003153 = "BTO_0003153"
    PERINEURIUM = "BTO_0003153"

    # epineurium
    BTO_0003154 = "BTO_0003154"
    EPINEURIUM = "BTO_0003154"

    # pleural mesothelium
    BTO_0003155 = "BTO_0003155"
    PLEURAL_MESOTHELIUM = "BTO_0003155"

    # peritoneal mesothelium
    BTO_0003156 = "BTO_0003156"
    PERITONEAL_MESOTHELIUM = "BTO_0003156"

    # pericardial mesothelium
    BTO_0003157 = "BTO_0003157"
    PERICARDIAL_MESOTHELIUM = "BTO_0003157"

    # prostate gland anterior lobe
    BTO_0003158 = "BTO_0003158"
    PROSTATE_GLAND_ANTERIOR_LOBE = "BTO_0003158"

    # prostate gland smooth muscle
    BTO_0003159 = "BTO_0003159"
    PROSTATE_GLAND_SMOOTH_MUSCLE = "BTO_0003159"

    # PrEC cell
    BTO_0003160 = "BTO_0003160"
    PREC_CELL = "BTO_0003160"

    # PrSMC cell
    BTO_0003161 = "BTO_0003161"
    PRSMC_CELL = "BTO_0003161"

    # PrSC cell
    BTO_0003162 = "BTO_0003162"
    PRSC_CELL = "BTO_0003162"

    # prostatic urethra
    BTO_0003163 = "BTO_0003163"
    PROSTATIC_URETHRA = "BTO_0003163"

    # cholangiocyte
    BTO_0003164 = "BTO_0003164"
    CHOLANGIOCYTE = "BTO_0003164"

    # cervical adenocarcinoma cell
    BTO_0003165 = "BTO_0003165"
    CERVICAL_ADENOCARCINOMA_CELL = "BTO_0003165"

    # 10T1/2 cell
    BTO_0003166 = "BTO_0003166"
    _10T1_2_CELL = "BTO_0003166"

    # 143-B cell
    BTO_0003167 = "BTO_0003167"
    _143_B_CELL = "BTO_0003167"

    # cysticercus
    BTO_0003168 = "BTO_0003168"
    CYSTICERCUS = "BTO_0003168"

    # SNU-368 cell
    BTO_0003169 = "BTO_0003169"
    SNU_368_CELL = "BTO_0003169"

    # SNU-398 cell
    BTO_0003170 = "BTO_0003170"
    SNU_398_CELL = "BTO_0003170"

    # CCD-841-CoN cell
    BTO_0003171 = "BTO_0003171"
    CCD_841_CON_CELL = "BTO_0003171"

    # KM-12 cell
    BTO_0003172 = "BTO_0003172"
    KM_12_CELL = "BTO_0003172"

    # endostyle
    BTO_0003173 = "BTO_0003173"
    ENDOSTYLE = "BTO_0003173"

    # outer plexiform layer
    BTO_0003174 = "BTO_0003174"
    OUTER_PLEXIFORM_LAYER = "BTO_0003174"

    # inner plexiform layer
    BTO_0003175 = "BTO_0003175"
    INNER_PLEXIFORM_LAYER = "BTO_0003175"

    # inner nuclear layer
    BTO_0003176 = "BTO_0003176"
    INNER_NUCLEAR_LAYER = "BTO_0003176"

    # semimembranosus
    BTO_0003177 = "BTO_0003177"
    SEMIMEMBRANOSUS = "BTO_0003177"

    # biceps
    BTO_0003178 = "BTO_0003178"
    BICEPS = "BTO_0003178"

    # hamstring muscle
    BTO_0003179 = "BTO_0003179"
    HAMSTRING_MUSCLE = "BTO_0003179"

    # HeLa-80 cell
    BTO_0003180 = "BTO_0003180"
    HELA_80_CELL = "BTO_0003180"

    # WEHI-7.2 cell
    BTO_0003181 = "BTO_0003181"
    WEHI_7_2_CELL = "BTO_0003181"

    # NHEK cell
    BTO_0003182 = "BTO_0003182"
    NHEK_CELL = "BTO_0003182"

    # melanocyte cell line
    BTO_0003183 = "BTO_0003183"
    MELANOCYTE_CELL_LINE = "BTO_0003183"

    # NHEM cell
    BTO_0003184 = "BTO_0003184"
    NHEM_CELL = "BTO_0003184"

    # NHDF cell
    BTO_0003185 = "BTO_0003185"
    NHDF_CELL = "BTO_0003185"

    # NHM cell
    BTO_0003186 = "BTO_0003186"
    NHM_CELL = "BTO_0003186"

    # SNU-423 cell
    BTO_0003187 = "BTO_0003187"
    SNU_423_CELL = "BTO_0003187"

    # SNU-449 cell
    BTO_0003188 = "BTO_0003188"
    SNU_449_CELL = "BTO_0003188"

    # SNU-475 cell
    BTO_0003189 = "BTO_0003189"
    SNU_475_CELL = "BTO_0003189"

    # SNU-354 cell
    BTO_0003190 = "BTO_0003190"
    SNU_354_CELL = "BTO_0003190"

    # SNU-387 cell
    BTO_0003191 = "BTO_0003191"
    SNU_387_CELL = "BTO_0003191"

    # renal cancer cell line
    BTO_0003192 = "BTO_0003192"
    RENAL_CANCER_CELL_LINE = "BTO_0003192"

    # SK-RC-1 cell
    BTO_0003193 = "BTO_0003193"
    SK_RC_1_CELL = "BTO_0003193"

    # SK-RC-6 cell
    BTO_0003194 = "BTO_0003194"
    SK_RC_6_CELL = "BTO_0003194"

    # SK-RC-7 cell
    BTO_0003195 = "BTO_0003195"
    SK_RC_7_CELL = "BTO_0003195"

    # SK-RC-17 cell
    BTO_0003196 = "BTO_0003196"
    SK_RC_17_CELL = "BTO_0003196"

    # SK-RC-29 cell
    BTO_0003197 = "BTO_0003197"
    SK_RC_29_CELL = "BTO_0003197"

    # SK-RC-35 cell
    BTO_0003198 = "BTO_0003198"
    SK_RC_35_CELL = "BTO_0003198"

    # SK-RC-39 cell
    BTO_0003199 = "BTO_0003199"
    SK_RC_39_CELL = "BTO_0003199"

    # SK-RC-44 cell
    BTO_0003200 = "BTO_0003200"
    SK_RC_44_CELL = "BTO_0003200"

    # SK-RC-45 cell
    BTO_0003201 = "BTO_0003201"
    SK_RC_45_CELL = "BTO_0003201"

    # SK-RC-99 cell
    BTO_0003202 = "BTO_0003202"
    SK_RC_99_CELL = "BTO_0003202"

    # Moroff cell
    BTO_0003203 = "BTO_0003203"
    MOROFF_CELL = "BTO_0003203"

    # Caki-1 cell
    BTO_0003204 = "BTO_0003204"
    CAKI_1_CELL = "BTO_0003204"

    # salivary gland cell line
    BTO_0003205 = "BTO_0003205"
    SALIVARY_GLAND_CELL_LINE = "BTO_0003205"

    # A-253 cell
    BTO_0003206 = "BTO_0003206"
    A_253_CELL = "BTO_0003206"

    # A2780/100 cell
    BTO_0003207 = "BTO_0003207"
    A2780_100_CELL = "BTO_0003207"

    # anaplastic thyroid cancer cell
    BTO_0003208 = "BTO_0003208"
    ANAPLASTIC_THYROID_CANCER_CELL = "BTO_0003208"

    # anaplastic thyroid cancer cell line
    BTO_0003209 = "BTO_0003209"
    ANAPLASTIC_THYROID_CANCER_CELL_LINE = "BTO_0003209"

    # papillary thyroid cancer cell line
    BTO_0003210 = "BTO_0003210"
    PAPILLARY_THYROID_CANCER_CELL_LINE = "BTO_0003210"

    # S49.A2 cell
    BTO_0003211 = "BTO_0003211"
    S49_A2_CELL = "BTO_0003211"

    # T-lymphoma cell line
    BTO_0003212 = "BTO_0003212"
    T_LYMPHOMA_CELL_LINE = "BTO_0003212"

    # lung epithelium cell line
    BTO_0003213 = "BTO_0003213"
    LUNG_EPITHELIUM_CELL_LINE = "BTO_0003213"

    # HPL1D cell
    BTO_0003214 = "BTO_0003214"
    HPL1D_CELL = "BTO_0003214"

    # VCaP cell
    BTO_0003215 = "BTO_0003215"
    VCAP_CELL = "BTO_0003215"

    # melan-a cell
    BTO_0003216 = "BTO_0003216"
    MELAN_A_CELL = "BTO_0003216"

    # melanoblast
    BTO_0003217 = "BTO_0003217"
    MELANOBLAST = "BTO_0003217"

    # U-343MG-A cell
    BTO_0003218 = "BTO_0003218"
    U_343MG_A_CELL = "BTO_0003218"

    # TMK-1 cell
    BTO_0003219 = "BTO_0003219"
    TMK_1_CELL = "BTO_0003219"

    # SK32 cell
    BTO_0003220 = "BTO_0003220"
    SK32_CELL = "BTO_0003220"

    # corneal cell line
    BTO_0003221 = "BTO_0003221"
    CORNEAL_CELL_LINE = "BTO_0003221"

    # respiratory bronchiole
    BTO_0003222 = "BTO_0003222"
    RESPIRATORY_BRONCHIOLE = "BTO_0003222"

    # terminal bronchiole
    BTO_0003223 = "BTO_0003223"
    TERMINAL_BRONCHIOLE = "BTO_0003223"

    # TRK-43 cell
    BTO_0003224 = "BTO_0003224"
    TRK_43_CELL = "BTO_0003224"

    # neurilemoma cell line
    BTO_0003225 = "BTO_0003225"
    NEURILEMOMA_CELL_LINE = "BTO_0003225"

    # STS-26T cell
    BTO_0003226 = "BTO_0003226"
    STS_26T_CELL = "BTO_0003226"

    # SMMC-7721 cell
    BTO_0003227 = "BTO_0003227"
    SMMC_7721_CELL = "BTO_0003227"

    # SK-LC-8 cell
    BTO_0003228 = "BTO_0003228"
    SK_LC_8_CELL = "BTO_0003228"

    # SK-LC-16 cell
    BTO_0003229 = "BTO_0003229"
    SK_LC_16_CELL = "BTO_0003229"

    # RL cell
    BTO_0003230 = "BTO_0003230"
    RL_CELL = "BTO_0003230"

    # SHG-44 cell
    BTO_0003231 = "BTO_0003231"
    SHG_44_CELL = "BTO_0003231"

    # BT-325 cell
    BTO_0003232 = "BTO_0003232"
    BT_325_CELL = "BTO_0003232"

    # FaDu cell
    BTO_0003233 = "BTO_0003233"
    FADU_CELL = "BTO_0003233"

    # FTO-2B cell
    BTO_0003234 = "BTO_0003234"
    FTO_2B_CELL = "BTO_0003234"

    # gall bladder cell line
    BTO_0003235 = "BTO_0003235"
    GALL_BLADDER_CELL_LINE = "BTO_0003235"

    # gall bladder cancer cell line
    BTO_0003236 = "BTO_0003236"
    GALL_BLADDER_CANCER_CELL_LINE = "BTO_0003236"

    # gall bladder cancer cell
    BTO_0003237 = "BTO_0003237"
    GALL_BLADDER_CANCER_CELL = "BTO_0003237"

    # NCI-H23 cell
    BTO_0003238 = "BTO_0003238"
    NCI_H23_CELL = "BTO_0003238"

    # NCI-H838 cell
    BTO_0003239 = "BTO_0003239"
    NCI_H838_CELL = "BTO_0003239"

    # NCI-H2126 cell
    BTO_0003240 = "BTO_0003240"
    NCI_H2126_CELL = "BTO_0003240"

    # NCI-H2087 cell
    BTO_0003241 = "BTO_0003241"
    NCI_H2087_CELL = "BTO_0003241"

    # NCI-H2009 cell
    BTO_0003242 = "BTO_0003242"
    NCI_H2009_CELL = "BTO_0003242"

    # NCI-H1684 cell
    BTO_0003243 = "BTO_0003243"
    NCI_H1684_CELL = "BTO_0003243"

    # NCI-H1437 cell
    BTO_0003244 = "BTO_0003244"
    NCI_H1437_CELL = "BTO_0003244"

    # aortic endothelial cell
    BTO_0003245 = "BTO_0003245"
    AORTIC_ENDOTHELIAL_CELL = "BTO_0003245"

    # aortic endothelial cell line
    BTO_0003246 = "BTO_0003246"
    AORTIC_ENDOTHELIAL_CELL_LINE = "BTO_0003246"

    # BAEC cell
    BTO_0003247 = "BTO_0003247"
    BAEC_CELL = "BTO_0003247"

    # brain endothelium
    BTO_0003248 = "BTO_0003248"
    BRAIN_ENDOTHELIUM = "BTO_0003248"

    # brain endothelium cell line
    BTO_0003249 = "BTO_0003249"
    BRAIN_ENDOTHELIUM_CELL_LINE = "BTO_0003249"

    # colonic epithelium cell line
    BTO_0003250 = "BTO_0003250"
    COLONIC_EPITHELIUM_CELL_LINE = "BTO_0003250"

    # CCD-841 cell
    BTO_0003251 = "BTO_0003251"
    CCD_841_CELL = "BTO_0003251"

    # uterine leiomyoma cell line
    BTO_0003252 = "BTO_0003252"
    UTERINE_LEIOMYOMA_CELL_LINE = "BTO_0003252"

    # ELT-3 cell
    BTO_0003253 = "BTO_0003253"
    ELT_3_CELL = "BTO_0003253"

    # DPK-SKDF-H cell
    BTO_0003254 = "BTO_0003254"
    DPK_SKDF_H_CELL = "BTO_0003254"

    # AX-4 cell
    BTO_0003255 = "BTO_0003255"
    AX_4_CELL = "BTO_0003255"

    # corpus amylaceum
    BTO_0003256 = "BTO_0003256"
    CORPUS_AMYLACEUM = "BTO_0003256"

    # granulation tissue
    BTO_0003257 = "BTO_0003257"
    GRANULATION_TISSUE = "BTO_0003257"

    # Col-1 cell
    BTO_0003258 = "BTO_0003258"
    COL_1_CELL = "BTO_0003258"

    # Col-24 cell
    BTO_0003259 = "BTO_0003259"
    COL_24_CELL = "BTO_0003259"

    # Col-6 cell
    BTO_0003260 = "BTO_0003260"
    COL_6_CELL = "BTO_0003260"

    # HCN-1A cell
    BTO_0003261 = "BTO_0003261"
    HCN_1A_CELL = "BTO_0003261"

    # HCN-2 cell
    BTO_0003262 = "BTO_0003262"
    HCN_2_CELL = "BTO_0003262"

    # HEK-AD293 cell
    BTO_0003263 = "BTO_0003263"
    HEK_AD293_CELL = "BTO_0003263"

    # HL-1 cell
    BTO_0003264 = "BTO_0003264"
    HL_1_CELL = "BTO_0003264"

    # cardiac muscle cell line
    BTO_0003265 = "BTO_0003265"
    CARDIAC_MUSCLE_CELL_LINE = "BTO_0003265"

    # HPAF-2 cell
    BTO_0003266 = "BTO_0003266"
    HPAF_2_CELL = "BTO_0003266"

    # HS-766T cell
    BTO_0003267 = "BTO_0003267"
    HS_766T_CELL = "BTO_0003267"

    # HS578 cell
    BTO_0003268 = "BTO_0003268"
    HS578_CELL = "BTO_0003268"

    # feather barbicels
    BTO_0003269 = "BTO_0003269"
    FEATHER_BARBICELS = "BTO_0003269"

    # Me665/2 cell
    BTO_0003270 = "BTO_0003270"
    ME665_2_CELL = "BTO_0003270"

    # great saphenous vein
    BTO_0003271 = "BTO_0003271"
    GREAT_SAPHENOUS_VEIN = "BTO_0003271"

    # small saphenous vein
    BTO_0003272 = "BTO_0003272"
    SMALL_SAPHENOUS_VEIN = "BTO_0003272"

    # saphenous vein endothelium
    BTO_0003273 = "BTO_0003273"
    SAPHENOUS_VEIN_ENDOTHELIUM = "BTO_0003273"

    # saphenous vein endothelial cell line
    BTO_0003274 = "BTO_0003274"
    SAPHENOUS_VEIN_ENDOTHELIAL_CELL_LINE = "BTO_0003274"

    # HSVEC cell
    BTO_0003275 = "BTO_0003275"
    HSVEC_CELL = "BTO_0003275"

    # EHEB cell
    BTO_0003276 = "BTO_0003276"
    EHEB_CELL = "BTO_0003276"

    # H2.35 cell
    BTO_0003277 = "BTO_0003277"
    H2_35_CELL = "BTO_0003277"

    # V79MZh11B1 cell
    BTO_0003278 = "BTO_0003278"
    V79MZH11B1_CELL = "BTO_0003278"

    # V79MZh11B2 cell
    BTO_0003279 = "BTO_0003279"
    V79MZH11B2_CELL = "BTO_0003279"

    # sessile cell
    BTO_0003280 = "BTO_0003280"
    SESSILE_CELL = "BTO_0003280"

    # planktonic cell
    BTO_0003281 = "BTO_0003281"
    PLANKTONIC_CELL = "BTO_0003281"

    # Tet-iNOS-293 cell
    BTO_0003282 = "BTO_0003282"
    TET_INOS_293_CELL = "BTO_0003282"

    # SC-M1 cell
    BTO_0003283 = "BTO_0003283"
    SC_M1_CELL = "BTO_0003283"

    # TMC-1 cell
    BTO_0003284 = "BTO_0003284"
    TMC_1_CELL = "BTO_0003284"

    # PCI-43 cell
    BTO_0003285 = "BTO_0003285"
    PCI_43_CELL = "BTO_0003285"

    # PCI-35 cell
    BTO_0003286 = "BTO_0003286"
    PCI_35_CELL = "BTO_0003286"

    # NK-92 cell
    BTO_0003287 = "BTO_0003287"
    NK_92_CELL = "BTO_0003287"

    # NALM-6 cell
    BTO_0003288 = "BTO_0003288"
    NALM_6_CELL = "BTO_0003288"

    # NAMALWA cell
    BTO_0003289 = "BTO_0003289"
    NAMALWA_CELL = "BTO_0003289"

    # PanIN cell
    BTO_0003290 = "BTO_0003290"
    PANIN_CELL = "BTO_0003290"

    # P493-6 cell
    BTO_0003291 = "BTO_0003291"
    P493_6_CELL = "BTO_0003291"

    # RAW-264.7 cell
    BTO_0003292 = "BTO_0003292"
    RAW_264_7_CELL = "BTO_0003292"

    # Rat-1 cell
    BTO_0003293 = "BTO_0003293"
    RAT_1_CELL = "BTO_0003293"

    # Rat1-R12 cell
    BTO_0003294 = "BTO_0003294"
    RAT1_R12_CELL = "BTO_0003294"

    # OP-9 cell
    BTO_0003295 = "BTO_0003295"
    OP_9_CELL = "BTO_0003295"

    # bone marrow stromal cell line
    BTO_0003296 = "BTO_0003296"
    BONE_MARROW_STROMAL_CELL_LINE = "BTO_0003296"

    # NCTC-2544 cell
    BTO_0003297 = "BTO_0003297"
    NCTC_2544_CELL = "BTO_0003297"

    # mesenchymal stem cell
    BTO_0003298 = "BTO_0003298"
    MESENCHYMAL_STEM_CELL = "BTO_0003298"

    # MM5MT cell
    BTO_0003299 = "BTO_0003299"
    MM5MT_CELL = "BTO_0003299"

    # MM5MTC cell
    BTO_0003300 = "BTO_0003300"
    MM5MTC_CELL = "BTO_0003300"

    # MEWO cell
    BTO_0003301 = "BTO_0003301"
    MEWO_CELL = "BTO_0003301"

    # MDA-Panc-3 cell
    BTO_0003302 = "BTO_0003302"
    MDA_PANC_3_CELL = "BTO_0003302"

    # MDA-Panc-28 cell
    BTO_0003303 = "BTO_0003303"
    MDA_PANC_28_CELL = "BTO_0003303"

    # MDA-1483 cell
    BTO_0003304 = "BTO_0003304"
    MDA_1483_CELL = "BTO_0003304"

    # epipodite
    BTO_0003305 = "BTO_0003305"
    EPIPODITE = "BTO_0003305"

    # Mat-Ly-Lu cell
    BTO_0003306 = "BTO_0003306"
    MAT_LY_LU_CELL = "BTO_0003306"

    # L6E9 cell
    BTO_0003307 = "BTO_0003307"
    L6E9_CELL = "BTO_0003307"

    # L-363 cell
    BTO_0003308 = "BTO_0003308"
    L_363_CELL = "BTO_0003308"

    # KMBC cell
    BTO_0003309 = "BTO_0003309"
    KMBC_CELL = "BTO_0003309"

    # KMCH cell
    BTO_0003310 = "BTO_0003310"
    KMCH_CELL = "BTO_0003310"

    # Mz-ChA-1 cell
    BTO_0003311 = "BTO_0003311"
    MZ_CHA_1_CELL = "BTO_0003311"

    # KM-12C cell
    BTO_0003312 = "BTO_0003312"
    KM_12C_CELL = "BTO_0003312"

    # WT-8 cell
    BTO_0003313 = "BTO_0003313"
    WT_8_CELL = "BTO_0003313"

    # J.CaM1.6 cell
    BTO_0003314 = "BTO_0003314"
    J_CAM1_6_CELL = "BTO_0003314"

    # UM-SCC-2 cell
    BTO_0003315 = "BTO_0003315"
    UM_SCC_2_CELL = "BTO_0003315"

    # JB6 Cl41 cell
    BTO_0003316 = "BTO_0003316"
    JB6_CL41_CELL = "BTO_0003316"

    # INS-1E cell
    BTO_0003317 = "BTO_0003317"
    INS_1E_CELL = "BTO_0003317"

    # INS-1 823/13 cell
    BTO_0003318 = "BTO_0003318"
    INS_1_823_13_CELL = "BTO_0003318"

    # Hepa-1 cell
    BTO_0003319 = "BTO_0003319"
    HEPA_1_CELL = "BTO_0003319"

    # HEL-92.1.7 cell
    BTO_0003320 = "BTO_0003320"
    HEL_92_1_7_CELL = "BTO_0003320"

    # HCE cell
    BTO_0003321 = "BTO_0003321"
    HCE_CELL = "BTO_0003321"

    # HCC-2998 cell
    BTO_0003322 = "BTO_0003322"
    HCC_2998_CELL = "BTO_0003322"

    # HCC-1937 cell
    BTO_0003323 = "BTO_0003323"
    HCC_1937_CELL = "BTO_0003323"

    # cardiomyocyte cell line
    BTO_0003324 = "BTO_0003324"
    CARDIOMYOCYTE_CELL_LINE = "BTO_0003324"

    # GE-11 cell
    BTO_0003325 = "BTO_0003325"
    GE_11_CELL = "BTO_0003325"

    # FLK cell
    BTO_0003326 = "BTO_0003326"
    FLK_CELL = "BTO_0003326"

    # FL83B cell
    BTO_0003327 = "BTO_0003327"
    FL83B_CELL = "BTO_0003327"

    # FL5.12 cell
    BTO_0003328 = "BTO_0003328"
    FL5_12_CELL = "BTO_0003328"

    # EMT-6 cell
    BTO_0003329 = "BTO_0003329"
    EMT_6_CELL = "BTO_0003329"

    # culture condition:n-hexadecane-grown cell
    BTO_0003330 = "BTO_0003330"
    CULTURE_CONDITION_N_HEXADECANE_GROWN_CELL = "BTO_0003330"

    # culture condition:methane-grown cell
    BTO_0003331 = "BTO_0003331"
    CULTURE_CONDITION_METHANE_GROWN_CELL = "BTO_0003331"

    # culture condition:glycolate-grown cell
    BTO_0003332 = "BTO_0003332"
    CULTURE_CONDITION_GLYCOLATE_GROWN_CELL = "BTO_0003332"

    # culture condition:1,2-propanediol-grown cell
    BTO_0003333 = "BTO_0003333"
    CULTURE_CONDITION_1_2_PROPANEDIOL_GROWN_CELL = "BTO_0003333"

    # culture condition:lactate/sulfate-grown cell
    BTO_0003334 = "BTO_0003334"
    CULTURE_CONDITION_LACTATE_SULFATE_GROWN_CELL = "BTO_0003334"

    # EBV-LCL cell
    BTO_0003335 = "BTO_0003335"
    EBV_LCL_CELL = "BTO_0003335"

    # pulmonary artery smooth muscle cell
    BTO_0003336 = "BTO_0003336"
    PULMONARY_ARTERY_SMOOTH_MUSCLE_CELL = "BTO_0003336"

    # pulmonary artery smooth muscle cell line
    BTO_0003337 = "BTO_0003337"
    PULMONARY_ARTERY_SMOOTH_MUSCLE_CELL_LINE = "BTO_0003337"

    # CS-54 cell
    BTO_0003338 = "BTO_0003338"
    CS_54_CELL = "BTO_0003338"

    # HCMEC/D3 cell
    BTO_0003339 = "BTO_0003339"
    HCMEC_D3_CELL = "BTO_0003339"

    # CL-3 cell
    BTO_0003340 = "BTO_0003340"
    CL_3_CELL = "BTO_0003340"

    # CL1-1 cell
    BTO_0003341 = "BTO_0003341"
    CL1_1_CELL = "BTO_0003341"

    # CL1-2 cell
    BTO_0003342 = "BTO_0003342"
    CL1_2_CELL = "BTO_0003342"

    # CL1-3 cell
    BTO_0003343 = "BTO_0003343"
    CL1_3_CELL = "BTO_0003343"

    # CL1-4 cell
    BTO_0003344 = "BTO_0003344"
    CL1_4_CELL = "BTO_0003344"

    # CL1 lung adenocarcinoma cell
    BTO_0003345 = "BTO_0003345"
    CL1_LUNG_ADENOCARCINOMA_CELL = "BTO_0003345"

    # corneal fibroblast cell line
    BTO_0003346 = "BTO_0003346"
    CORNEAL_FIBROBLAST_CELL_LINE = "BTO_0003346"

    # HEK-293 Tet-On 3G cell
    BTO_0003347 = "BTO_0003347"
    HEK_293_TET_ON_3G_CELL = "BTO_0003347"

    # C20D cell
    BTO_0003348 = "BTO_0003348"
    C20D_CELL = "BTO_0003348"

    # microglial cell line
    BTO_0003349 = "BTO_0003349"
    MICROGLIAL_CELL_LINE = "BTO_0003349"

    # BV-2 cell
    BTO_0003350 = "BTO_0003350"
    BV_2_CELL = "BTO_0003350"

    # BN17 cell
    BTO_0003351 = "BTO_0003351"
    BN17_CELL = "BTO_0003351"

    # brain capillary endothelial cell line
    BTO_0003352 = "BTO_0003352"
    BRAIN_CAPILLARY_ENDOTHELIAL_CELL_LINE = "BTO_0003352"

    # bEnd3 cell
    BTO_0003353 = "BTO_0003353"
    BEND3_CELL = "BTO_0003353"

    # B-cell chronic lymphocytic leukemia cell
    BTO_0003354 = "BTO_0003354"
    B_CELL_CHRONIC_LYMPHOCYTIC_LEUKEMIA_CELL = "BTO_0003354"

    # BEAS-2B/BBM cell
    BTO_0003355 = "BTO_0003355"
    BEAS_2B_BBM_CELL = "BTO_0003355"

    # BBm cell
    BTO_0003356 = "BTO_0003356"
    BBM_CELL = "BTO_0003356"

    # ARPE cell
    BTO_0003357 = "BTO_0003357"
    ARPE_CELL = "BTO_0003357"

    # groin
    BTO_0003358 = "BTO_0003358"
    GROIN = "BTO_0003358"

    # neointima
    BTO_0003359 = "BTO_0003359"
    NEOINTIMA = "BTO_0003359"

    # extraembryonic tissue
    BTO_0003360 = "BTO_0003360"
    EXTRAEMBRYONIC_TISSUE = "BTO_0003360"

    # anterior visceral endoderm
    BTO_0003361 = "BTO_0003361"
    ANTERIOR_VISCERAL_ENDODERM = "BTO_0003361"

    # anterior visceral ectoderm
    BTO_0003362 = "BTO_0003362"
    ANTERIOR_VISCERAL_ECTODERM = "BTO_0003362"

    # hyphal tip
    BTO_0003363 = "BTO_0003363"
    HYPHAL_TIP = "BTO_0003363"

    # gingival fluid
    BTO_0003364 = "BTO_0003364"
    GINGIVAL_FLUID = "BTO_0003364"

    # germinated grain
    BTO_0003365 = "BTO_0003365"
    GERMINATED_GRAIN = "BTO_0003365"

    # robust nucleus of arcopallium
    BTO_0003366 = "BTO_0003366"
    ROBUST_NUCLEUS_OF_ARCOPALLIUM = "BTO_0003366"

    # daphnid
    BTO_0003367 = "BTO_0003367"
    DAPHNID = "BTO_0003367"

    # frontal gland
    BTO_0003368 = "BTO_0003368"
    FRONTAL_GLAND = "BTO_0003368"

    # face
    BTO_0003369 = "BTO_0003369"
    FACE = "BTO_0003369"

    # craniofacial region
    BTO_0003370 = "BTO_0003370"
    CRANIOFACIAL_REGION = "BTO_0003370"

    # endometrial spiral artery
    BTO_0003371 = "BTO_0003371"
    ENDOMETRIAL_SPIRAL_ARTERY = "BTO_0003371"

    # gametophore
    BTO_0003372 = "BTO_0003372"
    GAMETOPHORE = "BTO_0003372"

    # gametangium
    BTO_0003373 = "BTO_0003373"
    GAMETANGIUM = "BTO_0003373"

    # antheridium
    BTO_0003374 = "BTO_0003374"
    ANTHERIDIUM = "BTO_0003374"

    # archegonium
    BTO_0003375 = "BTO_0003375"
    ARCHEGONIUM = "BTO_0003375"

    # RCH-ACV cell
    BTO_0003376 = "BTO_0003376"
    RCH_ACV_CELL = "BTO_0003376"

    # periderm
    BTO_0003377 = "BTO_0003377"
    PERIDERM = "BTO_0003377"

    # phellem
    BTO_0003378 = "BTO_0003378"
    PHELLEM = "BTO_0003378"

    # phellogen
    BTO_0003379 = "BTO_0003379"
    PHELLOGEN = "BTO_0003379"

    # phelloderm
    BTO_0003380 = "BTO_0003380"
    PHELLODERM = "BTO_0003380"

    # vestibular system
    BTO_0003381 = "BTO_0003381"
    VESTIBULAR_SYSTEM = "BTO_0003381"

    # inner ear vestibulum
    BTO_0003382 = "BTO_0003382"
    INNER_EAR_VESTIBULUM = "BTO_0003382"

    # semicircular canal
    BTO_0003383 = "BTO_0003383"
    SEMICIRCULAR_CANAL = "BTO_0003383"

    # small intestine adenoma cell
    BTO_0003384 = "BTO_0003384"
    SMALL_INTESTINE_ADENOMA_CELL = "BTO_0003384"

    # etiolated plant tissue
    BTO_0003385 = "BTO_0003385"
    ETIOLATED_PLANT_TISSUE = "BTO_0003385"

    # hypoglossal nerve
    BTO_0003386 = "BTO_0003386"
    HYPOGLOSSAL_NERVE = "BTO_0003386"

    # raphe nucleus
    BTO_0003387 = "BTO_0003387"
    RAPHE_NUCLEUS = "BTO_0003387"

    # tegmentum
    BTO_0003388 = "BTO_0003388"
    TEGMENTUM = "BTO_0003388"

    # nidopallium
    BTO_0003389 = "BTO_0003389"
    NIDOPALLIUM = "BTO_0003389"

    # high vocal center
    BTO_0003390 = "BTO_0003390"
    HIGH_VOCAL_CENTER = "BTO_0003390"

    # hepatic primordium
    BTO_0003391 = "BTO_0003391"
    HEPATIC_PRIMORDIUM = "BTO_0003391"

    # medial nidopallium
    BTO_0003392 = "BTO_0003392"
    MEDIAL_NIDOPALLIUM = "BTO_0003392"

    # granule cell
    BTO_0003393 = "BTO_0003393"
    GRANULE_CELL = "BTO_0003393"

    # Brockmann body
    BTO_0003394 = "BTO_0003394"
    BROCKMANN_BODY = "BTO_0003394"

    # Spemanns organizer
    BTO_0003395 = "BTO_0003395"
    SPEMANNS_ORGANIZER = "BTO_0003395"

    # pontine nucleus
    BTO_0003396 = "BTO_0003396"
    PONTINE_NUCLEUS = "BTO_0003396"

    # feather barbules
    BTO_0003397 = "BTO_0003397"
    FEATHER_BARBULES = "BTO_0003397"

    # ganglion cell layer
    BTO_0003398 = "BTO_0003398"
    GANGLION_CELL_LAYER = "BTO_0003398"

    # avian pallium
    BTO_0003399 = "BTO_0003399"
    AVIAN_PALLIUM = "BTO_0003399"

    # hyperpallium
    BTO_0003400 = "BTO_0003400"
    HYPERPALLIUM = "BTO_0003400"

    # subpallium
    BTO_0003401 = "BTO_0003401"
    SUBPALLIUM = "BTO_0003401"

    # hyperpallium apicale
    BTO_0003402 = "BTO_0003402"
    HYPERPALLIUM_APICALE = "BTO_0003402"

    # hyperpallium intercalare
    BTO_0003403 = "BTO_0003403"
    HYPERPALLIUM_INTERCALARE = "BTO_0003403"

    # hyperpallium densocellulare
    BTO_0003404 = "BTO_0003404"
    HYPERPALLIUM_DENSOCELLULARE = "BTO_0003404"

    # mesopallium
    BTO_0003405 = "BTO_0003405"
    MESOPALLIUM = "BTO_0003405"

    # mesopallium dorsale
    BTO_0003406 = "BTO_0003406"
    MESOPALLIUM_DORSALE = "BTO_0003406"

    # mesopallium ventrale
    BTO_0003407 = "BTO_0003407"
    MESOPALLIUM_VENTRALE = "BTO_0003407"

    # arcopallium
    BTO_0003408 = "BTO_0003408"
    ARCOPALLIUM = "BTO_0003408"

    # posterior amygdala
    BTO_0003409 = "BTO_0003409"
    POSTERIOR_AMYGDALA = "BTO_0003409"

    # nucleus taeniae
    BTO_0003410 = "BTO_0003410"
    NUCLEUS_TAENIAE = "BTO_0003410"

    # nucleus isthmo-opticus
    BTO_0003411 = "BTO_0003411"
    NUCLEUS_ISTHMO_OPTICUS = "BTO_0003411"

    # rostral migratory stream
    BTO_0003412 = "BTO_0003412"
    ROSTRAL_MIGRATORY_STREAM = "BTO_0003412"

    # encysting cell
    BTO_0003413 = "BTO_0003413"
    ENCYSTING_CELL = "BTO_0003413"

    # XF-498 cell
    BTO_0003414 = "BTO_0003414"
    XF_498_CELL = "BTO_0003414"

    # conjunctiva
    BTO_0003415 = "BTO_0003415"
    CONJUNCTIVA = "BTO_0003415"

    # culture condition:bovine serum albumin-grown cell
    BTO_0003416 = "BTO_0003416"
    CULTURE_CONDITION_BOVINE_SERUM_ALBUMIN_GROWN_CELL = "BTO_0003416"

    # culture condition:rhodamine B-grown cell
    BTO_0003417 = "BTO_0003417"
    CULTURE_CONDITION_RHODAMINE_B_GROWN_CELL = "BTO_0003417"

    # biceps femoris
    BTO_0003418 = "BTO_0003418"
    BICEPS_FEMORIS = "BTO_0003418"

    # biceps brachii
    BTO_0003419 = "BTO_0003419"
    BICEPS_BRACHII = "BTO_0003419"

    # trophoblast cell line
    BTO_0003420 = "BTO_0003420"
    TROPHOBLAST_CELL_LINE = "BTO_0003420"

    # ACH-3P cell
    BTO_0003421 = "BTO_0003421"
    ACH_3P_CELL = "BTO_0003421"

    # AF5 cell
    BTO_0003422 = "BTO_0003422"
    AF5_CELL = "BTO_0003422"

    # lacrimal gland acinar cell
    BTO_0003423 = "BTO_0003423"
    LACRIMAL_GLAND_ACINAR_CELL = "BTO_0003423"

    # B16F10-Nex2 cell
    BTO_0003424 = "BTO_0003424"
    B16F10_NEX2_CELL = "BTO_0003424"

    # area postrema
    BTO_0003425 = "BTO_0003425"
    AREA_POSTREMA = "BTO_0003425"

    # fourth ventricle
    BTO_0003426 = "BTO_0003426"
    FOURTH_VENTRICLE = "BTO_0003426"

    # Barrett's esophagus
    BTO_0003427 = "BTO_0003427"
    BARRETT_S_ESOPHAGUS = "BTO_0003427"

    # beta-TC6 cell
    BTO_0003428 = "BTO_0003428"
    BETA_TC6_CELL = "BTO_0003428"

    # BIC-1 cell
    BTO_0003429 = "BTO_0003429"
    BIC_1_CELL = "BTO_0003429"

    # SEG-1 cell
    BTO_0003430 = "BTO_0003430"
    SEG_1_CELL = "BTO_0003430"

    # dermatofibroma cell
    BTO_0003431 = "BTO_0003431"
    DERMATOFIBROMA_CELL = "BTO_0003431"

    # EL-4 cell
    BTO_0003432 = "BTO_0003432"
    EL_4_CELL = "BTO_0003432"

    # endometrial gland
    BTO_0003433 = "BTO_0003433"
    ENDOMETRIAL_GLAND = "BTO_0003433"

    # choanomastigote
    BTO_0003434 = "BTO_0003434"
    CHOANOMASTIGOTE = "BTO_0003434"

    # memory T-lymphocyte
    BTO_0003435 = "BTO_0003435"
    MEMORY_T_LYMPHOCYTE = "BTO_0003435"

    # synovial cell line
    BTO_0003436 = "BTO_0003436"
    SYNOVIAL_CELL_LINE = "BTO_0003436"

    # MH7A cell
    BTO_0003437 = "BTO_0003437"
    MH7A_CELL = "BTO_0003437"

    # WM-9 cell
    BTO_0003438 = "BTO_0003438"
    WM_9_CELL = "BTO_0003438"

    # NB-7 cell
    BTO_0003439 = "BTO_0003439"
    NB_7_CELL = "BTO_0003439"

    # COLO-357 cell
    BTO_0003440 = "BTO_0003440"
    COLO_357_CELL = "BTO_0003440"

    # L3.6pl cell
    BTO_0003441 = "BTO_0003441"
    L3_6PL_CELL = "BTO_0003441"

    # CCD-43Sk cell
    BTO_0003442 = "BTO_0003442"
    CCD_43SK_CELL = "BTO_0003442"

    # UACC-893 cell
    BTO_0003443 = "BTO_0003443"
    UACC_893_CELL = "BTO_0003443"

    # HCC-1395 cell
    BTO_0003444 = "BTO_0003444"
    HCC_1395_CELL = "BTO_0003444"

    # carotid atherosclerotic plaque
    BTO_0003445 = "BTO_0003445"
    CAROTID_ATHEROSCLEROTIC_PLAQUE = "BTO_0003445"

    # cholesteatoma tissue
    BTO_0003446 = "BTO_0003446"
    CHOLESTEATOMA_TISSUE = "BTO_0003446"

    # cavum septum pellucidum
    BTO_0003447 = "BTO_0003447"
    CAVUM_SEPTUM_PELLUCIDUM = "BTO_0003447"

    # septum pellucidum
    BTO_0003448 = "BTO_0003448"
    SEPTUM_PELLUCIDUM = "BTO_0003448"

    # AML-12 cell
    BTO_0003449 = "BTO_0003449"
    AML_12_CELL = "BTO_0003449"

    # CHO-6 cell
    BTO_0003450 = "BTO_0003450"
    CHO_6_CELL = "BTO_0003450"

    # C8PA cell
    BTO_0003451 = "BTO_0003451"
    C8PA_CELL = "BTO_0003451"

    # adipocyte cell line
    BTO_0003452 = "BTO_0003452"
    ADIPOCYTE_CELL_LINE = "BTO_0003452"

    # dentin
    BTO_0003453 = "BTO_0003453"
    DENTIN = "BTO_0003453"

    # eosinophilic myelocyte
    BTO_0003454 = "BTO_0003454"
    EOSINOPHILIC_MYELOCYTE = "BTO_0003454"

    # neutrophilic myelocyte
    BTO_0003455 = "BTO_0003455"
    NEUTROPHILIC_MYELOCYTE = "BTO_0003455"

    # basophilic myelocyte
    BTO_0003456 = "BTO_0003456"
    BASOPHILIC_MYELOCYTE = "BTO_0003456"

    # endometrioma cell
    BTO_0003457 = "BTO_0003457"
    ENDOMETRIOMA_CELL = "BTO_0003457"

    # chromophobe renal cell carcinoma cell
    BTO_0003458 = "BTO_0003458"
    CHROMOPHOBE_RENAL_CELL_CARCINOMA_CELL = "BTO_0003458"

    # GC-7 cell
    BTO_0003459 = "BTO_0003459"
    GC_7_CELL = "BTO_0003459"

    # HT-115 cell
    BTO_0003460 = "BTO_0003460"
    HT_115_CELL = "BTO_0003460"

    # HT-1376 cell
    BTO_0003461 = "BTO_0003461"
    HT_1376_CELL = "BTO_0003461"

    # outer dental epithelium
    BTO_0003462 = "BTO_0003462"
    OUTER_DENTAL_EPITHELIUM = "BTO_0003462"

    # inner dental epithelium
    BTO_0003463 = "BTO_0003463"
    INNER_DENTAL_EPITHELIUM = "BTO_0003463"

    # CA-HPV-10 cell
    BTO_0003464 = "BTO_0003464"
    CA_HPV_10_CELL = "BTO_0003464"

    # 293-IL-1RI cell
    BTO_0003465 = "BTO_0003465"
    _293_IL_1RI_CELL = "BTO_0003465"

    # 293-CD40 cell
    BTO_0003466 = "BTO_0003466"
    _293_CD40_CELL = "BTO_0003466"

    # HS-294T cell
    BTO_0003467 = "BTO_0003467"
    HS_294T_CELL = "BTO_0003467"

    # HEK-293B2 cell
    BTO_0003468 = "BTO_0003468"
    HEK_293B2_CELL = "BTO_0003468"

    # HKE-3 cell
    BTO_0003469 = "BTO_0003469"
    HKE_3_CELL = "BTO_0003469"

    # BT-483 cell
    BTO_0003470 = "BTO_0003470"
    BT_483_CELL = "BTO_0003470"

    # MDA-MB-175-VII cell
    BTO_0003471 = "BTO_0003471"
    MDA_MB_175_VII_CELL = "BTO_0003471"

    # vagus nerve
    BTO_0003472 = "BTO_0003472"
    VAGUS_NERVE = "BTO_0003472"

    # polymorphonuclear neutrophil
    BTO_0003473 = "BTO_0003473"
    POLYMORPHONUCLEAR_NEUTROPHIL = "BTO_0003473"

    # WM-239 cell
    BTO_0003474 = "BTO_0003474"
    WM_239_CELL = "BTO_0003474"

    # WM-35 cell
    BTO_0003475 = "BTO_0003475"
    WM_35_CELL = "BTO_0003475"

    # SK-MEL-2 cell
    BTO_0003476 = "BTO_0003476"
    SK_MEL_2_CELL = "BTO_0003476"

    # SK-HEP-1 cell
    BTO_0003477 = "BTO_0003477"
    SK_HEP_1_CELL = "BTO_0003477"

    # SNU-638 cell
    BTO_0003478 = "BTO_0003478"
    SNU_638_CELL = "BTO_0003478"

    # SNU-484 cell
    BTO_0003479 = "BTO_0003479"
    SNU_484_CELL = "BTO_0003479"

    # SNK-57 cell
    BTO_0003480 = "BTO_0003480"
    SNK_57_CELL = "BTO_0003480"

    # NKB-1 cell
    BTO_0003481 = "BTO_0003481"
    NKB_1_CELL = "BTO_0003481"

    # WI-26 cell
    BTO_0003482 = "BTO_0003482"
    WI_26_CELL = "BTO_0003482"

    # sebaceous gland cell line
    BTO_0003483 = "BTO_0003483"
    SEBACEOUS_GLAND_CELL_LINE = "BTO_0003483"

    # SZ-95 cell
    BTO_0003484 = "BTO_0003484"
    SZ_95_CELL = "BTO_0003484"

    # RPAEC cell
    BTO_0003485 = "BTO_0003485"
    RPAEC_CELL = "BTO_0003485"

    # RPMEC cell
    BTO_0003486 = "BTO_0003486"
    RPMEC_CELL = "BTO_0003486"

    # visceral endoderm
    BTO_0003487 = "BTO_0003487"
    VISCERAL_ENDODERM = "BTO_0003487"

    # vibrissa
    BTO_0003488 = "BTO_0003488"
    VIBRISSA = "BTO_0003488"

    # vibrissal follicle
    BTO_0003489 = "BTO_0003489"
    VIBRISSAL_FOLLICLE = "BTO_0003489"

    # vestibulocochlear nerve
    BTO_0003490 = "BTO_0003490"
    VESTIBULOCOCHLEAR_NERVE = "BTO_0003490"

    # SW-1990 cell
    BTO_0003491 = "BTO_0003491"
    SW_1990_CELL = "BTO_0003491"

    # PLC-PRF-5 cell
    BTO_0003492 = "BTO_0003492"
    PLC_PRF_5_CELL = "BTO_0003492"

    # SUIT-2 cell
    BTO_0003493 = "BTO_0003493"
    SUIT_2_CELL = "BTO_0003493"

    # peripheral blood cell
    BTO_0003494 = "BTO_0003494"
    PERIPHERAL_BLOOD_CELL = "BTO_0003494"

    # PDNEC cell
    BTO_0003495 = "BTO_0003495"
    PDNEC_CELL = "BTO_0003495"

    # MDNEC cell
    BTO_0003496 = "BTO_0003496"
    MDNEC_CELL = "BTO_0003496"

    # papillary renal cell carcinoma cell
    BTO_0003497 = "BTO_0003497"
    PAPILLARY_RENAL_CELL_CARCINOMA_CELL = "BTO_0003497"

    # OVISE cell
    BTO_0003498 = "BTO_0003498"
    OVISE_CELL = "BTO_0003498"

    # OVTOKO cell
    BTO_0003499 = "BTO_0003499"
    OVTOKO_CELL = "BTO_0003499"

    # OVMANA cell
    BTO_0003500 = "BTO_0003500"
    OVMANA_CELL = "BTO_0003500"

    # OVSAYO cell
    BTO_0003501 = "BTO_0003501"
    OVSAYO_CELL = "BTO_0003501"

    # OVSAHO cell
    BTO_0003502 = "BTO_0003502"
    OVSAHO_CELL = "BTO_0003502"

    # OVKATE cell
    BTO_0003503 = "BTO_0003503"
    OVKATE_CELL = "BTO_0003503"

    # OV-202 cell
    BTO_0003504 = "BTO_0003504"
    OV_202_CELL = "BTO_0003504"

    # T-cell chronic lymphocytic leukemia cell
    BTO_0003505 = "BTO_0003505"
    T_CELL_CHRONIC_LYMPHOCYTIC_LEUKEMIA_CELL = "BTO_0003505"

    # SAF-1 cell
    BTO_0003506 = "BTO_0003506"
    SAF_1_CELL = "BTO_0003506"

    # tail fin cell line
    BTO_0003507 = "BTO_0003507"
    TAIL_FIN_CELL_LINE = "BTO_0003507"

    # RPMI-7951 cell
    BTO_0003508 = "BTO_0003508"
    RPMI_7951_CELL = "BTO_0003508"

    # headfoot
    BTO_0003509 = "BTO_0003509"
    HEADFOOT = "BTO_0003509"

    # RLE-6TN cell
    BTO_0003510 = "BTO_0003510"
    RLE_6TN_CELL = "BTO_0003510"

    # alveolar epithelium
    BTO_0003511 = "BTO_0003511"
    ALVEOLAR_EPITHELIUM = "BTO_0003511"

    # alveolar epithelial cell line
    BTO_0003512 = "BTO_0003512"
    ALVEOLAR_EPITHELIAL_CELL_LINE = "BTO_0003512"

    # hepatic stellate cell line
    BTO_0003513 = "BTO_0003513"
    HEPATIC_STELLATE_CELL_LINE = "BTO_0003513"

    # HSC-180 cell
    BTO_0003514 = "BTO_0003514"
    HSC_180_CELL = "BTO_0003514"

    # LX-1 cell
    BTO_0003515 = "BTO_0003515"
    LX_1_CELL = "BTO_0003515"

    # LX-2 cell
    BTO_0003516 = "BTO_0003516"
    LX_2_CELL = "BTO_0003516"

    # hTERT-HSC cell
    BTO_0003517 = "BTO_0003517"
    HTERT_HSC_CELL = "BTO_0003517"

    # GREF-X cell
    BTO_0003518 = "BTO_0003518"
    GREF_X_CELL = "BTO_0003518"

    # LI90 cell
    BTO_0003519 = "BTO_0003519"
    LI90_CELL = "BTO_0003519"

    # HSC-T6 cell
    BTO_0003520 = "BTO_0003520"
    HSC_T6_CELL = "BTO_0003520"

    # NFSC cell
    BTO_0003521 = "BTO_0003521"
    NFSC_CELL = "BTO_0003521"

    # CFSC cell
    BTO_0003522 = "BTO_0003522"
    CFSC_CELL = "BTO_0003522"

    # PAV-1 cell
    BTO_0003523 = "BTO_0003523"
    PAV_1_CELL = "BTO_0003523"

    # HSC-PQ cell
    BTO_0003524 = "BTO_0003524"
    HSC_PQ_CELL = "BTO_0003524"

    # BSC cell
    BTO_0003525 = "BTO_0003525"
    BSC_CELL = "BTO_0003525"

    # MFBY2 cell
    BTO_0003526 = "BTO_0003526"
    MFBY2_CELL = "BTO_0003526"

    # T-HSC/Cl-6 cell
    BTO_0003527 = "BTO_0003527"
    T_HSC_CL_6_CELL = "BTO_0003527"

    # GRX cell
    BTO_0003528 = "BTO_0003528"
    GRX_CELL = "BTO_0003528"

    # SV68 c-IS cell
    BTO_0003529 = "BTO_0003529"
    SV68_C_IS_CELL = "BTO_0003529"

    # A640-IS cell
    BTO_0003530 = "BTO_0003530"
    A640_IS_CELL = "BTO_0003530"

    # M1-4HSC cell
    BTO_0003531 = "BTO_0003531"
    M1_4HSC_CELL = "BTO_0003531"

    # A7 cell
    BTO_0003532 = "BTO_0003532"
    A7_CELL = "BTO_0003532"

    # NOR-P1 cell
    BTO_0003533 = "BTO_0003533"
    NOR_P1_CELL = "BTO_0003533"

    # NMB-7 cell
    BTO_0003534 = "BTO_0003534"
    NMB_7_CELL = "BTO_0003534"

    # IMR-6 cell
    BTO_0003535 = "BTO_0003535"
    IMR_6_CELL = "BTO_0003535"

    # NCI-H522 cell
    BTO_0003536 = "BTO_0003536"
    NCI_H522_CELL = "BTO_0003536"

    # MIN6-m9 cell
    BTO_0003537 = "BTO_0003537"
    MIN6_M9_CELL = "BTO_0003537"

    # MIN6-m14 cell
    BTO_0003538 = "BTO_0003538"
    MIN6_M14_CELL = "BTO_0003538"

    # PNT2-C2 cell
    BTO_0003539 = "BTO_0003539"
    PNT2_C2_CELL = "BTO_0003539"

    # P4E6 cell
    BTO_0003540 = "BTO_0003540"
    P4E6_CELL = "BTO_0003540"

    # OE-33 cell
    BTO_0003541 = "BTO_0003541"
    OE_33_CELL = "BTO_0003541"

    # LAN-1 cell
    BTO_0003542 = "BTO_0003542"
    LAN_1_CELL = "BTO_0003542"

    # L-02 cell
    BTO_0003543 = "BTO_0003543"
    L_02_CELL = "BTO_0003543"

    # KU-7 cell
    BTO_0003544 = "BTO_0003544"
    KU_7_CELL = "BTO_0003544"

    # KU-1 cell
    BTO_0003545 = "BTO_0003545"
    KU_1_CELL = "BTO_0003545"

    # KP-N-YN cell
    BTO_0003546 = "BTO_0003546"
    KP_N_YN_CELL = "BTO_0003546"

    # KP-N-SI cell
    BTO_0003547 = "BTO_0003547"
    KP_N_SI_CELL = "BTO_0003547"

    # SMS-KCN cell
    BTO_0003548 = "BTO_0003548"
    SMS_KCN_CELL = "BTO_0003548"

    # KP-1N cell
    BTO_0003549 = "BTO_0003549"
    KP_1N_CELL = "BTO_0003549"

    # KP-2 cell
    BTO_0003550 = "BTO_0003550"
    KP_2_CELL = "BTO_0003550"

    # KP-3 cell
    BTO_0003551 = "BTO_0003551"
    KP_3_CELL = "BTO_0003551"

    # KK-47 cell
    BTO_0003552 = "BTO_0003552"
    KK_47_CELL = "BTO_0003552"

    # EJ-138 cell
    BTO_0003553 = "BTO_0003553"
    EJ_138_CELL = "BTO_0003553"

    # YTS-1 cell
    BTO_0003554 = "BTO_0003554"
    YTS_1_CELL = "BTO_0003554"

    # MBT-2 cell
    BTO_0003555 = "BTO_0003555"
    MBT_2_CELL = "BTO_0003555"

    # SN-56 cell
    BTO_0003556 = "BTO_0003556"
    SN_56_CELL = "BTO_0003556"

    # SN-56/OBR cell
    BTO_0003557 = "BTO_0003557"
    SN_56_OBR_CELL = "BTO_0003557"

    # REC-1 cell
    BTO_0003558 = "BTO_0003558"
    REC_1_CELL = "BTO_0003558"

    # rMC-1 cell
    BTO_0003559 = "BTO_0003559"
    RMC_1_CELL = "BTO_0003559"

    # CCE cell
    BTO_0003560 = "BTO_0003560"
    CCE_CELL = "BTO_0003560"

    # MG1.19 cell
    BTO_0003561 = "BTO_0003561"
    MG1_19_CELL = "BTO_0003561"

    # MB-49 cell
    BTO_0003562 = "BTO_0003562"
    MB_49_CELL = "BTO_0003562"

    # umbilical artery endothelial cell line
    BTO_0003563 = "BTO_0003563"
    UMBILICAL_ARTERY_ENDOTHELIAL_CELL_LINE = "BTO_0003563"

    # HUAEC cell
    BTO_0003564 = "BTO_0003564"
    HUAEC_CELL = "BTO_0003564"

    # HL1C cell
    BTO_0003565 = "BTO_0003565"
    HL1C_CELL = "BTO_0003565"

    # alphaT3-1 cell
    BTO_0003566 = "BTO_0003566"
    ALPHAT3_1_CELL = "BTO_0003566"

    # C-3842 cell
    BTO_0003567 = "BTO_0003567"
    C_3842_CELL = "BTO_0003567"

    # mammary gland cell line
    BTO_0003568 = "BTO_0003568"
    MAMMARY_GLAND_CELL_LINE = "BTO_0003568"

    # C57MG cell
    BTO_0003569 = "BTO_0003569"
    C57MG_CELL = "BTO_0003569"

    # feather bud
    BTO_0003570 = "BTO_0003570"
    FEATHER_BUD = "BTO_0003570"

    # HL-60/MX-2 cell
    BTO_0003571 = "BTO_0003571"
    HL_60_MX_2_CELL = "BTO_0003571"

    # HL60/ADR cell
    BTO_0003572 = "BTO_0003572"
    HL60_ADR_CELL = "BTO_0003572"

    # HL60/DNR cell
    BTO_0003573 = "BTO_0003573"
    HL60_DNR_CELL = "BTO_0003573"

    # HTC-4 cell
    BTO_0003574 = "BTO_0003574"
    HTC_4_CELL = "BTO_0003574"

    # HK-2 cell
    BTO_0003575 = "BTO_0003575"
    HK_2_CELL = "BTO_0003575"

    # renal proximal tubule epithelium
    BTO_0003576 = "BTO_0003576"
    RENAL_PROXIMAL_TUBULE_EPITHELIUM = "BTO_0003576"

    # renal proximal tubule epithelium cell line
    BTO_0003577 = "BTO_0003577"
    RENAL_PROXIMAL_TUBULE_EPITHELIUM_CELL_LINE = "BTO_0003577"

    # gingival cell line
    BTO_0003578 = "BTO_0003578"
    GINGIVAL_CELL_LINE = "BTO_0003578"

    # HGF cell
    BTO_0003579 = "BTO_0003579"
    HGF_CELL = "BTO_0003579"

    # HGEC cell
    BTO_0003580 = "BTO_0003580"
    HGEC_CELL = "BTO_0003580"

    # renal glomerular cell line
    BTO_0003581 = "BTO_0003581"
    RENAL_GLOMERULAR_CELL_LINE = "BTO_0003581"

    # SUP-T1 cell
    BTO_0003582 = "BTO_0003582"
    SUP_T1_CELL = "BTO_0003582"

    # neuroendocrine tumor cell line
    BTO_0003583 = "BTO_0003583"
    NEUROENDOCRINE_TUMOR_CELL_LINE = "BTO_0003583"

    # STC-1 cell
    BTO_0003584 = "BTO_0003584"
    STC_1_CELL = "BTO_0003584"

    # SR cell
    BTO_0003585 = "BTO_0003585"
    SR_CELL = "BTO_0003585"

    # Hep-G2/C3A cell
    BTO_0003586 = "BTO_0003586"
    HEP_G2_C3A_CELL = "BTO_0003586"

    # HeLa-MAGI-CCR5 cell
    BTO_0003587 = "BTO_0003587"
    HELA_MAGI_CCR5_CELL = "BTO_0003587"

    # HeLa-MAGI cell
    BTO_0003588 = "BTO_0003588"
    HELA_MAGI_CELL = "BTO_0003588"

    # GM08505 cell
    BTO_0003589 = "BTO_0003589"
    GM08505_CELL = "BTO_0003589"

    # GM01492 cell
    BTO_0003590 = "BTO_0003590"
    GM01492_CELL = "BTO_0003590"

    # GM00637 cell
    BTO_0003591 = "BTO_0003591"
    GM00637_CELL = "BTO_0003591"

    # GM00037 cell
    BTO_0003592 = "BTO_0003592"
    GM00037_CELL = "BTO_0003592"

    # schizozoite
    BTO_0003593 = "BTO_0003593"
    SCHIZOZOITE = "BTO_0003593"

    # hypnozoite
    BTO_0003594 = "BTO_0003594"
    HYPNOZOITE = "BTO_0003594"

    # knee
    BTO_0003595 = "BTO_0003595"
    KNEE = "BTO_0003595"

    # uterine sarcoma cell
    BTO_0003596 = "BTO_0003596"
    UTERINE_SARCOMA_CELL = "BTO_0003596"

    # uterine leiomyosarcoma cell
    BTO_0003597 = "BTO_0003597"
    UTERINE_LEIOMYOSARCOMA_CELL = "BTO_0003597"

    # uterine endometrial stromal sarcoma cell
    BTO_0003598 = "BTO_0003598"
    UTERINE_ENDOMETRIAL_STROMAL_SARCOMA_CELL = "BTO_0003598"

    # HLMVEC cell
    BTO_0003599 = "BTO_0003599"
    HLMVEC_CELL = "BTO_0003599"

    # M cell
    BTO_0003600 = "BTO_0003600"
    M_CELL = "BTO_0003600"

    # plant hilum
    BTO_0003601 = "BTO_0003601"
    PLANT_HILUM = "BTO_0003601"

    # HeLa GFP-histone H2B cell
    BTO_0003602 = "BTO_0003602"
    HELA_GFP_HISTONE_H2B_CELL = "BTO_0003602"

    # respiratory mucus
    BTO_0003603 = "BTO_0003603"
    RESPIRATORY_MUCUS = "BTO_0003603"

    # renal parenchyma
    BTO_0003604 = "BTO_0003604"
    RENAL_PARENCHYMA = "BTO_0003604"

    # 1321-N1 cell
    BTO_0003605 = "BTO_0003605"
    _1321_N1_CELL = "BTO_0003605"

    # airway fluid
    BTO_0003606 = "BTO_0003606"
    AIRWAY_FLUID = "BTO_0003606"

    # chondroblast
    BTO_0003607 = "BTO_0003607"
    CHONDROBLAST = "BTO_0003607"

    # culture condition:4-amino-3-hydroxybenzoate-grown cell
    BTO_0003608 = "BTO_0003608"
    CULTURE_CONDITION_4_AMINO_3_HYDROXYBENZOATE_GROWN_CELL = "BTO_0003608"

    # culture condition:dicyclopropylketone-grown cell
    BTO_0003609 = "BTO_0003609"
    CULTURE_CONDITION_DICYCLOPROPYLKETONE_GROWN_CELL = "BTO_0003609"

    # culture condition:L-galactonate-grown cell
    BTO_0003610 = "BTO_0003610"
    CULTURE_CONDITION_L_GALACTONATE_GROWN_CELL = "BTO_0003610"

    # culture condition:L-tryptophan-grown cell
    BTO_0003611 = "BTO_0003611"
    CULTURE_CONDITION_L_TRYPTOPHAN_GROWN_CELL = "BTO_0003611"

    # culture condition:n-octane-grown cell
    BTO_0003612 = "BTO_0003612"
    CULTURE_CONDITION_N_OCTANE_GROWN_CELL = "BTO_0003612"

    # lung squamous cell carcinoma cell
    BTO_0003613 = "BTO_0003613"
    LUNG_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0003613"

    # oral squamous cell carcinoma cell
    BTO_0003614 = "BTO_0003614"
    ORAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0003614"

    # HEK-293 PEAKrapid cell
    BTO_0003615 = "BTO_0003615"
    HEK_293_PEAKRAPID_CELL = "BTO_0003615"

    # peritoneal dialysis fluid
    BTO_0003616 = "BTO_0003616"
    PERITONEAL_DIALYSIS_FLUID = "BTO_0003616"

    # peritoneal exudate
    BTO_0003617 = "BTO_0003617"
    PERITONEAL_EXUDATE = "BTO_0003617"

    # HAP-1 cell
    BTO_0003618 = "BTO_0003618"
    HAP_1_CELL = "BTO_0003618"

    # Hi-5 cell
    BTO_0003619 = "BTO_0003619"
    HI_5_CELL = "BTO_0003619"

    # BMMC cell
    BTO_0003620 = "BTO_0003620"
    BMMC_CELL = "BTO_0003620"

    # serosal mast cell
    BTO_0003621 = "BTO_0003621"
    SEROSAL_MAST_CELL = "BTO_0003621"

    # mucosal mast cell
    BTO_0003622 = "BTO_0003622"
    MUCOSAL_MAST_CELL = "BTO_0003622"

    # uterine fluid
    BTO_0003623 = "BTO_0003623"
    UTERINE_FLUID = "BTO_0003623"

    # oronasal squamous cell carcinoma cell
    BTO_0003624 = "BTO_0003624"
    ORONASAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0003624"

    # intervertebral disc
    BTO_0003625 = "BTO_0003625"
    INTERVERTEBRAL_DISC = "BTO_0003625"

    # nucleus pulposus
    BTO_0003626 = "BTO_0003626"
    NUCLEUS_PULPOSUS = "BTO_0003626"

    # annulus fibrosus
    BTO_0003627 = "BTO_0003627"
    ANNULUS_FIBROSUS = "BTO_0003627"

    # annulus fibrosus cordis
    BTO_0003628 = "BTO_0003628"
    ANNULUS_FIBROSUS_CORDIS = "BTO_0003628"

    # annulus fibrosus disci intervertebralis
    BTO_0003629 = "BTO_0003629"
    ANNULUS_FIBROSUS_DISCI_INTERVERTEBRALIS = "BTO_0003629"

    # CT-26 cell
    BTO_0003630 = "BTO_0003630"
    CT_26_CELL = "BTO_0003630"

    # Colon C26-G cell
    BTO_0003631 = "BTO_0003631"
    COLON_C26_G_CELL = "BTO_0003631"

    # cervicovaginal fluid
    BTO_0003632 = "BTO_0003632"
    CERVICOVAGINAL_FLUID = "BTO_0003632"

    # colonic adenoma cell
    BTO_0003633 = "BTO_0003633"
    COLONIC_ADENOMA_CELL = "BTO_0003633"

    # esophageal gland
    BTO_0003634 = "BTO_0003634"
    ESOPHAGEAL_GLAND = "BTO_0003634"

    # esophageal squamous epithelium
    BTO_0003635 = "BTO_0003635"
    ESOPHAGEAL_SQUAMOUS_EPITHELIUM = "BTO_0003635"

    # brain microvascular endothelial cell
    BTO_0003636 = "BTO_0003636"
    BRAIN_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0003636"

    # DG-75 cell
    BTO_0003637 = "BTO_0003637"
    DG_75_CELL = "BTO_0003637"

    # DOV-13 cell
    BTO_0003638 = "BTO_0003638"
    DOV_13_CELL = "BTO_0003638"

    # EJ-1 cell
    BTO_0003639 = "BTO_0003639"
    EJ_1_CELL = "BTO_0003639"

    # esophageal cell line
    BTO_0003640 = "BTO_0003640"
    ESOPHAGEAL_CELL_LINE = "BTO_0003640"

    # FLO-1 cell
    BTO_0003641 = "BTO_0003641"
    FLO_1_CELL = "BTO_0003641"

    # Hca-F cell
    BTO_0003642 = "BTO_0003642"
    HCA_F_CELL = "BTO_0003642"

    # HD-11 cell
    BTO_0003643 = "BTO_0003643"
    HD_11_CELL = "BTO_0003643"

    # metanephric adenoma cell
    BTO_0003644 = "BTO_0003644"
    METANEPHRIC_ADENOMA_CELL = "BTO_0003644"

    # salivary gland tumor cell line
    BTO_0003645 = "BTO_0003645"
    SALIVARY_GLAND_TUMOR_CELL_LINE = "BTO_0003645"

    # pleomorphic adenoma cell
    BTO_0003646 = "BTO_0003646"
    PLEOMORPHIC_ADENOMA_CELL = "BTO_0003646"

    # olfactory tract
    BTO_0003647 = "BTO_0003647"
    OLFACTORY_TRACT = "BTO_0003647"

    # olfactory nerve
    BTO_0003648 = "BTO_0003648"
    OLFACTORY_NERVE = "BTO_0003648"

    # anterior olfactory nucleus
    BTO_0003649 = "BTO_0003649"
    ANTERIOR_OLFACTORY_NUCLEUS = "BTO_0003649"

    # optic ganglion
    BTO_0003650 = "BTO_0003650"
    OPTIC_GANGLION = "BTO_0003650"

    # spindle cell
    BTO_0003651 = "BTO_0003651"
    SPINDLE_CELL = "BTO_0003651"

    # synovial cell
    BTO_0003652 = "BTO_0003652"
    SYNOVIAL_CELL = "BTO_0003652"

    # olfactory glomerulus
    BTO_0003653 = "BTO_0003653"
    OLFACTORY_GLOMERULUS = "BTO_0003653"

    # ventricular zone
    BTO_0003654 = "BTO_0003654"
    VENTRICULAR_ZONE = "BTO_0003654"

    # thyroid cartilage
    BTO_0003655 = "BTO_0003655"
    THYROID_CARTILAGE = "BTO_0003655"

    # adams apple
    BTO_0003656 = "BTO_0003656"
    ADAMS_APPLE = "BTO_0003656"

    # tergal gland
    BTO_0003657 = "BTO_0003657"
    TERGAL_GLAND = "BTO_0003657"

    # tergal gland secretion
    BTO_0003658 = "BTO_0003658"
    TERGAL_GLAND_SECRETION = "BTO_0003658"

    # secretory cell
    BTO_0003659 = "BTO_0003659"
    SECRETORY_CELL = "BTO_0003659"

    # laryngeal cartilage
    BTO_0003660 = "BTO_0003660"
    LARYNGEAL_CARTILAGE = "BTO_0003660"

    # ovary epithelium
    BTO_0003661 = "BTO_0003661"
    OVARY_EPITHELIUM = "BTO_0003661"

    # nucleus recessus lateralis
    BTO_0003662 = "BTO_0003662"
    NUCLEUS_RECESSUS_LATERALIS = "BTO_0003662"

    # nucleus recessus posterioris
    BTO_0003663 = "BTO_0003663"
    NUCLEUS_RECESSUS_POSTERIORIS = "BTO_0003663"

    # nucleus preopticus
    BTO_0003664 = "BTO_0003664"
    NUCLEUS_PREOPTICUS = "BTO_0003664"

    # nucleus recessus preopticus
    BTO_0003665 = "BTO_0003665"
    NUCLEUS_RECESSUS_PREOPTICUS = "BTO_0003665"

    # outer hair cell
    BTO_0003666 = "BTO_0003666"
    OUTER_HAIR_CELL = "BTO_0003666"

    # inner hair cell
    BTO_0003667 = "BTO_0003667"
    INNER_HAIR_CELL = "BTO_0003667"

    # leaf bud
    BTO_0003668 = "BTO_0003668"
    LEAF_BUD = "BTO_0003668"

    # keloid
    BTO_0003669 = "BTO_0003669"
    KELOID = "BTO_0003669"

    # microfilarial stage
    BTO_0003670 = "BTO_0003670"
    MICROFILARIAL_STAGE = "BTO_0003670"

    # germinal center
    BTO_0003671 = "BTO_0003671"
    GERMINAL_CENTER = "BTO_0003671"

    # interdigitating reticulum cell
    BTO_0003672 = "BTO_0003672"
    INTERDIGITATING_RETICULUM_CELL = "BTO_0003672"

    # nephrotome
    BTO_0003673 = "BTO_0003673"
    NEPHROTOME = "BTO_0003673"

    # temporomandibular joint
    BTO_0003674 = "BTO_0003674"
    TEMPOROMANDIBULAR_JOINT = "BTO_0003674"

    # temporomandibular articular disk
    BTO_0003675 = "BTO_0003675"
    TEMPOROMANDIBULAR_ARTICULAR_DISK = "BTO_0003675"

    # lymphoblastic leukemia cell
    BTO_0003676 = "BTO_0003676"
    LYMPHOBLASTIC_LEUKEMIA_CELL = "BTO_0003676"

    # chorion frondosum
    BTO_0003677 = "BTO_0003677"
    CHORION_FRONDOSUM = "BTO_0003677"

    # placental disc
    BTO_0003678 = "BTO_0003678"
    PLACENTAL_DISC = "BTO_0003678"

    # MRK-nu-1 cell
    BTO_0003679 = "BTO_0003679"
    MRK_NU_1_CELL = "BTO_0003679"

    # Mo-B cell
    BTO_0003680 = "BTO_0003680"
    MO_B_CELL = "BTO_0003680"

    # hairy cell leukemia cell line
    BTO_0003681 = "BTO_0003681"
    HAIRY_CELL_LEUKEMIA_CELL_LINE = "BTO_0003681"

    # hairy cell leukemia cell
    BTO_0003682 = "BTO_0003682"
    HAIRY_CELL_LEUKEMIA_CELL = "BTO_0003682"

    # I 9.2 cell
    BTO_0003683 = "BTO_0003683"
    I_9_2_CELL = "BTO_0003683"

    # habenula
    BTO_0003684 = "BTO_0003684"
    HABENULA = "BTO_0003684"

    # habenular nucleus
    BTO_0003685 = "BTO_0003685"
    HABENULAR_NUCLEUS = "BTO_0003685"

    # medial habenular nucleus
    BTO_0003686 = "BTO_0003686"
    MEDIAL_HABENULAR_NUCLEUS = "BTO_0003686"

    # serous cell
    BTO_0003687 = "BTO_0003687"
    SEROUS_CELL = "BTO_0003687"

    # serous acinar cell
    BTO_0003688 = "BTO_0003688"
    SEROUS_ACINAR_CELL = "BTO_0003688"

    # mucous cell
    BTO_0003689 = "BTO_0003689"
    MUCOUS_CELL = "BTO_0003689"

    # mucous acinar cell
    BTO_0003690 = "BTO_0003690"
    MUCOUS_ACINAR_CELL = "BTO_0003690"

    # malignant mixed Muellerian tumor cell
    BTO_0003691 = "BTO_0003691"
    MALIGNANT_MIXED_MUELLERIAN_TUMOR_CELL = "BTO_0003691"

    # prostatic intraepithelial neoplasia cell
    BTO_0003692 = "BTO_0003692"
    PROSTATIC_INTRAEPITHELIAL_NEOPLASIA_CELL = "BTO_0003692"

    # natural killer large granular lymphocytic leukemia cell
    BTO_0003693 = "BTO_0003693"
    NATURAL_KILLER_LARGE_GRANULAR_LYMPHOCYTIC_LEUKEMIA_CELL = "BTO_0003693"

    # CNS cell line
    BTO_0003694 = "BTO_0003694"
    CNS_CELL_LINE = "BTO_0003694"

    # CAD cell
    BTO_0003695 = "BTO_0003695"
    CAD_CELL = "BTO_0003695"

    # ATRkd cell
    BTO_0003696 = "BTO_0003696"
    ATRKD_CELL = "BTO_0003696"

    # endometrial stromal cell
    BTO_0003697 = "BTO_0003697"
    ENDOMETRIAL_STROMAL_CELL = "BTO_0003697"

    # coronary atherosclerotic plaque
    BTO_0003698 = "BTO_0003698"
    CORONARY_ATHEROSCLEROTIC_PLAQUE = "BTO_0003698"

    # C1R cell
    BTO_0003699 = "BTO_0003699"
    C1R_CELL = "BTO_0003699"

    # C1R-B27 cell
    BTO_0003700 = "BTO_0003700"
    C1R_B27_CELL = "BTO_0003700"

    # spinal trigeminal tract
    BTO_0003701 = "BTO_0003701"
    SPINAL_TRIGEMINAL_TRACT = "BTO_0003701"

    # rheumatoid arthritis disease specific synovial tissue
    BTO_0003702 = "BTO_0003702"
    RHEUMATOID_ARTHRITIS_DISEASE_SPECIFIC_SYNOVIAL_TISSUE = "BTO_0003702"

    # rheumatoid arthritis disease specific fibroblast-like synoviocyte
    BTO_0003703 = "BTO_0003703"
    RHEUMATOID_ARTHRITIS_DISEASE_SPECIFIC_FIBROBLAST_LIKE_SYNOVIOCYTE = "BTO_0003703"

    # H4 neuroglioma cell
    BTO_0003704 = "BTO_0003704"
    H4_NEUROGLIOMA_CELL = "BTO_0003704"

    # cornu ammonis
    BTO_0003705 = "BTO_0003705"
    CORNU_AMMONIS = "BTO_0003705"

    # WTK-1 cell
    BTO_0003706 = "BTO_0003706"
    WTK_1_CELL = "BTO_0003706"

    # TK-6 cell
    BTO_0003707 = "BTO_0003707"
    TK_6_CELL = "BTO_0003707"

    # WPMY-1 cell
    BTO_0003708 = "BTO_0003708"
    WPMY_1_CELL = "BTO_0003708"

    # RWPE-1 cell
    BTO_0003709 = "BTO_0003709"
    RWPE_1_CELL = "BTO_0003709"

    # WM-451Lu cell
    BTO_0003710 = "BTO_0003710"
    WM_451LU_CELL = "BTO_0003710"

    # WM-75 cell
    BTO_0003711 = "BTO_0003711"
    WM_75_CELL = "BTO_0003711"

    # WM98-1 cell
    BTO_0003712 = "BTO_0003712"
    WM98_1_CELL = "BTO_0003712"

    # WM-793 cell
    BTO_0003713 = "BTO_0003713"
    WM_793_CELL = "BTO_0003713"

    # VMRC-RCW cell
    BTO_0003714 = "BTO_0003714"
    VMRC_RCW_CELL = "BTO_0003714"

    # VMRC-RCZ cell
    BTO_0003715 = "BTO_0003715"
    VMRC_RCZ_CELL = "BTO_0003715"

    # ScN2a cell
    BTO_0003716 = "BTO_0003716"
    SCN2A_CELL = "BTO_0003716"

    # vesicular gland
    BTO_0003717 = "BTO_0003717"
    VESICULAR_GLAND = "BTO_0003717"

    # vasculature
    BTO_0003718 = "BTO_0003718"
    VASCULATURE = "BTO_0003718"

    # V-79-4 cell
    BTO_0003719 = "BTO_0003719"
    V_79_4_CELL = "BTO_0003719"

    # UT-SCC-9 cell
    BTO_0003720 = "BTO_0003720"
    UT_SCC_9_CELL = "BTO_0003720"

    # UT-SCC-2 cell
    BTO_0003721 = "BTO_0003721"
    UT_SCC_2_CELL = "BTO_0003721"

    # UT-SCC-24A cell
    BTO_0003722 = "BTO_0003722"
    UT_SCC_24A_CELL = "BTO_0003722"

    # UM-UC-3 cell
    BTO_0003723 = "BTO_0003723"
    UM_UC_3_CELL = "BTO_0003723"

    # RT-112 cell
    BTO_0003724 = "BTO_0003724"
    RT_112_CELL = "BTO_0003724"

    # SK-UT-1B cell
    BTO_0003725 = "BTO_0003725"
    SK_UT_1B_CELL = "BTO_0003725"

    # SHP-77 cell
    BTO_0003726 = "BTO_0003726"
    SHP_77_CELL = "BTO_0003726"

    # U-1810 cell
    BTO_0003727 = "BTO_0003727"
    U_1810_CELL = "BTO_0003727"

    # TXM-13 cell
    BTO_0003728 = "BTO_0003728"
    TXM_13_CELL = "BTO_0003728"

    # TUHR-4TKB cell
    BTO_0003729 = "BTO_0003729"
    TUHR_4TKB_CELL = "BTO_0003729"

    # TUHR-14TKB cell
    BTO_0003730 = "BTO_0003730"
    TUHR_14TKB_CELL = "BTO_0003730"

    # RCC-10RGB cell
    BTO_0003731 = "BTO_0003731"
    RCC_10RGB_CELL = "BTO_0003731"

    # TUHR-10TKB cell
    BTO_0003732 = "BTO_0003732"
    TUHR_10TKB_CELL = "BTO_0003732"

    # TUHR-16TKB cell
    BTO_0003733 = "BTO_0003733"
    TUHR_16TKB_CELL = "BTO_0003733"

    # 598-RCC cell
    BTO_0003734 = "BTO_0003734"
    _598_RCC_CELL = "BTO_0003734"

    # TUHR-25TKB cell
    BTO_0003735 = "BTO_0003735"
    TUHR_25TKB_CELL = "BTO_0003735"

    # thyroid epithelial cell
    BTO_0003736 = "BTO_0003736"
    THYROID_EPITHELIAL_CELL = "BTO_0003736"

    # tailbud stage
    BTO_0003737 = "BTO_0003737"
    TAILBUD_STAGE = "BTO_0003737"

    # tenia tecta
    BTO_0003738 = "BTO_0003738"
    TENIA_TECTA = "BTO_0003738"

    # TALL-1 cell
    BTO_0003739 = "BTO_0003739"
    TALL_1_CELL = "BTO_0003739"

    # TALL-104 cell
    BTO_0003740 = "BTO_0003740"
    TALL_104_CELL = "BTO_0003740"

    # T-47 cell
    BTO_0003741 = "BTO_0003741"
    T_47_CELL = "BTO_0003741"

    # synoviocyte
    BTO_0003742 = "BTO_0003742"
    SYNOVIOCYTE = "BTO_0003742"

    # SW-872 cell
    BTO_0003743 = "BTO_0003743"
    SW_872_CELL = "BTO_0003743"

    # liposarcoma cell line
    BTO_0003744 = "BTO_0003744"
    LIPOSARCOMA_CELL_LINE = "BTO_0003744"

    # liposarcoma cell
    BTO_0003745 = "BTO_0003745"
    LIPOSARCOMA_CELL = "BTO_0003745"

    # SW-1398 cell
    BTO_0003746 = "BTO_0003746"
    SW_1398_CELL = "BTO_0003746"

    # superficial temporal artery
    BTO_0003747 = "BTO_0003747"
    SUPERFICIAL_TEMPORAL_ARTERY = "BTO_0003747"

    # superficial temporal vein
    BTO_0003748 = "BTO_0003748"
    SUPERFICIAL_TEMPORAL_VEIN = "BTO_0003748"

    # pars compacta
    BTO_0003749 = "BTO_0003749"
    PARS_COMPACTA = "BTO_0003749"

    # pars reticulata
    BTO_0003750 = "BTO_0003750"
    PARS_RETICULATA = "BTO_0003750"

    # submucosal gland
    BTO_0003751 = "BTO_0003751"
    SUBMUCOSAL_GLAND = "BTO_0003751"

    # lamina epithelialis mucosa
    BTO_0003752 = "BTO_0003752"
    LAMINA_EPITHELIALIS_MUCOSA = "BTO_0003752"

    # central medial thalamic nucleus
    BTO_0003753 = "BTO_0003753"
    CENTRAL_MEDIAL_THALAMIC_NUCLEUS = "BTO_0003753"

    # BRE-169 cell
    BTO_0003754 = "BTO_0003754"
    BRE_169_CELL = "BTO_0003754"

    # STF1-169 cell
    BTO_0003755 = "BTO_0003755"
    STF1_169_CELL = "BTO_0003755"

    # STAV-FCS cell
    BTO_0003756 = "BTO_0003756"
    STAV_FCS_CELL = "BTO_0003756"

    # Vester cell
    BTO_0003757 = "BTO_0003757"
    VESTER_CELL = "BTO_0003757"

    # STAV-AB cell
    BTO_0003758 = "BTO_0003758"
    STAV_AB_CELL = "BTO_0003758"

    # SNUOT-Rb1 cell
    BTO_0003759 = "BTO_0003759"
    SNUOT_RB1_CELL = "BTO_0003759"

    # SNU-182 cell
    BTO_0003760 = "BTO_0003760"
    SNU_182_CELL = "BTO_0003760"

    # SNB-19 cell
    BTO_0003761 = "BTO_0003761"
    SNB_19_CELL = "BTO_0003761"

    # PZ-HPV-7 cell
    BTO_0003762 = "BTO_0003762"
    PZ_HPV_7_CELL = "BTO_0003762"

    # SHAC cell
    BTO_0003763 = "BTO_0003763"
    SHAC_CELL = "BTO_0003763"

    # NCI cell
    BTO_0003764 = "BTO_0003764"
    NCI_CELL = "BTO_0003764"

    # dermatofibroma cell line
    BTO_0003765 = "BTO_0003765"
    DERMATOFIBROMA_CELL_LINE = "BTO_0003765"

    # giant cell tumor cell line
    BTO_0003766 = "BTO_0003766"
    GIANT_CELL_TUMOR_CELL_LINE = "BTO_0003766"

    # A-204 cell
    BTO_0003767 = "BTO_0003767"
    A_204_CELL = "BTO_0003767"

    # A-673 cell
    BTO_0003768 = "BTO_0003768"
    A_673_CELL = "BTO_0003768"

    # A-498 cell
    BTO_0003769 = "BTO_0003769"
    A_498_CELL = "BTO_0003769"

    # A-427 cell
    BTO_0003770 = "BTO_0003770"
    A_427_CELL = "BTO_0003770"

    # T2 cell
    BTO_0003771 = "BTO_0003771"
    T2_CELL = "BTO_0003771"

    # SF-268 cell
    BTO_0003772 = "BTO_0003772"
    SF_268_CELL = "BTO_0003772"

    # oropharyngeal squamous cell carcinoma cell
    BTO_0003773 = "BTO_0003773"
    OROPHARYNGEAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0003773"

    # SCC-25 cell
    BTO_0003774 = "BTO_0003774"
    SCC_25_CELL = "BTO_0003774"

    # SCC-4 cell
    BTO_0003775 = "BTO_0003775"
    SCC_4_CELL = "BTO_0003775"

    # urinary bladder squamous cell carcinoma cell line
    BTO_0003776 = "BTO_0003776"
    URINARY_BLADDER_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0003776"

    # SCaBER cell
    BTO_0003777 = "BTO_0003777"
    SCABER_CELL = "BTO_0003777"

    # SAOS-alpha2beta1 cell
    BTO_0003778 = "BTO_0003778"
    SAOS_ALPHA2BETA1_CELL = "BTO_0003778"

    # RN-46A cell
    BTO_0003779 = "BTO_0003779"
    RN_46A_CELL = "BTO_0003779"

    # RM-1 cell
    BTO_0003780 = "BTO_0003780"
    RM_1_CELL = "BTO_0003780"

    # RCC 786-O cell
    BTO_0003781 = "BTO_0003781"
    RCC_786_O_CELL = "BTO_0003781"

    # rectal adenocarcinoma cell
    BTO_0003782 = "BTO_0003782"
    RECTAL_ADENOCARCINOMA_CELL = "BTO_0003782"

    # rectal adenocarcinoma cell line
    BTO_0003783 = "BTO_0003783"
    RECTAL_ADENOCARCINOMA_CELL_LINE = "BTO_0003783"

    # RCCD-2 cell
    BTO_0003784 = "BTO_0003784"
    RCCD_2_CELL = "BTO_0003784"

    # ray floret
    BTO_0003785 = "BTO_0003785"
    RAY_FLORET = "BTO_0003785"

    # transverse occipital sulcus
    BTO_0003786 = "BTO_0003786"
    TRANSVERSE_OCCIPITAL_SULCUS = "BTO_0003786"

    # intraparietal sulcus
    BTO_0003787 = "BTO_0003787"
    INTRAPARIETAL_SULCUS = "BTO_0003787"

    # splenial gyrus
    BTO_0003788 = "BTO_0003788"
    SPLENIAL_GYRUS = "BTO_0003788"

    # PR-Mel cell
    BTO_0003789 = "BTO_0003789"
    PR_MEL_CELL = "BTO_0003789"

    # MR-Mel cell
    BTO_0003790 = "BTO_0003790"
    MR_MEL_CELL = "BTO_0003790"

    # glandular stomach
    BTO_0003791 = "BTO_0003791"
    GLANDULAR_STOMACH = "BTO_0003791"

    # OV-2008 cell
    BTO_0003792 = "BTO_0003792"
    OV_2008_CELL = "BTO_0003792"

    # pituicyte
    BTO_0003793 = "BTO_0003793"
    PITUICYTE = "BTO_0003793"

    # chlorenchyma
    BTO_0003794 = "BTO_0003794"
    CHLORENCHYMA = "BTO_0003794"

    # periventricular nucleus of hypothalamus
    BTO_0003795 = "BTO_0003795"
    PERIVENTRICULAR_NUCLEUS_OF_HYPOTHALAMUS = "BTO_0003795"

    # periglomerular cell
    BTO_0003796 = "BTO_0003796"
    PERIGLOMERULAR_CELL = "BTO_0003796"

    # unicellular trichome
    BTO_0003797 = "BTO_0003797"
    UNICELLULAR_TRICHOME = "BTO_0003797"

    # multicellular trichome
    BTO_0003798 = "BTO_0003798"
    MULTICELLULAR_TRICHOME = "BTO_0003798"

    # secretory trichome
    BTO_0003799 = "BTO_0003799"
    SECRETORY_TRICHOME = "BTO_0003799"

    # PCCL-3 cell
    BTO_0003800 = "BTO_0003800"
    PCCL_3_CELL = "BTO_0003800"

    # ovum
    BTO_0003801 = "BTO_0003801"
    OVUM = "BTO_0003801"

    # macrogamete
    BTO_0003802 = "BTO_0003802"
    MACROGAMETE = "BTO_0003802"

    # serous adenocarcinoma cell line
    BTO_0003803 = "BTO_0003803"
    SEROUS_ADENOCARCINOMA_CELL_LINE = "BTO_0003803"

    # ovarian serous adenocarcinoma cell line
    BTO_0003804 = "BTO_0003804"
    OVARIAN_SEROUS_ADENOCARCINOMA_CELL_LINE = "BTO_0003804"

    # alpha-motoneuron
    BTO_0003805 = "BTO_0003805"
    ALPHA_MOTONEURON = "BTO_0003805"

    # gamma-motoneuron
    BTO_0003806 = "BTO_0003806"
    GAMMA_MOTONEURON = "BTO_0003806"

    # BJ cell
    BTO_0003807 = "BTO_0003807"
    BJ_CELL = "BTO_0003807"

    # FHC cell
    BTO_0003808 = "BTO_0003808"
    FHC_CELL = "BTO_0003808"

    # soil
    BTO_0003809 = "BTO_0003809"
    SOIL = "BTO_0003809"

    # enrichment culture
    BTO_0003810 = "BTO_0003810"
    ENRICHMENT_CULTURE = "BTO_0003810"

    # interneuron
    BTO_0003811 = "BTO_0003811"
    INTERNEURON = "BTO_0003811"

    # culture condition:tetrahydrofurfuryl alcohol-grown cell
    BTO_0003812 = "BTO_0003812"
    CULTURE_CONDITION_TETRAHYDROFURFURYL_ALCOHOL_GROWN_CELL = "BTO_0003812"

    # culture condition:(4R)-limonene-grown cell
    BTO_0003813 = "BTO_0003813"
    CULTURE_CONDITION__4R__LIMONENE_GROWN_CELL = "BTO_0003813"

    # culture condition:1-butanol-grown cell
    BTO_0003814 = "BTO_0003814"
    CULTURE_CONDITION_1_BUTANOL_GROWN_CELL = "BTO_0003814"

    # culture condition:2-butanol-grown cell
    BTO_0003815 = "BTO_0003815"
    CULTURE_CONDITION_2_BUTANOL_GROWN_CELL = "BTO_0003815"

    # culture condition:benzylamine-grown cell
    BTO_0003816 = "BTO_0003816"
    CULTURE_CONDITION_BENZYLAMINE_GROWN_CELL = "BTO_0003816"

    # culture condition:butane-grown cell
    BTO_0003817 = "BTO_0003817"
    CULTURE_CONDITION_BUTANE_GROWN_CELL = "BTO_0003817"

    # culture condition:DL-lactate-grown cell
    BTO_0003818 = "BTO_0003818"
    CULTURE_CONDITION_DL_LACTATE_GROWN_CELL = "BTO_0003818"

    # culture condition:ethene-grown cell
    BTO_0003819 = "BTO_0003819"
    CULTURE_CONDITION_ETHENE_GROWN_CELL = "BTO_0003819"

    # culture condition:glucose/acetate-grown cell
    BTO_0003820 = "BTO_0003820"
    CULTURE_CONDITION_GLUCOSE_ACETATE_GROWN_CELL = "BTO_0003820"

    # culture condition:glycerol/acetate-grown cell
    BTO_0003821 = "BTO_0003821"
    CULTURE_CONDITION_GLYCEROL_ACETATE_GROWN_CELL = "BTO_0003821"

    # culture condition:maltose-grown cell
    BTO_0003822 = "BTO_0003822"
    CULTURE_CONDITION_MALTOSE_GROWN_CELL = "BTO_0003822"

    # culture condition:monoterpene-grown cell
    BTO_0003823 = "BTO_0003823"
    CULTURE_CONDITION_MONOTERPENE_GROWN_CELL = "BTO_0003823"

    # culture condition:n-butanol-grown cell
    BTO_0003824 = "BTO_0003824"
    CULTURE_CONDITION_N_BUTANOL_GROWN_CELL = "BTO_0003824"

    # neural crest cell
    BTO_0003825 = "BTO_0003825"
    NEURAL_CREST_CELL = "BTO_0003825"

    # culture condition:phenylethylamine-grown cell
    BTO_0003826 = "BTO_0003826"
    CULTURE_CONDITION_PHENYLETHYLAMINE_GROWN_CELL = "BTO_0003826"

    # culture condition:pimelate-grown cell
    BTO_0003827 = "BTO_0003827"
    CULTURE_CONDITION_PIMELATE_GROWN_CELL = "BTO_0003827"

    # culture condition:polyurethane foam-grown cell
    BTO_0003828 = "BTO_0003828"
    CULTURE_CONDITION_POLYURETHANE_FOAM_GROWN_CELL = "BTO_0003828"

    # culture condition:pyruvate-grown cell
    BTO_0003829 = "BTO_0003829"
    CULTURE_CONDITION_PYRUVATE_GROWN_CELL = "BTO_0003829"

    # culture condition:rutin-grown cell
    BTO_0003830 = "BTO_0003830"
    CULTURE_CONDITION_RUTIN_GROWN_CELL = "BTO_0003830"

    # culture condition:vinyl chloride-grown cell
    BTO_0003831 = "BTO_0003831"
    CULTURE_CONDITION_VINYL_CHLORIDE_GROWN_CELL = "BTO_0003831"

    # buccal mucosa
    BTO_0003833 = "BTO_0003833"
    BUCCAL_MUCOSA = "BTO_0003833"

    # conceptus
    BTO_0003834 = "BTO_0003834"
    CONCEPTUS = "BTO_0003834"

    # cerebellar nucleus
    BTO_0003835 = "BTO_0003835"
    CEREBELLAR_NUCLEUS = "BTO_0003835"

    # nucleus dentatus
    BTO_0003836 = "BTO_0003836"
    NUCLEUS_DENTATUS = "BTO_0003836"

    # nucleus emboliformis
    BTO_0003837 = "BTO_0003837"
    NUCLEUS_EMBOLIFORMIS = "BTO_0003837"

    # nucleus globosus
    BTO_0003838 = "BTO_0003838"
    NUCLEUS_GLOBOSUS = "BTO_0003838"

    # nucleus fastigii
    BTO_0003839 = "BTO_0003839"
    NUCLEUS_FASTIGII = "BTO_0003839"

    # cerebrovascular system
    BTO_0003840 = "BTO_0003840"
    CEREBROVASCULAR_SYSTEM = "BTO_0003840"

    # plant organ culture
    BTO_0003841 = "BTO_0003841"
    PLANT_ORGAN_CULTURE = "BTO_0003841"

    # GM02037 cell
    BTO_0003842 = "BTO_0003842"
    GM02037_CELL = "BTO_0003842"

    # FU-01 cell
    BTO_0003843 = "BTO_0003843"
    FU_01_CELL = "BTO_0003843"

    # inferior olivary nucleus
    BTO_0003844 = "BTO_0003844"
    INFERIOR_OLIVARY_NUCLEUS = "BTO_0003844"

    # A2780/CP70 cell
    BTO_0003845 = "BTO_0003845"
    A2780_CP70_CELL = "BTO_0003845"

    # ACHN cell
    BTO_0003846 = "BTO_0003846"
    ACHN_CELL = "BTO_0003846"

    # CRBM-1990 cell
    BTO_0003847 = "BTO_0003847"
    CRBM_1990_CELL = "BTO_0003847"

    # adenoid cystic carcinoma cell
    BTO_0003848 = "BTO_0003848"
    ADENOID_CYSTIC_CARCINOMA_CELL = "BTO_0003848"

    # adenosquamous carcinoma cell
    BTO_0003849 = "BTO_0003849"
    ADENOSQUAMOUS_CARCINOMA_CELL = "BTO_0003849"

    # ALVA-31 cell
    BTO_0003850 = "BTO_0003850"
    ALVA_31_CELL = "BTO_0003850"

    # AOK-B50 cell
    BTO_0003851 = "BTO_0003851"
    AOK_B50_CELL = "BTO_0003851"

    # astroglia
    BTO_0003852 = "BTO_0003852"
    ASTROGLIA = "BTO_0003852"

    # B16-F1 cell
    BTO_0003853 = "BTO_0003853"
    B16_F1_CELL = "BTO_0003853"

    # BL-41 cell
    BTO_0003854 = "BTO_0003854"
    BL_41_CELL = "BTO_0003854"

    # BL-70 cell
    BTO_0003855 = "BTO_0003855"
    BL_70_CELL = "BTO_0003855"

    # BON-1 cell
    BTO_0003856 = "BTO_0003856"
    BON_1_CELL = "BTO_0003856"

    # bone marrow-derived dendritic cell
    BTO_0003857 = "BTO_0003857"
    BONE_MARROW_DERIVED_DENDRITIC_CELL = "BTO_0003857"

    # chondrocyte cell line
    BTO_0003858 = "BTO_0003858"
    CHONDROCYTE_CELL_LINE = "BTO_0003858"

    # C-28/I2 cell
    BTO_0003859 = "BTO_0003859"
    C_28_I2_CELL = "BTO_0003859"

    # T/C-28a2 cell
    BTO_0003860 = "BTO_0003860"
    T_C_28A2_CELL = "BTO_0003860"

    # inflammatory cell
    BTO_0003861 = "BTO_0003861"
    INFLAMMATORY_CELL = "BTO_0003861"

    # CCD-19LU cell
    BTO_0003862 = "BTO_0003862"
    CCD_19LU_CELL = "BTO_0003862"

    # CCF-STTG1 cell
    BTO_0003863 = "BTO_0003863"
    CCF_STTG1_CELL = "BTO_0003863"

    # CMT-93 cell
    BTO_0003864 = "BTO_0003864"
    CMT_93_CELL = "BTO_0003864"

    # enteroendocrine cell
    BTO_0003865 = "BTO_0003865"
    ENTEROENDOCRINE_CELL = "BTO_0003865"

    # APUD cell
    BTO_0003866 = "BTO_0003866"
    APUD_CELL = "BTO_0003866"

    # deutocerebrum
    BTO_0003867 = "BTO_0003867"
    DEUTOCEREBRUM = "BTO_0003867"

    # protocerebrum
    BTO_0003868 = "BTO_0003868"
    PROTOCEREBRUM = "BTO_0003868"

    # tritocerebrum
    BTO_0003869 = "BTO_0003869"
    TRITOCEREBRUM = "BTO_0003869"

    # insect tracheal system
    BTO_0003870 = "BTO_0003870"
    INSECT_TRACHEAL_SYSTEM = "BTO_0003870"

    # uterine endometrial cancer cell
    BTO_0003871 = "BTO_0003871"
    UTERINE_ENDOMETRIAL_CANCER_CELL = "BTO_0003871"

    # foam cell
    BTO_0003872 = "BTO_0003872"
    FOAM_CELL = "BTO_0003872"

    # follicular adenoma cell
    BTO_0003873 = "BTO_0003873"
    FOLLICULAR_ADENOMA_CELL = "BTO_0003873"

    # follicular thyroid cancer cell line
    BTO_0003874 = "BTO_0003874"
    FOLLICULAR_THYROID_CANCER_CELL_LINE = "BTO_0003874"

    # FTC-236 cell
    BTO_0003875 = "BTO_0003875"
    FTC_236_CELL = "BTO_0003875"

    # plant funiculus
    BTO_0003876 = "BTO_0003876"
    PLANT_FUNICULUS = "BTO_0003876"

    # G-292 cell
    BTO_0003877 = "BTO_0003877"
    G_292_CELL = "BTO_0003877"

    # BGC-823 cell
    BTO_0003878 = "BTO_0003878"
    BGC_823_CELL = "BTO_0003878"

    # GBM-8401 cell
    BTO_0003879 = "BTO_0003879"
    GBM_8401_CELL = "BTO_0003879"

    # G9T/VGH cell
    BTO_0003880 = "BTO_0003880"
    G9T_VGH_CELL = "BTO_0003880"

    # HSC-2 cell
    BTO_0003881 = "BTO_0003881"
    HSC_2_CELL = "BTO_0003881"

    # blastocyte
    BTO_0003882 = "BTO_0003882"
    BLASTOCYTE = "BTO_0003882"

    # pancreatic ductal adenocarcinoma cell line
    BTO_0003883 = "BTO_0003883"
    PANCREATIC_DUCTAL_ADENOCARCINOMA_CELL_LINE = "BTO_0003883"

    # HMT-3522 cell
    BTO_0003884 = "BTO_0003884"
    HMT_3522_CELL = "BTO_0003884"

    # Hs-578T cell
    BTO_0003885 = "BTO_0003885"
    HS_578T_CELL = "BTO_0003885"

    # Hs-578Bst cell
    BTO_0003886 = "BTO_0003886"
    HS_578BST_CELL = "BTO_0003886"

    # JHU-022 cell
    BTO_0003887 = "BTO_0003887"
    JHU_022_CELL = "BTO_0003887"

    # JHU-029 cell
    BTO_0003888 = "BTO_0003888"
    JHU_029_CELL = "BTO_0003888"

    # JHU-019 cell
    BTO_0003889 = "BTO_0003889"
    JHU_019_CELL = "BTO_0003889"

    # JHU-013 cell
    BTO_0003890 = "BTO_0003890"
    JHU_013_CELL = "BTO_0003890"

    # JHU-011 cell
    BTO_0003891 = "BTO_0003891"
    JHU_011_CELL = "BTO_0003891"

    # HC-11 cell
    BTO_0003892 = "BTO_0003892"
    HC_11_CELL = "BTO_0003892"

    # HB4a cell
    BTO_0003893 = "BTO_0003893"
    HB4A_CELL = "BTO_0003893"

    # skin carcinoma cell line
    BTO_0003894 = "BTO_0003894"
    SKIN_CARCINOMA_CELL_LINE = "BTO_0003894"

    # HaCa-4 cell
    BTO_0003895 = "BTO_0003895"
    HACA_4_CELL = "BTO_0003895"

    # CarB cell
    BTO_0003896 = "BTO_0003896"
    CARB_CELL = "BTO_0003896"

    # hepatobiliary carcinoma cell
    BTO_0003897 = "BTO_0003897"
    HEPATOBILIARY_CARCINOMA_CELL = "BTO_0003897"

    # GT1 cell
    BTO_0003898 = "BTO_0003898"
    GT1_CELL = "BTO_0003898"

    # GT1-1 cell
    BTO_0003899 = "BTO_0003899"
    GT1_1_CELL = "BTO_0003899"

    # MCF-10F cell
    BTO_0003900 = "BTO_0003900"
    MCF_10F_CELL = "BTO_0003900"

    # 745A cell
    BTO_0003901 = "BTO_0003901"
    _745A_CELL = "BTO_0003901"

    # MEL-745A cl. DS19 cell
    BTO_0003902 = "BTO_0003902"
    MEL_745A_CL__DS19_CELL = "BTO_0003902"

    # HIG-82 cell
    BTO_0003903 = "BTO_0003903"
    HIG_82_CELL = "BTO_0003903"

    # HOS cell
    BTO_0003904 = "BTO_0003904"
    HOS_CELL = "BTO_0003904"

    # HPENC cell
    BTO_0003905 = "BTO_0003905"
    HPENC_CELL = "BTO_0003905"

    # uroepithelium
    BTO_0003906 = "BTO_0003906"
    UROEPITHELIUM = "BTO_0003906"

    # uroepithelial cell line
    BTO_0003907 = "BTO_0003907"
    UROEPITHELIAL_CELL_LINE = "BTO_0003907"

    # HUC-1 cell
    BTO_0003908 = "BTO_0003908"
    HUC_1_CELL = "BTO_0003908"

    # bile duct cell line
    BTO_0003909 = "BTO_0003909"
    BILE_DUCT_CELL_LINE = "BTO_0003909"

    # stellate reticulum
    BTO_0003910 = "BTO_0003910"
    STELLATE_RETICULUM = "BTO_0003910"

    # HuCCT-1 cell
    BTO_0003911 = "BTO_0003911"
    HUCCT_1_CELL = "BTO_0003911"

    # IMCD cell
    BTO_0003912 = "BTO_0003912"
    IMCD_CELL = "BTO_0003912"

    # mIMCD-3 cell
    BTO_0003913 = "BTO_0003913"
    MIMCD_3_CELL = "BTO_0003913"

    # interstitial cell of Cajal
    BTO_0003914 = "BTO_0003914"
    INTERSTITIAL_CELL_OF_CAJAL = "BTO_0003914"

    # hairy root culture
    BTO_0003915 = "BTO_0003915"
    HAIRY_ROOT_CULTURE = "BTO_0003915"

    # plant culture
    BTO_0003916 = "BTO_0003916"
    PLANT_CULTURE = "BTO_0003916"

    # KB-V1 cell
    BTO_0003917 = "BTO_0003917"
    KB_V1_CELL = "BTO_0003917"

    # KB-3-1 cell
    BTO_0003918 = "BTO_0003918"
    KB_3_1_CELL = "BTO_0003918"

    # KB-CH[R]-8-5 cell
    BTO_0003919 = "BTO_0003919"
    KB_CH_R__8_5_CELL = "BTO_0003919"

    # Kc-167 cell
    BTO_0003920 = "BTO_0003920"
    KC_167_CELL = "BTO_0003920"

    # KHOS cell
    BTO_0003921 = "BTO_0003921"
    KHOS_CELL = "BTO_0003921"

    # KHOS/NP (R-970-5) cell
    BTO_0003922 = "BTO_0003922"
    KHOS_NP__R_970_5__CELL = "BTO_0003922"

    # KHOS-240S cell
    BTO_0003923 = "BTO_0003923"
    KHOS_240S_CELL = "BTO_0003923"

    # KHOS-321H cell
    BTO_0003924 = "BTO_0003924"
    KHOS_321H_CELL = "BTO_0003924"

    # renal papilla
    BTO_0003925 = "BTO_0003925"
    RENAL_PAPILLA = "BTO_0003925"

    # renal pyramid
    BTO_0003926 = "BTO_0003926"
    RENAL_PYRAMID = "BTO_0003926"

    # metacercaria
    BTO_0003927 = "BTO_0003927"
    METACERCARIA = "BTO_0003927"

    # Mono-Mac-1 cell
    BTO_0003928 = "BTO_0003928"
    MONO_MAC_1_CELL = "BTO_0003928"

    # MM1-R cell
    BTO_0003929 = "BTO_0003929"
    MM1_R_CELL = "BTO_0003929"

    # ARK-B cell
    BTO_0003930 = "BTO_0003930"
    ARK_B_CELL = "BTO_0003930"

    # ARP-1 cell
    BTO_0003931 = "BTO_0003931"
    ARP_1_CELL = "BTO_0003931"

    # KMS-11 cell
    BTO_0003932 = "BTO_0003932"
    KMS_11_CELL = "BTO_0003932"

    # MM1-S cell
    BTO_0003933 = "BTO_0003933"
    MM1_S_CELL = "BTO_0003933"

    # KKU-100 cell
    BTO_0003934 = "BTO_0003934"
    KKU_100_CELL = "BTO_0003934"

    # L57-3-11 cell
    BTO_0003935 = "BTO_0003935"
    L57_3_11_CELL = "BTO_0003935"

    # laryngeal squamous cell carcinoma cell
    BTO_0003936 = "BTO_0003936"
    LARYNGEAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0003936"

    # lateral septal area
    BTO_0003937 = "BTO_0003937"
    LATERAL_SEPTAL_AREA = "BTO_0003937"

    # leaf disc
    BTO_0003938 = "BTO_0003938"
    LEAF_DISC = "BTO_0003938"

    # luteal cell
    BTO_0003939 = "BTO_0003939"
    LUTEAL_CELL = "BTO_0003939"

    # macula densa
    BTO_0003940 = "BTO_0003940"
    MACULA_DENSA = "BTO_0003940"

    # MDA-MB-435S cell
    BTO_0003941 = "BTO_0003941"
    MDA_MB_435S_CELL = "BTO_0003941"

    # MDAH-2774 cell
    BTO_0003942 = "BTO_0003942"
    MDAH_2774_CELL = "BTO_0003942"

    # SKOV cell
    BTO_0003943 = "BTO_0003943"
    SKOV_CELL = "BTO_0003943"

    # Mel-Ab cell
    BTO_0003944 = "BTO_0003944"
    MEL_AB_CELL = "BTO_0003944"

    # MN-9D cell
    BTO_0003945 = "BTO_0003945"
    MN_9D_CELL = "BTO_0003945"

    # MMDD1 cell
    BTO_0003946 = "BTO_0003946"
    MMDD1_CELL = "BTO_0003946"

    # MPCT-G cell
    BTO_0003947 = "BTO_0003947"
    MPCT_G_CELL = "BTO_0003947"

    # distal tubular epithelium
    BTO_0003948 = "BTO_0003948"
    DISTAL_TUBULAR_EPITHELIUM = "BTO_0003948"

    # distal tubular epithelium cell line
    BTO_0003949 = "BTO_0003949"
    DISTAL_TUBULAR_EPITHELIUM_CELL_LINE = "BTO_0003949"

    # DKC-8 cell
    BTO_0003950 = "BTO_0003950"
    DKC_8_CELL = "BTO_0003950"

    # medial longitudinal fasciculus
    BTO_0003951 = "BTO_0003951"
    MEDIAL_LONGITUDINAL_FASCICULUS = "BTO_0003951"

    # mesenchymal stromal cell
    BTO_0003952 = "BTO_0003952"
    MESENCHYMAL_STROMAL_CELL = "BTO_0003952"

    # mesendoderm
    BTO_0003953 = "BTO_0003953"
    MESENDODERM = "BTO_0003953"

    # dopaminergic system
    BTO_0003954 = "BTO_0003954"
    DOPAMINERGIC_SYSTEM = "BTO_0003954"

    # N-11 cell
    BTO_0003955 = "BTO_0003955"
    N_11_CELL = "BTO_0003955"

    # N-38 cell
    BTO_0003956 = "BTO_0003956"
    N_38_CELL = "BTO_0003956"

    # N-9 cell
    BTO_0003957 = "BTO_0003957"
    N_9_CELL = "BTO_0003957"

    # Neuro2A-Luc cell
    BTO_0003958 = "BTO_0003958"
    NEURO2A_LUC_CELL = "BTO_0003958"

    # NHOK cell
    BTO_0003959 = "BTO_0003959"
    NHOK_CELL = "BTO_0003959"

    # nasopharyngeal carcinoma cell line
    BTO_0003960 = "BTO_0003960"
    NASOPHARYNGEAL_CARCINOMA_CELL_LINE = "BTO_0003960"

    # NPC-TW02 cell
    BTO_0003961 = "BTO_0003961"
    NPC_TW02_CELL = "BTO_0003961"

    # NPC-TW04 cell
    BTO_0003962 = "BTO_0003962"
    NPC_TW04_CELL = "BTO_0003962"

    # nucleus solitarius
    BTO_0003963 = "BTO_0003963"
    NUCLEUS_SOLITARIUS = "BTO_0003963"

    # OECM-1 cell
    BTO_0003964 = "BTO_0003964"
    OECM_1_CELL = "BTO_0003964"

    # anterior olfactory lobule
    BTO_0003965 = "BTO_0003965"
    ANTERIOR_OLFACTORY_LOBULE = "BTO_0003965"

    # posterior olfactory lobule
    BTO_0003966 = "BTO_0003966"
    POSTERIOR_OLFACTORY_LOBULE = "BTO_0003966"

    # OSRGA cell
    BTO_0003967 = "BTO_0003967"
    OSRGA_CELL = "BTO_0003967"

    # OUS-11 cell
    BTO_0003968 = "BTO_0003968"
    OUS_11_CELL = "BTO_0003968"

    # hair follicle outer root sheath
    BTO_0003969 = "BTO_0003969"
    HAIR_FOLLICLE_OUTER_ROOT_SHEATH = "BTO_0003969"

    # outer root sheath companion layer
    BTO_0003970 = "BTO_0003970"
    OUTER_ROOT_SHEATH_COMPANION_LAYER = "BTO_0003970"

    # hair follicle inner root sheath
    BTO_0003971 = "BTO_0003971"
    HAIR_FOLLICLE_INNER_ROOT_SHEATH = "BTO_0003971"

    # prostate gland stromal cell
    BTO_0003972 = "BTO_0003972"
    PROSTATE_GLAND_STROMAL_CELL = "BTO_0003972"

    # pulmonary sclerosing hemangioma cell
    BTO_0003974 = "BTO_0003974"
    PULMONARY_SCLEROSING_HEMANGIOMA_CELL = "BTO_0003974"

    # cingulate cortex
    BTO_0003975 = "BTO_0003975"
    CINGULATE_CORTEX = "BTO_0003975"

    # cingulate gyrus
    BTO_0003976 = "BTO_0003976"
    CINGULATE_GYRUS = "BTO_0003976"

    # retrosplenial region
    BTO_0003977 = "BTO_0003977"
    RETROSPLENIAL_REGION = "BTO_0003977"

    # Brodmann area 29
    BTO_0003978 = "BTO_0003978"
    BRODMANN_AREA_29 = "BTO_0003978"

    # Brodmann area 26
    BTO_0003979 = "BTO_0003979"
    BRODMANN_AREA_26 = "BTO_0003979"

    # SGHPL-4 cell
    BTO_0003980 = "BTO_0003980"
    SGHPL_4_CELL = "BTO_0003980"

    # SAS cell
    BTO_0003981 = "BTO_0003981"
    SAS_CELL = "BTO_0003981"

    # retinal stem cell
    BTO_0003982 = "BTO_0003982"
    RETINAL_STEM_CELL = "BTO_0003982"

    # TXM-18 cell
    BTO_0003983 = "BTO_0003983"
    TXM_18_CELL = "BTO_0003983"

    # A-375P cell
    BTO_0003984 = "BTO_0003984"
    A_375P_CELL = "BTO_0003984"

    # A-375SM cell
    BTO_0003985 = "BTO_0003985"
    A_375SM_CELL = "BTO_0003985"

    # SB-2 cell
    BTO_0003986 = "BTO_0003986"
    SB_2_CELL = "BTO_0003986"

    # root culture
    BTO_0003987 = "BTO_0003987"
    ROOT_CULTURE = "BTO_0003987"

    # DX-3 cell
    BTO_0003988 = "BTO_0003988"
    DX_3_CELL = "BTO_0003988"

    # OV2008/C13 cell
    BTO_0003989 = "BTO_0003989"
    OV2008_C13_CELL = "BTO_0003989"

    # CH12F3-2 cell
    BTO_0003990 = "BTO_0003990"
    CH12F3_2_CELL = "BTO_0003990"

    # pleural mesothelioma cell line
    BTO_0003991 = "BTO_0003991"
    PLEURAL_MESOTHELIOMA_CELL_LINE = "BTO_0003991"

    # ZL-34 cell
    BTO_0003992 = "BTO_0003992"
    ZL_34_CELL = "BTO_0003992"

    # ZP-121 cell
    BTO_0003993 = "BTO_0003993"
    ZP_121_CELL = "BTO_0003993"

    # hoof
    BTO_0003994 = "BTO_0003994"
    HOOF = "BTO_0003994"

    # horny lamina
    BTO_0003995 = "BTO_0003995"
    HORNY_LAMINA = "BTO_0003995"

    # sensitive lamina
    BTO_0003996 = "BTO_0003996"
    SENSITIVE_LAMINA = "BTO_0003996"

    # hoof lamina
    BTO_0003997 = "BTO_0003997"
    HOOF_LAMINA = "BTO_0003997"

    # 41-M cell
    BTO_0003998 = "BTO_0003998"
    _41_M_CELL = "BTO_0003998"

    # M-14-K cell
    BTO_0003999 = "BTO_0003999"
    M_14_K_CELL = "BTO_0003999"

    # M-28-K cell
    BTO_0004000 = "BTO_0004000"
    M_28_K_CELL = "BTO_0004000"

    # M-9-K cell
    BTO_0004001 = "BTO_0004001"
    M_9_K_CELL = "BTO_0004001"

    # HEMn cell
    BTO_0004002 = "BTO_0004002"
    HEMN_CELL = "BTO_0004002"

    # NA cell
    BTO_0004003 = "BTO_0004003"
    NA_CELL = "BTO_0004003"

    # 3-LL cell
    BTO_0004004 = "BTO_0004004"
    _3_LL_CELL = "BTO_0004004"

    # BALB/3T3-T cell
    BTO_0004005 = "BTO_0004005"
    BALB_3T3_T_CELL = "BTO_0004005"

    # OC-3 cell
    BTO_0004006 = "BTO_0004006"
    OC_3_CELL = "BTO_0004006"

    # porcine aortic endothelial cell
    BTO_0004007 = "BTO_0004007"
    PORCINE_AORTIC_ENDOTHELIAL_CELL = "BTO_0004007"

    # medial mammillary nucleus
    BTO_0004008 = "BTO_0004008"
    MEDIAL_MAMMILLARY_NUCLEUS = "BTO_0004008"

    # lateral mammillary nucleus
    BTO_0004009 = "BTO_0004009"
    LATERAL_MAMMILLARY_NUCLEUS = "BTO_0004009"

    # HT-2 cell
    BTO_0004010 = "BTO_0004010"
    HT_2_CELL = "BTO_0004010"

    # PNET-2 cell
    BTO_0004011 = "BTO_0004011"
    PNET_2_CELL = "BTO_0004011"

    # ROS cell
    BTO_0004012 = "BTO_0004012"
    ROS_CELL = "BTO_0004012"

    # Colon-26 cell
    BTO_0004013 = "BTO_0004013"
    COLON_26_CELL = "BTO_0004013"

    # embryonic cerebral cortex
    BTO_0004014 = "BTO_0004014"
    EMBRYONIC_CEREBRAL_CORTEX = "BTO_0004014"

    # HC11-C24 cell
    BTO_0004015 = "BTO_0004015"
    HC11_C24_CELL = "BTO_0004015"

    # laterodorsal tegmental nucleus
    BTO_0004016 = "BTO_0004016"
    LATERODORSAL_TEGMENTAL_NUCLEUS = "BTO_0004016"

    # HCFMK-1 cell
    BTO_0004017 = "BTO_0004017"
    HCFMK_1_CELL = "BTO_0004017"

    # HCTK-1 cell
    BTO_0004018 = "BTO_0004018"
    HCTK_1_CELL = "BTO_0004018"

    # larynx squamous cell carcinoma cell line
    BTO_0004019 = "BTO_0004019"
    LARYNX_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0004019"

    # HLaC-78 cell
    BTO_0004020 = "BTO_0004020"
    HLAC_78_CELL = "BTO_0004020"

    # HLaC-79 cell
    BTO_0004021 = "BTO_0004021"
    HLAC_79_CELL = "BTO_0004021"

    # UM-SCC-17A cell
    BTO_0004022 = "BTO_0004022"
    UM_SCC_17A_CELL = "BTO_0004022"

    # UM-SCC-5 cell
    BTO_0004023 = "BTO_0004023"
    UM_SCC_5_CELL = "BTO_0004023"

    # neural cord
    BTO_0004024 = "BTO_0004024"
    NEURAL_CORD = "BTO_0004024"

    # claw muscle
    BTO_0004025 = "BTO_0004025"
    CLAW_MUSCLE = "BTO_0004025"

    # 4TO7 cell
    BTO_0004026 = "BTO_0004026"
    _4TO7_CELL = "BTO_0004026"

    # 94-H48 cell
    BTO_0004027 = "BTO_0004027"
    _94_H48_CELL = "BTO_0004027"

    # 95-H1 cell
    BTO_0004028 = "BTO_0004028"
    _95_H1_CELL = "BTO_0004028"

    # 94-H4 cell
    BTO_0004029 = "BTO_0004029"
    _94_H4_CELL = "BTO_0004029"

    # 95-H3 cell
    BTO_0004030 = "BTO_0004030"
    _95_H3_CELL = "BTO_0004030"

    # 95-H12 cell
    BTO_0004031 = "BTO_0004031"
    _95_H12_CELL = "BTO_0004031"

    # dopaminergic neuron
    BTO_0004032 = "BTO_0004032"
    DOPAMINERGIC_NEURON = "BTO_0004032"

    # catecholaminergic neuron
    BTO_0004033 = "BTO_0004033"
    CATECHOLAMINERGIC_NEURON = "BTO_0004033"

    # A-224 cell
    BTO_0004034 = "BTO_0004034"
    A_224_CELL = "BTO_0004034"

    # 222 cell
    BTO_0004035 = "BTO_0004035"
    _222_CELL = "BTO_0004035"

    # UCI-107 cell
    BTO_0004036 = "BTO_0004036"
    UCI_107_CELL = "BTO_0004036"

    # A2780/AD10 cell
    BTO_0004037 = "BTO_0004037"
    A2780_AD10_CELL = "BTO_0004037"

    # colonic neoplasm cell
    BTO_0004038 = "BTO_0004038"
    COLONIC_NEOPLASM_CELL = "BTO_0004038"

    # ML-3B cell
    BTO_0004039 = "BTO_0004039"
    ML_3B_CELL = "BTO_0004039"

    # ML-5 cell
    BTO_0004040 = "BTO_0004040"
    ML_5_CELL = "BTO_0004040"

    # abdominal adipose tissue
    BTO_0004041 = "BTO_0004041"
    ABDOMINAL_ADIPOSE_TISSUE = "BTO_0004041"

    # subcutaneous adipose tissue
    BTO_0004042 = "BTO_0004042"
    SUBCUTANEOUS_ADIPOSE_TISSUE = "BTO_0004042"

    # intramuscular adipose tissue
    BTO_0004043 = "BTO_0004043"
    INTRAMUSCULAR_ADIPOSE_TISSUE = "BTO_0004043"

    # amacrine cell
    BTO_0004044 = "BTO_0004044"
    AMACRINE_CELL = "BTO_0004044"

    # air pouch
    BTO_0004045 = "BTO_0004045"
    AIR_POUCH = "BTO_0004045"

    # alveolar mucosa
    BTO_0004046 = "BTO_0004046"
    ALVEOLAR_MUCOSA = "BTO_0004046"

    # apical hook
    BTO_0004047 = "BTO_0004047"
    APICAL_HOOK = "BTO_0004047"

    # aril
    BTO_0004048 = "BTO_0004048"
    ARIL = "BTO_0004048"

    # adult T-cell lymphoma cell line
    BTO_0004049 = "BTO_0004049"
    ADULT_T_CELL_LYMPHOMA_CELL_LINE = "BTO_0004049"

    # BEL-7402 cell
    BTO_0004050 = "BTO_0004050"
    BEL_7402_CELL = "BTO_0004050"

    # bipolar cell
    BTO_0004051 = "BTO_0004051"
    BIPOLAR_CELL = "BTO_0004051"

    # bone marrow stem cell
    BTO_0004052 = "BTO_0004052"
    BONE_MARROW_STEM_CELL = "BTO_0004052"

    # umbilical cord blood
    BTO_0004053 = "BTO_0004053"
    UMBILICAL_CORD_BLOOD = "BTO_0004053"

    # umbilical cord blood cell
    BTO_0004054 = "BTO_0004054"
    UMBILICAL_CORD_BLOOD_CELL = "BTO_0004054"

    # COS cell
    BTO_0004055 = "BTO_0004055"
    COS_CELL = "BTO_0004055"

    # culture condition:lupanine-grown cell
    BTO_0004056 = "BTO_0004056"
    CULTURE_CONDITION_LUPANINE_GROWN_CELL = "BTO_0004056"

    # fruit juice
    BTO_0004057 = "BTO_0004057"
    FRUIT_JUICE = "BTO_0004057"

    # C3H10T1/2 cell
    BTO_0004058 = "BTO_0004058"
    C3H10T1_2_CELL = "BTO_0004058"

    # CCD-18Co cell
    BTO_0004059 = "BTO_0004059"
    CCD_18CO_CELL = "BTO_0004059"

    # fibroblast-like synoviocyte
    BTO_0004060 = "BTO_0004060"
    FIBROBLAST_LIKE_SYNOVIOCYTE = "BTO_0004060"

    # CHL-1 cell
    BTO_0004061 = "BTO_0004061"
    CHL_1_CELL = "BTO_0004061"

    # RPMI-7932 cell
    BTO_0004062 = "BTO_0004062"
    RPMI_7932_CELL = "BTO_0004062"

    # chloragogen cell
    BTO_0004063 = "BTO_0004063"
    CHLORAGOGEN_CELL = "BTO_0004063"

    # chloragocyte
    BTO_0004064 = "BTO_0004064"
    CHLORAGOCYTE = "BTO_0004064"

    # CHO-MG cell
    BTO_0004065 = "BTO_0004065"
    CHO_MG_CELL = "BTO_0004065"

    # CHO-XRS6 cell
    BTO_0004066 = "BTO_0004066"
    CHO_XRS6_CELL = "BTO_0004066"

    # C26-10 cell
    BTO_0004067 = "BTO_0004067"
    C26_10_CELL = "BTO_0004067"

    # C26-A cell
    BTO_0004068 = "BTO_0004068"
    C26_A_CELL = "BTO_0004068"

    # C26-G cell
    BTO_0004069 = "BTO_0004069"
    C26_G_CELL = "BTO_0004069"

    # compost
    BTO_0004070 = "BTO_0004070"
    COMPOST = "BTO_0004070"

    # middle ear squamous cell carcinoma cell
    BTO_0004071 = "BTO_0004071"
    MIDDLE_EAR_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0004071"

    # middle ear squamous cell carcinoma cell line
    BTO_0004072 = "BTO_0004072"
    MIDDLE_EAR_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0004072"

    # CSM14.1 cell
    BTO_0004073 = "BTO_0004073"
    CSM14_1_CELL = "BTO_0004073"

    # cystocyte
    BTO_0004074 = "BTO_0004074"
    CYSTOCYTE = "BTO_0004074"

    # D1-HEK-293 cell
    BTO_0004075 = "BTO_0004075"
    D1_HEK_293_CELL = "BTO_0004075"

    # DHL-4 cell
    BTO_0004076 = "BTO_0004076"
    DHL_4_CELL = "BTO_0004076"

    # EKVX cell
    BTO_0004077 = "BTO_0004077"
    EKVX_CELL = "BTO_0004077"

    # non-small cell lung adenocarcinoma cell line
    BTO_0004078 = "BTO_0004078"
    NON_SMALL_CELL_LUNG_ADENOCARCINOMA_CELL_LINE = "BTO_0004078"

    # H-650 cell
    BTO_0004079 = "BTO_0004079"
    H_650_CELL = "BTO_0004079"

    # HOP-62 cell
    BTO_0004080 = "BTO_0004080"
    HOP_62_CELL = "BTO_0004080"

    # HCC-4006 cell
    BTO_0004081 = "BTO_0004081"
    HCC_4006_CELL = "BTO_0004081"

    # HCC-827 cell
    BTO_0004082 = "BTO_0004082"
    HCC_827_CELL = "BTO_0004082"

    # HCC-2935 cell
    BTO_0004083 = "BTO_0004083"
    HCC_2935_CELL = "BTO_0004083"

    # epitrochlearis muscle
    BTO_0004084 = "BTO_0004084"
    EPITROCHLEARIS_MUSCLE = "BTO_0004084"

    # HOP-92 cell
    BTO_0004085 = "BTO_0004085"
    HOP_92_CELL = "BTO_0004085"

    # mammary gland tumor cell line
    BTO_0004086 = "BTO_0004086"
    MAMMARY_GLAND_TUMOR_CELL_LINE = "BTO_0004086"

    # mammary gland tumor cell
    BTO_0004087 = "BTO_0004087"
    MAMMARY_GLAND_TUMOR_CELL = "BTO_0004087"

    # female urethra
    BTO_0004088 = "BTO_0004088"
    FEMALE_URETHRA = "BTO_0004088"

    # male urethra
    BTO_0004089 = "BTO_0004089"
    MALE_URETHRA = "BTO_0004089"

    # pancreatic invasive ductal adenocarcinoma cell
    BTO_0004090 = "BTO_0004090"
    PANCREATIC_INVASIVE_DUCTAL_ADENOCARCINOMA_CELL = "BTO_0004090"

    # embryonic neural stem cell
    BTO_0004091 = "BTO_0004091"
    EMBRYONIC_NEURAL_STEM_CELL = "BTO_0004091"

    # endogenous progenitor cell
    BTO_0004092 = "BTO_0004092"
    ENDOGENOUS_PROGENITOR_CELL = "BTO_0004092"

    # endothelial progenitor cell
    BTO_0004093 = "BTO_0004093"
    ENDOTHELIAL_PROGENITOR_CELL = "BTO_0004093"

    # epithelial ovarian cancer cell
    BTO_0004094 = "BTO_0004094"
    EPITHELIAL_OVARIAN_CANCER_CELL = "BTO_0004094"

    # EONT cell
    BTO_0004095 = "BTO_0004095"
    EONT_CELL = "BTO_0004095"

    # coronary artery endothelial cell
    BTO_0004096 = "BTO_0004096"
    CORONARY_ARTERY_ENDOTHELIAL_CELL = "BTO_0004096"

    # epididymal clear cell
    BTO_0004097 = "BTO_0004097"
    EPIDIDYMAL_CLEAR_CELL = "BTO_0004097"

    # renal clear cell
    BTO_0004098 = "BTO_0004098"
    RENAL_CLEAR_CELL = "BTO_0004098"

    # parathyroid gland clear cell
    BTO_0004099 = "BTO_0004099"
    PARATHYROID_GLAND_CLEAR_CELL = "BTO_0004099"

    # sweat gland clear cell
    BTO_0004100 = "BTO_0004100"
    SWEAT_GLAND_CLEAR_CELL = "BTO_0004100"

    # fascicle
    BTO_0004101 = "BTO_0004101"
    FASCICLE = "BTO_0004101"

    # cerebral cortical neuron
    BTO_0004102 = "BTO_0004102"
    CEREBRAL_CORTICAL_NEURON = "BTO_0004102"

    # leaf primordium
    BTO_0004103 = "BTO_0004103"
    LEAF_PRIMORDIUM = "BTO_0004103"

    # insect labium
    BTO_0004104 = "BTO_0004104"
    INSECT_LABIUM = "BTO_0004104"

    # FPMI-CF-203 cell
    BTO_0004105 = "BTO_0004105"
    FPMI_CF_203_CELL = "BTO_0004105"

    # IPRI-MD-66 cell
    BTO_0004106 = "BTO_0004106"
    IPRI_MD_66_CELL = "BTO_0004106"

    # antral mucosa
    BTO_0004107 = "BTO_0004107"
    ANTRAL_MUCOSA = "BTO_0004107"

    # G cell
    BTO_0004108 = "BTO_0004108"
    G_CELL = "BTO_0004108"

    # fundic mucosa
    BTO_0004109 = "BTO_0004109"
    FUNDIC_MUCOSA = "BTO_0004109"

    # pyloric mucosa
    BTO_0004110 = "BTO_0004110"
    PYLORIC_MUCOSA = "BTO_0004110"

    # gastrointestinal stromal tumor cell
    BTO_0004111 = "BTO_0004111"
    GASTROINTESTINAL_STROMAL_TUMOR_CELL = "BTO_0004111"

    # GBC-SD cell
    BTO_0004112 = "BTO_0004112"
    GBC_SD_CELL = "BTO_0004112"

    # GLC-82 cell
    BTO_0004113 = "BTO_0004113"
    GLC_82_CELL = "BTO_0004113"

    # adrenocortical carcinoma cell line
    BTO_0004114 = "BTO_0004114"
    ADRENOCORTICAL_CARCINOMA_CELL_LINE = "BTO_0004114"

    # HAC cell
    BTO_0004115 = "BTO_0004115"
    HAC_CELL = "BTO_0004115"

    # HEP-3B2 cell
    BTO_0004116 = "BTO_0004116"
    HEP_3B2_CELL = "BTO_0004116"

    # HFK cell
    BTO_0004117 = "BTO_0004117"
    HFK_CELL = "BTO_0004117"

    # HITC6 cell
    BTO_0004118 = "BTO_0004118"
    HITC6_CELL = "BTO_0004118"

    # HL-60 (TB) cell
    BTO_0004119 = "BTO_0004119"
    HL_60__TB__CELL = "BTO_0004119"

    # horizontal cell
    BTO_0004120 = "BTO_0004120"
    HORIZONTAL_CELL = "BTO_0004120"

    # HPAC cell
    BTO_0004121 = "BTO_0004121"
    HPAC_CELL = "BTO_0004121"

    # bone marrow stromal cell
    BTO_0004122 = "BTO_0004122"
    BONE_MARROW_STROMAL_CELL = "BTO_0004122"

    # HS-5 cell
    BTO_0004123 = "BTO_0004123"
    HS_5_CELL = "BTO_0004123"

    # HT-1197 cell
    BTO_0004124 = "BTO_0004124"
    HT_1197_CELL = "BTO_0004124"

    # HTR-8/SVneo cell
    BTO_0004125 = "BTO_0004125"
    HTR_8_SVNEO_CELL = "BTO_0004125"

    # Huh-7.5 cell
    BTO_0004126 = "BTO_0004126"
    HUH_7_5_CELL = "BTO_0004126"

    # Huma-7 cell
    BTO_0004127 = "BTO_0004127"
    HUMA_7_CELL = "BTO_0004127"

    # lung endothelium
    BTO_0004128 = "BTO_0004128"
    LUNG_ENDOTHELIUM = "BTO_0004128"

    # ovary epithelium cell line
    BTO_0004129 = "BTO_0004129"
    OVARY_EPITHELIUM_CELL_LINE = "BTO_0004129"

    # IOSE cell
    BTO_0004130 = "BTO_0004130"
    IOSE_CELL = "BTO_0004130"

    # IOSE-397 cell
    BTO_0004131 = "BTO_0004131"
    IOSE_397_CELL = "BTO_0004131"

    # IOSE-29 cell
    BTO_0004132 = "BTO_0004132"
    IOSE_29_CELL = "BTO_0004132"

    # IOSE-4p2 cell
    BTO_0004133 = "BTO_0004133"
    IOSE_4P2_CELL = "BTO_0004133"

    # IOSE-2Ap2 cell
    BTO_0004134 = "BTO_0004134"
    IOSE_2AP2_CELL = "BTO_0004134"

    # IOSE-398 cell
    BTO_0004135 = "BTO_0004135"
    IOSE_398_CELL = "BTO_0004135"

    # Kasumi-1 cell
    BTO_0004136 = "BTO_0004136"
    KASUMI_1_CELL = "BTO_0004136"

    # KCL-22 cell
    BTO_0004137 = "BTO_0004137"
    KCL_22_CELL = "BTO_0004137"

    # gingival fibroblast
    BTO_0004138 = "BTO_0004138"
    GINGIVAL_FIBROBLAST = "BTO_0004138"

    # LAD-2 cell
    BTO_0004139 = "BTO_0004139"
    LAD_2_CELL = "BTO_0004139"

    # ethmoid bone
    BTO_0004140 = "BTO_0004140"
    ETHMOID_BONE = "BTO_0004140"

    # cribriform plate
    BTO_0004141 = "BTO_0004141"
    CRIBRIFORM_PLATE = "BTO_0004141"

    # LH-86 cell
    BTO_0004142 = "BTO_0004142"
    LH_86_CELL = "BTO_0004142"

    # Lovo-175X2 cell
    BTO_0004143 = "BTO_0004143"
    LOVO_175X2_CELL = "BTO_0004143"

    # Lovo-273X17 cell
    BTO_0004144 = "BTO_0004144"
    LOVO_273X17_CELL = "BTO_0004144"

    # Lovo-li cell
    BTO_0004145 = "BTO_0004145"
    LOVO_LI_CELL = "BTO_0004145"

    # Lovo-92 cell
    BTO_0004146 = "BTO_0004146"
    LOVO_92_CELL = "BTO_0004146"

    # lumbar spine
    BTO_0004147 = "BTO_0004147"
    LUMBAR_SPINE = "BTO_0004147"

    # cervical spine
    BTO_0004148 = "BTO_0004148"
    CERVICAL_SPINE = "BTO_0004148"

    # ischial spine
    BTO_0004149 = "BTO_0004149"
    ISCHIAL_SPINE = "BTO_0004149"

    # thoracic spine
    BTO_0004150 = "BTO_0004150"
    THORACIC_SPINE = "BTO_0004150"

    # LOX-IMVI cell
    BTO_0004151 = "BTO_0004151"
    LOX_IMVI_CELL = "BTO_0004151"

    # UACC-62 cell
    BTO_0004152 = "BTO_0004152"
    UACC_62_CELL = "BTO_0004152"

    # KT-2 cell
    BTO_0004153 = "BTO_0004153"
    KT_2_CELL = "BTO_0004153"

    # KT-4 cell
    BTO_0004154 = "BTO_0004154"
    KT_4_CELL = "BTO_0004154"

    # Ma-25 cell
    BTO_0004155 = "BTO_0004155"
    MA_25_CELL = "BTO_0004155"

    # Ma-31 cell
    BTO_0004156 = "BTO_0004156"
    MA_31_CELL = "BTO_0004156"

    # Ma-34 cell
    BTO_0004157 = "BTO_0004157"
    MA_34_CELL = "BTO_0004157"

    # Ma-45 cell
    BTO_0004158 = "BTO_0004158"
    MA_45_CELL = "BTO_0004158"

    # Ma-53 cell
    BTO_0004159 = "BTO_0004159"
    MA_53_CELL = "BTO_0004159"

    # Ma-1 cell
    BTO_0004160 = "BTO_0004160"
    MA_1_CELL = "BTO_0004160"

    # MALME-3 cell
    BTO_0004161 = "BTO_0004161"
    MALME_3_CELL = "BTO_0004161"

    # MALME-3M cell
    BTO_0004162 = "BTO_0004162"
    MALME_3M_CELL = "BTO_0004162"

    # MC-38 cell
    BTO_0004163 = "BTO_0004163"
    MC_38_CELL = "BTO_0004163"

    # MDA-MB-435HGF cell
    BTO_0004164 = "BTO_0004164"
    MDA_MB_435HGF_CELL = "BTO_0004164"

    # meibomian gland
    BTO_0004165 = "BTO_0004165"
    MEIBOMIAN_GLAND = "BTO_0004165"

    # myofibroblast cell line
    BTO_0004166 = "BTO_0004166"
    MYOFIBROBLAST_CELL_LINE = "BTO_0004166"

    # lymphatic endothelial cell
    BTO_0004167 = "BTO_0004167"
    LYMPHATIC_ENDOTHELIAL_CELL = "BTO_0004167"

    # MHCC-97 cell
    BTO_0004168 = "BTO_0004168"
    MHCC_97_CELL = "BTO_0004168"

    # MHCC97-H cell
    BTO_0004169 = "BTO_0004169"
    MHCC97_H_CELL = "BTO_0004169"

    # MHCC97-L cell
    BTO_0004170 = "BTO_0004170"
    MHCC97_L_CELL = "BTO_0004170"

    # MOLT-13 cell
    BTO_0004171 = "BTO_0004171"
    MOLT_13_CELL = "BTO_0004171"

    # MOLT-14 cell
    BTO_0004172 = "BTO_0004172"
    MOLT_14_CELL = "BTO_0004172"

    # MOLT-16 cell
    BTO_0004173 = "BTO_0004173"
    MOLT_16_CELL = "BTO_0004173"

    # MOLT-17 cell
    BTO_0004174 = "BTO_0004174"
    MOLT_17_CELL = "BTO_0004174"

    # MOLM-13 cell
    BTO_0004175 = "BTO_0004175"
    MOLM_13_CELL = "BTO_0004175"

    # MOLM-16 cell
    BTO_0004176 = "BTO_0004176"
    MOLM_16_CELL = "BTO_0004176"

    # MOLM-6 cell
    BTO_0004177 = "BTO_0004177"
    MOLM_6_CELL = "BTO_0004177"

    # leukemic stem cell
    BTO_0004178 = "BTO_0004178"
    LEUKEMIC_STEM_CELL = "BTO_0004178"

    # MX-1 cell
    BTO_0004179 = "BTO_0004179"
    MX_1_CELL = "BTO_0004179"

    # NCCIT cell
    BTO_0004180 = "BTO_0004180"
    NCCIT_CELL = "BTO_0004180"

    # NCI/ADR-RES cell
    BTO_0004181 = "BTO_0004181"
    NCI_ADR_RES_CELL = "BTO_0004181"

    # NCI-H322M cell
    BTO_0004182 = "BTO_0004182"
    NCI_H322M_CELL = "BTO_0004182"

    # NMuMg cell
    BTO_0004183 = "BTO_0004183"
    NMUMG_CELL = "BTO_0004183"

    # OKM-2T cell
    BTO_0004184 = "BTO_0004184"
    OKM_2T_CELL = "BTO_0004184"

    # olfactory receptor neuron
    BTO_0004185 = "BTO_0004185"
    OLFACTORY_RECEPTOR_NEURON = "BTO_0004185"

    # DuPro cell
    BTO_0004186 = "BTO_0004186"
    DUPRO_CELL = "BTO_0004186"

    # NRK-E52 cell
    BTO_0004187 = "BTO_0004187"
    NRK_E52_CELL = "BTO_0004187"

    # ECRF cell
    BTO_0004188 = "BTO_0004188"
    ECRF_CELL = "BTO_0004188"

    # NCI/ADR cell
    BTO_0004189 = "BTO_0004189"
    NCI_ADR_CELL = "BTO_0004189"

    # pacemaker cell
    BTO_0004190 = "BTO_0004190"
    PACEMAKER_CELL = "BTO_0004190"

    # PC-J cell
    BTO_0004191 = "BTO_0004191"
    PC_J_CELL = "BTO_0004191"

    # perineuronal net
    BTO_0004192 = "BTO_0004192"
    PERINEURONAL_NET = "BTO_0004192"

    # pharyngeal pad
    BTO_0004193 = "BTO_0004193"
    PHARYNGEAL_PAD = "BTO_0004193"

    # pharyngeal process
    BTO_0004194 = "BTO_0004194"
    PHARYNGEAL_PROCESS = "BTO_0004194"

    # pharyngeal organ
    BTO_0004195 = "BTO_0004195"
    PHARYNGEAL_ORGAN = "BTO_0004195"

    # placental membrane
    BTO_0004196 = "BTO_0004196"
    PLACENTAL_MEMBRANE = "BTO_0004196"

    # insect labellum
    BTO_0004197 = "BTO_0004197"
    INSECT_LABELLUM = "BTO_0004197"

    # prostomium
    BTO_0004198 = "BTO_0004198"
    PROSTOMIUM = "BTO_0004198"

    # substantia nigra cell line
    BTO_0004199 = "BTO_0004199"
    SUBSTANTIA_NIGRA_CELL_LINE = "BTO_0004199"

    # RCSN-3 cell
    BTO_0004200 = "BTO_0004200"
    RCSN_3_CELL = "BTO_0004200"

    # Ewing's sarcoma cell line
    BTO_0004201 = "BTO_0004201"
    EWING_S_SARCOMA_CELL_LINE = "BTO_0004201"

    # RD-ES cell
    BTO_0004202 = "BTO_0004202"
    RD_ES_CELL = "BTO_0004202"

    # RIE-1 cell
    BTO_0004203 = "BTO_0004203"
    RIE_1_CELL = "BTO_0004203"

    # nasal squamous cell carcinoma cell line
    BTO_0004204 = "BTO_0004204"
    NASAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0004204"

    # RPMI-2650 cell
    BTO_0004205 = "BTO_0004205"
    RPMI_2650_CELL = "BTO_0004205"

    # RPMI-8866 cell
    BTO_0004206 = "BTO_0004206"
    RPMI_8866_CELL = "BTO_0004206"

    # RXF-393 cell
    BTO_0004207 = "BTO_0004207"
    RXF_393_CELL = "BTO_0004207"

    # SB-247 cell
    BTO_0004208 = "BTO_0004208"
    SB_247_CELL = "BTO_0004208"

    # seed vessel
    BTO_0004209 = "BTO_0004209"
    SEED_VESSEL = "BTO_0004209"

    # seminoma cell
    BTO_0004210 = "BTO_0004210"
    SEMINOMA_CELL = "BTO_0004210"

    # sensillum trichodeum
    BTO_0004211 = "BTO_0004211"
    SENSILLUM_TRICHODEUM = "BTO_0004211"

    # seta
    BTO_0004212 = "BTO_0004212"
    SETA = "BTO_0004212"

    # SF-295 cell
    BTO_0004213 = "BTO_0004213"
    SF_295_CELL = "BTO_0004213"

    # SF-539 cell
    BTO_0004214 = "BTO_0004214"
    SF_539_CELL = "BTO_0004214"

    # SF-763 cell
    BTO_0004215 = "BTO_0004215"
    SF_763_CELL = "BTO_0004215"

    # SJSA-1 cell
    BTO_0004216 = "BTO_0004216"
    SJSA_1_CELL = "BTO_0004216"

    # SK-N-DZ cell
    BTO_0004217 = "BTO_0004217"
    SK_N_DZ_CELL = "BTO_0004217"

    # SK-N-FI cell
    BTO_0004218 = "BTO_0004218"
    SK_N_FI_CELL = "BTO_0004218"

    # submandibular gland cell line
    BTO_0004219 = "BTO_0004219"
    SUBMANDIBULAR_GLAND_CELL_LINE = "BTO_0004219"

    # SMG-C6 cell
    BTO_0004220 = "BTO_0004220"
    SMG_C6_CELL = "BTO_0004220"

    # SN-12C cell
    BTO_0004221 = "BTO_0004221"
    SN_12C_CELL = "BTO_0004221"

    # SNB-75 cell
    BTO_0004222 = "BTO_0004222"
    SNB_75_CELL = "BTO_0004222"

    # cervical squamous cell carcinoma cell
    BTO_0004223 = "BTO_0004223"
    CERVICAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0004223"

    # stomodeum
    BTO_0004224 = "BTO_0004224"
    STOMODEUM = "BTO_0004224"

    # striatal neuron
    BTO_0004225 = "BTO_0004225"
    STRIATAL_NEURON = "BTO_0004225"

    # TAMH cell
    BTO_0004226 = "BTO_0004226"
    TAMH_CELL = "BTO_0004226"

    # TC-32 cell
    BTO_0004227 = "BTO_0004227"
    TC_32_CELL = "BTO_0004227"

    # thymus lymphoma cell
    BTO_0004228 = "BTO_0004228"
    THYMUS_LYMPHOMA_CELL = "BTO_0004228"

    # testicular cell line
    BTO_0004229 = "BTO_0004229"
    TESTICULAR_CELL_LINE = "BTO_0004229"

    # TM-4 cell
    BTO_0004230 = "BTO_0004230"
    TM_4_CELL = "BTO_0004230"

    # TCMK-1 cell
    BTO_0004231 = "BTO_0004231"
    TCMK_1_CELL = "BTO_0004231"

    # tsA-201 cell
    BTO_0004232 = "BTO_0004232"
    TSA_201_CELL = "BTO_0004232"

    # UACC-257 cell
    BTO_0004233 = "BTO_0004233"
    UACC_257_CELL = "BTO_0004233"

    # UO-31 cell
    BTO_0004234 = "BTO_0004234"
    UO_31_CELL = "BTO_0004234"

    # uterine horn
    BTO_0004235 = "BTO_0004235"
    UTERINE_HORN = "BTO_0004235"

    # Y1-BS1 cell
    BTO_0004236 = "BTO_0004236"
    Y1_BS1_CELL = "BTO_0004236"

    # myometrial cell line
    BTO_0004237 = "BTO_0004237"
    MYOMETRIAL_CELL_LINE = "BTO_0004237"

    # interstitial cell
    BTO_0004238 = "BTO_0004238"
    INTERSTITIAL_CELL = "BTO_0004238"

    # ovarian theca-interstitial cell
    BTO_0004239 = "BTO_0004239"
    OVARIAN_THECA_INTERSTITIAL_CELL = "BTO_0004239"

    # germarium
    BTO_0004240 = "BTO_0004240"
    GERMARIUM = "BTO_0004240"

    # ovariole
    BTO_0004241 = "BTO_0004241"
    OVARIOLE = "BTO_0004241"

    # vitellarium
    BTO_0004242 = "BTO_0004242"
    VITELLARIUM = "BTO_0004242"

    # trypanosomoid cell line
    BTO_0004243 = "BTO_0004243"
    TRYPANOSOMOID_CELL_LINE = "BTO_0004243"

    # 449 cell
    BTO_0004244 = "BTO_0004244"
    _449_CELL = "BTO_0004244"

    # NIH-3T3-A14 cell
    BTO_0004245 = "BTO_0004245"
    NIH_3T3_A14_CELL = "BTO_0004245"

    # A-364 cell
    BTO_0004246 = "BTO_0004246"
    A_364_CELL = "BTO_0004246"

    # A-547 cell
    BTO_0004247 = "BTO_0004247"
    A_547_CELL = "BTO_0004247"

    # Xenopus A6 cell
    BTO_0004248 = "BTO_0004248"
    XENOPUS_A6_CELL = "BTO_0004248"

    # anterior cingulate cortex
    BTO_0004249 = "BTO_0004249"
    ANTERIOR_CINGULATE_CORTEX = "BTO_0004249"

    # posterior cingulate cortex
    BTO_0004250 = "BTO_0004250"
    POSTERIOR_CINGULATE_CORTEX = "BTO_0004250"

    # Hepa-1c1c7-c12 cell
    BTO_0004251 = "BTO_0004251"
    HEPA_1C1C7_C12_CELL = "BTO_0004251"

    # Hepa-1c1c7-c4 cell
    BTO_0004252 = "BTO_0004252"
    HEPA_1C1C7_C4_CELL = "BTO_0004252"

    # plant candle
    BTO_0004253 = "BTO_0004253"
    PLANT_CANDLE = "BTO_0004253"

    # cancer stem cell
    BTO_0004254 = "BTO_0004254"
    CANCER_STEM_CELL = "BTO_0004254"

    # Ewing's family tumor cell
    BTO_0004255 = "BTO_0004255"
    EWING_S_FAMILY_TUMOR_CELL = "BTO_0004255"

    # long bone
    BTO_0004256 = "BTO_0004256"
    LONG_BONE = "BTO_0004256"

    # extraosseus Ewing's sarcoma cell
    BTO_0004257 = "BTO_0004257"
    EXTRAOSSEUS_EWING_S_SARCOMA_CELL = "BTO_0004257"

    # primitive neuroectodermal tumor cell
    BTO_0004258 = "BTO_0004258"
    PRIMITIVE_NEUROECTODERMAL_TUMOR_CELL = "BTO_0004258"

    # primitive neuroectodermal tumor cell line
    BTO_0004259 = "BTO_0004259"
    PRIMITIVE_NEUROECTODERMAL_TUMOR_CELL_LINE = "BTO_0004259"

    # Askin's tumor cell
    BTO_0004260 = "BTO_0004260"
    ASKIN_S_TUMOR_CELL = "BTO_0004260"

    # peripheral primitive neuroectodermal tumor cell
    BTO_0004261 = "BTO_0004261"
    PERIPHERAL_PRIMITIVE_NEUROECTODERMAL_TUMOR_CELL = "BTO_0004261"

    # cerebral giant cell
    BTO_0004262 = "BTO_0004262"
    CEREBRAL_GIANT_CELL = "BTO_0004262"

    # COM-3 cell
    BTO_0004263 = "BTO_0004263"
    COM_3_CELL = "BTO_0004263"

    # INC-2 cell
    BTO_0004264 = "BTO_0004264"
    INC_2_CELL = "BTO_0004264"

    # EJ cell
    BTO_0004265 = "BTO_0004265"
    EJ_CELL = "BTO_0004265"

    # H-10 cell
    BTO_0004266 = "BTO_0004266"
    H_10_CELL = "BTO_0004266"

    # follicular dendritic cell
    BTO_0004267 = "BTO_0004267"
    FOLLICULAR_DENDRITIC_CELL = "BTO_0004267"

    # follicular dendritic cell line
    BTO_0004268 = "BTO_0004268"
    FOLLICULAR_DENDRITIC_CELL_LINE = "BTO_0004268"

    # liver cancer stem cell
    BTO_0004269 = "BTO_0004269"
    LIVER_CANCER_STEM_CELL = "BTO_0004269"

    # adult liver stem cell
    BTO_0004270 = "BTO_0004270"
    ADULT_LIVER_STEM_CELL = "BTO_0004270"

    # hyalocyte
    BTO_0004271 = "BTO_0004271"
    HYALOCYTE = "BTO_0004271"

    # hyalocyte cell line
    BTO_0004272 = "BTO_0004272"
    HYALOCYTE_CELL_LINE = "BTO_0004272"

    # PH-5 cell
    BTO_0004273 = "BTO_0004273"
    PH_5_CELL = "BTO_0004273"

    # PLC-8024 cell
    BTO_0004274 = "BTO_0004274"
    PLC_8024_CELL = "BTO_0004274"

    # SM-5 cell
    BTO_0004275 = "BTO_0004275"
    SM_5_CELL = "BTO_0004275"

    # SM-7 cell
    BTO_0004276 = "BTO_0004276"
    SM_7_CELL = "BTO_0004276"

    # scleral lamina cribrosa
    BTO_0004277 = "BTO_0004277"
    SCLERAL_LAMINA_CRIBROSA = "BTO_0004277"

    # cerebellar granule cell
    BTO_0004278 = "BTO_0004278"
    CEREBELLAR_GRANULE_CELL = "BTO_0004278"

    # cerebral granule cell
    BTO_0004279 = "BTO_0004279"
    CEREBRAL_GRANULE_CELL = "BTO_0004279"

    # peptonephridium
    BTO_0004280 = "BTO_0004280"
    PEPTONEPHRIDIUM = "BTO_0004280"

    # C-81 cell
    BTO_0004281 = "BTO_0004281"
    C_81_CELL = "BTO_0004281"

    # TSA cell
    BTO_0004282 = "BTO_0004282"
    TSA_CELL = "BTO_0004282"

    # TK-10 cell
    BTO_0004283 = "BTO_0004283"
    TK_10_CELL = "BTO_0004283"

    # TK-164 cell
    BTO_0004284 = "BTO_0004284"
    TK_164_CELL = "BTO_0004284"

    # oviductal ampulla
    BTO_0004285 = "BTO_0004285"
    OVIDUCTAL_AMPULLA = "BTO_0004285"

    # basophilic leukemia cell
    BTO_0004286 = "BTO_0004286"
    BASOPHILIC_LEUKEMIA_CELL = "BTO_0004286"

    # culture condition:peptone-grown cell
    BTO_0004287 = "BTO_0004287"
    CULTURE_CONDITION_PEPTONE_GROWN_CELL = "BTO_0004287"

    # culture condition:starch-grown cell
    BTO_0004288 = "BTO_0004288"
    CULTURE_CONDITION_STARCH_GROWN_CELL = "BTO_0004288"

    # culture condition:Warrens medium-grown cell
    BTO_0004289 = "BTO_0004289"
    CULTURE_CONDITION_WARRENS_MEDIUM_GROWN_CELL = "BTO_0004289"

    # umbilical artery smooth muscle
    BTO_0004290 = "BTO_0004290"
    UMBILICAL_ARTERY_SMOOTH_MUSCLE = "BTO_0004290"

    # umbilical vein smooth muscle
    BTO_0004291 = "BTO_0004291"
    UMBILICAL_VEIN_SMOOTH_MUSCLE = "BTO_0004291"

    # claustrum
    BTO_0004292 = "BTO_0004292"
    CLAUSTRUM = "BTO_0004292"

    # heart endothelium
    BTO_0004293 = "BTO_0004293"
    HEART_ENDOTHELIUM = "BTO_0004293"

    # heart endothelial cell
    BTO_0004294 = "BTO_0004294"
    HEART_ENDOTHELIAL_CELL = "BTO_0004294"

    # umbilical artery endothelial cell
    BTO_0004295 = "BTO_0004295"
    UMBILICAL_ARTERY_ENDOTHELIAL_CELL = "BTO_0004295"

    # umbilical vein endothelial cell
    BTO_0004296 = "BTO_0004296"
    UMBILICAL_VEIN_ENDOTHELIAL_CELL = "BTO_0004296"

    # colonic epithelial cell
    BTO_0004297 = "BTO_0004297"
    COLONIC_EPITHELIAL_CELL = "BTO_0004297"

    # corneal epithelial cell
    BTO_0004298 = "BTO_0004298"
    CORNEAL_EPITHELIAL_CELL = "BTO_0004298"

    # lung epithelial cell
    BTO_0004299 = "BTO_0004299"
    LUNG_EPITHELIAL_CELL = "BTO_0004299"

    # mammary epithelial cell
    BTO_0004300 = "BTO_0004300"
    MAMMARY_EPITHELIAL_CELL = "BTO_0004300"

    # neuroepithelial cell
    BTO_0004301 = "BTO_0004301"
    NEUROEPITHELIAL_CELL = "BTO_0004301"

    # plant epithelium
    BTO_0004302 = "BTO_0004302"
    PLANT_EPITHELIUM = "BTO_0004302"

    # lymphatic endothelium
    BTO_0004303 = "BTO_0004303"
    LYMPHATIC_ENDOTHELIUM = "BTO_0004303"

    # cell lysate
    BTO_0004304 = "BTO_0004304"
    CELL_LYSATE = "BTO_0004304"

    # hairy root
    BTO_0004305 = "BTO_0004305"
    HAIRY_ROOT = "BTO_0004305"

    # NCM-460 cell
    BTO_0004306 = "BTO_0004306"
    NCM_460_CELL = "BTO_0004306"

    # hepatic artery
    BTO_0004307 = "BTO_0004307"
    HEPATIC_ARTERY = "BTO_0004307"

    # CGR-8 cell
    BTO_0004308 = "BTO_0004308"
    CGR_8_CELL = "BTO_0004308"

    # Cl-66 cell
    BTO_0004309 = "BTO_0004309"
    CL_66_CELL = "BTO_0004309"

    # Cl-66M2 cell
    BTO_0004310 = "BTO_0004310"
    CL_66M2_CELL = "BTO_0004310"

    # 4T1 cell
    BTO_0004311 = "BTO_0004311"
    _4T1_CELL = "BTO_0004311"

    # JIMT-1 cell
    BTO_0004312 = "BTO_0004312"
    JIMT_1_CELL = "BTO_0004312"

    # GM16096 cell
    BTO_0004313 = "BTO_0004313"
    GM16096_CELL = "BTO_0004313"

    # GM16088 cell
    BTO_0004314 = "BTO_0004314"
    GM16088_CELL = "BTO_0004314"

    # HTD-114 cell
    BTO_0004315 = "BTO_0004315"
    HTD_114_CELL = "BTO_0004315"

    # NBT-II cell
    BTO_0004316 = "BTO_0004316"
    NBT_II_CELL = "BTO_0004316"

    # immune stem cell
    BTO_0004317 = "BTO_0004317"
    IMMUNE_STEM_CELL = "BTO_0004317"

    # WB-F344 cell
    BTO_0004318 = "BTO_0004318"
    WB_F344_CELL = "BTO_0004318"

    # WB-311 cell
    BTO_0004319 = "BTO_0004319"
    WB_311_CELL = "BTO_0004319"

    # 1682-A cell
    BTO_0004320 = "BTO_0004320"
    _1682_A_CELL = "BTO_0004320"

    # 2BN cell
    BTO_0004321 = "BTO_0004321"
    _2BN_CELL = "BTO_0004321"

    # 2BNneo cell
    BTO_0004322 = "BTO_0004322"
    _2BNNEO_CELL = "BTO_0004322"

    # 2BNhTERT cell
    BTO_0004323 = "BTO_0004323"
    _2BNHTERT_CELL = "BTO_0004323"

    # osteoblast cell line
    BTO_0004324 = "BTO_0004324"
    OSTEOBLAST_CELL_LINE = "BTO_0004324"

    # 2T3 cell
    BTO_0004325 = "BTO_0004325"
    _2T3_CELL = "BTO_0004325"

    # ADF cell
    BTO_0004326 = "BTO_0004326"
    ADF_CELL = "BTO_0004326"

    # CESS cell
    BTO_0004327 = "BTO_0004327"
    CESS_CELL = "BTO_0004327"

    # DAOY cell
    BTO_0004328 = "BTO_0004328"
    DAOY_CELL = "BTO_0004328"

    # Madsen cell
    BTO_0004329 = "BTO_0004329"
    MADSEN_CELL = "BTO_0004329"

    # UW228-1 cell
    BTO_0004330 = "BTO_0004330"
    UW228_1_CELL = "BTO_0004330"

    # UW228-2 cell
    BTO_0004331 = "BTO_0004331"
    UW228_2_CELL = "BTO_0004331"

    # UW228-3 cell
    BTO_0004332 = "BTO_0004332"
    UW228_3_CELL = "BTO_0004332"

    # Do11.10 cell
    BTO_0004333 = "BTO_0004333"
    DO11_10_CELL = "BTO_0004333"

    # EBV-PBL cell
    BTO_0004334 = "BTO_0004334"
    EBV_PBL_CELL = "BTO_0004334"

    # GP6 cell
    BTO_0004335 = "BTO_0004335"
    GP6_CELL = "BTO_0004335"

    # THC-252 cell
    BTO_0004336 = "BTO_0004336"
    THC_252_CELL = "BTO_0004336"

    # THC-H5D cell
    BTO_0004337 = "BTO_0004337"
    THC_H5D_CELL = "BTO_0004337"

    # GN5 cell
    BTO_0004338 = "BTO_0004338"
    GN5_CELL = "BTO_0004338"

    # ScGT1 cell
    BTO_0004339 = "BTO_0004339"
    SCGT1_CELL = "BTO_0004339"

    # culture condition:high copper medium-grown cell
    BTO_0004340 = "BTO_0004340"
    CULTURE_CONDITION_HIGH_COPPER_MEDIUM_GROWN_CELL = "BTO_0004340"

    # granular insular cortex
    BTO_0004341 = "BTO_0004341"
    GRANULAR_INSULAR_CORTEX = "BTO_0004341"

    # agranular insular cortex
    BTO_0004342 = "BTO_0004342"
    AGRANULAR_INSULAR_CORTEX = "BTO_0004342"

    # auditory cortex
    BTO_0004343 = "BTO_0004343"
    AUDITORY_CORTEX = "BTO_0004343"

    # infralimbic cortex
    BTO_0004344 = "BTO_0004344"
    INFRALIMBIC_CORTEX = "BTO_0004344"

    # entorhinal cortex
    BTO_0004345 = "BTO_0004345"
    ENTORHINAL_CORTEX = "BTO_0004345"

    # medial entorhinal cortex
    BTO_0004346 = "BTO_0004346"
    MEDIAL_ENTORHINAL_CORTEX = "BTO_0004346"

    # lateral entorhinal cortex
    BTO_0004347 = "BTO_0004347"
    LATERAL_ENTORHINAL_CORTEX = "BTO_0004347"

    # motor cortex
    BTO_0004348 = "BTO_0004348"
    MOTOR_CORTEX = "BTO_0004348"

    # laterodorsal thalamic nucleus
    BTO_0004349 = "BTO_0004349"
    LATERODORSAL_THALAMIC_NUCLEUS = "BTO_0004349"

    # lateral dorsal nucleus
    BTO_0004350 = "BTO_0004350"
    LATERAL_DORSAL_NUCLEUS = "BTO_0004350"

    # lateral posterior nucleus
    BTO_0004351 = "BTO_0004351"
    LATERAL_POSTERIOR_NUCLEUS = "BTO_0004351"

    # pulvinar
    BTO_0004352 = "BTO_0004352"
    PULVINAR = "BTO_0004352"

    # somatosensory cortex
    BTO_0004353 = "BTO_0004353"
    SOMATOSENSORY_CORTEX = "BTO_0004353"

    # postcentral gyrus
    BTO_0004354 = "BTO_0004354"
    POSTCENTRAL_GYRUS = "BTO_0004354"

    # perirhinal cortex
    BTO_0004355 = "BTO_0004355"
    PERIRHINAL_CORTEX = "BTO_0004355"

    # Brodmann area 35
    BTO_0004356 = "BTO_0004356"
    BRODMANN_AREA_35 = "BTO_0004356"

    # Brodmann area 36
    BTO_0004357 = "BTO_0004357"
    BRODMANN_AREA_36 = "BTO_0004357"

    # sinus node
    BTO_0004358 = "BTO_0004358"
    SINUS_NODE = "BTO_0004358"

    # paw
    BTO_0004359 = "BTO_0004359"
    PAW = "BTO_0004359"

    # angiomyolipoma cell
    BTO_0004360 = "BTO_0004360"
    ANGIOMYOLIPOMA_CELL = "BTO_0004360"

    # callus culture
    BTO_0004361 = "BTO_0004361"
    CALLUS_CULTURE = "BTO_0004361"

    # colon muscle
    BTO_0004362 = "BTO_0004362"
    COLON_MUSCLE = "BTO_0004362"

    # gastroesophageal adenocarcinoma cell
    BTO_0004363 = "BTO_0004363"
    GASTROESOPHAGEAL_ADENOCARCINOMA_CELL = "BTO_0004363"

    # gastroesophageal junction
    BTO_0004364 = "BTO_0004364"
    GASTROESOPHAGEAL_JUNCTION = "BTO_0004364"

    # gastroesophageal cancer cell
    BTO_0004365 = "BTO_0004365"
    GASTROESOPHAGEAL_CANCER_CELL = "BTO_0004365"

    # lateral geniculate nucleus
    BTO_0004366 = "BTO_0004366"
    LATERAL_GENICULATE_NUCLEUS = "BTO_0004366"

    # lateral geniculate body
    BTO_0004367 = "BTO_0004367"
    LATERAL_GENICULATE_BODY = "BTO_0004367"

    # vestibular nucleus
    BTO_0004368 = "BTO_0004368"
    VESTIBULAR_NUCLEUS = "BTO_0004368"

    # inferior vestibular nucleus
    BTO_0004369 = "BTO_0004369"
    INFERIOR_VESTIBULAR_NUCLEUS = "BTO_0004369"

    # lateral vestibular nucleus
    BTO_0004370 = "BTO_0004370"
    LATERAL_VESTIBULAR_NUCLEUS = "BTO_0004370"

    # medial vestibular nucleus
    BTO_0004371 = "BTO_0004371"
    MEDIAL_VESTIBULAR_NUCLEUS = "BTO_0004371"

    # superior vestibular nucleus
    BTO_0004372 = "BTO_0004372"
    SUPERIOR_VESTIBULAR_NUCLEUS = "BTO_0004372"

    # ventral posterior nucleus
    BTO_0004373 = "BTO_0004373"
    VENTRAL_POSTERIOR_NUCLEUS = "BTO_0004373"

    # ventral posterior inferior nucleus
    BTO_0004374 = "BTO_0004374"
    VENTRAL_POSTERIOR_INFERIOR_NUCLEUS = "BTO_0004374"

    # ventral globus pallidus
    BTO_0004375 = "BTO_0004375"
    VENTRAL_GLOBUS_PALLIDUS = "BTO_0004375"

    # dorsal globus pallidus
    BTO_0004376 = "BTO_0004376"
    DORSAL_GLOBUS_PALLIDUS = "BTO_0004376"

    # pup
    BTO_0004377 = "BTO_0004377"
    PUP = "BTO_0004377"

    # blood vessel wall
    BTO_0004378 = "BTO_0004378"
    BLOOD_VESSEL_WALL = "BTO_0004378"

    # parahippocampal region
    BTO_0004379 = "BTO_0004379"
    PARAHIPPOCAMPAL_REGION = "BTO_0004379"

    # parahippocampal gyrus
    BTO_0004380 = "BTO_0004380"
    PARAHIPPOCAMPAL_GYRUS = "BTO_0004380"

    # prelimbic cortex
    BTO_0004381 = "BTO_0004381"
    PRELIMBIC_CORTEX = "BTO_0004381"

    # skin epithelium
    BTO_0004382 = "BTO_0004382"
    SKIN_EPITHELIUM = "BTO_0004382"

    # follicular fluid
    BTO_0004383 = "BTO_0004383"
    FOLLICULAR_FLUID = "BTO_0004383"

    # osteoclast stem cell
    BTO_0004384 = "BTO_0004384"
    OSTEOCLAST_STEM_CELL = "BTO_0004384"

    # cardinal vein
    BTO_0004385 = "BTO_0004385"
    CARDINAL_VEIN = "BTO_0004385"

    # posterior cardinal vein
    BTO_0004386 = "BTO_0004386"
    POSTERIOR_CARDINAL_VEIN = "BTO_0004386"

    # anterior cardinal vein
    BTO_0004387 = "BTO_0004387"
    ANTERIOR_CARDINAL_VEIN = "BTO_0004387"

    # common cardinal vein
    BTO_0004388 = "BTO_0004388"
    COMMON_CARDINAL_VEIN = "BTO_0004388"

    # angiomyolipoma cell line
    BTO_0004389 = "BTO_0004389"
    ANGIOMYOLIPOMA_CELL_LINE = "BTO_0004389"

    # SV7tert cell
    BTO_0004390 = "BTO_0004390"
    SV7TERT_CELL = "BTO_0004390"

    # SPAML/SV7 cell
    BTO_0004391 = "BTO_0004391"
    SPAML_SV7_CELL = "BTO_0004391"

    # skeletal muscle cell
    BTO_0004392 = "BTO_0004392"
    SKELETAL_MUSCLE_CELL = "BTO_0004392"

    # alabastrum
    BTO_0004393 = "BTO_0004393"
    ALABASTRUM = "BTO_0004393"

    # 16-HBEo cell
    BTO_0004394 = "BTO_0004394"
    _16_HBEO_CELL = "BTO_0004394"

    # microvessel
    BTO_0004395 = "BTO_0004395"
    MICROVESSEL = "BTO_0004395"

    # femorotibial joint
    BTO_0004396 = "BTO_0004396"
    FEMOROTIBIAL_JOINT = "BTO_0004396"

    # B-103 cell
    BTO_0004397 = "BTO_0004397"
    B_103_CELL = "BTO_0004397"

    # meningioma cell line
    BTO_0004398 = "BTO_0004398"
    MENINGIOMA_CELL_LINE = "BTO_0004398"

    # BEN-MEN-1 cell
    BTO_0004399 = "BTO_0004399"
    BEN_MEN_1_CELL = "BTO_0004399"

    # BPAEC cell
    BTO_0004400 = "BTO_0004400"
    BPAEC_CELL = "BTO_0004400"

    # bronchial smooth muscle
    BTO_0004401 = "BTO_0004401"
    BRONCHIAL_SMOOTH_MUSCLE = "BTO_0004401"

    # bronchial smooth muscle cell
    BTO_0004402 = "BTO_0004402"
    BRONCHIAL_SMOOTH_MUSCLE_CELL = "BTO_0004402"

    # tracheal smooth muscle cell
    BTO_0004403 = "BTO_0004403"
    TRACHEAL_SMOOTH_MUSCLE_CELL = "BTO_0004403"

    # BL-3 cell
    BTO_0004404 = "BTO_0004404"
    BL_3_CELL = "BTO_0004404"

    # 3D5 cell
    BTO_0004405 = "BTO_0004405"
    _3D5_CELL = "BTO_0004405"

    # CABA I cell
    BTO_0004406 = "BTO_0004406"
    CABA_I_CELL = "BTO_0004406"

    # CB33 cell
    BTO_0004407 = "BTO_0004407"
    CB33_CELL = "BTO_0004407"

    # culture condition:CD34+ cell
    BTO_0004408 = "BTO_0004408"
    CULTURE_CONDITION_CD34__CELL = "BTO_0004408"

    # culture condition:CD68+ cell
    BTO_0004409 = "BTO_0004409"
    CULTURE_CONDITION_CD68__CELL = "BTO_0004409"

    # culture condition:CD8+ cell
    BTO_0004410 = "BTO_0004410"
    CULTURE_CONDITION_CD8__CELL = "BTO_0004410"

    # oral lichen planus disease specific cell type
    BTO_0004412 = "BTO_0004412"
    ORAL_LICHEN_PLANUS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0004412"

    # CJ7 cell
    BTO_0004413 = "BTO_0004413"
    CJ7_CELL = "BTO_0004413"

    # KH2 cell
    BTO_0004414 = "BTO_0004414"
    KH2_CELL = "BTO_0004414"

    # DM-4 cell
    BTO_0004415 = "BTO_0004415"
    DM_4_CELL = "BTO_0004415"

    # Daltons lymphoma cell
    BTO_0004416 = "BTO_0004416"
    DALTONS_LYMPHOMA_CELL = "BTO_0004416"

    # Daltons lymphoma ascites cell
    BTO_0004417 = "BTO_0004417"
    DALTONS_LYMPHOMA_ASCITES_CELL = "BTO_0004417"

    # Daltons lymphoma ascites
    BTO_0004418 = "BTO_0004418"
    DALTONS_LYMPHOMA_ASCITES = "BTO_0004418"

    # dermal fibroblast
    BTO_0004419 = "BTO_0004419"
    DERMAL_FIBROBLAST = "BTO_0004419"

    # digestive cell
    BTO_0004420 = "BTO_0004420"
    DIGESTIVE_CELL = "BTO_0004420"

    # salivary gland epithelium
    BTO_0004421 = "BTO_0004421"
    SALIVARY_GLAND_EPITHELIUM = "BTO_0004421"

    # pleural cavity
    BTO_0004422 = "BTO_0004422"
    PLEURAL_CAVITY = "BTO_0004422"

    # empyema fluid
    BTO_0004423 = "BTO_0004423"
    EMPYEMA_FLUID = "BTO_0004423"

    # ES-2 cell
    BTO_0004424 = "BTO_0004424"
    ES_2_CELL = "BTO_0004424"

    # stratum granulosum cerebelli
    BTO_0004425 = "BTO_0004425"
    STRATUM_GRANULOSUM_CEREBELLI = "BTO_0004425"

    # NCI-H1915 cell
    BTO_0004426 = "BTO_0004426"
    NCI_H1915_CELL = "BTO_0004426"

    # NCI-H211 cell
    BTO_0004427 = "BTO_0004427"
    NCI_H211_CELL = "BTO_0004427"

    # H4-II-E-C3 cell
    BTO_0004428 = "BTO_0004428"
    H4_II_E_C3_CELL = "BTO_0004428"

    # H-59 cell
    BTO_0004429 = "BTO_0004429"
    H_59_CELL = "BTO_0004429"

    # HBL-52 cell
    BTO_0004430 = "BTO_0004430"
    HBL_52_CELL = "BTO_0004430"

    # coronary artery endothelial cell line
    BTO_0004431 = "BTO_0004431"
    CORONARY_ARTERY_ENDOTHELIAL_CELL_LINE = "BTO_0004431"

    # HCAEC cell
    BTO_0004432 = "BTO_0004432"
    HCAEC_CELL = "BTO_0004432"

    # HET-1A cell
    BTO_0004433 = "BTO_0004433"
    HET_1A_CELL = "BTO_0004433"

    # HMEC-1330 cell
    BTO_0004434 = "BTO_0004434"
    HMEC_1330_CELL = "BTO_0004434"

    # HOSE 11-12 cell
    BTO_0004435 = "BTO_0004435"
    HOSE_11_12_CELL = "BTO_0004435"

    # HOSE 6-3 cell
    BTO_0004436 = "BTO_0004436"
    HOSE_6_3_CELL = "BTO_0004436"

    # HOSE 17-1 cell
    BTO_0004437 = "BTO_0004437"
    HOSE_17_1_CELL = "BTO_0004437"

    # HSCC cell
    BTO_0004438 = "BTO_0004438"
    HSCC_CELL = "BTO_0004438"

    # hypopharyngeal carcinoma cell line
    BTO_0004439 = "BTO_0004439"
    HYPOPHARYNGEAL_CARCINOMA_CELL_LINE = "BTO_0004439"

    # UT-SCC-14 cell
    BTO_0004440 = "BTO_0004440"
    UT_SCC_14_CELL = "BTO_0004440"

    # UT-SCC-15 cell
    BTO_0004441 = "BTO_0004441"
    UT_SCC_15_CELL = "BTO_0004441"

    # UT-SCC-5 cell
    BTO_0004442 = "BTO_0004442"
    UT_SCC_5_CELL = "BTO_0004442"

    # XF354 cell
    BTO_0004443 = "BTO_0004443"
    XF354_CELL = "BTO_0004443"

    # HUVE-12 cell
    BTO_0004444 = "BTO_0004444"
    HUVE_12_CELL = "BTO_0004444"

    # IB3-1 cell
    BTO_0004445 = "BTO_0004445"
    IB3_1_CELL = "BTO_0004445"

    # S9 cell
    BTO_0004446 = "BTO_0004446"
    S9_CELL = "BTO_0004446"

    # C38 cell
    BTO_0004447 = "BTO_0004447"
    C38_CELL = "BTO_0004447"

    # LN-235 cell
    BTO_0004448 = "BTO_0004448"
    LN_235_CELL = "BTO_0004448"

    # LN-443 cell
    BTO_0004449 = "BTO_0004449"
    LN_443_CELL = "BTO_0004449"

    # LN-444 cell
    BTO_0004450 = "BTO_0004450"
    LN_444_CELL = "BTO_0004450"

    # LN-464 cell
    BTO_0004451 = "BTO_0004451"
    LN_464_CELL = "BTO_0004451"

    # LN-702 cell
    BTO_0004452 = "BTO_0004452"
    LN_702_CELL = "BTO_0004452"

    # LN-751 cell
    BTO_0004453 = "BTO_0004453"
    LN_751_CELL = "BTO_0004453"

    # LN-774 cell
    BTO_0004454 = "BTO_0004454"
    LN_774_CELL = "BTO_0004454"

    # LN-784 cell
    BTO_0004455 = "BTO_0004455"
    LN_784_CELL = "BTO_0004455"

    # LN-215 cell
    BTO_0004456 = "BTO_0004456"
    LN_215_CELL = "BTO_0004456"

    # LN-308 cell
    BTO_0004457 = "BTO_0004457"
    LN_308_CELL = "BTO_0004457"

    # LN-340 cell
    BTO_0004458 = "BTO_0004458"
    LN_340_CELL = "BTO_0004458"

    # LN-382 cell
    BTO_0004459 = "BTO_0004459"
    LN_382_CELL = "BTO_0004459"

    # FD-1 cell
    BTO_0004460 = "BTO_0004460"
    FD_1_CELL = "BTO_0004460"

    # KYSE-30 cell
    BTO_0004461 = "BTO_0004461"
    KYSE_30_CELL = "BTO_0004461"

    # K-562R cell
    BTO_0004462 = "BTO_0004462"
    K_562R_CELL = "BTO_0004462"

    # ileostomal fluid
    BTO_0004463 = "BTO_0004463"
    ILEOSTOMAL_FLUID = "BTO_0004463"

    # IOMM-Lee cell
    BTO_0004464 = "BTO_0004464"
    IOMM_LEE_CELL = "BTO_0004464"

    # LAMA-84 cell
    BTO_0004465 = "BTO_0004465"
    LAMA_84_CELL = "BTO_0004465"

    # LAMA-87 cell
    BTO_0004466 = "BTO_0004466"
    LAMA_87_CELL = "BTO_0004466"

    # LbetaT2 cell
    BTO_0004467 = "BTO_0004467"
    LBETAT2_CELL = "BTO_0004467"

    # lip epithelium
    BTO_0004468 = "BTO_0004468"
    LIP_EPITHELIUM = "BTO_0004468"

    # HCCLM-3 cell
    BTO_0004469 = "BTO_0004469"
    HCCLM_3_CELL = "BTO_0004469"

    # HCCLM-6 cell
    BTO_0004470 = "BTO_0004470"
    HCCLM_6_CELL = "BTO_0004470"

    # Mahlavu cell
    BTO_0004471 = "BTO_0004471"
    MAHLAVU_CELL = "BTO_0004471"

    # mantle cell lymphoma cell
    BTO_0004472 = "BTO_0004472"
    MANTLE_CELL_LYMPHOMA_CELL = "BTO_0004472"

    # MC3T3-E1(C4) cell
    BTO_0004473 = "BTO_0004473"
    MC3T3_E1_C4__CELL = "BTO_0004473"

    # MDA-MB-231-BAG cell
    BTO_0004474 = "BTO_0004474"
    MDA_MB_231_BAG_CELL = "BTO_0004474"

    # MEL cell
    BTO_0004475 = "BTO_0004475"
    MEL_CELL = "BTO_0004475"

    # MES-23.5 cell
    BTO_0004476 = "BTO_0004476"
    MES_23_5_CELL = "BTO_0004476"

    # medial temporal lobe
    BTO_0004477 = "BTO_0004477"
    MEDIAL_TEMPORAL_LOBE = "BTO_0004477"

    # mucosal melanoma cell
    BTO_0004478 = "BTO_0004478"
    MUCOSAL_MELANOMA_CELL = "BTO_0004478"

    # MV4-11 cell
    BTO_0004479 = "BTO_0004479"
    MV4_11_CELL = "BTO_0004479"

    # nasopharynx epithelium
    BTO_0004480 = "BTO_0004480"
    NASOPHARYNX_EPITHELIUM = "BTO_0004480"

    # neural crest-derived stem cell
    BTO_0004481 = "BTO_0004481"
    NEURAL_CREST_DERIVED_STEM_CELL = "BTO_0004481"

    # ovarian surface epithelial cell line
    BTO_0004482 = "BTO_0004482"
    OVARIAN_SURFACE_EPITHELIAL_CELL_LINE = "BTO_0004482"

    # ovarian surface epithelium
    BTO_0004483 = "BTO_0004483"
    OVARIAN_SURFACE_EPITHELIUM = "BTO_0004483"

    # ovarian surface epithelial cell
    BTO_0004484 = "BTO_0004484"
    OVARIAN_SURFACE_EPITHELIAL_CELL = "BTO_0004484"

    # OV-MZ-10 cell
    BTO_0004485 = "BTO_0004485"
    OV_MZ_10_CELL = "BTO_0004485"

    # OV-MZ-15 cell
    BTO_0004486 = "BTO_0004486"
    OV_MZ_15_CELL = "BTO_0004486"

    # OV-MZ-6 cell
    BTO_0004487 = "BTO_0004487"
    OV_MZ_6_CELL = "BTO_0004487"

    # NSC-34 cell
    BTO_0004488 = "BTO_0004488"
    NSC_34_CELL = "BTO_0004488"

    # OE-21 cell
    BTO_0004489 = "BTO_0004489"
    OE_21_CELL = "BTO_0004489"

    # RFL-6 cell
    BTO_0004490 = "BTO_0004490"
    RFL_6_CELL = "BTO_0004490"

    # RL95-2 cell
    BTO_0004491 = "BTO_0004491"
    RL95_2_CELL = "BTO_0004491"

    # gastric epithelial cell
    BTO_0004492 = "BTO_0004492"
    GASTRIC_EPITHELIAL_CELL = "BTO_0004492"

    # gastric epithelium cell line
    BTO_0004493 = "BTO_0004493"
    GASTRIC_EPITHELIUM_CELL_LINE = "BTO_0004493"

    # RGM-1 cell
    BTO_0004494 = "BTO_0004494"
    RGM_1_CELL = "BTO_0004494"

    # SIRC cell
    BTO_0004495 = "BTO_0004495"
    SIRC_CELL = "BTO_0004495"

    # preosteoclast
    BTO_0004496 = "BTO_0004496"
    PREOSTEOCLAST = "BTO_0004496"

    # WT-51 cell
    BTO_0004497 = "BTO_0004497"
    WT_51_CELL = "BTO_0004497"

    # THCE cell
    BTO_0004498 = "BTO_0004498"
    THCE_CELL = "BTO_0004498"

    # prostate gland intraepithelial neoplasia cell line
    BTO_0004499 = "BTO_0004499"
    PROSTATE_GLAND_INTRAEPITHELIAL_NEOPLASIA_CELL_LINE = "BTO_0004499"

    # R1 cell
    BTO_0004500 = "BTO_0004500"
    R1_CELL = "BTO_0004500"

    # plant vascular cell
    BTO_0004501 = "BTO_0004501"
    PLANT_VASCULAR_CELL = "BTO_0004501"

    # vascular cambium
    BTO_0004502 = "BTO_0004502"
    VASCULAR_CAMBIUM = "BTO_0004502"

    # submerged culture
    BTO_0004503 = "BTO_0004503"
    SUBMERGED_CULTURE = "BTO_0004503"

    # root vascular cell
    BTO_0004504 = "BTO_0004504"
    ROOT_VASCULAR_CELL = "BTO_0004504"

    # RS4-11 cell
    BTO_0004505 = "BTO_0004505"
    RS4_11_CELL = "BTO_0004505"

    # RT-2 cell
    BTO_0004506 = "BTO_0004506"
    RT_2_CELL = "BTO_0004506"

    # sEnd-1 cell
    BTO_0004507 = "BTO_0004507"
    SEND_1_CELL = "BTO_0004507"

    # endothelioma cell
    BTO_0004508 = "BTO_0004508"
    ENDOTHELIOMA_CELL = "BTO_0004508"

    # endothelioma cell line
    BTO_0004509 = "BTO_0004509"
    ENDOTHELIOMA_CELL_LINE = "BTO_0004509"

    # cystadenocarcinoma cell
    BTO_0004510 = "BTO_0004510"
    CYSTADENOCARCINOMA_CELL = "BTO_0004510"

    # serous cystadenocarcinoma cell
    BTO_0004511 = "BTO_0004511"
    SEROUS_CYSTADENOCARCINOMA_CELL = "BTO_0004511"

    # pseudomucinous cystadenocarcinoma cell
    BTO_0004512 = "BTO_0004512"
    PSEUDOMUCINOUS_CYSTADENOCARCINOMA_CELL = "BTO_0004512"

    # Sertoli cell line
    BTO_0004513 = "BTO_0004513"
    SERTOLI_CELL_LINE = "BTO_0004513"

    # Ser-W3 cell
    BTO_0004514 = "BTO_0004514"
    SER_W3_CELL = "BTO_0004514"

    # SF-3061 cell
    BTO_0004515 = "BTO_0004515"
    SF_3061_CELL = "BTO_0004515"

    # SF-4068 cell
    BTO_0004516 = "BTO_0004516"
    SF_4068_CELL = "BTO_0004516"

    # SF-4433 cell
    BTO_0004517 = "BTO_0004517"
    SF_4433_CELL = "BTO_0004517"

    # uterine gland
    BTO_0004518 = "BTO_0004518"
    UTERINE_GLAND = "BTO_0004518"

    # myometrial cell
    BTO_0004519 = "BTO_0004519"
    MYOMETRIAL_CELL = "BTO_0004519"

    # regulatory T-lymphocyte
    BTO_0004520 = "BTO_0004520"
    REGULATORY_T_LYMPHOCYTE = "BTO_0004520"

    # TIG-3-20 cell
    BTO_0004521 = "BTO_0004521"
    TIG_3_20_CELL = "BTO_0004521"

    # Leydig cell line
    BTO_0004522 = "BTO_0004522"
    LEYDIG_CELL_LINE = "BTO_0004522"

    # TM-3 cell
    BTO_0004523 = "BTO_0004523"
    TM_3_CELL = "BTO_0004523"

    # germinal epithelium
    BTO_0004524 = "BTO_0004524"
    GERMINAL_EPITHELIUM = "BTO_0004524"

    # subcutaneous tissue
    BTO_0004525 = "BTO_0004525"
    SUBCUTANEOUS_TISSUE = "BTO_0004525"

    # ulcerative colitis disease specific cell type
    BTO_0004526 = "BTO_0004526"
    ULCERATIVE_COLITIS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0004526"

    # uterine luminal fluid
    BTO_0004527 = "BTO_0004527"
    UTERINE_LUMINAL_FLUID = "BTO_0004527"

    # high endothelial venule
    BTO_0004528 = "BTO_0004528"
    HIGH_ENDOTHELIAL_VENULE = "BTO_0004528"

    # PA-23 cell
    BTO_0004529 = "BTO_0004529"
    PA_23_CELL = "BTO_0004529"

    # F5 meningioma cell
    BTO_0004530 = "BTO_0004530"
    F5_MENINGIOMA_CELL = "BTO_0004530"

    # bolting stage
    BTO_0004531 = "BTO_0004531"
    BOLTING_STAGE = "BTO_0004531"

    # C-10 cell
    BTO_0004532 = "BTO_0004532"
    C_10_CELL = "BTO_0004532"

    # respiratory epithelium cell
    BTO_0004533 = "BTO_0004533"
    RESPIRATORY_EPITHELIUM_CELL = "BTO_0004533"

    # cystic fibrosis disease specific cell type
    BTO_0004534 = "BTO_0004534"
    CYSTIC_FIBROSIS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0004534"

    # medullary collecting duct cell
    BTO_0004535 = "BTO_0004535"
    MEDULLARY_COLLECTING_DUCT_CELL = "BTO_0004535"

    # medullary collecting duct
    BTO_0004536 = "BTO_0004536"
    MEDULLARY_COLLECTING_DUCT = "BTO_0004536"

    # cortical collecting duct cell
    BTO_0004537 = "BTO_0004537"
    CORTICAL_COLLECTING_DUCT_CELL = "BTO_0004537"

    # initial collecting tubule
    BTO_0004538 = "BTO_0004538"
    INITIAL_COLLECTING_TUBULE = "BTO_0004538"

    # connecting tubule
    BTO_0004539 = "BTO_0004539"
    CONNECTING_TUBULE = "BTO_0004539"

    # papillary duct
    BTO_0004540 = "BTO_0004540"
    PAPILLARY_DUCT = "BTO_0004540"

    # connecting tubule cell
    BTO_0004541 = "BTO_0004541"
    CONNECTING_TUBULE_CELL = "BTO_0004541"

    # principal cell
    BTO_0004542 = "BTO_0004542"
    PRINCIPAL_CELL = "BTO_0004542"

    # inner medullary collecting duct cell
    BTO_0004543 = "BTO_0004543"
    INNER_MEDULLARY_COLLECTING_DUCT_CELL = "BTO_0004543"

    # inner medullary collecting duct
    BTO_0004544 = "BTO_0004544"
    INNER_MEDULLARY_COLLECTING_DUCT = "BTO_0004544"

    # M-1 collecting duct cell
    BTO_0004545 = "BTO_0004545"
    M_1_COLLECTING_DUCT_CELL = "BTO_0004545"

    # hypopharyngeal squamous cell carcinoma cell line
    BTO_0004546 = "BTO_0004546"
    HYPOPHARYNGEAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0004546"

    # hypopharyngeal squamous cell carcinoma cell
    BTO_0004547 = "BTO_0004547"
    HYPOPHARYNGEAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0004547"

    # deep inguinal lymph node
    BTO_0004548 = "BTO_0004548"
    DEEP_INGUINAL_LYMPH_NODE = "BTO_0004548"

    # superficial inguinal lymph node
    BTO_0004549 = "BTO_0004549"
    SUPERFICIAL_INGUINAL_LYMPH_NODE = "BTO_0004549"

    # proximal deep inguinal lymph node
    BTO_0004550 = "BTO_0004550"
    PROXIMAL_DEEP_INGUINAL_LYMPH_NODE = "BTO_0004550"

    # WT-100 cell
    BTO_0004551 = "BTO_0004551"
    WT_100_CELL = "BTO_0004551"

    # Barrett's epithelial cell line
    BTO_0004552 = "BTO_0004552"
    BARRETT_S_EPITHELIAL_CELL_LINE = "BTO_0004552"

    # E-18 rat primary hippocampal neuron
    BTO_0004553 = "BTO_0004553"
    E_18_RAT_PRIMARY_HIPPOCAMPAL_NEURON = "BTO_0004553"

    # parotid gland duct
    BTO_0004554 = "BTO_0004554"
    PAROTID_GLAND_DUCT = "BTO_0004554"

    # parotid gland duct epithelium
    BTO_0004555 = "BTO_0004555"
    PAROTID_GLAND_DUCT_EPITHELIUM = "BTO_0004555"

    # submandibular gland duct
    BTO_0004556 = "BTO_0004556"
    SUBMANDIBULAR_GLAND_DUCT = "BTO_0004556"

    # submandibular gland duct epithelium
    BTO_0004557 = "BTO_0004557"
    SUBMANDIBULAR_GLAND_DUCT_EPITHELIUM = "BTO_0004557"

    # sublingual gland duct
    BTO_0004558 = "BTO_0004558"
    SUBLINGUAL_GLAND_DUCT = "BTO_0004558"

    # sublingual gland duct epithelium
    BTO_0004559 = "BTO_0004559"
    SUBLINGUAL_GLAND_DUCT_EPITHELIUM = "BTO_0004559"

    # thymic medulla
    BTO_0004560 = "BTO_0004560"
    THYMIC_MEDULLA = "BTO_0004560"

    # thymic stromal cell
    BTO_0004561 = "BTO_0004561"
    THYMIC_STROMAL_CELL = "BTO_0004561"

    # thymic cortical epithelial cell
    BTO_0004562 = "BTO_0004562"
    THYMIC_CORTICAL_EPITHELIAL_CELL = "BTO_0004562"

    # thymic medullary epithelial cell
    BTO_0004563 = "BTO_0004563"
    THYMIC_MEDULLARY_EPITHELIAL_CELL = "BTO_0004563"

    # thymic dendritic cell
    BTO_0004564 = "BTO_0004564"
    THYMIC_DENDRITIC_CELL = "BTO_0004564"

    # thymic medullary epithelium
    BTO_0004565 = "BTO_0004565"
    THYMIC_MEDULLARY_EPITHELIUM = "BTO_0004565"

    # Rb-1 cell
    BTO_0004566 = "BTO_0004566"
    RB_1_CELL = "BTO_0004566"

    # sessile serrated adenoma cell
    BTO_0004567 = "BTO_0004567"
    SESSILE_SERRATED_ADENOMA_CELL = "BTO_0004567"

    # supportive connective tissue
    BTO_0004568 = "BTO_0004568"
    SUPPORTIVE_CONNECTIVE_TISSUE = "BTO_0004568"

    # ovarian fluid
    BTO_0004569 = "BTO_0004569"
    OVARIAN_FLUID = "BTO_0004569"

    # ulcer tissue
    BTO_0004570 = "BTO_0004570"
    ULCER_TISSUE = "BTO_0004570"

    # L3.3 cell
    BTO_0004571 = "BTO_0004571"
    L3_3_CELL = "BTO_0004571"

    # HEP-G2/2.2.1 cell
    BTO_0004572 = "BTO_0004572"
    HEP_G2_2_2_1_CELL = "BTO_0004572"

    # BOSC-23 cell
    BTO_0004573 = "BTO_0004573"
    BOSC_23_CELL = "BTO_0004573"

    # dermal microvascular endothelial cell
    BTO_0004574 = "BTO_0004574"
    DERMAL_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0004574"

    # nephroblastoma cell
    BTO_0004575 = "BTO_0004575"
    NEPHROBLASTOMA_CELL = "BTO_0004575"

    # smooth muscle cell
    BTO_0004576 = "BTO_0004576"
    SMOOTH_MUSCLE_CELL = "BTO_0004576"

    # aortic smooth muscle cell
    BTO_0004577 = "BTO_0004577"
    AORTIC_SMOOTH_MUSCLE_CELL = "BTO_0004577"

    # vascular smooth muscle cell
    BTO_0004578 = "BTO_0004578"
    VASCULAR_SMOOTH_MUSCLE_CELL = "BTO_0004578"

    # parenchyma of thyroid gland
    BTO_0004579 = "BTO_0004579"
    PARENCHYMA_OF_THYROID_GLAND = "BTO_0004579"

    # 862L cell
    BTO_0004580 = "BTO_0004580"
    _862L_CELL = "BTO_0004580"

    # 10/9CRC1 cell
    BTO_0004581 = "BTO_0004581"
    _10_9CRC1_CELL = "BTO_0004581"

    # A31N-ts20 cell
    BTO_0004582 = "BTO_0004582"
    A31N_TS20_CELL = "BTO_0004582"

    # A-704 cell
    BTO_0004583 = "BTO_0004583"
    A_704_CELL = "BTO_0004583"

    # acute nonlymphoblastic leukemia cell
    BTO_0004584 = "BTO_0004584"
    ACUTE_NONLYMPHOBLASTIC_LEUKEMIA_CELL = "BTO_0004584"

    # acute promyelocytic leukemia cell
    BTO_0004585 = "BTO_0004585"
    ACUTE_PROMYELOCYTIC_LEUKEMIA_CELL = "BTO_0004585"

    # alevin
    BTO_0004586 = "BTO_0004586"
    ALEVIN = "BTO_0004586"

    # AT6.1 cell
    BTO_0004587 = "BTO_0004587"
    AT6_1_CELL = "BTO_0004587"

    # BHY cell
    BTO_0004588 = "BTO_0004588"
    BHY_CELL = "BTO_0004588"

    # HN cell
    BTO_0004589 = "BTO_0004589"
    HN_CELL = "BTO_0004589"

    # nasal epithelium cell line
    BTO_0004590 = "BTO_0004590"
    NASAL_EPITHELIUM_CELL_LINE = "BTO_0004590"

    # NHEC cell
    BTO_0004591 = "BTO_0004591"
    NHEC_CELL = "BTO_0004591"

    # bone matrix
    BTO_0004592 = "BTO_0004592"
    BONE_MATRIX = "BTO_0004592"

    # epiblast
    BTO_0004593 = "BTO_0004593"
    EPIBLAST = "BTO_0004593"

    # CWR-22 cell
    BTO_0004594 = "BTO_0004594"
    CWR_22_CELL = "BTO_0004594"

    # D-407 cell
    BTO_0004595 = "BTO_0004595"
    D_407_CELL = "BTO_0004595"

    # garland cell
    BTO_0004596 = "BTO_0004596"
    GARLAND_CELL = "BTO_0004596"

    # nephrocyte
    BTO_0004597 = "BTO_0004597"
    NEPHROCYTE = "BTO_0004597"

    # TE-15 cell
    BTO_0004598 = "BTO_0004598"
    TE_15_CELL = "BTO_0004598"

    # TE-13 cell
    BTO_0004599 = "BTO_0004599"
    TE_13_CELL = "BTO_0004599"

    # TE-8 cell
    BTO_0004600 = "BTO_0004600"
    TE_8_CELL = "BTO_0004600"

    # TE-1 cell
    BTO_0004601 = "BTO_0004601"
    TE_1_CELL = "BTO_0004601"

    # human aortic endothelial cell
    BTO_0004602 = "BTO_0004602"
    HUMAN_AORTIC_ENDOTHELIAL_CELL = "BTO_0004602"

    # HBE cell
    BTO_0004603 = "BTO_0004603"
    HBE_CELL = "BTO_0004603"

    # IEC-18 cell
    BTO_0004604 = "BTO_0004604"
    IEC_18_CELL = "BTO_0004604"

    # U-118MG cell
    BTO_0004605 = "BTO_0004605"
    U_118MG_CELL = "BTO_0004605"

    # MDCK-1 cell
    BTO_0004606 = "BTO_0004606"
    MDCK_1_CELL = "BTO_0004606"

    # MDCK-2 cell
    BTO_0004607 = "BTO_0004607"
    MDCK_2_CELL = "BTO_0004607"

    # Henles loop
    BTO_0004608 = "BTO_0004608"
    HENLES_LOOP = "BTO_0004608"

    # TALH cell
    BTO_0004609 = "BTO_0004609"
    TALH_CELL = "BTO_0004609"

    # Henles loop cell line
    BTO_0004610 = "BTO_0004610"
    HENLES_LOOP_CELL_LINE = "BTO_0004610"

    # SW-900 cell
    BTO_0004611 = "BTO_0004611"
    SW_900_CELL = "BTO_0004611"

    # WM-793B cell
    BTO_0004612 = "BTO_0004612"
    WM_793B_CELL = "BTO_0004612"

    # sebocyte
    BTO_0004613 = "BTO_0004613"
    SEBOCYTE = "BTO_0004613"

    # NOSE1 cell
    BTO_0004614 = "BTO_0004614"
    NOSE1_CELL = "BTO_0004614"

    # regulatory dendritic cell
    BTO_0004615 = "BTO_0004615"
    REGULATORY_DENDRITIC_CELL = "BTO_0004615"

    # stria terminalis
    BTO_0004616 = "BTO_0004616"
    STRIA_TERMINALIS = "BTO_0004616"

    # mucilage
    BTO_0004617 = "BTO_0004617"
    MUCILAGE = "BTO_0004617"

    # T-289 cell
    BTO_0004618 = "BTO_0004618"
    T_289_CELL = "BTO_0004618"

    # OCI-AML2 cell
    BTO_0004619 = "BTO_0004619"
    OCI_AML2_CELL = "BTO_0004619"

    # OCI-AML3 cell
    BTO_0004620 = "BTO_0004620"
    OCI_AML3_CELL = "BTO_0004620"

    # OCI-AML5 cell
    BTO_0004621 = "BTO_0004621"
    OCI_AML5_CELL = "BTO_0004621"

    # OCI-M1 cell
    BTO_0004622 = "BTO_0004622"
    OCI_M1_CELL = "BTO_0004622"

    # OCI-M2 cell
    BTO_0004623 = "BTO_0004623"
    OCI_M2_CELL = "BTO_0004623"

    # YN-1 cell
    BTO_0004624 = "BTO_0004624"
    YN_1_CELL = "BTO_0004624"

    # plasmacytoid dendritic cell
    BTO_0004625 = "BTO_0004625"
    PLASMACYTOID_DENDRITIC_CELL = "BTO_0004625"

    # carotid artery endothelium
    BTO_0004626 = "BTO_0004626"
    CAROTID_ARTERY_ENDOTHELIUM = "BTO_0004626"

    # carotid artery endothelial cell
    BTO_0004627 = "BTO_0004627"
    CAROTID_ARTERY_ENDOTHELIAL_CELL = "BTO_0004627"

    # aortic valve
    BTO_0004628 = "BTO_0004628"
    AORTIC_VALVE = "BTO_0004628"

    # metaphloem
    BTO_0004629 = "BTO_0004629"
    METAPHLOEM = "BTO_0004629"

    # middle midgut
    BTO_0004630 = "BTO_0004630"
    MIDDLE_MIDGUT = "BTO_0004630"

    # glomerular endothelium
    BTO_0004631 = "BTO_0004631"
    GLOMERULAR_ENDOTHELIUM = "BTO_0004631"

    # glomerular endothelial cell
    BTO_0004632 = "BTO_0004632"
    GLOMERULAR_ENDOTHELIAL_CELL = "BTO_0004632"

    # invasive breast apocrine carcinoma cell
    BTO_0004633 = "BTO_0004633"
    INVASIVE_BREAST_APOCRINE_CARCINOMA_CELL = "BTO_0004633"

    # thoracico-abdominal ganglion
    BTO_0004634 = "BTO_0004634"
    THORACICO_ABDOMINAL_GANGLION = "BTO_0004634"

    # 29-13 cell
    BTO_0004635 = "BTO_0004635"
    _29_13_CELL = "BTO_0004635"

    # urinary bladder endothelium
    BTO_0004636 = "BTO_0004636"
    URINARY_BLADDER_ENDOTHELIUM = "BTO_0004636"

    # urinary bladder endothelial cell
    BTO_0004637 = "BTO_0004637"
    URINARY_BLADDER_ENDOTHELIAL_CELL = "BTO_0004637"

    # peribronchial gland
    BTO_0004638 = "BTO_0004638"
    PERIBRONCHIAL_GLAND = "BTO_0004638"

    # TT2 ES cell
    BTO_0004639 = "BTO_0004639"
    TT2_ES_CELL = "BTO_0004639"

    # FD-2 cell
    BTO_0004640 = "BTO_0004640"
    FD_2_CELL = "BTO_0004640"

    # tracheal cell line
    BTO_0004641 = "BTO_0004641"
    TRACHEAL_CELL_LINE = "BTO_0004641"

    # abductor
    BTO_0004642 = "BTO_0004642"
    ABDUCTOR = "BTO_0004642"

    # culture condition:1-naphthoic acid-grown cell
    BTO_0004643 = "BTO_0004643"
    CULTURE_CONDITION_1_NAPHTHOIC_ACID_GROWN_CELL = "BTO_0004643"

    # culture condition:acenaphthylene-grown cell
    BTO_0004644 = "BTO_0004644"
    CULTURE_CONDITION_ACENAPHTHYLENE_GROWN_CELL = "BTO_0004644"

    # culture condition:cocaine-grown cell
    BTO_0004645 = "BTO_0004645"
    CULTURE_CONDITION_COCAINE_GROWN_CELL = "BTO_0004645"

    # culture condition:phenanthrene-grown cell
    BTO_0004646 = "BTO_0004646"
    CULTURE_CONDITION_PHENANTHRENE_GROWN_CELL = "BTO_0004646"

    # culture condition:phosphonopyruvate-grown cell
    BTO_0004647 = "BTO_0004647"
    CULTURE_CONDITION_PHOSPHONOPYRUVATE_GROWN_CELL = "BTO_0004647"

    # culture condition:sucrose-grown cell
    BTO_0004648 = "BTO_0004648"
    CULTURE_CONDITION_SUCROSE_GROWN_CELL = "BTO_0004648"

    # fin
    BTO_0004649 = "BTO_0004649"
    FIN = "BTO_0004649"

    # dorsal fin
    BTO_0004650 = "BTO_0004650"
    DORSAL_FIN = "BTO_0004650"

    # pelvic fin
    BTO_0004651 = "BTO_0004651"
    PELVIC_FIN = "BTO_0004651"

    # anal fin
    BTO_0004652 = "BTO_0004652"
    ANAL_FIN = "BTO_0004652"

    # pectoral fin
    BTO_0004653 = "BTO_0004653"
    PECTORAL_FIN = "BTO_0004653"

    # Tet21N cell
    BTO_0004654 = "BTO_0004654"
    TET21N_CELL = "BTO_0004654"

    # SK-ChA-1 cell
    BTO_0004655 = "BTO_0004655"
    SK_CHA_1_CELL = "BTO_0004655"

    # follicular lymphoma cell
    BTO_0004656 = "BTO_0004656"
    FOLLICULAR_LYMPHOMA_CELL = "BTO_0004656"

    # premonocyte
    BTO_0004657 = "BTO_0004657"
    PREMONOCYTE = "BTO_0004657"

    # imaginal disc
    BTO_0004658 = "BTO_0004658"
    IMAGINAL_DISC = "BTO_0004658"

    # exoskeleton
    BTO_0004659 = "BTO_0004659"
    EXOSKELETON = "BTO_0004659"

    # human amniotic epithelial cell
    BTO_0004660 = "BTO_0004660"
    HUMAN_AMNIOTIC_EPITHELIAL_CELL = "BTO_0004660"

    # iliac artery endothelium
    BTO_0004661 = "BTO_0004661"
    ILIAC_ARTERY_ENDOTHELIUM = "BTO_0004661"

    # iliac artery endothelial cell
    BTO_0004662 = "BTO_0004662"
    ILIAC_ARTERY_ENDOTHELIAL_CELL = "BTO_0004662"

    # iliac artery endothelial cell line
    BTO_0004663 = "BTO_0004663"
    ILIAC_ARTERY_ENDOTHELIAL_CELL_LINE = "BTO_0004663"

    # human iliac artery endothelial cell
    BTO_0004664 = "BTO_0004664"
    HUMAN_ILIAC_ARTERY_ENDOTHELIAL_CELL = "BTO_0004664"

    # iliac artery
    BTO_0004665 = "BTO_0004665"
    ILIAC_ARTERY = "BTO_0004665"

    # external iliac artery
    BTO_0004666 = "BTO_0004666"
    EXTERNAL_ILIAC_ARTERY = "BTO_0004666"

    # internal iliac artery
    BTO_0004667 = "BTO_0004667"
    INTERNAL_ILIAC_ARTERY = "BTO_0004667"

    # hand
    BTO_0004668 = "BTO_0004668"
    HAND = "BTO_0004668"

    # finger
    BTO_0004669 = "BTO_0004669"
    FINGER = "BTO_0004669"

    # interdigit
    BTO_0004670 = "BTO_0004670"
    INTERDIGIT = "BTO_0004670"

    # hair medulla
    BTO_0004671 = "BTO_0004671"
    HAIR_MEDULLA = "BTO_0004671"

    # hair shaft
    BTO_0004672 = "BTO_0004672"
    HAIR_SHAFT = "BTO_0004672"

    # dorsal aorta
    BTO_0004673 = "BTO_0004673"
    DORSAL_AORTA = "BTO_0004673"

    # ventral aorta
    BTO_0004674 = "BTO_0004674"
    VENTRAL_AORTA = "BTO_0004674"

    # regio occipitalis capitis
    BTO_0004675 = "BTO_0004675"
    REGIO_OCCIPITALIS_CAPITIS = "BTO_0004675"

    # cerebral peduncle
    BTO_0004676 = "BTO_0004676"
    CEREBRAL_PEDUNCLE = "BTO_0004676"

    # basis pedunculi cerebri
    BTO_0004677 = "BTO_0004677"
    BASIS_PEDUNCULI_CEREBRI = "BTO_0004677"

    # regio frontalis capitis
    BTO_0004678 = "BTO_0004678"
    REGIO_FRONTALIS_CAPITIS = "BTO_0004678"

    # capillary pericyte
    BTO_0004679 = "BTO_0004679"
    CAPILLARY_PERICYTE = "BTO_0004679"

    # stratum basale
    BTO_0004680 = "BTO_0004680"
    STRATUM_BASALE = "BTO_0004680"

    # bursa copulatrix
    BTO_0004681 = "BTO_0004681"
    BURSA_COPULATRIX = "BTO_0004681"

    # gential atrium
    BTO_0004682 = "BTO_0004682"
    GENTIAL_ATRIUM = "BTO_0004682"

    # genital chamber
    BTO_0004683 = "BTO_0004683"
    GENITAL_CHAMBER = "BTO_0004683"

    # genital pore
    BTO_0004684 = "BTO_0004684"
    GENITAL_PORE = "BTO_0004684"

    # bony labyrinth
    BTO_0004685 = "BTO_0004685"
    BONY_LABYRINTH = "BTO_0004685"

    # cochlear labyrinth
    BTO_0004686 = "BTO_0004686"
    COCHLEAR_LABYRINTH = "BTO_0004686"

    # orbit
    BTO_0004687 = "BTO_0004687"
    ORBIT = "BTO_0004687"

    # regio orbitalis
    BTO_0004688 = "BTO_0004688"
    REGIO_ORBITALIS = "BTO_0004688"

    # external gill
    BTO_0004689 = "BTO_0004689"
    EXTERNAL_GILL = "BTO_0004689"

    # arterial system
    BTO_0004690 = "BTO_0004690"
    ARTERIAL_SYSTEM = "BTO_0004690"

    # hippocampus minor
    BTO_0004691 = "BTO_0004691"
    HIPPOCAMPUS_MINOR = "BTO_0004691"

    # venous system
    BTO_0004692 = "BTO_0004692"
    VENOUS_SYSTEM = "BTO_0004692"

    # regio parietalis capitis
    BTO_0004693 = "BTO_0004693"
    REGIO_PARIETALIS_CAPITIS = "BTO_0004693"

    # rectal sac
    BTO_0004694 = "BTO_0004694"
    RECTAL_SAC = "BTO_0004694"

    # aortic root
    BTO_0004695 = "BTO_0004695"
    AORTIC_ROOT = "BTO_0004695"

    # external carotid artery
    BTO_0004696 = "BTO_0004696"
    EXTERNAL_CAROTID_ARTERY = "BTO_0004696"

    # internal carotid artery
    BTO_0004697 = "BTO_0004697"
    INTERNAL_CAROTID_ARTERY = "BTO_0004697"

    # regio oralis
    BTO_0004698 = "BTO_0004698"
    REGIO_ORALIS = "BTO_0004698"

    # posterior pharynx
    BTO_0004699 = "BTO_0004699"
    POSTERIOR_PHARYNX = "BTO_0004699"

    # anterior pharynx
    BTO_0004700 = "BTO_0004700"
    ANTERIOR_PHARYNX = "BTO_0004700"

    # dorsal striatum
    BTO_0004701 = "BTO_0004701"
    DORSAL_STRIATUM = "BTO_0004701"

    # ventral striatum
    BTO_0004702 = "BTO_0004702"
    VENTRAL_STRIATUM = "BTO_0004702"

    # striate cortex
    BTO_0004703 = "BTO_0004703"
    STRIATE_CORTEX = "BTO_0004703"

    # extrastriate cortex
    BTO_0004704 = "BTO_0004704"
    EXTRASTRIATE_CORTEX = "BTO_0004704"

    # connecting stalk
    BTO_0004705 = "BTO_0004705"
    CONNECTING_STALK = "BTO_0004705"

    # ankle joint
    BTO_0004706 = "BTO_0004706"
    ANKLE_JOINT = "BTO_0004706"

    # hinge joint
    BTO_0004707 = "BTO_0004707"
    HINGE_JOINT = "BTO_0004707"

    # thyroid follicle
    BTO_0004708 = "BTO_0004708"
    THYROID_FOLLICLE = "BTO_0004708"

    # thyroid primordium
    BTO_0004709 = "BTO_0004709"
    THYROID_PRIMORDIUM = "BTO_0004709"

    # tunica interna bulbi
    BTO_0004710 = "BTO_0004710"
    TUNICA_INTERNA_BULBI = "BTO_0004710"

    # head capsule
    BTO_0004711 = "BTO_0004711"
    HEAD_CAPSULE = "BTO_0004711"

    # parathyroid hormone secreting cell
    BTO_0004712 = "BTO_0004712"
    PARATHYROID_HORMONE_SECRETING_CELL = "BTO_0004712"

    # larval ventral ganglion
    BTO_0004713 = "BTO_0004713"
    LARVAL_VENTRAL_GANGLION = "BTO_0004713"

    # palatine tonsil
    BTO_0004714 = "BTO_0004714"
    PALATINE_TONSIL = "BTO_0004714"

    # nasopharyngeal tonsil
    BTO_0004715 = "BTO_0004715"
    NASOPHARYNGEAL_TONSIL = "BTO_0004715"

    # null cell
    BTO_0004716 = "BTO_0004716"
    NULL_CELL = "BTO_0004716"

    # large granular lymphocyte
    BTO_0004717 = "BTO_0004717"
    LARGE_GRANULAR_LYMPHOCYTE = "BTO_0004717"

    # breast lobe
    BTO_0004718 = "BTO_0004718"
    BREAST_LOBE = "BTO_0004718"

    # excretory canal cell
    BTO_0004719 = "BTO_0004719"
    EXCRETORY_CANAL_CELL = "BTO_0004719"

    # mural cell
    BTO_0004720 = "BTO_0004720"
    MURAL_CELL = "BTO_0004720"

    # myeloid dendritic cell
    BTO_0004721 = "BTO_0004721"
    MYELOID_DENDRITIC_CELL = "BTO_0004721"

    # plasmacytoid T-lymphocyte
    BTO_0004722 = "BTO_0004722"
    PLASMACYTOID_T_LYMPHOCYTE = "BTO_0004722"

    # lymphoid dendritic cell
    BTO_0004723 = "BTO_0004723"
    LYMPHOID_DENDRITIC_CELL = "BTO_0004723"

    # animal cap
    BTO_0004724 = "BTO_0004724"
    ANIMAL_CAP = "BTO_0004724"

    # embryonic fibroblast
    BTO_0004725 = "BTO_0004725"
    EMBRYONIC_FIBROBLAST = "BTO_0004725"

    # embryonic brain
    BTO_0004726 = "BTO_0004726"
    EMBRYONIC_BRAIN = "BTO_0004726"

    # larval brain
    BTO_0004727 = "BTO_0004727"
    LARVAL_BRAIN = "BTO_0004727"

    # rheumatoid arthritis disease specific synovial fluid
    BTO_0004728 = "BTO_0004728"
    RHEUMATOID_ARTHRITIS_DISEASE_SPECIFIC_SYNOVIAL_FLUID = "BTO_0004728"

    # peripheral blood lymphocyte
    BTO_0004729 = "BTO_0004729"
    PERIPHERAL_BLOOD_LYMPHOCYTE = "BTO_0004729"

    # myeloid progenitor cell
    BTO_0004730 = "BTO_0004730"
    MYELOID_PROGENITOR_CELL = "BTO_0004730"

    # lymphoid progenitor cell
    BTO_0004731 = "BTO_0004731"
    LYMPHOID_PROGENITOR_CELL = "BTO_0004731"

    # bone marrow-derived macrophage
    BTO_0004732 = "BTO_0004732"
    BONE_MARROW_DERIVED_MACROPHAGE = "BTO_0004732"

    # gravid adult
    BTO_0004733 = "BTO_0004733"
    GRAVID_ADULT = "BTO_0004733"

    # HBL-100 cell
    BTO_0004734 = "BTO_0004734"
    HBL_100_CELL = "BTO_0004734"

    # brainstem glioma cell
    BTO_0004735 = "BTO_0004735"
    BRAINSTEM_GLIOMA_CELL = "BTO_0004735"

    # B-CPAP cell
    BTO_0004736 = "BTO_0004736"
    B_CPAP_CELL = "BTO_0004736"

    # AU-565 cell
    BTO_0004737 = "BTO_0004737"
    AU_565_CELL = "BTO_0004737"

    # CFPAC-1 cell
    BTO_0004738 = "BTO_0004738"
    CFPAC_1_CELL = "BTO_0004738"

    # CGTH-W3 cell
    BTO_0004739 = "BTO_0004739"
    CGTH_W3_CELL = "BTO_0004739"

    # CGTH-W1 cell
    BTO_0004740 = "BTO_0004740"
    CGTH_W1_CELL = "BTO_0004740"

    # CGTH-W2 cell
    BTO_0004741 = "BTO_0004741"
    CGTH_W2_CELL = "BTO_0004741"

    # HCT-115 cell
    BTO_0004742 = "BTO_0004742"
    HCT_115_CELL = "BTO_0004742"

    # HCT-166 cell
    BTO_0004743 = "BTO_0004743"
    HCT_166_CELL = "BTO_0004743"

    # hair cell
    BTO_0004744 = "BTO_0004744"
    HAIR_CELL = "BTO_0004744"

    # INA-6 cell
    BTO_0004745 = "BTO_0004745"
    INA_6_CELL = "BTO_0004745"

    # cecum cancer cell line
    BTO_0004746 = "BTO_0004746"
    CECUM_CANCER_CELL_LINE = "BTO_0004746"

    # NCI-H716 cell
    BTO_0004747 = "BTO_0004747"
    NCI_H716_CELL = "BTO_0004747"

    # metula
    BTO_0004748 = "BTO_0004748"
    METULA = "BTO_0004748"

    # phialide
    BTO_0004749 = "BTO_0004749"
    PHIALIDE = "BTO_0004749"

    # 129S6 cell
    BTO_0004750 = "BTO_0004750"
    _129S6_CELL = "BTO_0004750"

    # 1C9 cell
    BTO_0004751 = "BTO_0004751"
    _1C9_CELL = "BTO_0004751"

    # adipose-derived stromal cell
    BTO_0004752 = "BTO_0004752"
    ADIPOSE_DERIVED_STROMAL_CELL = "BTO_0004752"

    # XP-V XP30RO cell
    BTO_0004753 = "BTO_0004753"
    XP_V_XP30RO_CELL = "BTO_0004753"

    # VERO-76 cell
    BTO_0004754 = "BTO_0004754"
    VERO_76_CELL = "BTO_0004754"

    # VERO C1008 cell
    BTO_0004755 = "BTO_0004755"
    VERO_C1008_CELL = "BTO_0004755"

    # venous endothelium
    BTO_0004756 = "BTO_0004756"
    VENOUS_ENDOTHELIUM = "BTO_0004756"

    # arterial endothelium
    BTO_0004757 = "BTO_0004757"
    ARTERIAL_ENDOTHELIUM = "BTO_0004757"

    # arterial endothelial cell
    BTO_0004758 = "BTO_0004758"
    ARTERIAL_ENDOTHELIAL_CELL = "BTO_0004758"

    # venous endothelial cell
    BTO_0004759 = "BTO_0004759"
    VENOUS_ENDOTHELIAL_CELL = "BTO_0004759"

    # TF-1 cell
    BTO_0004760 = "BTO_0004760"
    TF_1_CELL = "BTO_0004760"

    # TF-1 BCR-ABL cell
    BTO_0004761 = "BTO_0004761"
    TF_1_BCR_ABL_CELL = "BTO_0004761"

    # TSM1 cell
    BTO_0004762 = "BTO_0004762"
    TSM1_CELL = "BTO_0004762"

    # V866 cell
    BTO_0004763 = "BTO_0004763"
    V866_CELL = "BTO_0004763"

    # V400 cell
    BTO_0004764 = "BTO_0004764"
    V400_CELL = "BTO_0004764"

    # UKE-1 cell
    BTO_0004765 = "BTO_0004765"
    UKE_1_CELL = "BTO_0004765"

    # SET-2 cell
    BTO_0004766 = "BTO_0004766"
    SET_2_CELL = "BTO_0004766"

    # MB-02 cell
    BTO_0004767 = "BTO_0004767"
    MB_02_CELL = "BTO_0004767"

    # MUTZ-8 cell
    BTO_0004768 = "BTO_0004768"
    MUTZ_8_CELL = "BTO_0004768"

    # teratocyte
    BTO_0004769 = "BTO_0004769"
    TERATOCYTE = "BTO_0004769"

    # TAD-2 cell
    BTO_0004770 = "BTO_0004770"
    TAD_2_CELL = "BTO_0004770"

    # NPA cell
    BTO_0004771 = "BTO_0004771"
    NPA_CELL = "BTO_0004771"

    # WRO cell
    BTO_0004772 = "BTO_0004772"
    WRO_CELL = "BTO_0004772"

    # trophoblast stem cell line
    BTO_0004773 = "BTO_0004773"
    TROPHOBLAST_STEM_CELL_LINE = "BTO_0004773"

    # trophoblast stem cell
    BTO_0004774 = "BTO_0004774"
    TROPHOBLAST_STEM_CELL = "BTO_0004774"

    # SUP-M2 cell
    BTO_0004775 = "BTO_0004775"
    SUP_M2_CELL = "BTO_0004775"

    # striatonigral neuron
    BTO_0004776 = "BTO_0004776"
    STRIATONIGRAL_NEURON = "BTO_0004776"

    # RSC96 cell
    BTO_0004777 = "BTO_0004777"
    RSC96_CELL = "BTO_0004777"

    # medium spiny neuron
    BTO_0004778 = "BTO_0004778"
    MEDIUM_SPINY_NEURON = "BTO_0004778"

    # soft tissue sarcoma cell
    BTO_0004779 = "BTO_0004779"
    SOFT_TISSUE_SARCOMA_CELL = "BTO_0004779"

    # soft tissue sarcoma cell line
    BTO_0004780 = "BTO_0004780"
    SOFT_TISSUE_SARCOMA_CELL_LINE = "BTO_0004780"

    # SK-RC-26B cell
    BTO_0004781 = "BTO_0004781"
    SK_RC_26B_CELL = "BTO_0004781"

    # SK-N-BE(2)C cell
    BTO_0004782 = "BTO_0004782"
    SK_N_BE_2_C_CELL = "BTO_0004782"

    # SeAx cell
    BTO_0004783 = "BTO_0004783"
    SEAX_CELL = "BTO_0004783"

    # HFF-1 cell
    BTO_0004784 = "BTO_0004784"
    HFF_1_CELL = "BTO_0004784"

    # Ewing's sarcoma family tumor cell line
    BTO_0004785 = "BTO_0004785"
    EWING_S_SARCOMA_FAMILY_TUMOR_CELL_LINE = "BTO_0004785"

    # SCMC-ES1 cell
    BTO_0004786 = "BTO_0004786"
    SCMC_ES1_CELL = "BTO_0004786"

    # SK-N-LO cell
    BTO_0004787 = "BTO_0004787"
    SK_N_LO_CELL = "BTO_0004787"

    # KP-EW-MS cell
    BTO_0004788 = "BTO_0004788"
    KP_EW_MS_CELL = "BTO_0004788"

    # ruminal fluid
    BTO_0004789 = "BTO_0004789"
    RUMINAL_FLUID = "BTO_0004789"

    # hTERT-RPE1 cell
    BTO_0004790 = "BTO_0004790"
    HTERT_RPE1_CELL = "BTO_0004790"

    # root primordium
    BTO_0004791 = "BTO_0004791"
    ROOT_PRIMORDIUM = "BTO_0004791"

    # RHEK-1 cell
    BTO_0004792 = "BTO_0004792"
    RHEK_1_CELL = "BTO_0004792"

    # TC1 cell
    BTO_0004793 = "BTO_0004793"
    TC1_CELL = "BTO_0004793"

    # TC2 cell
    BTO_0004794 = "BTO_0004794"
    TC2_CELL = "BTO_0004794"

    # JHU-1 cell
    BTO_0004795 = "BTO_0004795"
    JHU_1_CELL = "BTO_0004795"

    # 253J cell
    BTO_0004796 = "BTO_0004796"
    _253J_CELL = "BTO_0004796"

    # accessory olfactory bulb
    BTO_0004797 = "BTO_0004797"
    ACCESSORY_OLFACTORY_BULB = "BTO_0004797"

    # accessory sex gland
    BTO_0004798 = "BTO_0004798"
    ACCESSORY_SEX_GLAND = "BTO_0004798"

    # LNCaP-AI cell
    BTO_0004799 = "BTO_0004799"
    LNCAP_AI_CELL = "BTO_0004799"

    # amnioserosa
    BTO_0004800 = "BTO_0004800"
    AMNIOSEROSA = "BTO_0004800"

    # BG3A-C2 cell
    BTO_0004801 = "BTO_0004801"
    BG3A_C2_CELL = "BTO_0004801"

    # OCL-1 cell
    BTO_0004802 = "BTO_0004802"
    OCL_1_CELL = "BTO_0004802"

    # buccal epithelium
    BTO_0004803 = "BTO_0004803"
    BUCCAL_EPITHELIUM = "BTO_0004803"

    # buccal epithelial cell
    BTO_0004804 = "BTO_0004804"
    BUCCAL_EPITHELIAL_CELL = "BTO_0004804"

    # C666-1 cell
    BTO_0004805 = "BTO_0004805"
    C666_1_CELL = "BTO_0004805"

    # CHO-91-47-67 cell
    BTO_0004806 = "BTO_0004806"
    CHO_91_47_67_CELL = "BTO_0004806"

    # CHO-91-22-47-67 cell
    BTO_0004807 = "BTO_0004807"
    CHO_91_22_47_67_CELL = "BTO_0004807"

    # CHO-91-22 cell
    BTO_0004808 = "BTO_0004808"
    CHO_91_22_CELL = "BTO_0004808"

    # CHO-91 cell
    BTO_0004809 = "BTO_0004809"
    CHO_91_CELL = "BTO_0004809"

    # CHO-22 cell
    BTO_0004810 = "BTO_0004810"
    CHO_22_CELL = "BTO_0004810"

    # Clara cell
    BTO_0004811 = "BTO_0004811"
    CLARA_CELL = "BTO_0004811"

    # dermal dendritic cell
    BTO_0004812 = "BTO_0004812"
    DERMAL_DENDRITIC_CELL = "BTO_0004812"

    # DMS-114 cell
    BTO_0004813 = "BTO_0004813"
    DMS_114_CELL = "BTO_0004813"

    # DT-40 cell
    BTO_0004814 = "BTO_0004814"
    DT_40_CELL = "BTO_0004814"

    # ER-1 cell
    BTO_0004815 = "BTO_0004815"
    ER_1_CELL = "BTO_0004815"

    # ERpP cell
    BTO_0004816 = "BTO_0004816"
    ERPP_CELL = "BTO_0004816"

    # extraradical hypha
    BTO_0004817 = "BTO_0004817"
    EXTRARADICAL_HYPHA = "BTO_0004817"

    # FOM71 cell
    BTO_0004818 = "BTO_0004818"
    FOM71_CELL = "BTO_0004818"

    # FOM78 cell
    BTO_0004819 = "BTO_0004819"
    FOM78_CELL = "BTO_0004819"

    # NHEM693 cell
    BTO_0004820 = "BTO_0004820"
    NHEM693_CELL = "BTO_0004820"

    # NHEM2493 cell
    BTO_0004821 = "BTO_0004821"
    NHEM2493_CELL = "BTO_0004821"

    # germ tube
    BTO_0004822 = "BTO_0004822"
    GERM_TUBE = "BTO_0004822"

    # NCI-H1355 cell
    BTO_0004823 = "BTO_0004823"
    NCI_H1355_CELL = "BTO_0004823"

    # NCI-H1975 cell
    BTO_0004824 = "BTO_0004824"
    NCI_H1975_CELL = "BTO_0004824"

    # NCI-H524 cell
    BTO_0004825 = "BTO_0004825"
    NCI_H524_CELL = "BTO_0004825"

    # HFF2/T cell
    BTO_0004826 = "BTO_0004826"
    HFF2_T_CELL = "BTO_0004826"

    # hFOB cell
    BTO_0004827 = "BTO_0004827"
    HFOB_CELL = "BTO_0004827"

    # HGC-27 cell
    BTO_0004828 = "BTO_0004828"
    HGC_27_CELL = "BTO_0004828"

    # HOB-c cell
    BTO_0004829 = "BTO_0004829"
    HOB_C_CELL = "BTO_0004829"

    # epidermal cell line
    BTO_0004830 = "BTO_0004830"
    EPIDERMAL_CELL_LINE = "BTO_0004830"

    # JB6 cell
    BTO_0004831 = "BTO_0004831"
    JB6_CELL = "BTO_0004831"

    # L56Br-C1 cell
    BTO_0004832 = "BTO_0004832"
    L56BR_C1_CELL = "BTO_0004832"

    # large cell neuroendocrine carcinoma cell
    BTO_0004833 = "BTO_0004833"
    LARGE_CELL_NEUROENDOCRINE_CARCINOMA_CELL = "BTO_0004833"

    # middle frontal gyrus
    BTO_0004834 = "BTO_0004834"
    MIDDLE_FRONTAL_GYRUS = "BTO_0004834"

    # inferior frontal gyrus
    BTO_0004835 = "BTO_0004835"
    INFERIOR_FRONTAL_GYRUS = "BTO_0004835"

    # superior frontal gyrus
    BTO_0004836 = "BTO_0004836"
    SUPERIOR_FRONTAL_GYRUS = "BTO_0004836"

    # MRC5-SV cell
    BTO_0004837 = "BTO_0004837"
    MRC5_SV_CELL = "BTO_0004837"

    # muscular coat
    BTO_0004838 = "BTO_0004838"
    MUSCULAR_COAT = "BTO_0004838"

    # muscularis mucosa
    BTO_0004839 = "BTO_0004839"
    MUSCULARIS_MUCOSA = "BTO_0004839"

    # OCL-3 cell
    BTO_0004840 = "BTO_0004840"
    OCL_3_CELL = "BTO_0004840"

    # UCP-3 cell
    BTO_0004841 = "BTO_0004841"
    UCP_3_CELL = "BTO_0004841"

    # MyLa 2039 cell
    BTO_0004842 = "BTO_0004842"
    MYLA_2039_CELL = "BTO_0004842"

    # MyLa 2059 cell
    BTO_0004843 = "BTO_0004843"
    MYLA_2059_CELL = "BTO_0004843"

    # NG2 cell
    BTO_0004844 = "BTO_0004844"
    NG2_CELL = "BTO_0004844"

    # NHOst cell
    BTO_0004845 = "BTO_0004845"
    NHOST_CELL = "BTO_0004845"

    # OCUT-1 cell
    BTO_0004846 = "BTO_0004846"
    OCUT_1_CELL = "BTO_0004846"

    # ONCO-DG1 cell
    BTO_0004847 = "BTO_0004847"
    ONCO_DG1_CELL = "BTO_0004847"

    # PaCa-44 cell
    BTO_0004848 = "BTO_0004848"
    PACA_44_CELL = "BTO_0004848"

    # pharyngeal gland
    BTO_0004849 = "BTO_0004849"
    PHARYNGEAL_GLAND = "BTO_0004849"

    # bone marrow cell
    BTO_0004850 = "BTO_0004850"
    BONE_MARROW_CELL = "BTO_0004850"

    # mammary ductal carcinoma cell
    BTO_0004851 = "BTO_0004851"
    MAMMARY_DUCTAL_CARCINOMA_CELL = "BTO_0004851"

    # OV-90 cell
    BTO_0004852 = "BTO_0004852"
    OV_90_CELL = "BTO_0004852"

    # PC-3H cell
    BTO_0004853 = "BTO_0004853"
    PC_3H_CELL = "BTO_0004853"

    # PK-1 cell
    BTO_0004854 = "BTO_0004854"
    PK_1_CELL = "BTO_0004854"

    # PK-8 cell
    BTO_0004855 = "BTO_0004855"
    PK_8_CELL = "BTO_0004855"

    # pancreaticobiliary cancer cell
    BTO_0004856 = "BTO_0004856"
    PANCREATICOBILIARY_CANCER_CELL = "BTO_0004856"

    # ookinete
    BTO_0004857 = "BTO_0004857"
    OOKINETE = "BTO_0004857"

    # ACT-1 cell
    BTO_0004858 = "BTO_0004858"
    ACT_1_CELL = "BTO_0004858"

    # Nthy-ori 3-1 cell
    BTO_0004859 = "BTO_0004859"
    NTHY_ORI_3_1_CELL = "BTO_0004859"

    # GaMG cell
    BTO_0004860 = "BTO_0004860"
    GAMG_CELL = "BTO_0004860"

    # spiral organ cell line
    BTO_0004861 = "BTO_0004861"
    SPIRAL_ORGAN_CELL_LINE = "BTO_0004861"

    # HEI-OC1 cell
    BTO_0004862 = "BTO_0004862"
    HEI_OC1_CELL = "BTO_0004862"

    # HLCC cell
    BTO_0004863 = "BTO_0004863"
    HLCC_CELL = "BTO_0004863"

    # HMC cell
    BTO_0004864 = "BTO_0004864"
    HMC_CELL = "BTO_0004864"

    # Human-7 cell
    BTO_0004865 = "BTO_0004865"
    HUMAN_7_CELL = "BTO_0004865"

    # LiM-6 cell
    BTO_0004866 = "BTO_0004866"
    LIM_6_CELL = "BTO_0004866"

    # Sup-M2-TS cell
    BTO_0004867 = "BTO_0004867"
    SUP_M2_TS_CELL = "BTO_0004867"

    # anaplastic large cell lymphoma cell line
    BTO_0004868 = "BTO_0004868"
    ANAPLASTIC_LARGE_CELL_LYMPHOMA_CELL_LINE = "BTO_0004868"

    # Mac-1 cell
    BTO_0004869 = "BTO_0004869"
    MAC_1_CELL = "BTO_0004869"

    # MOLT cell
    BTO_0004870 = "BTO_0004870"
    MOLT_CELL = "BTO_0004870"

    # NB-39 cell
    BTO_0004871 = "BTO_0004871"
    NB_39_CELL = "BTO_0004871"

    # NCR-EW2 cell
    BTO_0004872 = "BTO_0004872"
    NCR_EW2_CELL = "BTO_0004872"

    # UT-SCC-118 cell
    BTO_0004873 = "BTO_0004873"
    UT_SCC_118_CELL = "BTO_0004873"

    # non-root-hair cell
    BTO_0004874 = "BTO_0004874"
    NON_ROOT_HAIR_CELL = "BTO_0004874"

    # labellum
    BTO_0004875 = "BTO_0004875"
    LABELLUM = "BTO_0004875"

    # distal tip
    BTO_0004876 = "BTO_0004876"
    DISTAL_TIP = "BTO_0004876"

    # distal tip cell
    BTO_0004877 = "BTO_0004877"
    DISTAL_TIP_CELL = "BTO_0004877"

    # enteric muscle
    BTO_0004878 = "BTO_0004878"
    ENTERIC_MUSCLE = "BTO_0004878"

    # Tu-132 cell
    BTO_0004879 = "BTO_0004879"
    TU_132_CELL = "BTO_0004879"

    # Tu-113 cell
    BTO_0004880 = "BTO_0004880"
    TU_113_CELL = "BTO_0004880"

    # parotid gland tumor cell
    BTO_0004881 = "BTO_0004881"
    PAROTID_GLAND_TUMOR_CELL = "BTO_0004881"

    # ventral midbrain
    BTO_0004882 = "BTO_0004882"
    VENTRAL_MIDBRAIN = "BTO_0004882"

    # cystadenocarcinoma cell line
    BTO_0004883 = "BTO_0004883"
    CYSTADENOCARCINOMA_CELL_LINE = "BTO_0004883"

    # QZG cell
    BTO_0004884 = "BTO_0004884"
    QZG_CELL = "BTO_0004884"

    # OSA-344 cell
    BTO_0004885 = "BTO_0004885"
    OSA_344_CELL = "BTO_0004885"

    # PC-10 cell
    BTO_0004886 = "BTO_0004886"
    PC_10_CELL = "BTO_0004886"

    # ACC-LC-319 cell
    BTO_0004887 = "BTO_0004887"
    ACC_LC_319_CELL = "BTO_0004887"

    # TC-1 cell
    BTO_0004888 = "BTO_0004888"
    TC_1_CELL = "BTO_0004888"

    # BM-314 cell
    BTO_0004889 = "BTO_0004889"
    BM_314_CELL = "BTO_0004889"

    # CHCY-1 cell
    BTO_0004890 = "BTO_0004890"
    CHCY_1_CELL = "BTO_0004890"

    # CH-27 cell
    BTO_0004891 = "BTO_0004891"
    CH_27_CELL = "BTO_0004891"

    # SLT4 cell
    BTO_0004892 = "BTO_0004892"
    SLT4_CELL = "BTO_0004892"

    # 253J laval cell
    BTO_0004893 = "BTO_0004893"
    _253J_LAVAL_CELL = "BTO_0004893"

    # 253J-BV cell
    BTO_0004894 = "BTO_0004894"
    _253J_BV_CELL = "BTO_0004894"

    # NPC-TW01 cell
    BTO_0004895 = "BTO_0004895"
    NPC_TW01_CELL = "BTO_0004895"

    # IMEC cell
    BTO_0004896 = "BTO_0004896"
    IMEC_CELL = "BTO_0004896"

    # CHO-LY-B cell
    BTO_0004897 = "BTO_0004897"
    CHO_LY_B_CELL = "BTO_0004897"

    # HML-Gb3 cell
    BTO_0004898 = "BTO_0004898"
    HML_GB3_CELL = "BTO_0004898"

    # HK-1 cell
    BTO_0004899 = "BTO_0004899"
    HK_1_CELL = "BTO_0004899"

    # pulmonary venous myocardium
    BTO_0004900 = "BTO_0004900"
    PULMONARY_VENOUS_MYOCARDIUM = "BTO_0004900"

    # non-neuronal cell
    BTO_0004901 = "BTO_0004901"
    NON_NEURONAL_CELL = "BTO_0004901"

    # cholinergic neuron
    BTO_0004902 = "BTO_0004902"
    CHOLINERGIC_NEURON = "BTO_0004902"

    # plant crown
    BTO_0004903 = "BTO_0004903"
    PLANT_CROWN = "BTO_0004903"

    # hair follicle bulge
    BTO_0004904 = "BTO_0004904"
    HAIR_FOLLICLE_BULGE = "BTO_0004904"

    # hair follicle bulge stem cell
    BTO_0004905 = "BTO_0004905"
    HAIR_FOLLICLE_BULGE_STEM_CELL = "BTO_0004905"

    # molecular layer
    BTO_0004906 = "BTO_0004906"
    MOLECULAR_LAYER = "BTO_0004906"

    # Bergmanns glia
    BTO_0004907 = "BTO_0004907"
    BERGMANNS_GLIA = "BTO_0004907"

    # Bergmann fiber
    BTO_0004908 = "BTO_0004908"
    BERGMANN_FIBER = "BTO_0004908"

    # Purkinje layer
    BTO_0004909 = "BTO_0004909"
    PURKINJE_LAYER = "BTO_0004909"

    # retinal pigment epithelium cell
    BTO_0004910 = "BTO_0004910"
    RETINAL_PIGMENT_EPITHELIUM_CELL = "BTO_0004910"

    # erythroid progenitor cell
    BTO_0004911 = "BTO_0004911"
    ERYTHROID_PROGENITOR_CELL = "BTO_0004911"

    # culture condition:peptone-yeast extract-grown cell
    BTO_0004912 = "BTO_0004912"
    CULTURE_CONDITION_PEPTONE_YEAST_EXTRACT_GROWN_CELL = "BTO_0004912"

    # vastus medialis
    BTO_0004913 = "BTO_0004913"
    VASTUS_MEDIALIS = "BTO_0004913"

    # rheumatoid arthritis disease specific synovial fibroblast
    BTO_0004914 = "BTO_0004914"
    RHEUMATOID_ARTHRITIS_DISEASE_SPECIFIC_SYNOVIAL_FIBROBLAST = "BTO_0004914"

    # ZR-75-30 cell
    BTO_0004915 = "BTO_0004915"
    ZR_75_30_CELL = "BTO_0004915"

    # ZR-78 cell
    BTO_0004916 = "BTO_0004916"
    ZR_78_CELL = "BTO_0004916"

    # ZR-78.1 cell
    BTO_0004917 = "BTO_0004917"
    ZR_78_1_CELL = "BTO_0004917"

    # ZR-82 cell
    BTO_0004918 = "BTO_0004918"
    ZR_82_CELL = "BTO_0004918"

    # ZR-75 cell
    BTO_0004919 = "BTO_0004919"
    ZR_75_CELL = "BTO_0004919"

    # WSS-1 cell
    BTO_0004920 = "BTO_0004920"
    WSS_1_CELL = "BTO_0004920"

    # swine testicular cell line
    BTO_0004921 = "BTO_0004921"
    SWINE_TESTICULAR_CELL_LINE = "BTO_0004921"

    # TAOV cell
    BTO_0004922 = "BTO_0004922"
    TAOV_CELL = "BTO_0004922"

    # NOS-2 cell
    BTO_0004923 = "BTO_0004923"
    NOS_2_CELL = "BTO_0004923"

    # NOS-4 cell
    BTO_0004924 = "BTO_0004924"
    NOS_4_CELL = "BTO_0004924"

    # HRA cell
    BTO_0004925 = "BTO_0004925"
    HRA_CELL = "BTO_0004925"

    # THP-6 cell
    BTO_0004926 = "BTO_0004926"
    THP_6_CELL = "BTO_0004926"

    # THP-8 cell
    BTO_0004927 = "BTO_0004927"
    THP_8_CELL = "BTO_0004927"

    # SUM-159PT cell
    BTO_0004928 = "BTO_0004928"
    SUM_159PT_CELL = "BTO_0004928"

    # RMG-II cell
    BTO_0004929 = "BTO_0004929"
    RMG_II_CELL = "BTO_0004929"

    # RMG-I cell
    BTO_0004930 = "BTO_0004930"
    RMG_I_CELL = "BTO_0004930"

    # NPD-1 cell
    BTO_0004931 = "BTO_0004931"
    NPD_1_CELL = "BTO_0004931"

    # RCC-10 cell
    BTO_0004932 = "BTO_0004932"
    RCC_10_CELL = "BTO_0004932"

    # NALM-17 cell
    BTO_0004933 = "BTO_0004933"
    NALM_17_CELL = "BTO_0004933"

    # NALM-20 cell
    BTO_0004934 = "BTO_0004934"
    NALM_20_CELL = "BTO_0004934"

    # NALM-24 cell
    BTO_0004935 = "BTO_0004935"
    NALM_24_CELL = "BTO_0004935"

    # NALM-26 cell
    BTO_0004936 = "BTO_0004936"
    NALM_26_CELL = "BTO_0004936"

    # KOCL-33 cell
    BTO_0004937 = "BTO_0004937"
    KOCL_33_CELL = "BTO_0004937"

    # KOCL-44 cell
    BTO_0004938 = "BTO_0004938"
    KOCL_44_CELL = "BTO_0004938"

    # KOCL-45 cell
    BTO_0004939 = "BTO_0004939"
    KOCL_45_CELL = "BTO_0004939"

    # KOCL-58 cell
    BTO_0004940 = "BTO_0004940"
    KOCL_58_CELL = "BTO_0004940"

    # KOCL-69 cell
    BTO_0004941 = "BTO_0004941"
    KOCL_69_CELL = "BTO_0004941"

    # HAL-01 cell
    BTO_0004942 = "BTO_0004942"
    HAL_01_CELL = "BTO_0004942"

    # KOPN-41 cell
    BTO_0004943 = "BTO_0004943"
    KOPN_41_CELL = "BTO_0004943"

    # KOPN-1 cell
    BTO_0004944 = "BTO_0004944"
    KOPN_1_CELL = "BTO_0004944"

    # LC4-1 cell
    BTO_0004945 = "BTO_0004945"
    LC4_1_CELL = "BTO_0004945"

    # UTP-L5 cell
    BTO_0004946 = "BTO_0004946"
    UTP_L5_CELL = "BTO_0004946"

    # UTP-L10 cell
    BTO_0004947 = "BTO_0004947"
    UTP_L10_CELL = "BTO_0004947"

    # UTP-2 cell
    BTO_0004948 = "BTO_0004948"
    UTP_2_CELL = "BTO_0004948"

    # SCMC-L10 cell
    BTO_0004949 = "BTO_0004949"
    SCMC_L10_CELL = "BTO_0004949"

    # BV173 cell
    BTO_0004950 = "BTO_0004950"
    BV173_CELL = "BTO_0004950"

    # NALL-1 cell
    BTO_0004951 = "BTO_0004951"
    NALL_1_CELL = "BTO_0004951"

    # MV-522 cell
    BTO_0004952 = "BTO_0004952"
    MV_522_CELL = "BTO_0004952"

    # MGC-803 cell
    BTO_0004953 = "BTO_0004953"
    MGC_803_CELL = "BTO_0004953"

    # capillary endothelium
    BTO_0004954 = "BTO_0004954"
    CAPILLARY_ENDOTHELIUM = "BTO_0004954"

    # MDA-B02 cell
    BTO_0004955 = "BTO_0004955"
    MDA_B02_CELL = "BTO_0004955"

    # capillary endothelial cell
    BTO_0004956 = "BTO_0004956"
    CAPILLARY_ENDOTHELIAL_CELL = "BTO_0004956"

    # hydathode
    BTO_0004957 = "BTO_0004957"
    HYDATHODE = "BTO_0004957"

    # F9-12 cell
    BTO_0004958 = "BTO_0004958"
    F9_12_CELL = "BTO_0004958"

    # LNCAP-C4-2B cell
    BTO_0004959 = "BTO_0004959"
    LNCAP_C4_2B_CELL = "BTO_0004959"

    # CMK-86 cell
    BTO_0004960 = "BTO_0004960"
    CMK_86_CELL = "BTO_0004960"

    # acute megakaryoblastic leukemia cell line
    BTO_0004961 = "BTO_0004961"
    ACUTE_MEGAKARYOBLASTIC_LEUKEMIA_CELL_LINE = "BTO_0004961"

    # acute megakaryocytic leukemia cell
    BTO_0004962 = "BTO_0004962"
    ACUTE_MEGAKARYOCYTIC_LEUKEMIA_CELL = "BTO_0004962"

    # acute megakaryoblastic leukemia cell
    BTO_0004963 = "BTO_0004963"
    ACUTE_MEGAKARYOBLASTIC_LEUKEMIA_CELL = "BTO_0004963"

    # KOPT-K1 cell
    BTO_0004964 = "BTO_0004964"
    KOPT_K1_CELL = "BTO_0004964"

    # TTA-1 cell
    BTO_0004965 = "BTO_0004965"
    TTA_1_CELL = "BTO_0004965"

    # Rat-1/BB16 cell
    BTO_0004966 = "BTO_0004966"
    RAT_1_BB16_CELL = "BTO_0004966"

    # Rat-1/tsLA29 cell
    BTO_0004967 = "BTO_0004967"
    RAT_1_TSLA29_CELL = "BTO_0004967"

    # NS-0 cell
    BTO_0004968 = "BTO_0004968"
    NS_0_CELL = "BTO_0004968"

    # KOC-5C cell
    BTO_0004969 = "BTO_0004969"
    KOC_5C_CELL = "BTO_0004969"

    # KOC-7C cell
    BTO_0004970 = "BTO_0004970"
    KOC_7C_CELL = "BTO_0004970"

    # 1BR3.G cell
    BTO_0004971 = "BTO_0004971"
    _1BR3_G_CELL = "BTO_0004971"

    # KM-H2 cell
    BTO_0004972 = "BTO_0004972"
    KM_H2_CELL = "BTO_0004972"

    # Hodgkin lymphoma cell line
    BTO_0004973 = "BTO_0004973"
    HODGKIN_LYMPHOMA_CELL_LINE = "BTO_0004973"

    # Hodgkin lymphoma cell
    BTO_0004974 = "BTO_0004974"
    HODGKIN_LYMPHOMA_CELL = "BTO_0004974"

    # embryogenic cell line
    BTO_0004975 = "BTO_0004975"
    EMBRYOGENIC_CELL_LINE = "BTO_0004975"

    # tongue cancer cell
    BTO_0004976 = "BTO_0004976"
    TONGUE_CANCER_CELL = "BTO_0004976"

    # nasal lavage fluid
    BTO_0004977 = "BTO_0004977"
    NASAL_LAVAGE_FLUID = "BTO_0004977"

    # carotid sinus nerve
    BTO_0004978 = "BTO_0004978"
    CAROTID_SINUS_NERVE = "BTO_0004978"

    # glossopharyngeal nerve
    BTO_0004979 = "BTO_0004979"
    GLOSSOPHARYNGEAL_NERVE = "BTO_0004979"

    # uveal melanoma cell
    BTO_0004980 = "BTO_0004980"
    UVEAL_MELANOMA_CELL = "BTO_0004980"

    # KARPAS-422 cell
    BTO_0004981 = "BTO_0004981"
    KARPAS_422_CELL = "BTO_0004981"

    # gonocyte
    BTO_0004982 = "BTO_0004982"
    GONOCYTE = "BTO_0004982"

    # MA-104 cell
    BTO_0004983 = "BTO_0004983"
    MA_104_CELL = "BTO_0004983"

    # alate adult
    BTO_0004984 = "BTO_0004984"
    ALATE_ADULT = "BTO_0004984"

    # angioblast
    BTO_0004985 = "BTO_0004985"
    ANGIOBLAST = "BTO_0004985"

    # SNU-5 cell
    BTO_0004986 = "BTO_0004986"
    SNU_5_CELL = "BTO_0004986"

    # SNU-16 cell
    BTO_0004987 = "BTO_0004987"
    SNU_16_CELL = "BTO_0004987"

    # SNU-216 cell
    BTO_0004988 = "BTO_0004988"
    SNU_216_CELL = "BTO_0004988"

    # monospore
    BTO_0004989 = "BTO_0004989"
    MONOSPORE = "BTO_0004989"

    # UM-UC-9 cell
    BTO_0004990 = "BTO_0004990"
    UM_UC_9_CELL = "BTO_0004990"

    # UM-UC-14 cell
    BTO_0004991 = "BTO_0004991"
    UM_UC_14_CELL = "BTO_0004991"

    # UM-UC-10 cell
    BTO_0004992 = "BTO_0004992"
    UM_UC_10_CELL = "BTO_0004992"

    # UM-UC-5 cell
    BTO_0004993 = "BTO_0004993"
    UM_UC_5_CELL = "BTO_0004993"

    # SK-MEL-110 cell
    BTO_0004994 = "BTO_0004994"
    SK_MEL_110_CELL = "BTO_0004994"

    # osphradium
    BTO_0004995 = "BTO_0004995"
    OSPHRADIUM = "BTO_0004995"

    # myelinating Schwann cell
    BTO_0004996 = "BTO_0004996"
    MYELINATING_SCHWANN_CELL = "BTO_0004996"

    # non-myelinating Schwann cell
    BTO_0004997 = "BTO_0004997"
    NON_MYELINATING_SCHWANN_CELL = "BTO_0004997"

    # gingival epithelium
    BTO_0004998 = "BTO_0004998"
    GINGIVAL_EPITHELIUM = "BTO_0004998"

    # vaginal smooth muscle
    BTO_0004999 = "BTO_0004999"
    VAGINAL_SMOOTH_MUSCLE = "BTO_0004999"

    # clitoral smooth muscle
    BTO_0005000 = "BTO_0005000"
    CLITORAL_SMOOTH_MUSCLE = "BTO_0005000"

    # retinal microvascular endothelial cell
    BTO_0005001 = "BTO_0005001"
    RETINAL_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0005001"

    # pulmonary microvascular endothelial cell
    BTO_0005002 = "BTO_0005002"
    PULMONARY_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0005002"

    # villous trophoblast
    BTO_0005003 = "BTO_0005003"
    VILLOUS_TROPHOBLAST = "BTO_0005003"

    # UROtsa cell
    BTO_0005004 = "BTO_0005004"
    UROTSA_CELL = "BTO_0005004"

    # FEPD cell
    BTO_0005005 = "BTO_0005005"
    FEPD_CELL = "BTO_0005005"

    # 253J-P cell
    BTO_0005006 = "BTO_0005006"
    _253J_P_CELL = "BTO_0005006"

    # psammomatous meningioma cell
    BTO_0005007 = "BTO_0005007"
    PSAMMOMATOUS_MENINGIOMA_CELL = "BTO_0005007"

    # psammoma body
    BTO_0005008 = "BTO_0005008"
    PSAMMOMA_BODY = "BTO_0005008"

    # stratum intermedium
    BTO_0005009 = "BTO_0005009"
    STRATUM_INTERMEDIUM = "BTO_0005009"

    # meningothelial meningioma cell
    BTO_0005010 = "BTO_0005010"
    MENINGOTHELIAL_MENINGIOMA_CELL = "BTO_0005010"

    # 1205-Lu cell
    BTO_0005011 = "BTO_0005011"
    _1205_LU_CELL = "BTO_0005011"

    # 46BR.1G1 cell
    BTO_0005012 = "BTO_0005012"
    _46BR_1G1_CELL = "BTO_0005012"

    # 46BRLigI cell
    BTO_0005013 = "BTO_0005013"
    _46BRLIGI_CELL = "BTO_0005013"

    # B-cell leukemia cell
    BTO_0005014 = "BTO_0005014"
    B_CELL_LEUKEMIA_CELL = "BTO_0005014"

    # ASTC-a-1 cell
    BTO_0005015 = "BTO_0005015"
    ASTC_A_1_CELL = "BTO_0005015"

    # breast hyperplasia cell
    BTO_0005016 = "BTO_0005016"
    BREAST_HYPERPLASIA_CELL = "BTO_0005016"

    # usual ductal hyperplasia cell
    BTO_0005017 = "BTO_0005017"
    USUAL_DUCTAL_HYPERPLASIA_CELL = "BTO_0005017"

    # atypical ductal hyperplasia cell
    BTO_0005018 = "BTO_0005018"
    ATYPICAL_DUCTAL_HYPERPLASIA_CELL = "BTO_0005018"

    # AX-2 cell
    BTO_0005019 = "BTO_0005019"
    AX_2_CELL = "BTO_0005019"

    # cytotrophoblast cell line
    BTO_0005020 = "BTO_0005020"
    CYTOTROPHOBLAST_CELL_LINE = "BTO_0005020"

    # B6Tert-1 cell
    BTO_0005021 = "BTO_0005021"
    B6TERT_1_CELL = "BTO_0005021"

    # CAMA-1 cell
    BTO_0005022 = "BTO_0005022"
    CAMA_1_CELL = "BTO_0005022"

    # cEND cell
    BTO_0005023 = "BTO_0005023"
    CEND_CELL = "BTO_0005023"

    # gastrointestinal smooth muscle
    BTO_0005024 = "BTO_0005024"
    GASTROINTESTINAL_SMOOTH_MUSCLE = "BTO_0005024"

    # HEK-293-TrkB cell
    BTO_0005025 = "BTO_0005025"
    HEK_293_TRKB_CELL = "BTO_0005025"

    # HTOXAR-3 cell
    BTO_0005026 = "BTO_0005026"
    HTOXAR_3_CELL = "BTO_0005026"

    # GM-3299 cell
    BTO_0005027 = "BTO_0005027"
    GM_3299_CELL = "BTO_0005027"

    # GM-4408 cell
    BTO_0005028 = "BTO_0005028"
    GM_4408_CELL = "BTO_0005028"

    # HEK-293FT cell
    BTO_0005029 = "BTO_0005029"
    HEK_293FT_CELL = "BTO_0005029"

    # HeLa-229 cell
    BTO_0005030 = "BTO_0005030"
    HELA_229_CELL = "BTO_0005030"

    # KR-4 cell
    BTO_0005031 = "BTO_0005031"
    KR_4_CELL = "BTO_0005031"

    # CW-2 cell
    BTO_0005032 = "BTO_0005032"
    CW_2_CELL = "BTO_0005032"

    # MV3 cell
    BTO_0005033 = "BTO_0005033"
    MV3_CELL = "BTO_0005033"

    # DT-40 3KO cell
    BTO_0005034 = "BTO_0005034"
    DT_40_3KO_CELL = "BTO_0005034"

    # Fanconi anemia disease specific cell type
    BTO_0005035 = "BTO_0005035"
    FANCONI_ANEMIA_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005035"

    # Fanconi anemia lymphoid cell line
    BTO_0005036 = "BTO_0005036"
    FANCONI_ANEMIA_LYMPHOID_CELL_LINE = "BTO_0005036"

    # HEI-193 cell
    BTO_0005037 = "BTO_0005037"
    HEI_193_CELL = "BTO_0005037"

    # HeLa-LTRHIV-1-Luc cell
    BTO_0005038 = "BTO_0005038"
    HELA_LTRHIV_1_LUC_CELL = "BTO_0005038"

    # HN-30 cell
    BTO_0005039 = "BTO_0005039"
    HN_30_CELL = "BTO_0005039"

    # HN-12 cell
    BTO_0005040 = "BTO_0005040"
    HN_12_CELL = "BTO_0005040"

    # HT-168 cell
    BTO_0005041 = "BTO_0005041"
    HT_168_CELL = "BTO_0005041"

    # WM-983/B cell
    BTO_0005042 = "BTO_0005042"
    WM_983_B_CELL = "BTO_0005042"

    # M1 melanoma cell
    BTO_0005043 = "BTO_0005043"
    M1_MELANOMA_CELL = "BTO_0005043"

    # LNCaP-17 cell
    BTO_0005044 = "BTO_0005044"
    LNCAP_17_CELL = "BTO_0005044"

    # LNCaP-34 cell
    BTO_0005045 = "BTO_0005045"
    LNCAP_34_CELL = "BTO_0005045"

    # LHCN-M2 cell
    BTO_0005046 = "BTO_0005046"
    LHCN_M2_CELL = "BTO_0005046"

    # MGSO-3 cell
    BTO_0005047 = "BTO_0005047"
    MGSO_3_CELL = "BTO_0005047"

    # MACL-1 cell
    BTO_0005048 = "BTO_0005048"
    MACL_1_CELL = "BTO_0005048"

    # prostate adenocarcinoma cell line
    BTO_0005049 = "BTO_0005049"
    PROSTATE_ADENOCARCINOMA_CELL_LINE = "BTO_0005049"

    # MDA-PCa-2b cell
    BTO_0005050 = "BTO_0005050"
    MDA_PCA_2B_CELL = "BTO_0005050"

    # L87/4 cell
    BTO_0005051 = "BTO_0005051"
    L87_4_CELL = "BTO_0005051"

    # L88/5 cell
    BTO_0005052 = "BTO_0005052"
    L88_5_CELL = "BTO_0005052"

    # midgut epithelium
    BTO_0005053 = "BTO_0005053"
    MIDGUT_EPITHELIUM = "BTO_0005053"

    # macrophage foam cell
    BTO_0005054 = "BTO_0005054"
    MACROPHAGE_FOAM_CELL = "BTO_0005054"

    # scale
    BTO_0005055 = "BTO_0005055"
    SCALE = "BTO_0005055"

    # J7 hepatoma cell
    BTO_0005056 = "BTO_0005056"
    J7_HEPATOMA_CELL = "BTO_0005056"

    # J5 hepatoma cell
    BTO_0005057 = "BTO_0005057"
    J5_HEPATOMA_CELL = "BTO_0005057"

    # SU-DHL-1 cell
    BTO_0005058 = "BTO_0005058"
    SU_DHL_1_CELL = "BTO_0005058"

    # TZM-bl cell
    BTO_0005059 = "BTO_0005059"
    TZM_BL_CELL = "BTO_0005059"

    # UACC-903 cell
    BTO_0005060 = "BTO_0005060"
    UACC_903_CELL = "BTO_0005060"

    # PC-12K cell
    BTO_0005061 = "BTO_0005061"
    PC_12K_CELL = "BTO_0005061"

    # M93-047 cell
    BTO_0005062 = "BTO_0005062"
    M93_047_CELL = "BTO_0005062"

    # UACC-647 cell
    BTO_0005063 = "BTO_0005063"
    UACC_647_CELL = "BTO_0005063"

    # UACC-1273EV cell
    BTO_0005064 = "BTO_0005064"
    UACC_1273EV_CELL = "BTO_0005064"

    # 3T3-Swiss albino cell
    BTO_0005065 = "BTO_0005065"
    _3T3_SWISS_ALBINO_CELL = "BTO_0005065"

    # MRC-5V1 cell
    BTO_0005066 = "BTO_0005066"
    MRC_5V1_CELL = "BTO_0005066"

    # PAM212 cell
    BTO_0005067 = "BTO_0005067"
    PAM212_CELL = "BTO_0005067"

    # SK-CO15 cell
    BTO_0005068 = "BTO_0005068"
    SK_CO15_CELL = "BTO_0005068"

    # Me665/2/21 cell
    BTO_0005069 = "BTO_0005069"
    ME665_2_21_CELL = "BTO_0005069"

    # Me665/2/60 cell
    BTO_0005070 = "BTO_0005070"
    ME665_2_60_CELL = "BTO_0005070"

    # PC3-MM2 cell
    BTO_0005071 = "BTO_0005071"
    PC3_MM2_CELL = "BTO_0005071"

    # NB5 cell
    BTO_0005072 = "BTO_0005072"
    NB5_CELL = "BTO_0005072"

    # NB14 cell
    BTO_0005073 = "BTO_0005073"
    NB14_CELL = "BTO_0005073"

    # M9A cell
    BTO_0005074 = "BTO_0005074"
    M9A_CELL = "BTO_0005074"

    # NT2-Rho0 cell
    BTO_0005075 = "BTO_0005075"
    NT2_RHO0_CELL = "BTO_0005075"

    # KG-1A cell
    BTO_0005076 = "BTO_0005076"
    KG_1A_CELL = "BTO_0005076"

    # LL24 cell
    BTO_0005077 = "BTO_0005077"
    LL24_CELL = "BTO_0005077"

    # foot sole
    BTO_0005078 = "BTO_0005078"
    FOOT_SOLE = "BTO_0005078"

    # KLE cell
    BTO_0005079 = "BTO_0005079"
    KLE_CELL = "BTO_0005079"

    # LLC-WRC 256 cell
    BTO_0005080 = "BTO_0005080"
    LLC_WRC_256_CELL = "BTO_0005080"

    # periurethral tissue
    BTO_0005081 = "BTO_0005081"
    PERIURETHRAL_TISSUE = "BTO_0005081"

    # skin mucus
    BTO_0005082 = "BTO_0005082"
    SKIN_MUCUS = "BTO_0005082"

    # plant mucous cell
    BTO_0005083 = "BTO_0005083"
    PLANT_MUCOUS_CELL = "BTO_0005083"

    # vocal fold
    BTO_0005084 = "BTO_0005084"
    VOCAL_FOLD = "BTO_0005084"

    # common penile artery
    BTO_0005085 = "BTO_0005085"
    COMMON_PENILE_ARTERY = "BTO_0005085"

    # arteria profunda penis
    BTO_0005086 = "BTO_0005086"
    ARTERIA_PROFUNDA_PENIS = "BTO_0005086"

    # arteria bulbi penis
    BTO_0005087 = "BTO_0005087"
    ARTERIA_BULBI_PENIS = "BTO_0005087"

    # arteria dorsalis penis
    BTO_0005088 = "BTO_0005088"
    ARTERIA_DORSALIS_PENIS = "BTO_0005088"

    # perichondrium
    BTO_0005089 = "BTO_0005089"
    PERICHONDRIUM = "BTO_0005089"

    # inner chondrogenic layer of perichondrium
    BTO_0005090 = "BTO_0005090"
    INNER_CHONDROGENIC_LAYER_OF_PERICHONDRIUM = "BTO_0005090"

    # outer fibrous layer of perichondrium
    BTO_0005091 = "BTO_0005091"
    OUTER_FIBROUS_LAYER_OF_PERICHONDRIUM = "BTO_0005091"

    # chondrogenic cell
    BTO_0005092 = "BTO_0005092"
    CHONDROGENIC_CELL = "BTO_0005092"

    # intercalated cell
    BTO_0005093 = "BTO_0005093"
    INTERCALATED_CELL = "BTO_0005093"

    # leaf sheath
    BTO_0005094 = "BTO_0005094"
    LEAF_SHEATH = "BTO_0005094"

    # H4-C99 cell
    BTO_0005095 = "BTO_0005095"
    H4_C99_CELL = "BTO_0005095"

    # epithelial stem cell
    BTO_0005096 = "BTO_0005096"
    EPITHELIAL_STEM_CELL = "BTO_0005096"

    # skin stem cell
    BTO_0005097 = "BTO_0005097"
    SKIN_STEM_CELL = "BTO_0005097"

    # epidermal stem cell
    BTO_0005098 = "BTO_0005098"
    EPIDERMAL_STEM_CELL = "BTO_0005098"

    # follicular stem cell
    BTO_0005099 = "BTO_0005099"
    FOLLICULAR_STEM_CELL = "BTO_0005099"

    # implantation fossa
    BTO_0005100 = "BTO_0005100"
    IMPLANTATION_FOSSA = "BTO_0005100"

    # coronary artery smooth muscle cell
    BTO_0005101 = "BTO_0005101"
    CORONARY_ARTERY_SMOOTH_MUSCLE_CELL = "BTO_0005101"

    # SCC-15 cell
    BTO_0005102 = "BTO_0005102"
    SCC_15_CELL = "BTO_0005102"

    # NB-1 cell
    BTO_0005103 = "BTO_0005103"
    NB_1_CELL = "BTO_0005103"

    # culture condition:2-sulfoacetate-grown cell
    BTO_0005104 = "BTO_0005104"
    CULTURE_CONDITION_2_SULFOACETATE_GROWN_CELL = "BTO_0005104"

    # culture condition:ammonium-grown cell
    BTO_0005105 = "BTO_0005105"
    CULTURE_CONDITION_AMMONIUM_GROWN_CELL = "BTO_0005105"

    # culture condition:ethylbenzene-grown cell
    BTO_0005106 = "BTO_0005106"
    CULTURE_CONDITION_ETHYLBENZENE_GROWN_CELL = "BTO_0005106"

    # culture condition:gellan-grown cell
    BTO_0005107 = "BTO_0005107"
    CULTURE_CONDITION_GELLAN_GROWN_CELL = "BTO_0005107"

    # culture condition:pyrrole-2-carboxylate-grown cell
    BTO_0005108 = "BTO_0005108"
    CULTURE_CONDITION_PYRROLE_2_CARBOXYLATE_GROWN_CELL = "BTO_0005108"

    # saphenous vein endothelial cell
    BTO_0005109 = "BTO_0005109"
    SAPHENOUS_VEIN_ENDOTHELIAL_CELL = "BTO_0005109"

    # ameloblastoma cell
    BTO_0005110 = "BTO_0005110"
    AMELOBLASTOMA_CELL = "BTO_0005110"

    # HaCaT II-4 cell
    BTO_0005111 = "BTO_0005111"
    HACAT_II_4_CELL = "BTO_0005111"

    # TRAMP-C1 cell
    BTO_0005112 = "BTO_0005112"
    TRAMP_C1_CELL = "BTO_0005112"

    # TRAMP-C3 cell
    BTO_0005113 = "BTO_0005113"
    TRAMP_C3_CELL = "BTO_0005113"

    # TRAMP-C2 cell
    BTO_0005114 = "BTO_0005114"
    TRAMP_C2_CELL = "BTO_0005114"

    # salivary duct
    BTO_0005115 = "BTO_0005115"
    SALIVARY_DUCT = "BTO_0005115"

    # salivary duct cancer cell
    BTO_0005116 = "BTO_0005116"
    SALIVARY_DUCT_CANCER_CELL = "BTO_0005116"

    # retinal ganglion cell line
    BTO_0005117 = "BTO_0005117"
    RETINAL_GANGLION_CELL_LINE = "BTO_0005117"

    # RGC-5 cell
    BTO_0005118 = "BTO_0005118"
    RGC_5_CELL = "BTO_0005118"

    # pleural mesothelioma cell
    BTO_0005119 = "BTO_0005119"
    PLEURAL_MESOTHELIOMA_CELL = "BTO_0005119"

    # neuroectodermal tumor cell
    BTO_0005120 = "BTO_0005120"
    NEUROECTODERMAL_TUMOR_CELL = "BTO_0005120"

    # PC3-B1 cell
    BTO_0005121 = "BTO_0005121"
    PC3_B1_CELL = "BTO_0005121"

    # ovarian cyst
    BTO_0005122 = "BTO_0005122"
    OVARIAN_CYST = "BTO_0005122"

    # ovarian cyst fluid
    BTO_0005123 = "BTO_0005123"
    OVARIAN_CYST_FLUID = "BTO_0005123"

    # platysma muscle
    BTO_0005124 = "BTO_0005124"
    PLATYSMA_MUSCLE = "BTO_0005124"

    # sternocleidomastoid muscle
    BTO_0005125 = "BTO_0005125"
    STERNOCLEIDOMASTOID_MUSCLE = "BTO_0005125"

    # Myc-CaP cell
    BTO_0005126 = "BTO_0005126"
    MYC_CAP_CELL = "BTO_0005126"

    # MCF-10A neoT cell
    BTO_0005127 = "BTO_0005127"
    MCF_10A_NEOT_CELL = "BTO_0005127"

    # M12 prostate cancer cell
    BTO_0005128 = "BTO_0005128"
    M12_PROSTATE_CANCER_CELL = "BTO_0005128"

    # A2780/S cell
    BTO_0005129 = "BTO_0005129"
    A2780_S_CELL = "BTO_0005129"

    # A2780/R cell
    BTO_0005130 = "BTO_0005130"
    A2780_R_CELL = "BTO_0005130"

    # conjunctival epithelium
    BTO_0005131 = "BTO_0005131"
    CONJUNCTIVAL_EPITHELIUM = "BTO_0005131"

    # arrector pili muscle
    BTO_0005132 = "BTO_0005132"
    ARRECTOR_PILI_MUSCLE = "BTO_0005132"

    # CCD-986Sk cell
    BTO_0005133 = "BTO_0005133"
    CCD_986SK_CELL = "BTO_0005133"

    # adenomatoid odontogenic tumor cell
    BTO_0005134 = "BTO_0005134"
    ADENOMATOID_ODONTOGENIC_TUMOR_CELL = "BTO_0005134"

    # D-283MED cell
    BTO_0005135 = "BTO_0005135"
    D_283MED_CELL = "BTO_0005135"

    # ES-E14 cell
    BTO_0005136 = "BTO_0005136"
    ES_E14_CELL = "BTO_0005136"

    # RST-307 cell
    BTO_0005137 = "BTO_0005137"
    RST_307_CELL = "BTO_0005137"

    # MTC-1 cell
    BTO_0005138 = "BTO_0005138"
    MTC_1_CELL = "BTO_0005138"

    # HEp-3 cell
    BTO_0005139 = "BTO_0005139"
    HEP_3_CELL = "BTO_0005139"

    # H273 cell
    BTO_0005140 = "BTO_0005140"
    H273_CELL = "BTO_0005140"

    # rheumatoid arthritis disease specific giant cell
    BTO_0005141 = "BTO_0005141"
    RHEUMATOID_ARTHRITIS_DISEASE_SPECIFIC_GIANT_CELL = "BTO_0005141"

    # ameloblastic layer
    BTO_0005142 = "BTO_0005142"
    AMELOBLASTIC_LAYER = "BTO_0005142"

    # OCUT-2 cell
    BTO_0005143 = "BTO_0005143"
    OCUT_2_CELL = "BTO_0005143"

    # KTC-1 cell
    BTO_0005144 = "BTO_0005144"
    KTC_1_CELL = "BTO_0005144"

    # chorionic epithelium
    BTO_0005145 = "BTO_0005145"
    CHORIONIC_EPITHELIUM = "BTO_0005145"

    # HTh-7 cell
    BTO_0005146 = "BTO_0005146"
    HTH_7_CELL = "BTO_0005146"

    # HTh-74 cell
    BTO_0005147 = "BTO_0005147"
    HTH_74_CELL = "BTO_0005147"

    # HTh-83 cell
    BTO_0005148 = "BTO_0005148"
    HTH_83_CELL = "BTO_0005148"

    # C-643 cell
    BTO_0005149 = "BTO_0005149"
    C_643_CELL = "BTO_0005149"

    # anococcygeus muscle
    BTO_0005150 = "BTO_0005150"
    ANOCOCCYGEUS_MUSCLE = "BTO_0005150"

    # anterior horn
    BTO_0005151 = "BTO_0005151"
    ANTERIOR_HORN = "BTO_0005151"

    # A2780/CDDP cell
    BTO_0005152 = "BTO_0005152"
    A2780_CDDP_CELL = "BTO_0005152"

    # CEM-VBL10 cell
    BTO_0005153 = "BTO_0005153"
    CEM_VBL10_CELL = "BTO_0005153"

    # CEM-VBL16 cell
    BTO_0005154 = "BTO_0005154"
    CEM_VBL16_CELL = "BTO_0005154"

    # CEM-VBL100 cell
    BTO_0005155 = "BTO_0005155"
    CEM_VBL100_CELL = "BTO_0005155"

    # Caco-2/BBe cell
    BTO_0005156 = "BTO_0005156"
    CACO_2_BBE_CELL = "BTO_0005156"

    # juxtaglomerular apparatus
    BTO_0005157 = "BTO_0005157"
    JUXTAGLOMERULAR_APPARATUS = "BTO_0005157"

    # juxtaglomerular cell
    BTO_0005158 = "BTO_0005158"
    JUXTAGLOMERULAR_CELL = "BTO_0005158"

    # extraglomerular mesangial cell
    BTO_0005159 = "BTO_0005159"
    EXTRAGLOMERULAR_MESANGIAL_CELL = "BTO_0005159"

    # oil gland
    BTO_0005160 = "BTO_0005160"
    OIL_GLAND = "BTO_0005160"

    # KAT-18 cell
    BTO_0005161 = "BTO_0005161"
    KAT_18_CELL = "BTO_0005161"

    # FB-1 cell
    BTO_0005162 = "BTO_0005162"
    FB_1_CELL = "BTO_0005162"

    # COLO-16 cell
    BTO_0005163 = "BTO_0005163"
    COLO_16_CELL = "BTO_0005163"

    # HKESC-1 cell
    BTO_0005164 = "BTO_0005164"
    HKESC_1_CELL = "BTO_0005164"

    # HKESC-2 cell
    BTO_0005165 = "BTO_0005165"
    HKESC_2_CELL = "BTO_0005165"

    # HKESC-3 cell
    BTO_0005166 = "BTO_0005166"
    HKESC_3_CELL = "BTO_0005166"

    # HSC-1 cell
    BTO_0005167 = "BTO_0005167"
    HSC_1_CELL = "BTO_0005167"

    # JJ012 cell
    BTO_0005168 = "BTO_0005168"
    JJ012_CELL = "BTO_0005168"

    # HCMEC cell
    BTO_0005169 = "BTO_0005169"
    HCMEC_CELL = "BTO_0005169"

    # keratocyte
    BTO_0005170 = "BTO_0005170"
    KERATOCYTE = "BTO_0005170"

    # SNU-620 cell
    BTO_0005171 = "BTO_0005171"
    SNU_620_CELL = "BTO_0005171"

    # MDA-MB-231-Luc2 cell
    BTO_0005172 = "BTO_0005172"
    MDA_MB_231_LUC2_CELL = "BTO_0005172"

    # UMR-106-01 cell
    BTO_0005173 = "BTO_0005173"
    UMR_106_01_CELL = "BTO_0005173"

    # Mel120 cell
    BTO_0005174 = "BTO_0005174"
    MEL120_CELL = "BTO_0005174"

    # Panc-02 cell
    BTO_0005175 = "BTO_0005175"
    PANC_02_CELL = "BTO_0005175"

    # L-540 cell
    BTO_0005176 = "BTO_0005176"
    L_540_CELL = "BTO_0005176"

    # BCWM.1 cell
    BTO_0005177 = "BTO_0005177"
    BCWM_1_CELL = "BTO_0005177"

    # PWR-1E cell
    BTO_0005178 = "BTO_0005178"
    PWR_1E_CELL = "BTO_0005178"

    # PSN-1 cell
    BTO_0005179 = "BTO_0005179"
    PSN_1_CELL = "BTO_0005179"

    # pterygium
    BTO_0005180 = "BTO_0005180"
    PTERYGIUM = "BTO_0005180"

    # RzM6-LC cell
    BTO_0005181 = "BTO_0005181"
    RZM6_LC_CELL = "BTO_0005181"

    # TOV-112D cell
    BTO_0005182 = "BTO_0005182"
    TOV_112D_CELL = "BTO_0005182"

    # TOV-21G cell
    BTO_0005183 = "BTO_0005183"
    TOV_21G_CELL = "BTO_0005183"

    # SVGp12 cell
    BTO_0005184 = "BTO_0005184"
    SVGP12_CELL = "BTO_0005184"

    # chondroma cell
    BTO_0005185 = "BTO_0005185"
    CHONDROMA_CELL = "BTO_0005185"

    # H4-APP751 cell
    BTO_0005186 = "BTO_0005186"
    H4_APP751_CELL = "BTO_0005186"

    # TTE-1 cell
    BTO_0005187 = "BTO_0005187"
    TTE_1_CELL = "BTO_0005187"

    # trunk kidney
    BTO_0005188 = "BTO_0005188"
    TRUNK_KIDNEY = "BTO_0005188"

    # head kidney
    BTO_0005189 = "BTO_0005189"
    HEAD_KIDNEY = "BTO_0005189"

    # sarcomatoid carcinoma cell
    BTO_0005190 = "BTO_0005190"
    SARCOMATOID_CARCINOMA_CELL = "BTO_0005190"

    # Patu-8988 cell
    BTO_0005191 = "BTO_0005191"
    PATU_8988_CELL = "BTO_0005191"

    # MCF-7/adr cell
    BTO_0005192 = "BTO_0005192"
    MCF_7_ADR_CELL = "BTO_0005192"

    # H4TG cell
    BTO_0005193 = "BTO_0005193"
    H4TG_CELL = "BTO_0005193"

    # fine root
    BTO_0005194 = "BTO_0005194"
    FINE_ROOT = "BTO_0005194"

    # K-562/R7 cell
    BTO_0005195 = "BTO_0005195"
    K_562_R7_CELL = "BTO_0005195"

    # KBv200 cell
    BTO_0005196 = "BTO_0005196"
    KBV200_CELL = "BTO_0005196"

    # peltate gland
    BTO_0005197 = "BTO_0005197"
    PELTATE_GLAND = "BTO_0005197"

    # adipose-derived stem cell
    BTO_0005198 = "BTO_0005198"
    ADIPOSE_DERIVED_STEM_CELL = "BTO_0005198"

    # CEM-ADR5000 cell
    BTO_0005199 = "BTO_0005199"
    CEM_ADR5000_CELL = "BTO_0005199"

    # brain microvessel endothelial cell
    BTO_0005200 = "BTO_0005200"
    BRAIN_MICROVESSEL_ENDOTHELIAL_CELL = "BTO_0005200"

    # brain endothelial cell
    BTO_0005201 = "BTO_0005201"
    BRAIN_ENDOTHELIAL_CELL = "BTO_0005201"

    # bulbil
    BTO_0005202 = "BTO_0005202"
    BULBIL = "BTO_0005202"

    # gingival cancer cell line
    BTO_0005203 = "BTO_0005203"
    GINGIVAL_CANCER_CELL_LINE = "BTO_0005203"

    # Ca9-22 cell
    BTO_0005204 = "BTO_0005204"
    CA9_22_CELL = "BTO_0005204"

    # cerebral artery
    BTO_0005205 = "BTO_0005205"
    CEREBRAL_ARTERY = "BTO_0005205"

    # middle cerebral artery
    BTO_0005206 = "BTO_0005206"
    MIDDLE_CEREBRAL_ARTERY = "BTO_0005206"

    # left middle cerebral artery
    BTO_0005207 = "BTO_0005207"
    LEFT_MIDDLE_CEREBRAL_ARTERY = "BTO_0005207"

    # right middle cerebral artery
    BTO_0005208 = "BTO_0005208"
    RIGHT_MIDDLE_CEREBRAL_ARTERY = "BTO_0005208"

    # culture condition:isophthalate-grown cell
    BTO_0005209 = "BTO_0005209"
    CULTURE_CONDITION_ISOPHTHALATE_GROWN_CELL = "BTO_0005209"

    # syntrophic cell culture
    BTO_0005210 = "BTO_0005210"
    SYNTROPHIC_CELL_CULTURE = "BTO_0005210"

    # choriodecidua
    BTO_0005211 = "BTO_0005211"
    CHORIODECIDUA = "BTO_0005211"

    # cervical intraepithelial neoplasia cell
    BTO_0005212 = "BTO_0005212"
    CERVICAL_INTRAEPITHELIAL_NEOPLASIA_CELL = "BTO_0005212"

    # circular smooth muscle
    BTO_0005213 = "BTO_0005213"
    CIRCULAR_SMOOTH_MUSCLE = "BTO_0005213"

    # longitudinal smooth muscle
    BTO_0005214 = "BTO_0005214"
    LONGITUDINAL_SMOOTH_MUSCLE = "BTO_0005214"

    # KB-C2 cell
    BTO_0005215 = "BTO_0005215"
    KB_C2_CELL = "BTO_0005215"

    # keratocyst
    BTO_0005216 = "BTO_0005216"
    KERATOCYST = "BTO_0005216"

    # LNGK-9 PCa cell
    BTO_0005217 = "BTO_0005217"
    LNGK_9_PCA_CELL = "BTO_0005217"

    # MC57 cell
    BTO_0005218 = "BTO_0005218"
    MC57_CELL = "BTO_0005218"

    # osteophyte
    BTO_0005219 = "BTO_0005219"
    OSTEOPHYTE = "BTO_0005219"

    # PC-3M cell
    BTO_0005220 = "BTO_0005220"
    PC_3M_CELL = "BTO_0005220"

    # PC-3M-LN4 cell
    BTO_0005221 = "BTO_0005221"
    PC_3M_LN4_CELL = "BTO_0005221"

    # PC-3M-Pro4 cell
    BTO_0005222 = "BTO_0005222"
    PC_3M_PRO4_CELL = "BTO_0005222"

    # Drosophila D17 cell
    BTO_0005223 = "BTO_0005223"
    DROSOPHILA_D17_CELL = "BTO_0005223"

    # hFOB 1.19 cell
    BTO_0005224 = "BTO_0005224"
    HFOB_1_19_CELL = "BTO_0005224"

    # CHO-CUR3 cell
    BTO_0005225 = "BTO_0005225"
    CHO_CUR3_CELL = "BTO_0005225"

    # medial pterygoid muscle
    BTO_0005226 = "BTO_0005226"
    MEDIAL_PTERYGOID_MUSCLE = "BTO_0005226"

    # XC cell
    BTO_0005227 = "BTO_0005227"
    XC_CELL = "BTO_0005227"

    # YT cell
    BTO_0005228 = "BTO_0005228"
    YT_CELL = "BTO_0005228"

    # XC-v cell
    BTO_0005229 = "BTO_0005229"
    XC_V_CELL = "BTO_0005229"

    # stem juice
    BTO_0005230 = "BTO_0005230"
    STEM_JUICE = "BTO_0005230"

    # culture condition:D-glucose-grown cell
    BTO_0005231 = "BTO_0005231"
    CULTURE_CONDITION_D_GLUCOSE_GROWN_CELL = "BTO_0005231"

    # culture condition:n-decane-grown cell
    BTO_0005232 = "BTO_0005232"
    CULTURE_CONDITION_N_DECANE_GROWN_CELL = "BTO_0005232"

    # culture condition:dextrose-grown cell
    BTO_0005233 = "BTO_0005233"
    CULTURE_CONDITION_DEXTROSE_GROWN_CELL = "BTO_0005233"

    # culture condition:D-glucose-L-asparagine-grown cell
    BTO_0005234 = "BTO_0005234"
    CULTURE_CONDITION_D_GLUCOSE_L_ASPARAGINE_GROWN_CELL = "BTO_0005234"

    # culture condition:L-asparagine-grown cell
    BTO_0005235 = "BTO_0005235"
    CULTURE_CONDITION_L_ASPARAGINE_GROWN_CELL = "BTO_0005235"

    # culture condition:salicylate-grown cell
    BTO_0005236 = "BTO_0005236"
    CULTURE_CONDITION_SALICYLATE_GROWN_CELL = "BTO_0005236"

    # culture condition:sulfolactate-grown cell
    BTO_0005237 = "BTO_0005237"
    CULTURE_CONDITION_SULFOLACTATE_GROWN_CELL = "BTO_0005237"

    # T-REx 293 cell
    BTO_0005238 = "BTO_0005238"
    T_REX_293_CELL = "BTO_0005238"

    # renal tubule epithelium
    BTO_0005239 = "BTO_0005239"
    RENAL_TUBULE_EPITHELIUM = "BTO_0005239"

    # pharyngeal epithelium
    BTO_0005240 = "BTO_0005240"
    PHARYNGEAL_EPITHELIUM = "BTO_0005240"

    # MSK-Leuk1 cell
    BTO_0005241 = "BTO_0005241"
    MSK_LEUK1_CELL = "BTO_0005241"

    # MLE-15 cell
    BTO_0005242 = "BTO_0005242"
    MLE_15_CELL = "BTO_0005242"

    # NCI-H1650 cell
    BTO_0005243 = "BTO_0005243"
    NCI_H1650_CELL = "BTO_0005243"

    # culture condition:CD19+ cell
    BTO_0005244 = "BTO_0005244"
    CULTURE_CONDITION_CD19__CELL = "BTO_0005244"

    # culture condition:CD31+ cell
    BTO_0005245 = "BTO_0005245"
    CULTURE_CONDITION_CD31__CELL = "BTO_0005245"

    # culture condition:CD103+ cell
    BTO_0005247 = "BTO_0005247"
    CULTURE_CONDITION_CD103__CELL = "BTO_0005247"

    # M-07E cell
    BTO_0005248 = "BTO_0005248"
    M_07E_CELL = "BTO_0005248"

    # M-07 cell
    BTO_0005249 = "BTO_0005249"
    M_07_CELL = "BTO_0005249"

    # CNE-2 cell
    BTO_0005250 = "BTO_0005250"
    CNE_2_CELL = "BTO_0005250"

    # ink sac
    BTO_0005251 = "BTO_0005251"
    INK_SAC = "BTO_0005251"

    # 36B-10 cell
    BTO_0005252 = "BTO_0005252"
    _36B_10_CELL = "BTO_0005252"

    # CHP-100 cell
    BTO_0005253 = "BTO_0005253"
    CHP_100_CELL = "BTO_0005253"

    # CHP-126 cell
    BTO_0005254 = "BTO_0005254"
    CHP_126_CELL = "BTO_0005254"

    # RPMI-1788 cell
    BTO_0005255 = "BTO_0005255"
    RPMI_1788_CELL = "BTO_0005255"

    # W001C cell
    BTO_0005256 = "BTO_0005256"
    W001C_CELL = "BTO_0005256"

    # oropharynx
    BTO_0005257 = "BTO_0005257"
    OROPHARYNX = "BTO_0005257"

    # oropharyngeal cancer cell
    BTO_0005258 = "BTO_0005258"
    OROPHARYNGEAL_CANCER_CELL = "BTO_0005258"

    # oropharyngeal carcinoma cell line
    BTO_0005259 = "BTO_0005259"
    OROPHARYNGEAL_CARCINOMA_CELL_LINE = "BTO_0005259"

    # MGL-8 cell
    BTO_0005260 = "BTO_0005260"
    MGL_8_CELL = "BTO_0005260"

    # B-lymphoblast cell line
    BTO_0005261 = "BTO_0005261"
    B_LYMPHOBLAST_CELL_LINE = "BTO_0005261"

    # NEF cell
    BTO_0005262 = "BTO_0005262"
    NEF_CELL = "BTO_0005262"

    # HER 14 cell
    BTO_0005263 = "BTO_0005263"
    HER_14_CELL = "BTO_0005263"

    # mucoepidermoid carcinoma cell
    BTO_0005264 = "BTO_0005264"
    MUCOEPIDERMOID_CARCINOMA_CELL = "BTO_0005264"

    # nonparenchymal liver cell
    BTO_0005265 = "BTO_0005265"
    NONPARENCHYMAL_LIVER_CELL = "BTO_0005265"

    # cirrhosis disease specific cell type
    BTO_0005266 = "BTO_0005266"
    CIRRHOSIS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005266"

    # 293-F FreeStyle cell
    BTO_0005267 = "BTO_0005267"
    _293_F_FREESTYLE_CELL = "BTO_0005267"

    # neuropil
    BTO_0005268 = "BTO_0005268"
    NEUROPIL = "BTO_0005268"

    # antennal lobe
    BTO_0005269 = "BTO_0005269"
    ANTENNAL_LOBE = "BTO_0005269"

    # HAoAF cell
    BTO_0005270 = "BTO_0005270"
    HAOAF_CELL = "BTO_0005270"

    # anterior hypodermis
    BTO_0005271 = "BTO_0005271"
    ANTERIOR_HYPODERMIS = "BTO_0005271"

    # radical leaf
    BTO_0005272 = "BTO_0005272"
    RADICAL_LEAF = "BTO_0005272"

    # adventitious root
    BTO_0005273 = "BTO_0005273"
    ADVENTITIOUS_ROOT = "BTO_0005273"

    # adventitious root culture
    BTO_0005274 = "BTO_0005274"
    ADVENTITIOUS_ROOT_CULTURE = "BTO_0005274"

    # HPK1A-ras cell
    BTO_0005275 = "BTO_0005275"
    HPK1A_RAS_CELL = "BTO_0005275"

    # HPK1A cell
    BTO_0005276 = "BTO_0005276"
    HPK1A_CELL = "BTO_0005276"

    # CAG cell
    BTO_0005277 = "BTO_0005277"
    CAG_CELL = "BTO_0005277"

    # cestode
    BTO_0005278 = "BTO_0005278"
    CESTODE = "BTO_0005278"

    # Caco-2/15 cell
    BTO_0005279 = "BTO_0005279"
    CACO_2_15_CELL = "BTO_0005279"

    # culture condition:oxalate-grown cell
    BTO_0005280 = "BTO_0005280"
    CULTURE_CONDITION_OXALATE_GROWN_CELL = "BTO_0005280"

    # intercostal muscle
    BTO_0005281 = "BTO_0005281"
    INTERCOSTAL_MUSCLE = "BTO_0005281"

    # WEHI-3B cell
    BTO_0005282 = "BTO_0005282"
    WEHI_3B_CELL = "BTO_0005282"

    # TS-20 cell
    BTO_0005283 = "BTO_0005283"
    TS_20_CELL = "BTO_0005283"

    # UML-49 cell
    BTO_0005284 = "BTO_0005284"
    UML_49_CELL = "BTO_0005284"

    # NPD-2 cell
    BTO_0005285 = "BTO_0005285"
    NPD_2_CELL = "BTO_0005285"

    # 13-90 cell
    BTO_0005286 = "BTO_0005286"
    _13_90_CELL = "BTO_0005286"

    # 2102Ep cell
    BTO_0005287 = "BTO_0005287"
    _2102EP_CELL = "BTO_0005287"

    # CL-48 cell
    BTO_0005288 = "BTO_0005288"
    CL_48_CELL = "BTO_0005288"

    # Col-2 cell
    BTO_0005289 = "BTO_0005289"
    COL_2_CELL = "BTO_0005289"

    # TE 353.Sk cell
    BTO_0005290 = "BTO_0005290"
    TE_353_SK_CELL = "BTO_0005290"

    # culture condition:yeast extract-grown cell
    BTO_0005291 = "BTO_0005291"
    CULTURE_CONDITION_YEAST_EXTRACT_GROWN_CELL = "BTO_0005291"

    # NCI-H1155 cell
    BTO_0005292 = "BTO_0005292"
    NCI_H1155_CELL = "BTO_0005292"

    # NCI-H2347 cell
    BTO_0005293 = "BTO_0005293"
    NCI_H2347_CELL = "BTO_0005293"

    # NCI-H647 cell
    BTO_0005294 = "BTO_0005294"
    NCI_H647_CELL = "BTO_0005294"

    # HCC-38 cell
    BTO_0005295 = "BTO_0005295"
    HCC_38_CELL = "BTO_0005295"

    # KBH5.0 cell
    BTO_0005296 = "BTO_0005296"
    KBH5_0_CELL = "BTO_0005296"

    # MEG-01S cell
    BTO_0005297 = "BTO_0005297"
    MEG_01S_CELL = "BTO_0005297"

    # MUM-2B cell
    BTO_0005298 = "BTO_0005298"
    MUM_2B_CELL = "BTO_0005298"

    # MUM-2C cell
    BTO_0005299 = "BTO_0005299"
    MUM_2C_CELL = "BTO_0005299"

    # muscle stem cell
    BTO_0005300 = "BTO_0005300"
    MUSCLE_STEM_CELL = "BTO_0005300"

    # NPrEC cell
    BTO_0005301 = "BTO_0005301"
    NPREC_CELL = "BTO_0005301"

    # GI-102 cell
    BTO_0005302 = "BTO_0005302"
    GI_102_CELL = "BTO_0005302"

    # AS-8 cell
    BTO_0005303 = "BTO_0005303"
    AS_8_CELL = "BTO_0005303"

    # culture condition:rice straw-grown cell
    BTO_0005304 = "BTO_0005304"
    CULTURE_CONDITION_RICE_STRAW_GROWN_CELL = "BTO_0005304"

    # corn ear
    BTO_0005305 = "BTO_0005305"
    CORN_EAR = "BTO_0005305"

    # culture condition:wine-grown cell
    BTO_0005306 = "BTO_0005306"
    CULTURE_CONDITION_WINE_GROWN_CELL = "BTO_0005306"

    # UAMS-32 cell
    BTO_0005307 = "BTO_0005307"
    UAMS_32_CELL = "BTO_0005307"

    # A-716 cell
    BTO_0005308 = "BTO_0005308"
    A_716_CELL = "BTO_0005308"

    # mTOP2beta-4 cell
    BTO_0005309 = "BTO_0005309"
    MTOP2BETA_4_CELL = "BTO_0005309"

    # mTOP2beta-5 cell
    BTO_0005310 = "BTO_0005310"
    MTOP2BETA_5_CELL = "BTO_0005310"

    # SF-xL cell
    BTO_0005311 = "BTO_0005311"
    SF_XL_CELL = "BTO_0005311"

    # amoeba
    BTO_0005312 = "BTO_0005312"
    AMOEBA = "BTO_0005312"

    # nerve sheath
    BTO_0005313 = "BTO_0005313"
    NERVE_SHEATH = "BTO_0005313"

    # nerve sheath cancer cell
    BTO_0005314 = "BTO_0005314"
    NERVE_SHEATH_CANCER_CELL = "BTO_0005314"

    # peripheral nerve sheath cancer cell
    BTO_0005315 = "BTO_0005315"
    PERIPHERAL_NERVE_SHEATH_CANCER_CELL = "BTO_0005315"

    # malignant peripheral nerve sheath cancer cell
    BTO_0005316 = "BTO_0005316"
    MALIGNANT_PERIPHERAL_NERVE_SHEATH_CANCER_CELL = "BTO_0005316"

    # CBRH-7919 cell
    BTO_0005317 = "BTO_0005317"
    CBRH_7919_CELL = "BTO_0005317"

    # cerebrovascular cell
    BTO_0005318 = "BTO_0005318"
    CEREBROVASCULAR_CELL = "BTO_0005318"

    # embryonic germ cell
    BTO_0005319 = "BTO_0005319"
    EMBRYONIC_GERM_CELL = "BTO_0005319"

    # MIN6-N8 cell
    BTO_0005320 = "BTO_0005320"
    MIN6_N8_CELL = "BTO_0005320"

    # B6SUtA1 cell
    BTO_0005321 = "BTO_0005321"
    B6SUTA1_CELL = "BTO_0005321"

    # chronic myelogenous leukemia progenitor cell
    BTO_0005322 = "BTO_0005322"
    CHRONIC_MYELOGENOUS_LEUKEMIA_PROGENITOR_CELL = "BTO_0005322"

    # culture condition:1-hydroxy-2-naphthoic acid-grown cell
    BTO_0005323 = "BTO_0005323"
    CULTURE_CONDITION_1_HYDROXY_2_NAPHTHOIC_ACID_GROWN_CELL = "BTO_0005323"

    # culture condition:chrysene-grown cell
    BTO_0005324 = "BTO_0005324"
    CULTURE_CONDITION_CHRYSENE_GROWN_CELL = "BTO_0005324"

    # culture condition:methanesulfonylmethane-grown cell
    BTO_0005325 = "BTO_0005325"
    CULTURE_CONDITION_METHANESULFONYLMETHANE_GROWN_CELL = "BTO_0005325"

    # culture condition:lactose-grown cell
    BTO_0005326 = "BTO_0005326"
    CULTURE_CONDITION_LACTOSE_GROWN_CELL = "BTO_0005326"

    # culture condition:malate-grown cell
    BTO_0005327 = "BTO_0005327"
    CULTURE_CONDITION_MALATE_GROWN_CELL = "BTO_0005327"

    # culture condition:methylamine-grown cell
    BTO_0005328 = "BTO_0005328"
    CULTURE_CONDITION_METHYLAMINE_GROWN_CELL = "BTO_0005328"

    # culture condition:nitrate-grown cell
    BTO_0005329 = "BTO_0005329"
    CULTURE_CONDITION_NITRATE_GROWN_CELL = "BTO_0005329"

    # culture condition:salicylic acid-grown cell
    BTO_0005330 = "BTO_0005330"
    CULTURE_CONDITION_SALICYLIC_ACID_GROWN_CELL = "BTO_0005330"

    # culture condition:sulfur-grown cell
    BTO_0005331 = "BTO_0005331"
    CULTURE_CONDITION_SULFUR_GROWN_CELL = "BTO_0005331"

    # RWLeu-4 cell
    BTO_0005332 = "BTO_0005332"
    RWLEU_4_CELL = "BTO_0005332"

    # SK-MEL-23 cell
    BTO_0005333 = "BTO_0005333"
    SK_MEL_23_CELL = "BTO_0005333"

    # UKRV-Mel-4 cell
    BTO_0005334 = "BTO_0005334"
    UKRV_MEL_4_CELL = "BTO_0005334"

    # UKRV-Mel-2 cell
    BTO_0005335 = "BTO_0005335"
    UKRV_MEL_2_CELL = "BTO_0005335"

    # Ma-Mel-01 cell
    BTO_0005336 = "BTO_0005336"
    MA_MEL_01_CELL = "BTO_0005336"

    # Ma-Mel-04 cell
    BTO_0005337 = "BTO_0005337"
    MA_MEL_04_CELL = "BTO_0005337"

    # Ma-Mel-05 cell
    BTO_0005338 = "BTO_0005338"
    MA_MEL_05_CELL = "BTO_0005338"

    # Ma-Mel-11 cell
    BTO_0005339 = "BTO_0005339"
    MA_MEL_11_CELL = "BTO_0005339"

    # Ma-Mel-12 cell
    BTO_0005340 = "BTO_0005340"
    MA_MEL_12_CELL = "BTO_0005340"

    # Ma-Mel-17 cell
    BTO_0005341 = "BTO_0005341"
    MA_MEL_17_CELL = "BTO_0005341"

    # Ma-Mel-19 cell
    BTO_0005342 = "BTO_0005342"
    MA_MEL_19_CELL = "BTO_0005342"

    # Ma-Mel-37b cell
    BTO_0005343 = "BTO_0005343"
    MA_MEL_37B_CELL = "BTO_0005343"

    # Ma-Mel-42b cell
    BTO_0005344 = "BTO_0005344"
    MA_MEL_42B_CELL = "BTO_0005344"

    # Ma-Mel-47 cell
    BTO_0005345 = "BTO_0005345"
    MA_MEL_47_CELL = "BTO_0005345"

    # Ma-Mel-52 cell
    BTO_0005346 = "BTO_0005346"
    MA_MEL_52_CELL = "BTO_0005346"

    # UKRV-Mel-06a cell
    BTO_0005347 = "BTO_0005347"
    UKRV_MEL_06A_CELL = "BTO_0005347"

    # UKRV-Mel-21a cell
    BTO_0005348 = "BTO_0005348"
    UKRV_MEL_21A_CELL = "BTO_0005348"

    # UKRV-Mel-27 cell
    BTO_0005349 = "BTO_0005349"
    UKRV_MEL_27_CELL = "BTO_0005349"

    # UKRV-Mel-31 cell
    BTO_0005350 = "BTO_0005350"
    UKRV_MEL_31_CELL = "BTO_0005350"

    # optic cup
    BTO_0005351 = "BTO_0005351"
    OPTIC_CUP = "BTO_0005351"

    # 1-LN cell
    BTO_0005352 = "BTO_0005352"
    _1_LN_CELL = "BTO_0005352"

    # Abrams cell
    BTO_0005353 = "BTO_0005353"
    ABRAMS_CELL = "BTO_0005353"

    # D17 cell
    BTO_0005354 = "BTO_0005354"
    D17_CELL = "BTO_0005354"

    # Grey cell
    BTO_0005355 = "BTO_0005355"
    GREY_CELL = "BTO_0005355"

    # Hughes cell
    BTO_0005356 = "BTO_0005356"
    HUGHES_CELL = "BTO_0005356"

    # Ingles cell
    BTO_0005357 = "BTO_0005357"
    INGLES_CELL = "BTO_0005357"

    # Jarques cell
    BTO_0005358 = "BTO_0005358"
    JARQUES_CELL = "BTO_0005358"

    # Marisco cell
    BTO_0005359 = "BTO_0005359"
    MARISCO_CELL = "BTO_0005359"

    # ALL-SIL cell
    BTO_0005360 = "BTO_0005360"
    ALL_SIL_CELL = "BTO_0005360"

    # amphidial gland
    BTO_0005361 = "BTO_0005361"
    AMPHIDIAL_GLAND = "BTO_0005361"

    # trophoblast giant cell
    BTO_0005362 = "BTO_0005362"
    TROPHOBLAST_GIANT_CELL = "BTO_0005362"

    # COS-31 cell
    BTO_0005363 = "BTO_0005363"
    COS_31_CELL = "BTO_0005363"

    # D-54MG cell
    BTO_0005364 = "BTO_0005364"
    D_54MG_CELL = "BTO_0005364"

    # ECC-1 cell
    BTO_0005365 = "BTO_0005365"
    ECC_1_CELL = "BTO_0005365"

    # NCI-H526 cell
    BTO_0005366 = "BTO_0005366"
    NCI_H526_CELL = "BTO_0005366"

    # H-69AR cell
    BTO_0005367 = "BTO_0005367"
    H_69AR_CELL = "BTO_0005367"

    # HCC-1954 cell
    BTO_0005368 = "BTO_0005368"
    HCC_1954_CELL = "BTO_0005368"

    # HMPOS cell
    BTO_0005369 = "BTO_0005369"
    HMPOS_CELL = "BTO_0005369"

    # CCRF-HSB-2 cell
    BTO_0005370 = "BTO_0005370"
    CCRF_HSB_2_CELL = "BTO_0005370"

    # hymenium
    BTO_0005371 = "BTO_0005371"
    HYMENIUM = "BTO_0005371"

    # SK-N-MC-IXC cell
    BTO_0005372 = "BTO_0005372"
    SK_N_MC_IXC_CELL = "BTO_0005372"

    # oil secretion
    BTO_0005373 = "BTO_0005373"
    OIL_SECRETION = "BTO_0005373"

    # OKF-6 cell
    BTO_0005374 = "BTO_0005374"
    OKF_6_CELL = "BTO_0005374"

    # oral cell line
    BTO_0005375 = "BTO_0005375"
    ORAL_CELL_LINE = "BTO_0005375"

    # P-93AF cell
    BTO_0005376 = "BTO_0005376"
    P_93AF_CELL = "BTO_0005376"

    # RD cell
    BTO_0005377 = "BTO_0005377"
    RD_CELL = "BTO_0005377"

    # Rh-1 cell
    BTO_0005378 = "BTO_0005378"
    RH_1_CELL = "BTO_0005378"

    # Rh-30 cell
    BTO_0005379 = "BTO_0005379"
    RH_30_CELL = "BTO_0005379"

    # Rh-18 cell
    BTO_0005380 = "BTO_0005380"
    RH_18_CELL = "BTO_0005380"

    # Rh-4 cell
    BTO_0005381 = "BTO_0005381"
    RH_4_CELL = "BTO_0005381"

    # Rh-5 cell
    BTO_0005382 = "BTO_0005382"
    RH_5_CELL = "BTO_0005382"

    # Rh-3 cell
    BTO_0005383 = "BTO_0005383"
    RH_3_CELL = "BTO_0005383"

    # Rh-28 cell
    BTO_0005384 = "BTO_0005384"
    RH_28_CELL = "BTO_0005384"

    # root quiescent center
    BTO_0005385 = "BTO_0005385"
    ROOT_QUIESCENT_CENTER = "BTO_0005385"

    # U-1752 cell
    BTO_0005386 = "BTO_0005386"
    U_1752_CELL = "BTO_0005386"

    # SUM-102PT cell
    BTO_0005387 = "BTO_0005387"
    SUM_102PT_CELL = "BTO_0005387"

    # SUM-149 cell
    BTO_0005388 = "BTO_0005388"
    SUM_149_CELL = "BTO_0005388"

    # SUM-44PE cell
    BTO_0005389 = "BTO_0005389"
    SUM_44PE_CELL = "BTO_0005389"

    # SUM-52PE cell
    BTO_0005390 = "BTO_0005390"
    SUM_52PE_CELL = "BTO_0005390"

    # SUM-225 cell
    BTO_0005391 = "BTO_0005391"
    SUM_225_CELL = "BTO_0005391"

    # SUM-229 cell
    BTO_0005392 = "BTO_0005392"
    SUM_229_CELL = "BTO_0005392"

    # SUM-190 cell
    BTO_0005393 = "BTO_0005393"
    SUM_190_CELL = "BTO_0005393"

    # SUM-185 cell
    BTO_0005394 = "BTO_0005394"
    SUM_185_CELL = "BTO_0005394"

    # 58CrPM cell
    BTO_0005395 = "BTO_0005395"
    _58CRPM_CELL = "BTO_0005395"

    # SKMG cell
    BTO_0005396 = "BTO_0005396"
    SKMG_CELL = "BTO_0005396"

    # SH-EP cell
    BTO_0005397 = "BTO_0005397"
    SH_EP_CELL = "BTO_0005397"

    # PaTuO-2 cell
    BTO_0005398 = "BTO_0005398"
    PATUO_2_CELL = "BTO_0005398"

    # POS cell
    BTO_0005399 = "BTO_0005399"
    POS_CELL = "BTO_0005399"

    # BPH cell
    BTO_0005400 = "BTO_0005400"
    BPH_CELL = "BTO_0005400"

    # junctional zone
    BTO_0005401 = "BTO_0005401"
    JUNCTIONAL_ZONE = "BTO_0005401"

    # spongiotrophoblast
    BTO_0005402 = "BTO_0005402"
    SPONGIOTROPHOBLAST = "BTO_0005402"

    # glycogen cell
    BTO_0005403 = "BTO_0005403"
    GLYCOGEN_CELL = "BTO_0005403"

    # labyrinthine zone
    BTO_0005404 = "BTO_0005404"
    LABYRINTHINE_ZONE = "BTO_0005404"

    # velum
    BTO_0005405 = "BTO_0005405"
    VELUM = "BTO_0005405"

    # terminal ampoule
    BTO_0005406 = "BTO_0005406"
    TERMINAL_AMPOULE = "BTO_0005406"

    # culture condition:4-methylsalicylate-grown cell
    BTO_0005407 = "BTO_0005407"
    CULTURE_CONDITION_4_METHYLSALICYLATE_GROWN_CELL = "BTO_0005407"

    # culture condition:5-methylsalicylate-grown cell
    BTO_0005408 = "BTO_0005408"
    CULTURE_CONDITION_5_METHYLSALICYLATE_GROWN_CELL = "BTO_0005408"

    # culture condition:5-chlorosalicylate-grown cell
    BTO_0005409 = "BTO_0005409"
    CULTURE_CONDITION_5_CHLOROSALICYLATE_GROWN_CELL = "BTO_0005409"

    # culture condition:monomethylamine-grown cell
    BTO_0005410 = "BTO_0005410"
    CULTURE_CONDITION_MONOMETHYLAMINE_GROWN_CELL = "BTO_0005410"

    # culture condition:tetramethylammonium-grown cell
    BTO_0005411 = "BTO_0005411"
    CULTURE_CONDITION_TETRAMETHYLAMMONIUM_GROWN_CELL = "BTO_0005411"

    # culture condition:trimethylamine-grown cell
    BTO_0005412 = "BTO_0005412"
    CULTURE_CONDITION_TRIMETHYLAMINE_GROWN_CELL = "BTO_0005412"

    # culture condition:urea-grown cell
    BTO_0005413 = "BTO_0005413"
    CULTURE_CONDITION_UREA_GROWN_CELL = "BTO_0005413"

    # fibrocarcinoma cell
    BTO_0005414 = "BTO_0005414"
    FIBROCARCINOMA_CELL = "BTO_0005414"

    # gastroduodenal mucosa
    BTO_0005415 = "BTO_0005415"
    GASTRODUODENAL_MUCOSA = "BTO_0005415"

    # MNNG/HOS cell
    BTO_0005416 = "BTO_0005416"
    MNNG_HOS_CELL = "BTO_0005416"

    # parietal trophoblast giant cell
    BTO_0005417 = "BTO_0005417"
    PARIETAL_TROPHOBLAST_GIANT_CELL = "BTO_0005417"

    # plant oil gland
    BTO_0005418 = "BTO_0005418"
    PLANT_OIL_GLAND = "BTO_0005418"

    # sinusoidal trophoblast giant cell
    BTO_0005419 = "BTO_0005419"
    SINUSOIDAL_TROPHOBLAST_GIANT_CELL = "BTO_0005419"

    # canal trophoblast giant cell
    BTO_0005420 = "BTO_0005420"
    CANAL_TROPHOBLAST_GIANT_CELL = "BTO_0005420"

    # spiral-associated trophoblast giant cell
    BTO_0005421 = "BTO_0005421"
    SPIRAL_ASSOCIATED_TROPHOBLAST_GIANT_CELL = "BTO_0005421"

    # culture condition:(+)-camphor-grown cell
    BTO_0005422 = "BTO_0005422"
    CULTURE_CONDITION_____CAMPHOR_GROWN_CELL = "BTO_0005422"

    # MDCK-MDR1 cell
    BTO_0005423 = "BTO_0005423"
    MDCK_MDR1_CELL = "BTO_0005423"

    # melan-a Hm cell
    BTO_0005424 = "BTO_0005424"
    MELAN_A_HM_CELL = "BTO_0005424"

    # NCI-H2170 cell
    BTO_0005425 = "BTO_0005425"
    NCI_H2170_CELL = "BTO_0005425"

    # NB-69 cell
    BTO_0005426 = "BTO_0005426"
    NB_69_CELL = "BTO_0005426"

    # NW-1539 cell
    BTO_0005427 = "BTO_0005427"
    NW_1539_CELL = "BTO_0005427"

    # NW-624 cell
    BTO_0005428 = "BTO_0005428"
    NW_624_CELL = "BTO_0005428"

    # PLHC-1/dox cell
    BTO_0005429 = "BTO_0005429"
    PLHC_1_DOX_CELL = "BTO_0005429"

    # STKM-1 cell
    BTO_0005430 = "BTO_0005430"
    STKM_1_CELL = "BTO_0005430"

    # Vgamma9Vdelta2 T-lymphocyte
    BTO_0005431 = "BTO_0005431"
    VGAMMA9VDELTA2_T_LYMPHOCYTE = "BTO_0005431"

    # Bm3-c2 cell
    BTO_0005432 = "BTO_0005432"
    BM3_C2_CELL = "BTO_0005432"

    # culture condition:4-nitrophenol-grown cell
    BTO_0005433 = "BTO_0005433"
    CULTURE_CONDITION_4_NITROPHENOL_GROWN_CELL = "BTO_0005433"

    # culture condition:L-alanine-grown cell
    BTO_0005434 = "BTO_0005434"
    CULTURE_CONDITION_L_ALANINE_GROWN_CELL = "BTO_0005434"

    # culture condition:succinate-glucose-grown cell
    BTO_0005435 = "BTO_0005435"
    CULTURE_CONDITION_SUCCINATE_GLUCOSE_GROWN_CELL = "BTO_0005435"

    # panicle
    BTO_0005436 = "BTO_0005436"
    PANICLE = "BTO_0005436"

    # mammary luminal epithelial cell
    BTO_0005437 = "BTO_0005437"
    MAMMARY_LUMINAL_EPITHELIAL_CELL = "BTO_0005437"

    # HO-8910 cell
    BTO_0005438 = "BTO_0005438"
    HO_8910_CELL = "BTO_0005438"

    # Lu-134-B cell
    BTO_0005439 = "BTO_0005439"
    LU_134_B_CELL = "BTO_0005439"

    # PC-7 cell
    BTO_0005440 = "BTO_0005440"
    PC_7_CELL = "BTO_0005440"

    # lateral root
    BTO_0005441 = "BTO_0005441"
    LATERAL_ROOT = "BTO_0005441"

    # SBC-1 cell
    BTO_0005442 = "BTO_0005442"
    SBC_1_CELL = "BTO_0005442"

    # STKM-2 cell
    BTO_0005443 = "BTO_0005443"
    STKM_2_CELL = "BTO_0005443"

    # root nodule primordium
    BTO_0005444 = "BTO_0005444"
    ROOT_NODULE_PRIMORDIUM = "BTO_0005444"

    # rectal epithelium
    BTO_0005445 = "BTO_0005445"
    RECTAL_EPITHELIUM = "BTO_0005445"

    # plant septum
    BTO_0005446 = "BTO_0005446"
    PLANT_SEPTUM = "BTO_0005446"

    # VMM39 cell
    BTO_0005447 = "BTO_0005447"
    VMM39_CELL = "BTO_0005447"

    # ARL-15C1 cell
    BTO_0005448 = "BTO_0005448"
    ARL_15C1_CELL = "BTO_0005448"

    # ARL-16T2 cell
    BTO_0005449 = "BTO_0005449"
    ARL_16T2_CELL = "BTO_0005449"

    # B-12 cell
    BTO_0005450 = "BTO_0005450"
    B_12_CELL = "BTO_0005450"

    # C32-TG cell
    BTO_0005451 = "BTO_0005451"
    C32_TG_CELL = "BTO_0005451"

    # C6/36 cell
    BTO_0005452 = "BTO_0005452"
    C6_36_CELL = "BTO_0005452"

    # culture condition:CD4+ cell
    BTO_0005453 = "BTO_0005453"
    CULTURE_CONDITION_CD4__CELL = "BTO_0005453"

    # corpus cavernosum
    BTO_0005454 = "BTO_0005454"
    CORPUS_CAVERNOSUM = "BTO_0005454"

    # cotyledonary node
    BTO_0005455 = "BTO_0005455"
    COTYLEDONARY_NODE = "BTO_0005455"

    # FM-516-SV cell
    BTO_0005456 = "BTO_0005456"
    FM_516_SV_CELL = "BTO_0005456"

    # foreskin melanocyte cell line
    BTO_0005457 = "BTO_0005457"
    FORESKIN_MELANOCYTE_CELL_LINE = "BTO_0005457"

    # NCE-G55T2 cell
    BTO_0005458 = "BTO_0005458"
    NCE_G55T2_CELL = "BTO_0005458"

    # GP-202 cell
    BTO_0005459 = "BTO_0005459"
    GP_202_CELL = "BTO_0005459"

    # HaEpi cell
    BTO_0005460 = "BTO_0005460"
    HAEPI_CELL = "BTO_0005460"

    # HBE135-E6E7 cell
    BTO_0005461 = "BTO_0005461"
    HBE135_E6E7_CELL = "BTO_0005461"

    # hemolymph vessel
    BTO_0005462 = "BTO_0005462"
    HEMOLYMPH_VESSEL = "BTO_0005462"

    # Huh-7.5.1 cell
    BTO_0005463 = "BTO_0005463"
    HUH_7_5_1_CELL = "BTO_0005463"

    # IME cell
    BTO_0005464 = "BTO_0005464"
    IME_CELL = "BTO_0005464"

    # intercalary meristem
    BTO_0005465 = "BTO_0005465"
    INTERCALARY_MERISTEM = "BTO_0005465"

    # IPA-220 cell
    BTO_0005466 = "BTO_0005466"
    IPA_220_CELL = "BTO_0005466"

    # KKU-M139 cell
    BTO_0005467 = "BTO_0005467"
    KKU_M139_CELL = "BTO_0005467"

    # labial palp
    BTO_0005468 = "BTO_0005468"
    LABIAL_PALP = "BTO_0005468"

    # RPK-9 cell
    BTO_0005469 = "BTO_0005469"
    RPK_9_CELL = "BTO_0005469"

    # RPK-1 cell
    BTO_0005470 = "BTO_0005470"
    RPK_1_CELL = "BTO_0005470"

    # RPK-59 cell
    BTO_0005471 = "BTO_0005471"
    RPK_59_CELL = "BTO_0005471"

    # RTG-2 cell
    BTO_0005472 = "BTO_0005472"
    RTG_2_CELL = "BTO_0005472"

    # RTG-P1 cell
    BTO_0005473 = "BTO_0005473"
    RTG_P1_CELL = "BTO_0005473"

    # SOB-15 cell
    BTO_0005474 = "BTO_0005474"
    SOB_15_CELL = "BTO_0005474"

    # SUM-149PT cell
    BTO_0005475 = "BTO_0005475"
    SUM_149PT_CELL = "BTO_0005475"

    # SUM-185PE cell
    BTO_0005476 = "BTO_0005476"
    SUM_185PE_CELL = "BTO_0005476"

    # SUM-190PT cell
    BTO_0005477 = "BTO_0005477"
    SUM_190PT_CELL = "BTO_0005477"

    # SUM-225CWN cell
    BTO_0005478 = "BTO_0005478"
    SUM_225CWN_CELL = "BTO_0005478"

    # SUM-229PE cell
    BTO_0005479 = "BTO_0005479"
    SUM_229PE_CELL = "BTO_0005479"

    # WM-278 cell
    BTO_0005480 = "BTO_0005480"
    WM_278_CELL = "BTO_0005480"

    # foreskin keratinocyte cell line
    BTO_0005481 = "BTO_0005481"
    FORESKIN_KERATINOCYTE_CELL_LINE = "BTO_0005481"

    # 38E6E7HFK cell
    BTO_0005482 = "BTO_0005482"
    _38E6E7HFK_CELL = "BTO_0005482"

    # molluscan catch muscle
    BTO_0005483 = "BTO_0005483"
    MOLLUSCAN_CATCH_MUSCLE = "BTO_0005483"

    # DLD-1/alpha-cat cell
    BTO_0005484 = "BTO_0005484"
    DLD_1_ALPHA_CAT_CELL = "BTO_0005484"

    # MC-3T3 cell
    BTO_0005485 = "BTO_0005485"
    MC_3T3_CELL = "BTO_0005485"

    # PK-9 cell
    BTO_0005486 = "BTO_0005486"
    PK_9_CELL = "BTO_0005486"

    # PK-59 cell
    BTO_0005487 = "BTO_0005487"
    PK_59_CELL = "BTO_0005487"

    # osteocyte cell line
    BTO_0005488 = "BTO_0005488"
    OSTEOCYTE_CELL_LINE = "BTO_0005488"

    # MLO-Y4 cell
    BTO_0005489 = "BTO_0005489"
    MLO_Y4_CELL = "BTO_0005489"

    # MM-1 cell
    BTO_0005490 = "BTO_0005490"
    MM_1_CELL = "BTO_0005490"

    # MO-91 cell
    BTO_0005491 = "BTO_0005491"
    MO_91_CELL = "BTO_0005491"

    # MT-2 cell
    BTO_0005492 = "BTO_0005492"
    MT_2_CELL = "BTO_0005492"

    # Mv1Lu cell
    BTO_0005493 = "BTO_0005493"
    MV1LU_CELL = "BTO_0005493"

    # N-1511 cell
    BTO_0005494 = "BTO_0005494"
    N_1511_CELL = "BTO_0005494"

    # NC-37 cell
    BTO_0005495 = "BTO_0005495"
    NC_37_CELL = "BTO_0005495"

    # NHEM-neo cell
    BTO_0005496 = "BTO_0005496"
    NHEM_NEO_CELL = "BTO_0005496"

    # nucleus pulposus cell line
    BTO_0005497 = "BTO_0005497"
    NUCLEUS_PULPOSUS_CELL_LINE = "BTO_0005497"

    # HNPC cell
    BTO_0005498 = "BTO_0005498"
    HNPC_CELL = "BTO_0005498"

    # NYH cell
    BTO_0005499 = "BTO_0005499"
    NYH_CELL = "BTO_0005499"

    # QGP-1 cell
    BTO_0005500 = "BTO_0005500"
    QGP_1_CELL = "BTO_0005500"

    # SW-2 cell
    BTO_0005501 = "BTO_0005501"
    SW_2_CELL = "BTO_0005501"

    # Panc1-bC2GnT-M cell
    BTO_0005502 = "BTO_0005502"
    PANC1_BC2GNT_M_CELL = "BTO_0005502"

    # corpus cavernosum smooth muscle
    BTO_0005503 = "BTO_0005503"
    CORPUS_CAVERNOSUM_SMOOTH_MUSCLE = "BTO_0005503"

    # fungal sporangium
    BTO_0005504 = "BTO_0005504"
    FUNGAL_SPORANGIUM = "BTO_0005504"

    # fungal sporangiophore
    BTO_0005505 = "BTO_0005505"
    FUNGAL_SPORANGIOPHORE = "BTO_0005505"

    # culture condition:H2-grown cell
    BTO_0005506 = "BTO_0005506"
    CULTURE_CONDITION_H2_GROWN_CELL = "BTO_0005506"

    # culture condition:H2/sulfate-grown cell
    BTO_0005507 = "BTO_0005507"
    CULTURE_CONDITION_H2_SULFATE_GROWN_CELL = "BTO_0005507"

    # culture condition:ferric citrate-grown cell
    BTO_0005508 = "BTO_0005508"
    CULTURE_CONDITION_FERRIC_CITRATE_GROWN_CELL = "BTO_0005508"

    # culture condition:2-aminophenol-grown cell
    BTO_0005509 = "BTO_0005509"
    CULTURE_CONDITION_2_AMINOPHENOL_GROWN_CELL = "BTO_0005509"

    # culture condition:2-phenylethanol-grown cell
    BTO_0005510 = "BTO_0005510"
    CULTURE_CONDITION_2_PHENYLETHANOL_GROWN_CELL = "BTO_0005510"

    # embryonic carcinoma cell
    BTO_0005511 = "BTO_0005511"
    EMBRYONIC_CARCINOMA_CELL = "BTO_0005511"

    # basal node
    BTO_0005512 = "BTO_0005512"
    BASAL_NODE = "BTO_0005512"

    # cercaria
    BTO_0005513 = "BTO_0005513"
    CERCARIA = "BTO_0005513"

    # gonadal sheath cell
    BTO_0005514 = "BTO_0005514"
    GONADAL_SHEATH_CELL = "BTO_0005514"

    # leaf vein
    BTO_0005515 = "BTO_0005515"
    LEAF_VEIN = "BTO_0005515"

    # wood
    BTO_0005516 = "BTO_0005516"
    WOOD = "BTO_0005516"

    # lyophilized cell
    BTO_0005517 = "BTO_0005517"
    LYOPHILIZED_CELL = "BTO_0005517"

    # PC-9 cell
    BTO_0005518 = "BTO_0005518"
    PC_9_CELL = "BTO_0005518"

    # spermathecal-uterine valve
    BTO_0005519 = "BTO_0005519"
    SPERMATHECAL_UTERINE_VALVE = "BTO_0005519"

    # uterine seam cell
    BTO_0005520 = "BTO_0005520"
    UTERINE_SEAM_CELL = "BTO_0005520"

    # GM0536 cell
    BTO_0005521 = "BTO_0005521"
    GM0536_CELL = "BTO_0005521"

    # plant epidermal cell
    BTO_0005522 = "BTO_0005522"
    PLANT_EPIDERMAL_CELL = "BTO_0005522"

    # culture condition:anaerobic and sulfate-thiosulfate-lactate-grown cell
    BTO_0005523 = "BTO_0005523"
    CULTURE_CONDITION_ANAEROBIC_AND_SULFATE_THIOSULFATE_LACTATE_GROWN_CELL = (
        "BTO_0005523"
    )

    # plant lip
    BTO_0005524 = "BTO_0005524"
    PLANT_LIP = "BTO_0005524"

    # plant primordium
    BTO_0005525 = "BTO_0005525"
    PLANT_PRIMORDIUM = "BTO_0005525"

    # axillary bud primordium
    BTO_0005526 = "BTO_0005526"
    AXILLARY_BUD_PRIMORDIUM = "BTO_0005526"

    # lateral root primordium
    BTO_0005527 = "BTO_0005527"
    LATERAL_ROOT_PRIMORDIUM = "BTO_0005527"

    # plant secretory cell
    BTO_0005528 = "BTO_0005528"
    PLANT_SECRETORY_CELL = "BTO_0005528"

    # plant hair
    BTO_0005529 = "BTO_0005529"
    PLANT_HAIR = "BTO_0005529"

    # plant glandular hair
    BTO_0005530 = "BTO_0005530"
    PLANT_GLANDULAR_HAIR = "BTO_0005530"

    # plant scale
    BTO_0005531 = "BTO_0005531"
    PLANT_SCALE = "BTO_0005531"

    # plant zygote
    BTO_0005532 = "BTO_0005532"
    PLANT_ZYGOTE = "BTO_0005532"

    # fungal primordium
    BTO_0005533 = "BTO_0005533"
    FUNGAL_PRIMORDIUM = "BTO_0005533"

    # arcuate nucleus
    BTO_0005534 = "BTO_0005534"
    ARCUATE_NUCLEUS = "BTO_0005534"

    # culture condition:CD56+ cell
    BTO_0005535 = "BTO_0005535"
    CULTURE_CONDITION_CD56__CELL = "BTO_0005535"

    # culture condition:copper-containing medium-grown cell
    BTO_0005536 = "BTO_0005536"
    CULTURE_CONDITION_COPPER_CONTAINING_MEDIUM_GROWN_CELL = "BTO_0005536"

    # culture condition:beta-phenylethylamine-grown cell
    BTO_0005537 = "BTO_0005537"
    CULTURE_CONDITION_BETA_PHENYLETHYLAMINE_GROWN_CELL = "BTO_0005537"

    # culture condition:copper-depleted medium-grown cell
    BTO_0005538 = "BTO_0005538"
    CULTURE_CONDITION_COPPER_DEPLETED_MEDIUM_GROWN_CELL = "BTO_0005538"

    # culture condition:cysteate-grown cell
    BTO_0005539 = "BTO_0005539"
    CULTURE_CONDITION_CYSTEATE_GROWN_CELL = "BTO_0005539"

    # culture condition:dimethylsulfone-grown cell
    BTO_0005540 = "BTO_0005540"
    CULTURE_CONDITION_DIMETHYLSULFONE_GROWN_CELL = "BTO_0005540"

    # culture condition:methylsulfone-grown cell
    BTO_0005541 = "BTO_0005541"
    CULTURE_CONDITION_METHYLSULFONE_GROWN_CELL = "BTO_0005541"

    # inflorescence primordium
    BTO_0005542 = "BTO_0005542"
    INFLORESCENCE_PRIMORDIUM = "BTO_0005542"

    # uterine epithelial cell
    BTO_0005543 = "BTO_0005543"
    UTERINE_EPITHELIAL_CELL = "BTO_0005543"

    # gastrointestinal adenocarcinoma cell
    BTO_0005544 = "BTO_0005544"
    GASTROINTESTINAL_ADENOCARCINOMA_CELL = "BTO_0005544"

    # renal epithelial cell
    BTO_0005545 = "BTO_0005545"
    RENAL_EPITHELIAL_CELL = "BTO_0005545"

    # tuber meristem
    BTO_0005546 = "BTO_0005546"
    TUBER_MERISTEM = "BTO_0005546"

    # para-high vocal center
    BTO_0005547 = "BTO_0005547"
    PARA_HIGH_VOCAL_CENTER = "BTO_0005547"

    # HEK-293ET cell
    BTO_0005548 = "BTO_0005548"
    HEK_293ET_CELL = "BTO_0005548"

    # NIH-3T3-ras cell
    BTO_0005549 = "BTO_0005549"
    NIH_3T3_RAS_CELL = "BTO_0005549"

    # 8505C cell
    BTO_0005550 = "BTO_0005550"
    _8505C_CELL = "BTO_0005550"

    # abdominal aorta aneurysm disease specific cell type
    BTO_0005551 = "BTO_0005551"
    ABDOMINAL_AORTA_ANEURYSM_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005551"

    # vertebral endplate
    BTO_0005552 = "BTO_0005552"
    VERTEBRAL_ENDPLATE = "BTO_0005552"

    # aortic intima
    BTO_0005553 = "BTO_0005553"
    AORTIC_INTIMA = "BTO_0005553"

    # B7E3 cell
    BTO_0005554 = "BTO_0005554"
    B7E3_CELL = "BTO_0005554"

    # basal prostate epithelium cell
    BTO_0005555 = "BTO_0005555"
    BASAL_PROSTATE_EPITHELIUM_CELL = "BTO_0005555"

    # luminal prostate epithelium cell
    BTO_0005556 = "BTO_0005556"
    LUMINAL_PROSTATE_EPITHELIUM_CELL = "BTO_0005556"

    # BP-ALL cell
    BTO_0005557 = "BTO_0005557"
    BP_ALL_CELL = "BTO_0005557"

    # T/C-28a4 cell
    BTO_0005558 = "BTO_0005558"
    T_C_28A4_CELL = "BTO_0005558"

    # Caki-dTub cell
    BTO_0005559 = "BTO_0005559"
    CAKI_DTUB_CELL = "BTO_0005559"

    # C8-MEF cell
    BTO_0005560 = "BTO_0005560"
    C8_MEF_CELL = "BTO_0005560"

    # C9-MEF cell
    BTO_0005561 = "BTO_0005561"
    C9_MEF_CELL = "BTO_0005561"

    # cardiac microvascular endothelial cell
    BTO_0005562 = "BTO_0005562"
    CARDIAC_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0005562"

    # dental lamina
    BTO_0005563 = "BTO_0005563"
    DENTAL_LAMINA = "BTO_0005563"

    # EBV-B cell
    BTO_0005564 = "BTO_0005564"
    EBV_B_CELL = "BTO_0005564"

    # embryonic tracheal system
    BTO_0005565 = "BTO_0005565"
    EMBRYONIC_TRACHEAL_SYSTEM = "BTO_0005565"

    # epithelial lining fluid
    BTO_0005566 = "BTO_0005566"
    EPITHELIAL_LINING_FLUID = "BTO_0005566"

    # esophageal adenocarcinoma cell
    BTO_0005567 = "BTO_0005567"
    ESOPHAGEAL_ADENOCARCINOMA_CELL = "BTO_0005567"

    # gastrointestinal mucosa
    BTO_0005568 = "BTO_0005568"
    GASTROINTESTINAL_MUCOSA = "BTO_0005568"

    # hair follicle dermal papilla cell
    BTO_0005569 = "BTO_0005569"
    HAIR_FOLLICLE_DERMAL_PAPILLA_CELL = "BTO_0005569"

    # HFDPC cell
    BTO_0005570 = "BTO_0005570"
    HFDPC_CELL = "BTO_0005570"

    # HAE cell
    BTO_0005571 = "BTO_0005571"
    HAE_CELL = "BTO_0005571"

    # HCE-4 cell
    BTO_0005572 = "BTO_0005572"
    HCE_4_CELL = "BTO_0005572"

    # HCE-6 cell
    BTO_0005573 = "BTO_0005573"
    HCE_6_CELL = "BTO_0005573"

    # ileum smooth muscle
    BTO_0005574 = "BTO_0005574"
    ILEUM_SMOOTH_MUSCLE = "BTO_0005574"

    # ileum smooth muscle cell
    BTO_0005575 = "BTO_0005575"
    ILEUM_SMOOTH_MUSCLE_CELL = "BTO_0005575"

    # inguinal canal
    BTO_0005576 = "BTO_0005576"
    INGUINAL_CANAL = "BTO_0005576"

    # lung disease specific cell type
    BTO_0005577 = "BTO_0005577"
    LUNG_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005577"

    # lymphangioleiomyomatosis disease specific cell type
    BTO_0005578 = "BTO_0005578"
    LYMPHANGIOLEIOMYOMATOSIS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005578"

    # acute undifferentiated leukemia cell
    BTO_0005579 = "BTO_0005579"
    ACUTE_UNDIFFERENTIATED_LEUKEMIA_CELL = "BTO_0005579"

    # WDNET cell
    BTO_0005580 = "BTO_0005580"
    WDNET_CELL = "BTO_0005580"

    # vestibular sensory epithelium
    BTO_0005581 = "BTO_0005581"
    VESTIBULAR_SENSORY_EPITHELIUM = "BTO_0005581"

    # Ra-2 cell
    BTO_0005582 = "BTO_0005582"
    RA_2_CELL = "BTO_0005582"

    # promonocytic leukemia cell line
    BTO_0005583 = "BTO_0005583"
    PROMONOCYTIC_LEUKEMIA_CELL_LINE = "BTO_0005583"

    # promonocytic leukemia cell
    BTO_0005584 = "BTO_0005584"
    PROMONOCYTIC_LEUKEMIA_CELL = "BTO_0005584"

    # prepolar cell
    BTO_0005585 = "BTO_0005585"
    PREPOLAR_CELL = "BTO_0005585"

    # polar cell
    BTO_0005586 = "BTO_0005586"
    POLAR_CELL = "BTO_0005586"

    # stalk cell
    BTO_0005587 = "BTO_0005587"
    STALK_CELL = "BTO_0005587"

    # peg cell
    BTO_0005588 = "BTO_0005588"
    PEG_CELL = "BTO_0005588"

    # oviduct ciliated cell
    BTO_0005589 = "BTO_0005589"
    OVIDUCT_CILIATED_CELL = "BTO_0005589"

    # cervical adenocarcinoma cell line
    BTO_0005590 = "BTO_0005590"
    CERVICAL_ADENOCARCINOMA_CELL_LINE = "BTO_0005590"

    # mesolimbic dopaminergic system
    BTO_0005591 = "BTO_0005591"
    MESOLIMBIC_DOPAMINERGIC_SYSTEM = "BTO_0005591"

    # mesocortical dopaminergic system
    BTO_0005592 = "BTO_0005592"
    MESOCORTICAL_DOPAMINERGIC_SYSTEM = "BTO_0005592"

    # mesocorticolimbic dopaminergic system
    BTO_0005593 = "BTO_0005593"
    MESOCORTICOLIMBIC_DOPAMINERGIC_SYSTEM = "BTO_0005593"

    # metastatic renal cell carcinoma cell
    BTO_0005594 = "BTO_0005594"
    METASTATIC_RENAL_CELL_CARCINOMA_CELL = "BTO_0005594"

    # microplantlet suspension culture
    BTO_0005595 = "BTO_0005595"
    MICROPLANTLET_SUSPENSION_CULTURE = "BTO_0005595"

    # epitheloid cell
    BTO_0005596 = "BTO_0005596"
    EPITHELOID_CELL = "BTO_0005596"

    # Langhans giant cell
    BTO_0005597 = "BTO_0005597"
    LANGHANS_GIANT_CELL = "BTO_0005597"

    # peritubular contractile cell
    BTO_0005598 = "BTO_0005598"
    PERITUBULAR_CONTRACTILE_CELL = "BTO_0005598"

    # periodontal ligament cell
    BTO_0005599 = "BTO_0005599"
    PERIODONTAL_LIGAMENT_CELL = "BTO_0005599"

    # outer nuclear layer
    BTO_0005600 = "BTO_0005600"
    OUTER_NUCLEAR_LAYER = "BTO_0005600"

    # paracentral lobule
    BTO_0005601 = "BTO_0005601"
    PARACENTRAL_LOBULE = "BTO_0005601"

    # anterior paracentral gyrus
    BTO_0005602 = "BTO_0005602"
    ANTERIOR_PARACENTRAL_GYRUS = "BTO_0005602"

    # posterior paracentral gyrus
    BTO_0005603 = "BTO_0005603"
    POSTERIOR_PARACENTRAL_GYRUS = "BTO_0005603"

    # pharate pupal cuticle
    BTO_0005604 = "BTO_0005604"
    PHARATE_PUPAL_CUTICLE = "BTO_0005604"

    # pulmonary neuroendocrine tumor cell
    BTO_0005605 = "BTO_0005605"
    PULMONARY_NEUROENDOCRINE_TUMOR_CELL = "BTO_0005605"

    # precerebellar system
    BTO_0005606 = "BTO_0005606"
    PRECEREBELLAR_SYSTEM = "BTO_0005606"

    # gamma delta T-lymphocyte
    BTO_0005607 = "BTO_0005607"
    GAMMA_DELTA_T_LYMPHOCYTE = "BTO_0005607"

    # pupal wing
    BTO_0005608 = "BTO_0005608"
    PUPAL_WING = "BTO_0005608"

    # pupal wing cuticle
    BTO_0005609 = "BTO_0005609"
    PUPAL_WING_CUTICLE = "BTO_0005609"

    # ventricular aneurysm disease specific cell type
    BTO_0005610 = "BTO_0005610"
    VENTRICULAR_ANEURYSM_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005610"

    # B16-BL6T cell
    BTO_0005611 = "BTO_0005611"
    B16_BL6T_CELL = "BTO_0005611"

    # BL-6 cell
    BTO_0005612 = "BTO_0005612"
    BL_6_CELL = "BTO_0005612"

    # BMC-2 cell
    BTO_0005613 = "BTO_0005613"
    BMC_2_CELL = "BTO_0005613"

    # BMA cell
    BTO_0005614 = "BTO_0005614"
    BMA_CELL = "BTO_0005614"

    # KM-20C cell
    BTO_0005615 = "BTO_0005615"
    KM_20C_CELL = "BTO_0005615"

    # Asp-86 cell
    BTO_0005616 = "BTO_0005616"
    ASP_86_CELL = "BTO_0005616"

    # Sly-1 cell
    BTO_0005617 = "BTO_0005617"
    SLY_1_CELL = "BTO_0005617"

    # subpharyngeal region
    BTO_0005618 = "BTO_0005618"
    SUBPHARYNGEAL_REGION = "BTO_0005618"

    # cladode
    BTO_0005619 = "BTO_0005619"
    CLADODE = "BTO_0005619"

    # CCE-24 cell
    BTO_0005620 = "BTO_0005620"
    CCE_24_CELL = "BTO_0005620"

    # Hep-G2/2.15 cell
    BTO_0005621 = "BTO_0005621"
    HEP_G2_2_15_CELL = "BTO_0005621"

    # K3OHD cell
    BTO_0005622 = "BTO_0005622"
    K3OHD_CELL = "BTO_0005622"

    # neuroepithelial cell line
    BTO_0005623 = "BTO_0005623"
    NEUROEPITHELIAL_CELL_LINE = "BTO_0005623"

    # NE-4C cell
    BTO_0005624 = "BTO_0005624"
    NE_4C_CELL = "BTO_0005624"

    # NE-GFP-4C cell
    BTO_0005625 = "BTO_0005625"
    NE_GFP_4C_CELL = "BTO_0005625"

    # osteoarticular cell
    BTO_0005626 = "BTO_0005626"
    OSTEOARTICULAR_CELL = "BTO_0005626"

    # parametrium
    BTO_0005627 = "BTO_0005627"
    PARAMETRIUM = "BTO_0005627"

    # parametrial fat pad
    BTO_0005628 = "BTO_0005628"
    PARAMETRIAL_FAT_PAD = "BTO_0005628"

    # satellite glial cell
    BTO_0005629 = "BTO_0005629"
    SATELLITE_GLIAL_CELL = "BTO_0005629"

    # sensory ganglion
    BTO_0005630 = "BTO_0005630"
    SENSORY_GANGLION = "BTO_0005630"

    # G3/F11 cell
    BTO_0005631 = "BTO_0005631"
    G3_F11_CELL = "BTO_0005631"

    # sympodium
    BTO_0005632 = "BTO_0005632"
    SYMPODIUM = "BTO_0005632"

    # monopodium
    BTO_0005633 = "BTO_0005633"
    MONOPODIUM = "BTO_0005633"

    # TIG-7 cell
    BTO_0005634 = "BTO_0005634"
    TIG_7_CELL = "BTO_0005634"

    # culture condition:avicel-grown cell
    BTO_0005635 = "BTO_0005635"
    CULTURE_CONDITION_AVICEL_GROWN_CELL = "BTO_0005635"

    # culture condition:wheat bran-grown cell
    BTO_0005636 = "BTO_0005636"
    CULTURE_CONDITION_WHEAT_BRAN_GROWN_CELL = "BTO_0005636"

    # Idiopathic pulmonary fibrosis disease specific cell type
    BTO_0005637 = "BTO_0005637"
    IDIOPATHIC_PULMONARY_FIBROSIS_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005637"

    # LF1 cell
    BTO_0005638 = "BTO_0005638"
    LF1_CELL = "BTO_0005638"

    # LF2 cell
    BTO_0005639 = "BTO_0005639"
    LF2_CELL = "BTO_0005639"

    # aortic adventitial fibroblast
    BTO_0005640 = "BTO_0005640"
    AORTIC_ADVENTITIAL_FIBROBLAST = "BTO_0005640"

    # awn
    BTO_0005641 = "BTO_0005641"
    AWN = "BTO_0005641"

    # culture condition:3-hydroxyphenylacetate-grown cell
    BTO_0005642 = "BTO_0005642"
    CULTURE_CONDITION_3_HYDROXYPHENYLACETATE_GROWN_CELL = "BTO_0005642"

    # culture condition:acetate/raffinose-grown cell
    BTO_0005643 = "BTO_0005643"
    CULTURE_CONDITION_ACETATE_RAFFINOSE_GROWN_CELL = "BTO_0005643"

    # culture condition:D-galacturonate-grown cell
    BTO_0005644 = "BTO_0005644"
    CULTURE_CONDITION_D_GALACTURONATE_GROWN_CELL = "BTO_0005644"

    # culture condition:D-glucosaminate-grown cell
    BTO_0005645 = "BTO_0005645"
    CULTURE_CONDITION_D_GLUCOSAMINATE_GROWN_CELL = "BTO_0005645"

    # culture condition:D-mannitol-grown cell
    BTO_0005646 = "BTO_0005646"
    CULTURE_CONDITION_D_MANNITOL_GROWN_CELL = "BTO_0005646"

    # culture condition:glycine betaine-grown cell
    BTO_0005647 = "BTO_0005647"
    CULTURE_CONDITION_GLYCINE_BETAINE_GROWN_CELL = "BTO_0005647"

    # culture condition:isoprimeverose-grown cell
    BTO_0005648 = "BTO_0005648"
    CULTURE_CONDITION_ISOPRIMEVEROSE_GROWN_CELL = "BTO_0005648"

    # culture condition:isopropanol-grown cell
    BTO_0005649 = "BTO_0005649"
    CULTURE_CONDITION_ISOPROPANOL_GROWN_CELL = "BTO_0005649"

    # culture condition:N-acetyltaurine-grown cell
    BTO_0005650 = "BTO_0005650"
    CULTURE_CONDITION_N_ACETYLTAURINE_GROWN_CELL = "BTO_0005650"

    # culture condition:scyllo-inositol-grown cell
    BTO_0005651 = "BTO_0005651"
    CULTURE_CONDITION_SCYLLO_INOSITOL_GROWN_CELL = "BTO_0005651"

    # culture condition:tetradecyltrimethylammonium bromide-grown cell
    BTO_0005652 = "BTO_0005652"
    CULTURE_CONDITION_TETRADECYLTRIMETHYLAMMONIUM_BROMIDE_GROWN_CELL = "BTO_0005652"

    # culture condition:tetrathionate-grown cell
    BTO_0005653 = "BTO_0005653"
    CULTURE_CONDITION_TETRATHIONATE_GROWN_CELL = "BTO_0005653"

    # nerve ring
    BTO_0005654 = "BTO_0005654"
    NERVE_RING = "BTO_0005654"

    # Th17 cell
    BTO_0005655 = "BTO_0005655"
    TH17_CELL = "BTO_0005655"

    # Z-12 cell
    BTO_0005656 = "BTO_0005656"
    Z_12_CELL = "BTO_0005656"

    # adrenal cortex steroidogenic cell
    BTO_0005657 = "BTO_0005657"
    ADRENAL_CORTEX_STEROIDOGENIC_CELL = "BTO_0005657"

    # testis steroidogenic cell
    BTO_0005658 = "BTO_0005658"
    TESTIS_STEROIDOGENIC_CELL = "BTO_0005658"

    # ovarian steroidogenic cell
    BTO_0005659 = "BTO_0005659"
    OVARIAN_STEROIDOGENIC_CELL = "BTO_0005659"

    # corolla tube
    BTO_0005660 = "BTO_0005660"
    COROLLA_TUBE = "BTO_0005660"

    # buccal mass
    BTO_0005661 = "BTO_0005661"
    BUCCAL_MASS = "BTO_0005661"

    # buccal muscle
    BTO_0005662 = "BTO_0005662"
    BUCCAL_MUSCLE = "BTO_0005662"

    # culture condition:autotrophically-grown cell
    BTO_0005663 = "BTO_0005663"
    CULTURE_CONDITION_AUTOTROPHICALLY_GROWN_CELL = "BTO_0005663"

    # COGA-1A cell
    BTO_0005664 = "BTO_0005664"
    COGA_1A_CELL = "BTO_0005664"

    # COGA-13 cell
    BTO_0005665 = "BTO_0005665"
    COGA_13_CELL = "BTO_0005665"

    # Caco-2/AQ cell
    BTO_0005666 = "BTO_0005666"
    CACO_2_AQ_CELL = "BTO_0005666"

    # NCI-H889 cell
    BTO_0005667 = "BTO_0005667"
    NCI_H889_CELL = "BTO_0005667"

    # DMS-53 cell
    BTO_0005668 = "BTO_0005668"
    DMS_53_CELL = "BTO_0005668"

    # NCI-H295A cell
    BTO_0005669 = "BTO_0005669"
    NCI_H295A_CELL = "BTO_0005669"

    # C-20/A4 cell
    BTO_0005670 = "BTO_0005670"
    C_20_A4_CELL = "BTO_0005670"

    # KGN cell
    BTO_0005671 = "BTO_0005671"
    KGN_CELL = "BTO_0005671"

    # LNCaP-C4-2 cell
    BTO_0005672 = "BTO_0005672"
    LNCAP_C4_2_CELL = "BTO_0005672"

    # LNCaP-CL1 cell
    BTO_0005673 = "BTO_0005673"
    LNCAP_CL1_CELL = "BTO_0005673"

    # SW-60 cell
    BTO_0005674 = "BTO_0005674"
    SW_60_CELL = "BTO_0005674"

    # BNL-HCC cell
    BTO_0005675 = "BTO_0005675"
    BNL_HCC_CELL = "BTO_0005675"

    # vaginal mucosa
    BTO_0005676 = "BTO_0005676"
    VAGINAL_MUCOSA = "BTO_0005676"

    # BmN4-SID1 cell
    BTO_0005677 = "BTO_0005677"
    BMN4_SID1_CELL = "BTO_0005677"

    # cervicovaginal cell
    BTO_0005678 = "BTO_0005678"
    CERVICOVAGINAL_CELL = "BTO_0005678"

    # small luteal cell
    BTO_0005679 = "BTO_0005679"
    SMALL_LUTEAL_CELL = "BTO_0005679"

    # large luteal cell
    BTO_0005680 = "BTO_0005680"
    LARGE_LUTEAL_CELL = "BTO_0005680"

    # storage root
    BTO_0005681 = "BTO_0005681"
    STORAGE_ROOT = "BTO_0005681"

    # 2B4-T cell
    BTO_0005682 = "BTO_0005682"
    _2B4_T_CELL = "BTO_0005682"

    # VK-2/E6E7 cell
    BTO_0005683 = "BTO_0005683"
    VK_2_E6E7_CELL = "BTO_0005683"

    # MYP-30 cell
    BTO_0005684 = "BTO_0005684"
    MYP_30_CELL = "BTO_0005684"

    # culture condition:4-hydroxybutyrate-grown cell
    BTO_0005685 = "BTO_0005685"
    CULTURE_CONDITION_4_HYDROXYBUTYRATE_GROWN_CELL = "BTO_0005685"

    # culture condition:heterotrophically-grown cell
    BTO_0005686 = "BTO_0005686"
    CULTURE_CONDITION_HETEROTROPHICALLY_GROWN_CELL = "BTO_0005686"

    # culture condition:D-tagatose-grown cell
    BTO_0005687 = "BTO_0005687"
    CULTURE_CONDITION_D_TAGATOSE_GROWN_CELL = "BTO_0005687"

    # shoot apical meristem
    BTO_0005688 = "BTO_0005688"
    SHOOT_APICAL_MERISTEM = "BTO_0005688"

    # atrioventricular node
    BTO_0005689 = "BTO_0005689"
    ATRIOVENTRICULAR_NODE = "BTO_0005689"

    # BmN4 cell
    BTO_0005690 = "BTO_0005690"
    BMN4_CELL = "BTO_0005690"

    # RCC-4 cell
    BTO_0005691 = "BTO_0005691"
    RCC_4_CELL = "BTO_0005691"

    # column
    BTO_0005692 = "BTO_0005692"
    COLUMN = "BTO_0005692"

    # lateral nerve cord
    BTO_0005693 = "BTO_0005693"
    LATERAL_NERVE_CORD = "BTO_0005693"

    # stem leaf
    BTO_0005694 = "BTO_0005694"
    STEM_LEAF = "BTO_0005694"

    # sensorimotor area
    BTO_0005695 = "BTO_0005695"
    SENSORIMOTOR_AREA = "BTO_0005695"

    # amoeboid microglia
    BTO_0005696 = "BTO_0005696"
    AMOEBOID_MICROGLIA = "BTO_0005696"

    # atrichoblast cell
    BTO_0005697 = "BTO_0005697"
    ATRICHOBLAST_CELL = "BTO_0005697"

    # trichoblast cell
    BTO_0005698 = "BTO_0005698"
    TRICHOBLAST_CELL = "BTO_0005698"

    # root epidermal cell
    BTO_0005699 = "BTO_0005699"
    ROOT_EPIDERMAL_CELL = "BTO_0005699"

    # culture condition:6-deoxy-6-sulfoglucose-grown cell
    BTO_0005700 = "BTO_0005700"
    CULTURE_CONDITION_6_DEOXY_6_SULFOGLUCOSE_GROWN_CELL = "BTO_0005700"

    # culture condition:carbon disulfide-grown cell
    BTO_0005701 = "BTO_0005701"
    CULTURE_CONDITION_CARBON_DISULFIDE_GROWN_CELL = "BTO_0005701"

    # culture condition:ferulate-grown cell
    BTO_0005702 = "BTO_0005702"
    CULTURE_CONDITION_FERULATE_GROWN_CELL = "BTO_0005702"

    # culture condition:vanillate-grown cell
    BTO_0005703 = "BTO_0005703"
    CULTURE_CONDITION_VANILLATE_GROWN_CELL = "BTO_0005703"

    # milk gland
    BTO_0005704 = "BTO_0005704"
    MILK_GLAND = "BTO_0005704"

    # headfoot muscle
    BTO_0005705 = "BTO_0005705"
    HEADFOOT_MUSCLE = "BTO_0005705"

    # HEY-1B cell
    BTO_0005706 = "BTO_0005706"
    HEY_1B_CELL = "BTO_0005706"

    # HMEEC cell
    BTO_0005707 = "BTO_0005707"
    HMEEC_CELL = "BTO_0005707"

    # middle ear cell line
    BTO_0005708 = "BTO_0005708"
    MIDDLE_EAR_CELL_LINE = "BTO_0005708"

    # IGR-3 cell
    BTO_0005709 = "BTO_0005709"
    IGR_3_CELL = "BTO_0005709"

    # M5 melanoma cell
    BTO_0005710 = "BTO_0005710"
    M5_MELANOMA_CELL = "BTO_0005710"

    # Mel007 cell
    BTO_0005711 = "BTO_0005711"
    MEL007_CELL = "BTO_0005711"

    # Mel-AT cell
    BTO_0005712 = "BTO_0005712"
    MEL_AT_CELL = "BTO_0005712"

    # Mel-CV cell
    BTO_0005713 = "BTO_0005713"
    MEL_CV_CELL = "BTO_0005713"

    # Mel-FH cell
    BTO_0005714 = "BTO_0005714"
    MEL_FH_CELL = "BTO_0005714"

    # Mel-RM cell
    BTO_0005715 = "BTO_0005715"
    MEL_RM_CELL = "BTO_0005715"

    # Me4405 cell
    BTO_0005716 = "BTO_0005716"
    ME4405_CELL = "BTO_0005716"

    # MM200 cell
    BTO_0005717 = "BTO_0005717"
    MM200_CELL = "BTO_0005717"

    # Mel-JD cell
    BTO_0005718 = "BTO_0005718"
    MEL_JD_CELL = "BTO_0005718"

    # Mel-RMU cell
    BTO_0005719 = "BTO_0005719"
    MEL_RMU_CELL = "BTO_0005719"

    # MOLM-14 cell
    BTO_0005720 = "BTO_0005720"
    MOLM_14_CELL = "BTO_0005720"

    # QGY-7703 cell
    BTO_0005721 = "BTO_0005721"
    QGY_7703_CELL = "BTO_0005721"

    # retrocerebral organ
    BTO_0005722 = "BTO_0005722"
    RETROCEREBRAL_ORGAN = "BTO_0005722"

    # cerebral organ
    BTO_0005723 = "BTO_0005723"
    CEREBRAL_ORGAN = "BTO_0005723"

    # CG-4 cell
    BTO_0005724 = "BTO_0005724"
    CG_4_CELL = "BTO_0005724"

    # HuH-7-Lunet cell
    BTO_0005725 = "BTO_0005725"
    HUH_7_LUNET_CELL = "BTO_0005725"

    # Lunet-Con1 cell
    BTO_0005726 = "BTO_0005726"
    LUNET_CON1_CELL = "BTO_0005726"

    # UOK-262 cell
    BTO_0005727 = "BTO_0005727"
    UOK_262_CELL = "BTO_0005727"

    # gynophore
    BTO_0005728 = "BTO_0005728"
    GYNOPHORE = "BTO_0005728"

    # chemoreceptor cell
    BTO_0005729 = "BTO_0005729"
    CHEMORECEPTOR_CELL = "BTO_0005729"

    # culture condition:chitin-grown cell
    BTO_0005730 = "BTO_0005730"
    CULTURE_CONDITION_CHITIN_GROWN_CELL = "BTO_0005730"

    # culture condition:dichloromethane-grown cell
    BTO_0005731 = "BTO_0005731"
    CULTURE_CONDITION_DICHLOROMETHANE_GROWN_CELL = "BTO_0005731"

    # culture condition:gentisate-grown cell
    BTO_0005732 = "BTO_0005732"
    CULTURE_CONDITION_GENTISATE_GROWN_CELL = "BTO_0005732"

    # culture condition:methyl ferulate-grown cell
    BTO_0005733 = "BTO_0005733"
    CULTURE_CONDITION_METHYL_FERULATE_GROWN_CELL = "BTO_0005733"

    # culture condition:methyl vanillate-grown cell
    BTO_0005734 = "BTO_0005734"
    CULTURE_CONDITION_METHYL_VANILLATE_GROWN_CELL = "BTO_0005734"

    # culture condition:rye flour-grown cell
    BTO_0005735 = "BTO_0005735"
    CULTURE_CONDITION_RYE_FLOUR_GROWN_CELL = "BTO_0005735"

    # Hepa-RG cell
    BTO_0005736 = "BTO_0005736"
    HEPA_RG_CELL = "BTO_0005736"

    # HMVEC cell
    BTO_0005737 = "BTO_0005737"
    HMVEC_CELL = "BTO_0005737"

    # lung microvascular endothelial cell
    BTO_0005738 = "BTO_0005738"
    LUNG_MICROVASCULAR_ENDOTHELIAL_CELL = "BTO_0005738"

    # transfer cell
    BTO_0005739 = "BTO_0005739"
    TRANSFER_CELL = "BTO_0005739"

    # plant stem cell
    BTO_0005740 = "BTO_0005740"
    PLANT_STEM_CELL = "BTO_0005740"

    # lateral meristem
    BTO_0005741 = "BTO_0005741"
    LATERAL_MERISTEM = "BTO_0005741"

    # transfer cell precursor
    BTO_0005742 = "BTO_0005742"
    TRANSFER_CELL_PRECURSOR = "BTO_0005742"

    # mature stage
    BTO_0005743 = "BTO_0005743"
    MATURE_STAGE = "BTO_0005743"

    # vegetative stage
    BTO_0005744 = "BTO_0005744"
    VEGETATIVE_STAGE = "BTO_0005744"

    # SHI-1 cell
    BTO_0005745 = "BTO_0005745"
    SHI_1_CELL = "BTO_0005745"

    # gynostemium
    BTO_0005746 = "BTO_0005746"
    GYNOSTEMIUM = "BTO_0005746"

    # IGR-37 cell
    BTO_0005747 = "BTO_0005747"
    IGR_37_CELL = "BTO_0005747"

    # AC2M2 cell
    BTO_0005748 = "BTO_0005748"
    AC2M2_CELL = "BTO_0005748"

    # 16-HBE cell
    BTO_0005749 = "BTO_0005749"
    _16_HBE_CELL = "BTO_0005749"

    # dentate granule cell
    BTO_0005750 = "BTO_0005750"
    DENTATE_GRANULE_CELL = "BTO_0005750"

    # C8161.9 cell
    BTO_0005751 = "BTO_0005751"
    C8161_9_CELL = "BTO_0005751"

    # CHO-13-5-1 cell
    BTO_0005752 = "BTO_0005752"
    CHO_13_5_1_CELL = "BTO_0005752"

    # CHO-A7 cell
    BTO_0005753 = "BTO_0005753"
    CHO_A7_CELL = "BTO_0005753"

    # choroid plexus cancer cell
    BTO_0005754 = "BTO_0005754"
    CHOROID_PLEXUS_CANCER_CELL = "BTO_0005754"

    # choroid plexus papilloma cell
    BTO_0005755 = "BTO_0005755"
    CHOROID_PLEXUS_PAPILLOMA_CELL = "BTO_0005755"

    # decidual stromal cell
    BTO_0005756 = "BTO_0005756"
    DECIDUAL_STROMAL_CELL = "BTO_0005756"

    # EC-9706 cell
    BTO_0005757 = "BTO_0005757"
    EC_9706_CELL = "BTO_0005757"

    # Eca-109 cell
    BTO_0005758 = "BTO_0005758"
    ECA_109_CELL = "BTO_0005758"

    # epitheliocyte
    BTO_0005759 = "BTO_0005759"
    EPITHELIOCYTE = "BTO_0005759"

    # alveolar epithelial cell
    BTO_0005760 = "BTO_0005760"
    ALVEOLAR_EPITHELIAL_CELL = "BTO_0005760"

    # adrenal glomerulosa cell
    BTO_0005761 = "BTO_0005761"
    ADRENAL_GLOMERULOSA_CELL = "BTO_0005761"

    # colonic mucosa cell
    BTO_0005762 = "BTO_0005762"
    COLONIC_MUCOSA_CELL = "BTO_0005762"

    # culture condition:2,4-dinitroanisole-grown cell
    BTO_0005763 = "BTO_0005763"
    CULTURE_CONDITION_2_4_DINITROANISOLE_GROWN_CELL = "BTO_0005763"

    # culture condition:chitosan-grown cell
    BTO_0005764 = "BTO_0005764"
    CULTURE_CONDITION_CHITOSAN_GROWN_CELL = "BTO_0005764"

    # 2fTGH cell
    BTO_0005765 = "BTO_0005765"
    _2FTGH_CELL = "BTO_0005765"

    # A2780/CP cell
    BTO_0005766 = "BTO_0005766"
    A2780_CP_CELL = "BTO_0005766"

    # buccal gland
    BTO_0005767 = "BTO_0005767"
    BUCCAL_GLAND = "BTO_0005767"

    # epididymal epithelium
    BTO_0005768 = "BTO_0005768"
    EPIDIDYMAL_EPITHELIUM = "BTO_0005768"

    # buccal mucosa cancer cell
    BTO_0005769 = "BTO_0005769"
    BUCCAL_MUCOSA_CANCER_CELL = "BTO_0005769"

    # buccal mucosa cancer cell line
    BTO_0005770 = "BTO_0005770"
    BUCCAL_MUCOSA_CANCER_CELL_LINE = "BTO_0005770"

    # HO-1-N-1 cell
    BTO_0005771 = "BTO_0005771"
    HO_1_N_1_CELL = "BTO_0005771"

    # HO-8910PM
    BTO_0005772 = "BTO_0005772"
    HO_8910PM = "BTO_0005772"

    # HuH-1 cell
    BTO_0005773 = "BTO_0005773"
    HUH_1_CELL = "BTO_0005773"

    # IPC-298 cell
    BTO_0005774 = "BTO_0005774"
    IPC_298_CELL = "BTO_0005774"

    # KBM-7 cell
    BTO_0005775 = "BTO_0005775"
    KBM_7_CELL = "BTO_0005775"

    # LN-71 cell
    BTO_0005776 = "BTO_0005776"
    LN_71_CELL = "BTO_0005776"

    # midgut diverticulum
    BTO_0005777 = "BTO_0005777"
    MIDGUT_DIVERTICULUM = "BTO_0005777"

    # myeloblastoma cell
    BTO_0005778 = "BTO_0005778"
    MYELOBLASTOMA_CELL = "BTO_0005778"

    # NCI-H1838 cell
    BTO_0005779 = "BTO_0005779"
    NCI_H1838_CELL = "BTO_0005779"

    # WM-902B cell
    BTO_0005780 = "BTO_0005780"
    WM_902B_CELL = "BTO_0005780"

    # uroepithelial cell
    BTO_0005781 = "BTO_0005781"
    UROEPITHELIAL_CELL = "BTO_0005781"

    # THLE-5b cell
    BTO_0005782 = "BTO_0005782"
    THLE_5B_CELL = "BTO_0005782"

    # tenocyte
    BTO_0005783 = "BTO_0005783"
    TENOCYTE = "BTO_0005783"

    # syncytium
    BTO_0005784 = "BTO_0005784"
    SYNCYTIUM = "BTO_0005784"

    # embryonic syncytium
    BTO_0005785 = "BTO_0005785"
    EMBRYONIC_SYNCYTIUM = "BTO_0005785"

    # SNU-1 cell
    BTO_0005786 = "BTO_0005786"
    SNU_1_CELL = "BTO_0005786"

    # skeletal muscle satellite cell
    BTO_0005787 = "BTO_0005787"
    SKELETAL_MUSCLE_SATELLITE_CELL = "BTO_0005787"

    # SH-EP1 cell
    BTO_0005788 = "BTO_0005788"
    SH_EP1_CELL = "BTO_0005788"

    # root band
    BTO_0005789 = "BTO_0005789"
    ROOT_BAND = "BTO_0005789"

    # promyelocyte
    BTO_0005790 = "BTO_0005790"
    PROMYELOCYTE = "BTO_0005790"

    # enamel knot
    BTO_0005791 = "BTO_0005791"
    ENAMEL_KNOT = "BTO_0005791"

    # primary enamel knot
    BTO_0005792 = "BTO_0005792"
    PRIMARY_ENAMEL_KNOT = "BTO_0005792"

    # secondary enamel knot
    BTO_0005793 = "BTO_0005793"
    SECONDARY_ENAMEL_KNOT = "BTO_0005793"

    # ophthalmic lavage fluid
    BTO_0005794 = "BTO_0005794"
    OPHTHALMIC_LAVAGE_FLUID = "BTO_0005794"

    # osteoma cell
    BTO_0005795 = "BTO_0005795"
    OSTEOMA_CELL = "BTO_0005795"

    # PEO-1 cell
    BTO_0005796 = "BTO_0005796"
    PEO_1_CELL = "BTO_0005796"

    # PEO-4 cell
    BTO_0005797 = "BTO_0005797"
    PEO_4_CELL = "BTO_0005797"

    # PEO-6 cell
    BTO_0005798 = "BTO_0005798"
    PEO_6_CELL = "BTO_0005798"

    # corticotroph adenoma cell
    BTO_0005799 = "BTO_0005799"
    CORTICOTROPH_ADENOMA_CELL = "BTO_0005799"

    # Neu-7 cell
    BTO_0005800 = "BTO_0005800"
    NEU_7_CELL = "BTO_0005800"

    # K-562/CP cell
    BTO_0005801 = "BTO_0005801"
    K_562_CP_CELL = "BTO_0005801"

    # dentate gyrus HICAP cell
    BTO_0005802 = "BTO_0005802"
    DENTATE_GYRUS_HICAP_CELL = "BTO_0005802"

    # dentate gyrus HIPP cell
    BTO_0005803 = "BTO_0005803"
    DENTATE_GYRUS_HIPP_CELL = "BTO_0005803"

    # dentate gyrus IS-I cell
    BTO_0005804 = "BTO_0005804"
    DENTATE_GYRUS_IS_I_CELL = "BTO_0005804"

    # dentate gyrus IS-II cell
    BTO_0005805 = "BTO_0005805"
    DENTATE_GYRUS_IS_II_CELL = "BTO_0005805"

    # flexor tendon
    BTO_0005806 = "BTO_0005806"
    FLEXOR_TENDON = "BTO_0005806"

    # GI-LA-N cell
    BTO_0005807 = "BTO_0005807"
    GI_LA_N_CELL = "BTO_0005807"

    # GI-ME-N cell
    BTO_0005808 = "BTO_0005808"
    GI_ME_N_CELL = "BTO_0005808"

    # HMVEC-dLy cell
    BTO_0005809 = "BTO_0005809"
    HMVEC_DLY_CELL = "BTO_0005809"

    # immune system
    BTO_0005810 = "BTO_0005810"
    IMMUNE_SYSTEM = "BTO_0005810"

    # cigar leaf
    BTO_0005811 = "BTO_0005811"
    CIGAR_LEAF = "BTO_0005811"

    # lung endothelial cell
    BTO_0005812 = "BTO_0005812"
    LUNG_ENDOTHELIAL_CELL = "BTO_0005812"

    # pancreatic islet cell
    BTO_0005813 = "BTO_0005813"
    PANCREATIC_ISLET_CELL = "BTO_0005813"

    # BEL-7404 cell
    BTO_0005814 = "BTO_0005814"
    BEL_7404_CELL = "BTO_0005814"

    # A-375.S2 cell
    BTO_0005815 = "BTO_0005815"
    A_375_S2_CELL = "BTO_0005815"

    # A549-CR cell
    BTO_0005816 = "BTO_0005816"
    A549_CR_CELL = "BTO_0005816"

    # adrenocortical cell
    BTO_0005817 = "BTO_0005817"
    ADRENOCORTICAL_CELL = "BTO_0005817"

    # BIN-67 cell
    BTO_0005818 = "BTO_0005818"
    BIN_67_CELL = "BTO_0005818"

    # histaminergic neuron
    BTO_0005819 = "BTO_0005819"
    HISTAMINERGIC_NEURON = "BTO_0005819"

    # CATH.a cell
    BTO_0005820 = "BTO_0005820"
    CATH_A_CELL = "BTO_0005820"

    # CMT-167 cell
    BTO_0005821 = "BTO_0005821"
    CMT_167_CELL = "BTO_0005821"

    # cochlear hair cell
    BTO_0005822 = "BTO_0005822"
    COCHLEAR_HAIR_CELL = "BTO_0005822"

    # hair-cell stereocilium
    BTO_0005823 = "BTO_0005823"
    HAIR_CELL_STEREOCILIUM = "BTO_0005823"

    # vestibular hair cell
    BTO_0005824 = "BTO_0005824"
    VESTIBULAR_HAIR_CELL = "BTO_0005824"

    # ctenidium
    BTO_0005825 = "BTO_0005825"
    CTENIDIUM = "BTO_0005825"

    # Detroit-551 cell
    BTO_0005826 = "BTO_0005826"
    DETROIT_551_CELL = "BTO_0005826"

    # FAA-HTC1 cell
    BTO_0005827 = "BTO_0005827"
    FAA_HTC1_CELL = "BTO_0005827"

    # hair follicle epithelium
    BTO_0005828 = "BTO_0005828"
    HAIR_FOLLICLE_EPITHELIUM = "BTO_0005828"

    # frontoparietal cortex
    BTO_0005829 = "BTO_0005829"
    FRONTOPARIETAL_CORTEX = "BTO_0005829"

    # leukodystrophy disease specific cell type
    BTO_0005830 = "BTO_0005830"
    LEUKODYSTROPHY_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005830"

    # globoid cell leukodystrophy disease specific cell type
    BTO_0005831 = "BTO_0005831"
    GLOBOID_CELL_LEUKODYSTROPHY_DISEASE_SPECIFIC_CELL_TYPE = "BTO_0005831"

    # globoid cell
    BTO_0005832 = "BTO_0005832"
    GLOBOID_CELL = "BTO_0005832"

    # plant gall
    BTO_0005833 = "BTO_0005833"
    PLANT_GALL = "BTO_0005833"

    # infectious granuloma cell
    BTO_0005834 = "BTO_0005834"
    INFECTIOUS_GRANULOMA_CELL = "BTO_0005834"

    # granuloma cell
    BTO_0005835 = "BTO_0005835"
    GRANULOMA_CELL = "BTO_0005835"

    # NCI-H1792 cell
    BTO_0005836 = "BTO_0005836"
    NCI_H1792_CELL = "BTO_0005836"

    # NCI-H1944 cell
    BTO_0005837 = "BTO_0005837"
    NCI_H1944_CELL = "BTO_0005837"

    # head and neck cancer cell
    BTO_0005838 = "BTO_0005838"
    HEAD_AND_NECK_CANCER_CELL = "BTO_0005838"

    # HEK-293VnR cell
    BTO_0005839 = "BTO_0005839"
    HEK_293VNR_CELL = "BTO_0005839"

    # Hs888Lu cell
    BTO_0005840 = "BTO_0005840"
    HS888LU_CELL = "BTO_0005840"

    # Hunter's organ
    BTO_0005841 = "BTO_0005841"
    HUNTER_S_ORGAN = "BTO_0005841"

    # Sach's organ
    BTO_0005842 = "BTO_0005842"
    SACH_S_ORGAN = "BTO_0005842"

    # vaginal epitelial cell
    BTO_0005843 = "BTO_0005843"
    VAGINAL_EPITELIAL_CELL = "BTO_0005843"

    # vaginal epithelial cell line
    BTO_0005844 = "BTO_0005844"
    VAGINAL_EPITHELIAL_CELL_LINE = "BTO_0005844"

    # HVEC cell
    BTO_0005845 = "BTO_0005845"
    HVEC_CELL = "BTO_0005845"

    # IMR-5 cell
    BTO_0005846 = "BTO_0005846"
    IMR_5_CELL = "BTO_0005846"

    # Johnston's organ
    BTO_0005847 = "BTO_0005847"
    JOHNSTON_S_ORGAN = "BTO_0005847"

    # K-457 cell
    BTO_0005848 = "BTO_0005848"
    K_457_CELL = "BTO_0005848"

    # KB-CP.5 cell
    BTO_0005849 = "BTO_0005849"
    KB_CP_5_CELL = "BTO_0005849"

    # mucinous ovarian adenocarcinoma cell
    BTO_0005850 = "BTO_0005850"
    MUCINOUS_OVARIAN_ADENOCARCINOMA_CELL = "BTO_0005850"

    # small cell ovarian carcinoma cell
    BTO_0005851 = "BTO_0005851"
    SMALL_CELL_OVARIAN_CARCINOMA_CELL = "BTO_0005851"

    # small cell ovarian carcinoma cell line
    BTO_0005852 = "BTO_0005852"
    SMALL_CELL_OVARIAN_CARCINOMA_CELL_LINE = "BTO_0005852"

    # SCCOHT-1 cell
    BTO_0005853 = "BTO_0005853"
    SCCOHT_1_CELL = "BTO_0005853"

    # pronephric tubule
    BTO_0005854 = "BTO_0005854"
    PRONEPHRIC_TUBULE = "BTO_0005854"

    # SCC-9 cell
    BTO_0005855 = "BTO_0005855"
    SCC_9_CELL = "BTO_0005855"

    # root apex
    BTO_0005856 = "BTO_0005856"
    ROOT_APEX = "BTO_0005856"

    # root cortex
    BTO_0005857 = "BTO_0005857"
    ROOT_CORTEX = "BTO_0005857"

    # root pericycle
    BTO_0005858 = "BTO_0005858"
    ROOT_PERICYCLE = "BTO_0005858"

    # KNS-42 cell
    BTO_0005859 = "BTO_0005859"
    KNS_42_CELL = "BTO_0005859"

    # LA1-55n cell
    BTO_0005860 = "BTO_0005860"
    LA1_55N_CELL = "BTO_0005860"

    # SK-MEL-24 cell
    BTO_0005861 = "BTO_0005861"
    SK_MEL_24_CELL = "BTO_0005861"

    # culture condition:DL-erythro-3,5-diaminohexanoate-grown cell
    BTO_0005862 = "BTO_0005862"
    CULTURE_CONDITION_DL_ERYTHRO_3_5_DIAMINOHEXANOATE_GROWN_CELL = "BTO_0005862"

    # culture condition:ethylamine-grown cell
    BTO_0005863 = "BTO_0005863"
    CULTURE_CONDITION_ETHYLAMINE_GROWN_CELL = "BTO_0005863"

    # culture condition:N-acetyl-DL-phenylalanine-grown cell
    BTO_0005864 = "BTO_0005864"
    CULTURE_CONDITION_N_ACETYL_DL_PHENYLALANINE_GROWN_CELL = "BTO_0005864"

    # U-251SP cell
    BTO_0005865 = "BTO_0005865"
    U_251SP_CELL = "BTO_0005865"

    # MDA435/LCC6 cell
    BTO_0005866 = "BTO_0005866"
    MDA435_LCC6_CELL = "BTO_0005866"

    # MDA435/LCC6MDR1 cell
    BTO_0005867 = "BTO_0005867"
    MDA435_LCC6MDR1_CELL = "BTO_0005867"

    # LNCaP-C4 cell
    BTO_0005868 = "BTO_0005868"
    LNCAP_C4_CELL = "BTO_0005868"

    # miracidium
    BTO_0005869 = "BTO_0005869"
    MIRACIDIUM = "BTO_0005869"

    # MOVAS cell
    BTO_0005870 = "BTO_0005870"
    MOVAS_CELL = "BTO_0005870"

    # naive T-lymphocyte
    BTO_0005871 = "BTO_0005871"
    NAIVE_T_LYMPHOCYTE = "BTO_0005871"

    # NMB cell
    BTO_0005872 = "BTO_0005872"
    NMB_CELL = "BTO_0005872"

    # yolk sac cancer cell line
    BTO_0005873 = "BTO_0005873"
    YOLK_SAC_CANCER_CELL_LINE = "BTO_0005873"

    # NOY-1 cell
    BTO_0005874 = "BTO_0005874"
    NOY_1_CELL = "BTO_0005874"

    # KMS-11/NTKO cell
    BTO_0005875 = "BTO_0005875"
    KMS_11_NTKO_CELL = "BTO_0005875"

    # KMS-11/TKO cell
    BTO_0005876 = "BTO_0005876"
    KMS_11_TKO_CELL = "BTO_0005876"

    # papillary adenocarcinoma cell
    BTO_0005877 = "BTO_0005877"
    PAPILLARY_ADENOCARCINOMA_CELL = "BTO_0005877"

    # PA-TU-8988T cell
    BTO_0005878 = "BTO_0005878"
    PA_TU_8988T_CELL = "BTO_0005878"

    # PA-TU-8988S cell
    BTO_0005879 = "BTO_0005879"
    PA_TU_8988S_CELL = "BTO_0005879"

    # Res-186 cell
    BTO_0005880 = "BTO_0005880"
    RES_186_CELL = "BTO_0005880"

    # Res-259 cell
    BTO_0005881 = "BTO_0005881"
    RES_259_CELL = "BTO_0005881"

    # scolopidium
    BTO_0005882 = "BTO_0005882"
    SCOLOPIDIUM = "BTO_0005882"

    # UACC-3291 cell
    BTO_0005883 = "BTO_0005883"
    UACC_3291_CELL = "BTO_0005883"

    # scolopale cap cell
    BTO_0005884 = "BTO_0005884"
    SCOLOPALE_CAP_CELL = "BTO_0005884"

    # scolopale cell
    BTO_0005885 = "BTO_0005885"
    SCOLOPALE_CELL = "BTO_0005885"

    # seedpod
    BTO_0005886 = "BTO_0005886"
    SEEDPOD = "BTO_0005886"

    # SK-6 cell
    BTO_0005887 = "BTO_0005887"
    SK_6_CELL = "BTO_0005887"

    # UW-479 cell
    BTO_0005888 = "BTO_0005888"
    UW_479_CELL = "BTO_0005888"

    # WIF-B cell
    BTO_0005889 = "BTO_0005889"
    WIF_B_CELL = "BTO_0005889"

    # xylem parenchyma cell
    BTO_0005890 = "BTO_0005890"
    XYLEM_PARENCHYMA_CELL = "BTO_0005890"

    # sporocyst
    BTO_0005891 = "BTO_0005891"
    SPOROCYST = "BTO_0005891"

    # SVOG-3e cell
    BTO_0005892 = "BTO_0005892"
    SVOG_3E_CELL = "BTO_0005892"

    # nonpigmented ciliary epithelium
    BTO_0005893 = "BTO_0005893"
    NONPIGMENTED_CILIARY_EPITHELIUM = "BTO_0005893"

    # pigmented ciliary epithelium
    BTO_0005894 = "BTO_0005894"
    PIGMENTED_CILIARY_EPITHELIUM = "BTO_0005894"

    # UACC-1308 cell
    BTO_0005895 = "BTO_0005895"
    UACC_1308_CELL = "BTO_0005895"

    # UACC-1940 cell
    BTO_0005896 = "BTO_0005896"
    UACC_1940_CELL = "BTO_0005896"

    # UACC-2534 cell
    BTO_0005897 = "BTO_0005897"
    UACC_2534_CELL = "BTO_0005897"

    # UACC-502 cell
    BTO_0005898 = "BTO_0005898"
    UACC_502_CELL = "BTO_0005898"

    # UACC-91 cell
    BTO_0005899 = "BTO_0005899"
    UACC_91_CELL = "BTO_0005899"

    # byssus retractor muscle
    BTO_0005901 = "BTO_0005901"
    BYSSUS_RETRACTOR_MUSCLE = "BTO_0005901"

    # DiFi cell
    BTO_0005902 = "BTO_0005902"
    DIFI_CELL = "BTO_0005902"

    # DMS-273 cell
    BTO_0005903 = "BTO_0005903"
    DMS_273_CELL = "BTO_0005903"

    # EM-2 cell
    BTO_0005904 = "BTO_0005904"
    EM_2_CELL = "BTO_0005904"

    # EM-3 cell
    BTO_0005905 = "BTO_0005905"
    EM_3_CELL = "BTO_0005905"

    # FU-97 cell
    BTO_0005906 = "BTO_0005906"
    FU_97_CELL = "BTO_0005906"

    # H-MESO-1 cell
    BTO_0005907 = "BTO_0005907"
    H_MESO_1_CELL = "BTO_0005907"

    # IM-95 cell
    BTO_0005908 = "BTO_0005908"
    IM_95_CELL = "BTO_0005908"

    # JURL-MK1 cell
    BTO_0005909 = "BTO_0005909"
    JURL_MK1_CELL = "BTO_0005909"

    # JURL-MK2 cell
    BTO_0005910 = "BTO_0005910"
    JURL_MK2_CELL = "BTO_0005910"

    # KM-20L2 cell
    BTO_0005911 = "BTO_0005911"
    KM_20L2_CELL = "BTO_0005911"

    # LP-1 cell
    BTO_0005912 = "BTO_0005912"
    LP_1_CELL = "BTO_0005912"

    # MEC-1 cell
    BTO_0005913 = "BTO_0005913"
    MEC_1_CELL = "BTO_0005913"

    # MEC-2 cell
    BTO_0005914 = "BTO_0005914"
    MEC_2_CELL = "BTO_0005914"

    # NCI-H727 cell
    BTO_0005915 = "BTO_0005915"
    NCI_H727_CELL = "BTO_0005915"

    # NOMO-1 cell
    BTO_0005916 = "BTO_0005916"
    NOMO_1_CELL = "BTO_0005916"

    # NUGC-4 cell
    BTO_0005917 = "BTO_0005917"
    NUGC_4_CELL = "BTO_0005917"

    # OCUM-1 cell
    BTO_0005918 = "BTO_0005918"
    OCUM_1_CELL = "BTO_0005918"

    # OPM-2 cell
    BTO_0005919 = "BTO_0005919"
    OPM_2_CELL = "BTO_0005919"

    # laryngeal cancer cell line
    BTO_0005920 = "BTO_0005920"
    LARYNGEAL_CANCER_CELL_LINE = "BTO_0005920"

    # laryngeal squamous cell carcinoma cell line
    BTO_0005921 = "BTO_0005921"
    LARYNGEAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0005921"

    # SNU-1076 cell
    BTO_0005922 = "BTO_0005922"
    SNU_1076_CELL = "BTO_0005922"

    # SNU-1214 cell
    BTO_0005923 = "BTO_0005923"
    SNU_1214_CELL = "BTO_0005923"

    # SNU-1066 cell
    BTO_0005924 = "BTO_0005924"
    SNU_1066_CELL = "BTO_0005924"

    # SNU-899 cell
    BTO_0005925 = "BTO_0005925"
    SNU_899_CELL = "BTO_0005925"

    # SNU-585 cell
    BTO_0005926 = "BTO_0005926"
    SNU_585_CELL = "BTO_0005926"

    # SNU-46 cell
    BTO_0005927 = "BTO_0005927"
    SNU_46_CELL = "BTO_0005927"

    # PL-21 cell
    BTO_0005928 = "BTO_0005928"
    PL_21_CELL = "BTO_0005928"

    # SCH cell
    BTO_0005929 = "BTO_0005929"
    SCH_CELL = "BTO_0005929"

    # C3H10T1/2 clone 8 cell
    BTO_0005930 = "BTO_0005930"
    C3H10T1_2_CLONE_8_CELL = "BTO_0005930"

    # CEM-C2 cell
    BTO_0005931 = "BTO_0005931"
    CEM_C2_CELL = "BTO_0005931"

    # SUM cell
    BTO_0005932 = "BTO_0005932"
    SUM_CELL = "BTO_0005932"

    # SUM-1315MO2 cell
    BTO_0005933 = "BTO_0005933"
    SUM_1315MO2_CELL = "BTO_0005933"

    # axial nerve cord
    BTO_0005934 = "BTO_0005934"
    AXIAL_NERVE_CORD = "BTO_0005934"

    # culture condition:crotonate-grown cell
    BTO_0005935 = "BTO_0005935"
    CULTURE_CONDITION_CROTONATE_GROWN_CELL = "BTO_0005935"

    # CWR22-R1 cell
    BTO_0005936 = "BTO_0005936"
    CWR22_R1_CELL = "BTO_0005936"

    # intestinal epithelial cell
    BTO_0005937 = "BTO_0005937"
    INTESTINAL_EPITHELIAL_CELL = "BTO_0005937"

    # pharyngeal tooth
    BTO_0005938 = "BTO_0005938"
    PHARYNGEAL_TOOTH = "BTO_0005938"

    # gynoecial nectary
    BTO_0005939 = "BTO_0005939"
    GYNOECIAL_NECTARY = "BTO_0005939"

    # sepal nectary
    BTO_0005940 = "BTO_0005940"
    SEPAL_NECTARY = "BTO_0005940"

    # staminal nectary
    BTO_0005941 = "BTO_0005941"
    STAMINAL_NECTARY = "BTO_0005941"

    # petal nectary
    BTO_0005942 = "BTO_0005942"
    PETAL_NECTARY = "BTO_0005942"

    # mesenteric adipose tissue
    BTO_0005943 = "BTO_0005943"
    MESENTERIC_ADIPOSE_TISSUE = "BTO_0005943"

    # epididymal white adipose tissue
    BTO_0005944 = "BTO_0005944"
    EPIDIDYMAL_WHITE_ADIPOSE_TISSUE = "BTO_0005944"

    # perirenal adipose tissue
    BTO_0005945 = "BTO_0005945"
    PERIRENAL_ADIPOSE_TISSUE = "BTO_0005945"

    # sublingual squamous cell carcinoma cell
    BTO_0005946 = "BTO_0005946"
    SUBLINGUAL_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0005946"

    # sublingual squamous cell carcinoma cell line
    BTO_0005947 = "BTO_0005947"
    SUBLINGUAL_SQUAMOUS_CELL_CARCINOMA_CELL_LINE = "BTO_0005947"

    # HO-1-u-1 cell
    BTO_0005948 = "BTO_0005948"
    HO_1_U_1_CELL = "BTO_0005948"

    # glioblastoma multiforme cell line
    BTO_0005949 = "BTO_0005949"
    GLIOBLASTOMA_MULTIFORME_CELL_LINE = "BTO_0005949"

    # BT-145 cell
    BTO_0005950 = "BTO_0005950"
    BT_145_CELL = "BTO_0005950"

    # BT-159 cell
    BTO_0005951 = "BTO_0005951"
    BT_159_CELL = "BTO_0005951"

    # BT-245 cell
    BTO_0005952 = "BTO_0005952"
    BT_245_CELL = "BTO_0005952"

    # BT-172 cell
    BTO_0005953 = "BTO_0005953"
    BT_172_CELL = "BTO_0005953"

    # DIPG-6 cell
    BTO_0005954 = "BTO_0005954"
    DIPG_6_CELL = "BTO_0005954"

    # DIPG-4 cell
    BTO_0005955 = "BTO_0005955"
    DIPG_4_CELL = "BTO_0005955"

    # UMNSAH/DF-1 cell
    BTO_0005956 = "BTO_0005956"
    UMNSAH_DF_1_CELL = "BTO_0005956"

    # extrastaminal nectary
    BTO_0005957 = "BTO_0005957"
    EXTRASTAMINAL_NECTARY = "BTO_0005957"

    # ovarian follicular epithelium
    BTO_0005958 = "BTO_0005958"
    OVARIAN_FOLLICULAR_EPITHELIUM = "BTO_0005958"

    # thyroid follicular epithelial cell
    BTO_0005959 = "BTO_0005959"
    THYROID_FOLLICULAR_EPITHELIAL_CELL = "BTO_0005959"

    # ovarian follicular epithelial cell
    BTO_0005960 = "BTO_0005960"
    OVARIAN_FOLLICULAR_EPITHELIAL_CELL = "BTO_0005960"

    # GM03440 cell
    BTO_0005961 = "BTO_0005961"
    GM03440_CELL = "BTO_0005961"

    # GM-95 cell
    BTO_0005962 = "BTO_0005962"
    GM_95_CELL = "BTO_0005962"

    # HCC-70 cell
    BTO_0005963 = "BTO_0005963"
    HCC_70_CELL = "BTO_0005963"

    # HIB-1B cell
    BTO_0005964 = "BTO_0005964"
    HIB_1B_CELL = "BTO_0005964"

    # HL-7702 cell
    BTO_0005965 = "BTO_0005965"
    HL_7702_CELL = "BTO_0005965"

    # NCI-H1688 cell
    BTO_0005966 = "BTO_0005966"
    NCI_H1688_CELL = "BTO_0005966"

    # HuTu-80 cell
    BTO_0005967 = "BTO_0005967"
    HUTU_80_CELL = "BTO_0005967"

    # KOSC-2 cell
    BTO_0005968 = "BTO_0005968"
    KOSC_2_CELL = "BTO_0005968"

    # KOSC-3 cell
    BTO_0005969 = "BTO_0005969"
    KOSC_3_CELL = "BTO_0005969"

    # MCF-7/LCC9 cell
    BTO_0005970 = "BTO_0005970"
    MCF_7_LCC9_CELL = "BTO_0005970"

    # culture condition:McCoys 5A medium-grown cell
    BTO_0005971 = "BTO_0005971"
    CULTURE_CONDITION_MCCOYS_5A_MEDIUM_GROWN_CELL = "BTO_0005971"

    # MI8-5 CHO cell
    BTO_0005972 = "BTO_0005972"
    MI8_5_CHO_CELL = "BTO_0005972"

    # Muellerian body
    BTO_0005973 = "BTO_0005973"
    MUELLERIAN_BODY = "BTO_0005973"

    # NCI-H1048 cell
    BTO_0005974 = "BTO_0005974"
    NCI_H1048_CELL = "BTO_0005974"

    # NCI-H1672 cell
    BTO_0005975 = "BTO_0005975"
    NCI_H1672_CELL = "BTO_0005975"

    # NCI-H1963 cell
    BTO_0005976 = "BTO_0005976"
    NCI_H1963_CELL = "BTO_0005976"

    # NCI-H2029 cell
    BTO_0005977 = "BTO_0005977"
    NCI_H2029_CELL = "BTO_0005977"

    # NCI-H2171 cell
    BTO_0005978 = "BTO_0005978"
    NCI_H2171_CELL = "BTO_0005978"

    # NCI-H740 cell
    BTO_0005979 = "BTO_0005979"
    NCI_H740_CELL = "BTO_0005979"

    # nectary parenchyma
    BTO_0005980 = "BTO_0005980"
    NECTARY_PARENCHYMA = "BTO_0005980"

    # auditory capsule
    BTO_0005981 = "BTO_0005981"
    AUDITORY_CAPSULE = "BTO_0005981"

    # P69 prostate cancer cell
    BTO_0005982 = "BTO_0005982"
    P69_PROSTATE_CANCER_CELL = "BTO_0005982"

    # culture condition:cholesterol-grown cell
    BTO_0005983 = "BTO_0005983"
    CULTURE_CONDITION_CHOLESTEROL_GROWN_CELL = "BTO_0005983"

    # culture condition:carbon monoxide-grown cell
    BTO_0005984 = "BTO_0005984"
    CULTURE_CONDITION_CARBON_MONOXIDE_GROWN_CELL = "BTO_0005984"

    # plant ear
    BTO_0005985 = "BTO_0005985"
    PLANT_EAR = "BTO_0005985"

    # head and neck squamous cell carcinoma cell
    BTO_0005986 = "BTO_0005986"
    HEAD_AND_NECK_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0005986"

    # hepatoma HLE cell
    BTO_0005987 = "BTO_0005987"
    HEPATOMA_HLE_CELL = "BTO_0005987"

    # CHO-Lec4 cell
    BTO_0005988 = "BTO_0005988"
    CHO_LEC4_CELL = "BTO_0005988"

    # CHO-Lec4A cell
    BTO_0005989 = "BTO_0005989"
    CHO_LEC4A_CELL = "BTO_0005989"

    # mesonephric duct
    BTO_0005990 = "BTO_0005990"
    MESONEPHRIC_DUCT = "BTO_0005990"

    # pronephric duct
    BTO_0005991 = "BTO_0005991"
    PRONEPHRIC_DUCT = "BTO_0005991"

    # pseudostem
    BTO_0005992 = "BTO_0005992"
    PSEUDOSTEM = "BTO_0005992"

    # basal swimming muscle
    BTO_0005993 = "BTO_0005993"
    BASAL_SWIMMING_MUSCLE = "BTO_0005993"

    # RWPE-2 cell
    BTO_0005994 = "BTO_0005994"
    RWPE_2_CELL = "BTO_0005994"

    # UM-SCC-11B cell
    BTO_0005995 = "BTO_0005995"
    UM_SCC_11B_CELL = "BTO_0005995"

    # stromal cell line
    BTO_0005996 = "BTO_0005996"
    STROMAL_CELL_LINE = "BTO_0005996"

    # ST-2 cell
    BTO_0005997 = "BTO_0005997"
    ST_2_CELL = "BTO_0005997"

    # walking leg
    BTO_0005998 = "BTO_0005998"
    WALKING_LEG = "BTO_0005998"

    # chelate leg
    BTO_0005999 = "BTO_0005999"
    CHELATE_LEG = "BTO_0005999"

    # WPE-int cell
    BTO_0006000 = "BTO_0006000"
    WPE_INT_CELL = "BTO_0006000"

    # GSC cell line
    BTO_0006001 = "BTO_0006001"
    GSC_CELL_LINE = "BTO_0006001"

    # 0308 cell
    BTO_0006002 = "BTO_0006002"
    _0308_CELL = "BTO_0006002"

    # 0822 cell
    BTO_0006003 = "BTO_0006003"
    _0822_CELL = "BTO_0006003"

    # 1228 cell
    BTO_0006004 = "BTO_0006004"
    _1228_CELL = "BTO_0006004"

    # brachial nerve
    BTO_0006005 = "BTO_0006005"
    BRACHIAL_NERVE = "BTO_0006005"

    # pseudopalisading cell
    BTO_0006006 = "BTO_0006006"
    PSEUDOPALISADING_CELL = "BTO_0006006"

    # LB-24-MEL cell
    BTO_0006007 = "BTO_0006007"
    LB_24_MEL_CELL = "BTO_0006007"

    # choroid plexus epithelium
    BTO_0006008 = "BTO_0006008"
    CHOROID_PLEXUS_EPITHELIUM = "BTO_0006008"

    # SUNE-1 cell
    BTO_0006009 = "BTO_0006009"
    SUNE_1_CELL = "BTO_0006009"

    # 5-8F cell
    BTO_0006010 = "BTO_0006010"
    _5_8F_CELL = "BTO_0006010"

    # 6-10B cell
    BTO_0006011 = "BTO_0006011"
    _6_10B_CELL = "BTO_0006011"

    # 13-9B cell
    BTO_0006012 = "BTO_0006012"
    _13_9B_CELL = "BTO_0006012"

    # anterior horn cell
    BTO_0006013 = "BTO_0006013"
    ANTERIOR_HORN_CELL = "BTO_0006013"

    # axillary bud meristem
    BTO_0006014 = "BTO_0006014"
    AXILLARY_BUD_MERISTEM = "BTO_0006014"

    # BRE-80 cell
    BTO_0006015 = "BTO_0006015"
    BRE_80_CELL = "BTO_0006015"

    # C-4-I cell
    BTO_0006016 = "BTO_0006016"
    C_4_I_CELL = "BTO_0006016"

    # cormel
    BTO_0006017 = "BTO_0006017"
    CORMEL = "BTO_0006017"

    # CT26.WT cell
    BTO_0006018 = "BTO_0006018"
    CT26_WT_CELL = "BTO_0006018"

    # CT26.CL25 cell
    BTO_0006019 = "BTO_0006019"
    CT26_CL25_CELL = "BTO_0006019"

    # female accessory gland
    BTO_0006020 = "BTO_0006020"
    FEMALE_ACCESSORY_GLAND = "BTO_0006020"

    # NCI-H2110 cell
    BTO_0006021 = "BTO_0006021"
    NCI_H2110_CELL = "BTO_0006021"

    # NCI-H2172 cell
    BTO_0006022 = "BTO_0006022"
    NCI_H2172_CELL = "BTO_0006022"

    # NCI-H2228 cell
    BTO_0006023 = "BTO_0006023"
    NCI_H2228_CELL = "BTO_0006023"

    # NCI-H820 cell
    BTO_0006024 = "BTO_0006024"
    NCI_H820_CELL = "BTO_0006024"

    # HCC-2279 cell
    BTO_0006025 = "BTO_0006025"
    HCC_2279_CELL = "BTO_0006025"

    # HCC-94 cell
    BTO_0006026 = "BTO_0006026"
    HCC_94_CELL = "BTO_0006026"

    # HCC-95 cell
    BTO_0006027 = "BTO_0006027"
    HCC_95_CELL = "BTO_0006027"

    # HCC-1171 cell
    BTO_0006028 = "BTO_0006028"
    HCC_1171_CELL = "BTO_0006028"

    # Hep-G2/ADM cell
    BTO_0006029 = "BTO_0006029"
    HEP_G2_ADM_CELL = "BTO_0006029"

    # HOC-313 cell
    BTO_0006030 = "BTO_0006030"
    HOC_313_CELL = "BTO_0006030"

    # HUASMC cell
    BTO_0006031 = "BTO_0006031"
    HUASMC_CELL = "BTO_0006031"

    # JVM-3 cell
    BTO_0006032 = "BTO_0006032"
    JVM_3_CELL = "BTO_0006032"

    # Kenyon cell
    BTO_0006033 = "BTO_0006033"
    KENYON_CELL = "BTO_0006033"

    # KRIB cell
    BTO_0006034 = "BTO_0006034"
    KRIB_CELL = "BTO_0006034"

    # foramen magnum
    BTO_0006035 = "BTO_0006035"
    FORAMEN_MAGNUM = "BTO_0006035"

    # subcutaneous tissue cell line
    BTO_0006036 = "BTO_0006036"
    SUBCUTANEOUS_TISSUE_CELL_LINE = "BTO_0006036"

    # L-Wnt-3A cell
    BTO_0006037 = "BTO_0006037"
    L_WNT_3A_CELL = "BTO_0006037"

    # LK-87 cell
    BTO_0006038 = "BTO_0006038"
    LK_87_CELL = "BTO_0006038"

    # MDA-MB-415 cell
    BTO_0006039 = "BTO_0006039"
    MDA_MB_415_CELL = "BTO_0006039"

    # mesophyll cell
    BTO_0006040 = "BTO_0006040"
    MESOPHYLL_CELL = "BTO_0006040"

    # MMT-060562 cell
    BTO_0006041 = "BTO_0006041"
    MMT_060562_CELL = "BTO_0006041"

    # NCI-H1581 cell
    BTO_0006042 = "BTO_0006042"
    NCI_H1581_CELL = "BTO_0006042"

    # NB4-LR1 cell
    BTO_0006043 = "BTO_0006043"
    NB4_LR1_CELL = "BTO_0006043"

    # NB4-LR2 cell
    BTO_0006044 = "BTO_0006044"
    NB4_LR2_CELL = "BTO_0006044"

    # nasopharyngeal cell line
    BTO_0006045 = "BTO_0006045"
    NASOPHARYNGEAL_CELL_LINE = "BTO_0006045"

    # NP-69 cell
    BTO_0006046 = "BTO_0006046"
    NP_69_CELL = "BTO_0006046"

    # PH5CH cell
    BTO_0006047 = "BTO_0006047"
    PH5CH_CELL = "BTO_0006047"

    # PH5CH-8 cell
    BTO_0006048 = "BTO_0006048"
    PH5CH_8_CELL = "BTO_0006048"

    # PH5CH-1 cell
    BTO_0006049 = "BTO_0006049"
    PH5CH_1_CELL = "BTO_0006049"

    # PH5CH-7 cell
    BTO_0006050 = "BTO_0006050"
    PH5CH_7_CELL = "BTO_0006050"

    # pharyngeal arch cartilage
    BTO_0006051 = "BTO_0006051"
    PHARYNGEAL_ARCH_CARTILAGE = "BTO_0006051"

    # SJNB-10 cell
    BTO_0006052 = "BTO_0006052"
    SJNB_10_CELL = "BTO_0006052"

    # SJNB-1 cell
    BTO_0006053 = "BTO_0006053"
    SJNB_1_CELL = "BTO_0006053"

    # SJNB-6 cell
    BTO_0006054 = "BTO_0006054"
    SJNB_6_CELL = "BTO_0006054"

    # SJNB-8 cell
    BTO_0006055 = "BTO_0006055"
    SJNB_8_CELL = "BTO_0006055"

    # SJNB-12 cell
    BTO_0006056 = "BTO_0006056"
    SJNB_12_CELL = "BTO_0006056"

    # SKW-3 cell
    BTO_0006057 = "BTO_0006057"
    SKW_3_CELL = "BTO_0006057"

    # Tca-8113 cell
    BTO_0006058 = "BTO_0006058"
    TCA_8113_CELL = "BTO_0006058"

    # TE-03 cell
    BTO_0006059 = "BTO_0006059"
    TE_03_CELL = "BTO_0006059"

    # WA-01 cell
    BTO_0006060 = "BTO_0006060"
    WA_01_CELL = "BTO_0006060"

    # WA-07 cell
    BTO_0006061 = "BTO_0006061"
    WA_07_CELL = "BTO_0006061"

    # WA-09 cell
    BTO_0006062 = "BTO_0006062"
    WA_09_CELL = "BTO_0006062"

    # YAC-1 cell
    BTO_0006063 = "BTO_0006063"
    YAC_1_CELL = "BTO_0006063"

    # X-organ-sinus-gland complex
    BTO_0006064 = "BTO_0006064"
    X_ORGAN_SINUS_GLAND_COMPLEX = "BTO_0006064"

    # BT-474-LR cell
    BTO_0006065 = "BTO_0006065"
    BT_474_LR_CELL = "BTO_0006065"

    # rHypoE-22 cell
    BTO_0006066 = "BTO_0006066"
    RHYPOE_22_CELL = "BTO_0006066"

    # culture condition:2-methylpropene-grown cell
    BTO_0006067 = "BTO_0006067"
    CULTURE_CONDITION_2_METHYLPROPENE_GROWN_CELL = "BTO_0006067"

    # culture condition:lactate-grown cell
    BTO_0006068 = "BTO_0006068"
    CULTURE_CONDITION_LACTATE_GROWN_CELL = "BTO_0006068"

    # OR-6 cell
    BTO_0006069 = "BTO_0006069"
    OR_6_CELL = "BTO_0006069"

    # Li-23 cell
    BTO_0006070 = "BTO_0006070"
    LI_23_CELL = "BTO_0006070"

    # ORL-8 cell
    BTO_0006071 = "BTO_0006071"
    ORL_8_CELL = "BTO_0006071"

    # tongue epithelial cell line
    BTO_0006072 = "BTO_0006072"
    TONGUE_EPITHELIAL_CELL_LINE = "BTO_0006072"

    # tongue epithelial cell
    BTO_0006073 = "BTO_0006073"
    TONGUE_EPITHELIAL_CELL = "BTO_0006073"

    # CNE-1 cell
    BTO_0006074 = "BTO_0006074"
    CNE_1_CELL = "BTO_0006074"

    # mHypoE-N43/5 cell
    BTO_0006075 = "BTO_0006075"
    MHYPOE_N43_5_CELL = "BTO_0006075"

    # benign prostatic hyperplasia cell
    BTO_0006076 = "BTO_0006076"
    BENIGN_PROSTATIC_HYPERPLASIA_CELL = "BTO_0006076"

    # SAEC cell
    BTO_0006077 = "BTO_0006077"
    SAEC_CELL = "BTO_0006077"

    # pluripotent stem cell
    BTO_0006078 = "BTO_0006078"
    PLURIPOTENT_STEM_CELL = "BTO_0006078"

    # hPSC cell
    BTO_0006079 = "BTO_0006079"
    HPSC_CELL = "BTO_0006079"

    # hESC cell
    BTO_0006080 = "BTO_0006080"
    HESC_CELL = "BTO_0006080"

    # hiPSC cell
    BTO_0006081 = "BTO_0006081"
    HIPSC_CELL = "BTO_0006081"

    # TSCCA cell
    BTO_0006082 = "BTO_0006082"
    TSCCA_CELL = "BTO_0006082"

    # U-87MG/DDP cell
    BTO_0006083 = "BTO_0006083"
    U_87MG_DDP_CELL = "BTO_0006083"

    # uninucleate trophoblast cell
    BTO_0006084 = "BTO_0006084"
    UNINUCLEATE_TROPHOBLAST_CELL = "BTO_0006084"

    # 212LN cell
    BTO_0006085 = "BTO_0006085"
    _212LN_CELL = "BTO_0006085"

    # HS-SY-2 cell
    BTO_0006086 = "BTO_0006086"
    HS_SY_2_CELL = "BTO_0006086"

    # caudolateral nidopallium
    BTO_0006087 = "BTO_0006087"
    CAUDOLATERAL_NIDOPALLIUM = "BTO_0006087"

    # KEL-FIB cell
    BTO_0006088 = "BTO_0006088"
    KEL_FIB_CELL = "BTO_0006088"

    # CCD-1113Sk cell
    BTO_0006089 = "BTO_0006089"
    CCD_1113SK_CELL = "BTO_0006089"

    # HCC-1569 cell
    BTO_0006090 = "BTO_0006090"
    HCC_1569_CELL = "BTO_0006090"

    # HeLa-HL3T1 cell
    BTO_0006091 = "BTO_0006091"
    HELA_HL3T1_CELL = "BTO_0006091"

    # hTERT-HPNE cell
    BTO_0006092 = "BTO_0006092"
    HTERT_HPNE_CELL = "BTO_0006092"

    # male inflorescence
    BTO_0006093 = "BTO_0006093"
    MALE_INFLORESCENCE = "BTO_0006093"

    # female inflorescence
    BTO_0006094 = "BTO_0006094"
    FEMALE_INFLORESCENCE = "BTO_0006094"

    # LNCaP clone FGC
    BTO_0006095 = "BTO_0006095"
    LNCAP_CLONE_FGC = "BTO_0006095"

    # culture condition:benzene-grown cell
    BTO_0006096 = "BTO_0006096"
    CULTURE_CONDITION_BENZENE_GROWN_CELL = "BTO_0006096"

    # HEKa cell
    BTO_0006097 = "BTO_0006097"
    HEKA_CELL = "BTO_0006097"

    # root apical meristem
    BTO_0006098 = "BTO_0006098"
    ROOT_APICAL_MERISTEM = "BTO_0006098"

    # S2-028 cell
    BTO_0006099 = "BTO_0006099"
    S2_028_CELL = "BTO_0006099"

    # plant protocorm
    BTO_0006100 = "BTO_0006100"
    PLANT_PROTOCORM = "BTO_0006100"

    # insect protocorm
    BTO_0006101 = "BTO_0006101"
    INSECT_PROTOCORM = "BTO_0006101"

    # activated skeletal muscle satellite cell
    BTO_0006102 = "BTO_0006102"
    ACTIVATED_SKELETAL_MUSCLE_SATELLITE_CELL = "BTO_0006102"

    # quiescent skeletal muscle satellite cell
    BTO_0006103 = "BTO_0006103"
    QUIESCENT_SKELETAL_MUSCLE_SATELLITE_CELL = "BTO_0006103"

    # proliferating skeletal muscle satellite cell
    BTO_0006104 = "BTO_0006104"
    PROLIFERATING_SKELETAL_MUSCLE_SATELLITE_CELL = "BTO_0006104"

    # skeletal muscle satellite stem cell
    BTO_0006105 = "BTO_0006105"
    SKELETAL_MUSCLE_SATELLITE_STEM_CELL = "BTO_0006105"

    # adrenal adenoma cell
    BTO_0006106 = "BTO_0006106"
    ADRENAL_ADENOMA_CELL = "BTO_0006106"

    # endometrial luminal epithelium
    BTO_0006107 = "BTO_0006107"
    ENDOMETRIAL_LUMINAL_EPITHELIUM = "BTO_0006107"

    # endometrial glandular epithelium
    BTO_0006108 = "BTO_0006108"
    ENDOMETRIAL_GLANDULAR_EPITHELIUM = "BTO_0006108"

    # uterine endometrial epithelium
    BTO_0006109 = "BTO_0006109"
    UTERINE_ENDOMETRIAL_EPITHELIUM = "BTO_0006109"

    # M1 macrophage
    BTO_0006110 = "BTO_0006110"
    M1_MACROPHAGE = "BTO_0006110"

    # M2 macrophage
    BTO_0006111 = "BTO_0006111"
    M2_MACROPHAGE = "BTO_0006111"

    # fibro-adipogenic progenitor cell
    BTO_0006112 = "BTO_0006112"
    FIBRO_ADIPOGENIC_PROGENITOR_CELL = "BTO_0006112"

    # megaspore
    BTO_0006113 = "BTO_0006113"
    MEGASPORE = "BTO_0006113"

    # MEL-C19 cell
    BTO_0006114 = "BTO_0006114"
    MEL_C19_CELL = "BTO_0006114"

    # mesenterial filament
    BTO_0006115 = "BTO_0006115"
    MESENTERIAL_FILAMENT = "BTO_0006115"

    # microsclerotium
    BTO_0006116 = "BTO_0006116"
    MICROSCLEROTIUM = "BTO_0006116"

    # middle silk gland
    BTO_0006117 = "BTO_0006117"
    MIDDLE_SILK_GLAND = "BTO_0006117"

    # MYCN2 cell
    BTO_0006118 = "BTO_0006118"
    MYCN2_CELL = "BTO_0006118"

    # villous cytotrophoblast
    BTO_0006119 = "BTO_0006119"
    VILLOUS_CYTOTROPHOBLAST = "BTO_0006119"

    # villous syncytiotrophoblast
    BTO_0006120 = "BTO_0006120"
    VILLOUS_SYNCYTIOTROPHOBLAST = "BTO_0006120"

    # synergid cell
    BTO_0006121 = "BTO_0006121"
    SYNERGID_CELL = "BTO_0006121"

    # TU-KATO-III cell
    BTO_0006122 = "BTO_0006122"
    TU_KATO_III_CELL = "BTO_0006122"

    # T-98 cell
    BTO_0006123 = "BTO_0006123"
    T_98_CELL = "BTO_0006123"

    # C3ABR cell
    BTO_0006124 = "BTO_0006124"
    C3ABR_CELL = "BTO_0006124"

    # AT1ABR cell
    BTO_0006125 = "BTO_0006125"
    AT1ABR_CELL = "BTO_0006125"

    # AT25ABR cell
    BTO_0006126 = "BTO_0006126"
    AT25ABR_CELL = "BTO_0006126"

    # adventitious root primordium
    BTO_0006127 = "BTO_0006127"
    ADVENTITIOUS_ROOT_PRIMORDIUM = "BTO_0006127"

    # spinothalamic tract
    BTO_0006128 = "BTO_0006128"
    SPINOTHALAMIC_TRACT = "BTO_0006128"

    # lateral spinothalamic tract
    BTO_0006129 = "BTO_0006129"
    LATERAL_SPINOTHALAMIC_TRACT = "BTO_0006129"

    # anterior spinothalamic tract
    BTO_0006130 = "BTO_0006130"
    ANTERIOR_SPINOTHALAMIC_TRACT = "BTO_0006130"

    # culture condition:B220+ cell
    BTO_0006131 = "BTO_0006131"
    CULTURE_CONDITION_B220__CELL = "BTO_0006131"

    # corticospinal tract
    BTO_0006132 = "BTO_0006132"
    CORTICOSPINAL_TRACT = "BTO_0006132"

    # forespore
    BTO_0006133 = "BTO_0006133"
    FORESPORE = "BTO_0006133"

    # culture condition:GR1+ cell
    BTO_0006134 = "BTO_0006134"
    CULTURE_CONDITION_GR1__CELL = "BTO_0006134"

    # HNE-1 cell
    BTO_0006135 = "BTO_0006135"
    HNE_1_CELL = "BTO_0006135"

    # HONE-1 cell
    BTO_0006136 = "BTO_0006136"
    HONE_1_CELL = "BTO_0006136"

    # Hs-27 cell
    BTO_0006137 = "BTO_0006137"
    HS_27_CELL = "BTO_0006137"

    # internal capsule
    BTO_0006138 = "BTO_0006138"
    INTERNAL_CAPSULE = "BTO_0006138"

    # NPC-TW03 cell
    BTO_0006139 = "BTO_0006139"
    NPC_TW03_CELL = "BTO_0006139"

    # SN4741 cell
    BTO_0006140 = "BTO_0006140"
    SN4741_CELL = "BTO_0006140"

    # Lu-99 cell
    BTO_0006141 = "BTO_0006141"
    LU_99_CELL = "BTO_0006141"

    # M4A4 LM3-4 CL16 GFP cell
    BTO_0006142 = "BTO_0006142"
    M4A4_LM3_4_CL16_GFP_CELL = "BTO_0006142"

    # MHCC-LM3 cell
    BTO_0006143 = "BTO_0006143"
    MHCC_LM3_CELL = "BTO_0006143"

    # NM2C5 cell
    BTO_0006144 = "BTO_0006144"
    NM2C5_CELL = "BTO_0006144"

    # NM2C5-GFP cell
    BTO_0006145 = "BTO_0006145"
    NM2C5_GFP_CELL = "BTO_0006145"

    # culture condition:corn steep liquor-grown cell
    BTO_0006146 = "BTO_0006146"
    CULTURE_CONDITION_CORN_STEEP_LIQUOR_GROWN_CELL = "BTO_0006146"

    # IHH cell
    BTO_0006147 = "BTO_0006147"
    IHH_CELL = "BTO_0006147"

    # mesenchymal glioma stem cell
    BTO_0006148 = "BTO_0006148"
    MESENCHYMAL_GLIOMA_STEM_CELL = "BTO_0006148"

    # Flp-In-T-REx cell
    BTO_0006149 = "BTO_0006149"
    FLP_IN_T_REX_CELL = "BTO_0006149"

    # plasmablastic lymphoma cell
    BTO_0006150 = "BTO_0006150"
    PLASMABLASTIC_LYMPHOMA_CELL = "BTO_0006150"

    # coral nubbin
    BTO_0006151 = "BTO_0006151"
    CORAL_NUBBIN = "BTO_0006151"

    # microtome section
    BTO_0006152 = "BTO_0006152"
    MICROTOME_SECTION = "BTO_0006152"

    # nigrostriatal system
    BTO_0006153 = "BTO_0006153"
    NIGROSTRIATAL_SYSTEM = "BTO_0006153"

    # renal proximal tubule epithelial cell
    BTO_0006154 = "BTO_0006154"
    RENAL_PROXIMAL_TUBULE_EPITHELIAL_CELL = "BTO_0006154"

    # glioma stem cell
    BTO_0006155 = "BTO_0006155"
    GLIOMA_STEM_CELL = "BTO_0006155"

    # proneural glioma stem cell
    BTO_0006156 = "BTO_0006156"
    PRONEURAL_GLIOMA_STEM_CELL = "BTO_0006156"

    # olivocerebellar fiber system
    BTO_0006157 = "BTO_0006157"
    OLIVOCEREBELLAR_FIBER_SYSTEM = "BTO_0006157"

    # root vascular cylinder
    BTO_0006158 = "BTO_0006158"
    ROOT_VASCULAR_CYLINDER = "BTO_0006158"

    # rubrospinal tract
    BTO_0006159 = "BTO_0006159"
    RUBROSPINAL_TRACT = "BTO_0006159"

    # olivopontocerebellar fiber
    BTO_0006160 = "BTO_0006160"
    OLIVOPONTOCEREBELLAR_FIBER = "BTO_0006160"

    # pontocerebellar fiber
    BTO_0006161 = "BTO_0006161"
    PONTOCEREBELLAR_FIBER = "BTO_0006161"

    # reproductive gland
    BTO_0006162 = "BTO_0006162"
    REPRODUCTIVE_GLAND = "BTO_0006162"

    # C-2 cell
    BTO_0006163 = "BTO_0006163"
    C_2_CELL = "BTO_0006163"

    # cancer-infiltrating inflammatory cell
    BTO_0006164 = "BTO_0006164"
    CANCER_INFILTRATING_INFLAMMATORY_CELL = "BTO_0006164"

    # endometrial luminal epithelial cell
    BTO_0006165 = "BTO_0006165"
    ENDOMETRIAL_LUMINAL_EPITHELIAL_CELL = "BTO_0006165"

    # nucleus preopticus lateralis
    BTO_0006166 = "BTO_0006166"
    NUCLEUS_PREOPTICUS_LATERALIS = "BTO_0006166"

    # nucleus preopticus medialis
    BTO_0006167 = "BTO_0006167"
    NUCLEUS_PREOPTICUS_MEDIALIS = "BTO_0006167"

    # nucleus preopticus medianus
    BTO_0006168 = "BTO_0006168"
    NUCLEUS_PREOPTICUS_MEDIANUS = "BTO_0006168"

    # nucleus preopticus periventricularis
    BTO_0006169 = "BTO_0006169"
    NUCLEUS_PREOPTICUS_PERIVENTRICULARIS = "BTO_0006169"

    # nonpigmented ciliary epithelial cell
    BTO_0006170 = "BTO_0006170"
    NONPIGMENTED_CILIARY_EPITHELIAL_CELL = "BTO_0006170"

    # syncytial embryo sac
    BTO_0006171 = "BTO_0006171"
    SYNCYTIAL_EMBRYO_SAC = "BTO_0006171"

    # testicular somatic cell
    BTO_0006172 = "BTO_0006172"
    TESTICULAR_SOMATIC_CELL = "BTO_0006172"

    # trichilium
    BTO_0006173 = "BTO_0006173"
    TRICHILIUM = "BTO_0006173"

    # smooth adductor muscle
    BTO_0006174 = "BTO_0006174"
    SMOOTH_ADDUCTOR_MUSCLE = "BTO_0006174"

    # inferior temporal gyrus
    BTO_0006175 = "BTO_0006175"
    INFERIOR_TEMPORAL_GYRUS = "BTO_0006175"

    # middle temporal gyrus
    BTO_0006176 = "BTO_0006176"
    MIDDLE_TEMPORAL_GYRUS = "BTO_0006176"

    # superior temporal gyrus
    BTO_0006177 = "BTO_0006177"
    SUPERIOR_TEMPORAL_GYRUS = "BTO_0006177"

    # temporal gyrus
    BTO_0006178 = "BTO_0006178"
    TEMPORAL_GYRUS = "BTO_0006178"

    # cardiac tube
    BTO_0006179 = "BTO_0006179"
    CARDIAC_TUBE = "BTO_0006179"

    # endocardial heart tube
    BTO_0006180 = "BTO_0006180"
    ENDOCARDIAL_HEART_TUBE = "BTO_0006180"

    # buffy coat
    BTO_0006181 = "BTO_0006181"
    BUFFY_COAT = "BTO_0006181"

    # venous blood cell
    BTO_0006182 = "BTO_0006182"
    VENOUS_BLOOD_CELL = "BTO_0006182"

    # arterial blood cell
    BTO_0006183 = "BTO_0006183"
    ARTERIAL_BLOOD_CELL = "BTO_0006183"

    # mouth floor
    BTO_0006184 = "BTO_0006184"
    MOUTH_FLOOR = "BTO_0006184"

    # buffy coat cell
    BTO_0006185 = "BTO_0006185"
    BUFFY_COAT_CELL = "BTO_0006185"

    # air pouch cell
    BTO_0006186 = "BTO_0006186"
    AIR_POUCH_CELL = "BTO_0006186"

    # venous blood
    BTO_0006187 = "BTO_0006187"
    VENOUS_BLOOD = "BTO_0006187"

    # arterial blood
    BTO_0006188 = "BTO_0006188"
    ARTERIAL_BLOOD = "BTO_0006188"

    # protoperithecium
    BTO_0006189 = "BTO_0006189"
    PROTOPERITHECIUM = "BTO_0006189"

    # cybrid cell
    BTO_0006190 = "BTO_0006190"
    CYBRID_CELL = "BTO_0006190"

    # cumulus-oocyte complex
    BTO_0006191 = "BTO_0006191"
    CUMULUS_OOCYTE_COMPLEX = "BTO_0006191"

    # glomus cell
    BTO_0006192 = "BTO_0006192"
    GLOMUS_CELL = "BTO_0006192"

    # aortic body
    BTO_0006193 = "BTO_0006193"
    AORTIC_BODY = "BTO_0006193"

    # aortic arch
    BTO_0006194 = "BTO_0006194"
    AORTIC_ARCH = "BTO_0006194"

    # EC-18 cell
    BTO_0006195 = "BTO_0006195"
    EC_18_CELL = "BTO_0006195"

    # vertebra
    BTO_0006196 = "BTO_0006196"
    VERTEBRA = "BTO_0006196"

    # KYSE-140 cell
    BTO_0006197 = "BTO_0006197"
    KYSE_140_CELL = "BTO_0006197"

    # esophageal epithelial cell line
    BTO_0006198 = "BTO_0006198"
    ESOPHAGEAL_EPITHELIAL_CELL_LINE = "BTO_0006198"

    # esophageal epithelial cell
    BTO_0006199 = "BTO_0006199"
    ESOPHAGEAL_EPITHELIAL_CELL = "BTO_0006199"

    # 250MK cell
    BTO_0006200 = "BTO_0006200"
    _250MK_CELL = "BTO_0006200"

    # 3D4/21 cell
    BTO_0006201 = "BTO_0006201"
    _3D4_21_CELL = "BTO_0006201"

    # 76NF2V cell
    BTO_0006202 = "BTO_0006202"
    _76NF2V_CELL = "BTO_0006202"

    # AML-193 cell
    BTO_0006203 = "BTO_0006203"
    AML_193_CELL = "BTO_0006203"

    # Caki-2 cell
    BTO_0006204 = "BTO_0006204"
    CAKI_2_CELL = "BTO_0006204"

    # serotonergic neuron
    BTO_0006205 = "BTO_0006205"
    SEROTONERGIC_NEURON = "BTO_0006205"

    # extravillous cytotrophoblast
    BTO_0006206 = "BTO_0006206"
    EXTRAVILLOUS_CYTOTROPHOBLAST = "BTO_0006206"

    # extravillous cytotrophoblast cell
    BTO_0006207 = "BTO_0006207"
    EXTRAVILLOUS_CYTOTROPHOBLAST_CELL = "BTO_0006207"

    # extravillous trophoblast cell
    BTO_0006208 = "BTO_0006208"
    EXTRAVILLOUS_TROPHOBLAST_CELL = "BTO_0006208"

    # HIPEC-65 cell
    BTO_0006209 = "BTO_0006209"
    HIPEC_65_CELL = "BTO_0006209"

    # HMT-3522 T4-2 cell
    BTO_0006210 = "BTO_0006210"
    HMT_3522_T4_2_CELL = "BTO_0006210"

    # HTC-C3 cell
    BTO_0006211 = "BTO_0006211"
    HTC_C3_CELL = "BTO_0006211"

    # HTR-8 cell
    BTO_0006212 = "BTO_0006212"
    HTR_8_CELL = "BTO_0006212"

    # KELLY cell
    BTO_0006213 = "BTO_0006213"
    KELLY_CELL = "BTO_0006213"

    # KIJ-265T cell
    BTO_0006214 = "BTO_0006214"
    KIJ_265T_CELL = "BTO_0006214"

    # KIJ-308T cell
    BTO_0006215 = "BTO_0006215"
    KIJ_308T_CELL = "BTO_0006215"

    # leaf epidermal cell
    BTO_0006216 = "BTO_0006216"
    LEAF_EPIDERMAL_CELL = "BTO_0006216"

    # chondrogenic MCT cell
    BTO_0006217 = "BTO_0006217"
    CHONDROGENIC_MCT_CELL = "BTO_0006217"

    # MDA-MB-157 cell
    BTO_0006218 = "BTO_0006218"
    MDA_MB_157_CELL = "BTO_0006218"

    # neuromast
    BTO_0006219 = "BTO_0006219"
    NEUROMAST = "BTO_0006219"

    # UACC-812 cell
    BTO_0006220 = "BTO_0006220"
    UACC_812_CELL = "BTO_0006220"

    # U-343MG cell
    BTO_0006221 = "BTO_0006221"
    U_343MG_CELL = "BTO_0006221"

    # olfactory placode
    BTO_0006222 = "BTO_0006222"
    OLFACTORY_PLACODE = "BTO_0006222"

    # neural ectoderm
    BTO_0006223 = "BTO_0006223"
    NEURAL_ECTODERM = "BTO_0006223"

    # OP-6 cell
    BTO_0006224 = "BTO_0006224"
    OP_6_CELL = "BTO_0006224"

    # olfactory placode cell line
    BTO_0006225 = "BTO_0006225"
    OLFACTORY_PLACODE_CELL_LINE = "BTO_0006225"

    # OP-27 cell
    BTO_0006226 = "BTO_0006226"
    OP_27_CELL = "BTO_0006226"

    # RERF-LC-AI cell
    BTO_0006227 = "BTO_0006227"
    RERF_LC_AI_CELL = "BTO_0006227"

    # MDS-92 cell
    BTO_0006228 = "BTO_0006228"
    MDS_92_CELL = "BTO_0006228"

    # MDS-L cell
    BTO_0006229 = "BTO_0006229"
    MDS_L_CELL = "BTO_0006229"

    # culture condition:camphor-grown cell
    BTO_0006230 = "BTO_0006230"
    CULTURE_CONDITION_CAMPHOR_GROWN_CELL = "BTO_0006230"

    # culture condition:(rac)-camphor-grown cell
    BTO_0006232 = "BTO_0006232"
    CULTURE_CONDITION__RAC__CAMPHOR_GROWN_CELL = "BTO_0006232"

    # culture condition:dimethylsulphoniopropionate-grown cell
    BTO_0006233 = "BTO_0006233"
    CULTURE_CONDITION_DIMETHYLSULPHONIOPROPIONATE_GROWN_CELL = "BTO_0006233"

    # culture condition:nicotine-grown cell
    BTO_0006234 = "BTO_0006234"
    CULTURE_CONDITION_NICOTINE_GROWN_CELL = "BTO_0006234"

    # culture condition:rice bran-grown cell
    BTO_0006235 = "BTO_0006235"
    CULTURE_CONDITION_RICE_BRAN_GROWN_CELL = "BTO_0006235"

    # culture condition:rice hull-grown cell
    BTO_0006236 = "BTO_0006236"
    CULTURE_CONDITION_RICE_HULL_GROWN_CELL = "BTO_0006236"

    # culture condition:sugarcane bagasse-grown cell
    BTO_0006237 = "BTO_0006237"
    CULTURE_CONDITION_SUGARCANE_BAGASSE_GROWN_CELL = "BTO_0006237"

    # interfascicular cambium
    BTO_0006238 = "BTO_0006238"
    INTERFASCICULAR_CAMBIUM = "BTO_0006238"

    # interfascicular region
    BTO_0006239 = "BTO_0006239"
    INTERFASCICULAR_REGION = "BTO_0006239"

    # PK-15CD163 cell
    BTO_0006240 = "BTO_0006240"
    PK_15CD163_CELL = "BTO_0006240"

    # endomysium
    BTO_0006241 = "BTO_0006241"
    ENDOMYSIUM = "BTO_0006241"

    # external ectoderm
    BTO_0006242 = "BTO_0006242"
    EXTERNAL_ECTODERM = "BTO_0006242"

    # bacteriocyte
    BTO_0006243 = "BTO_0006243"
    BACTERIOCYTE = "BTO_0006243"

    # blood-brain barrier
    BTO_0006244 = "BTO_0006244"
    BLOOD_BRAIN_BARRIER = "BTO_0006244"

    # brain capillary endothelium
    BTO_0006245 = "BTO_0006245"
    BRAIN_CAPILLARY_ENDOTHELIUM = "BTO_0006245"

    # brain capillary endothelial cell
    BTO_0006246 = "BTO_0006246"
    BRAIN_CAPILLARY_ENDOTHELIAL_CELL = "BTO_0006246"

    # culture condition:CD11c+ cell
    BTO_0006247 = "BTO_0006247"
    CULTURE_CONDITION_CD11C__CELL = "BTO_0006247"

    # dermatome
    BTO_0006248 = "BTO_0006248"
    DERMATOME = "BTO_0006248"

    # dorsal endoderm
    BTO_0006249 = "BTO_0006249"
    DORSAL_ENDODERM = "BTO_0006249"

    # epibranchial ganglion
    BTO_0006250 = "BTO_0006250"
    EPIBRANCHIAL_GANGLION = "BTO_0006250"

    # renal proximal tubule cell
    BTO_0006251 = "BTO_0006251"
    RENAL_PROXIMAL_TUBULE_CELL = "BTO_0006251"

    # prostate epithelium cell
    BTO_0006252 = "BTO_0006252"
    PROSTATE_EPITHELIUM_CELL = "BTO_0006252"

    # UWB1.289 cell
    BTO_0006253 = "BTO_0006253"
    UWB1_289_CELL = "BTO_0006253"

    # UWB1.289+BRCA1 cell
    BTO_0006254 = "BTO_0006254"
    UWB1_289_BRCA1_CELL = "BTO_0006254"

    # sclerotome
    BTO_0006255 = "BTO_0006255"
    SCLEROTOME = "BTO_0006255"

    # solid cancer cell
    BTO_0006256 = "BTO_0006256"
    SOLID_CANCER_CELL = "BTO_0006256"

    # oral sucker
    BTO_0006257 = "BTO_0006257"
    ORAL_SUCKER = "BTO_0006257"

    # ventral sucker
    BTO_0006258 = "BTO_0006258"
    VENTRAL_SUCKER = "BTO_0006258"

    # pluteus
    BTO_0006259 = "BTO_0006259"
    PLUTEUS = "BTO_0006259"

    # GM02784 cell
    BTO_0006260 = "BTO_0006260"
    GM02784_CELL = "BTO_0006260"

    # HL-60/S cell
    BTO_0006261 = "BTO_0006261"
    HL_60_S_CELL = "BTO_0006261"

    # thymic cancer cell line
    BTO_0006262 = "BTO_0006262"
    THYMIC_CANCER_CELL_LINE = "BTO_0006262"

    # IT-79MTNC3 cell
    BTO_0006263 = "BTO_0006263"
    IT_79MTNC3_CELL = "BTO_0006263"

    # LNCaP-95 cell
    BTO_0006264 = "BTO_0006264"
    LNCAP_95_CELL = "BTO_0006264"

    # MR49F cell
    BTO_0006265 = "BTO_0006265"
    MR49F_CELL = "BTO_0006265"

    # subfornical organ
    BTO_0006266 = "BTO_0006266"
    SUBFORNICAL_ORGAN = "BTO_0006266"

    # circumventricular organ
    BTO_0006267 = "BTO_0006267"
    CIRCUMVENTRICULAR_ORGAN = "BTO_0006267"

    # organum vasculosum laminae terminalis
    BTO_0006268 = "BTO_0006268"
    ORGANUM_VASCULOSUM_LAMINAE_TERMINALIS = "BTO_0006268"

    # ACI-45 cell
    BTO_0006269 = "BTO_0006269"
    ACI_45_CELL = "BTO_0006269"

    # uterine carcinosarcoma cell line
    BTO_0006270 = "BTO_0006270"
    UTERINE_CARCINOSARCOMA_CELL_LINE = "BTO_0006270"

    # endometrial gland cell line
    BTO_0006271 = "BTO_0006271"
    ENDOMETRIAL_GLAND_CELL_LINE = "BTO_0006271"

    # EM-E6E7TERT-1 cell
    BTO_0006272 = "BTO_0006272"
    EM_E6E7TERT_1_CELL = "BTO_0006272"

    # EM-E6E7TERT-2 cell
    BTO_0006273 = "BTO_0006273"
    EM_E6E7TERT_2_CELL = "BTO_0006273"

    # EM-E6E7TERT-3 cell
    BTO_0006274 = "BTO_0006274"
    EM_E6E7TERT_3_CELL = "BTO_0006274"

    # SW-1573/S1 cell
    BTO_0006275 = "BTO_0006275"
    SW_1573_S1_CELL = "BTO_0006275"

    # GNET cell
    BTO_0006276 = "BTO_0006276"
    GNET_CELL = "BTO_0006276"

    # outer mantle
    BTO_0006277 = "BTO_0006277"
    OUTER_MANTLE = "BTO_0006277"

    # inner mantle
    BTO_0006278 = "BTO_0006278"
    INNER_MANTLE = "BTO_0006278"

    # tubulointerstitium
    BTO_0006279 = "BTO_0006279"
    TUBULOINTERSTITIUM = "BTO_0006279"

    # vas deferens ampulla
    BTO_0006280 = "BTO_0006280"
    VAS_DEFERENS_AMPULLA = "BTO_0006280"

    # YY-8103 cell
    BTO_0006281 = "BTO_0006281"
    YY_8103_CELL = "BTO_0006281"

    # TIG-3 cell
    BTO_0006282 = "BTO_0006282"
    TIG_3_CELL = "BTO_0006282"

    # prechordal mesendoderm
    BTO_0006283 = "BTO_0006283"
    PRECHORDAL_MESENDODERM = "BTO_0006283"

    # root nodule cortex
    BTO_0006284 = "BTO_0006284"
    ROOT_NODULE_CORTEX = "BTO_0006284"

    # SPC-A4 cell
    BTO_0006285 = "BTO_0006285"
    SPC_A4_CELL = "BTO_0006285"

    # disc floret
    BTO_0006286 = "BTO_0006286"
    DISC_FLORET = "BTO_0006286"

    # MGH-U3 cell
    BTO_0006287 = "BTO_0006287"
    MGH_U3_CELL = "BTO_0006287"

    # MGH-U4 cell
    BTO_0006288 = "BTO_0006288"
    MGH_U4_CELL = "BTO_0006288"

    # Vero 2.2 cell
    BTO_0006289 = "BTO_0006289"
    VERO_2_2_CELL = "BTO_0006289"

    # UM-UC-2 cell
    BTO_0006290 = "BTO_0006290"
    UM_UC_2_CELL = "BTO_0006290"

    # Mbeta16tsA cell
    BTO_0006291 = "BTO_0006291"
    MBETA16TSA_CELL = "BTO_0006291"

    # Aag-2 cell
    BTO_0006292 = "BTO_0006292"
    AAG_2_CELL = "BTO_0006292"

    # breast cancer stem cell
    BTO_0006293 = "BTO_0006293"
    BREAST_CANCER_STEM_CELL = "BTO_0006293"

    # BWZ.36 cell
    BTO_0006294 = "BTO_0006294"
    BWZ_36_CELL = "BTO_0006294"

    # BWZ.36 CD8 alpha cell
    BTO_0006295 = "BTO_0006295"
    BWZ_36_CD8_ALPHA_CELL = "BTO_0006295"

    # celiac ganglion
    BTO_0006296 = "BTO_0006296"
    CELIAC_GANGLION = "BTO_0006296"

    # CH12F3 cell
    BTO_0006297 = "BTO_0006297"
    CH12F3_CELL = "BTO_0006297"

    # HepAD38 cell
    BTO_0006298 = "BTO_0006298"
    HEPAD38_CELL = "BTO_0006298"

    # gastric cecum
    BTO_0006299 = "BTO_0006299"
    GASTRIC_CECUM = "BTO_0006299"

    # hemolysate
    BTO_0006300 = "BTO_0006300"
    HEMOLYSATE = "BTO_0006300"

    # HepG2-N10 cell
    BTO_0006301 = "BTO_0006301"
    HEPG2_N10_CELL = "BTO_0006301"

    # mpkCCD cell
    BTO_0006302 = "BTO_0006302"
    MPKCCD_CELL = "BTO_0006302"

    # Mull cell
    BTO_0006303 = "BTO_0006303"
    MULL_CELL = "BTO_0006303"

    # JC cell
    BTO_0006304 = "BTO_0006304"
    JC_CELL = "BTO_0006304"

    # rhizodermis
    BTO_0006305 = "BTO_0006305"
    RHIZODERMIS = "BTO_0006305"

    # stichosome
    BTO_0006306 = "BTO_0006306"
    STICHOSOME = "BTO_0006306"

    # SW-780 cell
    BTO_0006307 = "BTO_0006307"
    SW_780_CELL = "BTO_0006307"

    # TCC-SUP cell
    BTO_0006308 = "BTO_0006308"
    TCC_SUP_CELL = "BTO_0006308"

    # WIF-B9 cell
    BTO_0006309 = "BTO_0006309"
    WIF_B9_CELL = "BTO_0006309"

    # WIF-B9/R cell
    BTO_0006310 = "BTO_0006310"
    WIF_B9_R_CELL = "BTO_0006310"

    # WI38-VA13 cell
    BTO_0006311 = "BTO_0006311"
    WI38_VA13_CELL = "BTO_0006311"

    # plantaris muscle
    BTO_0006312 = "BTO_0006312"
    PLANTARIS_MUSCLE = "BTO_0006312"

    # taproot
    BTO_0006313 = "BTO_0006313"
    TAPROOT = "BTO_0006313"

    # shell capitulum
    BTO_0006314 = "BTO_0006314"
    SHELL_CAPITULUM = "BTO_0006314"

    # shell peduncle
    BTO_0006315 = "BTO_0006315"
    SHELL_PEDUNCLE = "BTO_0006315"

    # compound leaf
    BTO_0006316 = "BTO_0006316"
    COMPOUND_LEAF = "BTO_0006316"

    # plant rachis
    BTO_0006317 = "BTO_0006317"
    PLANT_RACHIS = "BTO_0006317"

    # culture condition:beech wood-grown cell
    BTO_0006318 = "BTO_0006318"
    CULTURE_CONDITION_BEECH_WOOD_GROWN_CELL = "BTO_0006318"

    # culture condition:wheat straw-grown cell
    BTO_0006319 = "BTO_0006319"
    CULTURE_CONDITION_WHEAT_STRAW_GROWN_CELL = "BTO_0006319"

    # HKiG2 cell
    BTO_0006320 = "BTO_0006320"
    HKIG2_CELL = "BTO_0006320"

    # GC-1 spg cell
    BTO_0006321 = "BTO_0006321"
    GC_1_SPG_CELL = "BTO_0006321"

    # Jump-In-T-REx HEK293 cell
    BTO_0006322 = "BTO_0006322"
    JUMP_IN_T_REX_HEK293_CELL = "BTO_0006322"

    # culture condition:itaconate-grown cell
    BTO_0006323 = "BTO_0006323"
    CULTURE_CONDITION_ITACONATE_GROWN_CELL = "BTO_0006323"

    # culture condition:mesaconate-grown cell
    BTO_0006324 = "BTO_0006324"
    CULTURE_CONDITION_MESACONATE_GROWN_CELL = "BTO_0006324"

    # culture condition:chlorobenzene-grown cell
    BTO_0006325 = "BTO_0006325"
    CULTURE_CONDITION_CHLOROBENZENE_GROWN_CELL = "BTO_0006325"

    # A2780/AD cell
    BTO_0006326 = "BTO_0006326"
    A2780_AD_CELL = "BTO_0006326"

    # Phoenix-AMPHO cell
    BTO_0006327 = "BTO_0006327"
    PHOENIX_AMPHO_CELL = "BTO_0006327"

    # HEK-293T/17 cell
    BTO_0006328 = "BTO_0006328"
    HEK_293T_17_CELL = "BTO_0006328"

    # red nucleus
    BTO_0006329 = "BTO_0006329"
    RED_NUCLEUS = "BTO_0006329"

    # proglottid
    BTO_0006330 = "BTO_0006330"
    PROGLOTTID = "BTO_0006330"

    # strobila
    BTO_0006331 = "BTO_0006331"
    STROBILA = "BTO_0006331"

    # SJ-GBM-2 cell
    BTO_0006332 = "BTO_0006332"
    SJ_GBM_2_CELL = "BTO_0006332"

    # BM7 cell
    BTO_0006333 = "BTO_0006333"
    BM7_CELL = "BTO_0006333"

    # uterine endometrial clear cell carcinoma cell line
    BTO_0006334 = "BTO_0006334"
    UTERINE_ENDOMETRIAL_CLEAR_CELL_CARCINOMA_CELL_LINE = "BTO_0006334"

    # TMG-L cell
    BTO_0006335 = "BTO_0006335"
    TMG_L_CELL = "BTO_0006335"

    # TMCC-2 cell
    BTO_0006336 = "BTO_0006336"
    TMCC_2_CELL = "BTO_0006336"

    # uterine endometrial clear cell carcinoma cell
    BTO_0006337 = "BTO_0006337"
    UTERINE_ENDOMETRIAL_CLEAR_CELL_CARCINOMA_CELL = "BTO_0006337"

    # excretory system
    BTO_0006338 = "BTO_0006338"
    EXCRETORY_SYSTEM = "BTO_0006338"

    # excretory pore cell
    BTO_0006339 = "BTO_0006339"
    EXCRETORY_PORE_CELL = "BTO_0006339"

    # excretory duct cell
    BTO_0006340 = "BTO_0006340"
    EXCRETORY_DUCT_CELL = "BTO_0006340"

    # excretory duct
    BTO_0006341 = "BTO_0006341"
    EXCRETORY_DUCT = "BTO_0006341"

    # excretory gland cell
    BTO_0006342 = "BTO_0006342"
    EXCRETORY_GLAND_CELL = "BTO_0006342"

    # CL1-5-F4 cell
    BTO_0006343 = "BTO_0006343"
    CL1_5_F4_CELL = "BTO_0006343"

    # ovarian follicle layer
    BTO_0006344 = "BTO_0006344"
    OVARIAN_FOLLICLE_LAYER = "BTO_0006344"

    # glioblastoma multiforme cancer stem cell
    BTO_0006345 = "BTO_0006345"
    GLIOBLASTOMA_MULTIFORME_CANCER_STEM_CELL = "BTO_0006345"

    # vitellocyte
    BTO_0006346 = "BTO_0006346"
    VITELLOCYTE = "BTO_0006346"

    # neoblast
    BTO_0006347 = "BTO_0006347"
    NEOBLAST = "BTO_0006347"

    # type A spermatogonium
    BTO_0006348 = "BTO_0006348"
    TYPE_A_SPERMATOGONIUM = "BTO_0006348"

    # type B spermatogonium
    BTO_0006349 = "BTO_0006349"
    TYPE_B_SPERMATOGONIUM = "BTO_0006349"

    # polyp
    BTO_0006350 = "BTO_0006350"
    POLYP = "BTO_0006350"

    # glioma sphere-forming cell
    BTO_0006351 = "BTO_0006351"
    GLIOMA_SPHERE_FORMING_CELL = "BTO_0006351"

    # glomerular macrophage
    BTO_0006352 = "BTO_0006352"
    GLOMERULAR_MACROPHAGE = "BTO_0006352"

    # GM-12878 cell
    BTO_0006353 = "BTO_0006353"
    GM_12878_CELL = "BTO_0006353"

    # tracheal fluid
    BTO_0006354 = "BTO_0006354"
    TRACHEAL_FLUID = "BTO_0006354"

    # MS-1 cell
    BTO_0006355 = "BTO_0006355"
    MS_1_CELL = "BTO_0006355"

    # renal oncocytoma cell
    BTO_0006356 = "BTO_0006356"
    RENAL_ONCOCYTOMA_CELL = "BTO_0006356"

    # renal neoplasm cell
    BTO_0006357 = "BTO_0006357"
    RENAL_NEOPLASM_CELL = "BTO_0006357"

    # TIG-1 cell
    BTO_0006358 = "BTO_0006358"
    TIG_1_CELL = "BTO_0006358"

    # TEX cell
    BTO_0006359 = "BTO_0006359"
    TEX_CELL = "BTO_0006359"

    # skin squamous cell carcinoma cell
    BTO_0006360 = "BTO_0006360"
    SKIN_SQUAMOUS_CELL_CARCINOMA_CELL = "BTO_0006360"

    # SKOV-1 cell
    BTO_0006361 = "BTO_0006361"
    SKOV_1_CELL = "BTO_0006361"

    # RMC cell
    BTO_0006362 = "BTO_0006362"
    RMC_CELL = "BTO_0006362"

    # rete mirabile
    BTO_0006363 = "BTO_0006363"
    RETE_MIRABILE = "BTO_0006363"

    # Pfeiffer cell
    BTO_0006364 = "BTO_0006364"
    PFEIFFER_CELL = "BTO_0006364"

    # diffuse large B-cell lymphoma cell line
    BTO_0006365 = "BTO_0006365"
    DIFFUSE_LARGE_B_CELL_LYMPHOMA_CELL_LINE = "BTO_0006365"

    # pericryptal myofibroblast
    BTO_0006366 = "BTO_0006366"
    PERICRYPTAL_MYOFIBROBLAST = "BTO_0006366"

    # pericryptal fibroblast
    BTO_0006367 = "BTO_0006367"
    PERICRYPTAL_FIBROBLAST = "BTO_0006367"

    # PCI-51 cell
    BTO_0006368 = "BTO_0006368"
    PCI_51_CELL = "BTO_0006368"

    # PC-3ML cell
    BTO_0006369 = "BTO_0006369"
    PC_3ML_CELL = "BTO_0006369"

    # opisthonephros
    BTO_0006370 = "BTO_0006370"
    OPISTHONEPHROS = "BTO_0006370"

    # OBA-9 cell
    BTO_0006371 = "BTO_0006371"
    OBA_9_CELL = "BTO_0006371"

    # U87DND cell
    BTO_0006374 = "BTO_0006374"
    U87DND_CELL = "BTO_0006374"

    # 5TGM1 cell
    BTO_0006375 = "BTO_0006375"
    _5TGM1_CELL = "BTO_0006375"

    # 769-P cell
    BTO_0006376 = "BTO_0006376"
    _769_P_CELL = "BTO_0006376"

    # AHH-1 cell
    BTO_0006377 = "BTO_0006377"
    AHH_1_CELL = "BTO_0006377"

    # AK-D cell
    BTO_0006378 = "BTO_0006378"
    AK_D_CELL = "BTO_0006378"

    # ALC cell
    BTO_0006379 = "BTO_0006379"
    ALC_CELL = "BTO_0006379"

    # BEL-7404-CP20 cell
    BTO_0006380 = "BTO_0006380"
    BEL_7404_CP20_CELL = "BTO_0006380"

    # bone lining cell
    BTO_0006381 = "BTO_0006381"
    BONE_LINING_CELL = "BTO_0006381"

    # CH12F3-2A cell
    BTO_0006382 = "BTO_0006382"
    CH12F3_2A_CELL = "BTO_0006382"

    # CHLA-90 cell
    BTO_0006383 = "BTO_0006383"
    CHLA_90_CELL = "BTO_0006383"

    # synovial sarcoma cell line
    BTO_0006384 = "BTO_0006384"
    SYNOVIAL_SARCOMA_CELL_LINE = "BTO_0006384"

    # CME-1 cell
    BTO_0006385 = "BTO_0006385"
    CME_1_CELL = "BTO_0006385"

    # SW-982 cell
    BTO_0006386 = "BTO_0006386"
    SW_982_CELL = "BTO_0006386"

    # craniofacial bone
    BTO_0006387 = "BTO_0006387"
    CRANIOFACIAL_BONE = "BTO_0006387"

    # cuvierian tubule
    BTO_0006388 = "BTO_0006388"
    CUVIERIAN_TUBULE = "BTO_0006388"

    # enteric neuron
    BTO_0006389 = "BTO_0006389"
    ENTERIC_NEURON = "BTO_0006389"

    # EOC-13.31 cell
    BTO_0006390 = "BTO_0006390"
    EOC_13_31_CELL = "BTO_0006390"

    # ephyra
    BTO_0006391 = "BTO_0006391"
    EPHYRA = "BTO_0006391"

    # Fcwf-4 cell
    BTO_0006392 = "BTO_0006392"
    FCWF_4_CELL = "BTO_0006392"

    # FS-293F cell
    BTO_0006393 = "BTO_0006393"
    FS_293F_CELL = "BTO_0006393"

    # GES-1 cell
    BTO_0006394 = "BTO_0006394"
    GES_1_CELL = "BTO_0006394"

    # HCC-1806 cell
    BTO_0006395 = "BTO_0006395"
    HCC_1806_CELL = "BTO_0006395"

    # HCE-T cell
    BTO_0006396 = "BTO_0006396"
    HCE_T_CELL = "BTO_0006396"

    # HCM cell
    BTO_0006397 = "BTO_0006397"
    HCM_CELL = "BTO_0006397"

    # MCF-10-2A cell
    BTO_0006398 = "BTO_0006398"
    MCF_10_2A_CELL = "BTO_0006398"

    # HF-19 cell
    BTO_0006399 = "BTO_0006399"
    HF_19_CELL = "BTO_0006399"

    # HPMEC cell
    BTO_0006400 = "BTO_0006400"
    HPMEC_CELL = "BTO_0006400"

    # interstitial macrophage
    BTO_0006401 = "BTO_0006401"
    INTERSTITIAL_MACROPHAGE = "BTO_0006401"

    # IPEC-J2 cell
    BTO_0006402 = "BTO_0006402"
    IPEC_J2_CELL = "BTO_0006402"

    # IPEC-1 cell
    BTO_0006403 = "BTO_0006403"
    IPEC_1_CELL = "BTO_0006403"

    # JHU-028 cell
    BTO_0006404 = "BTO_0006404"
    JHU_028_CELL = "BTO_0006404"

    # K-1 cell
    BTO_0006405 = "BTO_0006405"
    K_1_CELL = "BTO_0006405"

    # GLAG-66 cell
    BTO_0006406 = "BTO_0006406"
    GLAG_66_CELL = "BTO_0006406"

    # K7M2-WT cell
    BTO_0006407 = "BTO_0006407"
    K7M2_WT_CELL = "BTO_0006407"

    # K7 cell
    BTO_0006408 = "BTO_0006408"
    K7_CELL = "BTO_0006408"

    # KB-CP20 cell
    BTO_0006409 = "BTO_0006409"
    KB_CP20_CELL = "BTO_0006409"

    # KB-CP10 cell
    BTO_0006410 = "BTO_0006410"
    KB_CP10_CELL = "BTO_0006410"

    # KB-CP5 cell
    BTO_0006411 = "BTO_0006411"
    KB_CP5_CELL = "BTO_0006411"

    # myeolomonocytic leukemia cell line
    BTO_0006412 = "BTO_0006412"
    MYEOLOMONOCYTIC_LEUKEMIA_CELL_LINE = "BTO_0006412"

    # MV-4-11 cell
    BTO_0006413 = "BTO_0006413"
    MV_4_11_CELL = "BTO_0006413"

    # OCI-LY7 cell
    BTO_0006414 = "BTO_0006414"
    OCI_LY7_CELL = "BTO_0006414"

    # ovary clear cell adenocarcinoma cell line
    BTO_0006415 = "BTO_0006415"
    OVARY_CLEAR_CELL_ADENOCARCINOMA_CELL_LINE = "BTO_0006415"

    # Sertoli cell tumor cell line
    BTO_0006416 = "BTO_0006416"
    SERTOLI_CELL_TUMOR_CELL_LINE = "BTO_0006416"

    # Sertoli cell tumor cell
    BTO_0006417 = "BTO_0006417"
    SERTOLI_CELL_TUMOR_CELL = "BTO_0006417"

    # SCC-25/CP cell
    BTO_0006418 = "BTO_0006418"
    SCC_25_CP_CELL = "BTO_0006418"

    # FD105 cell
    BTO_0006419 = "BTO_0006419"
    FD105_CELL = "BTO_0006419"

    # MHM cell
    BTO_0006420 = "BTO_0006420"
    MHM_CELL = "BTO_0006420"

    # KPD cell
    BTO_0006421 = "BTO_0006421"
    KPD_CELL = "BTO_0006421"

    # HEK-293-APPswe cell
    BTO_0006422 = "BTO_0006422"
    HEK_293_APPSWE_CELL = "BTO_0006422"

    # BCIRL-HZ-AM1 cell
    BTO_0006423 = "BTO_0006423"
    BCIRL_HZ_AM1_CELL = "BTO_0006423"

    # BCIRL-HZ-AM2 cell
    BTO_0006424 = "BTO_0006424"
    BCIRL_HZ_AM2_CELL = "BTO_0006424"

    # BCIRL-HZ-AM3 cell
    BTO_0006425 = "BTO_0006425"
    BCIRL_HZ_AM3_CELL = "BTO_0006425"

    # BCIRL-HV-AM2 cell
    BTO_0006426 = "BTO_0006426"
    BCIRL_HV_AM2_CELL = "BTO_0006426"

    # BCIRL-HV-AM1 cell
    BTO_0006427 = "BTO_0006427"
    BCIRL_HV_AM1_CELL = "BTO_0006427"

    # plant placenta
    BTO_0006428 = "BTO_0006428"
    PLANT_PLACENTA = "BTO_0006428"

    # white adipocyte
    BTO_0006429 = "BTO_0006429"
    WHITE_ADIPOCYTE = "BTO_0006429"

    # brown adipocyte
    BTO_0006430 = "BTO_0006430"
    BROWN_ADIPOCYTE = "BTO_0006430"

    # vagal lobe
    BTO_0006431 = "BTO_0006431"
    VAGAL_LOBE = "BTO_0006431"

    # posterior tuberculum
    BTO_0006432 = "BTO_0006432"
    POSTERIOR_TUBERCULUM = "BTO_0006432"

    # shuck
    BTO_0006433 = "BTO_0006433"
    SHUCK = "BTO_0006433"

    # phylloid
    BTO_0006434 = "BTO_0006434"
    PHYLLOID = "BTO_0006434"

    # OC-314 cell
    BTO_0006435 = "BTO_0006435"
    OC_314_CELL = "BTO_0006435"

    # OC-315 cell
    BTO_0006436 = "BTO_0006436"
    OC_315_CELL = "BTO_0006436"

    # OC-316 cell
    BTO_0006437 = "BTO_0006437"
    OC_316_CELL = "BTO_0006437"

    # NCI-H2030 cell
    BTO_0006438 = "BTO_0006438"
    NCI_H2030_CELL = "BTO_0006438"

    # H-414 cell
    BTO_0006439 = "BTO_0006439"
    H_414_CELL = "BTO_0006439"

    # HCC-1438 cell
    BTO_0006440 = "BTO_0006440"
    HCC_1438_CELL = "BTO_0006440"

    # HCC-1500 cell
    BTO_0006441 = "BTO_0006441"
    HCC_1500_CELL = "BTO_0006441"

    # HCC-1833 cell
    BTO_0006442 = "BTO_0006442"
    HCC_1833_CELL = "BTO_0006442"

    # culture condition:CD3+ cell
    BTO_0006443 = "BTO_0006443"
    CULTURE_CONDITION_CD3__CELL = "BTO_0006443"

    # Jeko-1 cell
    BTO_0006444 = "BTO_0006444"
    JEKO_1_CELL = "BTO_0006444"

    # AF22 cell
    BTO_0006445 = "BTO_0006445"
    AF22_CELL = "BTO_0006445"

    # CCD-1095Sk cell
    BTO_0006446 = "BTO_0006446"
    CCD_1095SK_CELL = "BTO_0006446"

    # EFM-19 cell
    BTO_0006447 = "BTO_0006447"
    EFM_19_CELL = "BTO_0006447"

    # F-180 cell
    BTO_0006448 = "BTO_0006448"
    F_180_CELL = "BTO_0006448"

    # F-184 cell
    BTO_0006449 = "BTO_0006449"
    F_184_CELL = "BTO_0006449"

    # FHCC-98 cell
    BTO_0006450 = "BTO_0006450"
    FHCC_98_CELL = "BTO_0006450"

    # peritoneal cancer cell
    BTO_0006451 = "BTO_0006451"
    PERITONEAL_CANCER_CELL = "BTO_0006451"

    # HCCLM-9 cell
    BTO_0006452 = "BTO_0006452"
    HCCLM_9_CELL = "BTO_0006452"

    # HEK-293S cell
    BTO_0006453 = "BTO_0006453"
    HEK_293S_CELL = "BTO_0006453"

    # HEY-A8 cell
    BTO_0006454 = "BTO_0006454"
    HEY_A8_CELL = "BTO_0006454"

    # HHL-5 cell
    BTO_0006455 = "BTO_0006455"
    HHL_5_CELL = "BTO_0006455"

    # HPDE6-C7 cell
    BTO_0006456 = "BTO_0006456"
    HPDE6_C7_CELL = "BTO_0006456"

    # UM-UC-1 cell
    BTO_0006457 = "BTO_0006457"
    UM_UC_1_CELL = "BTO_0006457"

    # HepG2-VL17A cell
    BTO_0006458 = "BTO_0006458"
    HEPG2_VL17A_CELL = "BTO_0006458"

    # KMS-12-BM cell
    BTO_0006459 = "BTO_0006459"
    KMS_12_BM_CELL = "BTO_0006459"

    # KMS-12-PE cell
    BTO_0006460 = "BTO_0006460"
    KMS_12_PE_CELL = "BTO_0006460"

    # KMS-26 cell
    BTO_0006461 = "BTO_0006461"
    KMS_26_CELL = "BTO_0006461"

    # SU-DHL-4 cell
    BTO_0006462 = "BTO_0006462"
    SU_DHL_4_CELL = "BTO_0006462"

    # SU-DHL-2 cell
    BTO_0006463 = "BTO_0006463"
    SU_DHL_2_CELL = "BTO_0006463"

    # muscle invasive bladder cancer cell
    BTO_0006464 = "BTO_0006464"
    MUSCLE_INVASIVE_BLADDER_CANCER_CELL = "BTO_0006464"

    # intestinal stem cell
    BTO_0006465 = "BTO_0006465"
    INTESTINAL_STEM_CELL = "BTO_0006465"

    # LC-2/ad cell
    BTO_0006466 = "BTO_0006466"
    LC_2_AD_CELL = "BTO_0006466"

    # LNCaP-Abl cell
    BTO_0006467 = "BTO_0006467"
    LNCAP_ABL_CELL = "BTO_0006467"

    # peritoneal cell line
    BTO_0006468 = "BTO_0006468"
    PERITONEAL_CELL_LINE = "BTO_0006468"

    # LP-9 cell
    BTO_0006469 = "BTO_0006469"
    LP_9_CELL = "BTO_0006469"

    # MDA-MB-231-Met2 cell
    BTO_0006470 = "BTO_0006470"
    MDA_MB_231_MET2_CELL = "BTO_0006470"

    # MIHA cell
    BTO_0006471 = "BTO_0006471"
    MIHA_CELL = "BTO_0006471"

    # GM01617 cell
    BTO_0006472 = "BTO_0006472"
    GM01617_CELL = "BTO_0006472"

    # brain-corpora cardiaca-corpora allata complex
    BTO_0006473 = "BTO_0006473"
    BRAIN_CORPORA_CARDIACA_CORPORA_ALLATA_COMPLEX = "BTO_0006473"

    # rhizoid
    BTO_0006474 = "BTO_0006474"
    RHIZOID = "BTO_0006474"

    # Sai1 cell
    BTO_0006475 = "BTO_0006475"
    SAI1_CELL = "BTO_0006475"

    # synencephalon
    BTO_0006476 = "BTO_0006476"
    SYNENCEPHALON = "BTO_0006476"

    # T37i cell
    BTO_0006477 = "BTO_0006477"
    T37I_CELL = "BTO_0006477"

    # Bm7Brm cell
    BTO_0006478 = "BTO_0006478"
    BM7BRM_CELL = "BTO_0006478"

    # Hep3B-c1 cell
    BTO_0006479 = "BTO_0006479"
    HEP3B_C1_CELL = "BTO_0006479"

    # NU-DUL-1 cell
    BTO_0006480 = "BTO_0006480"
    NU_DUL_1_CELL = "BTO_0006480"

    # lateral hypothalamus
    BTO_0006481 = "BTO_0006481"
    LATERAL_HYPOTHALAMUS = "BTO_0006481"

    # SNU-719 cell
    BTO_0006482 = "BTO_0006482"
    SNU_719_CELL = "BTO_0006482"

    # GL-261 cell
    BTO_0006483 = "BTO_0006483"
    GL_261_CELL = "BTO_0006483"

    # HMT-3522 S1 cell
    BTO_0006484 = "BTO_0006484"
    HMT_3522_S1_CELL = "BTO_0006484"

    # PA-TU-8902 cell
    BTO_0006485 = "BTO_0006485"
    PA_TU_8902_CELL = "BTO_0006485"

    # myxofibrosarcoma cell
    BTO_0006486 = "BTO_0006486"
    MYXOFIBROSARCOMA_CELL = "BTO_0006486"

    # aerodigestive tract
    BTO_0006487 = "BTO_0006487"
    AERODIGESTIVE_TRACT = "BTO_0006487"

    # steroidogenic cell
    BTO_0006488 = "BTO_0006488"
    STEROIDOGENIC_CELL = "BTO_0006488"

    # brood pouch
    BTO_0006489 = "BTO_0006489"
    BROOD_POUCH = "BTO_0006489"

    # GT-38 cell
    BTO_0006490 = "BTO_0006490"
    GT_38_CELL = "BTO_0006490"

    # GT-39 cell
    BTO_0006491 = "BTO_0006491"
    GT_39_CELL = "BTO_0006491"

    # palea
    BTO_0006492 = "BTO_0006492"
    PALEA = "BTO_0006492"

    # myxoliposarcoma cell
    BTO_0006493 = "BTO_0006493"
    MYXOLIPOSARCOMA_CELL = "BTO_0006493"

    # fibromyxosarcoma cell
    BTO_0006494 = "BTO_0006494"
    FIBROMYXOSARCOMA_CELL = "BTO_0006494"

    # spathe
    BTO_0006495 = "BTO_0006495"
    SPATHE = "BTO_0006495"

    # inflorescence bract
    BTO_0006496 = "BTO_0006496"
    INFLORESCENCE_BRACT = "BTO_0006496"

    # NASS cell
    BTO_0006497 = "BTO_0006497"
    NASS_CELL = "BTO_0006497"

    # FISK cell
    BTO_0006498 = "BTO_0006498"
    FISK_CELL = "BTO_0006498"

    # spermatocyte cell line
    BTO_0006499 = "BTO_0006499"
    SPERMATOCYTE_CELL_LINE = "BTO_0006499"

    # GC-2 cell
    BTO_0006500 = "BTO_0006500"
    GC_2_CELL = "BTO_0006500"

    # natural killer T cell
    BTO_0006501 = "BTO_0006501"
    NATURAL_KILLER_T_CELL = "BTO_0006501"

    # Jar-GnT4a cell
    BTO_0006502 = "BTO_0006502"
    JAR_GNT4A_CELL = "BTO_0006502"

    # CGL-2 cell
    BTO_0006503 = "BTO_0006503"
    CGL_2_CELL = "BTO_0006503"

    # oculomotor nucleus
    BTO_0006504 = "BTO_0006504"
    OCULOMOTOR_NUCLEUS = "BTO_0006504"

    # Edinger-Westphal nucleus
    BTO_0006505 = "BTO_0006505"
    EDINGER_WESTPHAL_NUCLEUS = "BTO_0006505"

    # CL1-5 Fut8-KD cell
    BTO_0006506 = "BTO_0006506"
    CL1_5_FUT8_KD_CELL = "BTO_0006506"

    # CHO-Lec8 cell
    BTO_0006507 = "BTO_0006507"
    CHO_LEC8_CELL = "BTO_0006507"

    # TPC-1 cell
    BTO_0006508 = "BTO_0006508"
    TPC_1_CELL = "BTO_0006508"

    # Hca-P cell
    BTO_0006509 = "BTO_0006509"
    HCA_P_CELL = "BTO_0006509"

    # MOSEC cell
    BTO_0006510 = "BTO_0006510"
    MOSEC_CELL = "BTO_0006510"

    # PMF-Ko14 cell
    BTO_0006511 = "BTO_0006511"
    PMF_KO14_CELL = "BTO_0006511"

    # SPCA-1 cell
    BTO_0006512 = "BTO_0006512"
    SPCA_1_CELL = "BTO_0006512"

    # HEK-293-AT1 cell
    BTO_0006513 = "BTO_0006513"
    HEK_293_AT1_CELL = "BTO_0006513"

    # foreleg
    BTO_0006514 = "BTO_0006514"
    FORELEG = "BTO_0006514"

    # hindleg
    BTO_0006515 = "BTO_0006515"
    HINDLEG = "BTO_0006515"

    # invertebrate maxilla
    BTO_0006516 = "BTO_0006516"
    INVERTEBRATE_MAXILLA = "BTO_0006516"

    # maxillary palp
    BTO_0006517 = "BTO_0006517"
    MAXILLARY_PALP = "BTO_0006517"

    # storage parenchyma
    BTO_0006518 = "BTO_0006518"
    STORAGE_PARENCHYMA = "BTO_0006518"

    # mesontle
    BTO_0006519 = "BTO_0006519"
    MESONTLE = "BTO_0006519"

    # bearer of
    bearer_of = "bearer_of"
    BEARER_OF = "bearer_of"

    # causually influences
    causually_influences = "causually_influences"
    CAUSUALLY_INFLUENCES = "causually_influences"

    # contained in
    contained_in = "contained_in"
    CONTAINED_IN = "contained_in"

    # derives from/develops from
    develops_from = "develops_from"
    DERIVES_FROM_DEVELOPS_FROM = "develops_from"

    # disease arises from structure
    disease_arises_from_structure = "disease_arises_from_structure"
    DISEASE_ARISES_FROM_STRUCTURE = "disease_arises_from_structure"

    # disease causes dysfunction of
    disease_causes_dysfunction_of = "disease_causes_dysfunction_of"
    DISEASE_CAUSES_DYSFUNCTION_OF = "disease_causes_dysfunction_of"

    # part of
    part_of = "part_of"
    PART_OF = "part_of"

    # produced by
    produced_by = "produced_by"
    PRODUCED_BY = "produced_by"

    # realized in
    realized_in = "realized_in"
    REALIZED_IN = "realized_in"

    # related to
    related_to = "related_to"
    RELATED_TO = "related_to"


__all__ = [
    "BTO",
]
