"""KISAO ontology."""

from enum import Enum
from typing import Optional, Union


KISAOType = Union[str, "KISAO"]

_terms = {
    "KISAO_0000000": "modelling and simulation algorithm",
    "KISAO_0000003": "weighted stochastic simulation algorithm",
    "KISAO_0000015": "Gillespie first reaction algorithm",
    "KISAO_0000017": "multi-state agent-based simulation method",
    "KISAO_0000019": "CVODE",
    "KISAO_0000020": "PVODE",
    "KISAO_0000021": "StochSim nearest-neighbour algorithm",
    "KISAO_0000022": "Elf and Ehrenberg method",
    "KISAO_0000027": "Gibson-Bruck next reaction algorithm",
    "KISAO_0000028": "slow-scale stochastic simulation algorithm",
    "KISAO_0000029": "Gillespie direct algorithm",
    "KISAO_0000030": "Euler forward method",
    "KISAO_0000031": "Euler backward method",
    "KISAO_0000032": "explicit fourth-order Runge-Kutta method",
    "KISAO_0000033": "Rosenbrock method",
    "KISAO_0000038": "sorting stochastic simulation algorithm",
    "KISAO_0000039": "tau-leaping method",
    "KISAO_0000040": "Poisson tau-leaping method",
    "KISAO_0000045": "implicit tau-leaping method",
    "KISAO_0000046": "trapezoidal tau-leaping method",
    "KISAO_0000048": "adaptive explicit-implicit tau-leaping method",
    "KISAO_0000051": "Bortz-Kalos-Lebowitz algorithm",
    "KISAO_0000056": "Smoluchowski equation based method",
    "KISAO_0000057": "Brownian diffusion Smoluchowski method",
    "KISAO_0000058": "Greens function reaction dynamics",
    "KISAO_0000064": "Runge-Kutta based method",
    "KISAO_0000068": "deterministic cellular automata update algorithm",
    "KISAO_0000071": "LSODE",
    "KISAO_0000074": "binomial tau-leaping method",
    "KISAO_0000075": "Gillespie multi-particle method",
    "KISAO_0000076": "Stundzia and Lumsden method",
    "KISAO_0000081": "estimated midpoint tau-leaping method",
    "KISAO_0000082": "k-alpha leaping method",
    "KISAO_0000084": "nonnegative Poisson tau-leaping method",
    "KISAO_0000086": "Fehlberg method",
    "KISAO_0000087": "Dormand-Prince method",
    "KISAO_0000088": "LSODA",
    "KISAO_0000089": "LSODAR",
    "KISAO_0000090": "LSODI",
    "KISAO_0000091": "LSODIS",
    "KISAO_0000093": "LSODPK",
    "KISAO_0000094": "Livermore solver",
    "KISAO_0000095": "sub-volume stochastic reaction-diffusion algorithm",
    "KISAO_0000097": "modelling and simulation algorithm characteristic",
    "KISAO_0000098": "type of variable",
    "KISAO_0000099": "type of system behaviour",
    "KISAO_0000100": "type of progression time step",
    "KISAO_0000102": "spatial description",
    "KISAO_0000103": "deterministic system behaviour",
    "KISAO_0000104": "stochastic system behaviour",
    "KISAO_0000105": "discrete variable",
    "KISAO_0000106": "continuous variable",
    "KISAO_0000107": "progression with adaptive time step",
    "KISAO_0000108": "progression with fixed time step",
    "KISAO_0000201": "modelling and simulation algorithm parameter",
    "KISAO_0000203": "particle number lower limit",
    "KISAO_0000204": "particle number upper limit",
    "KISAO_0000205": "partitioning interval",
    "KISAO_0000209": "relative tolerance",
    "KISAO_0000211": "absolute tolerance",
    "KISAO_0000216": "use reduced model",
    "KISAO_0000219": "maximum Adams order",
    "KISAO_0000220": "maximum BDF order",
    "KISAO_0000223": "number of history bins",
    "KISAO_0000228": "tau-leaping epsilon",
    "KISAO_0000230": "minimum reactions per leap",
    "KISAO_0000231": "Pahle hybrid method",
    "KISAO_0000232": "LSOIBT",
    "KISAO_0000233": "LSODES",
    "KISAO_0000234": "LSODKR",
    "KISAO_0000235": "type of solution",
    "KISAO_0000236": "exact solution",
    "KISAO_0000237": "approximate solution",
    "KISAO_0000238": "type of method",
    "KISAO_0000239": "explicit method type",
    "KISAO_0000240": "implicit method type",
    "KISAO_0000241": "Gillespie-like method",
    "KISAO_0000242": "error control parameter",
    "KISAO_0000243": "method switching control parameter",
    "KISAO_0000244": "granularity control parameter",
    "KISAO_0000245": "has characteristic",
    "KISAO_0000246": "is hybrid of",
    "KISAO_0000248": "tau-leaping delta",
    "KISAO_0000249": "critical firing threshold",
    "KISAO_0000250": "is parameter of",
    "KISAO_0000252": "partitioning control parameter",
    "KISAO_0000253": "coarse-graining factor",
    "KISAO_0000254": "Brownian diffusion accuracy",
    "KISAO_0000255": "molecules per virtual box",
    "KISAO_0000256": "virtual box side length",
    "KISAO_0000257": "surface-bound epsilon",
    "KISAO_0000258": "neighbour distance",
    "KISAO_0000259": "has parameter",
    "KISAO_0000260": "virtual box size",
    "KISAO_0000261": "Euler method",
    "KISAO_0000263": "NFSim agent-based simulation method",
    "KISAO_0000264": "cellular automata update method",
    "KISAO_0000268": "is characteristic of",
    "KISAO_0000273": "hard-particle molecular dynamics",
    "KISAO_0000274": "first-passage Monte Carlo algorithm",
    "KISAO_0000276": "Gill method",
    "KISAO_0000278": "Metropolis Monte Carlo algorithm",
    "KISAO_0000279": "Adams-Bashforth method",
    "KISAO_0000280": "Adams-Moulton method",
    "KISAO_0000281": "multistep method",
    "KISAO_0000282": "KINSOL",
    "KISAO_0000283": "IDA",
    "KISAO_0000285": "finite volume method",
    "KISAO_0000286": "Euler-Maruyama method",
    "KISAO_0000287": "Milstein method",
    "KISAO_0000288": "backward differentiation formula",
    "KISAO_0000289": "Adams method",
    "KISAO_0000290": "Merson method",
    "KISAO_0000296": "Hammer-Hollingsworth method",
    "KISAO_0000297": "Lobatto method",
    "KISAO_0000299": "Butcher-Kuntzmann method",
    "KISAO_0000301": "Heun method",
    "KISAO_0000302": "embedded Runge-Kutta method",
    "KISAO_0000303": "Zonneveld method",
    "KISAO_0000304": "Radau method",
    "KISAO_0000305": "Verner method",
    "KISAO_0000306": "Lagrangian sliding fluid element algorithm",
    "KISAO_0000307": "finite difference method",
    "KISAO_0000308": "MacCormack method",
    "KISAO_0000309": "Crank-Nicolson method",
    "KISAO_0000310": "method of lines",
    "KISAO_0000311": "type of domain geometry handling",
    "KISAO_0000314": "S-System power-law canonical differential equations solver",
    "KISAO_0000315": "lattice gas automata",
    "KISAO_0000316": "enhanced Greens function reaction dynamics",
    "KISAO_0000317": "E-Cell multi-algorithm simulation method",
    "KISAO_0000318": "Gauss-Legendre Runge-Kutta method",
    "KISAO_0000319": "Monte Carlo method",
    "KISAO_0000320": "BioRica hybrid method",
    "KISAO_0000321": "Cash-Karp method",
    "KISAO_0000322": "hybridity",
    "KISAO_0000323": "equation-free probabilistic steady-state approximation",
    "KISAO_0000324": "nested stochastic simulation algorithm",
    "KISAO_0000325": "minimum fast/discrete reaction occurrences number",
    "KISAO_0000326": "number of samples",
    "KISAO_0000327": "maximum discrete number",
    "KISAO_0000328": "minimum fast rate",
    "KISAO_0000329": "constant-time kinetic Monte Carlo algorithm",
    "KISAO_0000330": "R-leaping algorithm",
    "KISAO_0000331": "exact R-leaping algorithm",
    "KISAO_0000332": "ER-leap initial leap",
    "KISAO_0000333": "accelerated stochastic simulation algorithm",
    "KISAO_0000334": "multiparticle lattice gas automata",
    "KISAO_0000335": "generalized stochastic simulation algorithm",
    "KISAO_0000336": "D-leaping method",
    "KISAO_0000337": "finite element method",
    "KISAO_0000338": "h-version of the finite element method",
    "KISAO_0000339": "p-version of the finite element method",
    "KISAO_0000340": "h-p version of the finite element method",
    "KISAO_0000341": "mixed finite element method",
    "KISAO_0000342": "level set method",
    "KISAO_0000343": "generalized finite element method",
    "KISAO_0000345": "h-p cloud method",
    "KISAO_0000346": "mesh-based geometry handling",
    "KISAO_0000347": "meshless geometry handling",
    "KISAO_0000348": "extended finite element method",
    "KISAO_0000349": "method of finite spheres",
    "KISAO_0000350": "probability-weighted dynamic Monte Carlo method",
    "KISAO_0000351": "multinomial tau-leaping method",
    "KISAO_0000352": "hybrid method",
    "KISAO_0000353": "generalized minimal residual algorithm",
    "KISAO_0000354": "Krylov subspace projection method",
    "KISAO_0000355": "DASPK",
    "KISAO_0000356": "DASSL",
    "KISAO_0000357": "conjugate gradient method",
    "KISAO_0000358": "biconjugate gradient method",
    "KISAO_0000359": "is similar to",
    "KISAO_0000360": "uses",
    "KISAO_0000361": "is generalization of",
    "KISAO_0000362": "implicit-state Doob-Gillespie algorithm",
    "KISAO_0000363": "rule-based simulation method",
    "KISAO_0000364": "Adams predictor-corrector method",
    "KISAO_0000365": "NDSolve method",
    "KISAO_0000366": "symplecticness",
    "KISAO_0000367": "partitioned Runge-Kutta method",
    "KISAO_0000369": "partial differential equation discretization method",
    "KISAO_0000370": "type of problem",
    "KISAO_0000371": "stochastic differential equation problem",
    "KISAO_0000372": "partial differential equation problem",
    "KISAO_0000373": "differential-algebraic equation problem",
    "KISAO_0000374": "ordinary differential equation problem",
    "KISAO_0000375": "delay differential equation problem",
    "KISAO_0000376": "linearity of equation",
    "KISAO_0000377": "one-step method",
    "KISAO_0000378": "implicit midpoint rule",
    "KISAO_0000379": "Bulirsch-Stoer algorithm",
    "KISAO_0000380": "Richardson extrapolation based method",
    "KISAO_0000381": "midpoint method",
    "KISAO_0000382": "modified midpoint method",
    "KISAO_0000383": "Bader-Deuflhard method",
    "KISAO_0000384": "semi-implicit midpoint rule",
    "KISAO_0000386": "scaled preconditioned generalized minimal residual method",
    "KISAO_0000388": "minimal residual method",
    "KISAO_0000389": "quasi-minimal residual method",
    "KISAO_0000392": "biconjugate gradient stabilized method",
    "KISAO_0000393": "ingenious conjugate gradients-squared method",
    "KISAO_0000394": "quasi-minimal residual variant of biconjugate gradient stabilized method",
    "KISAO_0000395": "improved biconjugate gradient method",
    "KISAO_0000396": "transpose-free quasi-minimal residual algorithm",
    "KISAO_0000397": "preconditioning technique",
    "KISAO_0000398": "iterative method for solving a system of linear equations",
    "KISAO_0000399": "is used by",
    "KISAO_0000403": "homogeneousness of equation",
    "KISAO_0000404": "symmetricity of matrix",
    "KISAO_0000405": "type of differential equation",
    "KISAO_0000407": "steady state method",
    "KISAO_0000408": "Newton-type method",
    "KISAO_0000409": "ordinary Newton method",
    "KISAO_0000410": "simlified Newton method",
    "KISAO_0000411": "Newton-like method",
    "KISAO_0000412": "inexact Newton method",
    "KISAO_0000413": "exact Newton method",
    "KISAO_0000415": "maximum number of steps",
    "KISAO_0000416": "partial least squares regression method",
    "KISAO_0000417": "hierarchical cluster-based partial least squares regression method",
    "KISAO_0000418": "N-way partial least squares regression method",
    "KISAO_0000419": "metamodelling method",
    "KISAO_0000420": "number of partial least squares components",
    "KISAO_0000421": "type of validation",
    "KISAO_0000422": "number of N-way partial least squares regression factors",
    "KISAO_0000423": "partial least squares regression-like method",
    "KISAO_0000424": "mean-centring of variables",
    "KISAO_0000425": "standardising of variables",
    "KISAO_0000427": "number of clusters",
    "KISAO_0000428": "matrix for clusterization",
    "KISAO_0000429": "clusterization parameter",
    "KISAO_0000430": "variables preprocessing parameter",
    "KISAO_0000432": "IDA-like method",
    "KISAO_0000433": "CVODE-like method",
    "KISAO_0000434": "Higham-Hall method",
    "KISAO_0000435": "embedded Runge-Kutta 5(4) method",
    "KISAO_0000436": "Dormand-Prince 8(5,3) method",
    "KISAO_0000437": "flux balance analysis",
    "KISAO_0000447": "COAST",
    "KISAO_0000448": "logical model simulation method",
    "KISAO_0000449": "synchronous logical model simulation method",
    "KISAO_0000450": "asynchronous logical model simulation method",
    "KISAO_0000451": "type of updating policy",
    "KISAO_0000452": "random updating policy",
    "KISAO_0000453": "ordered updating policy",
    "KISAO_0000454": "constant updating policy",
    "KISAO_0000455": "prioritized updating policy",
    "KISAO_0000467": "maximum step size",
    "KISAO_0000468": "maximal timestep method",
    "KISAO_0000469": "maximal timestep",
    "KISAO_0000470": "optimization algorithm",
    "KISAO_0000471": "local optimization algorithm",
    "KISAO_0000472": "global optimization algorithm",
    "KISAO_0000473": "Bayesian inference algorithm",
    "KISAO_0000475": "integration method",
    "KISAO_0000476": "iteration type",
    "KISAO_0000477": "linear solver",
    "KISAO_0000478": "preconditioner",
    "KISAO_0000479": "upper half-bandwidth",
    "KISAO_0000480": "lower half-bandwidth",
    "KISAO_0000481": "interpolate solution",
    "KISAO_0000482": "half-bandwith parameter",
    "KISAO_0000483": "step size",
    "KISAO_0000484": "maximum order",
    "KISAO_0000485": "minimum step size",
    "KISAO_0000486": "maximum iterations",
    "KISAO_0000487": "minimum damping",
    "KISAO_0000488": "seed",
    "KISAO_0000491": "discrete event simulation algorithm",
    "KISAO_0000492": "asynchronous updating policy",
    "KISAO_0000493": "synchronous updating policy",
    "KISAO_0000494": "fully asynchronous updating policy",
    "KISAO_0000495": "random asynchronous updating policy",
    "KISAO_0000496": "CVODES",
    "KISAO_0000497": "KLU",
    "KISAO_0000498": "number of runs",
    "KISAO_0000499": "dynamic flux balance analysis",
    "KISAO_0000500": "SOA-DFBA",
    "KISAO_0000501": "DOA-DFBA",
    "KISAO_0000502": "DA-DFBA",
    "KISAO_0000503": "simulated annealing",
    "KISAO_0000504": "random search",
    "KISAO_0000505": "particle swarm",
    "KISAO_0000506": "genetic algorithm",
    "KISAO_0000507": "genetic algorithm SR",
    "KISAO_0000508": "evolutionary programming",
    "KISAO_0000509": "evolutionary strategy",
    "KISAO_0000510": "truncated Newton",
    "KISAO_0000511": "steepest descent",
    "KISAO_0000512": "praxis",
    "KISAO_0000513": "NL2SOL",
    "KISAO_0000514": "Nelder-Mead",
    "KISAO_0000515": "Levenberg-Marquardt",
    "KISAO_0000516": "Hooke&Jeeves",
    "KISAO_0000517": "number of generations",
    "KISAO_0000518": "evolutionary algorithm parameter",
    "KISAO_0000519": "population size",
    "KISAO_0000520": "evolutionary algorithm",
    "KISAO_0000521": "simulated annealing parameter",
    "KISAO_0000522": "start temperature",
    "KISAO_0000523": "cooling factor",
    "KISAO_0000524": "partitioned leaping method",
    "KISAO_0000525": "stop condition",
    "KISAO_0000526": "flux variability analysis",
    "KISAO_0000527": "geometric flux balance analysis",
    "KISAO_0000528": "parsimonious enzyme usage flux balance analysis (minimum sum of absolute fluxes)",
    "KISAO_0000529": "parallelism",
    "KISAO_0000531": "fraction of optimum",
    "KISAO_0000532": "loopless",
    "KISAO_0000533": "pFBA factor",
    "KISAO_0000534": "reactions",
    "KISAO_0000535": "VODE",
    "KISAO_0000536": "ZVODE",
    "KISAO_0000537": "explicit Runge-Kutta method of order 3(2)",
    "KISAO_0000538": "safety factor on new step selection",
    "KISAO_0000539": "minimum factor to change step size by",
    "KISAO_0000540": "maximum factor to change step size by",
    "KISAO_0000541": "beta parameter for stabilized step size control",
    "KISAO_0000542": "correction step should use internally generated full Jacobian",
    "KISAO_0000543": "stability limit detection flag",
    "KISAO_0000544": "IDAS",
    "KISAO_0000545": "include sensitivity variables in error control mechanism",
    "KISAO_0000546": "convex optimization algorithm",
    "KISAO_0000547": "linear programming",
    "KISAO_0000548": "quadratic programming",
    "KISAO_0000549": "non-linear programming",
    "KISAO_0000550": "simplex method",
    "KISAO_0000551": "primal-dual interior point method",
    "KISAO_0000552": "optimization method",
    "KISAO_0000553": "optimization solver",
    "KISAO_0000554": "parsimonius flux balance analysis (minimum number of active fluxes)",
    "KISAO_0000555": "absolute quadrature tolerance",
    "KISAO_0000556": "relative quadrature tolerance",
    "KISAO_0000557": "absolute steady-state tolerance",
    "KISAO_0000558": "relative steady-state tolerance",
    "KISAO_0000559": "initial step size",
    "KISAO_0000560": "LSODA/LSODAR hybrid method",
    "KISAO_0000561": "Pahle hybrid Gibson-Bruck Next Reaction method/Runge-Kutta method",
    "KISAO_0000562": "Pahle hybrid Gibson-Bruck Next Reaction method/LSODA method",
    "KISAO_0000563": "Pahle hybrid Gibson-Bruck Next Reaction method/RK-45 method",
    "KISAO_0000564": "stochastic Runge-Kutta method",
    "KISAO_0000565": "absolute tolerance for root finding",
    "KISAO_0000566": "stochastic second order Runge-Kutta method",
    "KISAO_0000567": "force physical correctness",
    "KISAO_0000568": "NLEQ1",
    "KISAO_0000569": "NLEQ2",
    "KISAO_0000570": "auto reduce tolerances",
    "KISAO_0000571": "absolute tolerance adjustment factor",
    "KISAO_0000572": "level of superimposed noise",
    "KISAO_0000573": "probabilistic logical model simulation method",
    "KISAO_0000574": "species transition probabilities",
    "KISAO_0000575": "hybrid tau-leaping method",
    "KISAO_0000576": "quadratic MOMA",
    "KISAO_0000577": "flux minimization weight",
    "KISAO_0000578": "nested algorithm",
    "KISAO_0000579": "linear MOMA",
    "KISAO_0000580": "ROOM",
    "KISAO_0000581": "BKMC",
    "KISAO_0000582": "Spatiocyte method",
    "KISAO_0000583": "minimum order",
    "KISAO_0000584": "initial order",
    "KISAO_0000585": "TOMS731",
    "KISAO_0000586": "Gibson-Bruck next reaction algorithm with indexed priority queue",
    "KISAO_0000587": "IMEX",
    "KISAO_0000588": "flux sampling",
    "KISAO_0000589": "ACB flux sampling method",
    "KISAO_0000590": "ACHR flux sampling method",
    "KISAO_0000591": "mdFBA",
    "KISAO_0000592": "dynamic rFBA",
    "KISAO_0000593": "MOMA",
    "KISAO_0000594": "order",
    "KISAO_0000595": "rFBA",
    "KISAO_0000596": "srFBA",
    "KISAO_0000597": "tolerance",
    "KISAO_0000598": "hybrid Gibson - Milstein method",
    "KISAO_0000599": "hybrid Gibson - Euler-Maruyama method",
    "KISAO_0000600": "hybrid adaptive Gibson - Milstein method",
    "KISAO_0000601": "number of trials",
    "KISAO_0000602": "minimum species threshold for continuous approximation",
    "KISAO_0000603": "minimum reaction rate for continuous approximation",
    "KISAO_0000604": "MSR tolerance",
    "KISAO_0000605": "SDE tolerance",
    "KISAO_0000606": "hierarchical stochastic simulation algorithm",
    "KISAO_0000607": "hierarchical Fehlberg method",
    "KISAO_0000608": "hierarchical flux balance analysis",
    "KISAO_0000609": "embedded Runge-Kutta Prince-Dormand (8,9) method",
    "KISAO_0000610": "composite-rejection stochastic simulation algorithm",
    "KISAO_0000611": "incremental stochastic simulation algorithm",
    "KISAO_0000612": "implicit 4th order Runge-Kutta method at Gaussian points",
    "KISAO_0000613": "stochastic simulation algorithm with normally-distributed next reaction times",
    "KISAO_0000614": "implementation",
    "KISAO_0000615": "fully-implicit regular grid finite volume method with a variable time step",
    "KISAO_0000616": "semi-implicit regular grid finite volume method with a fixed time step",
    "KISAO_0000617": "IDA-CVODE hybrid method",
    "KISAO_0000618": "bunker",
    "KISAO_0000619": "emc-sim",
    "KISAO_0000620": "parsimonius flux balance analysis",
    "KISAO_0000621": "stochastic simulation leaping method",
    "KISAO_0000622": "flux balance method",
    "KISAO_0000623": "flux balance problem",
    "KISAO_0000624": "method for solving a system of linear equations",
    "KISAO_0000625": "dense direct solver",
    "KISAO_0000626": "band direct solver",
    "KISAO_0000627": "diagonal approximate Jacobian solver",
    "KISAO_0000628": "modelling and simulation algorithm parameter value",
    "KISAO_0000629": "null",
    "KISAO_0000630": "root-finding method",
    "KISAO_0000631": "iterative root-finding method",
    "KISAO_0000632": "functional iteration root-finding method",
    "KISAO_0000633": "computational function",
    "KISAO_0000634": "scaled property",
    "KISAO_0000635": "unscaled property",
    "KISAO_0000636": "primary property",
    "KISAO_0000637": "derived property",
    "KISAO_0000638": "level",
    "KISAO_0000639": "flux",
    "KISAO_0000640": "lower bound",
    "KISAO_0000641": "bound",
    "KISAO_0000642": "minimum flux",
    "KISAO_0000643": "upper bound",
    "KISAO_0000644": "maximum flux",
    "KISAO_0000645": "objective value",
    "KISAO_0000646": "propensity",
    "KISAO_0000647": "derivative",
    "KISAO_0000648": "step",
    "KISAO_0000649": "shadow price",
    "KISAO_0000650": "sensitivity",
    "KISAO_0000651": "reduced costs",
    "KISAO_0000652": "concentration rate",
    "KISAO_0000653": "particle number rate",
    "KISAO_0000654": "amount rate",
    "KISAO_0000655": "rate",
    "KISAO_0000656": "use adaptive time steps",
    "KISAO_0000657": "sequential logical simulation method",
    "KISAO_0000658": "logical model analysis method",
    "KISAO_0000659": "Naldi MDD logical model stable state search method",
    "KISAO_0000660": "logical model stable state search method",
    "KISAO_0000661": "logical model trap space identification method",
    "KISAO_0000662": "Klarner ASP logical model trap space identification method",
    "KISAO_0000663": "BDD logical model trap space identification method",
    "KISAO_0000664": "Second order backward implicit product Euler scheme",
    "KISAO_0000665": "maximum number of iterations for root finding",
    "KISAO_0000666": "Jacobian epsilon",
    "KISAO_0000667": "memory size",
    "KISAO_0000668": "Numerical Recipes in C 'stiff' Rosenbrock method",
    "KISAO_0000669": "Resource Balance Analysis",
    "KISAO_0000670": "use multiple steps",
    "KISAO_0000671": "use stiff method",
    "KISAO_0000672": "Numerical Recipes in C 'quality-controlled Runge-Kutta' method",
    "KISAO_0000673": "skip reactions that produce negative species amounts",
    "KISAO_0000674": "presimulate",
    "KISAO_0000675": "Broyden method",
    "KISAO_0000676": "degree of linearity",
    "KISAO_0000677": "maximum number of steps for presimulation",
    "KISAO_0000678": "maximum number of steps for approximation",
    "KISAO_0000679": "maximum time for approximation",
    "KISAO_0000680": "duration",
    "KISAO_0000681": "maximum time",
    "KISAO_0000682": "allow approximation",
    "KISAO_0000683": "relative tolerance for approximation",
    "KISAO_0000684": "number of steps per output",
    "KISAO_0000685": "biological state optimization method",
    "KISAO_0000686": "Enzyme Cost Minimization",
    "KISAO_0000687": "Max-min Driving Force method",
    "KISAO_0000688": "type of system described",
    "KISAO_0000689": "mathematical system",
    "KISAO_0000690": "biological system",
    "KISAO_0000691": "metabolic system",
    "KISAO_0000692": "cellular system",
    "KISAO_0000693": "biochemical system",
    "KISAO_0000800": "systems property",
    "KISAO_0000801": "concentration control coefficient matrix (unscaled)",
    "KISAO_0000802": "control coefficient (scaled)",
    "KISAO_0000803": "control coefficient (unscaled)",
    "KISAO_0000804": "elasticity matrix (unscaled)",
    "KISAO_0000805": "elasticity coefficient (unscaled)",
    "KISAO_0000806": "elasticity matrix (scaled)",
    "KISAO_0000807": "elasticity coefficient (scaled)",
    "KISAO_0000808": "reduced stoichiometry matrix",
    "KISAO_0000809": "reduced Jacobian matrix",
    "KISAO_0000810": "reduced eigenvalue matrix",
    "KISAO_0000811": "stoichiometry matrix",
    "KISAO_0000812": "Jacobian matrix",
    "KISAO_0000813": "Eigenvalue matrix",
    "KISAO_0000814": "flux control coefficient matrix (unscaled)",
    "KISAO_0000815": "flux control coefficient matrix (scaled)",
    "KISAO_0000816": "link matrix",
    "KISAO_0000817": "kernel matrix",
    "KISAO_0000818": "L0 matrix",
    "KISAO_0000819": "Nr matrix",
    "KISAO_0000820": "model and simulation property characteristic",
    "KISAO_0000821": "intensive property",
    "KISAO_0000822": "extensive property",
    "KISAO_0000824": "aggregation function",
    "KISAO_0000825": "mean ignoring NaN",
    "KISAO_0000826": "standard deviation ignoring NaN",
    "KISAO_0000827": "standard error ignoring NaN",
    "KISAO_0000828": "maximum ignoring NaN",
    "KISAO_0000829": "minimum ignoring NaN",
    "KISAO_0000830": "maximum",
    "KISAO_0000831": "model and simulation property",
    "KISAO_0000832": "time",
    "KISAO_0000834": "rate of change",
    "KISAO_0000835": "concentration control coefficient matrix (scaled)",
    "KISAO_0000836": "amount",
    "KISAO_0000837": "particle number",
    "KISAO_0000838": "concentration",
    "KISAO_0000839": "temperature",
    "KISAO_0000840": "minimum",
    "KISAO_0000841": "mean",
    "KISAO_0000842": "standard deviation",
    "KISAO_0000843": "standard error",
    "KISAO_0000844": "sum ignoring NaN",
    "KISAO_0000845": "sum",
    "KISAO_0000846": "product ignoring NaN",
    "KISAO_0000847": "product",
    "KISAO_0000848": "cumulative sum ignoring NaN",
    "KISAO_0000849": "cumulative sum",
    "KISAO_0000850": "cumulative product ignoring NaN",
    "KISAO_0000851": "cumulative product",
    "KISAO_0000852": "count ignoring NaN",
    "KISAO_0000853": "count",
    "KISAO_0000854": "length ignoring NaN",
    "KISAO_0000855": "length",
    "KISAO_0000856": "median ignoring NaN",
    "KISAO_0000857": "median",
    "KISAO_0000858": "variance ignoring NaN",
    "KISAO_0000859": "variance",
}

pattern = r"^KISAO_\d{7}$"


class KISAO(str, Enum):
    """Enum for KISAO ontology."""

    # modelling and simulation algorithm
    KISAO_0000000 = "KISAO_0000000"
    MODELLING_AND_SIMULATION_ALGORITHM = "KISAO_0000000"

    # weighted stochastic simulation algorithm
    KISAO_0000003 = "KISAO_0000003"
    WEIGHTED_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000003"

    # Gillespie first reaction algorithm
    KISAO_0000015 = "KISAO_0000015"
    GILLESPIE_FIRST_REACTION_ALGORITHM = "KISAO_0000015"

    # multi-state agent-based simulation method
    KISAO_0000017 = "KISAO_0000017"
    MULTI_STATE_AGENT_BASED_SIMULATION_METHOD = "KISAO_0000017"

    # CVODE
    KISAO_0000019 = "KISAO_0000019"
    CVODE = "KISAO_0000019"

    # PVODE
    KISAO_0000020 = "KISAO_0000020"
    PVODE = "KISAO_0000020"

    # StochSim nearest-neighbour algorithm
    KISAO_0000021 = "KISAO_0000021"
    STOCHSIM_NEAREST_NEIGHBOUR_ALGORITHM = "KISAO_0000021"

    # Elf and Ehrenberg method
    KISAO_0000022 = "KISAO_0000022"
    ELF_AND_EHRENBERG_METHOD = "KISAO_0000022"

    # Gibson-Bruck next reaction algorithm
    KISAO_0000027 = "KISAO_0000027"
    GIBSON_BRUCK_NEXT_REACTION_ALGORITHM = "KISAO_0000027"

    # slow-scale stochastic simulation algorithm
    KISAO_0000028 = "KISAO_0000028"
    SLOW_SCALE_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000028"

    # Gillespie direct algorithm
    KISAO_0000029 = "KISAO_0000029"
    GILLESPIE_DIRECT_ALGORITHM = "KISAO_0000029"

    # Euler forward method
    KISAO_0000030 = "KISAO_0000030"
    EULER_FORWARD_METHOD = "KISAO_0000030"

    # Euler backward method
    KISAO_0000031 = "KISAO_0000031"
    EULER_BACKWARD_METHOD = "KISAO_0000031"

    # explicit fourth-order Runge-Kutta method
    KISAO_0000032 = "KISAO_0000032"
    EXPLICIT_FOURTH_ORDER_RUNGE_KUTTA_METHOD = "KISAO_0000032"

    # Rosenbrock method
    KISAO_0000033 = "KISAO_0000033"
    ROSENBROCK_METHOD = "KISAO_0000033"

    # sorting stochastic simulation algorithm
    KISAO_0000038 = "KISAO_0000038"
    SORTING_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000038"

    # tau-leaping method
    KISAO_0000039 = "KISAO_0000039"
    TAU_LEAPING_METHOD = "KISAO_0000039"

    # Poisson tau-leaping method
    KISAO_0000040 = "KISAO_0000040"
    POISSON_TAU_LEAPING_METHOD = "KISAO_0000040"

    # implicit tau-leaping method
    KISAO_0000045 = "KISAO_0000045"
    IMPLICIT_TAU_LEAPING_METHOD = "KISAO_0000045"

    # trapezoidal tau-leaping method
    KISAO_0000046 = "KISAO_0000046"
    TRAPEZOIDAL_TAU_LEAPING_METHOD = "KISAO_0000046"

    # adaptive explicit-implicit tau-leaping method
    KISAO_0000048 = "KISAO_0000048"
    ADAPTIVE_EXPLICIT_IMPLICIT_TAU_LEAPING_METHOD = "KISAO_0000048"

    # Bortz-Kalos-Lebowitz algorithm
    KISAO_0000051 = "KISAO_0000051"
    BORTZ_KALOS_LEBOWITZ_ALGORITHM = "KISAO_0000051"

    # Smoluchowski equation based method
    KISAO_0000056 = "KISAO_0000056"
    SMOLUCHOWSKI_EQUATION_BASED_METHOD = "KISAO_0000056"

    # Brownian diffusion Smoluchowski method
    KISAO_0000057 = "KISAO_0000057"
    BROWNIAN_DIFFUSION_SMOLUCHOWSKI_METHOD = "KISAO_0000057"

    # Greens function reaction dynamics
    KISAO_0000058 = "KISAO_0000058"
    GREENS_FUNCTION_REACTION_DYNAMICS = "KISAO_0000058"

    # Runge-Kutta based method
    KISAO_0000064 = "KISAO_0000064"
    RUNGE_KUTTA_BASED_METHOD = "KISAO_0000064"

    # deterministic cellular automata update algorithm
    KISAO_0000068 = "KISAO_0000068"
    DETERMINISTIC_CELLULAR_AUTOMATA_UPDATE_ALGORITHM = "KISAO_0000068"

    # LSODE
    KISAO_0000071 = "KISAO_0000071"
    LSODE = "KISAO_0000071"

    # binomial tau-leaping method
    KISAO_0000074 = "KISAO_0000074"
    BINOMIAL_TAU_LEAPING_METHOD = "KISAO_0000074"

    # Gillespie multi-particle method
    KISAO_0000075 = "KISAO_0000075"
    GILLESPIE_MULTI_PARTICLE_METHOD = "KISAO_0000075"

    # Stundzia and Lumsden method
    KISAO_0000076 = "KISAO_0000076"
    STUNDZIA_AND_LUMSDEN_METHOD = "KISAO_0000076"

    # estimated midpoint tau-leaping method
    KISAO_0000081 = "KISAO_0000081"
    ESTIMATED_MIDPOINT_TAU_LEAPING_METHOD = "KISAO_0000081"

    # k-alpha leaping method
    KISAO_0000082 = "KISAO_0000082"
    K_ALPHA_LEAPING_METHOD = "KISAO_0000082"

    # nonnegative Poisson tau-leaping method
    KISAO_0000084 = "KISAO_0000084"
    NONNEGATIVE_POISSON_TAU_LEAPING_METHOD = "KISAO_0000084"

    # Fehlberg method
    KISAO_0000086 = "KISAO_0000086"
    FEHLBERG_METHOD = "KISAO_0000086"

    # Dormand-Prince method
    KISAO_0000087 = "KISAO_0000087"
    DORMAND_PRINCE_METHOD = "KISAO_0000087"

    # LSODA
    KISAO_0000088 = "KISAO_0000088"
    LSODA = "KISAO_0000088"

    # LSODAR
    KISAO_0000089 = "KISAO_0000089"
    LSODAR = "KISAO_0000089"

    # LSODI
    KISAO_0000090 = "KISAO_0000090"
    LSODI = "KISAO_0000090"

    # LSODIS
    KISAO_0000091 = "KISAO_0000091"
    LSODIS = "KISAO_0000091"

    # LSODPK
    KISAO_0000093 = "KISAO_0000093"
    LSODPK = "KISAO_0000093"

    # Livermore solver
    KISAO_0000094 = "KISAO_0000094"
    LIVERMORE_SOLVER = "KISAO_0000094"

    # sub-volume stochastic reaction-diffusion algorithm
    KISAO_0000095 = "KISAO_0000095"
    SUB_VOLUME_STOCHASTIC_REACTION_DIFFUSION_ALGORITHM = "KISAO_0000095"

    # modelling and simulation algorithm characteristic
    KISAO_0000097 = "KISAO_0000097"
    MODELLING_AND_SIMULATION_ALGORITHM_CHARACTERISTIC = "KISAO_0000097"

    # type of variable
    KISAO_0000098 = "KISAO_0000098"
    TYPE_OF_VARIABLE = "KISAO_0000098"

    # type of system behaviour
    KISAO_0000099 = "KISAO_0000099"
    TYPE_OF_SYSTEM_BEHAVIOUR = "KISAO_0000099"

    # type of progression time step
    KISAO_0000100 = "KISAO_0000100"
    TYPE_OF_PROGRESSION_TIME_STEP = "KISAO_0000100"

    # spatial description
    KISAO_0000102 = "KISAO_0000102"
    SPATIAL_DESCRIPTION = "KISAO_0000102"

    # deterministic system behaviour
    KISAO_0000103 = "KISAO_0000103"
    DETERMINISTIC_SYSTEM_BEHAVIOUR = "KISAO_0000103"

    # stochastic system behaviour
    KISAO_0000104 = "KISAO_0000104"
    STOCHASTIC_SYSTEM_BEHAVIOUR = "KISAO_0000104"

    # discrete variable
    KISAO_0000105 = "KISAO_0000105"
    DISCRETE_VARIABLE = "KISAO_0000105"

    # continuous variable
    KISAO_0000106 = "KISAO_0000106"
    CONTINUOUS_VARIABLE = "KISAO_0000106"

    # progression with adaptive time step
    KISAO_0000107 = "KISAO_0000107"
    PROGRESSION_WITH_ADAPTIVE_TIME_STEP = "KISAO_0000107"

    # progression with fixed time step
    KISAO_0000108 = "KISAO_0000108"
    PROGRESSION_WITH_FIXED_TIME_STEP = "KISAO_0000108"

    # modelling and simulation algorithm parameter
    KISAO_0000201 = "KISAO_0000201"
    MODELLING_AND_SIMULATION_ALGORITHM_PARAMETER = "KISAO_0000201"

    # particle number lower limit
    KISAO_0000203 = "KISAO_0000203"
    PARTICLE_NUMBER_LOWER_LIMIT = "KISAO_0000203"

    # particle number upper limit
    KISAO_0000204 = "KISAO_0000204"
    PARTICLE_NUMBER_UPPER_LIMIT = "KISAO_0000204"

    # partitioning interval
    KISAO_0000205 = "KISAO_0000205"
    PARTITIONING_INTERVAL = "KISAO_0000205"

    # relative tolerance
    KISAO_0000209 = "KISAO_0000209"
    RELATIVE_TOLERANCE = "KISAO_0000209"

    # absolute tolerance
    KISAO_0000211 = "KISAO_0000211"
    ABSOLUTE_TOLERANCE = "KISAO_0000211"

    # use reduced model
    KISAO_0000216 = "KISAO_0000216"
    USE_REDUCED_MODEL = "KISAO_0000216"

    # maximum Adams order
    KISAO_0000219 = "KISAO_0000219"
    MAXIMUM_ADAMS_ORDER = "KISAO_0000219"

    # maximum BDF order
    KISAO_0000220 = "KISAO_0000220"
    MAXIMUM_BDF_ORDER = "KISAO_0000220"

    # number of history bins
    KISAO_0000223 = "KISAO_0000223"
    NUMBER_OF_HISTORY_BINS = "KISAO_0000223"

    # tau-leaping epsilon
    KISAO_0000228 = "KISAO_0000228"
    TAU_LEAPING_EPSILON = "KISAO_0000228"

    # minimum reactions per leap
    KISAO_0000230 = "KISAO_0000230"
    MINIMUM_REACTIONS_PER_LEAP = "KISAO_0000230"

    # Pahle hybrid method
    KISAO_0000231 = "KISAO_0000231"
    PAHLE_HYBRID_METHOD = "KISAO_0000231"

    # LSOIBT
    KISAO_0000232 = "KISAO_0000232"
    LSOIBT = "KISAO_0000232"

    # LSODES
    KISAO_0000233 = "KISAO_0000233"
    LSODES = "KISAO_0000233"

    # LSODKR
    KISAO_0000234 = "KISAO_0000234"
    LSODKR = "KISAO_0000234"

    # type of solution
    KISAO_0000235 = "KISAO_0000235"
    TYPE_OF_SOLUTION = "KISAO_0000235"

    # exact solution
    KISAO_0000236 = "KISAO_0000236"
    EXACT_SOLUTION = "KISAO_0000236"

    # approximate solution
    KISAO_0000237 = "KISAO_0000237"
    APPROXIMATE_SOLUTION = "KISAO_0000237"

    # type of method
    KISAO_0000238 = "KISAO_0000238"
    TYPE_OF_METHOD = "KISAO_0000238"

    # explicit method type
    KISAO_0000239 = "KISAO_0000239"
    EXPLICIT_METHOD_TYPE = "KISAO_0000239"

    # implicit method type
    KISAO_0000240 = "KISAO_0000240"
    IMPLICIT_METHOD_TYPE = "KISAO_0000240"

    # Gillespie-like method
    KISAO_0000241 = "KISAO_0000241"
    GILLESPIE_LIKE_METHOD = "KISAO_0000241"

    # error control parameter
    KISAO_0000242 = "KISAO_0000242"
    ERROR_CONTROL_PARAMETER = "KISAO_0000242"

    # method switching control parameter
    KISAO_0000243 = "KISAO_0000243"
    METHOD_SWITCHING_CONTROL_PARAMETER = "KISAO_0000243"

    # granularity control parameter
    KISAO_0000244 = "KISAO_0000244"
    GRANULARITY_CONTROL_PARAMETER = "KISAO_0000244"

    # has characteristic
    KISAO_0000245 = "KISAO_0000245"
    HAS_CHARACTERISTIC = "KISAO_0000245"

    # is hybrid of
    KISAO_0000246 = "KISAO_0000246"
    IS_HYBRID_OF = "KISAO_0000246"

    # tau-leaping delta
    KISAO_0000248 = "KISAO_0000248"
    TAU_LEAPING_DELTA = "KISAO_0000248"

    # critical firing threshold
    KISAO_0000249 = "KISAO_0000249"
    CRITICAL_FIRING_THRESHOLD = "KISAO_0000249"

    # is parameter of
    KISAO_0000250 = "KISAO_0000250"
    IS_PARAMETER_OF = "KISAO_0000250"

    # partitioning control parameter
    KISAO_0000252 = "KISAO_0000252"
    PARTITIONING_CONTROL_PARAMETER = "KISAO_0000252"

    # coarse-graining factor
    KISAO_0000253 = "KISAO_0000253"
    COARSE_GRAINING_FACTOR = "KISAO_0000253"

    # Brownian diffusion accuracy
    KISAO_0000254 = "KISAO_0000254"
    BROWNIAN_DIFFUSION_ACCURACY = "KISAO_0000254"

    # molecules per virtual box
    KISAO_0000255 = "KISAO_0000255"
    MOLECULES_PER_VIRTUAL_BOX = "KISAO_0000255"

    # virtual box side length
    KISAO_0000256 = "KISAO_0000256"
    VIRTUAL_BOX_SIDE_LENGTH = "KISAO_0000256"

    # surface-bound epsilon
    KISAO_0000257 = "KISAO_0000257"
    SURFACE_BOUND_EPSILON = "KISAO_0000257"

    # neighbour distance
    KISAO_0000258 = "KISAO_0000258"
    NEIGHBOUR_DISTANCE = "KISAO_0000258"

    # has parameter
    KISAO_0000259 = "KISAO_0000259"
    HAS_PARAMETER = "KISAO_0000259"

    # virtual box size
    KISAO_0000260 = "KISAO_0000260"
    VIRTUAL_BOX_SIZE = "KISAO_0000260"

    # Euler method
    KISAO_0000261 = "KISAO_0000261"
    EULER_METHOD = "KISAO_0000261"

    # NFSim agent-based simulation method
    KISAO_0000263 = "KISAO_0000263"
    NFSIM_AGENT_BASED_SIMULATION_METHOD = "KISAO_0000263"

    # cellular automata update method
    KISAO_0000264 = "KISAO_0000264"
    CELLULAR_AUTOMATA_UPDATE_METHOD = "KISAO_0000264"

    # is characteristic of
    KISAO_0000268 = "KISAO_0000268"
    IS_CHARACTERISTIC_OF = "KISAO_0000268"

    # hard-particle molecular dynamics
    KISAO_0000273 = "KISAO_0000273"
    HARD_PARTICLE_MOLECULAR_DYNAMICS = "KISAO_0000273"

    # first-passage Monte Carlo algorithm
    KISAO_0000274 = "KISAO_0000274"
    FIRST_PASSAGE_MONTE_CARLO_ALGORITHM = "KISAO_0000274"

    # Gill method
    KISAO_0000276 = "KISAO_0000276"
    GILL_METHOD = "KISAO_0000276"

    # Metropolis Monte Carlo algorithm
    KISAO_0000278 = "KISAO_0000278"
    METROPOLIS_MONTE_CARLO_ALGORITHM = "KISAO_0000278"

    # Adams-Bashforth method
    KISAO_0000279 = "KISAO_0000279"
    ADAMS_BASHFORTH_METHOD = "KISAO_0000279"

    # Adams-Moulton method
    KISAO_0000280 = "KISAO_0000280"
    ADAMS_MOULTON_METHOD = "KISAO_0000280"

    # multistep method
    KISAO_0000281 = "KISAO_0000281"
    MULTISTEP_METHOD = "KISAO_0000281"

    # KINSOL
    KISAO_0000282 = "KISAO_0000282"
    KINSOL = "KISAO_0000282"

    # IDA
    KISAO_0000283 = "KISAO_0000283"
    IDA = "KISAO_0000283"

    # finite volume method
    KISAO_0000285 = "KISAO_0000285"
    FINITE_VOLUME_METHOD = "KISAO_0000285"

    # Euler-Maruyama method
    KISAO_0000286 = "KISAO_0000286"
    EULER_MARUYAMA_METHOD = "KISAO_0000286"

    # Milstein method
    KISAO_0000287 = "KISAO_0000287"
    MILSTEIN_METHOD = "KISAO_0000287"

    # backward differentiation formula
    KISAO_0000288 = "KISAO_0000288"
    BACKWARD_DIFFERENTIATION_FORMULA = "KISAO_0000288"

    # Adams method
    KISAO_0000289 = "KISAO_0000289"
    ADAMS_METHOD = "KISAO_0000289"

    # Merson method
    KISAO_0000290 = "KISAO_0000290"
    MERSON_METHOD = "KISAO_0000290"

    # Hammer-Hollingsworth method
    KISAO_0000296 = "KISAO_0000296"
    HAMMER_HOLLINGSWORTH_METHOD = "KISAO_0000296"

    # Lobatto method
    KISAO_0000297 = "KISAO_0000297"
    LOBATTO_METHOD = "KISAO_0000297"

    # Butcher-Kuntzmann method
    KISAO_0000299 = "KISAO_0000299"
    BUTCHER_KUNTZMANN_METHOD = "KISAO_0000299"

    # Heun method
    KISAO_0000301 = "KISAO_0000301"
    HEUN_METHOD = "KISAO_0000301"

    # embedded Runge-Kutta method
    KISAO_0000302 = "KISAO_0000302"
    EMBEDDED_RUNGE_KUTTA_METHOD = "KISAO_0000302"

    # Zonneveld method
    KISAO_0000303 = "KISAO_0000303"
    ZONNEVELD_METHOD = "KISAO_0000303"

    # Radau method
    KISAO_0000304 = "KISAO_0000304"
    RADAU_METHOD = "KISAO_0000304"

    # Verner method
    KISAO_0000305 = "KISAO_0000305"
    VERNER_METHOD = "KISAO_0000305"

    # Lagrangian sliding fluid element algorithm
    KISAO_0000306 = "KISAO_0000306"
    LAGRANGIAN_SLIDING_FLUID_ELEMENT_ALGORITHM = "KISAO_0000306"

    # finite difference method
    KISAO_0000307 = "KISAO_0000307"
    FINITE_DIFFERENCE_METHOD = "KISAO_0000307"

    # MacCormack method
    KISAO_0000308 = "KISAO_0000308"
    MACCORMACK_METHOD = "KISAO_0000308"

    # Crank-Nicolson method
    KISAO_0000309 = "KISAO_0000309"
    CRANK_NICOLSON_METHOD = "KISAO_0000309"

    # method of lines
    KISAO_0000310 = "KISAO_0000310"
    METHOD_OF_LINES = "KISAO_0000310"

    # type of domain geometry handling
    KISAO_0000311 = "KISAO_0000311"
    TYPE_OF_DOMAIN_GEOMETRY_HANDLING = "KISAO_0000311"

    # S-System power-law canonical differential equations solver
    KISAO_0000314 = "KISAO_0000314"
    S_SYSTEM_POWER_LAW_CANONICAL_DIFFERENTIAL_EQUATIONS_SOLVER = "KISAO_0000314"

    # lattice gas automata
    KISAO_0000315 = "KISAO_0000315"
    LATTICE_GAS_AUTOMATA = "KISAO_0000315"

    # enhanced Greens function reaction dynamics
    KISAO_0000316 = "KISAO_0000316"
    ENHANCED_GREENS_FUNCTION_REACTION_DYNAMICS = "KISAO_0000316"

    # E-Cell multi-algorithm simulation method
    KISAO_0000317 = "KISAO_0000317"
    E_CELL_MULTI_ALGORITHM_SIMULATION_METHOD = "KISAO_0000317"

    # Gauss-Legendre Runge-Kutta method
    KISAO_0000318 = "KISAO_0000318"
    GAUSS_LEGENDRE_RUNGE_KUTTA_METHOD = "KISAO_0000318"

    # Monte Carlo method
    KISAO_0000319 = "KISAO_0000319"
    MONTE_CARLO_METHOD = "KISAO_0000319"

    # BioRica hybrid method
    KISAO_0000320 = "KISAO_0000320"
    BIORICA_HYBRID_METHOD = "KISAO_0000320"

    # Cash-Karp method
    KISAO_0000321 = "KISAO_0000321"
    CASH_KARP_METHOD = "KISAO_0000321"

    # hybridity
    KISAO_0000322 = "KISAO_0000322"
    HYBRIDITY = "KISAO_0000322"

    # equation-free probabilistic steady-state approximation
    KISAO_0000323 = "KISAO_0000323"
    EQUATION_FREE_PROBABILISTIC_STEADY_STATE_APPROXIMATION = "KISAO_0000323"

    # nested stochastic simulation algorithm
    KISAO_0000324 = "KISAO_0000324"
    NESTED_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000324"

    # minimum fast/discrete reaction occurrences number
    KISAO_0000325 = "KISAO_0000325"
    MINIMUM_FAST_DISCRETE_REACTION_OCCURRENCES_NUMBER = "KISAO_0000325"

    # number of samples
    KISAO_0000326 = "KISAO_0000326"
    NUMBER_OF_SAMPLES = "KISAO_0000326"

    # maximum discrete number
    KISAO_0000327 = "KISAO_0000327"
    MAXIMUM_DISCRETE_NUMBER = "KISAO_0000327"

    # minimum fast rate
    KISAO_0000328 = "KISAO_0000328"
    MINIMUM_FAST_RATE = "KISAO_0000328"

    # constant-time kinetic Monte Carlo algorithm
    KISAO_0000329 = "KISAO_0000329"
    CONSTANT_TIME_KINETIC_MONTE_CARLO_ALGORITHM = "KISAO_0000329"

    # R-leaping algorithm
    KISAO_0000330 = "KISAO_0000330"
    R_LEAPING_ALGORITHM = "KISAO_0000330"

    # exact R-leaping algorithm
    KISAO_0000331 = "KISAO_0000331"
    EXACT_R_LEAPING_ALGORITHM = "KISAO_0000331"

    # ER-leap initial leap
    KISAO_0000332 = "KISAO_0000332"
    ER_LEAP_INITIAL_LEAP = "KISAO_0000332"

    # accelerated stochastic simulation algorithm
    KISAO_0000333 = "KISAO_0000333"
    ACCELERATED_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000333"

    # multiparticle lattice gas automata
    KISAO_0000334 = "KISAO_0000334"
    MULTIPARTICLE_LATTICE_GAS_AUTOMATA = "KISAO_0000334"

    # generalized stochastic simulation algorithm
    KISAO_0000335 = "KISAO_0000335"
    GENERALIZED_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000335"

    # D-leaping method
    KISAO_0000336 = "KISAO_0000336"
    D_LEAPING_METHOD = "KISAO_0000336"

    # finite element method
    KISAO_0000337 = "KISAO_0000337"
    FINITE_ELEMENT_METHOD = "KISAO_0000337"

    # h-version of the finite element method
    KISAO_0000338 = "KISAO_0000338"
    H_VERSION_OF_THE_FINITE_ELEMENT_METHOD = "KISAO_0000338"

    # p-version of the finite element method
    KISAO_0000339 = "KISAO_0000339"
    P_VERSION_OF_THE_FINITE_ELEMENT_METHOD = "KISAO_0000339"

    # h-p version of the finite element method
    KISAO_0000340 = "KISAO_0000340"
    H_P_VERSION_OF_THE_FINITE_ELEMENT_METHOD = "KISAO_0000340"

    # mixed finite element method
    KISAO_0000341 = "KISAO_0000341"
    MIXED_FINITE_ELEMENT_METHOD = "KISAO_0000341"

    # level set method
    KISAO_0000342 = "KISAO_0000342"
    LEVEL_SET_METHOD = "KISAO_0000342"

    # generalized finite element method
    KISAO_0000343 = "KISAO_0000343"
    GENERALIZED_FINITE_ELEMENT_METHOD = "KISAO_0000343"

    # h-p cloud method
    KISAO_0000345 = "KISAO_0000345"
    H_P_CLOUD_METHOD = "KISAO_0000345"

    # mesh-based geometry handling
    KISAO_0000346 = "KISAO_0000346"
    MESH_BASED_GEOMETRY_HANDLING = "KISAO_0000346"

    # meshless geometry handling
    KISAO_0000347 = "KISAO_0000347"
    MESHLESS_GEOMETRY_HANDLING = "KISAO_0000347"

    # extended finite element method
    KISAO_0000348 = "KISAO_0000348"
    EXTENDED_FINITE_ELEMENT_METHOD = "KISAO_0000348"

    # method of finite spheres
    KISAO_0000349 = "KISAO_0000349"
    METHOD_OF_FINITE_SPHERES = "KISAO_0000349"

    # probability-weighted dynamic Monte Carlo method
    KISAO_0000350 = "KISAO_0000350"
    PROBABILITY_WEIGHTED_DYNAMIC_MONTE_CARLO_METHOD = "KISAO_0000350"

    # multinomial tau-leaping method
    KISAO_0000351 = "KISAO_0000351"
    MULTINOMIAL_TAU_LEAPING_METHOD = "KISAO_0000351"

    # hybrid method
    KISAO_0000352 = "KISAO_0000352"
    HYBRID_METHOD = "KISAO_0000352"

    # generalized minimal residual algorithm
    KISAO_0000353 = "KISAO_0000353"
    GENERALIZED_MINIMAL_RESIDUAL_ALGORITHM = "KISAO_0000353"

    # Krylov subspace projection method
    KISAO_0000354 = "KISAO_0000354"
    KRYLOV_SUBSPACE_PROJECTION_METHOD = "KISAO_0000354"

    # DASPK
    KISAO_0000355 = "KISAO_0000355"
    DASPK = "KISAO_0000355"

    # DASSL
    KISAO_0000356 = "KISAO_0000356"
    DASSL = "KISAO_0000356"

    # conjugate gradient method
    KISAO_0000357 = "KISAO_0000357"
    CONJUGATE_GRADIENT_METHOD = "KISAO_0000357"

    # biconjugate gradient method
    KISAO_0000358 = "KISAO_0000358"
    BICONJUGATE_GRADIENT_METHOD = "KISAO_0000358"

    # is similar to
    KISAO_0000359 = "KISAO_0000359"
    IS_SIMILAR_TO = "KISAO_0000359"

    # uses
    KISAO_0000360 = "KISAO_0000360"
    USES = "KISAO_0000360"

    # is generalization of
    KISAO_0000361 = "KISAO_0000361"
    IS_GENERALIZATION_OF = "KISAO_0000361"

    # implicit-state Doob-Gillespie algorithm
    KISAO_0000362 = "KISAO_0000362"
    IMPLICIT_STATE_DOOB_GILLESPIE_ALGORITHM = "KISAO_0000362"

    # rule-based simulation method
    KISAO_0000363 = "KISAO_0000363"
    RULE_BASED_SIMULATION_METHOD = "KISAO_0000363"

    # Adams predictor-corrector method
    KISAO_0000364 = "KISAO_0000364"
    ADAMS_PREDICTOR_CORRECTOR_METHOD = "KISAO_0000364"

    # NDSolve method
    KISAO_0000365 = "KISAO_0000365"
    NDSOLVE_METHOD = "KISAO_0000365"

    # symplecticness
    KISAO_0000366 = "KISAO_0000366"
    SYMPLECTICNESS = "KISAO_0000366"

    # partitioned Runge-Kutta method
    KISAO_0000367 = "KISAO_0000367"
    PARTITIONED_RUNGE_KUTTA_METHOD = "KISAO_0000367"

    # partial differential equation discretization method
    KISAO_0000369 = "KISAO_0000369"
    PARTIAL_DIFFERENTIAL_EQUATION_DISCRETIZATION_METHOD = "KISAO_0000369"

    # type of problem
    KISAO_0000370 = "KISAO_0000370"
    TYPE_OF_PROBLEM = "KISAO_0000370"

    # stochastic differential equation problem
    KISAO_0000371 = "KISAO_0000371"
    STOCHASTIC_DIFFERENTIAL_EQUATION_PROBLEM = "KISAO_0000371"

    # partial differential equation problem
    KISAO_0000372 = "KISAO_0000372"
    PARTIAL_DIFFERENTIAL_EQUATION_PROBLEM = "KISAO_0000372"

    # differential-algebraic equation problem
    KISAO_0000373 = "KISAO_0000373"
    DIFFERENTIAL_ALGEBRAIC_EQUATION_PROBLEM = "KISAO_0000373"

    # ordinary differential equation problem
    KISAO_0000374 = "KISAO_0000374"
    ORDINARY_DIFFERENTIAL_EQUATION_PROBLEM = "KISAO_0000374"

    # delay differential equation problem
    KISAO_0000375 = "KISAO_0000375"
    DELAY_DIFFERENTIAL_EQUATION_PROBLEM = "KISAO_0000375"

    # linearity of equation
    KISAO_0000376 = "KISAO_0000376"
    LINEARITY_OF_EQUATION = "KISAO_0000376"

    # one-step method
    KISAO_0000377 = "KISAO_0000377"
    ONE_STEP_METHOD = "KISAO_0000377"

    # implicit midpoint rule
    KISAO_0000378 = "KISAO_0000378"
    IMPLICIT_MIDPOINT_RULE = "KISAO_0000378"

    # Bulirsch-Stoer algorithm
    KISAO_0000379 = "KISAO_0000379"
    BULIRSCH_STOER_ALGORITHM = "KISAO_0000379"

    # Richardson extrapolation based method
    KISAO_0000380 = "KISAO_0000380"
    RICHARDSON_EXTRAPOLATION_BASED_METHOD = "KISAO_0000380"

    # midpoint method
    KISAO_0000381 = "KISAO_0000381"
    MIDPOINT_METHOD = "KISAO_0000381"

    # modified midpoint method
    KISAO_0000382 = "KISAO_0000382"
    MODIFIED_MIDPOINT_METHOD = "KISAO_0000382"

    # Bader-Deuflhard method
    KISAO_0000383 = "KISAO_0000383"
    BADER_DEUFLHARD_METHOD = "KISAO_0000383"

    # semi-implicit midpoint rule
    KISAO_0000384 = "KISAO_0000384"
    SEMI_IMPLICIT_MIDPOINT_RULE = "KISAO_0000384"

    # scaled preconditioned generalized minimal residual method
    KISAO_0000386 = "KISAO_0000386"
    SCALED_PRECONDITIONED_GENERALIZED_MINIMAL_RESIDUAL_METHOD = "KISAO_0000386"

    # minimal residual method
    KISAO_0000388 = "KISAO_0000388"
    MINIMAL_RESIDUAL_METHOD = "KISAO_0000388"

    # quasi-minimal residual method
    KISAO_0000389 = "KISAO_0000389"
    QUASI_MINIMAL_RESIDUAL_METHOD = "KISAO_0000389"

    # biconjugate gradient stabilized method
    KISAO_0000392 = "KISAO_0000392"
    BICONJUGATE_GRADIENT_STABILIZED_METHOD = "KISAO_0000392"

    # ingenious conjugate gradients-squared method
    KISAO_0000393 = "KISAO_0000393"
    INGENIOUS_CONJUGATE_GRADIENTS_SQUARED_METHOD = "KISAO_0000393"

    # quasi-minimal residual variant of biconjugate gradient stabilized method
    KISAO_0000394 = "KISAO_0000394"
    QUASI_MINIMAL_RESIDUAL_VARIANT_OF_BICONJUGATE_GRADIENT_STABILIZED_METHOD = (
        "KISAO_0000394"
    )

    # improved biconjugate gradient method
    KISAO_0000395 = "KISAO_0000395"
    IMPROVED_BICONJUGATE_GRADIENT_METHOD = "KISAO_0000395"

    # transpose-free quasi-minimal residual algorithm
    KISAO_0000396 = "KISAO_0000396"
    TRANSPOSE_FREE_QUASI_MINIMAL_RESIDUAL_ALGORITHM = "KISAO_0000396"

    # preconditioning technique
    KISAO_0000397 = "KISAO_0000397"
    PRECONDITIONING_TECHNIQUE = "KISAO_0000397"

    # iterative method for solving a system of linear equations
    KISAO_0000398 = "KISAO_0000398"
    ITERATIVE_METHOD_FOR_SOLVING_A_SYSTEM_OF_LINEAR_EQUATIONS = "KISAO_0000398"

    # is used by
    KISAO_0000399 = "KISAO_0000399"
    IS_USED_BY = "KISAO_0000399"

    # homogeneousness of equation
    KISAO_0000403 = "KISAO_0000403"
    HOMOGENEOUSNESS_OF_EQUATION = "KISAO_0000403"

    # symmetricity of matrix
    KISAO_0000404 = "KISAO_0000404"
    SYMMETRICITY_OF_MATRIX = "KISAO_0000404"

    # type of differential equation
    KISAO_0000405 = "KISAO_0000405"
    TYPE_OF_DIFFERENTIAL_EQUATION = "KISAO_0000405"

    # steady state method
    KISAO_0000407 = "KISAO_0000407"
    STEADY_STATE_METHOD = "KISAO_0000407"

    # Newton-type method
    KISAO_0000408 = "KISAO_0000408"
    NEWTON_TYPE_METHOD = "KISAO_0000408"

    # ordinary Newton method
    KISAO_0000409 = "KISAO_0000409"
    ORDINARY_NEWTON_METHOD = "KISAO_0000409"

    # simlified Newton method
    KISAO_0000410 = "KISAO_0000410"
    SIMLIFIED_NEWTON_METHOD = "KISAO_0000410"

    # Newton-like method
    KISAO_0000411 = "KISAO_0000411"
    NEWTON_LIKE_METHOD = "KISAO_0000411"

    # inexact Newton method
    KISAO_0000412 = "KISAO_0000412"
    INEXACT_NEWTON_METHOD = "KISAO_0000412"

    # exact Newton method
    KISAO_0000413 = "KISAO_0000413"
    EXACT_NEWTON_METHOD = "KISAO_0000413"

    # maximum number of steps
    KISAO_0000415 = "KISAO_0000415"
    MAXIMUM_NUMBER_OF_STEPS = "KISAO_0000415"

    # partial least squares regression method
    KISAO_0000416 = "KISAO_0000416"
    PARTIAL_LEAST_SQUARES_REGRESSION_METHOD = "KISAO_0000416"

    # hierarchical cluster-based partial least squares regression method
    KISAO_0000417 = "KISAO_0000417"
    HIERARCHICAL_CLUSTER_BASED_PARTIAL_LEAST_SQUARES_REGRESSION_METHOD = "KISAO_0000417"

    # N-way partial least squares regression method
    KISAO_0000418 = "KISAO_0000418"
    N_WAY_PARTIAL_LEAST_SQUARES_REGRESSION_METHOD = "KISAO_0000418"

    # metamodelling method
    KISAO_0000419 = "KISAO_0000419"
    METAMODELLING_METHOD = "KISAO_0000419"

    # number of partial least squares components
    KISAO_0000420 = "KISAO_0000420"
    NUMBER_OF_PARTIAL_LEAST_SQUARES_COMPONENTS = "KISAO_0000420"

    # type of validation
    KISAO_0000421 = "KISAO_0000421"
    TYPE_OF_VALIDATION = "KISAO_0000421"

    # number of N-way partial least squares regression factors
    KISAO_0000422 = "KISAO_0000422"
    NUMBER_OF_N_WAY_PARTIAL_LEAST_SQUARES_REGRESSION_FACTORS = "KISAO_0000422"

    # partial least squares regression-like method
    KISAO_0000423 = "KISAO_0000423"
    PARTIAL_LEAST_SQUARES_REGRESSION_LIKE_METHOD = "KISAO_0000423"

    # mean-centring of variables
    KISAO_0000424 = "KISAO_0000424"
    MEAN_CENTRING_OF_VARIABLES = "KISAO_0000424"

    # standardising of variables
    KISAO_0000425 = "KISAO_0000425"
    STANDARDISING_OF_VARIABLES = "KISAO_0000425"

    # number of clusters
    KISAO_0000427 = "KISAO_0000427"
    NUMBER_OF_CLUSTERS = "KISAO_0000427"

    # matrix for clusterization
    KISAO_0000428 = "KISAO_0000428"
    MATRIX_FOR_CLUSTERIZATION = "KISAO_0000428"

    # clusterization parameter
    KISAO_0000429 = "KISAO_0000429"
    CLUSTERIZATION_PARAMETER = "KISAO_0000429"

    # variables preprocessing parameter
    KISAO_0000430 = "KISAO_0000430"
    VARIABLES_PREPROCESSING_PARAMETER = "KISAO_0000430"

    # IDA-like method
    KISAO_0000432 = "KISAO_0000432"
    IDA_LIKE_METHOD = "KISAO_0000432"

    # CVODE-like method
    KISAO_0000433 = "KISAO_0000433"
    CVODE_LIKE_METHOD = "KISAO_0000433"

    # Higham-Hall method
    KISAO_0000434 = "KISAO_0000434"
    HIGHAM_HALL_METHOD = "KISAO_0000434"

    # embedded Runge-Kutta 5(4) method
    KISAO_0000435 = "KISAO_0000435"
    EMBEDDED_RUNGE_KUTTA_5_4__METHOD = "KISAO_0000435"

    # Dormand-Prince 8(5,3) method
    KISAO_0000436 = "KISAO_0000436"
    DORMAND_PRINCE_8_5_3__METHOD = "KISAO_0000436"

    # flux balance analysis
    KISAO_0000437 = "KISAO_0000437"
    FLUX_BALANCE_ANALYSIS = "KISAO_0000437"

    # COAST
    KISAO_0000447 = "KISAO_0000447"
    COAST = "KISAO_0000447"

    # logical model simulation method
    KISAO_0000448 = "KISAO_0000448"
    LOGICAL_MODEL_SIMULATION_METHOD = "KISAO_0000448"

    # synchronous logical model simulation method
    KISAO_0000449 = "KISAO_0000449"
    SYNCHRONOUS_LOGICAL_MODEL_SIMULATION_METHOD = "KISAO_0000449"

    # asynchronous logical model simulation method
    KISAO_0000450 = "KISAO_0000450"
    ASYNCHRONOUS_LOGICAL_MODEL_SIMULATION_METHOD = "KISAO_0000450"

    # type of updating policy
    KISAO_0000451 = "KISAO_0000451"
    TYPE_OF_UPDATING_POLICY = "KISAO_0000451"

    # random updating policy
    KISAO_0000452 = "KISAO_0000452"
    RANDOM_UPDATING_POLICY = "KISAO_0000452"

    # ordered updating policy
    KISAO_0000453 = "KISAO_0000453"
    ORDERED_UPDATING_POLICY = "KISAO_0000453"

    # constant updating policy
    KISAO_0000454 = "KISAO_0000454"
    CONSTANT_UPDATING_POLICY = "KISAO_0000454"

    # prioritized updating policy
    KISAO_0000455 = "KISAO_0000455"
    PRIORITIZED_UPDATING_POLICY = "KISAO_0000455"

    # maximum step size
    KISAO_0000467 = "KISAO_0000467"
    MAXIMUM_STEP_SIZE = "KISAO_0000467"

    # maximal timestep method
    KISAO_0000468 = "KISAO_0000468"
    MAXIMAL_TIMESTEP_METHOD = "KISAO_0000468"

    # maximal timestep
    KISAO_0000469 = "KISAO_0000469"
    MAXIMAL_TIMESTEP = "KISAO_0000469"

    # optimization algorithm
    KISAO_0000470 = "KISAO_0000470"
    OPTIMIZATION_ALGORITHM = "KISAO_0000470"

    # local optimization algorithm
    KISAO_0000471 = "KISAO_0000471"
    LOCAL_OPTIMIZATION_ALGORITHM = "KISAO_0000471"

    # global optimization algorithm
    KISAO_0000472 = "KISAO_0000472"
    GLOBAL_OPTIMIZATION_ALGORITHM = "KISAO_0000472"

    # Bayesian inference algorithm
    KISAO_0000473 = "KISAO_0000473"
    BAYESIAN_INFERENCE_ALGORITHM = "KISAO_0000473"

    # integration method
    KISAO_0000475 = "KISAO_0000475"
    INTEGRATION_METHOD = "KISAO_0000475"

    # iteration type
    KISAO_0000476 = "KISAO_0000476"
    ITERATION_TYPE = "KISAO_0000476"

    # linear solver
    KISAO_0000477 = "KISAO_0000477"
    LINEAR_SOLVER = "KISAO_0000477"

    # preconditioner
    KISAO_0000478 = "KISAO_0000478"
    PRECONDITIONER = "KISAO_0000478"

    # upper half-bandwidth
    KISAO_0000479 = "KISAO_0000479"
    UPPER_HALF_BANDWIDTH = "KISAO_0000479"

    # lower half-bandwidth
    KISAO_0000480 = "KISAO_0000480"
    LOWER_HALF_BANDWIDTH = "KISAO_0000480"

    # interpolate solution
    KISAO_0000481 = "KISAO_0000481"
    INTERPOLATE_SOLUTION = "KISAO_0000481"

    # half-bandwith parameter
    KISAO_0000482 = "KISAO_0000482"
    HALF_BANDWITH_PARAMETER = "KISAO_0000482"

    # step size
    KISAO_0000483 = "KISAO_0000483"
    STEP_SIZE = "KISAO_0000483"

    # maximum order
    KISAO_0000484 = "KISAO_0000484"
    MAXIMUM_ORDER = "KISAO_0000484"

    # minimum step size
    KISAO_0000485 = "KISAO_0000485"
    MINIMUM_STEP_SIZE = "KISAO_0000485"

    # maximum iterations
    KISAO_0000486 = "KISAO_0000486"
    MAXIMUM_ITERATIONS = "KISAO_0000486"

    # minimum damping
    KISAO_0000487 = "KISAO_0000487"
    MINIMUM_DAMPING = "KISAO_0000487"

    # seed
    KISAO_0000488 = "KISAO_0000488"
    SEED = "KISAO_0000488"

    # discrete event simulation algorithm
    KISAO_0000491 = "KISAO_0000491"
    DISCRETE_EVENT_SIMULATION_ALGORITHM = "KISAO_0000491"

    # asynchronous updating policy
    KISAO_0000492 = "KISAO_0000492"
    ASYNCHRONOUS_UPDATING_POLICY = "KISAO_0000492"

    # synchronous updating policy
    KISAO_0000493 = "KISAO_0000493"
    SYNCHRONOUS_UPDATING_POLICY = "KISAO_0000493"

    # fully asynchronous updating policy
    KISAO_0000494 = "KISAO_0000494"
    FULLY_ASYNCHRONOUS_UPDATING_POLICY = "KISAO_0000494"

    # random asynchronous updating policy
    KISAO_0000495 = "KISAO_0000495"
    RANDOM_ASYNCHRONOUS_UPDATING_POLICY = "KISAO_0000495"

    # CVODES
    KISAO_0000496 = "KISAO_0000496"
    CVODES = "KISAO_0000496"

    # KLU
    KISAO_0000497 = "KISAO_0000497"
    KLU = "KISAO_0000497"

    # number of runs
    KISAO_0000498 = "KISAO_0000498"
    NUMBER_OF_RUNS = "KISAO_0000498"

    # dynamic flux balance analysis
    KISAO_0000499 = "KISAO_0000499"
    DYNAMIC_FLUX_BALANCE_ANALYSIS = "KISAO_0000499"

    # SOA-DFBA
    KISAO_0000500 = "KISAO_0000500"
    SOA_DFBA = "KISAO_0000500"

    # DOA-DFBA
    KISAO_0000501 = "KISAO_0000501"
    DOA_DFBA = "KISAO_0000501"

    # DA-DFBA
    KISAO_0000502 = "KISAO_0000502"
    DA_DFBA = "KISAO_0000502"

    # simulated annealing
    KISAO_0000503 = "KISAO_0000503"
    SIMULATED_ANNEALING = "KISAO_0000503"

    # random search
    KISAO_0000504 = "KISAO_0000504"
    RANDOM_SEARCH = "KISAO_0000504"

    # particle swarm
    KISAO_0000505 = "KISAO_0000505"
    PARTICLE_SWARM = "KISAO_0000505"

    # genetic algorithm
    KISAO_0000506 = "KISAO_0000506"
    GENETIC_ALGORITHM = "KISAO_0000506"

    # genetic algorithm SR
    KISAO_0000507 = "KISAO_0000507"
    GENETIC_ALGORITHM_SR = "KISAO_0000507"

    # evolutionary programming
    KISAO_0000508 = "KISAO_0000508"
    EVOLUTIONARY_PROGRAMMING = "KISAO_0000508"

    # evolutionary strategy
    KISAO_0000509 = "KISAO_0000509"
    EVOLUTIONARY_STRATEGY = "KISAO_0000509"

    # truncated Newton
    KISAO_0000510 = "KISAO_0000510"
    TRUNCATED_NEWTON = "KISAO_0000510"

    # steepest descent
    KISAO_0000511 = "KISAO_0000511"
    STEEPEST_DESCENT = "KISAO_0000511"

    # praxis
    KISAO_0000512 = "KISAO_0000512"
    PRAXIS = "KISAO_0000512"

    # NL2SOL
    KISAO_0000513 = "KISAO_0000513"
    NL2SOL = "KISAO_0000513"

    # Nelder-Mead
    KISAO_0000514 = "KISAO_0000514"
    NELDER_MEAD = "KISAO_0000514"

    # Levenberg-Marquardt
    KISAO_0000515 = "KISAO_0000515"
    LEVENBERG_MARQUARDT = "KISAO_0000515"

    # Hooke&Jeeves
    KISAO_0000516 = "KISAO_0000516"
    HOOKE_JEEVES = "KISAO_0000516"

    # number of generations
    KISAO_0000517 = "KISAO_0000517"
    NUMBER_OF_GENERATIONS = "KISAO_0000517"

    # evolutionary algorithm parameter
    KISAO_0000518 = "KISAO_0000518"
    EVOLUTIONARY_ALGORITHM_PARAMETER = "KISAO_0000518"

    # population size
    KISAO_0000519 = "KISAO_0000519"
    POPULATION_SIZE = "KISAO_0000519"

    # evolutionary algorithm
    KISAO_0000520 = "KISAO_0000520"
    EVOLUTIONARY_ALGORITHM = "KISAO_0000520"

    # simulated annealing parameter
    KISAO_0000521 = "KISAO_0000521"
    SIMULATED_ANNEALING_PARAMETER = "KISAO_0000521"

    # start temperature
    KISAO_0000522 = "KISAO_0000522"
    START_TEMPERATURE = "KISAO_0000522"

    # cooling factor
    KISAO_0000523 = "KISAO_0000523"
    COOLING_FACTOR = "KISAO_0000523"

    # partitioned leaping method
    KISAO_0000524 = "KISAO_0000524"
    PARTITIONED_LEAPING_METHOD = "KISAO_0000524"

    # stop condition
    KISAO_0000525 = "KISAO_0000525"
    STOP_CONDITION = "KISAO_0000525"

    # flux variability analysis
    KISAO_0000526 = "KISAO_0000526"
    FLUX_VARIABILITY_ANALYSIS = "KISAO_0000526"

    # geometric flux balance analysis
    KISAO_0000527 = "KISAO_0000527"
    GEOMETRIC_FLUX_BALANCE_ANALYSIS = "KISAO_0000527"

    # parsimonious enzyme usage flux balance analysis (minimum sum of absolute fluxes)
    KISAO_0000528 = "KISAO_0000528"
    PARSIMONIOUS_ENZYME_USAGE_FLUX_BALANCE_ANALYSIS__MINIMUM_SUM_OF_ABSOLUTE_FLUXES_ = (
        "KISAO_0000528"
    )

    # parallelism
    KISAO_0000529 = "KISAO_0000529"
    PARALLELISM = "KISAO_0000529"

    # fraction of optimum
    KISAO_0000531 = "KISAO_0000531"
    FRACTION_OF_OPTIMUM = "KISAO_0000531"

    # loopless
    KISAO_0000532 = "KISAO_0000532"
    LOOPLESS = "KISAO_0000532"

    # pFBA factor
    KISAO_0000533 = "KISAO_0000533"
    PFBA_FACTOR = "KISAO_0000533"

    # reactions
    KISAO_0000534 = "KISAO_0000534"
    REACTIONS = "KISAO_0000534"

    # VODE
    KISAO_0000535 = "KISAO_0000535"
    VODE = "KISAO_0000535"

    # ZVODE
    KISAO_0000536 = "KISAO_0000536"
    ZVODE = "KISAO_0000536"

    # explicit Runge-Kutta method of order 3(2)
    KISAO_0000537 = "KISAO_0000537"
    EXPLICIT_RUNGE_KUTTA_METHOD_OF_ORDER_3_2_ = "KISAO_0000537"

    # safety factor on new step selection
    KISAO_0000538 = "KISAO_0000538"
    SAFETY_FACTOR_ON_NEW_STEP_SELECTION = "KISAO_0000538"

    # minimum factor to change step size by
    KISAO_0000539 = "KISAO_0000539"
    MINIMUM_FACTOR_TO_CHANGE_STEP_SIZE_BY = "KISAO_0000539"

    # maximum factor to change step size by
    KISAO_0000540 = "KISAO_0000540"
    MAXIMUM_FACTOR_TO_CHANGE_STEP_SIZE_BY = "KISAO_0000540"

    # beta parameter for stabilized step size control
    KISAO_0000541 = "KISAO_0000541"
    BETA_PARAMETER_FOR_STABILIZED_STEP_SIZE_CONTROL = "KISAO_0000541"

    # correction step should use internally generated full Jacobian
    KISAO_0000542 = "KISAO_0000542"
    CORRECTION_STEP_SHOULD_USE_INTERNALLY_GENERATED_FULL_JACOBIAN = "KISAO_0000542"

    # stability limit detection flag
    KISAO_0000543 = "KISAO_0000543"
    STABILITY_LIMIT_DETECTION_FLAG = "KISAO_0000543"

    # IDAS
    KISAO_0000544 = "KISAO_0000544"
    IDAS = "KISAO_0000544"

    # include sensitivity variables in error control mechanism
    KISAO_0000545 = "KISAO_0000545"
    INCLUDE_SENSITIVITY_VARIABLES_IN_ERROR_CONTROL_MECHANISM = "KISAO_0000545"

    # convex optimization algorithm
    KISAO_0000546 = "KISAO_0000546"
    CONVEX_OPTIMIZATION_ALGORITHM = "KISAO_0000546"

    # linear programming
    KISAO_0000547 = "KISAO_0000547"
    LINEAR_PROGRAMMING = "KISAO_0000547"

    # quadratic programming
    KISAO_0000548 = "KISAO_0000548"
    QUADRATIC_PROGRAMMING = "KISAO_0000548"

    # non-linear programming
    KISAO_0000549 = "KISAO_0000549"
    NON_LINEAR_PROGRAMMING = "KISAO_0000549"

    # simplex method
    KISAO_0000550 = "KISAO_0000550"
    SIMPLEX_METHOD = "KISAO_0000550"

    # primal-dual interior point method
    KISAO_0000551 = "KISAO_0000551"
    PRIMAL_DUAL_INTERIOR_POINT_METHOD = "KISAO_0000551"

    # optimization method
    KISAO_0000552 = "KISAO_0000552"
    OPTIMIZATION_METHOD = "KISAO_0000552"

    # optimization solver
    KISAO_0000553 = "KISAO_0000553"
    OPTIMIZATION_SOLVER = "KISAO_0000553"

    # parsimonius flux balance analysis (minimum number of active fluxes)
    KISAO_0000554 = "KISAO_0000554"
    PARSIMONIUS_FLUX_BALANCE_ANALYSIS__MINIMUM_NUMBER_OF_ACTIVE_FLUXES_ = (
        "KISAO_0000554"
    )

    # absolute quadrature tolerance
    KISAO_0000555 = "KISAO_0000555"
    ABSOLUTE_QUADRATURE_TOLERANCE = "KISAO_0000555"

    # relative quadrature tolerance
    KISAO_0000556 = "KISAO_0000556"
    RELATIVE_QUADRATURE_TOLERANCE = "KISAO_0000556"

    # absolute steady-state tolerance
    KISAO_0000557 = "KISAO_0000557"
    ABSOLUTE_STEADY_STATE_TOLERANCE = "KISAO_0000557"

    # relative steady-state tolerance
    KISAO_0000558 = "KISAO_0000558"
    RELATIVE_STEADY_STATE_TOLERANCE = "KISAO_0000558"

    # initial step size
    KISAO_0000559 = "KISAO_0000559"
    INITIAL_STEP_SIZE = "KISAO_0000559"

    # LSODA/LSODAR hybrid method
    KISAO_0000560 = "KISAO_0000560"
    LSODA_LSODAR_HYBRID_METHOD = "KISAO_0000560"

    # Pahle hybrid Gibson-Bruck Next Reaction method/Runge-Kutta method
    KISAO_0000561 = "KISAO_0000561"
    PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_RUNGE_KUTTA_METHOD = "KISAO_0000561"

    # Pahle hybrid Gibson-Bruck Next Reaction method/LSODA method
    KISAO_0000562 = "KISAO_0000562"
    PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_LSODA_METHOD = "KISAO_0000562"

    # Pahle hybrid Gibson-Bruck Next Reaction method/RK-45 method
    KISAO_0000563 = "KISAO_0000563"
    PAHLE_HYBRID_GIBSON_BRUCK_NEXT_REACTION_METHOD_RK_45_METHOD = "KISAO_0000563"

    # stochastic Runge-Kutta method
    KISAO_0000564 = "KISAO_0000564"
    STOCHASTIC_RUNGE_KUTTA_METHOD = "KISAO_0000564"

    # absolute tolerance for root finding
    KISAO_0000565 = "KISAO_0000565"
    ABSOLUTE_TOLERANCE_FOR_ROOT_FINDING = "KISAO_0000565"

    # stochastic second order Runge-Kutta method
    KISAO_0000566 = "KISAO_0000566"
    STOCHASTIC_SECOND_ORDER_RUNGE_KUTTA_METHOD = "KISAO_0000566"

    # force physical correctness
    KISAO_0000567 = "KISAO_0000567"
    FORCE_PHYSICAL_CORRECTNESS = "KISAO_0000567"

    # NLEQ1
    KISAO_0000568 = "KISAO_0000568"
    NLEQ1 = "KISAO_0000568"

    # NLEQ2
    KISAO_0000569 = "KISAO_0000569"
    NLEQ2 = "KISAO_0000569"

    # auto reduce tolerances
    KISAO_0000570 = "KISAO_0000570"
    AUTO_REDUCE_TOLERANCES = "KISAO_0000570"

    # absolute tolerance adjustment factor
    KISAO_0000571 = "KISAO_0000571"
    ABSOLUTE_TOLERANCE_ADJUSTMENT_FACTOR = "KISAO_0000571"

    # level of superimposed noise
    KISAO_0000572 = "KISAO_0000572"
    LEVEL_OF_SUPERIMPOSED_NOISE = "KISAO_0000572"

    # probabilistic logical model simulation method
    KISAO_0000573 = "KISAO_0000573"
    PROBABILISTIC_LOGICAL_MODEL_SIMULATION_METHOD = "KISAO_0000573"

    # species transition probabilities
    KISAO_0000574 = "KISAO_0000574"
    SPECIES_TRANSITION_PROBABILITIES = "KISAO_0000574"

    # hybrid tau-leaping method
    KISAO_0000575 = "KISAO_0000575"
    HYBRID_TAU_LEAPING_METHOD = "KISAO_0000575"

    # quadratic MOMA
    KISAO_0000576 = "KISAO_0000576"
    QUADRATIC_MOMA = "KISAO_0000576"

    # flux minimization weight
    KISAO_0000577 = "KISAO_0000577"
    FLUX_MINIMIZATION_WEIGHT = "KISAO_0000577"

    # nested algorithm
    KISAO_0000578 = "KISAO_0000578"
    NESTED_ALGORITHM = "KISAO_0000578"

    # linear MOMA
    KISAO_0000579 = "KISAO_0000579"
    LINEAR_MOMA = "KISAO_0000579"

    # ROOM
    KISAO_0000580 = "KISAO_0000580"
    ROOM = "KISAO_0000580"

    # BKMC
    KISAO_0000581 = "KISAO_0000581"
    BKMC = "KISAO_0000581"

    # Spatiocyte method
    KISAO_0000582 = "KISAO_0000582"
    SPATIOCYTE_METHOD = "KISAO_0000582"

    # minimum order
    KISAO_0000583 = "KISAO_0000583"
    MINIMUM_ORDER = "KISAO_0000583"

    # initial order
    KISAO_0000584 = "KISAO_0000584"
    INITIAL_ORDER = "KISAO_0000584"

    # TOMS731
    KISAO_0000585 = "KISAO_0000585"
    TOMS731 = "KISAO_0000585"

    # Gibson-Bruck next reaction algorithm with indexed priority queue
    KISAO_0000586 = "KISAO_0000586"
    GIBSON_BRUCK_NEXT_REACTION_ALGORITHM_WITH_INDEXED_PRIORITY_QUEUE = "KISAO_0000586"

    # IMEX
    KISAO_0000587 = "KISAO_0000587"
    IMEX = "KISAO_0000587"

    # flux sampling
    KISAO_0000588 = "KISAO_0000588"
    FLUX_SAMPLING = "KISAO_0000588"

    # ACB flux sampling method
    KISAO_0000589 = "KISAO_0000589"
    ACB_FLUX_SAMPLING_METHOD = "KISAO_0000589"

    # ACHR flux sampling method
    KISAO_0000590 = "KISAO_0000590"
    ACHR_FLUX_SAMPLING_METHOD = "KISAO_0000590"

    # mdFBA
    KISAO_0000591 = "KISAO_0000591"
    MDFBA = "KISAO_0000591"

    # dynamic rFBA
    KISAO_0000592 = "KISAO_0000592"
    DYNAMIC_RFBA = "KISAO_0000592"

    # MOMA
    KISAO_0000593 = "KISAO_0000593"
    MOMA = "KISAO_0000593"

    # order
    KISAO_0000594 = "KISAO_0000594"
    ORDER = "KISAO_0000594"

    # rFBA
    KISAO_0000595 = "KISAO_0000595"
    RFBA = "KISAO_0000595"

    # srFBA
    KISAO_0000596 = "KISAO_0000596"
    SRFBA = "KISAO_0000596"

    # tolerance
    KISAO_0000597 = "KISAO_0000597"
    TOLERANCE = "KISAO_0000597"

    # hybrid Gibson - Milstein method
    KISAO_0000598 = "KISAO_0000598"
    HYBRID_GIBSON___MILSTEIN_METHOD = "KISAO_0000598"

    # hybrid Gibson - Euler-Maruyama method
    KISAO_0000599 = "KISAO_0000599"
    HYBRID_GIBSON___EULER_MARUYAMA_METHOD = "KISAO_0000599"

    # hybrid adaptive Gibson - Milstein method
    KISAO_0000600 = "KISAO_0000600"
    HYBRID_ADAPTIVE_GIBSON___MILSTEIN_METHOD = "KISAO_0000600"

    # number of trials
    KISAO_0000601 = "KISAO_0000601"
    NUMBER_OF_TRIALS = "KISAO_0000601"

    # minimum species threshold for continuous approximation
    KISAO_0000602 = "KISAO_0000602"
    MINIMUM_SPECIES_THRESHOLD_FOR_CONTINUOUS_APPROXIMATION = "KISAO_0000602"

    # minimum reaction rate for continuous approximation
    KISAO_0000603 = "KISAO_0000603"
    MINIMUM_REACTION_RATE_FOR_CONTINUOUS_APPROXIMATION = "KISAO_0000603"

    # MSR tolerance
    KISAO_0000604 = "KISAO_0000604"
    MSR_TOLERANCE = "KISAO_0000604"

    # SDE tolerance
    KISAO_0000605 = "KISAO_0000605"
    SDE_TOLERANCE = "KISAO_0000605"

    # hierarchical stochastic simulation algorithm
    KISAO_0000606 = "KISAO_0000606"
    HIERARCHICAL_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000606"

    # hierarchical Fehlberg method
    KISAO_0000607 = "KISAO_0000607"
    HIERARCHICAL_FEHLBERG_METHOD = "KISAO_0000607"

    # hierarchical flux balance analysis
    KISAO_0000608 = "KISAO_0000608"
    HIERARCHICAL_FLUX_BALANCE_ANALYSIS = "KISAO_0000608"

    # embedded Runge-Kutta Prince-Dormand (8,9) method
    KISAO_0000609 = "KISAO_0000609"
    EMBEDDED_RUNGE_KUTTA_PRINCE_DORMAND__8_9__METHOD = "KISAO_0000609"

    # composite-rejection stochastic simulation algorithm
    KISAO_0000610 = "KISAO_0000610"
    COMPOSITE_REJECTION_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000610"

    # incremental stochastic simulation algorithm
    KISAO_0000611 = "KISAO_0000611"
    INCREMENTAL_STOCHASTIC_SIMULATION_ALGORITHM = "KISAO_0000611"

    # implicit 4th order Runge-Kutta method at Gaussian points
    KISAO_0000612 = "KISAO_0000612"
    IMPLICIT_4TH_ORDER_RUNGE_KUTTA_METHOD_AT_GAUSSIAN_POINTS = "KISAO_0000612"

    # stochastic simulation algorithm with normally-distributed next reaction times
    KISAO_0000613 = "KISAO_0000613"
    STOCHASTIC_SIMULATION_ALGORITHM_WITH_NORMALLY_DISTRIBUTED_NEXT_REACTION_TIMES = (
        "KISAO_0000613"
    )

    # implementation
    KISAO_0000614 = "KISAO_0000614"
    IMPLEMENTATION = "KISAO_0000614"

    # fully-implicit regular grid finite volume method with a variable time step
    KISAO_0000615 = "KISAO_0000615"
    FULLY_IMPLICIT_REGULAR_GRID_FINITE_VOLUME_METHOD_WITH_A_VARIABLE_TIME_STEP = (
        "KISAO_0000615"
    )

    # semi-implicit regular grid finite volume method with a fixed time step
    KISAO_0000616 = "KISAO_0000616"
    SEMI_IMPLICIT_REGULAR_GRID_FINITE_VOLUME_METHOD_WITH_A_FIXED_TIME_STEP = (
        "KISAO_0000616"
    )

    # IDA-CVODE hybrid method
    KISAO_0000617 = "KISAO_0000617"
    IDA_CVODE_HYBRID_METHOD = "KISAO_0000617"

    # bunker
    KISAO_0000618 = "KISAO_0000618"
    BUNKER = "KISAO_0000618"

    # emc-sim
    KISAO_0000619 = "KISAO_0000619"
    EMC_SIM = "KISAO_0000619"

    # parsimonius flux balance analysis
    KISAO_0000620 = "KISAO_0000620"
    PARSIMONIUS_FLUX_BALANCE_ANALYSIS = "KISAO_0000620"

    # stochastic simulation leaping method
    KISAO_0000621 = "KISAO_0000621"
    STOCHASTIC_SIMULATION_LEAPING_METHOD = "KISAO_0000621"

    # flux balance method
    KISAO_0000622 = "KISAO_0000622"
    FLUX_BALANCE_METHOD = "KISAO_0000622"

    # flux balance problem
    KISAO_0000623 = "KISAO_0000623"
    FLUX_BALANCE_PROBLEM = "KISAO_0000623"

    # method for solving a system of linear equations
    KISAO_0000624 = "KISAO_0000624"
    METHOD_FOR_SOLVING_A_SYSTEM_OF_LINEAR_EQUATIONS = "KISAO_0000624"

    # dense direct solver
    KISAO_0000625 = "KISAO_0000625"
    DENSE_DIRECT_SOLVER = "KISAO_0000625"

    # band direct solver
    KISAO_0000626 = "KISAO_0000626"
    BAND_DIRECT_SOLVER = "KISAO_0000626"

    # diagonal approximate Jacobian solver
    KISAO_0000627 = "KISAO_0000627"
    DIAGONAL_APPROXIMATE_JACOBIAN_SOLVER = "KISAO_0000627"

    # modelling and simulation algorithm parameter value
    KISAO_0000628 = "KISAO_0000628"
    MODELLING_AND_SIMULATION_ALGORITHM_PARAMETER_VALUE = "KISAO_0000628"

    # null
    KISAO_0000629 = "KISAO_0000629"
    NULL = "KISAO_0000629"

    # root-finding method
    KISAO_0000630 = "KISAO_0000630"
    ROOT_FINDING_METHOD = "KISAO_0000630"

    # iterative root-finding method
    KISAO_0000631 = "KISAO_0000631"
    ITERATIVE_ROOT_FINDING_METHOD = "KISAO_0000631"

    # functional iteration root-finding method
    KISAO_0000632 = "KISAO_0000632"
    FUNCTIONAL_ITERATION_ROOT_FINDING_METHOD = "KISAO_0000632"

    # computational function
    KISAO_0000633 = "KISAO_0000633"
    COMPUTATIONAL_FUNCTION = "KISAO_0000633"

    # scaled property
    KISAO_0000634 = "KISAO_0000634"
    SCALED_PROPERTY = "KISAO_0000634"

    # unscaled property
    KISAO_0000635 = "KISAO_0000635"
    UNSCALED_PROPERTY = "KISAO_0000635"

    # primary property
    KISAO_0000636 = "KISAO_0000636"
    PRIMARY_PROPERTY = "KISAO_0000636"

    # derived property
    KISAO_0000637 = "KISAO_0000637"
    DERIVED_PROPERTY = "KISAO_0000637"

    # level
    KISAO_0000638 = "KISAO_0000638"
    LEVEL = "KISAO_0000638"

    # flux
    KISAO_0000639 = "KISAO_0000639"
    FLUX = "KISAO_0000639"

    # lower bound
    KISAO_0000640 = "KISAO_0000640"
    LOWER_BOUND = "KISAO_0000640"

    # bound
    KISAO_0000641 = "KISAO_0000641"
    BOUND = "KISAO_0000641"

    # minimum flux
    KISAO_0000642 = "KISAO_0000642"
    MINIMUM_FLUX = "KISAO_0000642"

    # upper bound
    KISAO_0000643 = "KISAO_0000643"
    UPPER_BOUND = "KISAO_0000643"

    # maximum flux
    KISAO_0000644 = "KISAO_0000644"
    MAXIMUM_FLUX = "KISAO_0000644"

    # objective value
    KISAO_0000645 = "KISAO_0000645"
    OBJECTIVE_VALUE = "KISAO_0000645"

    # propensity
    KISAO_0000646 = "KISAO_0000646"
    PROPENSITY = "KISAO_0000646"

    # derivative
    KISAO_0000647 = "KISAO_0000647"
    DERIVATIVE = "KISAO_0000647"

    # step
    KISAO_0000648 = "KISAO_0000648"
    STEP = "KISAO_0000648"

    # shadow price
    KISAO_0000649 = "KISAO_0000649"
    SHADOW_PRICE = "KISAO_0000649"

    # sensitivity
    KISAO_0000650 = "KISAO_0000650"
    SENSITIVITY = "KISAO_0000650"

    # reduced costs
    KISAO_0000651 = "KISAO_0000651"
    REDUCED_COSTS = "KISAO_0000651"

    # concentration rate
    KISAO_0000652 = "KISAO_0000652"
    CONCENTRATION_RATE = "KISAO_0000652"

    # particle number rate
    KISAO_0000653 = "KISAO_0000653"
    PARTICLE_NUMBER_RATE = "KISAO_0000653"

    # amount rate
    KISAO_0000654 = "KISAO_0000654"
    AMOUNT_RATE = "KISAO_0000654"

    # rate
    KISAO_0000655 = "KISAO_0000655"
    RATE = "KISAO_0000655"

    # use adaptive time steps
    KISAO_0000656 = "KISAO_0000656"
    USE_ADAPTIVE_TIME_STEPS = "KISAO_0000656"

    # sequential logical simulation method
    KISAO_0000657 = "KISAO_0000657"
    SEQUENTIAL_LOGICAL_SIMULATION_METHOD = "KISAO_0000657"

    # logical model analysis method
    KISAO_0000658 = "KISAO_0000658"
    LOGICAL_MODEL_ANALYSIS_METHOD = "KISAO_0000658"

    # Naldi MDD logical model stable state search method
    KISAO_0000659 = "KISAO_0000659"
    NALDI_MDD_LOGICAL_MODEL_STABLE_STATE_SEARCH_METHOD = "KISAO_0000659"

    # logical model stable state search method
    KISAO_0000660 = "KISAO_0000660"
    LOGICAL_MODEL_STABLE_STATE_SEARCH_METHOD = "KISAO_0000660"

    # logical model trap space identification method
    KISAO_0000661 = "KISAO_0000661"
    LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD = "KISAO_0000661"

    # Klarner ASP logical model trap space identification method
    KISAO_0000662 = "KISAO_0000662"
    KLARNER_ASP_LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD = "KISAO_0000662"

    # BDD logical model trap space identification method
    KISAO_0000663 = "KISAO_0000663"
    BDD_LOGICAL_MODEL_TRAP_SPACE_IDENTIFICATION_METHOD = "KISAO_0000663"

    # Second order backward implicit product Euler scheme
    KISAO_0000664 = "KISAO_0000664"
    SECOND_ORDER_BACKWARD_IMPLICIT_PRODUCT_EULER_SCHEME = "KISAO_0000664"

    # maximum number of iterations for root finding
    KISAO_0000665 = "KISAO_0000665"
    MAXIMUM_NUMBER_OF_ITERATIONS_FOR_ROOT_FINDING = "KISAO_0000665"

    # Jacobian epsilon
    KISAO_0000666 = "KISAO_0000666"
    JACOBIAN_EPSILON = "KISAO_0000666"

    # memory size
    KISAO_0000667 = "KISAO_0000667"
    MEMORY_SIZE = "KISAO_0000667"

    # Numerical Recipes in C 'stiff' Rosenbrock method
    KISAO_0000668 = "KISAO_0000668"
    NUMERICAL_RECIPES_IN_C__STIFF__ROSENBROCK_METHOD = "KISAO_0000668"

    # Resource Balance Analysis
    KISAO_0000669 = "KISAO_0000669"
    RESOURCE_BALANCE_ANALYSIS = "KISAO_0000669"

    # use multiple steps
    KISAO_0000670 = "KISAO_0000670"
    USE_MULTIPLE_STEPS = "KISAO_0000670"

    # use stiff method
    KISAO_0000671 = "KISAO_0000671"
    USE_STIFF_METHOD = "KISAO_0000671"

    # Numerical Recipes in C 'quality-controlled Runge-Kutta' method
    KISAO_0000672 = "KISAO_0000672"
    NUMERICAL_RECIPES_IN_C__QUALITY_CONTROLLED_RUNGE_KUTTA__METHOD = "KISAO_0000672"

    # skip reactions that produce negative species amounts
    KISAO_0000673 = "KISAO_0000673"
    SKIP_REACTIONS_THAT_PRODUCE_NEGATIVE_SPECIES_AMOUNTS = "KISAO_0000673"

    # presimulate
    KISAO_0000674 = "KISAO_0000674"
    PRESIMULATE = "KISAO_0000674"

    # Broyden method
    KISAO_0000675 = "KISAO_0000675"
    BROYDEN_METHOD = "KISAO_0000675"

    # degree of linearity
    KISAO_0000676 = "KISAO_0000676"
    DEGREE_OF_LINEARITY = "KISAO_0000676"

    # maximum number of steps for presimulation
    KISAO_0000677 = "KISAO_0000677"
    MAXIMUM_NUMBER_OF_STEPS_FOR_PRESIMULATION = "KISAO_0000677"

    # maximum number of steps for approximation
    KISAO_0000678 = "KISAO_0000678"
    MAXIMUM_NUMBER_OF_STEPS_FOR_APPROXIMATION = "KISAO_0000678"

    # maximum time for approximation
    KISAO_0000679 = "KISAO_0000679"
    MAXIMUM_TIME_FOR_APPROXIMATION = "KISAO_0000679"

    # duration
    KISAO_0000680 = "KISAO_0000680"
    DURATION = "KISAO_0000680"

    # maximum time
    KISAO_0000681 = "KISAO_0000681"
    MAXIMUM_TIME = "KISAO_0000681"

    # allow approximation
    KISAO_0000682 = "KISAO_0000682"
    ALLOW_APPROXIMATION = "KISAO_0000682"

    # relative tolerance for approximation
    KISAO_0000683 = "KISAO_0000683"
    RELATIVE_TOLERANCE_FOR_APPROXIMATION = "KISAO_0000683"

    # number of steps per output
    KISAO_0000684 = "KISAO_0000684"
    NUMBER_OF_STEPS_PER_OUTPUT = "KISAO_0000684"

    # biological state optimization method
    KISAO_0000685 = "KISAO_0000685"
    BIOLOGICAL_STATE_OPTIMIZATION_METHOD = "KISAO_0000685"

    # Enzyme Cost Minimization
    KISAO_0000686 = "KISAO_0000686"
    ENZYME_COST_MINIMIZATION = "KISAO_0000686"

    # Max-min Driving Force method
    KISAO_0000687 = "KISAO_0000687"
    MAX_MIN_DRIVING_FORCE_METHOD = "KISAO_0000687"

    # type of system described
    KISAO_0000688 = "KISAO_0000688"
    TYPE_OF_SYSTEM_DESCRIBED = "KISAO_0000688"

    # mathematical system
    KISAO_0000689 = "KISAO_0000689"
    MATHEMATICAL_SYSTEM = "KISAO_0000689"

    # biological system
    KISAO_0000690 = "KISAO_0000690"
    BIOLOGICAL_SYSTEM = "KISAO_0000690"

    # metabolic system
    KISAO_0000691 = "KISAO_0000691"
    METABOLIC_SYSTEM = "KISAO_0000691"

    # cellular system
    KISAO_0000692 = "KISAO_0000692"
    CELLULAR_SYSTEM = "KISAO_0000692"

    # biochemical system
    KISAO_0000693 = "KISAO_0000693"
    BIOCHEMICAL_SYSTEM = "KISAO_0000693"

    # systems property
    KISAO_0000800 = "KISAO_0000800"
    SYSTEMS_PROPERTY = "KISAO_0000800"

    # concentration control coefficient matrix (unscaled)
    KISAO_0000801 = "KISAO_0000801"
    CONCENTRATION_CONTROL_COEFFICIENT_MATRIX__UNSCALED_ = "KISAO_0000801"

    # control coefficient (scaled)
    KISAO_0000802 = "KISAO_0000802"
    CONTROL_COEFFICIENT__SCALED_ = "KISAO_0000802"

    # control coefficient (unscaled)
    KISAO_0000803 = "KISAO_0000803"
    CONTROL_COEFFICIENT__UNSCALED_ = "KISAO_0000803"

    # elasticity matrix (unscaled)
    KISAO_0000804 = "KISAO_0000804"
    ELASTICITY_MATRIX__UNSCALED_ = "KISAO_0000804"

    # elasticity coefficient (unscaled)
    KISAO_0000805 = "KISAO_0000805"
    ELASTICITY_COEFFICIENT__UNSCALED_ = "KISAO_0000805"

    # elasticity matrix (scaled)
    KISAO_0000806 = "KISAO_0000806"
    ELASTICITY_MATRIX__SCALED_ = "KISAO_0000806"

    # elasticity coefficient (scaled)
    KISAO_0000807 = "KISAO_0000807"
    ELASTICITY_COEFFICIENT__SCALED_ = "KISAO_0000807"

    # reduced stoichiometry matrix
    KISAO_0000808 = "KISAO_0000808"
    REDUCED_STOICHIOMETRY_MATRIX = "KISAO_0000808"

    # reduced Jacobian matrix
    KISAO_0000809 = "KISAO_0000809"
    REDUCED_JACOBIAN_MATRIX = "KISAO_0000809"

    # reduced eigenvalue matrix
    KISAO_0000810 = "KISAO_0000810"
    REDUCED_EIGENVALUE_MATRIX = "KISAO_0000810"

    # stoichiometry matrix
    KISAO_0000811 = "KISAO_0000811"
    STOICHIOMETRY_MATRIX = "KISAO_0000811"

    # Jacobian matrix
    KISAO_0000812 = "KISAO_0000812"
    JACOBIAN_MATRIX = "KISAO_0000812"

    # Eigenvalue matrix
    KISAO_0000813 = "KISAO_0000813"
    EIGENVALUE_MATRIX = "KISAO_0000813"

    # flux control coefficient matrix (unscaled)
    KISAO_0000814 = "KISAO_0000814"
    FLUX_CONTROL_COEFFICIENT_MATRIX__UNSCALED_ = "KISAO_0000814"

    # flux control coefficient matrix (scaled)
    KISAO_0000815 = "KISAO_0000815"
    FLUX_CONTROL_COEFFICIENT_MATRIX__SCALED_ = "KISAO_0000815"

    # link matrix
    KISAO_0000816 = "KISAO_0000816"
    LINK_MATRIX = "KISAO_0000816"

    # kernel matrix
    KISAO_0000817 = "KISAO_0000817"
    KERNEL_MATRIX = "KISAO_0000817"

    # L0 matrix
    KISAO_0000818 = "KISAO_0000818"
    L0_MATRIX = "KISAO_0000818"

    # Nr matrix
    KISAO_0000819 = "KISAO_0000819"
    NR_MATRIX = "KISAO_0000819"

    # model and simulation property characteristic
    KISAO_0000820 = "KISAO_0000820"
    MODEL_AND_SIMULATION_PROPERTY_CHARACTERISTIC = "KISAO_0000820"

    # intensive property
    KISAO_0000821 = "KISAO_0000821"
    INTENSIVE_PROPERTY = "KISAO_0000821"

    # extensive property
    KISAO_0000822 = "KISAO_0000822"
    EXTENSIVE_PROPERTY = "KISAO_0000822"

    # aggregation function
    KISAO_0000824 = "KISAO_0000824"
    AGGREGATION_FUNCTION = "KISAO_0000824"

    # mean ignoring NaN
    KISAO_0000825 = "KISAO_0000825"
    MEAN_IGNORING_NAN = "KISAO_0000825"

    # standard deviation ignoring NaN
    KISAO_0000826 = "KISAO_0000826"
    STANDARD_DEVIATION_IGNORING_NAN = "KISAO_0000826"

    # standard error ignoring NaN
    KISAO_0000827 = "KISAO_0000827"
    STANDARD_ERROR_IGNORING_NAN = "KISAO_0000827"

    # maximum ignoring NaN
    KISAO_0000828 = "KISAO_0000828"
    MAXIMUM_IGNORING_NAN = "KISAO_0000828"

    # minimum ignoring NaN
    KISAO_0000829 = "KISAO_0000829"
    MINIMUM_IGNORING_NAN = "KISAO_0000829"

    # maximum
    KISAO_0000830 = "KISAO_0000830"
    MAXIMUM = "KISAO_0000830"

    # model and simulation property
    KISAO_0000831 = "KISAO_0000831"
    MODEL_AND_SIMULATION_PROPERTY = "KISAO_0000831"

    # time
    KISAO_0000832 = "KISAO_0000832"
    TIME = "KISAO_0000832"

    # rate of change
    KISAO_0000834 = "KISAO_0000834"
    RATE_OF_CHANGE = "KISAO_0000834"

    # concentration control coefficient matrix (scaled)
    KISAO_0000835 = "KISAO_0000835"
    CONCENTRATION_CONTROL_COEFFICIENT_MATRIX__SCALED_ = "KISAO_0000835"

    # amount
    KISAO_0000836 = "KISAO_0000836"
    AMOUNT = "KISAO_0000836"

    # particle number
    KISAO_0000837 = "KISAO_0000837"
    PARTICLE_NUMBER = "KISAO_0000837"

    # concentration
    KISAO_0000838 = "KISAO_0000838"
    CONCENTRATION = "KISAO_0000838"

    # temperature
    KISAO_0000839 = "KISAO_0000839"
    TEMPERATURE = "KISAO_0000839"

    # minimum
    KISAO_0000840 = "KISAO_0000840"
    MINIMUM = "KISAO_0000840"

    # mean
    KISAO_0000841 = "KISAO_0000841"
    MEAN = "KISAO_0000841"

    # standard deviation
    KISAO_0000842 = "KISAO_0000842"
    STANDARD_DEVIATION = "KISAO_0000842"

    # standard error
    KISAO_0000843 = "KISAO_0000843"
    STANDARD_ERROR = "KISAO_0000843"

    # sum ignoring NaN
    KISAO_0000844 = "KISAO_0000844"
    SUM_IGNORING_NAN = "KISAO_0000844"

    # sum
    KISAO_0000845 = "KISAO_0000845"
    SUM = "KISAO_0000845"

    # product ignoring NaN
    KISAO_0000846 = "KISAO_0000846"
    PRODUCT_IGNORING_NAN = "KISAO_0000846"

    # product
    KISAO_0000847 = "KISAO_0000847"
    PRODUCT = "KISAO_0000847"

    # cumulative sum ignoring NaN
    KISAO_0000848 = "KISAO_0000848"
    CUMULATIVE_SUM_IGNORING_NAN = "KISAO_0000848"

    # cumulative sum
    KISAO_0000849 = "KISAO_0000849"
    CUMULATIVE_SUM = "KISAO_0000849"

    # cumulative product ignoring NaN
    KISAO_0000850 = "KISAO_0000850"
    CUMULATIVE_PRODUCT_IGNORING_NAN = "KISAO_0000850"

    # cumulative product
    KISAO_0000851 = "KISAO_0000851"
    CUMULATIVE_PRODUCT = "KISAO_0000851"

    # count ignoring NaN
    KISAO_0000852 = "KISAO_0000852"
    COUNT_IGNORING_NAN = "KISAO_0000852"

    # count
    KISAO_0000853 = "KISAO_0000853"
    COUNT = "KISAO_0000853"

    # length ignoring NaN
    KISAO_0000854 = "KISAO_0000854"
    LENGTH_IGNORING_NAN = "KISAO_0000854"

    # length
    KISAO_0000855 = "KISAO_0000855"
    LENGTH = "KISAO_0000855"

    # median ignoring NaN
    KISAO_0000856 = "KISAO_0000856"
    MEDIAN_IGNORING_NAN = "KISAO_0000856"

    # median
    KISAO_0000857 = "KISAO_0000857"
    MEDIAN = "KISAO_0000857"

    # variance ignoring NaN
    KISAO_0000858 = "KISAO_0000858"
    VARIANCE_IGNORING_NAN = "KISAO_0000858"

    # variance
    KISAO_0000859 = "KISAO_0000859"
    VARIANCE = "KISAO_0000859"

    @staticmethod
    def get_name(kisao: "KISAO") -> Optional[str]:
        """Get name for term.

        :returns: None if term does not exist in ontology.
        """
        return _terms.get(kisao.value, None)

    @classmethod
    def validate(cls, kisao: "KISAOType") -> "KISAO":
        """Validate and normalize kisao."""
        term: "KISAO"
        if isinstance(kisao, str):
            if not kisao.startswith("KISAO"):
                raise ValueError(kisao + " is not a KISAO id.")
            if kisao.startswith("KISAO:"):
                kisao = kisao.replace(":", "_")

            term = getattr(cls, kisao)

        elif isinstance(kisao, "KISAO"):
            term = kisao
        else:
            raise ValueError

        return term


__all__ = [
    "KISAO",
    "KISAOType",
]
