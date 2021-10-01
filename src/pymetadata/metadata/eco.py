"""ECO ontology."""

from enum import Enum


class ECO(str, Enum):
    """Enum for ECO ontology."""

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

    # realized in
    BFO_0000054 = "BFO_0000054"
    REALIZED_IN = "BFO_0000054"

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

    # ATP
    CHEBI_15422 = "CHEBI_15422"
    ATP = "CHEBI_15422"

    # peptide
    CHEBI_16670 = "CHEBI_16670"
    PEPTIDE = "CHEBI_16670"

    # deoxyribonucleic acid
    CHEBI_16991 = "CHEBI_16991"
    DEOXYRIBONUCLEIC_ACID = "CHEBI_16991"

    # molecular entity
    CHEBI_23367 = "CHEBI_23367"
    MOLECULAR_ENTITY = "CHEBI_23367"

    # cytochalasin
    CHEBI_23528 = "CHEBI_23528"
    CYTOCHALASIN = "CHEBI_23528"

    # acrylamide
    CHEBI_28619 = "CHEBI_28619"
    ACRYLAMIDE = "CHEBI_28619"

    # atom
    CHEBI_33250 = "CHEBI_33250"
    ATOM = "CHEBI_33250"

    # nucleic acid
    CHEBI_33696 = "CHEBI_33696"
    NUCLEIC_ACID = "CHEBI_33696"

    # ribonucleic acid
    CHEBI_33697 = "CHEBI_33697"
    RIBONUCLEIC_ACID = "CHEBI_33697"

    # macromolecule
    CHEBI_33839 = "CHEBI_33839"
    MACROMOLECULE = "CHEBI_33839"

    # double-stranded DNA
    CHEBI_4705 = "CHEBI_4705"
    DOUBLE_STRANDED_DNA = "CHEBI_4705"

    # 5-bromo-2'-deoxyuridine
    CHEBI_472552 = "CHEBI_472552"
    _5_BROMO_2__DEOXYURIDINE = "CHEBI_472552"

    # chromium-51
    CHEBI_50076 = "CHEBI_50076"
    CHROMIUM_51 = "CHEBI_50076"

    # tritiated thymidine
    CHEBI_53526 = "CHEBI_53526"
    TRITIATED_THYMIDINE = "CHEBI_53526"

    # fluorescence microscopy
    CHMO_0000087 = "CHMO_0000087"
    FLUORESCENCE_MICROSCOPY = "CHMO_0000087"

    # light microscopy
    CHMO_0000102 = "CHMO_0000102"
    LIGHT_MICROSCOPY = "CHMO_0000102"

    # cell
    CL_0000000 = "CL_0000000"
    CELL = "CL_0000000"

    # cultured cell
    CL_0000010 = "CL_0000010"
    CULTURED_CELL = "CL_0000010"

    # B cell
    CL_0000236 = "CL_0000236"
    B_CELL = "CL_0000236"

    # lymphocyte
    CL_0000542 = "CL_0000542"
    LYMPHOCYTE = "CL_0000542"

    # experimentally modified cell in vitro
    CL_0000578 = "CL_0000578"
    EXPERIMENTALLY_MODIFIED_CELL_IN_VITRO = "CL_0000578"

    # mononuclear cell
    CL_0000842 = "CL_0000842"
    MONONUCLEAR_CELL = "CL_0000842"

    # evidence
    ECO_0000000 = "ECO_0000000"
    EVIDENCE = "ECO_0000000"

    # inference from background scientific knowledge
    ECO_0000001 = "ECO_0000001"
    INFERENCE_FROM_BACKGROUND_SCIENTIFIC_KNOWLEDGE = "ECO_0000001"

    # direct assay evidence
    ECO_0000002 = "ECO_0000002"
    DIRECT_ASSAY_EVIDENCE = "ECO_0000002"

    # reconstitution assay evidence
    ECO_0000003 = "ECO_0000003"
    RECONSTITUTION_ASSAY_EVIDENCE = "ECO_0000003"

    # cell fractionation evidence
    ECO_0000004 = "ECO_0000004"
    CELL_FRACTIONATION_EVIDENCE = "ECO_0000004"

    # enzymatic activity assay evidence
    ECO_0000005 = "ECO_0000005"
    ENZYMATIC_ACTIVITY_ASSAY_EVIDENCE = "ECO_0000005"

    # experimental evidence
    ECO_0000006 = "ECO_0000006"
    EXPERIMENTAL_EVIDENCE = "ECO_0000006"

    # immunofluorescence evidence
    ECO_0000007 = "ECO_0000007"
    IMMUNOFLUORESCENCE_EVIDENCE = "ECO_0000007"

    # expression pattern evidence
    ECO_0000008 = "ECO_0000008"
    EXPRESSION_PATTERN_EVIDENCE = "ECO_0000008"

    # transcript expression evidence
    ECO_0000009 = "ECO_0000009"
    TRANSCRIPT_EXPRESSION_EVIDENCE = "ECO_0000009"

    # protein expression evidence
    ECO_0000010 = "ECO_0000010"
    PROTEIN_EXPRESSION_EVIDENCE = "ECO_0000010"

    # genetic interaction evidence
    ECO_0000011 = "ECO_0000011"
    GENETIC_INTERACTION_EVIDENCE = "ECO_0000011"

    # functional complementation evidence
    ECO_0000012 = "ECO_0000012"
    FUNCTIONAL_COMPLEMENTATION_EVIDENCE = "ECO_0000012"

    # transgenic rescue experiment evidence
    ECO_0000013 = "ECO_0000013"
    TRANSGENIC_RESCUE_EXPERIMENT_EVIDENCE = "ECO_0000013"

    # mutant phenotype evidence
    ECO_0000015 = "ECO_0000015"
    MUTANT_PHENOTYPE_EVIDENCE = "ECO_0000015"

    # loss-of-function mutant phenotype evidence
    ECO_0000016 = "ECO_0000016"
    LOSS_OF_FUNCTION_MUTANT_PHENOTYPE_EVIDENCE = "ECO_0000016"

    # ectopic expression evidence
    ECO_0000017 = "ECO_0000017"
    ECTOPIC_EXPRESSION_EVIDENCE = "ECO_0000017"

    # anti-sense experiment evidence
    ECO_0000018 = "ECO_0000018"
    ANTI_SENSE_EXPERIMENT_EVIDENCE = "ECO_0000018"

    # RNAi evidence
    ECO_0000019 = "ECO_0000019"
    RNAI_EVIDENCE = "ECO_0000019"

    # protein inhibition evidence
    ECO_0000020 = "ECO_0000020"
    PROTEIN_INHIBITION_EVIDENCE = "ECO_0000020"

    # physical interaction evidence
    ECO_0000021 = "ECO_0000021"
    PHYSICAL_INTERACTION_EVIDENCE = "ECO_0000021"

    # co-purification evidence
    ECO_0000022 = "ECO_0000022"
    CO_PURIFICATION_EVIDENCE = "ECO_0000022"

    # affinity evidence
    ECO_0000023 = "ECO_0000023"
    AFFINITY_EVIDENCE = "ECO_0000023"

    # protein binding evidence
    ECO_0000024 = "ECO_0000024"
    PROTEIN_BINDING_EVIDENCE = "ECO_0000024"

    # bait-prey hybrid interaction evidence
    ECO_0000025 = "ECO_0000025"
    BAIT_PREY_HYBRID_INTERACTION_EVIDENCE = "ECO_0000025"

    # nucleic acid hybridization evidence
    ECO_0000026 = "ECO_0000026"
    NUCLEIC_ACID_HYBRIDIZATION_EVIDENCE = "ECO_0000026"

    # structural similarity evidence
    ECO_0000027 = "ECO_0000027"
    STRUCTURAL_SIMILARITY_EVIDENCE = "ECO_0000027"

    # motif similarity evidence
    ECO_0000028 = "ECO_0000028"
    MOTIF_SIMILARITY_EVIDENCE = "ECO_0000028"

    # match to InterPro member signature evidence
    ECO_0000029 = "ECO_0000029"
    MATCH_TO_INTERPRO_MEMBER_SIGNATURE_EVIDENCE = "ECO_0000029"

    # BLAST evidence used in manual assertion
    ECO_0000030 = "ECO_0000030"
    BLAST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000030"

    # protein BLAST evidence used in manual assertion
    ECO_0000031 = "ECO_0000031"
    PROTEIN_BLAST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000031"

    # nucleotide BLAST evidence used in manual assertion
    ECO_0000032 = "ECO_0000032"
    NUCLEOTIDE_BLAST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000032"

    # author statement supported by traceable reference
    ECO_0000033 = "ECO_0000033"
    AUTHOR_STATEMENT_SUPPORTED_BY_TRACEABLE_REFERENCE = "ECO_0000033"

    # author statement without traceable support
    ECO_0000034 = "ECO_0000034"
    AUTHOR_STATEMENT_WITHOUT_TRACEABLE_SUPPORT = "ECO_0000034"

    # no evidence data found
    ECO_0000035 = "ECO_0000035"
    NO_EVIDENCE_DATA_FOUND = "ECO_0000035"

    # not_recorded
    ECO_0000037 = "ECO_0000037"
    NOT_RECORDED = "ECO_0000037"

    # transient rescue experiment evidence
    ECO_0000038 = "ECO_0000038"
    TRANSIENT_RESCUE_EXPERIMENT_EVIDENCE = "ECO_0000038"

    # protein assay evidence
    ECO_0000039 = "ECO_0000039"
    PROTEIN_ASSAY_EVIDENCE = "ECO_0000039"

    # immunological assay evidence
    ECO_0000040 = "ECO_0000040"
    IMMUNOLOGICAL_ASSAY_EVIDENCE = "ECO_0000040"

    # similarity evidence
    ECO_0000041 = "ECO_0000041"
    SIMILARITY_EVIDENCE = "ECO_0000041"

    # gain-of-function mutant phenotypic evidence
    ECO_0000042 = "ECO_0000042"
    GAIN_OF_FUNCTION_MUTANT_PHENOTYPIC_EVIDENCE = "ECO_0000042"

    # sequence similarity evidence
    ECO_0000044 = "ECO_0000044"
    SEQUENCE_SIMILARITY_EVIDENCE = "ECO_0000044"

    # spatial pattern of protein expression evidence
    ECO_0000045 = "ECO_0000045"
    SPATIAL_PATTERN_OF_PROTEIN_EXPRESSION_EVIDENCE = "ECO_0000045"

    # spatial pattern of transcript expression evidence
    ECO_0000047 = "ECO_0000047"
    SPATIAL_PATTERN_OF_TRANSCRIPT_EXPRESSION_EVIDENCE = "ECO_0000047"

    # reporter gene assay evidence
    ECO_0000049 = "ECO_0000049"
    REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0000049"

    # voucher specimen phenotypic analysis evidence
    ECO_0000050 = "ECO_0000050"
    VOUCHER_SPECIMEN_PHENOTYPIC_ANALYSIS_EVIDENCE = "ECO_0000050"

    # genetic similarity evidence
    ECO_0000051 = "ECO_0000051"
    GENETIC_SIMILARITY_EVIDENCE = "ECO_0000051"

    # suppressor/enhancer interaction phenotypic evidence
    ECO_0000052 = "ECO_0000052"
    SUPPRESSOR_ENHANCER_INTERACTION_PHENOTYPIC_EVIDENCE = "ECO_0000052"

    # automatically integrated combinatorial evidence used in automatic assertion
    ECO_0000053 = "ECO_0000053"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000053"
    )

    # double mutant phenotypic evidence
    ECO_0000054 = "ECO_0000054"
    DOUBLE_MUTANT_PHENOTYPIC_EVIDENCE = "ECO_0000054"

    # array experiment evidence
    ECO_0000055 = "ECO_0000055"
    ARRAY_EXPERIMENT_EVIDENCE = "ECO_0000055"

    # epistatic interaction phenotypic evidence
    ECO_0000056 = "ECO_0000056"
    EPISTATIC_INTERACTION_PHENOTYPIC_EVIDENCE = "ECO_0000056"

    # phenotypic similarity evidence
    ECO_0000057 = "ECO_0000057"
    PHENOTYPIC_SIMILARITY_EVIDENCE = "ECO_0000057"

    # expression microarray evidence
    ECO_0000058 = "ECO_0000058"
    EXPRESSION_MICROARRAY_EVIDENCE = "ECO_0000058"

    # experimental phenotypic evidence
    ECO_0000059 = "ECO_0000059"
    EXPERIMENTAL_PHENOTYPIC_EVIDENCE = "ECO_0000059"

    # positional similarity evidence
    ECO_0000060 = "ECO_0000060"
    POSITIONAL_SIMILARITY_EVIDENCE = "ECO_0000060"

    # quantitative trait analysis evidence
    ECO_0000061 = "ECO_0000061"
    QUANTITATIVE_TRAIT_ANALYSIS_EVIDENCE = "ECO_0000061"

    # cRNA to DNA expression microarray evidence
    ECO_0000062 = "ECO_0000062"
    CRNA_TO_DNA_EXPRESSION_MICROARRAY_EVIDENCE = "ECO_0000062"

    # compositional similarity evidence
    ECO_0000063 = "ECO_0000063"
    COMPOSITIONAL_SIMILARITY_EVIDENCE = "ECO_0000063"

    # functional complementation in heterologous system evidence
    ECO_0000064 = "ECO_0000064"
    FUNCTIONAL_COMPLEMENTATION_IN_HETEROLOGOUS_SYSTEM_EVIDENCE = "ECO_0000064"

    # yeast one-hybrid evidence
    ECO_0000066 = "ECO_0000066"
    YEAST_ONE_HYBRID_EVIDENCE = "ECO_0000066"

    # developmental similarity evidence
    ECO_0000067 = "ECO_0000067"
    DEVELOPMENTAL_SIMILARITY_EVIDENCE = "ECO_0000067"

    # yeast 2-hybrid evidence
    ECO_0000068 = "ECO_0000068"
    YEAST_2_HYBRID_EVIDENCE = "ECO_0000068"

    # differential methylation hybridization evidence
    ECO_0000069 = "ECO_0000069"
    DIFFERENTIAL_METHYLATION_HYBRIDIZATION_EVIDENCE = "ECO_0000069"

    # co-immunoprecipitation evidence
    ECO_0000070 = "ECO_0000070"
    CO_IMMUNOPRECIPITATION_EVIDENCE = "ECO_0000070"

    # morphological similarity evidence
    ECO_0000071 = "ECO_0000071"
    MORPHOLOGICAL_SIMILARITY_EVIDENCE = "ECO_0000071"

    # Sos-recruitment assay evidence
    ECO_0000072 = "ECO_0000072"
    SOS_RECRUITMENT_ASSAY_EVIDENCE = "ECO_0000072"

    # experimental genomic evidence
    ECO_0000073 = "ECO_0000073"
    EXPERIMENTAL_GENOMIC_EVIDENCE = "ECO_0000073"

    # split-ubiquitin functional complementation evidence
    ECO_0000074 = "ECO_0000074"
    SPLIT_UBIQUITIN_FUNCTIONAL_COMPLEMENTATION_EVIDENCE = "ECO_0000074"

    # gene expression similarity evidence
    ECO_0000075 = "ECO_0000075"
    GENE_EXPRESSION_SIMILARITY_EVIDENCE = "ECO_0000075"

    # far-Western blotting evidence
    ECO_0000076 = "ECO_0000076"
    FAR_WESTERN_BLOTTING_EVIDENCE = "ECO_0000076"

    # methylation-specific polymerase chain reaction evidence
    ECO_0000077 = "ECO_0000077"
    METHYLATION_SPECIFIC_POLYMERASE_CHAIN_REACTION_EVIDENCE = "ECO_0000077"

    # southern hybridization evidence
    ECO_0000078 = "ECO_0000078"
    SOUTHERN_HYBRIDIZATION_EVIDENCE = "ECO_0000078"

    # affinity chromatography evidence
    ECO_0000079 = "ECO_0000079"
    AFFINITY_CHROMATOGRAPHY_EVIDENCE = "ECO_0000079"

    # phylogenetic evidence
    ECO_0000080 = "ECO_0000080"
    PHYLOGENETIC_EVIDENCE = "ECO_0000080"

    # targeting sequence prediction evidence
    ECO_0000081 = "ECO_0000081"
    TARGETING_SEQUENCE_PREDICTION_EVIDENCE = "ECO_0000081"

    # polymerase chain reaction evidence
    ECO_0000082 = "ECO_0000082"
    POLYMERASE_CHAIN_REACTION_EVIDENCE = "ECO_0000082"

    # transmembrane domain prediction evidence
    ECO_0000083 = "ECO_0000083"
    TRANSMEMBRANE_DOMAIN_PREDICTION_EVIDENCE = "ECO_0000083"

    # gene neighbors evidence
    ECO_0000084 = "ECO_0000084"
    GENE_NEIGHBORS_EVIDENCE = "ECO_0000084"

    # immunoprecipitation evidence
    ECO_0000085 = "ECO_0000085"
    IMMUNOPRECIPITATION_EVIDENCE = "ECO_0000085"

    # amplification of intermethylated sites evidence
    ECO_0000086 = "ECO_0000086"
    AMPLIFICATION_OF_INTERMETHYLATED_SITES_EVIDENCE = "ECO_0000086"

    # immunolocalization evidence
    ECO_0000087 = "ECO_0000087"
    IMMUNOLOCALIZATION_EVIDENCE = "ECO_0000087"

    # biological system reconstruction evidence
    ECO_0000088 = "ECO_0000088"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE = "ECO_0000088"

    # restriction landmark genomic scanning evidence
    ECO_0000089 = "ECO_0000089"
    RESTRICTION_LANDMARK_GENOMIC_SCANNING_EVIDENCE = "ECO_0000089"

    # immunogold labelling evidence
    ECO_0000090 = "ECO_0000090"
    IMMUNOGOLD_LABELLING_EVIDENCE = "ECO_0000090"

    # epitope-tagged protein immunolocalization evidence
    ECO_0000092 = "ECO_0000092"
    EPITOPE_TAGGED_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE = "ECO_0000092"

    # array-based sequence capture evidence
    ECO_0000093 = "ECO_0000093"
    ARRAY_BASED_SEQUENCE_CAPTURE_EVIDENCE = "ECO_0000093"

    # biological assay evidence
    ECO_0000094 = "ECO_0000094"
    BIOLOGICAL_ASSAY_EVIDENCE = "ECO_0000094"

    # cell growth regulation assay evidence
    ECO_0000095 = "ECO_0000095"
    CELL_GROWTH_REGULATION_ASSAY_EVIDENCE = "ECO_0000095"

    # electrophoretic mobility shift assay evidence
    ECO_0000096 = "ECO_0000096"
    ELECTROPHORETIC_MOBILITY_SHIFT_ASSAY_EVIDENCE = "ECO_0000096"

    # cDNA to DNA expression microarray evidence
    ECO_0000097 = "ECO_0000097"
    CDNA_TO_DNA_EXPRESSION_MICROARRAY_EVIDENCE = "ECO_0000097"

    # obsolete in situ hybridization evidence
    ECO_0000098 = "ECO_0000098"
    OBSOLETE_IN_SITU_HYBRIDIZATION_EVIDENCE = "ECO_0000098"

    # fractionation evidence
    ECO_0000100 = "ECO_0000100"
    FRACTIONATION_EVIDENCE = "ECO_0000100"

    # Affymetrix GeneChip evidence
    ECO_0000101 = "ECO_0000101"
    AFFYMETRIX_GENECHIP_EVIDENCE = "ECO_0000101"

    # co-fractionation evidence
    ECO_0000102 = "ECO_0000102"
    CO_FRACTIONATION_EVIDENCE = "ECO_0000102"

    # DNA to cDNA expression microarray evidence
    ECO_0000104 = "ECO_0000104"
    DNA_TO_CDNA_EXPRESSION_MICROARRAY_EVIDENCE = "ECO_0000104"

    # Nimblegen array evidence
    ECO_0000105 = "ECO_0000105"
    NIMBLEGEN_ARRAY_EVIDENCE = "ECO_0000105"

    # northern blot evidence
    ECO_0000106 = "ECO_0000106"
    NORTHERN_BLOT_EVIDENCE = "ECO_0000106"

    # reverse transcription polymerase chain reaction evidence
    ECO_0000109 = "ECO_0000109"
    REVERSE_TRANSCRIPTION_POLYMERASE_CHAIN_REACTION_EVIDENCE = "ECO_0000109"

    # RNA protection assay evidence
    ECO_0000110 = "ECO_0000110"
    RNA_PROTECTION_ASSAY_EVIDENCE = "ECO_0000110"

    # qualitative western immunoblotting evidence
    ECO_0000112 = "ECO_0000112"
    QUALITATIVE_WESTERN_IMMUNOBLOTTING_EVIDENCE = "ECO_0000112"

    # expression library screen evidence
    ECO_0000114 = "ECO_0000114"
    EXPRESSION_LIBRARY_SCREEN_EVIDENCE = "ECO_0000114"

    # differential hybridization evidence
    ECO_0000116 = "ECO_0000116"
    DIFFERENTIAL_HYBRIDIZATION_EVIDENCE = "ECO_0000116"

    # subtractive hybridization evidence
    ECO_0000118 = "ECO_0000118"
    SUBTRACTIVE_HYBRIDIZATION_EVIDENCE = "ECO_0000118"

    # over expression analysis evidence
    ECO_0000120 = "ECO_0000120"
    OVER_EXPRESSION_ANALYSIS_EVIDENCE = "ECO_0000120"

    # protein localization evidence
    ECO_0000122 = "ECO_0000122"
    PROTEIN_LOCALIZATION_EVIDENCE = "ECO_0000122"

    # fusion protein localization evidence
    ECO_0000124 = "ECO_0000124"
    FUSION_PROTEIN_LOCALIZATION_EVIDENCE = "ECO_0000124"

    # green fluorescent protein fusion protein localization evidence
    ECO_0000126 = "ECO_0000126"
    GREEN_FLUORESCENT_PROTEIN_FUSION_PROTEIN_LOCALIZATION_EVIDENCE = "ECO_0000126"

    # yellow fluorescent protein fusion protein localization evidence
    ECO_0000128 = "ECO_0000128"
    YELLOW_FLUORESCENT_PROTEIN_FUSION_PROTEIN_LOCALIZATION_EVIDENCE = "ECO_0000128"

    # beta-glucuronidase fusion protein localization evidence
    ECO_0000130 = "ECO_0000130"
    BETA_GLUCURONIDASE_FUSION_PROTEIN_LOCALIZATION_EVIDENCE = "ECO_0000130"

    # beta-galactosidase fusion protein localization evidence
    ECO_0000132 = "ECO_0000132"
    BETA_GALACTOSIDASE_FUSION_PROTEIN_LOCALIZATION_EVIDENCE = "ECO_0000132"

    # transport assay evidence
    ECO_0000134 = "ECO_0000134"
    TRANSPORT_ASSAY_EVIDENCE = "ECO_0000134"

    # nucleic acid binding evidence
    ECO_0000136 = "ECO_0000136"
    NUCLEIC_ACID_BINDING_EVIDENCE = "ECO_0000136"

    # ribohomopolymer binding assay evidence
    ECO_0000138 = "ECO_0000138"
    RIBOHOMOPOLYMER_BINDING_ASSAY_EVIDENCE = "ECO_0000138"

    # thin layer chromatography evidence
    ECO_0000140 = "ECO_0000140"
    THIN_LAYER_CHROMATOGRAPHY_EVIDENCE = "ECO_0000140"

    # protein:ion binding evidence
    ECO_0000142 = "ECO_0000142"
    PROTEIN_ION_BINDING_EVIDENCE = "ECO_0000142"

    # Southwestern blot evidence
    ECO_0000144 = "ECO_0000144"
    SOUTHWESTERN_BLOT_EVIDENCE = "ECO_0000144"

    # Northwestern blot evidence
    ECO_0000146 = "ECO_0000146"
    NORTHWESTERN_BLOT_EVIDENCE = "ECO_0000146"

    # in vitro binding evidence
    ECO_0000148 = "ECO_0000148"
    IN_VITRO_BINDING_EVIDENCE = "ECO_0000148"

    # in vitro transcription reconstitution assay evidence
    ECO_0000150 = "ECO_0000150"
    IN_VITRO_TRANSCRIPTION_RECONSTITUTION_ASSAY_EVIDENCE = "ECO_0000150"

    # in vitro recombinant protein transcription reconstitution assay evidence
    ECO_0000152 = "ECO_0000152"
    IN_VITRO_RECOMBINANT_PROTEIN_TRANSCRIPTION_RECONSTITUTION_ASSAY_EVIDENCE = (
        "ECO_0000152"
    )

    # heterologous protein expression evidence
    ECO_0000154 = "ECO_0000154"
    HETEROLOGOUS_PROTEIN_EXPRESSION_EVIDENCE = "ECO_0000154"

    # protein separation evidence
    ECO_0000156 = "ECO_0000156"
    PROTEIN_SEPARATION_EVIDENCE = "ECO_0000156"

    # protein separation followed by direct sequencing evidence
    ECO_0000158 = "ECO_0000158"
    PROTEIN_SEPARATION_FOLLOWED_BY_DIRECT_SEQUENCING_EVIDENCE = "ECO_0000158"

    # protein separation followed by fragment identification evidence
    ECO_0000160 = "ECO_0000160"
    PROTEIN_SEPARATION_FOLLOWED_BY_FRAGMENT_IDENTIFICATION_EVIDENCE = "ECO_0000160"

    # heterologous system uptake evidence
    ECO_0000162 = "ECO_0000162"
    HETEROLOGOUS_SYSTEM_UPTAKE_EVIDENCE = "ECO_0000162"

    # electrophysiology assay evidence
    ECO_0000164 = "ECO_0000164"
    ELECTROPHYSIOLOGY_ASSAY_EVIDENCE = "ECO_0000164"

    # two-electrode voltage clamp recording evidence
    ECO_0000166 = "ECO_0000166"
    TWO_ELECTRODE_VOLTAGE_CLAMP_RECORDING_EVIDENCE = "ECO_0000166"

    # transcription assay evidence
    ECO_0000168 = "ECO_0000168"
    TRANSCRIPTION_ASSAY_EVIDENCE = "ECO_0000168"

    # transcriptional activation assay evidence
    ECO_0000170 = "ECO_0000170"
    TRANSCRIPTIONAL_ACTIVATION_ASSAY_EVIDENCE = "ECO_0000170"

    # biochemical trait analysis evidence
    ECO_0000172 = "ECO_0000172"
    BIOCHEMICAL_TRAIT_ANALYSIS_EVIDENCE = "ECO_0000172"

    # mutant physiological response evidence
    ECO_0000174 = "ECO_0000174"
    MUTANT_PHYSIOLOGICAL_RESPONSE_EVIDENCE = "ECO_0000174"

    # mutant visible phenotype evidence
    ECO_0000176 = "ECO_0000176"
    MUTANT_VISIBLE_PHENOTYPE_EVIDENCE = "ECO_0000176"

    # genomic context evidence
    ECO_0000177 = "ECO_0000177"
    GENOMIC_CONTEXT_EVIDENCE = "ECO_0000177"

    # in vivo assay evidence
    ECO_0000178 = "ECO_0000178"
    IN_VIVO_ASSAY_EVIDENCE = "ECO_0000178"

    # animal model system study evidence
    ECO_0000179 = "ECO_0000179"
    ANIMAL_MODEL_SYSTEM_STUDY_EVIDENCE = "ECO_0000179"

    # clinical study evidence
    ECO_0000180 = "ECO_0000180"
    CLINICAL_STUDY_EVIDENCE = "ECO_0000180"

    # in vitro assay evidence
    ECO_0000181 = "ECO_0000181"
    IN_VITRO_ASSAY_EVIDENCE = "ECO_0000181"

    # in vitro culture assay evidence
    ECO_0000182 = "ECO_0000182"
    IN_VITRO_CULTURE_ASSAY_EVIDENCE = "ECO_0000182"

    # cell-free assay evidence
    ECO_0000183 = "ECO_0000183"
    CELL_FREE_ASSAY_EVIDENCE = "ECO_0000183"

    # enzyme inhibition evidence
    ECO_0000184 = "ECO_0000184"
    ENZYME_INHIBITION_EVIDENCE = "ECO_0000184"

    # sequence alignment evidence
    ECO_0000200 = "ECO_0000200"
    SEQUENCE_ALIGNMENT_EVIDENCE = "ECO_0000200"

    # sequence orthology evidence
    ECO_0000201 = "ECO_0000201"
    SEQUENCE_ORTHOLOGY_EVIDENCE = "ECO_0000201"

    # match to sequence model evidence
    ECO_0000202 = "ECO_0000202"
    MATCH_TO_SEQUENCE_MODEL_EVIDENCE = "ECO_0000202"

    # automatic assertion
    ECO_0000203 = "ECO_0000203"
    AUTOMATIC_ASSERTION = "ECO_0000203"

    # author statement
    ECO_0000204 = "ECO_0000204"
    AUTHOR_STATEMENT = "ECO_0000204"

    # curator inference
    ECO_0000205 = "ECO_0000205"
    CURATOR_INFERENCE = "ECO_0000205"

    # BLAST evidence
    ECO_0000206 = "ECO_0000206"
    BLAST_EVIDENCE = "ECO_0000206"

    # nucleotide BLAST evidence
    ECO_0000207 = "ECO_0000207"
    NUCLEOTIDE_BLAST_EVIDENCE = "ECO_0000207"

    # protein BLAST evidence
    ECO_0000208 = "ECO_0000208"
    PROTEIN_BLAST_EVIDENCE = "ECO_0000208"

    # BLAST evidence used in automatic assertion
    ECO_0000209 = "ECO_0000209"
    BLAST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000209"

    # nucleotide BLAST evidence used in automatic assertion
    ECO_0000210 = "ECO_0000210"
    NUCLEOTIDE_BLAST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000210"

    # protein BLAST evidence used in automatic assertion
    ECO_0000211 = "ECO_0000211"
    PROTEIN_BLAST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000211"

    # combinatorial evidence
    ECO_0000212 = "ECO_0000212"
    COMBINATORIAL_EVIDENCE = "ECO_0000212"

    # combinatorial evidence used in automatic assertion
    ECO_0000213 = "ECO_0000213"
    COMBINATORIAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000213"

    # biological aspect of descendant evidence
    ECO_0000214 = "ECO_0000214"
    BIOLOGICAL_ASPECT_OF_DESCENDANT_EVIDENCE = "ECO_0000214"

    # rapid divergence from ancestral sequence evidence
    ECO_0000215 = "ECO_0000215"
    RAPID_DIVERGENCE_FROM_ANCESTRAL_SEQUENCE_EVIDENCE = "ECO_0000215"

    # phylogenetic determination of loss of key residues evidence
    ECO_0000216 = "ECO_0000216"
    PHYLOGENETIC_DETERMINATION_OF_LOSS_OF_KEY_RESIDUES_EVIDENCE = "ECO_0000216"

    # assertion method
    ECO_0000217 = "ECO_0000217"
    ASSERTION_METHOD = "ECO_0000217"

    # manual assertion
    ECO_0000218 = "ECO_0000218"
    MANUAL_ASSERTION = "ECO_0000218"

    # nucleotide sequencing assay evidence
    ECO_0000219 = "ECO_0000219"
    NUCLEOTIDE_SEQUENCING_ASSAY_EVIDENCE = "ECO_0000219"

    # sequencing assay evidence
    ECO_0000220 = "ECO_0000220"
    SEQUENCING_ASSAY_EVIDENCE = "ECO_0000220"

    # high throughput nucleotide sequencing assay evidence
    ECO_0000221 = "ECO_0000221"
    HIGH_THROUGHPUT_NUCLEOTIDE_SEQUENCING_ASSAY_EVIDENCE = "ECO_0000221"

    # Illumina sequencing evidence
    ECO_0000222 = "ECO_0000222"
    ILLUMINA_SEQUENCING_EVIDENCE = "ECO_0000222"

    # 454 pyrosequencing evidence
    ECO_0000223 = "ECO_0000223"
    _454_PYROSEQUENCING_EVIDENCE = "ECO_0000223"

    # SOLiD sequencing evidence
    ECO_0000224 = "ECO_0000224"
    SOLID_SEQUENCING_EVIDENCE = "ECO_0000224"

    # chain termination sequencing evidence
    ECO_0000225 = "ECO_0000225"
    CHAIN_TERMINATION_SEQUENCING_EVIDENCE = "ECO_0000225"

    # chromatin immunoprecipitation evidence
    ECO_0000226 = "ECO_0000226"
    CHROMATIN_IMMUNOPRECIPITATION_EVIDENCE = "ECO_0000226"

    # chromatin immunoprecipitation-PCR evidence
    ECO_0000227 = "ECO_0000227"
    CHROMATIN_IMMUNOPRECIPITATION_PCR_EVIDENCE = "ECO_0000227"

    # chromatin immunoprecipitation-qPCR evidence
    ECO_0000228 = "ECO_0000228"
    CHROMATIN_IMMUNOPRECIPITATION_QPCR_EVIDENCE = "ECO_0000228"

    # chromatin immunoprecipitation-seq evidence
    ECO_0000229 = "ECO_0000229"
    CHROMATIN_IMMUNOPRECIPITATION_SEQ_EVIDENCE = "ECO_0000229"

    # chromatin immunoprecipitation-chip evidence
    ECO_0000230 = "ECO_0000230"
    CHROMATIN_IMMUNOPRECIPITATION_CHIP_EVIDENCE = "ECO_0000230"

    # quantitative polymerase chain reaction evidence
    ECO_0000231 = "ECO_0000231"
    QUANTITATIVE_POLYMERASE_CHAIN_REACTION_EVIDENCE = "ECO_0000231"

    # chromosome conformation-based evidence
    ECO_0000232 = "ECO_0000232"
    CHROMOSOME_CONFORMATION_BASED_EVIDENCE = "ECO_0000232"

    # 3C evidence
    ECO_0000233 = "ECO_0000233"
    _3C_EVIDENCE = "ECO_0000233"

    # 4C evidence
    ECO_0000234 = "ECO_0000234"
    _4C_EVIDENCE = "ECO_0000234"

    # 5C evidence
    ECO_0000235 = "ECO_0000235"
    _5C_EVIDENCE = "ECO_0000235"

    # chromosome conformation capture-PCR evidence
    ECO_0000236 = "ECO_0000236"
    CHROMOSOME_CONFORMATION_CAPTURE_PCR_EVIDENCE = "ECO_0000236"

    # 3C-qPCR evidence
    ECO_0000237 = "ECO_0000237"
    _3C_QPCR_EVIDENCE = "ECO_0000237"

    # Hi-C evidence
    ECO_0000238 = "ECO_0000238"
    HI_C_EVIDENCE = "ECO_0000238"

    # 3C-seq evidence
    ECO_0000239 = "ECO_0000239"
    _3C_SEQ_EVIDENCE = "ECO_0000239"

    # anatomical perturbation phenotypic evidence
    ECO_0000240 = "ECO_0000240"
    ANATOMICAL_PERTURBATION_PHENOTYPIC_EVIDENCE = "ECO_0000240"

    # environmental perturbation phenotypic evidence
    ECO_0000241 = "ECO_0000241"
    ENVIRONMENTAL_PERTURBATION_PHENOTYPIC_EVIDENCE = "ECO_0000241"

    # tissue ablation phenotypic evidence
    ECO_0000242 = "ECO_0000242"
    TISSUE_ABLATION_PHENOTYPIC_EVIDENCE = "ECO_0000242"

    # tissue grafting phenotypic evidence
    ECO_0000243 = "ECO_0000243"
    TISSUE_GRAFTING_PHENOTYPIC_EVIDENCE = "ECO_0000243"

    # combinatorial evidence used in manual assertion
    ECO_0000244 = "ECO_0000244"
    COMBINATORIAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000244"

    # automatically integrated combinatorial evidence used in manual assertion
    ECO_0000245 = "ECO_0000245"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000245"
    )

    # computational combinatorial evidence used in automatic assertion
    ECO_0000246 = "ECO_0000246"
    COMPUTATIONAL_COMBINATORIAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000246"

    # sequence alignment evidence used in manual assertion
    ECO_0000247 = "ECO_0000247"
    SEQUENCE_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000247"

    # sequence alignment evidence used in automatic assertion
    ECO_0000248 = "ECO_0000248"
    SEQUENCE_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000248"

    # sequence similarity evidence used in automatic assertion
    ECO_0000249 = "ECO_0000249"
    SEQUENCE_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000249"

    # sequence similarity evidence used in manual assertion
    ECO_0000250 = "ECO_0000250"
    SEQUENCE_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000250"

    # similarity evidence used in automatic assertion
    ECO_0000251 = "ECO_0000251"
    SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000251"

    # similarity evidence used in manual assertion
    ECO_0000252 = "ECO_0000252"
    SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000252"

    # genetic similarity evidence used in manual assertion
    ECO_0000253 = "ECO_0000253"
    GENETIC_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000253"

    # genetic similarity evidence used in automatic assertion
    ECO_0000254 = "ECO_0000254"
    GENETIC_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000254"

    # match to sequence model evidence used in manual assertion
    ECO_0000255 = "ECO_0000255"
    MATCH_TO_SEQUENCE_MODEL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000255"

    # match to sequence model evidence used in automatic assertion
    ECO_0000256 = "ECO_0000256"
    MATCH_TO_SEQUENCE_MODEL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000256"

    # motif similarity evidence used in manual assertion
    ECO_0000257 = "ECO_0000257"
    MOTIF_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000257"

    # motif similarity evidence used in automatic assertion
    ECO_0000258 = "ECO_0000258"
    MOTIF_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000258"

    # match to InterPro member signature evidence used in automatic assertion
    ECO_0000259 = "ECO_0000259"
    MATCH_TO_INTERPRO_MEMBER_SIGNATURE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000259"
    )

    # match to InterPro member signature evidence used in manual assertion
    ECO_0000260 = "ECO_0000260"
    MATCH_TO_INTERPRO_MEMBER_SIGNATURE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000260"

    # targeting sequence prediction evidence used in automatic assertion
    ECO_0000261 = "ECO_0000261"
    TARGETING_SEQUENCE_PREDICTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000261"

    # targeting sequence prediction evidence used in manual assertion
    ECO_0000262 = "ECO_0000262"
    TARGETING_SEQUENCE_PREDICTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000262"

    # transmembrane domain prediction evidence used in automatic assertion
    ECO_0000263 = "ECO_0000263"
    TRANSMEMBRANE_DOMAIN_PREDICTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000263"

    # transmembrane domain prediction evidence used in manual assertion
    ECO_0000264 = "ECO_0000264"
    TRANSMEMBRANE_DOMAIN_PREDICTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000264"

    # sequence orthology evidence used in automatic assertion
    ECO_0000265 = "ECO_0000265"
    SEQUENCE_ORTHOLOGY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000265"

    # sequence orthology evidence used in manual assertion
    ECO_0000266 = "ECO_0000266"
    SEQUENCE_ORTHOLOGY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000266"

    # enzyme-linked immunoabsorbent assay evidence
    ECO_0000267 = "ECO_0000267"
    ENZYME_LINKED_IMMUNOABSORBENT_ASSAY_EVIDENCE = "ECO_0000267"

    # flow cytometry evidence
    ECO_0000268 = "ECO_0000268"
    FLOW_CYTOMETRY_EVIDENCE = "ECO_0000268"

    # experimental evidence used in manual assertion
    ECO_0000269 = "ECO_0000269"
    EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000269"

    # expression pattern evidence used in manual assertion
    ECO_0000270 = "ECO_0000270"
    EXPRESSION_PATTERN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000270"

    # array experiment evidence used in manual assertion
    ECO_0000271 = "ECO_0000271"
    ARRAY_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000271"

    # Affymetrix GeneChip evidence used in manual assertion
    ECO_0000272 = "ECO_0000272"
    AFFYMETRIX_GENECHIP_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000272"

    # cDNA to DNA expression microarray evidence used in manual assertion
    ECO_0000273 = "ECO_0000273"
    CDNA_TO_DNA_EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000273"

    # differential methylation hybridization evidence used in manual assertion
    ECO_0000274 = "ECO_0000274"
    DIFFERENTIAL_METHYLATION_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000274"
    )

    # expression microarray evidence used in manual assertion
    ECO_0000275 = "ECO_0000275"
    EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000275"

    # cRNA to DNA expression microarray evidence used in manual assertion
    ECO_0000276 = "ECO_0000276"
    CRNA_TO_DNA_EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000276"

    # Nimblegen array evidence used in manual assertion
    ECO_0000277 = "ECO_0000277"
    NIMBLEGEN_ARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000277"

    # array-based sequence capture evidence used in manual assertion
    ECO_0000278 = "ECO_0000278"
    ARRAY_BASED_SEQUENCE_CAPTURE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000278"

    # qualitative western immunoblotting evidence used in manual assertion
    ECO_0000279 = "ECO_0000279"
    QUALITATIVE_WESTERN_IMMUNOBLOTTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000279"

    # expression library screen evidence used in manual assertion
    ECO_0000281 = "ECO_0000281"
    EXPRESSION_LIBRARY_SCREEN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000281"

    # heterologous protein expression evidence used in manual assertion
    ECO_0000282 = "ECO_0000282"
    HETEROLOGOUS_PROTEIN_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000282"

    # spatial pattern of protein expression evidence used in manual assertion
    ECO_0000283 = "ECO_0000283"
    SPATIAL_PATTERN_OF_PROTEIN_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000283"
    )

    # protein expression evidence used in manual assertion
    ECO_0000284 = "ECO_0000284"
    PROTEIN_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000284"

    # DNA to cDNA expression microarray evidence used in manual assertion
    ECO_0000285 = "ECO_0000285"
    DNA_TO_CDNA_EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000285"

    # differential hybridization evidence used in manual assertion
    ECO_0000287 = "ECO_0000287"
    DIFFERENTIAL_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000287"

    # RNA protection assay evidence used in manual assertion
    ECO_0000288 = "ECO_0000288"
    RNA_PROTECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000288"

    # spatial pattern of transcript expression evidence used in manual assertion
    ECO_0000289 = "ECO_0000289"
    SPATIAL_PATTERN_OF_TRANSCRIPT_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000289"
    )

    # subtractive hybridization evidence used in manual assertion
    ECO_0000290 = "ECO_0000290"
    SUBTRACTIVE_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000290"

    # transcript expression evidence used in manual assertion
    ECO_0000291 = "ECO_0000291"
    TRANSCRIPT_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000291"

    # morpholino experiment evidence
    ECO_0000292 = "ECO_0000292"
    MORPHOLINO_EXPERIMENT_EVIDENCE = "ECO_0000292"

    # systematic evolution of ligands by exponential amplification evidence
    ECO_0000293 = "ECO_0000293"
    SYSTEMATIC_EVOLUTION_OF_LIGANDS_BY_EXPONENTIAL_AMPLIFICATION_EVIDENCE = (
        "ECO_0000293"
    )

    # bacterial one-hybrid evidence
    ECO_0000294 = "ECO_0000294"
    BACTERIAL_ONE_HYBRID_EVIDENCE = "ECO_0000294"

    # RNA-sequencing evidence
    ECO_0000295 = "ECO_0000295"
    RNA_SEQUENCING_EVIDENCE = "ECO_0000295"

    # cleavage arrested development evidence
    ECO_0000298 = "ECO_0000298"
    CLEAVAGE_ARRESTED_DEVELOPMENT_EVIDENCE = "ECO_0000298"

    # cytochalasin experiment evidence
    ECO_0000299 = "ECO_0000299"
    CYTOCHALASIN_EXPERIMENT_EVIDENCE = "ECO_0000299"

    # green fluorescent protein immunolocalization evidence
    ECO_0000300 = "ECO_0000300"
    GREEN_FLUORESCENT_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE = "ECO_0000300"

    # beta-galactosidase protein immunolocalization evidence
    ECO_0000301 = "ECO_0000301"
    BETA_GALACTOSIDASE_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE = "ECO_0000301"

    # author statement used in manual assertion
    ECO_0000302 = "ECO_0000302"
    AUTHOR_STATEMENT_USED_IN_MANUAL_ASSERTION = "ECO_0000302"

    # author statement without traceable support used in manual assertion
    ECO_0000303 = "ECO_0000303"
    AUTHOR_STATEMENT_WITHOUT_TRACEABLE_SUPPORT_USED_IN_MANUAL_ASSERTION = "ECO_0000303"

    # author statement supported by traceable reference used in manual assertion
    ECO_0000304 = "ECO_0000304"
    AUTHOR_STATEMENT_SUPPORTED_BY_TRACEABLE_REFERENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000304"
    )

    # curator inference used in manual assertion
    ECO_0000305 = "ECO_0000305"
    CURATOR_INFERENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000305"

    # inference from background scientific knowledge used in manual assertion
    ECO_0000306 = "ECO_0000306"
    INFERENCE_FROM_BACKGROUND_SCIENTIFIC_KNOWLEDGE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000306"
    )

    # no evidence data found used in manual assertion
    ECO_0000307 = "ECO_0000307"
    NO_EVIDENCE_DATA_FOUND_USED_IN_MANUAL_ASSERTION = "ECO_0000307"

    # biological aspect of ancestor evidence
    ECO_0000308 = "ECO_0000308"
    BIOLOGICAL_ASPECT_OF_ANCESTOR_EVIDENCE = "ECO_0000308"

    # cap analysis of gene expression evidence
    ECO_0000309 = "ECO_0000309"
    CAP_ANALYSIS_OF_GENE_EXPRESSION_EVIDENCE = "ECO_0000309"

    # nano-cap analysis of gene expression evidence
    ECO_0000310 = "ECO_0000310"
    NANO_CAP_ANALYSIS_OF_GENE_EXPRESSION_EVIDENCE = "ECO_0000310"

    # imported information
    ECO_0000311 = "ECO_0000311"
    IMPORTED_INFORMATION = "ECO_0000311"

    # imported information used in manual assertion
    ECO_0000312 = "ECO_0000312"
    IMPORTED_INFORMATION_USED_IN_MANUAL_ASSERTION = "ECO_0000312"

    # imported information used in automatic assertion
    ECO_0000313 = "ECO_0000313"
    IMPORTED_INFORMATION_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000313"

    # direct assay evidence used in manual assertion
    ECO_0000314 = "ECO_0000314"
    DIRECT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000314"

    # mutant phenotype evidence used in manual assertion
    ECO_0000315 = "ECO_0000315"
    MUTANT_PHENOTYPE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000315"

    # genetic interaction evidence used in manual assertion
    ECO_0000316 = "ECO_0000316"
    GENETIC_INTERACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000316"

    # genomic context evidence used in manual assertion
    ECO_0000317 = "ECO_0000317"
    GENOMIC_CONTEXT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000317"

    # biological aspect of ancestor evidence used in manual assertion
    ECO_0000318 = "ECO_0000318"
    BIOLOGICAL_ASPECT_OF_ANCESTOR_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000318"

    # biological aspect of descendant evidence used in manual assertion
    ECO_0000319 = "ECO_0000319"
    BIOLOGICAL_ASPECT_OF_DESCENDANT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000319"

    # phylogenetic determination of loss of key residues evidence used in manual assertion
    ECO_0000320 = "ECO_0000320"
    PHYLOGENETIC_DETERMINATION_OF_LOSS_OF_KEY_RESIDUES_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000320"
    )

    # rapid divergence from ancestral sequence evidence used in manual assertion
    ECO_0000321 = "ECO_0000321"
    RAPID_DIVERGENCE_FROM_ANCESTRAL_SEQUENCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000321"
    )

    # imported manually asserted information used in automatic assertion
    ECO_0000322 = "ECO_0000322"
    IMPORTED_MANUALLY_ASSERTED_INFORMATION_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000322"

    # imported automatically asserted information used in automatic assertion
    ECO_0000323 = "ECO_0000323"
    IMPORTED_AUTOMATICALLY_ASSERTED_INFORMATION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000323"
    )

    # imaging assay evidence
    ECO_0000324 = "ECO_0000324"
    IMAGING_ASSAY_EVIDENCE = "ECO_0000324"

    # chromatography evidence
    ECO_0000325 = "ECO_0000325"
    CHROMATOGRAPHY_EVIDENCE = "ECO_0000325"

    # transcript splice pattern evidence
    ECO_0000326 = "ECO_0000326"
    TRANSCRIPT_SPLICE_PATTERN_EVIDENCE = "ECO_0000326"

    # whole transcript splice pattern evidence
    ECO_0000327 = "ECO_0000327"
    WHOLE_TRANSCRIPT_SPLICE_PATTERN_EVIDENCE = "ECO_0000327"

    # coding sequence splice pattern evidence
    ECO_0000328 = "ECO_0000328"
    CODING_SEQUENCE_SPLICE_PATTERN_EVIDENCE = "ECO_0000328"

    # whole transcript splice pattern evidence used in manual assertion
    ECO_0000329 = "ECO_0000329"
    WHOLE_TRANSCRIPT_SPLICE_PATTERN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000329"

    # coding sequence splice pattern evidence used in manual assertion
    ECO_0000330 = "ECO_0000330"
    CODING_SEQUENCE_SPLICE_PATTERN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000330"

    # coding sequence splice pattern evidence used in automatic assertion
    ECO_0000331 = "ECO_0000331"
    CODING_SEQUENCE_SPLICE_PATTERN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000331"

    # whole transcript splice pattern evidence used in automatic assertion
    ECO_0000332 = "ECO_0000332"
    WHOLE_TRANSCRIPT_SPLICE_PATTERN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000332"

    # sodium dodecyl sulfate polyacrylamide gel electrophoresis evidence
    ECO_0000333 = "ECO_0000333"
    SODIUM_DODECYL_SULFATE_POLYACRYLAMIDE_GEL_ELECTROPHORESIS_EVIDENCE = "ECO_0000333"

    # particle size and count assay evidence
    ECO_0000334 = "ECO_0000334"
    PARTICLE_SIZE_AND_COUNT_ASSAY_EVIDENCE = "ECO_0000334"

    # substance quantification evidence
    ECO_0000335 = "ECO_0000335"
    SUBSTANCE_QUANTIFICATION_EVIDENCE = "ECO_0000335"

    # competitive growth assay evidence
    ECO_0000336 = "ECO_0000336"
    COMPETITIVE_GROWTH_ASSAY_EVIDENCE = "ECO_0000336"

    # gel electrophoresis evidence
    ECO_0000337 = "ECO_0000337"
    GEL_ELECTROPHORESIS_EVIDENCE = "ECO_0000337"

    # pulsed-field gel electrophoresis evidence
    ECO_0000338 = "ECO_0000338"
    PULSED_FIELD_GEL_ELECTROPHORESIS_EVIDENCE = "ECO_0000338"

    # two-dimensional agarose gel electrophoresis evidence
    ECO_0000339 = "ECO_0000339"
    TWO_DIMENSIONAL_AGAROSE_GEL_ELECTROPHORESIS_EVIDENCE = "ECO_0000339"

    # plasmid maintenance assay evidence
    ECO_0000340 = "ECO_0000340"
    PLASMID_MAINTENANCE_ASSAY_EVIDENCE = "ECO_0000340"

    # specific protein inhibition by antibody evidence
    ECO_0000341 = "ECO_0000341"
    SPECIFIC_PROTEIN_INHIBITION_BY_ANTIBODY_EVIDENCE = "ECO_0000341"

    # support of intron positions by RNA-sequencing alignment evidence
    ECO_0000342 = "ECO_0000342"
    SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE = "ECO_0000342"

    # full support of intron positions by RNA-sequencing alignment evidence
    ECO_0000343 = "ECO_0000343"
    FULL_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE = (
        "ECO_0000343"
    )

    # partial support of intron positions by RNA-sequencing alignment evidence
    ECO_0000344 = "ECO_0000344"
    PARTIAL_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE = (
        "ECO_0000344"
    )

    # single exon transcript confirmation via alignment evidence
    ECO_0000345 = "ECO_0000345"
    SINGLE_EXON_TRANSCRIPT_CONFIRMATION_VIA_ALIGNMENT_EVIDENCE = "ECO_0000345"

    # support of intron positions by RNA-sequencing alignment evidence used in manual assertion
    ECO_0000346 = "ECO_0000346"
    SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000346"
    )

    # support of intron positions by RNA-sequencing alignment evidence used in automatic assertion
    ECO_0000347 = "ECO_0000347"
    SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000347"
    )

    # full support of intron positions by RNA-sequencing alignment evidence used in automatic assertion
    ECO_0000348 = "ECO_0000348"
    FULL_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000348"
    )

    # full support of intron positions by RNA-sequencing alignment evidence used in manual assertion
    ECO_0000349 = "ECO_0000349"
    FULL_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000349"
    )

    # partial support of intron positions by RNA-sequencing alignment evidence used in automatic assertion
    ECO_0000350 = "ECO_0000350"
    PARTIAL_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000350"
    )

    # partial support of intron positions by RNA-sequencing alignment evidence used in manual assertion
    ECO_0000351 = "ECO_0000351"
    PARTIAL_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0000351"
    )

    # evidence used in manual assertion
    ECO_0000352 = "ECO_0000352"
    EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000352"

    # physical interaction evidence used in manual assertion
    ECO_0000353 = "ECO_0000353"
    PHYSICAL_INTERACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000353"

    # gene neighbors evidence used in manual assertion
    ECO_0000354 = "ECO_0000354"
    GENE_NEIGHBORS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0000354"

    # phylogenetic distribution evidence
    ECO_0000355 = "ECO_0000355"
    PHYLOGENETIC_DISTRIBUTION_EVIDENCE = "ECO_0000355"

    # differential geneset expression evidence from microarray experiment (GSEA, Fisher-exact)
    ECO_0000358 = "ECO_0000358"
    DIFFERENTIAL_GENESET_EXPRESSION_EVIDENCE_FROM_MICROARRAY_EXPERIMENT__GSEA__FISHER_EXACT_ = (
        "ECO_0000358"
    )

    # differential geneset expression evidence from RNA-seq experiment (GSEA, Fisher-exact)
    ECO_0000359 = "ECO_0000359"
    DIFFERENTIAL_GENESET_EXPRESSION_EVIDENCE_FROM_RNA_SEQ_EXPERIMENT__GSEA__FISHER_EXACT_ = (
        "ECO_0000359"
    )

    # biological target-disease association via drug evidence
    ECO_0000360 = "ECO_0000360"
    BIOLOGICAL_TARGET_DISEASE_ASSOCIATION_VIA_DRUG_EVIDENCE = "ECO_0000360"

    # inferential evidence
    ECO_0000361 = "ECO_0000361"
    INFERENTIAL_EVIDENCE = "ECO_0000361"

    # computational inference
    ECO_0000362 = "ECO_0000362"
    COMPUTATIONAL_INFERENCE = "ECO_0000362"

    # computational inference used in automatic assertion
    ECO_0000363 = "ECO_0000363"
    COMPUTATIONAL_INFERENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000363"

    # evidence based on logical inference from manual annotation used in automatic assertion
    ECO_0000364 = "ECO_0000364"
    EVIDENCE_BASED_ON_LOGICAL_INFERENCE_FROM_MANUAL_ANNOTATION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000364"
    )

    # evidence based on logical inference from automatic annotation used in automatic assertion
    ECO_0000366 = "ECO_0000366"
    EVIDENCE_BASED_ON_LOGICAL_INFERENCE_FROM_AUTOMATIC_ANNOTATION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0000366"
    )

    # evidence used in automatic assertion
    ECO_0000501 = "ECO_0000501"
    EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0000501"

    # 3D cell culture evidence
    ECO_0001001 = "ECO_0001001"
    _3D_CELL_CULTURE_EVIDENCE = "ECO_0001001"

    # [3H]arachidonic acid release assay evidence
    ECO_0001002 = "ECO_0001002"
    _3H_ARACHIDONIC_ACID_RELEASE_ASSAY_EVIDENCE = "ECO_0001002"

    # [3H]-thymidine incorporation assay evidence
    ECO_0001003 = "ECO_0001003"
    _3H__THYMIDINE_INCORPORATION_ASSAY_EVIDENCE = "ECO_0001003"

    # 51Cr release assay evidence
    ECO_0001004 = "ECO_0001004"
    _51CR_RELEASE_ASSAY_EVIDENCE = "ECO_0001004"

    # 7-aminoactinomycin staining evidence
    ECO_0001005 = "ECO_0001005"
    _7_AMINOACTINOMYCIN_STAINING_EVIDENCE = "ECO_0001005"

    # adhesion assay evidence
    ECO_0001006 = "ECO_0001006"
    ADHESION_ASSAY_EVIDENCE = "ECO_0001006"

    # adoptive cell transfer evidence
    ECO_0001007 = "ECO_0001007"
    ADOPTIVE_CELL_TRANSFER_EVIDENCE = "ECO_0001007"

    # alamarBlue assay evidence
    ECO_0001008 = "ECO_0001008"
    ALAMARBLUE_ASSAY_EVIDENCE = "ECO_0001008"

    # allograft transplantation phenotypic evidence
    ECO_0001009 = "ECO_0001009"
    ALLOGRAFT_TRANSPLANTATION_PHENOTYPIC_EVIDENCE = "ECO_0001009"

    # anion-exchange chromatography evidence
    ECO_0001010 = "ECO_0001010"
    ANION_EXCHANGE_CHROMATOGRAPHY_EVIDENCE = "ECO_0001010"

    # annexin-V staining evidence
    ECO_0001011 = "ECO_0001011"
    ANNEXIN_V_STAINING_EVIDENCE = "ECO_0001011"

    # cognitive assay phenotypic evidence
    ECO_0001012 = "ECO_0001012"
    COGNITIVE_ASSAY_PHENOTYPIC_EVIDENCE = "ECO_0001012"

    # blocking monoclonal antibody evidence
    ECO_0001013 = "ECO_0001013"
    BLOCKING_MONOCLONAL_ANTIBODY_EVIDENCE = "ECO_0001013"

    # blocking peptide evidence
    ECO_0001014 = "ECO_0001014"
    BLOCKING_PEPTIDE_EVIDENCE = "ECO_0001014"

    # blocking polyclonal antibody evidence
    ECO_0001015 = "ECO_0001015"
    BLOCKING_POLYCLONAL_ANTIBODY_EVIDENCE = "ECO_0001015"

    # blood test evidence
    ECO_0001016 = "ECO_0001016"
    BLOOD_TEST_EVIDENCE = "ECO_0001016"

    # Boyden chamber assay evidence
    ECO_0001017 = "ECO_0001017"
    BOYDEN_CHAMBER_ASSAY_EVIDENCE = "ECO_0001017"

    # bromodeoxyuridine incorporation assay evidence
    ECO_0001018 = "ECO_0001018"
    BROMODEOXYURIDINE_INCORPORATION_ASSAY_EVIDENCE = "ECO_0001018"

    # caspase assay evidence
    ECO_0001019 = "ECO_0001019"
    CASPASE_ASSAY_EVIDENCE = "ECO_0001019"

    # cell counting evidence
    ECO_0001020 = "ECO_0001020"
    CELL_COUNTING_EVIDENCE = "ECO_0001020"

    # cell permeability assay evidence
    ECO_0001021 = "ECO_0001021"
    CELL_PERMEABILITY_ASSAY_EVIDENCE = "ECO_0001021"

    # carboxyfluorescein diacetate succinimidyl ester staining evidence
    ECO_0001022 = "ECO_0001022"
    CARBOXYFLUORESCEIN_DIACETATE_SUCCINIMIDYL_ESTER_STAINING_EVIDENCE = "ECO_0001022"

    # chemiluminescence-linked immunoassay evidence
    ECO_0001023 = "ECO_0001023"
    CHEMILUMINESCENCE_LINKED_IMMUNOASSAY_EVIDENCE = "ECO_0001023"

    # chimeric protein phenotypic evidence
    ECO_0001024 = "ECO_0001024"
    CHIMERIC_PROTEIN_PHENOTYPIC_EVIDENCE = "ECO_0001024"

    # co-electrophoresis evidence
    ECO_0001025 = "ECO_0001025"
    CO_ELECTROPHORESIS_EVIDENCE = "ECO_0001025"

    # co-localization evidence
    ECO_0001026 = "ECO_0001026"
    CO_LOCALIZATION_EVIDENCE = "ECO_0001026"

    # colony counting evidence
    ECO_0001027 = "ECO_0001027"
    COLONY_COUNTING_EVIDENCE = "ECO_0001027"

    # co-sedimentation assay evidence
    ECO_0001028 = "ECO_0001028"
    CO_SEDIMENTATION_ASSAY_EVIDENCE = "ECO_0001028"

    # comet assay evidence
    ECO_0001029 = "ECO_0001029"
    COMET_ASSAY_EVIDENCE = "ECO_0001029"

    # conditional knockout evidence
    ECO_0001030 = "ECO_0001030"
    CONDITIONAL_KNOCKOUT_EVIDENCE = "ECO_0001030"

    # conditional knockin evidence
    ECO_0001031 = "ECO_0001031"
    CONDITIONAL_KNOCKIN_EVIDENCE = "ECO_0001031"

    # constitutively active mutant evidence
    ECO_0001032 = "ECO_0001032"
    CONSTITUTIVELY_ACTIVE_MUTANT_EVIDENCE = "ECO_0001032"

    # cross-linking evidence
    ECO_0001033 = "ECO_0001033"
    CROSS_LINKING_EVIDENCE = "ECO_0001033"

    # crystallography evidence
    ECO_0001034 = "ECO_0001034"
    CRYSTALLOGRAPHY_EVIDENCE = "ECO_0001034"

    # cytochemistry evidence
    ECO_0001035 = "ECO_0001035"
    CYTOCHEMISTRY_EVIDENCE = "ECO_0001035"

    # cytochrome C release assay evidence
    ECO_0001036 = "ECO_0001036"
    CYTOCHROME_C_RELEASE_ASSAY_EVIDENCE = "ECO_0001036"

    # 4',6-diamidino-2-phenylindole staining evidence
    ECO_0001037 = "ECO_0001037"
    _4__6_DIAMIDINO_2_PHENYLINDOLE_STAINING_EVIDENCE = "ECO_0001037"

    # deletion mutation phenotypic evidence
    ECO_0001038 = "ECO_0001038"
    DELETION_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0001038"

    # DNA laddering assay evidence
    ECO_0001039 = "ECO_0001039"
    DNA_LADDERING_ASSAY_EVIDENCE = "ECO_0001039"

    # RNA dot blot assay evidence
    ECO_0001040 = "ECO_0001040"
    RNA_DOT_BLOT_ASSAY_EVIDENCE = "ECO_0001040"

    # dominant-negative mutant phenotypic evidence
    ECO_0001042 = "ECO_0001042"
    DOMINANT_NEGATIVE_MUTANT_PHENOTYPIC_EVIDENCE = "ECO_0001042"

    # Edman degradation evidence used in manual assertion
    ECO_0001043 = "ECO_0001043"
    EDMAN_DEGRADATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001043"

    # Edman degradation evidence
    ECO_0001044 = "ECO_0001044"
    EDMAN_DEGRADATION_EVIDENCE = "ECO_0001044"

    # eTag assay evidence
    ECO_0001045 = "ECO_0001045"
    ETAG_ASSAY_EVIDENCE = "ECO_0001045"

    # filter binding assay evidence
    ECO_0001046 = "ECO_0001046"
    FILTER_BINDING_ASSAY_EVIDENCE = "ECO_0001046"

    # fluorescence in situ hybridization evidence
    ECO_0001047 = "ECO_0001047"
    FLUORESCENCE_IN_SITU_HYBRIDIZATION_EVIDENCE = "ECO_0001047"

    # fluorescence resonance energy transfer evidence
    ECO_0001048 = "ECO_0001048"
    FLUORESCENCE_RESONANCE_ENERGY_TRANSFER_EVIDENCE = "ECO_0001048"

    # gel-filtration evidence
    ECO_0001049 = "ECO_0001049"
    GEL_FILTRATION_EVIDENCE = "ECO_0001049"

    # histochemistry evidence
    ECO_0001050 = "ECO_0001050"
    HISTOCHEMISTRY_EVIDENCE = "ECO_0001050"

    # histology evidence
    ECO_0001051 = "ECO_0001051"
    HISTOLOGY_EVIDENCE = "ECO_0001051"

    # high-performance liquid chromatography evidence
    ECO_0001052 = "ECO_0001052"
    HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY_EVIDENCE = "ECO_0001052"

    # immunocytochemistry evidence
    ECO_0001053 = "ECO_0001053"
    IMMUNOCYTOCHEMISTRY_EVIDENCE = "ECO_0001053"

    # immunodepletion evidence
    ECO_0001054 = "ECO_0001054"
    IMMUNODEPLETION_EVIDENCE = "ECO_0001054"

    # immunohistochemistry evidence
    ECO_0001055 = "ECO_0001055"
    IMMUNOHISTOCHEMISTRY_EVIDENCE = "ECO_0001055"

    # induced mutation evidence
    ECO_0001056 = "ECO_0001056"
    INDUCED_MUTATION_EVIDENCE = "ECO_0001056"

    # in vitro acetylation assay evidence
    ECO_0001057 = "ECO_0001057"
    IN_VITRO_ACETYLATION_ASSAY_EVIDENCE = "ECO_0001057"

    # in vitro cleavage assay evidence
    ECO_0001058 = "ECO_0001058"
    IN_VITRO_CLEAVAGE_ASSAY_EVIDENCE = "ECO_0001058"

    # in vitro deubiquitination assay evidence
    ECO_0001059 = "ECO_0001059"
    IN_VITRO_DEUBIQUITINATION_ASSAY_EVIDENCE = "ECO_0001059"

    # in vitro deacetylation assay evidence
    ECO_0001060 = "ECO_0001060"
    IN_VITRO_DEACETYLATION_ASSAY_EVIDENCE = "ECO_0001060"

    # in vitro defarnesylation assay evidence
    ECO_0001061 = "ECO_0001061"
    IN_VITRO_DEFARNESYLATION_ASSAY_EVIDENCE = "ECO_0001061"

    # in vitro demethylation assay evidence
    ECO_0001062 = "ECO_0001062"
    IN_VITRO_DEMETHYLATION_ASSAY_EVIDENCE = "ECO_0001062"

    # in vitro desumoylation assay evidence
    ECO_0001063 = "ECO_0001063"
    IN_VITRO_DESUMOYLATION_ASSAY_EVIDENCE = "ECO_0001063"

    # in vitro farnesylation assay evidence
    ECO_0001064 = "ECO_0001064"
    IN_VITRO_FARNESYLATION_ASSAY_EVIDENCE = "ECO_0001064"

    # in vitro methylation assay evidence
    ECO_0001065 = "ECO_0001065"
    IN_VITRO_METHYLATION_ASSAY_EVIDENCE = "ECO_0001065"

    # in vitro palmitoylation assay evidence
    ECO_0001066 = "ECO_0001066"
    IN_VITRO_PALMITOYLATION_ASSAY_EVIDENCE = "ECO_0001066"

    # in vitro phosphatase assay evidence
    ECO_0001067 = "ECO_0001067"
    IN_VITRO_PHOSPHATASE_ASSAY_EVIDENCE = "ECO_0001067"

    # in vitro protein kinase assay evidence
    ECO_0001068 = "ECO_0001068"
    IN_VITRO_PROTEIN_KINASE_ASSAY_EVIDENCE = "ECO_0001068"

    # in vitro polyADP-ribosylation assay evidence
    ECO_0001069 = "ECO_0001069"
    IN_VITRO_POLYADP_RIBOSYLATION_ASSAY_EVIDENCE = "ECO_0001069"

    # in vitro sumoylation assay evidence
    ECO_0001070 = "ECO_0001070"
    IN_VITRO_SUMOYLATION_ASSAY_EVIDENCE = "ECO_0001070"

    # in vitro transcription assay evidence
    ECO_0001071 = "ECO_0001071"
    IN_VITRO_TRANSCRIPTION_ASSAY_EVIDENCE = "ECO_0001071"

    # in vitro translation assay evidence
    ECO_0001072 = "ECO_0001072"
    IN_VITRO_TRANSLATION_ASSAY_EVIDENCE = "ECO_0001072"

    # in vitro ubiquitination assay evidence
    ECO_0001073 = "ECO_0001073"
    IN_VITRO_UBIQUITINATION_ASSAY_EVIDENCE = "ECO_0001073"

    # in vivo acetylation assay evidence
    ECO_0001074 = "ECO_0001074"
    IN_VIVO_ACETYLATION_ASSAY_EVIDENCE = "ECO_0001074"

    # in vivo cleavage assay evidence
    ECO_0001075 = "ECO_0001075"
    IN_VIVO_CLEAVAGE_ASSAY_EVIDENCE = "ECO_0001075"

    # in vivo deacetylation assay evidence
    ECO_0001076 = "ECO_0001076"
    IN_VIVO_DEACETYLATION_ASSAY_EVIDENCE = "ECO_0001076"

    # in vivo defarnesylation assay evidence
    ECO_0001077 = "ECO_0001077"
    IN_VIVO_DEFARNESYLATION_ASSAY_EVIDENCE = "ECO_0001077"

    # in vivo demethylation assay evidence
    ECO_0001078 = "ECO_0001078"
    IN_VIVO_DEMETHYLATION_ASSAY_EVIDENCE = "ECO_0001078"

    # in vivo deubiquitination assay evidence
    ECO_0001079 = "ECO_0001079"
    IN_VIVO_DEUBIQUITINATION_ASSAY_EVIDENCE = "ECO_0001079"

    # in vivo desumoylation assay evidence
    ECO_0001080 = "ECO_0001080"
    IN_VIVO_DESUMOYLATION_ASSAY_EVIDENCE = "ECO_0001080"

    # in vivo farnesylation assay evidence
    ECO_0001081 = "ECO_0001081"
    IN_VIVO_FARNESYLATION_ASSAY_EVIDENCE = "ECO_0001081"

    # in vivo methylation assay evidence
    ECO_0001082 = "ECO_0001082"
    IN_VIVO_METHYLATION_ASSAY_EVIDENCE = "ECO_0001082"

    # in vivo palmitoylation assay evidence
    ECO_0001083 = "ECO_0001083"
    IN_VIVO_PALMITOYLATION_ASSAY_EVIDENCE = "ECO_0001083"

    # in vivo phosphatase assay evidence
    ECO_0001084 = "ECO_0001084"
    IN_VIVO_PHOSPHATASE_ASSAY_EVIDENCE = "ECO_0001084"

    # in vivo protein kinase assay evidence
    ECO_0001085 = "ECO_0001085"
    IN_VIVO_PROTEIN_KINASE_ASSAY_EVIDENCE = "ECO_0001085"

    # in vivo sumoylation assay evidence
    ECO_0001086 = "ECO_0001086"
    IN_VIVO_SUMOYLATION_ASSAY_EVIDENCE = "ECO_0001086"

    # in vivo transcription assay evidence
    ECO_0001087 = "ECO_0001087"
    IN_VIVO_TRANSCRIPTION_ASSAY_EVIDENCE = "ECO_0001087"

    # in vivo translation assay evidence
    ECO_0001088 = "ECO_0001088"
    IN_VIVO_TRANSLATION_ASSAY_EVIDENCE = "ECO_0001088"

    # in vivo ubiquitination assay evidence
    ECO_0001089 = "ECO_0001089"
    IN_VIVO_UBIQUITINATION_ASSAY_EVIDENCE = "ECO_0001089"

    # knockin evidence
    ECO_0001090 = "ECO_0001090"
    KNOCKIN_EVIDENCE = "ECO_0001090"

    # knockout phenotypic evidence
    ECO_0001091 = "ECO_0001091"
    KNOCKOUT_PHENOTYPIC_EVIDENCE = "ECO_0001091"

    # lipid binding assay evidence
    ECO_0001092 = "ECO_0001092"
    LIPID_BINDING_ASSAY_EVIDENCE = "ECO_0001092"

    # luminescence-based mammalian interactome mapping assay evidence
    ECO_0001093 = "ECO_0001093"
    LUMINESCENCE_BASED_MAMMALIAN_INTERACTOME_MAPPING_ASSAY_EVIDENCE = "ECO_0001093"

    # macroscopy evidence
    ECO_0001094 = "ECO_0001094"
    MACROSCOPY_EVIDENCE = "ECO_0001094"

    # mammalian 2-hybrid assay evidence
    ECO_0001095 = "ECO_0001095"
    MAMMALIAN_2_HYBRID_ASSAY_EVIDENCE = "ECO_0001095"

    # mass spectrometry evidence
    ECO_0001096 = "ECO_0001096"
    MASS_SPECTROMETRY_EVIDENCE = "ECO_0001096"

    # medical imaging evidence
    ECO_0001097 = "ECO_0001097"
    MEDICAL_IMAGING_EVIDENCE = "ECO_0001097"

    # microscopy evidence
    ECO_0001098 = "ECO_0001098"
    MICROSCOPY_EVIDENCE = "ECO_0001098"

    # motility wound healing assay evidence
    ECO_0001099 = "ECO_0001099"
    MOTILITY_WOUND_HEALING_ASSAY_EVIDENCE = "ECO_0001099"

    # MTS assay evidence
    ECO_0001100 = "ECO_0001100"
    MTS_ASSAY_EVIDENCE = "ECO_0001100"

    # MTT assay evidence
    ECO_0001101 = "ECO_0001101"
    MTT_ASSAY_EVIDENCE = "ECO_0001101"

    # multiplex bead-based immunoassay evidence
    ECO_0001102 = "ECO_0001102"
    MULTIPLEX_BEAD_BASED_IMMUNOASSAY_EVIDENCE = "ECO_0001102"

    # natural variation mutant evidence
    ECO_0001103 = "ECO_0001103"
    NATURAL_VARIATION_MUTANT_EVIDENCE = "ECO_0001103"

    # nuclear fragmentation evidence
    ECO_0001104 = "ECO_0001104"
    NUCLEAR_FRAGMENTATION_EVIDENCE = "ECO_0001104"

    # nuclear magnetic resonance evidence
    ECO_0001105 = "ECO_0001105"
    NUCLEAR_MAGNETIC_RESONANCE_EVIDENCE = "ECO_0001105"

    # nuclease protection assay evidence
    ECO_0001106 = "ECO_0001106"
    NUCLEASE_PROTECTION_ASSAY_EVIDENCE = "ECO_0001106"

    # nucleotide analog incorporation assay evidence
    ECO_0001107 = "ECO_0001107"
    NUCLEOTIDE_ANALOG_INCORPORATION_ASSAY_EVIDENCE = "ECO_0001107"

    # phage display evidence
    ECO_0001108 = "ECO_0001108"
    PHAGE_DISPLAY_EVIDENCE = "ECO_0001108"

    # phosphoamino acid analysis evidence
    ECO_0001109 = "ECO_0001109"
    PHOSPHOAMINO_ACID_ANALYSIS_EVIDENCE = "ECO_0001109"

    # peptide affinity enrichment evidence
    ECO_0001110 = "ECO_0001110"
    PEPTIDE_AFFINITY_ENRICHMENT_EVIDENCE = "ECO_0001110"

    # physical examination evidence
    ECO_0001111 = "ECO_0001111"
    PHYSICAL_EXAMINATION_EVIDENCE = "ECO_0001111"

    # peptide array evidence
    ECO_0001112 = "ECO_0001112"
    PEPTIDE_ARRAY_EVIDENCE = "ECO_0001112"

    # point mutation phenotypic evidence
    ECO_0001113 = "ECO_0001113"
    POINT_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0001113"

    # propidium iodide staining evidence
    ECO_0001114 = "ECO_0001114"
    PROPIDIUM_IODIDE_STAINING_EVIDENCE = "ECO_0001114"

    # fluorescence evidence
    ECO_0001115 = "ECO_0001115"
    FLUORESCENCE_EVIDENCE = "ECO_0001115"

    # protein dot blot assay evidence
    ECO_0001116 = "ECO_0001116"
    PROTEIN_DOT_BLOT_ASSAY_EVIDENCE = "ECO_0001116"

    # protein microarray evidence
    ECO_0001117 = "ECO_0001117"
    PROTEIN_MICROARRAY_EVIDENCE = "ECO_0001117"

    # protein sequencing assay evidence
    ECO_0001118 = "ECO_0001118"
    PROTEIN_SEQUENCING_ASSAY_EVIDENCE = "ECO_0001118"

    # quantitative mass spectrometry evidence
    ECO_0001119 = "ECO_0001119"
    QUANTITATIVE_MASS_SPECTROMETRY_EVIDENCE = "ECO_0001119"

    # radioisotope assay evidence
    ECO_0001120 = "ECO_0001120"
    RADIOISOTOPE_ASSAY_EVIDENCE = "ECO_0001120"

    # radioimmunoassay evidence
    ECO_0001121 = "ECO_0001121"
    RADIOIMMUNOASSAY_EVIDENCE = "ECO_0001121"

    # resonant mirror biosensor evidence
    ECO_0001123 = "ECO_0001123"
    RESONANT_MIRROR_BIOSENSOR_EVIDENCE = "ECO_0001123"

    # restriction fragment detection evidence
    ECO_0001124 = "ECO_0001124"
    RESTRICTION_FRAGMENT_DETECTION_EVIDENCE = "ECO_0001124"

    # spectrophotometry evidence
    ECO_0001126 = "ECO_0001126"
    SPECTROPHOTOMETRY_EVIDENCE = "ECO_0001126"

    # surface plasmon resonance evidence
    ECO_0001127 = "ECO_0001127"
    SURFACE_PLASMON_RESONANCE_EVIDENCE = "ECO_0001127"

    # syngeneic transplantation experiment evidence
    ECO_0001128 = "ECO_0001128"
    SYNGENEIC_TRANSPLANTATION_EXPERIMENT_EVIDENCE = "ECO_0001128"

    # TACE activity assay evidence
    ECO_0001129 = "ECO_0001129"
    TACE_ACTIVITY_ASSAY_EVIDENCE = "ECO_0001129"

    # tissue microarray evidence
    ECO_0001130 = "ECO_0001130"
    TISSUE_MICROARRAY_EVIDENCE = "ECO_0001130"

    # transgenic organism evidence
    ECO_0001131 = "ECO_0001131"
    TRANSGENIC_ORGANISM_EVIDENCE = "ECO_0001131"

    # tryptic phosphopeptide mapping assay evidence
    ECO_0001132 = "ECO_0001132"
    TRYPTIC_PHOSPHOPEPTIDE_MAPPING_ASSAY_EVIDENCE = "ECO_0001132"

    # terminal deoxynucleotidyl transferase dUTP nick end labeling assay evidence
    ECO_0001133 = "ECO_0001133"
    TERMINAL_DEOXYNUCLEOTIDYL_TRANSFERASE_DUTP_NICK_END_LABELING_ASSAY_EVIDENCE = (
        "ECO_0001133"
    )

    # urine test evidence
    ECO_0001134 = "ECO_0001134"
    URINE_TEST_EVIDENCE = "ECO_0001134"

    # WST-1 assay evidence
    ECO_0001136 = "ECO_0001136"
    WST_1_ASSAY_EVIDENCE = "ECO_0001136"

    # xenotransplantation phenotypic evidence
    ECO_0001137 = "ECO_0001137"
    XENOTRANSPLANTATION_PHENOTYPIC_EVIDENCE = "ECO_0001137"

    # 3D cell culture evidence used in manual assertion
    ECO_0001138 = "ECO_0001138"
    _3D_CELL_CULTURE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001138"

    # 51Cr release assay evidence used in manual assertion
    ECO_0001139 = "ECO_0001139"
    _51CR_RELEASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001139"

    # 7-aminoactinomycin staining evidence used in manual assertion
    ECO_0001140 = "ECO_0001140"
    _7_AMINOACTINOMYCIN_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001140"

    # [3H]-thymidine incorporation assay evidence used in manual assertion
    ECO_0001141 = "ECO_0001141"
    _3H__THYMIDINE_INCORPORATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001141"

    # [3H]arachidonic acid release assay evidence used in manual assertion
    ECO_0001142 = "ECO_0001142"
    _3H_ARACHIDONIC_ACID_RELEASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001142"

    # adhesion assay evidence used in manual assertion
    ECO_0001143 = "ECO_0001143"
    ADHESION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001143"

    # adoptive cell transfer evidence used in manual assertion
    ECO_0001144 = "ECO_0001144"
    ADOPTIVE_CELL_TRANSFER_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001144"

    # alamarBlue assay evidence used in manual assertion
    ECO_0001145 = "ECO_0001145"
    ALAMARBLUE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001145"

    # allograft transplantation phenotypic evidence used in manual assertion
    ECO_0001146 = "ECO_0001146"
    ALLOGRAFT_TRANSPLANTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001146"
    )

    # anion-exchange chromatography evidence used in manual assertion
    ECO_0001147 = "ECO_0001147"
    ANION_EXCHANGE_CHROMATOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001147"

    # annexin-V staining evidence used in manual assertion
    ECO_0001148 = "ECO_0001148"
    ANNEXIN_V_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001148"

    # cognitive assay phenotypic evidence used in manual assertion
    ECO_0001149 = "ECO_0001149"
    COGNITIVE_ASSAY_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001149"

    # blocking monoclonal antibody evidence used in manual assertion
    ECO_0001150 = "ECO_0001150"
    BLOCKING_MONOCLONAL_ANTIBODY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001150"

    # blocking peptide evidence used in manual assertion
    ECO_0001151 = "ECO_0001151"
    BLOCKING_PEPTIDE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001151"

    # blocking polyclonal antibody evidence used in manual assertion
    ECO_0001152 = "ECO_0001152"
    BLOCKING_POLYCLONAL_ANTIBODY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001152"

    # blood test evidence used in manual assertion
    ECO_0001153 = "ECO_0001153"
    BLOOD_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001153"

    # Boyden chamber assay evidence used in manual assertion
    ECO_0001154 = "ECO_0001154"
    BOYDEN_CHAMBER_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001154"

    # bromodeoxyuridine incorporation assay evidence used in manual assertion
    ECO_0001155 = "ECO_0001155"
    BROMODEOXYURIDINE_INCORPORATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001155"
    )

    # caspase assay evidence used in manual assertion
    ECO_0001156 = "ECO_0001156"
    CASPASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001156"

    # cell counting evidence used in manual assertion
    ECO_0001157 = "ECO_0001157"
    CELL_COUNTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001157"

    # cell permeability assay evidence used in manual assertion
    ECO_0001158 = "ECO_0001158"
    CELL_PERMEABILITY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001158"

    # carboxyfluorescein diacetate succinimidyl ester staining evidence used in manual assertion
    ECO_0001159 = "ECO_0001159"
    CARBOXYFLUORESCEIN_DIACETATE_SUCCINIMIDYL_ESTER_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001159"
    )

    # chemiluminescence-linked immunoassay evidence used in manual assertion
    ECO_0001160 = "ECO_0001160"
    CHEMILUMINESCENCE_LINKED_IMMUNOASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001160"
    )

    # chimeric protein phenotypic evidence used in manual assertion
    ECO_0001161 = "ECO_0001161"
    CHIMERIC_PROTEIN_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001161"

    # co-electrophoresis evidence used in manual assertion
    ECO_0001162 = "ECO_0001162"
    CO_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001162"

    # co-localization evidence used in manual assertion
    ECO_0001163 = "ECO_0001163"
    CO_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001163"

    # co-sedimentation assay evidence used in manual assertion
    ECO_0001164 = "ECO_0001164"
    CO_SEDIMENTATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001164"

    # colony counting evidence used in manual assertion
    ECO_0001165 = "ECO_0001165"
    COLONY_COUNTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001165"

    # comet assay evidence used in manual assertion
    ECO_0001166 = "ECO_0001166"
    COMET_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001166"

    # conditional knockin evidence used in manual assertion
    ECO_0001167 = "ECO_0001167"
    CONDITIONAL_KNOCKIN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001167"

    # conditional knockout evidence used in manual assertion
    ECO_0001168 = "ECO_0001168"
    CONDITIONAL_KNOCKOUT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001168"

    # constitutively active mutant evidence used in manual assertion
    ECO_0001169 = "ECO_0001169"
    CONSTITUTIVELY_ACTIVE_MUTANT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001169"

    # cross-linking evidence used in manual assertion
    ECO_0001170 = "ECO_0001170"
    CROSS_LINKING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001170"

    # crystallography evidence used in manual assertion
    ECO_0001171 = "ECO_0001171"
    CRYSTALLOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001171"

    # cytochemistry evidence used in manual assertion
    ECO_0001172 = "ECO_0001172"
    CYTOCHEMISTRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001172"

    # cytochrome C release assay evidence used in manual assertion
    ECO_0001173 = "ECO_0001173"
    CYTOCHROME_C_RELEASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001173"

    # 4',6-diamidino-2-phenylindole staining evidence used in manual assertion
    ECO_0001174 = "ECO_0001174"
    _4__6_DIAMIDINO_2_PHENYLINDOLE_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001174"
    )

    # deletion mutation phenotypic evidence used in manual assertion
    ECO_0001175 = "ECO_0001175"
    DELETION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001175"

    # DNA laddering assay evidence used in manual assertion
    ECO_0001176 = "ECO_0001176"
    DNA_LADDERING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001176"

    # RNA dot blot assay evidence used in manual assertion
    ECO_0001177 = "ECO_0001177"
    RNA_DOT_BLOT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001177"

    # dominant-negative mutant phenotypic evidence used in manual assertion
    ECO_0001179 = "ECO_0001179"
    DOMINANT_NEGATIVE_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001179"
    )

    # eTag assay evidence used in manual assertion
    ECO_0001180 = "ECO_0001180"
    ETAG_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001180"

    # filter binding assay evidence used in manual assertion
    ECO_0001181 = "ECO_0001181"
    FILTER_BINDING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001181"

    # fluorescence in situ hybridization evidence used in manual assertion
    ECO_0001182 = "ECO_0001182"
    FLUORESCENCE_IN_SITU_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001182"

    # fluorescence resonance energy transfer evidence used in manual assertion
    ECO_0001183 = "ECO_0001183"
    FLUORESCENCE_RESONANCE_ENERGY_TRANSFER_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001183"
    )

    # gel-filtration evidence used in manual assertion
    ECO_0001184 = "ECO_0001184"
    GEL_FILTRATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001184"

    # histochemistry evidence used in manual assertion
    ECO_0001185 = "ECO_0001185"
    HISTOCHEMISTRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001185"

    # immunocytochemistry evidence used in manual assertion
    ECO_0001186 = "ECO_0001186"
    IMMUNOCYTOCHEMISTRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001186"

    # histology evidence used in manual assertion
    ECO_0001187 = "ECO_0001187"
    HISTOLOGY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001187"

    # immunodepletion evidence used in manual assertion
    ECO_0001188 = "ECO_0001188"
    IMMUNODEPLETION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001188"

    # immunohistochemistry evidence used in manual assertion
    ECO_0001189 = "ECO_0001189"
    IMMUNOHISTOCHEMISTRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001189"

    # in vitro acetylation assay evidence used in manual assertion
    ECO_0001190 = "ECO_0001190"
    IN_VITRO_ACETYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001190"

    # in vitro cleavage assay evidence used in manual assertion
    ECO_0001191 = "ECO_0001191"
    IN_VITRO_CLEAVAGE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001191"

    # in vitro deacetylation assay evidence used in manual assertion
    ECO_0001192 = "ECO_0001192"
    IN_VITRO_DEACETYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001192"

    # in vitro defarnesylation assay evidence used in manual assertion
    ECO_0001193 = "ECO_0001193"
    IN_VITRO_DEFARNESYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001193"

    # in vitro demethylation assay evidence used in manual assertion
    ECO_0001194 = "ECO_0001194"
    IN_VITRO_DEMETHYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001194"

    # in vitro desumoylation assay evidence used in manual assertion
    ECO_0001195 = "ECO_0001195"
    IN_VITRO_DESUMOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001195"

    # in vitro deubiquitination assay evidence used in manual assertion
    ECO_0001196 = "ECO_0001196"
    IN_VITRO_DEUBIQUITINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001196"

    # in vitro farnesylation assay evidence used in manual assertion
    ECO_0001197 = "ECO_0001197"
    IN_VITRO_FARNESYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001197"

    # in vitro methylation assay evidence used in manual assertion
    ECO_0001198 = "ECO_0001198"
    IN_VITRO_METHYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001198"

    # in vitro palmitoylation assay evidence used in manual assertion
    ECO_0001199 = "ECO_0001199"
    IN_VITRO_PALMITOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001199"

    # in vitro phosphatase assay evidence used in manual assertion
    ECO_0001200 = "ECO_0001200"
    IN_VITRO_PHOSPHATASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001200"

    # in vitro polyADP-ribosylation assay evidence used in manual assertion
    ECO_0001201 = "ECO_0001201"
    IN_VITRO_POLYADP_RIBOSYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001201"
    )

    # in vitro protein kinase assay evidence used in manual assertion
    ECO_0001202 = "ECO_0001202"
    IN_VITRO_PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001202"

    # in vitro sumoylation assay evidence used in manual assertion
    ECO_0001203 = "ECO_0001203"
    IN_VITRO_SUMOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001203"

    # in vitro transcription assay evidence used in manual assertion
    ECO_0001204 = "ECO_0001204"
    IN_VITRO_TRANSCRIPTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001204"

    # in vitro translation assay evidence used in manual assertion
    ECO_0001205 = "ECO_0001205"
    IN_VITRO_TRANSLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001205"

    # in vitro ubiquitination assay evidence used in manual assertion
    ECO_0001206 = "ECO_0001206"
    IN_VITRO_UBIQUITINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001206"

    # in vivo acetylation assay evidence used in manual assertion
    ECO_0001207 = "ECO_0001207"
    IN_VIVO_ACETYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001207"

    # in vivo cleavage assay evidence used in manual assertion
    ECO_0001208 = "ECO_0001208"
    IN_VIVO_CLEAVAGE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001208"

    # in vivo deacetylation assay evidence used in manual assertion
    ECO_0001209 = "ECO_0001209"
    IN_VIVO_DEACETYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001209"

    # in vivo defarnesylation assay evidence used in manual assertion
    ECO_0001210 = "ECO_0001210"
    IN_VIVO_DEFARNESYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001210"

    # in vivo demethylation assay evidence used in manual assertion
    ECO_0001211 = "ECO_0001211"
    IN_VIVO_DEMETHYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001211"

    # in vivo desumoylation assay evidence used in manual assertion
    ECO_0001212 = "ECO_0001212"
    IN_VIVO_DESUMOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001212"

    # in vivo deubiquitination assay evidence used in manual assertion
    ECO_0001213 = "ECO_0001213"
    IN_VIVO_DEUBIQUITINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001213"

    # in vivo farnesylation assay evidence used in manual assertion
    ECO_0001214 = "ECO_0001214"
    IN_VIVO_FARNESYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001214"

    # in vivo methylation assay evidence used in manual assertion
    ECO_0001215 = "ECO_0001215"
    IN_VIVO_METHYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001215"

    # in vivo palmitoylation assay evidence used in manual assertion
    ECO_0001216 = "ECO_0001216"
    IN_VIVO_PALMITOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001216"

    # in vivo phosphatase assay evidence used in manual assertion
    ECO_0001217 = "ECO_0001217"
    IN_VIVO_PHOSPHATASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001217"

    # in vivo protein kinase assay evidence used in manual assertion
    ECO_0001218 = "ECO_0001218"
    IN_VIVO_PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001218"

    # in vivo sumoylation assay evidence used in manual assertion
    ECO_0001219 = "ECO_0001219"
    IN_VIVO_SUMOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001219"

    # in vivo transcription assay evidence used in manual assertion
    ECO_0001220 = "ECO_0001220"
    IN_VIVO_TRANSCRIPTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001220"

    # in vivo translation assay evidence used in manual assertion
    ECO_0001221 = "ECO_0001221"
    IN_VIVO_TRANSLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001221"

    # in vivo ubiquitination assay evidence used in manual assertion
    ECO_0001222 = "ECO_0001222"
    IN_VIVO_UBIQUITINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001222"

    # induced mutation evidence used in manual assertion
    ECO_0001223 = "ECO_0001223"
    INDUCED_MUTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001223"

    # knockin evidence used in manual assertion
    ECO_0001224 = "ECO_0001224"
    KNOCKIN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001224"

    # knockout evidence used in manual assertion
    ECO_0001225 = "ECO_0001225"
    KNOCKOUT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001225"

    # lipid binding assay evidence used in manual assertion
    ECO_0001226 = "ECO_0001226"
    LIPID_BINDING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001226"

    # luminescence-based mammalian interactome mapping assay evidence used in manual assertion
    ECO_0001227 = "ECO_0001227"
    LUMINESCENCE_BASED_MAMMALIAN_INTERACTOME_MAPPING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001227"
    )

    # macroscopy evidence used in manual assertion
    ECO_0001228 = "ECO_0001228"
    MACROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001228"

    # mammalian 2-hybrid assay evidence used in manual assertion
    ECO_0001229 = "ECO_0001229"
    MAMMALIAN_2_HYBRID_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001229"

    # mass spectrometry evidence used in manual assertion
    ECO_0001230 = "ECO_0001230"
    MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001230"

    # medical imaging evidence used in manual assertion
    ECO_0001231 = "ECO_0001231"
    MEDICAL_IMAGING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001231"

    # microscopy evidence used in manual assertion
    ECO_0001232 = "ECO_0001232"
    MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001232"

    # motility wound healing assay evidence used in manual assertion
    ECO_0001233 = "ECO_0001233"
    MOTILITY_WOUND_HEALING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001233"

    # MTS assay evidence used in manual assertion
    ECO_0001234 = "ECO_0001234"
    MTS_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001234"

    # MTT assay evidence used in manual assertion
    ECO_0001235 = "ECO_0001235"
    MTT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001235"

    # multiplex bead-based immunoassay evidence used in manual assertion
    ECO_0001236 = "ECO_0001236"
    MULTIPLEX_BEAD_BASED_IMMUNOASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001236"

    # natural variation mutant evidence used in manual assertion
    ECO_0001237 = "ECO_0001237"
    NATURAL_VARIATION_MUTANT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001237"

    # nuclear magnetic resonance evidence used in manual assertion
    ECO_0001238 = "ECO_0001238"
    NUCLEAR_MAGNETIC_RESONANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001238"

    # nuclear fragmentation evidence used in manual assertion
    ECO_0001239 = "ECO_0001239"
    NUCLEAR_FRAGMENTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001239"

    # nuclease protection assay evidence used in manual assertion
    ECO_0001240 = "ECO_0001240"
    NUCLEASE_PROTECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001240"

    # nucleotide analog incorporation assay evidence used in manual assertion
    ECO_0001241 = "ECO_0001241"
    NUCLEOTIDE_ANALOG_INCORPORATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001241"
    )

    # phage display evidence used in manual assertion
    ECO_0001242 = "ECO_0001242"
    PHAGE_DISPLAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001242"

    # phosphoamino acid analysis evidence used in manual assertion
    ECO_0001243 = "ECO_0001243"
    PHOSPHOAMINO_ACID_ANALYSIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001243"

    # peptide affinity enrichment evidence used in manual assertion
    ECO_0001244 = "ECO_0001244"
    PEPTIDE_AFFINITY_ENRICHMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001244"

    # peptide array evidence used in manual assertion
    ECO_0001245 = "ECO_0001245"
    PEPTIDE_ARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001245"

    # physical examination evidence used in manual assertion
    ECO_0001246 = "ECO_0001246"
    PHYSICAL_EXAMINATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001246"

    # point mutation phenotypic evidence used in manual assertion
    ECO_0001247 = "ECO_0001247"
    POINT_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001247"

    # propidium iodide staining evidence used in manual assertion
    ECO_0001248 = "ECO_0001248"
    PROPIDIUM_IODIDE_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001248"

    # fluorescence evidence used in manual assertion
    ECO_0001249 = "ECO_0001249"
    FLUORESCENCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001249"

    # protein dot blot assay evidence used in manual assertion
    ECO_0001250 = "ECO_0001250"
    PROTEIN_DOT_BLOT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001250"

    # protein microarray evidence used in manual assertion
    ECO_0001251 = "ECO_0001251"
    PROTEIN_MICROARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001251"

    # protein sequencing assay evidence used in manual assertion
    ECO_0001252 = "ECO_0001252"
    PROTEIN_SEQUENCING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001252"

    # quantitative mass spectrometry evidence used in manual assertion
    ECO_0001253 = "ECO_0001253"
    QUANTITATIVE_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001253"

    # radioisotope assay evidence used in manual assertion
    ECO_0001254 = "ECO_0001254"
    RADIOISOTOPE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001254"

    # radioimmunoassay evidence used in manual assertion
    ECO_0001255 = "ECO_0001255"
    RADIOIMMUNOASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001255"

    # imaging assay evidence used in manual assertion
    ECO_0001256 = "ECO_0001256"
    IMAGING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001256"

    # restriction fragment detection evidence used in manual assertion
    ECO_0001257 = "ECO_0001257"
    RESTRICTION_FRAGMENT_DETECTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001257"

    # spectrophotometry evidence used in manual assertion
    ECO_0001258 = "ECO_0001258"
    SPECTROPHOTOMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001258"

    # syngeneic transplantation experiment evidence used in manual assertion
    ECO_0001259 = "ECO_0001259"
    SYNGENEIC_TRANSPLANTATION_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001259"
    )

    # xenotransplantation phenotypic evidence used in manual assertion
    ECO_0001260 = "ECO_0001260"
    XENOTRANSPLANTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001260"

    # WST-1 assay evidence used in manual assertion
    ECO_0001261 = "ECO_0001261"
    WST_1_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001261"

    # urine test evidence used in manual assertion
    ECO_0001263 = "ECO_0001263"
    URINE_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001263"

    # terminal deoxynucleotidyl transferase dUTP nick end labeling assay evidence used in manual assertion
    ECO_0001264 = "ECO_0001264"
    TERMINAL_DEOXYNUCLEOTIDYL_TRANSFERASE_DUTP_NICK_END_LABELING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001264"
    )

    # tryptic phosphopeptide mapping assay evidence used in manual assertion
    ECO_0001265 = "ECO_0001265"
    TRYPTIC_PHOSPHOPEPTIDE_MAPPING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001265"
    )

    # transgenic organism evidence used in manual assertion
    ECO_0001266 = "ECO_0001266"
    TRANSGENIC_ORGANISM_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001266"

    # tissue microarray evidence used in manual assertion
    ECO_0001267 = "ECO_0001267"
    TISSUE_MICROARRAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001267"

    # TACE activity assay evidence used in manual assertion
    ECO_0001268 = "ECO_0001268"
    TACE_ACTIVITY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001268"

    # surface plasmon resonance evidence used in manual assertion
    ECO_0001269 = "ECO_0001269"
    SURFACE_PLASMON_RESONANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001269"

    # restriction landmark genomic scanning evidence used in manual assertion
    ECO_0001270 = "ECO_0001270"
    RESTRICTION_LANDMARK_GENOMIC_SCANNING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001270"
    )

    # resonant mirror biosensor evidence used in manual assertion
    ECO_0001271 = "ECO_0001271"
    RESONANT_MIRROR_BIOSENSOR_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001271"

    # high-performance liquid chromatography evidence used in manual assertion
    ECO_0001272 = "ECO_0001272"
    HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001272"
    )

    # ectopic expression evidence used in manual assertion
    ECO_0001273 = "ECO_0001273"
    ECTOPIC_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001273"

    # small molecule detection assay evidence
    ECO_0001522 = "ECO_0001522"
    SMALL_MOLECULE_DETECTION_ASSAY_EVIDENCE = "ECO_0001522"

    # localization evidence
    ECO_0001533 = "ECO_0001533"
    LOCALIZATION_EVIDENCE = "ECO_0001533"

    # nucleic acid localization evidence
    ECO_0001534 = "ECO_0001534"
    NUCLEIC_ACID_LOCALIZATION_EVIDENCE = "ECO_0001534"

    # acetylation assay evidence
    ECO_0001546 = "ECO_0001546"
    ACETYLATION_ASSAY_EVIDENCE = "ECO_0001546"

    # cleavage assay evidence
    ECO_0001547 = "ECO_0001547"
    CLEAVAGE_ASSAY_EVIDENCE = "ECO_0001547"

    # deacetylation assay evidence
    ECO_0001548 = "ECO_0001548"
    DEACETYLATION_ASSAY_EVIDENCE = "ECO_0001548"

    # defarnesylation assay evidence
    ECO_0001549 = "ECO_0001549"
    DEFARNESYLATION_ASSAY_EVIDENCE = "ECO_0001549"

    # demethylation assay evidence
    ECO_0001550 = "ECO_0001550"
    DEMETHYLATION_ASSAY_EVIDENCE = "ECO_0001550"

    # desumoylation assay evidence
    ECO_0001551 = "ECO_0001551"
    DESUMOYLATION_ASSAY_EVIDENCE = "ECO_0001551"

    # deubiquitination assay evidence
    ECO_0001552 = "ECO_0001552"
    DEUBIQUITINATION_ASSAY_EVIDENCE = "ECO_0001552"

    # farnesylation assay evidence
    ECO_0001553 = "ECO_0001553"
    FARNESYLATION_ASSAY_EVIDENCE = "ECO_0001553"

    # methylation assay evidence
    ECO_0001554 = "ECO_0001554"
    METHYLATION_ASSAY_EVIDENCE = "ECO_0001554"

    # palmitoylation assay evidence
    ECO_0001555 = "ECO_0001555"
    PALMITOYLATION_ASSAY_EVIDENCE = "ECO_0001555"

    # phosphatase assay evidence
    ECO_0001556 = "ECO_0001556"
    PHOSPHATASE_ASSAY_EVIDENCE = "ECO_0001556"

    # polyADP-ribosylation assay evidence
    ECO_0001557 = "ECO_0001557"
    POLYADP_RIBOSYLATION_ASSAY_EVIDENCE = "ECO_0001557"

    # protein kinase assay evidence
    ECO_0001558 = "ECO_0001558"
    PROTEIN_KINASE_ASSAY_EVIDENCE = "ECO_0001558"

    # sumoylation assay evidence
    ECO_0001559 = "ECO_0001559"
    SUMOYLATION_ASSAY_EVIDENCE = "ECO_0001559"

    # single-cell RNA-sequencing evidence used in automatic assertion
    ECO_000156 = "ECO_000156"
    SINGLE_CELL_RNA_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_000156"

    # single-cell RNA-sequencing evidence
    ECO_0001560 = "ECO_0001560"
    SINGLE_CELL_RNA_SEQUENCING_EVIDENCE = "ECO_0001560"

    # translation assay evidence
    ECO_0001561 = "ECO_0001561"
    TRANSLATION_ASSAY_EVIDENCE = "ECO_0001561"

    # ubiquitination assay evidence
    ECO_0001562 = "ECO_0001562"
    UBIQUITINATION_ASSAY_EVIDENCE = "ECO_0001562"

    # cell growth assay evidence
    ECO_0001563 = "ECO_0001563"
    CELL_GROWTH_ASSAY_EVIDENCE = "ECO_0001563"

    # cell-based assay evidence
    ECO_0001565 = "ECO_0001565"
    CELL_BASED_ASSAY_EVIDENCE = "ECO_0001565"

    # quantitative reverse transcription polymerase chain reaction evidence
    ECO_0001566 = "ECO_0001566"
    QUANTITATIVE_REVERSE_TRANSCRIPTION_POLYMERASE_CHAIN_REACTION_EVIDENCE = (
        "ECO_0001566"
    )

    # quantitative reverse transcription polymerase chain reaction evidence used in manual assertion
    ECO_0001567 = "ECO_0001567"
    QUANTITATIVE_REVERSE_TRANSCRIPTION_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001567"
    )

    # quantitative reverse transcription polymerase chain reaction evidence used in automatic assertion.
    ECO_0001568 = "ECO_0001568"
    QUANTITATIVE_REVERSE_TRANSCRIPTION_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION_ = (
        "ECO_0001568"
    )

    # colony diameter phenotype evidence used in manual assertion
    ECO_000157 = "ECO_000157"
    COLONY_DIAMETER_PHENOTYPE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_000157"

    # single-cell RNA-sequencing evidence used in manual assertion
    ECO_0001570 = "ECO_0001570"
    SINGLE_CELL_RNA_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001570"

    # colony diameter phenotype evidence
    ECO_0001571 = "ECO_0001571"
    COLONY_DIAMETER_PHENOTYPE_EVIDENCE = "ECO_0001571"

    # colony diameter phenotype evidence used in automatic assertion
    ECO_0001572 = "ECO_0001572"
    COLONY_DIAMETER_PHENOTYPE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001572"

    # membrane fusion assay evidence
    ECO_0001574 = "ECO_0001574"
    MEMBRANE_FUSION_ASSAY_EVIDENCE = "ECO_0001574"

    # membrane fusion assay evidence used in automatic assertion
    ECO_0001575 = "ECO_0001575"
    MEMBRANE_FUSION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001575"

    # membrane fusion assay evidence used in manual assertion
    ECO_0001576 = "ECO_0001576"
    MEMBRANE_FUSION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001576"

    # spheroplast fusion assay evidence
    ECO_0001577 = "ECO_0001577"
    SPHEROPLAST_FUSION_ASSAY_EVIDENCE = "ECO_0001577"

    # spheroplast fusion assay evidence used in automatic assertion
    ECO_0001578 = "ECO_0001578"
    SPHEROPLAST_FUSION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001578"

    # spheroplast fusion assay evidence used in manual assertion
    ECO_0001579 = "ECO_0001579"
    SPHEROPLAST_FUSION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001579"

    # liquid chromatography coupled with tandem mass spectrometry evidence
    ECO_0001580 = "ECO_0001580"
    LIQUID_CHROMATOGRAPHY_COUPLED_WITH_TANDEM_MASS_SPECTROMETRY_EVIDENCE = "ECO_0001580"

    # liquid chromatography coupled with tandem mass spectrometry evidence used in automatic assertion
    ECO_0001581 = "ECO_0001581"
    LIQUID_CHROMATOGRAPHY_COUPLED_WITH_TANDEM_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0001581"
    )

    # liquid chromatography coupled with tandem mass spectrometry evidence used in manual assertion
    ECO_0001582 = "ECO_0001582"
    LIQUID_CHROMATOGRAPHY_COUPLED_WITH_TANDEM_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001582"
    )

    # small interfering RNA knockdown evidence
    ECO_0001583 = "ECO_0001583"
    SMALL_INTERFERING_RNA_KNOCKDOWN_EVIDENCE = "ECO_0001583"

    # small interfering RNA knockdown evidence used in automatic assertion
    ECO_0001584 = "ECO_0001584"
    SMALL_INTERFERING_RNA_KNOCKDOWN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001584"

    # small interfering RNA knockdown evidence used in manual assertion
    ECO_0001585 = "ECO_0001585"
    SMALL_INTERFERING_RNA_KNOCKDOWN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001585"

    # ion trap mass spectrometry evidence
    ECO_0001586 = "ECO_0001586"
    ION_TRAP_MASS_SPECTROMETRY_EVIDENCE = "ECO_0001586"

    # ion trap mass spectrometry evidence used in automatic assertion
    ECO_0001587 = "ECO_0001587"
    ION_TRAP_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001587"

    # ion trap mass spectrometry evidence used in manual assertion
    ECO_0001588 = "ECO_0001588"
    ION_TRAP_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001588"

    # atomic force microscopy evidence
    ECO_0001589 = "ECO_0001589"
    ATOMIC_FORCE_MICROSCOPY_EVIDENCE = "ECO_0001589"

    # atomic force microscopy evidence used in automatic assertion
    ECO_0001590 = "ECO_0001590"
    ATOMIC_FORCE_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001590"

    # atomic force microscopy evidence used in manual assertion
    ECO_0001591 = "ECO_0001591"
    ATOMIC_FORCE_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001591"

    # polysome profiling evidence
    ECO_0001592 = "ECO_0001592"
    POLYSOME_PROFILING_EVIDENCE = "ECO_0001592"

    # polysome profiling evidence used in automatic assertion
    ECO_0001593 = "ECO_0001593"
    POLYSOME_PROFILING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001593"

    # polysome profiling evidence used in manual assertion
    ECO_0001594 = "ECO_0001594"
    POLYSOME_PROFILING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001594"

    # multilocus sequence typing evidence
    ECO_0001598 = "ECO_0001598"
    MULTILOCUS_SEQUENCE_TYPING_EVIDENCE = "ECO_0001598"

    # multilocus sequence typing evidence used in automatic assertion
    ECO_0001599 = "ECO_0001599"
    MULTILOCUS_SEQUENCE_TYPING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001599"

    # multilocus sequence typing evidence used in manual assertion
    ECO_0001600 = "ECO_0001600"
    MULTILOCUS_SEQUENCE_TYPING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001600"

    # protein-oligonucleotide microarray binding evidence
    ECO_0001601 = "ECO_0001601"
    PROTEIN_OLIGONUCLEOTIDE_MICROARRAY_BINDING_EVIDENCE = "ECO_0001601"

    # cell staining evidence
    ECO_0001603 = "ECO_0001603"
    CELL_STAINING_EVIDENCE = "ECO_0001603"

    # alkaline phosphatase reporter gene assay evidence
    ECO_0001801 = "ECO_0001801"
    ALKALINE_PHOSPHATASE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0001801"

    # beta-galactosidase reporter gene assay evidence
    ECO_0001802 = "ECO_0001802"
    BETA_GALACTOSIDASE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0001802"

    # chloramphenicol acetyltransferase reporter gene assay evidence
    ECO_0001803 = "ECO_0001803"
    CHLORAMPHENICOL_ACETYLTRANSFERASE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0001803"

    # beta-glucuronidase reporter gene assay evidence
    ECO_0001804 = "ECO_0001804"
    BETA_GLUCURONIDASE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0001804"

    # luciferase reporter gene assay evidence
    ECO_0001805 = "ECO_0001805"
    LUCIFERASE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0001805"

    # chromatin immunoprecipitation- exonuclease evidence
    ECO_0001806 = "ECO_0001806"
    CHROMATIN_IMMUNOPRECIPITATION__EXONUCLEASE_EVIDENCE = "ECO_0001806"

    # electrophoretic mobility shift assay evidence used in manual assertion
    ECO_0001807 = "ECO_0001807"
    ELECTROPHORETIC_MOBILITY_SHIFT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001807"
    )

    # reverse transcription polymerase chain reaction evidence used in manual assertion
    ECO_0001808 = "ECO_0001808"
    REVERSE_TRANSCRIPTION_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001808"
    )

    # DNA affinity chromatography evidence
    ECO_0001809 = "ECO_0001809"
    DNA_AFFINITY_CHROMATOGRAPHY_EVIDENCE = "ECO_0001809"

    # DNAse footprinting evidence
    ECO_0001810 = "ECO_0001810"
    DNASE_FOOTPRINTING_EVIDENCE = "ECO_0001810"

    # fluorescence anisotropy evidence
    ECO_0001811 = "ECO_0001811"
    FLUORESCENCE_ANISOTROPY_EVIDENCE = "ECO_0001811"

    # genomic systematic evolution of ligands by exponential amplification evidence
    ECO_0001812 = "ECO_0001812"
    GENOMIC_SYSTEMATIC_EVOLUTION_OF_LIGANDS_BY_EXPONENTIAL_AMPLIFICATION_EVIDENCE = (
        "ECO_0001812"
    )

    # heteronuclear single quantum coherence spectroscopy evidence
    ECO_0001813 = "ECO_0001813"
    HETERONUCLEAR_SINGLE_QUANTUM_COHERENCE_SPECTROSCOPY_EVIDENCE = "ECO_0001813"

    # methidiumpropyl-ethylenediaminetetraacetic acid iron (II) footprinting evidence
    ECO_0001814 = "ECO_0001814"
    METHIDIUMPROPYL_ETHYLENEDIAMINETETRAACETIC_ACID_IRON__II__FOOTPRINTING_EVIDENCE = (
        "ECO_0001814"
    )

    # copper-phenanthroline footprinting evidence
    ECO_0001815 = "ECO_0001815"
    COPPER_PHENANTHROLINE_FOOTPRINTING_EVIDENCE = "ECO_0001815"

    # green fluorescent protein reporter gene assay evidence
    ECO_0001816 = "ECO_0001816"
    GREEN_FLUORESCENT_PROTEIN_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0001816"

    # glutathione S-transferase pull-down assay evidence
    ECO_0001817 = "ECO_0001817"
    GLUTATHIONE_S_TRANSFERASE_PULL_DOWN_ASSAY_EVIDENCE = "ECO_0001817"

    # hydroxyl-radical footprinting evidence
    ECO_0001818 = "ECO_0001818"
    HYDROXYL_RADICAL_FOOTPRINTING_EVIDENCE = "ECO_0001818"

    # primer extension assay evidence
    ECO_0001819 = "ECO_0001819"
    PRIMER_EXTENSION_ASSAY_EVIDENCE = "ECO_0001819"

    # rapid amplification of cDNA ends polymerase chain reaction evidence
    ECO_0001820 = "ECO_0001820"
    RAPID_AMPLIFICATION_OF_CDNA_ENDS_POLYMERASE_CHAIN_REACTION_EVIDENCE = "ECO_0001820"

    # RNA sequencing assay evidence
    ECO_0001821 = "ECO_0001821"
    RNA_SEQUENCING_ASSAY_EVIDENCE = "ECO_0001821"

    # survival rate analysis evidence
    ECO_0001822 = "ECO_0001822"
    SURVIVAL_RATE_ANALYSIS_EVIDENCE = "ECO_0001822"

    # x-ray crystallography evidence
    ECO_0001823 = "ECO_0001823"
    X_RAY_CRYSTALLOGRAPHY_EVIDENCE = "ECO_0001823"

    # DNA adenine methyltransferase identification evidence
    ECO_0001824 = "ECO_0001824"
    DNA_ADENINE_METHYLTRANSFERASE_IDENTIFICATION_EVIDENCE = "ECO_0001824"

    # isothermal titration calorimetry evidence
    ECO_0001825 = "ECO_0001825"
    ISOTHERMAL_TITRATION_CALORIMETRY_EVIDENCE = "ECO_0001825"

    # ultraviolet light footprinting evidence
    ECO_0001826 = "ECO_0001826"
    ULTRAVIOLET_LIGHT_FOOTPRINTING_EVIDENCE = "ECO_0001826"

    # methylation interference footprinting evidence
    ECO_0001827 = "ECO_0001827"
    METHYLATION_INTERFERENCE_FOOTPRINTING_EVIDENCE = "ECO_0001827"

    # inference of sequence features from visual inspection used in manual assertion
    ECO_0001828 = "ECO_0001828"
    INFERENCE_OF_SEQUENCE_FEATURES_FROM_VISUAL_INSPECTION_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001828"
    )

    # ferric uptake regulator titration assay evidence
    ECO_0001829 = "ECO_0001829"
    FERRIC_UPTAKE_REGULATOR_TITRATION_ASSAY_EVIDENCE = "ECO_0001829"

    # host colonization assay evidence
    ECO_0001830 = "ECO_0001830"
    HOST_COLONIZATION_ASSAY_EVIDENCE = "ECO_0001830"

    # host colonization assay evidence used in automatic assertion
    ECO_0001831 = "ECO_0001831"
    HOST_COLONIZATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001831"

    # host colonization assay evidence used in manual assertion
    ECO_0001832 = "ECO_0001832"
    HOST_COLONIZATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001832"

    # infection assay evidence
    ECO_0001833 = "ECO_0001833"
    INFECTION_ASSAY_EVIDENCE = "ECO_0001833"

    # infection assay evidence used in automatic assertion
    ECO_0001834 = "ECO_0001834"
    INFECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001834"

    # infection assay evidence used in manual assertion
    ECO_0001835 = "ECO_0001835"
    INFECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001835"

    # in situ hybridization evidence
    ECO_0001836 = "ECO_0001836"
    IN_SITU_HYBRIDIZATION_EVIDENCE = "ECO_0001836"

    # in situ hybridization evidence used in automatic assertion
    ECO_0001837 = "ECO_0001837"
    IN_SITU_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001837"

    # in situ hybridization evidence used in manual assertion
    ECO_0001838 = "ECO_0001838"
    IN_SITU_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001838"

    # colorimetric in situ hybridization evidence
    ECO_0001839 = "ECO_0001839"
    COLORIMETRIC_IN_SITU_HYBRIDIZATION_EVIDENCE = "ECO_0001839"

    # colorimetric in situ hybridization evidence used in automatic assertion
    ECO_0001840 = "ECO_0001840"
    COLORIMETRIC_IN_SITU_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0001840"
    )

    # colorimetric in situ hybridization evidence used in manual assertion
    ECO_0001841 = "ECO_0001841"
    COLORIMETRIC_IN_SITU_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001841"

    # random mutagenesis of specific target DNA evidence
    ECO_0001842 = "ECO_0001842"
    RANDOM_MUTAGENESIS_OF_SPECIFIC_TARGET_DNA_EVIDENCE = "ECO_0001842"

    # random mutagenesis of specific target DNA evidence used in automatic assertion
    ECO_0001843 = "ECO_0001843"
    RANDOM_MUTAGENESIS_OF_SPECIFIC_TARGET_DNA_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0001843"
    )

    # random mutagenesis of specific target DNA evidence used in manual assertion
    ECO_0001844 = "ECO_0001844"
    RANDOM_MUTAGENESIS_OF_SPECIFIC_TARGET_DNA_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0001844"
    )

    # cell population optical density evidence
    ECO_0001845 = "ECO_0001845"
    CELL_POPULATION_OPTICAL_DENSITY_EVIDENCE = "ECO_0001845"

    # cell population optical density evidence used in automatic assertion
    ECO_0001846 = "ECO_0001846"
    CELL_POPULATION_OPTICAL_DENSITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0001846"

    # cell population optical density evidence used in manual assertion
    ECO_0001847 = "ECO_0001847"
    CELL_POPULATION_OPTICAL_DENSITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0001847"

    # cell viability assay evidence
    ECO_0005004 = "ECO_0005004"
    CELL_VIABILITY_ASSAY_EVIDENCE = "ECO_0005004"

    # cell proliferation assay evidence
    ECO_0005007 = "ECO_0005007"
    CELL_PROLIFERATION_ASSAY_EVIDENCE = "ECO_0005007"

    # DNA synthesis cell proliferation assay evidence
    ECO_0005008 = "ECO_0005008"
    DNA_SYNTHESIS_CELL_PROLIFERATION_ASSAY_EVIDENCE = "ECO_0005008"

    # ATP bioluminescence assay evidence
    ECO_0005011 = "ECO_0005011"
    ATP_BIOLUMINESCENCE_ASSAY_EVIDENCE = "ECO_0005011"

    # cytotoxicity assay evidence
    ECO_0005012 = "ECO_0005012"
    CYTOTOXICITY_ASSAY_EVIDENCE = "ECO_0005012"

    # in vitro cell based assay evidence
    ECO_0005014 = "ECO_0005014"
    IN_VITRO_CELL_BASED_ASSAY_EVIDENCE = "ECO_0005014"

    # staining evidence
    ECO_0005019 = "ECO_0005019"
    STAINING_EVIDENCE = "ECO_0005019"

    # chemotaxis assay evidence
    ECO_0005021 = "ECO_0005021"
    CHEMOTAXIS_ASSAY_EVIDENCE = "ECO_0005021"

    # genetic transformation evidence
    ECO_0005027 = "ECO_0005027"
    GENETIC_TRANSFORMATION_EVIDENCE = "ECO_0005027"

    # structure determination evidence
    ECO_0005031 = "ECO_0005031"
    STRUCTURE_DETERMINATION_EVIDENCE = "ECO_0005031"

    # electron microscopy evidence
    ECO_0005033 = "ECO_0005033"
    ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0005033"

    # apoptotic assay evidence
    ECO_0005034 = "ECO_0005034"
    APOPTOTIC_ASSAY_EVIDENCE = "ECO_0005034"

    # in vivo polyADP-ribosylation assay evidence
    ECO_0005500 = "ECO_0005500"
    IN_VIVO_POLYADP_RIBOSYLATION_ASSAY_EVIDENCE = "ECO_0005500"

    # in vivo polyADP-ribosylation assay evidence used in manual assertion
    ECO_0005501 = "ECO_0005501"
    IN_VIVO_POLYADP_RIBOSYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005501"

    # ex vivo assay evidence
    ECO_0005502 = "ECO_0005502"
    EX_VIVO_ASSAY_EVIDENCE = "ECO_0005502"

    # two-dimensional polyacrylamide gel electrophoresis evidence
    ECO_0005503 = "ECO_0005503"
    TWO_DIMENSIONAL_POLYACRYLAMIDE_GEL_ELECTROPHORESIS_EVIDENCE = "ECO_0005503"

    # spectrometry evidence
    ECO_0005504 = "ECO_0005504"
    SPECTROMETRY_EVIDENCE = "ECO_0005504"

    # regular expression motif search evidence
    ECO_0005505 = "ECO_0005505"
    REGULAR_EXPRESSION_MOTIF_SEARCH_EVIDENCE = "ECO_0005505"

    # missense mutation phenotypic evidence
    ECO_0005506 = "ECO_0005506"
    MISSENSE_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005506"

    # nonsense mutation phenotypic evidence
    ECO_0005507 = "ECO_0005507"
    NONSENSE_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005507"

    # silent mutation evidence
    ECO_0005508 = "ECO_0005508"
    SILENT_MUTATION_EVIDENCE = "ECO_0005508"

    # insertion mutation phenotypic evidence
    ECO_0005509 = "ECO_0005509"
    INSERTION_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005509"

    # duplication mutation evidence
    ECO_0005511 = "ECO_0005511"
    DUPLICATION_MUTATION_EVIDENCE = "ECO_0005511"

    # frameshift mutation phenotypic evidence
    ECO_0005512 = "ECO_0005512"
    FRAMESHIFT_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005512"

    # repeat expansion mutation phenotypic evidence
    ECO_0005513 = "ECO_0005513"
    REPEAT_EXPANSION_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005513"

    # splice site mutation phenotypic evidence
    ECO_0005514 = "ECO_0005514"
    SPLICE_SITE_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005514"

    # translocation mutation phenotypic evidence
    ECO_0005515 = "ECO_0005515"
    TRANSLOCATION_MUTATION_PHENOTYPIC_EVIDENCE = "ECO_0005515"

    # molecule detection assay evidence
    ECO_0005516 = "ECO_0005516"
    MOLECULE_DETECTION_ASSAY_EVIDENCE = "ECO_0005516"

    # protein detection assay evidence
    ECO_0005517 = "ECO_0005517"
    PROTEIN_DETECTION_ASSAY_EVIDENCE = "ECO_0005517"

    # RNA detection assay evidence
    ECO_0005518 = "ECO_0005518"
    RNA_DETECTION_ASSAY_EVIDENCE = "ECO_0005518"

    # DNA detection assay evidence
    ECO_0005519 = "ECO_0005519"
    DNA_DETECTION_ASSAY_EVIDENCE = "ECO_0005519"

    # interferometric reflectance imaging sensor evidence
    ECO_0005520 = "ECO_0005520"
    INTERFEROMETRIC_REFLECTANCE_IMAGING_SENSOR_EVIDENCE = "ECO_0005520"

    # S1 nuclease protection assay evidence
    ECO_0005521 = "ECO_0005521"
    S1_NUCLEASE_PROTECTION_ASSAY_EVIDENCE = "ECO_0005521"

    # DNA dot blot assay evidence
    ECO_0005522 = "ECO_0005522"
    DNA_DOT_BLOT_ASSAY_EVIDENCE = "ECO_0005522"

    # DNA dot blot assay evidence used in manual assertion
    ECO_0005523 = "ECO_0005523"
    DNA_DOT_BLOT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005523"

    # matrix-assisted laser desorption/ionization time-of-flight mass spectrometry evidence
    ECO_0005526 = "ECO_0005526"
    MATRIX_ASSISTED_LASER_DESORPTION_IONIZATION_TIME_OF_FLIGHT_MASS_SPECTROMETRY_EVIDENCE = (
        "ECO_0005526"
    )

    # matrix-assisted laser desorption/ionization time-of-flight mass spectrometry evidence used in manual assertion
    ECO_0005527 = "ECO_0005527"
    MATRIX_ASSISTED_LASER_DESORPTION_IONIZATION_TIME_OF_FLIGHT_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005527"
    )

    # site-directed mutagenesis phenotypic evidence
    ECO_0005528 = "ECO_0005528"
    SITE_DIRECTED_MUTAGENESIS_PHENOTYPIC_EVIDENCE = "ECO_0005528"

    # random mutagenesis phenotypic evidence
    ECO_0005529 = "ECO_0005529"
    RANDOM_MUTAGENESIS_PHENOTYPIC_EVIDENCE = "ECO_0005529"

    # random mutagenesis evidence used in manual assertion
    ECO_0005530 = "ECO_0005530"
    RANDOM_MUTAGENESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005530"

    # motif discovery evidence
    ECO_0005531 = "ECO_0005531"
    MOTIF_DISCOVERY_EVIDENCE = "ECO_0005531"

    # consensus search evidence
    ECO_0005532 = "ECO_0005532"
    CONSENSUS_SEARCH_EVIDENCE = "ECO_0005532"

    # phylogenetic footprinting evidence
    ECO_0005533 = "ECO_0005533"
    PHYLOGENETIC_FOOTPRINTING_EVIDENCE = "ECO_0005533"

    # comparative genomics motif search evidence
    ECO_0005534 = "ECO_0005534"
    COMPARATIVE_GENOMICS_MOTIF_SEARCH_EVIDENCE = "ECO_0005534"

    # machine learning prediction of motif instance evidence
    ECO_0005535 = "ECO_0005535"
    MACHINE_LEARNING_PREDICTION_OF_MOTIF_INSTANCE_EVIDENCE = "ECO_0005535"

    # position-specific scoring matrix motif search evidence
    ECO_0005536 = "ECO_0005536"
    POSITION_SPECIFIC_SCORING_MATRIX_MOTIF_SEARCH_EVIDENCE = "ECO_0005536"

    # xylE reporter gene assay evidence
    ECO_0005537 = "ECO_0005537"
    XYLE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0005537"

    # computationally derived logical inference
    ECO_0005538 = "ECO_0005538"
    COMPUTATIONALLY_DERIVED_LOGICAL_INFERENCE = "ECO_0005538"

    # computationally derived logical inference used in automatic assertion
    ECO_0005539 = "ECO_0005539"
    COMPUTATIONALLY_DERIVED_LOGICAL_INFERENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005539"
    )

    # computationally derived logical inference from automatic assertion used in automatic assertion
    ECO_0005540 = "ECO_0005540"
    COMPUTATIONALLY_DERIVED_LOGICAL_INFERENCE_FROM_AUTOMATIC_ASSERTION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005540"
    )

    # computationally derived logical inference from manual assertion used in automatic assertion
    ECO_0005541 = "ECO_0005541"
    COMPUTATIONALLY_DERIVED_LOGICAL_INFERENCE_FROM_MANUAL_ASSERTION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005541"
    )

    # biological system reconstruction evidence by experimental evidence from single species used in manual assertion
    ECO_0005542 = "ECO_0005542"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_FROM_SINGLE_SPECIES_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005542"
    )

    # biological system reconstruction evidence by experimental evidence from mixed species used in manual assertion
    ECO_0005543 = "ECO_0005543"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_FROM_MIXED_SPECIES_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005543"
    )

    # biological system reconstruction evidence based on orthology evidence used in manual assertion
    ECO_0005544 = "ECO_0005544"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_ORTHOLOGY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005544"
    )

    # biological system reconstruction evidence based on orthology evidence
    ECO_0005545 = "ECO_0005545"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_ORTHOLOGY_EVIDENCE = (
        "ECO_0005545"
    )

    # biological system reconstruction evidence based on paralogy evidence used in manual assertion
    ECO_0005546 = "ECO_0005546"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_PARALOGY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005546"
    )

    # biological system reconstruction evidence based on inference from background scientific knowledge used in manual assertion
    ECO_0005547 = "ECO_0005547"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_INFERENCE_FROM_BACKGROUND_SCIENTIFIC_KNOWLEDGE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005547"
    )

    # biological system reconstruction evidence based on inference from background scientific knowledge
    ECO_0005548 = "ECO_0005548"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_INFERENCE_FROM_BACKGROUND_SCIENTIFIC_KNOWLEDGE = (
        "ECO_0005548"
    )

    # biological system reconstruction evidence based on homology evidence
    ECO_0005549 = "ECO_0005549"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_HOMOLOGY_EVIDENCE = "ECO_0005549"

    # biological system reconstruction evidence based on paralogy evidence
    ECO_0005550 = "ECO_0005550"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_PARALOGY_EVIDENCE = "ECO_0005550"

    # biological system reconstruction evidence by experimental evidence
    ECO_0005551 = "ECO_0005551"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE = "ECO_0005551"

    # biological system reconstruction evidence by experimental evidence from mixed species
    ECO_0005552 = "ECO_0005552"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_FROM_MIXED_SPECIES = (
        "ECO_0005552"
    )

    # biological system reconstruction evidence by experimental evidence from single species
    ECO_0005553 = "ECO_0005553"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_FROM_SINGLE_SPECIES = (
        "ECO_0005553"
    )

    # pairwise sequence alignment evidence
    ECO_0005554 = "ECO_0005554"
    PAIRWISE_SEQUENCE_ALIGNMENT_EVIDENCE = "ECO_0005554"

    # multiple sequence alignment evidence
    ECO_0005555 = "ECO_0005555"
    MULTIPLE_SEQUENCE_ALIGNMENT_EVIDENCE = "ECO_0005555"

    # multiple sequence alignment evidence used in manual assertion
    ECO_0005556 = "ECO_0005556"
    MULTIPLE_SEQUENCE_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005556"

    # multiple sequence alignment evidence used in automatic assertion
    ECO_0005557 = "ECO_0005557"
    MULTIPLE_SEQUENCE_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005557"

    # motif discovery evidence used in manual assertion
    ECO_0005558 = "ECO_0005558"
    MOTIF_DISCOVERY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005558"

    # motif discovery evidence used in automatic assertion
    ECO_0005559 = "ECO_0005559"
    MOTIF_DISCOVERY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005559"

    # pairwise sequence alignment evidence used in manual assertion
    ECO_0005560 = "ECO_0005560"
    PAIRWISE_SEQUENCE_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005560"

    # pairwise sequence alignment evidence used in automatic assertion
    ECO_0005561 = "ECO_0005561"
    PAIRWISE_SEQUENCE_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005561"

    # in-gel protein kinase assay evidence
    ECO_0005562 = "ECO_0005562"
    IN_GEL_PROTEIN_KINASE_ASSAY_EVIDENCE = "ECO_0005562"

    # macroscopic current trace evidence
    ECO_0005563 = "ECO_0005563"
    MACROSCOPIC_CURRENT_TRACE_EVIDENCE = "ECO_0005563"

    # current density evidence
    ECO_0005564 = "ECO_0005564"
    CURRENT_DENSITY_EVIDENCE = "ECO_0005564"

    # single channel conductance evidence
    ECO_0005565 = "ECO_0005565"
    SINGLE_CHANNEL_CONDUCTANCE_EVIDENCE = "ECO_0005565"

    # sustained current evidence
    ECO_0005566 = "ECO_0005566"
    SUSTAINED_CURRENT_EVIDENCE = "ECO_0005566"

    # steady state activation curve evidence
    ECO_0005567 = "ECO_0005567"
    STEADY_STATE_ACTIVATION_CURVE_EVIDENCE = "ECO_0005567"

    # steady state inactivation curve evidence
    ECO_0005568 = "ECO_0005568"
    STEADY_STATE_INACTIVATION_CURVE_EVIDENCE = "ECO_0005568"

    # window current trace evidence
    ECO_0005569 = "ECO_0005569"
    WINDOW_CURRENT_TRACE_EVIDENCE = "ECO_0005569"

    # use dependence of inactivation evidence
    ECO_0005570 = "ECO_0005570"
    USE_DEPENDENCE_OF_INACTIVATION_EVIDENCE = "ECO_0005570"

    # current clamp recording evidence
    ECO_0005571 = "ECO_0005571"
    CURRENT_CLAMP_RECORDING_EVIDENCE = "ECO_0005571"

    # whole-cell voltage clamp recording evidence
    ECO_0005572 = "ECO_0005572"
    WHOLE_CELL_VOLTAGE_CLAMP_RECORDING_EVIDENCE = "ECO_0005572"

    # cell-attached single-channel recording evidence
    ECO_0005573 = "ECO_0005573"
    CELL_ATTACHED_SINGLE_CHANNEL_RECORDING_EVIDENCE = "ECO_0005573"

    # cell-detached inside-out single-channel recording evidence
    ECO_0005574 = "ECO_0005574"
    CELL_DETACHED_INSIDE_OUT_SINGLE_CHANNEL_RECORDING_EVIDENCE = "ECO_0005574"

    # reconstituted bilayer single-channel patch recording evidence
    ECO_0005575 = "ECO_0005575"
    RECONSTITUTED_BILAYER_SINGLE_CHANNEL_PATCH_RECORDING_EVIDENCE = "ECO_0005575"

    # voltage clamp recording evidence
    ECO_0005576 = "ECO_0005576"
    VOLTAGE_CLAMP_RECORDING_EVIDENCE = "ECO_0005576"

    # electroencephalography recording evidence
    ECO_0005577 = "ECO_0005577"
    ELECTROENCEPHALOGRAPHY_RECORDING_EVIDENCE = "ECO_0005577"

    # super-resolution microscopy evidence
    ECO_0005578 = "ECO_0005578"
    SUPER_RESOLUTION_MICROSCOPY_EVIDENCE = "ECO_0005578"

    # immunogold labelling evidence used in manual assertion
    ECO_0005579 = "ECO_0005579"
    IMMUNOGOLD_LABELLING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005579"

    # flow cytometry evidence used in manual assertion
    ECO_0005580 = "ECO_0005580"
    FLOW_CYTOMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005580"

    # enzyme-linked immunoabsorbent assay evidence used in manual assertion
    ECO_0005581 = "ECO_0005581"
    ENZYME_LINKED_IMMUNOABSORBENT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005581"
    )

    # cell-detached outside-out single-channel recording evidence
    ECO_0005582 = "ECO_0005582"
    CELL_DETACHED_OUTSIDE_OUT_SINGLE_CHANNEL_RECORDING_EVIDENCE = "ECO_0005582"

    # cut-open oocyte voltage clamp recording evidence
    ECO_0005583 = "ECO_0005583"
    CUT_OPEN_OOCYTE_VOLTAGE_CLAMP_RECORDING_EVIDENCE = "ECO_0005583"

    # macropatch voltage clamp recording evidence
    ECO_0005584 = "ECO_0005584"
    MACROPATCH_VOLTAGE_CLAMP_RECORDING_EVIDENCE = "ECO_0005584"

    # high throughput mass spectrometry evidence
    ECO_0005585 = "ECO_0005585"
    HIGH_THROUGHPUT_MASS_SPECTROMETRY_EVIDENCE = "ECO_0005585"

    # high throughput mass spectrometry evidence used in manual assertion
    ECO_0005586 = "ECO_0005586"
    HIGH_THROUGHPUT_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005586"

    # confocal microscopy evidence
    ECO_0005587 = "ECO_0005587"
    CONFOCAL_MICROSCOPY_EVIDENCE = "ECO_0005587"

    # wide-field microscopy evidence
    ECO_0005588 = "ECO_0005588"
    WIDE_FIELD_MICROSCOPY_EVIDENCE = "ECO_0005588"

    # confocal microscopy evidence used in manual assertion
    ECO_0005589 = "ECO_0005589"
    CONFOCAL_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005589"

    # wide-field microscopy evidence used in manual assertion
    ECO_0005590 = "ECO_0005590"
    WIDE_FIELD_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005590"

    # immunogold labelling electron microscopy assay evidence
    ECO_0005591 = "ECO_0005591"
    IMMUNOGOLD_LABELLING_ELECTRON_MICROSCOPY_ASSAY_EVIDENCE = "ECO_0005591"

    # immunogold labelling electron microscopy assay evidence used in manual assertion
    ECO_0005592 = "ECO_0005592"
    IMMUNOGOLD_LABELLING_ELECTRON_MICROSCOPY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005592"
    )

    # immunodetection assay evidence
    ECO_0005593 = "ECO_0005593"
    IMMUNODETECTION_ASSAY_EVIDENCE = "ECO_0005593"

    # immunoperoxidase immunolocalization evidence
    ECO_0005594 = "ECO_0005594"
    IMMUNOPEROXIDASE_IMMUNOLOCALIZATION_EVIDENCE = "ECO_0005594"

    # immunoperoxidase immunolocalization evidence used in manual assertion
    ECO_0005595 = "ECO_0005595"
    IMMUNOPEROXIDASE_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005595"
    )

    # immunoperoxidase immunolocalization electron microscopy evidence
    ECO_0005596 = "ECO_0005596"
    IMMUNOPEROXIDASE_IMMUNOLOCALIZATION_ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0005596"

    # immunoperoxidase immunolocalization electron microscopy evidence used in manual assertion
    ECO_0005597 = "ECO_0005597"
    IMMUNOPEROXIDASE_IMMUNOLOCALIZATION_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005597"
    )

    # wide-field fluorescence microscopy evidence
    ECO_0005598 = "ECO_0005598"
    WIDE_FIELD_FLUORESCENCE_MICROSCOPY_EVIDENCE = "ECO_0005598"

    # immunofluorescence wide-field microscopy evidence
    ECO_0005599 = "ECO_0005599"
    IMMUNOFLUORESCENCE_WIDE_FIELD_MICROSCOPY_EVIDENCE = "ECO_0005599"

    # immunofluorescence confocal microscopy evidence
    ECO_0005600 = "ECO_0005600"
    IMMUNOFLUORESCENCE_CONFOCAL_MICROSCOPY_EVIDENCE = "ECO_0005600"

    # immunofluorescence confocal microscopy evidence used in manual assertion
    ECO_0005601 = "ECO_0005601"
    IMMUNOFLUORESCENCE_CONFOCAL_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005601"
    )

    # protein mass spectrometry evidence
    ECO_0005603 = "ECO_0005603"
    PROTEIN_MASS_SPECTROMETRY_EVIDENCE = "ECO_0005603"

    # cross-streak test evidence
    ECO_0005604 = "ECO_0005604"
    CROSS_STREAK_TEST_EVIDENCE = "ECO_0005604"

    # disk diffusion test evidence
    ECO_0005605 = "ECO_0005605"
    DISK_DIFFUSION_TEST_EVIDENCE = "ECO_0005605"

    # cell transfection experiment evidence
    ECO_0005606 = "ECO_0005606"
    CELL_TRANSFECTION_EXPERIMENT_EVIDENCE = "ECO_0005606"

    # tethered cell assay evidence
    ECO_0005607 = "ECO_0005607"
    TETHERED_CELL_ASSAY_EVIDENCE = "ECO_0005607"

    # tumble frequency assay evidence
    ECO_0005608 = "ECO_0005608"
    TUMBLE_FREQUENCY_ASSAY_EVIDENCE = "ECO_0005608"

    # capillary assay evidence
    ECO_0005609 = "ECO_0005609"
    CAPILLARY_ASSAY_EVIDENCE = "ECO_0005609"

    # biological system reconstruction evidence based on homology evidence used in manual assertion
    ECO_0005610 = "ECO_0005610"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_HOMOLOGY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005610"
    )

    # inference from experimental data evidence
    ECO_0005611 = "ECO_0005611"
    INFERENCE_FROM_EXPERIMENTAL_DATA_EVIDENCE = "ECO_0005611"

    # inference from phenotype manipulation evidence
    ECO_0005612 = "ECO_0005612"
    INFERENCE_FROM_PHENOTYPE_MANIPULATION_EVIDENCE = "ECO_0005612"

    # inference by association of genotype from phenotype
    ECO_0005613 = "ECO_0005613"
    INFERENCE_BY_ASSOCIATION_OF_GENOTYPE_FROM_PHENOTYPE = "ECO_0005613"

    # two-dimensional polyacrylamide gel electrophoresis evidence used in manual assertion
    ECO_0005614 = "ECO_0005614"
    TWO_DIMENSIONAL_POLYACRYLAMIDE_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005614"
    )

    # alkaline phosphatase reporter gene assay evidence used in manual assertion
    ECO_0005615 = "ECO_0005615"
    ALKALINE_PHOSPHATASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005615"
    )

    # beta-galactosidase reporter gene assay evidence used in manual assertion
    ECO_0005616 = "ECO_0005616"
    BETA_GALACTOSIDASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005616"
    )

    # chloramphenicol acetyltransferase reporter gene assay evidence used in manual assertion
    ECO_0005617 = "ECO_0005617"
    CHLORAMPHENICOL_ACETYLTRANSFERASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005617"
    )

    # chromatin immunoprecipitation-chip evidence used in automatic assertion
    ECO_0005618 = "ECO_0005618"
    CHROMATIN_IMMUNOPRECIPITATION_CHIP_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005618"
    )

    # chromatin immunoprecipitation- exonuclease evidence used in automatic assertion
    ECO_0005619 = "ECO_0005619"
    CHROMATIN_IMMUNOPRECIPITATION__EXONUCLEASE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005619"
    )

    # chromatin immunoprecipitation-PCR evidence used in manual assertion
    ECO_0005620 = "ECO_0005620"
    CHROMATIN_IMMUNOPRECIPITATION_PCR_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005620"

    # chromatin immunoprecipitation-seq evidence used in automatic assertion
    ECO_0005621 = "ECO_0005621"
    CHROMATIN_IMMUNOPRECIPITATION_SEQ_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005621"
    )

    # comparative genomics motif search evidence used in manual assertion
    ECO_0005622 = "ECO_0005622"
    COMPARATIVE_GENOMICS_MOTIF_SEARCH_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005622"

    # comparative genomics motif search evidence used in automatic assertion
    ECO_0005623 = "ECO_0005623"
    COMPARATIVE_GENOMICS_MOTIF_SEARCH_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005623"
    )

    # consensus search evidence used in manual assertion
    ECO_0005624 = "ECO_0005624"
    CONSENSUS_SEARCH_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005624"

    # consensus search evidence used in automatic assertion
    ECO_0005625 = "ECO_0005625"
    CONSENSUS_SEARCH_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005625"

    # copper-phenanthroline footprinting evidence used in manual assertion
    ECO_0005626 = "ECO_0005626"
    COPPER_PHENANTHROLINE_FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005626"

    # DNA adenine methyltransferase identification evidence used in manual assertion
    ECO_0005627 = "ECO_0005627"
    DNA_ADENINE_METHYLTRANSFERASE_IDENTIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005627"
    )

    # DNA adenine methyltransferase identification evidence used in automatic assertion
    ECO_0005628 = "ECO_0005628"
    DNA_ADENINE_METHYLTRANSFERASE_IDENTIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005628"
    )

    # DNA affinity chromatography evidence used in manual assertion
    ECO_0005629 = "ECO_0005629"
    DNA_AFFINITY_CHROMATOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005629"

    # cDNA to DNA expression microarray evidence used in automatic assertion
    ECO_0005630 = "ECO_0005630"
    CDNA_TO_DNA_EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005630"
    )

    # DNAse footprinting evidence used in manual assertion
    ECO_0005631 = "ECO_0005631"
    DNASE_FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005631"

    # fluorescence anisotropy evidence used in manual assertion
    ECO_0005632 = "ECO_0005632"
    FLUORESCENCE_ANISOTROPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005632"

    # ferric uptake regulator titration assay evidence used in manual assertion
    ECO_0005633 = "ECO_0005633"
    FERRIC_UPTAKE_REGULATOR_TITRATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005633"
    )

    # genomic systematic evolution of ligands by exponential amplification evidence used in manual assertion
    ECO_0005634 = "ECO_0005634"
    GENOMIC_SYSTEMATIC_EVOLUTION_OF_LIGANDS_BY_EXPONENTIAL_AMPLIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005634"
    )

    # genomic systematic evolution of ligands by exponential amplification evidence used in automatic assertion
    ECO_0005635 = "ECO_0005635"
    GENOMIC_SYSTEMATIC_EVOLUTION_OF_LIGANDS_BY_EXPONENTIAL_AMPLIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005635"
    )

    # green fluorescent protein reporter gene assay evidence used in manual assertion
    ECO_0005636 = "ECO_0005636"
    GREEN_FLUORESCENT_PROTEIN_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005636"
    )

    # green fluorescent protein reporter gene assay evidence used in automatic assertion
    ECO_0005637 = "ECO_0005637"
    GREEN_FLUORESCENT_PROTEIN_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005637"
    )

    # cell growth regulation assay evidence used in manual assertion
    ECO_0005638 = "ECO_0005638"
    CELL_GROWTH_REGULATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005638"

    # cell growth regulation assay evidence used in automatic assertion
    ECO_0005639 = "ECO_0005639"
    CELL_GROWTH_REGULATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005639"

    # glutathione S-transferase pull-down assay evidence used in manual assertion
    ECO_0005640 = "ECO_0005640"
    GLUTATHIONE_S_TRANSFERASE_PULL_DOWN_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005640"
    )

    # beta-glucuronidase reporter gene assay evidence used in manual assertion
    ECO_0005641 = "ECO_0005641"
    BETA_GLUCURONIDASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005641"
    )

    # heteronuclear single quantum coherence spectroscopy evidence used in manual assertion
    ECO_0005642 = "ECO_0005642"
    HETERONUCLEAR_SINGLE_QUANTUM_COHERENCE_SPECTROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005642"
    )

    # hydroxyl-radical footprinting evidence used in manual assertion
    ECO_0005643 = "ECO_0005643"
    HYDROXYL_RADICAL_FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005643"

    # immunoprecipitation evidence used in manual assertion
    ECO_0005644 = "ECO_0005644"
    IMMUNOPRECIPITATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005644"

    # interferometric reflectance imaging sensor evidence used in manual assertion
    ECO_0005645 = "ECO_0005645"
    INTERFEROMETRIC_REFLECTANCE_IMAGING_SENSOR_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005645"
    )

    # interferometric reflectance imaging sensor evidence used in automatic assertion
    ECO_0005646 = "ECO_0005646"
    INTERFEROMETRIC_REFLECTANCE_IMAGING_SENSOR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005646"
    )

    # isothermal titration calorimetry evidence used in manual assertion
    ECO_0005647 = "ECO_0005647"
    ISOTHERMAL_TITRATION_CALORIMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005647"

    # luciferase reporter gene assay evidence used in manual assertion
    ECO_0005648 = "ECO_0005648"
    LUCIFERASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005648"

    # machine learning prediction of motif instance evidence used in manual assertion
    ECO_0005649 = "ECO_0005649"
    MACHINE_LEARNING_PREDICTION_OF_MOTIF_INSTANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005649"
    )

    # machine learning prediction of motif instance evidence used in automatic assertion
    ECO_0005650 = "ECO_0005650"
    MACHINE_LEARNING_PREDICTION_OF_MOTIF_INSTANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005650"
    )

    # matrix-assisted laser desorption/ionization time-of-flight mass spectrometry evidence used in automatic assertion
    ECO_0005651 = "ECO_0005651"
    MATRIX_ASSISTED_LASER_DESORPTION_IONIZATION_TIME_OF_FLIGHT_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005651"
    )

    # methidiumpropyl-ethylenediaminetetraacetic acid iron (II) footprinting evidence used in manual assertion
    ECO_0005652 = "ECO_0005652"
    METHIDIUMPROPYL_ETHYLENEDIAMINETETRAACETIC_ACID_IRON__II__FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005652"
    )

    # northern assay evidence used in manual assertion
    ECO_0005653 = "ECO_0005653"
    NORTHERN_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005653"

    # phylogenetic footprinting evidence used in manual assertion
    ECO_0005654 = "ECO_0005654"
    PHYLOGENETIC_FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005654"

    # phylogenetic footprinting evidence used in automatic assertion
    ECO_0005655 = "ECO_0005655"
    PHYLOGENETIC_FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005655"

    # methylation interference footprinting evidence used in manual assertion
    ECO_0005656 = "ECO_0005656"
    METHYLATION_INTERFERENCE_FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005656"
    )

    # primer extension assay evidence used in manual assertion
    ECO_0005657 = "ECO_0005657"
    PRIMER_EXTENSION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005657"

    # position-specific scoring matrix motif search evidence used in manual assertion
    ECO_0005658 = "ECO_0005658"
    POSITION_SPECIFIC_SCORING_MATRIX_MOTIF_SEARCH_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005658"
    )

    # position-specific scoring matrix motif search evidence used in automatic assertion
    ECO_0005659 = "ECO_0005659"
    POSITION_SPECIFIC_SCORING_MATRIX_MOTIF_SEARCH_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0005659"
    )

    # quantitative polymerase chain reaction evidence used in manual assertion
    ECO_0005660 = "ECO_0005660"
    QUANTITATIVE_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005660"
    )

    # rapid amplification of cDNA ends polymerase chain reaction evidence used in manual assertion
    ECO_0005661 = "ECO_0005661"
    RAPID_AMPLIFICATION_OF_CDNA_ENDS_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005661"
    )

    # regular expression motif search evidence used in manual assertion
    ECO_0005662 = "ECO_0005662"
    REGULAR_EXPRESSION_MOTIF_SEARCH_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005662"

    # regular expression motif search evidence used in automatic assertion
    ECO_0005663 = "ECO_0005663"
    REGULAR_EXPRESSION_MOTIF_SEARCH_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005663"

    # RNA sequencing assay evidence used in manual assertion
    ECO_0005664 = "ECO_0005664"
    RNA_SEQUENCING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005664"

    # RNA sequencing assay evidence used in automatic assertion
    ECO_0005665 = "ECO_0005665"
    RNA_SEQUENCING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005665"

    # S1 nuclease protection assay evidence used in manual assertion
    ECO_0005666 = "ECO_0005666"
    S1_NUCLEASE_PROTECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005666"

    # site-directed mutagenesis phenotypic evidence used in manual assertion
    ECO_0005667 = "ECO_0005667"
    SITE_DIRECTED_MUTAGENESIS_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005667"
    )

    # survival rate analysis evidence used in manual assertion
    ECO_0005668 = "ECO_0005668"
    SURVIVAL_RATE_ANALYSIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005668"

    # ultraviolet light footprinting evidence used in manual assertion
    ECO_0005669 = "ECO_0005669"
    ULTRAVIOLET_LIGHT_FOOTPRINTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005669"

    # x-ray crystallography evidence used in manual assertion
    ECO_0005670 = "ECO_0005670"
    X_RAY_CRYSTALLOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005670"

    # x-ray crystallography evidence used in automatic assertion
    ECO_0005671 = "ECO_0005671"
    X_RAY_CRYSTALLOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0005671"

    # xylE reporter gene assay evidence used in manual assertion
    ECO_0005672 = "ECO_0005672"
    XYLE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005672"

    # ad-hoc qualitative phenotype observation evidence
    ECO_0005673 = "ECO_0005673"
    AD_HOC_QUALITATIVE_PHENOTYPE_OBSERVATION_EVIDENCE = "ECO_0005673"

    # ad-hoc qualitative phenotype observation evidence used in manual assertion
    ECO_0005674 = "ECO_0005674"
    AD_HOC_QUALITATIVE_PHENOTYPE_OBSERVATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005674"
    )

    # ad-hoc quantitative phenotype observation evidence
    ECO_0005675 = "ECO_0005675"
    AD_HOC_QUANTITATIVE_PHENOTYPE_OBSERVATION_EVIDENCE = "ECO_0005675"

    # ad-hoc quantitative phenotype observation evidence used in manual assertion
    ECO_0005676 = "ECO_0005676"
    AD_HOC_QUANTITATIVE_PHENOTYPE_OBSERVATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0005676"
    )

    # dilution assay evidence
    ECO_0005800 = "ECO_0005800"
    DILUTION_ASSAY_EVIDENCE = "ECO_0005800"

    # enzymatic activity assay evidence used in manual assertion
    ECO_0005801 = "ECO_0005801"
    ENZYMATIC_ACTIVITY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005801"

    # cell transfection experiment evidence used in manual assertion
    ECO_0005802 = "ECO_0005802"
    CELL_TRANSFECTION_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005802"

    # motility assay evidence
    ECO_0005803 = "ECO_0005803"
    MOTILITY_ASSAY_EVIDENCE = "ECO_0005803"

    # immunofluorescence evidence used in manual assertion
    ECO_0005804 = "ECO_0005804"
    IMMUNOFLUORESCENCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005804"

    # yeast 2-hybrid evidence used in manual assertion
    ECO_0005805 = "ECO_0005805"
    YEAST_2_HYBRID_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0005805"

    # Cya fusion reporter assay evidence
    ECO_0006001 = "ECO_0006001"
    CYA_FUSION_REPORTER_ASSAY_EVIDENCE = "ECO_0006001"

    # Cya fusion reporter assay evidence used in manual assertion
    ECO_0006002 = "ECO_0006002"
    CYA_FUSION_REPORTER_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006002"

    # electron microscopy evidence used in manual assertion
    ECO_0006003 = "ECO_0006003"
    ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006003"

    # super-resolution microscopy evidence used in manual assertion
    ECO_0006004 = "ECO_0006004"
    SUPER_RESOLUTION_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006004"

    # fractionation evidence used in manual assertion
    ECO_0006005 = "ECO_0006005"
    FRACTIONATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006005"

    # electrophysiology assay evidence used in manual assertion
    ECO_0006006 = "ECO_0006006"
    ELECTROPHYSIOLOGY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006006"

    # chromatin immunoprecipitation-chip evidence used in manual assertion
    ECO_0006007 = "ECO_0006007"
    CHROMATIN_IMMUNOPRECIPITATION_CHIP_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006007"

    # chromatin immunoprecipitation- exonuclease evidence used in manual assertion
    ECO_0006008 = "ECO_0006008"
    CHROMATIN_IMMUNOPRECIPITATION__EXONUCLEASE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006008"
    )

    # chromatin immunoprecipitation-seq evidence used in manual assertion
    ECO_0006009 = "ECO_0006009"
    CHROMATIN_IMMUNOPRECIPITATION_SEQ_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006009"

    # mRNA interactome capture evidence
    ECO_0006010 = "ECO_0006010"
    MRNA_INTERACTOME_CAPTURE_EVIDENCE = "ECO_0006010"

    # mRNA interactome capture evidence used in manual assertion
    ECO_0006011 = "ECO_0006011"
    MRNA_INTERACTOME_CAPTURE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006011"

    # patch-clamp recording evidence
    ECO_0006012 = "ECO_0006012"
    PATCH_CLAMP_RECORDING_EVIDENCE = "ECO_0006012"

    # patch-clamp recording evidence used in manual assertion
    ECO_0006013 = "ECO_0006013"
    PATCH_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006013"

    # whole-cell patch-clamp recording evidence
    ECO_0006014 = "ECO_0006014"
    WHOLE_CELL_PATCH_CLAMP_RECORDING_EVIDENCE = "ECO_0006014"

    # whole-cell patch-clamp recording evidence used in manual assertion
    ECO_0006015 = "ECO_0006015"
    WHOLE_CELL_PATCH_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006015"

    # author statement from published clinical study
    ECO_0006016 = "ECO_0006016"
    AUTHOR_STATEMENT_FROM_PUBLISHED_CLINICAL_STUDY = "ECO_0006016"

    # author statement from published clinical study used in manual assertion
    ECO_0006017 = "ECO_0006017"
    AUTHOR_STATEMENT_FROM_PUBLISHED_CLINICAL_STUDY_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006017"
    )

    # inference based on individual clinical experience
    ECO_0006018 = "ECO_0006018"
    INFERENCE_BASED_ON_INDIVIDUAL_CLINICAL_EXPERIENCE = "ECO_0006018"

    # inference based on individual clinical experience used in manual assertion
    ECO_0006019 = "ECO_0006019"
    INFERENCE_BASED_ON_INDIVIDUAL_CLINICAL_EXPERIENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006019"
    )

    # biofilm formation assay evidence
    ECO_0006020 = "ECO_0006020"
    BIOFILM_FORMATION_ASSAY_EVIDENCE = "ECO_0006020"

    # biofilm formation assay evidence used in manual assertion
    ECO_0006021 = "ECO_0006021"
    BIOFILM_FORMATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006021"

    # microtiter plate biofilm assay evidence
    ECO_0006022 = "ECO_0006022"
    MICROTITER_PLATE_BIOFILM_ASSAY_EVIDENCE = "ECO_0006022"

    # microtiter plate biofilm assay evidence used in manual assertion
    ECO_0006023 = "ECO_0006023"
    MICROTITER_PLATE_BIOFILM_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006023"

    # air-liquid interface assay evidence
    ECO_0006024 = "ECO_0006024"
    AIR_LIQUID_INTERFACE_ASSAY_EVIDENCE = "ECO_0006024"

    # air-liquid interface assay evidence used in manual assertion
    ECO_0006025 = "ECO_0006025"
    AIR_LIQUID_INTERFACE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006025"

    # colony biofilm assay evidence
    ECO_0006026 = "ECO_0006026"
    COLONY_BIOFILM_ASSAY_EVIDENCE = "ECO_0006026"

    # colony biofilm assay evidence used in manual assertion
    ECO_0006027 = "ECO_0006027"
    COLONY_BIOFILM_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006027"

    # Kadouri drip-fed biofilm assay evidence
    ECO_0006028 = "ECO_0006028"
    KADOURI_DRIP_FED_BIOFILM_ASSAY_EVIDENCE = "ECO_0006028"

    # Kadouri drip-fed biofilm assay evidence used in manual assertion
    ECO_0006029 = "ECO_0006029"
    KADOURI_DRIP_FED_BIOFILM_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006029"

    # co-immunoprecipitation evidence used in manual assertion
    ECO_0006030 = "ECO_0006030"
    CO_IMMUNOPRECIPITATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006030"

    # immunolocalization evidence used in manual assertion
    ECO_0006031 = "ECO_0006031"
    IMMUNOLOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006031"

    # optogenetic evidence
    ECO_0006032 = "ECO_0006032"
    OPTOGENETIC_EVIDENCE = "ECO_0006032"

    # optogenetic evidence used in manual assertion
    ECO_0006033 = "ECO_0006033"
    OPTOGENETIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006033"

    # fluorescent sensor evidence
    ECO_0006034 = "ECO_0006034"
    FLUORESCENT_SENSOR_EVIDENCE = "ECO_0006034"

    # fluorescent sensor evidence used in manual assertion
    ECO_0006035 = "ECO_0006035"
    FLUORESCENT_SENSOR_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006035"

    # genetically encoded fluorescent sensor evidence
    ECO_0006036 = "ECO_0006036"
    GENETICALLY_ENCODED_FLUORESCENT_SENSOR_EVIDENCE = "ECO_0006036"

    # genetically encoded fluorescent sensor evidence used in manual assertion
    ECO_0006037 = "ECO_0006037"
    GENETICALLY_ENCODED_FLUORESCENT_SENSOR_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006037"
    )

    # genetically encoded fluorescent electrophysiology assay evidence
    ECO_0006038 = "ECO_0006038"
    GENETICALLY_ENCODED_FLUORESCENT_ELECTROPHYSIOLOGY_ASSAY_EVIDENCE = "ECO_0006038"

    # genetically encoded fluorescent electrophysiology assay evidence used in manual assertion
    ECO_0006039 = "ECO_0006039"
    GENETICALLY_ENCODED_FLUORESCENT_ELECTROPHYSIOLOGY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006039"
    )

    # genetically encoded fluorescent ion concentration sensor assay evidence
    ECO_0006040 = "ECO_0006040"
    GENETICALLY_ENCODED_FLUORESCENT_ION_CONCENTRATION_SENSOR_ASSAY_EVIDENCE = (
        "ECO_0006040"
    )

    # genetically encoded fluorescent ion concentration sensor assay evidence used in manual assertion
    ECO_0006041 = "ECO_0006041"
    GENETICALLY_ENCODED_FLUORESCENT_ION_CONCENTRATION_SENSOR_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006041"
    )

    # cell fractionation evidence used in manual assertion
    ECO_0006042 = "ECO_0006042"
    CELL_FRACTIONATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006042"

    # extracellular recording evidence
    ECO_0006043 = "ECO_0006043"
    EXTRACELLULAR_RECORDING_EVIDENCE = "ECO_0006043"

    # extracellular recording evidence used in manual assertion
    ECO_0006044 = "ECO_0006044"
    EXTRACELLULAR_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006044"

    # single-unit extracellular recording evidence
    ECO_0006045 = "ECO_0006045"
    SINGLE_UNIT_EXTRACELLULAR_RECORDING_EVIDENCE = "ECO_0006045"

    # single-unit extracellular recording evidence used in manual assertion
    ECO_0006046 = "ECO_0006046"
    SINGLE_UNIT_EXTRACELLULAR_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006046"
    )

    # field potential recording evidence
    ECO_0006047 = "ECO_0006047"
    FIELD_POTENTIAL_RECORDING_EVIDENCE = "ECO_0006047"

    # field potential recording evidence used in manual assertion
    ECO_0006048 = "ECO_0006048"
    FIELD_POTENTIAL_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006048"

    # genetic transformation evidence used in manual assertion
    ECO_0006049 = "ECO_0006049"
    GENETIC_TRANSFORMATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006049"

    # anti-sense experiment evidence used in manual assertion
    ECO_0006050 = "ECO_0006050"
    ANTI_SENSE_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006050"

    # morpholino experiment evidence used in manual assertion
    ECO_0006051 = "ECO_0006051"
    MORPHOLINO_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006051"

    # RNAi evidence used in manual assertion
    ECO_0006052 = "ECO_0006052"
    RNAI_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006052"

    # pharmacological assay evidence
    ECO_0006053 = "ECO_0006053"
    PHARMACOLOGICAL_ASSAY_EVIDENCE = "ECO_0006053"

    # pharmacological assay evidence used in manual assertion
    ECO_0006054 = "ECO_0006054"
    PHARMACOLOGICAL_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006054"

    # high throughput evidence
    ECO_0006055 = "ECO_0006055"
    HIGH_THROUGHPUT_EVIDENCE = "ECO_0006055"

    # high throughput evidence used in manual assertion
    ECO_0006056 = "ECO_0006056"
    HIGH_THROUGHPUT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006056"

    # high throughput evidence used in automatic assertion
    ECO_0006057 = "ECO_0006057"
    HIGH_THROUGHPUT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006057"

    # high throughput cell biology evidence
    ECO_0006058 = "ECO_0006058"
    HIGH_THROUGHPUT_CELL_BIOLOGY_EVIDENCE = "ECO_0006058"

    # high throughput cell biology evidence used in manual assertion
    ECO_0006059 = "ECO_0006059"
    HIGH_THROUGHPUT_CELL_BIOLOGY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006059"

    # high throughput cell biology evidence used in automatic assertion
    ECO_0006060 = "ECO_0006060"
    HIGH_THROUGHPUT_CELL_BIOLOGY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006060"

    # immunofluorescence wide-field microscopy evidence used in manual assertion
    ECO_0006061 = "ECO_0006061"
    IMMUNOFLUORESCENCE_WIDE_FIELD_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006061"
    )

    # wide-field fluorescence microscopy evidence used in manual assertion
    ECO_0006062 = "ECO_0006062"
    WIDE_FIELD_FLUORESCENCE_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006062"

    # over expression analysis evidence used in manual assertion
    ECO_0006063 = "ECO_0006063"
    OVER_EXPRESSION_ANALYSIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006063"

    # cell-free assay evidence used in manual assertion
    ECO_0006064 = "ECO_0006064"
    CELL_FREE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006064"

    # in vitro cell based assay evidence used in manual assertion
    ECO_0006065 = "ECO_0006065"
    IN_VITRO_CELL_BASED_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006065"

    # fluorescence recovery after photobleaching evidence
    ECO_0006066 = "ECO_0006066"
    FLUORESCENCE_RECOVERY_AFTER_PHOTOBLEACHING_EVIDENCE = "ECO_0006066"

    # fluorescence recovery after photobleaching evidence used in manual assertion
    ECO_0006067 = "ECO_0006067"
    FLUORESCENCE_RECOVERY_AFTER_PHOTOBLEACHING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006067"
    )

    # RNA-sequencing evidence used in manual assertion
    ECO_0006068 = "ECO_0006068"
    RNA_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006068"

    # RNA-sequencing evidence used in automatic assertion
    ECO_0006069 = "ECO_0006069"
    RNA_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006069"

    # immuno-labelling electron microscopy evidence
    ECO_0006070 = "ECO_0006070"
    IMMUNO_LABELLING_ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0006070"

    # immuno-labelling electron microscopy evidence used in manual assertion
    ECO_0006071 = "ECO_0006071"
    IMMUNO_LABELLING_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006071"
    )

    # immunofluorescence super resolution microscopy evidence
    ECO_0006072 = "ECO_0006072"
    IMMUNOFLUORESCENCE_SUPER_RESOLUTION_MICROSCOPY_EVIDENCE = "ECO_0006072"

    # immunofluorescence super resolution microscopy evidence used in manual assertion
    ECO_0006073 = "ECO_0006073"
    IMMUNOFLUORESCENCE_SUPER_RESOLUTION_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006073"
    )

    # co-purification evidence used in manual assertion
    ECO_0006074 = "ECO_0006074"
    CO_PURIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006074"

    # affinity evidence used in manual assertion
    ECO_0006075 = "ECO_0006075"
    AFFINITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006075"

    # protein binding evidence used in manual assertion
    ECO_0006076 = "ECO_0006076"
    PROTEIN_BINDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006076"

    # bait-prey hybrid interaction evidence used in manual assertion
    ECO_0006077 = "ECO_0006077"
    BAIT_PREY_HYBRID_INTERACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006077"

    # immunological assay evidence used in manual assertion
    ECO_0006078 = "ECO_0006078"
    IMMUNOLOGICAL_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006078"

    # yeast one-hybrid evidence used in manual assertion
    ECO_0006079 = "ECO_0006079"
    YEAST_ONE_HYBRID_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006079"

    # split-ubiquitin functional complementation evidence used in manual assertion
    ECO_0006080 = "ECO_0006080"
    SPLIT_UBIQUITIN_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006080"
    )

    # far-Western blotting evidence used in manual assertion
    ECO_0006081 = "ECO_0006081"
    FAR_WESTERN_BLOTTING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006081"

    # affinity chromatography evidence used in manual assertion
    ECO_0006082 = "ECO_0006082"
    AFFINITY_CHROMATOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006082"

    # nucleic acid binding evidence used in manual assertion
    ECO_0006083 = "ECO_0006083"
    NUCLEIC_ACID_BINDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006083"

    # ribohomopolymer binding assay evidence used in manual assertion
    ECO_0006084 = "ECO_0006084"
    RIBOHOMOPOLYMER_BINDING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006084"

    # protein:ion binding evidence used in manual assertion
    ECO_0006085 = "ECO_0006085"
    PROTEIN_ION_BINDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006085"

    # Southwestern blot evidence used in manual assertion
    ECO_0006086 = "ECO_0006086"
    SOUTHWESTERN_BLOT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006086"

    # Northwestern blot evidence used in manual assertion
    ECO_0006087 = "ECO_0006087"
    NORTHWESTERN_BLOT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006087"

    # systematic evolution of ligands by exponential amplification evidence used in manual assertion
    ECO_0006088 = "ECO_0006088"
    SYSTEMATIC_EVOLUTION_OF_LIGANDS_BY_EXPONENTIAL_AMPLIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006088"
    )

    # bacterial one-hybrid evidence used in manual assertion
    ECO_0006089 = "ECO_0006089"
    BACTERIAL_ONE_HYBRID_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006089"

    # protein-oligonucleotide microarray binding evidence used in manual assertion
    ECO_0006090 = "ECO_0006090"
    PROTEIN_OLIGONUCLEOTIDE_MICROARRAY_BINDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006090"
    )

    # functional complementation evidence used in manual assertion
    ECO_0006091 = "ECO_0006091"
    FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006091"

    # transgenic rescue experiment evidence used in manual assertion
    ECO_0006092 = "ECO_0006092"
    TRANSGENIC_RESCUE_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006092"

    # transient rescue experiment evidence used in manual assertion
    ECO_0006093 = "ECO_0006093"
    TRANSIENT_RESCUE_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006093"

    # suppressor/enhancer interaction phenotypic evidence used in manual assertion
    ECO_0006094 = "ECO_0006094"
    SUPPRESSOR_ENHANCER_INTERACTION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006094"
    )

    # double mutant phenotypic evidence used in manual assertion
    ECO_0006095 = "ECO_0006095"
    DOUBLE_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006095"

    # epistatic interaction phenotypic evidence used in manual assertion
    ECO_0006096 = "ECO_0006096"
    EPISTATIC_INTERACTION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006096"

    # functional complementation in heterologous system evidence used in manual assertion
    ECO_0006097 = "ECO_0006097"
    FUNCTIONAL_COMPLEMENTATION_IN_HETEROLOGOUS_SYSTEM_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006097"
    )

    # temperature-sensitive mutant phenotypic evidence
    ECO_0006098 = "ECO_0006098"
    TEMPERATURE_SENSITIVE_MUTANT_PHENOTYPIC_EVIDENCE = "ECO_0006098"

    # temperature-sensitive mutant phenotypic evidence used in manual assertion
    ECO_0006099 = "ECO_0006099"
    TEMPERATURE_SENSITIVE_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006099"
    )

    # recessive mutant phenotype evidence
    ECO_0006100 = "ECO_0006100"
    RECESSIVE_MUTANT_PHENOTYPE_EVIDENCE = "ECO_0006100"

    # recessive mutant phenotype evidence used in manual assertion
    ECO_0006101 = "ECO_0006101"
    RECESSIVE_MUTANT_PHENOTYPE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006101"

    # quantum mechanics/molecular mechanics simulation evidence
    ECO_0006135 = "ECO_0006135"
    QUANTUM_MECHANICS_MOLECULAR_MECHANICS_SIMULATION_EVIDENCE = "ECO_0006135"

    # quantum mechanics/molecular mechanics simulation evidence used in automatic assertion
    ECO_0006136 = "ECO_0006136"
    QUANTUM_MECHANICS_MOLECULAR_MECHANICS_SIMULATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006136"
    )

    # quantum mechanics/molecular mechanics simulation evidence used in manual assertion
    ECO_0006137 = "ECO_0006137"
    QUANTUM_MECHANICS_MOLECULAR_MECHANICS_SIMULATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006137"
    )

    # molecular mechanics simulation evidence
    ECO_0006138 = "ECO_0006138"
    MOLECULAR_MECHANICS_SIMULATION_EVIDENCE = "ECO_0006138"

    # molecular mechanics simulation evidence used in automatic assertion
    ECO_0006139 = "ECO_0006139"
    MOLECULAR_MECHANICS_SIMULATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006139"

    # molecular mechanics simulation evidence used in manual assertion
    ECO_0006140 = "ECO_0006140"
    MOLECULAR_MECHANICS_SIMULATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006140"

    # quantum mechanics simulation evidence
    ECO_0006141 = "ECO_0006141"
    QUANTUM_MECHANICS_SIMULATION_EVIDENCE = "ECO_0006141"

    # quantum mechanics simulation evidence used in automatic assertion
    ECO_0006142 = "ECO_0006142"
    QUANTUM_MECHANICS_SIMULATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006142"

    # quantum mechanics simulation evidence used in manual assertion
    ECO_0006143 = "ECO_0006143"
    QUANTUM_MECHANICS_SIMULATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006143"

    # density functional theory simulation evidence
    ECO_0006144 = "ECO_0006144"
    DENSITY_FUNCTIONAL_THEORY_SIMULATION_EVIDENCE = "ECO_0006144"

    # density functional theory simulation evidence used in manual assertion
    ECO_0006145 = "ECO_0006145"
    DENSITY_FUNCTIONAL_THEORY_SIMULATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006145"
    )

    # density functional theory simulation evidence used in automatic assertion
    ECO_0006146 = "ECO_0006146"
    DENSITY_FUNCTIONAL_THEORY_SIMULATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006146"
    )

    # documented statement evidence
    ECO_0006151 = "ECO_0006151"
    DOCUMENTED_STATEMENT_EVIDENCE = "ECO_0006151"

    # medical practitioner statement evidence
    ECO_0006152 = "ECO_0006152"
    MEDICAL_PRACTITIONER_STATEMENT_EVIDENCE = "ECO_0006152"

    # self-reported individual's statement evidence
    ECO_0006153 = "ECO_0006153"
    SELF_REPORTED_INDIVIDUAL_S_STATEMENT_EVIDENCE = "ECO_0006153"

    # self-reported patient statement evidence
    ECO_0006154 = "ECO_0006154"
    SELF_REPORTED_PATIENT_STATEMENT_EVIDENCE = "ECO_0006154"

    # documented statement evidence used in manual assertion
    ECO_0006155 = "ECO_0006155"
    DOCUMENTED_STATEMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006155"

    # documented statement evidence used in automatic assertion
    ECO_0006156 = "ECO_0006156"
    DOCUMENTED_STATEMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006156"

    # self-reported individual's statement evidence used in manual assertion
    ECO_0006157 = "ECO_0006157"
    SELF_REPORTED_INDIVIDUAL_S_STATEMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006157"
    )

    # self-reported individual's statement evidence used in automatic assertion
    ECO_0006158 = "ECO_0006158"
    SELF_REPORTED_INDIVIDUAL_S_STATEMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006158"
    )

    # self-reported patient statement evidence used in manual assertion
    ECO_0006159 = "ECO_0006159"
    SELF_REPORTED_PATIENT_STATEMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006159"

    # self-reported patient statement evidence used in automatic assertion
    ECO_0006160 = "ECO_0006160"
    SELF_REPORTED_PATIENT_STATEMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006160"

    # medical practitioner statement evidence used in manual assertion
    ECO_0006161 = "ECO_0006161"
    MEDICAL_PRACTITIONER_STATEMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006161"

    # medical practitioner statement evidence used in automatic assertion
    ECO_0006162 = "ECO_0006162"
    MEDICAL_PRACTITIONER_STATEMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006162"

    # nuclear magnetic resonance spectroscopy evidence
    ECO_0006163 = "ECO_0006163"
    NUCLEAR_MAGNETIC_RESONANCE_SPECTROSCOPY_EVIDENCE = "ECO_0006163"

    # nuclear magnetic resonance spectroscopy evidence used in automatic assertion
    ECO_0006164 = "ECO_0006164"
    NUCLEAR_MAGNETIC_RESONANCE_SPECTROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006164"
    )

    # nuclear magnetic resonance spectroscopy evidence used in manual assertion
    ECO_0006165 = "ECO_0006165"
    NUCLEAR_MAGNETIC_RESONANCE_SPECTROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006165"
    )

    # nuclear magnetic resonance imaging evidence
    ECO_0006166 = "ECO_0006166"
    NUCLEAR_MAGNETIC_RESONANCE_IMAGING_EVIDENCE = "ECO_0006166"

    # nuclear magnetic resonance imaging evidence used in automatic assertion
    ECO_0006167 = "ECO_0006167"
    NUCLEAR_MAGNETIC_RESONANCE_IMAGING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006167"
    )

    # nuclear magnetic resonance imaging evidence used in manual assertion
    ECO_0006168 = "ECO_0006168"
    NUCLEAR_MAGNETIC_RESONANCE_IMAGING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006168"

    # quantitative western immunoblotting evidence
    ECO_0006169 = "ECO_0006169"
    QUANTITATIVE_WESTERN_IMMUNOBLOTTING_EVIDENCE = "ECO_0006169"

    # quantitative western immunoblotting evidence used in manual evidence
    ECO_0006170 = "ECO_0006170"
    QUANTITATIVE_WESTERN_IMMUNOBLOTTING_EVIDENCE_USED_IN_MANUAL_EVIDENCE = "ECO_0006170"

    # quantitative western immunoblotting evidence used in automatic assertion
    ECO_0006171 = "ECO_0006171"
    QUANTITATIVE_WESTERN_IMMUNOBLOTTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006171"
    )

    # mixed support of intron positions by RNA-sequencing alignment evidence
    ECO_0006172 = "ECO_0006172"
    MIXED_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE = (
        "ECO_0006172"
    )

    # mixed support of intron positions by RNA-sequencing alignment evidence used in automatic assertion
    ECO_0006173 = "ECO_0006173"
    MIXED_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006173"
    )

    # mixed support of intron positions by RNA-sequencing alignment evidence used in manual assertion
    ECO_0006174 = "ECO_0006174"
    MIXED_SUPPORT_OF_INTRON_POSITIONS_BY_RNA_SEQUENCING_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006174"
    )

    # nuclear magnetic resonance spectroscopy-based hydrogen-deuterium exchange evidence
    ECO_0006175 = "ECO_0006175"
    NUCLEAR_MAGNETIC_RESONANCE_SPECTROSCOPY_BASED_HYDROGEN_DEUTERIUM_EXCHANGE_EVIDENCE = (
        "ECO_0006175"
    )

    # proton-based nuclear magnetic resonance evidence
    ECO_0006176 = "ECO_0006176"
    PROTON_BASED_NUCLEAR_MAGNETIC_RESONANCE_EVIDENCE = "ECO_0006176"

    # circular dichroism evidence
    ECO_0006177 = "ECO_0006177"
    CIRCULAR_DICHROISM_EVIDENCE = "ECO_0006177"

    # synchrotron radiation circular dichroism evidence
    ECO_0006178 = "ECO_0006178"
    SYNCHROTRON_RADIATION_CIRCULAR_DICHROISM_EVIDENCE = "ECO_0006178"

    # far-UV circular dichroism evidence
    ECO_0006179 = "ECO_0006179"
    FAR_UV_CIRCULAR_DICHROISM_EVIDENCE = "ECO_0006179"

    # near-UV circular dichroism evidence
    ECO_0006180 = "ECO_0006180"
    NEAR_UV_CIRCULAR_DICHROISM_EVIDENCE = "ECO_0006180"

    # cryogenic electron microscopy evidence
    ECO_0006181 = "ECO_0006181"
    CRYOGENIC_ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0006181"

    # small-angle X-ray scattering evidence
    ECO_0006182 = "ECO_0006182"
    SMALL_ANGLE_X_RAY_SCATTERING_EVIDENCE = "ECO_0006182"

    # particle scattering evidence
    ECO_0006183 = "ECO_0006183"
    PARTICLE_SCATTERING_EVIDENCE = "ECO_0006183"

    # small-angle neutron scattering evidence
    ECO_0006184 = "ECO_0006184"
    SMALL_ANGLE_NEUTRON_SCATTERING_EVIDENCE = "ECO_0006184"

    # author inference
    ECO_0006185 = "ECO_0006185"
    AUTHOR_INFERENCE = "ECO_0006185"

    # combinatorial experimental and author inference evidence contained in single publication
    ECO_0006186 = "ECO_0006186"
    COMBINATORIAL_EXPERIMENTAL_AND_AUTHOR_INFERENCE_EVIDENCE_CONTAINED_IN_SINGLE_PUBLICATION = (
        "ECO_0006186"
    )

    # X-ray crystallography-based structural model with missing residue coordinates
    ECO_0006187 = "ECO_0006187"
    X_RAY_CRYSTALLOGRAPHY_BASED_STRUCTURAL_MODEL_WITH_MISSING_RESIDUE_COORDINATES = (
        "ECO_0006187"
    )

    # X-ray crystallography-based structural model with high relative B-factor values
    ECO_0006188 = "ECO_0006188"
    X_RAY_CRYSTALLOGRAPHY_BASED_STRUCTURAL_MODEL_WITH_HIGH_RELATIVE_B_FACTOR_VALUES = (
        "ECO_0006188"
    )

    # cryogenic electron microscopy-based structural model with missing residue coordinates
    ECO_0006189 = "ECO_0006189"
    CRYOGENIC_ELECTRON_MICROSCOPY_BASED_STRUCTURAL_MODEL_WITH_MISSING_RESIDUE_COORDINATES = (
        "ECO_0006189"
    )

    # cryogenic electron microscopy-based structural model with high relative B-factor values
    ECO_0006190 = "ECO_0006190"
    CRYOGENIC_ELECTRON_MICROSCOPY_BASED_STRUCTURAL_MODEL_WITH_HIGH_RELATIVE_B_FACTOR_VALUES = (
        "ECO_0006190"
    )

    # Fourier-transform infrared spectroscopy evidence
    ECO_0006191 = "ECO_0006191"
    FOURIER_TRANSFORM_INFRARED_SPECTROSCOPY_EVIDENCE = "ECO_0006191"

    # heat capacity-based evidence
    ECO_0006192 = "ECO_0006192"
    HEAT_CAPACITY_BASED_EVIDENCE = "ECO_0006192"

    # differential scanning calorimetry evidence
    ECO_0006193 = "ECO_0006193"
    DIFFERENTIAL_SCANNING_CALORIMETRY_EVIDENCE = "ECO_0006193"

    # selective antibody-based structural conformation evidence
    ECO_0006194 = "ECO_0006194"
    SELECTIVE_ANTIBODY_BASED_STRUCTURAL_CONFORMATION_EVIDENCE = "ECO_0006194"

    # protein hydrogen-deuterium exchange mass spectrometry evidence
    ECO_0006195 = "ECO_0006195"
    PROTEIN_HYDROGEN_DEUTERIUM_EXCHANGE_MASS_SPECTROMETRY_EVIDENCE = "ECO_0006195"

    # nuclear magnetic resonance spectroscopy-based hydrogen-deuterium exchange evidence used in manual assertion
    ECO_0006196 = "ECO_0006196"
    NUCLEAR_MAGNETIC_RESONANCE_SPECTROSCOPY_BASED_HYDROGEN_DEUTERIUM_EXCHANGE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006196"
    )

    # nuclear magnetic resonance spectroscopy-based hydrogen-deuterium exchange evidence used in automatic assertion
    ECO_0006197 = "ECO_0006197"
    NUCLEAR_MAGNETIC_RESONANCE_SPECTROSCOPY_BASED_HYDROGEN_DEUTERIUM_EXCHANGE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006197"
    )

    # proton-based nuclear magnetic resonance evidence used in manual assertion
    ECO_0006198 = "ECO_0006198"
    PROTON_BASED_NUCLEAR_MAGNETIC_RESONANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006198"
    )

    # proton-based nuclear magnetic resonance evidence used in automatic assertion
    ECO_0006199 = "ECO_0006199"
    PROTON_BASED_NUCLEAR_MAGNETIC_RESONANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006199"
    )

    # circular dichroism evidence used in manual assertion
    ECO_0006200 = "ECO_0006200"
    CIRCULAR_DICHROISM_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006200"

    # circular dichroism evidence used in automatic assertion
    ECO_0006201 = "ECO_0006201"
    CIRCULAR_DICHROISM_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006201"

    # synchrotron radiation circular dichroism evidence used in manual assertion
    ECO_0006202 = "ECO_0006202"
    SYNCHROTRON_RADIATION_CIRCULAR_DICHROISM_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006202"
    )

    # synchrotron radiation circular dichroism evidence used in automatic assertion
    ECO_0006203 = "ECO_0006203"
    SYNCHROTRON_RADIATION_CIRCULAR_DICHROISM_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006203"
    )

    # far-UV circular dichroism evidence used in manual assertion
    ECO_0006204 = "ECO_0006204"
    FAR_UV_CIRCULAR_DICHROISM_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006204"

    # far-UV circular dichroism evidence used in automatic assertion
    ECO_0006205 = "ECO_0006205"
    FAR_UV_CIRCULAR_DICHROISM_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006205"

    # near-UV circular dichroism evidence used in manual assertion
    ECO_0006206 = "ECO_0006206"
    NEAR_UV_CIRCULAR_DICHROISM_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006206"

    # near-UV circular dichroism evidence used in automatic assertion
    ECO_0006207 = "ECO_0006207"
    NEAR_UV_CIRCULAR_DICHROISM_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006207"

    # cryogenic electron microscopy evidence used in manual assertion
    ECO_0006208 = "ECO_0006208"
    CRYOGENIC_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006208"

    # cryogenic electron microscopy evidence used in automatic assertion
    ECO_0006209 = "ECO_0006209"
    CRYOGENIC_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006209"

    # small-angle X-ray scattering evidence used in manual assertion
    ECO_0006210 = "ECO_0006210"
    SMALL_ANGLE_X_RAY_SCATTERING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006210"

    # small-angle X-ray scattering evidence used in automatic assertion
    ECO_0006211 = "ECO_0006211"
    SMALL_ANGLE_X_RAY_SCATTERING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006211"

    # particle scattering evidence used in manual assertion
    ECO_0006212 = "ECO_0006212"
    PARTICLE_SCATTERING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006212"

    # particle scattering evidence used in automatic assertion
    ECO_0006213 = "ECO_0006213"
    PARTICLE_SCATTERING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006213"

    # small-angle neutron scattering evidence used in manual assertion
    ECO_0006214 = "ECO_0006214"
    SMALL_ANGLE_NEUTRON_SCATTERING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006214"

    # small-angle neutron scattering evidence used in automatic assertion
    ECO_0006215 = "ECO_0006215"
    SMALL_ANGLE_NEUTRON_SCATTERING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006215"

    # author inference used in manual assertion
    ECO_0006216 = "ECO_0006216"
    AUTHOR_INFERENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006216"

    # author inference used in automatic assertion
    ECO_0006217 = "ECO_0006217"
    AUTHOR_INFERENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006217"

    # combinatorial experimental and author inference evidence contained in single publication used in manual assertion
    ECO_0006218 = "ECO_0006218"
    COMBINATORIAL_EXPERIMENTAL_AND_AUTHOR_INFERENCE_EVIDENCE_CONTAINED_IN_SINGLE_PUBLICATION_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006218"
    )

    # combinatorial experimental and author inference evidence contained in single publication used in automatic assertion
    ECO_0006219 = "ECO_0006219"
    COMBINATORIAL_EXPERIMENTAL_AND_AUTHOR_INFERENCE_EVIDENCE_CONTAINED_IN_SINGLE_PUBLICATION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006219"
    )

    # X-ray crystallography-based structural model with missing residue coordinates used in manual assertion
    ECO_0006220 = "ECO_0006220"
    X_RAY_CRYSTALLOGRAPHY_BASED_STRUCTURAL_MODEL_WITH_MISSING_RESIDUE_COORDINATES_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006220"
    )

    # X-ray crystallography-based structural model with missing residue coordinates used in automatic assertion
    ECO_0006221 = "ECO_0006221"
    X_RAY_CRYSTALLOGRAPHY_BASED_STRUCTURAL_MODEL_WITH_MISSING_RESIDUE_COORDINATES_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006221"
    )

    # X-ray crystallography-based structural model with high relative B-factor values used in manual assertion
    ECO_0006222 = "ECO_0006222"
    X_RAY_CRYSTALLOGRAPHY_BASED_STRUCTURAL_MODEL_WITH_HIGH_RELATIVE_B_FACTOR_VALUES_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006222"
    )

    # X-ray crystallography-based structural model with high relative B-factor values used in automatic assertion
    ECO_0006223 = "ECO_0006223"
    X_RAY_CRYSTALLOGRAPHY_BASED_STRUCTURAL_MODEL_WITH_HIGH_RELATIVE_B_FACTOR_VALUES_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006223"
    )

    # cryogenic electron microscopy-based structural model with missing residue coordinates used in manual assertion
    ECO_0006224 = "ECO_0006224"
    CRYOGENIC_ELECTRON_MICROSCOPY_BASED_STRUCTURAL_MODEL_WITH_MISSING_RESIDUE_COORDINATES_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006224"
    )

    # cryogenic electron microscopy-based structural model with missing residue coordinates used in automatic assertion
    ECO_0006225 = "ECO_0006225"
    CRYOGENIC_ELECTRON_MICROSCOPY_BASED_STRUCTURAL_MODEL_WITH_MISSING_RESIDUE_COORDINATES_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006225"
    )

    # cryogenic electron microscopy-based structural model with high relative B-factor values used in manual assertion
    ECO_0006226 = "ECO_0006226"
    CRYOGENIC_ELECTRON_MICROSCOPY_BASED_STRUCTURAL_MODEL_WITH_HIGH_RELATIVE_B_FACTOR_VALUES_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006226"
    )

    # cryogenic electron microscopy-based structural model with high relative B-factor values used in automatic assertion
    ECO_0006227 = "ECO_0006227"
    CRYOGENIC_ELECTRON_MICROSCOPY_BASED_STRUCTURAL_MODEL_WITH_HIGH_RELATIVE_B_FACTOR_VALUES_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006227"
    )

    # Fourier-transform infrared spectroscopy evidence used in manual assertion
    ECO_0006228 = "ECO_0006228"
    FOURIER_TRANSFORM_INFRARED_SPECTROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006228"
    )

    # Fourier-transform infrared spectroscopy evidence used in automatic assertion
    ECO_0006229 = "ECO_0006229"
    FOURIER_TRANSFORM_INFRARED_SPECTROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006229"
    )

    # heat capacity-based evidence used in manual assertion
    ECO_0006230 = "ECO_0006230"
    HEAT_CAPACITY_BASED_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006230"

    # heat capacity-based evidence used in automatic assertion
    ECO_0006231 = "ECO_0006231"
    HEAT_CAPACITY_BASED_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006231"

    # differential scanning calorimetry evidence used in manual assertion
    ECO_0006232 = "ECO_0006232"
    DIFFERENTIAL_SCANNING_CALORIMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006232"

    # differential scanning calorimetry evidence used in automatic assertion
    ECO_0006233 = "ECO_0006233"
    DIFFERENTIAL_SCANNING_CALORIMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006233"
    )

    # selective antibody-based structural conformation evidence used in manual assertion
    ECO_0006234 = "ECO_0006234"
    SELECTIVE_ANTIBODY_BASED_STRUCTURAL_CONFORMATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006234"
    )

    # selective antibody-based structural conformation evidence used in automatic assertion
    ECO_0006235 = "ECO_0006235"
    SELECTIVE_ANTIBODY_BASED_STRUCTURAL_CONFORMATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006235"
    )

    # protein hydrogen-deuterium exchange mass spectrometry evidence used in manual assertion
    ECO_0006236 = "ECO_0006236"
    PROTEIN_HYDROGEN_DEUTERIUM_EXCHANGE_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006236"
    )

    # protein hydrogen-deuterium exchange mass spectrometry evidence used in automatic assertion
    ECO_0006237 = "ECO_0006237"
    PROTEIN_HYDROGEN_DEUTERIUM_EXCHANGE_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006237"
    )

    # galactokinase reporter gene assay evidence
    ECO_0006238 = "ECO_0006238"
    GALACTOKINASE_REPORTER_GENE_ASSAY_EVIDENCE = "ECO_0006238"

    # polyadenylated transcript 3'-end-sequencing evidence
    ECO_0006239 = "ECO_0006239"
    POLYADENYLATED_TRANSCRIPT_3__END_SEQUENCING_EVIDENCE = "ECO_0006239"

    # colony boundary assay evidence
    ECO_0006240 = "ECO_0006240"
    COLONY_BOUNDARY_ASSAY_EVIDENCE = "ECO_0006240"

    # galactokinase reporter gene assay evidence used in manual assertion
    ECO_0006241 = "ECO_0006241"
    GALACTOKINASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006241"

    # galactokinase reporter gene assay evidence used in automatic assertion
    ECO_0006242 = "ECO_0006242"
    GALACTOKINASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006242"
    )

    # polyadenylated transcript 3'-end-sequencing evidence used in manual assertion
    ECO_0006243 = "ECO_0006243"
    POLYADENYLATED_TRANSCRIPT_3__END_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006243"
    )

    # polyadenylated transcript 3'-end-sequencing evidence used in automatic assertion
    ECO_0006244 = "ECO_0006244"
    POLYADENYLATED_TRANSCRIPT_3__END_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006244"
    )

    # colony boundary assay evidence used in manual assertion
    ECO_0006245 = "ECO_0006245"
    COLONY_BOUNDARY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006245"

    # colony boundary assay evidence used in automatic assertion
    ECO_0006246 = "ECO_0006246"
    COLONY_BOUNDARY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006246"

    # analytical ultracentrifugation evidence
    ECO_0006247 = "ECO_0006247"
    ANALYTICAL_ULTRACENTRIFUGATION_EVIDENCE = "ECO_0006247"

    # fluorescence polarization evidence
    ECO_0006248 = "ECO_0006248"
    FLUORESCENCE_POLARIZATION_EVIDENCE = "ECO_0006248"

    # obsolete bait-prey protein pull-down evidence
    ECO_0006249 = "ECO_0006249"
    OBSOLETE_BAIT_PREY_PROTEIN_PULL_DOWN_EVIDENCE = "ECO_0006249"

    # rotary shadowing electron microscopy evidence
    ECO_0006250 = "ECO_0006250"
    ROTARY_SHADOWING_ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0006250"

    # electrospray ionization fourier transform ion cyclotron resonance mass spectrometry evidence
    ECO_0006251 = "ECO_0006251"
    ELECTROSPRAY_IONIZATION_FOURIER_TRANSFORM_ION_CYCLOTRON_RESONANCE_MASS_SPECTROMETRY_EVIDENCE = (
        "ECO_0006251"
    )

    # magnetic resonance evidence
    ECO_0006252 = "ECO_0006252"
    MAGNETIC_RESONANCE_EVIDENCE = "ECO_0006252"

    # electron paramagnetic resonance evidence
    ECO_0006253 = "ECO_0006253"
    ELECTRON_PARAMAGNETIC_RESONANCE_EVIDENCE = "ECO_0006253"

    # site-directed spin-labelling electron paramagnetic resonance evidence
    ECO_0006254 = "ECO_0006254"
    SITE_DIRECTED_SPIN_LABELLING_ELECTRON_PARAMAGNETIC_RESONANCE_EVIDENCE = (
        "ECO_0006254"
    )

    # deglycosylation assay evidence
    ECO_0006255 = "ECO_0006255"
    DEGLYCOSYLATION_ASSAY_EVIDENCE = "ECO_0006255"

    # protein fragment functional complementation evidence
    ECO_0006256 = "ECO_0006256"
    PROTEIN_FRAGMENT_FUNCTIONAL_COMPLEMENTATION_EVIDENCE = "ECO_0006256"

    # beta galactosidase functional complementation evidence
    ECO_0006257 = "ECO_0006257"
    BETA_GALACTOSIDASE_FUNCTIONAL_COMPLEMENTATION_EVIDENCE = "ECO_0006257"

    # GAL4-VP16 functional complementation evidence
    ECO_0006258 = "ECO_0006258"
    GAL4_VP16_FUNCTIONAL_COMPLEMENTATION_EVIDENCE = "ECO_0006258"

    # Raman spectroscopy evidence
    ECO_0006259 = "ECO_0006259"
    RAMAN_SPECTROSCOPY_EVIDENCE = "ECO_0006259"

    # protein thermal shift assay evidence
    ECO_0006260 = "ECO_0006260"
    PROTEIN_THERMAL_SHIFT_ASSAY_EVIDENCE = "ECO_0006260"

    # microscale thermophoresis evidence
    ECO_0006261 = "ECO_0006261"
    MICROSCALE_THERMOPHORESIS_EVIDENCE = "ECO_0006261"

    # native protein gel electrophoresis evidence
    ECO_0006262 = "ECO_0006262"
    NATIVE_PROTEIN_GEL_ELECTROPHORESIS_EVIDENCE = "ECO_0006262"

    # turbidity measurement evidence
    ECO_0006263 = "ECO_0006263"
    TURBIDITY_MEASUREMENT_EVIDENCE = "ECO_0006263"

    # competitive binding evidence
    ECO_0006264 = "ECO_0006264"
    COMPETITIVE_BINDING_EVIDENCE = "ECO_0006264"

    # protein unfolding evidence
    ECO_0006265 = "ECO_0006265"
    PROTEIN_UNFOLDING_EVIDENCE = "ECO_0006265"

    # urea-induced protein unfolding evidence
    ECO_0006266 = "ECO_0006266"
    UREA_INDUCED_PROTEIN_UNFOLDING_EVIDENCE = "ECO_0006266"

    # pH-induced protein unfolding evidence
    ECO_0006267 = "ECO_0006267"
    PH_INDUCED_PROTEIN_UNFOLDING_EVIDENCE = "ECO_0006267"

    # temperature-induced protein unfolding evidence
    ECO_0006268 = "ECO_0006268"
    TEMPERATURE_INDUCED_PROTEIN_UNFOLDING_EVIDENCE = "ECO_0006268"

    # cell aggregation evidence
    ECO_0006269 = "ECO_0006269"
    CELL_AGGREGATION_EVIDENCE = "ECO_0006269"

    # RNA-protein binding evidence
    ECO_0006270 = "ECO_0006270"
    RNA_PROTEIN_BINDING_EVIDENCE = "ECO_0006270"

    # fluorescence microscopy evidence
    ECO_0006271 = "ECO_0006271"
    FLUORESCENCE_MICROSCOPY_EVIDENCE = "ECO_0006271"

    # viscosity measurement evidence
    ECO_0006272 = "ECO_0006272"
    VISCOSITY_MEASUREMENT_EVIDENCE = "ECO_0006272"

    # dynamic fluorescence quenching evidence
    ECO_0006273 = "ECO_0006273"
    DYNAMIC_FLUORESCENCE_QUENCHING_EVIDENCE = "ECO_0006273"

    # static fluorescence quenching evidence
    ECO_0006274 = "ECO_0006274"
    STATIC_FLUORESCENCE_QUENCHING_EVIDENCE = "ECO_0006274"

    # analytical ultracentrifugation evidence used in manual assertion
    ECO_0006275 = "ECO_0006275"
    ANALYTICAL_ULTRACENTRIFUGATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006275"

    # analytical ultracentrifugation evidence used in automatic assertion
    ECO_0006276 = "ECO_0006276"
    ANALYTICAL_ULTRACENTRIFUGATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006276"

    # fluorescence polarization evidence used in manual assertion
    ECO_0006277 = "ECO_0006277"
    FLUORESCENCE_POLARIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006277"

    # fluorescence polarization evidence used in automatic assertion
    ECO_0006278 = "ECO_0006278"
    FLUORESCENCE_POLARIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006278"

    # obsolete bait-prey protein pull-down evidence used in manual assertion
    ECO_0006279 = "ECO_0006279"
    OBSOLETE_BAIT_PREY_PROTEIN_PULL_DOWN_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006279"
    )

    # obsolete bait-prey protein pull-down evidence used in automatic assertion
    ECO_0006280 = "ECO_0006280"
    OBSOLETE_BAIT_PREY_PROTEIN_PULL_DOWN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006280"
    )

    # rotary shadowing electron microscopy evidence used in manual assertion
    ECO_0006281 = "ECO_0006281"
    ROTARY_SHADOWING_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006281"
    )

    # rotary shadowing electron microscopy evidence used in automatic assertion
    ECO_0006282 = "ECO_0006282"
    ROTARY_SHADOWING_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006282"
    )

    # electrospray ionization fourier transform ion cyclotron resonance mass spectrometry evidence used in manual assertion
    ECO_0006283 = "ECO_0006283"
    ELECTROSPRAY_IONIZATION_FOURIER_TRANSFORM_ION_CYCLOTRON_RESONANCE_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006283"
    )

    # electrospray ionization fourier transform ion cyclotron resonance mass spectrometry evidence used in automatic assertion
    ECO_0006284 = "ECO_0006284"
    ELECTROSPRAY_IONIZATION_FOURIER_TRANSFORM_ION_CYCLOTRON_RESONANCE_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006284"
    )

    # magnetic resonance evidence used in manual assertion
    ECO_0006285 = "ECO_0006285"
    MAGNETIC_RESONANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006285"

    # magnetic resonance evidence used in automatic assertion
    ECO_0006286 = "ECO_0006286"
    MAGNETIC_RESONANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006286"

    # electron paramagnetic resonance evidence used in manual assertion
    ECO_0006287 = "ECO_0006287"
    ELECTRON_PARAMAGNETIC_RESONANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006287"

    # electron paramagnetic resonance evidence used in automatic assertion
    ECO_0006288 = "ECO_0006288"
    ELECTRON_PARAMAGNETIC_RESONANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006288"

    # site-directed spin-labelling electron paramagnetic resonance evidence used in manual assertion
    ECO_0006289 = "ECO_0006289"
    SITE_DIRECTED_SPIN_LABELLING_ELECTRON_PARAMAGNETIC_RESONANCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006289"
    )

    # site-directed spin-labelling electron paramagnetic resonance evidence used in automatic assertion
    ECO_0006290 = "ECO_0006290"
    SITE_DIRECTED_SPIN_LABELLING_ELECTRON_PARAMAGNETIC_RESONANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006290"
    )

    # deglycosylation assay evidence used in manual assertion
    ECO_0006291 = "ECO_0006291"
    DEGLYCOSYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006291"

    # deglycosylation assay evidence used in automatic assertion
    ECO_0006292 = "ECO_0006292"
    DEGLYCOSYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006292"

    # protein fragment functional complementation evidence used in manual assertion
    ECO_0006293 = "ECO_0006293"
    PROTEIN_FRAGMENT_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006293"
    )

    # protein fragment functional complementation evidence used in automatic assertion
    ECO_0006294 = "ECO_0006294"
    PROTEIN_FRAGMENT_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006294"
    )

    # beta galactosidase functional complementation evidence used in manual assertion
    ECO_0006295 = "ECO_0006295"
    BETA_GALACTOSIDASE_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006295"
    )

    # beta galactosidase functional complementation evidence used in automatic assertion
    ECO_0006296 = "ECO_0006296"
    BETA_GALACTOSIDASE_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006296"
    )

    # GAL4-VP16 functional complementation evidence used in manual assertion
    ECO_0006297 = "ECO_0006297"
    GAL4_VP16_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006297"
    )

    # GAL4-VP16 functional complementation evidence used in automatic assertion
    ECO_0006298 = "ECO_0006298"
    GAL4_VP16_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006298"
    )

    # Raman spectroscopy evidence used in manual assertion
    ECO_0006299 = "ECO_0006299"
    RAMAN_SPECTROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006299"

    # Raman spectroscopy evidence used in automatic assertion
    ECO_0006300 = "ECO_0006300"
    RAMAN_SPECTROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006300"

    # protein thermal shift assay evidence used in manual assertion
    ECO_0006301 = "ECO_0006301"
    PROTEIN_THERMAL_SHIFT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006301"

    # protein thermal shift assay evidence used in automatic assertion
    ECO_0006302 = "ECO_0006302"
    PROTEIN_THERMAL_SHIFT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006302"

    # microscale thermophoresis evidence used in manual assertion
    ECO_0006303 = "ECO_0006303"
    MICROSCALE_THERMOPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006303"

    # microscale thermophoresis evidence used in automatic assertion
    ECO_0006304 = "ECO_0006304"
    MICROSCALE_THERMOPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006304"

    # native protein gel electrophoresis evidence used in manual assertion
    ECO_0006305 = "ECO_0006305"
    NATIVE_PROTEIN_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006305"

    # native protein gel electrophoresis evidence used in automatic assertion
    ECO_0006306 = "ECO_0006306"
    NATIVE_PROTEIN_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006306"
    )

    # turbidity measurement evidence used in manual assertion
    ECO_0006307 = "ECO_0006307"
    TURBIDITY_MEASUREMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006307"

    # turbidity measurement evidence used in automatic assertion
    ECO_0006308 = "ECO_0006308"
    TURBIDITY_MEASUREMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006308"

    # competitive binding evidence used in manual assertion
    ECO_0006309 = "ECO_0006309"
    COMPETITIVE_BINDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006309"

    # competitive binding evidence used in automatic assertion
    ECO_0006310 = "ECO_0006310"
    COMPETITIVE_BINDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006310"

    # protein unfolding evidence used in manual assertion
    ECO_0006311 = "ECO_0006311"
    PROTEIN_UNFOLDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006311"

    # protein unfolding evidence used in automatic assertion
    ECO_0006312 = "ECO_0006312"
    PROTEIN_UNFOLDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006312"

    # urea-induced protein unfolding evidence used in manual assertion
    ECO_0006313 = "ECO_0006313"
    UREA_INDUCED_PROTEIN_UNFOLDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006313"

    # urea-induced protein unfolding evidence used in automatic assertion
    ECO_0006314 = "ECO_0006314"
    UREA_INDUCED_PROTEIN_UNFOLDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006314"

    # pH-induced protein unfolding evidence used in manual assertion
    ECO_0006315 = "ECO_0006315"
    PH_INDUCED_PROTEIN_UNFOLDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006315"

    # pH-induced protein unfolding evidence used in automatic assertion
    ECO_0006316 = "ECO_0006316"
    PH_INDUCED_PROTEIN_UNFOLDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006316"

    # temperature-induced protein unfolding evidence used in manual assertion
    ECO_0006317 = "ECO_0006317"
    TEMPERATURE_INDUCED_PROTEIN_UNFOLDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0006317"
    )

    # temperature-induced protein unfolding evidence used in automatic assertion
    ECO_0006318 = "ECO_0006318"
    TEMPERATURE_INDUCED_PROTEIN_UNFOLDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0006318"
    )

    # cell aggregation evidence used in manual assertion
    ECO_0006319 = "ECO_0006319"
    CELL_AGGREGATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006319"

    # cell aggregation evidence used in automatic assertion
    ECO_0006320 = "ECO_0006320"
    CELL_AGGREGATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006320"

    # RNA-protein binding evidence used in manual assertion
    ECO_0006321 = "ECO_0006321"
    RNA_PROTEIN_BINDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006321"

    # RNA-protein binding evidence used in automatic assertion
    ECO_0006322 = "ECO_0006322"
    RNA_PROTEIN_BINDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006322"

    # fluorescence microscopy evidence used in manual assertion
    ECO_0006323 = "ECO_0006323"
    FLUORESCENCE_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006323"

    # fluorescence microscopy evidence used in automatic assertion
    ECO_0006324 = "ECO_0006324"
    FLUORESCENCE_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006324"

    # viscosity measurement evidence used in manual assertion
    ECO_0006325 = "ECO_0006325"
    VISCOSITY_MEASUREMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006325"

    # viscosity measurement evidence used in automatic assertion
    ECO_0006326 = "ECO_0006326"
    VISCOSITY_MEASUREMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006326"

    # dynamic fluorescence quenching evidence used in manual assertion
    ECO_0006327 = "ECO_0006327"
    DYNAMIC_FLUORESCENCE_QUENCHING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006327"

    # dynamic fluorescence quenching evidence used in automatic assertion
    ECO_0006328 = "ECO_0006328"
    DYNAMIC_FLUORESCENCE_QUENCHING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006328"

    # static fluorescence quenching evidence used in manual assertion
    ECO_0006329 = "ECO_0006329"
    STATIC_FLUORESCENCE_QUENCHING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0006329"

    # static fluorescence quenching evidence used in automatic assertion
    ECO_0006330 = "ECO_0006330"
    STATIC_FLUORESCENCE_QUENCHING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0006330"

    # high throughput mutant phenotypic evidence
    ECO_0007000 = "ECO_0007000"
    HIGH_THROUGHPUT_MUTANT_PHENOTYPIC_EVIDENCE = "ECO_0007000"

    # high throughput mutant phenotypic evidence used in manual assertion
    ECO_0007001 = "ECO_0007001"
    HIGH_THROUGHPUT_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007001"

    # high throughput genetic interaction phenotypic evidence
    ECO_0007002 = "ECO_0007002"
    HIGH_THROUGHPUT_GENETIC_INTERACTION_PHENOTYPIC_EVIDENCE = "ECO_0007002"

    # high throughput genetic interaction phenotypic evidence used in manual assertion
    ECO_0007003 = "ECO_0007003"
    HIGH_THROUGHPUT_GENETIC_INTERACTION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007003"
    )

    # high throughput direct assay evidence
    ECO_0007004 = "ECO_0007004"
    HIGH_THROUGHPUT_DIRECT_ASSAY_EVIDENCE = "ECO_0007004"

    # high throughput direct assay evidence used in manual assertion
    ECO_0007005 = "ECO_0007005"
    HIGH_THROUGHPUT_DIRECT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007005"

    # high throughput expression pattern evidence
    ECO_0007006 = "ECO_0007006"
    HIGH_THROUGHPUT_EXPRESSION_PATTERN_EVIDENCE = "ECO_0007006"

    # high throughput expression pattern evidence used in manual assertion
    ECO_0007007 = "ECO_0007007"
    HIGH_THROUGHPUT_EXPRESSION_PATTERN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007007"

    # radioligand binding assay evidence
    ECO_0007008 = "ECO_0007008"
    RADIOLIGAND_BINDING_ASSAY_EVIDENCE = "ECO_0007008"

    # radioligand binding assay evidence used in manual assertion
    ECO_0007009 = "ECO_0007009"
    RADIOLIGAND_BINDING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007009"

    # combinatorial experimental and author inference evidence
    ECO_0007011 = "ECO_0007011"
    COMBINATORIAL_EXPERIMENTAL_AND_AUTHOR_INFERENCE_EVIDENCE = "ECO_0007011"

    # combinatorial experimental and curator inference evidence
    ECO_0007012 = "ECO_0007012"
    COMBINATORIAL_EXPERIMENTAL_AND_CURATOR_INFERENCE_EVIDENCE = "ECO_0007012"

    # combinatorial experimental and author inference evidence used in manual assertion
    ECO_0007013 = "ECO_0007013"
    COMBINATORIAL_EXPERIMENTAL_AND_AUTHOR_INFERENCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007013"
    )

    # combinatorial experimental and curator inference evidence used in manual assertion
    ECO_0007014 = "ECO_0007014"
    COMBINATORIAL_EXPERIMENTAL_AND_CURATOR_INFERENCE_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007014"
    )

    # voltammetry evidence
    ECO_0007015 = "ECO_0007015"
    VOLTAMMETRY_EVIDENCE = "ECO_0007015"

    # voltammetry evidence used in manual assertion
    ECO_0007016 = "ECO_0007016"
    VOLTAMMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007016"

    # photoconversion evidence
    ECO_0007017 = "ECO_0007017"
    PHOTOCONVERSION_EVIDENCE = "ECO_0007017"

    # photoconversion evidence used in manual assertion
    ECO_0007018 = "ECO_0007018"
    PHOTOCONVERSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007018"

    # agglutination test evidence
    ECO_0007019 = "ECO_0007019"
    AGGLUTINATION_TEST_EVIDENCE = "ECO_0007019"

    # agglutination test evidence used in manual assertion
    ECO_0007020 = "ECO_0007020"
    AGGLUTINATION_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007020"

    # slide agglutination test evidence
    ECO_0007021 = "ECO_0007021"
    SLIDE_AGGLUTINATION_TEST_EVIDENCE = "ECO_0007021"

    # slide agglutination test evidence used in manual assertion
    ECO_0007022 = "ECO_0007022"
    SLIDE_AGGLUTINATION_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007022"

    # direct Coombs test evidence
    ECO_0007023 = "ECO_0007023"
    DIRECT_COOMBS_TEST_EVIDENCE = "ECO_0007023"

    # direct Coombs test evidence used in manual assertion
    ECO_0007024 = "ECO_0007024"
    DIRECT_COOMBS_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007024"

    # indirect Coombs test evidence
    ECO_0007025 = "ECO_0007025"
    INDIRECT_COOMBS_TEST_EVIDENCE = "ECO_0007025"

    # indirect Coombs test evidence used in manual assertion
    ECO_0007026 = "ECO_0007026"
    INDIRECT_COOMBS_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007026"

    # direct hemagglutination assay evidence
    ECO_0007027 = "ECO_0007027"
    DIRECT_HEMAGGLUTINATION_ASSAY_EVIDENCE = "ECO_0007027"

    # direct hemagglutination assay evidence used in manual assertion
    ECO_0007028 = "ECO_0007028"
    DIRECT_HEMAGGLUTINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007028"

    # viral hemagglutination inhibition assay evidence
    ECO_0007029 = "ECO_0007029"
    VIRAL_HEMAGGLUTINATION_INHIBITION_ASSAY_EVIDENCE = "ECO_0007029"

    # viral hemagglutination inhibition assay evidence used in manual assertion
    ECO_0007030 = "ECO_0007030"
    VIRAL_HEMAGGLUTINATION_INHIBITION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007030"
    )

    # compement fixation assay evidence
    ECO_0007031 = "ECO_0007031"
    COMPEMENT_FIXATION_ASSAY_EVIDENCE = "ECO_0007031"

    # compement fixation assay evidence used in manual assertion
    ECO_0007032 = "ECO_0007032"
    COMPEMENT_FIXATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007032"

    # neutralization test assay evidence
    ECO_0007033 = "ECO_0007033"
    NEUTRALIZATION_TEST_ASSAY_EVIDENCE = "ECO_0007033"

    # neutralization test assay evidence used in manual assertion
    ECO_0007034 = "ECO_0007034"
    NEUTRALIZATION_TEST_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007034"

    # copper transport assay evidence
    ECO_0007035 = "ECO_0007035"
    COPPER_TRANSPORT_ASSAY_EVIDENCE = "ECO_0007035"

    # copper transport assay evidence used in manual assertion
    ECO_0007036 = "ECO_0007036"
    COPPER_TRANSPORT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007036"

    # 5-cyano-2,3-ditolyl tetrazolium chloride staining evidence
    ECO_0007037 = "ECO_0007037"
    _5_CYANO_2_3_DITOLYL_TETRAZOLIUM_CHLORIDE_STAINING_EVIDENCE = "ECO_0007037"

    # 5-cyano-2,3-ditolyl tetrazolium chloride staining evidence used in manual assertion
    ECO_0007038 = "ECO_0007038"
    _5_CYANO_2_3_DITOLYL_TETRAZOLIUM_CHLORIDE_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007038"
    )

    # plaque assay evidence
    ECO_0007039 = "ECO_0007039"
    PLAQUE_ASSAY_EVIDENCE = "ECO_0007039"

    # plaque assay evidence used in manual assertion
    ECO_0007040 = "ECO_0007040"
    PLAQUE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007040"

    # epifluorescence microscopy evidence
    ECO_0007041 = "ECO_0007041"
    EPIFLUORESCENCE_MICROSCOPY_EVIDENCE = "ECO_0007041"

    # epifluorescence microscopy evidence used in manual assertion
    ECO_0007042 = "ECO_0007042"
    EPIFLUORESCENCE_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007042"

    # transmission electron microscopy evidence
    ECO_0007043 = "ECO_0007043"
    TRANSMISSION_ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0007043"

    # transmission electron microscopy evidence used in manual assertion
    ECO_0007044 = "ECO_0007044"
    TRANSMISSION_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007044"

    # scanning electron microscopy evidence
    ECO_0007045 = "ECO_0007045"
    SCANNING_ELECTRON_MICROSCOPY_EVIDENCE = "ECO_0007045"

    # scanning electron microscopy evidence used in manual assertion
    ECO_0007046 = "ECO_0007046"
    SCANNING_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007046"

    # time-lapsed microscopy evidence
    ECO_0007047 = "ECO_0007047"
    TIME_LAPSED_MICROSCOPY_EVIDENCE = "ECO_0007047"

    # time-lapsed microscopy evidence used in manual assertion
    ECO_0007048 = "ECO_0007048"
    TIME_LAPSED_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007048"

    # phase contrast microscopy evidence
    ECO_0007049 = "ECO_0007049"
    PHASE_CONTRAST_MICROSCOPY_EVIDENCE = "ECO_0007049"

    # phase contrast microscopy evidence used in manual assertion
    ECO_0007050 = "ECO_0007050"
    PHASE_CONTRAST_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007050"

    # transmitted light brightfied mircoscopy evidence
    ECO_0007051 = "ECO_0007051"
    TRANSMITTED_LIGHT_BRIGHTFIED_MIRCOSCOPY_EVIDENCE = "ECO_0007051"

    # transmitted light brightfied mircoscopy evidence used in manual assertion
    ECO_0007052 = "ECO_0007052"
    TRANSMITTED_LIGHT_BRIGHTFIED_MIRCOSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007052"
    )

    # koehler illumination microscopy evidence
    ECO_0007053 = "ECO_0007053"
    KOEHLER_ILLUMINATION_MICROSCOPY_EVIDENCE = "ECO_0007053"

    # koehler illumination microscopy evidence used in manual assertion
    ECO_0007054 = "ECO_0007054"
    KOEHLER_ILLUMINATION_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007054"

    # differential interference contrast microscopy evidence
    ECO_0007055 = "ECO_0007055"
    DIFFERENTIAL_INTERFERENCE_CONTRAST_MICROSCOPY_EVIDENCE = "ECO_0007055"

    # differential interference contrast microscopy evidence used in manual assertion
    ECO_0007056 = "ECO_0007056"
    DIFFERENTIAL_INTERFERENCE_CONTRAST_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007056"
    )

    # extended field laser confocal microscopy evidence
    ECO_0007057 = "ECO_0007057"
    EXTENDED_FIELD_LASER_CONFOCAL_MICROSCOPY_EVIDENCE = "ECO_0007057"

    # extended field laser confocal microscopy evidence used in manual assertion
    ECO_0007058 = "ECO_0007058"
    EXTENDED_FIELD_LASER_CONFOCAL_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007058"
    )

    # confocal laser scanning microscopy evidence
    ECO_0007059 = "ECO_0007059"
    CONFOCAL_LASER_SCANNING_MICROSCOPY_EVIDENCE = "ECO_0007059"

    # confocal laser scanning microscopy evidence used in manual assertion
    ECO_0007060 = "ECO_0007060"
    CONFOCAL_LASER_SCANNING_MICROSCOPY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007060"

    # light scattering evidence
    ECO_0007061 = "ECO_0007061"
    LIGHT_SCATTERING_EVIDENCE = "ECO_0007061"

    # light scattering evidence used in manual assertion
    ECO_0007062 = "ECO_0007062"
    LIGHT_SCATTERING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007062"

    # dynamic light scattering assay evidence
    ECO_0007063 = "ECO_0007063"
    DYNAMIC_LIGHT_SCATTERING_ASSAY_EVIDENCE = "ECO_0007063"

    # dynamic light scattering assay evidence used in manual assertion
    ECO_0007064 = "ECO_0007064"
    DYNAMIC_LIGHT_SCATTERING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007064"

    # static light scattering assay evidence
    ECO_0007065 = "ECO_0007065"
    STATIC_LIGHT_SCATTERING_ASSAY_EVIDENCE = "ECO_0007065"

    # static light scattering assay evidence used in manual assertion
    ECO_0007066 = "ECO_0007066"
    STATIC_LIGHT_SCATTERING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007066"

    # colony papillation assay phenotypic evidence
    ECO_0007067 = "ECO_0007067"
    COLONY_PAPILLATION_ASSAY_PHENOTYPIC_EVIDENCE = "ECO_0007067"

    # colony papillation assay phenotypic evidence used in manual assertion
    ECO_0007068 = "ECO_0007068"
    COLONY_PAPILLATION_ASSAY_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007068"
    )

    # crystal violet staining evidence
    ECO_0007069 = "ECO_0007069"
    CRYSTAL_VIOLET_STAINING_EVIDENCE = "ECO_0007069"

    # crystal violet staining evidence used in manual assertion
    ECO_0007070 = "ECO_0007070"
    CRYSTAL_VIOLET_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007070"

    # flow cell biofilm assay evidence
    ECO_0007071 = "ECO_0007071"
    FLOW_CELL_BIOFILM_ASSAY_EVIDENCE = "ECO_0007071"

    # flow cell biofilm assay evidence used in manual assertion
    ECO_0007072 = "ECO_0007072"
    FLOW_CELL_BIOFILM_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007072"

    # bacterial 2-hybrid assay evidence
    ECO_0007073 = "ECO_0007073"
    BACTERIAL_2_HYBRID_ASSAY_EVIDENCE = "ECO_0007073"

    # bacterial 2-hybrid assay evidence used in manual assertion
    ECO_0007074 = "ECO_0007074"
    BACTERIAL_2_HYBRID_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007074"

    # phenomic profiling assay evidence
    ECO_0007075 = "ECO_0007075"
    PHENOMIC_PROFILING_ASSAY_EVIDENCE = "ECO_0007075"

    # phenomic profiling assay evidence used in manual assertion
    ECO_0007076 = "ECO_0007076"
    PHENOMIC_PROFILING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007076"

    # colony morphology phenotypic evidence
    ECO_0007077 = "ECO_0007077"
    COLONY_MORPHOLOGY_PHENOTYPIC_EVIDENCE = "ECO_0007077"

    # colony morphology phenotypic evidence used in manual assertion
    ECO_0007078 = "ECO_0007078"
    COLONY_MORPHOLOGY_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007078"

    # colony color phenotypic evidence
    ECO_0007079 = "ECO_0007079"
    COLONY_COLOR_PHENOTYPIC_EVIDENCE = "ECO_0007079"

    # colony color phenotypic evidence used in manual assertion
    ECO_0007080 = "ECO_0007080"
    COLONY_COLOR_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007080"

    # colony size phenotypic evidence
    ECO_0007081 = "ECO_0007081"
    COLONY_SIZE_PHENOTYPIC_EVIDENCE = "ECO_0007081"

    # colony size phenotypic evidence used in manual assertion
    ECO_0007082 = "ECO_0007082"
    COLONY_SIZE_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007082"

    # zone of inhibition evidence
    ECO_0007083 = "ECO_0007083"
    ZONE_OF_INHIBITION_EVIDENCE = "ECO_0007083"

    # zone of inhibition evidence used in manual assertion
    ECO_0007084 = "ECO_0007084"
    ZONE_OF_INHIBITION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007084"

    # Etest evidence
    ECO_0007085 = "ECO_0007085"
    ETEST_EVIDENCE = "ECO_0007085"

    # Etest evidence used in manual assertion
    ECO_0007086 = "ECO_0007086"
    ETEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007086"

    # ribosome profiling evidence used in manual assertion
    ECO_0007087 = "ECO_0007087"
    RIBOSOME_PROFILING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007087"

    # loss-of-function mutant phenotype evidence used in manual assertion
    ECO_0007089 = "ECO_0007089"
    LOSS_OF_FUNCTION_MUTANT_PHENOTYPE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007089"

    # structural similarity evidence used in manual assertion
    ECO_0007090 = "ECO_0007090"
    STRUCTURAL_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007090"

    # gain-of-function mutant phenotypic evidence used in manual assertion
    ECO_0007092 = "ECO_0007092"
    GAIN_OF_FUNCTION_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007092"

    # voucher specimen phenotypic analysis evidence used in manual assertion
    ECO_0007093 = "ECO_0007093"
    VOUCHER_SPECIMEN_PHENOTYPIC_ANALYSIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007093"
    )

    # positional similarity evidence used in manual assertion
    ECO_0007094 = "ECO_0007094"
    POSITIONAL_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007094"

    # quantitative trait analysis evidence used in manual assertion
    ECO_0007095 = "ECO_0007095"
    QUANTITATIVE_TRAIT_ANALYSIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007095"

    # compositional similarity evidence used in manual assertion
    ECO_0007096 = "ECO_0007096"
    COMPOSITIONAL_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007096"

    # developmental similarity evidence used in manual assertion
    ECO_0007097 = "ECO_0007097"
    DEVELOPMENTAL_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007097"

    # morphological similarity evidence used in manual assertion
    ECO_0007098 = "ECO_0007098"
    MORPHOLOGICAL_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007098"

    # gene expression similarity evidence used in manual assertion
    ECO_0007099 = "ECO_0007099"
    GENE_EXPRESSION_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007099"

    # methylation-specific polymerase chain reaction evidence used in manual assertion
    ECO_0007100 = "ECO_0007100"
    METHYLATION_SPECIFIC_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007100"
    )

    # southern hybridization evidence used in manual assertion
    ECO_0007101 = "ECO_0007101"
    SOUTHERN_HYBRIDIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007101"

    # intermethylated site amplification evidence used in manual assertion
    ECO_0007102 = "ECO_0007102"
    INTERMETHYLATED_SITE_AMPLIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007102"

    # epitope-tagged protein immunolocalization evidence used in manual assertion
    ECO_0007103 = "ECO_0007103"
    EPITOPE_TAGGED_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007103"
    )

    # co-fractionation evidence used in manual assertion
    ECO_0007104 = "ECO_0007104"
    CO_FRACTIONATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007104"

    # green fluorescent protein fusion protein localization evidence used in manual assertion
    ECO_0007106 = "ECO_0007106"
    GREEN_FLUORESCENT_PROTEIN_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007106"
    )

    # yellow fluorescent protein fusion protein localization evidence used in manual assertion
    ECO_0007107 = "ECO_0007107"
    YELLOW_FLUORESCENT_PROTEIN_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007107"
    )

    # beta-glucuronidase fusion protein localization evidence used in manual assertion
    ECO_0007108 = "ECO_0007108"
    BETA_GLUCURONIDASE_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007108"
    )

    # beta-galactosidase fusion protein localization evidence used in manual assertion
    ECO_0007109 = "ECO_0007109"
    BETA_GALACTOSIDASE_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007109"
    )

    # thin layer chromatography evidence used in manual assertion
    ECO_0007110 = "ECO_0007110"
    THIN_LAYER_CHROMATOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007110"

    # in vitro recombinant protein transcription reconstitution assay evidence used in manual assertion
    ECO_0007111 = "ECO_0007111"
    IN_VITRO_RECOMBINANT_PROTEIN_TRANSCRIPTION_RECONSTITUTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007111"
    )

    # protein separation followed by direct sequencing evidence used in manual assertion
    ECO_0007112 = "ECO_0007112"
    PROTEIN_SEPARATION_FOLLOWED_BY_DIRECT_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007112"
    )

    # protein separation followed by fragment identification evidence used in manual assertion
    ECO_0007113 = "ECO_0007113"
    PROTEIN_SEPARATION_FOLLOWED_BY_FRAGMENT_IDENTIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007113"
    )

    # heterologous system uptake evidence used in manual assertion
    ECO_0007114 = "ECO_0007114"
    HETEROLOGOUS_SYSTEM_UPTAKE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007114"

    # two-electrode voltage clamp recording evidence used in manual assertion
    ECO_0007115 = "ECO_0007115"
    TWO_ELECTRODE_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007115"
    )

    # biochemical trait analysis evidence used in manual assertion
    ECO_0007116 = "ECO_0007116"
    BIOCHEMICAL_TRAIT_ANALYSIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007116"

    # mutant physiological response evidence used in manual assertion
    ECO_0007117 = "ECO_0007117"
    MUTANT_PHYSIOLOGICAL_RESPONSE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007117"

    # mutant visible phenotype evidence used in manual assertion
    ECO_0007118 = "ECO_0007118"
    MUTANT_VISIBLE_PHENOTYPE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007118"

    # in vivo assay evidence used in manual assertion
    ECO_0007119 = "ECO_0007119"
    IN_VIVO_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007119"

    # animal model system study evidence used in manual assertion
    ECO_0007120 = "ECO_0007120"
    ANIMAL_MODEL_SYSTEM_STUDY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007120"

    # clinical study evidence used in manual assertion
    ECO_0007121 = "ECO_0007121"
    CLINICAL_STUDY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007121"

    # in vitro assay evidence used in manual assertion
    ECO_0007122 = "ECO_0007122"
    IN_VITRO_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007122"

    # enzyme inhibition evidence used in manual assertion
    ECO_0007123 = "ECO_0007123"
    ENZYME_INHIBITION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007123"

    # Illumina sequencing evidence used in manual assertion
    ECO_0007125 = "ECO_0007125"
    ILLUMINA_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007125"

    # 454 pyrosequencing evidence used in manual assertion
    ECO_0007126 = "ECO_0007126"
    _454_PYROSEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007126"

    # SOLiD sequencing evidence used in manual assertion
    ECO_0007127 = "ECO_0007127"
    SOLID_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007127"

    # chain termination sequencing evidence used in manual assertion
    ECO_0007128 = "ECO_0007128"
    CHAIN_TERMINATION_SEQUENCING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007128"

    # chromatin immunoprecipitation-qPCR evidence used in manual assertion
    ECO_0007129 = "ECO_0007129"
    CHROMATIN_IMMUNOPRECIPITATION_QPCR_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007129"

    # 4C evidence used in manual assertion
    ECO_0007130 = "ECO_0007130"
    _4C_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007130"

    # 5C evidence used in manual assertion
    ECO_0007131 = "ECO_0007131"
    _5C_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007131"

    # 3C-qPCR evidence used in manual assertion
    ECO_0007133 = "ECO_0007133"
    _3C_QPCR_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007133"

    # Hi-C evidence used in manual assertion
    ECO_0007134 = "ECO_0007134"
    HI_C_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007134"

    # 3C-seq evidence used in manual assertion
    ECO_0007135 = "ECO_0007135"
    _3C_SEQ_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007135"

    # environmental perturbation phenotypic evidence used in manual assertion
    ECO_0007136 = "ECO_0007136"
    ENVIRONMENTAL_PERTURBATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007136"
    )

    # tissue ablation phenotypic evidence used in manual assertion
    ECO_0007137 = "ECO_0007137"
    TISSUE_ABLATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007137"

    # tissue grafting phenotypic evidence used in manual assertion
    ECO_0007138 = "ECO_0007138"
    TISSUE_GRAFTING_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007138"

    # cytochalasin experiment evidence used in manual assertion
    ECO_0007141 = "ECO_0007141"
    CYTOCHALASIN_EXPERIMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007141"

    # green fluorescent protein immunolocalization evidence used in manual assertion
    ECO_0007142 = "ECO_0007142"
    GREEN_FLUORESCENT_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007142"
    )

    # beta-galactosidase protein immunolocalization evidence used in manual assertion
    ECO_0007143 = "ECO_0007143"
    BETA_GALACTOSIDASE_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007143"
    )

    # cap analysis of gene expression evidence used in manual assertion
    ECO_0007144 = "ECO_0007144"
    CAP_ANALYSIS_OF_GENE_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007144"

    # nano-cap analysis of gene expression evidence used in manual assertion
    ECO_0007145 = "ECO_0007145"
    NANO_CAP_ANALYSIS_OF_GENE_EXPRESSION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007145"
    )

    # particle size and count assay evidence used in manual assertion
    ECO_0007146 = "ECO_0007146"
    PARTICLE_SIZE_AND_COUNT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007146"

    # competitive growth assay evidence used in manual assertion
    ECO_0007147 = "ECO_0007147"
    COMPETITIVE_GROWTH_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007147"

    # pulsed-field gel electrophoresis evidence used in manual assertion
    ECO_0007148 = "ECO_0007148"
    PULSED_FIELD_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007148"

    # two-dimensional agarose gel electrophoresis evidence used in manual assertion
    ECO_0007149 = "ECO_0007149"
    TWO_DIMENSIONAL_AGAROSE_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007149"
    )

    # plasmid maintenance assay evidence used in manual assertion
    ECO_0007150 = "ECO_0007150"
    PLASMID_MAINTENANCE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007150"

    # specific protein inhibition by antibody evidence used in manual assertion
    ECO_0007151 = "ECO_0007151"
    SPECIFIC_PROTEIN_INHIBITION_BY_ANTIBODY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007151"
    )

    # single exon transcript confirmation via alignment evidence used in manual assertion
    ECO_0007152 = "ECO_0007152"
    SINGLE_EXON_TRANSCRIPT_CONFIRMATION_VIA_ALIGNMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007152"
    )

    # phylogenetic distribution evidence used in manual assertion
    ECO_0007153 = "ECO_0007153"
    PHYLOGENETIC_DISTRIBUTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007153"

    # differential geneset expression evidence from microarray experiment (GSEA, Fisher-exact) used in manual assertion
    ECO_0007154 = "ECO_0007154"
    DIFFERENTIAL_GENESET_EXPRESSION_EVIDENCE_FROM_MICROARRAY_EXPERIMENT__GSEA__FISHER_EXACT__USED_IN_MANUAL_ASSERTION = (
        "ECO_0007154"
    )

    # differential geneset expression evidence from RNA-seq experiment (GSEA, Fisher-exact) used in manual assertion
    ECO_0007155 = "ECO_0007155"
    DIFFERENTIAL_GENESET_EXPRESSION_EVIDENCE_FROM_RNA_SEQ_EXPERIMENT__GSEA__FISHER_EXACT__USED_IN_MANUAL_ASSERTION = (
        "ECO_0007155"
    )

    # biological target-disease association via drug evidence used in manual assertion
    ECO_0007156 = "ECO_0007156"
    BIOLOGICAL_TARGET_DISEASE_ASSOCIATION_VIA_DRUG_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007156"
    )

    # cell staining evidence used in manual assertion
    ECO_0007157 = "ECO_0007157"
    CELL_STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007157"

    # visual sequence inspection evidence used in manual assertion
    ECO_0007158 = "ECO_0007158"
    VISUAL_SEQUENCE_INSPECTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007158"

    # ATP bioluminescence assay evidence used in manual assertion
    ECO_0007159 = "ECO_0007159"
    ATP_BIOLUMINESCENCE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007159"

    # missense mutation pohenotypic evidence used in manual assertion
    ECO_0007160 = "ECO_0007160"
    MISSENSE_MUTATION_POHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007160"

    # nonsense mutation phenotypic evidence used in manual assertion
    ECO_0007161 = "ECO_0007161"
    NONSENSE_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007161"

    # silent mutation evidence used in manual assertion
    ECO_0007162 = "ECO_0007162"
    SILENT_MUTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007162"

    # insertion mutation phenotypic evidence used in manual assertion
    ECO_0007163 = "ECO_0007163"
    INSERTION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007163"

    # duplication mutation evidence used in manual assertion
    ECO_0007164 = "ECO_0007164"
    DUPLICATION_MUTATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007164"

    # frameshift mutation phenotypic evidence used in manual assertion
    ECO_0007165 = "ECO_0007165"
    FRAMESHIFT_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007165"

    # repeat expansion mutation phenotypic evidence used in manual assertion
    ECO_0007166 = "ECO_0007166"
    REPEAT_EXPANSION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007166"
    )

    # splice site mutation phenotypic evidence used in manual assertion
    ECO_0007167 = "ECO_0007167"
    SPLICE_SITE_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007167"

    # translocation mutation phenotypic evidence used in manual assertion
    ECO_0007168 = "ECO_0007168"
    TRANSLOCATION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007168"

    # in-gel protein kinase assay evidence used in manual assertion
    ECO_0007169 = "ECO_0007169"
    IN_GEL_PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007169"

    # macroscopic current trace evidence used in manual assertion
    ECO_0007170 = "ECO_0007170"
    MACROSCOPIC_CURRENT_TRACE_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007170"

    # current density evidence used in manual assertion
    ECO_0007171 = "ECO_0007171"
    CURRENT_DENSITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007171"

    # sustained current evidence used in manual assertion
    ECO_0007172 = "ECO_0007172"
    SUSTAINED_CURRENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007172"

    # use dependence of inactivation evidence used in manual assertion
    ECO_0007173 = "ECO_0007173"
    USE_DEPENDENCE_OF_INACTIVATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007173"

    # current clamp recording evidence used in manual assertion
    ECO_0007174 = "ECO_0007174"
    CURRENT_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007174"

    # whole-cell voltage clamp recording evidence used in manual assertion
    ECO_0007175 = "ECO_0007175"
    WHOLE_CELL_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007175"

    # cell-attached single-channel recording evidence used in manual assertion
    ECO_0007176 = "ECO_0007176"
    CELL_ATTACHED_SINGLE_CHANNEL_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007176"
    )

    # cell-detached inside-out single-channel recording evidence used in manual assertion
    ECO_0007177 = "ECO_0007177"
    CELL_DETACHED_INSIDE_OUT_SINGLE_CHANNEL_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007177"
    )

    # reconstituted bilayer single-channel patch recording evidence used in manual assertion
    ECO_0007178 = "ECO_0007178"
    RECONSTITUTED_BILAYER_SINGLE_CHANNEL_PATCH_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007178"
    )

    # electroencephalography recording evidence used in manual assertion
    ECO_0007179 = "ECO_0007179"
    ELECTROENCEPHALOGRAPHY_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007179"

    # cell-detached outside-out single-channel recording evidence used in manual assertion
    ECO_0007180 = "ECO_0007180"
    CELL_DETACHED_OUTSIDE_OUT_SINGLE_CHANNEL_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007180"
    )

    # cut-open oocyte voltage clamp recording evidence used in manual assertion
    ECO_0007181 = "ECO_0007181"
    CUT_OPEN_OOCYTE_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007181"
    )

    # macropatch voltage clamp recording evidence used in manual assertion
    ECO_0007182 = "ECO_0007182"
    MACROPATCH_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007182"

    # protein mass spectrometry evidence used in manual assertion
    ECO_0007184 = "ECO_0007184"
    PROTEIN_MASS_SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007184"

    # cross-streak test evidence used in manual assertion
    ECO_0007185 = "ECO_0007185"
    CROSS_STREAK_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007185"

    # tethered cell assay evidence used in manual assertion
    ECO_0007186 = "ECO_0007186"
    TETHERED_CELL_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007186"

    # tumble frequency assay evidence used in manual assertion
    ECO_0007187 = "ECO_0007187"
    TUMBLE_FREQUENCY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007187"

    # capillary assay evidence used in manual assertion
    ECO_0007188 = "ECO_0007188"
    CAPILLARY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007188"

    # inference from experimental data evidence used in manual assertion
    ECO_0007189 = "ECO_0007189"
    INFERENCE_FROM_EXPERIMENTAL_DATA_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007189"

    # inference from phenotype manipulation evidence used in manual assertion
    ECO_0007190 = "ECO_0007190"
    INFERENCE_FROM_PHENOTYPE_MANIPULATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007190"
    )

    # inference by association of genotype from phenotype used in manual assertion
    ECO_0007191 = "ECO_0007191"
    INFERENCE_BY_ASSOCIATION_OF_GENOTYPE_FROM_PHENOTYPE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007191"
    )

    # motility assay evidence used in manual assertion
    ECO_0007192 = "ECO_0007192"
    MOTILITY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007192"

    # loss-of-function mutant phenotype evidence used in automatic assertion
    ECO_0007193 = "ECO_0007193"
    LOSS_OF_FUNCTION_MUTANT_PHENOTYPE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007193"
    )

    # structural similarity evidence used in automatic assertion
    ECO_0007194 = "ECO_0007194"
    STRUCTURAL_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007194"

    # gain-of-function mutant phenotypic evidence used in automatic assertion
    ECO_0007196 = "ECO_0007196"
    GAIN_OF_FUNCTION_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007196"
    )

    # voucher specimen phenotypic analysis evidence used in automatic assertion
    ECO_0007197 = "ECO_0007197"
    VOUCHER_SPECIMEN_PHENOTYPIC_ANALYSIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007197"
    )

    # positional similarity evidence used in automatic assertion
    ECO_0007198 = "ECO_0007198"
    POSITIONAL_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007198"

    # quantitative trait analysis evidence used in automatic assertion
    ECO_0007199 = "ECO_0007199"
    QUANTITATIVE_TRAIT_ANALYSIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007199"

    # compositional similarity evidence used in automatic assertion
    ECO_0007200 = "ECO_0007200"
    COMPOSITIONAL_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007200"

    # developmental similarity evidence used in automatic assertion
    ECO_0007201 = "ECO_0007201"
    DEVELOPMENTAL_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007201"

    # morphological similarity evidence used in automatic assertion
    ECO_0007202 = "ECO_0007202"
    MORPHOLOGICAL_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007202"

    # gene expression similarity evidence used in automatic assertion
    ECO_0007203 = "ECO_0007203"
    GENE_EXPRESSION_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007203"

    # methylation-specific polymerase chain reaction evidence used in automatic assertion
    ECO_0007204 = "ECO_0007204"
    METHYLATION_SPECIFIC_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007204"
    )

    # southern hybridization evidence used in automatic assertion
    ECO_0007205 = "ECO_0007205"
    SOUTHERN_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007205"

    # intermethylated site amplification evidence used in automatic assertion
    ECO_0007206 = "ECO_0007206"
    INTERMETHYLATED_SITE_AMPLIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007206"
    )

    # epitope-tagged protein immunolocalization evidence used in automatic assertion
    ECO_0007207 = "ECO_0007207"
    EPITOPE_TAGGED_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007207"
    )

    # co-fractionation evidence used in automatic assertion
    ECO_0007208 = "ECO_0007208"
    CO_FRACTIONATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007208"

    # green fluorescent protein fusion protein localization evidence used in automatic assertion
    ECO_0007210 = "ECO_0007210"
    GREEN_FLUORESCENT_PROTEIN_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007210"
    )

    # yellow fluorescent protein fusion protein localization evidence used in automatic assertion
    ECO_0007211 = "ECO_0007211"
    YELLOW_FLUORESCENT_PROTEIN_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007211"
    )

    # beta-glucuronidase fusion protein localization evidence used in automatic assertion
    ECO_0007212 = "ECO_0007212"
    BETA_GLUCURONIDASE_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007212"
    )

    # beta-galactosidase fusion protein localization evidence used in automatic assertion
    ECO_0007213 = "ECO_0007213"
    BETA_GALACTOSIDASE_FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007213"
    )

    # thin layer chromatography evidence used in automatic assertion
    ECO_0007214 = "ECO_0007214"
    THIN_LAYER_CHROMATOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007214"

    # in vitro recombinant protein transcription reconstitution assay evidence used in automatic assertion
    ECO_0007215 = "ECO_0007215"
    IN_VITRO_RECOMBINANT_PROTEIN_TRANSCRIPTION_RECONSTITUTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007215"
    )

    # protein separation followed by direct sequencing evidence used in automatic assertion
    ECO_0007216 = "ECO_0007216"
    PROTEIN_SEPARATION_FOLLOWED_BY_DIRECT_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007216"
    )

    # protein separation followed by fragment identification evidence used in automatic assertion
    ECO_0007217 = "ECO_0007217"
    PROTEIN_SEPARATION_FOLLOWED_BY_FRAGMENT_IDENTIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007217"
    )

    # heterologous system uptake evidence used in automatic assertion
    ECO_0007218 = "ECO_0007218"
    HETEROLOGOUS_SYSTEM_UPTAKE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007218"

    # two-electrode voltage clamp recording evidence used in automatic assertion
    ECO_0007219 = "ECO_0007219"
    TWO_ELECTRODE_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007219"
    )

    # biochemical trait analysis evidence used in automatic assertion
    ECO_0007220 = "ECO_0007220"
    BIOCHEMICAL_TRAIT_ANALYSIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007220"

    # mutant physiological response evidence used in automatic assertion
    ECO_0007221 = "ECO_0007221"
    MUTANT_PHYSIOLOGICAL_RESPONSE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007221"

    # mutant visible phenotype evidence used in automatic assertion
    ECO_0007222 = "ECO_0007222"
    MUTANT_VISIBLE_PHENOTYPE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007222"

    # in vivo assay evidence used in automatic assertion
    ECO_0007223 = "ECO_0007223"
    IN_VIVO_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007223"

    # animal model system study evidence used in automatic assertion
    ECO_0007224 = "ECO_0007224"
    ANIMAL_MODEL_SYSTEM_STUDY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007224"

    # clinical study evidence used in automatic assertion
    ECO_0007225 = "ECO_0007225"
    CLINICAL_STUDY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007225"

    # in vitro assay evidence used in automatic assertion
    ECO_0007226 = "ECO_0007226"
    IN_VITRO_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007226"

    # enzyme inhibition evidence used in automatic assertion
    ECO_0007227 = "ECO_0007227"
    ENZYME_INHIBITION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007227"

    # Illumina sequencing evidence used in automatic assertion
    ECO_0007229 = "ECO_0007229"
    ILLUMINA_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007229"

    # 454 pyrosequencing evidence used in automatic assertion
    ECO_0007230 = "ECO_0007230"
    _454_PYROSEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007230"

    # SOLiD sequencing evidence used in automatic assertion
    ECO_0007231 = "ECO_0007231"
    SOLID_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007231"

    # chain termination sequencing evidence used in automatic assertion
    ECO_0007232 = "ECO_0007232"
    CHAIN_TERMINATION_SEQUENCING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007232"

    # chromatin immunoprecipitation-qPCR evidence used in automatic assertion
    ECO_0007233 = "ECO_0007233"
    CHROMATIN_IMMUNOPRECIPITATION_QPCR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007233"
    )

    # 4C evidence used in automatic assertion
    ECO_0007234 = "ECO_0007234"
    _4C_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007234"

    # 5C evidence used in automatic assertion
    ECO_0007235 = "ECO_0007235"
    _5C_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007235"

    # 3C-qPCR evidence used in automatic assertion
    ECO_0007237 = "ECO_0007237"
    _3C_QPCR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007237"

    # Hi-C evidence used in automatic assertion
    ECO_0007238 = "ECO_0007238"
    HI_C_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007238"

    # 3C-seq evidence used in automatic assertion
    ECO_0007239 = "ECO_0007239"
    _3C_SEQ_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007239"

    # environmental perturbation phenotypic evidence used in automatic assertion
    ECO_0007240 = "ECO_0007240"
    ENVIRONMENTAL_PERTURBATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007240"
    )

    # tissue ablation phenotypic evidence used in automatic assertion
    ECO_0007241 = "ECO_0007241"
    TISSUE_ABLATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007241"

    # tissue grafting phenotypic evidence used in automatic assertion
    ECO_0007242 = "ECO_0007242"
    TISSUE_GRAFTING_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007242"

    # cytochalasin experiment evidence used in automatic assertion
    ECO_0007245 = "ECO_0007245"
    CYTOCHALASIN_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007245"

    # green fluorescent protein immunolocalization evidence used in automatic assertion
    ECO_0007246 = "ECO_0007246"
    GREEN_FLUORESCENT_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007246"
    )

    # beta-galactosidase protein immunolocalization evidence used in automatic assertion
    ECO_0007247 = "ECO_0007247"
    BETA_GALACTOSIDASE_PROTEIN_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007247"
    )

    # cap analysis of gene expression evidence used in automatic assertion
    ECO_0007248 = "ECO_0007248"
    CAP_ANALYSIS_OF_GENE_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007248"

    # nano-cap analysis of gene expression evidence used in automatic assertion
    ECO_0007249 = "ECO_0007249"
    NANO_CAP_ANALYSIS_OF_GENE_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007249"
    )

    # particle size and count assay evidence used in automatic assertion
    ECO_0007250 = "ECO_0007250"
    PARTICLE_SIZE_AND_COUNT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007250"

    # competitive growth assay evidence used in automatic assertion
    ECO_0007251 = "ECO_0007251"
    COMPETITIVE_GROWTH_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007251"

    # pulsed-field gel electrophoresis evidence used in automatic assertion
    ECO_0007252 = "ECO_0007252"
    PULSED_FIELD_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007252"
    )

    # two-dimensional agarose gel electrophoresis evidence used in automatic assertion
    ECO_0007253 = "ECO_0007253"
    TWO_DIMENSIONAL_AGAROSE_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007253"
    )

    # plasmid maintenance assay evidence used in automatic assertion
    ECO_0007254 = "ECO_0007254"
    PLASMID_MAINTENANCE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007254"

    # specific protein inhibition by antibody evidence used in automatic assertion
    ECO_0007255 = "ECO_0007255"
    SPECIFIC_PROTEIN_INHIBITION_BY_ANTIBODY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007255"
    )

    # single exon transcript confirmation via alignment evidence used in automatic assertion
    ECO_0007256 = "ECO_0007256"
    SINGLE_EXON_TRANSCRIPT_CONFIRMATION_VIA_ALIGNMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007256"
    )

    # phylogenetic distribution evidence used in automatic assertion
    ECO_0007257 = "ECO_0007257"
    PHYLOGENETIC_DISTRIBUTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007257"

    # differential geneset expression evidence from microarray experiment (GSEA, Fisher-exact) used in automatic assertion
    ECO_0007258 = "ECO_0007258"
    DIFFERENTIAL_GENESET_EXPRESSION_EVIDENCE_FROM_MICROARRAY_EXPERIMENT__GSEA__FISHER_EXACT__USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007258"
    )

    # differential geneset expression evidence from RNA-seq experiment (GSEA, Fisher-exact) used in automatic assertion
    ECO_0007259 = "ECO_0007259"
    DIFFERENTIAL_GENESET_EXPRESSION_EVIDENCE_FROM_RNA_SEQ_EXPERIMENT__GSEA__FISHER_EXACT__USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007259"
    )

    # biological target-disease association via drug evidence used in automatic assertion
    ECO_0007260 = "ECO_0007260"
    BIOLOGICAL_TARGET_DISEASE_ASSOCIATION_VIA_DRUG_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007260"
    )

    # cell staining evidence used in automatic assertion
    ECO_0007261 = "ECO_0007261"
    CELL_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007261"

    # visual sequence inspection evidence used in automatic assertion
    ECO_0007262 = "ECO_0007262"
    VISUAL_SEQUENCE_INSPECTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007262"

    # ATP bioluminescence assay evidence used in automatic assertion
    ECO_0007263 = "ECO_0007263"
    ATP_BIOLUMINESCENCE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007263"

    # missense mutation phenotypic evidence used in automatic assertion
    ECO_0007264 = "ECO_0007264"
    MISSENSE_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007264"

    # nonsense mutation phenotypic evidence used in automatic assertion
    ECO_0007265 = "ECO_0007265"
    NONSENSE_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007265"

    # silent mutation evidence used in automatic assertion
    ECO_0007266 = "ECO_0007266"
    SILENT_MUTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007266"

    # insertion mutation phenotypic evidence used in automatic assertion
    ECO_0007267 = "ECO_0007267"
    INSERTION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007267"

    # duplication mutation evidence used in automatic assertion
    ECO_0007268 = "ECO_0007268"
    DUPLICATION_MUTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007268"

    # frameshift mutation phenotypic evidence used in automatic assertion
    ECO_0007269 = "ECO_0007269"
    FRAMESHIFT_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007269"

    # repeat expansion mutation phenotypic evidence used in automatic assertion
    ECO_0007270 = "ECO_0007270"
    REPEAT_EXPANSION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007270"
    )

    # splice site mutation phenotypic evidence used in automatic assertion
    ECO_0007271 = "ECO_0007271"
    SPLICE_SITE_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007271"

    # translocation mutation phenotypic evidence used in automatic assertion
    ECO_0007272 = "ECO_0007272"
    TRANSLOCATION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007272"
    )

    # in-gel protein kinase assay evidence used in automatic assertion
    ECO_0007273 = "ECO_0007273"
    IN_GEL_PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007273"

    # macroscopic current trace evidence used in automatic assertion
    ECO_0007274 = "ECO_0007274"
    MACROSCOPIC_CURRENT_TRACE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007274"

    # current density evidence used in automatic assertion
    ECO_0007275 = "ECO_0007275"
    CURRENT_DENSITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007275"

    # sustained current evidence used in automatic assertion
    ECO_0007276 = "ECO_0007276"
    SUSTAINED_CURRENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007276"

    # use dependence of inactivation evidence used in automatic assertion
    ECO_0007277 = "ECO_0007277"
    USE_DEPENDENCE_OF_INACTIVATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007277"

    # current clamp recording evidence used in automatic assertion
    ECO_0007278 = "ECO_0007278"
    CURRENT_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007278"

    # whole-cell voltage clamp recording evidence used in automatic assertion
    ECO_0007279 = "ECO_0007279"
    WHOLE_CELL_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007279"
    )

    # cell-attached single-channel recording evidence used in automatic assertion
    ECO_0007280 = "ECO_0007280"
    CELL_ATTACHED_SINGLE_CHANNEL_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007280"
    )

    # cell-detached inside-out single-channel recording evidence used in automatic assertion
    ECO_0007281 = "ECO_0007281"
    CELL_DETACHED_INSIDE_OUT_SINGLE_CHANNEL_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007281"
    )

    # reconstituted bilayer single-channel patch recording evidence used in automatic assertion
    ECO_0007282 = "ECO_0007282"
    RECONSTITUTED_BILAYER_SINGLE_CHANNEL_PATCH_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007282"
    )

    # electroencephalography recording evidence used in automatic assertion
    ECO_0007283 = "ECO_0007283"
    ELECTROENCEPHALOGRAPHY_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007283"
    )

    # cell-detached outside-out single-channel recording evidence used in automatic assertion
    ECO_0007284 = "ECO_0007284"
    CELL_DETACHED_OUTSIDE_OUT_SINGLE_CHANNEL_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007284"
    )

    # cut-open oocyte voltage clamp recording evidence used in automatic assertion
    ECO_0007285 = "ECO_0007285"
    CUT_OPEN_OOCYTE_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007285"
    )

    # macropatch voltage clamp recording evidence used in automatic assertion
    ECO_0007286 = "ECO_0007286"
    MACROPATCH_VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007286"
    )

    # protein mass spectrometry evidence used in automatic assertion
    ECO_0007288 = "ECO_0007288"
    PROTEIN_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007288"

    # cross-streak test evidence used in automatic assertion
    ECO_0007289 = "ECO_0007289"
    CROSS_STREAK_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007289"

    # tethered cell assay evidence used in automatic assertion
    ECO_0007290 = "ECO_0007290"
    TETHERED_CELL_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007290"

    # tumble frequency assay evidence used in automatic assertion
    ECO_0007291 = "ECO_0007291"
    TUMBLE_FREQUENCY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007291"

    # capillary assay evidence used in automatic assertion
    ECO_0007292 = "ECO_0007292"
    CAPILLARY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007292"

    # inference from experimental data evidence used in automatic assertion
    ECO_0007293 = "ECO_0007293"
    INFERENCE_FROM_EXPERIMENTAL_DATA_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007293"
    )

    # inference from phenotype manipulation evidence used in automatic assertion
    ECO_0007294 = "ECO_0007294"
    INFERENCE_FROM_PHENOTYPE_MANIPULATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007294"
    )

    # inference by association of genotype from phenotype used in automatic assertion
    ECO_0007295 = "ECO_0007295"
    INFERENCE_BY_ASSOCIATION_OF_GENOTYPE_FROM_PHENOTYPE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007295"
    )

    # motility assay evidence used in automatic assertion
    ECO_0007296 = "ECO_0007296"
    MOTILITY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007296"

    # experimental evidence used in automatic assertion
    ECO_0007297 = "ECO_0007297"
    EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007297"

    # expression pattern evidence used in automatic assertion
    ECO_0007298 = "ECO_0007298"
    EXPRESSION_PATTERN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007298"

    # Affymetrix GeneChip evidence used in automatic assertion
    ECO_0007299 = "ECO_0007299"
    AFFYMETRIX_GENECHIP_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007299"

    # cRNA to DNA expression microarray evidence used in automatic assertion
    ECO_0007300 = "ECO_0007300"
    CRNA_TO_DNA_EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007300"
    )

    # expression microarray evidence used in automatic assertion
    ECO_0007301 = "ECO_0007301"
    EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007301"

    # differential methylation hybridization evidence used in automatic assertion
    ECO_0007302 = "ECO_0007302"
    DIFFERENTIAL_METHYLATION_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007302"
    )

    # transcript expression evidence used in automatic assertion
    ECO_0007303 = "ECO_0007303"
    TRANSCRIPT_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007303"

    # Nimblegen array evidence used in automatic assertion
    ECO_0007304 = "ECO_0007304"
    NIMBLEGEN_ARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007304"

    # array-based sequence capture evidence used in automatic assertion
    ECO_0007305 = "ECO_0007305"
    ARRAY_BASED_SEQUENCE_CAPTURE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007305"

    # qualitative western immunoblotting evidence used in automatic assertion
    ECO_0007306 = "ECO_0007306"
    QUALITATIVE_WESTERN_IMMUNOBLOTTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007306"
    )

    # direct assay evidence used in automatic assertion
    ECO_0007307 = "ECO_0007307"
    DIRECT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007307"

    # protein expression evidence used in automatic assertion
    ECO_0007309 = "ECO_0007309"
    PROTEIN_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007309"

    # expression library screen evidence used in automatic assertion
    ECO_0007310 = "ECO_0007310"
    EXPRESSION_LIBRARY_SCREEN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007310"

    # heterologous protein expression evidence used in automatic assertion
    ECO_0007311 = "ECO_0007311"
    HETEROLOGOUS_PROTEIN_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007311"

    # spatial pattern of protein expression evidence used in automatic assertion
    ECO_0007312 = "ECO_0007312"
    SPATIAL_PATTERN_OF_PROTEIN_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007312"
    )

    # DNA to cDNA expression microarray evidence used in automatic assertion
    ECO_0007313 = "ECO_0007313"
    DNA_TO_CDNA_EXPRESSION_MICROARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007313"
    )

    # differential hybridization evidence used in automatic assertion
    ECO_0007314 = "ECO_0007314"
    DIFFERENTIAL_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007314"

    # RNA protection assay evidence used in automatic assertion
    ECO_0007315 = "ECO_0007315"
    RNA_PROTECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007315"

    # nuclease protection assay evidence used in automatic assertion
    ECO_0007316 = "ECO_0007316"
    NUCLEASE_PROTECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007316"

    # spatial pattern of transcript expression evidence used in automatic assertion
    ECO_0007317 = "ECO_0007317"
    SPATIAL_PATTERN_OF_TRANSCRIPT_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007317"
    )

    # subtractive hybridization evidence used in automatic assertion
    ECO_0007318 = "ECO_0007318"
    SUBTRACTIVE_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007318"

    # author statement used in automatic assertion
    ECO_0007319 = "ECO_0007319"
    AUTHOR_STATEMENT_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007319"

    # author statement without traceable support used in automatic assertion
    ECO_0007320 = "ECO_0007320"
    AUTHOR_STATEMENT_WITHOUT_TRACEABLE_SUPPORT_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007320"
    )

    # author statement supported by traceable reference used in automatic assertion
    ECO_0007321 = "ECO_0007321"
    AUTHOR_STATEMENT_SUPPORTED_BY_TRACEABLE_REFERENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007321"
    )

    # curator inference used in automatic assertion
    ECO_0007322 = "ECO_0007322"
    CURATOR_INFERENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007322"

    # inference from background scientific knowledge used in automatic assertion
    ECO_0007323 = "ECO_0007323"
    INFERENCE_FROM_BACKGROUND_SCIENTIFIC_KNOWLEDGE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007323"
    )

    # no evidence data found used in automatic assertion
    ECO_0007324 = "ECO_0007324"
    NO_EVIDENCE_DATA_FOUND_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007324"

    # mutant phenotype evidence used in automatic assertion
    ECO_0007325 = "ECO_0007325"
    MUTANT_PHENOTYPE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007325"

    # genetic interaction evidence used in automatic assertion
    ECO_0007326 = "ECO_0007326"
    GENETIC_INTERACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007326"

    # genomic context evidence used in automatic assertion
    ECO_0007327 = "ECO_0007327"
    GENOMIC_CONTEXT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007327"

    # biological aspect of ancestor evidence used in automatic assertion
    ECO_0007328 = "ECO_0007328"
    BIOLOGICAL_ASPECT_OF_ANCESTOR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007328"

    # biological aspect of descendant evidence used in automatic assertion
    ECO_0007329 = "ECO_0007329"
    BIOLOGICAL_ASPECT_OF_DESCENDANT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007329"

    # phylogenetic determination of loss of key residues evidence used in automatic assertion
    ECO_0007330 = "ECO_0007330"
    PHYLOGENETIC_DETERMINATION_OF_LOSS_OF_KEY_RESIDUES_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007330"
    )

    # rapid divergence from ancestral sequence evidence used in automatic assertion
    ECO_0007331 = "ECO_0007331"
    RAPID_DIVERGENCE_FROM_ANCESTRAL_SEQUENCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007331"
    )

    # physical interaction evidence used in automatic assertion
    ECO_0007332 = "ECO_0007332"
    PHYSICAL_INTERACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007332"

    # gene neighbors evidence used in automatic assertion
    ECO_0007333 = "ECO_0007333"
    GENE_NEIGHBORS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007333"

    # Edman degradation evidence used in automatic assertion
    ECO_0007334 = "ECO_0007334"
    EDMAN_DEGRADATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007334"

    # 3D cell culture evidence used in automatic assertion
    ECO_0007335 = "ECO_0007335"
    _3D_CELL_CULTURE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007335"

    # 51Cr release assay evidence used in automatic assertion
    ECO_0007336 = "ECO_0007336"
    _51CR_RELEASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007336"

    # 7-aminoactinomycin staining evidence used in automatic assertion
    ECO_0007337 = "ECO_0007337"
    _7_AMINOACTINOMYCIN_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007337"

    # [3H]-thymidine incorporation assay evidence used in automatic assertion
    ECO_0007338 = "ECO_0007338"
    _3H__THYMIDINE_INCORPORATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007338"
    )

    # [3H]arachidonic acid release assay evidence used in automatic assertion
    ECO_0007339 = "ECO_0007339"
    _3H_ARACHIDONIC_ACID_RELEASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007339"
    )

    # adhesion assay evidence used in automatic assertion
    ECO_0007340 = "ECO_0007340"
    ADHESION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007340"

    # adoptive cell transfer evidence used in automatic assertion
    ECO_0007341 = "ECO_0007341"
    ADOPTIVE_CELL_TRANSFER_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007341"

    # alamarBlue assay evidence used in automatic assertion
    ECO_0007342 = "ECO_0007342"
    ALAMARBLUE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007342"

    # allograft transplantation phenotypic evidence used in automatic assertion
    ECO_0007343 = "ECO_0007343"
    ALLOGRAFT_TRANSPLANTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007343"
    )

    # anion-exchange chromatography evidence used in automatic assertion
    ECO_0007344 = "ECO_0007344"
    ANION_EXCHANGE_CHROMATOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007344"

    # annexin-V staining evidence used in automatic assertion
    ECO_0007345 = "ECO_0007345"
    ANNEXIN_V_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007345"

    # cognitive assay phenotypic evidence used in automatic assertion
    ECO_0007346 = "ECO_0007346"
    COGNITIVE_ASSAY_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007346"

    # blocking monoclonal antibody evidence used in automatic assertion
    ECO_0007347 = "ECO_0007347"
    BLOCKING_MONOCLONAL_ANTIBODY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007347"

    # immunological assay evidence used in automatic assertion
    ECO_0007348 = "ECO_0007348"
    IMMUNOLOGICAL_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007348"

    # blocking peptide evidence used in automatic assertion
    ECO_0007349 = "ECO_0007349"
    BLOCKING_PEPTIDE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007349"

    # blocking polyclonal antibody evidence used in automatic assertion
    ECO_0007350 = "ECO_0007350"
    BLOCKING_POLYCLONAL_ANTIBODY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007350"

    # blood test evidence used in automatic assertion
    ECO_0007351 = "ECO_0007351"
    BLOOD_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007351"

    # Boyden chamber assay evidence used in automatic assertion
    ECO_0007352 = "ECO_0007352"
    BOYDEN_CHAMBER_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007352"

    # bromodeoxyuridine incorporation assay evidence used in automatic assertion
    ECO_0007353 = "ECO_0007353"
    BROMODEOXYURIDINE_INCORPORATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007353"
    )

    # nucleotide analog incorporation assay evidence used in automatic assertion
    ECO_0007354 = "ECO_0007354"
    NUCLEOTIDE_ANALOG_INCORPORATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007354"
    )

    # caspase assay evidence used in automatic assertion
    ECO_0007355 = "ECO_0007355"
    CASPASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007355"

    # cell counting evidence used in automatic assertion
    ECO_0007356 = "ECO_0007356"
    CELL_COUNTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007356"

    # cell permeability assay evidence used in automatic assertion
    ECO_0007357 = "ECO_0007357"
    CELL_PERMEABILITY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007357"

    # carboxyfluorescein diacetate succinimidyl ester staining evidence used in automatic assertion
    ECO_0007358 = "ECO_0007358"
    CARBOXYFLUORESCEIN_DIACETATE_SUCCINIMIDYL_ESTER_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007358"
    )

    # chemiluminescence-linked immunoassay evidence used in automatic assertion
    ECO_0007359 = "ECO_0007359"
    CHEMILUMINESCENCE_LINKED_IMMUNOASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007359"
    )

    # chimeric protein phenotypic evidence used in automatic assertion
    ECO_0007360 = "ECO_0007360"
    CHIMERIC_PROTEIN_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007360"

    # co-electrophoresis evidence used in automatic assertion
    ECO_0007361 = "ECO_0007361"
    CO_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007361"

    # co-localization evidence used in automatic assertion
    ECO_0007362 = "ECO_0007362"
    CO_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007362"

    # imaging assay evidence used in automatic assertion
    ECO_0007363 = "ECO_0007363"
    IMAGING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007363"

    # co-sedimentation assay evidence used in automatic assertion
    ECO_0007364 = "ECO_0007364"
    CO_SEDIMENTATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007364"

    # colony counting evidence used in automatic assertion
    ECO_0007365 = "ECO_0007365"
    COLONY_COUNTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007365"

    # comet assay evidence used in automatic assertion
    ECO_0007366 = "ECO_0007366"
    COMET_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007366"

    # conditional knockin evidence used in automatic assertion
    ECO_0007367 = "ECO_0007367"
    CONDITIONAL_KNOCKIN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007367"

    # knockin evidence used in automatic assertion
    ECO_0007368 = "ECO_0007368"
    KNOCKIN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007368"

    # conditional knockout evidence used in automatic assertion
    ECO_0007369 = "ECO_0007369"
    CONDITIONAL_KNOCKOUT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007369"

    # knockout evidence used in automatic assertion
    ECO_0007370 = "ECO_0007370"
    KNOCKOUT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007370"

    # constitutively active mutant evidence used in automatic assertion
    ECO_0007371 = "ECO_0007371"
    CONSTITUTIVELY_ACTIVE_MUTANT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007371"

    # cross-linking evidence used in automatic assertion
    ECO_0007372 = "ECO_0007372"
    CROSS_LINKING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007372"

    # protein binding evidence used in automatic assertion
    ECO_0007373 = "ECO_0007373"
    PROTEIN_BINDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007373"

    # crystallography evidence used in automatic assertion
    ECO_0007374 = "ECO_0007374"
    CRYSTALLOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007374"

    # cytochemistry evidence used in automatic assertion
    ECO_0007375 = "ECO_0007375"
    CYTOCHEMISTRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007375"

    # histochemistry evidence used in automatic assertion
    ECO_0007376 = "ECO_0007376"
    HISTOCHEMISTRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007376"

    # cytochrome C release assay evidence used in automatic assertion
    ECO_0007377 = "ECO_0007377"
    CYTOCHROME_C_RELEASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007377"

    # 4',6-diamidino-2-phenylindole staining evidence used in automatic assertion
    ECO_0007378 = "ECO_0007378"
    _4__6_DIAMIDINO_2_PHENYLINDOLE_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007378"
    )

    # deletion mutation phenotypic evidence used in automatic assertion
    ECO_0007379 = "ECO_0007379"
    DELETION_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007379"

    # DNA laddering assay evidence used in automatic assertion
    ECO_0007380 = "ECO_0007380"
    DNA_LADDERING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007380"

    # RNA dot blot assay evidence used in automatic assertion
    ECO_0007381 = "ECO_0007381"
    RNA_DOT_BLOT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007381"

    # dominant-negative mutant phenotypic evidence used in automatic assertion
    ECO_0007382 = "ECO_0007382"
    DOMINANT_NEGATIVE_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007382"
    )

    # eTag assay evidence used in automatic assertion
    ECO_0007383 = "ECO_0007383"
    ETAG_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007383"

    # affinity evidence used in automatic assertion
    ECO_0007384 = "ECO_0007384"
    AFFINITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007384"

    # filter binding assay evidence used in automatic assertion
    ECO_0007385 = "ECO_0007385"
    FILTER_BINDING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007385"

    # fluorescence in situ hybridization evidence used in automatic assertion
    ECO_0007386 = "ECO_0007386"
    FLUORESCENCE_IN_SITU_HYBRIDIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007386"
    )

    # fluorescence resonance energy transfer evidence used in automatic assertion
    ECO_0007387 = "ECO_0007387"
    FLUORESCENCE_RESONANCE_ENERGY_TRANSFER_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007387"
    )

    # gel-filtration evidence used in automatic assertion
    ECO_0007388 = "ECO_0007388"
    GEL_FILTRATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007388"

    # histology evidence used in automatic assertion
    ECO_0007389 = "ECO_0007389"
    HISTOLOGY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007389"

    # immunocytochemistry evidence used in automatic assertion
    ECO_0007390 = "ECO_0007390"
    IMMUNOCYTOCHEMISTRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007390"

    # immunodepletion evidence used in automatic assertion
    ECO_0007391 = "ECO_0007391"
    IMMUNODEPLETION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007391"

    # immunohistochemistry evidence used in automatic assertion
    ECO_0007392 = "ECO_0007392"
    IMMUNOHISTOCHEMISTRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007392"

    # in vitro acetylation assay evidence used in automatic assertion
    ECO_0007393 = "ECO_0007393"
    IN_VITRO_ACETYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007393"

    # in vitro cleavage assay evidence used in automatic assertion
    ECO_0007394 = "ECO_0007394"
    IN_VITRO_CLEAVAGE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007394"

    # in vitro deacetylation assay evidence used in automatic assertion
    ECO_0007395 = "ECO_0007395"
    IN_VITRO_DEACETYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007395"

    # in vitro defarnesylation assay evidence used in automatic assertion
    ECO_0007396 = "ECO_0007396"
    IN_VITRO_DEFARNESYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007396"

    # in vitro demethylation assay evidence used in automatic assertion
    ECO_0007397 = "ECO_0007397"
    IN_VITRO_DEMETHYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007397"

    # in vitro desumoylation assay evidence used in automatic assertion
    ECO_0007398 = "ECO_0007398"
    IN_VITRO_DESUMOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007398"

    # in vitro deubiquitination assay evidence used in automatic assertion
    ECO_0007399 = "ECO_0007399"
    IN_VITRO_DEUBIQUITINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007399"

    # in vitro farnesylation assay evidence used in automatic assertion
    ECO_0007400 = "ECO_0007400"
    IN_VITRO_FARNESYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007400"

    # in vitro methylation assay evidence used in automatic assertion
    ECO_0007401 = "ECO_0007401"
    IN_VITRO_METHYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007401"

    # in vitro palmitoylation assay evidence used in automatic assertion
    ECO_0007402 = "ECO_0007402"
    IN_VITRO_PALMITOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007402"

    # in vitro phosphatase assay evidence used in automatic assertion
    ECO_0007403 = "ECO_0007403"
    IN_VITRO_PHOSPHATASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007403"

    # in vitro polyADP-ribosylation assay evidence used in automatic assertion
    ECO_0007404 = "ECO_0007404"
    IN_VITRO_POLYADP_RIBOSYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007404"
    )

    # in vitro protein kinase assay evidence used in automatic assertion
    ECO_0007405 = "ECO_0007405"
    IN_VITRO_PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007405"

    # in vitro sumoylation assay evidence used in automatic assertion
    ECO_0007406 = "ECO_0007406"
    IN_VITRO_SUMOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007406"

    # in vitro transcription assay evidence used in automatic assertion
    ECO_0007407 = "ECO_0007407"
    IN_VITRO_TRANSCRIPTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007407"

    # in vitro translation assay evidence used in automatic assertion
    ECO_0007408 = "ECO_0007408"
    IN_VITRO_TRANSLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007408"

    # in vitro ubiquitination assay evidence used in automatic assertion
    ECO_0007409 = "ECO_0007409"
    IN_VITRO_UBIQUITINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007409"

    # in vivo acetylation assay evidence used in automatic assertion
    ECO_0007410 = "ECO_0007410"
    IN_VIVO_ACETYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007410"

    # in vivo cleavage assay evidence used in automatic assertion
    ECO_0007411 = "ECO_0007411"
    IN_VIVO_CLEAVAGE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007411"

    # in vivo deacetylation assay evidence used in automatic assertion
    ECO_0007412 = "ECO_0007412"
    IN_VIVO_DEACETYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007412"

    # in vivo defarnesylation assay evidence used in automatic assertion
    ECO_0007413 = "ECO_0007413"
    IN_VIVO_DEFARNESYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007413"

    # in vivo demethylation assay evidence used in automatic assertion
    ECO_0007414 = "ECO_0007414"
    IN_VIVO_DEMETHYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007414"

    # in vivo desumoylation assay evidence used in automatic assertion
    ECO_0007415 = "ECO_0007415"
    IN_VIVO_DESUMOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007415"

    # in vivo deubiquitination assay evidence used in automatic assertion
    ECO_0007416 = "ECO_0007416"
    IN_VIVO_DEUBIQUITINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007416"

    # in vivo farnesylation assay evidence used in automatic assertion
    ECO_0007417 = "ECO_0007417"
    IN_VIVO_FARNESYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007417"

    # in vivo methylation assay evidence used in automatic assertion
    ECO_0007418 = "ECO_0007418"
    IN_VIVO_METHYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007418"

    # in vivo palmitoylation assay evidence used in automatic assertion
    ECO_0007419 = "ECO_0007419"
    IN_VIVO_PALMITOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007419"

    # in vivo phosphatase assay evidence used in automatic assertion
    ECO_0007420 = "ECO_0007420"
    IN_VIVO_PHOSPHATASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007420"

    # in vivo protein kinase assay evidence used in automatic assertion
    ECO_0007421 = "ECO_0007421"
    IN_VIVO_PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007421"

    # in vivo sumoylation assay evidence used in automatic assertion
    ECO_0007422 = "ECO_0007422"
    IN_VIVO_SUMOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007422"

    # in vivo transcription assay evidence used in automatic assertion
    ECO_0007423 = "ECO_0007423"
    IN_VIVO_TRANSCRIPTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007423"

    # in vivo translation assay evidence used in automatic assertion
    ECO_0007424 = "ECO_0007424"
    IN_VIVO_TRANSLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007424"

    # in vivo ubiquitination assay evidence used in automatic assertion
    ECO_0007425 = "ECO_0007425"
    IN_VIVO_UBIQUITINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007425"

    # induced mutation evidence used in automatic assertion
    ECO_0007426 = "ECO_0007426"
    INDUCED_MUTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007426"

    # genetic transformation evidence used in automatic assertion
    ECO_0007427 = "ECO_0007427"
    GENETIC_TRANSFORMATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007427"

    # lipid binding assay evidence used in automatic assertion
    ECO_0007428 = "ECO_0007428"
    LIPID_BINDING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007428"

    # luminescence-based mammalian interactome mapping assay evidence used in automatic assertion
    ECO_0007429 = "ECO_0007429"
    LUMINESCENCE_BASED_MAMMALIAN_INTERACTOME_MAPPING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007429"
    )

    # macroscopy evidence used in automatic assertion
    ECO_0007430 = "ECO_0007430"
    MACROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007430"

    # mammalian 2-hybrid assay evidence used in automatic assertion
    ECO_0007431 = "ECO_0007431"
    MAMMALIAN_2_HYBRID_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007431"

    # bait-prey hybrid interaction evidence used in automatic assertion
    ECO_0007432 = "ECO_0007432"
    BAIT_PREY_HYBRID_INTERACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007432"

    # mass spectrometry evidence used in automatic assertion
    ECO_0007433 = "ECO_0007433"
    MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007433"

    # medical imaging evidence used in automatic assertion
    ECO_0007434 = "ECO_0007434"
    MEDICAL_IMAGING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007434"

    # microscopy evidence used in automatic assertion
    ECO_0007435 = "ECO_0007435"
    MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007435"

    # motility wound healing assay evidence used in automatic assertion
    ECO_0007436 = "ECO_0007436"
    MOTILITY_WOUND_HEALING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007436"

    # MTS assay evidence used in automatic assertion
    ECO_0007437 = "ECO_0007437"
    MTS_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007437"

    # MTT assay evidence used in automatic assertion
    ECO_0007438 = "ECO_0007438"
    MTT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007438"

    # multiplex bead-based immunoassay evidence used in automatic assertion
    ECO_0007439 = "ECO_0007439"
    MULTIPLEX_BEAD_BASED_IMMUNOASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007439"
    )

    # natural variation mutant evidence used in automatic assertion
    ECO_0007440 = "ECO_0007440"
    NATURAL_VARIATION_MUTANT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007440"

    # nuclear magnetic resonance evidence used in automatic assertion
    ECO_0007441 = "ECO_0007441"
    NUCLEAR_MAGNETIC_RESONANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007441"

    # nuclear fragmentation evidence used in automatic assertion
    ECO_0007442 = "ECO_0007442"
    NUCLEAR_FRAGMENTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007442"

    # phage display evidence used in automatic assertion
    ECO_0007443 = "ECO_0007443"
    PHAGE_DISPLAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007443"

    # phosphoamino acid analysis evidence used in automatic assertion
    ECO_0007444 = "ECO_0007444"
    PHOSPHOAMINO_ACID_ANALYSIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007444"

    # peptide affinity enrichment evidence used in automatic assertion
    ECO_0007445 = "ECO_0007445"
    PEPTIDE_AFFINITY_ENRICHMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007445"

    # peptide array evidence used in automatic assertion
    ECO_0007446 = "ECO_0007446"
    PEPTIDE_ARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007446"

    # physical examination evidence used in automatic assertion
    ECO_0007447 = "ECO_0007447"
    PHYSICAL_EXAMINATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007447"

    # point mutation phenotypic evidence used in automatic assertion
    ECO_0007448 = "ECO_0007448"
    POINT_MUTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007448"

    # propidium iodide staining evidence used in automatic assertion
    ECO_0007449 = "ECO_0007449"
    PROPIDIUM_IODIDE_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007449"

    # fluorescence evidence used in automatic assertion
    ECO_0007450 = "ECO_0007450"
    FLUORESCENCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007450"

    # protein dot blot assay evidence used in automatic assertion
    ECO_0007451 = "ECO_0007451"
    PROTEIN_DOT_BLOT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007451"

    # protein microarray evidence used in automatic assertion
    ECO_0007452 = "ECO_0007452"
    PROTEIN_MICROARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007452"

    # protein sequencing assay evidence used in automatic assertion
    ECO_0007453 = "ECO_0007453"
    PROTEIN_SEQUENCING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007453"

    # quantitative mass spectrometry evidence used in automatic assertion
    ECO_0007454 = "ECO_0007454"
    QUANTITATIVE_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007454"

    # radioisotope assay evidence used in automatic assertion
    ECO_0007455 = "ECO_0007455"
    RADIOISOTOPE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007455"

    # radioimmunoassay evidence used in automatic assertion
    ECO_0007456 = "ECO_0007456"
    RADIOIMMUNOASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007456"

    # restriction fragment detection evidence used in automatic assertion
    ECO_0007457 = "ECO_0007457"
    RESTRICTION_FRAGMENT_DETECTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007457"

    # spectrophotometry evidence used in automatic assertion
    ECO_0007458 = "ECO_0007458"
    SPECTROPHOTOMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007458"

    # syngeneic transplantation experiment evidence used in automatic assertion
    ECO_0007459 = "ECO_0007459"
    SYNGENEIC_TRANSPLANTATION_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007459"
    )

    # xenotransplantation phenotypic evidence used in automatic assertion
    ECO_0007460 = "ECO_0007460"
    XENOTRANSPLANTATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007460"

    # WST-1 assay evidence used in automatic assertion
    ECO_0007461 = "ECO_0007461"
    WST_1_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007461"

    # urine test evidence used in automatic assertion
    ECO_0007462 = "ECO_0007462"
    URINE_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007462"

    # terminal deoxynucleotidyl transferase dUTP nick end labeling assay evidence used in automatic assertion
    ECO_0007463 = "ECO_0007463"
    TERMINAL_DEOXYNUCLEOTIDYL_TRANSFERASE_DUTP_NICK_END_LABELING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007463"
    )

    # tryptic phosphopeptide mapping assay evidence used in automatic assertion
    ECO_0007464 = "ECO_0007464"
    TRYPTIC_PHOSPHOPEPTIDE_MAPPING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007464"
    )

    # transgenic organism evidence used in automatic assertion
    ECO_0007465 = "ECO_0007465"
    TRANSGENIC_ORGANISM_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007465"

    # tissue microarray evidence used in automatic assertion
    ECO_0007466 = "ECO_0007466"
    TISSUE_MICROARRAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007466"

    # TACE activity assay evidence used in automatic assertion
    ECO_0007467 = "ECO_0007467"
    TACE_ACTIVITY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007467"

    # enzymatic activity assay evidence used in automatic assertion
    ECO_0007468 = "ECO_0007468"
    ENZYMATIC_ACTIVITY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007468"

    # surface plasmon resonance evidence used in automatic assertion
    ECO_0007469 = "ECO_0007469"
    SURFACE_PLASMON_RESONANCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007469"

    # restriction landmark genomic scanning evidence used in automatic assertion
    ECO_0007470 = "ECO_0007470"
    RESTRICTION_LANDMARK_GENOMIC_SCANNING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007470"
    )

    # resonant mirror biosensor evidence used in automatic assertion
    ECO_0007471 = "ECO_0007471"
    RESONANT_MIRROR_BIOSENSOR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007471"

    # high-performance liquid chromatography evidence used in automatic assertion
    ECO_0007472 = "ECO_0007472"
    HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007472"
    )

    # ectopic expression evidence used in automatic assertion
    ECO_0007473 = "ECO_0007473"
    ECTOPIC_EXPRESSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007473"

    # electrophoretic mobility shift assay evidence used in automatic assertion
    ECO_0007474 = "ECO_0007474"
    ELECTROPHORETIC_MOBILITY_SHIFT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007474"
    )

    # reverse transcription polymerase chain reaction evidence used in automatic assertion
    ECO_0007475 = "ECO_0007475"
    REVERSE_TRANSCRIPTION_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007475"
    )

    # in vivo polyADP-ribosylation assay evidence used in automatic assertion
    ECO_0007476 = "ECO_0007476"
    IN_VIVO_POLYADP_RIBOSYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007476"
    )

    # DNA dot blot assay evidence used in automatic assertion
    ECO_0007477 = "ECO_0007477"
    DNA_DOT_BLOT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007477"

    # random mutagenesis evidence used in automatic assertion
    ECO_0007478 = "ECO_0007478"
    RANDOM_MUTAGENESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007478"

    # biological system reconstruction evidence by experimental evidence from single species used in automatic assertion
    ECO_0007479 = "ECO_0007479"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_FROM_SINGLE_SPECIES_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007479"
    )

    # biological system reconstruction evidence by experimental evidence from mixed species used in automatic assertion
    ECO_0007480 = "ECO_0007480"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_FROM_MIXED_SPECIES_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007480"
    )

    # biological system reconstruction evidence based on orthology evidence used in automatic assertion
    ECO_0007481 = "ECO_0007481"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_ORTHOLOGY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007481"
    )

    # biological system reconstruction evidence based on homology evidence used in automatic assertion
    ECO_0007482 = "ECO_0007482"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_HOMOLOGY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007482"
    )

    # biological system reconstruction evidence based on paralogy evidence used in automatic assertion
    ECO_0007483 = "ECO_0007483"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_PARALOGY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007483"
    )

    # biological system reconstruction evidence based on inference from background scientific knowledge used in automatic assertion
    ECO_0007484 = "ECO_0007484"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BASED_ON_INFERENCE_FROM_BACKGROUND_SCIENTIFIC_KNOWLEDGE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007484"
    )

    # immunogold labelling evidence used in automatic assertion
    ECO_0007485 = "ECO_0007485"
    IMMUNOGOLD_LABELLING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007485"

    # immunolocalization evidence used in automatic assertion
    ECO_0007486 = "ECO_0007486"
    IMMUNOLOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007486"

    # flow cytometry evidence used in automatic assertion
    ECO_0007487 = "ECO_0007487"
    FLOW_CYTOMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007487"

    # enzyme-linked immunoabsorbent assay evidence used in automatic assertion
    ECO_0007488 = "ECO_0007488"
    ENZYME_LINKED_IMMUNOABSORBENT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007488"
    )

    # high throughput mass spectrometry evidence used in automatic assertion
    ECO_0007489 = "ECO_0007489"
    HIGH_THROUGHPUT_MASS_SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007489"
    )

    # confocal microscopy evidence used in automatic assertion
    ECO_0007490 = "ECO_0007490"
    CONFOCAL_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007490"

    # wide-field microscopy evidence used in automatic assertion
    ECO_0007491 = "ECO_0007491"
    WIDE_FIELD_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007491"

    # immunogold labelling electron microscopy assay evidence used in automatic assertion
    ECO_0007492 = "ECO_0007492"
    IMMUNOGOLD_LABELLING_ELECTRON_MICROSCOPY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007492"
    )

    # electron microscopy evidence used in automatic assertion
    ECO_0007493 = "ECO_0007493"
    ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007493"

    # immunoperoxidase immunolocalization evidence used in automatic assertion
    ECO_0007494 = "ECO_0007494"
    IMMUNOPEROXIDASE_IMMUNOLOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007494"
    )

    # immunoperoxidase immunolocalization electron microscopy evidence used in automatic assertion
    ECO_0007495 = "ECO_0007495"
    IMMUNOPEROXIDASE_IMMUNOLOCALIZATION_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007495"
    )

    # immunofluorescence confocal microscopy evidence used in automatic assertion
    ECO_0007496 = "ECO_0007496"
    IMMUNOFLUORESCENCE_CONFOCAL_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007496"
    )

    # immunofluorescence evidence used in automatic assertion
    ECO_0007497 = "ECO_0007497"
    IMMUNOFLUORESCENCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007497"

    # two-dimensional polyacrylamide gel electrophoresis evidence used in automatic assertion
    ECO_0007498 = "ECO_0007498"
    TWO_DIMENSIONAL_POLYACRYLAMIDE_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007498"
    )

    # alkaline phosphatase reporter gene assay evidence used in automatic assertion
    ECO_0007499 = "ECO_0007499"
    ALKALINE_PHOSPHATASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007499"
    )

    # beta-galactosidase reporter gene assay evidence used in automatic assertion
    ECO_0007500 = "ECO_0007500"
    BETA_GALACTOSIDASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007500"
    )

    # chloramphenicol acetyltransferase reporter gene assay evidence used in automatic assertion
    ECO_0007501 = "ECO_0007501"
    CHLORAMPHENICOL_ACETYLTRANSFERASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007501"
    )

    # chromatin immunoprecipitation-PCR evidence used in automatic assertion
    ECO_0007502 = "ECO_0007502"
    CHROMATIN_IMMUNOPRECIPITATION_PCR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007502"
    )

    # immunoprecipitation evidence used in automatic assertion
    ECO_0007503 = "ECO_0007503"
    IMMUNOPRECIPITATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007503"

    # copper-phenanthroline footprinting evidence used in automatic assertion
    ECO_0007504 = "ECO_0007504"
    COPPER_PHENANTHROLINE_FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007504"
    )

    # nucleic acid binding evidence used in automatic assertion
    ECO_0007505 = "ECO_0007505"
    NUCLEIC_ACID_BINDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007505"

    # DNA affinity chromatography evidence used in automatic assertion
    ECO_0007506 = "ECO_0007506"
    DNA_AFFINITY_CHROMATOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007506"

    # DNAse footprinting evidence used in automatic assertion
    ECO_0007507 = "ECO_0007507"
    DNASE_FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007507"

    # fluorescence anisotropy evidence used in automatic assertion
    ECO_0007508 = "ECO_0007508"
    FLUORESCENCE_ANISOTROPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007508"

    # ferric uptake regulator titration assay evidence used in automatic assertion
    ECO_0007509 = "ECO_0007509"
    FERRIC_UPTAKE_REGULATOR_TITRATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007509"
    )

    # systematic evolution of ligands by exponential amplification evidence used in automatic assertion
    ECO_0007510 = "ECO_0007510"
    SYSTEMATIC_EVOLUTION_OF_LIGANDS_BY_EXPONENTIAL_AMPLIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007510"
    )

    # glutathione S-transferase pull-down assay evidence used in automatic assertion
    ECO_0007511 = "ECO_0007511"
    GLUTATHIONE_S_TRANSFERASE_PULL_DOWN_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007511"
    )

    # beta-glucuronidase reporter gene assay evidence used in automatic assertion
    ECO_0007512 = "ECO_0007512"
    BETA_GLUCURONIDASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007512"
    )

    # heteronuclear single quantum coherence spectroscopy evidence used in automatic assertion
    ECO_0007513 = "ECO_0007513"
    HETERONUCLEAR_SINGLE_QUANTUM_COHERENCE_SPECTROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007513"
    )

    # hydroxyl-radical footprinting evidence used in automatic assertion
    ECO_0007514 = "ECO_0007514"
    HYDROXYL_RADICAL_FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007514"

    # isothermal titration calorimetry evidence used in automatic assertion
    ECO_0007515 = "ECO_0007515"
    ISOTHERMAL_TITRATION_CALORIMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007515"
    )

    # luciferase reporter gene assay evidence used in automatic assertion
    ECO_0007516 = "ECO_0007516"
    LUCIFERASE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007516"

    # methidiumpropyl-ethylenediaminetetraacetic acid iron (II) footprinting evidence used in automatic assertion
    ECO_0007517 = "ECO_0007517"
    METHIDIUMPROPYL_ETHYLENEDIAMINETETRAACETIC_ACID_IRON__II__FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007517"
    )

    # northern blot evidence used in automatic assertion
    ECO_0007518 = "ECO_0007518"
    NORTHERN_BLOT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007518"

    # methylation interference footprinting evidence used in automatic assertion
    ECO_0007519 = "ECO_0007519"
    METHYLATION_INTERFERENCE_FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007519"
    )

    # primer extension assay evidence used in automatic assertion
    ECO_0007520 = "ECO_0007520"
    PRIMER_EXTENSION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007520"

    # quantitative polymerase chain reaction evidence used in automatic assertion
    ECO_0007521 = "ECO_0007521"
    QUANTITATIVE_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007521"
    )

    # rapid amplification of cDNA ends polymerase chain reaction evidence used in automatic assertion
    ECO_0007522 = "ECO_0007522"
    RAPID_AMPLIFICATION_OF_CDNA_ENDS_POLYMERASE_CHAIN_REACTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007522"
    )

    # S1 nuclease protection assay evidence used in automatic assertion
    ECO_0007523 = "ECO_0007523"
    S1_NUCLEASE_PROTECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007523"

    # site-directed mutagenesis phenotypic evidence used in automatic assertion
    ECO_0007524 = "ECO_0007524"
    SITE_DIRECTED_MUTAGENESIS_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007524"
    )

    # survival rate analysis evidence used in automatic assertion
    ECO_0007525 = "ECO_0007525"
    SURVIVAL_RATE_ANALYSIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007525"

    # ultraviolet light footprinting evidence used in automatic assertion
    ECO_0007526 = "ECO_0007526"
    ULTRAVIOLET_LIGHT_FOOTPRINTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007526"

    # xylE reporter gene assay evidence used in automatic assertion
    ECO_0007527 = "ECO_0007527"
    XYLE_REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007527"

    # ad-hoc qualitative phenotype observation evidence used in automatic assertion
    ECO_0007528 = "ECO_0007528"
    AD_HOC_QUALITATIVE_PHENOTYPE_OBSERVATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007528"
    )

    # ad-hoc quantitative phenotype observation evidence used in automatic assertion
    ECO_0007529 = "ECO_0007529"
    AD_HOC_QUANTITATIVE_PHENOTYPE_OBSERVATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007529"
    )

    # cell transfection experiment evidence used in automatic assertion
    ECO_0007530 = "ECO_0007530"
    CELL_TRANSFECTION_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007530"

    # yeast 2-hybrid evidence used in automatic assertion
    ECO_0007531 = "ECO_0007531"
    YEAST_2_HYBRID_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007531"

    # Cya fusion reporter assay evidence used in automatic assertion
    ECO_0007532 = "ECO_0007532"
    CYA_FUSION_REPORTER_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007532"

    # super-resolution microscopy evidence used in automatic assertion
    ECO_0007533 = "ECO_0007533"
    SUPER_RESOLUTION_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007533"

    # fractionation evidence used in automatic assertion
    ECO_0007534 = "ECO_0007534"
    FRACTIONATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007534"

    # electrophysiology assay evidence used in automatic assertion
    ECO_0007535 = "ECO_0007535"
    ELECTROPHYSIOLOGY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007535"

    # mRNA interactome capture evidence used in automatic assertion
    ECO_0007536 = "ECO_0007536"
    MRNA_INTERACTOME_CAPTURE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007536"

    # patch-clamp recording evidence used in automatic assertion
    ECO_0007537 = "ECO_0007537"
    PATCH_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007537"

    # whole-cell patch-clamp recording evidence used in automatic assertion
    ECO_0007538 = "ECO_0007538"
    WHOLE_CELL_PATCH_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007538"
    )

    # author statement from published clinical study used in automatic assertion
    ECO_0007539 = "ECO_0007539"
    AUTHOR_STATEMENT_FROM_PUBLISHED_CLINICAL_STUDY_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007539"
    )

    # inference based on individual clinical experience used in automatic assertion
    ECO_0007540 = "ECO_0007540"
    INFERENCE_BASED_ON_INDIVIDUAL_CLINICAL_EXPERIENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007540"
    )

    # biofilm formation assay evidence used in automatic assertion
    ECO_0007541 = "ECO_0007541"
    BIOFILM_FORMATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007541"

    # microtiter plate biofilm assay evidence used in automatic assertion
    ECO_0007542 = "ECO_0007542"
    MICROTITER_PLATE_BIOFILM_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007542"

    # air-liquid interface assay evidence used in automatic assertion
    ECO_0007543 = "ECO_0007543"
    AIR_LIQUID_INTERFACE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007543"

    # colony biofilm assay evidence used in automatic assertion
    ECO_0007544 = "ECO_0007544"
    COLONY_BIOFILM_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007544"

    # Kadouri drip-fed biofilm assay evidence used in automatic assertion
    ECO_0007545 = "ECO_0007545"
    KADOURI_DRIP_FED_BIOFILM_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007545"

    # co-immunoprecipitation evidence used in automatic assertion
    ECO_0007546 = "ECO_0007546"
    CO_IMMUNOPRECIPITATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007546"

    # optogenetic evidence used in automatic assertion
    ECO_0007547 = "ECO_0007547"
    OPTOGENETIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007547"

    # fluorescent sensor evidence used in automatic assertion
    ECO_0007548 = "ECO_0007548"
    FLUORESCENT_SENSOR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007548"

    # genetically encoded fluorescent sensor evidence used in automatic assertion
    ECO_0007549 = "ECO_0007549"
    GENETICALLY_ENCODED_FLUORESCENT_SENSOR_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007549"
    )

    # genetically encoded fluorescent electrophysiology assay evidence used in automatic assertion
    ECO_0007550 = "ECO_0007550"
    GENETICALLY_ENCODED_FLUORESCENT_ELECTROPHYSIOLOGY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007550"
    )

    # genetically encoded fluorescent ion concentration sensor assay evidence used in automatic assertion
    ECO_0007551 = "ECO_0007551"
    GENETICALLY_ENCODED_FLUORESCENT_ION_CONCENTRATION_SENSOR_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007551"
    )

    # cell fractionation evidence used in automatic assertion
    ECO_0007552 = "ECO_0007552"
    CELL_FRACTIONATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007552"

    # extracellular recording evidence used in automatic assertion
    ECO_0007553 = "ECO_0007553"
    EXTRACELLULAR_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007553"

    # single-unit extracellular recording evidence used in automatic assertion
    ECO_0007554 = "ECO_0007554"
    SINGLE_UNIT_EXTRACELLULAR_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007554"
    )

    # field potential recording evidence used in automatic assertion
    ECO_0007555 = "ECO_0007555"
    FIELD_POTENTIAL_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007555"

    # anti-sense experiment evidence used in automatic assertion
    ECO_0007556 = "ECO_0007556"
    ANTI_SENSE_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007556"

    # morpholino experiment evidence used in automatic assertion
    ECO_0007557 = "ECO_0007557"
    MORPHOLINO_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007557"

    # RNAi evidence used in automatic assertion
    ECO_0007558 = "ECO_0007558"
    RNAI_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007558"

    # pharmacological assay evidence used in automatic assertion
    ECO_0007559 = "ECO_0007559"
    PHARMACOLOGICAL_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007559"

    # immunofluorescence wide-field microscopy evidence used in automatic assertion
    ECO_0007560 = "ECO_0007560"
    IMMUNOFLUORESCENCE_WIDE_FIELD_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007560"
    )

    # wide-field fluorescence microscopy evidence used in automatic assertion
    ECO_0007561 = "ECO_0007561"
    WIDE_FIELD_FLUORESCENCE_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007561"
    )

    # over expression analysis evidence used in automatic assertion
    ECO_0007562 = "ECO_0007562"
    OVER_EXPRESSION_ANALYSIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007562"

    # cell-free assay evidence used in automatic assertion
    ECO_0007563 = "ECO_0007563"
    CELL_FREE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007563"

    # fluorescence recovery after photobleaching evidence used in automatic assertion
    ECO_0007564 = "ECO_0007564"
    FLUORESCENCE_RECOVERY_AFTER_PHOTOBLEACHING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007564"
    )

    # immuno-labelling electron microscopy evidence used in automatic assertion
    ECO_0007565 = "ECO_0007565"
    IMMUNO_LABELLING_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007565"
    )

    # immunofluorescence super resolution microscopy evidence used in automatic assertion
    ECO_0007566 = "ECO_0007566"
    IMMUNOFLUORESCENCE_SUPER_RESOLUTION_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007566"
    )

    # co-purification evidence used in automatic assertion
    ECO_0007567 = "ECO_0007567"
    CO_PURIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007567"

    # yeast one-hybrid evidence used in automatic assertion
    ECO_0007568 = "ECO_0007568"
    YEAST_ONE_HYBRID_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007568"

    # split-ubiquitin functional complementation evidence used in automatic assertion
    ECO_0007569 = "ECO_0007569"
    SPLIT_UBIQUITIN_FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007569"
    )

    # far-Western blotting evidence used in automatic assertion
    ECO_0007570 = "ECO_0007570"
    FAR_WESTERN_BLOTTING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007570"

    # affinity chromatography evidence used in automatic assertion
    ECO_0007571 = "ECO_0007571"
    AFFINITY_CHROMATOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007571"

    # ribohomopolymer binding assay evidence used in automatic assertion
    ECO_0007572 = "ECO_0007572"
    RIBOHOMOPOLYMER_BINDING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007572"

    # protein:ion binding evidence used in automatic assertion
    ECO_0007573 = "ECO_0007573"
    PROTEIN_ION_BINDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007573"

    # Southwestern blot evidence used in automatic assertion
    ECO_0007574 = "ECO_0007574"
    SOUTHWESTERN_BLOT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007574"

    # Northwestern blot evidence used in automatic assertion
    ECO_0007575 = "ECO_0007575"
    NORTHWESTERN_BLOT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007575"

    # bacterial one-hybrid evidence used in automatic assertion
    ECO_0007576 = "ECO_0007576"
    BACTERIAL_ONE_HYBRID_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007576"

    # protein-oligonucleotide microarray binding evidence used in automatic assertion
    ECO_0007577 = "ECO_0007577"
    PROTEIN_OLIGONUCLEOTIDE_MICROARRAY_BINDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007577"
    )

    # functional complementation evidence used in automatic assertion
    ECO_0007578 = "ECO_0007578"
    FUNCTIONAL_COMPLEMENTATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007578"

    # transgenic rescue experiment evidence used in automatic assertion
    ECO_0007579 = "ECO_0007579"
    TRANSGENIC_RESCUE_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007579"

    # transient rescue experiment evidence used in automatic assertion
    ECO_0007580 = "ECO_0007580"
    TRANSIENT_RESCUE_EXPERIMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007580"

    # suppressor/enhancer interaction phenotypic evidence used in automatic assertion
    ECO_0007581 = "ECO_0007581"
    SUPPRESSOR_ENHANCER_INTERACTION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007581"
    )

    # double mutant phenotypic evidence used in automatic assertion
    ECO_0007582 = "ECO_0007582"
    DOUBLE_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007582"

    # epistatic interaction phenotypic evidence used in automatic assertion
    ECO_0007583 = "ECO_0007583"
    EPISTATIC_INTERACTION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007583"
    )

    # functional complementation in heterologous system evidence used in automatic assertion
    ECO_0007584 = "ECO_0007584"
    FUNCTIONAL_COMPLEMENTATION_IN_HETEROLOGOUS_SYSTEM_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007584"
    )

    # temperature-sensitive mutant phenotypic evidence used in automatic assertion
    ECO_0007585 = "ECO_0007585"
    TEMPERATURE_SENSITIVE_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007585"
    )

    # recessive mutant phenotype evidence used in automatic assertion
    ECO_0007586 = "ECO_0007586"
    RECESSIVE_MUTANT_PHENOTYPE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007586"

    # high throughput mutant phenotypic evidence used in automatic assertion
    ECO_0007587 = "ECO_0007587"
    HIGH_THROUGHPUT_MUTANT_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007587"
    )

    # high throughput genetic interaction phenotypic evidence used in automatic assertion
    ECO_0007588 = "ECO_0007588"
    HIGH_THROUGHPUT_GENETIC_INTERACTION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007588"
    )

    # high throughput direct assay evidence used in automatic assertion
    ECO_0007589 = "ECO_0007589"
    HIGH_THROUGHPUT_DIRECT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007589"

    # high throughput expression pattern evidence used in automatic assertion
    ECO_0007590 = "ECO_0007590"
    HIGH_THROUGHPUT_EXPRESSION_PATTERN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007590"
    )

    # radioligand binding assay evidence used in automatic assertion
    ECO_0007591 = "ECO_0007591"
    RADIOLIGAND_BINDING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007591"

    # combinatorial experimental and author inference evidence used in automatic assertion
    ECO_0007592 = "ECO_0007592"
    COMBINATORIAL_EXPERIMENTAL_AND_AUTHOR_INFERENCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007592"
    )

    # combinatorial experimental and curator inference evidence used in automatic assertion
    ECO_0007593 = "ECO_0007593"
    COMBINATORIAL_EXPERIMENTAL_AND_CURATOR_INFERENCE_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007593"
    )

    # voltammetry evidence used in automatic assertion
    ECO_0007594 = "ECO_0007594"
    VOLTAMMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007594"

    # photoconversion evidence used in automatic assertion
    ECO_0007595 = "ECO_0007595"
    PHOTOCONVERSION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007595"

    # agglutination test evidence used in automatic assertion
    ECO_0007596 = "ECO_0007596"
    AGGLUTINATION_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007596"

    # slide agglutination test evidence used in automatic assertion
    ECO_0007597 = "ECO_0007597"
    SLIDE_AGGLUTINATION_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007597"

    # direct Coombs test evidence used in automatic assertion
    ECO_0007598 = "ECO_0007598"
    DIRECT_COOMBS_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007598"

    # indirect Coombs test evidence used in automatic assertion
    ECO_0007599 = "ECO_0007599"
    INDIRECT_COOMBS_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007599"

    # direct hemagglutination assay evidence used in automatic assertion
    ECO_0007600 = "ECO_0007600"
    DIRECT_HEMAGGLUTINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007600"

    # viral hemagglutination inhibition assay evidence used in automatic assertion
    ECO_0007601 = "ECO_0007601"
    VIRAL_HEMAGGLUTINATION_INHIBITION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007601"
    )

    # compement fixation assay evidence used in automatic assertion
    ECO_0007602 = "ECO_0007602"
    COMPEMENT_FIXATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007602"

    # neutralization test assay evidence used in automatic assertion
    ECO_0007603 = "ECO_0007603"
    NEUTRALIZATION_TEST_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007603"

    # copper transport assay evidence used in automatic assertion
    ECO_0007604 = "ECO_0007604"
    COPPER_TRANSPORT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007604"

    # 5-cyano-2,3-ditolyl tetrazolium chloride staining evidence used in automatic assertion
    ECO_0007605 = "ECO_0007605"
    _5_CYANO_2_3_DITOLYL_TETRAZOLIUM_CHLORIDE_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007605"
    )

    # plaque assay evidence used in automatic assertion
    ECO_0007606 = "ECO_0007606"
    PLAQUE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007606"

    # epifluorescence microscopy evidence used in automatic assertion
    ECO_0007607 = "ECO_0007607"
    EPIFLUORESCENCE_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007607"

    # transmission electron microscopy evidence used in automatic assertion
    ECO_0007608 = "ECO_0007608"
    TRANSMISSION_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007608"
    )

    # scanning electron microscopy evidence used in automatic assertion
    ECO_0007609 = "ECO_0007609"
    SCANNING_ELECTRON_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007609"

    # time-lapsed microscopy evidence used in automatic assertion
    ECO_0007610 = "ECO_0007610"
    TIME_LAPSED_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007610"

    # phase contrast microscopy evidence used in automatic assertion
    ECO_0007611 = "ECO_0007611"
    PHASE_CONTRAST_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007611"

    # transmitted light brightfied mircoscopy evidence used in automatic assertion
    ECO_0007612 = "ECO_0007612"
    TRANSMITTED_LIGHT_BRIGHTFIED_MIRCOSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007612"
    )

    # koehler illumination microscopy evidence used in automatic assertion
    ECO_0007613 = "ECO_0007613"
    KOEHLER_ILLUMINATION_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007613"

    # differential interference contrast microscopy evidence used in automatic assertion
    ECO_0007614 = "ECO_0007614"
    DIFFERENTIAL_INTERFERENCE_CONTRAST_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007614"
    )

    # extended field laser confocal microscopy evidence used in automatic assertion
    ECO_0007615 = "ECO_0007615"
    EXTENDED_FIELD_LASER_CONFOCAL_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007615"
    )

    # confocal laser scanning microscopy evidence used in automatic assertion
    ECO_0007616 = "ECO_0007616"
    CONFOCAL_LASER_SCANNING_MICROSCOPY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007616"
    )

    # light scattering evidence used in automatic assertion
    ECO_0007617 = "ECO_0007617"
    LIGHT_SCATTERING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007617"

    # dynamic light scattering assay evidence used in automatic assertion
    ECO_0007618 = "ECO_0007618"
    DYNAMIC_LIGHT_SCATTERING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007618"

    # static light scattering assay evidence used in automatic assertion
    ECO_0007619 = "ECO_0007619"
    STATIC_LIGHT_SCATTERING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007619"

    # colony papillation assay phenotypic evidence used in automatic assertion
    ECO_0007620 = "ECO_0007620"
    COLONY_PAPILLATION_ASSAY_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007620"
    )

    # crystal violet staining evidence used in automatic assertion
    ECO_0007621 = "ECO_0007621"
    CRYSTAL_VIOLET_STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007621"

    # flow cell biofilm assay evidence used in automatic assertion
    ECO_0007622 = "ECO_0007622"
    FLOW_CELL_BIOFILM_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007622"

    # bacterial 2-hybrid assay evidence used in automatic assertion
    ECO_0007623 = "ECO_0007623"
    BACTERIAL_2_HYBRID_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007623"

    # phenomic profiling assay evidence used in automatic assertion
    ECO_0007624 = "ECO_0007624"
    PHENOMIC_PROFILING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007624"

    # colony morphology phenotypic evidence used in automatic assertion
    ECO_0007625 = "ECO_0007625"
    COLONY_MORPHOLOGY_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007625"

    # colony color phenotypic evidence used in automatic assertion
    ECO_0007626 = "ECO_0007626"
    COLONY_COLOR_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007626"

    # colony size phenotypic evidence used in automatic assertion
    ECO_0007627 = "ECO_0007627"
    COLONY_SIZE_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007627"

    # zone of inhibition evidence used in automatic assertion
    ECO_0007628 = "ECO_0007628"
    ZONE_OF_INHIBITION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007628"

    # Etest evidence used in automatic assertion
    ECO_0007629 = "ECO_0007629"
    ETEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007629"

    # ribosome profiling evidence used in automatic assertion
    ECO_0007630 = "ECO_0007630"
    RIBOSOME_PROFILING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007630"

    # computational inference used in manual assertion
    ECO_0007631 = "ECO_0007631"
    COMPUTATIONAL_INFERENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007631"

    # transcriptional activation assay evidence used in manual assertion
    ECO_0007632 = "ECO_0007632"
    TRANSCRIPTIONAL_ACTIVATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007632"

    # transcriptional activation assay evidence used in automatic assertion
    ECO_0007633 = "ECO_0007633"
    TRANSCRIPTIONAL_ACTIVATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007633"
    )

    # experimental phenotypic evidence used in manual assertion
    ECO_0007634 = "ECO_0007634"
    EXPERIMENTAL_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007634"

    # experimental phenotypic evidence used in automatic assertion
    ECO_0007635 = "ECO_0007635"
    EXPERIMENTAL_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007635"

    # curator inference from database
    ECO_0007636 = "ECO_0007636"
    CURATOR_INFERENCE_FROM_DATABASE = "ECO_0007636"

    # curator inference from encyclopedia
    ECO_0007637 = "ECO_0007637"
    CURATOR_INFERENCE_FROM_ENCYCLOPEDIA = "ECO_0007637"

    # curator inference from Wikipedia
    ECO_0007638 = "ECO_0007638"
    CURATOR_INFERENCE_FROM_WIKIPEDIA = "ECO_0007638"

    # curator inference from Britannica
    ECO_0007639 = "ECO_0007639"
    CURATOR_INFERENCE_FROM_BRITANNICA = "ECO_0007639"

    # curator inference from MedlinePlus encyclopedia
    ECO_0007640 = "ECO_0007640"
    CURATOR_INFERENCE_FROM_MEDLINEPLUS_ENCYCLOPEDIA = "ECO_0007640"

    # curator inference from dictionary
    ECO_0007641 = "ECO_0007641"
    CURATOR_INFERENCE_FROM_DICTIONARY = "ECO_0007641"

    # curator inference from Oxford Dictionary
    ECO_0007642 = "ECO_0007642"
    CURATOR_INFERENCE_FROM_OXFORD_DICTIONARY = "ECO_0007642"

    # curator inference from Merriam-Webster Dictionary
    ECO_0007643 = "ECO_0007643"
    CURATOR_INFERENCE_FROM_MERRIAM_WEBSTER_DICTIONARY = "ECO_0007643"

    # curator inference from MedlinePlus dictionary
    ECO_0007644 = "ECO_0007644"
    CURATOR_INFERENCE_FROM_MEDLINEPLUS_DICTIONARY = "ECO_0007644"

    # curator inference from journal publication
    ECO_0007645 = "ECO_0007645"
    CURATOR_INFERENCE_FROM_JOURNAL_PUBLICATION = "ECO_0007645"

    # curator inference from book
    ECO_0007646 = "ECO_0007646"
    CURATOR_INFERENCE_FROM_BOOK = "ECO_0007646"

    # curator inference from authoritative source
    ECO_0007647 = "ECO_0007647"
    CURATOR_INFERENCE_FROM_AUTHORITATIVE_SOURCE = "ECO_0007647"

    # manually integrated combinatorial computational evidence
    ECO_0007648 = "ECO_0007648"
    MANUALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_EVIDENCE = "ECO_0007648"

    # manually integrated combinatorial computational evidence used in manual assertion
    ECO_0007649 = "ECO_0007649"
    MANUALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007649"
    )

    # manually integrated combinatorial computational evidence used in automatic assertion
    ECO_0007650 = "ECO_0007650"
    MANUALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007650"
    )

    # automatically integrated combinatorial computational evidence
    ECO_0007651 = "ECO_0007651"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_EVIDENCE = "ECO_0007651"

    # automatically integrated combinatorial computational evidence used in manual assertion
    ECO_0007652 = "ECO_0007652"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007652"
    )

    # automatically integrated combinatorial computational evidence used in automatic assertion
    ECO_0007653 = "ECO_0007653"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007653"
    )

    # combinatorial experimental evidence
    ECO_0007654 = "ECO_0007654"
    COMBINATORIAL_EXPERIMENTAL_EVIDENCE = "ECO_0007654"

    # manually integrated combinatorial experimental evidence
    ECO_0007655 = "ECO_0007655"
    MANUALLY_INTEGRATED_COMBINATORIAL_EXPERIMENTAL_EVIDENCE = "ECO_0007655"

    # manually integrated combinatorial experimental evidence used in manual assertion
    ECO_0007656 = "ECO_0007656"
    MANUALLY_INTEGRATED_COMBINATORIAL_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007656"
    )

    # manually integrated combinatorial experimental evidence used in automatic assertion
    ECO_0007657 = "ECO_0007657"
    MANUALLY_INTEGRATED_COMBINATORIAL_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007657"
    )

    # automatically integrated combinatorial experimental evidence
    ECO_0007658 = "ECO_0007658"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_EXPERIMENTAL_EVIDENCE = "ECO_0007658"

    # automatically integrated combinatorial experimental evidence used in manual assertion
    ECO_0007659 = "ECO_0007659"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007659"
    )

    # automatically integrated combinatorial experimental evidence used in automatic assertion
    ECO_0007660 = "ECO_0007660"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007660"
    )

    # combinatorial computational and experimental evidence
    ECO_0007661 = "ECO_0007661"
    COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE = "ECO_0007661"

    # manually integrated combinatorial computational and experimental evidence
    ECO_0007662 = "ECO_0007662"
    MANUALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE = (
        "ECO_0007662"
    )

    # manually integrated combinatorial computational and experimental evidence used in manual assertion
    ECO_0007663 = "ECO_0007663"
    MANUALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007663"
    )

    # manually integrated combinatorial computational and experimental evidence used in automatic assertion
    ECO_0007664 = "ECO_0007664"
    MANUALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007664"
    )

    # automatically integrated combinatorial computational and experimental evidence
    ECO_0007665 = "ECO_0007665"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE = (
        "ECO_0007665"
    )

    # automatically integrated combinatorial computational and experimental evidence used in manual assertion
    ECO_0007666 = "ECO_0007666"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007666"
    )

    # automatically integrated combinatorial computational and experimental evidence used in automatic assertion
    ECO_0007667 = "ECO_0007667"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007667"
    )

    # computational evidence used in manual assertion
    ECO_0007668 = "ECO_0007668"
    COMPUTATIONAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007668"

    # computational evidence used in automatic assertion
    ECO_0007669 = "ECO_0007669"
    COMPUTATIONAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007669"

    # computational evidence
    ECO_0007672 = "ECO_0007672"
    COMPUTATIONAL_EVIDENCE = "ECO_0007672"

    # automatically integrated combinatorial evidence
    ECO_0007673 = "ECO_0007673"
    AUTOMATICALLY_INTEGRATED_COMBINATORIAL_EVIDENCE = "ECO_0007673"

    # manually integrated combinatorial evidence
    ECO_0007674 = "ECO_0007674"
    MANUALLY_INTEGRATED_COMBINATORIAL_EVIDENCE = "ECO_0007674"

    # manually integrated combinatorial evidence used in manual assertion
    ECO_0007675 = "ECO_0007675"
    MANUALLY_INTEGRATED_COMBINATORIAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007675"

    # manually integrated combinatorial evidence used in automatic assertion
    ECO_0007676 = "ECO_0007676"
    MANUALLY_INTEGRATED_COMBINATORIAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007676"
    )

    # combinatorial computational evidence
    ECO_0007677 = "ECO_0007677"
    COMBINATORIAL_COMPUTATIONAL_EVIDENCE = "ECO_0007677"

    # combinatorial computational evidence used in manual assertion
    ECO_0007678 = "ECO_0007678"
    COMBINATORIAL_COMPUTATIONAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007678"

    # combinatorial computational evidence used in automatic assertion
    ECO_0007679 = "ECO_0007679"
    COMBINATORIAL_COMPUTATIONAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007679"

    # chromatography evidence used in manual assertion
    ECO_0007680 = "ECO_0007680"
    CHROMATOGRAPHY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007680"

    # chromatography evidence used in automatic assertion
    ECO_0007681 = "ECO_0007681"
    CHROMATOGRAPHY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007681"

    # reporter gene assay evidence used in manual assertion
    ECO_0007682 = "ECO_0007682"
    REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007682"

    # protein separation evidence used in manual assertion
    ECO_0007684 = "ECO_0007684"
    PROTEIN_SEPARATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007684"

    # substance quantification evidence used in manual assertion
    ECO_0007685 = "ECO_0007685"
    SUBSTANCE_QUANTIFICATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007685"

    # voltage clamp recording evidence used in manual assertion
    ECO_0007686 = "ECO_0007686"
    VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007686"

    # protein kinase assay evidence used in manual assertion
    ECO_0007687 = "ECO_0007687"
    PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007687"

    # gel electrophoresis evidence used in manual assertion
    ECO_0007688 = "ECO_0007688"
    GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007688"

    # sodium dodecyl sulfate polyacrylamide gel electrophoresis evidence used in manual assertion
    ECO_0007689 = "ECO_0007689"
    SODIUM_DODECYL_SULFATE_POLYACRYLAMIDE_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007689"
    )

    # ex vivo assay evidence used in manual assertion
    ECO_0007690 = "ECO_0007690"
    EX_VIVO_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007690"

    # cleavage assay evidence used in manual assertion
    ECO_0007691 = "ECO_0007691"
    CLEAVAGE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007691"

    # deacetylation assay evidence used in manual assertion
    ECO_0007692 = "ECO_0007692"
    DEACETYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007692"

    # transcription assay evidence used in manual assertion
    ECO_0007693 = "ECO_0007693"
    TRANSCRIPTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007693"

    # phosphatase assay evidence used in manual assertion
    ECO_0007694 = "ECO_0007694"
    PHOSPHATASE_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007694"

    # cell-based assay evidence used in manual assertion
    ECO_0007695 = "ECO_0007695"
    CELL_BASED_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007695"

    # cell proliferation assay evidence used in manual assertion
    ECO_0007696 = "ECO_0007696"
    CELL_PROLIFERATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007696"

    # DNA synthesis cell proliferation assay evidence used in manual assertion
    ECO_0007697 = "ECO_0007697"
    DNA_SYNTHESIS_CELL_PROLIFERATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007697"
    )

    # apoptotic assay evidence used in manual assertion
    ECO_0007698 = "ECO_0007698"
    APOPTOTIC_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007698"

    # cell growth assay evidence used in manual assertion
    ECO_0007699 = "ECO_0007699"
    CELL_GROWTH_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007699"

    # disk diffusion test evidence used in manual assertion
    ECO_0007700 = "ECO_0007700"
    DISK_DIFFUSION_TEST_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007700"

    # chemotaxis assay evidence used in manual assertion
    ECO_0007701 = "ECO_0007701"
    CHEMOTAXIS_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007701"

    # cytotoxicity assay evidence used in manual assertion
    ECO_0007702 = "ECO_0007702"
    CYTOTOXICITY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007702"

    # cell viability assay evidence used in manual assertion
    ECO_0007703 = "ECO_0007703"
    CELL_VIABILITY_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007703"

    # methylation assay evidence used in manual assertion
    ECO_0007704 = "ECO_0007704"
    METHYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007704"

    # protein assay evidence used in manual assertion
    ECO_0007705 = "ECO_0007705"
    PROTEIN_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007705"

    # chromatin immunoprecipitation evidence used in manual assertion
    ECO_0007706 = "ECO_0007706"
    CHROMATIN_IMMUNOPRECIPITATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007706"

    # protein inhibition evidence used in manual assertion
    ECO_0007707 = "ECO_0007707"
    PROTEIN_INHIBITION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007707"

    # sumoylation assay evidence used in manual assertion
    ECO_0007708 = "ECO_0007708"
    SUMOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007708"

    # transport assay evidence used in manual assertion
    ECO_0007709 = "ECO_0007709"
    TRANSPORT_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007709"

    # defarnesylation assay evidence used in manual assertion
    ECO_0007710 = "ECO_0007710"
    DEFARNESYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007710"

    # deubiquitination assay evidence used in manual assertion
    ECO_0007711 = "ECO_0007711"
    DEUBIQUITINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007711"

    # palmitoylation assay evidence used in manual assertion
    ECO_0007712 = "ECO_0007712"
    PALMITOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007712"

    # acetylation assay evidence used in manual assertion
    ECO_0007713 = "ECO_0007713"
    ACETYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007713"

    # demethylation assay evidence used in manual assertion
    ECO_0007714 = "ECO_0007714"
    DEMETHYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007714"

    # polyADP-ribosylation assay evidence used in manual assertion
    ECO_0007715 = "ECO_0007715"
    POLYADP_RIBOSYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007715"

    # staining evidence used in manual assertion
    ECO_0007716 = "ECO_0007716"
    STAINING_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007716"

    # translation assay evidence used in manual assertion
    ECO_0007717 = "ECO_0007717"
    TRANSLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007717"

    # ubiquitination assay evidence used in manual assertion
    ECO_0007718 = "ECO_0007718"
    UBIQUITINATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007718"

    # immunodetection assay evidence used in manual assertion
    ECO_0007719 = "ECO_0007719"
    IMMUNODETECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007719"

    # desumoylation assay evidence used in manual assertion
    ECO_0007720 = "ECO_0007720"
    DESUMOYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007720"

    # farnesylation assay evidence used in manual assertion
    ECO_0007721 = "ECO_0007721"
    FARNESYLATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007721"

    # reconstitution assay evidence used in manual assertion
    ECO_0007722 = "ECO_0007722"
    RECONSTITUTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007722"

    # in vitro transcription reconstitution assay evidence used in manual assertion
    ECO_0007723 = "ECO_0007723"
    IN_VITRO_TRANSCRIPTION_RECONSTITUTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007723"
    )

    # localization evidence used in manual assertion
    ECO_0007724 = "ECO_0007724"
    LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007724"

    # protein localization evidence used in manual assertion
    ECO_0007725 = "ECO_0007725"
    PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007725"

    # fusion protein localization evidence used in manual assertion
    ECO_0007726 = "ECO_0007726"
    FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007726"

    # nucleic acid localization evidence used in manual assertion
    ECO_0007727 = "ECO_0007727"
    NUCLEIC_ACID_LOCALIZATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007727"

    # anatomical perturbation phenotypic evidence used in manual assertion
    ECO_0007728 = "ECO_0007728"
    ANATOMICAL_PERTURBATION_PHENOTYPIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007728"

    # cleavage arrested development evidence used in manual assertion
    ECO_0007730 = "ECO_0007730"
    CLEAVAGE_ARRESTED_DEVELOPMENT_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007730"

    # spectrometry evidence used in manual assertion
    ECO_0007731 = "ECO_0007731"
    SPECTROMETRY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007731"

    # sequencing assay evidence used in manual assertion
    ECO_0007732 = "ECO_0007732"
    SEQUENCING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007732"

    # nucleotide sequencing assay evidence used in manual assertion
    ECO_0007733 = "ECO_0007733"
    NUCLEOTIDE_SEQUENCING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007733"

    # high throughput nucleotide sequencing assay evidence used in manual assertion
    ECO_0007734 = "ECO_0007734"
    HIGH_THROUGHPUT_NUCLEOTIDE_SEQUENCING_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007734"
    )

    # structure determination evidence used in manual assertion
    ECO_0007735 = "ECO_0007735"
    STRUCTURE_DETERMINATION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007735"

    # molecule detection assay evidence used in manual assertion
    ECO_0007736 = "ECO_0007736"
    MOLECULE_DETECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007736"

    # DNA detection assay evidence used in manual assertion
    ECO_0007737 = "ECO_0007737"
    DNA_DETECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007737"

    # protein detection assay evidence used in manual assertion
    ECO_0007738 = "ECO_0007738"
    PROTEIN_DETECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007738"

    # RNA detection assay evidence used in manual assertion
    ECO_0007739 = "ECO_0007739"
    RNA_DETECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007739"

    # small molecule detection assay evidence used in manual assertion
    ECO_0007740 = "ECO_0007740"
    SMALL_MOLECULE_DETECTION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007740"

    # chromosome conformation-based evidence used in manual assertion
    ECO_0007741 = "ECO_0007741"
    CHROMOSOME_CONFORMATION_BASED_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007741"

    # 3C evidence used in manual assertion
    ECO_0007742 = "ECO_0007742"
    _3C_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007742"

    # combinatorial computational and experimental evidence used in manual assertion
    ECO_0007744 = "ECO_0007744"
    COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007744"
    )

    # combinatorial experimental evidence used in manual assertion
    ECO_0007745 = "ECO_0007745"
    COMBINATORIAL_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007745"

    # biological system reconstruction evidence used in manual assertion
    ECO_0007746 = "ECO_0007746"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007746"

    # biological system reconstruction evidence by experimental evidence used in manual assertion
    ECO_0007747 = "ECO_0007747"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007747"
    )

    # phenotypic similarity evidence used in manual assertion
    ECO_0007748 = "ECO_0007748"
    PHENOTYPIC_SIMILARITY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007748"

    # transcript splice pattern evidence used in manual assertion
    ECO_0007749 = "ECO_0007749"
    TRANSCRIPT_SPLICE_PATTERN_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007749"

    # phylogenetic evidence used in manual assertion
    ECO_0007750 = "ECO_0007750"
    PHYLOGENETIC_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007750"

    # inferential evidence used in manual assertion
    ECO_0007751 = "ECO_0007751"
    INFERENTIAL_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007751"

    # curator inference from authoritative source used in manual assertion
    ECO_0007752 = "ECO_0007752"
    CURATOR_INFERENCE_FROM_AUTHORITATIVE_SOURCE_USED_IN_MANUAL_ASSERTION = "ECO_0007752"

    # curator inference from encyclopedia used in manual assertion
    ECO_0007753 = "ECO_0007753"
    CURATOR_INFERENCE_FROM_ENCYCLOPEDIA_USED_IN_MANUAL_ASSERTION = "ECO_0007753"

    # curator inference from Wikipedia used in manual assertion
    ECO_0007754 = "ECO_0007754"
    CURATOR_INFERENCE_FROM_WIKIPEDIA_USED_IN_MANUAL_ASSERTION = "ECO_0007754"

    # curator inference from MedlinePlus encyclopedia used in manual assertion
    ECO_0007755 = "ECO_0007755"
    CURATOR_INFERENCE_FROM_MEDLINEPLUS_ENCYCLOPEDIA_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007755"
    )

    # curator inference from Britannica used in manual assertion
    ECO_0007756 = "ECO_0007756"
    CURATOR_INFERENCE_FROM_BRITANNICA_USED_IN_MANUAL_ASSERTION = "ECO_0007756"

    # curator inference from book used in manual assertion
    ECO_0007757 = "ECO_0007757"
    CURATOR_INFERENCE_FROM_BOOK_USED_IN_MANUAL_ASSERTION = "ECO_0007757"

    # curator inference from journal publication used in manual assertion
    ECO_0007758 = "ECO_0007758"
    CURATOR_INFERENCE_FROM_JOURNAL_PUBLICATION_USED_IN_MANUAL_ASSERTION = "ECO_0007758"

    # curator inference from database used in manual assertion
    ECO_0007759 = "ECO_0007759"
    CURATOR_INFERENCE_FROM_DATABASE_USED_IN_MANUAL_ASSERTION = "ECO_0007759"

    # curator inference from dictionary used in manual assertion
    ECO_0007760 = "ECO_0007760"
    CURATOR_INFERENCE_FROM_DICTIONARY_USED_IN_MANUAL_ASSERTION = "ECO_0007760"

    # curator inference from MedlinePlus dictionary used in manual assertion
    ECO_0007761 = "ECO_0007761"
    CURATOR_INFERENCE_FROM_MEDLINEPLUS_DICTIONARY_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007761"
    )

    # curator inference from Oxford Dictionary used in manual assertion
    ECO_0007762 = "ECO_0007762"
    CURATOR_INFERENCE_FROM_OXFORD_DICTIONARY_USED_IN_MANUAL_ASSERTION = "ECO_0007762"

    # curator inference from Merriam-Webster Dictionary used in manual assertion
    ECO_0007763 = "ECO_0007763"
    CURATOR_INFERENCE_FROM_MERRIAM_WEBSTER_DICTIONARY_USED_IN_MANUAL_ASSERTION = (
        "ECO_0007763"
    )

    # reporter gene assay evidence used in automatic assertion
    ECO_0007765 = "ECO_0007765"
    REPORTER_GENE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007765"

    # voltage clamp recording evidence used in automatic assertion
    ECO_0007766 = "ECO_0007766"
    VOLTAGE_CLAMP_RECORDING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007766"

    # protein kinase assay evidence used in automatic assertion
    ECO_0007767 = "ECO_0007767"
    PROTEIN_KINASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007767"

    # transcription assay evidence used in automatic assertion
    ECO_0007768 = "ECO_0007768"
    TRANSCRIPTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007768"

    # gel electrophoresis evidence used in automatic assertion
    ECO_0007769 = "ECO_0007769"
    GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007769"

    # sodium dodecyl sulfate polyacrylamide gel electrophoresis evidence used in automatic assertion
    ECO_0007770 = "ECO_0007770"
    SODIUM_DODECYL_SULFATE_POLYACRYLAMIDE_GEL_ELECTROPHORESIS_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007770"
    )

    # deacetylation assay evidence used in automatic assertion
    ECO_0007771 = "ECO_0007771"
    DEACETYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007771"

    # phosphatase assay evidence used in automatic assertion
    ECO_0007772 = "ECO_0007772"
    PHOSPHATASE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007772"

    # cell-based assay evidence used in automatic assertion
    ECO_0007773 = "ECO_0007773"
    CELL_BASED_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007773"

    # cell viability assay evidence used in automatic assertion
    ECO_0007774 = "ECO_0007774"
    CELL_VIABILITY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007774"

    # cell proliferation assay evidence used in automatic assertion
    ECO_0007775 = "ECO_0007775"
    CELL_PROLIFERATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007775"

    # DNA synthesis cell proliferation assay evidence used in automatic assertion
    ECO_0007776 = "ECO_0007776"
    DNA_SYNTHESIS_CELL_PROLIFERATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007776"
    )

    # apoptotic assay evidence used in automatic assertion
    ECO_0007777 = "ECO_0007777"
    APOPTOTIC_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007777"

    # cell growth assay evidence used in automatic assertion
    ECO_0007778 = "ECO_0007778"
    CELL_GROWTH_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007778"

    # disk diffusion test evidence used in automatic assertion
    ECO_0007779 = "ECO_0007779"
    DISK_DIFFUSION_TEST_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007779"

    # chemotaxis assay evidence used in automatic assertion
    ECO_0007780 = "ECO_0007780"
    CHEMOTAXIS_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007780"

    # cytotoxicity assay evidence used in automatic assertion
    ECO_0007781 = "ECO_0007781"
    CYTOTOXICITY_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007781"

    # cleavage assay evidence used in automatic assertion
    ECO_0007782 = "ECO_0007782"
    CLEAVAGE_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007782"

    # methylation assay evidence used in automatic assertion
    ECO_0007783 = "ECO_0007783"
    METHYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007783"

    # protein assay evidence used in automatic assertion
    ECO_0007784 = "ECO_0007784"
    PROTEIN_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007784"

    # protein inhibition evidence used in automatic assertion
    ECO_0007785 = "ECO_0007785"
    PROTEIN_INHIBITION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007785"

    # chromatin immunoprecipitation evidence used in automatic assertion
    ECO_0007786 = "ECO_0007786"
    CHROMATIN_IMMUNOPRECIPITATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007786"

    # protein separation evidence used in automatic assertion
    ECO_0007787 = "ECO_0007787"
    PROTEIN_SEPARATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007787"

    # sumoylation assay evidence used in automatic assertion
    ECO_0007788 = "ECO_0007788"
    SUMOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007788"

    # transport assay evidence used in automatic assertion
    ECO_0007789 = "ECO_0007789"
    TRANSPORT_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007789"

    # defarnesylation assay evidence used in automatic assertion
    ECO_0007790 = "ECO_0007790"
    DEFARNESYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007790"

    # deubiquitination assay evidence used in automatic assertion
    ECO_0007791 = "ECO_0007791"
    DEUBIQUITINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007791"

    # palmitoylation assay evidence used in automatic assertion
    ECO_0007792 = "ECO_0007792"
    PALMITOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007792"

    # ex vivo assay evidence used in automatic assertion
    ECO_0007793 = "ECO_0007793"
    EX_VIVO_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007793"

    # acetylation assay evidence used in automatic assertion
    ECO_0007794 = "ECO_0007794"
    ACETYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007794"

    # demethylation assay evidence used in automatic assertion
    ECO_0007795 = "ECO_0007795"
    DEMETHYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007795"

    # immunodetection assay evidence used in automatic assertion
    ECO_0007796 = "ECO_0007796"
    IMMUNODETECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007796"

    # polyADP-ribosylation assay evidence used in automatic assertion
    ECO_0007797 = "ECO_0007797"
    POLYADP_RIBOSYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007797"

    # staining evidence used in automatic assertion
    ECO_0007798 = "ECO_0007798"
    STAINING_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007798"

    # translation assay evidence used in automatic assertion
    ECO_0007799 = "ECO_0007799"
    TRANSLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007799"

    # farnesylation assay evidence used in automatic assertion
    ECO_0007800 = "ECO_0007800"
    FARNESYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007800"

    # ubiquitination assay evidence used in automatic assertion
    ECO_0007801 = "ECO_0007801"
    UBIQUITINATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007801"

    # desumoylation assay evidence used in automatic assertion
    ECO_0007802 = "ECO_0007802"
    DESUMOYLATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007802"

    # reconstitution assay evidence used in automatic assertion
    ECO_0007803 = "ECO_0007803"
    RECONSTITUTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007803"

    # in vitro transcription reconstitution assay evidence used in automatic assertion
    ECO_0007804 = "ECO_0007804"
    IN_VITRO_TRANSCRIPTION_RECONSTITUTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007804"
    )

    # substance quantification evidence used in automatic assertion
    ECO_0007805 = "ECO_0007805"
    SUBSTANCE_QUANTIFICATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007805"

    # localization evidence used in automatic assertion
    ECO_0007806 = "ECO_0007806"
    LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007806"

    # protein localization evidence used in automatic assertion
    ECO_0007807 = "ECO_0007807"
    PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007807"

    # fusion protein localization evidence used in automatic assertion
    ECO_0007808 = "ECO_0007808"
    FUSION_PROTEIN_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007808"

    # nucleic acid localization evidence used in automatic assertion
    ECO_0007809 = "ECO_0007809"
    NUCLEIC_ACID_LOCALIZATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007809"

    # anatomical perturbation phenotypic evidence used in automatic assertion
    ECO_0007810 = "ECO_0007810"
    ANATOMICAL_PERTURBATION_PHENOTYPIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007810"
    )

    # cleavage arrested development evidence used in automatic assertion
    ECO_0007811 = "ECO_0007811"
    CLEAVAGE_ARRESTED_DEVELOPMENT_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007811"

    # sequencing assay evidence used in automatic assertion
    ECO_0007812 = "ECO_0007812"
    SEQUENCING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007812"

    # nucleotide sequencing assay evidence used in automatic assertion
    ECO_0007813 = "ECO_0007813"
    NUCLEOTIDE_SEQUENCING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007813"

    # high throughput nucleotide sequencing assay evidence used in automatic assertion
    ECO_0007814 = "ECO_0007814"
    HIGH_THROUGHPUT_NUCLEOTIDE_SEQUENCING_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007814"
    )

    # structure determination evidence used in automatic assertion
    ECO_0007815 = "ECO_0007815"
    STRUCTURE_DETERMINATION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007815"

    # molecule detection assay evidence used in automatic assertion
    ECO_0007816 = "ECO_0007816"
    MOLECULE_DETECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007816"

    # DNA detection assay evidence used in automatic assertion
    ECO_0007817 = "ECO_0007817"
    DNA_DETECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007817"

    # RNA detection assay evidence used in automatic assertion
    ECO_0007818 = "ECO_0007818"
    RNA_DETECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007818"

    # protein detection assay evidence used in automatic assertion
    ECO_0007819 = "ECO_0007819"
    PROTEIN_DETECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007819"

    # small molecule detection assay evidence used in automatic assertion
    ECO_0007820 = "ECO_0007820"
    SMALL_MOLECULE_DETECTION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007820"

    # spectrometry evidence used in automatic assertion
    ECO_0007821 = "ECO_0007821"
    SPECTROMETRY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007821"

    # chromosome conformation-based evidence used in automatic assertion
    ECO_0007822 = "ECO_0007822"
    CHROMOSOME_CONFORMATION_BASED_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007822"

    # 3C evidence used in automatic assertion
    ECO_0007823 = "ECO_0007823"
    _3C_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007823"

    # phenotypic similarity evidence used in automatic assertion
    ECO_0007824 = "ECO_0007824"
    PHENOTYPIC_SIMILARITY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007824"

    # transcript splice pattern evidence used in automatic assertion
    ECO_0007825 = "ECO_0007825"
    TRANSCRIPT_SPLICE_PATTERN_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007825"

    # phylogenetic evidence used in automatic assertion
    ECO_0007826 = "ECO_0007826"
    PHYLOGENETIC_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007826"

    # biological system reconstruction evidence used in automatic assertion
    ECO_0007827 = "ECO_0007827"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007827"
    )

    # biological system reconstruction evidence by experimental evidence used in automatic assertion
    ECO_0007828 = "ECO_0007828"
    BIOLOGICAL_SYSTEM_RECONSTRUCTION_EVIDENCE_BY_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007828"
    )

    # combinatorial computational and experimental evidence used in automatic assertion
    ECO_0007829 = "ECO_0007829"
    COMBINATORIAL_COMPUTATIONAL_AND_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007829"
    )

    # combinatorial experimental evidence used in automatic assertion
    ECO_0007830 = "ECO_0007830"
    COMBINATORIAL_EXPERIMENTAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007830"

    # inferential evidence used in automatic assertion
    ECO_0007832 = "ECO_0007832"
    INFERENTIAL_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007832"

    # curator inference from authoritative source used in automatic assertion
    ECO_0007833 = "ECO_0007833"
    CURATOR_INFERENCE_FROM_AUTHORITATIVE_SOURCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007833"
    )

    # curator inference from encyclopedia used in automatic assertion
    ECO_0007834 = "ECO_0007834"
    CURATOR_INFERENCE_FROM_ENCYCLOPEDIA_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007834"

    # curator inference from Wikipedia used in automatic assertion
    ECO_0007835 = "ECO_0007835"
    CURATOR_INFERENCE_FROM_WIKIPEDIA_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007835"

    # curator inference from Britannica used in automatic assertion
    ECO_0007836 = "ECO_0007836"
    CURATOR_INFERENCE_FROM_BRITANNICA_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007836"

    # curator inference from MedlinePlus encyclopedia used in automatic assertion
    ECO_0007837 = "ECO_0007837"
    CURATOR_INFERENCE_FROM_MEDLINEPLUS_ENCYCLOPEDIA_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007837"
    )

    # curator inference from book used in automatic assertion
    ECO_0007838 = "ECO_0007838"
    CURATOR_INFERENCE_FROM_BOOK_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007838"

    # curator inference from dictionary used in automatic assertion
    ECO_0007839 = "ECO_0007839"
    CURATOR_INFERENCE_FROM_DICTIONARY_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007839"

    # curator inference from MedlinePlus dictionary used in automatic assertion
    ECO_0007840 = "ECO_0007840"
    CURATOR_INFERENCE_FROM_MEDLINEPLUS_DICTIONARY_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007840"
    )

    # curator inference from Merriam-Webster Dictionary used in automatic assertion
    ECO_0007841 = "ECO_0007841"
    CURATOR_INFERENCE_FROM_MERRIAM_WEBSTER_DICTIONARY_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007841"
    )

    # curator inference from Oxford Dictionary used in automatic assertion
    ECO_0007842 = "ECO_0007842"
    CURATOR_INFERENCE_FROM_OXFORD_DICTIONARY_USED_IN_AUTOMATIC_ASSERTION = "ECO_0007842"

    # curator inference from journal publication used in automatic assertion
    ECO_0007843 = "ECO_0007843"
    CURATOR_INFERENCE_FROM_JOURNAL_PUBLICATION_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007843"
    )

    # radioisotope quantification assay evidence
    ECO_0007844 = "ECO_0007844"
    RADIOISOTOPE_QUANTIFICATION_ASSAY_EVIDENCE = "ECO_0007844"

    # radioisotope quantification assay evidence used in automatic assertion
    ECO_0007845 = "ECO_0007845"
    RADIOISOTOPE_QUANTIFICATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007845"
    )

    # radioisotope quantification assay evidence used in manual assertion
    ECO_0007846 = "ECO_0007846"
    RADIOISOTOPE_QUANTIFICATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007846"

    # fluorescence quantification assay evidence
    ECO_0007847 = "ECO_0007847"
    FLUORESCENCE_QUANTIFICATION_ASSAY_EVIDENCE = "ECO_0007847"

    # fluorescence quantification assay evidence used in automatic assertion
    ECO_0007848 = "ECO_0007848"
    FLUORESCENCE_QUANTIFICATION_ASSAY_EVIDENCE_USED_IN_AUTOMATIC_ASSERTION = (
        "ECO_0007848"
    )

    # fluorescence quantification assay evidence used in manual assertion
    ECO_0007849 = "ECO_0007849"
    FLUORESCENCE_QUANTIFICATION_ASSAY_EVIDENCE_USED_IN_MANUAL_ASSERTION = "ECO_0007849"

    # inference of sequence features from visual inspection
    ECO_0007850 = "ECO_0007850"
    INFERENCE_OF_SEQUENCE_FEATURES_FROM_VISUAL_INSPECTION = "ECO_0007850"

    # DNA catabolic process, endonucleolytic
    GO_0000737 = "GO_0000737"
    DNA_CATABOLIC_PROCESS__ENDONUCLEOLYTIC = "GO_0000737"

    # chromatin
    GO_0000785 = "GO_0000785"
    CHROMATIN = "GO_0000785"

    # core promoter binding
    GO_0001047 = "GO_0001047"
    CORE_PROMOTER_BINDING = "GO_0001047"

    # regulatory region nucleic acid binding
    GO_0001067 = "GO_0001067"
    REGULATORY_REGION_NUCLEIC_ACID_BINDING = "GO_0001067"

    # transcription, RNA-templated
    GO_0001172 = "GO_0001172"
    TRANSCRIPTION__RNA_TEMPLATED = "GO_0001172"

    # action potential
    GO_0001508 = "GO_0001508"
    ACTION_POTENTIAL = "GO_0001508"

    # regulation of cell growth
    GO_0001558 = "GO_0001558"
    REGULATION_OF_CELL_GROWTH = "GO_0001558"

    # cytokine production
    GO_0001816 = "GO_0001816"
    CYTOKINE_PRODUCTION = "GO_0001816"

    # regulation of cytokine production
    GO_0001817 = "GO_0001817"
    REGULATION_OF_CYTOKINE_PRODUCTION = "GO_0001817"

    # negative regulation of cytokine production
    GO_0001818 = "GO_0001818"
    NEGATIVE_REGULATION_OF_CYTOKINE_PRODUCTION = "GO_0001818"

    # positive regulation of cytokine production
    GO_0001819 = "GO_0001819"
    POSITIVE_REGULATION_OF_CYTOKINE_PRODUCTION = "GO_0001819"

    # nucleoside binding
    GO_0001882 = "GO_0001882"
    NUCLEOSIDE_BINDING = "GO_0001882"

    # cell killing
    GO_0001906 = "GO_0001906"
    CELL_KILLING = "GO_0001906"

    # peptide secretion
    GO_0002790 = "GO_0002790"
    PEPTIDE_SECRETION = "GO_0002790"

    # regulation of peptide secretion
    GO_0002791 = "GO_0002791"
    REGULATION_OF_PEPTIDE_SECRETION = "GO_0002791"

    # negative regulation of peptide secretion
    GO_0002792 = "GO_0002792"
    NEGATIVE_REGULATION_OF_PEPTIDE_SECRETION = "GO_0002792"

    # positive regulation of peptide secretion
    GO_0002793 = "GO_0002793"
    POSITIVE_REGULATION_OF_PEPTIDE_SECRETION = "GO_0002793"

    # regulation of response to biotic stimulus
    GO_0002831 = "GO_0002831"
    REGULATION_OF_RESPONSE_TO_BIOTIC_STIMULUS = "GO_0002831"

    # negative regulation of response to biotic stimulus
    GO_0002832 = "GO_0002832"
    NEGATIVE_REGULATION_OF_RESPONSE_TO_BIOTIC_STIMULUS = "GO_0002832"

    # positive regulation of response to biotic stimulus
    GO_0002833 = "GO_0002833"
    POSITIVE_REGULATION_OF_RESPONSE_TO_BIOTIC_STIMULUS = "GO_0002833"

    # GO:molecular_function
    GO_0003674 = "GO_0003674"
    GO_MOLECULAR_FUNCTION = "GO_0003674"

    # nucleic acid binding
    GO_0003676 = "GO_0003676"
    NUCLEIC_ACID_BINDING = "GO_0003676"

    # DNA binding
    GO_0003677 = "GO_0003677"
    DNA_BINDING = "GO_0003677"

    # antigen binding
    GO_0003823 = "GO_0003823"
    ANTIGEN_BINDING = "GO_0003823"

    # catalytic activity
    GO_0003824 = "GO_0003824"
    CATALYTIC_ACTIVITY = "GO_0003824"

    # RNA-directed DNA polymerase activity
    GO_0003964 = "GO_0003964"
    RNA_DIRECTED_DNA_POLYMERASE_ACTIVITY = "GO_0003964"

    # nuclease activity
    GO_0004518 = "GO_0004518"
    NUCLEASE_ACTIVITY = "GO_0004518"

    # endonuclease activity
    GO_0004519 = "GO_0004519"
    ENDONUCLEASE_ACTIVITY = "GO_0004519"

    # endodeoxyribonuclease activity
    GO_0004520 = "GO_0004520"
    ENDODEOXYRIBONUCLEASE_ACTIVITY = "GO_0004520"

    # deoxyribonuclease activity
    GO_0004536 = "GO_0004536"
    DEOXYRIBONUCLEASE_ACTIVITY = "GO_0004536"

    # transporter activity
    GO_0005215 = "GO_0005215"
    TRANSPORTER_ACTIVITY = "GO_0005215"

    # ion channel activity
    GO_0005216 = "GO_0005216"
    ION_CHANNEL_ACTIVITY = "GO_0005216"

    # binding
    GO_0005488 = "GO_0005488"
    BINDING = "GO_0005488"

    # protein binding
    GO_0005515 = "GO_0005515"
    PROTEIN_BINDING = "GO_0005515"

    # cellular_component
    GO_0005575 = "GO_0005575"
    CELLULAR_COMPONENT = "GO_0005575"

    # intracellular
    GO_0005622 = "GO_0005622"
    INTRACELLULAR = "GO_0005622"

    # chromosome
    GO_0005694 = "GO_0005694"
    CHROMOSOME = "GO_0005694"

    # nucleobase-containing compound metabolic process
    GO_0006139 = "GO_0006139"
    NUCLEOBASE_CONTAINING_COMPOUND_METABOLIC_PROCESS = "GO_0006139"

    # DNA metabolic process
    GO_0006259 = "GO_0006259"
    DNA_METABOLIC_PROCESS = "GO_0006259"

    # DNA replication
    GO_0006260 = "GO_0006260"
    DNA_REPLICATION = "GO_0006260"

    # regulation of DNA replication
    GO_0006275 = "GO_0006275"
    REGULATION_OF_DNA_REPLICATION = "GO_0006275"

    # plasmid maintenance
    GO_0006276 = "GO_0006276"
    PLASMID_MAINTENANCE = "GO_0006276"

    # DNA modification
    GO_0006304 = "GO_0006304"
    DNA_MODIFICATION = "GO_0006304"

    # DNA alkylation
    GO_0006305 = "GO_0006305"
    DNA_ALKYLATION = "GO_0006305"

    # DNA methylation
    GO_0006306 = "GO_0006306"
    DNA_METHYLATION = "GO_0006306"

    # DNA catabolic process
    GO_0006308 = "GO_0006308"
    DNA_CATABOLIC_PROCESS = "GO_0006308"

    # apoptotic DNA fragmentation
    GO_0006309 = "GO_0006309"
    APOPTOTIC_DNA_FRAGMENTATION = "GO_0006309"

    # transcription, DNA-templated
    GO_0006351 = "GO_0006351"
    TRANSCRIPTION__DNA_TEMPLATED = "GO_0006351"

    # regulation of transcription, DNA-templated
    GO_0006355 = "GO_0006355"
    REGULATION_OF_TRANSCRIPTION__DNA_TEMPLATED = "GO_0006355"

    # translation
    GO_0006412 = "GO_0006412"
    TRANSLATION = "GO_0006412"

    # translational elongation
    GO_0006414 = "GO_0006414"
    TRANSLATIONAL_ELONGATION = "GO_0006414"

    # regulation of translation
    GO_0006417 = "GO_0006417"
    REGULATION_OF_TRANSLATION = "GO_0006417"

    # regulation of translational elongation
    GO_0006448 = "GO_0006448"
    REGULATION_OF_TRANSLATIONAL_ELONGATION = "GO_0006448"

    # peptide metabolic process
    GO_0006518 = "GO_0006518"
    PEPTIDE_METABOLIC_PROCESS = "GO_0006518"

    # cellular aromatic compound metabolic process
    GO_0006725 = "GO_0006725"
    CELLULAR_AROMATIC_COMPOUND_METABOLIC_PROCESS = "GO_0006725"

    # nitrogen compound metabolic process
    GO_0006807 = "GO_0006807"
    NITROGEN_COMPOUND_METABOLIC_PROCESS = "GO_0006807"

    # transport
    GO_0006810 = "GO_0006810"
    TRANSPORT = "GO_0006810"

    # ion transport
    GO_0006811 = "GO_0006811"
    ION_TRANSPORT = "GO_0006811"

    # anion transport
    GO_0006820 = "GO_0006820"
    ANION_TRANSPORT = "GO_0006820"

    # lipid transport
    GO_0006869 = "GO_0006869"
    LIPID_TRANSPORT = "GO_0006869"

    # apoptotic process
    GO_0006915 = "GO_0006915"
    APOPTOTIC_PROCESS = "GO_0006915"

    # cellular component disassembly involved in execution phase of apoptosis
    GO_0006921 = "GO_0006921"
    CELLULAR_COMPONENT_DISASSEMBLY_INVOLVED_IN_EXECUTION_PHASE_OF_APOPTOSIS = (
        "GO_0006921"
    )

    # movement of cell or subcellular component
    GO_0006928 = "GO_0006928"
    MOVEMENT_OF_CELL_OR_SUBCELLULAR_COMPONENT = "GO_0006928"

    # chemotaxis
    GO_0006935 = "GO_0006935"
    CHEMOTAXIS = "GO_0006935"

    # response to stress
    GO_0006950 = "GO_0006950"
    RESPONSE_TO_STRESS = "GO_0006950"

    # cellular response to DNA damage stimulus
    GO_0006974 = "GO_0006974"
    CELLULAR_RESPONSE_TO_DNA_DAMAGE_STIMULUS = "GO_0006974"

    # organelle organization
    GO_0006996 = "GO_0006996"
    ORGANELLE_ORGANIZATION = "GO_0006996"

    # nucleus organization
    GO_0006997 = "GO_0006997"
    NUCLEUS_ORGANIZATION = "GO_0006997"

    # nucleolus organization
    GO_0007000 = "GO_0007000"
    NUCLEOLUS_ORGANIZATION = "GO_0007000"

    # aging
    GO_0007568 = "GO_0007568"
    AGING = "GO_0007568"

    # cell aging
    GO_0007569 = "GO_0007569"
    CELL_AGING = "GO_0007569"

    # nucleolar fragmentation
    GO_0007576 = "GO_0007576"
    NUCLEOLAR_FRAGMENTATION = "GO_0007576"

    # protein localization
    GO_0008104 = "GO_0008104"
    PROTEIN_LOCALIZATION = "GO_0008104"

    # biological_process
    GO_0008150 = "GO_0008150"
    BIOLOGICAL_PROCESS = "GO_0008150"

    # metabolic process
    GO_0008152 = "GO_0008152"
    METABOLIC_PROCESS = "GO_0008152"

    # negative regulation of DNA replication
    GO_0008156 = "GO_0008156"
    NEGATIVE_REGULATION_OF_DNA_REPLICATION = "GO_0008156"

    # cell death
    GO_0008219 = "GO_0008219"
    CELL_DEATH = "GO_0008219"

    # cell population proliferation
    GO_0008283 = "GO_0008283"
    CELL_POPULATION_PROLIFERATION = "GO_0008283"

    # positive regulation of cell population proliferation
    GO_0008284 = "GO_0008284"
    POSITIVE_REGULATION_OF_CELL_POPULATION_PROLIFERATION = "GO_0008284"

    # negative regulation of cell population proliferation
    GO_0008285 = "GO_0008285"
    NEGATIVE_REGULATION_OF_CELL_POPULATION_PROLIFERATION = "GO_0008285"

    # lipid binding
    GO_0008289 = "GO_0008289"
    LIPID_BINDING = "GO_0008289"

    # catabolic process
    GO_0009056 = "GO_0009056"
    CATABOLIC_PROCESS = "GO_0009056"

    # macromolecule catabolic process
    GO_0009057 = "GO_0009057"
    MACROMOLECULE_CATABOLIC_PROCESS = "GO_0009057"

    # biosynthetic process
    GO_0009058 = "GO_0009058"
    BIOSYNTHETIC_PROCESS = "GO_0009058"

    # macromolecule biosynthetic process
    GO_0009059 = "GO_0009059"
    MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_0009059"

    # antisense RNA transcription
    GO_0009300 = "GO_0009300"
    ANTISENSE_RNA_TRANSCRIPTION = "GO_0009300"

    # protein secretion
    GO_0009306 = "GO_0009306"
    PROTEIN_SECRETION = "GO_0009306"

    # response to external stimulus
    GO_0009605 = "GO_0009605"
    RESPONSE_TO_EXTERNAL_STIMULUS = "GO_0009605"

    # response to biotic stimulus
    GO_0009607 = "GO_0009607"
    RESPONSE_TO_BIOTIC_STIMULUS = "GO_0009607"

    # response to wounding
    GO_0009611 = "GO_0009611"
    RESPONSE_TO_WOUNDING = "GO_0009611"

    # response to toxic substance
    GO_0009636 = "GO_0009636"
    RESPONSE_TO_TOXIC_SUBSTANCE = "GO_0009636"

    # anatomical structure morphogenesis
    GO_0009653 = "GO_0009653"
    ANATOMICAL_STRUCTURE_MORPHOGENESIS = "GO_0009653"

    # response to endogenous stimulus
    GO_0009719 = "GO_0009719"
    RESPONSE_TO_ENDOGENOUS_STIMULUS = "GO_0009719"

    # regulation of biosynthetic process
    GO_0009889 = "GO_0009889"
    REGULATION_OF_BIOSYNTHETIC_PROCESS = "GO_0009889"

    # negative regulation of biosynthetic process
    GO_0009890 = "GO_0009890"
    NEGATIVE_REGULATION_OF_BIOSYNTHETIC_PROCESS = "GO_0009890"

    # positive regulation of biosynthetic process
    GO_0009891 = "GO_0009891"
    POSITIVE_REGULATION_OF_BIOSYNTHETIC_PROCESS = "GO_0009891"

    # negative regulation of metabolic process
    GO_0009892 = "GO_0009892"
    NEGATIVE_REGULATION_OF_METABOLIC_PROCESS = "GO_0009892"

    # positive regulation of metabolic process
    GO_0009893 = "GO_0009893"
    POSITIVE_REGULATION_OF_METABOLIC_PROCESS = "GO_0009893"

    # regulation of catabolic process
    GO_0009894 = "GO_0009894"
    REGULATION_OF_CATABOLIC_PROCESS = "GO_0009894"

    # negative regulation of catabolic process
    GO_0009895 = "GO_0009895"
    NEGATIVE_REGULATION_OF_CATABOLIC_PROCESS = "GO_0009895"

    # positive regulation of catabolic process
    GO_0009896 = "GO_0009896"
    POSITIVE_REGULATION_OF_CATABOLIC_PROCESS = "GO_0009896"

    # cellular process
    GO_0009987 = "GO_0009987"
    CELLULAR_PROCESS = "GO_0009987"

    # response to organic substance
    GO_0010033 = "GO_0010033"
    RESPONSE_TO_ORGANIC_SUBSTANCE = "GO_0010033"

    # response to mycotoxin
    GO_0010046 = "GO_0010046"
    RESPONSE_TO_MYCOTOXIN = "GO_0010046"

    # response to organonitrogen compound
    GO_0010243 = "GO_0010243"
    RESPONSE_TO_ORGANONITROGEN_COMPOUND = "GO_0010243"

    # gene expression
    GO_0010467 = "GO_0010467"
    GENE_EXPRESSION = "GO_0010467"

    # regulation of gene expression
    GO_0010468 = "GO_0010468"
    REGULATION_OF_GENE_EXPRESSION = "GO_0010468"

    # regulation of macromolecule biosynthetic process
    GO_0010556 = "GO_0010556"
    REGULATION_OF_MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_0010556"

    # positive regulation of macromolecule biosynthetic process
    GO_0010557 = "GO_0010557"
    POSITIVE_REGULATION_OF_MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_0010557"

    # negative regulation of macromolecule biosynthetic process
    GO_0010558 = "GO_0010558"
    NEGATIVE_REGULATION_OF_MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_0010558"

    # positive regulation of macromolecule metabolic process
    GO_0010604 = "GO_0010604"
    POSITIVE_REGULATION_OF_MACROMOLECULE_METABOLIC_PROCESS = "GO_0010604"

    # negative regulation of macromolecule metabolic process
    GO_0010605 = "GO_0010605"
    NEGATIVE_REGULATION_OF_MACROMOLECULE_METABOLIC_PROCESS = "GO_0010605"

    # posttranscriptional regulation of gene expression
    GO_0010608 = "GO_0010608"
    POSTTRANSCRIPTIONAL_REGULATION_OF_GENE_EXPRESSION = "GO_0010608"

    # positive regulation of gene expression
    GO_0010628 = "GO_0010628"
    POSITIVE_REGULATION_OF_GENE_EXPRESSION = "GO_0010628"

    # negative regulation of gene expression
    GO_0010629 = "GO_0010629"
    NEGATIVE_REGULATION_OF_GENE_EXPRESSION = "GO_0010629"

    # positive regulation of organelle organization
    GO_0010638 = "GO_0010638"
    POSITIVE_REGULATION_OF_ORGANELLE_ORGANIZATION = "GO_0010638"

    # negative regulation of organelle organization
    GO_0010639 = "GO_0010639"
    NEGATIVE_REGULATION_OF_ORGANELLE_ORGANIZATION = "GO_0010639"

    # lipid localization
    GO_0010876 = "GO_0010876"
    LIPID_LOCALIZATION = "GO_0010876"

    # cellular component assembly involved in morphogenesis
    GO_0010927 = "GO_0010927"
    CELLULAR_COMPONENT_ASSEMBLY_INVOLVED_IN_MORPHOGENESIS = "GO_0010927"

    # regulation of cell death
    GO_0010941 = "GO_0010941"
    REGULATION_OF_CELL_DEATH = "GO_0010941"

    # positive regulation of cell death
    GO_0010942 = "GO_0010942"
    POSITIVE_REGULATION_OF_CELL_DEATH = "GO_0010942"

    # programmed cell death
    GO_0012501 = "GO_0012501"
    PROGRAMMED_CELL_DEATH = "GO_0012501"

    # response to organic cyclic compound
    GO_0014070 = "GO_0014070"
    RESPONSE_TO_ORGANIC_CYCLIC_COMPOUND = "GO_0014070"

    # protein transport
    GO_0015031 = "GO_0015031"
    PROTEIN_TRANSPORT = "GO_0015031"

    # ion transmembrane transporter activity
    GO_0015075 = "GO_0015075"
    ION_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0015075"

    # channel activity
    GO_0015267 = "GO_0015267"
    CHANNEL_ACTIVITY = "GO_0015267"

    # inorganic molecular entity transmembrane transporter activity
    GO_0015318 = "GO_0015318"
    INORGANIC_MOLECULAR_ENTITY_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0015318"

    # organic anion transport
    GO_0015711 = "GO_0015711"
    ORGANIC_ANION_TRANSPORT = "GO_0015711"

    # monocarboxylic acid transport
    GO_0015718 = "GO_0015718"
    MONOCARBOXYLIC_ACID_TRANSPORT = "GO_0015718"

    # peptide transport
    GO_0015833 = "GO_0015833"
    PEPTIDE_TRANSPORT = "GO_0015833"

    # organic acid transport
    GO_0015849 = "GO_0015849"
    ORGANIC_ACID_TRANSPORT = "GO_0015849"

    # fatty acid transport
    GO_0015908 = "GO_0015908"
    FATTY_ACID_TRANSPORT = "GO_0015908"

    # long-chain fatty acid transport
    GO_0015909 = "GO_0015909"
    LONG_CHAIN_FATTY_ACID_TRANSPORT = "GO_0015909"

    # cellular component organization
    GO_0016043 = "GO_0016043"
    CELLULAR_COMPONENT_ORGANIZATION = "GO_0016043"

    # cell growth
    GO_0016049 = "GO_0016049"
    CELL_GROWTH = "GO_0016049"

    # RNA metabolic process
    GO_0016070 = "GO_0016070"
    RNA_METABOLIC_PROCESS = "GO_0016070"

    # RNA interference
    GO_0016246 = "GO_0016246"
    RNA_INTERFERENCE = "GO_0016246"

    # posttranscriptional gene silencing
    GO_0016441 = "GO_0016441"
    POSTTRANSCRIPTIONAL_GENE_SILENCING = "GO_0016441"

    # gene silencing
    GO_0016458 = "GO_0016458"
    GENE_SILENCING = "GO_0016458"

    # cell migration
    GO_0016477 = "GO_0016477"
    CELL_MIGRATION = "GO_0016477"

    # hydrolase activity
    GO_0016787 = "GO_0016787"
    HYDROLASE_ACTIVITY = "GO_0016787"

    # hydrolase activity, acting on ester bonds
    GO_0016788 = "GO_0016788"
    HYDROLASE_ACTIVITY__ACTING_ON_ESTER_BONDS = "GO_0016788"

    # negative regulation of translation
    GO_0017148 = "GO_0017148"
    NEGATIVE_REGULATION_OF_TRANSLATION = "GO_0017148"

    # heterocycle biosynthetic process
    GO_0018130 = "GO_0018130"
    HETEROCYCLE_BIOSYNTHETIC_PROCESS = "GO_0018130"

    # regulation of nucleobase-containing compound metabolic process
    GO_0019219 = "GO_0019219"
    REGULATION_OF_NUCLEOBASE_CONTAINING_COMPOUND_METABOLIC_PROCESS = "GO_0019219"

    # regulation of metabolic process
    GO_0019222 = "GO_0019222"
    REGULATION_OF_METABOLIC_PROCESS = "GO_0019222"

    # aromatic compound biosynthetic process
    GO_0019438 = "GO_0019438"
    AROMATIC_COMPOUND_BIOSYNTHETIC_PROCESS = "GO_0019438"

    # aromatic compound catabolic process
    GO_0019439 = "GO_0019439"
    AROMATIC_COMPOUND_CATABOLIC_PROCESS = "GO_0019439"

    # protein metabolic process
    GO_0019538 = "GO_0019538"
    PROTEIN_METABOLIC_PROCESS = "GO_0019538"

    # immunoglobulin complex
    GO_0019814 = "GO_0019814"
    IMMUNOGLOBULIN_COMPLEX = "GO_0019814"

    # B cell receptor complex
    GO_0019815 = "GO_0019815"
    B_CELL_RECEPTOR_COMPLEX = "GO_0019815"

    # protein domain specific binding
    GO_0019904 = "GO_0019904"
    PROTEIN_DOMAIN_SPECIFIC_BINDING = "GO_0019904"

    # cellular component disassembly
    GO_0022411 = "GO_0022411"
    CELLULAR_COMPONENT_DISASSEMBLY = "GO_0022411"

    # regulation of anatomical structure morphogenesis
    GO_0022603 = "GO_0022603"
    REGULATION_OF_ANATOMICAL_STRUCTURE_MORPHOGENESIS = "GO_0022603"

    # cellular component assembly
    GO_0022607 = "GO_0022607"
    CELLULAR_COMPONENT_ASSEMBLY = "GO_0022607"

    # passive transmembrane transporter activity
    GO_0022803 = "GO_0022803"
    PASSIVE_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0022803"

    # transmembrane transporter activity
    GO_0022857 = "GO_0022857"
    TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0022857"

    # regulation of transmembrane transporter activity
    GO_0022898 = "GO_0022898"
    REGULATION_OF_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0022898"

    # cell projection organization
    GO_0030030 = "GO_0030030"
    CELL_PROJECTION_ORGANIZATION = "GO_0030030"

    # cell projection assembly
    GO_0030031 = "GO_0030031"
    CELL_PROJECTION_ASSEMBLY = "GO_0030031"

    # actin filament polymerization
    GO_0030041 = "GO_0030041"
    ACTIN_FILAMENT_POLYMERIZATION = "GO_0030041"

    # hemopoiesis
    GO_0030097 = "GO_0030097"
    HEMOPOIESIS = "GO_0030097"

    # apoptotic nuclear changes
    GO_0030262 = "GO_0030262"
    APOPTOTIC_NUCLEAR_CHANGES = "GO_0030262"

    # positive regulation of cell growth
    GO_0030307 = "GO_0030307"
    POSITIVE_REGULATION_OF_CELL_GROWTH = "GO_0030307"

    # negative regulation of cell growth
    GO_0030308 = "GO_0030308"
    NEGATIVE_REGULATION_OF_CELL_GROWTH = "GO_0030308"

    # regulation of cell migration
    GO_0030334 = "GO_0030334"
    REGULATION_OF_CELL_MIGRATION = "GO_0030334"

    # positive regulation of cell migration
    GO_0030335 = "GO_0030335"
    POSITIVE_REGULATION_OF_CELL_MIGRATION = "GO_0030335"

    # negative regulation of cell migration
    GO_0030336 = "GO_0030336"
    NEGATIVE_REGULATION_OF_CELL_MIGRATION = "GO_0030336"

    # gene silencing by RNA
    GO_0031047 = "GO_0031047"
    GENE_SILENCING_BY_RNA = "GO_0031047"

    # regulation of cellular metabolic process
    GO_0031323 = "GO_0031323"
    REGULATION_OF_CELLULAR_METABOLIC_PROCESS = "GO_0031323"

    # negative regulation of cellular metabolic process
    GO_0031324 = "GO_0031324"
    NEGATIVE_REGULATION_OF_CELLULAR_METABOLIC_PROCESS = "GO_0031324"

    # positive regulation of cellular metabolic process
    GO_0031325 = "GO_0031325"
    POSITIVE_REGULATION_OF_CELLULAR_METABOLIC_PROCESS = "GO_0031325"

    # regulation of cellular biosynthetic process
    GO_0031326 = "GO_0031326"
    REGULATION_OF_CELLULAR_BIOSYNTHETIC_PROCESS = "GO_0031326"

    # negative regulation of cellular biosynthetic process
    GO_0031327 = "GO_0031327"
    NEGATIVE_REGULATION_OF_CELLULAR_BIOSYNTHETIC_PROCESS = "GO_0031327"

    # positive regulation of cellular biosynthetic process
    GO_0031328 = "GO_0031328"
    POSITIVE_REGULATION_OF_CELLULAR_BIOSYNTHETIC_PROCESS = "GO_0031328"

    # regulation of cellular catabolic process
    GO_0031329 = "GO_0031329"
    REGULATION_OF_CELLULAR_CATABOLIC_PROCESS = "GO_0031329"

    # negative regulation of cellular catabolic process
    GO_0031330 = "GO_0031330"
    NEGATIVE_REGULATION_OF_CELLULAR_CATABOLIC_PROCESS = "GO_0031330"

    # positive regulation of cellular catabolic process
    GO_0031331 = "GO_0031331"
    POSITIVE_REGULATION_OF_CELLULAR_CATABOLIC_PROCESS = "GO_0031331"

    # regulation of cell killing
    GO_0031341 = "GO_0031341"
    REGULATION_OF_CELL_KILLING = "GO_0031341"

    # negative regulation of cell killing
    GO_0031342 = "GO_0031342"
    NEGATIVE_REGULATION_OF_CELL_KILLING = "GO_0031342"

    # positive regulation of cell killing
    GO_0031343 = "GO_0031343"
    POSITIVE_REGULATION_OF_CELL_KILLING = "GO_0031343"

    # regulation of cell projection organization
    GO_0031344 = "GO_0031344"
    REGULATION_OF_CELL_PROJECTION_ORGANIZATION = "GO_0031344"

    # negative regulation of cell projection organization
    GO_0031345 = "GO_0031345"
    NEGATIVE_REGULATION_OF_CELL_PROJECTION_ORGANIZATION = "GO_0031345"

    # positive regulation of cell projection organization
    GO_0031346 = "GO_0031346"
    POSITIVE_REGULATION_OF_CELL_PROJECTION_ORGANIZATION = "GO_0031346"

    # bleb assembly
    GO_0032060 = "GO_0032060"
    BLEB_ASSEMBLY = "GO_0032060"

    # regulation of nuclease activity
    GO_0032069 = "GO_0032069"
    REGULATION_OF_NUCLEASE_ACTIVITY = "GO_0032069"

    # regulation of deoxyribonuclease activity
    GO_0032070 = "GO_0032070"
    REGULATION_OF_DEOXYRIBONUCLEASE_ACTIVITY = "GO_0032070"

    # regulation of endodeoxyribonuclease activity
    GO_0032071 = "GO_0032071"
    REGULATION_OF_ENDODEOXYRIBONUCLEASE_ACTIVITY = "GO_0032071"

    # negative regulation of nuclease activity
    GO_0032074 = "GO_0032074"
    NEGATIVE_REGULATION_OF_NUCLEASE_ACTIVITY = "GO_0032074"

    # positive regulation of nuclease activity
    GO_0032075 = "GO_0032075"
    POSITIVE_REGULATION_OF_NUCLEASE_ACTIVITY = "GO_0032075"

    # negative regulation of deoxyribonuclease activity
    GO_0032076 = "GO_0032076"
    NEGATIVE_REGULATION_OF_DEOXYRIBONUCLEASE_ACTIVITY = "GO_0032076"

    # positive regulation of deoxyribonuclease activity
    GO_0032077 = "GO_0032077"
    POSITIVE_REGULATION_OF_DEOXYRIBONUCLEASE_ACTIVITY = "GO_0032077"

    # negative regulation of endodeoxyribonuclease activity
    GO_0032078 = "GO_0032078"
    NEGATIVE_REGULATION_OF_ENDODEOXYRIBONUCLEASE_ACTIVITY = "GO_0032078"

    # positive regulation of endodeoxyribonuclease activity
    GO_0032079 = "GO_0032079"
    POSITIVE_REGULATION_OF_ENDODEOXYRIBONUCLEASE_ACTIVITY = "GO_0032079"

    # negative regulation of protein binding
    GO_0032091 = "GO_0032091"
    NEGATIVE_REGULATION_OF_PROTEIN_BINDING = "GO_0032091"

    # positive regulation of protein binding
    GO_0032092 = "GO_0032092"
    POSITIVE_REGULATION_OF_PROTEIN_BINDING = "GO_0032092"

    # regulation of response to external stimulus
    GO_0032101 = "GO_0032101"
    REGULATION_OF_RESPONSE_TO_EXTERNAL_STIMULUS = "GO_0032101"

    # negative regulation of response to external stimulus
    GO_0032102 = "GO_0032102"
    NEGATIVE_REGULATION_OF_RESPONSE_TO_EXTERNAL_STIMULUS = "GO_0032102"

    # positive regulation of response to external stimulus
    GO_0032103 = "GO_0032103"
    POSITIVE_REGULATION_OF_RESPONSE_TO_EXTERNAL_STIMULUS = "GO_0032103"

    # methylation
    GO_0032259 = "GO_0032259"
    METHYLATION = "GO_0032259"

    # regulation of cellular protein metabolic process
    GO_0032268 = "GO_0032268"
    REGULATION_OF_CELLULAR_PROTEIN_METABOLIC_PROCESS = "GO_0032268"

    # negative regulation of cellular protein metabolic process
    GO_0032269 = "GO_0032269"
    NEGATIVE_REGULATION_OF_CELLULAR_PROTEIN_METABOLIC_PROCESS = "GO_0032269"

    # positive regulation of cellular protein metabolic process
    GO_0032270 = "GO_0032270"
    POSITIVE_REGULATION_OF_CELLULAR_PROTEIN_METABOLIC_PROCESS = "GO_0032270"

    # regulation of icosanoid secretion
    GO_0032303 = "GO_0032303"
    REGULATION_OF_ICOSANOID_SECRETION = "GO_0032303"

    # negative regulation of icosanoid secretion
    GO_0032304 = "GO_0032304"
    NEGATIVE_REGULATION_OF_ICOSANOID_SECRETION = "GO_0032304"

    # positive regulation of icosanoid secretion
    GO_0032305 = "GO_0032305"
    POSITIVE_REGULATION_OF_ICOSANOID_SECRETION = "GO_0032305"

    # icosanoid secretion
    GO_0032309 = "GO_0032309"
    ICOSANOID_SECRETION = "GO_0032309"

    # regulation of lipid transport
    GO_0032368 = "GO_0032368"
    REGULATION_OF_LIPID_TRANSPORT = "GO_0032368"

    # negative regulation of lipid transport
    GO_0032369 = "GO_0032369"
    NEGATIVE_REGULATION_OF_LIPID_TRANSPORT = "GO_0032369"

    # positive regulation of lipid transport
    GO_0032370 = "GO_0032370"
    POSITIVE_REGULATION_OF_LIPID_TRANSPORT = "GO_0032370"

    # regulation of transporter activity
    GO_0032409 = "GO_0032409"
    REGULATION_OF_TRANSPORTER_ACTIVITY = "GO_0032409"

    # negative regulation of transporter activity
    GO_0032410 = "GO_0032410"
    NEGATIVE_REGULATION_OF_TRANSPORTER_ACTIVITY = "GO_0032410"

    # positive regulation of transporter activity
    GO_0032411 = "GO_0032411"
    POSITIVE_REGULATION_OF_TRANSPORTER_ACTIVITY = "GO_0032411"

    # regulation of ion transmembrane transporter activity
    GO_0032412 = "GO_0032412"
    REGULATION_OF_ION_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0032412"

    # negative regulation of ion transmembrane transporter activity
    GO_0032413 = "GO_0032413"
    NEGATIVE_REGULATION_OF_ION_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0032413"

    # positive regulation of ion transmembrane transporter activity
    GO_0032414 = "GO_0032414"
    POSITIVE_REGULATION_OF_ION_TRANSMEMBRANE_TRANSPORTER_ACTIVITY = "GO_0032414"

    # multicellular organismal process
    GO_0032501 = "GO_0032501"
    MULTICELLULAR_ORGANISMAL_PROCESS = "GO_0032501"

    # developmental process
    GO_0032502 = "GO_0032502"
    DEVELOPMENTAL_PROCESS = "GO_0032502"

    # ribonucleoside binding
    GO_0032549 = "GO_0032549"
    RIBONUCLEOSIDE_BINDING = "GO_0032549"

    # tumor necrosis factor production
    GO_0032640 = "GO_0032640"
    TUMOR_NECROSIS_FACTOR_PRODUCTION = "GO_0032640"

    # regulation of tumor necrosis factor production
    GO_0032680 = "GO_0032680"
    REGULATION_OF_TUMOR_NECROSIS_FACTOR_PRODUCTION = "GO_0032680"

    # negative regulation of tumor necrosis factor production
    GO_0032720 = "GO_0032720"
    NEGATIVE_REGULATION_OF_TUMOR_NECROSIS_FACTOR_PRODUCTION = "GO_0032720"

    # positive regulation of tumor necrosis factor production
    GO_0032760 = "GO_0032760"
    POSITIVE_REGULATION_OF_TUMOR_NECROSIS_FACTOR_PRODUCTION = "GO_0032760"

    # RNA biosynthetic process
    GO_0032774 = "GO_0032774"
    RNA_BIOSYNTHETIC_PROCESS = "GO_0032774"

    # regulation of localization
    GO_0032879 = "GO_0032879"
    REGULATION_OF_LOCALIZATION = "GO_0032879"

    # regulation of protein localization
    GO_0032880 = "GO_0032880"
    REGULATION_OF_PROTEIN_LOCALIZATION = "GO_0032880"

    # regulation of organic acid transport
    GO_0032890 = "GO_0032890"
    REGULATION_OF_ORGANIC_ACID_TRANSPORT = "GO_0032890"

    # negative regulation of organic acid transport
    GO_0032891 = "GO_0032891"
    NEGATIVE_REGULATION_OF_ORGANIC_ACID_TRANSPORT = "GO_0032891"

    # positive regulation of organic acid transport
    GO_0032892 = "GO_0032892"
    POSITIVE_REGULATION_OF_ORGANIC_ACID_TRANSPORT = "GO_0032892"

    # secretion by cell
    GO_0032940 = "GO_0032940"
    SECRETION_BY_CELL = "GO_0032940"

    # cellular component morphogenesis
    GO_0032989 = "GO_0032989"
    CELLULAR_COMPONENT_MORPHOGENESIS = "GO_0032989"

    # protein-containing complex
    GO_0032991 = "GO_0032991"
    PROTEIN_CONTAINING_COMPLEX = "GO_0032991"

    # macromolecule localization
    GO_0033036 = "GO_0033036"
    MACROMOLECULE_LOCALIZATION = "GO_0033036"

    # regulation of organelle organization
    GO_0033043 = "GO_0033043"
    REGULATION_OF_ORGANELLE_ORGANIZATION = "GO_0033043"

    # regulation of chromosome organization
    GO_0033044 = "GO_0033044"
    REGULATION_OF_CHROMOSOME_ORGANIZATION = "GO_0033044"

    # amide binding
    GO_0033218 = "GO_0033218"
    AMIDE_BINDING = "GO_0033218"

    # cellular response to stress
    GO_0033554 = "GO_0033554"
    CELLULAR_RESPONSE_TO_STRESS = "GO_0033554"

    # DNA polymerase activity
    GO_0034061 = "GO_0034061"
    DNA_POLYMERASE_ACTIVITY = "GO_0034061"

    # ion transmembrane transport
    GO_0034220 = "GO_0034220"
    ION_TRANSMEMBRANE_TRANSPORT = "GO_0034220"

    # regulation of cellular amide metabolic process
    GO_0034248 = "GO_0034248"
    REGULATION_OF_CELLULAR_AMIDE_METABOLIC_PROCESS = "GO_0034248"

    # negative regulation of cellular amide metabolic process
    GO_0034249 = "GO_0034249"
    NEGATIVE_REGULATION_OF_CELLULAR_AMIDE_METABOLIC_PROCESS = "GO_0034249"

    # positive regulation of cellular amide metabolic process
    GO_0034250 = "GO_0034250"
    POSITIVE_REGULATION_OF_CELLULAR_AMIDE_METABOLIC_PROCESS = "GO_0034250"

    # cellular protein localization
    GO_0034613 = "GO_0034613"
    CELLULAR_PROTEIN_LOCALIZATION = "GO_0034613"

    # cellular nitrogen compound metabolic process
    GO_0034641 = "GO_0034641"
    CELLULAR_NITROGEN_COMPOUND_METABOLIC_PROCESS = "GO_0034641"

    # cellular macromolecule biosynthetic process
    GO_0034645 = "GO_0034645"
    CELLULAR_MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_0034645"

    # nucleobase-containing compound biosynthetic process
    GO_0034654 = "GO_0034654"
    NUCLEOBASE_CONTAINING_COMPOUND_BIOSYNTHETIC_PROCESS = "GO_0034654"

    # nucleobase-containing compound catabolic process
    GO_0034655 = "GO_0034655"
    NUCLEOBASE_CONTAINING_COMPOUND_CATABOLIC_PROCESS = "GO_0034655"

    # ncRNA metabolic process
    GO_0034660 = "GO_0034660"
    NCRNA_METABOLIC_PROCESS = "GO_0034660"

    # methyltransferase complex
    GO_0034708 = "GO_0034708"
    METHYLTRANSFERASE_COMPLEX = "GO_0034708"

    # regulation of transmembrane transport
    GO_0034762 = "GO_0034762"
    REGULATION_OF_TRANSMEMBRANE_TRANSPORT = "GO_0034762"

    # negative regulation of transmembrane transport
    GO_0034763 = "GO_0034763"
    NEGATIVE_REGULATION_OF_TRANSMEMBRANE_TRANSPORT = "GO_0034763"

    # positive regulation of transmembrane transport
    GO_0034764 = "GO_0034764"
    POSITIVE_REGULATION_OF_TRANSMEMBRANE_TRANSPORT = "GO_0034764"

    # regulation of ion transmembrane transport
    GO_0034765 = "GO_0034765"
    REGULATION_OF_ION_TRANSMEMBRANE_TRANSPORT = "GO_0034765"

    # negative regulation of ion transmembrane transport
    GO_0034766 = "GO_0034766"
    NEGATIVE_REGULATION_OF_ION_TRANSMEMBRANE_TRANSPORT = "GO_0034766"

    # positive regulation of ion transmembrane transport
    GO_0034767 = "GO_0034767"
    POSITIVE_REGULATION_OF_ION_TRANSMEMBRANE_TRANSPORT = "GO_0034767"

    # posttranscriptional gene silencing by RNA
    GO_0035194 = "GO_0035194"
    POSTTRANSCRIPTIONAL_GENE_SILENCING_BY_RNA = "GO_0035194"

    # establishment of protein localization to extracellular region
    GO_0035592 = "GO_0035592"
    ESTABLISHMENT_OF_PROTEIN_LOCALIZATION_TO_EXTRACELLULAR_REGION = "GO_0035592"

    # cellular response to drug
    GO_0035690 = "GO_0035690"
    CELLULAR_RESPONSE_TO_DRUG = "GO_0035690"

    # small molecule binding
    GO_0036094 = "GO_0036094"
    SMALL_MOLECULE_BINDING = "GO_0036094"

    # cellular response to mycotoxin
    GO_0036146 = "GO_0036146"
    CELLULAR_RESPONSE_TO_MYCOTOXIN = "GO_0036146"

    # growth
    GO_0040007 = "GO_0040007"
    GROWTH = "GO_0040007"

    # regulation of growth
    GO_0040008 = "GO_0040008"
    REGULATION_OF_GROWTH = "GO_0040008"

    # locomotion
    GO_0040011 = "GO_0040011"
    LOCOMOTION = "GO_0040011"

    # regulation of locomotion
    GO_0040012 = "GO_0040012"
    REGULATION_OF_LOCOMOTION = "GO_0040012"

    # negative regulation of locomotion
    GO_0040013 = "GO_0040013"
    NEGATIVE_REGULATION_OF_LOCOMOTION = "GO_0040013"

    # positive regulation of locomotion
    GO_0040017 = "GO_0040017"
    POSITIVE_REGULATION_OF_LOCOMOTION = "GO_0040017"

    # regulation of gene expression, epigenetic
    GO_0040029 = "GO_0040029"
    REGULATION_OF_GENE_EXPRESSION__EPIGENETIC = "GO_0040029"

    # regulation of molecular function, epigenetic
    GO_0040030 = "GO_0040030"
    REGULATION_OF_MOLECULAR_FUNCTION__EPIGENETIC = "GO_0040030"

    # negative regulation of translation, ncRNA-mediated
    GO_0040033 = "GO_0040033"
    NEGATIVE_REGULATION_OF_TRANSLATION__NCRNA_MEDIATED = "GO_0040033"

    # wound healing
    GO_0042060 = "GO_0042060"
    WOUND_HEALING = "GO_0042060"

    # T cell receptor complex
    GO_0042101 = "GO_0042101"
    T_CELL_RECEPTOR_COMPLEX = "GO_0042101"

    # regulation of cell population proliferation
    GO_0042127 = "GO_0042127"
    REGULATION_OF_CELL_POPULATION_PROLIFERATION = "GO_0042127"

    # response to chemical
    GO_0042221 = "GO_0042221"
    RESPONSE_TO_CHEMICAL = "GO_0042221"

    # peptide binding
    GO_0042277 = "GO_0042277"
    PEPTIDE_BINDING = "GO_0042277"

    # taxis
    GO_0042330 = "GO_0042330"
    TAXIS = "GO_0042330"

    # regulation of membrane potential
    GO_0042391 = "GO_0042391"
    REGULATION_OF_MEMBRANE_POTENTIAL = "GO_0042391"

    # response to drug
    GO_0042493 = "GO_0042493"
    RESPONSE_TO_DRUG = "GO_0042493"

    # immunoglobulin complex, circulating
    GO_0042571 = "GO_0042571"
    IMMUNOGLOBULIN_COMPLEX__CIRCULATING = "GO_0042571"

    # DNA polymerase complex
    GO_0042575 = "GO_0042575"
    DNA_POLYMERASE_COMPLEX = "GO_0042575"

    # peptide antigen binding
    GO_0042605 = "GO_0042605"
    PEPTIDE_ANTIGEN_BINDING = "GO_0042605"

    # biofilm formation
    GO_0042710 = "GO_0042710"
    BIOFILM_FORMATION = "GO_0042710"

    # antisense RNA metabolic process
    GO_0042868 = "GO_0042868"
    ANTISENSE_RNA_METABOLIC_PROCESS = "GO_0042868"

    # amide transport
    GO_0042886 = "GO_0042886"
    AMIDE_TRANSPORT = "GO_0042886"

    # regulation of apoptotic process
    GO_0042981 = "GO_0042981"
    REGULATION_OF_APOPTOTIC_PROCESS = "GO_0042981"

    # peptide biosynthetic process
    GO_0043043 = "GO_0043043"
    PEPTIDE_BIOSYNTHETIC_PROCESS = "GO_0043043"

    # positive regulation of apoptotic process
    GO_0043065 = "GO_0043065"
    POSITIVE_REGULATION_OF_APOPTOTIC_PROCESS = "GO_0043065"

    # negative regulation of apoptotic process
    GO_0043066 = "GO_0043066"
    NEGATIVE_REGULATION_OF_APOPTOTIC_PROCESS = "GO_0043066"

    # regulation of programmed cell death
    GO_0043067 = "GO_0043067"
    REGULATION_OF_PROGRAMMED_CELL_DEATH = "GO_0043067"

    # positive regulation of programmed cell death
    GO_0043068 = "GO_0043068"
    POSITIVE_REGULATION_OF_PROGRAMMED_CELL_DEATH = "GO_0043068"

    # negative regulation of programmed cell death
    GO_0043069 = "GO_0043069"
    NEGATIVE_REGULATION_OF_PROGRAMMED_CELL_DEATH = "GO_0043069"

    # positive regulation of catalytic activity
    GO_0043085 = "GO_0043085"
    POSITIVE_REGULATION_OF_CATALYTIC_ACTIVITY = "GO_0043085"

    # negative regulation of catalytic activity
    GO_0043086 = "GO_0043086"
    NEGATIVE_REGULATION_OF_CATALYTIC_ACTIVITY = "GO_0043086"

    # regulation of translation by machinery localization
    GO_0043143 = "GO_0043143"
    REGULATION_OF_TRANSLATION_BY_MACHINERY_LOCALIZATION = "GO_0043143"

    # macromolecule metabolic process
    GO_0043170 = "GO_0043170"
    MACROMOLECULE_METABOLIC_PROCESS = "GO_0043170"

    # regulation of ion transport
    GO_0043269 = "GO_0043269"
    REGULATION_OF_ION_TRANSPORT = "GO_0043269"

    # positive regulation of ion transport
    GO_0043270 = "GO_0043270"
    POSITIVE_REGULATION_OF_ION_TRANSPORT = "GO_0043270"

    # negative regulation of ion transport
    GO_0043271 = "GO_0043271"
    NEGATIVE_REGULATION_OF_ION_TRANSPORT = "GO_0043271"

    # positive regulation of DNA binding
    GO_0043388 = "GO_0043388"
    POSITIVE_REGULATION_OF_DNA_BINDING = "GO_0043388"

    # negative regulation of DNA binding
    GO_0043392 = "GO_0043392"
    NEGATIVE_REGULATION_OF_DNA_BINDING = "GO_0043392"

    # regulation of protein binding
    GO_0043393 = "GO_0043393"
    REGULATION_OF_PROTEIN_BINDING = "GO_0043393"

    # macromolecule modification
    GO_0043412 = "GO_0043412"
    MACROMOLECULE_MODIFICATION = "GO_0043412"

    # macromolecule methylation
    GO_0043414 = "GO_0043414"
    MACROMOLECULE_METHYLATION = "GO_0043414"

    # sequence-specific DNA binding
    GO_0043565 = "GO_0043565"
    SEQUENCE_SPECIFIC_DNA_BINDING = "GO_0043565"

    # cellular amide metabolic process
    GO_0043603 = "GO_0043603"
    CELLULAR_AMIDE_METABOLIC_PROCESS = "GO_0043603"

    # amide biosynthetic process
    GO_0043604 = "GO_0043604"
    AMIDE_BIOSYNTHETIC_PROCESS = "GO_0043604"

    # regulation of multi-organism process
    GO_0043900 = "GO_0043900"
    REGULATION_OF_MULTI_ORGANISM_PROCESS = "GO_0043900"

    # negative regulation of multi-organism process
    GO_0043901 = "GO_0043901"
    NEGATIVE_REGULATION_OF_MULTI_ORGANISM_PROCESS = "GO_0043901"

    # positive regulation of multi-organism process
    GO_0043902 = "GO_0043902"
    POSITIVE_REGULATION_OF_MULTI_ORGANISM_PROCESS = "GO_0043902"

    # regulation of DNA methylation
    GO_0044030 = "GO_0044030"
    REGULATION_OF_DNA_METHYLATION = "GO_0044030"

    # regulation of anion transport
    GO_0044070 = "GO_0044070"
    REGULATION_OF_ANION_TRANSPORT = "GO_0044070"

    # cellular component biogenesis
    GO_0044085 = "GO_0044085"
    CELLULAR_COMPONENT_BIOGENESIS = "GO_0044085"

    # regulation of cellular component biogenesis
    GO_0044087 = "GO_0044087"
    REGULATION_OF_CELLULAR_COMPONENT_BIOGENESIS = "GO_0044087"

    # positive regulation of cellular component biogenesis
    GO_0044089 = "GO_0044089"
    POSITIVE_REGULATION_OF_CELLULAR_COMPONENT_BIOGENESIS = "GO_0044089"

    # negative regulation of molecular function
    GO_0044092 = "GO_0044092"
    NEGATIVE_REGULATION_OF_MOLECULAR_FUNCTION = "GO_0044092"

    # positive regulation of molecular function
    GO_0044093 = "GO_0044093"
    POSITIVE_REGULATION_OF_MOLECULAR_FUNCTION = "GO_0044093"

    # transcription regulatory region DNA binding
    GO_0044212 = "GO_0044212"
    TRANSCRIPTION_REGULATORY_REGION_DNA_BINDING = "GO_0044212"

    # cellular metabolic process
    GO_0044237 = "GO_0044237"
    CELLULAR_METABOLIC_PROCESS = "GO_0044237"

    # primary metabolic process
    GO_0044238 = "GO_0044238"
    PRIMARY_METABOLIC_PROCESS = "GO_0044238"

    # cellular catabolic process
    GO_0044248 = "GO_0044248"
    CELLULAR_CATABOLIC_PROCESS = "GO_0044248"

    # cellular biosynthetic process
    GO_0044249 = "GO_0044249"
    CELLULAR_BIOSYNTHETIC_PROCESS = "GO_0044249"

    # cellular macromolecule metabolic process
    GO_0044260 = "GO_0044260"
    CELLULAR_MACROMOLECULE_METABOLIC_PROCESS = "GO_0044260"

    # cellular macromolecule catabolic process
    GO_0044265 = "GO_0044265"
    CELLULAR_MACROMOLECULE_CATABOLIC_PROCESS = "GO_0044265"

    # cellular protein metabolic process
    GO_0044267 = "GO_0044267"
    CELLULAR_PROTEIN_METABOLIC_PROCESS = "GO_0044267"

    # cellular nitrogen compound catabolic process
    GO_0044270 = "GO_0044270"
    CELLULAR_NITROGEN_COMPOUND_CATABOLIC_PROCESS = "GO_0044270"

    # cellular nitrogen compound biosynthetic process
    GO_0044271 = "GO_0044271"
    CELLULAR_NITROGEN_COMPOUND_BIOSYNTHETIC_PROCESS = "GO_0044271"

    # DNA methylation or demethylation
    GO_0044728 = "GO_0044728"
    DNA_METHYLATION_OR_DEMETHYLATION = "GO_0044728"

    # multi-organism cellular process
    GO_0044764 = "GO_0044764"
    MULTI_ORGANISM_CELLULAR_PROCESS = "GO_0044764"

    # translation regulator activity
    GO_0045182 = "GO_0045182"
    TRANSLATION_REGULATOR_ACTIVITY = "GO_0045182"

    # establishment of protein localization
    GO_0045184 = "GO_0045184"
    ESTABLISHMENT_OF_PROTEIN_LOCALIZATION = "GO_0045184"

    # positive regulation of translation
    GO_0045727 = "GO_0045727"
    POSITIVE_REGULATION_OF_TRANSLATION = "GO_0045727"

    # positive regulation of DNA replication
    GO_0045740 = "GO_0045740"
    POSITIVE_REGULATION_OF_DNA_REPLICATION = "GO_0045740"

    # negative regulation of action potential
    GO_0045759 = "GO_0045759"
    NEGATIVE_REGULATION_OF_ACTION_POTENTIAL = "GO_0045759"

    # positive regulation of action potential
    GO_0045760 = "GO_0045760"
    POSITIVE_REGULATION_OF_ACTION_POTENTIAL = "GO_0045760"

    # negative regulation of transcription, DNA-templated
    GO_0045892 = "GO_0045892"
    NEGATIVE_REGULATION_OF_TRANSCRIPTION__DNA_TEMPLATED = "GO_0045892"

    # positive regulation of transcription, DNA-templated
    GO_0045893 = "GO_0045893"
    POSITIVE_REGULATION_OF_TRANSCRIPTION__DNA_TEMPLATED = "GO_0045893"

    # negative regulation of translational elongation
    GO_0045900 = "GO_0045900"
    NEGATIVE_REGULATION_OF_TRANSLATIONAL_ELONGATION = "GO_0045900"

    # positive regulation of translational elongation
    GO_0045901 = "GO_0045901"
    POSITIVE_REGULATION_OF_TRANSLATIONAL_ELONGATION = "GO_0045901"

    # negative regulation of growth
    GO_0045926 = "GO_0045926"
    NEGATIVE_REGULATION_OF_GROWTH = "GO_0045926"

    # positive regulation of growth
    GO_0045927 = "GO_0045927"
    POSITIVE_REGULATION_OF_GROWTH = "GO_0045927"

    # negative regulation of nucleobase-containing compound metabolic process
    GO_0045934 = "GO_0045934"
    NEGATIVE_REGULATION_OF_NUCLEOBASE_CONTAINING_COMPOUND_METABOLIC_PROCESS = (
        "GO_0045934"
    )

    # positive regulation of nucleobase-containing compound metabolic process
    GO_0045935 = "GO_0045935"
    POSITIVE_REGULATION_OF_NUCLEOBASE_CONTAINING_COMPOUND_METABOLIC_PROCESS = (
        "GO_0045935"
    )

    # regulation of translation, ncRNA-mediated
    GO_0045974 = "GO_0045974"
    REGULATION_OF_TRANSLATION__NCRNA_MEDIATED = "GO_0045974"

    # heterocycle metabolic process
    GO_0046483 = "GO_0046483"
    HETEROCYCLE_METABOLIC_PROCESS = "GO_0046483"

    # response to antibiotic
    GO_0046677 = "GO_0046677"
    RESPONSE_TO_ANTIBIOTIC = "GO_0046677"

    # heterocycle catabolic process
    GO_0046700 = "GO_0046700"
    HETEROCYCLE_CATABOLIC_PROCESS = "GO_0046700"

    # acid secretion
    GO_0046717 = "GO_0046717"
    ACID_SECRETION = "GO_0046717"

    # secretion
    GO_0046903 = "GO_0046903"
    SECRETION = "GO_0046903"

    # carboxylic acid transport
    GO_0046942 = "GO_0046942"
    CARBOXYLIC_ACID_TRANSPORT = "GO_0046942"

    # positive regulation of biological process
    GO_0048518 = "GO_0048518"
    POSITIVE_REGULATION_OF_BIOLOGICAL_PROCESS = "GO_0048518"

    # negative regulation of biological process
    GO_0048519 = "GO_0048519"
    NEGATIVE_REGULATION_OF_BIOLOGICAL_PROCESS = "GO_0048519"

    # positive regulation of cellular process
    GO_0048522 = "GO_0048522"
    POSITIVE_REGULATION_OF_CELLULAR_PROCESS = "GO_0048522"

    # negative regulation of cellular process
    GO_0048523 = "GO_0048523"
    NEGATIVE_REGULATION_OF_CELLULAR_PROCESS = "GO_0048523"

    # anatomical structure arrangement
    GO_0048532 = "GO_0048532"
    ANATOMICAL_STRUCTURE_ARRANGEMENT = "GO_0048532"

    # regulation of response to stimulus
    GO_0048583 = "GO_0048583"
    REGULATION_OF_RESPONSE_TO_STIMULUS = "GO_0048583"

    # positive regulation of response to stimulus
    GO_0048584 = "GO_0048584"
    POSITIVE_REGULATION_OF_RESPONSE_TO_STIMULUS = "GO_0048584"

    # negative regulation of response to stimulus
    GO_0048585 = "GO_0048585"
    NEGATIVE_REGULATION_OF_RESPONSE_TO_STIMULUS = "GO_0048585"

    # anatomical structure formation involved in morphogenesis
    GO_0048646 = "GO_0048646"
    ANATOMICAL_STRUCTURE_FORMATION_INVOLVED_IN_MORPHOGENESIS = "GO_0048646"

    # anatomical structure development
    GO_0048856 = "GO_0048856"
    ANATOMICAL_STRUCTURE_DEVELOPMENT = "GO_0048856"

    # cellular developmental process
    GO_0048869 = "GO_0048869"
    CELLULAR_DEVELOPMENTAL_PROCESS = "GO_0048869"

    # cell motility
    GO_0048870 = "GO_0048870"
    CELL_MOTILITY = "GO_0048870"

    # arachidonic acid secretion
    GO_0050482 = "GO_0050482"
    ARACHIDONIC_ACID_SECRETION = "GO_0050482"

    # cytokine secretion
    GO_0050663 = "GO_0050663"
    CYTOKINE_SECRETION = "GO_0050663"

    # regulation of cytokine secretion
    GO_0050707 = "GO_0050707"
    REGULATION_OF_CYTOKINE_SECRETION = "GO_0050707"

    # regulation of protein secretion
    GO_0050708 = "GO_0050708"
    REGULATION_OF_PROTEIN_SECRETION = "GO_0050708"

    # negative regulation of protein secretion
    GO_0050709 = "GO_0050709"
    NEGATIVE_REGULATION_OF_PROTEIN_SECRETION = "GO_0050709"

    # negative regulation of cytokine secretion
    GO_0050710 = "GO_0050710"
    NEGATIVE_REGULATION_OF_CYTOKINE_SECRETION = "GO_0050710"

    # positive regulation of protein secretion
    GO_0050714 = "GO_0050714"
    POSITIVE_REGULATION_OF_PROTEIN_SECRETION = "GO_0050714"

    # positive regulation of cytokine secretion
    GO_0050715 = "GO_0050715"
    POSITIVE_REGULATION_OF_CYTOKINE_SECRETION = "GO_0050715"

    # regulation of biological process
    GO_0050789 = "GO_0050789"
    REGULATION_OF_BIOLOGICAL_PROCESS = "GO_0050789"

    # regulation of catalytic activity
    GO_0050790 = "GO_0050790"
    REGULATION_OF_CATALYTIC_ACTIVITY = "GO_0050790"

    # regulation of developmental process
    GO_0050793 = "GO_0050793"
    REGULATION_OF_DEVELOPMENTAL_PROCESS = "GO_0050793"

    # regulation of cellular process
    GO_0050794 = "GO_0050794"
    REGULATION_OF_CELLULAR_PROCESS = "GO_0050794"

    # response to stimulus
    GO_0050896 = "GO_0050896"
    RESPONSE_TO_STIMULUS = "GO_0050896"

    # regulation of chemotaxis
    GO_0050920 = "GO_0050920"
    REGULATION_OF_CHEMOTAXIS = "GO_0050920"

    # positive regulation of chemotaxis
    GO_0050921 = "GO_0050921"
    POSITIVE_REGULATION_OF_CHEMOTAXIS = "GO_0050921"

    # negative regulation of chemotaxis
    GO_0050922 = "GO_0050922"
    NEGATIVE_REGULATION_OF_CHEMOTAXIS = "GO_0050922"

    # regulation of secretion
    GO_0051046 = "GO_0051046"
    REGULATION_OF_SECRETION = "GO_0051046"

    # positive regulation of secretion
    GO_0051047 = "GO_0051047"
    POSITIVE_REGULATION_OF_SECRETION = "GO_0051047"

    # negative regulation of secretion
    GO_0051048 = "GO_0051048"
    NEGATIVE_REGULATION_OF_SECRETION = "GO_0051048"

    # regulation of transport
    GO_0051049 = "GO_0051049"
    REGULATION_OF_TRANSPORT = "GO_0051049"

    # positive regulation of transport
    GO_0051050 = "GO_0051050"
    POSITIVE_REGULATION_OF_TRANSPORT = "GO_0051050"

    # negative regulation of transport
    GO_0051051 = "GO_0051051"
    NEGATIVE_REGULATION_OF_TRANSPORT = "GO_0051051"

    # regulation of DNA metabolic process
    GO_0051052 = "GO_0051052"
    REGULATION_OF_DNA_METABOLIC_PROCESS = "GO_0051052"

    # negative regulation of DNA metabolic process
    GO_0051053 = "GO_0051053"
    NEGATIVE_REGULATION_OF_DNA_METABOLIC_PROCESS = "GO_0051053"

    # positive regulation of DNA metabolic process
    GO_0051054 = "GO_0051054"
    POSITIVE_REGULATION_OF_DNA_METABOLIC_PROCESS = "GO_0051054"

    # negative regulation of developmental process
    GO_0051093 = "GO_0051093"
    NEGATIVE_REGULATION_OF_DEVELOPMENTAL_PROCESS = "GO_0051093"

    # positive regulation of developmental process
    GO_0051094 = "GO_0051094"
    POSITIVE_REGULATION_OF_DEVELOPMENTAL_PROCESS = "GO_0051094"

    # regulation of binding
    GO_0051098 = "GO_0051098"
    REGULATION_OF_BINDING = "GO_0051098"

    # positive regulation of binding
    GO_0051099 = "GO_0051099"
    POSITIVE_REGULATION_OF_BINDING = "GO_0051099"

    # negative regulation of binding
    GO_0051100 = "GO_0051100"
    NEGATIVE_REGULATION_OF_BINDING = "GO_0051100"

    # regulation of DNA binding
    GO_0051101 = "GO_0051101"
    REGULATION_OF_DNA_BINDING = "GO_0051101"

    # regulation of cellular component organization
    GO_0051128 = "GO_0051128"
    REGULATION_OF_CELLULAR_COMPONENT_ORGANIZATION = "GO_0051128"

    # negative regulation of cellular component organization
    GO_0051129 = "GO_0051129"
    NEGATIVE_REGULATION_OF_CELLULAR_COMPONENT_ORGANIZATION = "GO_0051129"

    # positive regulation of cellular component organization
    GO_0051130 = "GO_0051130"
    POSITIVE_REGULATION_OF_CELLULAR_COMPONENT_ORGANIZATION = "GO_0051130"

    # regulation of nitrogen compound metabolic process
    GO_0051171 = "GO_0051171"
    REGULATION_OF_NITROGEN_COMPOUND_METABOLIC_PROCESS = "GO_0051171"

    # negative regulation of nitrogen compound metabolic process
    GO_0051172 = "GO_0051172"
    NEGATIVE_REGULATION_OF_NITROGEN_COMPOUND_METABOLIC_PROCESS = "GO_0051172"

    # positive regulation of nitrogen compound metabolic process
    GO_0051173 = "GO_0051173"
    POSITIVE_REGULATION_OF_NITROGEN_COMPOUND_METABOLIC_PROCESS = "GO_0051173"

    # localization
    GO_0051179 = "GO_0051179"
    LOCALIZATION = "GO_0051179"

    # positive regulation of protein transport
    GO_0051222 = "GO_0051222"
    POSITIVE_REGULATION_OF_PROTEIN_TRANSPORT = "GO_0051222"

    # regulation of protein transport
    GO_0051223 = "GO_0051223"
    REGULATION_OF_PROTEIN_TRANSPORT = "GO_0051223"

    # negative regulation of protein transport
    GO_0051224 = "GO_0051224"
    NEGATIVE_REGULATION_OF_PROTEIN_TRANSPORT = "GO_0051224"

    # establishment of localization
    GO_0051234 = "GO_0051234"
    ESTABLISHMENT_OF_LOCALIZATION = "GO_0051234"

    # regulation of multicellular organismal process
    GO_0051239 = "GO_0051239"
    REGULATION_OF_MULTICELLULAR_ORGANISMAL_PROCESS = "GO_0051239"

    # positive regulation of multicellular organismal process
    GO_0051240 = "GO_0051240"
    POSITIVE_REGULATION_OF_MULTICELLULAR_ORGANISMAL_PROCESS = "GO_0051240"

    # negative regulation of multicellular organismal process
    GO_0051241 = "GO_0051241"
    NEGATIVE_REGULATION_OF_MULTICELLULAR_ORGANISMAL_PROCESS = "GO_0051241"

    # regulation of protein metabolic process
    GO_0051246 = "GO_0051246"
    REGULATION_OF_PROTEIN_METABOLIC_PROCESS = "GO_0051246"

    # positive regulation of protein metabolic process
    GO_0051247 = "GO_0051247"
    POSITIVE_REGULATION_OF_PROTEIN_METABOLIC_PROCESS = "GO_0051247"

    # negative regulation of protein metabolic process
    GO_0051248 = "GO_0051248"
    NEGATIVE_REGULATION_OF_PROTEIN_METABOLIC_PROCESS = "GO_0051248"

    # regulation of RNA metabolic process
    GO_0051252 = "GO_0051252"
    REGULATION_OF_RNA_METABOLIC_PROCESS = "GO_0051252"

    # negative regulation of RNA metabolic process
    GO_0051253 = "GO_0051253"
    NEGATIVE_REGULATION_OF_RNA_METABOLIC_PROCESS = "GO_0051253"

    # positive regulation of RNA metabolic process
    GO_0051254 = "GO_0051254"
    POSITIVE_REGULATION_OF_RNA_METABOLIC_PROCESS = "GO_0051254"

    # regulation of cellular component movement
    GO_0051270 = "GO_0051270"
    REGULATION_OF_CELLULAR_COMPONENT_MOVEMENT = "GO_0051270"

    # negative regulation of cellular component movement
    GO_0051271 = "GO_0051271"
    NEGATIVE_REGULATION_OF_CELLULAR_COMPONENT_MOVEMENT = "GO_0051271"

    # positive regulation of cellular component movement
    GO_0051272 = "GO_0051272"
    POSITIVE_REGULATION_OF_CELLULAR_COMPONENT_MOVEMENT = "GO_0051272"

    # chromosome organization
    GO_0051276 = "GO_0051276"
    CHROMOSOME_ORGANIZATION = "GO_0051276"

    # regulation of hydrolase activity
    GO_0051336 = "GO_0051336"
    REGULATION_OF_HYDROLASE_ACTIVITY = "GO_0051336"

    # positive regulation of hydrolase activity
    GO_0051345 = "GO_0051345"
    POSITIVE_REGULATION_OF_HYDROLASE_ACTIVITY = "GO_0051345"

    # negative regulation of hydrolase activity
    GO_0051346 = "GO_0051346"
    NEGATIVE_REGULATION_OF_HYDROLASE_ACTIVITY = "GO_0051346"

    # cellular localization
    GO_0051641 = "GO_0051641"
    CELLULAR_LOCALIZATION = "GO_0051641"

    # localization of cell
    GO_0051674 = "GO_0051674"
    LOCALIZATION_OF_CELL = "GO_0051674"

    # multi-organism process
    GO_0051704 = "GO_0051704"
    MULTI_ORGANISM_PROCESS = "GO_0051704"

    # cellular response to stimulus
    GO_0051716 = "GO_0051716"
    CELLULAR_RESPONSE_TO_STIMULUS = "GO_0051716"

    # transmembrane transport
    GO_0055085 = "GO_0055085"
    TRANSMEMBRANE_TRANSPORT = "GO_0055085"

    # regulation of posttranscriptional gene silencing
    GO_0060147 = "GO_0060147"
    REGULATION_OF_POSTTRANSCRIPTIONAL_GENE_SILENCING = "GO_0060147"

    # positive regulation of posttranscriptional gene silencing
    GO_0060148 = "GO_0060148"
    POSITIVE_REGULATION_OF_POSTTRANSCRIPTIONAL_GENE_SILENCING = "GO_0060148"

    # negative regulation of posttranscriptional gene silencing
    GO_0060149 = "GO_0060149"
    NEGATIVE_REGULATION_OF_POSTTRANSCRIPTIONAL_GENE_SILENCING = "GO_0060149"

    # regulation of antisense RNA transcription
    GO_0060194 = "GO_0060194"
    REGULATION_OF_ANTISENSE_RNA_TRANSCRIPTION = "GO_0060194"

    # negative regulation of antisense RNA transcription
    GO_0060195 = "GO_0060195"
    NEGATIVE_REGULATION_OF_ANTISENSE_RNA_TRANSCRIPTION = "GO_0060195"

    # positive regulation of antisense RNA transcription
    GO_0060196 = "GO_0060196"
    POSITIVE_REGULATION_OF_ANTISENSE_RNA_TRANSCRIPTION = "GO_0060196"

    # regulation of macromolecule metabolic process
    GO_0060255 = "GO_0060255"
    REGULATION_OF_MACROMOLECULE_METABOLIC_PROCESS = "GO_0060255"

    # cell chemotaxis
    GO_0060326 = "GO_0060326"
    CELL_CHEMOTAXIS = "GO_0060326"

    # regulation of cellular localization
    GO_0060341 = "GO_0060341"
    REGULATION_OF_CELLULAR_LOCALIZATION = "GO_0060341"

    # cell adhesion molecule production
    GO_0060352 = "GO_0060352"
    CELL_ADHESION_MOLECULE_PRODUCTION = "GO_0060352"

    # regulation of cell adhesion molecule production
    GO_0060353 = "GO_0060353"
    REGULATION_OF_CELL_ADHESION_MOLECULE_PRODUCTION = "GO_0060353"

    # negative regulation of cell adhesion molecule production
    GO_0060354 = "GO_0060354"
    NEGATIVE_REGULATION_OF_CELL_ADHESION_MOLECULE_PRODUCTION = "GO_0060354"

    # positive regulation of cell adhesion molecule production
    GO_0060355 = "GO_0060355"
    POSITIVE_REGULATION_OF_CELL_ADHESION_MOLECULE_PRODUCTION = "GO_0060355"

    # regulation of cell projection assembly
    GO_0060491 = "GO_0060491"
    REGULATION_OF_CELL_PROJECTION_ASSEMBLY = "GO_0060491"

    # negative regulation of cell death
    GO_0060548 = "GO_0060548"
    NEGATIVE_REGULATION_OF_CELL_DEATH = "GO_0060548"

    # apoptotic process involved in morphogenesis
    GO_0060561 = "GO_0060561"
    APOPTOTIC_PROCESS_INVOLVED_IN_MORPHOGENESIS = "GO_0060561"

    # regulation of gene silencing by RNA
    GO_0060966 = "GO_0060966"
    REGULATION_OF_GENE_SILENCING_BY_RNA = "GO_0060966"

    # negative regulation of gene silencing by RNA
    GO_0060967 = "GO_0060967"
    NEGATIVE_REGULATION_OF_GENE_SILENCING_BY_RNA = "GO_0060967"

    # regulation of gene silencing
    GO_0060968 = "GO_0060968"
    REGULATION_OF_GENE_SILENCING = "GO_0060968"

    # negative regulation of gene silencing
    GO_0060969 = "GO_0060969"
    NEGATIVE_REGULATION_OF_GENE_SILENCING = "GO_0060969"

    # regulation of wound healing
    GO_0061041 = "GO_0061041"
    REGULATION_OF_WOUND_HEALING = "GO_0061041"

    # negative regulation of wound healing
    GO_0061045 = "GO_0061045"
    NEGATIVE_REGULATION_OF_WOUND_HEALING = "GO_0061045"

    # response to platelet aggregation inhibitor
    GO_0061478 = "GO_0061478"
    RESPONSE_TO_PLATELET_AGGREGATION_INHIBITOR = "GO_0061478"

    # biological regulation
    GO_0065007 = "GO_0065007"
    BIOLOGICAL_REGULATION = "GO_0065007"

    # regulation of biological quality
    GO_0065008 = "GO_0065008"
    REGULATION_OF_BIOLOGICAL_QUALITY = "GO_0065008"

    # regulation of molecular function
    GO_0065009 = "GO_0065009"
    REGULATION_OF_MOLECULAR_FUNCTION = "GO_0065009"

    # regulation of establishment of protein localization
    GO_0070201 = "GO_0070201"
    REGULATION_OF_ESTABLISHMENT_OF_PROTEIN_LOCALIZATION = "GO_0070201"

    # negative regulation of translation involved in RNA interference
    GO_0070549 = "GO_0070549"
    NEGATIVE_REGULATION_OF_TRANSLATION_INVOLVED_IN_RNA_INTERFERENCE = "GO_0070549"

    # cellular macromolecule localization
    GO_0070727 = "GO_0070727"
    CELLULAR_MACROMOLECULE_LOCALIZATION = "GO_0070727"

    # cellular response to chemical stimulus
    GO_0070887 = "GO_0070887"
    CELLULAR_RESPONSE_TO_CHEMICAL_STIMULUS = "GO_0070887"

    # cellular response to organic substance
    GO_0071310 = "GO_0071310"
    CELLULAR_RESPONSE_TO_ORGANIC_SUBSTANCE = "GO_0071310"

    # cellular response to organic cyclic compound
    GO_0071407 = "GO_0071407"
    CELLULAR_RESPONSE_TO_ORGANIC_CYCLIC_COMPOUND = "GO_0071407"

    # cellular response to organonitrogen compound
    GO_0071417 = "GO_0071417"
    CELLULAR_RESPONSE_TO_ORGANONITROGEN_COMPOUND = "GO_0071417"

    # cellular response to endogenous stimulus
    GO_0071495 = "GO_0071495"
    CELLULAR_RESPONSE_TO_ENDOGENOUS_STIMULUS = "GO_0071495"

    # protein localization to extracellular region
    GO_0071692 = "GO_0071692"
    PROTEIN_LOCALIZATION_TO_EXTRACELLULAR_REGION = "GO_0071692"

    # organic substance transport
    GO_0071702 = "GO_0071702"
    ORGANIC_SUBSTANCE_TRANSPORT = "GO_0071702"

    # organic substance metabolic process
    GO_0071704 = "GO_0071704"
    ORGANIC_SUBSTANCE_METABOLIC_PROCESS = "GO_0071704"

    # nitrogen compound transport
    GO_0071705 = "GO_0071705"
    NITROGEN_COMPOUND_TRANSPORT = "GO_0071705"

    # tumor necrosis factor superfamily cytokine production
    GO_0071706 = "GO_0071706"
    TUMOR_NECROSIS_FACTOR_SUPERFAMILY_CYTOKINE_PRODUCTION = "GO_0071706"

    # icosanoid transport
    GO_0071715 = "GO_0071715"
    ICOSANOID_TRANSPORT = "GO_0071715"

    # cellular component organization or biogenesis
    GO_0071840 = "GO_0071840"
    CELLULAR_COMPONENT_ORGANIZATION_OR_BIOGENESIS = "GO_0071840"

    # DNA biosynthetic process
    GO_0071897 = "GO_0071897"
    DNA_BIOSYNTHETIC_PROCESS = "GO_0071897"

    # cellular response to cytochalasin B
    GO_0072749 = "GO_0072749"
    CELLULAR_RESPONSE_TO_CYTOCHALASIN_B = "GO_0072749"

    # regulation of primary metabolic process
    GO_0080090 = "GO_0080090"
    REGULATION_OF_PRIMARY_METABOLIC_PROCESS = "GO_0080090"

    # regulation of response to stress
    GO_0080134 = "GO_0080134"
    REGULATION_OF_RESPONSE_TO_STRESS = "GO_0080134"

    # regulation of cellular response to stress
    GO_0080135 = "GO_0080135"
    REGULATION_OF_CELLULAR_RESPONSE_TO_STRESS = "GO_0080135"

    # regulation of peptide transport
    GO_0090087 = "GO_0090087"
    REGULATION_OF_PEPTIDE_TRANSPORT = "GO_0090087"

    # regulation of arachidonic acid secretion
    GO_0090237 = "GO_0090237"
    REGULATION_OF_ARACHIDONIC_ACID_SECRETION = "GO_0090237"

    # positive regulation of arachidonic acid secretion
    GO_0090238 = "GO_0090238"
    POSITIVE_REGULATION_OF_ARACHIDONIC_ACID_SECRETION = "GO_0090238"

    # positive regulation of wound healing
    GO_0090303 = "GO_0090303"
    POSITIVE_REGULATION_OF_WOUND_HEALING = "GO_0090303"

    # nucleic acid metabolic process
    GO_0090304 = "GO_0090304"
    NUCLEIC_ACID_METABOLIC_PROCESS = "GO_0090304"

    # nucleic acid phosphodiester bond hydrolysis
    GO_0090305 = "GO_0090305"
    NUCLEIC_ACID_PHOSPHODIESTER_BOND_HYDROLYSIS = "GO_0090305"

    # regulation of cell aging
    GO_0090342 = "GO_0090342"
    REGULATION_OF_CELL_AGING = "GO_0090342"

    # positive regulation of cell aging
    GO_0090343 = "GO_0090343"
    POSITIVE_REGULATION_OF_CELL_AGING = "GO_0090343"

    # negative regulation of cell aging
    GO_0090344 = "GO_0090344"
    NEGATIVE_REGULATION_OF_CELL_AGING = "GO_0090344"

    # DNA synthesis involved in DNA replication
    GO_0090592 = "GO_0090592"
    DNA_SYNTHESIS_INVOLVED_IN_DNA_REPLICATION = "GO_0090592"

    # organic cyclic compound binding
    GO_0097159 = "GO_0097159"
    ORGANIC_CYCLIC_COMPOUND_BINDING = "GO_0097159"

    # execution phase of apoptosis
    GO_0097194 = "GO_0097194"
    EXECUTION_PHASE_OF_APOPTOSIS = "GO_0097194"

    # cellular response to toxic substance
    GO_0097237 = "GO_0097237"
    CELLULAR_RESPONSE_TO_TOXIC_SUBSTANCE = "GO_0097237"

    # carbohydrate derivative binding
    GO_0097367 = "GO_0097367"
    CARBOHYDRATE_DERIVATIVE_BINDING = "GO_0097367"

    # neuron part
    GO_0097458 = "GO_0097458"
    NEURON_PART = "GO_0097458"

    # nucleic acid-templated transcription
    GO_0097659 = "GO_0097659"
    NUCLEIC_ACID_TEMPLATED_TRANSCRIPTION = "GO_0097659"

    # regulation of action potential
    GO_0098900 = "GO_0098900"
    REGULATION_OF_ACTION_POTENTIAL = "GO_0098900"

    # plasma membrane bounded cell projection assembly
    GO_0120031 = "GO_0120031"
    PLASMA_MEMBRANE_BOUNDED_CELL_PROJECTION_ASSEMBLY = "GO_0120031"

    # regulation of plasma membrane bounded cell projection assembly
    GO_0120032 = "GO_0120032"
    REGULATION_OF_PLASMA_MEMBRANE_BOUNDED_CELL_PROJECTION_ASSEMBLY = "GO_0120032"

    # negative regulation of plasma membrane bounded cell projection assembly
    GO_0120033 = "GO_0120033"
    NEGATIVE_REGULATION_OF_PLASMA_MEMBRANE_BOUNDED_CELL_PROJECTION_ASSEMBLY = (
        "GO_0120033"
    )

    # positive regulation of plasma membrane bounded cell projection assembly
    GO_0120034 = "GO_0120034"
    POSITIVE_REGULATION_OF_PLASMA_MEMBRANE_BOUNDED_CELL_PROJECTION_ASSEMBLY = (
        "GO_0120034"
    )

    # regulation of plasma membrane bounded cell projection organization
    GO_0120035 = "GO_0120035"
    REGULATION_OF_PLASMA_MEMBRANE_BOUNDED_CELL_PROJECTION_ORGANIZATION = "GO_0120035"

    # plasma membrane bounded cell projection organization
    GO_0120036 = "GO_0120036"
    PLASMA_MEMBRANE_BOUNDED_CELL_PROJECTION_ORGANIZATION = "GO_0120036"

    # catalytic activity, acting on DNA
    GO_0140097 = "GO_0140097"
    CATALYTIC_ACTIVITY__ACTING_ON_DNA = "GO_0140097"

    # export from cell
    GO_0140352 = "GO_0140352"
    EXPORT_FROM_CELL = "GO_0140352"

    # regulation of execution phase of apoptosis
    GO_1900117 = "GO_1900117"
    REGULATION_OF_EXECUTION_PHASE_OF_APOPTOSIS = "GO_1900117"

    # negative regulation of execution phase of apoptosis
    GO_1900118 = "GO_1900118"
    NEGATIVE_REGULATION_OF_EXECUTION_PHASE_OF_APOPTOSIS = "GO_1900118"

    # positive regulation of execution phase of apoptosis
    GO_1900119 = "GO_1900119"
    POSITIVE_REGULATION_OF_EXECUTION_PHASE_OF_APOPTOSIS = "GO_1900119"

    # regulation of lipid binding
    GO_1900130 = "GO_1900130"
    REGULATION_OF_LIPID_BINDING = "GO_1900130"

    # negative regulation of lipid binding
    GO_1900131 = "GO_1900131"
    NEGATIVE_REGULATION_OF_LIPID_BINDING = "GO_1900131"

    # positive regulation of lipid binding
    GO_1900132 = "GO_1900132"
    POSITIVE_REGULATION_OF_LIPID_BINDING = "GO_1900132"

    # negative regulation of arachidonic acid secretion
    GO_1900139 = "GO_1900139"
    NEGATIVE_REGULATION_OF_ARACHIDONIC_ACID_SECRETION = "GO_1900139"

    # regulation of RNA interference
    GO_1900368 = "GO_1900368"
    REGULATION_OF_RNA_INTERFERENCE = "GO_1900368"

    # negative regulation of RNA interference
    GO_1900369 = "GO_1900369"
    NEGATIVE_REGULATION_OF_RNA_INTERFERENCE = "GO_1900369"

    # positive regulation of RNA interference
    GO_1900370 = "GO_1900370"
    POSITIVE_REGULATION_OF_RNA_INTERFERENCE = "GO_1900370"

    # response to cytochalasin B
    GO_1901328 = "GO_1901328"
    RESPONSE_TO_CYTOCHALASIN_B = "GO_1901328"

    # organic cyclic compound metabolic process
    GO_1901360 = "GO_1901360"
    ORGANIC_CYCLIC_COMPOUND_METABOLIC_PROCESS = "GO_1901360"

    # organic cyclic compound catabolic process
    GO_1901361 = "GO_1901361"
    ORGANIC_CYCLIC_COMPOUND_CATABOLIC_PROCESS = "GO_1901361"

    # organic cyclic compound biosynthetic process
    GO_1901362 = "GO_1901362"
    ORGANIC_CYCLIC_COMPOUND_BIOSYNTHETIC_PROCESS = "GO_1901362"

    # heterocyclic compound binding
    GO_1901363 = "GO_1901363"
    HETEROCYCLIC_COMPOUND_BINDING = "GO_1901363"

    # organonitrogen compound metabolic process
    GO_1901564 = "GO_1901564"
    ORGANONITROGEN_COMPOUND_METABOLIC_PROCESS = "GO_1901564"

    # organonitrogen compound biosynthetic process
    GO_1901566 = "GO_1901566"
    ORGANONITROGEN_COMPOUND_BIOSYNTHETIC_PROCESS = "GO_1901566"

    # fatty acid derivative transport
    GO_1901571 = "GO_1901571"
    FATTY_ACID_DERIVATIVE_TRANSPORT = "GO_1901571"

    # organic substance catabolic process
    GO_1901575 = "GO_1901575"
    ORGANIC_SUBSTANCE_CATABOLIC_PROCESS = "GO_1901575"

    # organic substance biosynthetic process
    GO_1901576 = "GO_1901576"
    ORGANIC_SUBSTANCE_BIOSYNTHETIC_PROCESS = "GO_1901576"

    # response to nitrogen compound
    GO_1901698 = "GO_1901698"
    RESPONSE_TO_NITROGEN_COMPOUND = "GO_1901698"

    # cellular response to nitrogen compound
    GO_1901699 = "GO_1901699"
    CELLULAR_RESPONSE_TO_NITROGEN_COMPOUND = "GO_1901699"

    # response to oxygen-containing compound
    GO_1901700 = "GO_1901700"
    RESPONSE_TO_OXYGEN_CONTAINING_COMPOUND = "GO_1901700"

    # cellular response to oxygen-containing compound
    GO_1901701 = "GO_1901701"
    CELLULAR_RESPONSE_TO_OXYGEN_CONTAINING_COMPOUND = "GO_1901701"

    # regulation of apoptotic process involved in morphogenesis
    GO_1902337 = "GO_1902337"
    REGULATION_OF_APOPTOTIC_PROCESS_INVOLVED_IN_MORPHOGENESIS = "GO_1902337"

    # negative regulation of apoptotic process involved in morphogenesis
    GO_1902338 = "GO_1902338"
    NEGATIVE_REGULATION_OF_APOPTOTIC_PROCESS_INVOLVED_IN_MORPHOGENESIS = "GO_1902338"

    # positive regulation of apoptotic process involved in morphogenesis
    GO_1902339 = "GO_1902339"
    POSITIVE_REGULATION_OF_APOPTOTIC_PROCESS_INVOLVED_IN_MORPHOGENESIS = "GO_1902339"

    # catalytic complex
    GO_1902494 = "GO_1902494"
    CATALYTIC_COMPLEX = "GO_1902494"

    # regulation of apoptotic DNA fragmentation
    GO_1902510 = "GO_1902510"
    REGULATION_OF_APOPTOTIC_DNA_FRAGMENTATION = "GO_1902510"

    # negative regulation of apoptotic DNA fragmentation
    GO_1902511 = "GO_1902511"
    NEGATIVE_REGULATION_OF_APOPTOTIC_DNA_FRAGMENTATION = "GO_1902511"

    # positive regulation of apoptotic DNA fragmentation
    GO_1902512 = "GO_1902512"
    POSITIVE_REGULATION_OF_APOPTOTIC_DNA_FRAGMENTATION = "GO_1902512"

    # negative regulation of RNA biosynthetic process
    GO_1902679 = "GO_1902679"
    NEGATIVE_REGULATION_OF_RNA_BIOSYNTHETIC_PROCESS = "GO_1902679"

    # positive regulation of RNA biosynthetic process
    GO_1902680 = "GO_1902680"
    POSITIVE_REGULATION_OF_RNA_BIOSYNTHETIC_PROCESS = "GO_1902680"

    # apoptotic process involved in development
    GO_1902742 = "GO_1902742"
    APOPTOTIC_PROCESS_INVOLVED_IN_DEVELOPMENT = "GO_1902742"

    # regulation of response to wounding
    GO_1903034 = "GO_1903034"
    REGULATION_OF_RESPONSE_TO_WOUNDING = "GO_1903034"

    # negative regulation of response to wounding
    GO_1903035 = "GO_1903035"
    NEGATIVE_REGULATION_OF_RESPONSE_TO_WOUNDING = "GO_1903035"

    # positive regulation of response to wounding
    GO_1903036 = "GO_1903036"
    POSITIVE_REGULATION_OF_RESPONSE_TO_WOUNDING = "GO_1903036"

    # regulation of nucleus organization
    GO_1903353 = "GO_1903353"
    REGULATION_OF_NUCLEUS_ORGANIZATION = "GO_1903353"

    # regulation of nucleic acid-templated transcription
    GO_1903506 = "GO_1903506"
    REGULATION_OF_NUCLEIC_ACID_TEMPLATED_TRANSCRIPTION = "GO_1903506"

    # negative regulation of nucleic acid-templated transcription
    GO_1903507 = "GO_1903507"
    NEGATIVE_REGULATION_OF_NUCLEIC_ACID_TEMPLATED_TRANSCRIPTION = "GO_1903507"

    # positive regulation of nucleic acid-templated transcription
    GO_1903508 = "GO_1903508"
    POSITIVE_REGULATION_OF_NUCLEIC_ACID_TEMPLATED_TRANSCRIPTION = "GO_1903508"

    # regulation of secretion by cell
    GO_1903530 = "GO_1903530"
    REGULATION_OF_SECRETION_BY_CELL = "GO_1903530"

    # negative regulation of secretion by cell
    GO_1903531 = "GO_1903531"
    NEGATIVE_REGULATION_OF_SECRETION_BY_CELL = "GO_1903531"

    # positive regulation of secretion by cell
    GO_1903532 = "GO_1903532"
    POSITIVE_REGULATION_OF_SECRETION_BY_CELL = "GO_1903532"

    # regulation of tumor necrosis factor superfamily cytokine production
    GO_1903555 = "GO_1903555"
    REGULATION_OF_TUMOR_NECROSIS_FACTOR_SUPERFAMILY_CYTOKINE_PRODUCTION = "GO_1903555"

    # negative regulation of tumor necrosis factor superfamily cytokine production
    GO_1903556 = "GO_1903556"
    NEGATIVE_REGULATION_OF_TUMOR_NECROSIS_FACTOR_SUPERFAMILY_CYTOKINE_PRODUCTION = (
        "GO_1903556"
    )

    # positive regulation of tumor necrosis factor superfamily cytokine production
    GO_1903557 = "GO_1903557"
    POSITIVE_REGULATION_OF_TUMOR_NECROSIS_FACTOR_SUPERFAMILY_CYTOKINE_PRODUCTION = (
        "GO_1903557"
    )

    # regulation of DNA catabolic process
    GO_1903624 = "GO_1903624"
    REGULATION_OF_DNA_CATABOLIC_PROCESS = "GO_1903624"

    # negative regulation of DNA catabolic process
    GO_1903625 = "GO_1903625"
    NEGATIVE_REGULATION_OF_DNA_CATABOLIC_PROCESS = "GO_1903625"

    # positive regulation of DNA catabolic process
    GO_1903626 = "GO_1903626"
    POSITIVE_REGULATION_OF_DNA_CATABOLIC_PROCESS = "GO_1903626"

    # negative regulation of anion transport
    GO_1903792 = "GO_1903792"
    NEGATIVE_REGULATION_OF_ANION_TRANSPORT = "GO_1903792"

    # positive regulation of anion transport
    GO_1903793 = "GO_1903793"
    POSITIVE_REGULATION_OF_ANION_TRANSPORT = "GO_1903793"

    # regulation of cellular protein localization
    GO_1903827 = "GO_1903827"
    REGULATION_OF_CELLULAR_PROTEIN_LOCALIZATION = "GO_1903827"

    # negative regulation of cellular protein localization
    GO_1903828 = "GO_1903828"
    NEGATIVE_REGULATION_OF_CELLULAR_PROTEIN_LOCALIZATION = "GO_1903828"

    # positive regulation of cellular protein localization
    GO_1903829 = "GO_1903829"
    POSITIVE_REGULATION_OF_CELLULAR_PROTEIN_LOCALIZATION = "GO_1903829"

    # arachidonate transport
    GO_1903963 = "GO_1903963"
    ARACHIDONATE_TRANSPORT = "GO_1903963"

    # regulation of bleb assembly
    GO_1904170 = "GO_1904170"
    REGULATION_OF_BLEB_ASSEMBLY = "GO_1904170"

    # negative regulation of bleb assembly
    GO_1904171 = "GO_1904171"
    NEGATIVE_REGULATION_OF_BLEB_ASSEMBLY = "GO_1904171"

    # positive regulation of bleb assembly
    GO_1904172 = "GO_1904172"
    POSITIVE_REGULATION_OF_BLEB_ASSEMBLY = "GO_1904172"

    # regulation of tumor necrosis factor secretion
    GO_1904467 = "GO_1904467"
    REGULATION_OF_TUMOR_NECROSIS_FACTOR_SECRETION = "GO_1904467"

    # negative regulation of tumor necrosis factor secretion
    GO_1904468 = "GO_1904468"
    NEGATIVE_REGULATION_OF_TUMOR_NECROSIS_FACTOR_SECRETION = "GO_1904468"

    # positive regulation of tumor necrosis factor secretion
    GO_1904469 = "GO_1904469"
    POSITIVE_REGULATION_OF_TUMOR_NECROSIS_FACTOR_SECRETION = "GO_1904469"

    # negative regulation of apoptotic process involved in development
    GO_1904746 = "GO_1904746"
    NEGATIVE_REGULATION_OF_APOPTOTIC_PROCESS_INVOLVED_IN_DEVELOPMENT = "GO_1904746"

    # positive regulation of apoptotic process involved in development
    GO_1904747 = "GO_1904747"
    POSITIVE_REGULATION_OF_APOPTOTIC_PROCESS_INVOLVED_IN_DEVELOPMENT = "GO_1904747"

    # regulation of apoptotic process involved in development
    GO_1904748 = "GO_1904748"
    REGULATION_OF_APOPTOTIC_PROCESS_INVOLVED_IN_DEVELOPMENT = "GO_1904748"

    # regulation of core promoter binding
    GO_1904796 = "GO_1904796"
    REGULATION_OF_CORE_PROMOTER_BINDING = "GO_1904796"

    # negative regulation of core promoter binding
    GO_1904797 = "GO_1904797"
    NEGATIVE_REGULATION_OF_CORE_PROMOTER_BINDING = "GO_1904797"

    # positive regulation of core promoter binding
    GO_1904798 = "GO_1904798"
    POSITIVE_REGULATION_OF_CORE_PROMOTER_BINDING = "GO_1904798"

    # negative regulation of establishment of protein localization
    GO_1904950 = "GO_1904950"
    NEGATIVE_REGULATION_OF_ESTABLISHMENT_OF_PROTEIN_LOCALIZATION = "GO_1904950"

    # positive regulation of establishment of protein localization
    GO_1904951 = "GO_1904951"
    POSITIVE_REGULATION_OF_ESTABLISHMENT_OF_PROTEIN_LOCALIZATION = "GO_1904951"

    # negative regulation of DNA methylation
    GO_1905642 = "GO_1905642"
    NEGATIVE_REGULATION_OF_DNA_METHYLATION = "GO_1905642"

    # positive regulation of DNA methylation
    GO_1905643 = "GO_1905643"
    POSITIVE_REGULATION_OF_DNA_METHYLATION = "GO_1905643"

    # regulation of lipid localization
    GO_1905952 = "GO_1905952"
    REGULATION_OF_LIPID_LOCALIZATION = "GO_1905952"

    # negative regulation of lipid localization
    GO_1905953 = "GO_1905953"
    NEGATIVE_REGULATION_OF_LIPID_LOCALIZATION = "GO_1905953"

    # positive regulation of lipid localization
    GO_1905954 = "GO_1905954"
    POSITIVE_REGULATION_OF_LIPID_LOCALIZATION = "GO_1905954"

    # transferase complex
    GO_1990234 = "GO_1990234"
    TRANSFERASE_COMPLEX = "GO_1990234"

    # tumor necrosis factor secretion
    GO_1990774 = "GO_1990774"
    TUMOR_NECROSIS_FACTOR_SECRETION = "GO_1990774"

    # regulation of cellular macromolecule biosynthetic process
    GO_2000112 = "GO_2000112"
    REGULATION_OF_CELLULAR_MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_2000112"

    # negative regulation of cellular macromolecule biosynthetic process
    GO_2000113 = "GO_2000113"
    NEGATIVE_REGULATION_OF_CELLULAR_MACROMOLECULE_BIOSYNTHETIC_PROCESS = "GO_2000113"

    # regulation of cell motility
    GO_2000145 = "GO_2000145"
    REGULATION_OF_CELL_MOTILITY = "GO_2000145"

    # negative regulation of cell motility
    GO_2000146 = "GO_2000146"
    NEGATIVE_REGULATION_OF_CELL_MOTILITY = "GO_2000146"

    # positive regulation of cell motility
    GO_2000147 = "GO_2000147"
    POSITIVE_REGULATION_OF_CELL_MOTILITY = "GO_2000147"

    # regulation of fatty acid transport
    GO_2000191 = "GO_2000191"
    REGULATION_OF_FATTY_ACID_TRANSPORT = "GO_2000191"

    # negative regulation of fatty acid transport
    GO_2000192 = "GO_2000192"
    NEGATIVE_REGULATION_OF_FATTY_ACID_TRANSPORT = "GO_2000192"

    # positive regulation of fatty acid transport
    GO_2000193 = "GO_2000193"
    POSITIVE_REGULATION_OF_FATTY_ACID_TRANSPORT = "GO_2000193"

    # regulation of DNA biosynthetic process
    GO_2000278 = "GO_2000278"
    REGULATION_OF_DNA_BIOSYNTHETIC_PROCESS = "GO_2000278"

    # negative regulation of DNA biosynthetic process
    GO_2000279 = "GO_2000279"
    NEGATIVE_REGULATION_OF_DNA_BIOSYNTHETIC_PROCESS = "GO_2000279"

    # positive regulation of DNA biosynthetic process
    GO_2000573 = "GO_2000573"
    POSITIVE_REGULATION_OF_DNA_BIOSYNTHETIC_PROCESS = "GO_2000573"

    # regulation of transcription regulatory region DNA binding
    GO_2000677 = "GO_2000677"
    REGULATION_OF_TRANSCRIPTION_REGULATORY_REGION_DNA_BINDING = "GO_2000677"

    # negative regulation of transcription regulatory region DNA binding
    GO_2000678 = "GO_2000678"
    NEGATIVE_REGULATION_OF_TRANSCRIPTION_REGULATORY_REGION_DNA_BINDING = "GO_2000678"

    # positive regulation of transcription regulatory region DNA binding
    GO_2000679 = "GO_2000679"
    POSITIVE_REGULATION_OF_TRANSCRIPTION_REGULATORY_REGION_DNA_BINDING = "GO_2000679"

    # regulation of response to DNA damage stimulus
    GO_2001020 = "GO_2001020"
    REGULATION_OF_RESPONSE_TO_DNA_DAMAGE_STIMULUS = "GO_2001020"

    # negative regulation of response to DNA damage stimulus
    GO_2001021 = "GO_2001021"
    NEGATIVE_REGULATION_OF_RESPONSE_TO_DNA_DAMAGE_STIMULUS = "GO_2001021"

    # positive regulation of response to DNA damage stimulus
    GO_2001022 = "GO_2001022"
    POSITIVE_REGULATION_OF_RESPONSE_TO_DNA_DAMAGE_STIMULUS = "GO_2001022"

    # regulation of response to drug
    GO_2001023 = "GO_2001023"
    REGULATION_OF_RESPONSE_TO_DRUG = "GO_2001023"

    # negative regulation of response to drug
    GO_2001024 = "GO_2001024"
    NEGATIVE_REGULATION_OF_RESPONSE_TO_DRUG = "GO_2001024"

    # positive regulation of response to drug
    GO_2001025 = "GO_2001025"
    POSITIVE_REGULATION_OF_RESPONSE_TO_DRUG = "GO_2001025"

    # regulation of cellular response to drug
    GO_2001038 = "GO_2001038"
    REGULATION_OF_CELLULAR_RESPONSE_TO_DRUG = "GO_2001038"

    # negative regulation of cellular response to drug
    GO_2001039 = "GO_2001039"
    NEGATIVE_REGULATION_OF_CELLULAR_RESPONSE_TO_DRUG = "GO_2001039"

    # positive regulation of cellular response to drug
    GO_2001040 = "GO_2001040"
    POSITIVE_REGULATION_OF_CELLULAR_RESPONSE_TO_DRUG = "GO_2001040"

    # regulation of RNA biosynthetic process
    GO_2001141 = "GO_2001141"
    REGULATION_OF_RNA_BIOSYNTHETIC_PROCESS = "GO_2001141"

    # negative regulation of chromosome organization
    GO_2001251 = "GO_2001251"
    NEGATIVE_REGULATION_OF_CHROMOSOME_ORGANIZATION = "GO_2001251"

    # positive regulation of chromosome organization
    GO_2001252 = "GO_2001252"
    POSITIVE_REGULATION_OF_CHROMOSOME_ORGANIZATION = "GO_2001252"

    # measurement unit label
    IAO_0000003 = "IAO_0000003"
    MEASUREMENT_UNIT_LABEL = "IAO_0000003"

    # objective specification
    IAO_0000005 = "IAO_0000005"
    OBJECTIVE_SPECIFICATION = "IAO_0000005"

    # action specification
    IAO_0000007 = "IAO_0000007"
    ACTION_SPECIFICATION = "IAO_0000007"

    # datum label
    IAO_0000009 = "IAO_0000009"
    DATUM_LABEL = "IAO_0000009"

    # information carrier
    IAO_0000015 = "IAO_0000015"
    INFORMATION_CARRIER = "IAO_0000015"

    # data item
    IAO_0000027 = "IAO_0000027"
    DATA_ITEM = "IAO_0000027"

    # information content entity
    IAO_0000030 = "IAO_0000030"
    INFORMATION_CONTENT_ENTITY = "IAO_0000030"

    # scalar measurement datum
    IAO_0000032 = "IAO_0000032"
    SCALAR_MEASUREMENT_DATUM = "IAO_0000032"

    # directive information entity
    IAO_0000033 = "IAO_0000033"
    DIRECTIVE_INFORMATION_ENTITY = "IAO_0000033"

    # graph
    IAO_0000038 = "IAO_0000038"
    GRAPH = "IAO_0000038"

    # has measurement unit label
    IAO_0000039 = "IAO_0000039"
    HAS_MEASUREMENT_UNIT_LABEL = "IAO_0000039"

    # algorithm
    IAO_0000064 = "IAO_0000064"
    ALGORITHM = "IAO_0000064"

    # curation status specification
    IAO_0000078 = "IAO_0000078"
    CURATION_STATUS_SPECIFICATION = "IAO_0000078"

    # image
    IAO_0000101 = "IAO_0000101"
    IMAGE = "IAO_0000101"

    # data about an ontology part
    IAO_0000102 = "IAO_0000102"
    DATA_ABOUT_AN_ONTOLOGY_PART = "IAO_0000102"

    # plan specification
    IAO_0000104 = "IAO_0000104"
    PLAN_SPECIFICATION = "IAO_0000104"

    # measurement datum
    IAO_0000109 = "IAO_0000109"
    MEASUREMENT_DATUM = "IAO_0000109"

    # is about
    IAO_0000136 = "IAO_0000136"
    IS_ABOUT = "IAO_0000136"

    # material information bearer
    IAO_0000178 = "IAO_0000178"
    MATERIAL_INFORMATION_BEARER = "IAO_0000178"

    # is quality measurement of
    IAO_0000221 = "IAO_0000221"
    IS_QUALITY_MEASUREMENT_OF = "IAO_0000221"

    # obsolescence reason specification
    IAO_0000225 = "IAO_0000225"
    OBSOLESCENCE_REASON_SPECIFICATION = "IAO_0000225"

    # figure
    IAO_0000308 = "IAO_0000308"
    FIGURE = "IAO_0000308"

    # diagram
    IAO_0000309 = "IAO_0000309"
    DIAGRAM = "IAO_0000309"

    # denotator type
    IAO_0000409 = "IAO_0000409"
    DENOTATOR_TYPE = "IAO_0000409"

    # is duration of
    IAO_0000413 = "IAO_0000413"
    IS_DURATION_OF = "IAO_0000413"

    # mass measurement datum
    IAO_0000414 = "IAO_0000414"
    MASS_MEASUREMENT_DATUM = "IAO_0000414"

    # time measurement datum
    IAO_0000416 = "IAO_0000416"
    TIME_MEASUREMENT_DATUM = "IAO_0000416"

    # is quality measured as
    IAO_0000417 = "IAO_0000417"
    IS_QUALITY_MEASURED_AS = "IAO_0000417"

    # line graph
    IAO_0000573 = "IAO_0000573"
    LINE_GRAPH = "IAO_0000573"

    # infection
    IDO_0000586 = "IDO_0000586"
    INFECTION = "IDO_0000586"

    # Viruses
    NCBITaxon_10239 = "NCBITaxon_10239"
    VIRUSES = "NCBITaxon_10239"

    # Euteleostomi
    NCBITaxon_117571 = "NCBITaxon_117571"
    EUTELEOSTOMI = "NCBITaxon_117571"

    # Bacteria
    NCBITaxon_2 = "NCBITaxon_2"
    BACTERIA = "NCBITaxon_2"

    # Archaea
    NCBITaxon_2157 = "NCBITaxon_2157"
    ARCHAEA = "NCBITaxon_2157"

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

    # Bilateria
    NCBITaxon_33213 = "NCBITaxon_33213"
    BILATERIA = "NCBITaxon_33213"

    # Mammalia
    NCBITaxon_40674 = "NCBITaxon_40674"
    MAMMALIA = "NCBITaxon_40674"

    # Vertebrata <Metazoa>
    NCBITaxon_7742 = "NCBITaxon_7742"
    VERTEBRATA__METAZOA_ = "NCBITaxon_7742"

    # Homo sapiens
    NCBITaxon_9606 = "NCBITaxon_9606"
    HOMO_SAPIENS = "NCBITaxon_9606"

    # planned process
    OBI_0000011 = "OBI_0000011"
    PLANNED_PROCESS = "OBI_0000011"

    # biological feature identification objective
    OBI_0000015 = "OBI_0000015"
    BIOLOGICAL_FEATURE_IDENTIFICATION_OBJECTIVE = "OBI_0000015"

    # reference substance role
    OBI_0000025 = "OBI_0000025"
    REFERENCE_SUBSTANCE_ROLE = "OBI_0000025"

    # chromatography column
    OBI_0000038 = "OBI_0000038"
    CHROMATOGRAPHY_COLUMN = "OBI_0000038"

    # xenotransplantation
    OBI_0000043 = "OBI_0000043"
    XENOTRANSPLANTATION = "OBI_0000043"

    # processed material
    OBI_0000047 = "OBI_0000047"
    PROCESSED_MATERIAL = "OBI_0000047"

    # chromatography device
    OBI_0000048 = "OBI_0000048"
    CHROMATOGRAPHY_DEVICE = "OBI_0000048"

    # mass spectrometer
    OBI_0000049 = "OBI_0000049"
    MASS_SPECTROMETER = "OBI_0000049"

    # allotransplantation
    OBI_0000057 = "OBI_0000057"
    ALLOTRANSPLANTATION = "OBI_0000057"

    # positive reference substance role
    OBI_0000064 = "OBI_0000064"
    POSITIVE_REFERENCE_SUBSTANCE_ROLE = "OBI_0000064"

    # evaluant role
    OBI_0000067 = "OBI_0000067"
    EVALUANT_ROLE = "OBI_0000067"

    # assay
    OBI_0000070 = "OBI_0000070"
    ASSAY = "OBI_0000070"

    # culture medium
    OBI_0000079 = "OBI_0000079"
    CULTURE_MEDIUM = "OBI_0000079"

    # reagent role
    OBI_0000086 = "OBI_0000086"
    REAGENT_ROLE = "OBI_0000086"

    # material processing
    OBI_0000094 = "OBI_0000094"
    MATERIAL_PROCESSING = "OBI_0000094"

    # participant under investigation role
    OBI_0000097 = "OBI_0000097"
    PARTICIPANT_UNDER_INVESTIGATION_ROLE = "OBI_0000097"

    # transplantation
    OBI_0000105 = "OBI_0000105"
    TRANSPLANTATION = "OBI_0000105"

    # specimen role
    OBI_0000112 = "OBI_0000112"
    SPECIMEN_ROLE = "OBI_0000112"

    # sequence feature identification objective
    OBI_0000113 = "OBI_0000113"
    SEQUENCE_FEATURE_IDENTIFICATION_OBJECTIVE = "OBI_0000113"

    # intervention design
    OBI_0000115 = "OBI_0000115"
    INTERVENTION_DESIGN = "OBI_0000115"

    # molecular feature identification objective
    OBI_0000131 = "OBI_0000131"
    MOLECULAR_FEATURE_IDENTIFICATION_OBJECTIVE = "OBI_0000131"

    # filter paper
    OBI_0000151 = "OBI_0000151"
    FILTER_PAPER = "OBI_0000151"

    # cell co-culturing
    OBI_0000153 = "OBI_0000153"
    CELL_CO_CULTURING = "OBI_0000153"

    # cDNA library
    OBI_0000164 = "OBI_0000164"
    CDNA_LIBRARY = "OBI_0000164"

    # imaging assay
    OBI_0000185 = "OBI_0000185"
    IMAGING_ASSAY = "OBI_0000185"

    # microtiter plate
    OBI_0000192 = "OBI_0000192"
    MICROTITER_PLATE = "OBI_0000192"

    # chromatin immunoprecipitation
    OBI_00001975 = "OBI_00001975"
    CHROMATIN_IMMUNOPRECIPITATION = "OBI_00001975"

    # radioactivity detection
    OBI_0000201 = "OBI_0000201"
    RADIOACTIVITY_DETECTION = "OBI_0000201"

    # cellular feature identification objective
    OBI_0000219 = "OBI_0000219"
    CELLULAR_FEATURE_IDENTIFICATION_OBJECTIVE = "OBI_0000219"

    # enzymatic cleavage
    OBI_0000231 = "OBI_0000231"
    ENZYMATIC_CLEAVAGE = "OBI_0000231"

    # organization
    OBI_0000245 = "OBI_0000245"
    ORGANIZATION = "OBI_0000245"

    # dye role
    OBI_0000250 = "OBI_0000250"
    DYE_ROLE = "OBI_0000250"

    # artificially induced nucleic acid hybridization
    OBI_0000253 = "OBI_0000253"
    ARTIFICIALLY_INDUCED_NUCLEIC_ACID_HYBRIDIZATION = "OBI_0000253"

    # DNA extraction
    OBI_0000257 = "OBI_0000257"
    DNA_EXTRACTION = "OBI_0000257"

    # organism feature identification objective
    OBI_0000268 = "OBI_0000268"
    ORGANISM_FEATURE_IDENTIFICATION_OBJECTIVE = "OBI_0000268"

    # protocol
    OBI_0000272 = "OBI_0000272"
    PROTOCOL = "OBI_0000272"

    # adding a material entity into a target
    OBI_0000274 = "OBI_0000274"
    ADDING_A_MATERIAL_ENTITY_INTO_A_TARGET = "OBI_0000274"

    # analyte role
    OBI_0000275 = "OBI_0000275"
    ANALYTE_ROLE = "OBI_0000275"

    # protein-protein interaction detection assay
    OBI_0000288 = "OBI_0000288"
    PROTEIN_PROTEIN_INTERACTION_DETECTION_ASSAY = "OBI_0000288"

    # has_specified_input
    OBI_0000293 = "OBI_0000293"
    HAS_SPECIFIED_INPUT = "OBI_0000293"

    # is_specified_input_of
    OBI_0000295 = "OBI_0000295"
    IS_SPECIFIED_INPUT_OF = "OBI_0000295"

    # has_specified_output
    OBI_0000299 = "OBI_0000299"
    HAS_SPECIFIED_OUTPUT = "OBI_0000299"

    # is_manufactured_by
    OBI_0000304 = "OBI_0000304"
    IS_MANUFACTURED_BY = "OBI_0000304"

    # is_specified_output_of
    OBI_0000312 = "OBI_0000312"
    IS_SPECIFIED_OUTPUT_OF = "OBI_0000312"

    # eluate
    OBI_0000318 = "OBI_0000318"
    ELUATE = "OBI_0000318"

    # material to be added role
    OBI_0000319 = "OBI_0000319"
    MATERIAL_TO_BE_ADDED_ROLE = "OBI_0000319"

    # histological sample preparation
    OBI_0000341 = "OBI_0000341"
    HISTOLOGICAL_SAMPLE_PREPARATION = "OBI_0000341"

    # mass analyzer
    OBI_0000345 = "OBI_0000345"
    MASS_ANALYZER = "OBI_0000345"

    # ion source
    OBI_0000361 = "OBI_0000361"
    ION_SOURCE = "OBI_0000361"

    # ion detector
    OBI_0000364 = "OBI_0000364"
    ION_DETECTOR = "OBI_0000364"

    # metabolite profiling assay
    OBI_0000366 = "OBI_0000366"
    METABOLITE_PROFILING_ASSAY = "OBI_0000366"

    # light emission function
    OBI_0000367 = "OBI_0000367"
    LIGHT_EMISSION_FUNCTION = "OBI_0000367"

    # magnify function
    OBI_0000369 = "OBI_0000369"
    MAGNIFY_FUNCTION = "OBI_0000369"

    # contain function
    OBI_0000370 = "OBI_0000370"
    CONTAIN_FUNCTION = "OBI_0000370"

    # heat function
    OBI_0000371 = "OBI_0000371"
    HEAT_FUNCTION = "OBI_0000371"

    # material separation function
    OBI_0000372 = "OBI_0000372"
    MATERIAL_SEPARATION_FUNCTION = "OBI_0000372"

    # excitation function
    OBI_0000374 = "OBI_0000374"
    EXCITATION_FUNCTION = "OBI_0000374"

    # synthesizing function
    OBI_0000376 = "OBI_0000376"
    SYNTHESIZING_FUNCTION = "OBI_0000376"

    # perturb function
    OBI_0000377 = "OBI_0000377"
    PERTURB_FUNCTION = "OBI_0000377"

    # filter function
    OBI_0000378 = "OBI_0000378"
    FILTER_FUNCTION = "OBI_0000378"

    # mechanical function
    OBI_0000379 = "OBI_0000379"
    MECHANICAL_FUNCTION = "OBI_0000379"

    # electricity supply function
    OBI_0000384 = "OBI_0000384"
    ELECTRICITY_SUPPLY_FUNCTION = "OBI_0000384"

    # ionization function
    OBI_0000385 = "OBI_0000385"
    IONIZATION_FUNCTION = "OBI_0000385"

    # cool function
    OBI_0000387 = "OBI_0000387"
    COOL_FUNCTION = "OBI_0000387"

    # energy supply function
    OBI_0000391 = "OBI_0000391"
    ENERGY_SUPPLY_FUNCTION = "OBI_0000391"

    # image acquisition function
    OBI_0000397 = "OBI_0000397"
    IMAGE_ACQUISITION_FUNCTION = "OBI_0000397"

    # image creation device
    OBI_0000398 = "OBI_0000398"
    IMAGE_CREATION_DEVICE = "OBI_0000398"

    # solid support function
    OBI_0000399 = "OBI_0000399"
    SOLID_SUPPORT_FUNCTION = "OBI_0000399"

    # environment control function
    OBI_0000401 = "OBI_0000401"
    ENVIRONMENT_CONTROL_FUNCTION = "OBI_0000401"

    # sort function
    OBI_0000403 = "OBI_0000403"
    SORT_FUNCTION = "OBI_0000403"

    # PCR product
    OBI_0000406 = "OBI_0000406"
    PCR_PRODUCT = "OBI_0000406"

    # nucleic acid template role
    OBI_0000409 = "OBI_0000409"
    NUCLEIC_ACID_TEMPLATE_ROLE = "OBI_0000409"

    # cloning vector role
    OBI_0000411 = "OBI_0000411"
    CLONING_VECTOR_ROLE = "OBI_0000411"

    # polymerase chain reaction
    OBI_0000415 = "OBI_0000415"
    POLYMERASE_CHAIN_REACTION = "OBI_0000415"

    # cloning insert role
    OBI_0000416 = "OBI_0000416"
    CLONING_INSERT_ROLE = "OBI_0000416"

    # achieves_planned_objective
    OBI_0000417 = "OBI_0000417"
    ACHIEVES_PLANNED_OBJECTIVE = "OBI_0000417"

    # reverse transcriptase
    OBI_0000419 = "OBI_0000419"
    REVERSE_TRANSCRIPTASE = "OBI_0000419"

    # extract
    OBI_0000423 = "OBI_0000423"
    EXTRACT = "OBI_0000423"

    # transcription profiling assay
    OBI_0000424 = "OBI_0000424"
    TRANSCRIPTION_PROFILING_ASSAY = "OBI_0000424"

    # enzyme
    OBI_0000427 = "OBI_0000427"
    ENZYME = "OBI_0000427"

    # polyacrylamide gel
    OBI_0000432 = "OBI_0000432"
    POLYACRYLAMIDE_GEL = "OBI_0000432"

    # adding material objective
    OBI_0000434 = "OBI_0000434"
    ADDING_MATERIAL_OBJECTIVE = "OBI_0000434"

    # genotyping assay
    OBI_0000435 = "OBI_0000435"
    GENOTYPING_ASSAY = "OBI_0000435"

    # analyte measurement objective
    OBI_0000437 = "OBI_0000437"
    ANALYTE_MEASUREMENT_OBJECTIVE = "OBI_0000437"

    # agarose gel
    OBI_0000439 = "OBI_0000439"
    AGAROSE_GEL = "OBI_0000439"

    # assay objective
    OBI_0000441 = "OBI_0000441"
    ASSAY_OBJECTIVE = "OBI_0000441"

    # analyte assay
    OBI_0000443 = "OBI_0000443"
    ANALYTE_ASSAY = "OBI_0000443"

    # target of material addition role
    OBI_0000444 = "OBI_0000444"
    TARGET_OF_MATERIAL_ADDITION_ROLE = "OBI_0000444"

    # intra cellular electrophysiology recording assay
    OBI_0000447 = "OBI_0000447"
    INTRA_CELLULAR_ELECTROPHYSIOLOGY_RECORDING_ASSAY = "OBI_0000447"

    # measure function
    OBI_0000453 = "OBI_0000453"
    MEASURE_FUNCTION = "OBI_0000453"

    # extracellular electrophysiology recording assay
    OBI_0000454 = "OBI_0000454"
    EXTRACELLULAR_ELECTROPHYSIOLOGY_RECORDING_ASSAY = "OBI_0000454"

    # material transformation objective
    OBI_0000456 = "OBI_0000456"
    MATERIAL_TRANSFORMATION_OBJECTIVE = "OBI_0000456"

    # mass spectrometry assay
    OBI_0000470 = "OBI_0000470"
    MASS_SPECTROMETRY_ASSAY = "OBI_0000470"

    # study design execution
    OBI_0000471 = "OBI_0000471"
    STUDY_DESIGN_EXECUTION = "OBI_0000471"

    # affinity column
    OBI_0000533 = "OBI_0000533"
    AFFINITY_COLUMN = "OBI_0000533"

    # gel filtration column
    OBI_0000535 = "OBI_0000535"
    GEL_FILTRATION_COLUMN = "OBI_0000535"

    # reverse transcribed polymerase chain reaction
    OBI_0000552 = "OBI_0000552"
    REVERSE_TRANSCRIBED_POLYMERASE_CHAIN_REACTION = "OBI_0000552"

    # scattered molecular aggregate
    OBI_0000576 = "OBI_0000576"
    SCATTERED_MOLECULAR_AGGREGATE = "OBI_0000576"

    # chromatography consumable
    OBI_0000601 = "OBI_0000601"
    CHROMATOGRAPHY_CONSUMABLE = "OBI_0000601"

    # size exclusion column
    OBI_0000618 = "OBI_0000618"
    SIZE_EXCLUSION_COLUMN = "OBI_0000618"

    # NMR spectroscopy assay
    OBI_0000623 = "OBI_0000623"
    NMR_SPECTROSCOPY_ASSAY = "OBI_0000623"

    # DNA sequencing assay
    OBI_0000626 = "OBI_0000626"
    DNA_SEQUENCING_ASSAY = "OBI_0000626"

    # hematology assay
    OBI_0000630 = "OBI_0000630"
    HEMATOLOGY_ASSAY = "OBI_0000630"

    # DNA methylation profiling assay
    OBI_0000634 = "OBI_0000634"
    DNA_METHYLATION_PROFILING_ASSAY = "OBI_0000634"

    # material separation objective
    OBI_0000639 = "OBI_0000639"
    MATERIAL_SEPARATION_OBJECTIVE = "OBI_0000639"

    # has grain
    OBI_0000643 = "OBI_0000643"
    HAS_GRAIN = "OBI_0000643"

    # supplies
    OBI_0000646 = "OBI_0000646"
    SUPPLIES = "OBI_0000646"

    # has_supplier
    OBI_0000647 = "OBI_0000647"
    HAS_SUPPLIER = "OBI_0000647"

    # differential expression analysis data transformation
    OBI_0000650 = "OBI_0000650"
    DIFFERENTIAL_EXPRESSION_ANALYSIS_DATA_TRANSFORMATION = "OBI_0000650"

    # urine specimen
    OBI_0000651 = "OBI_0000651"
    URINE_SPECIMEN = "OBI_0000651"

    # material combination
    OBI_0000652 = "OBI_0000652"
    MATERIAL_COMBINATION = "OBI_0000652"

    # device setting
    OBI_0000654 = "OBI_0000654"
    DEVICE_SETTING = "OBI_0000654"

    # specimen collection process
    OBI_0000659 = "OBI_0000659"
    SPECIMEN_COLLECTION_PROCESS = "OBI_0000659"

    # BrdU incorporation assay
    OBI_0000664 = "OBI_0000664"
    BRDU_INCORPORATION_ASSAY = "OBI_0000664"

    # tritiated thymidine incorporation assay
    OBI_0000669 = "OBI_0000669"
    TRITIATED_THYMIDINE_INCORPORATION_ASSAY = "OBI_0000669"

    # sample from organism
    OBI_0000671 = "OBI_0000671"
    SAMPLE_FROM_ORGANISM = "OBI_0000671"

    # portioning objective
    OBI_0000678 = "OBI_0000678"
    PORTIONING_OBJECTIVE = "OBI_0000678"

    # separation into different composition objective
    OBI_0000681 = "OBI_0000681"
    SEPARATION_INTO_DIFFERENT_COMPOSITION_OBJECTIVE = "OBI_0000681"

    # specimen collection objective
    OBI_0000684 = "OBI_0000684"
    SPECIMEN_COLLECTION_OBJECTIVE = "OBI_0000684"

    # creating a mixture of molecules in solution
    OBI_0000685 = "OBI_0000685"
    CREATING_A_MIXTURE_OF_MOLECULES_IN_SOLUTION = "OBI_0000685"

    # material combination objective
    OBI_0000686 = "OBI_0000686"
    MATERIAL_COMBINATION_OBJECTIVE = "OBI_0000686"

    # immunoprecipitation
    OBI_0000690 = "OBI_0000690"
    IMMUNOPRECIPITATION = "OBI_0000690"

    # survival assessment assay
    OBI_0000699 = "OBI_0000699"
    SURVIVAL_ASSESSMENT_ASSAY = "OBI_0000699"

    # library preparation
    OBI_0000711 = "OBI_0000711"
    LIBRARY_PREPARATION = "OBI_0000711"

    # ChIP-seq assay
    OBI_0000716 = "OBI_0000716"
    CHIP_SEQ_ASSAY = "OBI_0000716"

    # paired-end library
    OBI_0000722 = "OBI_0000722"
    PAIRED_END_LIBRARY = "OBI_0000722"

    # recombinant vector
    OBI_0000731 = "OBI_0000731"
    RECOMBINANT_VECTOR = "OBI_0000731"

    # single fragment library
    OBI_0000736 = "OBI_0000736"
    SINGLE_FRAGMENT_LIBRARY = "OBI_0000736"

    # cloning vector
    OBI_0000737 = "OBI_0000737"
    CLONING_VECTOR = "OBI_0000737"

    # material sample role
    OBI_0000740 = "OBI_0000740"
    MATERIAL_SAMPLE_ROLE = "OBI_0000740"

    # material sampling process
    OBI_0000744 = "OBI_0000744"
    MATERIAL_SAMPLING_PROCESS = "OBI_0000744"

    # material sample
    OBI_0000747 = "OBI_0000747"
    MATERIAL_SAMPLE = "OBI_0000747"

    # study design independent variable
    OBI_0000750 = "OBI_0000750"
    STUDY_DESIGN_INDEPENDENT_VARIABLE = "OBI_0000750"

    # survival rate
    OBI_0000789 = "OBI_0000789"
    SURVIVAL_RATE = "OBI_0000789"

    # purification objective
    OBI_0000796 = "OBI_0000796"
    PURIFICATION_OBJECTIVE = "OBI_0000796"

    # cross linking
    OBI_0000800 = "OBI_0000800"
    CROSS_LINKING = "OBI_0000800"

    # material maintenance objective
    OBI_0000806 = "OBI_0000806"
    MATERIAL_MAINTENANCE_OBJECTIVE = "OBI_0000806"

    # presentation of stimulus
    OBI_0000807 = "OBI_0000807"
    PRESENTATION_OF_STIMULUS = "OBI_0000807"

    # amplified DNA
    OBI_0000809 = "OBI_0000809"
    AMPLIFIED_DNA = "OBI_0000809"

    # primary structure of DNA macromolecule
    OBI_0000811 = "OBI_0000811"
    PRIMARY_STRUCTURE_OF_DNA_MACROMOLECULE = "OBI_0000811"

    # micro electrode
    OBI_0000816 = "OBI_0000816"
    MICRO_ELECTRODE = "OBI_0000816"

    # measurement device
    OBI_0000832 = "OBI_0000832"
    MEASUREMENT_DEVICE = "OBI_0000832"

    # objective_achieved_by
    OBI_0000833 = "OBI_0000833"
    OBJECTIVE_ACHIEVED_BY = "OBI_0000833"

    # high molecular weight DNA extract
    OBI_0000834 = "OBI_0000834"
    HIGH_MOLECULAR_WEIGHT_DNA_EXTRACT = "OBI_0000834"

    # material maintenance
    OBI_0000838 = "OBI_0000838"
    MATERIAL_MAINTENANCE = "OBI_0000838"

    # primary structure of RNA molecule
    OBI_0000845 = "OBI_0000845"
    PRIMARY_STRUCTURE_OF_RNA_MOLECULE = "OBI_0000845"

    # complementary nucleotide probe role
    OBI_0000857 = "OBI_0000857"
    COMPLEMENTARY_NUCLEOTIDE_PROBE_ROLE = "OBI_0000857"

    # northern blot assay
    OBI_0000860 = "OBI_0000860"
    NORTHERN_BLOT_ASSAY = "OBI_0000860"

    # pre-mortem specimen
    OBI_0000873 = "OBI_0000873"
    PRE_MORTEM_SPECIMEN = "OBI_0000873"

    # detection of specific nucleic acid polymers with complementary probes
    OBI_0000874 = "OBI_0000874"
    DETECTION_OF_SPECIFIC_NUCLEIC_ACID_POLYMERS_WITH_COMPLEMENTARY_PROBES = (
        "OBI_0000874"
    )

    # RNA extract
    OBI_0000880 = "OBI_0000880"
    RNA_EXTRACT = "OBI_0000880"

    # cell-cell killing assay
    OBI_0000882 = "OBI_0000882"
    CELL_CELL_KILLING_ASSAY = "OBI_0000882"

    # in vivo cell killing assay
    OBI_0000883 = "OBI_0000883"
    IN_VIVO_CELL_KILLING_ASSAY = "OBI_0000883"

    # cell proliferation assay
    OBI_0000891 = "OBI_0000891"
    CELL_PROLIFERATION_ASSAY = "OBI_0000891"

    # Southern blot assay
    OBI_0000892 = "OBI_0000892"
    SOUTHERN_BLOT_ASSAY = "OBI_0000892"

    # real time polymerase chain reaction assay
    OBI_0000893 = "OBI_0000893"
    REAL_TIME_POLYMERASE_CHAIN_REACTION_ASSAY = "OBI_0000893"

    # post mortem specimen
    OBI_0000902 = "OBI_0000902"
    POST_MORTEM_SPECIMEN = "OBI_0000902"

    # in vitro cell killing assay
    OBI_0000903 = "OBI_0000903"
    IN_VITRO_CELL_KILLING_ASSAY = "OBI_0000903"

    # X-ray crystallography assay
    OBI_0000912 = "OBI_0000912"
    X_RAY_CRYSTALLOGRAPHY_ASSAY = "OBI_0000912"

    # promoter activity detection by reporter gene assay
    OBI_0000913 = "OBI_0000913"
    PROMOTER_ACTIVITY_DETECTION_BY_REPORTER_GENE_ASSAY = "OBI_0000913"

    # flow cytometry assay
    OBI_0000916 = "OBI_0000916"
    FLOW_CYTOMETRY_ASSAY = "OBI_0000916"

    # labeled RNA extract
    OBI_0000921 = "OBI_0000921"
    LABELED_RNA_EXTRACT = "OBI_0000921"

    # surface plasmon resonance binding assay
    OBI_0000923 = "OBI_0000923"
    SURFACE_PLASMON_RESONANCE_BINDING_ASSAY = "OBI_0000923"

    # labeled specimen
    OBI_0000924 = "OBI_0000924"
    LABELED_SPECIMEN = "OBI_0000924"

    # infectious agent
    OBI_0000925 = "OBI_0000925"
    INFECTIOUS_AGENT = "OBI_0000925"

    # calorimeter
    OBI_0000930 = "OBI_0000930"
    CALORIMETER = "OBI_0000930"

    # study intervention
    OBI_0000931 = "OBI_0000931"
    STUDY_INTERVENTION = "OBI_0000931"

    # material separation device
    OBI_0000932 = "OBI_0000932"
    MATERIAL_SEPARATION_DEVICE = "OBI_0000932"

    # processed specimen
    OBI_0000953 = "OBI_0000953"
    PROCESSED_SPECIMEN = "OBI_0000953"

    # in live cell assay
    OBI_0000964 = "OBI_0000964"
    IN_LIVE_CELL_ASSAY = "OBI_0000964"

    # in live organism assay
    OBI_0000966 = "OBI_0000966"
    IN_LIVE_ORGANISM_ASSAY = "OBI_0000966"

    # container
    OBI_0000967 = "OBI_0000967"
    CONTAINER = "OBI_0000967"

    # device
    OBI_0000968 = "OBI_0000968"
    DEVICE = "OBI_0000968"

    # sequence data
    OBI_0000973 = "OBI_0000973"
    SEQUENCE_DATA = "OBI_0000973"

    # cell-cell binding detection by flow cytometry assay
    OBI_0000975 = "OBI_0000975"
    CELL_CELL_BINDING_DETECTION_BY_FLOW_CYTOMETRY_ASSAY = "OBI_0000975"

    # in container assay
    OBI_0000978 = "OBI_0000978"
    IN_CONTAINER_ASSAY = "OBI_0000978"

    # growth condition intervention design
    OBI_0000985 = "OBI_0000985"
    GROWTH_CONDITION_INTERVENTION_DESIGN = "OBI_0000985"

    # PCR instrument
    OBI_0000989 = "OBI_0000989"
    PCR_INSTRUMENT = "OBI_0000989"

    # electron microscope
    OBI_0000990 = "OBI_0000990"
    ELECTRON_MICROSCOPE = "OBI_0000990"

    # growth environment
    OBI_0000997 = "OBI_0000997"
    GROWTH_ENVIRONMENT = "OBI_0000997"

    # image creation
    OBI_0001007 = "OBI_0001007"
    IMAGE_CREATION = "OBI_0001007"

    # nucleic acid extract
    OBI_0001010 = "OBI_0001010"
    NUCLEIC_ACID_EXTRACT = "OBI_0001010"

    # binding constant determination assay
    OBI_0001025 = "OBI_0001025"
    BINDING_CONSTANT_DETERMINATION_ASSAY = "OBI_0001025"

    # light emission device
    OBI_0001032 = "OBI_0001032"
    LIGHT_EMISSION_DEVICE = "OBI_0001032"

    # perturbation device
    OBI_0001033 = "OBI_0001033"
    PERTURBATION_DEVICE = "OBI_0001033"

    # environmental control device
    OBI_0001034 = "OBI_0001034"
    ENVIRONMENTAL_CONTROL_DEVICE = "OBI_0001034"

    # DNA extract
    OBI_0001051 = "OBI_0001051"
    DNA_EXTRACT = "OBI_0001051"

    # electrophoresis system
    OBI_0001053 = "OBI_0001053"
    ELECTROPHORESIS_SYSTEM = "OBI_0001053"

    # high performance liquid chromatography instrument
    OBI_0001057 = "OBI_0001057"
    HIGH_PERFORMANCE_LIQUID_CHROMATOGRAPHY_INSTRUMENT = "OBI_0001057"

    # confocal microscope
    OBI_0001079 = "OBI_0001079"
    CONFOCAL_MICROSCOPE = "OBI_0001079"

    # patch clamp device
    OBI_0001080 = "OBI_0001080"
    PATCH_CLAMP_DEVICE = "OBI_0001080"

    # nucleic acid sequencer
    OBI_0001108 = "OBI_0001108"
    NUCLEIC_ACID_SEQUENCER = "OBI_0001108"

    # gel electrophoresis system
    OBI_0001121 = "OBI_0001121"
    GEL_ELECTROPHORESIS_SYSTEM = "OBI_0001121"

    # voltage clamp device
    OBI_0001129 = "OBI_0001129"
    VOLTAGE_CLAMP_DEVICE = "OBI_0001129"

    # surface plasmon resonance instrument
    OBI_0001136 = "OBI_0001136"
    SURFACE_PLASMON_RESONANCE_INSTRUMENT = "OBI_0001136"

    # protein sequencer
    OBI_0001137 = "OBI_0001137"
    PROTEIN_SEQUENCER = "OBI_0001137"

    # X-ray source
    OBI_0001138 = "OBI_0001138"
    X_RAY_SOURCE = "OBI_0001138"

    # liquid chromatography instrument
    OBI_0001139 = "OBI_0001139"
    LIQUID_CHROMATOGRAPHY_INSTRUMENT = "OBI_0001139"

    # labeled nucleic acid extract
    OBI_0001143 = "OBI_0001143"
    LABELED_NUCLEIC_ACID_EXTRACT = "OBI_0001143"

    # binding constant
    OBI_0001144 = "OBI_0001144"
    BINDING_CONSTANT = "OBI_0001144"

    # 3D structure determination of bound complex assay
    OBI_0001145 = "OBI_0001145"
    _3D_STRUCTURE_DETERMINATION_OF_BOUND_COMPLEX_ASSAY = "OBI_0001145"

    # binding assay
    OBI_0001146 = "OBI_0001146"
    BINDING_ASSAY = "OBI_0001146"

    # cell culture expansion
    OBI_0001147 = "OBI_0001147"
    CELL_CULTURE_EXPANSION = "OBI_0001147"

    # gene knock out
    OBI_0001148 = "OBI_0001148"
    GENE_KNOCK_OUT = "OBI_0001148"

    # gene knock in
    OBI_0001149 = "OBI_0001149"
    GENE_KNOCK_IN = "OBI_0001149"

    # genetically modified material
    OBI_0001151 = "OBI_0001151"
    GENETICALLY_MODIFIED_MATERIAL = "OBI_0001151"

    # transfection
    OBI_0001152 = "OBI_0001152"
    TRANSFECTION = "OBI_0001152"

    # genetic transformation objective
    OBI_0001153 = "OBI_0001153"
    GENETIC_TRANSFORMATION_OBJECTIVE = "OBI_0001153"

    # induced mutation
    OBI_0001154 = "OBI_0001154"
    INDUCED_MUTATION = "OBI_0001154"

    # 3D structural organization datum
    OBI_0001155 = "OBI_0001155"
    _3D_STRUCTURAL_ORGANIZATION_DATUM = "OBI_0001155"

    # half life datum (t 1/2)
    OBI_0001171 = "OBI_0001171"
    HALF_LIFE_DATUM__T_1_2_ = "OBI_0001171"

    # dose response curve
    OBI_0001172 = "OBI_0001172"
    DOSE_RESPONSE_CURVE = "OBI_0001172"

    # RNA sequencing assay
    OBI_0001177 = "OBI_0001177"
    RNA_SEQUENCING_ASSAY = "OBI_0001177"

    # half maximal effective concentration (EC50)
    OBI_0001180 = "OBI_0001180"
    HALF_MAXIMAL_EFFECTIVE_CONCENTRATION__EC50_ = "OBI_0001180"

    # binding datum
    OBI_0001181 = "OBI_0001181"
    BINDING_DATUM = "OBI_0001181"

    # half maximal inhibitory concentration (IC50)
    OBI_0001191 = "OBI_0001191"
    HALF_MAXIMAL_INHIBITORY_CONCENTRATION__IC50_ = "OBI_0001191"

    # in vivo design
    OBI_0001199 = "OBI_0001199"
    IN_VIVO_DESIGN = "OBI_0001199"

    # genotyping by high throughput sequencing design
    OBI_0001200 = "OBI_0001200"
    GENOTYPING_BY_HIGH_THROUGHPUT_SEQUENCING_DESIGN = "OBI_0001200"

    # ex vivo design
    OBI_0001211 = "OBI_0001211"
    EX_VIVO_DESIGN = "OBI_0001211"

    # genetic population background information
    OBI_0001225 = "OBI_0001225"
    GENETIC_POPULATION_BACKGROUND_INFORMATION = "OBI_0001225"

    # epigenetic modification identification objective
    OBI_0001234 = "OBI_0001234"
    EPIGENETIC_MODIFICATION_IDENTIFICATION_OBJECTIVE = "OBI_0001234"

    # transcription profiling by high throughput sequencing design
    OBI_0001239 = "OBI_0001239"
    TRANSCRIPTION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING_DESIGN = "OBI_0001239"

    # genotyping by high throughput sequencing assay
    OBI_0001247 = "OBI_0001247"
    GENOTYPING_BY_HIGH_THROUGHPUT_SEQUENCING_ASSAY = "OBI_0001247"

    # ChIP-chip assay
    OBI_0001248 = "OBI_0001248"
    CHIP_CHIP_ASSAY = "OBI_0001248"

    # ChIP-seq design
    OBI_0001258 = "OBI_0001258"
    CHIP_SEQ_DESIGN = "OBI_0001258"

    # DNA methylation profiling by high throughput sequencing assay
    OBI_0001266 = "OBI_0001266"
    DNA_METHYLATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING_ASSAY = "OBI_0001266"

    # RNA-seq assay
    OBI_0001271 = "OBI_0001271"
    RNA_SEQ_ASSAY = "OBI_0001271"

    # DNA methylation profiling by array design
    OBI_0001278 = "OBI_0001278"
    DNA_METHYLATION_PROFILING_BY_ARRAY_DESIGN = "OBI_0001278"

    # in vitro design
    OBI_0001285 = "OBI_0001285"
    IN_VITRO_DESIGN = "OBI_0001285"

    # transcription profiling by array design
    OBI_0001290 = "OBI_0001290"
    TRANSCRIPTION_PROFILING_BY_ARRAY_DESIGN = "OBI_0001290"

    # genotype information
    OBI_0001305 = "OBI_0001305"
    GENOTYPE_INFORMATION = "OBI_0001305"

    # transcription profiling by RT-PCR design
    OBI_0001313 = "OBI_0001313"
    TRANSCRIPTION_PROFILING_BY_RT_PCR_DESIGN = "OBI_0001313"

    # proteomic profiling by array assay
    OBI_0001318 = "OBI_0001318"
    PROTEOMIC_PROFILING_BY_ARRAY_ASSAY = "OBI_0001318"

    # transcription profiling identification objective
    OBI_0001331 = "OBI_0001331"
    TRANSCRIPTION_PROFILING_IDENTIFICATION_OBJECTIVE = "OBI_0001331"

    # post-transcriptional modification design
    OBI_0001358 = "OBI_0001358"
    POST_TRANSCRIPTIONAL_MODIFICATION_DESIGN = "OBI_0001358"

    # transcription profiling by RT-PCR assay
    OBI_0001361 = "OBI_0001361"
    TRANSCRIPTION_PROFILING_BY_RT_PCR_ASSAY = "OBI_0001361"

    # genetic alteration information
    OBI_0001364 = "OBI_0001364"
    GENETIC_ALTERATION_INFORMATION = "OBI_0001364"

    # cellular process design
    OBI_0001365 = "OBI_0001365"
    CELLULAR_PROCESS_DESIGN = "OBI_0001365"

    # stimulus or stress design
    OBI_0001396 = "OBI_0001396"
    STIMULUS_OR_STRESS_DESIGN = "OBI_0001396"

    # protein and DNA interaction identification objective
    OBI_0001398 = "OBI_0001398"
    PROTEIN_AND_DNA_INTERACTION_IDENTIFICATION_OBJECTIVE = "OBI_0001398"

    # ChIP-chip design
    OBI_0001403 = "OBI_0001403"
    CHIP_CHIP_DESIGN = "OBI_0001403"

    # genetic characteristics information
    OBI_0001404 = "OBI_0001404"
    GENETIC_CHARACTERISTICS_INFORMATION = "OBI_0001404"

    # protein binding site identification design
    OBI_0001425 = "OBI_0001425"
    PROTEIN_BINDING_SITE_IDENTIFICATION_DESIGN = "OBI_0001425"

    # transcription profiling design
    OBI_0001430 = "OBI_0001430"
    TRANSCRIPTION_PROFILING_DESIGN = "OBI_0001430"

    # proteomic profiling by array design
    OBI_0001441 = "OBI_0001441"
    PROTEOMIC_PROFILING_BY_ARRAY_DESIGN = "OBI_0001441"

    # genotyping design
    OBI_0001444 = "OBI_0001444"
    GENOTYPING_DESIGN = "OBI_0001444"

    # genetic modification design
    OBI_0001460 = "OBI_0001460"
    GENETIC_MODIFICATION_DESIGN = "OBI_0001460"

    # transcription profiling by array assay
    OBI_0001463 = "OBI_0001463"
    TRANSCRIPTION_PROFILING_BY_ARRAY_ASSAY = "OBI_0001463"

    # phage display binding assay
    OBI_0001476 = "OBI_0001476"
    PHAGE_DISPLAY_BINDING_ASSAY = "OBI_0001476"

    # specimen from organism
    OBI_0001479 = "OBI_0001479"
    SPECIMEN_FROM_ORGANISM = "OBI_0001479"

    # phage display library panning
    OBI_0001480 = "OBI_0001480"
    PHAGE_DISPLAY_LIBRARY_PANNING = "OBI_0001480"

    # fluorescence detection assay
    OBI_0001501 = "OBI_0001501"
    FLUORESCENCE_DETECTION_ASSAY = "OBI_0001501"

    # purification
    OBI_0001505 = "OBI_0001505"
    PURIFICATION = "OBI_0001505"

    # specimen with pre- or post-mortem status
    OBI_0001506 = "OBI_0001506"
    SPECIMEN_WITH_PRE__OR_POST_MORTEM_STATUS = "OBI_0001506"

    # equilibrium dissociation constant (KD)
    OBI_0001536 = "OBI_0001536"
    EQUILIBRIUM_DISSOCIATION_CONSTANT__KD_ = "OBI_0001536"

    # equilibrium association constant (KA)
    OBI_0001548 = "OBI_0001548"
    EQUILIBRIUM_ASSOCIATION_CONSTANT__KA_ = "OBI_0001548"

    # rate measurement datum
    OBI_0001554 = "OBI_0001554"
    RATE_MEASUREMENT_DATUM = "OBI_0001554"

    # equilibrium dissociation constant (KD) approximated by IC50
    OBI_0001571 = "OBI_0001571"
    EQUILIBRIUM_DISSOCIATION_CONSTANT__KD__APPROXIMATED_BY_IC50 = "OBI_0001571"

    # DNA sequence data
    OBI_0001573 = "OBI_0001573"
    DNA_SEQUENCE_DATA = "OBI_0001573"

    # equilibrium dissociation constant (KD) approximated by EC50
    OBI_0001581 = "OBI_0001581"
    EQUILIBRIUM_DISSOCIATION_CONSTANT__KD__APPROXIMATED_BY_EC50 = "OBI_0001581"

    # half life of binding datum
    OBI_0001583 = "OBI_0001583"
    HALF_LIFE_OF_BINDING_DATUM = "OBI_0001583"

    # direct binding assay
    OBI_0001591 = "OBI_0001591"
    DIRECT_BINDING_ASSAY = "OBI_0001591"

    # competitive inhibition of binding assay
    OBI_0001593 = "OBI_0001593"
    COMPETITIVE_INHIBITION_OF_BINDING_ASSAY = "OBI_0001593"

    # binding off rate measurement datum (koff)
    OBI_0001603 = "OBI_0001603"
    BINDING_OFF_RATE_MEASUREMENT_DATUM__KOFF_ = "OBI_0001603"

    # binding on rate measurement datum (kon)
    OBI_0001605 = "OBI_0001605"
    BINDING_ON_RATE_MEASUREMENT_DATUM__KON_ = "OBI_0001605"

    # analytical chromatography
    OBI_0001630 = "OBI_0001630"
    ANALYTICAL_CHROMATOGRAPHY = "OBI_0001630"

    # electron microscopy imaging assay
    OBI_0001631 = "OBI_0001631"
    ELECTRON_MICROSCOPY_IMAGING_ASSAY = "OBI_0001631"

    # immuno staining assay
    OBI_0001632 = "OBI_0001632"
    IMMUNO_STAINING_ASSAY = "OBI_0001632"

    # purified material
    OBI_0001633 = "OBI_0001633"
    PURIFIED_MATERIAL = "OBI_0001633"

    # calorimetric binding assay
    OBI_0001634 = "OBI_0001634"
    CALORIMETRIC_BINDING_ASSAY = "OBI_0001634"

    # antibody binding detection by fluorescence quenching
    OBI_0001635 = "OBI_0001635"
    ANTIBODY_BINDING_DETECTION_BY_FLUORESCENCE_QUENCHING = "OBI_0001635"

    # split-ubiquitin assay
    OBI_0001668 = "OBI_0001668"
    SPLIT_UBIQUITIN_ASSAY = "OBI_0001668"

    # far-Western blot assay
    OBI_0001669 = "OBI_0001669"
    FAR_WESTERN_BLOT_ASSAY = "OBI_0001669"

    # RNA protection assay
    OBI_0001670 = "OBI_0001670"
    RNA_PROTECTION_ASSAY = "OBI_0001670"

    # electrophoretic mobility shift assay
    OBI_0001671 = "OBI_0001671"
    ELECTROPHORETIC_MOBILITY_SHIFT_ASSAY = "OBI_0001671"

    # gene knock-down assay
    OBI_0001672 = "OBI_0001672"
    GENE_KNOCK_DOWN_ASSAY = "OBI_0001672"

    # nano-cap analysis of gene expression assay
    OBI_0001673 = "OBI_0001673"
    NANO_CAP_ANALYSIS_OF_GENE_EXPRESSION_ASSAY = "OBI_0001673"

    # cap analysis of gene expression assay
    OBI_0001674 = "OBI_0001674"
    CAP_ANALYSIS_OF_GENE_EXPRESSION_ASSAY = "OBI_0001674"

    # yeast 2-hybrid assay
    OBI_0001679 = "OBI_0001679"
    YEAST_2_HYBRID_ASSAY = "OBI_0001679"

    # yeast one-hybrid assay
    OBI_0001681 = "OBI_0001681"
    YEAST_ONE_HYBRID_ASSAY = "OBI_0001681"

    # bacterial one-hybrid assay
    OBI_0001682 = "OBI_0001682"
    BACTERIAL_ONE_HYBRID_ASSAY = "OBI_0001682"

    # chromosome organization assay by fluorescence in-situ hybridization
    OBI_0001683 = "OBI_0001683"
    CHROMOSOME_ORGANIZATION_ASSAY_BY_FLUORESCENCE_IN_SITU_HYBRIDIZATION = "OBI_0001683"

    # methylation-specific polymerase chain reaction assay
    OBI_0001684 = "OBI_0001684"
    METHYLATION_SPECIFIC_POLYMERASE_CHAIN_REACTION_ASSAY = "OBI_0001684"

    # amplification of intermethylated sites assay
    OBI_0001685 = "OBI_0001685"
    AMPLIFICATION_OF_INTERMETHYLATED_SITES_ASSAY = "OBI_0001685"

    # in-situ hybridization assay
    OBI_0001686 = "OBI_0001686"
    IN_SITU_HYBRIDIZATION_ASSAY = "OBI_0001686"

    # cytochalasin-induced inhibition of actin polymerization assay
    OBI_0001689 = "OBI_0001689"
    CYTOCHALASIN_INDUCED_INHIBITION_OF_ACTIN_POLYMERIZATION_ASSAY = "OBI_0001689"

    # cellular structure feature identification objective
    OBI_0001691 = "OBI_0001691"
    CELLULAR_STRUCTURE_FEATURE_IDENTIFICATION_OBJECTIVE = "OBI_0001691"

    # immunoprecipitation assay
    OBI_0001700 = "OBI_0001700"
    IMMUNOPRECIPITATION_ASSAY = "OBI_0001700"

    # immunoglobulin binding to epitope
    OBI_0001702 = "OBI_0001702"
    IMMUNOGLOBULIN_BINDING_TO_EPITOPE = "OBI_0001702"

    # paired-end library preparation
    OBI_0001852 = "OBI_0001852"
    PAIRED_END_LIBRARY_PREPARATION = "OBI_0001852"

    # methylation-sensitive restriction enzyme sequencing assay
    OBI_0001861 = "OBI_0001861"
    METHYLATION_SENSITIVE_RESTRICTION_ENZYME_SEQUENCING_ASSAY = "OBI_0001861"

    # assay array
    OBI_0001865 = "OBI_0001865"
    ASSAY_ARRAY = "OBI_0001865"

    # reagent
    OBI_0001879 = "OBI_0001879"
    REAGENT = "OBI_0001879"

    # cell freezing medium
    OBI_0001912 = "OBI_0001912"
    CELL_FREEZING_MEDIUM = "OBI_0001912"

    # multiplex ligation-mediated amplification
    OBI_0001914 = "OBI_0001914"
    MULTIPLEX_LIGATION_MEDIATED_AMPLIFICATION = "OBI_0001914"

    # chromosome conformation identification objective
    OBI_0001917 = "OBI_0001917"
    CHROMOSOME_CONFORMATION_IDENTIFICATION_OBJECTIVE = "OBI_0001917"

    # Carbon-copy chromosome conformation capture assay
    OBI_0001919 = "OBI_0001919"
    CARBON_COPY_CHROMOSOME_CONFORMATION_CAPTURE_ASSAY = "OBI_0001919"

    # chromatin immunoprecipitation with exonuclease sequencing assay
    OBI_0001925 = "OBI_0001925"
    CHROMATIN_IMMUNOPRECIPITATION_WITH_EXONUCLEASE_SEQUENCING_ASSAY = "OBI_0001925"

    # scalar value specification
    OBI_0001931 = "OBI_0001931"
    SCALAR_VALUE_SPECIFICATION = "OBI_0001931"

    # value specification
    OBI_0001933 = "OBI_0001933"
    VALUE_SPECIFICATION = "OBI_0001933"

    # molecular-labeled material
    OBI_0001936 = "OBI_0001936"
    MOLECULAR_LABELED_MATERIAL = "OBI_0001936"

    # has value specification
    OBI_0001938 = "OBI_0001938"
    HAS_VALUE_SPECIFICATION = "OBI_0001938"

    # ChIP assay
    OBI_0001954 = "OBI_0001954"
    CHIP_ASSAY = "OBI_0001954"

    # competitive binding reference ligand role
    OBI_0001955 = "OBI_0001955"
    COMPETITIVE_BINDING_REFERENCE_LIGAND_ROLE = "OBI_0001955"

    # assay using chromatin immunoprecipitation
    OBI_0001956 = "OBI_0001956"
    ASSAY_USING_CHROMATIN_IMMUNOPRECIPITATION = "OBI_0001956"

    # cytometry assay
    OBI_0001977 = "OBI_0001977"
    CYTOMETRY_ASSAY = "OBI_0001977"

    # fluorescence quenching binding assay
    OBI_0001979 = "OBI_0001979"
    FLUORESCENCE_QUENCHING_BINDING_ASSAY = "OBI_0001979"

    # microarray assay
    OBI_0001985 = "OBI_0001985"
    MICROARRAY_ASSAY = "OBI_0001985"

    # immunohistochemistry
    OBI_0001986 = "OBI_0001986"
    IMMUNOHISTOCHEMISTRY = "OBI_0001986"

    # epigenetic modification assay
    OBI_0002020 = "OBI_0002020"
    EPIGENETIC_MODIFICATION_ASSAY = "OBI_0002020"

    # peptide mass fingerprinting assay
    OBI_0002035 = "OBI_0002035"
    PEPTIDE_MASS_FINGERPRINTING_ASSAY = "OBI_0002035"

    # collection of specimens
    OBI_0002076 = "OBI_0002076"
    COLLECTION_OF_SPECIMENS = "OBI_0002076"

    # reporter gene assay
    OBI_0002082 = "OBI_0002082"
    REPORTER_GENE_ASSAY = "OBI_0002082"

    # physical store
    OBI_0002089 = "OBI_0002089"
    PHYSICAL_STORE = "OBI_0002089"

    # rapid amplification of cDNA ends
    OBI_0002090 = "OBI_0002090"
    RAPID_AMPLIFICATION_OF_CDNA_ENDS = "OBI_0002090"

    # high performance liquid chromotography assay
    OBI_0002116 = "OBI_0002116"
    HIGH_PERFORMANCE_LIQUID_CHROMOTOGRAPHY_ASSAY = "OBI_0002116"

    # microscopy assay
    OBI_0002119 = "OBI_0002119"
    MICROSCOPY_ASSAY = "OBI_0002119"

    # protein localization assay
    OBI_0002165 = "OBI_0002165"
    PROTEIN_LOCALIZATION_ASSAY = "OBI_0002165"

    # subcellular protein localization assay
    OBI_0002167 = "OBI_0002167"
    SUBCELLULAR_PROTEIN_LOCALIZATION_ASSAY = "OBI_0002167"

    # ChIP-qPCR assay
    OBI_0002169 = "OBI_0002169"
    CHIP_QPCR_ASSAY = "OBI_0002169"

    # dot blot assay
    OBI_0002171 = "OBI_0002171"
    DOT_BLOT_ASSAY = "OBI_0002171"

    # ATP bioluminescence assay
    OBI_0002175 = "OBI_0002175"
    ATP_BIOLUMINESCENCE_ASSAY = "OBI_0002175"

    # electrophysiology assay
    OBI_0002176 = "OBI_0002176"
    ELECTROPHYSIOLOGY_ASSAY = "OBI_0002176"

    # patch clamp assay
    OBI_0002177 = "OBI_0002177"
    PATCH_CLAMP_ASSAY = "OBI_0002177"

    # whole-cell patch clamp assay
    OBI_0002178 = "OBI_0002178"
    WHOLE_CELL_PATCH_CLAMP_ASSAY = "OBI_0002178"

    # cell-attached patch clamp assay
    OBI_0002179 = "OBI_0002179"
    CELL_ATTACHED_PATCH_CLAMP_ASSAY = "OBI_0002179"

    # inside-out patch clamp assay
    OBI_0002180 = "OBI_0002180"
    INSIDE_OUT_PATCH_CLAMP_ASSAY = "OBI_0002180"

    # outside-out patch clamp assay
    OBI_0002181 = "OBI_0002181"
    OUTSIDE_OUT_PATCH_CLAMP_ASSAY = "OBI_0002181"

    # electroencephalography
    OBI_0002186 = "OBI_0002186"
    ELECTROENCEPHALOGRAPHY = "OBI_0002186"

    # single-unit recording
    OBI_0002187 = "OBI_0002187"
    SINGLE_UNIT_RECORDING = "OBI_0002187"

    # local field potential recording
    OBI_0002189 = "OBI_0002189"
    LOCAL_FIELD_POTENTIAL_RECORDING = "OBI_0002189"

    # RNA interactome capture
    OBI_0002436 = "OBI_0002436"
    RNA_INTERACTOME_CAPTURE = "OBI_0002436"

    # nuclear ligation assay
    OBI_0002438 = "OBI_0002438"
    NUCLEAR_LIGATION_ASSAY = "OBI_0002438"

    # chromosome conformation capture assay
    OBI_0002439 = "OBI_0002439"
    CHROMOSOME_CONFORMATION_CAPTURE_ASSAY = "OBI_0002439"

    # Hi-C assay
    OBI_0002440 = "OBI_0002440"
    HI_C_ASSAY = "OBI_0002440"

    # measurand role
    OBI_0002444 = "OBI_0002444"
    MEASURAND_ROLE = "OBI_0002444"

    # suppression subtractive hybridization
    OBI_0002447 = "OBI_0002447"
    SUPPRESSION_SUBTRACTIVE_HYBRIDIZATION = "OBI_0002447"

    # differential screening hybridization
    OBI_0002448 = "OBI_0002448"
    DIFFERENTIAL_SCREENING_HYBRIDIZATION = "OBI_0002448"

    # brain specimen
    OBI_0002516 = "OBI_0002516"
    BRAIN_SPECIMEN = "OBI_0002516"

    # molecular interaction identification design
    OBI_0002590 = "OBI_0002590"
    MOLECULAR_INTERACTION_IDENTIFICATION_DESIGN = "OBI_0002590"

    # site-directed mutagenesis
    OBI_0002619 = "OBI_0002619"
    SITE_DIRECTED_MUTAGENESIS = "OBI_0002619"

    # random mutagenesis
    OBI_0002620 = "OBI_0002620"
    RANDOM_MUTAGENESIS = "OBI_0002620"

    # reconstitution assay
    OBI_0002621 = "OBI_0002621"
    RECONSTITUTION_ASSAY = "OBI_0002621"

    # in vitro transcription reconstitution assay
    OBI_0002622 = "OBI_0002622"
    IN_VITRO_TRANSCRIPTION_RECONSTITUTION_ASSAY = "OBI_0002622"

    # gene knockdown
    OBI_0002625 = "OBI_0002625"
    GENE_KNOCKDOWN = "OBI_0002625"

    # Epstein Barr virus transformed B cell
    OBI_0100010 = "OBI_0100010"
    EPSTEIN_BARR_VIRUS_TRANSFORMED_B_CELL = "OBI_0100010"

    # organism
    OBI_0100026 = "OBI_0100026"
    ORGANISM = "OBI_0100026"

    # specimen
    OBI_0100051 = "OBI_0100051"
    SPECIMEN = "OBI_0100051"

    # cultured cell population
    OBI_0100060 = "OBI_0100060"
    CULTURED_CELL_POPULATION = "OBI_0100060"

    # organ section
    OBI_0100066 = "OBI_0100066"
    ORGAN_SECTION = "OBI_0100066"

    # data transformation
    OBI_0200000 = "OBI_0200000"
    DATA_TRANSFORMATION = "OBI_0200000"

    # differential expression analysis objective
    OBI_0200031 = "OBI_0200031"
    DIFFERENTIAL_EXPRESSION_ANALYSIS_OBJECTIVE = "OBI_0200031"

    # mass spectrometry analysis
    OBI_0200085 = "OBI_0200085"
    MASS_SPECTROMETRY_ANALYSIS = "OBI_0200085"

    # data transformation objective
    OBI_0200166 = "OBI_0200166"
    DATA_TRANSFORMATION_OBJECTIVE = "OBI_0200166"

    # spectrum analysis objective
    OBI_0200197 = "OBI_0200197"
    SPECTRUM_ANALYSIS_OBJECTIVE = "OBI_0200197"

    # pool of specimens
    OBI_0302716 = "OBI_0302716"
    POOL_OF_SPECIMENS = "OBI_0302716"

    # chemical solution
    OBI_0302729 = "OBI_0302729"
    CHEMICAL_SOLUTION = "OBI_0302729"

    # solvent role
    OBI_0302732 = "OBI_0302732"
    SOLVENT_ROLE = "OBI_0302732"

    # solute role
    OBI_0302733 = "OBI_0302733"
    SOLUTE_ROLE = "OBI_0302733"

    # comet assay
    OBI_0302736 = "OBI_0302736"
    COMET_ASSAY = "OBI_0302736"

    # genetically modified organism
    OBI_0302859 = "OBI_0302859"
    GENETICALLY_MODIFIED_ORGANISM = "OBI_0302859"

    # dissolved material entity
    OBI_0302876 = "OBI_0302876"
    DISSOLVED_MATERIAL_ENTITY = "OBI_0302876"

    # extraction
    OBI_0302884 = "OBI_0302884"
    EXTRACTION = "OBI_0302884"

    # staining
    OBI_0302887 = "OBI_0302887"
    STAINING = "OBI_0302887"

    # polymerization
    OBI_0302890 = "OBI_0302890"
    POLYMERIZATION = "OBI_0302890"

    # enzymatic ligation
    OBI_0302892 = "OBI_0302892"
    ENZYMATIC_LIGATION = "OBI_0302892"

    # nucleic acid hybridization
    OBI_0302903 = "OBI_0302903"
    NUCLEIC_ACID_HYBRIDIZATION = "OBI_0302903"

    # elution
    OBI_0302905 = "OBI_0302905"
    ELUTION = "OBI_0302905"

    # flow cell
    OBI_0400043 = "OBI_0400043"
    FLOW_CELL = "OBI_0400043"

    # flow cytometer
    OBI_0400044 = "OBI_0400044"
    FLOW_CYTOMETER = "OBI_0400044"

    # light source
    OBI_0400065 = "OBI_0400065"
    LIGHT_SOURCE = "OBI_0400065"

    # obscuration bar
    OBI_0400078 = "OBI_0400078"
    OBSCURATION_BAR = "OBI_0400078"

    # optical filter
    OBI_0400079 = "OBI_0400079"
    OPTICAL_FILTER = "OBI_0400079"

    # photodetector
    OBI_0400082 = "OBI_0400082"
    PHOTODETECTOR = "OBI_0400082"

    # DNA sequencer
    OBI_0400103 = "OBI_0400103"
    DNA_SEQUENCER = "OBI_0400103"

    # hybridization chamber
    OBI_0400110 = "OBI_0400110"
    HYBRIDIZATION_CHAMBER = "OBI_0400110"

    # hybridization station
    OBI_0400111 = "OBI_0400111"
    HYBRIDIZATION_STATION = "OBI_0400111"

    # sonicator
    OBI_0400114 = "OBI_0400114"
    SONICATOR = "OBI_0400114"

    # spectrophotometer
    OBI_0400115 = "OBI_0400115"
    SPECTROPHOTOMETER = "OBI_0400115"

    # thermal cycler
    OBI_0400116 = "OBI_0400116"
    THERMAL_CYCLER = "OBI_0400116"

    # cytometer
    OBI_0400137 = "OBI_0400137"
    CYTOMETER = "OBI_0400137"

    # gel tank
    OBI_0400140 = "OBI_0400140"
    GEL_TANK = "OBI_0400140"

    # power supply
    OBI_0400142 = "OBI_0400142"
    POWER_SUPPLY = "OBI_0400142"

    # microarray
    OBI_0400147 = "OBI_0400147"
    MICROARRAY = "OBI_0400147"

    # DNA microarray
    OBI_0400148 = "OBI_0400148"
    DNA_MICROARRAY = "OBI_0400148"

    # protein microarray
    OBI_0400149 = "OBI_0400149"
    PROTEIN_MICROARRAY = "OBI_0400149"

    # droplet sorter
    OBI_0400153 = "OBI_0400153"
    DROPLET_SORTER = "OBI_0400153"

    # microtome
    OBI_0400168 = "OBI_0400168"
    MICROTOME = "OBI_0400168"

    # microscope
    OBI_0400169 = "OBI_0400169"
    MICROSCOPE = "OBI_0400169"

    # study design
    OBI_0500000 = "OBI_0500000"
    STUDY_DESIGN = "OBI_0500000"

    # clinical study design
    OBI_0500001 = "OBI_0500001"
    CLINICAL_STUDY_DESIGN = "OBI_0500001"

    # reference design
    OBI_0500010 = "OBI_0500010"
    REFERENCE_DESIGN = "OBI_0500010"

    # adding substance to cell culture
    OBI_0600000 = "OBI_0600000"
    ADDING_SUBSTANCE_TO_CELL_CULTURE = "OBI_0600000"

    # collecting specimen from organism
    OBI_0600005 = "OBI_0600005"
    COLLECTING_SPECIMEN_FROM_ORGANISM = "OBI_0600005"

    # administering substance in vivo
    OBI_0600007 = "OBI_0600007"
    ADMINISTERING_SUBSTANCE_IN_VIVO = "OBI_0600007"

    # material component separation
    OBI_0600014 = "OBI_0600014"
    MATERIAL_COMPONENT_SEPARATION = "OBI_0600014"

    # assay detecting a molecular label
    OBI_0600017 = "OBI_0600017"
    ASSAY_DETECTING_A_MOLECULAR_LABEL = "OBI_0600017"

    # histological assay
    OBI_0600020 = "OBI_0600020"
    HISTOLOGICAL_ASSAY = "OBI_0600020"

    # maintaining cell culture
    OBI_0600024 = "OBI_0600024"
    MAINTAINING_CELL_CULTURE = "OBI_0600024"

    # substance detection assay
    OBI_0600025 = "OBI_0600025"
    SUBSTANCE_DETECTION_ASSAY = "OBI_0600025"

    # artificially induced reverse transcription
    OBI_0600028 = "OBI_0600028"
    ARTIFICIALLY_INDUCED_REVERSE_TRANSCRIPTION = "OBI_0600028"

    # cell permeabilization
    OBI_0600033 = "OBI_0600033"
    CELL_PERMEABILIZATION = "OBI_0600033"

    # establishing cell culture
    OBI_0600036 = "OBI_0600036"
    ESTABLISHING_CELL_CULTURE = "OBI_0600036"

    # addition of molecular label
    OBI_0600038 = "OBI_0600038"
    ADDITION_OF_MOLECULAR_LABEL = "OBI_0600038"

    # genetic transformation
    OBI_0600043 = "OBI_0600043"
    GENETIC_TRANSFORMATION = "OBI_0600043"

    # 3D structure determination assay
    OBI_0600045 = "OBI_0600045"
    _3D_STRUCTURE_DETERMINATION_ASSAY = "OBI_0600045"

    # preparative chromatography
    OBI_0600046 = "OBI_0600046"
    PREPARATIVE_CHROMATOGRAPHY = "OBI_0600046"

    # sequencing assay
    OBI_0600047 = "OBI_0600047"
    SEQUENCING_ASSAY = "OBI_0600047"

    # specific enzymatic cleavage
    OBI_0600050 = "OBI_0600050"
    SPECIFIC_ENZYMATIC_CLEAVAGE = "OBI_0600050"

    # gradient separation
    OBI_0600051 = "OBI_0600051"
    GRADIENT_SEPARATION = "OBI_0600051"

    # electrophoresis
    OBI_0600053 = "OBI_0600053"
    ELECTROPHORESIS = "OBI_0600053"

    # selection by survival
    OBI_0600054 = "OBI_0600054"
    SELECTION_BY_SURVIVAL = "OBI_0600054"

    # DNA cleavage, restriction analysis
    OBI_0600055 = "OBI_0600055"
    DNA_CLEAVAGE__RESTRICTION_ANALYSIS = "OBI_0600055"

    # enzymatic amplification
    OBI_0600058 = "OBI_0600058"
    ENZYMATIC_AMPLIFICATION = "OBI_0600058"

    # recombinant vector cloning
    OBI_0600064 = "OBI_0600064"
    RECOMBINANT_VECTOR_CLONING = "OBI_0600064"

    # RNA extraction
    OBI_0666666 = "OBI_0666666"
    RNA_EXTRACTION = "OBI_0666666"

    # nucleic acid extraction
    OBI_0666667 = "OBI_0666667"
    NUCLEIC_ACID_EXTRACTION = "OBI_0666667"

    # phage display library
    OBI_1000029 = "OBI_1000029"
    PHAGE_DISPLAY_LIBRARY = "OBI_1000029"

    # transgenic organism
    OBI_1000048 = "OBI_1000048"
    TRANSGENIC_ORGANISM = "OBI_1000048"

    # epitope
    OBI_1110001 = "OBI_1110001"
    EPITOPE = "OBI_1110001"

    # epitope binding by adaptive immune receptor
    OBI_1110014 = "OBI_1110014"
    EPITOPE_BINDING_BY_ADAPTIVE_IMMUNE_RECEPTOR = "OBI_1110014"

    # infection process
    OBI_1110021 = "OBI_1110021"
    INFECTION_PROCESS = "OBI_1110021"

    # adaptive immune receptor
    OBI_1110022 = "OBI_1110022"
    ADAPTIVE_IMMUNE_RECEPTOR = "OBI_1110022"

    # experimental infection of cell culture
    OBI_1110030 = "OBI_1110030"
    EXPERIMENTAL_INFECTION_OF_CELL_CULTURE = "OBI_1110030"

    # antigen
    OBI_1110034 = "OBI_1110034"
    ANTIGEN = "OBI_1110034"

    # disposition to be bound by an adaptive immune receptor
    OBI_1110045 = "OBI_1110045"
    DISPOSITION_TO_BE_BOUND_BY_AN_ADAPTIVE_IMMUNE_RECEPTOR = "OBI_1110045"

    # disposition to infect an organism
    OBI_1110093 = "OBI_1110093"
    DISPOSITION_TO_INFECT_AN_ORGANISM = "OBI_1110093"

    # material to be added
    OBI_1110108 = "OBI_1110108"
    MATERIAL_TO_BE_ADDED = "OBI_1110108"

    # target of material addition
    OBI_1110109 = "OBI_1110109"
    TARGET_OF_MATERIAL_ADDITION = "OBI_1110109"

    # bound_to
    OBI_1110119 = "OBI_1110119"
    BOUND_TO = "OBI_1110119"

    # assay antigen role
    OBI_1110120 = "OBI_1110120"
    ASSAY_ANTIGEN_ROLE = "OBI_1110120"

    # pathologic process
    OBI_1110122 = "OBI_1110122"
    PATHOLOGIC_PROCESS = "OBI_1110122"

    # chromium release assay
    OBI_9999994 = "OBI_9999994"
    CHROMIUM_RELEASE_ASSAY = "OBI_9999994"

    # fluorescence
    PATO_0000018 = "PATO_0000018"
    FLUORESCENCE = "PATO_0000018"

    # mass
    PATO_0000125 = "PATO_0000125"
    MASS = "PATO_0000125"

    # viability
    PATO_0000169 = "PATO_0000169"
    VIABILITY = "PATO_0000169"

    # physical quality
    PATO_0001018 = "PATO_0001018"
    PHYSICAL_QUALITY = "PATO_0001018"

    # physical object quality
    PATO_0001241 = "PATO_0001241"
    PHYSICAL_OBJECT_QUALITY = "PATO_0001241"

    # electromagnetic (EM) radiation quality
    PATO_0001291 = "PATO_0001291"
    ELECTROMAGNETIC__EM__RADIATION_QUALITY = "PATO_0001291"

    # luminous flux
    PATO_0001296 = "PATO_0001296"
    LUMINOUS_FLUX = "PATO_0001296"

    # optical quality
    PATO_0001300 = "PATO_0001300"
    OPTICAL_QUALITY = "PATO_0001300"

    # alive
    PATO_0001421 = "PATO_0001421"
    ALIVE = "PATO_0001421"

    # dead
    PATO_0001422 = "PATO_0001422"
    DEAD = "PATO_0001422"

    # radiation quality
    PATO_0001739 = "PATO_0001739"
    RADIATION_QUALITY = "PATO_0001739"

    # activity (of a radionuclide)
    PATO_0001740 = "PATO_0001740"
    ACTIVITY__OF_A_RADIONUCLIDE_ = "PATO_0001740"

    # radioactive
    PATO_0001741 = "PATO_0001741"
    RADIOACTIVE = "PATO_0001741"

    # organismal quality
    PATO_0001995 = "PATO_0001995"
    ORGANISMAL_QUALITY = "PATO_0001995"

    # protein
    PR_000000001 = "PR_000000001"
    PROTEIN = "PR_000000001"

    # DNA ligase
    PR_000023089 = "PR_000023089"
    DNA_LIGASE = "PR_000023089"

    # nuclease S1
    PR_000025471 = "PR_000025471"
    NUCLEASE_S1 = "PR_000025471"

    # molecular label role
    REO_0000171 = "REO_0000171"
    MOLECULAR_LABEL_ROLE = "REO_0000171"

    # molecular label
    REO_0000280 = "REO_0000280"
    MOLECULAR_LABEL = "REO_0000280"

    # inheres in
    RO_0000052 = "RO_0000052"
    INHERES_IN = "RO_0000052"

    # bearer of
    RO_0000053 = "RO_0000053"
    BEARER_OF = "RO_0000053"

    # participates in
    RO_0000056 = "RO_0000056"
    PARTICIPATES_IN = "RO_0000056"

    # has participant
    RO_0000057 = "RO_0000057"
    HAS_PARTICIPANT = "RO_0000057"

    # is concretized as
    RO_0000058 = "RO_0000058"
    IS_CONCRETIZED_AS = "RO_0000058"

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

    # derives from
    RO_0001000 = "RO_0001000"
    DERIVES_FROM = "RO_0001000"

    # derives into
    RO_0001001 = "RO_0001001"
    DERIVES_INTO = "RO_0001001"

    # location of
    RO_0001015 = "RO_0001015"
    LOCATION_OF = "RO_0001015"

    # located in
    RO_0001025 = "RO_0001025"
    LOCATED_IN = "RO_0001025"

    # immediately preceded by
    RO_0002087 = "RO_0002087"
    IMMEDIATELY_PRECEDED_BY = "RO_0002087"

    # immediately precedes
    RO_0002090 = "RO_0002090"
    IMMEDIATELY_PRECEDES = "RO_0002090"

    # temporal relation
    RO_0002222 = "RO_0002222"
    TEMPORAL_RELATION = "RO_0002222"

    # member of
    RO_0002350 = "RO_0002350"
    MEMBER_OF = "RO_0002350"

    # has member
    RO_0002351 = "RO_0002351"
    HAS_MEMBER = "RO_0002351"

    # region
    SO_0000001 = "SO_0000001"
    REGION = "SO_0000001"

    # blood
    UBERON_0000178 = "UBERON_0000178"
    BLOOD = "UBERON_0000178"

    # organism substance
    UBERON_0000463 = "UBERON_0000463"
    ORGANISM_SUBSTANCE = "UBERON_0000463"

    # material anatomical entity
    UBERON_0000465 = "UBERON_0000465"
    MATERIAL_ANATOMICAL_ENTITY = "UBERON_0000465"

    # anatomical cluster
    UBERON_0000477 = "UBERON_0000477"
    ANATOMICAL_CLUSTER = "UBERON_0000477"

    # tissue
    UBERON_0000479 = "UBERON_0000479"
    TISSUE = "UBERON_0000479"

    # brain
    UBERON_0000955 = "UBERON_0000955"
    BRAIN = "UBERON_0000955"

    # urine
    UBERON_0001088 = "UBERON_0001088"
    URINE = "UBERON_0001088"

    # mass unit
    UO_0000002 = "UO_0000002"
    MASS_UNIT = "UO_0000002"

    # time unit
    UO_0000003 = "UO_0000003"
    TIME_UNIT = "UO_0000003"

    # concentration unit
    UO_0000051 = "UO_0000051"
    CONCENTRATION_UNIT = "UO_0000051"

    # has part
    has_part = "has_part"
    HAS_PART = "has_part"

    # negatively regulates
    negatively_regulates = "negatively_regulates"
    NEGATIVELY_REGULATES = "negatively_regulates"

    # part of
    part_of = "part_of"
    PART_OF = "part_of"

    # positively regulates
    positively_regulates = "positively_regulates"
    POSITIVELY_REGULATES = "positively_regulates"

    # regulates
    regulates = "regulates"
    REGULATES = "regulates"

    # used_in
    used_in = "used_in"
    USED_IN = "used_in"

    # uses
    uses = "uses"
    USES = "uses"


__all__ = [
    "ECO",
]
