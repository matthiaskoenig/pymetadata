"""KISAO ontology.

Generated from the ontology release by
`pymetadata.ontologies._ontology_builder`, do not edit.
"""

from pymetadata.ontologies.term import OntologyTerm, TermData

pattern = r"^KISAO_\d{7}$"


class KISAO(OntologyTerm):
    """KISAO ontology."""

    KISAO_0000000: "KISAO"
    """modelling and simulation algorithm: Algorithm used to instantiate a simulation from a mathematical model."""

    MODELLING_AND_SIMULATION_ALGORITHM: "KISAO"
    """modelling and simulation algorithm: Algorithm used to instantiate a simulation from a mathematical model."""

    KISAO_0000003: "KISAO"
    """weighted stochastic simulation algorithm: The weighted stochastic simulation algorithm manipulates the probabilities measure of biochemical systems by sampling, in order to increase the fraction of simulation runs exhibiting rare events."""

    WEIGHTED_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """weighted stochastic simulation algorithm: The weighted stochastic simulation algorithm manipulates the probabilities measure of biochemical systems by sampling, in order to increase the fraction of simulation runs exhibiting rare events."""

    KISAO_0000015: "KISAO"
    """Gillespie first reaction algorithm: Stochastic simulation algorithm using the reaction probability density function (next-reaction density function), giving the probability that the next reaction will happen in a given time interval. To choose the next reaction to fire, the algorithm calculates a tentative reaction time for each reaction and then select the smallest."""

    GILLESPIE_FIRST_REACTION_ALGORITHM: "KISAO"
    """Gillespie first reaction algorithm: Stochastic simulation algorithm using the reaction probability density function (next-reaction density function), giving the probability that the next reaction will happen in a given time interval. To choose the next reaction to fire, the algorithm calculates a tentative reaction time for each reaction and then select the smallest."""

    KISAO_0000017: "KISAO"
    """multi-state agent-based simulation method: The agent-based simulation method instantiates each molecule as an individual software object. The interactions between those objects are determined by interaction probabilities according to experimental data. The probability is depended on the state the molecule is in at that specific time (molecules have multiple-state). Additionally, ''pseudo-molecules'' are introduced to the system in order to simulate unimolecular reactions. For simulation, continuous time is broken down into discrete, independent ''slices''. During each time slice one molecule is selected randomly, a second molecule or pseudo-molecule is selected afterwards (leading to either a unimolecular or a bimolecular reaction). The reaction will only take place if a produced random number exceeds the reaction probability calculated beforehand. In that case, the system is updated after that reaction."""

    MULTI_STATE_AGENT_BASED_SIMULATION_METHOD: "KISAO"
    """multi-state agent-based simulation method: The agent-based simulation method instantiates each molecule as an individual software object. The interactions between those objects are determined by interaction probabilities according to experimental data. The probability is depended on the state the molecule is in at that specific time (molecules have multiple-state). Additionally, ''pseudo-molecules'' are introduced to the system in order to simulate unimolecular reactions. For simulation, continuous time is broken down into discrete, independent ''slices''. During each time slice one molecule is selected randomly, a second molecule or pseudo-molecule is selected afterwards (leading to either a unimolecular or a bimolecular reaction). The reaction will only take place if a produced random number exceeds the reaction probability calculated beforehand. In that case, the system is updated after that reaction."""

    KISAO_0000019: "KISAO"
    """CVODE: The CVODE is a package written in C that solves ODE initial value problems, in real N-space, written as y'=f(t,y), y(t0)=y0. It is capable for stiff and non-stiff systems and uses two different linear multi-step methods, namely the Adam-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] method and the backward differentiation formula [http://identifiers.org/biomodels.kisao/KISAO_0000288]."""

    CVODE: "KISAO"
    """CVODE: The CVODE is a package written in C that solves ODE initial value problems, in real N-space, written as y'=f(t,y), y(t0)=y0. It is capable for stiff and non-stiff systems and uses two different linear multi-step methods, namely the Adam-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] method and the backward differentiation formula [http://identifiers.org/biomodels.kisao/KISAO_0000288]."""

    KISAO_0000020: "KISAO"
    """PVODE: PVODE is a general-purpose solver for ordinary differential equation (ODE) systems that implements methods for both stiff and nonstiff systems. [...] In the stiff case, PVODE uses a backward differentiation formula method [http://identifiers.org/biomodels.kisao/KISAO_0000288] combined with preconditioned GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000253] iteration. Parallelism is achieved by distributing the ODE solution vector into user-specified segments and parallelizing a set of vector kernels accordingly. For PDE-based ODE systems, we provide a module that generates a band block-diagonal preconditioner for use with the GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000253] iteration. PVODE is based on CVODE [http://identifiers.org/biomodels.kisao/KISAO_0000019]."""

    PVODE: "KISAO"
    """PVODE: PVODE is a general-purpose solver for ordinary differential equation (ODE) systems that implements methods for both stiff and nonstiff systems. [...] In the stiff case, PVODE uses a backward differentiation formula method [http://identifiers.org/biomodels.kisao/KISAO_0000288] combined with preconditioned GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000253] iteration. Parallelism is achieved by distributing the ODE solution vector into user-specified segments and parallelizing a set of vector kernels accordingly. For PDE-based ODE systems, we provide a module that generates a band block-diagonal preconditioner for use with the GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000253] iteration. PVODE is based on CVODE [http://identifiers.org/biomodels.kisao/KISAO_0000019]."""

    KISAO_0000021: "KISAO"
    """StochSim nearest-neighbour algorithm: The nearest-neighbour algorithm allows for the representation of spatial information, by adding a two-dimensional lattice in the form of a probabilistic cellular automata. That way, nearest neighbour interactions do additionally influence reactions taking place in the systems. Reactions between entities are calculated using the agent-based simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000017]."""

    STOCHSIM_NEAREST_NEIGHBOUR_ALGORITHM: "KISAO"
    """StochSim nearest-neighbour algorithm: The nearest-neighbour algorithm allows for the representation of spatial information, by adding a two-dimensional lattice in the form of a probabilistic cellular automata. That way, nearest neighbour interactions do additionally influence reactions taking place in the systems. Reactions between entities are calculated using the agent-based simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000017]."""

    KISAO_0000022: "KISAO"
    """Elf and Ehrenberg method: Sub-volume stochastic reaction-diffusion method that is a combination of the Direct Method [http://identifiers.org/biomodels.kisao/KISAO_0000029] for sampling the time for a next reaction or diffusion event in each subvolume, with Gibson and Bruck's Next Reaction Method [http://identifiers.org/biomodels.kisao/KISAO_0000027], which is used to keep track of in which subvolume an event occurs next. The subvolumes are kept sorted in a queue, implemented as a binary tree, according to increasing time of the next event. When an event has occurred in the subvolume at the top of the queue, new event times need to be sampled only for one (the event is a chemical reaction) or two (the event is a diffusion jump) subvolume(s)."""

    ELF_AND_EHRENBERG_METHOD: "KISAO"
    """Elf and Ehrenberg method: Sub-volume stochastic reaction-diffusion method that is a combination of the Direct Method [http://identifiers.org/biomodels.kisao/KISAO_0000029] for sampling the time for a next reaction or diffusion event in each subvolume, with Gibson and Bruck's Next Reaction Method [http://identifiers.org/biomodels.kisao/KISAO_0000027], which is used to keep track of in which subvolume an event occurs next. The subvolumes are kept sorted in a queue, implemented as a binary tree, according to increasing time of the next event. When an event has occurred in the subvolume at the top of the queue, new event times need to be sampled only for one (the event is a chemical reaction) or two (the event is a diffusion jump) subvolume(s)."""

    KISAO_0000027: "KISAO"
    """Gibson-Bruck next reaction algorithm: As with the first reaction method [http://identifiers.org/biomodels.kisao/KISAO_0000015], a putative reaction time is calculated for each reaction, and the reaction with the shortest reaction time will be realized. However, the unused calculated reaction times are not wasted. The set of reactions is organized in a priority queue to allow for the efficient search for the fastest reaction. In addition, by using a so-called dependency graph only those reaction times are recalculated in each step, that are dependent on the reaction, which has been realized."""

    GIBSON_BRUCK_NEXT_REACTION_ALGORITHM: "KISAO"
    """Gibson-Bruck next reaction algorithm: As with the first reaction method [http://identifiers.org/biomodels.kisao/KISAO_0000015], a putative reaction time is calculated for each reaction, and the reaction with the shortest reaction time will be realized. However, the unused calculated reaction times are not wasted. The set of reactions is organized in a priority queue to allow for the efficient search for the fastest reaction. In addition, by using a so-called dependency graph only those reaction times are recalculated in each step, that are dependent on the reaction, which has been realized."""

    KISAO_0000028: "KISAO"
    """slow-scale stochastic simulation algorithm: Attempt to overcome the problem of stiff systems by developing an ''approximate theory that allows one to stochastically advance the system in time by simulating the firings of only the slow reaction events''."""

    SLOW_SCALE_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """slow-scale stochastic simulation algorithm: Attempt to overcome the problem of stiff systems by developing an ''approximate theory that allows one to stochastically advance the system in time by simulating the firings of only the slow reaction events''."""

    KISAO_0000029: "KISAO"
    """Gillespie direct algorithm: Stochastic simulation algorithm using the reaction probability density function (next-reaction density function), giving the probability that the next reaction will happen in a given time interval. To choose the next reaction to fire, the algorithm directly and separately calculates the identity of the reaction and the time it will fire."""

    GILLESPIE_DIRECT_ALGORITHM: "KISAO"
    """Gillespie direct algorithm: Stochastic simulation algorithm using the reaction probability density function (next-reaction density function), giving the probability that the next reaction will happen in a given time interval. To choose the next reaction to fire, the algorithm directly and separately calculates the identity of the reaction and the time it will fire."""

    KISAO_0000030: "KISAO"
    """Euler forward method: The Euler method is an explicit one-step method for the numerical integration of ODES with a given initial value. The calculation of the next integration step at time t+1 is based on the state of the system at time point t."""

    EULER_FORWARD_METHOD: "KISAO"
    """Euler forward method: The Euler method is an explicit one-step method for the numerical integration of ODES with a given initial value. The calculation of the next integration step at time t+1 is based on the state of the system at time point t."""

    KISAO_0000031: "KISAO"
    """Euler backward method: The Euler backward method is an implicit one-step method for the numerical integration of ODES with a given initial value. The next state of a system is calculated by solving an equation that considers both, the current state of the system and the later one."""

    EULER_BACKWARD_METHOD: "KISAO"
    """Euler backward method: The Euler backward method is an implicit one-step method for the numerical integration of ODES with a given initial value. The next state of a system is calculated by solving an equation that considers both, the current state of the system and the later one."""

    KISAO_0000032: "KISAO"
    """explicit fourth-order Runge-Kutta method: The Runge-Kutta method is a method for the numerical integration of ODES with a given initial value. The calculation of the next integration step at time t+1 is based on the state of the system at time point t, plus the product of the size of the interval and an estimated slope. The slope is a weighted average of 4 single slope points (beginning of interval-midpoint-midpoint-end of interval)."""

    EXPLICIT_FOURTH_ORDER_RUNGE_KUTTA_METHOD: "KISAO"
    """explicit fourth-order Runge-Kutta method: The Runge-Kutta method is a method for the numerical integration of ODES with a given initial value. The calculation of the next integration step at time t+1 is based on the state of the system at time point t, plus the product of the size of the interval and an estimated slope. The slope is a weighted average of 4 single slope points (beginning of interval-midpoint-midpoint-end of interval)."""

    KISAO_0000033: "KISAO"
    """Rosenbrock method: Some general implicit processes are given for the solution of simultaneous first-order differential equations. These processes, which use successive substitution, are implicit analogues of the (explicit) Runge-Kutta processes. They require the solution in each time step of one or more set of simultaneous linear equations, usually of a special and simple form. Processes of any required order can be devised, and they can be made to have a wide margin of stability when applied to a linear problem."""

    ROSENBROCK_METHOD: "KISAO"
    """Rosenbrock method: Some general implicit processes are given for the solution of simultaneous first-order differential equations. These processes, which use successive substitution, are implicit analogues of the (explicit) Runge-Kutta processes. They require the solution in each time step of one or more set of simultaneous linear equations, usually of a special and simple form. Processes of any required order can be devised, and they can be made to have a wide margin of stability when applied to a linear problem."""

    KISAO_0000038: "KISAO"
    """sorting stochastic simulation algorithm: In order to overcome the problem of high complexity of the stochastic simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000029] when simulating large systems, the sorting direct method maintains a loosely sorted order of the reactions as the simulation executes."""

    SORTING_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """sorting stochastic simulation algorithm: In order to overcome the problem of high complexity of the stochastic simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000029] when simulating large systems, the sorting direct method maintains a loosely sorted order of the reactions as the simulation executes."""

    KISAO_0000039: "KISAO"
    """tau-leaping method: Approximate acceleration procedure of the stochastic simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000029] that divides the time into subintervals and ''leaps'' from one to another, firing all the reaction events in each subinterval."""

    TAU_LEAPING_METHOD: "KISAO"
    """tau-leaping method: Approximate acceleration procedure of the stochastic simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000029] that divides the time into subintervals and ''leaps'' from one to another, firing all the reaction events in each subinterval."""

    KISAO_0000040: "KISAO"
    """Poisson tau-leaping method: Explicit tau-leaping method with basic pre leap check."""

    POISSON_TAU_LEAPING_METHOD: "KISAO"
    """Poisson tau-leaping method: Explicit tau-leaping method with basic pre leap check."""

    KISAO_0000045: "KISAO"
    """implicit tau-leaping method: Contrary to the explicit tau-leaping [http://identifiers.org/biomodels.kisao/KISAO_0000039 and http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000239] , the implicit tau-leaping allows for much larger time-steps when simulating stiff systems."""

    IMPLICIT_TAU_LEAPING_METHOD: "KISAO"
    """implicit tau-leaping method: Contrary to the explicit tau-leaping [http://identifiers.org/biomodels.kisao/KISAO_0000039 and http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000239] , the implicit tau-leaping allows for much larger time-steps when simulating stiff systems."""

    KISAO_0000046: "KISAO"
    """trapezoidal tau-leaping method: Formula for accelerated discrete efficient stochastic simulation of chemically reacting system [which] has better accuracy and stiff stability properties than the explicit and implicit [http://identifiers.org/biomodels.kisao/KISAO_0000045] tau-leaping formulas for discrete stochastic systems, and it limits to the trapezoidal rule in the deterministic regime."""

    TRAPEZOIDAL_TAU_LEAPING_METHOD: "KISAO"
    """trapezoidal tau-leaping method: Formula for accelerated discrete efficient stochastic simulation of chemically reacting system [which] has better accuracy and stiff stability properties than the explicit and implicit [http://identifiers.org/biomodels.kisao/KISAO_0000045] tau-leaping formulas for discrete stochastic systems, and it limits to the trapezoidal rule in the deterministic regime."""

    KISAO_0000048: "KISAO"
    """adaptive explicit-implicit tau-leaping method: Modification of the original tau-selection strategy [http://identifiers.org/biomodels.kisao/KISAO_0000040], designed for explicit tau-leaping, is modified to apply to implicit tau-leaping, allowing for longer steps when the system is stiff. Further, an adaptive strategy is proposed that identifies stiffness and automatically chooses between the explicit and the (new) implicit tau-selection methods to achieve better efficiency."""

    ADAPTIVE_EXPLICIT_IMPLICIT_TAU_LEAPING_METHOD: "KISAO"
    """adaptive explicit-implicit tau-leaping method: Modification of the original tau-selection strategy [http://identifiers.org/biomodels.kisao/KISAO_0000040], designed for explicit tau-leaping, is modified to apply to implicit tau-leaping, allowing for longer steps when the system is stiff. Further, an adaptive strategy is proposed that identifies stiffness and automatically chooses between the explicit and the (new) implicit tau-selection methods to achieve better efficiency."""

    KISAO_0000051: "KISAO"
    """Bortz-Kalos-Lebowitz algorithm: The Bortz-Kalos-Lebowitz (or: kinetic Monte-Carlo-) method is a stochastic method for the simulation of time evolution of processes using (pseudo-)random numbers."""

    BORTZ_KALOS_LEBOWITZ_ALGORITHM: "KISAO"
    """Bortz-Kalos-Lebowitz algorithm: The Bortz-Kalos-Lebowitz (or: kinetic Monte-Carlo-) method is a stochastic method for the simulation of time evolution of processes using (pseudo-)random numbers."""

    KISAO_0000056: "KISAO"
    """Smoluchowski equation based method: Method based on the Smoluchowski equation."""

    SMOLUCHOWSKI_EQUATION_BASED_METHOD: "KISAO"
    """Smoluchowski equation based method: Method based on the Smoluchowski equation."""

    KISAO_0000057: "KISAO"
    """Brownian diffusion Smoluchowski method: In the Brownian diffusion Smoluchowski method, ''each molecule is treated as a point-like particle that diffuses freely in three-dimensional space. When a pair of reactive molecules collide, such as an enzyme and its substrate, a reaction occurs and the simulated reactants are replaced by products. [..] Analytic solutions are presented for some simulation parameters while others are calculated using look-up tables''. Supported chemical processes include molecular diffusion, treatment of surfaces, zeroth-order-, unimolecular-, and bimolecular reactions."""

    BROWNIAN_DIFFUSION_SMOLUCHOWSKI_METHOD: "KISAO"
    """Brownian diffusion Smoluchowski method: In the Brownian diffusion Smoluchowski method, ''each molecule is treated as a point-like particle that diffuses freely in three-dimensional space. When a pair of reactive molecules collide, such as an enzyme and its substrate, a reaction occurs and the simulated reactants are replaced by products. [..] Analytic solutions are presented for some simulation parameters while others are calculated using look-up tables''. Supported chemical processes include molecular diffusion, treatment of surfaces, zeroth-order-, unimolecular-, and bimolecular reactions."""

    KISAO_0000058: "KISAO"
    """Greens function reaction dynamics: Method that simulates biochemical networks on particle level. It considers both changes in time and space by ''exploiting both the exact solution of the Smoluchowski Equation to set up an event-driven algorithm'' which allows for large jumps in time when the considered particles are far away from each other [in space] and thus cannot react. GFRD combines the propagation of particles in space with the reactions taking place between them in one simulation step."""

    GREENS_FUNCTION_REACTION_DYNAMICS: "KISAO"
    """Greens function reaction dynamics: Method that simulates biochemical networks on particle level. It considers both changes in time and space by ''exploiting both the exact solution of the Smoluchowski Equation to set up an event-driven algorithm'' which allows for large jumps in time when the considered particles are far away from each other [in space] and thus cannot react. GFRD combines the propagation of particles in space with the reactions taking place between them in one simulation step."""

    KISAO_0000064: "KISAO"
    """Runge-Kutta based method: A method of numerically integrating ordinary differential equations, which uses a sampling of slopes through an interval and takes a weighted average to determine the right end point. This averaging gives a very accurate approximation."""

    RUNGE_KUTTA_BASED_METHOD: "KISAO"
    """Runge-Kutta based method: A method of numerically integrating ordinary differential equations, which uses a sampling of slopes through an interval and takes a weighted average to determine the right end point. This averaging gives a very accurate approximation."""

    KISAO_0000068: "KISAO"
    """deterministic cellular automata update algorithm: A cellular automaton is a discrete model of a regular grid of cells with a finite number of dimensions. Each cell has a finite number of defined states. The automaton changes its state in a discrete manner, meaning that the state of a cell at time t is determined by a function of the states of its neighbours at time t - 1. These neighbours are a selection of cells relative to the specified cell. Famous examples for deterministic cellular automata are Conway's game of life or Wolfram's elementary cellular automata."""

    DETERMINISTIC_CELLULAR_AUTOMATA_UPDATE_ALGORITHM: "KISAO"
    """deterministic cellular automata update algorithm: A cellular automaton is a discrete model of a regular grid of cells with a finite number of dimensions. Each cell has a finite number of defined states. The automaton changes its state in a discrete manner, meaning that the state of a cell at time t is determined by a function of the states of its neighbours at time t - 1. These neighbours are a selection of cells relative to the specified cell. Famous examples for deterministic cellular automata are Conway's game of life or Wolfram's elementary cellular automata."""

    KISAO_0000071: "KISAO"
    """LSODE: LSODE solves stiff and nonstiff systems of the form dy/dt = f. In the stiff case, it treats the Jacobian matrix sf/dy as either a dense (full) or a banded matrix, and as either user-supplied or internally approximated by difference quotients. It uses Adams methods (predictor-corrector) [http://identifiers.org/biomodels.kisao/KISAO_0000364] in the nonstiff case, and Backward Differentiation Formula (BDF) methods (the Gear methods) [http://identifiers.org/biomodels.kisao/KISAO_0000288] in the stiff case."""

    LSODE: "KISAO"
    """LSODE: LSODE solves stiff and nonstiff systems of the form dy/dt = f. In the stiff case, it treats the Jacobian matrix sf/dy as either a dense (full) or a banded matrix, and as either user-supplied or internally approximated by difference quotients. It uses Adams methods (predictor-corrector) [http://identifiers.org/biomodels.kisao/KISAO_0000364] in the nonstiff case, and Backward Differentiation Formula (BDF) methods (the Gear methods) [http://identifiers.org/biomodels.kisao/KISAO_0000288] in the stiff case."""

    KISAO_0000074: "KISAO"
    """binomial tau-leaping method: Coarse grained modified version of the next subvolume method [http://identifiers.org/biomodels.kisao/KISAO_0000022] that allows the user to consider both diffusion and reaction events in relatively long simulation time spans as compared with the original method and other commonly used fully stochastic computational methods."""

    BINOMIAL_TAU_LEAPING_METHOD: "KISAO"
    """binomial tau-leaping method: Coarse grained modified version of the next subvolume method [http://identifiers.org/biomodels.kisao/KISAO_0000022] that allows the user to consider both diffusion and reaction events in relatively long simulation time spans as compared with the original method and other commonly used fully stochastic computational methods."""

    KISAO_0000075: "KISAO"
    """Gillespie multi-particle method: Combination of the multiparticle method for diffusion [http://identifiers.org/biomodels.kisao/KISAO_0000334] and the SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029]."""

    GILLESPIE_MULTI_PARTICLE_METHOD: "KISAO"
    """Gillespie multi-particle method: Combination of the multiparticle method for diffusion [http://identifiers.org/biomodels.kisao/KISAO_0000334] and the SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029]."""

    KISAO_0000076: "KISAO"
    """Stundzia and Lumsden method: Sub-volume stochastic reaction-diffusion method that using Green's function to link the bulk diffusion coefficient D in Fick's differential law to the corresponding transition rate probability for diffusion of a particle between finite volume elements. This generalized stochastic algorithm enables to numerically calculate the time evolution of a spatially inhomogeneous mixture of reaction-diffusion species in a finite volume. The time step is stochastic and is generated by a probability distribution determined by the intrinsic reaction kinetics and diffusion dynamics."""

    STUNDZIA_AND_LUMSDEN_METHOD: "KISAO"
    """Stundzia and Lumsden method: Sub-volume stochastic reaction-diffusion method that using Green's function to link the bulk diffusion coefficient D in Fick's differential law to the corresponding transition rate probability for diffusion of a particle between finite volume elements. This generalized stochastic algorithm enables to numerically calculate the time evolution of a spatially inhomogeneous mixture of reaction-diffusion species in a finite volume. The time step is stochastic and is generated by a probability distribution determined by the intrinsic reaction kinetics and diffusion dynamics."""

    KISAO_0000081: "KISAO"
    """estimated midpoint tau-leaping method: Estimated-Midpoint tau-Leap Method: For the selected leaping time tau which satisfies the Leap Condition, compute the expected state change lambda' = tau sumj( aj(x)vj ) during [t, t + tau). Then, with x' =x + [lambda'/2], generate for each j = 1,...,M a sample value kj of the Poisson random variable P(aj(x'), tau). Compute the actual state change, lambda = sumj( kjvj ), and effect the leap by replacing t by t + tau and x by x + lambda."""

    ESTIMATED_MIDPOINT_TAU_LEAPING_METHOD: "KISAO"
    """estimated midpoint tau-leaping method: Estimated-Midpoint tau-Leap Method: For the selected leaping time tau which satisfies the Leap Condition, compute the expected state change lambda' = tau sumj( aj(x)vj ) during [t, t + tau). Then, with x' =x + [lambda'/2], generate for each j = 1,...,M a sample value kj of the Poisson random variable P(aj(x'), tau). Compute the actual state change, lambda = sumj( kjvj ), and effect the leap by replacing t by t + tau and x by x + lambda."""

    KISAO_0000082: "KISAO"
    """k-alpha leaping method: Alternative to the tau-leaping [http://identifiers.org/biomodels.kisao/KISAO_0000039], where one leaps a fixed number of reaction-events."""

    K_ALPHA_LEAPING_METHOD: "KISAO"
    """k-alpha leaping method: Alternative to the tau-leaping [http://identifiers.org/biomodels.kisao/KISAO_0000039], where one leaps a fixed number of reaction-events."""

    KISAO_0000084: "KISAO"
    """nonnegative Poisson tau-leaping method: The explicit tau-leaping procedure attempts to speed up the stochastic simulation of a chemically reacting system by approximating the number of firings of each reaction channel during a chosen time increment Tau as a Poisson random variable. Since the Poisson random variable can have arbitrarily large sample values, there is always the possibility that this procedure will cause one or more reaction channels to fire so many times during Tau that the population of some reactant species will be driven negative. Two recent papers have shown how that unacceptable occurrence can be avoided by replacing the Poisson random variables with binomial random variables, whose values are naturally bounded. This paper describes a modified Poisson tau-leaping procedure that also avoids negative populations, but is easier to implement than the binomial procedure. The new Poisson procedure also introduces a second control parameter, whose value essentially dials the procedure from the original Poisson tau-leaping at one extreme to the exact stochastic simulation algorithm at the other; therefore, the modified Poisson procedure will generally be more accurate than the original Poisson procedure [http://identifiers.org/biomodels.kisao/KISAO_0000040]."""

    NONNEGATIVE_POISSON_TAU_LEAPING_METHOD: "KISAO"
    """nonnegative Poisson tau-leaping method: The explicit tau-leaping procedure attempts to speed up the stochastic simulation of a chemically reacting system by approximating the number of firings of each reaction channel during a chosen time increment Tau as a Poisson random variable. Since the Poisson random variable can have arbitrarily large sample values, there is always the possibility that this procedure will cause one or more reaction channels to fire so many times during Tau that the population of some reactant species will be driven negative. Two recent papers have shown how that unacceptable occurrence can be avoided by replacing the Poisson random variables with binomial random variables, whose values are naturally bounded. This paper describes a modified Poisson tau-leaping procedure that also avoids negative populations, but is easier to implement than the binomial procedure. The new Poisson procedure also introduces a second control parameter, whose value essentially dials the procedure from the original Poisson tau-leaping at one extreme to the exact stochastic simulation algorithm at the other; therefore, the modified Poisson procedure will generally be more accurate than the original Poisson procedure [http://identifiers.org/biomodels.kisao/KISAO_0000040]."""

    KISAO_0000086: "KISAO"
    """Fehlberg method: The method was developed by the German mathematician Erwin Fehlberg and is based on the class of Runge-Kutta methods. The Runge-Kutta-Fehlberg method uses an O(h4) method together with an O(h5) method that uses all of the points of the O(h4) method, and hence is often referred to as an RKF45 method. Similar schemes with different orders have since been developed. By performing one extra calculation that would be required for an RK5 method, the error in the solution can be estimated and controlled and an appropriate step size can be determined automatically, making this method efficient for ordinary problems of automated numerical integration of ordinary differential equations."""

    FEHLBERG_METHOD: "KISAO"
    """Fehlberg method: The method was developed by the German mathematician Erwin Fehlberg and is based on the class of Runge-Kutta methods. The Runge-Kutta-Fehlberg method uses an O(h4) method together with an O(h5) method that uses all of the points of the O(h4) method, and hence is often referred to as an RKF45 method. Similar schemes with different orders have since been developed. By performing one extra calculation that would be required for an RK5 method, the error in the solution can be estimated and controlled and an appropriate step size can be determined automatically, making this method efficient for ordinary problems of automated numerical integration of ordinary differential equations."""

    KISAO_0000087: "KISAO"
    """Dormand-Prince method: Dormand-Prince is an explicit method for the numerical integration of ODES with a given initial value. It is an 'embedded Runge-Kutta method' [http://identifiers.org/biomodels.kisao/KISAO_0000302] RK5 (4) which (a) has a 'small' principal truncation term in the Fifth order and (b) has an extended region of absolute stability."""

    DORMAND_PRINCE_METHOD: "KISAO"
    """Dormand-Prince method: Dormand-Prince is an explicit method for the numerical integration of ODES with a given initial value. It is an 'embedded Runge-Kutta method' [http://identifiers.org/biomodels.kisao/KISAO_0000302] RK5 (4) which (a) has a 'small' principal truncation term in the Fifth order and (b) has an extended region of absolute stability."""

    KISAO_0000088: "KISAO"
    """LSODA: LSODA solves systems dy/dt = f with a dense or banded Jacobian when the problem is stiff, but it automatically selects between non-stiff (Adams [http://identifiers.org/biomodels.kisao/KISAO_0000289]) and stiff (BDF [http://identifiers.org/biomodels.kisao/KISAO_0000288]) methods. It uses the non-stiff method initially, and dynamically monitors data in order to decide which method to use."""

    LSODA: "KISAO"
    """LSODA: LSODA solves systems dy/dt = f with a dense or banded Jacobian when the problem is stiff, but it automatically selects between non-stiff (Adams [http://identifiers.org/biomodels.kisao/KISAO_0000289]) and stiff (BDF [http://identifiers.org/biomodels.kisao/KISAO_0000288]) methods. It uses the non-stiff method initially, and dynamically monitors data in order to decide which method to use."""

    KISAO_0000089: "KISAO"
    """LSODAR: LSODAR is a variant of LSODA [http://identifiers.org/biomodels.kisao/KISAO_0000088] with a root finding capability added. Thus it solves problems dy/dt = f with dense or banded Jacobian and automatic method selection, and at the same time, it finds the roots of any of a set of given functions of the form g(t,y). This is often useful for finding stop conditions, or for finding points at which a switch is to be made in the function f."""

    LSODAR: "KISAO"
    """LSODAR: LSODAR is a variant of LSODA [http://identifiers.org/biomodels.kisao/KISAO_0000088] with a root finding capability added. Thus it solves problems dy/dt = f with dense or banded Jacobian and automatic method selection, and at the same time, it finds the roots of any of a set of given functions of the form g(t,y). This is often useful for finding stop conditions, or for finding points at which a switch is to be made in the function f."""

    KISAO_0000090: "KISAO"
    """LSODI: LSODI solves systems given in linearly implicit form, including differential-algebraic systems."""

    LSODI: "KISAO"
    """LSODI: LSODI solves systems given in linearly implicit form, including differential-algebraic systems."""

    KISAO_0000091: "KISAO"
    """LSODIS: LSODIS is a set of general-purpose FORTRAN routines solver for the initial value problem for ordinary differential equation systems. It is suitable for both stiff and nonstiff systems. LSODIS treat systems in the linearly implicit form A(t,y) dy/dt = g(t,y), A = a square matrix, i.e. with the derivative dy/dt implicit, but linearly so."""

    LSODIS: "KISAO"
    """LSODIS: LSODIS is a set of general-purpose FORTRAN routines solver for the initial value problem for ordinary differential equation systems. It is suitable for both stiff and nonstiff systems. LSODIS treat systems in the linearly implicit form A(t,y) dy/dt = g(t,y), A = a square matrix, i.e. with the derivative dy/dt implicit, but linearly so."""

    KISAO_0000093: "KISAO"
    """LSODPK: LSODPK is a set of FORTRAN subroutines for solving the initial value problem for stiff and nonstiff systems of ordinary differential equations. In solving stiff systems, LSODPK uses a corrector iteration composed of Newton iteration and one of four preconditioned Krylov subspace iteration methods [http://identifiers.org/biomodels.kisao/KISAO_0000354]. The user must select the desired Krylov method and supply a pair of routine to evaluate, preprocess, and solve the (left and/or right) preconditioner matrices. Aside from preconditioning, the implementation is matrix-free, meaning that explicit storage of the Jacobian (or related) matrix is not required. The method is experimental because the scope of problems for which it is effective is not well-known, and users are forewarned that LSODPK may or may not be competitive with traditional methods on a given problem. LSODPK also includes an option for a user-supplied linear system solver to be used without Krylov iteration."""

    LSODPK: "KISAO"
    """LSODPK: LSODPK is a set of FORTRAN subroutines for solving the initial value problem for stiff and nonstiff systems of ordinary differential equations. In solving stiff systems, LSODPK uses a corrector iteration composed of Newton iteration and one of four preconditioned Krylov subspace iteration methods [http://identifiers.org/biomodels.kisao/KISAO_0000354]. The user must select the desired Krylov method and supply a pair of routine to evaluate, preprocess, and solve the (left and/or right) preconditioner matrices. Aside from preconditioning, the implementation is matrix-free, meaning that explicit storage of the Jacobian (or related) matrix is not required. The method is experimental because the scope of problems for which it is effective is not well-known, and users are forewarned that LSODPK may or may not be competitive with traditional methods on a given problem. LSODPK also includes an option for a user-supplied linear system solver to be used without Krylov iteration."""

    KISAO_0000094: "KISAO"
    """Livermore solver: Method to solve ordinary differential equations developed at the Lawrence Livermore National Laboratory."""

    LIVERMORE_SOLVER: "KISAO"
    """Livermore solver: Method to solve ordinary differential equations developed at the Lawrence Livermore National Laboratory."""

    KISAO_0000095: "KISAO"
    """sub-volume stochastic reaction-diffusion algorithm: Stochastic method using a combination of discretisation of compartment volumes into voxels and Gillespie-like algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000241] to simulate the evolution of the system."""

    SUB_VOLUME_STOCHASTIC_REACTION_DIFFUSION_ALGORITHM: "KISAO"
    """sub-volume stochastic reaction-diffusion algorithm: Stochastic method using a combination of discretisation of compartment volumes into voxels and Gillespie-like algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000241] to simulate the evolution of the system."""

    KISAO_0000097: "KISAO"
    """modelling and simulation algorithm characteristic: Simulation algorithm property, which can, for example, describe the model, such as the type of variables (discrete or continuous), and information on the treatment of spatial descriptions, or can be a numerical characteristic, such as the system's behaviour (deterministic or stochastic) as well as the progression mechanism (fixed or adaptive time steps)."""

    MODELLING_AND_SIMULATION_ALGORITHM_CHARACTERISTIC: "KISAO"
    """modelling and simulation algorithm characteristic: Simulation algorithm property, which can, for example, describe the model, such as the type of variables (discrete or continuous), and information on the treatment of spatial descriptions, or can be a numerical characteristic, such as the system's behaviour (deterministic or stochastic) as well as the progression mechanism (fixed or adaptive time steps)."""

    KISAO_0000098: "KISAO"
    """type of variable: Type of variables used for the simulation."""

    TYPE_OF_VARIABLE: "KISAO"
    """type of variable: Type of variables used for the simulation."""

    KISAO_0000099: "KISAO"
    """type of system behaviour: A characteristic describing the rules the algorithm uses to simulate the temporal evolution of a system, specifically whether or not the final state is uniquely determined from a precise initial state."""

    TYPE_OF_SYSTEM_BEHAVIOUR: "KISAO"
    """type of system behaviour: A characteristic describing the rules the algorithm uses to simulate the temporal evolution of a system, specifically whether or not the final state is uniquely determined from a precise initial state."""

    KISAO_0000100: "KISAO"
    """type of progression time step: Type of time steps used by the algorithm."""

    TYPE_OF_PROGRESSION_TIME_STEP: "KISAO"
    """type of progression time step: Type of time steps used by the algorithm."""

    KISAO_0000102: "KISAO"
    """spatial description: Algorithm, possessing this characteristic, takes into account the location of the reacting components."""

    SPATIAL_DESCRIPTION: "KISAO"
    """spatial description: Algorithm, possessing this characteristic, takes into account the location of the reacting components."""

    KISAO_0000103: "KISAO"
    """deterministic system behaviour: Algorithm, possessing this characteristic, simulates the temporal evolution of a system deterministically, so that from a precise initial state the algorithm will always end up in the same final state."""

    DETERMINISTIC_SYSTEM_BEHAVIOUR: "KISAO"
    """deterministic system behaviour: Algorithm, possessing this characteristic, simulates the temporal evolution of a system deterministically, so that from a precise initial state the algorithm will always end up in the same final state."""

    KISAO_0000104: "KISAO"
    """stochastic system behaviour: Algorithm, possessing this characteristic, simulates the temporal evolution of a system using probabilistic rules, so that between two simulations, the same precise initial state may result in a different final state."""

    STOCHASTIC_SYSTEM_BEHAVIOUR: "KISAO"
    """stochastic system behaviour: Algorithm, possessing this characteristic, simulates the temporal evolution of a system using probabilistic rules, so that between two simulations, the same precise initial state may result in a different final state."""

    KISAO_0000105: "KISAO"
    """discrete variable: Algorithm, possessing this characteristic, allows values of system's variables to change by discrete (integral) amounts."""

    DISCRETE_VARIABLE: "KISAO"
    """discrete variable: Algorithm, possessing this characteristic, allows values of system's variables to change by discrete (integral) amounts."""

    KISAO_0000106: "KISAO"
    """continuous variable: Algorithm, possessing this characteristic, allows the values of a system's variables to change by continuous (non-integral) amounts."""

    CONTINUOUS_VARIABLE: "KISAO"
    """continuous variable: Algorithm, possessing this characteristic, allows the values of a system's variables to change by continuous (non-integral) amounts."""

    KISAO_0000107: "KISAO"
    """progression with adaptive time step: Algorithm, possessing this characteristic, does not use fixed time steps to update the state of a system during the whole simulation, but on the contrary adapts the length of the time steps to the local situation."""

    PROGRESSION_WITH_ADAPTIVE_TIME_STEP: "KISAO"
    """progression with adaptive time step: Algorithm, possessing this characteristic, does not use fixed time steps to update the state of a system during the whole simulation, but on the contrary adapts the length of the time steps to the local situation."""

    KISAO_0000108: "KISAO"
    """progression with fixed time step: Algorithm, possessing this characteristic, uses time steps of constant length to update the state of a system during the whole simulation."""

    PROGRESSION_WITH_FIXED_TIME_STEP: "KISAO"
    """progression with fixed time step: Algorithm, possessing this characteristic, uses time steps of constant length to update the state of a system during the whole simulation."""

    KISAO_0000201: "KISAO"
    """modelling and simulation algorithm parameter: Parameter that can be used in the simulation experiment settings."""

    MODELLING_AND_SIMULATION_ALGORITHM_PARAMETER: "KISAO"
    """modelling and simulation algorithm parameter: Parameter that can be used in the simulation experiment settings."""

    KISAO_0000203: "KISAO"
    """particle number lower limit: This parameter of 'Pahle hybrid method' [http://identifiers.org/biomodels.kisao/KISAO_0000231] is a double value specifying the lower limit for particle numbers. Species with a particle number below this value are considered as having a low particle number. The 'particle number lower limit' cannot be higher than the 'particle number upper limit' [http://identifiers.org/biomodels.kisao/KISAO_0000204]."""

    PARTICLE_NUMBER_LOWER_LIMIT: "KISAO"
    """particle number lower limit: This parameter of 'Pahle hybrid method' [http://identifiers.org/biomodels.kisao/KISAO_0000231] is a double value specifying the lower limit for particle numbers. Species with a particle number below this value are considered as having a low particle number. The 'particle number lower limit' cannot be higher than the 'particle number upper limit' [http://identifiers.org/biomodels.kisao/KISAO_0000204]."""

    KISAO_0000204: "KISAO"
    """particle number upper limit: This parameter of 'Pahle hybrid method' [http://identifiers.org/biomodels.kisao/KISAO_0000231] is a double value specifying the upper limit for particle numbers. Species with a particle number above this value are considered as having a high particle number. The 'particle number upper limit' cannot be lower than the 'particle number lower limit' [http://identifiers.org/biomodels.kisao/KISAO_0000203]."""

    PARTICLE_NUMBER_UPPER_LIMIT: "KISAO"
    """particle number upper limit: This parameter of 'Pahle hybrid method' [http://identifiers.org/biomodels.kisao/KISAO_0000231] is a double value specifying the upper limit for particle numbers. Species with a particle number above this value are considered as having a high particle number. The 'particle number upper limit' cannot be lower than the 'particle number lower limit' [http://identifiers.org/biomodels.kisao/KISAO_0000203]."""

    KISAO_0000205: "KISAO"
    """partitioning interval: This positive integer value specifies after how many steps the internal partitioning of the system should be recalculated."""

    PARTITIONING_INTERVAL: "KISAO"
    """partitioning interval: This positive integer value specifies after how many steps the internal partitioning of the system should be recalculated."""

    KISAO_0000209: "KISAO"
    """relative tolerance: This parameter is a numeric value specifying the desired relative tolerance the user wants to achieve. A smaller value means that the trajectory is calculated more accurately."""

    RELATIVE_TOLERANCE: "KISAO"
    """relative tolerance: This parameter is a numeric value specifying the desired relative tolerance the user wants to achieve. A smaller value means that the trajectory is calculated more accurately."""

    KISAO_0000211: "KISAO"
    """absolute tolerance: This parameter is a positive numeric value specifying the desired absolute tolerance the user wants to achieve."""

    ABSOLUTE_TOLERANCE: "KISAO"
    """absolute tolerance: This parameter is a positive numeric value specifying the desired absolute tolerance the user wants to achieve."""

    KISAO_0000216: "KISAO"
    """use reduced model: Boolean value which indicates whether the simulation/analysis should be performed using the complete model or an equivalent reduced model. Reduced models can be determined in many ways such as using mass conservation laws."""

    USE_REDUCED_MODEL: "KISAO"
    """use reduced model: Boolean value which indicates whether the simulation/analysis should be performed using the complete model or an equivalent reduced model. Reduced models can be determined in many ways such as using mass conservation laws."""

    KISAO_0000219: "KISAO"
    """maximum Adams order: This parameter is a positive integer value specifying the maximal order the non-stiff Adams integration method [http://identifiers.org/biomodels.kisao/KISAO_0000289] shall attempt before switching to the stiff BDF method [http://identifiers.org/biomodels.kisao/KISAO_0000288]."""

    MAXIMUM_ADAMS_ORDER: "KISAO"
    """maximum Adams order: This parameter is a positive integer value specifying the maximal order the non-stiff Adams integration method [http://identifiers.org/biomodels.kisao/KISAO_0000289] shall attempt before switching to the stiff BDF method [http://identifiers.org/biomodels.kisao/KISAO_0000288]."""

    KISAO_0000220: "KISAO"
    """maximum BDF order: This parameter is a positive integer value specifying the maximal order the stiff BDF integration method [http://identifiers.org/biomodels.kisao/KISAO_0000288] shall attempt before switching to smaller internal step sizes."""

    MAXIMUM_BDF_ORDER: "KISAO"
    """maximum BDF order: This parameter is a positive integer value specifying the maximal order the stiff BDF integration method [http://identifiers.org/biomodels.kisao/KISAO_0000288] shall attempt before switching to smaller internal step sizes."""

    KISAO_0000223: "KISAO"
    """number of history bins: The 'number of history bins' is only enabled for models that contain delayed or multistep reactions for specifying the granularity with which the delayed reaction solver should retain the history of species values, for species that participate in delayed reactions."""

    NUMBER_OF_HISTORY_BINS: "KISAO"
    """number of history bins: The 'number of history bins' is only enabled for models that contain delayed or multistep reactions for specifying the granularity with which the delayed reaction solver should retain the history of species values, for species that participate in delayed reactions."""

    KISAO_0000228: "KISAO"
    """tau-leaping epsilon: The leap condition is chosen such that the expected change in the propensity function aj(x) is bounded by Epsilon * a0 where Epsilon is an error control parameter between 0 and 1. This parameter is the basic error control mechanism for the Tau-Leaping algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000039]. As Epsilon decreases the leaps become shorter and the simulation is more accurate."""

    TAU_LEAPING_EPSILON: "KISAO"
    """tau-leaping epsilon: The leap condition is chosen such that the expected change in the propensity function aj(x) is bounded by Epsilon * a0 where Epsilon is an error control parameter between 0 and 1. This parameter is the basic error control mechanism for the Tau-Leaping algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000039]. As Epsilon decreases the leaps become shorter and the simulation is more accurate."""

    KISAO_0000230: "KISAO"
    """minimum reactions per leap: 'minimum reactions per leap' parameter is used in hybrid methods, which adaptively switch between the tau-leaping algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000039] to the SSA Direct Method [http://identifiers.org/biomodels.kisao/KISAO_0000029] when the number of reactions in a single tau-leaping leap step is less than the threshold."""

    MINIMUM_REACTIONS_PER_LEAP: "KISAO"
    """minimum reactions per leap: 'minimum reactions per leap' parameter is used in hybrid methods, which adaptively switch between the tau-leaping algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000039] to the SSA Direct Method [http://identifiers.org/biomodels.kisao/KISAO_0000029] when the number of reactions in a single tau-leaping leap step is less than the threshold."""

    KISAO_0000231: "KISAO"
    """Pahle hybrid method: The hybrid method combines the stochastic 'Gibson-Bruck's next reaction method' [http://identifiers.org/biomodels.kisao/KISAO_0000027] with different algorithms for the numerical integration of ODEs [http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000374]. The biochemical network is dynamically partitioned into a deterministic and a stochastic subnet depending on the current particle numbers in the system. The user can define limits for when a particle number should be considered low or high. The stochastic subnet contains reactions involving low numbered species as substrate or product. All the other reactions form the deterministic subnet. The two subnets are then simulated in parallel using the stochastic and deterministic solver, respectively. The reaction probabilities in the stochastic subnet are approximated as constant between two stochastic reaction events."""

    PAHLE_HYBRID_METHOD: "KISAO"
    """Pahle hybrid method: The hybrid method combines the stochastic 'Gibson-Bruck's next reaction method' [http://identifiers.org/biomodels.kisao/KISAO_0000027] with different algorithms for the numerical integration of ODEs [http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000374]. The biochemical network is dynamically partitioned into a deterministic and a stochastic subnet depending on the current particle numbers in the system. The user can define limits for when a particle number should be considered low or high. The stochastic subnet contains reactions involving low numbered species as substrate or product. All the other reactions form the deterministic subnet. The two subnets are then simulated in parallel using the stochastic and deterministic solver, respectively. The reaction probabilities in the stochastic subnet are approximated as constant between two stochastic reaction events."""

    KISAO_0000232: "KISAO"
    """LSOIBT: LSOIBT solves linearly implicit systems in which the matrices involved are all assumed to be block-tridiagonal. Linear systems are solved by the LU method."""

    LSOIBT: "KISAO"
    """LSOIBT: LSOIBT solves linearly implicit systems in which the matrices involved are all assumed to be block-tridiagonal. Linear systems are solved by the LU method."""

    KISAO_0000233: "KISAO"
    """LSODES: LSODES solves systems dy/dt = f and in the stiff case treats the Jacobian matrix in general sparse form. It determines the sparsity structure on its own, or optionally accepts this information from the user. It then uses parts of the Yale Sparse Matrix Package (YSMP) to solve the linear systems that arise, by a sparse (direct) LU factorization/backsolve method."""

    LSODES: "KISAO"
    """LSODES: LSODES solves systems dy/dt = f and in the stiff case treats the Jacobian matrix in general sparse form. It determines the sparsity structure on its own, or optionally accepts this information from the user. It then uses parts of the Yale Sparse Matrix Package (YSMP) to solve the linear systems that arise, by a sparse (direct) LU factorization/backsolve method."""

    KISAO_0000234: "KISAO"
    """LSODKR: LSODKR is an initial value ODE solver for stiff and nonstiff systems. It is a variant of the LSODPK [http://identifiers.org/biomodels.kisao/KISAO_0000093] and LSODE [http://identifiers.org/biomodels.kisao/KISAO_0000071] solvers, intended mainly for large stiff systems. The main differences between LSODKR and LSODE [http://identifiers.org/biomodels.kisao/KISAO_0000071] are the following: a) for stiff systems, LSODKR uses a corrector iteration composed of Newton iteration and one of four preconditioned Krylov subspace iteration methods. The user must supply routines for the preconditioning operations, b) within the corrector iteration, LSODKR does automatic switching between functional (fixpoint) iteration and modified Newton iteration, c) LSODKR includes the ability to find roots of given functions of the solution during the integration."""

    LSODKR: "KISAO"
    """LSODKR: LSODKR is an initial value ODE solver for stiff and nonstiff systems. It is a variant of the LSODPK [http://identifiers.org/biomodels.kisao/KISAO_0000093] and LSODE [http://identifiers.org/biomodels.kisao/KISAO_0000071] solvers, intended mainly for large stiff systems. The main differences between LSODKR and LSODE [http://identifiers.org/biomodels.kisao/KISAO_0000071] are the following: a) for stiff systems, LSODKR uses a corrector iteration composed of Newton iteration and one of four preconditioned Krylov subspace iteration methods. The user must supply routines for the preconditioning operations, b) within the corrector iteration, LSODKR does automatic switching between functional (fixpoint) iteration and modified Newton iteration, c) LSODKR includes the ability to find roots of given functions of the solution during the integration."""

    KISAO_0000235: "KISAO"
    """type of solution: A characteristic describing the type of the solution produced by the method, specifically whether it is exact or approximate."""

    TYPE_OF_SOLUTION: "KISAO"
    """type of solution: A characteristic describing the type of the solution produced by the method, specifically whether it is exact or approximate."""

    KISAO_0000236: "KISAO"
    """exact solution: Algorithm, possessing this characteristic, provides an exact solution to the initial problem."""

    EXACT_SOLUTION: "KISAO"
    """exact solution: Algorithm, possessing this characteristic, provides an exact solution to the initial problem."""

    KISAO_0000237: "KISAO"
    """approximate solution: Approximation algorithms are algorithms used to find approximate solutions to optimization problems. Approximation algorithms are often associated with NP-hard problems; since it is unlikely that there can ever be efficient polynomial time exact algorithms solving NP-hard problems, one settles for polynomial time sub-optimal solutions. Unlike heuristics, which usually only find reasonably good solutions reasonably fast, one wants provable solution quality and provable run time bounds. Ideally, the approximation is optimal up to a small constant factor (for instance within 5% of the optimal solution). Approximation algorithms are increasingly being used for problems where exact polynomial-time algorithms are known but are too expensive due to the input size."""

    APPROXIMATE_SOLUTION: "KISAO"
    """approximate solution: Approximation algorithms are algorithms used to find approximate solutions to optimization problems. Approximation algorithms are often associated with NP-hard problems; since it is unlikely that there can ever be efficient polynomial time exact algorithms solving NP-hard problems, one settles for polynomial time sub-optimal solutions. Unlike heuristics, which usually only find reasonably good solutions reasonably fast, one wants provable solution quality and provable run time bounds. Ideally, the approximation is optimal up to a small constant factor (for instance within 5% of the optimal solution). Approximation algorithms are increasingly being used for problems where exact polynomial-time algorithms are known but are too expensive due to the input size."""

    KISAO_0000238: "KISAO"
    """type of method: A characteristic describing the way the method finds a solution, specifically whether it solves an equation involving only the current state of the system (explicit) or both the current and the later one (implicit)."""

    TYPE_OF_METHOD: "KISAO"
    """type of method: A characteristic describing the way the method finds a solution, specifically whether it solves an equation involving only the current state of the system (explicit) or both the current and the later one (implicit)."""

    KISAO_0000239: "KISAO"
    """explicit method type: Explicit methods calculate the state of a system at a later time from the state of the system at the current time. Mathematically, if Y(t) is the current system state and Y((t+delta t) is the state at the later time (delta t is a small time step), then, for an explicit method Y(t+delta t) = F(Y(t)), to find Y(t+delta t)."""

    EXPLICIT_METHOD_TYPE: "KISAO"
    """explicit method type: Explicit methods calculate the state of a system at a later time from the state of the system at the current time. Mathematically, if Y(t) is the current system state and Y((t+delta t) is the state at the later time (delta t is a small time step), then, for an explicit method Y(t+delta t) = F(Y(t)), to find Y(t+delta t)."""

    KISAO_0000240: "KISAO"
    """implicit method type: Implicit methods find a solution by solving an equation involving both the current state of the system and the later one. Mathematically, if Y(t) is the current system state and Y((t+delta t) is the state at the later time (delta t is a small time step), then, for an implicit method one solves an equation G(Y(t), Y(t+delta t))=0, to find Y(t+delta t)."""

    IMPLICIT_METHOD_TYPE: "KISAO"
    """implicit method type: Implicit methods find a solution by solving an equation involving both the current state of the system and the later one. Mathematically, if Y(t) is the current system state and Y((t+delta t) is the state at the later time (delta t is a small time step), then, for an implicit method one solves an equation G(Y(t), Y(t+delta t))=0, to find Y(t+delta t)."""

    KISAO_0000241: "KISAO"
    """Gillespie-like method: Stochastic simulation algorithm using an approach alike the one described in Gillespie's papers of 1976 and 1977."""

    GILLESPIE_LIKE_METHOD: "KISAO"
    """Gillespie-like method: Stochastic simulation algorithm using an approach alike the one described in Gillespie's papers of 1976 and 1977."""

    KISAO_0000242: "KISAO"
    """error control parameter: Parameter controlling method accuracy."""

    ERROR_CONTROL_PARAMETER: "KISAO"
    """error control parameter: Parameter controlling method accuracy."""

    KISAO_0000243: "KISAO"
    """method switching control parameter: Parameters describing threshold conditions for algorithms that switch between different methods."""

    METHOD_SWITCHING_CONTROL_PARAMETER: "KISAO"
    """method switching control parameter: Parameters describing threshold conditions for algorithms that switch between different methods."""

    KISAO_0000244: "KISAO"
    """granularity control parameter: Parameter controlling granularity."""

    GRANULARITY_CONTROL_PARAMETER: "KISAO"
    """granularity control parameter: Parameter controlling granularity."""

    KISAO_0000245: "KISAO"
    """has characteristic."""

    HAS_CHARACTERISTIC: "KISAO"
    """has characteristic."""

    KISAO_0000246: "KISAO"
    """is hybrid of."""

    IS_HYBRID_OF: "KISAO"
    """is hybrid of."""

    KISAO_0000248: "KISAO"
    """tau-leaping delta: Tau-leaping delta specifies how close two symmetric transition rates must be before we classify them as in partial-equilibrium. Only applies to the implicit tau routine [http://identifiers.org/biomodels.kisao/KISAO_0000045]."""

    TAU_LEAPING_DELTA: "KISAO"
    """tau-leaping delta: Tau-leaping delta specifies how close two symmetric transition rates must be before we classify them as in partial-equilibrium. Only applies to the implicit tau routine [http://identifiers.org/biomodels.kisao/KISAO_0000045]."""

    KISAO_0000249: "KISAO"
    """critical firing threshold: The 'nonnegative Poisson tau-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000084] is based on the fact that negative populations typically arise from multiple firings of reactions that are only a few firings away from consuming all the molecules of one of their reactants. To focus on those reaction channels, the modified tau-leaping algorithm introduces a second control parameter nc, a positive integer that is usually set somewhere between 5 and 20. Any reaction channel with a positive propensity function that is currently within nc firings of exhausting one of its reactants is then classified as a critical reaction. The modified algorithm chooses tau in such a way that no more than one firing of all the critical reactions can occur during the leap."""

    CRITICAL_FIRING_THRESHOLD: "KISAO"
    """critical firing threshold: The 'nonnegative Poisson tau-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000084] is based on the fact that negative populations typically arise from multiple firings of reactions that are only a few firings away from consuming all the molecules of one of their reactants. To focus on those reaction channels, the modified tau-leaping algorithm introduces a second control parameter nc, a positive integer that is usually set somewhere between 5 and 20. Any reaction channel with a positive propensity function that is currently within nc firings of exhausting one of its reactants is then classified as a critical reaction. The modified algorithm chooses tau in such a way that no more than one firing of all the critical reactions can occur during the leap."""

    KISAO_0000250: "KISAO"
    """is parameter of."""

    IS_PARAMETER_OF: "KISAO"
    """is parameter of."""

    KISAO_0000252: "KISAO"
    """partitioning control parameter."""

    PARTITIONING_CONTROL_PARAMETER: "KISAO"
    """partitioning control parameter."""

    KISAO_0000253: "KISAO"
    """coarse-graining factor: The time in each Monte-Carlo iteration of 'binomial tau-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000074] is updated with the time increments tau=f/(a1+a2+...+aM). Here 1/(a1+a2+...+aM) is the averaged microscopic increment of the SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] and f is a coarse-graining factor, controlling the speed-up."""

    COARSE_GRAINING_FACTOR: "KISAO"
    """coarse-graining factor: The time in each Monte-Carlo iteration of 'binomial tau-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000074] is updated with the time increments tau=f/(a1+a2+...+aM). Here 1/(a1+a2+...+aM) is the averaged microscopic increment of the SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] and f is a coarse-graining factor, controlling the speed-up."""

    KISAO_0000254: "KISAO"
    """Brownian diffusion accuracy: Accuracy code of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057], which sets which neighbouring boxes are checked for potential bi-molecular reactions. Consider the reaction A + B -> C and suppose that A and B are within a binding radius of each other. This reaction will always be performed if A and B are in the same virtual box. If accuracy is set to at least 3, then it will also occur if A and B are in nearest-neighbour virtual boxes. If it is at least 7, then the reaction will happen if they are in nearest-neighbour boxes that are separated by periodic boundary conditions. And if it is 9 or 10, then all edge and corner boxes are checked for reactions, which means that no potential reactions are overlooked."""

    BROWNIAN_DIFFUSION_ACCURACY: "KISAO"
    """Brownian diffusion accuracy: Accuracy code of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057], which sets which neighbouring boxes are checked for potential bi-molecular reactions. Consider the reaction A + B -> C and suppose that A and B are within a binding radius of each other. This reaction will always be performed if A and B are in the same virtual box. If accuracy is set to at least 3, then it will also occur if A and B are in nearest-neighbour virtual boxes. If it is at least 7, then the reaction will happen if they are in nearest-neighbour boxes that are separated by periodic boundary conditions. And if it is 9 or 10, then all edge and corner boxes are checked for reactions, which means that no potential reactions are overlooked."""

    KISAO_0000255: "KISAO"
    """molecules per virtual box: Target molecules per virtual box is a parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057], which sets the box sizes so that the average number of molecules per box, at simulation initiation, is close to the requested number."""

    MOLECULES_PER_VIRTUAL_BOX: "KISAO"
    """molecules per virtual box: Target molecules per virtual box is a parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057], which sets the box sizes so that the average number of molecules per box, at simulation initiation, is close to the requested number."""

    KISAO_0000256: "KISAO"
    """virtual box side length: The 'virtual box side length' is a parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. It requests the length of one side of a box."""

    VIRTUAL_BOX_SIDE_LENGTH: "KISAO"
    """virtual box side length: The 'virtual box side length' is a parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. It requests the length of one side of a box."""

    KISAO_0000257: "KISAO"
    """surface-bound epsilon: A parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. Molecules that are bound to a surface are given locations that are extremely close to that surface. However, this position does not need to be exactly at the surface, and in fact it usually cannot be exactly at the surface due to round-off error. The tolerance for how far a surface-bound molecule is allowed to be away from the surface can be set with the epsilon statement."""

    SURFACE_BOUND_EPSILON: "KISAO"
    """surface-bound epsilon: A parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. Molecules that are bound to a surface are given locations that are extremely close to that surface. However, this position does not need to be exactly at the surface, and in fact it usually cannot be exactly at the surface due to round-off error. The tolerance for how far a surface-bound molecule is allowed to be away from the surface can be set with the epsilon statement."""

    KISAO_0000258: "KISAO"
    """neighbour distance: A parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. When a surface-bound molecule diffuses off of one surface panel, it can sometimes diffuse onto the neighbouring surface tile. It does so only if the neighbouring panel is declared to be a neighbour and also the neighbour is within a distance that is set with the neighbour distance statement."""

    NEIGHBOUR_DISTANCE: "KISAO"
    """neighbour distance: A parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. When a surface-bound molecule diffuses off of one surface panel, it can sometimes diffuse onto the neighbouring surface tile. It does so only if the neighbouring panel is declared to be a neighbour and also the neighbour is within a distance that is set with the neighbour distance statement."""

    KISAO_0000259: "KISAO"
    """has parameter."""

    HAS_PARAMETER: "KISAO"
    """has parameter."""

    KISAO_0000260: "KISAO"
    """virtual box size: Target size of virtual boxes for 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]."""

    VIRTUAL_BOX_SIZE: "KISAO"
    """virtual box size: Target size of virtual boxes for 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]."""

    KISAO_0000261: "KISAO"
    """Euler method: The Euler method, named after Leonhard Euler, is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value."""

    EULER_METHOD: "KISAO"
    """Euler method: The Euler method, named after Leonhard Euler, is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value."""

    KISAO_0000263: "KISAO"
    """NFSim agent-based simulation method: A generalization a rule-based version of 'Gillespie's direct method' (SSA) [http://identifiers.org/biomodels.kisao/KISAO_0000029]. The method is guaranteed to produce the same results as the exact SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] by cycling over three primary steps. First, NFsim calculates the probability or propensity for each rule to take effect given the current molecular states. Second, it samples the time to the next reaction event and selects the corresponding reaction rule. Finally, NFsim executes the selected reaction by applying the rule and updating the molecular agents accordingly."""

    NFSIM_AGENT_BASED_SIMULATION_METHOD: "KISAO"
    """NFSim agent-based simulation method: A generalization a rule-based version of 'Gillespie's direct method' (SSA) [http://identifiers.org/biomodels.kisao/KISAO_0000029]. The method is guaranteed to produce the same results as the exact SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] by cycling over three primary steps. First, NFsim calculates the probability or propensity for each rule to take effect given the current molecular states. Second, it samples the time to the next reaction event and selects the corresponding reaction rule. Finally, NFsim executes the selected reaction by applying the rule and updating the molecular agents accordingly."""

    KISAO_0000264: "KISAO"
    """cellular automata update method: Cellular automata are mathematical idealizations of physical systems in which space and time are discrete, and physical quantities take on a finite set of discrete values. A cellular automaton consists of a regular uniform lattice (or ''array''), usually infinite in extent, with a discrete variable at each site (''cell''). A cellular automaton evolves in discrete time steps, with the value of the variable at one site being affected by the values of variables at sites in its ''neighbourhood'' on the previous time step. The neighbourhood of a site is typically taken to be the site itself and all immediately adjacent sites. The variables at each site are updated simultaneously (''synchronously''), based on the values of the variables in their neighbourhood at the preceding time step, and according to a definite set of ''local rules''."""

    CELLULAR_AUTOMATA_UPDATE_METHOD: "KISAO"
    """cellular automata update method: Cellular automata are mathematical idealizations of physical systems in which space and time are discrete, and physical quantities take on a finite set of discrete values. A cellular automaton consists of a regular uniform lattice (or ''array''), usually infinite in extent, with a discrete variable at each site (''cell''). A cellular automaton evolves in discrete time steps, with the value of the variable at one site being affected by the values of variables at sites in its ''neighbourhood'' on the previous time step. The neighbourhood of a site is typically taken to be the site itself and all immediately adjacent sites. The variables at each site are updated simultaneously (''synchronously''), based on the values of the variables in their neighbourhood at the preceding time step, and according to a definite set of ''local rules''."""

    KISAO_0000268: "KISAO"
    """is characteristic of."""

    IS_CHARACTERISTIC_OF: "KISAO"
    """is characteristic of."""

    KISAO_0000273: "KISAO"
    """hard-particle molecular dynamics: A collision-driven molecular dynamics algorithm for a system of non-spherical particles."""

    HARD_PARTICLE_MOLECULAR_DYNAMICS: "KISAO"
    """hard-particle molecular dynamics: A collision-driven molecular dynamics algorithm for a system of non-spherical particles."""

    KISAO_0000274: "KISAO"
    """first-passage Monte Carlo algorithm: We present a novel Monte Carlo algorithm for N diffusing finite particles that react on collisions. Using the theory of first-passage processes and time dependent Green's functions, we break the difficult N-body problem into independent single- and two-body propagations circumventing numerous diffusion hops used in standard Monte Carlo simulations. The new algorithm is exact, extremely efficient, and applicable to many important physical situations in arbitrary integer dimensions."""

    FIRST_PASSAGE_MONTE_CARLO_ALGORITHM: "KISAO"
    """first-passage Monte Carlo algorithm: We present a novel Monte Carlo algorithm for N diffusing finite particles that react on collisions. Using the theory of first-passage processes and time dependent Green's functions, we break the difficult N-body problem into independent single- and two-body propagations circumventing numerous diffusion hops used in standard Monte Carlo simulations. The new algorithm is exact, extremely efficient, and applicable to many important physical situations in arbitrary integer dimensions."""

    KISAO_0000276: "KISAO"
    """Gill method: Gill's fourth order method is a Runge-Kutta method for approximating the solution of the initial value problem y'(x) = f(x,y); y(x0) = y0 which evaluates the integrand,f(x,y), four times per step. This method is a fourth order procedure for which Richardson extrapolation can be used."""

    GILL_METHOD: "KISAO"
    """Gill method: Gill's fourth order method is a Runge-Kutta method for approximating the solution of the initial value problem y'(x) = f(x,y); y(x0) = y0 which evaluates the integrand,f(x,y), four times per step. This method is a fourth order procedure for which Richardson extrapolation can be used."""

    KISAO_0000278: "KISAO"
    """Metropolis Monte Carlo algorithm: A general method, suitable for fast computing machines, for investigating such properties as equations of state for substances consisting of interacting individual molecules is described. The method consists of a modified Monte Carlo integration [http://identifiers.org/biomodels.kisao/KISAO_0000051] over configuration space."""

    METROPOLIS_MONTE_CARLO_ALGORITHM: "KISAO"
    """Metropolis Monte Carlo algorithm: A general method, suitable for fast computing machines, for investigating such properties as equations of state for substances consisting of interacting individual molecules is described. The method consists of a modified Monte Carlo integration [http://identifiers.org/biomodels.kisao/KISAO_0000051] over configuration space."""

    KISAO_0000279: "KISAO"
    """Adams-Bashforth method: Given an initial value problem: y' = f(x,y), y(x0) = y0 together with additional starting values y1 = y(x0 + h), . . . , yk-1 = y(x0 + (k-1) h) the k-step Adams-Bashforth method is an explicit linear multistep method that approximates the solution, y(x) at x = x0+kh, of the initial value problem by yk = yk - 1 + h * ( a0 f(xk - 1,yk - 1) + a1 f(xk - 2,yk - 2) + . . . + ak - 1 f(x0,y0) ), where a0, a1, . . . , ak - 1 are constants."""

    ADAMS_BASHFORTH_METHOD: "KISAO"
    """Adams-Bashforth method: Given an initial value problem: y' = f(x,y), y(x0) = y0 together with additional starting values y1 = y(x0 + h), . . . , yk-1 = y(x0 + (k-1) h) the k-step Adams-Bashforth method is an explicit linear multistep method that approximates the solution, y(x) at x = x0+kh, of the initial value problem by yk = yk - 1 + h * ( a0 f(xk - 1,yk - 1) + a1 f(xk - 2,yk - 2) + . . . + ak - 1 f(x0,y0) ), where a0, a1, . . . , ak - 1 are constants."""

    KISAO_0000280: "KISAO"
    """Adams-Moulton method: The (k-1)-step Adams-Moulton method is an implicit linear multistep method that iteratively approximates the solution, y(x) at x = x0+kh, of the initial value problem by yk = yk - 1 + h * ( b0 f(xk,yk) + b1 f(xk - 1,yk - 1) + . . . + bk - 1 f(x1,y1) ), where b1, . . . , bk - 1 are constants."""

    ADAMS_MOULTON_METHOD: "KISAO"
    """Adams-Moulton method: The (k-1)-step Adams-Moulton method is an implicit linear multistep method that iteratively approximates the solution, y(x) at x = x0+kh, of the initial value problem by yk = yk - 1 + h * ( b0 f(xk,yk) + b1 f(xk - 1,yk - 1) + . . . + bk - 1 f(x1,y1) ), where b1, . . . , bk - 1 are constants."""

    KISAO_0000281: "KISAO"
    """multistep method: A numerical method for differential equations which is based on several values of the solution."""

    MULTISTEP_METHOD: "KISAO"
    """multistep method: A numerical method for differential equations which is based on several values of the solution."""

    KISAO_0000282: "KISAO"
    """KINSOL: KINSOL solves algebraic systems in real N-space, written as F(u)=0, F:RN->RN, given an initial guess u0. The basic method is either a modified or an inexact Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408]. The linear systems that arise are solved with either a direct (dense or banded) solver (serial version only), or one of the Krylov iterative solvers [http://identifiers.org/biomodels.kisao/KISAO_0000354]. In the Krylov case, the user can (optionally) supply a right preconditioner."""

    KINSOL: "KISAO"
    """KINSOL: KINSOL solves algebraic systems in real N-space, written as F(u)=0, F:RN->RN, given an initial guess u0. The basic method is either a modified or an inexact Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408]. The linear systems that arise are solved with either a direct (dense or banded) solver (serial version only), or one of the Krylov iterative solvers [http://identifiers.org/biomodels.kisao/KISAO_0000354]. In the Krylov case, the user can (optionally) supply a right preconditioner."""

    KISAO_0000283: "KISAO"
    """IDA: IDA solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0. At each step, a Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408] leads to linear systems Jx=b, which are solved by one of five methods - two direct (dense or band; serial version only) and three Krylov [http://identifiers.org/biomodels.kisao/KISAO_0000354] (GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000353], BiCGStab [http://identifiers.org/biomodels.kisao/KISAO_0000392], or TFQMR [http://identifiers.org/biomodels.kisao/KISAO_0000396]). IDA is written in C, but derived from the package DASPK [http://identifiers.org/biomodels.kisao/KISAO_0000355] which is written in Fortran."""

    IDA: "KISAO"
    """IDA: IDA solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0. At each step, a Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408] leads to linear systems Jx=b, which are solved by one of five methods - two direct (dense or band; serial version only) and three Krylov [http://identifiers.org/biomodels.kisao/KISAO_0000354] (GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000353], BiCGStab [http://identifiers.org/biomodels.kisao/KISAO_0000392], or TFQMR [http://identifiers.org/biomodels.kisao/KISAO_0000396]). IDA is written in C, but derived from the package DASPK [http://identifiers.org/biomodels.kisao/KISAO_0000355] which is written in Fortran."""

    KISAO_0000285: "KISAO"
    """finite volume method: The finite volume method is a method for representing and evaluating partial differential equations in the form of algebraic equations, which attempts to emulate continuous conservation laws of physics."""

    FINITE_VOLUME_METHOD: "KISAO"
    """finite volume method: The finite volume method is a method for representing and evaluating partial differential equations in the form of algebraic equations, which attempts to emulate continuous conservation laws of physics."""

    KISAO_0000286: "KISAO"
    """Euler-Maruyama method: The Euler-Maruyama method is a method for the approximate numerical solution of a stochastic differential equation, which truncates the Ito and Stratonovich Taylor series of the exact solution after the first order stochastic terms. This converges to the Ito solution with strong global order accuracy 1/2 or weak global order accuracy 1. It is a simple generalization of the Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261] for ordinary differential equations to stochastic differential equations."""

    EULER_MARUYAMA_METHOD: "KISAO"
    """Euler-Maruyama method: The Euler-Maruyama method is a method for the approximate numerical solution of a stochastic differential equation, which truncates the Ito and Stratonovich Taylor series of the exact solution after the first order stochastic terms. This converges to the Ito solution with strong global order accuracy 1/2 or weak global order accuracy 1. It is a simple generalization of the Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261] for ordinary differential equations to stochastic differential equations."""

    KISAO_0000287: "KISAO"
    """Milstein method: The Milstein method is a technique for the approximate numerical solution of a stochastic differential equation."""

    MILSTEIN_METHOD: "KISAO"
    """Milstein method: The Milstein method is a technique for the approximate numerical solution of a stochastic differential equation."""

    KISAO_0000288: "KISAO"
    """backward differentiation formula: The backward differentiation formulas (BDF) are implicit multistep methods based on the numerical differentiation of a given function and are wildly used for integration of stiff differential equations."""

    BACKWARD_DIFFERENTIATION_FORMULA: "KISAO"
    """backward differentiation formula: The backward differentiation formulas (BDF) are implicit multistep methods based on the numerical differentiation of a given function and are wildly used for integration of stiff differential equations."""

    KISAO_0000289: "KISAO"
    """Adams method: Adams' methods are multi-step methods used for the numerical integration of initial value problems in Ordinary Differential Equations (ODE's). Adams' algorithm consists of two parts: firstly, a starting procedure which provides y1, ... , yk-1 ( approximations to the exact solution at the points x0 + h, ... , x0 + (k - 1)h ) and, secondly, a multistep formula to obtain an approximation to the exact solution y(x0 + kh). This is then applied recursively, based on the numerical approximation of k successive steps, to compute y(x0 + (k + 1)h)."""

    ADAMS_METHOD: "KISAO"
    """Adams method: Adams' methods are multi-step methods used for the numerical integration of initial value problems in Ordinary Differential Equations (ODE's). Adams' algorithm consists of two parts: firstly, a starting procedure which provides y1, ... , yk-1 ( approximations to the exact solution at the points x0 + h, ... , x0 + (k - 1)h ) and, secondly, a multistep formula to obtain an approximation to the exact solution y(x0 + kh). This is then applied recursively, based on the numerical approximation of k successive steps, to compute y(x0 + (k + 1)h)."""

    KISAO_0000290: "KISAO"
    """Merson method: A five-stage Runge-Kutta method with fourth-order accuracy."""

    MERSON_METHOD: "KISAO"
    """Merson method: A five-stage Runge-Kutta method with fourth-order accuracy."""

    KISAO_0000296: "KISAO"
    """Hammer-Hollingsworth method: The numerical integration of ordinary differential equations by the use of Gaussian quadrature methods."""

    HAMMER_HOLLINGSWORTH_METHOD: "KISAO"
    """Hammer-Hollingsworth method: The numerical integration of ordinary differential equations by the use of Gaussian quadrature methods."""

    KISAO_0000297: "KISAO"
    """Lobatto method: There are three families of Lobatto methods, called IIIA, IIIB and IIIC. These are named after Rehuel Lobatto. All are implicit Runge-Kutta methods, have order 2s − 2 and they all have c1 = 0 and cs = 1."""

    LOBATTO_METHOD: "KISAO"
    """Lobatto method: There are three families of Lobatto methods, called IIIA, IIIB and IIIC. These are named after Rehuel Lobatto. All are implicit Runge-Kutta methods, have order 2s − 2 and they all have c1 = 0 and cs = 1."""

    KISAO_0000299: "KISAO"
    """Butcher-Kuntzmann method: From a theoretical point of view, the Butcher-Kuntzmann Runge-Kutta methods belong to the best step-by-step methods for nonstiff problems. These methods integrate first-order initial-value problems by means of formulas based on Gauss-Legendre quadrature, and combine excellent stability features with the property of superconvergence at the step points."""

    BUTCHER_KUNTZMANN_METHOD: "KISAO"
    """Butcher-Kuntzmann method: From a theoretical point of view, the Butcher-Kuntzmann Runge-Kutta methods belong to the best step-by-step methods for nonstiff problems. These methods integrate first-order initial-value problems by means of formulas based on Gauss-Legendre quadrature, and combine excellent stability features with the property of superconvergence at the step points."""

    KISAO_0000301: "KISAO"
    """Heun method: The method is named after Karl L. W. M. Heun and is a numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It can be seen as extension of the Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261] into two-stage second-order Runge-Kutta method."""

    HEUN_METHOD: "KISAO"
    """Heun method: The method is named after Karl L. W. M. Heun and is a numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It can be seen as extension of the Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261] into two-stage second-order Runge-Kutta method."""

    KISAO_0000302: "KISAO"
    """embedded Runge-Kutta method: An embedded Runge-Kutta method is a method in which two Runge-Kutta estimates are obtained using the same auxiliary functions ki but with a different linear combination of these functions so that one estimate has an order one greater than the other."""

    EMBEDDED_RUNGE_KUTTA_METHOD: "KISAO"
    """embedded Runge-Kutta method: An embedded Runge-Kutta method is a method in which two Runge-Kutta estimates are obtained using the same auxiliary functions ki but with a different linear combination of these functions so that one estimate has an order one greater than the other."""

    KISAO_0000303: "KISAO"
    """Zonneveld method: An embedded Runge-Kutta method [http://identifiers.org/biomodels.kisao/KISAO_0000302] of order 4(3), proposed by J.A. Zonneveld in 1964."""

    ZONNEVELD_METHOD: "KISAO"
    """Zonneveld method: An embedded Runge-Kutta method [http://identifiers.org/biomodels.kisao/KISAO_0000302] of order 4(3), proposed by J.A. Zonneveld in 1964."""

    KISAO_0000304: "KISAO"
    """Radau method: Implicit Runge-Kutta methods based on Radau quadrature."""

    RADAU_METHOD: "KISAO"
    """Radau method: Implicit Runge-Kutta methods based on Radau quadrature."""

    KISAO_0000305: "KISAO"
    """Verner method: The first high order (6(5)) embedded Runge-Kutta formulas that avoid the drawback of giving identically zero error estimates for quadrature problems y' = f(x) were constructed by Verner in 1978."""

    VERNER_METHOD: "KISAO"
    """Verner method: The first high order (6(5)) embedded Runge-Kutta formulas that avoid the drawback of giving identically zero error estimates for quadrature problems y' = f(x) were constructed by Verner in 1978."""

    KISAO_0000306: "KISAO"
    """Lagrangian sliding fluid element algorithm: Because the analytic solutions to the partial differential equations require convolution integration, solutions are obtained relatively efficiently by a fast numerical method. Our approach centers on the use of a sliding fluid element algorithm for capillary convection, with the time step set equal to the length step divided by the fluid velocity. Radial fluxes by permeation between plasma, interstitial fluid, and cells and axial diffusion exchanges within each time step are calculated analytically. The method enforces mass conservation unless there is regional consumption."""

    LAGRANGIAN_SLIDING_FLUID_ELEMENT_ALGORITHM: "KISAO"
    """Lagrangian sliding fluid element algorithm: Because the analytic solutions to the partial differential equations require convolution integration, solutions are obtained relatively efficiently by a fast numerical method. Our approach centers on the use of a sliding fluid element algorithm for capillary convection, with the time step set equal to the length step divided by the fluid velocity. Radial fluxes by permeation between plasma, interstitial fluid, and cells and axial diffusion exchanges within each time step are calculated analytically. The method enforces mass conservation unless there is regional consumption."""

    KISAO_0000307: "KISAO"
    """finite difference method: The finite difference method is based on local approximations of the partial derivatives in a Partial Differential Equation, which are derived by low order Taylor series expansions."""

    FINITE_DIFFERENCE_METHOD: "KISAO"
    """finite difference method: The finite difference method is based on local approximations of the partial derivatives in a Partial Differential Equation, which are derived by low order Taylor series expansions."""

    KISAO_0000308: "KISAO"
    """MacCormack method: In computational fluid dynamics, the MacCormack method is a widely used discretization scheme for the numerical solution of hyperbolic partial differential equations. This second-order finite difference method [http://identifiers.org/biomodels.kisao/KISAO_0000307] is introduced by R. W. MacCormack in 1969."""

    MACCORMACK_METHOD: "KISAO"
    """MacCormack method: In computational fluid dynamics, the MacCormack method is a widely used discretization scheme for the numerical solution of hyperbolic partial differential equations. This second-order finite difference method [http://identifiers.org/biomodels.kisao/KISAO_0000307] is introduced by R. W. MacCormack in 1969."""

    KISAO_0000309: "KISAO"
    """Crank-Nicolson method: In numerical analysis, the Crank-Nicolson method is a finite difference method [http://identifiers.org/biomodels.kisao/KISAO_0000307] used for numerically solving the heat equation and similar partial differential equations. It is a second-order method in time, implicit in time, and is numerically stable. The method was developed by John Crank and Phyllis Nicolson in the mid 20th century."""

    CRANK_NICOLSON_METHOD: "KISAO"
    """Crank-Nicolson method: In numerical analysis, the Crank-Nicolson method is a finite difference method [http://identifiers.org/biomodels.kisao/KISAO_0000307] used for numerically solving the heat equation and similar partial differential equations. It is a second-order method in time, implicit in time, and is numerically stable. The method was developed by John Crank and Phyllis Nicolson in the mid 20th century."""

    KISAO_0000310: "KISAO"
    """method of lines: The method of lines is a general technique for solving partial differential equations (PDEs) by typically using finite difference relationships for the spatial derivatives and ordinary differential equations for the time derivative."""

    METHOD_OF_LINES: "KISAO"
    """method of lines: The method of lines is a general technique for solving partial differential equations (PDEs) by typically using finite difference relationships for the spatial derivatives and ordinary differential equations for the time derivative."""

    KISAO_0000311: "KISAO"
    """type of domain geometry handling."""

    TYPE_OF_DOMAIN_GEOMETRY_HANDLING: "KISAO"
    """type of domain geometry handling."""

    KISAO_0000314: "KISAO"
    """S-System power-law canonical differential equations solver: Ordinary differential equations can be recast into a nonlinear canonical form called an S-system. Evidence for the generality of this class comes from extensive empirical examples that have been recast and from the discovery that sets of differential equations and functions, recognized as among the most general, are special cases of S-systems. Identification of this nonlinear canonical form suggests a radically different approach to numerical solution of ordinary differential equations. By capitalizing on the regular structure of S-systems, efficient formulas for a variable-order, variable-step Taylor-series method are developed."""

    S_SYSTEM_POWER_LAW_CANONICAL_DIFFERENTIAL_EQUATIONS_SOLVER: "KISAO"
    """S-System power-law canonical differential equations solver: Ordinary differential equations can be recast into a nonlinear canonical form called an S-system. Evidence for the generality of this class comes from extensive empirical examples that have been recast and from the discovery that sets of differential equations and functions, recognized as among the most general, are special cases of S-systems. Identification of this nonlinear canonical form suggests a radically different approach to numerical solution of ordinary differential equations. By capitalizing on the regular structure of S-systems, efficient formulas for a variable-order, variable-step Taylor-series method are developed."""

    KISAO_0000315: "KISAO"
    """lattice gas automata: Lattice gas automata methods are a series of cellular automata methods used to simulate fluid flows. From the LGCA, it is possible to derive the macroscopic Navier-Stokes equations."""

    LATTICE_GAS_AUTOMATA: "KISAO"
    """lattice gas automata: Lattice gas automata methods are a series of cellular automata methods used to simulate fluid flows. From the LGCA, it is possible to derive the macroscopic Navier-Stokes equations."""

    KISAO_0000316: "KISAO"
    """enhanced Greens function reaction dynamics: GFRD [http://identifiers.org/biomodels.kisao/KISAO_0000058] decomposes the multi­body reaction diffusion problem to a set of single and two body problems. Analytical solutions for two body reaction diffusion are available via Smoluchowski equation. eGFRD allows to solve each sub­problem asynchronously by introducing the concept of first passage processes."""

    ENHANCED_GREENS_FUNCTION_REACTION_DYNAMICS: "KISAO"
    """enhanced Greens function reaction dynamics: GFRD [http://identifiers.org/biomodels.kisao/KISAO_0000058] decomposes the multi­body reaction diffusion problem to a set of single and two body problems. Analytical solutions for two body reaction diffusion are available via Smoluchowski equation. eGFRD allows to solve each sub­problem asynchronously by introducing the concept of first passage processes."""

    KISAO_0000317: "KISAO"
    """E-Cell multi-algorithm simulation method: A modular meta-algorithm with a discrete event scheduler that can incorporate any type of time-driven simulation algorithm. It was shown that this meta-algorithm can efficiently drive simulation models with different simulation algorithms with little intrusive modification to the algorithms themselves. Only a few additional methods to handle communications between computational modules are required."""

    E_CELL_MULTI_ALGORITHM_SIMULATION_METHOD: "KISAO"
    """E-Cell multi-algorithm simulation method: A modular meta-algorithm with a discrete event scheduler that can incorporate any type of time-driven simulation algorithm. It was shown that this meta-algorithm can efficiently drive simulation models with different simulation algorithms with little intrusive modification to the algorithms themselves. Only a few additional methods to handle communications between computational modules are required."""

    KISAO_0000318: "KISAO"
    """Gauss-Legendre Runge-Kutta method: So called 'Open Formula', two points formula, three points formula, four points formula, five points formula and six points formula of the Runge-Kutta method to solve the initial value problem of the ordinary differential equation. These formulas use the points and weights from the Gauss-Legendre Quadrature formulas for finding the value of the definite integral."""

    GAUSS_LEGENDRE_RUNGE_KUTTA_METHOD: "KISAO"
    """Gauss-Legendre Runge-Kutta method: So called 'Open Formula', two points formula, three points formula, four points formula, five points formula and six points formula of the Runge-Kutta method to solve the initial value problem of the ordinary differential equation. These formulas use the points and weights from the Gauss-Legendre Quadrature formulas for finding the value of the definite integral."""

    KISAO_0000319: "KISAO"
    """Monte Carlo method: Monte Carlo methods (or Monte Carlo experiments) are a class of computational algorithms that rely on repeated random sampling to compute their results."""

    MONTE_CARLO_METHOD: "KISAO"
    """Monte Carlo method: Monte Carlo methods (or Monte Carlo experiments) are a class of computational algorithms that rely on repeated random sampling to compute their results."""

    KISAO_0000320: "KISAO"
    """BioRica hybrid method: The simulation schema for a given BioRica node is given by a hybrid algorithm that deals with continuous time and allows for discrete events that roll back the time according to these discrete interruptions."""

    BIORICA_HYBRID_METHOD: "KISAO"
    """BioRica hybrid method: The simulation schema for a given BioRica node is given by a hybrid algorithm that deals with continuous time and allows for discrete events that roll back the time according to these discrete interruptions."""

    KISAO_0000321: "KISAO"
    """Cash-Karp method: An family of explicit Runge-Kutta formulas, which are very efficient for problems with smooth solution as well as problems having rapidly varying solutions. Each member of this family consists of a fifty-order formula that contains embedded formulas of all orders 1 through 4. By computing solutions at several different orders, it is possible to detect sharp fronts or discontinuities before all the function evaluations defining the full Runge-Kutta step have been computed."""

    CASH_KARP_METHOD: "KISAO"
    """Cash-Karp method: An family of explicit Runge-Kutta formulas, which are very efficient for problems with smooth solution as well as problems having rapidly varying solutions. Each member of this family consists of a fifty-order formula that contains embedded formulas of all orders 1 through 4. By computing solutions at several different orders, it is possible to detect sharp fronts or discontinuities before all the function evaluations defining the full Runge-Kutta step have been computed."""

    KISAO_0000322: "KISAO"
    """hybridity: The basic idea of hybrid simulation methods is to combine the advantages of complementary simulation approaches: the whole system is subdivided into appropriate parts and different simulation methods operate on these parts at the same time."""

    HYBRIDITY: "KISAO"
    """hybridity: The basic idea of hybrid simulation methods is to combine the advantages of complementary simulation approaches: the whole system is subdivided into appropriate parts and different simulation methods operate on these parts at the same time."""

    KISAO_0000323: "KISAO"
    """equation-free probabilistic steady-state approximation: We present a probabilistic steady-state approximation that separates the time scales of an arbitrary reaction network, detects the convergence of a marginal distribution to a quasi-steady-state, directly samples the underlying distribution, and uses those samples to accurately predict the state of the system, including the effects of the slow dynamics, at future times. The numerical method produces an accurate solution of both the fast and slow reaction dynamics while, for stiff systems, reducing the computational time by orders of magnitude. The developed theory makes no approximations on the shape or form of the underlying steady-state distribution and only assumes that it is ergodic. <...> The developed theory may be applied to any type of kinetic Monte Carlo simulation to more efficiently simulate dynamically stiff systems, including existing exact, approximate, or hybrid stochastic simulation techniques."""

    EQUATION_FREE_PROBABILISTIC_STEADY_STATE_APPROXIMATION: "KISAO"
    """equation-free probabilistic steady-state approximation: We present a probabilistic steady-state approximation that separates the time scales of an arbitrary reaction network, detects the convergence of a marginal distribution to a quasi-steady-state, directly samples the underlying distribution, and uses those samples to accurately predict the state of the system, including the effects of the slow dynamics, at future times. The numerical method produces an accurate solution of both the fast and slow reaction dynamics while, for stiff systems, reducing the computational time by orders of magnitude. The developed theory makes no approximations on the shape or form of the underlying steady-state distribution and only assumes that it is ergodic. <...> The developed theory may be applied to any type of kinetic Monte Carlo simulation to more efficiently simulate dynamically stiff systems, including existing exact, approximate, or hybrid stochastic simulation techniques."""

    KISAO_0000324: "KISAO"
    """nested stochastic simulation algorithm: This multiscale method is a small modification of the Gillespie's direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029], in the form of a nested SSA, with inner loops for the fast reactions, and outer loop for the slow reactions. The number of groups can be more than two, and the grouping into fast and slow variables can be done dynamically in an adaptive version of the scheme."""

    NESTED_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """nested stochastic simulation algorithm: This multiscale method is a small modification of the Gillespie's direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029], in the form of a nested SSA, with inner loops for the fast reactions, and outer loop for the slow reactions. The number of groups can be more than two, and the grouping into fast and slow variables can be done dynamically in an adaptive version of the scheme."""

    KISAO_0000325: "KISAO"
    """minimum fast/discrete reaction occurrences number: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which describes the minimum number of fast/discrete reaction occurrences before their effects cause convergence to a quasi-steady-state distribution."""

    MINIMUM_FAST_DISCRETE_REACTION_OCCURRENCES_NUMBER: "KISAO"
    """minimum fast/discrete reaction occurrences number: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which describes the minimum number of fast/discrete reaction occurrences before their effects cause convergence to a quasi-steady-state distribution."""

    KISAO_0000326: "KISAO"
    """number of samples: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which determines the number of samples taken from the distribution."""

    NUMBER_OF_SAMPLES: "KISAO"
    """number of samples: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which determines the number of samples taken from the distribution."""

    KISAO_0000327: "KISAO"
    """maximum discrete number: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which controls the maximum number of molecules of some reactant species in order for the reaction to be considered discrete."""

    MAXIMUM_DISCRETE_NUMBER: "KISAO"
    """maximum discrete number: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which controls the maximum number of molecules of some reactant species in order for the reaction to be considered discrete."""

    KISAO_0000328: "KISAO"
    """minimum fast rate: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which controls the minimum rate of the reaction in order for it to be considered fast."""

    MINIMUM_FAST_RATE: "KISAO"
    """minimum fast rate: Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which controls the minimum rate of the reaction in order for it to be considered fast."""

    KISAO_0000329: "KISAO"
    """constant-time kinetic Monte Carlo algorithm: The computational cost of the original SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] scaled linearly with the number of reactions in the network. Gibson and Bruck developed a logarithmic scaling version of the SSA which uses a priority queue or binary tree for more efficient reaction selection [http://identifiers.org/biomodels.kisao/KISAO_0000027]. More generally, this problem is one of dynamic discrete random variate generation which finds many uses in kinetic Monte Carlo and discrete event simulation. We present here a constant-time algorithm, whose cost is independent of the number of reactions, enabled by a slightly more complex underlying data structure."""

    CONSTANT_TIME_KINETIC_MONTE_CARLO_ALGORITHM: "KISAO"
    """constant-time kinetic Monte Carlo algorithm: The computational cost of the original SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] scaled linearly with the number of reactions in the network. Gibson and Bruck developed a logarithmic scaling version of the SSA which uses a priority queue or binary tree for more efficient reaction selection [http://identifiers.org/biomodels.kisao/KISAO_0000027]. More generally, this problem is one of dynamic discrete random variate generation which finds many uses in kinetic Monte Carlo and discrete event simulation. We present here a constant-time algorithm, whose cost is independent of the number of reactions, enabled by a slightly more complex underlying data structure."""

    KISAO_0000330: "KISAO"
    """R-leaping algorithm: A novel algorithm is proposed for the acceleration of the exact stochastic simulation algorithm by a predefined number of reaction firings (R-leaping) that may occur across several reaction channels. In the present approach, the numbers of reaction firings are correlated binomial distributions and the sampling procedure is independent of any permutation of the reaction channels. This enables the algorithm to efficiently handle large systems with disparate rates, providing substantial computational savings in certain cases."""

    R_LEAPING_ALGORITHM: "KISAO"
    """R-leaping algorithm: A novel algorithm is proposed for the acceleration of the exact stochastic simulation algorithm by a predefined number of reaction firings (R-leaping) that may occur across several reaction channels. In the present approach, the numbers of reaction firings are correlated binomial distributions and the sampling procedure is independent of any permutation of the reaction channels. This enables the algorithm to efficiently handle large systems with disparate rates, providing substantial computational savings in certain cases."""

    KISAO_0000331: "KISAO"
    """exact R-leaping algorithm: We present a SSA which, similar to R-leap [http://identifiers.org/biomodels.kisao/KISAO_0000330], accelerates SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] by executing multiple reactions per algorithmic step, but which samples the reactant trajectories from the same probability distribution as the SSA. This 'exact R-leap' or 'ER-leap' algorithm is a modification of the R-leap algorithm which is both exact and capable of substantial speed-up over SSA."""

    EXACT_R_LEAPING_ALGORITHM: "KISAO"
    """exact R-leaping algorithm: We present a SSA which, similar to R-leap [http://identifiers.org/biomodels.kisao/KISAO_0000330], accelerates SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] by executing multiple reactions per algorithmic step, but which samples the reactant trajectories from the same probability distribution as the SSA. This 'exact R-leap' or 'ER-leap' algorithm is a modification of the R-leap algorithm which is both exact and capable of substantial speed-up over SSA."""

    KISAO_0000332: "KISAO"
    """ER-leap initial leap: L (initial step) is a parameter of 'exact R-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000331]. ''We will assume that the reaction event to be bounded occurs within a run of L events in the SSA algorithm[http://identifiers.org/biomodels.kisao/KISAO_0000029], in order to execute L reactions at once in the manner of the R-leap algorithm[http://identifiers.org/biomodels.kisao/KISAO_0000230]''."""

    ER_LEAP_INITIAL_LEAP: "KISAO"
    """ER-leap initial leap: L (initial step) is a parameter of 'exact R-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000331]. ''We will assume that the reaction event to be bounded occurs within a run of L events in the SSA algorithm[http://identifiers.org/biomodels.kisao/KISAO_0000029], in order to execute L reactions at once in the manner of the R-leap algorithm[http://identifiers.org/biomodels.kisao/KISAO_0000230]''."""

    KISAO_0000333: "KISAO"
    """accelerated stochastic simulation algorithm: An algorithm, which accelerates SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] either at the expense of its accuracy or exact."""

    ACCELERATED_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """accelerated stochastic simulation algorithm: An algorithm, which accelerates SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] either at the expense of its accuracy or exact."""

    KISAO_0000334: "KISAO"
    """multiparticle lattice gas automata: An algorithm which allows for an arbitrary number of particles, while keeping the benefits of the cellular automata approach [http://identifiers.org/biomodels.kisao/KISAO_0000315]."""

    MULTIPARTICLE_LATTICE_GAS_AUTOMATA: "KISAO"
    """multiparticle lattice gas automata: An algorithm which allows for an arbitrary number of particles, while keeping the benefits of the cellular automata approach [http://identifiers.org/biomodels.kisao/KISAO_0000315]."""

    KISAO_0000335: "KISAO"
    """generalized stochastic simulation algorithm: Gillespie direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029] follows unit-by-unit changes in the total numbers of each reactant species, it is especially well suited to the study of systems in which reactant densities are low and the application of methods based on continuum approximations, such as the traditional ordinary differential equations of chemical kinetics, is questionable. The 'generalized stochastic simulation algorithm' branch presents methods, which extend Gillespie direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029] to suit to systems with other characteristics."""

    GENERALIZED_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """generalized stochastic simulation algorithm: Gillespie direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029] follows unit-by-unit changes in the total numbers of each reactant species, it is especially well suited to the study of systems in which reactant densities are low and the application of methods based on continuum approximations, such as the traditional ordinary differential equations of chemical kinetics, is questionable. The 'generalized stochastic simulation algorithm' branch presents methods, which extend Gillespie direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029] to suit to systems with other characteristics."""

    KISAO_0000336: "KISAO"
    """D-leaping method: We propose a novel, accelerated algorithm for the approximate stochastic simulation of biochemical systems with delays. The present work extends existing accelerated algorithms by distributing, in a time adaptive fashion, the delayed reactions so as to minimize the computational effort while preserving their accuracy."""

    D_LEAPING_METHOD: "KISAO"
    """D-leaping method: We propose a novel, accelerated algorithm for the approximate stochastic simulation of biochemical systems with delays. The present work extends existing accelerated algorithms by distributing, in a time adaptive fashion, the delayed reactions so as to minimize the computational effort while preserving their accuracy."""

    KISAO_0000337: "KISAO"
    """finite element method: A numerical technique for finding approximate solutions of partial differential equations (PDE) as well as of integral equations. The solution approach is based either on eliminating the differential equation completely (steady state problems), or rendering the PDE into an approximating system of ordinary differential equations, which are then numerically integrated using standard techniques such as Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261], Runge-Kutta [http://identifiers.org/biomodels.kisao/KISAO_0000064], etc."""

    FINITE_ELEMENT_METHOD: "KISAO"
    """finite element method: A numerical technique for finding approximate solutions of partial differential equations (PDE) as well as of integral equations. The solution approach is based either on eliminating the differential equation completely (steady state problems), or rendering the PDE into an approximating system of ordinary differential equations, which are then numerically integrated using standard techniques such as Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261], Runge-Kutta [http://identifiers.org/biomodels.kisao/KISAO_0000064], etc."""

    KISAO_0000338: "KISAO"
    """h-version of the finite element method: Classical form of the 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337], in which polynomials of fixed degree p are used and the mesh is refined to increase accuracy. Can be considered as a special case of the h-p version [http://identifiers.org/biomodels.kisao/KISAO_0000340]."""

    H_VERSION_OF_THE_FINITE_ELEMENT_METHOD: "KISAO"
    """h-version of the finite element method: Classical form of the 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337], in which polynomials of fixed degree p are used and the mesh is refined to increase accuracy. Can be considered as a special case of the h-p version [http://identifiers.org/biomodels.kisao/KISAO_0000340]."""

    KISAO_0000339: "KISAO"
    """p-version of the finite element method: The p version of 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] uses a fixed mesh but increases the polynomial degree p to increase accuracy. Can be considered as a special case of the h-p version [http://identifiers.org/biomodels.kisao/KISAO_0000340]."""

    P_VERSION_OF_THE_FINITE_ELEMENT_METHOD: "KISAO"
    """p-version of the finite element method: The p version of 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] uses a fixed mesh but increases the polynomial degree p to increase accuracy. Can be considered as a special case of the h-p version [http://identifiers.org/biomodels.kisao/KISAO_0000340]."""

    KISAO_0000340: "KISAO"
    """h-p version of the finite element method: In h-p version of 'finite difference method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] the two approaches of mesh refinement and degree enchacement are combined."""

    H_P_VERSION_OF_THE_FINITE_ELEMENT_METHOD: "KISAO"
    """h-p version of the finite element method: In h-p version of 'finite difference method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] the two approaches of mesh refinement and degree enchacement are combined."""

    KISAO_0000341: "KISAO"
    """mixed finite element method: A 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] in which both stress and displacement fields are approximated as primary variables."""

    MIXED_FINITE_ELEMENT_METHOD: "KISAO"
    """mixed finite element method: A 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] in which both stress and displacement fields are approximated as primary variables."""

    KISAO_0000342: "KISAO"
    """level set method: An algorithm for moving surfaces under their curvature. This algorithm rely on numerically solving Hamilton-Jacobi equations with viscous terms, using approximation techniques from hyperbolic conservation laws."""

    LEVEL_SET_METHOD: "KISAO"
    """level set method: An algorithm for moving surfaces under their curvature. This algorithm rely on numerically solving Hamilton-Jacobi equations with viscous terms, using approximation techniques from hyperbolic conservation laws."""

    KISAO_0000343: "KISAO"
    """generalized finite element method: The GFEM is a generalization of the classical 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] — in its h [http://identifiers.org/biomodels.kisao/KISAO_0000338], p [http://identifiers.org/biomodels.kisao/KISAO_0000339], and h-p versions [http://identifiers.org/biomodels.kisao/KISAO_0000340]— as well as of the various forms of meshless methods used in engineering."""

    GENERALIZED_FINITE_ELEMENT_METHOD: "KISAO"
    """generalized finite element method: The GFEM is a generalization of the classical 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] — in its h [http://identifiers.org/biomodels.kisao/KISAO_0000338], p [http://identifiers.org/biomodels.kisao/KISAO_0000339], and h-p versions [http://identifiers.org/biomodels.kisao/KISAO_0000340]— as well as of the various forms of meshless methods used in engineering."""

    KISAO_0000345: "KISAO"
    """h-p cloud method: A meshless method, which uses a partition of unity to construct the family of h-p cloud functions."""

    H_P_CLOUD_METHOD: "KISAO"
    """h-p cloud method: A meshless method, which uses a partition of unity to construct the family of h-p cloud functions."""

    KISAO_0000346: "KISAO"
    """mesh-based geometry handling: In most large-scale numerical simulations of physical phenomena, a large percentage of the overall computational effort is expended on technical details connected with meshing. These details include, in particular, grid generation, mesh adaptation to domain geometry, element or cell connectivity, grid motion and separation to model fracture, fragmentation, free surfaces, etc."""

    MESH_BASED_GEOMETRY_HANDLING: "KISAO"
    """mesh-based geometry handling: In most large-scale numerical simulations of physical phenomena, a large percentage of the overall computational effort is expended on technical details connected with meshing. These details include, in particular, grid generation, mesh adaptation to domain geometry, element or cell connectivity, grid motion and separation to model fracture, fragmentation, free surfaces, etc."""

    KISAO_0000347: "KISAO"
    """meshless geometry handling: Most meshless methods require a scattered set of nodal points in the domain of interest. In these methods, there may be no fixed connectivities between the nodes, unlike the finite element or finite difference methods. This feature has significant implications in modeling some physical phenomena that are characterized by a continuous change in the geometry of the domain under analysis."""

    MESHLESS_GEOMETRY_HANDLING: "KISAO"
    """meshless geometry handling: Most meshless methods require a scattered set of nodal points in the domain of interest. In these methods, there may be no fixed connectivities between the nodes, unlike the finite element or finite difference methods. This feature has significant implications in modeling some physical phenomena that are characterized by a continuous change in the geometry of the domain under analysis."""

    KISAO_0000348: "KISAO"
    """extended finite element method: A numerical method to model arbitrary discontinuities in continuous bodies that does not require the mesh to conform to the discontinuities nor significant mesh refinement near singularities. In X-FEM the standard finite element approximation [http://identifiers.org/biomodels.kisao/KISAO_0000337] is enriched and the approximation space is extended by an additional family of functions."""

    EXTENDED_FINITE_ELEMENT_METHOD: "KISAO"
    """extended finite element method: A numerical method to model arbitrary discontinuities in continuous bodies that does not require the mesh to conform to the discontinuities nor significant mesh refinement near singularities. In X-FEM the standard finite element approximation [http://identifiers.org/biomodels.kisao/KISAO_0000337] is enriched and the approximation space is extended by an additional family of functions."""

    KISAO_0000349: "KISAO"
    """method of finite spheres: Method of finite spheres is truly meshless in the sense that the nodes are placed and the numerical integration is performed without a mesh. Some of the novel features of the method of finite spheres are the numerical integration scheme and the way in which the Dirichlet boundary conditions are incorporated."""

    METHOD_OF_FINITE_SPHERES: "KISAO"
    """method of finite spheres: Method of finite spheres is truly meshless in the sense that the nodes are placed and the numerical integration is performed without a mesh. Some of the novel features of the method of finite spheres are the numerical integration scheme and the way in which the Dirichlet boundary conditions are incorporated."""

    KISAO_0000350: "KISAO"
    """probability-weighted dynamic Monte Carlo method: We have developed a probability-weighted DMC method by incorporating the weighted sampling algorithm of equilibrium molecular simulations. This new algorithm samples the slow reactions very efficiently and makes it possible to simulate in a computationally efficient manner the reaction kinetics of physical systems in which the rates of reactions vary by several orders of magnitude."""

    PROBABILITY_WEIGHTED_DYNAMIC_MONTE_CARLO_METHOD: "KISAO"
    """probability-weighted dynamic Monte Carlo method: We have developed a probability-weighted DMC method by incorporating the weighted sampling algorithm of equilibrium molecular simulations. This new algorithm samples the slow reactions very efficiently and makes it possible to simulate in a computationally efficient manner the reaction kinetics of physical systems in which the rates of reactions vary by several orders of magnitude."""

    KISAO_0000351: "KISAO"
    """multinomial tau-leaping method: The multinomial tau-leaping method is an extension of the binomial tau-leaping method [http://identifiers.org/biomodels.kisao/KISAO_0000074] to networks with arbitrary multiple-channel reactant dependencies. Improvements were achieved by a combination of three factors: First, tau-leaping steps are determined simply and efficiently using a-priori information and Poisson distribution based estimates of expectation values for reaction numbers. Second, networks are partitioned into closed groups of reactions and corresponding reactants in which no group reactant set is found in any other group. Third, product formation is factored into upper bound estimation of the number of times a particular reaction occurs."""

    MULTINOMIAL_TAU_LEAPING_METHOD: "KISAO"
    """multinomial tau-leaping method: The multinomial tau-leaping method is an extension of the binomial tau-leaping method [http://identifiers.org/biomodels.kisao/KISAO_0000074] to networks with arbitrary multiple-channel reactant dependencies. Improvements were achieved by a combination of three factors: First, tau-leaping steps are determined simply and efficiently using a-priori information and Poisson distribution based estimates of expectation values for reaction numbers. Second, networks are partitioned into closed groups of reactions and corresponding reactants in which no group reactant set is found in any other group. Third, product formation is factored into upper bound estimation of the number of times a particular reaction occurs."""

    KISAO_0000352: "KISAO"
    """hybrid method: A simulation methods which combines the advantages of complementary simulation approaches: the whole system is subdivided into appropriate parts and different simulation methods operate on these parts at the same time."""

    HYBRID_METHOD: "KISAO"
    """hybrid method: A simulation methods which combines the advantages of complementary simulation approaches: the whole system is subdivided into appropriate parts and different simulation methods operate on these parts at the same time."""

    KISAO_0000353: "KISAO"
    """generalized minimal residual algorithm: An iterative method for solving linear systems, which has the property of minimizing at every step the norm of the residual vector over a Krylov subspace. The generalized minimal residual method extends the minimal residual method (MINRES) [http://identifiers.org/biomodels.kisao/KISAO_0000388], which is only applicable to symmetric systems, to non-symmetric systems."""

    GENERALIZED_MINIMAL_RESIDUAL_ALGORITHM: "KISAO"
    """generalized minimal residual algorithm: An iterative method for solving linear systems, which has the property of minimizing at every step the norm of the residual vector over a Krylov subspace. The generalized minimal residual method extends the minimal residual method (MINRES) [http://identifiers.org/biomodels.kisao/KISAO_0000388], which is only applicable to symmetric systems, to non-symmetric systems."""

    KISAO_0000354: "KISAO"
    """Krylov subspace projection method: Krylov subspace method is an iterative linear equation method, which builds up Krylov subspaces and look for good approximations to eigenvectors and invariant subspaces within the Krylov spaces."""

    KRYLOV_SUBSPACE_PROJECTION_METHOD: "KISAO"
    """Krylov subspace projection method: Krylov subspace method is an iterative linear equation method, which builds up Krylov subspaces and look for good approximations to eigenvectors and invariant subspaces within the Krylov spaces."""

    KISAO_0000355: "KISAO"
    """DASPK: In DASPK, we have combined the time-stepping methods of DASSL [http://identifiers.org/biomodels.kisao/KISAO_0000255] with preconditioned iterative method GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000386], for solving large-scale systems of DAEs of the form F(t, y, y') = 0, where F, y, y' are N-dimensional vectors, and a consistent set of initial conditions y(t0) = y0, y'(t0) = y'0 is given. DASPK is written in Fortran."""

    DASPK: "KISAO"
    """DASPK: In DASPK, we have combined the time-stepping methods of DASSL [http://identifiers.org/biomodels.kisao/KISAO_0000255] with preconditioned iterative method GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000386], for solving large-scale systems of DAEs of the form F(t, y, y') = 0, where F, y, y' are N-dimensional vectors, and a consistent set of initial conditions y(t0) = y0, y'(t0) = y'0 is given. DASPK is written in Fortran."""

    KISAO_0000356: "KISAO"
    """DASSL: DASSL is designed for the numerical solution of implicit systems of differential/algebraic equations written in the form F(t,y,y')=0, where F, y, and y' are vectors, and initial values for y and y' are given."""

    DASSL: "KISAO"
    """DASSL: DASSL is designed for the numerical solution of implicit systems of differential/algebraic equations written in the form F(t,y,y')=0, where F, y, and y' are vectors, and initial values for y and y' are given."""

    KISAO_0000357: "KISAO"
    """conjugate gradient method: Conjugate gradient method is an algorithm for the numerical solution of particular systems of linear equations, namely those whose matrix is symmetric and positive-definite. The conjugate gradient method is an iterative method, so it can be applied to sparse systems that are too large to be handled by direct methods. Such systems often arise when numerically solving partial differential equations."""

    CONJUGATE_GRADIENT_METHOD: "KISAO"
    """conjugate gradient method: Conjugate gradient method is an algorithm for the numerical solution of particular systems of linear equations, namely those whose matrix is symmetric and positive-definite. The conjugate gradient method is an iterative method, so it can be applied to sparse systems that are too large to be handled by direct methods. Such systems often arise when numerically solving partial differential equations."""

    KISAO_0000358: "KISAO"
    """biconjugate gradient method: The biconjugate gradient method provides a generalization of conjugate gradient method [http://identifiers.org/biomodels.kisao/KISAO_0000357] to non-symmetric matrices."""

    BICONJUGATE_GRADIENT_METHOD: "KISAO"
    """biconjugate gradient method: The biconjugate gradient method provides a generalization of conjugate gradient method [http://identifiers.org/biomodels.kisao/KISAO_0000357] to non-symmetric matrices."""

    KISAO_0000359: "KISAO"
    """is similar to."""

    IS_SIMILAR_TO: "KISAO"
    """is similar to."""

    KISAO_0000360: "KISAO"
    """uses."""

    USES: "KISAO"
    """uses."""

    KISAO_0000361: "KISAO"
    """is generalization of."""

    IS_GENERALIZATION_OF: "KISAO"
    """is generalization of."""

    KISAO_0000362: "KISAO"
    """implicit-state Doob-Gillespie algorithm: The algorithm uses a representation of the system together with a super-approximation of its ‘event horizon’ (all events that may happen next), and a specific correction scheme to obtain exact timings. Being completely local and not based on any kind of enumeration, this algorithm has a per event time cost which is independent of (i) the size of the set of generable species (which can even be infinite), and (ii) independent of the size of the system (ie, the number of agent instances). The algorithm can be refined, using concepts derived from the classical notion of causality, so that in addition to the above one also has that the even cost is depending (iii) only logarithmically on the size of the model (ie, the number of rules)."""

    IMPLICIT_STATE_DOOB_GILLESPIE_ALGORITHM: "KISAO"
    """implicit-state Doob-Gillespie algorithm: The algorithm uses a representation of the system together with a super-approximation of its ‘event horizon’ (all events that may happen next), and a specific correction scheme to obtain exact timings. Being completely local and not based on any kind of enumeration, this algorithm has a per event time cost which is independent of (i) the size of the set of generable species (which can even be infinite), and (ii) independent of the size of the system (ie, the number of agent instances). The algorithm can be refined, using concepts derived from the classical notion of causality, so that in addition to the above one also has that the even cost is depending (iii) only logarithmically on the size of the model (ie, the number of rules)."""

    KISAO_0000363: "KISAO"
    """rule-based simulation method: Rule-based models provide a powerful alternative to approaches that require explicit enumeration of all possible molecular species of a system. Such models consist of formal rules governing interactive behaviour. Rule-based simulation methods simulate such models."""

    RULE_BASED_SIMULATION_METHOD: "KISAO"
    """rule-based simulation method: Rule-based models provide a powerful alternative to approaches that require explicit enumeration of all possible molecular species of a system. Such models consist of formal rules governing interactive behaviour. Rule-based simulation methods simulate such models."""

    KISAO_0000364: "KISAO"
    """Adams predictor-corrector method: The combination of evaluating a single explicit integration method ('Adams-Bashforth method' [http://identifiers.org/biomodels.kisao/KISAO_0000279]) (the predictor step) in order to provide a good initial guess for the successive evaluation of an implicit method ('Adams-Moulton method' [http://identifiers.org/biomodels.kisao/KISAO_0000280]) (the corrector step) using iteration."""

    ADAMS_PREDICTOR_CORRECTOR_METHOD: "KISAO"
    """Adams predictor-corrector method: The combination of evaluating a single explicit integration method ('Adams-Bashforth method' [http://identifiers.org/biomodels.kisao/KISAO_0000279]) (the predictor step) in order to provide a good initial guess for the successive evaluation of an implicit method ('Adams-Moulton method' [http://identifiers.org/biomodels.kisao/KISAO_0000280]) (the corrector step) using iteration."""

    KISAO_0000365: "KISAO"
    """NDSolve method: The Mathematica computation system function NDSolve is a general numerical differential equation solver. It can handle a wide range of ordinary differential equations as well as some partial differential equations. NDSolve can also solve some differential-algebraic equations, which are typically a mix of differential and algebraic equations."""

    NDSOLVE_METHOD: "KISAO"
    """NDSolve method: The Mathematica computation system function NDSolve is a general numerical differential equation solver. It can handle a wide range of ordinary differential equations as well as some partial differential equations. NDSolve can also solve some differential-algebraic equations, which are typically a mix of differential and algebraic equations."""

    KISAO_0000366: "KISAO"
    """symplecticness: Roughly speaking, ‘symplecticness’ is a characteristic property possessed by the solutions of Hamiltonian problems. A numerical method is called symplectic if, when applied to Hamiltonian problems, it generates numerical solutions which inherit the property of symplecticness (phase volume preservation)."""

    SYMPLECTICNESS: "KISAO"
    """symplecticness: Roughly speaking, ‘symplecticness’ is a characteristic property possessed by the solutions of Hamiltonian problems. A numerical method is called symplectic if, when applied to Hamiltonian problems, it generates numerical solutions which inherit the property of symplecticness (phase volume preservation)."""

    KISAO_0000367: "KISAO"
    """partitioned Runge-Kutta method: If a Hamiltonian system possesses a natural partitioning, it is possible to integrate its certain components using one Runge-Kutta method and other components using a different Runge-Kutta method. The overall s-stage scheme is called a partitioned Runge-Kutta method."""

    PARTITIONED_RUNGE_KUTTA_METHOD: "KISAO"
    """partitioned Runge-Kutta method: If a Hamiltonian system possesses a natural partitioning, it is possible to integrate its certain components using one Runge-Kutta method and other components using a different Runge-Kutta method. The overall s-stage scheme is called a partitioned Runge-Kutta method."""

    KISAO_0000369: "KISAO"
    """partial differential equation discretization method: A method which solves partial differential equations by discretizing them, i.e. approximating them by equations that involve a finite number of unknowns."""

    PARTIAL_DIFFERENTIAL_EQUATION_DISCRETIZATION_METHOD: "KISAO"
    """partial differential equation discretization method: A method which solves partial differential equations by discretizing them, i.e. approximating them by equations that involve a finite number of unknowns."""

    KISAO_0000370: "KISAO"
    """type of problem: A characteristic describing the type of the problems which can be solved by the algorithm."""

    TYPE_OF_PROBLEM: "KISAO"
    """type of problem: A characteristic describing the type of the problems which can be solved by the algorithm."""

    KISAO_0000371: "KISAO"
    """stochastic differential equation problem."""

    STOCHASTIC_DIFFERENTIAL_EQUATION_PROBLEM: "KISAO"
    """stochastic differential equation problem."""

    KISAO_0000372: "KISAO"
    """partial differential equation problem."""

    PARTIAL_DIFFERENTIAL_EQUATION_PROBLEM: "KISAO"
    """partial differential equation problem."""

    KISAO_0000373: "KISAO"
    """differential-algebraic equation problem."""

    DIFFERENTIAL_ALGEBRAIC_EQUATION_PROBLEM: "KISAO"
    """differential-algebraic equation problem."""

    KISAO_0000374: "KISAO"
    """ordinary differential equation problem."""

    ORDINARY_DIFFERENTIAL_EQUATION_PROBLEM: "KISAO"
    """ordinary differential equation problem."""

    KISAO_0000375: "KISAO"
    """delay differential equation problem."""

    DELAY_DIFFERENTIAL_EQUATION_PROBLEM: "KISAO"
    """delay differential equation problem."""

    KISAO_0000376: "KISAO"
    """linearity of equation: Linear differential equations are of the form Ly = f, where the differential operator L is a linear operator, y is the unknown function, and the right hand side f is a given function of the same nature as y."""

    LINEARITY_OF_EQUATION: "KISAO"
    """linearity of equation: Linear differential equations are of the form Ly = f, where the differential operator L is a linear operator, y is the unknown function, and the right hand side f is a given function of the same nature as y."""

    KISAO_0000377: "KISAO"
    """one-step method: A numerical method for differential equations which uses one starting value at each step."""

    ONE_STEP_METHOD: "KISAO"
    """one-step method: A numerical method for differential equations which uses one starting value at each step."""

    KISAO_0000378: "KISAO"
    """implicit midpoint rule: The implicit midpoint rule is a second-order case of the more general implicit s-stage Runge-Kutta methods [http://identifiers.org/biomodels.kisao/KISAO_0000064 and (http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000240)]."""

    IMPLICIT_MIDPOINT_RULE: "KISAO"
    """implicit midpoint rule: The implicit midpoint rule is a second-order case of the more general implicit s-stage Runge-Kutta methods [http://identifiers.org/biomodels.kisao/KISAO_0000064 and (http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000240)]."""

    KISAO_0000379: "KISAO"
    """Bulirsch-Stoer algorithm: The Bulirsch-Stoer method is an adaptive method which uses Gragg's modified midpoint method [http://identifiers.org/biomodels.kisao/KISAO_0000382] to estimate the solution of an initial value problem for various step sizes. The estimates are fit to a 'diagonal' rational function or a polynomial as a function of the step size and the limit as the step size tends to zero is taken as the final estimate."""

    BULIRSCH_STOER_ALGORITHM: "KISAO"
    """Bulirsch-Stoer algorithm: The Bulirsch-Stoer method is an adaptive method which uses Gragg's modified midpoint method [http://identifiers.org/biomodels.kisao/KISAO_0000382] to estimate the solution of an initial value problem for various step sizes. The estimates are fit to a 'diagonal' rational function or a polynomial as a function of the step size and the limit as the step size tends to zero is taken as the final estimate."""

    KISAO_0000380: "KISAO"
    """Richardson extrapolation based method: A method based on ideas of Richardson extrapolation, which is a process for obtaining increased accuracy in a discretized approximation by extrapolating results from coarse discretizations to an arbitrarily fine one."""

    RICHARDSON_EXTRAPOLATION_BASED_METHOD: "KISAO"
    """Richardson extrapolation based method: A method based on ideas of Richardson extrapolation, which is a process for obtaining increased accuracy in a discretized approximation by extrapolating results from coarse discretizations to an arbitrarily fine one."""

    KISAO_0000381: "KISAO"
    """midpoint method: The midpoint method is an explicit method for approximating the solution of the initial value problem y' = f(x,y); y(x0) = y0 at x for a given step size h. For the midpoint method the derivative of y(x) is approximated by the symmetric difference y'(x) = ( y(x+h) - y(x-h) ) / 2h + O(h2)."""

    MIDPOINT_METHOD: "KISAO"
    """midpoint method: The midpoint method is an explicit method for approximating the solution of the initial value problem y' = f(x,y); y(x0) = y0 at x for a given step size h. For the midpoint method the derivative of y(x) is approximated by the symmetric difference y'(x) = ( y(x+h) - y(x-h) ) / 2h + O(h2)."""

    KISAO_0000382: "KISAO"
    """modified midpoint method: The modified midpoint method is globally a second order method for approximating the solution of the initial value problem y' = f(x, y), y(x0) = y0, which advances a vector of dependent variables y(x) from a point x to a point x + H by a sequence of n substeps each of size h, h = H/n."""

    MODIFIED_MIDPOINT_METHOD: "KISAO"
    """modified midpoint method: The modified midpoint method is globally a second order method for approximating the solution of the initial value problem y' = f(x, y), y(x0) = y0, which advances a vector of dependent variables y(x) from a point x to a point x + H by a sequence of n substeps each of size h, h = H/n."""

    KISAO_0000383: "KISAO"
    """Bader-Deuflhard method: The Bader-Deuflhard method is an extrapolation method based on a semi-implicit discretization [http://identifiers.org/biomodels.kisao/KISAO_0000387]. It is a generalization of the Bulirsch-Stoer algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000379] for solving ordinary differential equations."""

    BADER_DEUFLHARD_METHOD: "KISAO"
    """Bader-Deuflhard method: The Bader-Deuflhard method is an extrapolation method based on a semi-implicit discretization [http://identifiers.org/biomodels.kisao/KISAO_0000387]. It is a generalization of the Bulirsch-Stoer algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000379] for solving ordinary differential equations."""

    KISAO_0000384: "KISAO"
    """semi-implicit midpoint rule: A semi-implicit version of the midpoint method that has an even error series [http://identifiers.org/biomodels.kisao/KISAO_0000381]."""

    SEMI_IMPLICIT_MIDPOINT_RULE: "KISAO"
    """semi-implicit midpoint rule: A semi-implicit version of the midpoint method that has an even error series [http://identifiers.org/biomodels.kisao/KISAO_0000381]."""

    KISAO_0000386: "KISAO"
    """scaled preconditioned generalized minimal residual method: A scaled preconditioned version of 'generalized minimal residual algorithm' [http://identifiers.org/biomodels.kisao/KISAO_0000353]. For linear system Ax = b a preconditioner matrix P that approximates A is sought, for which linear system Px = b can be solved easily. Preconditioning is applied on the left only. Scaling is done using diagonal matrix D whose diagonal elements are weights w^i = rtol|y^i| +atol^i, where rtol is 'relative tolerance' [http://identifiers.org/biomodels.kisao/KISAO_0000209] and atol is 'absolute tolerance' [http://identifiers.org/biomodels.kisao/KISAO_0000211]."""

    SCALED_PRECONDITIONED_GENERALIZED_MINIMAL_RESIDUAL_METHOD: "KISAO"
    """scaled preconditioned generalized minimal residual method: A scaled preconditioned version of 'generalized minimal residual algorithm' [http://identifiers.org/biomodels.kisao/KISAO_0000353]. For linear system Ax = b a preconditioner matrix P that approximates A is sought, for which linear system Px = b can be solved easily. Preconditioning is applied on the left only. Scaling is done using diagonal matrix D whose diagonal elements are weights w^i = rtol|y^i| +atol^i, where rtol is 'relative tolerance' [http://identifiers.org/biomodels.kisao/KISAO_0000209] and atol is 'absolute tolerance' [http://identifiers.org/biomodels.kisao/KISAO_0000211]."""

    KISAO_0000388: "KISAO"
    """minimal residual method: The 'minimal residual method' is an algorithm for the numerical solution of indefinite symmertic systems of linear equations."""

    MINIMAL_RESIDUAL_METHOD: "KISAO"
    """minimal residual method: The 'minimal residual method' is an algorithm for the numerical solution of indefinite symmertic systems of linear equations."""

    KISAO_0000389: "KISAO"
    """quasi-minimal residual method: The QMR algorithm is a robust iterative solver for general nonsingular non-Hermitian linear systems. The method uses a robust implementation of the look-ahead Lanczos algorithm to generate basis vectors for the Krylov subspaces Kn(r0, A). The QMR iterates are characterized by a quasi-minimal residual property over Kn(r0, A)."""

    QUASI_MINIMAL_RESIDUAL_METHOD: "KISAO"
    """quasi-minimal residual method: The QMR algorithm is a robust iterative solver for general nonsingular non-Hermitian linear systems. The method uses a robust implementation of the look-ahead Lanczos algorithm to generate basis vectors for the Krylov subspaces Kn(r0, A). The QMR iterates are characterized by a quasi-minimal residual property over Kn(r0, A)."""

    KISAO_0000392: "KISAO"
    """biconjugate gradient stabilized method: An iterative method for the numerical solution of nonsymmetric linear systems. It is a variant of the biconjugate gradient method (BiCG) [http://identifiers.org/biomodels.kisao/KISAO_0000358] and has faster and smoother convergence than the original BiCG."""

    BICONJUGATE_GRADIENT_STABILIZED_METHOD: "KISAO"
    """biconjugate gradient stabilized method: An iterative method for the numerical solution of nonsymmetric linear systems. It is a variant of the biconjugate gradient method (BiCG) [http://identifiers.org/biomodels.kisao/KISAO_0000358] and has faster and smoother convergence than the original BiCG."""

    KISAO_0000393: "KISAO"
    """ingenious conjugate gradients-squared method: A Lanczos-type method for nonsymmetric sparse linear systems. The method is based on a polynomial variant of the conjugate gradients algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000357]. Although related to the so-called bi-conjugate gradients (Bi-CG) algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000358], it does not involve adjoint matrix-vector multiplications, and the expected convergence rate is about twice that of the Bi-CG algorithm."""

    INGENIOUS_CONJUGATE_GRADIENTS_SQUARED_METHOD: "KISAO"
    """ingenious conjugate gradients-squared method: A Lanczos-type method for nonsymmetric sparse linear systems. The method is based on a polynomial variant of the conjugate gradients algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000357]. Although related to the so-called bi-conjugate gradients (Bi-CG) algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000358], it does not involve adjoint matrix-vector multiplications, and the expected convergence rate is about twice that of the Bi-CG algorithm."""

    KISAO_0000394: "KISAO"
    """quasi-minimal residual variant of biconjugate gradient stabilized method: QMRCGSTAB is a quasi-minimal residual (QMR) variant of the Bi-CGSTAB algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000394] of van der Vorst for solving nonsymmetric linear systems. The motivation for the QMR variant is to obtain smoother convergence behavior of the underlying method."""

    QUASI_MINIMAL_RESIDUAL_VARIANT_OF_BICONJUGATE_GRADIENT_STABILIZED_METHOD: "KISAO"
    """quasi-minimal residual variant of biconjugate gradient stabilized method: QMRCGSTAB is a quasi-minimal residual (QMR) variant of the Bi-CGSTAB algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000394] of van der Vorst for solving nonsymmetric linear systems. The motivation for the QMR variant is to obtain smoother convergence behavior of the underlying method."""

    KISAO_0000395: "KISAO"
    """improved biconjugate gradient method: An 'improved biconjugate gradient method' branch contains algorithms which can be viewed as improvements over some of drawbacks of BCG [http://identifiers.org/biomodels.kisao/KISAO_0000358], such as (1) the need for matrix-vector multiplications with A^T (which can be inconvenient as well as doubling the number of matrix-vector multiplications compared to CG [http://identifiers.org/biomodels.kisao/KISAO_0000357] for each increase in the degree of the underlying Krylov subspace), (2) the possibility of breakdowns and (3) erratic convergence behavior."""

    IMPROVED_BICONJUGATE_GRADIENT_METHOD: "KISAO"
    """improved biconjugate gradient method: An 'improved biconjugate gradient method' branch contains algorithms which can be viewed as improvements over some of drawbacks of BCG [http://identifiers.org/biomodels.kisao/KISAO_0000358], such as (1) the need for matrix-vector multiplications with A^T (which can be inconvenient as well as doubling the number of matrix-vector multiplications compared to CG [http://identifiers.org/biomodels.kisao/KISAO_0000357] for each increase in the degree of the underlying Krylov subspace), (2) the possibility of breakdowns and (3) erratic convergence behavior."""

    KISAO_0000396: "KISAO"
    """transpose-free quasi-minimal residual algorithm: A version of CGS [http://identifiers.org/biomodels.kisao/KISAO_0000393] which 'quasi-minimizes' the residual in the space spanned by the vectors generated by the CGS iteration."""

    TRANSPOSE_FREE_QUASI_MINIMAL_RESIDUAL_ALGORITHM: "KISAO"
    """transpose-free quasi-minimal residual algorithm: A version of CGS [http://identifiers.org/biomodels.kisao/KISAO_0000393] which 'quasi-minimizes' the residual in the space spanned by the vectors generated by the CGS iteration."""

    KISAO_0000397: "KISAO"
    """preconditioning technique: Preconditioning is simply a means of transforming the original linear system into one which has the same solution, but which is likely to be easier to solve with an iterative solver."""

    PRECONDITIONING_TECHNIQUE: "KISAO"
    """preconditioning technique: Preconditioning is simply a means of transforming the original linear system into one which has the same solution, but which is likely to be easier to solve with an iterative solver."""

    KISAO_0000398: "KISAO"
    """iterative method for solving a system of linear equations."""

    ITERATIVE_METHOD_FOR_SOLVING_A_SYSTEM_OF_LINEAR_EQUATIONS: "KISAO"
    """iterative method for solving a system of linear equations."""

    KISAO_0000399: "KISAO"
    """is used by."""

    IS_USED_BY: "KISAO"
    """is used by."""

    KISAO_0000403: "KISAO"
    """homogeneousness of equation: Homogeneous equations are of the form Ly = 0, where the differential operator L is a linear operator and y is the unknown function."""

    HOMOGENEOUSNESS_OF_EQUATION: "KISAO"
    """homogeneousness of equation: Homogeneous equations are of the form Ly = 0, where the differential operator L is a linear operator and y is the unknown function."""

    KISAO_0000404: "KISAO"
    """symmetricity of matrix: In linear algebra, a symmetric matrix is a square matrix that is equal to its transpose."""

    SYMMETRICITY_OF_MATRIX: "KISAO"
    """symmetricity of matrix: In linear algebra, a symmetric matrix is a square matrix that is equal to its transpose."""

    KISAO_0000405: "KISAO"
    """type of differential equation."""

    TYPE_OF_DIFFERENTIAL_EQUATION: "KISAO"
    """type of differential equation."""

    KISAO_0000407: "KISAO"
    """steady state root-finding method: Requested by Frank T. Bergmann on Sunday, November 27, 2011 4:45:30 PM."""

    STEADY_STATE_ROOT_FINDING_METHOD: "KISAO"
    """steady state root-finding method: Requested by Frank T. Bergmann on Sunday, November 27, 2011 4:45:30 PM."""

    KISAO_0000408: "KISAO"
    """Newton-type method: Requested by Frank T. Bergmann on Sunday, November 27, 2011 4:45:30 PM."""

    NEWTON_TYPE_METHOD: "KISAO"
    """Newton-type method: Requested by Frank T. Bergmann on Sunday, November 27, 2011 4:45:30 PM."""

    KISAO_0000409: "KISAO"
    """ordinary Newton method: A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which solves the general nonlinear problem F(x)=0 by applying successive linearization F'(x[k])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,..."""

    ORDINARY_NEWTON_METHOD: "KISAO"
    """ordinary Newton method: A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which solves the general nonlinear problem F(x)=0 by applying successive linearization F'(x[k])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,..."""

    KISAO_0000410: "KISAO"
    """simplified Newton method: A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which is characterized by keeping the initial derivative throughout the whole iteration: F'(x[0])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,..."""

    SIMPLIFIED_NEWTON_METHOD: "KISAO"
    """simplified Newton method: A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which is characterized by keeping the initial derivative throughout the whole iteration: F'(x[0])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,..."""

    KISAO_0000411: "KISAO"
    """Newton-like method: A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which is characterized by the fact that, in finite dimension, the Jacodian matrices are either replaced by some fixed 'close by' Jacobian F'(z) with z not equal to the initial guess x[0], or by some approximation so that: M'(x[0])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,..."""

    NEWTON_LIKE_METHOD: "KISAO"
    """Newton-like method: A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which is characterized by the fact that, in finite dimension, the Jacodian matrices are either replaced by some fixed 'close by' Jacobian F'(z) with z not equal to the initial guess x[0], or by some approximation so that: M'(x[0])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,..."""

    KISAO_0000412: "KISAO"
    """inexact Newton method: For extremely large scale nonlinear problems the arising linear systems for the Newton corrections can no longer be solved directly ('exactly'), but must be solved iterativly ('inexactly) - which gives the name inexact Newton methods. The whole scheme then consists of an inner iteration (at Newton step k): F'(x[k])deltaxi[k]=-F(x[k])+ri[k], k=0,1,... xi[k+1]=x[k]+deltaxi[k], i=0,1,..,imax[k] in terms of residuals ri[k] and an outer iteration where, given x[0], the iterates are defined as x[k+1]=xi[k+1] for i=imax[k], k=0,1,..."""

    INEXACT_NEWTON_METHOD: "KISAO"
    """inexact Newton method: For extremely large scale nonlinear problems the arising linear systems for the Newton corrections can no longer be solved directly ('exactly'), but must be solved iterativly ('inexactly) - which gives the name inexact Newton methods. The whole scheme then consists of an inner iteration (at Newton step k): F'(x[k])deltaxi[k]=-F(x[k])+ri[k], k=0,1,... xi[k+1]=x[k]+deltaxi[k], i=0,1,..,imax[k] in terms of residuals ri[k] and an outer iteration where, given x[0], the iterates are defined as x[k+1]=xi[k+1] for i=imax[k], k=0,1,..."""

    KISAO_0000413: "KISAO"
    """exact Newton method: Any of the finite dimensional Newton-type methods [http://identifiers.org/biomodels.kisao/KISAO_0000408] requires the numerical solution of the linear equations F'(x[k])deltax[k]=-F(x[k]). Whenever direct elimination methods are applicable, we speak of exact Newton methods."""

    EXACT_NEWTON_METHOD: "KISAO"
    """exact Newton method: Any of the finite dimensional Newton-type methods [http://identifiers.org/biomodels.kisao/KISAO_0000408] requires the numerical solution of the linear equations F'(x[k])deltax[k]=-F(x[k]). Whenever direct elimination methods are applicable, we speak of exact Newton methods."""

    KISAO_0000415: "KISAO"
    """maximum number of steps: The limit on number of internal steps before an output point."""

    MAXIMUM_NUMBER_OF_STEPS: "KISAO"
    """maximum number of steps: The limit on number of internal steps before an output point."""

    KISAO_0000416: "KISAO"
    """partial least squares regression method: Requested by Kristin Tøndel on Thursday, October 13, 2011 10:46:04 AM."""

    PARTIAL_LEAST_SQUARES_REGRESSION_METHOD: "KISAO"
    """partial least squares regression method: Requested by Kristin Tøndel on Thursday, October 13, 2011 10:46:04 AM."""

    KISAO_0000417: "KISAO"
    """hierarchical cluster-based partial least squares regression method: Requested by Kristin Tøndel on Thursday, October 13, 2011 11:13:17 AM."""

    HIERARCHICAL_CLUSTER_BASED_PARTIAL_LEAST_SQUARES_REGRESSION_METHOD: "KISAO"
    """hierarchical cluster-based partial least squares regression method: Requested by Kristin Tøndel on Thursday, October 13, 2011 11:13:17 AM."""

    KISAO_0000418: "KISAO"
    """N-way partial least squares regression method: Requested by Kristin Tøndel on Thursday, October 13, 2011 11:33:06 AM."""

    N_WAY_PARTIAL_LEAST_SQUARES_REGRESSION_METHOD: "KISAO"
    """N-way partial least squares regression method: Requested by Kristin Tøndel on Thursday, October 13, 2011 11:33:06 AM."""

    KISAO_0000419: "KISAO"
    """metamodelling method: Deterministic dynamic models of complex biological systems contain a large number of parameters and state variables, related through nonlinear differential equations with various types of feedback. A metamodel of such a dynamic model is a statistical approximation model that maps variation in parameters and initial conditions (inputs) to variation in features of the trajectories of the state variables (outputs) throughout the entire biologically relevant input space."""

    METAMODELLING_METHOD: "KISAO"
    """metamodelling method: Deterministic dynamic models of complex biological systems contain a large number of parameters and state variables, related through nonlinear differential equations with various types of feedback. A metamodel of such a dynamic model is a statistical approximation model that maps variation in parameters and initial conditions (inputs) to variation in features of the trajectories of the state variables (outputs) throughout the entire biologically relevant input space."""

    KISAO_0000420: "KISAO"
    """number of partial least squares components: Parameter used by 'partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000416] describing number of PLS components to include in the regression analysis."""

    NUMBER_OF_PARTIAL_LEAST_SQUARES_COMPONENTS: "KISAO"
    """number of partial least squares components: Parameter used by 'partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000416] describing number of PLS components to include in the regression analysis."""

    KISAO_0000421: "KISAO"
    """type of validation: Parameter of 'partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000416] describing how validation is performed. Possible values include cross-validation and test set validation."""

    TYPE_OF_VALIDATION: "KISAO"
    """type of validation: Parameter of 'partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000416] describing how validation is performed. Possible values include cross-validation and test set validation."""

    KISAO_0000422: "KISAO"
    """number of N-way partial least squares regression factors: Parameter of 'N-way partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000369] describing the number of factors to compute."""

    NUMBER_OF_N_WAY_PARTIAL_LEAST_SQUARES_REGRESSION_FACTORS: "KISAO"
    """number of N-way partial least squares regression factors: Parameter of 'N-way partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000369] describing the number of factors to compute."""

    KISAO_0000423: "KISAO"
    """partial least squares regression-like method: Method for building regression models between independent and dependent variables."""

    PARTIAL_LEAST_SQUARES_REGRESSION_LIKE_METHOD: "KISAO"
    """partial least squares regression-like method: Method for building regression models between independent and dependent variables."""

    KISAO_0000424: "KISAO"
    """mean-centring of variables: A boolean parameter of the 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417] specifying whether the variables were mean-centred prior to the regression analysis."""

    MEAN_CENTRING_OF_VARIABLES: "KISAO"
    """mean-centring of variables: A boolean parameter of the 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417] specifying whether the variables were mean-centred prior to the regression analysis."""

    KISAO_0000425: "KISAO"
    """standardising of variables: A boolean parameter of the 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417] specifying whether the variables were standardised (divided by their standard deviations) prior to the regression analysis."""

    STANDARDISING_OF_VARIABLES: "KISAO"
    """standardising of variables: A boolean parameter of the 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417] specifying whether the variables were standardised (divided by their standard deviations) prior to the regression analysis."""

    KISAO_0000427: "KISAO"
    """number of clusters: Parameter specifying the number of clusters used by C-means algorithm."""

    NUMBER_OF_CLUSTERS: "KISAO"
    """number of clusters: Parameter specifying the number of clusters used by C-means algorithm."""

    KISAO_0000428: "KISAO"
    """matrix for clusterization: A matrix to do the clustering in 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417]."""

    MATRIX_FOR_CLUSTERIZATION: "KISAO"
    """matrix for clusterization: A matrix to do the clustering in 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417]."""

    KISAO_0000429: "KISAO"
    """clusterization parameter: Parameter used by algorithms performing clusterization."""

    CLUSTERIZATION_PARAMETER: "KISAO"
    """clusterization parameter: Parameter used by algorithms performing clusterization."""

    KISAO_0000430: "KISAO"
    """variables preprocessing parameter."""

    VARIABLES_PREPROCESSING_PARAMETER: "KISAO"
    """variables preprocessing parameter."""

    KISAO_0000432: "KISAO"
    """IDA-like method: Solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0. At each step, a Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408] leads to linear systems Jx=b, which are solved by one of five methods - two direct (dense or band; serial version only) and three Krylov [http://identifiers.org/biomodels.kisao/KISAO_0000354] (GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000353], BiCGStab [http://identifiers.org/biomodels.kisao/KISAO_0000392], or TFQMR [http://identifiers.org/biomodels.kisao/KISAO_0000396])."""

    IDA_LIKE_METHOD: "KISAO"
    """IDA-like method: Solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0. At each step, a Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408] leads to linear systems Jx=b, which are solved by one of five methods - two direct (dense or band; serial version only) and three Krylov [http://identifiers.org/biomodels.kisao/KISAO_0000354] (GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000353], BiCGStab [http://identifiers.org/biomodels.kisao/KISAO_0000392], or TFQMR [http://identifiers.org/biomodels.kisao/KISAO_0000396])."""

    KISAO_0000433: "KISAO"
    """CVODE-like method: Solves ODE initial value problems, in real N-space, written as y'=f(t,y), y(t0)=y0. It is capable for stiff and non-stiff systems and uses two different linear multi-step methods, namely the Adam-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] method and the backward differentiation formula [http://identifiers.org/biomodels.kisao/KISAO_0000288]."""

    CVODE_LIKE_METHOD: "KISAO"
    """CVODE-like method: Solves ODE initial value problems, in real N-space, written as y'=f(t,y), y(t0)=y0. It is capable for stiff and non-stiff systems and uses two different linear multi-step methods, namely the Adam-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] method and the backward differentiation formula [http://identifiers.org/biomodels.kisao/KISAO_0000288]."""

    KISAO_0000434: "KISAO"
    """Higham-Hall method: The equilibrium theory of Hall and Higham (1988) can be used to determine whether a Runge-Kutta algorithm will perform smoothly when stability restricts the stepsize. Higham-Hall method is a fifth order embedded Runge-Kutta method [http://identifiers.org/biomodels.kisao/KISAO_0000302], which behaves smoothly with respect to the standard type of stepsize controllers."""

    HIGHAM_HALL_METHOD: "KISAO"
    """Higham-Hall method: The equilibrium theory of Hall and Higham (1988) can be used to determine whether a Runge-Kutta algorithm will perform smoothly when stability restricts the stepsize. Higham-Hall method is a fifth order embedded Runge-Kutta method [http://identifiers.org/biomodels.kisao/KISAO_0000302], which behaves smoothly with respect to the standard type of stepsize controllers."""

    KISAO_0000435: "KISAO"
    """embedded Runge-Kutta 5(4) method: An embedded Runge-Kutta integrator of order 5(4)."""

    EMBEDDED_RUNGE_KUTTA_5_4__METHOD: "KISAO"
    """embedded Runge-Kutta 5(4) method: An embedded Runge-Kutta integrator of order 5(4)."""

    KISAO_0000436: "KISAO"
    """Dormand-Prince 8(5,3) method: This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction."""

    DORMAND_PRINCE_8_5_3__METHOD: "KISAO"
    """Dormand-Prince 8(5,3) method: This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction."""

    KISAO_0000437: "KISAO"
    """flux balance analysis: Requested by Frank T. Bergmann on Thursday, November 29, 2012 9:51:58 AM."""

    FLUX_BALANCE_ANALYSIS: "KISAO"
    """flux balance analysis: Requested by Frank T. Bergmann on Thursday, November 29, 2012 9:51:58 AM."""

    KISAO_0000447: "KISAO"
    """COAST: Requested by Mark Moeller on Friday, January 25, 2013 11:11:30 AM."""

    COAST: "KISAO"
    """COAST: Requested by Mark Moeller on Friday, January 25, 2013 11:11:30 AM."""

    KISAO_0000448: "KISAO"
    """logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. In each state a number of transitions are enabled. A 'logical model simulation method' guides the choice of the transitions processed at each step."""

    LOGICAL_MODEL_SIMULATION_METHOD: "KISAO"
    """logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. In each state a number of transitions are enabled. A 'logical model simulation method' guides the choice of the transitions processed at each step."""

    KISAO_0000449: "KISAO"
    """synchronous logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. In the case of a synchronous updating all enabled transitions are processed simultaneously."""

    SYNCHRONOUS_LOGICAL_MODEL_SIMULATION_METHOD: "KISAO"
    """synchronous logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. In the case of a synchronous updating all enabled transitions are processed simultaneously."""

    KISAO_0000450: "KISAO"
    """asynchronous logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. It the case of an asynchronous updating all enabled transitions are performed independently: a state has as many successors as the number of transitions enabled in this state. An 'asynchronous logical model simulation method' specifies a rule to guide the choice of a unique transition at each step (for example random)."""

    ASYNCHRONOUS_LOGICAL_MODEL_SIMULATION_METHOD: "KISAO"
    """asynchronous logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. It the case of an asynchronous updating all enabled transitions are performed independently: a state has as many successors as the number of transitions enabled in this state. An 'asynchronous logical model simulation method' specifies a rule to guide the choice of a unique transition at each step (for example random)."""

    KISAO_0000451: "KISAO"
    """type of updating policy: A rule to guide the choice of a unique transition at each step used by an 'asynchronous logical model simulation method' [http://identifiers.org/biomodels.kisao/KISAO_0000450]."""

    TYPE_OF_UPDATING_POLICY: "KISAO"
    """type of updating policy: A rule to guide the choice of a unique transition at each step used by an 'asynchronous logical model simulation method' [http://identifiers.org/biomodels.kisao/KISAO_0000450]."""

    KISAO_0000452: "KISAO"
    """random updating policy: An updating policy that chooses a transition randomly."""

    RANDOM_UPDATING_POLICY: "KISAO"
    """random updating policy: An updating policy that chooses a transition randomly."""

    KISAO_0000453: "KISAO"
    """ordered updating policy: An updating policy that chooses a transition in a definite way."""

    ORDERED_UPDATING_POLICY: "KISAO"
    """ordered updating policy: An updating policy that chooses a transition in a definite way."""

    KISAO_0000454: "KISAO"
    """constant updating policy: An updating policy that chooses a transition in a constant way."""

    CONSTANT_UPDATING_POLICY: "KISAO"
    """constant updating policy: An updating policy that chooses a transition in a constant way."""

    KISAO_0000455: "KISAO"
    """prioritized updating policy: An updating policy that chooses a transition in a prioritized way."""

    PRIORITIZED_UPDATING_POLICY: "KISAO"
    """prioritized updating policy: An updating policy that chooses a transition in a prioritized way."""

    KISAO_0000467: "KISAO"
    """maximum step size: Requested by Andrew Miller on Tuesday, June 4, 2013 2:33:51 AM."""

    MAXIMUM_STEP_SIZE: "KISAO"
    """maximum step size: Requested by Andrew Miller on Tuesday, June 4, 2013 2:33:51 AM."""

    KISAO_0000468: "KISAO"
    """maximal timestep method: Requested by Andrzej Kierzek on Thursday, April 24, 2014 12:40:35 PM Used to simulate systems involving reactions with propensities varying by many orders of magnitude."""

    MAXIMAL_TIMESTEP_METHOD: "KISAO"
    """maximal timestep method: Requested by Andrzej Kierzek on Thursday, April 24, 2014 12:40:35 PM Used to simulate systems involving reactions with propensities varying by many orders of magnitude."""

    KISAO_0000469: "KISAO"
    """maximal timestep: Key parameter of the 'maximal timestep method' [http://www.biomodels.net/kisao/KISAO#KISAO_0000468]. If Gillespie [http://www.biomodels.net/kisao/KISAO#KISAO_0000027] waiting time is longer than maximal timestep, slow reaction is not fired and tau-leap [http://www.biomodels.net/kisao/KISAO#KISAO_0000039] step is executed for fast reactions. Otherwise, slow reaction is fired and tau-leap [http://www.biomodels.net/kisao/KISAO#KISAO_0000039] is executed with shorter time step."""

    MAXIMAL_TIMESTEP: "KISAO"
    """maximal timestep: Key parameter of the 'maximal timestep method' [http://www.biomodels.net/kisao/KISAO#KISAO_0000468]. If Gillespie [http://www.biomodels.net/kisao/KISAO#KISAO_0000027] waiting time is longer than maximal timestep, slow reaction is not fired and tau-leap [http://www.biomodels.net/kisao/KISAO#KISAO_0000039] step is executed for fast reactions. Otherwise, slow reaction is fired and tau-leap [http://www.biomodels.net/kisao/KISAO#KISAO_0000039] is executed with shorter time step."""

    KISAO_0000470: "KISAO"
    """optimization algorithm: An optimization algorithm tries to find the minumum or maximum of an arbitrary function. It takes a function of one or several variables and determines the values for the variables so that the function value is optimal."""

    OPTIMIZATION_ALGORITHM: "KISAO"
    """optimization algorithm: An optimization algorithm tries to find the minumum or maximum of an arbitrary function. It takes a function of one or several variables and determines the values for the variables so that the function value is optimal."""

    KISAO_0000471: "KISAO"
    """local optimization algorithm: A local optimization algorithm is an optimisation algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000470] that only finds a local optimum of a function. If several optima exist for the function, it usually depends on the starting values for the variables which optimum is found."""

    LOCAL_OPTIMIZATION_ALGORITHM: "KISAO"
    """local optimization algorithm: A local optimization algorithm is an optimisation algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000470] that only finds a local optimum of a function. If several optima exist for the function, it usually depends on the starting values for the variables which optimum is found."""

    KISAO_0000472: "KISAO"
    """global optimization algorithm: A global optimization algorithm is an optimization algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000470] that tries to find the global optimum of a function. If a function has several minima/maxima with in the allowed range of variable values, the global minimum/maximum is the one with the smallest/largest function value."""

    GLOBAL_OPTIMIZATION_ALGORITHM: "KISAO"
    """global optimization algorithm: A global optimization algorithm is an optimization algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000470] that tries to find the global optimum of a function. If a function has several minima/maxima with in the allowed range of variable values, the global minimum/maximum is the one with the smallest/largest function value."""

    KISAO_0000473: "KISAO"
    """Bayesian inference algorithm: A bayesian inference algorithm calculates a posterior probability distribution from a prior probability distribution and some additional evidence in the form of a likelyhood function."""

    BAYESIAN_INFERENCE_ALGORITHM: "KISAO"
    """Bayesian inference algorithm: A bayesian inference algorithm calculates a posterior probability distribution from a prior probability distribution and some additional evidence in the form of a likelyhood function."""

    KISAO_0000475: "KISAO"
    """integration method: the integration method used by the solver"""

    INTEGRATION_METHOD: "KISAO"
    """integration method: the integration method used by the solver"""

    KISAO_0000476: "KISAO"
    """iteration type: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    ITERATION_TYPE: "KISAO"
    """iteration type: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    KISAO_0000477: "KISAO"
    """linear solver: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    LINEAR_SOLVER: "KISAO"
    """linear solver: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    KISAO_0000478: "KISAO"
    """preconditioner: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    PRECONDITIONER: "KISAO"
    """preconditioner: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    KISAO_0000479: "KISAO"
    """upper half-bandwidth: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    UPPER_HALF_BANDWIDTH: "KISAO"
    """upper half-bandwidth: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    KISAO_0000480: "KISAO"
    """lower half-bandwidth: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    LOWER_HALF_BANDWIDTH: "KISAO"
    """lower half-bandwidth: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    KISAO_0000481: "KISAO"
    """interpolate solution: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    INTERPOLATE_SOLUTION: "KISAO"
    """interpolate solution: Requested in https://sourceforge.net/p/kisao/feature-requests/12/"""

    KISAO_0000482: "KISAO"
    """half-bandwith parameter: the parameter related to the half-bandwidth value used by the Banded linear solver or preconditioner."""

    HALF_BANDWITH_PARAMETER: "KISAO"
    """half-bandwith parameter: the parameter related to the half-bandwidth value used by the Banded linear solver or preconditioner."""

    KISAO_0000483: "KISAO"
    """step size: Requested in https://sourceforge.net/p/kisao/feature-requests/13/"""

    STEP_SIZE: "KISAO"
    """step size: Requested in https://sourceforge.net/p/kisao/feature-requests/13/"""

    KISAO_0000484: "KISAO"
    """maximum order: Maximum order of method. For example, in Roadrunner it can be used for two parameters that one can set for deterministic runs: 'maximum_bdf_order' and 'maximum_adams_order'."""

    MAXIMUM_ORDER: "KISAO"
    """maximum order: Maximum order of method. For example, in Roadrunner it can be used for two parameters that one can set for deterministic runs: 'maximum_bdf_order' and 'maximum_adams_order'."""

    KISAO_0000485: "KISAO"
    """minimum step size: A lower limit, in the units of the bound variable over which a numerical integration is being performed, that a numerical integration algorithm with variable step size should take."""

    MINIMUM_STEP_SIZE: "KISAO"
    """minimum step size: A lower limit, in the units of the bound variable over which a numerical integration is being performed, that a numerical integration algorithm with variable step size should take."""

    KISAO_0000486: "KISAO"
    """maximum iterations: For algorithms that iterate to a solution (steady state finders in particular), a limit on the number of iterations that should be performed."""

    MAXIMUM_ITERATIONS: "KISAO"
    """maximum iterations: For algorithms that iterate to a solution (steady state finders in particular), a limit on the number of iterations that should be performed."""

    KISAO_0000487: "KISAO"
    """minimum damping: The damping factor is a variable for at least some steady state algorithms: roadrunner allows you to set the minimum value for this."""

    MINIMUM_DAMPING: "KISAO"
    """minimum damping: The damping factor is a variable for at least some steady state algorithms: roadrunner allows you to set the minimum value for this."""

    KISAO_0000488: "KISAO"
    """seed: Random seed of a stochastic algorithm. Setting it allows one to reproduce their results while running the same algorithm on the same computer."""

    SEED: "KISAO"
    """seed: Random seed of a stochastic algorithm. Setting it allows one to reproduce their results while running the same algorithm on the same computer."""

    KISAO_0000491: "KISAO"
    """discrete event simulation algorithm: Discrete Event Simulation algorithm refers to the simulation of systems whose (countable) discrete states change over time and are event-driven."""

    DISCRETE_EVENT_SIMULATION_ALGORITHM: "KISAO"
    """discrete event simulation algorithm: Discrete Event Simulation algorithm refers to the simulation of systems whose (countable) discrete states change over time and are event-driven."""

    KISAO_0000492: "KISAO"
    """asynchronous updating policy: An updating policy where all enabled transitions (events) occur independently. Thus a state has as many successors as the number of transitions enabled in this state."""

    ASYNCHRONOUS_UPDATING_POLICY: "KISAO"
    """asynchronous updating policy: An updating policy where all enabled transitions (events) occur independently. Thus a state has as many successors as the number of transitions enabled in this state."""

    KISAO_0000493: "KISAO"
    """synchronous updating policy: An updating policy where all enabled transitions occur simultaneously. Thus a state will have at most one successor."""

    SYNCHRONOUS_UPDATING_POLICY: "KISAO"
    """synchronous updating policy: An updating policy where all enabled transitions occur simultaneously. Thus a state will have at most one successor."""

    KISAO_0000494: "KISAO"
    """fully asynchronous updating policy: An updating policy where all enabled transitions occur either independently or (partially) simultaneously. (i.e. considering all possible combinations of enabled transitions). Thus a state has as many successors as the number of combinations of transitions enabled in this state."""

    FULLY_ASYNCHRONOUS_UPDATING_POLICY: "KISAO"
    """fully asynchronous updating policy: An updating policy where all enabled transitions occur either independently or (partially) simultaneously. (i.e. considering all possible combinations of enabled transitions). Thus a state has as many successors as the number of combinations of transitions enabled in this state."""

    KISAO_0000495: "KISAO"
    """random asynchronous updating policy: An updating policy where a single transition is picked randomly from the set of transitions enabled in this state. Thus a state will have at most one successor."""

    RANDOM_ASYNCHRONOUS_UPDATING_POLICY: "KISAO"
    """random asynchronous updating policy: An updating policy where a single transition is picked randomly from the set of transitions enabled in this state. Thus a state will have at most one successor."""

    KISAO_0000496: "KISAO"
    """CVODES: CVODES is a superset of CVODE [http://identifiers.org/biomodels.kisao/KISAO_0000019] and hence all options available to CVODE (with the exception of the FCVODE interface module) are also available for CVODES. Both integration methods (Adams-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] and BDF [http://identifiers.org/biomodels.kisao/KISAO_0000288]) and the corresponding nonlinear iteration methods, as well as all linear solver and preconditioner modules, are available for the integration of the original ODEs, the sensitivity systems, or the adjoint system."""

    CVODES: "KISAO"
    """CVODES: CVODES is a superset of CVODE [http://identifiers.org/biomodels.kisao/KISAO_0000019] and hence all options available to CVODE (with the exception of the FCVODE interface module) are also available for CVODES. Both integration methods (Adams-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] and BDF [http://identifiers.org/biomodels.kisao/KISAO_0000288]) and the corresponding nonlinear iteration methods, as well as all linear solver and preconditioner modules, are available for the integration of the original ODEs, the sensitivity systems, or the adjoint system."""

    KISAO_0000497: "KISAO"
    """KLU: KLU is a software package and an algorithm for solving sparse unsymmetric linear systems of equations that arise in circuit simulation applications. It relies on a permutation to Block Triangular Form (BTF), several methods for finding a fill-reducing ordering (variants of approximate minimum degree and nested dissection), and Gilbert/Peierls’ sparse left-looking LU factorization algorithm to factorize each block. The package is written in C and includes a MATLAB interface."""

    KLU: "KISAO"
    """KLU: KLU is a software package and an algorithm for solving sparse unsymmetric linear systems of equations that arise in circuit simulation applications. It relies on a permutation to Block Triangular Form (BTF), several methods for finding a fill-reducing ordering (variants of approximate minimum degree and nested dissection), and Gilbert/Peierls’ sparse left-looking LU factorization algorithm to factorize each block. The package is written in C and includes a MATLAB interface."""

    KISAO_0000498: "KISAO"
    """number of runs: Requested in https://sourceforge.net/p/kisao/feature-requests/31/"""

    NUMBER_OF_RUNS: "KISAO"
    """number of runs: Requested in https://sourceforge.net/p/kisao/feature-requests/31/"""

    KISAO_0000499: "KISAO"
    """dynamic flux balance analysis: Ticket 32"""

    DYNAMIC_FLUX_BALANCE_ANALYSIS: "KISAO"
    """dynamic flux balance analysis: Ticket 32"""

    KISAO_0000500: "KISAO"
    """SOA-DFBA: Ticket 32"""

    SOA_DFBA: "KISAO"
    """SOA-DFBA: Ticket 32"""

    KISAO_0000501: "KISAO"
    """DOA-DFBA: Ticket 32"""

    DOA_DFBA: "KISAO"
    """DOA-DFBA: Ticket 32"""

    KISAO_0000502: "KISAO"
    """DA-DFBA: Ticket 32"""

    DA_DFBA: "KISAO"
    """DA-DFBA: Ticket 32"""

    KISAO_0000503: "KISAO"
    """simulated annealing: Simulated annealing is an optimization algorithm first proposed by Kirkpatrick et al. and was inspired by statistical mechanics and the way in which perfect crystals are formed. Perfect crystals are formed by first melting the substance of interest, and then cooling it very slowly. At large temperatures the particles vibrate with wide amplitude and this allows a search for global optimum. As the temperature decreases so do the vibrations until the system settles to the global optimum (the perfect crystal). The simulated annealing optimization algorithm uses a similar concept: the objective function is considered a measure of the energy of the system and this is maintained constant for a certain number of iterations (a temperature cycle). In each iteration, the parameters are changed to a nearby location in parameter space and the new objective function value calculated; if it decreased, then the new state is accepted, if it increased then the new state is accepted with a probability that follows a Boltzmann distribution (higher temperature means higher probability of accepting the new state). After a fixed number of iterations, the stopping criterion is checked; if it is not time to stop, then the system's temperature is reduced and the algorithm continues. Simulated annealing is a stochastic algorithm that is guaranteed to converge if ran for an infinite number of iterations. It is one of the most robust global optimization algorithms, although it is also one of the slowest. (Be warned that simulated annealing can run for hours or even days!)."""

    SIMULATED_ANNEALING: "KISAO"
    """simulated annealing: Simulated annealing is an optimization algorithm first proposed by Kirkpatrick et al. and was inspired by statistical mechanics and the way in which perfect crystals are formed. Perfect crystals are formed by first melting the substance of interest, and then cooling it very slowly. At large temperatures the particles vibrate with wide amplitude and this allows a search for global optimum. As the temperature decreases so do the vibrations until the system settles to the global optimum (the perfect crystal). The simulated annealing optimization algorithm uses a similar concept: the objective function is considered a measure of the energy of the system and this is maintained constant for a certain number of iterations (a temperature cycle). In each iteration, the parameters are changed to a nearby location in parameter space and the new objective function value calculated; if it decreased, then the new state is accepted, if it increased then the new state is accepted with a probability that follows a Boltzmann distribution (higher temperature means higher probability of accepting the new state). After a fixed number of iterations, the stopping criterion is checked; if it is not time to stop, then the system's temperature is reduced and the algorithm continues. Simulated annealing is a stochastic algorithm that is guaranteed to converge if ran for an infinite number of iterations. It is one of the most robust global optimization algorithms, although it is also one of the slowest. (Be warned that simulated annealing can run for hours or even days!)."""

    KISAO_0000504: "KISAO"
    """random search: Random search is an optimization method that attempts to find the optimum by testing the objective function's value on a series of combinations of random values of the adjustable parameters. The random values are generated complying with any boundaries selected by the user, furthermore, any combinations of parameter values that do not fulfill constraints on the variables are excluded. This means that the method is capable of handling bounds on the adjustable parameters and fulfilling constraints. For infinite number of iterations this method is guaranteed to find the global optimum of the objective function. In general one is interested in processing a very large number of iterations."""

    RANDOM_SEARCH: "KISAO"
    """random search: Random search is an optimization method that attempts to find the optimum by testing the objective function's value on a series of combinations of random values of the adjustable parameters. The random values are generated complying with any boundaries selected by the user, furthermore, any combinations of parameter values that do not fulfill constraints on the variables are excluded. This means that the method is capable of handling bounds on the adjustable parameters and fulfilling constraints. For infinite number of iterations this method is guaranteed to find the global optimum of the objective function. In general one is interested in processing a very large number of iterations."""

    KISAO_0000505: "KISAO"
    """particle swarm: The particle swarm optimization method suggested by Kennedy and Eberhart is inspired by a flock of birds or a school of fish searching for food. Each particle has a position Xi and a velocity Vi in the parameter space. Additionally, it remembers its best achieved objective value O and position Mi. Dependent on its own information and the position of its best neighbor (a random subset of particles of the swarm) a new velocity is calculated. With this information the position is updated."""

    PARTICLE_SWARM: "KISAO"
    """particle swarm: The particle swarm optimization method suggested by Kennedy and Eberhart is inspired by a flock of birds or a school of fish searching for food. Each particle has a position Xi and a velocity Vi in the parameter space. Additionally, it remembers its best achieved objective value O and position Mi. Dependent on its own information and the position of its best neighbor (a random subset of particles of the swarm) a new velocity is calculated. With this information the position is updated."""

    KISAO_0000506: "KISAO"
    """genetic algorithm: The genetic algorithm (GA) is a computational technique that mimics evolution and is based on reproduction and selection. A GA is composed of individuals that reproduce and compete, each one is a potential solution to the (optimization) problem and is represented by a 'genome' where each gene corresponds to one adjustable parameter. At each generation of the GA, each individual is paired with one other at random for reproduction. Two offspring are produced by combining their genomes and allowing for 'cross-over', i.e., the two new individuals have genomes that are formed from a combination of the genomes of their parents. Also each new gene might have mutated, i.e. the parameter value might have changed slightly. At the end of the generation, the algorithm has double the number of individuals. Then each of the individuals is confronted with a number of others to count how many does it outperform (the number of wins is the number of these competitors that represent worse solutions than itself). All the individuals are ranked by their number of wins, and the population is again reduced to the original number of individuals by eliminating those which have worse fitness (solutions)."""

    GENETIC_ALGORITHM: "KISAO"
    """genetic algorithm: The genetic algorithm (GA) is a computational technique that mimics evolution and is based on reproduction and selection. A GA is composed of individuals that reproduce and compete, each one is a potential solution to the (optimization) problem and is represented by a 'genome' where each gene corresponds to one adjustable parameter. At each generation of the GA, each individual is paired with one other at random for reproduction. Two offspring are produced by combining their genomes and allowing for 'cross-over', i.e., the two new individuals have genomes that are formed from a combination of the genomes of their parents. Also each new gene might have mutated, i.e. the parameter value might have changed slightly. At the end of the generation, the algorithm has double the number of individuals. Then each of the individuals is confronted with a number of others to count how many does it outperform (the number of wins is the number of these competitors that represent worse solutions than itself). All the individuals are ranked by their number of wins, and the population is again reduced to the original number of individuals by eliminating those which have worse fitness (solutions)."""

    KISAO_0000507: "KISAO"
    """genetic algorithm SR."""

    GENETIC_ALGORITHM_SR: "KISAO"
    """genetic algorithm SR."""

    KISAO_0000508: "KISAO"
    """evolutionary programming: Evolutionary programming (EP) is a computational technique that mimics evolution and is based on reproduction and selection. An EP algorithm is composed of individuals that reproduce and compete, each one is a potential solution to the (optimization) problem and is represented by a 'genome' where each gene corresponds to one adjustable parameter. At each generation of the EP, each individual reproduces asexually, i.e. divides into two individuals. One of these contains exactly the same 'genome' as the parent while the other suffers some mutations (the parameter values of each gene change slightly). At the end of the generation, the algorithm has double the number of individuals. Then each of the individuals is confronted with a number of others to count how many does it outperform (the number of wins is the number of these competitors that represent worse solutions than itself). All the individuals are ranked by their number of wins, and the population is again reduced to the original number of individuals by eliminating those which have worse fitness (solutions)."""

    EVOLUTIONARY_PROGRAMMING: "KISAO"
    """evolutionary programming: Evolutionary programming (EP) is a computational technique that mimics evolution and is based on reproduction and selection. An EP algorithm is composed of individuals that reproduce and compete, each one is a potential solution to the (optimization) problem and is represented by a 'genome' where each gene corresponds to one adjustable parameter. At each generation of the EP, each individual reproduces asexually, i.e. divides into two individuals. One of these contains exactly the same 'genome' as the parent while the other suffers some mutations (the parameter values of each gene change slightly). At the end of the generation, the algorithm has double the number of individuals. Then each of the individuals is confronted with a number of others to count how many does it outperform (the number of wins is the number of these competitors that represent worse solutions than itself). All the individuals are ranked by their number of wins, and the population is again reduced to the original number of individuals by eliminating those which have worse fitness (solutions)."""

    KISAO_0000509: "KISAO"
    """evolutionary strategy: Evolutionary Strategies with Stochastic Ranking (SRES) is similar to Evolutionary Programming. However, a parent has multiple offsprings during each generation. Each offspring will contain a recombination of genes with another parent and additional mutations. The algorithm assures that each parameter value will be within its boundaries. But constraints to the solutions may be violated."""

    EVOLUTIONARY_STRATEGY: "KISAO"
    """evolutionary strategy: Evolutionary Strategies with Stochastic Ranking (SRES) is similar to Evolutionary Programming. However, a parent has multiple offsprings during each generation. Each offspring will contain a recombination of genes with another parent and additional mutations. The algorithm assures that each parameter value will be within its boundaries. But constraints to the solutions may be violated."""

    KISAO_0000510: "KISAO"
    """truncated Newton: The Truncated Newton method is a sophisticated variant of the Newton optimization method. The Newton optimization method searches for the minimum of a nonlinear function by following descent directions determined from the function's first and second partial derivatives. The Truncated Newton method does an incomplete (truncated) solution of a system of linear equations to calculate the Newton direction. This means that the actual direction chosen for the descent is between the steepest descent direction and the true Newton direction."""

    TRUNCATED_NEWTON: "KISAO"
    """truncated Newton: The Truncated Newton method is a sophisticated variant of the Newton optimization method. The Newton optimization method searches for the minimum of a nonlinear function by following descent directions determined from the function's first and second partial derivatives. The Truncated Newton method does an incomplete (truncated) solution of a system of linear equations to calculate the Newton direction. This means that the actual direction chosen for the descent is between the steepest descent direction and the true Newton direction."""

    KISAO_0000511: "KISAO"
    """steepest descent: Steepest descent is an optimization method that follows the direction of steepest descent on the hyper-surface of the objective function to find a local minimum. The direction of steepest descent is defined by the negative of the gradient of the objective function."""

    STEEPEST_DESCENT: "KISAO"
    """steepest descent: Steepest descent is an optimization method that follows the direction of steepest descent on the hyper-surface of the objective function to find a local minimum. The direction of steepest descent is defined by the negative of the gradient of the objective function."""

    KISAO_0000512: "KISAO"
    """praxis: Praxis is a direct search method that searches for the minimum of a nonlinear function without requiring (or attempting to calculate) derivatives of that function. Praxis was developed by Brent after the method proposed by Powell. The inspiration for Praxis was the well-known method of minimising each adjustable parameter (direction) at a time - the principal axes method. In Praxis directions are chosen that do not coincide with the principal axes, in fact if the objective function is quadratic then these will be conjugate directions, assuring a fast convergence rate."""

    PRAXIS: "KISAO"
    """praxis: Praxis is a direct search method that searches for the minimum of a nonlinear function without requiring (or attempting to calculate) derivatives of that function. Praxis was developed by Brent after the method proposed by Powell. The inspiration for Praxis was the well-known method of minimising each adjustable parameter (direction) at a time - the principal axes method. In Praxis directions are chosen that do not coincide with the principal axes, in fact if the objective function is quadratic then these will be conjugate directions, assuring a fast convergence rate."""

    KISAO_0000513: "KISAO"
    """NL2SOL: The NL2SOL method is based on an adaptive nonlinear least-squares algorithm, devised by Dennis and colleagues. For problems with large number of residuals, this algorithm is known to be more reliable than Gauss-Newton or Levenberg-Marquardt method and more efficient than the secant or variable metric algorithms that are intended for general function minimization."""

    NL2SOL: "KISAO"
    """NL2SOL: The NL2SOL method is based on an adaptive nonlinear least-squares algorithm, devised by Dennis and colleagues. For problems with large number of residuals, this algorithm is known to be more reliable than Gauss-Newton or Levenberg-Marquardt method and more efficient than the secant or variable metric algorithms that are intended for general function minimization."""

    KISAO_0000514: "KISAO"
    """Nelder-Mead: This method also known as the simplex method is due to Nelder and Mead. A simplex is a polytope of N+1 vertices in N dimensions. The objective function is evaluated at each vertex. Dependent on these calculated values a new simplex is constructed. The simplest step is to replace the worst point with a point reflected through the centroid of the remaining N points. If this point is better than the best current point, then we can try stretching exponentially out along this line. On the other hand, if this new point isn't much better than the previous value then we are stepping across a valley, so we shrink the simplex towards the best point."""

    NELDER_MEAD: "KISAO"
    """Nelder-Mead: This method also known as the simplex method is due to Nelder and Mead. A simplex is a polytope of N+1 vertices in N dimensions. The objective function is evaluated at each vertex. Dependent on these calculated values a new simplex is constructed. The simplest step is to replace the worst point with a point reflected through the centroid of the remaining N points. If this point is better than the best current point, then we can try stretching exponentially out along this line. On the other hand, if this new point isn't much better than the previous value then we are stepping across a valley, so we shrink the simplex towards the best point."""

    KISAO_0000515: "KISAO"
    """Levenberg-Marquardt: Levenberg-Marquardt is a gradient descent method. It is a hybrid between the steepest descent and the Newton methods. Levenberg first suggested an improvement to the Newton method in order to make it more robust, i.e. to overcome the problem of non-convergence. His suggestion was to add a factor to the diagonal elements of the Hessian matrix of second derivatives when not close to the minimum (this can be judged by how positive definite the matrix is). The effect when this factor is large compared to the elements of Hessian is that the method then becomes the steepest descent method. Later Marquardt suggested that the factor should be multiplicative rather than additive and also defined a heuristic to make this factor increase or decrease. The method known as Levenberg-Marquardt is thus an adaptive method that effectively changes between the steepest descent to the Newton method."""

    LEVENBERG_MARQUARDT: "KISAO"
    """Levenberg-Marquardt: Levenberg-Marquardt is a gradient descent method. It is a hybrid between the steepest descent and the Newton methods. Levenberg first suggested an improvement to the Newton method in order to make it more robust, i.e. to overcome the problem of non-convergence. His suggestion was to add a factor to the diagonal elements of the Hessian matrix of second derivatives when not close to the minimum (this can be judged by how positive definite the matrix is). The effect when this factor is large compared to the elements of Hessian is that the method then becomes the steepest descent method. Later Marquardt suggested that the factor should be multiplicative rather than additive and also defined a heuristic to make this factor increase or decrease. The method known as Levenberg-Marquardt is thus an adaptive method that effectively changes between the steepest descent to the Newton method."""

    KISAO_0000516: "KISAO"
    """Hooke&Jeeves: The method of Hooke and Jeeves is a direct search algorithm that searches for the minimum of a nonlinear function without requiring (or attempting to calculate) derivatives of the function. Instead it is based on a heuristic that suggests a descent direction using the values of the function calculated in a number of previous iterations."""

    HOOKE_JEEVES: "KISAO"
    """Hooke&Jeeves: The method of Hooke and Jeeves is a direct search algorithm that searches for the minimum of a nonlinear function without requiring (or attempting to calculate) derivatives of the function. Instead it is based on a heuristic that suggests a descent direction using the values of the function calculated in a number of previous iterations."""

    KISAO_0000517: "KISAO"
    """number of generations: The parameter is a positive integer value to determine the number of generations the evolutionary algorithm shall evolve the population."""

    NUMBER_OF_GENERATIONS: "KISAO"
    """number of generations: The parameter is a positive integer value to determine the number of generations the evolutionary algorithm shall evolve the population."""

    KISAO_0000518: "KISAO"
    """evolutionary algorithm parameter."""

    EVOLUTIONARY_ALGORITHM_PARAMETER: "KISAO"
    """evolutionary algorithm parameter."""

    KISAO_0000519: "KISAO"
    """population size: The parameter is a positive integer value to determine the size of the population, i.e., the number of individuals that survive after each generation."""

    POPULATION_SIZE: "KISAO"
    """population size: The parameter is a positive integer value to determine the size of the population, i.e., the number of individuals that survive after each generation."""

    KISAO_0000520: "KISAO"
    """evolutionary algorithm: An optimisation algorithm that mimics evolution and is based on reproduction and selection."""

    EVOLUTIONARY_ALGORITHM: "KISAO"
    """evolutionary algorithm: An optimisation algorithm that mimics evolution and is based on reproduction and selection."""

    KISAO_0000521: "KISAO"
    """simulated annealing parameter."""

    SIMULATED_ANNEALING_PARAMETER: "KISAO"
    """simulated annealing parameter."""

    KISAO_0000522: "KISAO"
    """start temperature: Initial temperature of the system. The higher the temperature, the larger the probability that a global optimum is found. Note that the temperature should be very high in the beginning of the method (the system should be above the 'melting' temperature). This value has the same units as the objective function, so what represents 'high' is different from problem to problem."""

    START_TEMPERATURE: "KISAO"
    """start temperature: Initial temperature of the system. The higher the temperature, the larger the probability that a global optimum is found. Note that the temperature should be very high in the beginning of the method (the system should be above the 'melting' temperature). This value has the same units as the objective function, so what represents 'high' is different from problem to problem."""

    KISAO_0000523: "KISAO"
    """cooling factor: Rate by which the temperature is reduced from one cycle to the next, given by the formula: Tnew=Told*'Cooling Factor'. The simulated annealing algorithm works best if the temperature is reduced at a slow rate, so this value should be close to 1."""

    COOLING_FACTOR: "KISAO"
    """cooling factor: Rate by which the temperature is reduced from one cycle to the next, given by the formula: Tnew=Told*'Cooling Factor'. The simulated annealing algorithm works best if the temperature is reduced at a slow rate, so this value should be close to 1."""

    KISAO_0000524: "KISAO"
    """partitioned leaping method: Multiscale simulation approach for modeling stochasticity in chemical reaction networks. The approach seamlessly integrates exact-stochastic and 'leaping' methodologies into a single partitioned leaping algorithmic framework. The technique correctly accounts for stochastic noise at significantly reduced computational cost, requires the definition of only three modelindependent parameters and is particularly well-suited for simulating systems containing widely disparate species populations."""

    PARTITIONED_LEAPING_METHOD: "KISAO"
    """partitioned leaping method: Multiscale simulation approach for modeling stochasticity in chemical reaction networks. The approach seamlessly integrates exact-stochastic and 'leaping' methodologies into a single partitioned leaping algorithmic framework. The technique correctly accounts for stochastic noise at significantly reduced computational cost, requires the definition of only three modelindependent parameters and is particularly well-suited for simulating systems containing widely disparate species populations."""

    KISAO_0000525: "KISAO"
    """stop condition: A condition upon which a simulation should terminate."""

    STOP_CONDITION: "KISAO"
    """stop condition: A condition upon which a simulation should terminate."""

    KISAO_0000526: "KISAO"
    """flux variability analysis: Method for determining the minimum and maximum flux of each reaction that satisfies the flux constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model."""

    FLUX_VARIABILITY_ANALYSIS: "KISAO"
    """flux variability analysis: Method for determining the minimum and maximum flux of each reaction that satisfies the flux constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model."""

    KISAO_0000527: "KISAO"
    """geometric flux balance analysis: Method for determining the central flux distribution among all flux distributions that satisfy the constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model."""

    GEOMETRIC_FLUX_BALANCE_ANALYSIS: "KISAO"
    """geometric flux balance analysis: Method for determining the central flux distribution among all flux distributions that satisfy the constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model."""

    KISAO_0000528: "KISAO"
    """parsimonious enzyme usage flux balance analysis (minimum sum of absolute fluxes): Method for determining the smallest flux distribution among all flux distributions that satisfy the constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model."""

    PARSIMONIOUS_ENZYME_USAGE_FLUX_BALANCE_ANALYSIS__MINIMUM_SUM_OF_ABSOLUTE_FLUXES_: (
        "KISAO"
    )
    """parsimonious enzyme usage flux balance analysis (minimum sum of absolute fluxes): Method for determining the smallest flux distribution among all flux distributions that satisfy the constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model."""

    KISAO_0000529: "KISAO"
    """parallelism: Number of parallel processes to use."""

    PARALLELISM: "KISAO"
    """parallelism: Number of parallel processes to use."""

    KISAO_0000531: "KISAO"
    """fraction of optimum: Fraction of the optimum solution which must be maintained."""

    FRACTION_OF_OPTIMUM: "KISAO"
    """fraction of optimum: Fraction of the optimum solution which must be maintained."""

    KISAO_0000532: "KISAO"
    """loopless: Whether to return only loopless flux solutions."""

    LOOPLESS: "KISAO"
    """loopless: Whether to return only loopless flux solutions."""

    KISAO_0000533: "KISAO"
    """pFBA factor: Maximum permissible sum of absolute fluxes."""

    PFBA_FACTOR: "KISAO"
    """pFBA factor: Maximum permissible sum of absolute fluxes."""

    KISAO_0000534: "KISAO"
    """reactions: FVA algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000526] parameter: reactions to compute the variablity of."""

    REACTIONS: "KISAO"
    """reactions: FVA algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000526] parameter: reactions to compute the variablity of."""

    KISAO_0000535: "KISAO"
    """VODE: VODE provides implicit Adams method (for non-stiff problems) and a method based on backward differentiation formulas (BDF) (for stiff problems)."""

    VODE: "KISAO"
    """VODE: VODE provides implicit Adams method (for non-stiff problems) and a method based on backward differentiation formulas (BDF) (for stiff problems)."""

    KISAO_0000536: "KISAO"
    """ZVODE: ZVODE provides implicit Adams method (for non-stiff problems) and a method based on backward differentiation formulas (BDF) (for stiff problems)."""

    ZVODE: "KISAO"
    """ZVODE: ZVODE provides implicit Adams method (for non-stiff problems) and a method based on backward differentiation formulas (BDF) (for stiff problems)."""

    KISAO_0000537: "KISAO"
    """explicit Runge-Kutta method of order 3(2): RK23 uses the Bogacki-Shampine pair of formulas [1]. The error is controlled assuming accuracy of the second-order method, but steps are taken using the third-order accurate formula (local extrapolation is done). A cubic Hermite polynomial is used for the dense output."""

    EXPLICIT_RUNGE_KUTTA_METHOD_OF_ORDER_3_2_: "KISAO"
    """explicit Runge-Kutta method of order 3(2): RK23 uses the Bogacki-Shampine pair of formulas [1]. The error is controlled assuming accuracy of the second-order method, but steps are taken using the third-order accurate formula (local extrapolation is done). A cubic Hermite polynomial is used for the dense output."""

    KISAO_0000538: "KISAO"
    """safety factor on new step selection."""

    SAFETY_FACTOR_ON_NEW_STEP_SELECTION: "KISAO"
    """safety factor on new step selection."""

    KISAO_0000539: "KISAO"
    """minimum factor to change step size by: Minimum factor to increase/decrease step size by in one step. The new step-size is chosen subject to the restriction fac1 <= current step-size / old step-size <= fac2."""

    MINIMUM_FACTOR_TO_CHANGE_STEP_SIZE_BY: "KISAO"
    """minimum factor to change step size by: Minimum factor to increase/decrease step size by in one step. The new step-size is chosen subject to the restriction fac1 <= current step-size / old step-size <= fac2."""

    KISAO_0000540: "KISAO"
    """maximum factor to change step size by: Maximum factor to increase/decrease step size by in one step. The new step-size is chosen subject to the restriction fac1 <= current step-size / old step-size <= fac2."""

    MAXIMUM_FACTOR_TO_CHANGE_STEP_SIZE_BY: "KISAO"
    """maximum factor to change step size by: Maximum factor to increase/decrease step size by in one step. The new step-size is chosen subject to the restriction fac1 <= current step-size / old step-size <= fac2."""

    KISAO_0000541: "KISAO"
    """beta parameter for stabilized step size control."""

    BETA_PARAMETER_FOR_STABILIZED_STEP_SIZE_CONTROL: "KISAO"
    """beta parameter for stabilized step size control."""

    KISAO_0000542: "KISAO"
    """correction step should use internally generated full Jacobian: Specifies whether the iteration method of the ODE solver’s correction step is chord iteration with an internally generated full Jacobian or functional iteration with no Jacobian. Option is only considered when the user has not supplied a Jacobian function and has not indicated (by setting either upper or lower band) that the Jacobian is banded."""

    CORRECTION_STEP_SHOULD_USE_INTERNALLY_GENERATED_FULL_JACOBIAN: "KISAO"
    """correction step should use internally generated full Jacobian: Specifies whether the iteration method of the ODE solver’s correction step is chord iteration with an internally generated full Jacobian or functional iteration with no Jacobian. Option is only considered when the user has not supplied a Jacobian function and has not indicated (by setting either upper or lower band) that the Jacobian is banded."""

    KISAO_0000543: "KISAO"
    """stability limit detection flag: Flag to activate stability limit detection."""

    STABILITY_LIMIT_DETECTION_FLAG: "KISAO"
    """stability limit detection flag: Flag to activate stability limit detection."""

    KISAO_0000544: "KISAO"
    """IDAS: IDAS solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0 with sensitivity analysis."""

    IDAS: "KISAO"
    """IDAS: IDAS solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0 with sensitivity analysis."""

    KISAO_0000545: "KISAO"
    """include sensitivity variables in error control mechanism: Specifies whether sensitivity variables are included or not in the error control mechanism."""

    INCLUDE_SENSITIVITY_VARIABLES_IN_ERROR_CONTROL_MECHANISM: "KISAO"
    """include sensitivity variables in error control mechanism: Specifies whether sensitivity variables are included or not in the error control mechanism."""

    KISAO_0000546: "KISAO"
    """convex optimization algorithm: Optimization of a convex function over a convex set. Convex optimization is subclass of global optimization because conveness gaurantees that each local optimum is a global optimum."""

    CONVEX_OPTIMIZATION_ALGORITHM: "KISAO"
    """convex optimization algorithm: Optimization of a convex function over a convex set. Convex optimization is subclass of global optimization because conveness gaurantees that each local optimum is a global optimum."""

    KISAO_0000547: "KISAO"
    """linear programming: Method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships."""

    LINEAR_PROGRAMMING: "KISAO"
    """linear programming: Method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships."""

    KISAO_0000548: "KISAO"
    """quadratic programming: Process of solving a quadratic optimization problem."""

    QUADRATIC_PROGRAMMING: "KISAO"
    """quadratic programming: Process of solving a quadratic optimization problem."""

    KISAO_0000549: "KISAO"
    """non-linear programming: Process of solving an optimization problem where some of the constraints or the objective function are nonlinear."""

    NON_LINEAR_PROGRAMMING: "KISAO"
    """non-linear programming: Process of solving an optimization problem where some of the constraints or the objective function are nonlinear."""

    KISAO_0000550: "KISAO"
    """simplex method: Approach to solving linear programming models by hand using slack variables, tableaus, and pivot variables as a means to finding the optimal solution of an optimization problem."""

    SIMPLEX_METHOD: "KISAO"
    """simplex method: Approach to solving linear programming models by hand using slack variables, tableaus, and pivot variables as a means to finding the optimal solution of an optimization problem."""

    KISAO_0000551: "KISAO"
    """primal-dual interior point method: The Interior Point method approximates the constraints of a linear programming model as a set of boundaries surrounding a region."""

    PRIMAL_DUAL_INTERIOR_POINT_METHOD: "KISAO"
    """primal-dual interior point method: The Interior Point method approximates the constraints of a linear programming model as a set of boundaries surrounding a region."""

    KISAO_0000552: "KISAO"
    """optimization method: Optimization method such as the revised simplex method [http://identifiers.org/biomodels.kisao/KISAO_0000550] or primal-dual interior point method [http://identifiers.org/biomodels.kisao/KISAO_0000551]."""

    OPTIMIZATION_METHOD: "KISAO"
    """optimization method: Optimization method such as the revised simplex method [http://identifiers.org/biomodels.kisao/KISAO_0000550] or primal-dual interior point method [http://identifiers.org/biomodels.kisao/KISAO_0000551]."""

    KISAO_0000553: "KISAO"
    """optimization solver: Optimization solver such as CPLEX, GLPK, or Gurobi."""

    OPTIMIZATION_SOLVER: "KISAO"
    """optimization solver: Optimization solver such as CPLEX, GLPK, or Gurobi."""

    KISAO_0000554: "KISAO"
    """parsimonius flux balance analysis (minimum number of active fluxes): A technique for selecting a parsimonious flux distribution which has a minimal number of active fluxes."""

    PARSIMONIUS_FLUX_BALANCE_ANALYSIS__MINIMUM_NUMBER_OF_ACTIVE_FLUXES_: "KISAO"
    """parsimonius flux balance analysis (minimum number of active fluxes): A technique for selecting a parsimonious flux distribution which has a minimal number of active fluxes."""

    KISAO_0000555: "KISAO"
    """absolute quadrature tolerance: Absolute error tolerance of the adjoint solution."""

    ABSOLUTE_QUADRATURE_TOLERANCE: "KISAO"
    """absolute quadrature tolerance: Absolute error tolerance of the adjoint solution."""

    KISAO_0000556: "KISAO"
    """relative quadrature tolerance: Relative error tolerance of the adjoint solution."""

    RELATIVE_QUADRATURE_TOLERANCE: "KISAO"
    """relative quadrature tolerance: Relative error tolerance of the adjoint solution."""

    KISAO_0000557: "KISAO"
    """absolute steady-state tolerance: Absolute error tolerance of the steady-state."""

    ABSOLUTE_STEADY_STATE_TOLERANCE: "KISAO"
    """absolute steady-state tolerance: Absolute error tolerance of the steady-state."""

    KISAO_0000558: "KISAO"
    """relative steady-state tolerance: Relative error tolerance of the steady-state."""

    RELATIVE_STEADY_STATE_TOLERANCE: "KISAO"
    """relative steady-state tolerance: Relative error tolerance of the steady-state."""

    KISAO_0000559: "KISAO"
    """initial step size: Initial time step size."""

    INITIAL_STEP_SIZE: "KISAO"
    """initial step size: Initial time step size."""

    KISAO_0000560: "KISAO"
    """LSODA/LSODAR hybrid method: Automatically use LSODA or LSODAR as apropriate for the given problem. Use LSODA if the problem has no roots. Use LSODAR if the problem has roots."""

    LSODA_LSODAR_HYBRID_METHOD: "KISAO"
    """LSODA/LSODAR hybrid method: Automatically use LSODA or LSODAR as apropriate for the given problem. Use LSODA if the problem has no roots. Use LSODAR if the problem has roots."""

    KISAO_0000561: "KISAO"
    """Pahle hybrid Gibson-Bruck Next Reaction method/Runge-Kutta method: Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. A 4th-order Runge-Kutta method is used to numerically integrate the deterministic part of the system. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method."""

    PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_RUNGE_KUTTA_METHOD: "KISAO"
    """Pahle hybrid Gibson-Bruck Next Reaction method/Runge-Kutta method: Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. A 4th-order Runge-Kutta method is used to numerically integrate the deterministic part of the system. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method."""

    KISAO_0000562: "KISAO"
    """Pahle hybrid Gibson-Bruck Next Reaction method/LSODA method: Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. The deterministic subnet is integrated with LSODA. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method."""

    PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_LSODA_METHOD: "KISAO"
    """Pahle hybrid Gibson-Bruck Next Reaction method/LSODA method: Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. The deterministic subnet is integrated with LSODA. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method."""

    KISAO_0000563: "KISAO"
    """Pahle hybrid Gibson-Bruck Next Reaction method/RK-45 method: Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. The deterministic subnet is integrated with RK-45. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method."""

    PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_RK_45_METHOD: "KISAO"
    """Pahle hybrid Gibson-Bruck Next Reaction method/RK-45 method: Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. The deterministic subnet is integrated with RK-45. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method."""

    KISAO_0000564: "KISAO"
    """stochastic Runge-Kutta method: Technique for the approximate numerical solution of a systems of stochastic differential equations (SDEs). The method is a generalisation of the Runge-Kutta method for ordinary differential equations to stochastic differential equations."""

    STOCHASTIC_RUNGE_KUTTA_METHOD: "KISAO"
    """stochastic Runge-Kutta method: Technique for the approximate numerical solution of a systems of stochastic differential equations (SDEs). The method is a generalisation of the Runge-Kutta method for ordinary differential equations to stochastic differential equations."""

    KISAO_0000565: "KISAO"
    """absolute tolerance for root finding: Absolute error tolerance for root finding."""

    ABSOLUTE_TOLERANCE_FOR_ROOT_FINDING: "KISAO"
    """absolute tolerance for root finding: Absolute error tolerance for root finding."""

    KISAO_0000566: "KISAO"
    """stochastic second order Runge-Kutta method: Technique for the second order approximate numerical solution of a systems of stochastic differential equations (SDEs). The method is a generalisation of the Runge-Kutta method for ordinary differential equations to stochastic differential equations."""

    STOCHASTIC_SECOND_ORDER_RUNGE_KUTTA_METHOD: "KISAO"
    """stochastic second order Runge-Kutta method: Technique for the second order approximate numerical solution of a systems of stochastic differential equations (SDEs). The method is a generalisation of the Runge-Kutta method for ordinary differential equations to stochastic differential equations."""

    KISAO_0000567: "KISAO"
    """force physical correctness: Indicates whether to force physical correctness."""

    FORCE_PHYSICAL_CORRECTNESS: "KISAO"
    """force physical correctness: Indicates whether to force physical correctness."""

    KISAO_0000568: "KISAO"
    """NLEQ1: Damped Newton-algorithm with rank strategy for systems of highly nonlinear equations. Global Newton method with error oriented convergence criterion; arbitrary selection of direct linear equation solver."""

    NLEQ1: "KISAO"
    """NLEQ1: Damped Newton-algorithm with rank strategy for systems of highly nonlinear equations. Global Newton method with error oriented convergence criterion; arbitrary selection of direct linear equation solver."""

    KISAO_0000569: "KISAO"
    """NLEQ2: Damped Newton-algorithm with rank strategy for systems of highly nonlinear equations. Global Newton method with error oriented convergence criterion; QR-decomposition with subcondition number estimate."""

    NLEQ2: "KISAO"
    """NLEQ2: Damped Newton-algorithm with rank strategy for systems of highly nonlinear equations. Global Newton method with error oriented convergence criterion; QR-decomposition with subcondition number estimate."""

    KISAO_0000570: "KISAO"
    """auto reduce tolerances: Whether to automatically reduce tolerances."""

    AUTO_REDUCE_TOLERANCES: "KISAO"
    """auto reduce tolerances: Whether to automatically reduce tolerances."""

    KISAO_0000571: "KISAO"
    """absolute tolerance adjustment factor: How much to adjust the absolute tolerance."""

    ABSOLUTE_TOLERANCE_ADJUSTMENT_FACTOR: "KISAO"
    """absolute tolerance adjustment factor: How much to adjust the absolute tolerance."""

    KISAO_0000572: "KISAO"
    """level of superimposed noise: Standard deviation of the Gaussian noise which is added to each prediction."""

    LEVEL_OF_SUPERIMPOSED_NOISE: "KISAO"
    """level of superimposed noise: Standard deviation of the Gaussian noise which is added to each prediction."""

    KISAO_0000573: "KISAO"
    """probabilistic logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. Probabilistic networks allow for specifying more than one transition function per variable/gene. Each of these functions has a probability to be chosen, where the probabilities of all functions for one variable sum up to 1. Transitions are performed synchronously by choosing one transition function for each gene according to their probabilities and applying them to the current state."""

    PROBABILISTIC_LOGICAL_MODEL_SIMULATION_METHOD: "KISAO"
    """probabilistic logical model simulation method: Qualitative (logical) models specify the evolution rules of their components. Probabilistic networks allow for specifying more than one transition function per variable/gene. Each of these functions has a probability to be chosen, where the probabilities of all functions for one variable sum up to 1. Transitions are performed synchronously by choosing one transition function for each gene according to their probabilities and applying them to the current state."""

    KISAO_0000574: "KISAO"
    """species transition probabilities: Probability of each species to be chosen for the next state transition."""

    SPECIES_TRANSITION_PROBABILITIES: "KISAO"
    """species transition probabilities: Probability of each species to be chosen for the next state transition."""

    KISAO_0000575: "KISAO"
    """hybrid tau-leaping method: A continuously coupled hybrid deterministic/stochastic simulation algorithm for biochemical networks. Biochemical species are classified as continuous, discrete, or switch. Tau-leaping is used to simulate stochastic species, and LSODA or another ODE integration method is used to simulate continuous species. Switch species are dynamically classified as either continuous or discrete at each timestep depending on a user defined error tolerance."""

    HYBRID_TAU_LEAPING_METHOD: "KISAO"
    """hybrid tau-leaping method: A continuously coupled hybrid deterministic/stochastic simulation algorithm for biochemical networks. Biochemical species are classified as continuous, discrete, or switch. Tau-leaping is used to simulate stochastic species, and LSODA or another ODE integration method is used to simulate continuous species. Switch species are dynamically classified as either continuous or discrete at each timestep depending on a user defined error tolerance."""

    KISAO_0000576: "KISAO"
    """quadratic MOMA: Minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. MOMA employs quadratic programming to identify the closest point (in terms of its Euclidean distance) in the permissible flux space of the knockout to the wild-type flux vector by solving the optimization problem Min sum((fluxAi - fluxBi)^2) + sum(fluxAi)^(fluxMinimizationWeight) + sum(fluxBi)^(fluxMinimizationWeight)"""

    QUADRATIC_MOMA: "KISAO"
    """quadratic MOMA: Minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. MOMA employs quadratic programming to identify the closest point (in terms of its Euclidean distance) in the permissible flux space of the knockout to the wild-type flux vector by solving the optimization problem Min sum((fluxAi - fluxBi)^2) + sum(fluxAi)^(fluxMinimizationWeight) + sum(fluxBi)^(fluxMinimizationWeight)"""

    KISAO_0000577: "KISAO"
    """flux minimization weight: The degree to which minimization of the sum of fluxes should be taken into account in Minimization of Metabolic Adjustment (MOMA) which solvers the optimization problem Min sum((fluxAi - fluxBi)^2) + sum(fluxAi)^(fluxMinimizationWeight) + sum(fluxBi)^(fluxMinimizationWeight)"""

    FLUX_MINIMIZATION_WEIGHT: "KISAO"
    """flux minimization weight: The degree to which minimization of the sum of fluxes should be taken into account in Minimization of Metabolic Adjustment (MOMA) which solvers the optimization problem Min sum((fluxAi - fluxBi)^2) + sum(fluxAi)^(fluxMinimizationWeight) + sum(fluxBi)^(fluxMinimizationWeight)"""

    KISAO_0000578: "KISAO"
    """nested algorithm: A nested algorithm of an algorithm"""

    NESTED_ALGORITHM: "KISAO"
    """nested algorithm: A nested algorithm of an algorithm"""

    KISAO_0000579: "KISAO"
    """linear MOMA: Linear minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. Linear MOMA employs linear programming to identify the closest point (in terms of its L1 norm) in the permissible flux space of the knockout to the wild-type flux vector by solving the optimization problem Min sum(|fluxAi - fluxBi|)"""

    LINEAR_MOMA: "KISAO"
    """linear MOMA: Linear minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. Linear MOMA employs linear programming to identify the closest point (in terms of its L1 norm) in the permissible flux space of the knockout to the wild-type flux vector by solving the optimization problem Min sum(|fluxAi - fluxBi|)"""

    KISAO_0000580: "KISAO"
    """ROOM: Constraint-based algorithm for predicting the metabolic steady state after gene knockouts which aims to minimize the number of significant flux changes (hence on/off) with respect to the wild type."""

    ROOM: "KISAO"
    """ROOM: Constraint-based algorithm for predicting the metabolic steady state after gene knockouts which aims to minimize the number of significant flux changes (hence on/off) with respect to the wild type."""

    KISAO_0000581: "KISAO"
    """BKMC: The Boolean kinetic Monte Carlo method (BKMC) is a natural generalization of the asynchronous Boolean simulation method, with a direct probabilistic interpretation. In the BKMC framework, the dynamics is parameterized by a biological time and the order of update is noisy, which is less strict than priority classes introduced in GINsin. A BKMC model is specified by logical rules as in regular Boolean models but with a more precise information: a numerical rate is added for each transition of each node."""

    BKMC: "KISAO"
    """BKMC: The Boolean kinetic Monte Carlo method (BKMC) is a natural generalization of the asynchronous Boolean simulation method, with a direct probabilistic interpretation. In the BKMC framework, the dynamics is parameterized by a biological time and the order of update is noisy, which is less strict than priority classes introduced in GINsin. A BKMC model is specified by logical rules as in regular Boolean models but with a more precise information: a numerical rate is added for each transition of each node."""

    KISAO_0000582: "KISAO"
    """Spatiocyte method: Lattice-based stochastic particle simulation method for biochemical reaction and diffusion processes."""

    SPATIOCYTE_METHOD: "KISAO"
    """Spatiocyte method: Lattice-based stochastic particle simulation method for biochemical reaction and diffusion processes."""

    KISAO_0000583: "KISAO"
    """minimum order: Minimum order of method."""

    MINIMUM_ORDER: "KISAO"
    """minimum order: Minimum order of method."""

    KISAO_0000584: "KISAO"
    """initial order: Initial order of method."""

    INITIAL_ORDER: "KISAO"
    """initial order: Initial order of method."""

    KISAO_0000585: "KISAO"
    """TOMS731: Moving-grid interface for systems of one-dimensional time-dependent partial differential equations."""

    TOMS731: "KISAO"
    """TOMS731: Moving-grid interface for systems of one-dimensional time-dependent partial differential equations."""

    KISAO_0000586: "KISAO"
    """Gibson-Bruck next reaction algorithm with indexed priority queue."""

    GIBSON_BRUCK_NEXT_REACTION_ALGORITHM_WITH_INDEXED_PRIORITY_QUEUE: "KISAO"
    """Gibson-Bruck next reaction algorithm with indexed priority queue."""

    KISAO_0000587: "KISAO"
    """IMEX: Method for solving stiff and imaginary ODE problems"""

    IMEX: "KISAO"
    """IMEX: Method for solving stiff and imaginary ODE problems"""

    KISAO_0000588: "KISAO"
    """flux sampling: Method for sampling fluxes from the null space of a flux balance analysis model"""

    FLUX_SAMPLING: "KISAO"
    """flux sampling: Method for sampling fluxes from the null space of a flux balance analysis model"""

    KISAO_0000589: "KISAO"
    """ACB flux sampling method."""

    ACB_FLUX_SAMPLING_METHOD: "KISAO"
    """ACB flux sampling method."""

    KISAO_0000590: "KISAO"
    """ACHR flux sampling method."""

    ACHR_FLUX_SAMPLING_METHOD: "KISAO"
    """ACHR flux sampling method."""

    KISAO_0000591: "KISAO"
    """mdFBA."""

    MDFBA: "KISAO"
    """mdFBA."""

    KISAO_0000592: "KISAO"
    """dynamic rFBA: Method for predicting the dynamics of metabolic fluxes under patterns of the regulation of gene expression"""

    DYNAMIC_RFBA: "KISAO"
    """dynamic rFBA: Method for predicting the dynamics of metabolic fluxes under patterns of the regulation of gene expression"""

    KISAO_0000593: "KISAO"
    """MOMA: minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. MOMA identifies the closest point in the permissible flux space of the knockout to the wild-type flux vector by solving an optimization problem."""

    MOMA: "KISAO"
    """MOMA: minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. MOMA identifies the closest point in the permissible flux space of the knockout to the wild-type flux vector by solving an optimization problem."""

    KISAO_0000594: "KISAO"
    """order: Order of method"""

    ORDER: "KISAO"
    """order: Order of method"""

    KISAO_0000595: "KISAO"
    """rFBA: Method for predicting metabolic fluxes under patterns of the regulation of gene expression"""

    RFBA: "KISAO"
    """rFBA: Method for predicting metabolic fluxes under patterns of the regulation of gene expression"""

    KISAO_0000596: "KISAO"
    """srFBA: Method for predicting steady-state metabolic fluxes under patterns of the regulation of gene expression"""

    SRFBA: "KISAO"
    """srFBA: Method for predicting steady-state metabolic fluxes under patterns of the regulation of gene expression"""

    KISAO_0000597: "KISAO"
    """tolerance: Numeric value specifying the desired tolerance the user wants to achieve. A smaller value means that the prediction is calculated more accurately."""

    TOLERANCE: "KISAO"
    """tolerance: Numeric value specifying the desired tolerance the user wants to achieve. A smaller value means that the prediction is calculated more accurately."""

    KISAO_0000598: "KISAO"
    """hybrid Gibson - Milstein method: A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE."""

    HYBRID_GIBSON___MILSTEIN_METHOD: "KISAO"
    """hybrid Gibson - Milstein method: A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE."""

    KISAO_0000599: "KISAO"
    """hybrid Gibson - Euler-Maruyama method: A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE."""

    HYBRID_GIBSON___EULER_MARUYAMA_METHOD: "KISAO"
    """hybrid Gibson - Euler-Maruyama method: A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE."""

    KISAO_0000600: "KISAO"
    """hybrid adaptive Gibson - Milstein method: A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE."""

    HYBRID_ADAPTIVE_GIBSON___MILSTEIN_METHOD: "KISAO"
    """hybrid adaptive Gibson - Milstein method: A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE."""

    KISAO_0000601: "KISAO"
    """number of trials: Number of multiple trials (e.g., of a scatter search method)."""

    NUMBER_OF_TRIALS: "KISAO"
    """number of trials: Number of multiple trials (e.g., of a scatter search method)."""

    KISAO_0000602: "KISAO"
    """minimum species threshold for continuous approximation: Minimum number of molecules of both reactant and product species required for approximation as a continuous Markov process."""

    MINIMUM_SPECIES_THRESHOLD_FOR_CONTINUOUS_APPROXIMATION: "KISAO"
    """minimum species threshold for continuous approximation: Minimum number of molecules of both reactant and product species required for approximation as a continuous Markov process."""

    KISAO_0000603: "KISAO"
    """minimum reaction rate for continuous approximation: Minimum reaction rate required for approximation as a continuous Markov process."""

    MINIMUM_REACTION_RATE_FOR_CONTINUOUS_APPROXIMATION: "KISAO"
    """minimum reaction rate for continuous approximation: Minimum reaction rate required for approximation as a continuous Markov process."""

    KISAO_0000604: "KISAO"
    """MSR tolerance: Maximum allowed effect of executing multiple slow reactions per numerical integration of the SDEs."""

    MSR_TOLERANCE: "KISAO"
    """MSR tolerance: Maximum allowed effect of executing multiple slow reactions per numerical integration of the SDEs."""

    KISAO_0000605: "KISAO"
    """SDE tolerance: Stochastic differential equation tolerance"""

    SDE_TOLERANCE: "KISAO"
    """SDE tolerance: Stochastic differential equation tolerance"""

    KISAO_0000606: "KISAO"
    """hierarchical stochastic simulation algorithm: Fast, memory-efficient method for stochastic simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions."""

    HIERARCHICAL_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """hierarchical stochastic simulation algorithm: Fast, memory-efficient method for stochastic simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions."""

    KISAO_0000607: "KISAO"
    """hierarchical Fehlberg method: Method for continuous simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions."""

    HIERARCHICAL_FEHLBERG_METHOD: "KISAO"
    """hierarchical Fehlberg method: Method for continuous simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions."""

    KISAO_0000608: "KISAO"
    """hierarchical flux balance analysis: Method for constraint-based simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions."""

    HIERARCHICAL_FLUX_BALANCE_ANALYSIS: "KISAO"
    """hierarchical flux balance analysis: Method for constraint-based simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions."""

    KISAO_0000609: "KISAO"
    """embedded Runge-Kutta Prince-Dormand (8,9) method: An embedded Runge-Kutta integrator of order 8(9)."""

    EMBEDDED_RUNGE_KUTTA_PRINCE_DORMAND__8_9__METHOD: "KISAO"
    """embedded Runge-Kutta Prince-Dormand (8,9) method: An embedded Runge-Kutta integrator of order 8(9)."""

    KISAO_0000610: "KISAO"
    """composite-rejection stochastic simulation algorithm."""

    COMPOSITE_REJECTION_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """composite-rejection stochastic simulation algorithm."""

    KISAO_0000611: "KISAO"
    """incremental stochastic simulation algorithm: Performs local averaging over small time-intervals to compute statistics on typical behavior."""

    INCREMENTAL_STOCHASTIC_SIMULATION_ALGORITHM: "KISAO"
    """incremental stochastic simulation algorithm: Performs local averaging over small time-intervals to compute statistics on typical behavior."""

    KISAO_0000612: "KISAO"
    """implicit 4th order Runge-Kutta method at Gaussian points."""

    IMPLICIT_4TH_ORDER_RUNGE_KUTTA_METHOD_AT_GAUSSIAN_POINTS: "KISAO"
    """implicit 4th order Runge-Kutta method at Gaussian points."""

    KISAO_0000613: "KISAO"
    """stochastic simulation algorithm with normally-distributed next reaction times."""

    STOCHASTIC_SIMULATION_ALGORITHM_WITH_NORMALLY_DISTRIBUTED_NEXT_REACTION_TIMES: (
        "KISAO"
    )
    """stochastic simulation algorithm with normally-distributed next reaction times."""

    KISAO_0000614: "KISAO"
    """implementation: An implementation of an algorithm. For example, simulation tools can this parameter to differentiate among C, Python, and Java implementations of the same algorithms and allow investigators to select one of these specific implementations through SED-ML."""

    IMPLEMENTATION: "KISAO"
    """implementation: An implementation of an algorithm. For example, simulation tools can this parameter to differentiate among C, Python, and Java implementations of the same algorithms and allow investigators to select one of these specific implementations through SED-ML."""

    KISAO_0000615: "KISAO"
    """fully-implicit regular grid finite volume method with a variable time step."""

    FULLY_IMPLICIT_REGULAR_GRID_FINITE_VOLUME_METHOD_WITH_A_VARIABLE_TIME_STEP: "KISAO"
    """fully-implicit regular grid finite volume method with a variable time step."""

    KISAO_0000616: "KISAO"
    """semi-implicit regular grid finite volume method with a fixed time step."""

    SEMI_IMPLICIT_REGULAR_GRID_FINITE_VOLUME_METHOD_WITH_A_FIXED_TIME_STEP: "KISAO"
    """semi-implicit regular grid finite volume method with a fixed time step."""

    KISAO_0000617: "KISAO"
    """IDA-CVODE hybrid method: Meta algorithm which chooses between IDA and CVODE depending on the problem to be solved. CVODE is used for ordinary differential equation (ODE) systems. IDA is used for differential-algebraic equation (DAE) systems."""

    IDA_CVODE_HYBRID_METHOD: "KISAO"
    """IDA-CVODE hybrid method: Meta algorithm which chooses between IDA and CVODE depending on the problem to be solved. CVODE is used for ordinary differential equation (ODE) systems. IDA is used for differential-algebraic equation (DAE) systems."""

    KISAO_0000618: "KISAO"
    """bunker: A variant of the stochastic simulation algorithm (SSA) in which the time to the next reaction is equated to the mean inter-event time (inverse of the sum of the propensitites of the reactions) rather than sampled from a distribution parameterized by this mean inter-event time. In this method, the next reaction time is deterministic rather than stochastic as in SSA."""

    BUNKER: "KISAO"
    """bunker: A variant of the stochastic simulation algorithm (SSA) in which the time to the next reaction is equated to the mean inter-event time (inverse of the sum of the propensitites of the reactions) rather than sampled from a distribution parameterized by this mean inter-event time. In this method, the next reaction time is deterministic rather than stochastic as in SSA."""

    KISAO_0000619: "KISAO"
    """emc-sim: A variant of the stochastic simulation algorithm (SSA) in which the time to the next reaction is a constant equal to 1 time unit. In this method, the next reaction time is deterministic rather than stochastic as in SSA."""

    EMC_SIM: "KISAO"
    """emc-sim: A variant of the stochastic simulation algorithm (SSA) in which the time to the next reaction is a constant equal to 1 time unit. In this method, the next reaction time is deterministic rather than stochastic as in SSA."""

    KISAO_0000620: "KISAO"
    """parsimonius flux balance analysis: A technique for selecting a flux distribution which is parsimonious by some metric, such as a solution which has the minimal number of active fluxes or a solution which has the smallest sum of active fluxes."""

    PARSIMONIUS_FLUX_BALANCE_ANALYSIS: "KISAO"
    """parsimonius flux balance analysis: A technique for selecting a flux distribution which is parsimonious by some metric, such as a solution which has the minimal number of active fluxes or a solution which has the smallest sum of active fluxes."""

    KISAO_0000621: "KISAO"
    """stochastic simulation leaping method."""

    STOCHASTIC_SIMULATION_LEAPING_METHOD: "KISAO"
    """stochastic simulation leaping method."""

    KISAO_0000622: "KISAO"
    """flux balance method."""

    FLUX_BALANCE_METHOD: "KISAO"
    """flux balance method."""

    KISAO_0000623: "KISAO"
    """flux balance problem."""

    FLUX_BALANCE_PROBLEM: "KISAO"
    """flux balance problem."""

    KISAO_0000624: "KISAO"
    """method for solving a system of linear equations: method for solving a system of linear equations Example system of equations: 3x + 2y - z = 0 2x - 2y + 4z = 0 -x + 1/2y - z = 0"""

    METHOD_FOR_SOLVING_A_SYSTEM_OF_LINEAR_EQUATIONS: "KISAO"
    """method for solving a system of linear equations: method for solving a system of linear equations Example system of equations: 3x + 2y - z = 0 2x - 2y + 4z = 0 -x + 1/2y - z = 0"""

    KISAO_0000625: "KISAO"
    """dense direct solver."""

    DENSE_DIRECT_SOLVER: "KISAO"
    """dense direct solver."""

    KISAO_0000626: "KISAO"
    """band direct solver."""

    BAND_DIRECT_SOLVER: "KISAO"
    """band direct solver."""

    KISAO_0000627: "KISAO"
    """diagonal approximate Jacobian solver."""

    DIAGONAL_APPROXIMATE_JACOBIAN_SOLVER: "KISAO"
    """diagonal approximate Jacobian solver."""

    KISAO_0000628: "KISAO"
    """modelling and simulation algorithm parameter value: A value of a parameter of an algorithm"""

    MODELLING_AND_SIMULATION_ALGORITHM_PARAMETER_VALUE: "KISAO"
    """modelling and simulation algorithm parameter value: A value of a parameter of an algorithm"""

    KISAO_0000629: "KISAO"
    """null."""

    NULL: "KISAO"
    """null."""

    KISAO_0000630: "KISAO"
    """general steady state method: A method looking for a steady state of a dynamic system."""

    GENERAL_STEADY_STATE_METHOD: "KISAO"
    """general steady state method: A method looking for a steady state of a dynamic system."""

    KISAO_0000631: "KISAO"
    """iterative root-finding method: Iterative method for finding the root of a function (f(x) = 0)."""

    ITERATIVE_ROOT_FINDING_METHOD: "KISAO"
    """iterative root-finding method: Iterative method for finding the root of a function (f(x) = 0)."""

    KISAO_0000632: "KISAO"
    """functional iteration root-finding method: Iterative method for finding the root of a function f(x) given by y^{n(m+1)} = h_{n} β_{n,0} f(t_{n}, y^{n(m)}) + a_n This method only involves evaluations of f. This method is suitable for non-stiff functions."""

    FUNCTIONAL_ITERATION_ROOT_FINDING_METHOD: "KISAO"
    """functional iteration root-finding method: Iterative method for finding the root of a function f(x) given by y^{n(m+1)} = h_{n} β_{n,0} f(t_{n}, y^{n(m)}) + a_n This method only involves evaluations of f. This method is suitable for non-stiff functions."""

    KISAO_0000633: "KISAO"
    """computational function: A mathematical function such as the calculation of a minimum, maximum, or mean of a set of values."""

    COMPUTATIONAL_FUNCTION: "KISAO"
    """computational function: A mathematical function such as the calculation of a minimum, maximum, or mean of a set of values."""

    KISAO_0000634: "KISAO"
    """scaled property."""

    SCALED_PROPERTY: "KISAO"
    """scaled property."""

    KISAO_0000635: "KISAO"
    """unscaled property."""

    UNSCALED_PROPERTY: "KISAO"
    """unscaled property."""

    KISAO_0000636: "KISAO"
    """primary property: A primary output of a simulation."""

    PRIMARY_PROPERTY: "KISAO"
    """primary property: A primary output of a simulation."""

    KISAO_0000637: "KISAO"
    """derived property: An output of a simulation which can be derived from its primary outputs."""

    DERIVED_PROPERTY: "KISAO"
    """derived property: An output of a simulation which can be derived from its primary outputs."""

    KISAO_0000638: "KISAO"
    """level: A level such as of a qualitative variable."""

    LEVEL: "KISAO"
    """level: A level such as of a qualitative variable."""

    KISAO_0000639: "KISAO"
    """flux: A rate through an volume such as of a reaction of a constraint-based models."""

    FLUX: "KISAO"
    """flux: A rate through an volume such as of a reaction of a constraint-based models."""

    KISAO_0000640: "KISAO"
    """lower bound: A lower bound on an estimate of a quantity."""

    LOWER_BOUND: "KISAO"
    """lower bound: A lower bound on an estimate of a quantity."""

    KISAO_0000641: "KISAO"
    """bound: An upper or lower bound on an estimate of a quantity."""

    BOUND: "KISAO"
    """bound: An upper or lower bound on an estimate of a quantity."""

    KISAO_0000642: "KISAO"
    """minimum flux: Minimum possible flux such as computed by flux variability analysis (FVA, KISAO_0000526)."""

    MINIMUM_FLUX: "KISAO"
    """minimum flux: Minimum possible flux such as computed by flux variability analysis (FVA, KISAO_0000526)."""

    KISAO_0000643: "KISAO"
    """upper bound: An upper bound on an estimate of a quantity."""

    UPPER_BOUND: "KISAO"
    """upper bound: An upper bound on an estimate of a quantity."""

    KISAO_0000644: "KISAO"
    """maximum flux: Maximum possible flux such as computed by flux variability analysis (FVA, KISAO_0000526)."""

    MAXIMUM_FLUX: "KISAO"
    """maximum flux: Maximum possible flux such as computed by flux variability analysis (FVA, KISAO_0000526)."""

    KISAO_0000645: "KISAO"
    """objective value: Value of an objective function such as of a constraint-based model."""

    OBJECTIVE_VALUE: "KISAO"
    """objective value: Value of an objective function such as of a constraint-based model."""

    KISAO_0000646: "KISAO"
    """propensity: Tendency of an event such as of the firing of a reaction in the stochastic simulation algorithm (SSA, KISAO_0000029)."""

    PROPENSITY: "KISAO"
    """propensity: Tendency of an event such as of the firing of a reaction in the stochastic simulation algorithm (SSA, KISAO_0000029)."""

    KISAO_0000647: "KISAO"
    """derivative: Rate of change of a variable with respect to another variable."""

    DERIVATIVE: "KISAO"
    """derivative: Rate of change of a variable with respect to another variable."""

    KISAO_0000648: "KISAO"
    """step: Iteration such as along a pseudo timecourse of a logical simulation."""

    STEP: "KISAO"
    """step: Iteration such as along a pseudo timecourse of a logical simulation."""

    KISAO_0000649: "KISAO"
    """shadow price: Change, per infinitesimal unit of the constraint, in the optimal value of the objective function of an optimization problem obtained by relaxing the constraint."""

    SHADOW_PRICE: "KISAO"
    """shadow price: Change, per infinitesimal unit of the constraint, in the optimal value of the objective function of an optimization problem obtained by relaxing the constraint."""

    KISAO_0000650: "KISAO"
    """sensitivity: The sensitivity of a variable to another variable, such as the derivative a variable with respect to another."""

    SENSITIVITY: "KISAO"
    """sensitivity: The sensitivity of a variable to another variable, such as the derivative a variable with respect to another."""

    KISAO_0000651: "KISAO"
    """reduced costs: The amount by which an objective function coefficient would have to improve before it would be possible for a corresponding variable to assume a positive value in the optimal solution."""

    REDUCED_COSTS: "KISAO"
    """reduced costs: The amount by which an objective function coefficient would have to improve before it would be possible for a corresponding variable to assume a positive value in the optimal solution."""

    KISAO_0000652: "KISAO"
    """concentration rate: Rate of a process relative to a volume, such as the rate of a reaction in molar^-1 s^-1."""

    CONCENTRATION_RATE: "KISAO"
    """concentration rate: Rate of a process relative to a volume, such as the rate of a reaction in molar^-1 s^-1."""

    KISAO_0000653: "KISAO"
    """particle number rate: Rate of a process in extensive/absolute units such as mole reactions per second."""

    PARTICLE_NUMBER_RATE: "KISAO"
    """particle number rate: Rate of a process in extensive/absolute units such as mole reactions per second."""

    KISAO_0000654: "KISAO"
    """amount rate: rate of a process in extensive/absolute units such as reactions per second."""

    AMOUNT_RATE: "KISAO"
    """amount rate: rate of a process in extensive/absolute units such as reactions per second."""

    KISAO_0000655: "KISAO"
    """rate: Speed at which a process is occuring such as the temporal rate of a chemical reaction,"""

    RATE: "KISAO"
    """rate: Speed at which a process is occuring such as the temporal rate of a chemical reaction,"""

    KISAO_0000656: "KISAO"
    """use adaptive time steps: Whether an algorithm should use adaptive or fixed time steps."""

    USE_ADAPTIVE_TIME_STEPS: "KISAO"
    """use adaptive time steps: Whether an algorithm should use adaptive or fixed time steps."""

    KISAO_0000657: "KISAO"
    """sequential logical simulation method: Qualitative (logical) models specify the evolution rules of their components. In the case of a sequential updating, nodes are updated sequentially in a pre-determined deterministic order."""

    SEQUENTIAL_LOGICAL_SIMULATION_METHOD: "KISAO"
    """sequential logical simulation method: Qualitative (logical) models specify the evolution rules of their components. In the case of a sequential updating, nodes are updated sequentially in a pre-determined deterministic order."""

    KISAO_0000658: "KISAO"
    """logical model analysis method: A method for analyzing a logical model, such as finding its fixed points."""

    LOGICAL_MODEL_ANALYSIS_METHOD: "KISAO"
    """logical model analysis method: A method for analyzing a logical model, such as finding its fixed points."""

    KISAO_0000659: "KISAO"
    """Naldi MDD logical model stable state search method: Efficient method for determining the stable states of a regulatory graph using a Multi-valued Decision Diagram (MDD) representation of the logical functions."""

    NALDI_MDD_LOGICAL_MODEL_STABLE_STATE_SEARCH_METHOD: "KISAO"
    """Naldi MDD logical model stable state search method: Efficient method for determining the stable states of a regulatory graph using a Multi-valued Decision Diagram (MDD) representation of the logical functions."""

    KISAO_0000660: "KISAO"
    """logical model stable state search method: Method for determining the stable states of a regulatory graph."""

    LOGICAL_MODEL_STABLE_STATE_SEARCH_METHOD: "KISAO"
    """logical model stable state search method: Method for determining the stable states of a regulatory graph."""

    KISAO_0000661: "KISAO"
    """logical model trap space identification method: Method for determining the trap spaces, or stable motifs or symbolic stable states, of a regulatory graph,"""

    LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD: "KISAO"
    """logical model trap space identification method: Method for determining the trap spaces, or stable motifs or symbolic stable states, of a regulatory graph,"""

    KISAO_0000662: "KISAO"
    """Klarner ASP logical model trap space identification method: Optimization-based method rooted in answer set programming (ASP) for computing the trap spaces of a regulatory graph."""

    KLARNER_ASP_LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD: "KISAO"
    """Klarner ASP logical model trap space identification method: Optimization-based method rooted in answer set programming (ASP) for computing the trap spaces of a regulatory graph."""

    KISAO_0000663: "KISAO"
    """BDD logical model trap space identification method: Method for determining the trap spaces of a regulatory graph using a Binary Decision Diagram (BDD)."""

    BDD_LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD: "KISAO"
    """BDD logical model trap space identification method: Method for determining the trap spaces of a regulatory graph using a Binary Decision Diagram (BDD)."""

    KISAO_0000664: "KISAO"
    """Second order backward implicit product Euler scheme."""

    SECOND_ORDER_BACKWARD_IMPLICIT_PRODUCT_EULER_SCHEME: "KISAO"
    """Second order backward implicit product Euler scheme."""

    KISAO_0000665: "KISAO"
    """maximum number of iterations for root finding."""

    MAXIMUM_NUMBER_OF_ITERATIONS_FOR_ROOT_FINDING: "KISAO"
    """maximum number of iterations for root finding."""

    KISAO_0000666: "KISAO"
    """Jacobian epsilon."""

    JACOBIAN_EPSILON: "KISAO"
    """Jacobian epsilon."""

    KISAO_0000667: "KISAO"
    """memory size: Maximum number of points to store in memory, such as in the second order backward implicit product Euler scheme."""

    MEMORY_SIZE: "KISAO"
    """memory size: Maximum number of points to store in memory, such as in the second order backward implicit product Euler scheme."""

    KISAO_0000668: "KISAO"
    """Numerical Recipes in C 'stiff' Rosenbrock method."""

    NUMERICAL_RECIPES_IN_C__STIFF__ROSENBROCK_METHOD: "KISAO"
    """Numerical Recipes in C 'stiff' Rosenbrock method."""

    KISAO_0000669: "KISAO"
    """Resource Balance Analysis."""

    RESOURCE_BALANCE_ANALYSIS: "KISAO"
    """Resource Balance Analysis."""

    KISAO_0000670: "KISAO"
    """use multiple steps: Whether to perform a multiple time step simulation."""

    USE_MULTIPLE_STEPS: "KISAO"
    """use multiple steps: Whether to perform a multiple time step simulation."""

    KISAO_0000671: "KISAO"
    """use stiff method: Specifies whether the integrator attempts to solve stiff equations."""

    USE_STIFF_METHOD: "KISAO"
    """use stiff method: Specifies whether the integrator attempts to solve stiff equations."""

    KISAO_0000672: "KISAO"
    """Numerical Recipes in C 'quality-controlled Runge-Kutta' method: Cash-Karp method with step size adjustment."""

    NUMERICAL_RECIPES_IN_C__QUALITY_CONTROLLED_RUNGE_KUTTA__METHOD: "KISAO"
    """Numerical Recipes in C 'quality-controlled Runge-Kutta' method: Cash-Karp method with step size adjustment."""

    KISAO_0000673: "KISAO"
    """skip reactions that produce negative species amounts: Parameter which instructs a simulation tool to skip reactions that would result in negative amounts of species."""

    SKIP_REACTIONS_THAT_PRODUCE_NEGATIVE_SPECIES_AMOUNTS: "KISAO"
    """skip reactions that produce negative species amounts: Parameter which instructs a simulation tool to skip reactions that would result in negative amounts of species."""

    KISAO_0000674: "KISAO"
    """presimulate: Whether a model should be presimulated prior to analysis."""

    PRESIMULATE: "KISAO"
    """presimulate: Whether a model should be presimulated prior to analysis."""

    KISAO_0000675: "KISAO"
    """Broyden method: Family of Quasi-Newton methods for finding roots in k variables originally described by C. G. Broyden in 1965."""

    BROYDEN_METHOD: "KISAO"
    """Broyden method: Family of Quasi-Newton methods for finding roots in k variables originally described by C. G. Broyden in 1965."""

    KISAO_0000676: "KISAO"
    """degree of linearity: The degree of linearity of a system."""

    DEGREE_OF_LINEARITY: "KISAO"
    """degree of linearity: The degree of linearity of a system."""

    KISAO_0000677: "KISAO"
    """maximum number of steps for presimulation: Maximum number of steps to take in presimulating a model prior to analysis."""

    MAXIMUM_NUMBER_OF_STEPS_FOR_PRESIMULATION: "KISAO"
    """maximum number of steps for presimulation: Maximum number of steps to take in presimulating a model prior to analysis."""

    KISAO_0000678: "KISAO"
    """maximum number of steps for approximation: Maximum number of steps to take in approximating an analysis."""

    MAXIMUM_NUMBER_OF_STEPS_FOR_APPROXIMATION: "KISAO"
    """maximum number of steps for approximation: Maximum number of steps to take in approximating an analysis."""

    KISAO_0000679: "KISAO"
    """maximum time for approximation: Maximum amount of time to spend approximating an analysis."""

    MAXIMUM_TIME_FOR_APPROXIMATION: "KISAO"
    """maximum time for approximation: Maximum amount of time to spend approximating an analysis."""

    KISAO_0000680: "KISAO"
    """duration: Length of time to simulate."""

    DURATION: "KISAO"
    """duration: Length of time to simulate."""

    KISAO_0000681: "KISAO"
    """maximum time: Maximum amount of wall time for an operation."""

    MAXIMUM_TIME: "KISAO"
    """maximum time: Maximum amount of wall time for an operation."""

    KISAO_0000682: "KISAO"
    """allow approximation: Whether to find an approximate solution if an exact solution could not be found."""

    ALLOW_APPROXIMATION: "KISAO"
    """allow approximation: Whether to find an approximate solution if an exact solution could not be found."""

    KISAO_0000683: "KISAO"
    """relative tolerance for approximation: Relatative tolerance for an alternative approximate solution to an exact solution which could not be found."""

    RELATIVE_TOLERANCE_FOR_APPROXIMATION: "KISAO"
    """relative tolerance for approximation: Relatative tolerance for an alternative approximate solution to an exact solution which could not be found."""

    KISAO_0000684: "KISAO"
    """number of steps per output: Number of simulation steps between each simulation output."""

    NUMBER_OF_STEPS_PER_OUTPUT: "KISAO"
    """number of steps per output: Number of simulation steps between each simulation output."""

    KISAO_0000685: "KISAO"
    """biological state optimization method: A method for computing the optimal state of a biological system according to a particular objective."""

    BIOLOGICAL_STATE_OPTIMIZATION_METHOD: "KISAO"
    """biological state optimization method: A method for computing the optimal state of a biological system according to a particular objective."""

    KISAO_0000686: "KISAO"
    """Enzyme Cost Minimization: For a given metabolic network model, the Enzyme Cost Minimization method determines plausible metabolite and enzyme concentrations (which determine thermodynamic forces and enzyme catalytic rates). Fluxes, enzyme kinetic constants, admissible metabolite concentration ranges, and enzyme cost weights (e.g. enzyme molecular masses) are given as input data. The method applies the principle that high enzyme (or enzyme plus metabolite) concentrations must be avoided, and maximizes a weighted sum of enzyme and metabolite concentrations."""

    ENZYME_COST_MINIMIZATION: "KISAO"
    """Enzyme Cost Minimization: For a given metabolic network model, the Enzyme Cost Minimization method determines plausible metabolite and enzyme concentrations (which determine thermodynamic forces and enzyme catalytic rates). Fluxes, enzyme kinetic constants, admissible metabolite concentration ranges, and enzyme cost weights (e.g. enzyme molecular masses) are given as input data. The method applies the principle that high enzyme (or enzyme plus metabolite) concentrations must be avoided, and maximizes a weighted sum of enzyme and metabolite concentrations."""

    KISAO_0000687: "KISAO"
    """Max-min Driving Force method: For a given metabolic network model, the MDF method determines plausible metabolite concentrations and thermodynamic forces. Flux directions, equilibrium constants (or equivalently, standard Gibbs free energies of reactions) and admissible metabolite concentration ranges are given as input data. The method applies the principle that low thermodynamic forces must be avoided, and maximizes the minimum thermodynamic force across the entire network."""

    MAX_MIN_DRIVING_FORCE_METHOD: "KISAO"
    """Max-min Driving Force method: For a given metabolic network model, the MDF method determines plausible metabolite concentrations and thermodynamic forces. Flux directions, equilibrium constants (or equivalently, standard Gibbs free energies of reactions) and admissible metabolite concentration ranges are given as input data. The method applies the principle that low thermodynamic forces must be avoided, and maximizes the minimum thermodynamic force across the entire network."""

    KISAO_0000688: "KISAO"
    """type of system described."""

    TYPE_OF_SYSTEM_DESCRIBED: "KISAO"
    """type of system described."""

    KISAO_0000689: "KISAO"
    """mathematical system."""

    MATHEMATICAL_SYSTEM: "KISAO"
    """mathematical system."""

    KISAO_0000690: "KISAO"
    """biological system."""

    BIOLOGICAL_SYSTEM: "KISAO"
    """biological system."""

    KISAO_0000691: "KISAO"
    """metabolic system."""

    METABOLIC_SYSTEM: "KISAO"
    """metabolic system."""

    KISAO_0000692: "KISAO"
    """cellular system."""

    CELLULAR_SYSTEM: "KISAO"
    """cellular system."""

    KISAO_0000693: "KISAO"
    """biochemical system."""

    BIOCHEMICAL_SYSTEM: "KISAO"
    """biochemical system."""

    KISAO_0000694: "KISAO"
    """ODE solver: An ODE solver is the general category of packages such as CVODE-like methods [http://identifiers.org/biomodels.kisao/KISAO_0000433] or Livermore solvers [http://identifiers.org/biomodels.kisao/KISAO_0000094] that solve systems of ordinary differential equations."""

    ODE_SOLVER: "KISAO"
    """ODE solver: An ODE solver is the general category of packages such as CVODE-like methods [http://identifiers.org/biomodels.kisao/KISAO_0000433] or Livermore solvers [http://identifiers.org/biomodels.kisao/KISAO_0000094] that solve systems of ordinary differential equations."""

    KISAO_0000695: "KISAO"
    """parameters for: The children parameters of this term are applied when the parent general term is implented as the more-specific value of this term. For example: a 'parameters for' term might be used as a child of an 'ODE Solver' ([http://identifiers.org/biomodels.kisao/KISAO_0000694]), have a value of 'KISAO_0000019' (CVODE)', and have a child term 'use stiff method' of 'true' ([http://identifiers.org/biomodels.kisao/KISAO_0000671])"""

    PARAMETERS_FOR: "KISAO"
    """parameters for: The children parameters of this term are applied when the parent general term is implented as the more-specific value of this term. For example: a 'parameters for' term might be used as a child of an 'ODE Solver' ([http://identifiers.org/biomodels.kisao/KISAO_0000694]), have a value of 'KISAO_0000019' (CVODE)', and have a child term 'use stiff method' of 'true' ([http://identifiers.org/biomodels.kisao/KISAO_0000671])"""

    KISAO_0000696: "KISAO"
    """steady state root-finding problem."""

    STEADY_STATE_ROOT_FINDING_PROBLEM: "KISAO"
    """steady state root-finding problem."""

    KISAO_0000697: "KISAO"
    """SDE solver: An SDE solver is the general category of packages that provide stochastic solutions to a system of differential equations with propensities."""

    SDE_SOLVER: "KISAO"
    """SDE solver: An SDE solver is the general category of packages that provide stochastic solutions to a system of differential equations with propensities."""

    KISAO_0000698: "KISAO"
    """particle coordinates: The set of coordinates for all particles of these entities."""

    PARTICLE_COORDINATES: "KISAO"
    """particle coordinates: The set of coordinates for all particles of these entities."""

    KISAO_0000699: "KISAO"
    """DAE Solver: A DAE solver is the general category of packages such as IDA-like methods [http://identifiers.org/biomodels.kisao/KISAO_0000432] that solve systems of differential algebraic equations (DAEs). DAEs are a superset of ODEs that may additionally contain algebraic equations or 'fast' reactions."""

    DAE_SOLVER: "KISAO"
    """DAE Solver: A DAE solver is the general category of packages such as IDA-like methods [http://identifiers.org/biomodels.kisao/KISAO_0000432] that solve systems of differential algebraic equations (DAEs). DAEs are a superset of ODEs that may additionally contain algebraic equations or 'fast' reactions."""

    KISAO_0000700: "KISAO"
    """logical network: A network of logical-valued (an enumeration, such as a set of integers) variables."""

    LOGICAL_NETWORK: "KISAO"
    """logical network: A network of logical-valued (an enumeration, such as a set of integers) variables."""

    KISAO_0000701: "KISAO"
    """boolean network: A network of Boolean-valued variables."""

    BOOLEAN_NETWORK: "KISAO"
    """boolean network: A network of Boolean-valued variables."""

    KISAO_0000702: "KISAO"
    """locally-monotone Boolean network: Boolean network where each regulator is either an activator or an inhibitor, but cannot be both."""

    LOCALLY_MONOTONE_BOOLEAN_NETWORK: "KISAO"
    """locally-monotone Boolean network: Boolean network where each regulator is either an activator or an inhibitor, but cannot be both."""

    KISAO_0000703: "KISAO"
    """logical variable: A variable whose value can be one of an enumerated set of possible values such as ON/OFF, HIGH/MEDIUM/LOW, or a set integers (e.g., 0, 1, 2)."""

    LOGICAL_VARIABLE: "KISAO"
    """logical variable: A variable whose value can be one of an enumerated set of possible values such as ON/OFF, HIGH/MEDIUM/LOW, or a set integers (e.g., 0, 1, 2)."""

    KISAO_0000704: "KISAO"
    """Boolean variable: A variable whose value can be TRUE/FALSE (e.g., ON/OFF, YES/NO, 1/0)."""

    BOOLEAN_VARIABLE: "KISAO"
    """Boolean variable: A variable whose value can be TRUE/FALSE (e.g., ON/OFF, YES/NO, 1/0)."""

    KISAO_0000705: "KISAO"
    """most permissive updating policy: The most permissive updating policy captures behaviors of any compatible quantitative model."""

    MOST_PERMISSIVE_UPDATING_POLICY: "KISAO"
    """most permissive updating policy: The most permissive updating policy captures behaviors of any compatible quantitative model."""

    KISAO_0000706: "KISAO"
    """Paulevé ASP-based fixed point identification."""

    PAULEVÉ_ASP_BASED_FIXED_POINT_IDENTIFICATION: "KISAO"
    """Paulevé ASP-based fixed point identification."""

    KISAO_0000707: "KISAO"
    """Paulevé ASP-based minimal trap space identification."""

    PAULEVÉ_ASP_BASED_MINIMAL_TRAP_SPACE_IDENTIFICATION: "KISAO"
    """Paulevé ASP-based minimal trap space identification."""

    KISAO_0000708: "KISAO"
    """logical model attractor identification method."""

    LOGICAL_MODEL_ATTRACTOR_IDENTIFICATION_METHOD: "KISAO"
    """logical model attractor identification method."""

    KISAO_0000709: "KISAO"
    """Paulevé ASP-based most permissive attractor identification."""

    PAULEVÉ_ASP_BASED_MOST_PERMISSIVE_ATTRACTOR_IDENTIFICATION: "KISAO"
    """Paulevé ASP-based most permissive attractor identification."""

    KISAO_0000710: "KISAO"
    """trap space."""

    TRAP_SPACE: "KISAO"
    """trap space."""

    KISAO_0000711: "KISAO"
    """stable state."""

    STABLE_STATE: "KISAO"
    """stable state."""

    KISAO_0000712: "KISAO"
    """minimal trap space."""

    MINIMAL_TRAP_SPACE: "KISAO"
    """minimal trap space."""

    KISAO_0000713: "KISAO"
    """attractor."""

    ATTRACTOR: "KISAO"
    """attractor."""

    KISAO_0000800: "KISAO"
    """systems property: A systems-level property of an entire model or simulation."""

    SYSTEMS_PROPERTY: "KISAO"
    """systems property: A systems-level property of an entire model or simulation."""

    KISAO_0000801: "KISAO"
    """concentration control coefficient matrix (unscaled): The unscaled concentration control coefficient matrix. The dimensions are species by reactions."""

    CONCENTRATION_CONTROL_COEFFICIENT_MATRIX__UNSCALED_: "KISAO"
    """concentration control coefficient matrix (unscaled): The unscaled concentration control coefficient matrix. The dimensions are species by reactions."""

    KISAO_0000802: "KISAO"
    """control coefficient (scaled): A scaled control coefficient of any dependent element (such as a reaction or a floating species) with respect to an independent element (such as a global parameter or boundary species)."""

    CONTROL_COEFFICIENT__SCALED_: "KISAO"
    """control coefficient (scaled): A scaled control coefficient of any dependent element (such as a reaction or a floating species) with respect to an independent element (such as a global parameter or boundary species)."""

    KISAO_0000803: "KISAO"
    """control coefficient (unscaled): An unscaled control coefficient of any dependent element (such as a reaction or a floating species) with respect to an independent element (such as a global parameter or boundary species)."""

    CONTROL_COEFFICIENT__UNSCALED_: "KISAO"
    """control coefficient (unscaled): An unscaled control coefficient of any dependent element (such as a reaction or a floating species) with respect to an independent element (such as a global parameter or boundary species)."""

    KISAO_0000804: "KISAO"
    """elasticity matrix (unscaled): The unscaled elasticity matrix. The dimensions are reactions by species."""

    ELASTICITY_MATRIX__UNSCALED_: "KISAO"
    """elasticity matrix (unscaled): The unscaled elasticity matrix. The dimensions are reactions by species."""

    KISAO_0000805: "KISAO"
    """elasticity coefficient (unscaled): An unscaled elasticity coefficient of any reaction with respect to an independent element (such as a global parameter or boundary species)."""

    ELASTICITY_COEFFICIENT__UNSCALED_: "KISAO"
    """elasticity coefficient (unscaled): An unscaled elasticity coefficient of any reaction with respect to an independent element (such as a global parameter or boundary species)."""

    KISAO_0000806: "KISAO"
    """elasticity matrix (scaled): The scaled elasticity matrix. The dimensions are reactions by species."""

    ELASTICITY_MATRIX__SCALED_: "KISAO"
    """elasticity matrix (scaled): The scaled elasticity matrix. The dimensions are reactions by species."""

    KISAO_0000807: "KISAO"
    """elasticity coefficient (scaled): A scaled elasticity coefficient of any reaction with respect to an independent element (such as a global parameter or boundary species)."""

    ELASTICITY_COEFFICIENT__SCALED_: "KISAO"
    """elasticity coefficient (scaled): A scaled elasticity coefficient of any reaction with respect to an independent element (such as a global parameter or boundary species)."""

    KISAO_0000808: "KISAO"
    """reduced stoichiometry matrix: The reduced stoichiometry matrix. The dimensions are species by reactions."""

    REDUCED_STOICHIOMETRY_MATRIX: "KISAO"
    """reduced stoichiometry matrix: The reduced stoichiometry matrix. The dimensions are species by reactions."""

    KISAO_0000809: "KISAO"
    """reduced Jacobian matrix: The reduced Jacobian matrix. The dimensions are species by species."""

    REDUCED_JACOBIAN_MATRIX: "KISAO"
    """reduced Jacobian matrix: The reduced Jacobian matrix. The dimensions are species by species."""

    KISAO_0000810: "KISAO"
    """reduced eigenvalue matrix: The reduced eigenvalue matrix of a model. The dimensions are species by two, where the first column is the real part of the eigenvalues, and the second column is the imaginary part of the eigenvalues."""

    REDUCED_EIGENVALUE_MATRIX: "KISAO"
    """reduced eigenvalue matrix: The reduced eigenvalue matrix of a model. The dimensions are species by two, where the first column is the real part of the eigenvalues, and the second column is the imaginary part of the eigenvalues."""

    KISAO_0000811: "KISAO"
    """stoichiometry matrix: The (full) stoichiometry matrix. The dimensions are species by reactions."""

    STOICHIOMETRY_MATRIX: "KISAO"
    """stoichiometry matrix: The (full) stoichiometry matrix. The dimensions are species by reactions."""

    KISAO_0000812: "KISAO"
    """Jacobian matrix: The (full) Jacobian matrix. The dimensions are species by species."""

    JACOBIAN_MATRIX: "KISAO"
    """Jacobian matrix: The (full) Jacobian matrix. The dimensions are species by species."""

    KISAO_0000813: "KISAO"
    """Eigenvalue matrix: The (full) eigenvalue matrix of a model. The dimensions are species by two, where the first column is the real part of the eigenvalues, and the second column is the imaginary part of the eigenvalues."""

    EIGENVALUE_MATRIX: "KISAO"
    """Eigenvalue matrix: The (full) eigenvalue matrix of a model. The dimensions are species by two, where the first column is the real part of the eigenvalues, and the second column is the imaginary part of the eigenvalues."""

    KISAO_0000814: "KISAO"
    """flux control coefficient matrix (unscaled): The unscaled flux control coefficient matrix. The dimensions are reactions by reactions."""

    FLUX_CONTROL_COEFFICIENT_MATRIX__UNSCALED_: "KISAO"
    """flux control coefficient matrix (unscaled): The unscaled flux control coefficient matrix. The dimensions are reactions by reactions."""

    KISAO_0000815: "KISAO"
    """flux control coefficient matrix (scaled): The scaled flux control coefficient matrix. The dimensions are reactions by reactions."""

    FLUX_CONTROL_COEFFICIENT_MATRIX__SCALED_: "KISAO"
    """flux control coefficient matrix (scaled): The scaled flux control coefficient matrix. The dimensions are reactions by reactions."""

    KISAO_0000816: "KISAO"
    """link matrix: The link matrix of a model."""

    LINK_MATRIX: "KISAO"
    """link matrix: The link matrix of a model."""

    KISAO_0000817: "KISAO"
    """kernel matrix: The Kernel matrix of a model."""

    KERNEL_MATRIX: "KISAO"
    """kernel matrix: The Kernel matrix of a model."""

    KISAO_0000818: "KISAO"
    """L0 matrix: The L0 matrix of a model."""

    L0_MATRIX: "KISAO"
    """L0 matrix: The L0 matrix of a model."""

    KISAO_0000819: "KISAO"
    """Nr matrix: The Nr matrix of a model."""

    NR_MATRIX: "KISAO"
    """Nr matrix: The Nr matrix of a model."""

    KISAO_0000820: "KISAO"
    """model and simulation property characteristic: A property of a variable of a model or simulation."""

    MODEL_AND_SIMULATION_PROPERTY_CHARACTERISTIC: "KISAO"
    """model and simulation property characteristic: A property of a variable of a model or simulation."""

    KISAO_0000821: "KISAO"
    """intensive property: An intensive variable such as a concentration or temperature."""

    INTENSIVE_PROPERTY: "KISAO"
    """intensive property: An intensive variable such as a concentration or temperature."""

    KISAO_0000822: "KISAO"
    """extensive property: An extensive variable such as an amount, particle number, or mass."""

    EXTENSIVE_PROPERTY: "KISAO"
    """extensive property: An extensive variable such as an amount, particle number, or mass."""

    KISAO_0000824: "KISAO"
    """aggregation function: A function that aggregates a set of results, reducing its dimension(s). Examples include functions that compute minima or maxima of sets of values."""

    AGGREGATION_FUNCTION: "KISAO"
    """aggregation function: A function that aggregates a set of results, reducing its dimension(s). Examples include functions that compute minima or maxima of sets of values."""

    KISAO_0000825: "KISAO"
    """mean ignoring NaN: The mean (average) of a set of values, ignoring NaN entries."""

    MEAN_IGNORING_NAN: "KISAO"
    """mean ignoring NaN: The mean (average) of a set of values, ignoring NaN entries."""

    KISAO_0000826: "KISAO"
    """standard deviation ignoring NaN: The standard deviation of a set of values, ignoring NaN entries."""

    STANDARD_DEVIATION_IGNORING_NAN: "KISAO"
    """standard deviation ignoring NaN: The standard deviation of a set of values, ignoring NaN entries."""

    KISAO_0000827: "KISAO"
    """standard error ignoring NaN: The standard error of a set of values, ignoring NaN entries."""

    STANDARD_ERROR_IGNORING_NAN: "KISAO"
    """standard error ignoring NaN: The standard error of a set of values, ignoring NaN entries."""

    KISAO_0000828: "KISAO"
    """maximum ignoring NaN: The maximum value of a set of values, ignoring NaN entries."""

    MAXIMUM_IGNORING_NAN: "KISAO"
    """maximum ignoring NaN: The maximum value of a set of values, ignoring NaN entries."""

    KISAO_0000829: "KISAO"
    """minimum ignoring NaN: The minimum value of a set of values, ignoring NaN entries."""

    MINIMUM_IGNORING_NAN: "KISAO"
    """minimum ignoring NaN: The minimum value of a set of values, ignoring NaN entries."""

    KISAO_0000830: "KISAO"
    """maximum: The maximum of a set of values. If the values contain NaN the maximum is NaN."""

    MAXIMUM: "KISAO"
    """maximum: The maximum of a set of values. If the values contain NaN the maximum is NaN."""

    KISAO_0000831: "KISAO"
    """model and simulation property: A variable of a model or simulation."""

    MODEL_AND_SIMULATION_PROPERTY: "KISAO"
    """model and simulation property: A variable of a model or simulation."""

    KISAO_0000832: "KISAO"
    """time: The implied time variable of the model state."""

    TIME: "KISAO"
    """time: The implied time variable of the model state."""

    KISAO_0000834: "KISAO"
    """rate of change: The rate of change of one variable with respect to a second variable."""

    RATE_OF_CHANGE: "KISAO"
    """rate of change: The rate of change of one variable with respect to a second variable."""

    KISAO_0000835: "KISAO"
    """concentration control coefficient matrix (scaled): The scaled concentration control coefficient matrix. The dimensions are species by reactions."""

    CONCENTRATION_CONTROL_COEFFICIENT_MATRIX__SCALED_: "KISAO"
    """concentration control coefficient matrix (scaled): The scaled concentration control coefficient matrix. The dimensions are species by reactions."""

    KISAO_0000836: "KISAO"
    """amount: The extensive quantity amount."""

    AMOUNT: "KISAO"
    """amount: The extensive quantity amount."""

    KISAO_0000837: "KISAO"
    """particle number: The extensive quantity particle number, or, the molar amount of the entity multiplied by Avogadro's number."""

    PARTICLE_NUMBER: "KISAO"
    """particle number: The extensive quantity particle number, or, the molar amount of the entity multiplied by Avogadro's number."""

    KISAO_0000838: "KISAO"
    """concentration: The intensive quantity concentration, or, the amount of the entity with respect to the entity in which it resides."""

    CONCENTRATION: "KISAO"
    """concentration: The intensive quantity concentration, or, the amount of the entity with respect to the entity in which it resides."""

    KISAO_0000839: "KISAO"
    """temperature: The intensive quantity temperature."""

    TEMPERATURE: "KISAO"
    """temperature: The intensive quantity temperature."""

    KISAO_0000840: "KISAO"
    """minimum: The minimum of a set of values. If the values contain NaN the minimum is NaN."""

    MINIMUM: "KISAO"
    """minimum: The minimum of a set of values. If the values contain NaN the minimum is NaN."""

    KISAO_0000841: "KISAO"
    """mean: The mean of a set of values. If the values contain NaN the mean is NaN."""

    MEAN: "KISAO"
    """mean: The mean of a set of values. If the values contain NaN the mean is NaN."""

    KISAO_0000842: "KISAO"
    """standard deviation: The standard deviation of a set of values. If the values contain NaN the standard deviation is NaN."""

    STANDARD_DEVIATION: "KISAO"
    """standard deviation: The standard deviation of a set of values. If the values contain NaN the standard deviation is NaN."""

    KISAO_0000843: "KISAO"
    """standard error: The standard error of a set of values. If the values contain NaN the standard deviation is NaN."""

    STANDARD_ERROR: "KISAO"
    """standard error: The standard error of a set of values. If the values contain NaN the standard deviation is NaN."""

    KISAO_0000844: "KISAO"
    """sum ignoring NaN: The sum of a set of values, ignoring Nan entries."""

    SUM_IGNORING_NAN: "KISAO"
    """sum ignoring NaN: The sum of a set of values, ignoring Nan entries."""

    KISAO_0000845: "KISAO"
    """sum: The sum of a set of values. If the values contain NaN the sum is NaN."""

    SUM: "KISAO"
    """sum: The sum of a set of values. If the values contain NaN the sum is NaN."""

    KISAO_0000846: "KISAO"
    """product ignoring NaN: The product of a set of values, ignoring Nan entries."""

    PRODUCT_IGNORING_NAN: "KISAO"
    """product ignoring NaN: The product of a set of values, ignoring Nan entries."""

    KISAO_0000847: "KISAO"
    """product: The product of a set of values. If the values contain NaN the product is NaN."""

    PRODUCT: "KISAO"
    """product: The product of a set of values. If the values contain NaN the product is NaN."""

    KISAO_0000848: "KISAO"
    """cumulative sum ignoring NaN: The cumulative sum of a set of values, ignoring Nan entries."""

    CUMULATIVE_SUM_IGNORING_NAN: "KISAO"
    """cumulative sum ignoring NaN: The cumulative sum of a set of values, ignoring Nan entries."""

    KISAO_0000849: "KISAO"
    """cumulative sum: The cumulative sum of a set of values. If the values contain NaN the cumulative sum is NaN."""

    CUMULATIVE_SUM: "KISAO"
    """cumulative sum: The cumulative sum of a set of values. If the values contain NaN the cumulative sum is NaN."""

    KISAO_0000850: "KISAO"
    """cumulative product ignoring NaN: The cumulative product of a set of values, ignoring Nan entries."""

    CUMULATIVE_PRODUCT_IGNORING_NAN: "KISAO"
    """cumulative product ignoring NaN: The cumulative product of a set of values, ignoring Nan entries."""

    KISAO_0000851: "KISAO"
    """cumulative product: The cumulative product of a set of values. If the values contain NaN the cumulative product is NaN."""

    CUMULATIVE_PRODUCT: "KISAO"
    """cumulative product: The cumulative product of a set of values. If the values contain NaN the cumulative product is NaN."""

    KISAO_0000852: "KISAO"
    """count ignoring NaN: The number of non-zero elements of a set of values, ignoring Nan entries."""

    COUNT_IGNORING_NAN: "KISAO"
    """count ignoring NaN: The number of non-zero elements of a set of values, ignoring Nan entries."""

    KISAO_0000853: "KISAO"
    """count: The number of non-zero elements of a set of values. If the values contain NaN the count is NaN."""

    COUNT: "KISAO"
    """count: The number of non-zero elements of a set of values. If the values contain NaN the count is NaN."""

    KISAO_0000854: "KISAO"
    """length ignoring NaN: The number of elements of a set of values, ignoring Nan entries."""

    LENGTH_IGNORING_NAN: "KISAO"
    """length ignoring NaN: The number of elements of a set of values, ignoring Nan entries."""

    KISAO_0000855: "KISAO"
    """length: The number of elements of a set of values."""

    LENGTH: "KISAO"
    """length: The number of elements of a set of values."""

    KISAO_0000856: "KISAO"
    """median ignoring NaN: The median of a set of values, ignoring Nan entries."""

    MEDIAN_IGNORING_NAN: "KISAO"
    """median ignoring NaN: The median of a set of values, ignoring Nan entries."""

    KISAO_0000857: "KISAO"
    """median: The median of a set of values. If the values contain NaN the median is NaN."""

    MEDIAN: "KISAO"
    """median: The median of a set of values. If the values contain NaN the median is NaN."""

    KISAO_0000858: "KISAO"
    """variance ignoring NaN: The variance of a set of values, ignoring Nan entries."""

    VARIANCE_IGNORING_NAN: "KISAO"
    """variance ignoring NaN: The variance of a set of values, ignoring Nan entries."""

    KISAO_0000859: "KISAO"
    """variance: The variance of a set of values. If the values contain NaN the variance is NaN."""

    VARIANCE: "KISAO"
    """variance: The variance of a set of values. If the values contain NaN the variance is NaN."""


KISAOType = str | KISAO

#: information of every term, registered on the class below
_terms: list[TermData] = [
    (
        "KISAO_0000000",
        ("KISAO_0000000", "MODELLING_AND_SIMULATION_ALGORITHM"),
        "modelling and simulation algorithm",
        "Algorithm used to instantiate a simulation from a mathematical model.",
        ("modeling and simulation algorithm",),
        False,
    ),
    (
        "KISAO_0000003",
        ("KISAO_0000003", "WEIGHTED_STOCHASTIC_SIMULATION_ALGORITHM"),
        "weighted stochastic simulation algorithm",
        "The weighted stochastic simulation algorithm manipulates the probabilities measure of biochemical systems by sampling, in order to increase the fraction of simulation runs exhibiting rare events.",
        ("weighted SSA",),
        False,
    ),
    (
        "KISAO_0000015",
        ("KISAO_0000015", "GILLESPIE_FIRST_REACTION_ALGORITHM"),
        "Gillespie first reaction algorithm",
        "Stochastic simulation algorithm using the reaction probability density function (next-reaction density function), giving the probability that the next reaction will happen in a given time interval. To choose the next reaction to fire, the algorithm calculates a tentative reaction time for each reaction and then select the smallest.",
        ("Gillespie's first reaction method",),
        False,
    ),
    (
        "KISAO_0000017",
        ("KISAO_0000017", "MULTI_STATE_AGENT_BASED_SIMULATION_METHOD"),
        "multi-state agent-based simulation method",
        "The agent-based simulation method instantiates each molecule as an individual software object. The interactions between those objects are determined by interaction probabilities according to experimental data. The probability is depended on the state the molecule is in at that specific time (molecules have multiple-state). Additionally, ''pseudo-molecules'' are introduced to the system in order to simulate unimolecular reactions. For simulation, continuous time is broken down into discrete, independent ''slices''. During each time slice one molecule is selected randomly, a second molecule or pseudo-molecule is selected afterwards (leading to either a unimolecular or a bimolecular reaction). The reaction will only take place if a produced random number exceeds the reaction probability calculated beforehand. In that case, the system is updated after that reaction.",
        ("Morton-Firth",),
        False,
    ),
    (
        "KISAO_0000019",
        ("KISAO_0000019", "CVODE"),
        "CVODE",
        "The CVODE is a package written in C that solves ODE initial value problems, in real N-space, written as y'=f(t,y), y(t0)=y0. It is capable for stiff and non-stiff systems and uses two different linear multi-step methods, namely the Adam-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] method and the backward differentiation formula [http://identifiers.org/biomodels.kisao/KISAO_0000288].",
        ("VODE", "VODEPK", "code value ordinary differential equation solver"),
        False,
    ),
    (
        "KISAO_0000020",
        ("KISAO_0000020", "PVODE"),
        "PVODE",
        "PVODE is a general-purpose solver for ordinary differential equation (ODE) systems that implements methods for both stiff and nonstiff systems. [...] In the stiff case, PVODE uses a backward differentiation formula method [http://identifiers.org/biomodels.kisao/KISAO_0000288] combined with preconditioned GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000253] iteration. Parallelism is achieved by distributing the ODE solution vector into user-specified segments and parallelizing a set of vector kernels accordingly. For PDE-based ODE systems, we provide a module that generates a band block-diagonal preconditioner for use with the GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000253] iteration. PVODE is based on CVODE [http://identifiers.org/biomodels.kisao/KISAO_0000019].",
        ("parallel code value ordinary differential equation solver",),
        False,
    ),
    (
        "KISAO_0000021",
        ("KISAO_0000021", "STOCHSIM_NEAREST_NEIGHBOUR_ALGORITHM"),
        "StochSim nearest-neighbour algorithm",
        "The nearest-neighbour algorithm allows for the representation of spatial information, by adding a two-dimensional lattice in the form of a probabilistic cellular automata. That way, nearest neighbour interactions do additionally influence reactions taking place in the systems. Reactions between entities are calculated using the agent-based simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000017].",
        (),
        False,
    ),
    (
        "KISAO_0000022",
        ("KISAO_0000022", "ELF_AND_EHRENBERG_METHOD"),
        "Elf and Ehrenberg method",
        "Sub-volume stochastic reaction-diffusion method that is a combination of the Direct Method [http://identifiers.org/biomodels.kisao/KISAO_0000029] for sampling the time for a next reaction or diffusion event in each subvolume, with Gibson and Bruck's Next Reaction Method [http://identifiers.org/biomodels.kisao/KISAO_0000027], which is used to keep track of in which subvolume an event occurs next. The subvolumes are kept sorted in a queue, implemented as a binary tree, according to increasing time of the next event. When an event has occurred in the subvolume at the top of the queue, new event times need to be sampled only for one (the event is a chemical reaction) or two (the event is a diffusion jump) subvolume(s).",
        ("Elf algorithm", "NSM", "next-subvolume method"),
        False,
    ),
    (
        "KISAO_0000027",
        ("KISAO_0000027", "GIBSON_BRUCK_NEXT_REACTION_ALGORITHM"),
        "Gibson-Bruck next reaction algorithm",
        "As with the first reaction method [http://identifiers.org/biomodels.kisao/KISAO_0000015], a putative reaction time is calculated for each reaction, and the reaction with the shortest reaction time will be realized. However, the unused calculated reaction times are not wasted. The set of reactions is organized in a priority queue to allow for the efficient search for the fastest reaction. In addition, by using a so-called dependency graph only those reaction times are recalculated in each step, that are dependent on the reaction, which has been realized.",
        (
            "Gibson and Bruck algorithm",
            "Gibson-Bruck's next reaction algorithm",
            "Gillespie-Gibson stochastic simulation algorithm",
            "SSA-GB",
            "next reaction method",
        ),
        False,
    ),
    (
        "KISAO_0000028",
        ("KISAO_0000028", "SLOW_SCALE_STOCHASTIC_SIMULATION_ALGORITHM"),
        "slow-scale stochastic simulation algorithm",
        "Attempt to overcome the problem of stiff systems by developing an ''approximate theory that allows one to stochastically advance the system in time by simulating the firings of only the slow reaction events''.",
        ("slow-scale stochastic SSA", "ssSSA"),
        False,
    ),
    (
        "KISAO_0000029",
        ("KISAO_0000029", "GILLESPIE_DIRECT_ALGORITHM"),
        "Gillespie direct algorithm",
        "Stochastic simulation algorithm using the reaction probability density function (next-reaction density function), giving the probability that the next reaction will happen in a given time interval. To choose the next reaction to fire, the algorithm directly and separately calculates the identity of the reaction and the time it will fire.",
        (
            "DM",
            "Doob-Gillespie method",
            "Gillespie's algorithm",
            "Gillespie's direct method",
            "SSA",
            "stochastic simulation algorithm",
        ),
        False,
    ),
    (
        "KISAO_0000030",
        ("KISAO_0000030", "EULER_FORWARD_METHOD"),
        "Euler forward method",
        "The Euler method is an explicit one-step method for the numerical integration of ODES with a given initial value. The calculation of the next integration step at time t+1 is based on the state of the system at time point t.",
        ("explicit Euler method", "explicit Gaussian first order Runge-Kutta"),
        False,
    ),
    (
        "KISAO_0000031",
        ("KISAO_0000031", "EULER_BACKWARD_METHOD"),
        "Euler backward method",
        "The Euler backward method is an implicit one-step method for the numerical integration of ODES with a given initial value. The next state of a system is calculated by solving an equation that considers both, the current state of the system and the later one.",
        ("implicit Euler method", "implicit Gaussian first order Runge-Kutta"),
        False,
    ),
    (
        "KISAO_0000032",
        ("KISAO_0000032", "EXPLICIT_FOURTH_ORDER_RUNGE_KUTTA_METHOD"),
        "explicit fourth-order Runge-Kutta method",
        "The Runge-Kutta method is a method for the numerical integration of ODES with a given initial value. The calculation of the next integration step at time t+1 is based on the state of the system at time point t, plus the product of the size of the interval and an estimated slope. The slope is a weighted average of 4 single slope points (beginning of interval-midpoint-midpoint-end of interval).",
        ("ERK4", "RK4", "Runge-Kutta method"),
        False,
    ),
    (
        "KISAO_0000033",
        ("KISAO_0000033", "ROSENBROCK_METHOD"),
        "Rosenbrock method",
        "Some general implicit processes are given for the solution of simultaneous first-order differential equations. These processes, which use successive substitution, are implicit analogues of the (explicit) Runge-Kutta processes. They require the solution in each time step of one or more set of simultaneous linear equations, usually of a special and simple form. Processes of any required order can be devised, and they can be made to have a wide margin of stability when applied to a linear problem.",
        ("Kaps-Rentrop method", "generalized fourth order Runge-Kutta method"),
        False,
    ),
    (
        "KISAO_0000038",
        ("KISAO_0000038", "SORTING_STOCHASTIC_SIMULATION_ALGORITHM"),
        "sorting stochastic simulation algorithm",
        "In order to overcome the problem of high complexity of the stochastic simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000029] when simulating large systems, the sorting direct method maintains a loosely sorted order of the reactions as the simulation executes.",
        ("sorting SSA", "sorting direct method"),
        False,
    ),
    (
        "KISAO_0000039",
        ("KISAO_0000039", "TAU_LEAPING_METHOD"),
        "tau-leaping method",
        "Approximate acceleration procedure of the stochastic simulation algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000029] that divides the time into subintervals and ''leaps'' from one to another, firing all the reaction events in each subinterval.",
        ("tauL",),
        False,
    ),
    (
        "KISAO_0000040",
        ("KISAO_0000040", "POISSON_TAU_LEAPING_METHOD"),
        "Poisson tau-leaping method",
        "Explicit tau-leaping method with basic pre leap check.",
        (
            "explicit tau-leaping",
            "explicit tau-leaping method with basic pre-leap check",
            "explicit tau-leaping method with basic preleap check",
            "poisson tau-leaping",
        ),
        False,
    ),
    (
        "KISAO_0000045",
        ("KISAO_0000045", "IMPLICIT_TAU_LEAPING_METHOD"),
        "implicit tau-leaping method",
        "Contrary to the explicit tau-leaping [http://identifiers.org/biomodels.kisao/KISAO_0000039 and http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000239] , the implicit tau-leaping allows for much larger time-steps when simulating stiff systems.",
        (),
        False,
    ),
    (
        "KISAO_0000046",
        ("KISAO_0000046", "TRAPEZOIDAL_TAU_LEAPING_METHOD"),
        "trapezoidal tau-leaping method",
        "Formula for accelerated discrete efficient stochastic simulation of chemically reacting system [which] has better accuracy and stiff stability properties than the explicit and implicit [http://identifiers.org/biomodels.kisao/KISAO_0000045] tau-leaping formulas for discrete stochastic systems, and it limits to the trapezoidal rule in the deterministic regime.",
        ("trapezoidal implicit tau-leaping method",),
        False,
    ),
    (
        "KISAO_0000048",
        ("KISAO_0000048", "ADAPTIVE_EXPLICIT_IMPLICIT_TAU_LEAPING_METHOD"),
        "adaptive explicit-implicit tau-leaping method",
        "Modification of the original tau-selection strategy [http://identifiers.org/biomodels.kisao/KISAO_0000040], designed for explicit tau-leaping, is modified to apply to implicit tau-leaping, allowing for longer steps when the system is stiff. Further, an adaptive strategy is proposed that identifies stiffness and automatically chooses between the explicit and the (new) implicit tau-selection methods to achieve better efficiency.",
        (),
        False,
    ),
    (
        "KISAO_0000051",
        ("KISAO_0000051", "BORTZ_KALOS_LEBOWITZ_ALGORITHM"),
        "Bortz-Kalos-Lebowitz algorithm",
        "The Bortz-Kalos-Lebowitz (or: kinetic Monte-Carlo-) method is a stochastic method for the simulation of time evolution of processes using (pseudo-)random numbers.",
        (
            "BKL",
            "DMC",
            "KMC",
            "dynamic Monte Carlo",
            "dynamic Monte Carlo method",
            "kinetic Monte Carlo",
            "kinetic Monte Carlo method",
            "n-fold way",
        ),
        False,
    ),
    (
        "KISAO_0000056",
        ("KISAO_0000056", "SMOLUCHOWSKI_EQUATION_BASED_METHOD"),
        "Smoluchowski equation based method",
        "Method based on the Smoluchowski equation.",
        (),
        False,
    ),
    (
        "KISAO_0000057",
        ("KISAO_0000057", "BROWNIAN_DIFFUSION_SMOLUCHOWSKI_METHOD"),
        "Brownian diffusion Smoluchowski method",
        "In the Brownian diffusion Smoluchowski method, ''each molecule is treated as a point-like particle that diffuses freely in three-dimensional space. When a pair of reactive molecules collide, such as an enzyme and its substrate, a reaction occurs and the simulated reactants are replaced by products. [..] Analytic solutions are presented for some simulation parameters while others are calculated using look-up tables''. Supported chemical processes include molecular diffusion, treatment of surfaces, zeroth-order-, unimolecular-, and bimolecular reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000058",
        ("KISAO_0000058", "GREENS_FUNCTION_REACTION_DYNAMICS"),
        "Greens function reaction dynamics",
        "Method that simulates biochemical networks on particle level. It considers both changes in time and space by ''exploiting both the exact solution of the Smoluchowski Equation to set up an event-driven algorithm'' which allows for large jumps in time when the considered particles are far away from each other [in space] and thus cannot react. GFRD combines the propagation of particles in space with the reactions taking place between them in one simulation step.",
        ("GFRD", "Green's function reaction dynamics"),
        False,
    ),
    (
        "KISAO_0000064",
        ("KISAO_0000064", "RUNGE_KUTTA_BASED_METHOD"),
        "Runge-Kutta based method",
        "A method of numerically integrating ordinary differential equations, which uses a sampling of slopes through an interval and takes a weighted average to determine the right end point. This averaging gives a very accurate approximation.",
        ("modified Euler method",),
        False,
    ),
    (
        "KISAO_0000068",
        ("KISAO_0000068", "DETERMINISTIC_CELLULAR_AUTOMATA_UPDATE_ALGORITHM"),
        "deterministic cellular automata update algorithm",
        "A cellular automaton is a discrete model of a regular grid of cells with a finite number of dimensions. Each cell has a finite number of defined states. The automaton changes its state in a discrete manner, meaning that the state of a cell at time t is determined by a function of the states of its neighbours at time t - 1. These neighbours are a selection of cells relative to the specified cell. Famous examples for deterministic cellular automata are Conway's game of life or Wolfram's elementary cellular automata.",
        (),
        False,
    ),
    (
        "KISAO_0000071",
        ("KISAO_0000071", "LSODE"),
        "LSODE",
        "LSODE solves stiff and nonstiff systems of the form dy/dt = f. In the stiff case, it treats the Jacobian matrix sf/dy as either a dense (full) or a banded matrix, and as either user-supplied or internally approximated by difference quotients. It uses Adams methods (predictor-corrector) [http://identifiers.org/biomodels.kisao/KISAO_0000364] in the nonstiff case, and Backward Differentiation Formula (BDF) methods (the Gear methods) [http://identifiers.org/biomodels.kisao/KISAO_0000288] in the stiff case.",
        ("Livermore solver for ordinary differential equations",),
        False,
    ),
    (
        "KISAO_0000074",
        ("KISAO_0000074", "BINOMIAL_TAU_LEAPING_METHOD"),
        "binomial tau-leaping method",
        "Coarse grained modified version of the next subvolume method [http://identifiers.org/biomodels.kisao/KISAO_0000022] that allows the user to consider both diffusion and reaction events in relatively long simulation time spans as compared with the original method and other commonly used fully stochastic computational methods.",
        ("BtauL", "binomial tau-leap spatial stochastic simulation algorithm"),
        False,
    ),
    (
        "KISAO_0000075",
        ("KISAO_0000075", "GILLESPIE_MULTI_PARTICLE_METHOD"),
        "Gillespie multi-particle method",
        "Combination of the multiparticle method for diffusion [http://identifiers.org/biomodels.kisao/KISAO_0000334] and the SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029].",
        (
            "GMP",
            "Gillespie's multi-particle method",
            "particle-based spatial stochastic method",
        ),
        False,
    ),
    (
        "KISAO_0000076",
        ("KISAO_0000076", "STUNDZIA_AND_LUMSDEN_METHOD"),
        "Stundzia and Lumsden method",
        "Sub-volume stochastic reaction-diffusion method that using Green's function to link the bulk diffusion coefficient D in Fick's differential law to the corresponding transition rate probability for diffusion of a particle between finite volume elements. This generalized stochastic algorithm enables to numerically calculate the time evolution of a spatially inhomogeneous mixture of reaction-diffusion species in a finite volume. The time step is stochastic and is generated by a probability distribution determined by the intrinsic reaction kinetics and diffusion dynamics.",
        ("RD SSA", "reaction-diffusion stochastic simulation algorithm"),
        False,
    ),
    (
        "KISAO_0000081",
        ("KISAO_0000081", "ESTIMATED_MIDPOINT_TAU_LEAPING_METHOD"),
        "estimated midpoint tau-leaping method",
        "Estimated-Midpoint tau-Leap Method: For the selected leaping time tau which satisfies the Leap Condition, compute the expected state change lambda' = tau sumj( aj(x)vj ) during [t, t + tau). Then, with x' =x + [lambda'/2], generate for each j = 1,...,M a sample value kj of the Poisson random variable P(aj(x'), tau). Compute the actual state change, lambda = sumj( kjvj ), and effect the leap by replacing t by t + tau and x by x + lambda.",
        ("explicit tau-leaping method with estimated-mid point technique",),
        False,
    ),
    (
        "KISAO_0000082",
        ("KISAO_0000082", "K_ALPHA_LEAPING_METHOD"),
        "k-alpha leaping method",
        "Alternative to the tau-leaping [http://identifiers.org/biomodels.kisao/KISAO_0000039], where one leaps a fixed number of reaction-events.",
        (),
        False,
    ),
    (
        "KISAO_0000084",
        ("KISAO_0000084", "NONNEGATIVE_POISSON_TAU_LEAPING_METHOD"),
        "nonnegative Poisson tau-leaping method",
        "The explicit tau-leaping procedure attempts to speed up the stochastic simulation of a chemically reacting system by approximating the number of firings of each reaction channel during a chosen time increment Tau as a Poisson random variable. Since the Poisson random variable can have arbitrarily large sample values, there is always the possibility that this procedure will cause one or more reaction channels to fire so many times during Tau that the population of some reactant species will be driven negative. Two recent papers have shown how that unacceptable occurrence can be avoided by replacing the Poisson random variables with binomial random variables, whose values are naturally bounded. This paper describes a modified Poisson tau-leaping procedure that also avoids negative populations, but is easier to implement than the binomial procedure. The new Poisson procedure also introduces a second control parameter, whose value essentially dials the procedure from the original Poisson tau-leaping at one extreme to the exact stochastic simulation algorithm at the other; therefore, the modified Poisson procedure will generally be more accurate than the original Poisson procedure [http://identifiers.org/biomodels.kisao/KISAO_0000040].",
        ("modified poisson tau-leaping",),
        False,
    ),
    (
        "KISAO_0000086",
        ("KISAO_0000086", "FEHLBERG_METHOD"),
        "Fehlberg method",
        "The method was developed by the German mathematician Erwin Fehlberg and is based on the class of Runge-Kutta methods. The Runge-Kutta-Fehlberg method uses an O(h4) method together with an O(h5) method that uses all of the points of the O(h4) method, and hence is often referred to as an RKF45 method. Similar schemes with different orders have since been developed. By performing one extra calculation that would be required for an RK5 method, the error in the solution can be estimated and controlled and an appropriate step size can be determined automatically, making this method efficient for ordinary problems of automated numerical integration of ordinary differential equations.",
        ("RKF45", "Runge-Kutta-Fehlberg method"),
        False,
    ),
    (
        "KISAO_0000087",
        ("KISAO_0000087", "DORMAND_PRINCE_METHOD"),
        "Dormand-Prince method",
        "Dormand-Prince is an explicit method for the numerical integration of ODES with a given initial value. It is an 'embedded Runge-Kutta method' [http://identifiers.org/biomodels.kisao/KISAO_0000302] RK5 (4) which (a) has a 'small' principal truncation term in the Fifth order and (b) has an extended region of absolute stability.",
        ("DOPRI", "Prince-Dormand method"),
        False,
    ),
    (
        "KISAO_0000088",
        ("KISAO_0000088", "LSODA"),
        "LSODA",
        "LSODA solves systems dy/dt = f with a dense or banded Jacobian when the problem is stiff, but it automatically selects between non-stiff (Adams [http://identifiers.org/biomodels.kisao/KISAO_0000289]) and stiff (BDF [http://identifiers.org/biomodels.kisao/KISAO_0000288]) methods. It uses the non-stiff method initially, and dynamically monitors data in order to decide which method to use.",
        (
            "Livermore solver for ordinary differential equations with automatic method switching",
        ),
        False,
    ),
    (
        "KISAO_0000089",
        ("KISAO_0000089", "LSODAR"),
        "LSODAR",
        "LSODAR is a variant of LSODA [http://identifiers.org/biomodels.kisao/KISAO_0000088] with a root finding capability added. Thus it solves problems dy/dt = f with dense or banded Jacobian and automatic method selection, and at the same time, it finds the roots of any of a set of given functions of the form g(t,y). This is often useful for finding stop conditions, or for finding points at which a switch is to be made in the function f.",
        (
            "Livermore solver for ordinary differential equations with automatic method switching and root finding",
            "ordinary differential equation solver for stiff or non-stiff systems with root finding",
        ),
        False,
    ),
    (
        "KISAO_0000090",
        ("KISAO_0000090", "LSODI"),
        "LSODI",
        "LSODI solves systems given in linearly implicit form, including differential-algebraic systems.",
        ("Livermore solver for ordinary differential equations, implicit version",),
        False,
    ),
    (
        "KISAO_0000091",
        ("KISAO_0000091", "LSODIS"),
        "LSODIS",
        "LSODIS is a set of general-purpose FORTRAN routines solver for the initial value problem for ordinary differential equation systems. It is suitable for both stiff and nonstiff systems. LSODIS treat systems in the linearly implicit form A(t,y) dy/dt = g(t,y), A = a square matrix, i.e. with the derivative dy/dt implicit, but linearly so.",
        (
            "Livermore solver for ordinary differential equations, implicit sparse version",
        ),
        False,
    ),
    (
        "KISAO_0000093",
        ("KISAO_0000093", "LSODPK"),
        "LSODPK",
        "LSODPK is a set of FORTRAN subroutines for solving the initial value problem for stiff and nonstiff systems of ordinary differential equations. In solving stiff systems, LSODPK uses a corrector iteration composed of Newton iteration and one of four preconditioned Krylov subspace iteration methods [http://identifiers.org/biomodels.kisao/KISAO_0000354]. The user must select the desired Krylov method and supply a pair of routine to evaluate, preprocess, and solve the (left and/or right) preconditioner matrices. Aside from preconditioning, the implementation is matrix-free, meaning that explicit storage of the Jacobian (or related) matrix is not required. The method is experimental because the scope of problems for which it is effective is not well-known, and users are forewarned that LSODPK may or may not be competitive with traditional methods on a given problem. LSODPK also includes an option for a user-supplied linear system solver to be used without Krylov iteration.",
        (
            "Livermore solver for ordinary differential equations for stiff and nonstiff systems with krylov corrector iteration",
        ),
        False,
    ),
    (
        "KISAO_0000094",
        ("KISAO_0000094", "LIVERMORE_SOLVER"),
        "Livermore solver",
        "Method to solve ordinary differential equations developed at the Lawrence Livermore National Laboratory.",
        (),
        False,
    ),
    (
        "KISAO_0000095",
        ("KISAO_0000095", "SUB_VOLUME_STOCHASTIC_REACTION_DIFFUSION_ALGORITHM"),
        "sub-volume stochastic reaction-diffusion algorithm",
        "Stochastic method using a combination of discretisation of compartment volumes into voxels and Gillespie-like algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000241] to simulate the evolution of the system.",
        (),
        False,
    ),
    (
        "KISAO_0000097",
        ("KISAO_0000097", "MODELLING_AND_SIMULATION_ALGORITHM_CHARACTERISTIC"),
        "modelling and simulation algorithm characteristic",
        "Simulation algorithm property, which can, for example, describe the model, such as the type of variables (discrete or continuous), and information on the treatment of spatial descriptions, or can be a numerical characteristic, such as the system's behaviour (deterministic or stochastic) as well as the progression mechanism (fixed or adaptive time steps).",
        ("modeling and simulation algorithm characteristic",),
        False,
    ),
    (
        "KISAO_0000098",
        ("KISAO_0000098", "TYPE_OF_VARIABLE"),
        "type of variable",
        "Type of variables used for the simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000099",
        ("KISAO_0000099", "TYPE_OF_SYSTEM_BEHAVIOUR"),
        "type of system behaviour",
        "A characteristic describing the rules the algorithm uses to simulate the temporal evolution of a system, specifically whether or not the final state is uniquely determined from a precise initial state.",
        (),
        False,
    ),
    (
        "KISAO_0000100",
        ("KISAO_0000100", "TYPE_OF_PROGRESSION_TIME_STEP"),
        "type of progression time step",
        "Type of time steps used by the algorithm.",
        (),
        False,
    ),
    (
        "KISAO_0000102",
        ("KISAO_0000102", "SPATIAL_DESCRIPTION"),
        "spatial description",
        "Algorithm, possessing this characteristic, takes into account the location of the reacting components.",
        (),
        False,
    ),
    (
        "KISAO_0000103",
        ("KISAO_0000103", "DETERMINISTIC_SYSTEM_BEHAVIOUR"),
        "deterministic system behaviour",
        "Algorithm, possessing this characteristic, simulates the temporal evolution of a system deterministically, so that from a precise initial state the algorithm will always end up in the same final state.",
        (),
        False,
    ),
    (
        "KISAO_0000104",
        ("KISAO_0000104", "STOCHASTIC_SYSTEM_BEHAVIOUR"),
        "stochastic system behaviour",
        "Algorithm, possessing this characteristic, simulates the temporal evolution of a system using probabilistic rules, so that between two simulations, the same precise initial state may result in a different final state.",
        (),
        False,
    ),
    (
        "KISAO_0000105",
        ("KISAO_0000105", "DISCRETE_VARIABLE"),
        "discrete variable",
        "Algorithm, possessing this characteristic, allows values of system's variables to change by discrete (integral) amounts.",
        (),
        False,
    ),
    (
        "KISAO_0000106",
        ("KISAO_0000106", "CONTINUOUS_VARIABLE"),
        "continuous variable",
        "Algorithm, possessing this characteristic, allows the values of a system's variables to change by continuous (non-integral) amounts.",
        (),
        False,
    ),
    (
        "KISAO_0000107",
        ("KISAO_0000107", "PROGRESSION_WITH_ADAPTIVE_TIME_STEP"),
        "progression with adaptive time step",
        "Algorithm, possessing this characteristic, does not use fixed time steps to update the state of a system during the whole simulation, but on the contrary adapts the length of the time steps to the local situation.",
        (),
        False,
    ),
    (
        "KISAO_0000108",
        ("KISAO_0000108", "PROGRESSION_WITH_FIXED_TIME_STEP"),
        "progression with fixed time step",
        "Algorithm, possessing this characteristic, uses time steps of constant length to update the state of a system during the whole simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000201",
        ("KISAO_0000201", "MODELLING_AND_SIMULATION_ALGORITHM_PARAMETER"),
        "modelling and simulation algorithm parameter",
        "Parameter that can be used in the simulation experiment settings.",
        ("modeling and simulation algorithm parameter",),
        False,
    ),
    (
        "KISAO_0000203",
        ("KISAO_0000203", "PARTICLE_NUMBER_LOWER_LIMIT"),
        "particle number lower limit",
        "This parameter of 'Pahle hybrid method' [http://identifiers.org/biomodels.kisao/KISAO_0000231] is a double value specifying the lower limit for particle numbers. Species with a particle number below this value are considered as having a low particle number. The 'particle number lower limit' cannot be higher than the 'particle number upper limit' [http://identifiers.org/biomodels.kisao/KISAO_0000204].",
        (),
        False,
    ),
    (
        "KISAO_0000204",
        ("KISAO_0000204", "PARTICLE_NUMBER_UPPER_LIMIT"),
        "particle number upper limit",
        "This parameter of 'Pahle hybrid method' [http://identifiers.org/biomodels.kisao/KISAO_0000231] is a double value specifying the upper limit for particle numbers. Species with a particle number above this value are considered as having a high particle number. The 'particle number upper limit' cannot be lower than the 'particle number lower limit' [http://identifiers.org/biomodels.kisao/KISAO_0000203].",
        (),
        False,
    ),
    (
        "KISAO_0000205",
        ("KISAO_0000205", "PARTITIONING_INTERVAL"),
        "partitioning interval",
        "This positive integer value specifies after how many steps the internal partitioning of the system should be recalculated.",
        (),
        False,
    ),
    (
        "KISAO_0000209",
        ("KISAO_0000209", "RELATIVE_TOLERANCE"),
        "relative tolerance",
        "This parameter is a numeric value specifying the desired relative tolerance the user wants to achieve. A smaller value means that the trajectory is calculated more accurately.",
        ("RTOL",),
        False,
    ),
    (
        "KISAO_0000211",
        ("KISAO_0000211", "ABSOLUTE_TOLERANCE"),
        "absolute tolerance",
        "This parameter is a positive numeric value specifying the desired absolute tolerance the user wants to achieve.",
        ("ATOL",),
        False,
    ),
    (
        "KISAO_0000216",
        ("KISAO_0000216", "USE_REDUCED_MODEL"),
        "use reduced model",
        "Boolean value which indicates whether the simulation/analysis should be performed using the complete model or an equivalent reduced model. Reduced models can be determined in many ways such as using mass conservation laws.",
        ("integrate reduced model",),
        False,
    ),
    (
        "KISAO_0000219",
        ("KISAO_0000219", "MAXIMUM_ADAMS_ORDER"),
        "maximum Adams order",
        "This parameter is a positive integer value specifying the maximal order the non-stiff Adams integration method [http://identifiers.org/biomodels.kisao/KISAO_0000289] shall attempt before switching to the stiff BDF method [http://identifiers.org/biomodels.kisao/KISAO_0000288].",
        ("Adams max order", "maximum non-stiff order"),
        False,
    ),
    (
        "KISAO_0000220",
        ("KISAO_0000220", "MAXIMUM_BDF_ORDER"),
        "maximum BDF order",
        "This parameter is a positive integer value specifying the maximal order the stiff BDF integration method [http://identifiers.org/biomodels.kisao/KISAO_0000288] shall attempt before switching to smaller internal step sizes.",
        ("BDF max order", "maximum stiff order"),
        False,
    ),
    (
        "KISAO_0000223",
        ("KISAO_0000223", "NUMBER_OF_HISTORY_BINS"),
        "number of history bins",
        "The 'number of history bins' is only enabled for models that contain delayed or multistep reactions for specifying the granularity with which the delayed reaction solver should retain the history of species values, for species that participate in delayed reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000228",
        ("KISAO_0000228", "TAU_LEAPING_EPSILON"),
        "tau-leaping epsilon",
        "The leap condition is chosen such that the expected change in the propensity function aj(x) is bounded by Epsilon * a0 where Epsilon is an error control parameter between 0 and 1. This parameter is the basic error control mechanism for the Tau-Leaping algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000039]. As Epsilon decreases the leaps become shorter and the simulation is more accurate.",
        ("epsilon", "tolerance"),
        False,
    ),
    (
        "KISAO_0000230",
        ("KISAO_0000230", "MINIMUM_REACTIONS_PER_LEAP"),
        "minimum reactions per leap",
        "'minimum reactions per leap' parameter is used in hybrid methods, which adaptively switch between the tau-leaping algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000039] to the SSA Direct Method [http://identifiers.org/biomodels.kisao/KISAO_0000029] when the number of reactions in a single tau-leaping leap step is less than the threshold.",
        ("threshold",),
        False,
    ),
    (
        "KISAO_0000231",
        ("KISAO_0000231", "PAHLE_HYBRID_METHOD"),
        "Pahle hybrid method",
        "The hybrid method combines the stochastic 'Gibson-Bruck's next reaction method' [http://identifiers.org/biomodels.kisao/KISAO_0000027] with different algorithms for the numerical integration of ODEs [http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000374]. The biochemical network is dynamically partitioned into a deterministic and a stochastic subnet depending on the current particle numbers in the system. The user can define limits for when a particle number should be considered low or high. The stochastic subnet contains reactions involving low numbered species as substrate or product. All the other reactions form the deterministic subnet. The two subnets are then simulated in parallel using the stochastic and deterministic solver, respectively. The reaction probabilities in the stochastic subnet are approximated as constant between two stochastic reaction events.",
        (),
        False,
    ),
    (
        "KISAO_0000232",
        ("KISAO_0000232", "LSOIBT"),
        "LSOIBT",
        "LSOIBT solves linearly implicit systems in which the matrices involved are all assumed to be block-tridiagonal. Linear systems are solved by the LU method.",
        (
            "Livermore solver for ordinary differential equations given in implicit form, with block-tridiagonal Jacobian treatment",
        ),
        False,
    ),
    (
        "KISAO_0000233",
        ("KISAO_0000233", "LSODES"),
        "LSODES",
        "LSODES solves systems dy/dt = f and in the stiff case treats the Jacobian matrix in general sparse form. It determines the sparsity structure on its own, or optionally accepts this information from the user. It then uses parts of the Yale Sparse Matrix Package (YSMP) to solve the linear systems that arise, by a sparse (direct) LU factorization/backsolve method.",
        (
            "Livermore solver for ordinary differential equations with general sparse Jacobian matrix",
        ),
        False,
    ),
    (
        "KISAO_0000234",
        ("KISAO_0000234", "LSODKR"),
        "LSODKR",
        "LSODKR is an initial value ODE solver for stiff and nonstiff systems. It is a variant of the LSODPK [http://identifiers.org/biomodels.kisao/KISAO_0000093] and LSODE [http://identifiers.org/biomodels.kisao/KISAO_0000071] solvers, intended mainly for large stiff systems. The main differences between LSODKR and LSODE [http://identifiers.org/biomodels.kisao/KISAO_0000071] are the following: a) for stiff systems, LSODKR uses a corrector iteration composed of Newton iteration and one of four preconditioned Krylov subspace iteration methods. The user must supply routines for the preconditioning operations, b) within the corrector iteration, LSODKR does automatic switching between functional (fixpoint) iteration and modified Newton iteration, c) LSODKR includes the ability to find roots of given functions of the solution during the integration.",
        (
            "Livermore solver for ordinary differential equations, with preconditioned Krylov iteration methods for the Newton correction linear systems, and with root finding.",
        ),
        False,
    ),
    (
        "KISAO_0000235",
        ("KISAO_0000235", "TYPE_OF_SOLUTION"),
        "type of solution",
        "A characteristic describing the type of the solution produced by the method, specifically whether it is exact or approximate.",
        (),
        False,
    ),
    (
        "KISAO_0000236",
        ("KISAO_0000236", "EXACT_SOLUTION"),
        "exact solution",
        "Algorithm, possessing this characteristic, provides an exact solution to the initial problem.",
        (),
        False,
    ),
    (
        "KISAO_0000237",
        ("KISAO_0000237", "APPROXIMATE_SOLUTION"),
        "approximate solution",
        "Approximation algorithms are algorithms used to find approximate solutions to optimization problems. Approximation algorithms are often associated with NP-hard problems; since it is unlikely that there can ever be efficient polynomial time exact algorithms solving NP-hard problems, one settles for polynomial time sub-optimal solutions. Unlike heuristics, which usually only find reasonably good solutions reasonably fast, one wants provable solution quality and provable run time bounds. Ideally, the approximation is optimal up to a small constant factor (for instance within 5% of the optimal solution). Approximation algorithms are increasingly being used for problems where exact polynomial-time algorithms are known but are too expensive due to the input size.",
        (),
        False,
    ),
    (
        "KISAO_0000238",
        ("KISAO_0000238", "TYPE_OF_METHOD"),
        "type of method",
        "A characteristic describing the way the method finds a solution, specifically whether it solves an equation involving only the current state of the system (explicit) or both the current and the later one (implicit).",
        (),
        False,
    ),
    (
        "KISAO_0000239",
        ("KISAO_0000239", "EXPLICIT_METHOD_TYPE"),
        "explicit method type",
        "Explicit methods calculate the state of a system at a later time from the state of the system at the current time. Mathematically, if Y(t) is the current system state and Y((t+delta t) is the state at the later time (delta t is a small time step), then, for an explicit method Y(t+delta t) = F(Y(t)), to find Y(t+delta t).",
        (),
        False,
    ),
    (
        "KISAO_0000240",
        ("KISAO_0000240", "IMPLICIT_METHOD_TYPE"),
        "implicit method type",
        "Implicit methods find a solution by solving an equation involving both the current state of the system and the later one. Mathematically, if Y(t) is the current system state and Y((t+delta t) is the state at the later time (delta t is a small time step), then, for an implicit method one solves an equation G(Y(t), Y(t+delta t))=0, to find Y(t+delta t).",
        (),
        False,
    ),
    (
        "KISAO_0000241",
        ("KISAO_0000241", "GILLESPIE_LIKE_METHOD"),
        "Gillespie-like method",
        "Stochastic simulation algorithm using an approach alike the one described in Gillespie's papers of 1976 and 1977.",
        (),
        False,
    ),
    (
        "KISAO_0000242",
        ("KISAO_0000242", "ERROR_CONTROL_PARAMETER"),
        "error control parameter",
        "Parameter controlling method accuracy.",
        (),
        False,
    ),
    (
        "KISAO_0000243",
        ("KISAO_0000243", "METHOD_SWITCHING_CONTROL_PARAMETER"),
        "method switching control parameter",
        "Parameters describing threshold conditions for algorithms that switch between different methods.",
        (),
        False,
    ),
    (
        "KISAO_0000244",
        ("KISAO_0000244", "GRANULARITY_CONTROL_PARAMETER"),
        "granularity control parameter",
        "Parameter controlling granularity.",
        (),
        False,
    ),
    (
        "KISAO_0000245",
        ("KISAO_0000245", "HAS_CHARACTERISTIC"),
        "has characteristic",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000246",
        ("KISAO_0000246", "IS_HYBRID_OF"),
        "is hybrid of",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000248",
        ("KISAO_0000248", "TAU_LEAPING_DELTA"),
        "tau-leaping delta",
        "Tau-leaping delta specifies how close two symmetric transition rates must be before we classify them as in partial-equilibrium. Only applies to the implicit tau routine [http://identifiers.org/biomodels.kisao/KISAO_0000045].",
        (),
        False,
    ),
    (
        "KISAO_0000249",
        ("KISAO_0000249", "CRITICAL_FIRING_THRESHOLD"),
        "critical firing threshold",
        "The 'nonnegative Poisson tau-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000084] is based on the fact that negative populations typically arise from multiple firings of reactions that are only a few firings away from consuming all the molecules of one of their reactants. To focus on those reaction channels, the modified tau-leaping algorithm introduces a second control parameter nc, a positive integer that is usually set somewhere between 5 and 20. Any reaction channel with a positive propensity function that is currently within nc firings of exhausting one of its reactants is then classified as a critical reaction. The modified algorithm chooses tau in such a way that no more than one firing of all the critical reactions can occur during the leap.",
        ("nonnegative tau-leaping second control parameter",),
        False,
    ),
    (
        "KISAO_0000250",
        ("KISAO_0000250", "IS_PARAMETER_OF"),
        "is parameter of",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000252",
        ("KISAO_0000252", "PARTITIONING_CONTROL_PARAMETER"),
        "partitioning control parameter",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000253",
        ("KISAO_0000253", "COARSE_GRAINING_FACTOR"),
        "coarse-graining factor",
        "The time in each Monte-Carlo iteration of 'binomial tau-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000074] is updated with the time increments tau=f/(a1+a2+...+aM). Here 1/(a1+a2+...+aM) is the averaged microscopic increment of the SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] and f is a coarse-graining factor, controlling the speed-up.",
        (),
        False,
    ),
    (
        "KISAO_0000254",
        ("KISAO_0000254", "BROWNIAN_DIFFUSION_ACCURACY"),
        "Brownian diffusion accuracy",
        "Accuracy code of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057], which sets which neighbouring boxes are checked for potential bi-molecular reactions. Consider the reaction A + B -> C and suppose that A and B are within a binding radius of each other. This reaction will always be performed if A and B are in the same virtual box. If accuracy is set to at least 3, then it will also occur if A and B are in nearest-neighbour virtual boxes. If it is at least 7, then the reaction will happen if they are in nearest-neighbour boxes that are separated by periodic boundary conditions. And if it is 9 or 10, then all edge and corner boxes are checked for reactions, which means that no potential reactions are overlooked.",
        (),
        False,
    ),
    (
        "KISAO_0000255",
        ("KISAO_0000255", "MOLECULES_PER_VIRTUAL_BOX"),
        "molecules per virtual box",
        "Target molecules per virtual box is a parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057], which sets the box sizes so that the average number of molecules per box, at simulation initiation, is close to the requested number.",
        (),
        False,
    ),
    (
        "KISAO_0000256",
        ("KISAO_0000256", "VIRTUAL_BOX_SIDE_LENGTH"),
        "virtual box side length",
        "The 'virtual box side length' is a parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. It requests the length of one side of a box.",
        (),
        False,
    ),
    (
        "KISAO_0000257",
        ("KISAO_0000257", "SURFACE_BOUND_EPSILON"),
        "surface-bound epsilon",
        "A parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. Molecules that are bound to a surface are given locations that are extremely close to that surface. However, this position does not need to be exactly at the surface, and in fact it usually cannot be exactly at the surface due to round-off error. The tolerance for how far a surface-bound molecule is allowed to be away from the surface can be set with the epsilon statement.",
        (),
        False,
    ),
    (
        "KISAO_0000258",
        ("KISAO_0000258", "NEIGHBOUR_DISTANCE"),
        "neighbour distance",
        "A parameter of 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057]. When a surface-bound molecule diffuses off of one surface panel, it can sometimes diffuse onto the neighbouring surface tile. It does so only if the neighbouring panel is declared to be a neighbour and also the neighbour is within a distance that is set with the neighbour distance statement.",
        (),
        False,
    ),
    (
        "KISAO_0000259",
        ("KISAO_0000259", "HAS_PARAMETER"),
        "has parameter",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000260",
        ("KISAO_0000260", "VIRTUAL_BOX_SIZE"),
        "virtual box size",
        "Target size of virtual boxes for 'Brownian diffusion Smoluchowski method' [http://identifiers.org/biomodels.kisao/KISAO_0000057].",
        (),
        False,
    ),
    (
        "KISAO_0000261",
        ("KISAO_0000261", "EULER_METHOD"),
        "Euler method",
        "The Euler method, named after Leonhard Euler, is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value.",
        (),
        False,
    ),
    (
        "KISAO_0000263",
        ("KISAO_0000263", "NFSIM_AGENT_BASED_SIMULATION_METHOD"),
        "NFSim agent-based simulation method",
        "A generalization a rule-based version of 'Gillespie's direct method' (SSA) [http://identifiers.org/biomodels.kisao/KISAO_0000029]. The method is guaranteed to produce the same results as the exact SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] by cycling over three primary steps. First, NFsim calculates the probability or propensity for each rule to take effect given the current molecular states. Second, it samples the time to the next reaction event and selects the corresponding reaction rule. Finally, NFsim executes the selected reaction by applying the rule and updating the molecular agents accordingly.",
        (),
        False,
    ),
    (
        "KISAO_0000264",
        ("KISAO_0000264", "CELLULAR_AUTOMATA_UPDATE_METHOD"),
        "cellular automata update method",
        "Cellular automata are mathematical idealizations of physical systems in which space and time are discrete, and physical quantities take on a finite set of discrete values. A cellular automaton consists of a regular uniform lattice (or ''array''), usually infinite in extent, with a discrete variable at each site (''cell''). A cellular automaton evolves in discrete time steps, with the value of the variable at one site being affected by the values of variables at sites in its ''neighbourhood'' on the previous time step. The neighbourhood of a site is typically taken to be the site itself and all immediately adjacent sites. The variables at each site are updated simultaneously (''synchronously''), based on the values of the variables in their neighbourhood at the preceding time step, and according to a definite set of ''local rules''.",
        (
            "CA",
            "cellular automata",
            "cellular spaces",
            "cellular structures",
            "homogeneous structures",
            "iterative arrays",
            "tessellation automata",
            "tessellation structures",
        ),
        False,
    ),
    (
        "KISAO_0000268",
        ("KISAO_0000268", "IS_CHARACTERISTIC_OF"),
        "is characteristic of",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000273",
        ("KISAO_0000273", "HARD_PARTICLE_MOLECULAR_DYNAMICS"),
        "hard-particle molecular dynamics",
        "A collision-driven molecular dynamics algorithm for a system of non-spherical particles.",
        (),
        False,
    ),
    (
        "KISAO_0000274",
        ("KISAO_0000274", "FIRST_PASSAGE_MONTE_CARLO_ALGORITHM"),
        "first-passage Monte Carlo algorithm",
        "We present a novel Monte Carlo algorithm for N diffusing finite particles that react on collisions. Using the theory of first-passage processes and time dependent Green's functions, we break the difficult N-body problem into independent single- and two-body propagations circumventing numerous diffusion hops used in standard Monte Carlo simulations. The new algorithm is exact, extremely efficient, and applicable to many important physical situations in arbitrary integer dimensions.",
        (
            "AED DKMC",
            "AED diffusion kinetic Monte Carlo method",
            "asynchronous event-driven diffusion Monte Carlo",
        ),
        False,
    ),
    (
        "KISAO_0000276",
        ("KISAO_0000276", "GILL_METHOD"),
        "Gill method",
        "Gill's fourth order method is a Runge-Kutta method for approximating the solution of the initial value problem y'(x) = f(x,y); y(x0) = y0 which evaluates the integrand,f(x,y), four times per step. This method is a fourth order procedure for which Richardson extrapolation can be used.",
        ("Gill's method", "Runge-Kutta-Gill method"),
        False,
    ),
    (
        "KISAO_0000278",
        ("KISAO_0000278", "METROPOLIS_MONTE_CARLO_ALGORITHM"),
        "Metropolis Monte Carlo algorithm",
        "A general method, suitable for fast computing machines, for investigating such properties as equations of state for substances consisting of interacting individual molecules is described. The method consists of a modified Monte Carlo integration [http://identifiers.org/biomodels.kisao/KISAO_0000051] over configuration space.",
        ("Metropolis algorithm", "Metropolis-Hastings algorithm"),
        False,
    ),
    (
        "KISAO_0000279",
        ("KISAO_0000279", "ADAMS_BASHFORTH_METHOD"),
        "Adams-Bashforth method",
        "Given an initial value problem: y' = f(x,y), y(x0) = y0 together with additional starting values y1 = y(x0 + h), . . . , yk-1 = y(x0 + (k-1) h) the k-step Adams-Bashforth method is an explicit linear multistep method that approximates the solution, y(x) at x = x0+kh, of the initial value problem by yk = yk - 1 + h * ( a0 f(xk - 1,yk - 1) + a1 f(xk - 2,yk - 2) + . . . + ak - 1 f(x0,y0) ), where a0, a1, . . . , ak - 1 are constants.",
        ("explicit Adams method",),
        False,
    ),
    (
        "KISAO_0000280",
        ("KISAO_0000280", "ADAMS_MOULTON_METHOD"),
        "Adams-Moulton method",
        "The (k-1)-step Adams-Moulton method is an implicit linear multistep method that iteratively approximates the solution, y(x) at x = x0+kh, of the initial value problem by yk = yk - 1 + h * ( b0 f(xk,yk) + b1 f(xk - 1,yk - 1) + . . . + bk - 1 f(x1,y1) ), where b1, . . . , bk - 1 are constants.",
        ("implicit Adams method",),
        False,
    ),
    (
        "KISAO_0000281",
        ("KISAO_0000281", "MULTISTEP_METHOD"),
        "multistep method",
        "A numerical method for differential equations which is based on several values of the solution.",
        ("multi-value method",),
        False,
    ),
    (
        "KISAO_0000282",
        ("KISAO_0000282", "KINSOL"),
        "KINSOL",
        "KINSOL solves algebraic systems in real N-space, written as F(u)=0, F:RN->RN, given an initial guess u0. The basic method is either a modified or an inexact Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408]. The linear systems that arise are solved with either a direct (dense or banded) solver (serial version only), or one of the Krylov iterative solvers [http://identifiers.org/biomodels.kisao/KISAO_0000354]. In the Krylov case, the user can (optionally) supply a right preconditioner.",
        ("FKINSOL", "NKSOL", "Newton-Krylov solver for nonlinear algebraic systems"),
        False,
    ),
    (
        "KISAO_0000283",
        ("KISAO_0000283", "IDA"),
        "IDA",
        "IDA solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0. At each step, a Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408] leads to linear systems Jx=b, which are solved by one of five methods - two direct (dense or band; serial version only) and three Krylov [http://identifiers.org/biomodels.kisao/KISAO_0000354] (GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000353], BiCGStab [http://identifiers.org/biomodels.kisao/KISAO_0000392], or TFQMR [http://identifiers.org/biomodels.kisao/KISAO_0000396]). IDA is written in C, but derived from the package DASPK [http://identifiers.org/biomodels.kisao/KISAO_0000355] which is written in Fortran.",
        (
            "implicit differential-algebraic solver",
            "solver for differential-algebraic equation systems",
        ),
        False,
    ),
    (
        "KISAO_0000285",
        ("KISAO_0000285", "FINITE_VOLUME_METHOD"),
        "finite volume method",
        "The finite volume method is a method for representing and evaluating partial differential equations in the form of algebraic equations, which attempts to emulate continuous conservation laws of physics.",
        ("FVM",),
        False,
    ),
    (
        "KISAO_0000286",
        ("KISAO_0000286", "EULER_MARUYAMA_METHOD"),
        "Euler-Maruyama method",
        "The Euler-Maruyama method is a method for the approximate numerical solution of a stochastic differential equation, which truncates the Ito and Stratonovich Taylor series of the exact solution after the first order stochastic terms. This converges to the Ito solution with strong global order accuracy 1/2 or weak global order accuracy 1. It is a simple generalization of the Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261] for ordinary differential equations to stochastic differential equations.",
        ("stochastic Euler scheme",),
        False,
    ),
    (
        "KISAO_0000287",
        ("KISAO_0000287", "MILSTEIN_METHOD"),
        "Milstein method",
        "The Milstein method is a technique for the approximate numerical solution of a stochastic differential equation.",
        (),
        False,
    ),
    (
        "KISAO_0000288",
        ("KISAO_0000288", "BACKWARD_DIFFERENTIATION_FORMULA"),
        "backward differentiation formula",
        "The backward differentiation formulas (BDF) are implicit multistep methods based on the numerical differentiation of a given function and are wildly used for integration of stiff differential equations.",
        ("BDF", "Gear method", "Gear's method"),
        False,
    ),
    (
        "KISAO_0000289",
        ("KISAO_0000289", "ADAMS_METHOD"),
        "Adams method",
        "Adams' methods are multi-step methods used for the numerical integration of initial value problems in Ordinary Differential Equations (ODE's). Adams' algorithm consists of two parts: firstly, a starting procedure which provides y1, ... , yk-1 ( approximations to the exact solution at the points x0 + h, ... , x0 + (k - 1)h ) and, secondly, a multistep formula to obtain an approximation to the exact solution y(x0 + kh). This is then applied recursively, based on the numerical approximation of k successive steps, to compute y(x0 + (k + 1)h).",
        (),
        False,
    ),
    (
        "KISAO_0000290",
        ("KISAO_0000290", "MERSON_METHOD"),
        "Merson method",
        "A five-stage Runge-Kutta method with fourth-order accuracy.",
        ("KM", "Kutta-Merson method", "Merson's method", "Runge-Kutta-Merson method"),
        False,
    ),
    (
        "KISAO_0000296",
        ("KISAO_0000296", "HAMMER_HOLLINGSWORTH_METHOD"),
        "Hammer-Hollingsworth method",
        "The numerical integration of ordinary differential equations by the use of Gaussian quadrature methods.",
        (),
        False,
    ),
    (
        "KISAO_0000297",
        ("KISAO_0000297", "LOBATTO_METHOD"),
        "Lobatto method",
        "There are three families of Lobatto methods, called IIIA, IIIB and IIIC. These are named after Rehuel Lobatto. All are implicit Runge-Kutta methods, have order 2s − 2 and they all have c1 = 0 and cs = 1.",
        ("implicit Runge-Kutta method based on Lobatto quadrature",),
        False,
    ),
    (
        "KISAO_0000299",
        ("KISAO_0000299", "BUTCHER_KUNTZMANN_METHOD"),
        "Butcher-Kuntzmann method",
        "From a theoretical point of view, the Butcher-Kuntzmann Runge-Kutta methods belong to the best step-by-step methods for nonstiff problems. These methods integrate first-order initial-value problems by means of formulas based on Gauss-Legendre quadrature, and combine excellent stability features with the property of superconvergence at the step points.",
        ("Gauss method",),
        False,
    ),
    (
        "KISAO_0000301",
        ("KISAO_0000301", "HEUN_METHOD"),
        "Heun method",
        "The method is named after Karl L. W. M. Heun and is a numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It can be seen as extension of the Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261] into two-stage second-order Runge-Kutta method.",
        ("Heun's method",),
        False,
    ),
    (
        "KISAO_0000302",
        ("KISAO_0000302", "EMBEDDED_RUNGE_KUTTA_METHOD"),
        "embedded Runge-Kutta method",
        "An embedded Runge-Kutta method is a method in which two Runge-Kutta estimates are obtained using the same auxiliary functions ki but with a different linear combination of these functions so that one estimate has an order one greater than the other.",
        ("embedded RK",),
        False,
    ),
    (
        "KISAO_0000303",
        ("KISAO_0000303", "ZONNEVELD_METHOD"),
        "Zonneveld method",
        "An embedded Runge-Kutta method [http://identifiers.org/biomodels.kisao/KISAO_0000302] of order 4(3), proposed by J.A. Zonneveld in 1964.",
        (),
        False,
    ),
    (
        "KISAO_0000304",
        ("KISAO_0000304", "RADAU_METHOD"),
        "Radau method",
        "Implicit Runge-Kutta methods based on Radau quadrature.",
        ("implicit Runge-Kutta method based on Radau quadrature",),
        False,
    ),
    (
        "KISAO_0000305",
        ("KISAO_0000305", "VERNER_METHOD"),
        "Verner method",
        "The first high order (6(5)) embedded Runge-Kutta formulas that avoid the drawback of giving identically zero error estimates for quadrature problems y' = f(x) were constructed by Verner in 1978.",
        ("Verner's method",),
        False,
    ),
    (
        "KISAO_0000306",
        ("KISAO_0000306", "LAGRANGIAN_SLIDING_FLUID_ELEMENT_ALGORITHM"),
        "Lagrangian sliding fluid element algorithm",
        "Because the analytic solutions to the partial differential equations require convolution integration, solutions are obtained relatively efficiently by a fast numerical method. Our approach centers on the use of a sliding fluid element algorithm for capillary convection, with the time step set equal to the length step divided by the fluid velocity. Radial fluxes by permeation between plasma, interstitial fluid, and cells and axial diffusion exchanges within each time step are calculated analytically. The method enforces mass conservation unless there is regional consumption.",
        ("BTEX", "LSFEA", "blood-tissue exchange method"),
        False,
    ),
    (
        "KISAO_0000307",
        ("KISAO_0000307", "FINITE_DIFFERENCE_METHOD"),
        "finite difference method",
        "The finite difference method is based on local approximations of the partial derivatives in a Partial Differential Equation, which are derived by low order Taylor series expansions.",
        ("FDM",),
        False,
    ),
    (
        "KISAO_0000308",
        ("KISAO_0000308", "MACCORMACK_METHOD"),
        "MacCormack method",
        "In computational fluid dynamics, the MacCormack method is a widely used discretization scheme for the numerical solution of hyperbolic partial differential equations. This second-order finite difference method [http://identifiers.org/biomodels.kisao/KISAO_0000307] is introduced by R. W. MacCormack in 1969.",
        (),
        False,
    ),
    (
        "KISAO_0000309",
        ("KISAO_0000309", "CRANK_NICOLSON_METHOD"),
        "Crank-Nicolson method",
        "In numerical analysis, the Crank-Nicolson method is a finite difference method [http://identifiers.org/biomodels.kisao/KISAO_0000307] used for numerically solving the heat equation and similar partial differential equations. It is a second-order method in time, implicit in time, and is numerically stable. The method was developed by John Crank and Phyllis Nicolson in the mid 20th century.",
        (),
        False,
    ),
    (
        "KISAO_0000310",
        ("KISAO_0000310", "METHOD_OF_LINES"),
        "method of lines",
        "The method of lines is a general technique for solving partial differential equations (PDEs) by typically using finite difference relationships for the spatial derivatives and ordinary differential equations for the time derivative.",
        ("MOL", "NMOL", "NUMOL"),
        False,
    ),
    (
        "KISAO_0000311",
        ("KISAO_0000311", "TYPE_OF_DOMAIN_GEOMETRY_HANDLING"),
        "type of domain geometry handling",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000314",
        ("KISAO_0000314", "S_SYSTEM_POWER_LAW_CANONICAL_DIFFERENTIAL_EQUATIONS_SOLVER"),
        "S-System power-law canonical differential equations solver",
        "Ordinary differential equations can be recast into a nonlinear canonical form called an S-system. Evidence for the generality of this class comes from extensive empirical examples that have been recast and from the discovery that sets of differential equations and functions, recognized as among the most general, are special cases of S-systems. Identification of this nonlinear canonical form suggests a radically different approach to numerical solution of ordinary differential equations. By capitalizing on the regular structure of S-systems, efficient formulas for a variable-order, variable-step Taylor-series method are developed.",
        ("ESSYNS GMA",),
        False,
    ),
    (
        "KISAO_0000315",
        ("KISAO_0000315", "LATTICE_GAS_AUTOMATA"),
        "lattice gas automata",
        "Lattice gas automata methods are a series of cellular automata methods used to simulate fluid flows. From the LGCA, it is possible to derive the macroscopic Navier-Stokes equations.",
        ("LGA", "LGCA", "lattice gas cellular automata"),
        False,
    ),
    (
        "KISAO_0000316",
        ("KISAO_0000316", "ENHANCED_GREENS_FUNCTION_REACTION_DYNAMICS"),
        "enhanced Greens function reaction dynamics",
        "GFRD [http://identifiers.org/biomodels.kisao/KISAO_0000058] decomposes the multi\xadbody reaction diffusion problem to a set of single and two body problems. Analytical solutions for two body reaction diffusion are available via Smoluchowski equation. eGFRD allows to solve each sub\xadproblem asynchronously by introducing the concept of first passage processes.",
        ("eGFRD",),
        False,
    ),
    (
        "KISAO_0000317",
        ("KISAO_0000317", "E_CELL_MULTI_ALGORITHM_SIMULATION_METHOD"),
        "E-Cell multi-algorithm simulation method",
        "A modular meta-algorithm with a discrete event scheduler that can incorporate any type of time-driven simulation algorithm. It was shown that this meta-algorithm can efficiently drive simulation models with different simulation algorithms with little intrusive modification to the algorithms themselves. Only a few additional methods to handle communications between computational modules are required.",
        (),
        False,
    ),
    (
        "KISAO_0000318",
        ("KISAO_0000318", "GAUSS_LEGENDRE_RUNGE_KUTTA_METHOD"),
        "Gauss-Legendre Runge-Kutta method",
        "So called 'Open Formula', two points formula, three points formula, four points formula, five points formula and six points formula of the Runge-Kutta method to solve the initial value problem of the ordinary differential equation. These formulas use the points and weights from the Gauss-Legendre Quadrature formulas for finding the value of the definite integral.",
        ("Open Formula",),
        False,
    ),
    (
        "KISAO_0000319",
        ("KISAO_0000319", "MONTE_CARLO_METHOD"),
        "Monte Carlo method",
        "Monte Carlo methods (or Monte Carlo experiments) are a class of computational algorithms that rely on repeated random sampling to compute their results.",
        ("MC",),
        False,
    ),
    (
        "KISAO_0000320",
        ("KISAO_0000320", "BIORICA_HYBRID_METHOD"),
        "BioRica hybrid method",
        "The simulation schema for a given BioRica node is given by a hybrid algorithm that deals with continuous time and allows for discrete events that roll back the time according to these discrete interruptions.",
        (),
        False,
    ),
    (
        "KISAO_0000321",
        ("KISAO_0000321", "CASH_KARP_METHOD"),
        "Cash-Karp method",
        "An family of explicit Runge-Kutta formulas, which are very efficient for problems with smooth solution as well as problems having rapidly varying solutions. Each member of this family consists of a fifty-order formula that contains embedded formulas of all orders 1 through 4. By computing solutions at several different orders, it is possible to detect sharp fronts or discontinuities before all the function evaluations defining the full Runge-Kutta step have been computed.",
        (),
        False,
    ),
    (
        "KISAO_0000322",
        ("KISAO_0000322", "HYBRIDITY"),
        "hybridity",
        "The basic idea of hybrid simulation methods is to combine the advantages of complementary simulation approaches: the whole system is subdivided into appropriate parts and different simulation methods operate on these parts at the same time.",
        (),
        False,
    ),
    (
        "KISAO_0000323",
        ("KISAO_0000323", "EQUATION_FREE_PROBABILISTIC_STEADY_STATE_APPROXIMATION"),
        "equation-free probabilistic steady-state approximation",
        "We present a probabilistic steady-state approximation that separates the time scales of an arbitrary reaction network, detects the convergence of a marginal distribution to a quasi-steady-state, directly samples the underlying distribution, and uses those samples to accurately predict the state of the system, including the effects of the slow dynamics, at future times. The numerical method produces an accurate solution of both the fast and slow reaction dynamics while, for stiff systems, reducing the computational time by orders of magnitude. The developed theory makes no approximations on the shape or form of the underlying steady-state distribution and only assumes that it is ergodic. <...> The developed theory may be applied to any type of kinetic Monte Carlo simulation to more efficiently simulate dynamically stiff systems, including existing exact, approximate, or hybrid stochastic simulation techniques.",
        (),
        False,
    ),
    (
        "KISAO_0000324",
        ("KISAO_0000324", "NESTED_STOCHASTIC_SIMULATION_ALGORITHM"),
        "nested stochastic simulation algorithm",
        "This multiscale method is a small modification of the Gillespie's direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029], in the form of a nested SSA, with inner loops for the fast reactions, and outer loop for the slow reactions. The number of groups can be more than two, and the grouping into fast and slow variables can be done dynamically in an adaptive version of the scheme.",
        ("nested SSA",),
        False,
    ),
    (
        "KISAO_0000325",
        ("KISAO_0000325", "MINIMUM_FAST_DISCRETE_REACTION_OCCURRENCES_NUMBER"),
        "minimum fast/discrete reaction occurrences number",
        "Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which describes the minimum number of fast/discrete reaction occurrences before their effects cause convergence to a quasi-steady-state distribution.",
        (),
        False,
    ),
    (
        "KISAO_0000326",
        ("KISAO_0000326", "NUMBER_OF_SAMPLES"),
        "number of samples",
        "Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which determines the number of samples taken from the distribution.",
        (),
        False,
    ),
    (
        "KISAO_0000327",
        ("KISAO_0000327", "MAXIMUM_DISCRETE_NUMBER"),
        "maximum discrete number",
        "Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which controls the maximum number of molecules of some reactant species in order for the reaction to be considered discrete.",
        (),
        False,
    ),
    (
        "KISAO_0000328",
        ("KISAO_0000328", "MINIMUM_FAST_RATE"),
        "minimum fast rate",
        "Parameter of 'equation-free probabilistic steady-state approximation' method [http://identifiers.org/biomodels.kisao/KISAO_0000323], which controls the minimum rate of the reaction in order for it to be considered fast.",
        (),
        False,
    ),
    (
        "KISAO_0000329",
        ("KISAO_0000329", "CONSTANT_TIME_KINETIC_MONTE_CARLO_ALGORITHM"),
        "constant-time kinetic Monte Carlo algorithm",
        "The computational cost of the original SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] scaled linearly with the number of reactions in the network. Gibson and Bruck developed a logarithmic scaling version of the SSA which uses a priority queue or binary tree for more efficient reaction selection [http://identifiers.org/biomodels.kisao/KISAO_0000027]. More generally, this problem is one of dynamic discrete random variate generation which finds many uses in kinetic Monte Carlo and discrete event simulation. We present here a constant-time algorithm, whose cost is independent of the number of reactions, enabled by a slightly more complex underlying data structure.",
        ("SSA-CR",),
        False,
    ),
    (
        "KISAO_0000330",
        ("KISAO_0000330", "R_LEAPING_ALGORITHM"),
        "R-leaping algorithm",
        "A novel algorithm is proposed for the acceleration of the exact stochastic simulation algorithm by a predefined number of reaction firings (R-leaping) that may occur across several reaction channels. In the present approach, the numbers of reaction firings are correlated binomial distributions and the sampling procedure is independent of any permutation of the reaction channels. This enables the algorithm to efficiently handle large systems with disparate rates, providing substantial computational savings in certain cases.",
        ("R-leap method",),
        False,
    ),
    (
        "KISAO_0000331",
        ("KISAO_0000331", "EXACT_R_LEAPING_ALGORITHM"),
        "exact R-leaping algorithm",
        "We present a SSA which, similar to R-leap [http://identifiers.org/biomodels.kisao/KISAO_0000330], accelerates SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] by executing multiple reactions per algorithmic step, but which samples the reactant trajectories from the same probability distribution as the SSA. This 'exact R-leap' or 'ER-leap' algorithm is a modification of the R-leap algorithm which is both exact and capable of substantial speed-up over SSA.",
        (
            "ER-leap method",
            "exact R-leap method",
            "exact accelerated stochastic simulation algorithm",
        ),
        False,
    ),
    (
        "KISAO_0000332",
        ("KISAO_0000332", "ER_LEAP_INITIAL_LEAP"),
        "ER-leap initial leap",
        "L (initial step) is a parameter of 'exact R-leaping method' [http://identifiers.org/biomodels.kisao/KISAO_0000331]. ''We will assume that the reaction event to be bounded occurs within a run of L events in the SSA algorithm[http://identifiers.org/biomodels.kisao/KISAO_0000029], in order to execute L reactions at once in the manner of the R-leap algorithm[http://identifiers.org/biomodels.kisao/KISAO_0000230]''.",
        ("L",),
        False,
    ),
    (
        "KISAO_0000333",
        ("KISAO_0000333", "ACCELERATED_STOCHASTIC_SIMULATION_ALGORITHM"),
        "accelerated stochastic simulation algorithm",
        "An algorithm, which accelerates SSA [http://identifiers.org/biomodels.kisao/KISAO_0000029] either at the expense of its accuracy or exact.",
        ("accelerated SSA",),
        False,
    ),
    (
        "KISAO_0000334",
        ("KISAO_0000334", "MULTIPARTICLE_LATTICE_GAS_AUTOMATA"),
        "multiparticle lattice gas automata",
        "An algorithm which allows for an arbitrary number of particles, while keeping the benefits of the cellular automata approach [http://identifiers.org/biomodels.kisao/KISAO_0000315].",
        ("multiparticle lattice gas cellular automata",),
        False,
    ),
    (
        "KISAO_0000335",
        ("KISAO_0000335", "GENERALIZED_STOCHASTIC_SIMULATION_ALGORITHM"),
        "generalized stochastic simulation algorithm",
        "Gillespie direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029] follows unit-by-unit changes in the total numbers of each reactant species, it is especially well suited to the study of systems in which reactant densities are low and the application of methods based on continuum approximations, such as the traditional ordinary differential equations of chemical kinetics, is questionable. The 'generalized stochastic simulation algorithm' branch presents methods, which extend Gillespie direct method [http://identifiers.org/biomodels.kisao/KISAO_0000029] to suit to systems with other characteristics.",
        (),
        False,
    ),
    (
        "KISAO_0000336",
        ("KISAO_0000336", "D_LEAPING_METHOD"),
        "D-leaping method",
        "We propose a novel, accelerated algorithm for the approximate stochastic simulation of biochemical systems with delays. The present work extends existing accelerated algorithms by distributing, in a time adaptive fashion, the delayed reactions so as to minimize the computational effort while preserving their accuracy.",
        (),
        False,
    ),
    (
        "KISAO_0000337",
        ("KISAO_0000337", "FINITE_ELEMENT_METHOD"),
        "finite element method",
        "A numerical technique for finding approximate solutions of partial differential equations (PDE) as well as of integral equations. The solution approach is based either on eliminating the differential equation completely (steady state problems), or rendering the PDE into an approximating system of ordinary differential equations, which are then numerically integrated using standard techniques such as Euler method [http://identifiers.org/biomodels.kisao/KISAO_0000261], Runge-Kutta [http://identifiers.org/biomodels.kisao/KISAO_0000064], etc.",
        ("FEA", "FEM", "finite element analysis"),
        False,
    ),
    (
        "KISAO_0000338",
        ("KISAO_0000338", "H_VERSION_OF_THE_FINITE_ELEMENT_METHOD"),
        "h-version of the finite element method",
        "Classical form of the 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337], in which polynomials of fixed degree p are used and the mesh is refined to increase accuracy. Can be considered as a special case of the h-p version [http://identifiers.org/biomodels.kisao/KISAO_0000340].",
        ("h-FEM", "h-method"),
        False,
    ),
    (
        "KISAO_0000339",
        ("KISAO_0000339", "P_VERSION_OF_THE_FINITE_ELEMENT_METHOD"),
        "p-version of the finite element method",
        "The p version of 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] uses a fixed mesh but increases the polynomial degree p to increase accuracy. Can be considered as a special case of the h-p version [http://identifiers.org/biomodels.kisao/KISAO_0000340].",
        ("p-FEM", "p-method"),
        False,
    ),
    (
        "KISAO_0000340",
        ("KISAO_0000340", "H_P_VERSION_OF_THE_FINITE_ELEMENT_METHOD"),
        "h-p version of the finite element method",
        "In h-p version of 'finite difference method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] the two approaches of mesh refinement and degree enchacement are combined.",
        ("hp-FEM", "hp-method"),
        False,
    ),
    (
        "KISAO_0000341",
        ("KISAO_0000341", "MIXED_FINITE_ELEMENT_METHOD"),
        "mixed finite element method",
        "A 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] in which both stress and displacement fields are approximated as primary variables.",
        (),
        False,
    ),
    (
        "KISAO_0000342",
        ("KISAO_0000342", "LEVEL_SET_METHOD"),
        "level set method",
        "An algorithm for moving surfaces under their curvature. This algorithm rely on numerically solving Hamilton-Jacobi equations with viscous terms, using approximation techniques from hyperbolic conservation laws.",
        ("LSM", "level-set method"),
        False,
    ),
    (
        "KISAO_0000343",
        ("KISAO_0000343", "GENERALIZED_FINITE_ELEMENT_METHOD"),
        "generalized finite element method",
        "The GFEM is a generalization of the classical 'finite element method' [http://identifiers.org/biomodels.kisao/KISAO_0000337] — in its h [http://identifiers.org/biomodels.kisao/KISAO_0000338], p [http://identifiers.org/biomodels.kisao/KISAO_0000339], and h-p versions [http://identifiers.org/biomodels.kisao/KISAO_0000340]— as well as of the various forms of meshless methods used in engineering.",
        ("GFEM", "PUM", "partition of unity method"),
        False,
    ),
    (
        "KISAO_0000345",
        ("KISAO_0000345", "H_P_CLOUD_METHOD"),
        "h-p cloud method",
        "A meshless method, which uses a partition of unity to construct the family of h-p cloud functions.",
        ("h-p clouds", "method of clouds"),
        False,
    ),
    (
        "KISAO_0000346",
        ("KISAO_0000346", "MESH_BASED_GEOMETRY_HANDLING"),
        "mesh-based geometry handling",
        "In most large-scale numerical simulations of physical phenomena, a large percentage of the overall computational effort is expended on technical details connected with meshing. These details include, in particular, grid generation, mesh adaptation to domain geometry, element or cell connectivity, grid motion and separation to model fracture, fragmentation, free surfaces, etc.",
        (),
        False,
    ),
    (
        "KISAO_0000347",
        ("KISAO_0000347", "MESHLESS_GEOMETRY_HANDLING"),
        "meshless geometry handling",
        "Most meshless methods require a scattered set of nodal points in the domain of interest. In these methods, there may be no fixed connectivities between the nodes, unlike the finite element or finite difference methods. This feature has significant implications in modeling some physical phenomena that are characterized by a continuous change in the geometry of the domain under analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000348",
        ("KISAO_0000348", "EXTENDED_FINITE_ELEMENT_METHOD"),
        "extended finite element method",
        "A numerical method to model arbitrary discontinuities in continuous bodies that does not require the mesh to conform to the discontinuities nor significant mesh refinement near singularities. In X-FEM the standard finite element approximation [http://identifiers.org/biomodels.kisao/KISAO_0000337] is enriched and the approximation space is extended by an additional family of functions.",
        ("X-FEM", "XFEM"),
        False,
    ),
    (
        "KISAO_0000349",
        ("KISAO_0000349", "METHOD_OF_FINITE_SPHERES"),
        "method of finite spheres",
        "Method of finite spheres is truly meshless in the sense that the nodes are placed and the numerical integration is performed without a mesh. Some of the novel features of the method of finite spheres are the numerical integration scheme and the way in which the Dirichlet boundary conditions are incorporated.",
        ("MFS",),
        False,
    ),
    (
        "KISAO_0000350",
        ("KISAO_0000350", "PROBABILITY_WEIGHTED_DYNAMIC_MONTE_CARLO_METHOD"),
        "probability-weighted dynamic Monte Carlo method",
        "We have developed a probability-weighted DMC method by incorporating the weighted sampling algorithm of equilibrium molecular simulations. This new algorithm samples the slow reactions very efficiently and makes it possible to simulate in a computationally efficient manner the reaction kinetics of physical systems in which the rates of reactions vary by several orders of magnitude.",
        ("PW-DMC", "probability-weighted DMC"),
        False,
    ),
    (
        "KISAO_0000351",
        ("KISAO_0000351", "MULTINOMIAL_TAU_LEAPING_METHOD"),
        "multinomial tau-leaping method",
        "The multinomial tau-leaping method is an extension of the binomial tau-leaping method [http://identifiers.org/biomodels.kisao/KISAO_0000074] to networks with arbitrary multiple-channel reactant dependencies. Improvements were achieved by a combination of three factors: First, tau-leaping steps are determined simply and efficiently using a-priori information and Poisson distribution based estimates of expectation values for reaction numbers. Second, networks are partitioned into closed groups of reactions and corresponding reactants in which no group reactant set is found in any other group. Third, product formation is factored into upper bound estimation of the number of times a particular reaction occurs.",
        ("MtauL",),
        False,
    ),
    (
        "KISAO_0000352",
        ("KISAO_0000352", "HYBRID_METHOD"),
        "hybrid method",
        "A simulation methods which combines the advantages of complementary simulation approaches: the whole system is subdivided into appropriate parts and different simulation methods operate on these parts at the same time.",
        (),
        False,
    ),
    (
        "KISAO_0000353",
        ("KISAO_0000353", "GENERALIZED_MINIMAL_RESIDUAL_ALGORITHM"),
        "generalized minimal residual algorithm",
        "An iterative method for solving linear systems, which has the property of minimizing at every step the norm of the residual vector over a Krylov subspace. The generalized minimal residual method extends the minimal residual method (MINRES) [http://identifiers.org/biomodels.kisao/KISAO_0000388], which is only applicable to symmetric systems, to non-symmetric systems.",
        ("GMRES",),
        False,
    ),
    (
        "KISAO_0000354",
        ("KISAO_0000354", "KRYLOV_SUBSPACE_PROJECTION_METHOD"),
        "Krylov subspace projection method",
        "Krylov subspace method is an iterative linear equation method, which builds up Krylov subspaces and look for good approximations to eigenvectors and invariant subspaces within the Krylov spaces.",
        ("Krylov subspace method",),
        False,
    ),
    (
        "KISAO_0000355",
        ("KISAO_0000355", "DASPK"),
        "DASPK",
        "In DASPK, we have combined the time-stepping methods of DASSL [http://identifiers.org/biomodels.kisao/KISAO_0000255] with preconditioned iterative method GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000386], for solving large-scale systems of DAEs of the form F(t, y, y') = 0, where F, y, y' are N-dimensional vectors, and a consistent set of initial conditions y(t0) = y0, y'(t0) = y'0 is given. DASPK is written in Fortran.",
        (
            "DDASPK",
            "SDASPK",
            "differential algebraic system solver with Krylov preconditioning",
        ),
        False,
    ),
    (
        "KISAO_0000356",
        ("KISAO_0000356", "DASSL"),
        "DASSL",
        "DASSL is designed for the numerical solution of implicit systems of differential/algebraic equations written in the form F(t,y,y')=0, where F, y, and y' are vectors, and initial values for y and y' are given.",
        ("DDASSL", "SDASSL", "differential algebraic system solver"),
        False,
    ),
    (
        "KISAO_0000357",
        ("KISAO_0000357", "CONJUGATE_GRADIENT_METHOD"),
        "conjugate gradient method",
        "Conjugate gradient method is an algorithm for the numerical solution of particular systems of linear equations, namely those whose matrix is symmetric and positive-definite. The conjugate gradient method is an iterative method, so it can be applied to sparse systems that are too large to be handled by direct methods. Such systems often arise when numerically solving partial differential equations.",
        ("CG",),
        False,
    ),
    (
        "KISAO_0000358",
        ("KISAO_0000358", "BICONJUGATE_GRADIENT_METHOD"),
        "biconjugate gradient method",
        "The biconjugate gradient method provides a generalization of conjugate gradient method [http://identifiers.org/biomodels.kisao/KISAO_0000357] to non-symmetric matrices.",
        ("BCG", "Bi-CG", "BiCG"),
        False,
    ),
    (
        "KISAO_0000359",
        ("KISAO_0000359", "IS_SIMILAR_TO"),
        "is similar to",
        None,
        (),
        False,
    ),
    ("KISAO_0000360", ("KISAO_0000360", "USES"), "uses", None, (), False),
    (
        "KISAO_0000361",
        ("KISAO_0000361", "IS_GENERALIZATION_OF"),
        "is generalization of",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000362",
        ("KISAO_0000362", "IMPLICIT_STATE_DOOB_GILLESPIE_ALGORITHM"),
        "implicit-state Doob-Gillespie algorithm",
        "The algorithm uses a representation of the system together with a super-approximation of its ‘event horizon’ (all events that may happen next), and a specific correction scheme to obtain exact timings. Being completely local and not based on any kind of enumeration, this algorithm has a per event time cost which is independent of (i) the size of the set of generable species (which can even be infinite), and (ii) independent of the size of the system (ie, the number of agent instances). The algorithm can be refined, using concepts derived from the classical notion of causality, so that in addition to the above one also has that the even cost is depending (iii) only logarithmically on the size of the model (ie, the number of rules).",
        (),
        False,
    ),
    (
        "KISAO_0000363",
        ("KISAO_0000363", "RULE_BASED_SIMULATION_METHOD"),
        "rule-based simulation method",
        "Rule-based models provide a powerful alternative to approaches that require explicit enumeration of all possible molecular species of a system. Such models consist of formal rules governing interactive behaviour. Rule-based simulation methods simulate such models.",
        (),
        False,
    ),
    (
        "KISAO_0000364",
        ("KISAO_0000364", "ADAMS_PREDICTOR_CORRECTOR_METHOD"),
        "Adams predictor-corrector method",
        "The combination of evaluating a single explicit integration method ('Adams-Bashforth method' [http://identifiers.org/biomodels.kisao/KISAO_0000279]) (the predictor step) in order to provide a good initial guess for the successive evaluation of an implicit method ('Adams-Moulton method' [http://identifiers.org/biomodels.kisao/KISAO_0000280]) (the corrector step) using iteration.",
        (),
        False,
    ),
    (
        "KISAO_0000365",
        ("KISAO_0000365", "NDSOLVE_METHOD"),
        "NDSolve method",
        "The Mathematica computation system function NDSolve is a general numerical differential equation solver. It can handle a wide range of ordinary differential equations as well as some partial differential equations. NDSolve can also solve some differential-algebraic equations, which are typically a mix of differential and algebraic equations.",
        (),
        False,
    ),
    (
        "KISAO_0000366",
        ("KISAO_0000366", "SYMPLECTICNESS"),
        "symplecticness",
        "Roughly speaking, ‘symplecticness’ is a characteristic property possessed by the solutions of Hamiltonian problems. A numerical method is called symplectic if, when applied to Hamiltonian problems, it generates numerical solutions which inherit the property of symplecticness (phase volume preservation).",
        (),
        False,
    ),
    (
        "KISAO_0000367",
        ("KISAO_0000367", "PARTITIONED_RUNGE_KUTTA_METHOD"),
        "partitioned Runge-Kutta method",
        "If a Hamiltonian system possesses a natural partitioning, it is possible to integrate its certain components using one Runge-Kutta method and other components using a different Runge-Kutta method. The overall s-stage scheme is called a partitioned Runge-Kutta method.",
        ("PRK", "SPRK", "symplectic partitioned Runge-Kutta method"),
        False,
    ),
    (
        "KISAO_0000369",
        ("KISAO_0000369", "PARTIAL_DIFFERENTIAL_EQUATION_DISCRETIZATION_METHOD"),
        "partial differential equation discretization method",
        "A method which solves partial differential equations by discretizing them, i.e. approximating them by equations that involve a finite number of unknowns.",
        (),
        False,
    ),
    (
        "KISAO_0000370",
        ("KISAO_0000370", "TYPE_OF_PROBLEM"),
        "type of problem",
        "A characteristic describing the type of the problems which can be solved by the algorithm.",
        (),
        False,
    ),
    (
        "KISAO_0000371",
        ("KISAO_0000371", "STOCHASTIC_DIFFERENTIAL_EQUATION_PROBLEM"),
        "stochastic differential equation problem",
        None,
        ("SDE problem",),
        False,
    ),
    (
        "KISAO_0000372",
        ("KISAO_0000372", "PARTIAL_DIFFERENTIAL_EQUATION_PROBLEM"),
        "partial differential equation problem",
        None,
        ("PDE problem",),
        False,
    ),
    (
        "KISAO_0000373",
        ("KISAO_0000373", "DIFFERENTIAL_ALGEBRAIC_EQUATION_PROBLEM"),
        "differential-algebraic equation problem",
        None,
        ("DAE",),
        False,
    ),
    (
        "KISAO_0000374",
        ("KISAO_0000374", "ORDINARY_DIFFERENTIAL_EQUATION_PROBLEM"),
        "ordinary differential equation problem",
        None,
        ("ODE problem",),
        False,
    ),
    (
        "KISAO_0000375",
        ("KISAO_0000375", "DELAY_DIFFERENTIAL_EQUATION_PROBLEM"),
        "delay differential equation problem",
        None,
        ("DDE problem",),
        False,
    ),
    (
        "KISAO_0000376",
        ("KISAO_0000376", "LINEARITY_OF_EQUATION"),
        "linearity of equation",
        "Linear differential equations are of the form Ly = f, where the differential operator L is a linear operator, y is the unknown function, and the right hand side f is a given function of the same nature as y.",
        (),
        False,
    ),
    (
        "KISAO_0000377",
        ("KISAO_0000377", "ONE_STEP_METHOD"),
        "one-step method",
        "A numerical method for differential equations which uses one starting value at each step.",
        (),
        False,
    ),
    (
        "KISAO_0000378",
        ("KISAO_0000378", "IMPLICIT_MIDPOINT_RULE"),
        "implicit midpoint rule",
        "The implicit midpoint rule is a second-order case of the more general implicit s-stage Runge-Kutta methods [http://identifiers.org/biomodels.kisao/KISAO_0000064 and (http://identifiers.org/biomodels.kisao/KISAO_0000245 some http://identifiers.org/biomodels.kisao/KISAO_0000240)].",
        ("implicit Gaussian second order Runge-Kutta method",),
        False,
    ),
    (
        "KISAO_0000379",
        ("KISAO_0000379", "BULIRSCH_STOER_ALGORITHM"),
        "Bulirsch-Stoer algorithm",
        'The Bulirsch-Stoer method is an adaptive method which uses Gragg\'s modified midpoint method [http://identifiers.org/biomodels.kisao/KISAO_0000382] to estimate the solution of an initial value problem for various step sizes. The estimates are fit to a "diagonal" rational function or a polynomial as a function of the step size and the limit as the step size tends to zero is taken as the final estimate.',
        ("GBS", "Gragg-Bulirsch-Stoer algorithm"),
        False,
    ),
    (
        "KISAO_0000380",
        ("KISAO_0000380", "RICHARDSON_EXTRAPOLATION_BASED_METHOD"),
        "Richardson extrapolation based method",
        "A method based on ideas of Richardson extrapolation, which is a process for obtaining increased accuracy in a discretized approximation by extrapolating results from coarse discretizations to an arbitrarily fine one.",
        (),
        False,
    ),
    (
        "KISAO_0000381",
        ("KISAO_0000381", "MIDPOINT_METHOD"),
        "midpoint method",
        "The midpoint method is an explicit method for approximating the solution of the initial value problem y' = f(x,y); y(x0) = y0 at x for a given step size h. For the midpoint method the derivative of y(x) is approximated by the symmetric difference y'(x) = ( y(x+h) - y(x-h) ) / 2h + O(h2).",
        (),
        False,
    ),
    (
        "KISAO_0000382",
        ("KISAO_0000382", "MODIFIED_MIDPOINT_METHOD"),
        "modified midpoint method",
        "The modified midpoint method is globally a second order method for approximating the solution of the initial value problem y' = f(x, y), y(x0) = y0, which advances a vector of dependent variables y(x) from a point x to a point x + H by a sequence of n substeps each of size h, h = H/n.",
        ("Gragg's method", "Gragg's modified midpoint method"),
        False,
    ),
    (
        "KISAO_0000383",
        ("KISAO_0000383", "BADER_DEUFLHARD_METHOD"),
        "Bader-Deuflhard method",
        "The Bader-Deuflhard method is an extrapolation method based on a semi-implicit discretization [http://identifiers.org/biomodels.kisao/KISAO_0000387]. It is a generalization of the Bulirsch-Stoer algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000379] for solving ordinary differential equations.",
        (),
        False,
    ),
    (
        "KISAO_0000384",
        ("KISAO_0000384", "SEMI_IMPLICIT_MIDPOINT_RULE"),
        "semi-implicit midpoint rule",
        "A semi-implicit version of the midpoint method that has an even error series [http://identifiers.org/biomodels.kisao/KISAO_0000381].",
        (),
        False,
    ),
    (
        "KISAO_0000386",
        ("KISAO_0000386", "SCALED_PRECONDITIONED_GENERALIZED_MINIMAL_RESIDUAL_METHOD"),
        "scaled preconditioned generalized minimal residual method",
        "A scaled preconditioned version of 'generalized minimal residual algorithm' [http://identifiers.org/biomodels.kisao/KISAO_0000353]. For linear system Ax = b a preconditioner matrix P that approximates A is sought, for which linear system Px = b can be solved easily. Preconditioning is applied on the left only. Scaling is done using diagonal matrix D whose diagonal elements are weights w^i = rtol|y^i| +atol^i, where rtol is 'relative tolerance' [http://identifiers.org/biomodels.kisao/KISAO_0000209] and atol is 'absolute tolerance' [http://identifiers.org/biomodels.kisao/KISAO_0000211].",
        ("SPGMR",),
        False,
    ),
    (
        "KISAO_0000388",
        ("KISAO_0000388", "MINIMAL_RESIDUAL_METHOD"),
        "minimal residual method",
        "The 'minimal residual method' is an algorithm for the numerical solution of indefinite symmertic systems of linear equations.",
        ("MINRES",),
        False,
    ),
    (
        "KISAO_0000389",
        ("KISAO_0000389", "QUASI_MINIMAL_RESIDUAL_METHOD"),
        "quasi-minimal residual method",
        "The QMR algorithm is a robust iterative solver for general nonsingular non-Hermitian linear systems. The method uses a robust implementation of the look-ahead Lanczos algorithm to generate basis vectors for the Krylov subspaces Kn(r0, A). The QMR iterates are characterized by a quasi-minimal residual property over Kn(r0, A).",
        ("QMR",),
        False,
    ),
    (
        "KISAO_0000392",
        ("KISAO_0000392", "BICONJUGATE_GRADIENT_STABILIZED_METHOD"),
        "biconjugate gradient stabilized method",
        "An iterative method for the numerical solution of nonsymmetric linear systems. It is a variant of the biconjugate gradient method (BiCG) [http://identifiers.org/biomodels.kisao/KISAO_0000358] and has faster and smoother convergence than the original BiCG.",
        ("Bi-CGSTAB", "BiCGSTAB"),
        False,
    ),
    (
        "KISAO_0000393",
        ("KISAO_0000393", "INGENIOUS_CONJUGATE_GRADIENTS_SQUARED_METHOD"),
        "ingenious conjugate gradients-squared method",
        "A Lanczos-type method for nonsymmetric sparse linear systems. The method is based on a polynomial variant of the conjugate gradients algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000357]. Although related to the so-called bi-conjugate gradients (Bi-CG) algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000358], it does not involve adjoint matrix-vector multiplications, and the expected convergence rate is about twice that of the Bi-CG algorithm.",
        ("CGS",),
        False,
    ),
    (
        "KISAO_0000394",
        (
            "KISAO_0000394",
            "QUASI_MINIMAL_RESIDUAL_VARIANT_OF_BICONJUGATE_GRADIENT_STABILIZED_METHOD",
        ),
        "quasi-minimal residual variant of biconjugate gradient stabilized method",
        "QMRCGSTAB is a quasi-minimal residual (QMR) variant of the Bi-CGSTAB algorithm [http://identifiers.org/biomodels.kisao/KISAO_0000394] of van der Vorst for solving nonsymmetric linear systems. The motivation for the QMR variant is to obtain smoother convergence behavior of the underlying method.",
        ("QMRCGSTAB",),
        False,
    ),
    (
        "KISAO_0000395",
        ("KISAO_0000395", "IMPROVED_BICONJUGATE_GRADIENT_METHOD"),
        "improved biconjugate gradient method",
        "An 'improved biconjugate gradient method' branch contains algorithms which can be viewed as improvements over some of drawbacks of BCG [http://identifiers.org/biomodels.kisao/KISAO_0000358], such as (1) the need for matrix-vector multiplications with A^T (which can be inconvenient as well as doubling the number of matrix-vector multiplications compared to CG [http://identifiers.org/biomodels.kisao/KISAO_0000357] for each increase in the degree of the underlying Krylov subspace), (2) the possibility of breakdowns and (3) erratic convergence behavior.",
        (),
        False,
    ),
    (
        "KISAO_0000396",
        ("KISAO_0000396", "TRANSPOSE_FREE_QUASI_MINIMAL_RESIDUAL_ALGORITHM"),
        "transpose-free quasi-minimal residual algorithm",
        "A version of CGS [http://identifiers.org/biomodels.kisao/KISAO_0000393] which 'quasi-minimizes' the residual in the space spanned by the vectors generated by the CGS iteration.",
        ("TFQMR",),
        False,
    ),
    (
        "KISAO_0000397",
        ("KISAO_0000397", "PRECONDITIONING_TECHNIQUE"),
        "preconditioning technique",
        "Preconditioning is simply a means of transforming the original linear system into one which has the same solution, but which is likely to be easier to solve with an iterative solver.",
        (),
        False,
    ),
    (
        "KISAO_0000398",
        ("KISAO_0000398", "ITERATIVE_METHOD_FOR_SOLVING_A_SYSTEM_OF_LINEAR_EQUATIONS"),
        "iterative method for solving a system of linear equations",
        None,
        (),
        False,
    ),
    ("KISAO_0000399", ("KISAO_0000399", "IS_USED_BY"), "is used by", None, (), False),
    (
        "KISAO_0000403",
        ("KISAO_0000403", "HOMOGENEOUSNESS_OF_EQUATION"),
        "homogeneousness of equation",
        "Homogeneous equations are of the form Ly = 0, where the differential operator L is a linear operator and y is the unknown function.",
        (),
        False,
    ),
    (
        "KISAO_0000404",
        ("KISAO_0000404", "SYMMETRICITY_OF_MATRIX"),
        "symmetricity of matrix",
        "In linear algebra, a symmetric matrix is a square matrix that is equal to its transpose.",
        (),
        False,
    ),
    (
        "KISAO_0000405",
        ("KISAO_0000405", "TYPE_OF_DIFFERENTIAL_EQUATION"),
        "type of differential equation",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000407",
        ("KISAO_0000407", "STEADY_STATE_ROOT_FINDING_METHOD"),
        "steady state root-finding method",
        "Requested by Frank T. Bergmann on Sunday, November 27, 2011 4:45:30 PM.",
        (),
        False,
    ),
    (
        "KISAO_0000408",
        ("KISAO_0000408", "NEWTON_TYPE_METHOD"),
        "Newton-type method",
        "Requested by Frank T. Bergmann on Sunday, November 27, 2011 4:45:30 PM.",
        (),
        False,
    ),
    (
        "KISAO_0000409",
        ("KISAO_0000409", "ORDINARY_NEWTON_METHOD"),
        "ordinary Newton method",
        "A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which solves the general nonlinear problem F(x)=0 by applying successive linearization F'(x[k])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,...",
        (),
        False,
    ),
    (
        "KISAO_0000410",
        ("KISAO_0000410", "SIMPLIFIED_NEWTON_METHOD"),
        "simplified Newton method",
        "A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which is characterized by keeping the initial derivative throughout the whole iteration: F'(x[0])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,...",
        (),
        False,
    ),
    (
        "KISAO_0000411",
        ("KISAO_0000411", "NEWTON_LIKE_METHOD"),
        "Newton-like method",
        "A 'Newton-type method' [http://identifiers.org/biomodels.kisao/KISAO_0000408] which is characterized by the fact that, in finite dimension, the Jacodian matrices are either replaced by some fixed 'close by' Jacobian F'(z) with z not equal to the initial guess x[0], or by some approximation so that: M'(x[0])deltax[k]=-F(x[k]), x[k+1]=x[k]+deltax[k], k=0,1,...",
        (),
        False,
    ),
    (
        "KISAO_0000412",
        ("KISAO_0000412", "INEXACT_NEWTON_METHOD"),
        "inexact Newton method",
        "For extremely large scale nonlinear problems the arising linear systems for the Newton corrections can no longer be solved directly ('exactly'), but must be solved iterativly ('inexactly) - which gives the name inexact Newton methods. The whole scheme then consists of an inner iteration (at Newton step k): F'(x[k])deltaxi[k]=-F(x[k])+ri[k], k=0,1,... xi[k+1]=x[k]+deltaxi[k], i=0,1,..,imax[k] in terms of residuals ri[k] and an outer iteration where, given x[0], the iterates are defined as x[k+1]=xi[k+1] for i=imax[k], k=0,1,...",
        ("iterative Newton method", "truncated Newton method"),
        False,
    ),
    (
        "KISAO_0000413",
        ("KISAO_0000413", "EXACT_NEWTON_METHOD"),
        "exact Newton method",
        "Any of the finite dimensional Newton-type methods [http://identifiers.org/biomodels.kisao/KISAO_0000408] requires the numerical solution of the linear equations F'(x[k])deltax[k]=-F(x[k]). Whenever direct elimination methods are applicable, we speak of exact Newton methods.",
        ("direct Newton method",),
        False,
    ),
    (
        "KISAO_0000415",
        ("KISAO_0000415", "MAXIMUM_NUMBER_OF_STEPS"),
        "maximum number of steps",
        "The limit on number of internal steps before an output point.",
        ("maximum steps",),
        False,
    ),
    (
        "KISAO_0000416",
        ("KISAO_0000416", "PARTIAL_LEAST_SQUARES_REGRESSION_METHOD"),
        "partial least squares regression method",
        "Requested by Kristin Tøndel on Thursday, October 13, 2011 10:46:04 AM.",
        ("PLSR", "PLSR method"),
        False,
    ),
    (
        "KISAO_0000417",
        (
            "KISAO_0000417",
            "HIERARCHICAL_CLUSTER_BASED_PARTIAL_LEAST_SQUARES_REGRESSION_METHOD",
        ),
        "hierarchical cluster-based partial least squares regression method",
        "Requested by Kristin Tøndel on Thursday, October 13, 2011 11:13:17 AM.",
        (
            "HC-PLSR",
            "Multivariate regression method based on separating the observations into clusters and generating Partial Least Squares Regression (PLSR) [http://identifiers.org/biomodels.kisao/KISAO_0000416] models within each cluster. This local regression analysis is suitable for very non-linear systems. PLSR is a regression method based on estimated latent variables, related to Principal Component Analysis (PCA) and Principal Component Regression (PCR).\nHierarchical cluster-based partial least squares regression method uses fuzzy C-means clustering, PLSR and Linear Discriminant Analysis (LDA), Quadratic Discriminant Analysis (QDA) or Naive Bayes for classification of new observations to be predicted.",
        ),
        False,
    ),
    (
        "KISAO_0000418",
        ("KISAO_0000418", "N_WAY_PARTIAL_LEAST_SQUARES_REGRESSION_METHOD"),
        "N-way partial least squares regression method",
        "Requested by Kristin Tøndel on Thursday, October 13, 2011 11:33:06 AM.",
        ("N-PLS", "N-way PLSR", "N-way partial least squares method"),
        False,
    ),
    (
        "KISAO_0000419",
        ("KISAO_0000419", "METAMODELLING_METHOD"),
        "metamodelling method",
        "Deterministic dynamic models of complex biological systems contain a large number of parameters and state variables, related through nonlinear differential equations with various types of feedback. A metamodel of such a dynamic model is a statistical approximation model that maps variation in parameters and initial conditions (inputs) to variation in features of the trajectories of the state variables (outputs) throughout the entire biologically relevant input space.",
        (),
        False,
    ),
    (
        "KISAO_0000420",
        ("KISAO_0000420", "NUMBER_OF_PARTIAL_LEAST_SQUARES_COMPONENTS"),
        "number of partial least squares components",
        "Parameter used by 'partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000416] describing number of PLS components to include in the regression analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000421",
        ("KISAO_0000421", "TYPE_OF_VALIDATION"),
        "type of validation",
        "Parameter of 'partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000416] describing how validation is performed. Possible values include cross-validation and test set validation.",
        (),
        False,
    ),
    (
        "KISAO_0000422",
        ("KISAO_0000422", "NUMBER_OF_N_WAY_PARTIAL_LEAST_SQUARES_REGRESSION_FACTORS"),
        "number of N-way partial least squares regression factors",
        "Parameter of 'N-way partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000369] describing the number of factors to compute.",
        ("number of factors",),
        False,
    ),
    (
        "KISAO_0000423",
        ("KISAO_0000423", "PARTIAL_LEAST_SQUARES_REGRESSION_LIKE_METHOD"),
        "partial least squares regression-like method",
        "Method for building regression models between independent and dependent variables.",
        (),
        False,
    ),
    (
        "KISAO_0000424",
        ("KISAO_0000424", "MEAN_CENTRING_OF_VARIABLES"),
        "mean-centring of variables",
        "A boolean parameter of the 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417] specifying whether the variables were mean-centred prior to the regression analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000425",
        ("KISAO_0000425", "STANDARDISING_OF_VARIABLES"),
        "standardising of variables",
        "A boolean parameter of the 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417] specifying whether the variables were standardised (divided by their standard deviations) prior to the regression analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000427",
        ("KISAO_0000427", "NUMBER_OF_CLUSTERS"),
        "number of clusters",
        "Parameter specifying the number of clusters used by C-means algorithm.",
        (),
        False,
    ),
    (
        "KISAO_0000428",
        ("KISAO_0000428", "MATRIX_FOR_CLUSTERIZATION"),
        "matrix for clusterization",
        "A matrix to do the clustering in 'hierarchical cluster-based partial least squares regression method' [http://identifiers.org/biomodels.kisao/KISAO_0000417].",
        (),
        False,
    ),
    (
        "KISAO_0000429",
        ("KISAO_0000429", "CLUSTERIZATION_PARAMETER"),
        "clusterization parameter",
        "Parameter used by algorithms performing clusterization.",
        (),
        False,
    ),
    (
        "KISAO_0000430",
        ("KISAO_0000430", "VARIABLES_PREPROCESSING_PARAMETER"),
        "variables preprocessing parameter",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000432",
        ("KISAO_0000432", "IDA_LIKE_METHOD"),
        "IDA-like method",
        "Solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0. At each step, a Newton iteration [http://identifiers.org/biomodels.kisao/KISAO_0000408] leads to linear systems Jx=b, which are solved by one of five methods - two direct (dense or band; serial version only) and three Krylov [http://identifiers.org/biomodels.kisao/KISAO_0000354] (GMRES [http://identifiers.org/biomodels.kisao/KISAO_0000353], BiCGStab [http://identifiers.org/biomodels.kisao/KISAO_0000392], or TFQMR [http://identifiers.org/biomodels.kisao/KISAO_0000396]).",
        (),
        False,
    ),
    (
        "KISAO_0000433",
        ("KISAO_0000433", "CVODE_LIKE_METHOD"),
        "CVODE-like method",
        "Solves ODE initial value problems, in real N-space, written as y'=f(t,y), y(t0)=y0. It is capable for stiff and non-stiff systems and uses two different linear multi-step methods, namely the Adam-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] method and the backward differentiation formula [http://identifiers.org/biomodels.kisao/KISAO_0000288].",
        (),
        False,
    ),
    (
        "KISAO_0000434",
        ("KISAO_0000434", "HIGHAM_HALL_METHOD"),
        "Higham-Hall method",
        "The equilibrium theory of Hall and Higham (1988) can be used to determine whether a Runge-Kutta algorithm will perform smoothly when stability restricts the stepsize. Higham-Hall method is a fifth order embedded Runge-Kutta method [http://identifiers.org/biomodels.kisao/KISAO_0000302], which behaves smoothly with respect to the standard type of stepsize controllers.",
        ("RK5(4)7FEql",),
        False,
    ),
    (
        "KISAO_0000435",
        ("KISAO_0000435", "EMBEDDED_RUNGE_KUTTA_5_4__METHOD"),
        "embedded Runge-Kutta 5(4) method",
        "An embedded Runge-Kutta integrator of order 5(4).",
        ("RK5(4)",),
        False,
    ),
    (
        "KISAO_0000436",
        ("KISAO_0000436", "DORMAND_PRINCE_8_5_3__METHOD"),
        "Dormand-Prince 8(5,3) method",
        "This method is based on an 8(6) method by Dormand and Prince (i.e. order 8 for the integration and order 6 for error estimation) modified by Hairer and Wanner to use a 5th order error estimator with 3rd order correction.",
        (),
        False,
    ),
    (
        "KISAO_0000437",
        ("KISAO_0000437", "FLUX_BALANCE_ANALYSIS"),
        "flux balance analysis",
        "Requested by Frank T. Bergmann on Thursday, November 29, 2012 9:51:58 AM.",
        ("FBA",),
        False,
    ),
    (
        "KISAO_0000447",
        ("KISAO_0000447", "COAST"),
        "COAST",
        "Requested by Mark Moeller on Friday, January 25, 2013 11:11:30 AM.",
        ("controllable approximative stochastic reaction algorithm",),
        False,
    ),
    (
        "KISAO_0000448",
        ("KISAO_0000448", "LOGICAL_MODEL_SIMULATION_METHOD"),
        "logical model simulation method",
        "Qualitative (logical) models specify the evolution rules of their components. In each state a number of transitions are enabled. A 'logical model simulation method' guides the choice of the transitions processed at each step.",
        (),
        False,
    ),
    (
        "KISAO_0000449",
        ("KISAO_0000449", "SYNCHRONOUS_LOGICAL_MODEL_SIMULATION_METHOD"),
        "synchronous logical model simulation method",
        "Qualitative (logical) models specify the evolution rules of their components. In the case of a synchronous updating all enabled transitions are processed simultaneously.",
        (),
        False,
    ),
    (
        "KISAO_0000450",
        ("KISAO_0000450", "ASYNCHRONOUS_LOGICAL_MODEL_SIMULATION_METHOD"),
        "asynchronous logical model simulation method",
        "Qualitative (logical) models specify the evolution rules of their components. It the case of an asynchronous updating all enabled transitions are performed independently: a state has as many successors as the number of transitions enabled in this state. An 'asynchronous logical model simulation method' specifies a rule to guide the choice of a unique transition at each step (for example random).",
        (),
        False,
    ),
    (
        "KISAO_0000451",
        ("KISAO_0000451", "TYPE_OF_UPDATING_POLICY"),
        "type of updating policy",
        "A rule to guide the choice of a unique transition at each step used by an 'asynchronous logical model simulation method' [http://identifiers.org/biomodels.kisao/KISAO_0000450].",
        (),
        False,
    ),
    (
        "KISAO_0000452",
        ("KISAO_0000452", "RANDOM_UPDATING_POLICY"),
        "random updating policy",
        "An updating policy that chooses a transition randomly.",
        (),
        False,
    ),
    (
        "KISAO_0000453",
        ("KISAO_0000453", "ORDERED_UPDATING_POLICY"),
        "ordered updating policy",
        "An updating policy that chooses a transition in a definite way.",
        (),
        False,
    ),
    (
        "KISAO_0000454",
        ("KISAO_0000454", "CONSTANT_UPDATING_POLICY"),
        "constant updating policy",
        "An updating policy that chooses a transition in a constant way.",
        (),
        False,
    ),
    (
        "KISAO_0000455",
        ("KISAO_0000455", "PRIORITIZED_UPDATING_POLICY"),
        "prioritized updating policy",
        "An updating policy that chooses a transition in a prioritized way.",
        (),
        False,
    ),
    (
        "KISAO_0000467",
        ("KISAO_0000467", "MAXIMUM_STEP_SIZE"),
        "maximum step size",
        "Requested by Andrew Miller on Tuesday, June 4, 2013 2:33:51 AM.",
        (),
        False,
    ),
    (
        "KISAO_0000468",
        ("KISAO_0000468", "MAXIMAL_TIMESTEP_METHOD"),
        "maximal timestep method",
        "Requested by Andrzej Kierzek on Thursday, April 24, 2014 12:40:35 PM Used to simulate systems involving reactions with propensities varying by many orders of magnitude.",
        (),
        False,
    ),
    (
        "KISAO_0000469",
        ("KISAO_0000469", "MAXIMAL_TIMESTEP"),
        "maximal timestep",
        "Key parameter of the 'maximal timestep method' [http://www.biomodels.net/kisao/KISAO#KISAO_0000468]. If Gillespie [http://www.biomodels.net/kisao/KISAO#KISAO_0000027] waiting time is longer than maximal timestep, slow reaction is not fired and tau-leap [http://www.biomodels.net/kisao/KISAO#KISAO_0000039] step is executed for fast reactions. Otherwise, slow reaction is fired and tau-leap [http://www.biomodels.net/kisao/KISAO#KISAO_0000039] is executed with shorter time step.",
        (),
        False,
    ),
    (
        "KISAO_0000470",
        ("KISAO_0000470", "OPTIMIZATION_ALGORITHM"),
        "optimization algorithm",
        "An optimization algorithm tries to find the minumum or maximum of an arbitrary function. It takes a function of one or several variables and determines the values for the variables so that the function value is optimal.",
        ("optimization method",),
        False,
    ),
    (
        "KISAO_0000471",
        ("KISAO_0000471", "LOCAL_OPTIMIZATION_ALGORITHM"),
        "local optimization algorithm",
        "A local optimization algorithm is an optimisation algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000470] that only finds a local optimum of a function. If several optima exist for the function, it usually depends on the starting values for the variables which optimum is found.",
        ("local optimiation method",),
        False,
    ),
    (
        "KISAO_0000472",
        ("KISAO_0000472", "GLOBAL_OPTIMIZATION_ALGORITHM"),
        "global optimization algorithm",
        "A global optimization algorithm is an optimization algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000470] that tries to find the global optimum of a function. If a function has several minima/maxima with in the allowed range of variable values, the global minimum/maximum is the one with the smallest/largest function value.",
        ("global optimization method",),
        False,
    ),
    (
        "KISAO_0000473",
        ("KISAO_0000473", "BAYESIAN_INFERENCE_ALGORITHM"),
        "Bayesian inference algorithm",
        "A bayesian inference algorithm calculates a posterior probability distribution from a prior probability distribution and some additional evidence in the form of a likelyhood function.",
        (),
        False,
    ),
    (
        "KISAO_0000475",
        ("KISAO_0000475", "INTEGRATION_METHOD"),
        "integration method",
        "the integration method used by the solver",
        (),
        False,
    ),
    (
        "KISAO_0000476",
        ("KISAO_0000476", "ITERATION_TYPE"),
        "iteration type",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/12/",
        (),
        False,
    ),
    (
        "KISAO_0000477",
        ("KISAO_0000477", "LINEAR_SOLVER"),
        "linear solver",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/12/",
        (),
        False,
    ),
    (
        "KISAO_0000478",
        ("KISAO_0000478", "PRECONDITIONER"),
        "preconditioner",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/12/",
        (),
        False,
    ),
    (
        "KISAO_0000479",
        ("KISAO_0000479", "UPPER_HALF_BANDWIDTH"),
        "upper half-bandwidth",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/12/",
        (),
        False,
    ),
    (
        "KISAO_0000480",
        ("KISAO_0000480", "LOWER_HALF_BANDWIDTH"),
        "lower half-bandwidth",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/12/",
        (),
        False,
    ),
    (
        "KISAO_0000481",
        ("KISAO_0000481", "INTERPOLATE_SOLUTION"),
        "interpolate solution",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/12/",
        (),
        False,
    ),
    (
        "KISAO_0000482",
        ("KISAO_0000482", "HALF_BANDWITH_PARAMETER"),
        "half-bandwith parameter",
        "the parameter related to the half-bandwidth value used by the Banded linear solver or preconditioner.",
        (),
        False,
    ),
    (
        "KISAO_0000483",
        ("KISAO_0000483", "STEP_SIZE"),
        "step size",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/13/",
        (),
        False,
    ),
    (
        "KISAO_0000484",
        ("KISAO_0000484", "MAXIMUM_ORDER"),
        "maximum order",
        "Maximum order of method. For example, in Roadrunner it can be used for two parameters that one can set for deterministic runs: 'maximum_bdf_order' and 'maximum_adams_order'.",
        (),
        False,
    ),
    (
        "KISAO_0000485",
        ("KISAO_0000485", "MINIMUM_STEP_SIZE"),
        "minimum step size",
        "A lower limit, in the units of the bound variable over which a numerical integration is being performed, that a numerical integration algorithm with variable step size should take.",
        (),
        False,
    ),
    (
        "KISAO_0000486",
        ("KISAO_0000486", "MAXIMUM_ITERATIONS"),
        "maximum iterations",
        "For algorithms that iterate to a solution (steady state finders in particular), a limit on the number of iterations that should be performed.",
        ("iteration limit",),
        False,
    ),
    (
        "KISAO_0000487",
        ("KISAO_0000487", "MINIMUM_DAMPING"),
        "minimum damping",
        "The damping factor is a variable for at least some steady state algorithms: roadrunner allows you to set the minimum value for this.",
        (),
        False,
    ),
    (
        "KISAO_0000488",
        ("KISAO_0000488", "SEED"),
        "seed",
        "Random seed of a stochastic algorithm. Setting it allows one to reproduce their results while running the same algorithm on the same computer.",
        ("random seed",),
        False,
    ),
    (
        "KISAO_0000491",
        ("KISAO_0000491", "DISCRETE_EVENT_SIMULATION_ALGORITHM"),
        "discrete event simulation algorithm",
        "Discrete Event Simulation algorithm refers to the simulation of systems whose (countable) discrete states change over time and are event-driven.",
        ("DES",),
        False,
    ),
    (
        "KISAO_0000492",
        ("KISAO_0000492", "ASYNCHRONOUS_UPDATING_POLICY"),
        "asynchronous updating policy",
        "An updating policy where all enabled transitions (events) occur independently. Thus a state has as many successors as the number of transitions enabled in this state.",
        (),
        False,
    ),
    (
        "KISAO_0000493",
        ("KISAO_0000493", "SYNCHRONOUS_UPDATING_POLICY"),
        "synchronous updating policy",
        "An updating policy where all enabled transitions occur simultaneously. Thus a state will have at most one successor.",
        (),
        False,
    ),
    (
        "KISAO_0000494",
        ("KISAO_0000494", "FULLY_ASYNCHRONOUS_UPDATING_POLICY"),
        "fully asynchronous updating policy",
        "An updating policy where all enabled transitions occur either independently or (partially) simultaneously. (i.e. considering all possible combinations of enabled transitions). Thus a state has as many successors as the number of combinations of transitions enabled in this state.",
        (),
        False,
    ),
    (
        "KISAO_0000495",
        ("KISAO_0000495", "RANDOM_ASYNCHRONOUS_UPDATING_POLICY"),
        "random asynchronous updating policy",
        "An updating policy where a single transition is picked randomly from the set of transitions enabled in this state. Thus a state will have at most one successor.",
        (),
        False,
    ),
    (
        "KISAO_0000496",
        ("KISAO_0000496", "CVODES"),
        "CVODES",
        "CVODES is a superset of CVODE [http://identifiers.org/biomodels.kisao/KISAO_0000019] and hence all options available to CVODE (with the exception of the FCVODE interface module) are also available for CVODES. Both integration methods (Adams-Moulton [http://identifiers.org/biomodels.kisao/KISAO_0000280] and BDF [http://identifiers.org/biomodels.kisao/KISAO_0000288]) and the corresponding nonlinear iteration methods, as well as all linear solver and preconditioner modules, are available for the integration of the original ODEs, the sensitivity systems, or the adjoint system.",
        (),
        False,
    ),
    (
        "KISAO_0000497",
        ("KISAO_0000497", "KLU"),
        "KLU",
        "KLU is a software package and an algorithm for solving sparse unsymmetric linear systems of equations that arise in circuit simulation applications. It relies on a permutation to Block Triangular Form (BTF), several methods for finding a fill-reducing ordering (variants of approximate minimum degree and nested dissection), and Gilbert/Peierls’ sparse left-looking LU factorization algorithm to factorize each block. The package is written in C and includes a MATLAB interface.",
        ('"Clark Kent" LU factorization algorithm',),
        False,
    ),
    (
        "KISAO_0000498",
        ("KISAO_0000498", "NUMBER_OF_RUNS"),
        "number of runs",
        "Requested in https://sourceforge.net/p/kisao/feature-requests/31/",
        (),
        False,
    ),
    (
        "KISAO_0000499",
        ("KISAO_0000499", "DYNAMIC_FLUX_BALANCE_ANALYSIS"),
        "dynamic flux balance analysis",
        "Ticket 32",
        ("DFBA",),
        False,
    ),
    (
        "KISAO_0000500",
        ("KISAO_0000500", "SOA_DFBA"),
        "SOA-DFBA",
        "Ticket 32",
        ("SOA", "static optimization approach dynamic flux balance analysis"),
        False,
    ),
    (
        "KISAO_0000501",
        ("KISAO_0000501", "DOA_DFBA"),
        "DOA-DFBA",
        "Ticket 32",
        ("DOA", "dynamic optimization approach dynamic flux balance analysis"),
        False,
    ),
    (
        "KISAO_0000502",
        ("KISAO_0000502", "DA_DFBA"),
        "DA-DFBA",
        "Ticket 32",
        ("DA", "direct approach dynamics flux balance analysis"),
        False,
    ),
    (
        "KISAO_0000503",
        ("KISAO_0000503", "SIMULATED_ANNEALING"),
        "simulated annealing",
        "Simulated annealing is an optimization algorithm first proposed by Kirkpatrick et al. and was inspired by statistical mechanics and the way in which perfect crystals are formed. Perfect crystals are formed by first melting the substance of interest, and then cooling it very slowly. At large temperatures the particles vibrate with wide amplitude and this allows a search for global optimum. As the temperature decreases so do the vibrations until the system settles to the global optimum (the perfect crystal). The simulated annealing optimization algorithm uses a similar concept: the objective function is considered a measure of the energy of the system and this is maintained constant for a certain number of iterations (a temperature cycle). In each iteration, the parameters are changed to a nearby location in parameter space and the new objective function value calculated; if it decreased, then the new state is accepted, if it increased then the new state is accepted with a probability that follows a Boltzmann distribution (higher temperature means higher probability of accepting the new state). After a fixed number of iterations, the stopping criterion is checked; if it is not time to stop, then the system's temperature is reduced and the algorithm continues. Simulated annealing is a stochastic algorithm that is guaranteed to converge if ran for an infinite number of iterations. It is one of the most robust global optimization algorithms, although it is also one of the slowest. (Be warned that simulated annealing can run for hours or even days!).",
        (),
        False,
    ),
    (
        "KISAO_0000504",
        ("KISAO_0000504", "RANDOM_SEARCH"),
        "random search",
        "Random search is an optimization method that attempts to find the optimum by testing the objective function's value on a series of combinations of random values of the adjustable parameters. The random values are generated complying with any boundaries selected by the user, furthermore, any combinations of parameter values that do not fulfill constraints on the variables are excluded. This means that the method is capable of handling bounds on the adjustable parameters and fulfilling constraints. For infinite number of iterations this method is guaranteed to find the global optimum of the objective function. In general one is interested in processing a very large number of iterations.",
        (),
        False,
    ),
    (
        "KISAO_0000505",
        ("KISAO_0000505", "PARTICLE_SWARM"),
        "particle swarm",
        "The particle swarm optimization method suggested by Kennedy and Eberhart is inspired by a flock of birds or a school of fish searching for food. Each particle has a position Xi and a velocity Vi in the parameter space. Additionally, it remembers its best achieved objective value O and position Mi. Dependent on its own information and the position of its best neighbor (a random subset of particles of the swarm) a new velocity is calculated. With this information the position is updated.",
        (),
        False,
    ),
    (
        "KISAO_0000506",
        ("KISAO_0000506", "GENETIC_ALGORITHM"),
        "genetic algorithm",
        'The genetic algorithm (GA) is a computational technique that mimics evolution and is based on reproduction and selection. A GA is composed of individuals that reproduce and compete, each one is a potential solution to the (optimization) problem and is represented by a "genome" where each gene corresponds to one adjustable parameter. At each generation of the GA, each individual is paired with one other at random for reproduction. Two offspring are produced by combining their genomes and allowing for "cross-over", i.e., the two new individuals have genomes that are formed from a combination of the genomes of their parents. Also each new gene might have mutated, i.e. the parameter value might have changed slightly. At the end of the generation, the algorithm has double the number of individuals. Then each of the individuals is confronted with a number of others to count how many does it outperform (the number of wins is the number of these competitors that represent worse solutions than itself). All the individuals are ranked by their number of wins, and the population is again reduced to the original number of individuals by eliminating those which have worse fitness (solutions).',
        ("GA",),
        False,
    ),
    (
        "KISAO_0000507",
        ("KISAO_0000507", "GENETIC_ALGORITHM_SR"),
        "genetic algorithm SR",
        None,
        ("genetic algorithm with stochastic ranking",),
        False,
    ),
    (
        "KISAO_0000508",
        ("KISAO_0000508", "EVOLUTIONARY_PROGRAMMING"),
        "evolutionary programming",
        'Evolutionary programming (EP) is a computational technique that mimics evolution and is based on reproduction and selection. An EP algorithm is composed of individuals that reproduce and compete, each one is a potential solution to the (optimization) problem and is represented by a "genome" where each gene corresponds to one adjustable parameter. At each generation of the EP, each individual reproduces asexually, i.e. divides into two individuals. One of these contains exactly the same "genome" as the parent while the other suffers some mutations (the parameter values of each gene change slightly). At the end of the generation, the algorithm has double the number of individuals. Then each of the individuals is confronted with a number of others to count how many does it outperform (the number of wins is the number of these competitors that represent worse solutions than itself). All the individuals are ranked by their number of wins, and the population is again reduced to the original number of individuals by eliminating those which have worse fitness (solutions).',
        ("EP",),
        False,
    ),
    (
        "KISAO_0000509",
        ("KISAO_0000509", "EVOLUTIONARY_STRATEGY"),
        "evolutionary strategy",
        "Evolutionary Strategies with Stochastic Ranking (SRES) is similar to Evolutionary Programming. However, a parent has multiple offsprings during each generation. Each offspring will contain a recombination of genes with another parent and additional mutations. The algorithm assures that each parameter value will be within its boundaries. But constraints to the solutions may be violated.",
        ("SRES", "evolutionary strategies with stochastic ranking"),
        False,
    ),
    (
        "KISAO_0000510",
        ("KISAO_0000510", "TRUNCATED_NEWTON"),
        "truncated Newton",
        "The Truncated Newton method is a sophisticated variant of the Newton optimization method. The Newton optimization method searches for the minimum of a nonlinear function by following descent directions determined from the function's first and second partial derivatives. The Truncated Newton method does an incomplete (truncated) solution of a system of linear equations to calculate the Newton direction. This means that the actual direction chosen for the descent is between the steepest descent direction and the true Newton direction.",
        (),
        False,
    ),
    (
        "KISAO_0000511",
        ("KISAO_0000511", "STEEPEST_DESCENT"),
        "steepest descent",
        "Steepest descent is an optimization method that follows the direction of steepest descent on the hyper-surface of the objective function to find a local minimum. The direction of steepest descent is defined by the negative of the gradient of the objective function.",
        (),
        False,
    ),
    (
        "KISAO_0000512",
        ("KISAO_0000512", "PRAXIS"),
        "praxis",
        "Praxis is a direct search method that searches for the minimum of a nonlinear function without requiring (or attempting to calculate) derivatives of that function. Praxis was developed by Brent after the method proposed by Powell. The inspiration for Praxis was the well-known method of minimising each adjustable parameter (direction) at a time - the principal axes method. In Praxis directions are chosen that do not coincide with the principal axes, in fact if the objective function is quadratic then these will be conjugate directions, assuring a fast convergence rate.",
        (),
        False,
    ),
    (
        "KISAO_0000513",
        ("KISAO_0000513", "NL2SOL"),
        "NL2SOL",
        "The NL2SOL method is based on an adaptive nonlinear least-squares algorithm, devised by Dennis and colleagues. For problems with large number of residuals, this algorithm is known to be more reliable than Gauss-Newton or Levenberg-Marquardt method and more efficient than the secant or variable metric algorithms that are intended for general function minimization.",
        ("adaptive nonlinear least-squares algorithm",),
        False,
    ),
    (
        "KISAO_0000514",
        ("KISAO_0000514", "NELDER_MEAD"),
        "Nelder-Mead",
        "This method also known as the simplex method is due to Nelder and Mead. A simplex is a polytope of N+1 vertices in N dimensions. The objective function is evaluated at each vertex. Dependent on these calculated values a new simplex is constructed. The simplest step is to replace the worst point with a point reflected through the centroid of the remaining N points. If this point is better than the best current point, then we can try stretching exponentially out along this line. On the other hand, if this new point isn't much better than the previous value then we are stepping across a valley, so we shrink the simplex towards the best point.",
        ("simplex method",),
        False,
    ),
    (
        "KISAO_0000515",
        ("KISAO_0000515", "LEVENBERG_MARQUARDT"),
        "Levenberg-Marquardt",
        "Levenberg-Marquardt is a gradient descent method. It is a hybrid between the steepest descent and the Newton methods. Levenberg first suggested an improvement to the Newton method in order to make it more robust, i.e. to overcome the problem of non-convergence. His suggestion was to add a factor to the diagonal elements of the Hessian matrix of second derivatives when not close to the minimum (this can be judged by how positive definite the matrix is). The effect when this factor is large compared to the elements of Hessian is that the method then becomes the steepest descent method. Later Marquardt suggested that the factor should be multiplicative rather than additive and also defined a heuristic to make this factor increase or decrease. The method known as Levenberg-Marquardt is thus an adaptive method that effectively changes between the steepest descent to the Newton method.",
        (),
        False,
    ),
    (
        "KISAO_0000516",
        ("KISAO_0000516", "HOOKE_JEEVES"),
        "Hooke&Jeeves",
        "The method of Hooke and Jeeves is a direct search algorithm that searches for the minimum of a nonlinear function without requiring (or attempting to calculate) derivatives of the function. Instead it is based on a heuristic that suggests a descent direction using the values of the function calculated in a number of previous iterations.",
        (
            "Hooke and Jeeves method",
            "Hooke-Jeeves method",
            "method of Hooke and Jeeves",
        ),
        False,
    ),
    (
        "KISAO_0000517",
        ("KISAO_0000517", "NUMBER_OF_GENERATIONS"),
        "number of generations",
        "The parameter is a positive integer value to determine the number of generations the evolutionary algorithm shall evolve the population.",
        (),
        False,
    ),
    (
        "KISAO_0000518",
        ("KISAO_0000518", "EVOLUTIONARY_ALGORITHM_PARAMETER"),
        "evolutionary algorithm parameter",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000519",
        ("KISAO_0000519", "POPULATION_SIZE"),
        "population size",
        "The parameter is a positive integer value to determine the size of the population, i.e., the number of individuals that survive after each generation.",
        (),
        False,
    ),
    (
        "KISAO_0000520",
        ("KISAO_0000520", "EVOLUTIONARY_ALGORITHM"),
        "evolutionary algorithm",
        "An optimisation algorithm that mimics evolution and is based on reproduction and selection.",
        (),
        False,
    ),
    (
        "KISAO_0000521",
        ("KISAO_0000521", "SIMULATED_ANNEALING_PARAMETER"),
        "simulated annealing parameter",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000522",
        ("KISAO_0000522", "START_TEMPERATURE"),
        "start temperature",
        'Initial temperature of the system. The higher the temperature, the larger the probability that a global optimum is found. Note that the temperature should be very high in the beginning of the method (the system should be above the "melting" temperature). This value has the same units as the objective function, so what represents "high" is different from problem to problem.',
        (),
        False,
    ),
    (
        "KISAO_0000523",
        ("KISAO_0000523", "COOLING_FACTOR"),
        "cooling factor",
        'Rate by which the temperature is reduced from one cycle to the next, given by the formula: Tnew=Told*"Cooling Factor". The simulated annealing algorithm works best if the temperature is reduced at a slow rate, so this value should be close to 1.',
        (),
        False,
    ),
    (
        "KISAO_0000524",
        ("KISAO_0000524", "PARTITIONED_LEAPING_METHOD"),
        "partitioned leaping method",
        'Multiscale simulation approach for modeling stochasticity in chemical reaction networks. The approach seamlessly integrates exact-stochastic and "leaping" methodologies into a single partitioned leaping algorithmic framework. The technique correctly accounts for stochastic noise at significantly reduced computational cost, requires the definition of only three modelindependent parameters and is particularly well-suited for simulating systems containing widely disparate species populations.',
        (),
        False,
    ),
    (
        "KISAO_0000525",
        ("KISAO_0000525", "STOP_CONDITION"),
        "stop condition",
        "A condition upon which a simulation should terminate.",
        (),
        False,
    ),
    (
        "KISAO_0000526",
        ("KISAO_0000526", "FLUX_VARIABILITY_ANALYSIS"),
        "flux variability analysis",
        "Method for determining the minimum and maximum flux of each reaction that satisfies the flux constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model.",
        ("FVA",),
        False,
    ),
    (
        "KISAO_0000527",
        ("KISAO_0000527", "GEOMETRIC_FLUX_BALANCE_ANALYSIS"),
        "geometric flux balance analysis",
        "Method for determining the central flux distribution among all flux distributions that satisfy the constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model.",
        ("gFBA", "geometric FBA"),
        False,
    ),
    (
        "KISAO_0000528",
        (
            "KISAO_0000528",
            "PARSIMONIOUS_ENZYME_USAGE_FLUX_BALANCE_ANALYSIS__MINIMUM_SUM_OF_ABSOLUTE_FLUXES_",
        ),
        "parsimonious enzyme usage flux balance analysis (minimum sum of absolute fluxes)",
        "Method for determining the smallest flux distribution among all flux distributions that satisfy the constraints of the flux balance analysis (FBA) [http://identifiers.org/biomodels.kisao/KISAO_0000437] model.",
        ("pFBA", "parsimonious FBA", "parsimonious flux balance analysis"),
        False,
    ),
    (
        "KISAO_0000529",
        ("KISAO_0000529", "PARALLELISM"),
        "parallelism",
        "Number of parallel processes to use.",
        (),
        False,
    ),
    (
        "KISAO_0000531",
        ("KISAO_0000531", "FRACTION_OF_OPTIMUM"),
        "fraction of optimum",
        "Fraction of the optimum solution which must be maintained.",
        (),
        False,
    ),
    (
        "KISAO_0000532",
        ("KISAO_0000532", "LOOPLESS"),
        "loopless",
        "Whether to return only loopless flux solutions.",
        (),
        False,
    ),
    (
        "KISAO_0000533",
        ("KISAO_0000533", "PFBA_FACTOR"),
        "pFBA factor",
        "Maximum permissible sum of absolute fluxes.",
        (),
        False,
    ),
    (
        "KISAO_0000534",
        ("KISAO_0000534", "REACTIONS"),
        "reactions",
        "FVA algorithm [http://www.biomodels.net/kisao/KISAO#KISAO_0000526] parameter: reactions to compute the variablity of.",
        (),
        False,
    ),
    (
        "KISAO_0000535",
        ("KISAO_0000535", "VODE"),
        "VODE",
        "VODE provides implicit Adams method (for non-stiff problems) and a method based on backward differentiation formulas (BDF) (for stiff problems).",
        (
            "DVODE",
            "Real-valued Variable-coefficient Ordinary Differential Equation solver, with fixed-leading-coefficient implementation",
            "real-valued variable-coefficient ordinary differential equation solver, with fixed-leading-coefficient implementation",
        ),
        False,
    ),
    (
        "KISAO_0000536",
        ("KISAO_0000536", "ZVODE"),
        "ZVODE",
        "ZVODE provides implicit Adams method (for non-stiff problems) and a method based on backward differentiation formulas (BDF) (for stiff problems).",
        (
            "Complex-valued Variable-coefficient Ordinary Differential Equation solver, with fixed-leading-coefficient implementation",
            "complex-valued variable-coefficient ordinary differential equation solver, with fixed-leading-coefficient implementation",
        ),
        False,
    ),
    (
        "KISAO_0000537",
        ("KISAO_0000537", "EXPLICIT_RUNGE_KUTTA_METHOD_OF_ORDER_3_2_"),
        "explicit Runge-Kutta method of order 3(2)",
        "RK23 uses the Bogacki-Shampine pair of formulas [1]. The error is controlled assuming accuracy of the second-order method, but steps are taken using the third-order accurate formula (local extrapolation is done). A cubic Hermite polynomial is used for the dense output.",
        ("RK23",),
        False,
    ),
    (
        "KISAO_0000538",
        ("KISAO_0000538", "SAFETY_FACTOR_ON_NEW_STEP_SELECTION"),
        "safety factor on new step selection",
        None,
        ("safe", "safety"),
        False,
    ),
    (
        "KISAO_0000539",
        ("KISAO_0000539", "MINIMUM_FACTOR_TO_CHANGE_STEP_SIZE_BY"),
        "minimum factor to change step size by",
        "Minimum factor to increase/decrease step size by in one step. The new step-size is chosen subject to the restriction fac1 <= current step-size / old step-size <= fac2.",
        ("dfactor", "fac1"),
        False,
    ),
    (
        "KISAO_0000540",
        ("KISAO_0000540", "MAXIMUM_FACTOR_TO_CHANGE_STEP_SIZE_BY"),
        "maximum factor to change step size by",
        "Maximum factor to increase/decrease step size by in one step. The new step-size is chosen subject to the restriction fac1 <= current step-size / old step-size <= fac2.",
        ("fac2", "ifactor"),
        False,
    ),
    (
        "KISAO_0000541",
        ("KISAO_0000541", "BETA_PARAMETER_FOR_STABILIZED_STEP_SIZE_CONTROL"),
        "beta parameter for stabilized step size control",
        None,
        ("beta",),
        False,
    ),
    (
        "KISAO_0000542",
        (
            "KISAO_0000542",
            "CORRECTION_STEP_SHOULD_USE_INTERNALLY_GENERATED_FULL_JACOBIAN",
        ),
        "correction step should use internally generated full Jacobian",
        "Specifies whether the iteration method of the ODE solver’s correction step is chord iteration with an internally generated full Jacobian or functional iteration with no Jacobian. Option is only considered when the user has not supplied a Jacobian function and has not indicated (by setting either upper or lower band) that the Jacobian is banded.",
        ("MF=22", "with Jacobian"),
        False,
    ),
    (
        "KISAO_0000543",
        ("KISAO_0000543", "STABILITY_LIMIT_DETECTION_FLAG"),
        "stability limit detection flag",
        "Flag to activate stability limit detection.",
        (),
        False,
    ),
    (
        "KISAO_0000544",
        ("KISAO_0000544", "IDAS"),
        "IDAS",
        "IDAS solves real differential-algebraic systems in N-space, in the general form F(t,y,y')=0, y(t0)=y0, y'(t0)=y'0 with sensitivity analysis.",
        ("implicit differential-algebraic solver with sensitivity analysis",),
        False,
    ),
    (
        "KISAO_0000545",
        ("KISAO_0000545", "INCLUDE_SENSITIVITY_VARIABLES_IN_ERROR_CONTROL_MECHANISM"),
        "include sensitivity variables in error control mechanism",
        "Specifies whether sensitivity variables are included or not in the error control mechanism.",
        ("errconS",),
        False,
    ),
    (
        "KISAO_0000546",
        ("KISAO_0000546", "CONVEX_OPTIMIZATION_ALGORITHM"),
        "convex optimization algorithm",
        "Optimization of a convex function over a convex set. Convex optimization is subclass of global optimization because conveness gaurantees that each local optimum is a global optimum.",
        (),
        False,
    ),
    (
        "KISAO_0000547",
        ("KISAO_0000547", "LINEAR_PROGRAMMING"),
        "linear programming",
        "Method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships.",
        ("LP",),
        False,
    ),
    (
        "KISAO_0000548",
        ("KISAO_0000548", "QUADRATIC_PROGRAMMING"),
        "quadratic programming",
        "Process of solving a quadratic optimization problem.",
        ("QP",),
        False,
    ),
    (
        "KISAO_0000549",
        ("KISAO_0000549", "NON_LINEAR_PROGRAMMING"),
        "non-linear programming",
        "Process of solving an optimization problem where some of the constraints or the objective function are nonlinear.",
        (),
        False,
    ),
    (
        "KISAO_0000550",
        ("KISAO_0000550", "SIMPLEX_METHOD"),
        "simplex method",
        "Approach to solving linear programming models by hand using slack variables, tableaus, and pivot variables as a means to finding the optimal solution of an optimization problem.",
        ("Dantzig's simplex algorithm",),
        False,
    ),
    (
        "KISAO_0000551",
        ("KISAO_0000551", "PRIMAL_DUAL_INTERIOR_POINT_METHOD"),
        "primal-dual interior point method",
        "The Interior Point method approximates the constraints of a linear programming model as a set of boundaries surrounding a region.",
        (),
        False,
    ),
    (
        "KISAO_0000552",
        ("KISAO_0000552", "OPTIMIZATION_METHOD"),
        "optimization method",
        "Optimization method such as the revised simplex method [http://identifiers.org/biomodels.kisao/KISAO_0000550] or primal-dual interior point method [http://identifiers.org/biomodels.kisao/KISAO_0000551].",
        (),
        False,
    ),
    (
        "KISAO_0000553",
        ("KISAO_0000553", "OPTIMIZATION_SOLVER"),
        "optimization solver",
        "Optimization solver such as CPLEX, GLPK, or Gurobi.",
        (),
        False,
    ),
    (
        "KISAO_0000554",
        (
            "KISAO_0000554",
            "PARSIMONIUS_FLUX_BALANCE_ANALYSIS__MINIMUM_NUMBER_OF_ACTIVE_FLUXES_",
        ),
        "parsimonius flux balance analysis (minimum number of active fluxes)",
        "A technique for selecting a parsimonious flux distribution which has a minimal number of active fluxes.",
        ("pFBA", "parsimonious FBA", "parsimonious flux balance analysis"),
        False,
    ),
    (
        "KISAO_0000555",
        ("KISAO_0000555", "ABSOLUTE_QUADRATURE_TOLERANCE"),
        "absolute quadrature tolerance",
        "Absolute error tolerance of the adjoint solution.",
        (),
        False,
    ),
    (
        "KISAO_0000556",
        ("KISAO_0000556", "RELATIVE_QUADRATURE_TOLERANCE"),
        "relative quadrature tolerance",
        "Relative error tolerance of the adjoint solution.",
        (),
        False,
    ),
    (
        "KISAO_0000557",
        ("KISAO_0000557", "ABSOLUTE_STEADY_STATE_TOLERANCE"),
        "absolute steady-state tolerance",
        "Absolute error tolerance of the steady-state.",
        (),
        False,
    ),
    (
        "KISAO_0000558",
        ("KISAO_0000558", "RELATIVE_STEADY_STATE_TOLERANCE"),
        "relative steady-state tolerance",
        "Relative error tolerance of the steady-state.",
        (),
        False,
    ),
    (
        "KISAO_0000559",
        ("KISAO_0000559", "INITIAL_STEP_SIZE"),
        "initial step size",
        "Initial time step size.",
        (),
        False,
    ),
    (
        "KISAO_0000560",
        ("KISAO_0000560", "LSODA_LSODAR_HYBRID_METHOD"),
        "LSODA/LSODAR hybrid method",
        "Automatically use LSODA or LSODAR as apropriate for the given problem. Use LSODA if the problem has no roots. Use LSODAR if the problem has roots.",
        (),
        False,
    ),
    (
        "KISAO_0000561",
        (
            "KISAO_0000561",
            "PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_RUNGE_KUTTA_METHOD",
        ),
        "Pahle hybrid Gibson-Bruck Next Reaction method/Runge-Kutta method",
        "Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. A 4th-order Runge-Kutta method is used to numerically integrate the deterministic part of the system. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method.",
        (),
        False,
    ),
    (
        "KISAO_0000562",
        (
            "KISAO_0000562",
            "PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_LSODA_METHOD",
        ),
        "Pahle hybrid Gibson-Bruck Next Reaction method/LSODA method",
        "Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. The deterministic subnet is integrated with LSODA. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method.",
        (),
        False,
    ),
    (
        "KISAO_0000563",
        (
            "KISAO_0000563",
            "PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_RK_45_METHOD",
        ),
        "Pahle hybrid Gibson-Bruck Next Reaction method/RK-45 method",
        "Combines a deterministic numerical integration of ODEs with a stochastic simulation algorithm. The whole biochemical network is partitioned into a deterministic and a stochastic subnet internally. The deterministic subnet contains all reactions in which only species with high particle numbers take part. All reactions with at least one low-numbered species are in the stochastic subnet. The partitioning of the biochemical network can change dynamically during the simulation. The reaction probabilities of the stochastic subnet are approximated as constant during one stochastic step. The deterministic subnet is integrated with RK-45. The stochastic subnet is simulated by the Gibson-Bruck Next Reaction Method.",
        (),
        False,
    ),
    (
        "KISAO_0000564",
        ("KISAO_0000564", "STOCHASTIC_RUNGE_KUTTA_METHOD"),
        "stochastic Runge-Kutta method",
        "Technique for the approximate numerical solution of a systems of stochastic differential equations (SDEs). The method is a generalisation of the Runge-Kutta method for ordinary differential equations to stochastic differential equations.",
        (),
        False,
    ),
    (
        "KISAO_0000565",
        ("KISAO_0000565", "ABSOLUTE_TOLERANCE_FOR_ROOT_FINDING"),
        "absolute tolerance for root finding",
        "Absolute error tolerance for root finding.",
        (),
        False,
    ),
    (
        "KISAO_0000566",
        ("KISAO_0000566", "STOCHASTIC_SECOND_ORDER_RUNGE_KUTTA_METHOD"),
        "stochastic second order Runge-Kutta method",
        "Technique for the second order approximate numerical solution of a systems of stochastic differential equations (SDEs). The method is a generalisation of the Runge-Kutta method for ordinary differential equations to stochastic differential equations.",
        ("RI5",),
        False,
    ),
    (
        "KISAO_0000567",
        ("KISAO_0000567", "FORCE_PHYSICAL_CORRECTNESS"),
        "force physical correctness",
        "Indicates whether to force physical correctness.",
        (),
        False,
    ),
    (
        "KISAO_0000568",
        ("KISAO_0000568", "NLEQ1"),
        "NLEQ1",
        "Damped Newton-algorithm with rank strategy for systems of highly nonlinear equations. Global Newton method with error oriented convergence criterion; arbitrary selection of direct linear equation solver.",
        (
            "Newton-type method for solveing non-linear (NL) equations (EQ)",
            "numerical solution of nonlinear (NL) equations (EQ) especially designed for numerically sensitive problems",
        ),
        False,
    ),
    (
        "KISAO_0000569",
        ("KISAO_0000569", "NLEQ2"),
        "NLEQ2",
        "Damped Newton-algorithm with rank strategy for systems of highly nonlinear equations. Global Newton method with error oriented convergence criterion; QR-decomposition with subcondition number estimate.",
        (
            "Newton-type method for solveing non-linear (NL) equations (EQ)",
            "numerical solution of nonlinear (NL) equations (EQ) especially designed for numerically sensitive problems",
        ),
        False,
    ),
    (
        "KISAO_0000570",
        ("KISAO_0000570", "AUTO_REDUCE_TOLERANCES"),
        "auto reduce tolerances",
        "Whether to automatically reduce tolerances.",
        (),
        False,
    ),
    (
        "KISAO_0000571",
        ("KISAO_0000571", "ABSOLUTE_TOLERANCE_ADJUSTMENT_FACTOR"),
        "absolute tolerance adjustment factor",
        "How much to adjust the absolute tolerance.",
        (),
        False,
    ),
    (
        "KISAO_0000572",
        ("KISAO_0000572", "LEVEL_OF_SUPERIMPOSED_NOISE"),
        "level of superimposed noise",
        "Standard deviation of the Gaussian noise which is added to each prediction.",
        ("noise level",),
        False,
    ),
    (
        "KISAO_0000573",
        ("KISAO_0000573", "PROBABILISTIC_LOGICAL_MODEL_SIMULATION_METHOD"),
        "probabilistic logical model simulation method",
        "Qualitative (logical) models specify the evolution rules of their components. Probabilistic networks allow for specifying more than one transition function per variable/gene. Each of these functions has a probability to be chosen, where the probabilities of all functions for one variable sum up to 1. Transitions are performed synchronously by choosing one transition function for each gene according to their probabilities and applying them to the current state.",
        (),
        False,
    ),
    (
        "KISAO_0000574",
        ("KISAO_0000574", "SPECIES_TRANSITION_PROBABILITIES"),
        "species transition probabilities",
        "Probability of each species to be chosen for the next state transition.",
        (),
        False,
    ),
    (
        "KISAO_0000575",
        ("KISAO_0000575", "HYBRID_TAU_LEAPING_METHOD"),
        "hybrid tau-leaping method",
        "A continuously coupled hybrid deterministic/stochastic simulation algorithm for biochemical networks. Biochemical species are classified as continuous, discrete, or switch. Tau-leaping is used to simulate stochastic species, and LSODA or another ODE integration method is used to simulate continuous species. Switch species are dynamically classified as either continuous or discrete at each timestep depending on a user defined error tolerance.",
        (),
        False,
    ),
    (
        "KISAO_0000576",
        ("KISAO_0000576", "QUADRATIC_MOMA"),
        "quadratic MOMA",
        "Minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. MOMA employs quadratic programming to identify the closest point (in terms of its Euclidean distance) in the permissible flux space of the knockout to the wild-type flux vector by solving the optimization problem Min sum((fluxAi - fluxBi)^2) + sum(fluxAi)^(fluxMinimizationWeight) + sum(fluxBi)^(fluxMinimizationWeight)",
        (
            "MOMA",
            "Quadratic Minimization of Metabolic Adjustment",
            "minimization of metabolic adjustment",
            "quadratic minimization of metabolic adjustment",
        ),
        False,
    ),
    (
        "KISAO_0000577",
        ("KISAO_0000577", "FLUX_MINIMIZATION_WEIGHT"),
        "flux minimization weight",
        "The degree to which minimization of the sum of fluxes should be taken into account in Minimization of Metabolic Adjustment (MOMA) which solvers the optimization problem Min sum((fluxAi - fluxBi)^2) + sum(fluxAi)^(fluxMinimizationWeight) + sum(fluxBi)^(fluxMinimizationWeight)",
        (),
        False,
    ),
    (
        "KISAO_0000578",
        ("KISAO_0000578", "NESTED_ALGORITHM"),
        "nested algorithm",
        "A nested algorithm of an algorithm",
        ("nested method", "subalgorithm"),
        False,
    ),
    (
        "KISAO_0000579",
        ("KISAO_0000579", "LINEAR_MOMA"),
        "linear MOMA",
        "Linear minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. Linear MOMA employs linear programming to identify the closest point (in terms of its L1 norm) in the permissible flux space of the knockout to the wild-type flux vector by solving the optimization problem Min sum(|fluxAi - fluxBi|)",
        (
            "Linear Minimization of Metabolic Adjustment",
            "linear minimization of metabolic adjustment",
        ),
        False,
    ),
    (
        "KISAO_0000580",
        ("KISAO_0000580", "ROOM"),
        "ROOM",
        "Constraint-based algorithm for predicting the metabolic steady state after gene knockouts which aims to minimize the number of significant flux changes (hence on/off) with respect to the wild type.",
        (
            "Regulatory on/off minimization of metabolic flux changes",
            "regulatory on/off minimization of metabolic flux changes",
        ),
        False,
    ),
    (
        "KISAO_0000581",
        ("KISAO_0000581", "BKMC"),
        "BKMC",
        "The Boolean kinetic Monte Carlo method (BKMC) is a natural generalization of the asynchronous Boolean simulation method, with a direct probabilistic interpretation. In the BKMC framework, the dynamics is parameterized by a biological time and the order of update is noisy, which is less strict than priority classes introduced in GINsin. A BKMC model is specified by logical rules as in regular Boolean models but with a more precise information: a numerical rate is added for each transition of each node.",
        ("Boolean Kinetic Monte-Carlo", "Boolean kinetic Monte-Carlo"),
        False,
    ),
    (
        "KISAO_0000582",
        ("KISAO_0000582", "SPATIOCYTE_METHOD"),
        "Spatiocyte method",
        "Lattice-based stochastic particle simulation method for biochemical reaction and diffusion processes.",
        (),
        False,
    ),
    (
        "KISAO_0000583",
        ("KISAO_0000583", "MINIMUM_ORDER"),
        "minimum order",
        "Minimum order of method.",
        (),
        False,
    ),
    (
        "KISAO_0000584",
        ("KISAO_0000584", "INITIAL_ORDER"),
        "initial order",
        "Initial order of method.",
        (),
        False,
    ),
    (
        "KISAO_0000585",
        ("KISAO_0000585", "TOMS731"),
        "TOMS731",
        "Moving-grid interface for systems of one-dimensional time-dependent partial differential equations.",
        (),
        False,
    ),
    (
        "KISAO_0000586",
        (
            "KISAO_0000586",
            "GIBSON_BRUCK_NEXT_REACTION_ALGORITHM_WITH_INDEXED_PRIORITY_QUEUE",
        ),
        "Gibson-Bruck next reaction algorithm with indexed priority queue",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000587",
        ("KISAO_0000587", "IMEX"),
        "IMEX",
        "Method for solving stiff and imaginary ODE problems",
        (
            "Implicit-Explicit Runge-Kutta method",
            "implicit-explicit Runge-Kutta method",
        ),
        False,
    ),
    (
        "KISAO_0000588",
        ("KISAO_0000588", "FLUX_SAMPLING"),
        "flux sampling",
        "Method for sampling fluxes from the null space of a flux balance analysis model",
        (),
        False,
    ),
    (
        "KISAO_0000589",
        ("KISAO_0000589", "ACB_FLUX_SAMPLING_METHOD"),
        "ACB flux sampling method",
        None,
        (
            "Artificial centering boundary flux sampling method",
            "artificial centering boundary flux sampling method",
        ),
        False,
    ),
    (
        "KISAO_0000590",
        ("KISAO_0000590", "ACHR_FLUX_SAMPLING_METHOD"),
        "ACHR flux sampling method",
        None,
        ("artificial centering hit-and-run flux sampling method",),
        False,
    ),
    (
        "KISAO_0000591",
        ("KISAO_0000591", "MDFBA"),
        "mdFBA",
        None,
        ("metabolic dilution flux balance analysis",),
        False,
    ),
    (
        "KISAO_0000592",
        ("KISAO_0000592", "DYNAMIC_RFBA"),
        "dynamic rFBA",
        "Method for predicting the dynamics of metabolic fluxes under patterns of the regulation of gene expression",
        (
            "dynamic regulatory flux balance analysis",
            "rFBA",
            "regulatory flux balance analysis",
        ),
        False,
    ),
    (
        "KISAO_0000593",
        ("KISAO_0000593", "MOMA"),
        "MOMA",
        "minimization of metabolic adjustment (MOMA) is an extension of FBA for the prediction of flux distributions in gene knockouts. MOMA identifies the closest point in the permissible flux space of the knockout to the wild-type flux vector by solving an optimization problem.",
        (
            "Minimization of Metabolic Adjustment",
            "minimization of metabolic adjustment",
        ),
        False,
    ),
    (
        "KISAO_0000594",
        ("KISAO_0000594", "ORDER"),
        "order",
        "Order of method",
        (),
        False,
    ),
    (
        "KISAO_0000595",
        ("KISAO_0000595", "RFBA"),
        "rFBA",
        "Method for predicting metabolic fluxes under patterns of the regulation of gene expression",
        ("regulatory flux balance analysis",),
        False,
    ),
    (
        "KISAO_0000596",
        ("KISAO_0000596", "SRFBA"),
        "srFBA",
        "Method for predicting steady-state metabolic fluxes under patterns of the regulation of gene expression",
        ("SR-FBA", "steady-state regulatory flux balance analysis"),
        False,
    ),
    (
        "KISAO_0000597",
        ("KISAO_0000597", "TOLERANCE"),
        "tolerance",
        "Numeric value specifying the desired tolerance the user wants to achieve. A smaller value means that the prediction is calculated more accurately.",
        (),
        False,
    ),
    (
        "KISAO_0000598",
        ("KISAO_0000598", "HYBRID_GIBSON___MILSTEIN_METHOD"),
        "hybrid Gibson - Milstein method",
        "A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE.",
        (),
        False,
    ),
    (
        "KISAO_0000599",
        ("KISAO_0000599", "HYBRID_GIBSON___EULER_MARUYAMA_METHOD"),
        "hybrid Gibson - Euler-Maruyama method",
        "A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE.",
        (),
        False,
    ),
    (
        "KISAO_0000600",
        ("KISAO_0000600", "HYBRID_ADAPTIVE_GIBSON___MILSTEIN_METHOD"),
        "hybrid adaptive Gibson - Milstein method",
        "A hybrid stochastic method partitions the system into subsets of fast and slow reactions and approximates the fast reactions as a continuous Markov process, using a chemical Langevin equation, and accurately describes the slow dynamics using the Gibson algorithm. Fixed time step Milstein is used for approximate numerical solution of CLE.",
        (),
        False,
    ),
    (
        "KISAO_0000601",
        ("KISAO_0000601", "NUMBER_OF_TRIALS"),
        "number of trials",
        "Number of multiple trials (e.g., of a scatter search method).",
        ("trials",),
        False,
    ),
    (
        "KISAO_0000602",
        ("KISAO_0000602", "MINIMUM_SPECIES_THRESHOLD_FOR_CONTINUOUS_APPROXIMATION"),
        "minimum species threshold for continuous approximation",
        "Minimum number of molecules of both reactant and product species required for approximation as a continuous Markov process.",
        ("Epsilon", "epsilon"),
        False,
    ),
    (
        "KISAO_0000603",
        ("KISAO_0000603", "MINIMUM_REACTION_RATE_FOR_CONTINUOUS_APPROXIMATION"),
        "minimum reaction rate for continuous approximation",
        "Minimum reaction rate required for approximation as a continuous Markov process.",
        ("Lambda", "lambda"),
        False,
    ),
    (
        "KISAO_0000604",
        ("KISAO_0000604", "MSR_TOLERANCE"),
        "MSR tolerance",
        "Maximum allowed effect of executing multiple slow reactions per numerical integration of the SDEs.",
        ("Multiple slow reactions tolerance", "multiple slow reactions tolerance"),
        False,
    ),
    (
        "KISAO_0000605",
        ("KISAO_0000605", "SDE_TOLERANCE"),
        "SDE tolerance",
        "Stochastic differential equation tolerance",
        (
            "Maximum allowed value of the drift and diffusion errors.",
            "maximum allowed value of the drift and diffusion errors.",
        ),
        False,
    ),
    (
        "KISAO_0000606",
        ("KISAO_0000606", "HIERARCHICAL_STOCHASTIC_SIMULATION_ALGORITHM"),
        "hierarchical stochastic simulation algorithm",
        "Fast, memory-efficient method for stochastic simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions.",
        ("hSSA",),
        False,
    ),
    (
        "KISAO_0000607",
        ("KISAO_0000607", "HIERARCHICAL_FEHLBERG_METHOD"),
        "hierarchical Fehlberg method",
        "Method for continuous simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions.",
        (
            "hODE",
            "hierarchical ODE integration method",
            "hierarchical ordinary differential equation integration method",
        ),
        False,
    ),
    (
        "KISAO_0000608",
        ("KISAO_0000608", "HIERARCHICAL_FLUX_BALANCE_ANALYSIS"),
        "hierarchical flux balance analysis",
        "Method for constraint-based simulation of hierarchically organized models, such as a model of a cellular population where each cell in the population is represented by the same species and reactions.",
        ("Hierarchical FBA", "hFBA", "hierarchical FBA"),
        False,
    ),
    (
        "KISAO_0000609",
        ("KISAO_0000609", "EMBEDDED_RUNGE_KUTTA_PRINCE_DORMAND__8_9__METHOD"),
        "embedded Runge-Kutta Prince-Dormand (8,9) method",
        "An embedded Runge-Kutta integrator of order 8(9).",
        ("RK8PD",),
        False,
    ),
    (
        "KISAO_0000610",
        ("KISAO_0000610", "COMPOSITE_REJECTION_STOCHASTIC_SIMULATION_ALGORITHM"),
        "composite-rejection stochastic simulation algorithm",
        None,
        ("SSA-CR",),
        False,
    ),
    (
        "KISAO_0000611",
        ("KISAO_0000611", "INCREMENTAL_STOCHASTIC_SIMULATION_ALGORITHM"),
        "incremental stochastic simulation algorithm",
        "Performs local averaging over small time-intervals to compute statistics on typical behavior.",
        ("iSSA",),
        False,
    ),
    (
        "KISAO_0000612",
        ("KISAO_0000612", "IMPLICIT_4TH_ORDER_RUNGE_KUTTA_METHOD_AT_GAUSSIAN_POINTS"),
        "implicit 4th order Runge-Kutta method at Gaussian points",
        None,
        ("RK4IMP",),
        False,
    ),
    (
        "KISAO_0000613",
        (
            "KISAO_0000613",
            "STOCHASTIC_SIMULATION_ALGORITHM_WITH_NORMALLY_DISTRIBUTED_NEXT_REACTION_TIMES",
        ),
        "stochastic simulation algorithm with normally-distributed next reaction times",
        None,
        ("NMC",),
        False,
    ),
    (
        "KISAO_0000614",
        ("KISAO_0000614", "IMPLEMENTATION"),
        "implementation",
        "An implementation of an algorithm. For example, simulation tools can this parameter to differentiate among C, Python, and Java implementations of the same algorithms and allow investigators to select one of these specific implementations through SED-ML.",
        (),
        False,
    ),
    (
        "KISAO_0000615",
        (
            "KISAO_0000615",
            "FULLY_IMPLICIT_REGULAR_GRID_FINITE_VOLUME_METHOD_WITH_A_VARIABLE_TIME_STEP",
        ),
        "fully-implicit regular grid finite volume method with a variable time step",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000616",
        (
            "KISAO_0000616",
            "SEMI_IMPLICIT_REGULAR_GRID_FINITE_VOLUME_METHOD_WITH_A_FIXED_TIME_STEP",
        ),
        "semi-implicit regular grid finite volume method with a fixed time step",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000617",
        ("KISAO_0000617", "IDA_CVODE_HYBRID_METHOD"),
        "IDA-CVODE hybrid method",
        "Meta algorithm which chooses between IDA and CVODE depending on the problem to be solved. CVODE is used for ordinary differential equation (ODE) systems. IDA is used for differential-algebraic equation (DAE) systems.",
        (),
        False,
    ),
    (
        "KISAO_0000618",
        ("KISAO_0000618", "BUNKER"),
        "bunker",
        "A variant of the stochastic simulation algorithm (SSA) in which the time to the next reaction is equated to the mean inter-event time (inverse of the sum of the propensitites of the reactions) rather than sampled from a distribution parameterized by this mean inter-event time. In this method, the next reaction time is deterministic rather than stochastic as in SSA.",
        (),
        False,
    ),
    (
        "KISAO_0000619",
        ("KISAO_0000619", "EMC_SIM"),
        "emc-sim",
        "A variant of the stochastic simulation algorithm (SSA) in which the time to the next reaction is a constant equal to 1 time unit. In this method, the next reaction time is deterministic rather than stochastic as in SSA.",
        (),
        False,
    ),
    (
        "KISAO_0000620",
        ("KISAO_0000620", "PARSIMONIUS_FLUX_BALANCE_ANALYSIS"),
        "parsimonius flux balance analysis",
        "A technique for selecting a flux distribution which is parsimonious by some metric, such as a solution which has the minimal number of active fluxes or a solution which has the smallest sum of active fluxes.",
        ("pFBA",),
        False,
    ),
    (
        "KISAO_0000621",
        ("KISAO_0000621", "STOCHASTIC_SIMULATION_LEAPING_METHOD"),
        "stochastic simulation leaping method",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000622",
        ("KISAO_0000622", "FLUX_BALANCE_METHOD"),
        "flux balance method",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000623",
        ("KISAO_0000623", "FLUX_BALANCE_PROBLEM"),
        "flux balance problem",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000624",
        ("KISAO_0000624", "METHOD_FOR_SOLVING_A_SYSTEM_OF_LINEAR_EQUATIONS"),
        "method for solving a system of linear equations",
        "method for solving a system of linear equations Example system of equations: 3x + 2y - z = 0 2x - 2y + 4z = 0 -x + 1/2y - z = 0",
        (),
        False,
    ),
    (
        "KISAO_0000625",
        ("KISAO_0000625", "DENSE_DIRECT_SOLVER"),
        "dense direct solver",
        None,
        ("denese",),
        False,
    ),
    (
        "KISAO_0000626",
        ("KISAO_0000626", "BAND_DIRECT_SOLVER"),
        "band direct solver",
        None,
        ("banded",),
        False,
    ),
    (
        "KISAO_0000627",
        ("KISAO_0000627", "DIAGONAL_APPROXIMATE_JACOBIAN_SOLVER"),
        "diagonal approximate Jacobian solver",
        None,
        ("diagonal",),
        False,
    ),
    (
        "KISAO_0000628",
        ("KISAO_0000628", "MODELLING_AND_SIMULATION_ALGORITHM_PARAMETER_VALUE"),
        "modelling and simulation algorithm parameter value",
        "A value of a parameter of an algorithm",
        (),
        False,
    ),
    ("KISAO_0000629", ("KISAO_0000629", "NULL"), "null", None, ("none",), False),
    (
        "KISAO_0000630",
        ("KISAO_0000630", "GENERAL_STEADY_STATE_METHOD"),
        "general steady state method",
        "A method looking for a steady state of a dynamic system.",
        ("root-finding method",),
        False,
    ),
    (
        "KISAO_0000631",
        ("KISAO_0000631", "ITERATIVE_ROOT_FINDING_METHOD"),
        "iterative root-finding method",
        "Iterative method for finding the root of a function (f(x) = 0).",
        (),
        False,
    ),
    (
        "KISAO_0000632",
        ("KISAO_0000632", "FUNCTIONAL_ITERATION_ROOT_FINDING_METHOD"),
        "functional iteration root-finding method",
        "Iterative method for finding the root of a function f(x) given by y^{n(m+1)} = h_{n} β_{n,0} f(t_{n}, y^{n(m)}) + a_n This method only involves evaluations of f. This method is suitable for non-stiff functions.",
        (),
        False,
    ),
    (
        "KISAO_0000633",
        ("KISAO_0000633", "COMPUTATIONAL_FUNCTION"),
        "computational function",
        "A mathematical function such as the calculation of a minimum, maximum, or mean of a set of values.",
        (),
        False,
    ),
    (
        "KISAO_0000634",
        ("KISAO_0000634", "SCALED_PROPERTY"),
        "scaled property",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000635",
        ("KISAO_0000635", "UNSCALED_PROPERTY"),
        "unscaled property",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000636",
        ("KISAO_0000636", "PRIMARY_PROPERTY"),
        "primary property",
        "A primary output of a simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000637",
        ("KISAO_0000637", "DERIVED_PROPERTY"),
        "derived property",
        "An output of a simulation which can be derived from its primary outputs.",
        (),
        False,
    ),
    (
        "KISAO_0000638",
        ("KISAO_0000638", "LEVEL"),
        "level",
        "A level such as of a qualitative variable.",
        (),
        False,
    ),
    (
        "KISAO_0000639",
        ("KISAO_0000639", "FLUX"),
        "flux",
        "A rate through an volume such as of a reaction of a constraint-based models.",
        (),
        False,
    ),
    (
        "KISAO_0000640",
        ("KISAO_0000640", "LOWER_BOUND"),
        "lower bound",
        "A lower bound on an estimate of a quantity.",
        (),
        False,
    ),
    (
        "KISAO_0000641",
        ("KISAO_0000641", "BOUND"),
        "bound",
        "An upper or lower bound on an estimate of a quantity.",
        (),
        False,
    ),
    (
        "KISAO_0000642",
        ("KISAO_0000642", "MINIMUM_FLUX"),
        "minimum flux",
        "Minimum possible flux such as computed by flux variability analysis (FVA, KISAO_0000526).",
        (),
        False,
    ),
    (
        "KISAO_0000643",
        ("KISAO_0000643", "UPPER_BOUND"),
        "upper bound",
        "An upper bound on an estimate of a quantity.",
        (),
        False,
    ),
    (
        "KISAO_0000644",
        ("KISAO_0000644", "MAXIMUM_FLUX"),
        "maximum flux",
        "Maximum possible flux such as computed by flux variability analysis (FVA, KISAO_0000526).",
        (),
        False,
    ),
    (
        "KISAO_0000645",
        ("KISAO_0000645", "OBJECTIVE_VALUE"),
        "objective value",
        "Value of an objective function such as of a constraint-based model.",
        (),
        False,
    ),
    (
        "KISAO_0000646",
        ("KISAO_0000646", "PROPENSITY"),
        "propensity",
        "Tendency of an event such as of the firing of a reaction in the stochastic simulation algorithm (SSA, KISAO_0000029).",
        (),
        False,
    ),
    (
        "KISAO_0000647",
        ("KISAO_0000647", "DERIVATIVE"),
        "derivative",
        "Rate of change of a variable with respect to another variable.",
        (),
        False,
    ),
    (
        "KISAO_0000648",
        ("KISAO_0000648", "STEP"),
        "step",
        "Iteration such as along a pseudo timecourse of a logical simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000649",
        ("KISAO_0000649", "SHADOW_PRICE"),
        "shadow price",
        "Change, per infinitesimal unit of the constraint, in the optimal value of the objective function of an optimization problem obtained by relaxing the constraint.",
        (),
        False,
    ),
    (
        "KISAO_0000650",
        ("KISAO_0000650", "SENSITIVITY"),
        "sensitivity",
        "The sensitivity of a variable to another variable, such as the derivative a variable with respect to another.",
        (),
        False,
    ),
    (
        "KISAO_0000651",
        ("KISAO_0000651", "REDUCED_COSTS"),
        "reduced costs",
        "The amount by which an objective function coefficient would have to improve before it would be possible for a corresponding variable to assume a positive value in the optimal solution.",
        (),
        False,
    ),
    (
        "KISAO_0000652",
        ("KISAO_0000652", "CONCENTRATION_RATE"),
        "concentration rate",
        "Rate of a process relative to a volume, such as the rate of a reaction in molar^-1 s^-1.",
        (),
        False,
    ),
    (
        "KISAO_0000653",
        ("KISAO_0000653", "PARTICLE_NUMBER_RATE"),
        "particle number rate",
        "Rate of a process in extensive/absolute units such as mole reactions per second.",
        (),
        False,
    ),
    (
        "KISAO_0000654",
        ("KISAO_0000654", "AMOUNT_RATE"),
        "amount rate",
        "rate of a process in extensive/absolute units such as reactions per second.",
        (),
        False,
    ),
    (
        "KISAO_0000655",
        ("KISAO_0000655", "RATE"),
        "rate",
        "Speed at which a process is occuring such as the temporal rate of a chemical reaction,",
        (),
        False,
    ),
    (
        "KISAO_0000656",
        ("KISAO_0000656", "USE_ADAPTIVE_TIME_STEPS"),
        "use adaptive time steps",
        "Whether an algorithm should use adaptive or fixed time steps.",
        (),
        False,
    ),
    (
        "KISAO_0000657",
        ("KISAO_0000657", "SEQUENTIAL_LOGICAL_SIMULATION_METHOD"),
        "sequential logical simulation method",
        "Qualitative (logical) models specify the evolution rules of their components. In the case of a sequential updating, nodes are updated sequentially in a pre-determined deterministic order.",
        (),
        False,
    ),
    (
        "KISAO_0000658",
        ("KISAO_0000658", "LOGICAL_MODEL_ANALYSIS_METHOD"),
        "logical model analysis method",
        "A method for analyzing a logical model, such as finding its fixed points.",
        (),
        False,
    ),
    (
        "KISAO_0000659",
        ("KISAO_0000659", "NALDI_MDD_LOGICAL_MODEL_STABLE_STATE_SEARCH_METHOD"),
        "Naldi MDD logical model stable state search method",
        "Efficient method for determining the stable states of a regulatory graph using a Multi-valued Decision Diagram (MDD) representation of the logical functions.",
        ("Naldi Multi-valued Decision Diagram stable state search method",),
        False,
    ),
    (
        "KISAO_0000660",
        ("KISAO_0000660", "LOGICAL_MODEL_STABLE_STATE_SEARCH_METHOD"),
        "logical model stable state search method",
        "Method for determining the stable states of a regulatory graph.",
        (),
        False,
    ),
    (
        "KISAO_0000661",
        ("KISAO_0000661", "LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD"),
        "logical model trap space identification method",
        "Method for determining the trap spaces, or stable motifs or symbolic stable states, of a regulatory graph,",
        (),
        False,
    ),
    (
        "KISAO_0000662",
        ("KISAO_0000662", "KLARNER_ASP_LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD"),
        "Klarner ASP logical model trap space identification method",
        "Optimization-based method rooted in answer set programming (ASP) for computing the trap spaces of a regulatory graph.",
        (
            "Klarner Answer Set Programming logical model trap space identification method",
        ),
        False,
    ),
    (
        "KISAO_0000663",
        ("KISAO_0000663", "BDD_LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD"),
        "BDD logical model trap space identification method",
        "Method for determining the trap spaces of a regulatory graph using a Binary Decision Diagram (BDD).",
        ("Binary Decision Diagram logical model trap space identification method",),
        False,
    ),
    (
        "KISAO_0000664",
        ("KISAO_0000664", "SECOND_ORDER_BACKWARD_IMPLICIT_PRODUCT_EULER_SCHEME"),
        "Second order backward implicit product Euler scheme",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000665",
        ("KISAO_0000665", "MAXIMUM_NUMBER_OF_ITERATIONS_FOR_ROOT_FINDING"),
        "maximum number of iterations for root finding",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000666",
        ("KISAO_0000666", "JACOBIAN_EPSILON"),
        "Jacobian epsilon",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000667",
        ("KISAO_0000667", "MEMORY_SIZE"),
        "memory size",
        "Maximum number of points to store in memory, such as in the second order backward implicit product Euler scheme.",
        (),
        False,
    ),
    (
        "KISAO_0000668",
        ("KISAO_0000668", "NUMERICAL_RECIPES_IN_C__STIFF__ROSENBROCK_METHOD"),
        'Numerical Recipes in C "stiff" Rosenbrock method',
        None,
        ("stiff",),
        False,
    ),
    (
        "KISAO_0000669",
        ("KISAO_0000669", "RESOURCE_BALANCE_ANALYSIS"),
        "Resource Balance Analysis",
        None,
        ("RBA",),
        False,
    ),
    (
        "KISAO_0000670",
        ("KISAO_0000670", "USE_MULTIPLE_STEPS"),
        "use multiple steps",
        "Whether to perform a multiple time step simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000671",
        ("KISAO_0000671", "USE_STIFF_METHOD"),
        "use stiff method",
        "Specifies whether the integrator attempts to solve stiff equations.",
        (),
        False,
    ),
    (
        "KISAO_0000672",
        (
            "KISAO_0000672",
            "NUMERICAL_RECIPES_IN_C__QUALITY_CONTROLLED_RUNGE_KUTTA__METHOD",
        ),
        'Numerical Recipes in C "quality-controlled Runge-Kutta" method',
        "Cash-Karp method with step size adjustment.",
        ("rkqs",),
        False,
    ),
    (
        "KISAO_0000673",
        ("KISAO_0000673", "SKIP_REACTIONS_THAT_PRODUCE_NEGATIVE_SPECIES_AMOUNTS"),
        "skip reactions that produce negative species amounts",
        "Parameter which instructs a simulation tool to skip reactions that would result in negative amounts of species.",
        (),
        False,
    ),
    (
        "KISAO_0000674",
        ("KISAO_0000674", "PRESIMULATE"),
        "presimulate",
        "Whether a model should be presimulated prior to analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000675",
        ("KISAO_0000675", "BROYDEN_METHOD"),
        "Broyden method",
        "Family of Quasi-Newton methods for finding roots in k variables originally described by C. G. Broyden in 1965.",
        (),
        False,
    ),
    (
        "KISAO_0000676",
        ("KISAO_0000676", "DEGREE_OF_LINEARITY"),
        "degree of linearity",
        "The degree of linearity of a system.",
        (),
        False,
    ),
    (
        "KISAO_0000677",
        ("KISAO_0000677", "MAXIMUM_NUMBER_OF_STEPS_FOR_PRESIMULATION"),
        "maximum number of steps for presimulation",
        "Maximum number of steps to take in presimulating a model prior to analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000678",
        ("KISAO_0000678", "MAXIMUM_NUMBER_OF_STEPS_FOR_APPROXIMATION"),
        "maximum number of steps for approximation",
        "Maximum number of steps to take in approximating an analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000679",
        ("KISAO_0000679", "MAXIMUM_TIME_FOR_APPROXIMATION"),
        "maximum time for approximation",
        "Maximum amount of time to spend approximating an analysis.",
        (),
        False,
    ),
    (
        "KISAO_0000680",
        ("KISAO_0000680", "DURATION"),
        "duration",
        "Length of time to simulate.",
        (),
        False,
    ),
    (
        "KISAO_0000681",
        ("KISAO_0000681", "MAXIMUM_TIME"),
        "maximum time",
        "Maximum amount of wall time for an operation.",
        (),
        False,
    ),
    (
        "KISAO_0000682",
        ("KISAO_0000682", "ALLOW_APPROXIMATION"),
        "allow approximation",
        "Whether to find an approximate solution if an exact solution could not be found.",
        (),
        False,
    ),
    (
        "KISAO_0000683",
        ("KISAO_0000683", "RELATIVE_TOLERANCE_FOR_APPROXIMATION"),
        "relative tolerance for approximation",
        "Relatative tolerance for an alternative approximate solution to an exact solution which could not be found.",
        (),
        False,
    ),
    (
        "KISAO_0000684",
        ("KISAO_0000684", "NUMBER_OF_STEPS_PER_OUTPUT"),
        "number of steps per output",
        "Number of simulation steps between each simulation output.",
        (),
        False,
    ),
    (
        "KISAO_0000685",
        ("KISAO_0000685", "BIOLOGICAL_STATE_OPTIMIZATION_METHOD"),
        "biological state optimization method",
        "A method for computing the optimal state of a biological system according to a particular objective.",
        (),
        False,
    ),
    (
        "KISAO_0000686",
        ("KISAO_0000686", "ENZYME_COST_MINIMIZATION"),
        "Enzyme Cost Minimization",
        "For a given metabolic network model, the Enzyme Cost Minimization method determines plausible metabolite and enzyme concentrations (which determine thermodynamic forces and enzyme catalytic rates). Fluxes, enzyme kinetic constants, admissible metabolite concentration ranges, and enzyme cost weights (e.g. enzyme molecular masses) are given as input data. The method applies the principle that high enzyme (or enzyme plus metabolite) concentrations must be avoided, and maximizes a weighted sum of enzyme and metabolite concentrations.",
        ("ECM",),
        False,
    ),
    (
        "KISAO_0000687",
        ("KISAO_0000687", "MAX_MIN_DRIVING_FORCE_METHOD"),
        "Max-min Driving Force method",
        "For a given metabolic network model, the MDF method determines plausible metabolite concentrations and thermodynamic forces. Flux directions, equilibrium constants (or equivalently, standard Gibbs free energies of reactions) and admissible metabolite concentration ranges are given as input data. The method applies the principle that low thermodynamic forces must be avoided, and maximizes the minimum thermodynamic force across the entire network.",
        ("MDF",),
        False,
    ),
    (
        "KISAO_0000688",
        ("KISAO_0000688", "TYPE_OF_SYSTEM_DESCRIBED"),
        "type of system described",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000689",
        ("KISAO_0000689", "MATHEMATICAL_SYSTEM"),
        "mathematical system",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000690",
        ("KISAO_0000690", "BIOLOGICAL_SYSTEM"),
        "biological system",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000691",
        ("KISAO_0000691", "METABOLIC_SYSTEM"),
        "metabolic system",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000692",
        ("KISAO_0000692", "CELLULAR_SYSTEM"),
        "cellular system",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000693",
        ("KISAO_0000693", "BIOCHEMICAL_SYSTEM"),
        "biochemical system",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000694",
        ("KISAO_0000694", "ODE_SOLVER"),
        "ODE solver",
        "An ODE solver is the general category of packages such as CVODE-like methods [http://identifiers.org/biomodels.kisao/KISAO_0000433] or Livermore solvers [http://identifiers.org/biomodels.kisao/KISAO_0000094] that solve systems of ordinary differential equations.",
        ("ordinary differential equation solver",),
        False,
    ),
    (
        "KISAO_0000695",
        ("KISAO_0000695", "PARAMETERS_FOR"),
        "parameters for",
        "The children parameters of this term are applied when the parent general term is implented as the more-specific value of this term. For example: a 'parameters for' term might be used as a child of an 'ODE Solver' ([http://identifiers.org/biomodels.kisao/KISAO_0000694]), have a value of 'KISAO_0000019' (CVODE)', and have a child term 'use stiff method' of 'true' ([http://identifiers.org/biomodels.kisao/KISAO_0000671])",
        (),
        False,
    ),
    (
        "KISAO_0000696",
        ("KISAO_0000696", "STEADY_STATE_ROOT_FINDING_PROBLEM"),
        "steady state root-finding problem",
        None,
        ("steady state problem",),
        False,
    ),
    (
        "KISAO_0000697",
        ("KISAO_0000697", "SDE_SOLVER"),
        "SDE solver",
        "An SDE solver is the general category of packages that provide stochastic solutions to a system of differential equations with propensities.",
        ("stochastic differential equation solver",),
        False,
    ),
    (
        "KISAO_0000698",
        ("KISAO_0000698", "PARTICLE_COORDINATES"),
        "particle coordinates",
        "The set of coordinates for all particles of these entities.",
        (),
        False,
    ),
    (
        "KISAO_0000699",
        ("KISAO_0000699", "DAE_SOLVER"),
        "DAE Solver",
        "A DAE solver is the general category of packages such as IDA-like methods [http://identifiers.org/biomodels.kisao/KISAO_0000432] that solve systems of differential algebraic equations (DAEs). DAEs are a superset of ODEs that may additionally contain algebraic equations or 'fast' reactions.",
        ("differential algebraic equation solver",),
        False,
    ),
    (
        "KISAO_0000700",
        ("KISAO_0000700", "LOGICAL_NETWORK"),
        "logical network",
        "A network of logical-valued (an enumeration, such as a set of integers) variables.",
        (),
        False,
    ),
    (
        "KISAO_0000701",
        ("KISAO_0000701", "BOOLEAN_NETWORK"),
        "boolean network",
        "A network of Boolean-valued variables.",
        (),
        False,
    ),
    (
        "KISAO_0000702",
        ("KISAO_0000702", "LOCALLY_MONOTONE_BOOLEAN_NETWORK"),
        "locally-monotone Boolean network",
        "Boolean network where each regulator is either an activator or an inhibitor, but cannot be both.",
        (),
        False,
    ),
    (
        "KISAO_0000703",
        ("KISAO_0000703", "LOGICAL_VARIABLE"),
        "logical variable",
        "A variable whose value can be one of an enumerated set of possible values such as ON/OFF, HIGH/MEDIUM/LOW, or a set integers (e.g., 0, 1, 2).",
        (),
        False,
    ),
    (
        "KISAO_0000704",
        ("KISAO_0000704", "BOOLEAN_VARIABLE"),
        "Boolean variable",
        "A variable whose value can be TRUE/FALSE (e.g., ON/OFF, YES/NO, 1/0).",
        (),
        False,
    ),
    (
        "KISAO_0000705",
        ("KISAO_0000705", "MOST_PERMISSIVE_UPDATING_POLICY"),
        "most permissive updating policy",
        "The most permissive updating policy captures behaviors of any compatible quantitative model.",
        (),
        False,
    ),
    (
        "KISAO_0000706",
        ("KISAO_0000706", "PAULEVÉ_ASP_BASED_FIXED_POINT_IDENTIFICATION"),
        "Paulevé ASP-based fixed point identification",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000707",
        ("KISAO_0000707", "PAULEVÉ_ASP_BASED_MINIMAL_TRAP_SPACE_IDENTIFICATION"),
        "Paulevé ASP-based minimal trap space identification",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000708",
        ("KISAO_0000708", "LOGICAL_MODEL_ATTRACTOR_IDENTIFICATION_METHOD"),
        "logical model attractor identification method",
        None,
        (),
        False,
    ),
    (
        "KISAO_0000709",
        ("KISAO_0000709", "PAULEVÉ_ASP_BASED_MOST_PERMISSIVE_ATTRACTOR_IDENTIFICATION"),
        "Paulevé ASP-based most permissive attractor identification",
        None,
        (),
        False,
    ),
    ("KISAO_0000710", ("KISAO_0000710", "TRAP_SPACE"), "trap space", None, (), False),
    (
        "KISAO_0000711",
        ("KISAO_0000711", "STABLE_STATE"),
        "stable state",
        None,
        ("steady state",),
        False,
    ),
    (
        "KISAO_0000712",
        ("KISAO_0000712", "MINIMAL_TRAP_SPACE"),
        "minimal trap space",
        None,
        (),
        False,
    ),
    ("KISAO_0000713", ("KISAO_0000713", "ATTRACTOR"), "attractor", None, (), False),
    (
        "KISAO_0000800",
        ("KISAO_0000800", "SYSTEMS_PROPERTY"),
        "systems property",
        "A systems-level property of an entire model or simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000801",
        ("KISAO_0000801", "CONCENTRATION_CONTROL_COEFFICIENT_MATRIX__UNSCALED_"),
        "concentration control coefficient matrix (unscaled)",
        "The unscaled concentration control coefficient matrix. The dimensions are species by reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000802",
        ("KISAO_0000802", "CONTROL_COEFFICIENT__SCALED_"),
        "control coefficient (scaled)",
        "A scaled control coefficient of any dependent element (such as a reaction or a floating species) with respect to an independent element (such as a global parameter or boundary species).",
        (),
        False,
    ),
    (
        "KISAO_0000803",
        ("KISAO_0000803", "CONTROL_COEFFICIENT__UNSCALED_"),
        "control coefficient (unscaled)",
        "An unscaled control coefficient of any dependent element (such as a reaction or a floating species) with respect to an independent element (such as a global parameter or boundary species).",
        (),
        False,
    ),
    (
        "KISAO_0000804",
        ("KISAO_0000804", "ELASTICITY_MATRIX__UNSCALED_"),
        "elasticity matrix (unscaled)",
        "The unscaled elasticity matrix. The dimensions are reactions by species.",
        (),
        False,
    ),
    (
        "KISAO_0000805",
        ("KISAO_0000805", "ELASTICITY_COEFFICIENT__UNSCALED_"),
        "elasticity coefficient (unscaled)",
        "An unscaled elasticity coefficient of any reaction with respect to an independent element (such as a global parameter or boundary species).",
        (),
        False,
    ),
    (
        "KISAO_0000806",
        ("KISAO_0000806", "ELASTICITY_MATRIX__SCALED_"),
        "elasticity matrix (scaled)",
        "The scaled elasticity matrix. The dimensions are reactions by species.",
        (),
        False,
    ),
    (
        "KISAO_0000807",
        ("KISAO_0000807", "ELASTICITY_COEFFICIENT__SCALED_"),
        "elasticity coefficient (scaled)",
        "A scaled elasticity coefficient of any reaction with respect to an independent element (such as a global parameter or boundary species).",
        (),
        False,
    ),
    (
        "KISAO_0000808",
        ("KISAO_0000808", "REDUCED_STOICHIOMETRY_MATRIX"),
        "reduced stoichiometry matrix",
        "The reduced stoichiometry matrix. The dimensions are species by reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000809",
        ("KISAO_0000809", "REDUCED_JACOBIAN_MATRIX"),
        "reduced Jacobian matrix",
        "The reduced Jacobian matrix. The dimensions are species by species.",
        (),
        False,
    ),
    (
        "KISAO_0000810",
        ("KISAO_0000810", "REDUCED_EIGENVALUE_MATRIX"),
        "reduced eigenvalue matrix",
        "The reduced eigenvalue matrix of a model. The dimensions are species by two, where the first column is the real part of the eigenvalues, and the second column is the imaginary part of the eigenvalues.",
        (),
        False,
    ),
    (
        "KISAO_0000811",
        ("KISAO_0000811", "STOICHIOMETRY_MATRIX"),
        "stoichiometry matrix",
        "The (full) stoichiometry matrix. The dimensions are species by reactions.",
        ("full stochiometry matrix",),
        False,
    ),
    (
        "KISAO_0000812",
        ("KISAO_0000812", "JACOBIAN_MATRIX"),
        "Jacobian matrix",
        "The (full) Jacobian matrix. The dimensions are species by species.",
        ("full Jacobian matrix",),
        False,
    ),
    (
        "KISAO_0000813",
        ("KISAO_0000813", "EIGENVALUE_MATRIX"),
        "Eigenvalue matrix",
        "The (full) eigenvalue matrix of a model. The dimensions are species by two, where the first column is the real part of the eigenvalues, and the second column is the imaginary part of the eigenvalues.",
        ("full eigenvalue matrix",),
        False,
    ),
    (
        "KISAO_0000814",
        ("KISAO_0000814", "FLUX_CONTROL_COEFFICIENT_MATRIX__UNSCALED_"),
        "flux control coefficient matrix (unscaled)",
        "The unscaled flux control coefficient matrix. The dimensions are reactions by reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000815",
        ("KISAO_0000815", "FLUX_CONTROL_COEFFICIENT_MATRIX__SCALED_"),
        "flux control coefficient matrix (scaled)",
        "The scaled flux control coefficient matrix. The dimensions are reactions by reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000816",
        ("KISAO_0000816", "LINK_MATRIX"),
        "link matrix",
        "The link matrix of a model.",
        (),
        False,
    ),
    (
        "KISAO_0000817",
        ("KISAO_0000817", "KERNEL_MATRIX"),
        "kernel matrix",
        "The Kernel matrix of a model.",
        (),
        False,
    ),
    (
        "KISAO_0000818",
        ("KISAO_0000818", "L0_MATRIX"),
        "L0 matrix",
        "The L0 matrix of a model.",
        (),
        False,
    ),
    (
        "KISAO_0000819",
        ("KISAO_0000819", "NR_MATRIX"),
        "Nr matrix",
        "The Nr matrix of a model.",
        (),
        False,
    ),
    (
        "KISAO_0000820",
        ("KISAO_0000820", "MODEL_AND_SIMULATION_PROPERTY_CHARACTERISTIC"),
        "model and simulation property characteristic",
        "A property of a variable of a model or simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000821",
        ("KISAO_0000821", "INTENSIVE_PROPERTY"),
        "intensive property",
        "An intensive variable such as a concentration or temperature.",
        (),
        False,
    ),
    (
        "KISAO_0000822",
        ("KISAO_0000822", "EXTENSIVE_PROPERTY"),
        "extensive property",
        "An extensive variable such as an amount, particle number, or mass.",
        (),
        False,
    ),
    (
        "KISAO_0000824",
        ("KISAO_0000824", "AGGREGATION_FUNCTION"),
        "aggregation function",
        "A function that aggregates a set of results, reducing its dimension(s). Examples include functions that compute minima or maxima of sets of values.",
        (),
        False,
    ),
    (
        "KISAO_0000825",
        ("KISAO_0000825", "MEAN_IGNORING_NAN"),
        "mean ignoring NaN",
        "The mean (average) of a set of values, ignoring NaN entries.",
        (),
        False,
    ),
    (
        "KISAO_0000826",
        ("KISAO_0000826", "STANDARD_DEVIATION_IGNORING_NAN"),
        "standard deviation ignoring NaN",
        "The standard deviation of a set of values, ignoring NaN entries.",
        (),
        False,
    ),
    (
        "KISAO_0000827",
        ("KISAO_0000827", "STANDARD_ERROR_IGNORING_NAN"),
        "standard error ignoring NaN",
        "The standard error of a set of values, ignoring NaN entries.",
        (),
        False,
    ),
    (
        "KISAO_0000828",
        ("KISAO_0000828", "MAXIMUM_IGNORING_NAN"),
        "maximum ignoring NaN",
        "The maximum value of a set of values, ignoring NaN entries.",
        (),
        False,
    ),
    (
        "KISAO_0000829",
        ("KISAO_0000829", "MINIMUM_IGNORING_NAN"),
        "minimum ignoring NaN",
        "The minimum value of a set of values, ignoring NaN entries.",
        (),
        False,
    ),
    (
        "KISAO_0000830",
        ("KISAO_0000830", "MAXIMUM"),
        "maximum",
        "The maximum of a set of values. If the values contain NaN the maximum is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000831",
        ("KISAO_0000831", "MODEL_AND_SIMULATION_PROPERTY"),
        "model and simulation property",
        "A variable of a model or simulation.",
        (),
        False,
    ),
    (
        "KISAO_0000832",
        ("KISAO_0000832", "TIME"),
        "time",
        "The implied time variable of the model state.",
        (),
        False,
    ),
    (
        "KISAO_0000834",
        ("KISAO_0000834", "RATE_OF_CHANGE"),
        "rate of change",
        "The rate of change of one variable with respect to a second variable.",
        ("rate",),
        False,
    ),
    (
        "KISAO_0000835",
        ("KISAO_0000835", "CONCENTRATION_CONTROL_COEFFICIENT_MATRIX__SCALED_"),
        "concentration control coefficient matrix (scaled)",
        "The scaled concentration control coefficient matrix. The dimensions are species by reactions.",
        (),
        False,
    ),
    (
        "KISAO_0000836",
        ("KISAO_0000836", "AMOUNT"),
        "amount",
        "The extensive quantity amount.",
        (),
        False,
    ),
    (
        "KISAO_0000837",
        ("KISAO_0000837", "PARTICLE_NUMBER"),
        "particle number",
        "The extensive quantity particle number, or, the molar amount of the entity multiplied by Avogadro's number.",
        (),
        False,
    ),
    (
        "KISAO_0000838",
        ("KISAO_0000838", "CONCENTRATION"),
        "concentration",
        "The intensive quantity concentration, or, the amount of the entity with respect to the entity in which it resides.",
        (),
        False,
    ),
    (
        "KISAO_0000839",
        ("KISAO_0000839", "TEMPERATURE"),
        "temperature",
        "The intensive quantity temperature.",
        (),
        False,
    ),
    (
        "KISAO_0000840",
        ("KISAO_0000840", "MINIMUM"),
        "minimum",
        "The minimum of a set of values. If the values contain NaN the minimum is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000841",
        ("KISAO_0000841", "MEAN"),
        "mean",
        "The mean of a set of values. If the values contain NaN the mean is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000842",
        ("KISAO_0000842", "STANDARD_DEVIATION"),
        "standard deviation",
        "The standard deviation of a set of values. If the values contain NaN the standard deviation is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000843",
        ("KISAO_0000843", "STANDARD_ERROR"),
        "standard error",
        "The standard error of a set of values. If the values contain NaN the standard deviation is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000844",
        ("KISAO_0000844", "SUM_IGNORING_NAN"),
        "sum ignoring NaN",
        "The sum of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000845",
        ("KISAO_0000845", "SUM"),
        "sum",
        "The sum of a set of values. If the values contain NaN the sum is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000846",
        ("KISAO_0000846", "PRODUCT_IGNORING_NAN"),
        "product ignoring NaN",
        "The product of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000847",
        ("KISAO_0000847", "PRODUCT"),
        "product",
        "The product of a set of values. If the values contain NaN the product is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000848",
        ("KISAO_0000848", "CUMULATIVE_SUM_IGNORING_NAN"),
        "cumulative sum ignoring NaN",
        "The cumulative sum of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000849",
        ("KISAO_0000849", "CUMULATIVE_SUM"),
        "cumulative sum",
        "The cumulative sum of a set of values. If the values contain NaN the cumulative sum is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000850",
        ("KISAO_0000850", "CUMULATIVE_PRODUCT_IGNORING_NAN"),
        "cumulative product ignoring NaN",
        "The cumulative product of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000851",
        ("KISAO_0000851", "CUMULATIVE_PRODUCT"),
        "cumulative product",
        "The cumulative product of a set of values. If the values contain NaN the cumulative product is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000852",
        ("KISAO_0000852", "COUNT_IGNORING_NAN"),
        "count ignoring NaN",
        "The number of non-zero elements of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000853",
        ("KISAO_0000853", "COUNT"),
        "count",
        "The number of non-zero elements of a set of values. If the values contain NaN the count is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000854",
        ("KISAO_0000854", "LENGTH_IGNORING_NAN"),
        "length ignoring NaN",
        "The number of elements of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000855",
        ("KISAO_0000855", "LENGTH"),
        "length",
        "The number of elements of a set of values.",
        (),
        False,
    ),
    (
        "KISAO_0000856",
        ("KISAO_0000856", "MEDIAN_IGNORING_NAN"),
        "median ignoring NaN",
        "The median of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000857",
        ("KISAO_0000857", "MEDIAN"),
        "median",
        "The median of a set of values. If the values contain NaN the median is NaN.",
        (),
        False,
    ),
    (
        "KISAO_0000858",
        ("KISAO_0000858", "VARIANCE_IGNORING_NAN"),
        "variance ignoring NaN",
        "The variance of a set of values, ignoring Nan entries.",
        (),
        False,
    ),
    (
        "KISAO_0000859",
        ("KISAO_0000859", "VARIANCE"),
        "variance",
        "The variance of a set of values. If the values contain NaN the variance is NaN.",
        (),
        False,
    ),
]

KISAO._register(_terms)

__all__ = [
    "KISAO",
    "KISAOType",
]
