# Working with composite annotations.

Composite annotations are semantic annotations that are comprised of multiple annotation
terms linked using  standard  qualifiers  (also  known  as  “relations”  or  “predicates”)
to  indicate  the  meaning  of  anannotation.
Composite annotations are used when a single knowledge resource term is not available to
sufficiently define a model or data element.  For model-component annotations,
composite annotations have two primary components:
1. the physical property represented by the annotated item (e.g., chemical concentration,
fluid volume) and
2. the physical entity, process, force, or dependency that bears the property (e.g., a pool
of ATP in the cytoplasm, blood in a cardiac cavity, the glucokinase reaction).



**entity** 
OPB: https://bioportal.bioontology.org/ontologies/OPB
Ontology of Physics for Biology

Molecular weight: OPB_01146; constant parameter
Concentration of chemical: OPB_00340

OBP: fluid volume; plasma;
similar to blood volume in vessel
portion of plasma (portion of blood)

dose
OBP: mass amount of chemical;

aborption rate: "Material flow rate"
Property first; entity second


**Properties of processes**  
- describe process: source, sink & mediator; flow of material from one pool to another
- to describe the source: stomach; sink
