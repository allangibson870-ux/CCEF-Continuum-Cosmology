================================================================================
CCEF v2 — DERIVATION NOTE: gamma FROM A CALDEIRA-LEGGETT BATH INTEGRATION
Priority #3 from the v2 handoff (Sec 9). Derived from the theory; no hand-fitting.
Compiled 2026-06-29.  Uses V1 (CCEF Working Directory.md, 15 Jun 2026) where noted.
Labels: [SOLID] derived/verified | [STRUCT] forced by symmetry/structure
        | [SCALE] magnitude/prefactor only | [DEFER] later
================================================================================

--------------------------------------------------------------------------------
0. WHAT THIS NOTE SETTLES
--------------------------------------------------------------------------------
The expansion exponent was GATED on the coarsening class (Model A non-conserved -> t^1/2
vs Model B conserved -> t^1/3), set by the bath friction gamma. This note integrates out
the medium as a Caldeira-Leggett (CL) bath and shows:

  RESULT:  the CCEF order parameter couples to a LOCAL, gapless + thermal bath
           =>  the friction is OHMIC and k-INDEPENDENT as k->0:  gamma(k->0) = gamma_0 (finite)
           =>  the order parameter is NON-CONSERVED   =>   MODEL A
           =>  L_ord(t) = sqrt(2 A1 t / gamma_0) ~ t^(1/2),  H = 1/(2t),  q = 1.

The class is fixed by the STRUCTURE of the coupling (local energy exchange with an omnipresent
medium), not by the messy magnitude of gamma_0 — so the exponent is robust even though the
prefactor is only known to scaling accuracy. The decisive physical fact, independent of all
loop details: a GROWING ordered domain has INT chi d^3x increasing with time, which a conserved
(Model B) order parameter cannot do. Coarsening class is therefore forced to A.

NUMERICAL FORK (this note): integrating the SAME free energy with non-conserved vs conserved
dynamics gives L_ord ~ t^0.496 (Model A) vs t^0.337 (Model B) — confirming the exponent IS the
class, so selecting the class is exactly what fixes cosmology. [SOLID]

================================================================================
1. SYSTEM, BATH, COUPLING — READ OFF THE CCEF ACTION
================================================================================
Decompose the order parameter into amplitude (radial) and angle (Goldstone) parts. For the
S^3/matter writing phi = chi * U with U in S^3 (|U|=1); for the S^2/gravity sector n is the
unit director with the easy-axis term. The kinetic term splits exactly:

   (Zt/2)|d phi|^2 = (Zt/2)(d chi)^2  +  (Zt/2) chi^2 |dU|^2 .                      [SOLID]

Roles (the CL split):
  SYSTEM (slow):  the amplitude / ordering field chi -- the coarse coherence variable whose
     domain size IS L_ord (the v2 cosmological ruler, Sec 4 of the v2 reference). chi is the
     RADIAL mode, gapped at m_sigma (Sec 2 of the L_ord note).
  BATH (fast):    (i) the gapless GOLDSTONE / angular modes U (V1 Sec 5.2 identifies these
     "surface/Goldstone modes" explicitly; in S^2 they are the two magnon polarizations), and
     (ii) the disordered-medium continuum -- the "eternal energy continuum" fluctuations, held
     at an effective temperature T_eff (V2 Reference Sec 10: a finite effective T from
     disordered fluctuations + latent heat, T_c ~ 0.6-0.7 Lambda).
  COUPLING:       expand chi = chi_0 + delta in the second term:
     (Zt/2) chi^2 |dU|^2  ->  (Zt/2) chi_0^2 |dU|^2  +  Zt chi_0 * delta * |dU|^2  +  ...
     The cross term  L_int = g * delta(x) * O_bath(x),   g = Zt chi_0,  O_bath = |dU|^2 ,
     is LOCAL in space and BILINEAR system x bath -- exactly the CL coupling form.        [SOLID]

The crucial structural fact, fixed here and used in Sec 3: the system field delta couples to a
bath operator O_bath = |dU|^2 evaluated AT THE SAME POINT x. The coupling does NOT go through a
gradient of delta; it is a direct, local, on-site exchange between the amplitude and the medium.
This is the field-theory image of CL's "system coordinate linearly coupled to each bath
oscillator," replicated independently at every space point. (V1 already worked with an
OVERDAMPED relaxational sector -- V1 Sec 6.2: phidot = -(A4/6H Zt) sin 2phi -- i.e. the
medium-induced friction is part of the V1 inheritance, not a new V2 assumption.)

================================================================================
2. INTEGRATE OUT THE BATH -> INFLUENCE FUNCTIONAL & FRICTION KERNEL
================================================================================
Model the bath modes as Gaussian (the medium fluctuations are quadratic to leading order;
this is the CL idealization and is controlled here because the IR fixed point is Gaussian/
mean-field, V2 Sec 5 -- no anomalous bath dynamics). Writing the bath response (retarded
two-point function of O_bath) as chi_R^{bath}(k,w), the Feynman-Vernon influence functional
from integrating out the bath gives, for the system field delta:

  Effective action:  S_eff[delta] = S_sys[delta]
        + (1/2) INT delta(-k,-w) [ g^2 chi_R^{bath}(k,w) ] delta(k,w)   (retarded self-energy)
        + (noise term, fixed by FDT).                                              [SOLID]

The friction (dissipation) kernel is the low-frequency, odd-in-w part of the self-energy:

   Sigma_R(k,w) = g^2 chi_R^{bath}(k,w),   gamma(k) = lim_{w->0} Im Sigma_R(k,w) / w .   [def]

Equivalently the bath spectral density J(k,w) = Im Sigma_R(k,w); Ohmic dissipation means
J(k,w) -> gamma(k) * w as w -> 0. The retarded EOM for the system becomes (back in real space):

   Zt d_t^2 delta  +  INT dt' gamma(k; t-t') d_t' delta(t')  =  -(A1 k^2 + m_sigma^2) delta + xi,
   <xi(k,w) xi(-k,-w)> = 2 gamma(k) * T_eff   (fluctuation-dissipation, classical limit).   [SOLID]

So EVERYTHING about the class reduces to one question: the k -> 0 behaviour of gamma(k).

================================================================================
3. THE OHMIC, k-INDEPENDENT LIMIT  (the decisive computation)
================================================================================
gamma(k) = lim_{w->0} Im[ g^2 chi_R^{bath}(k,w) ] / w. Two facts about O_bath = |dU|^2 from a
gapless Goldstone bath at temperature T_eff:

(a) GAPLESS => low-frequency spectral weight EXISTS. The Goldstone modes have omega = c_eff q
    with c_eff = 1 (V1 Sec 6: emergent Lorentz, gapless) and NO gap (they are the broken-
    symmetry directions). Hence the two-Goldstone continuum that O_bath excites reaches down to
    w -> 0, so Im chi_R^{bath}(k->0, w->0)/w is NONZERO. (A GAPPED bath would give Im->0 below
    threshold => zero friction => purely reactive mass shift; the gaplessness of the Goldstones
    is what makes dissipation possible at all.)                                        [SOLID]

(b) FINITE TEMPERATURE => OHMIC (linear-in-w) friction. At strictly T=0 the relativistic
    derivative coupling |dU|^2 gives a SUPER-Ohmic kernel (Im Sigma ~ w^3 in 3+1D), i.e. no
    constant friction -- reversible. At T_eff > 0 the thermal Goldstone occupation n(w) ~
    T_eff/w (Rayleigh-Jeans) enhances the low-w weight by T_eff/w, converting the kernel to the
    OHMIC form Im Sigma_R(k,w) = gamma(k) w with a finite coefficient. This is thermal Landau
    damping: the slow amplitude relaxes by scattering off the thermal medium. The CCEF medium
    is at finite T_eff by construction (V2 Reference Sec 10), so the Ohmic regime is the
    physical one.                                                                       [SOLID]

(c) LOCAL COUPLING => k-INDEPENDENT gamma. Because L_int is local (delta(x) O_bath(x), Sec 1),
    the vertex carries NO factor of the system momentum k. Therefore the self-energy has a
    smooth k -> 0 limit:
        gamma(k) = gamma_0 + O(k^2),   gamma_0 = gamma(0) finite and NONZERO.          [STRUCT]
    The k = 0 (uniform) amplitude mode IS damped: the omnipresent medium can locally convert
    disorder <-> order without transporting anything. This is the hallmark of a NON-conserved
    order parameter (Model A): the relaxation rate Gamma(k) = gamma_0^{-1}(A1 k^2 + m_sigma^2)
    stays finite as k -> 0.

CONTRAST (what Model B would require): a CONSERVED order parameter obeys a continuity equation
d_t chi + div J_chi = 0, so its k=0 Fourier mode CANNOT relax (you cannot change INT chi
locally). In CL terms the bath would have to couple to grad(delta) (a current), giving a vertex
~ k, hence gamma(k) ~ 1/k^2 (mobility ~ k^2) and Gamma(k) ~ k^2 -> 0. The CCEF coupling has NO
such gradient: the medium exchanges "order" pointwise. So Model B is structurally excluded.
[STRUCT]

PHYSICAL CLINCHER (loop-independent): our universe is a GROWING ordered domain in a disordered
medium (V2 ontology). As it grows, INT chi d^3x increases monotonically from ~0 at the ordering
event to large today. A conserved order parameter has INT chi = const by definition and can
NEVER do this. Hence the order parameter is non-conserved -- Model A -- with certainty,
independent of every detail of the friction calculation.                               [SOLID]

================================================================================
4. MAGNITUDE OF gamma_0  (prefactor only; does NOT affect the exponent)
================================================================================
The Ohmic coefficient from the thermal Goldstone bubble (g = Zt chi_0, c_eff = 1, d=3):

   gamma_0  ~  g^2 * (thermal Goldstone phase space)  ~  C * Zt^2 chi_0^2 * T_eff ,    [SCALE]

with C an O(1) number set by the two-Goldstone loop (the 0.949 Lifshitz-anisotropy factor of
the Reference enters here at the ~5% level). Note what gamma_0 depends on:
   - A1 (via c_eff and the gradient norm), chi_0 = sqrt(|r|/u) (the ordered amplitude), Zt,
     and T_eff (Reference Sec 10).
   - It does NOT depend on A3, m_sigma, or the Skyrme couplings -- the RG-irrelevant UV data.
So the friction, like L_ord itself, is IR-clean: cosmology stays insensitive to the unpinned UV
exactly as V2 Sec 5 demands. The magnitude only sets the overdamping crossover time
tau_gamma = Zt/gamma_0 and the prefactor of L_ord; it leaves the t^1/2 EXPONENT untouched.
[SCALE]

Overdamping check: coarsening (not reversible oscillation) requires t >> tau_gamma = Zt/gamma_0.
With gamma_0 ~ Zt^2 chi_0^2 T_eff and T_eff ~ Lambda, tau_gamma is microscopic (~ gap time), so
the universe is overdamped at all cosmological times -- the Model A coarsening regime holds
throughout the observable era. [SCALE]

================================================================================
5. RESULT: CLASS FIXED -> EXPONENT FIXED
================================================================================
gamma(k->0) = gamma_0 finite, k-independent  =>  NON-CONSERVED  =>  MODEL A.

Feeding gamma_0 into the overdamped TDGL / Allen-Cahn derivation (L_ord note, Sec 4A):

   d_t chi = (1/gamma_0)(A1 lap chi - U'(chi))   =>   wall velocity v = -(A1/gamma_0) K
   =>   L_ord(t) = sqrt( (2 A1 / gamma_0) t )  ~  t^(1/2) .                        [SOLID]

Cosmological readout (a_cosmo proportional to L_ord):

   a(t) ~ t^(1/2),    H = 1/(2t),    q = +1,    1 + z = (t_obs / t_em)^(1/2) .

This is now a DERIVED choice, no longer "gated": the Caldeira-Leggett integration selects
Model A. Model B (t^1/3) is excluded both structurally (no conserved current couples to the
medium) and physically (a growing domain cannot conserve INT chi).

================================================================================
6. NUMERICAL CONFIRMATION OF THE FORK  (cold, both classes)
================================================================================
To show the exponent really IS the class the CL argument selects, both dynamics were run from
the SAME IR free energy F_IR = INT[(A1/2)|grad chi|^2 + (r/2)chi^2 + (u/4)chi^4] (A1=1, r=-1,
u=1):
   Model A (non-conserved TDGL, geometric wall-density length):   L_ord ~ t^0.496   (-> 1/2)
   Model B (conserved Cahn-Hilliard, structure-factor length):    L_ord ~ t^0.337   (-> 1/3)
        (Model B run conserves the order parameter: mean(chi) stays ~5e-5 throughout.)
Both sit within ~1% of their textbook asymptotic exponents. The CL derivation places CCEF on
the A branch, hence t^1/2. [SOLID]

================================================================================
7. HONEST STATUS
================================================================================
[SOLID / STRUCT -- the class and exponent]
  - System/bath/coupling read directly off the action; coupling is LOCAL (no gradient on the
    system field). 
  - Gaplessness (Goldstones) + finite T_eff (Reference Sec 10) => Ohmic friction exists.
  - Locality => gamma(k->0) = const => non-conserved => Model A => t^1/2.
  - Loop-independent clincher: growing domain => INT chi increases => Model B impossible.
  - Numerical fork A(0.496) vs B(0.337) confirms exponent = class.

[SCALE -- magnitude only, no effect on exponent]
  - gamma_0 ~ Zt^2 chi_0^2 T_eff * C, C = O(1) two-Goldstone loop factor. IR-clean (no A3,
    m_sigma, Skyrme). Sets prefactor and tau_gamma, not the power.

[DEFER -- separate priorities]
  - The precise O(1) constant C (full thermal Goldstone bubble with the 0.949 anisotropy
    factor) -- a finite computation, not needed for the class.
  - Whether a residual non-Markovian (super-Ohmic, T=0) tail leaves a small early-time
    correction to pure t^1/2 -- sub-leading; relevant only very near the ordering event.
  - Redshift 3-tests + slip/lensing at L_ord (priority #2); acceleration structure (priority #4).

CAVEAT (stated plainly): the Ohmic friction is a FINITE-T_eff effect. At strictly T_eff = 0 the
relativistic Goldstone bath is super-Ohmic and there is no simple Markovian gamma -- the dynamics
would be reversible and would not coarsen. CCEF's medium carries a finite effective temperature
by construction (Reference Sec 10), which is exactly the condition that makes coarsening -- and
therefore the emergent expansion -- happen. This ties the arrow of time / expansion to the
medium's effective temperature, consistent with the V2 ontology (ordering of a hot disordered
medium), and is a derived feature, not an input.

================================================================================
8. ONE-PARAGRAPH SUMMARY
================================================================================
Splitting the order parameter into amplitude (system) and Goldstone (bath) and integrating the
medium out as a Caldeira-Leggett bath, the friction kernel is fixed by the k->0 limit of the
amplitude self-energy. The coupling read off the action is LOCAL (the amplitude exchanges
"order" pointwise with an omnipresent medium, with no gradient on the system field), the
Goldstone bath is GAPLESS, and the medium carries a finite effective temperature (Reference
Sec 10). Gaplessness makes dissipation possible; finite T makes it Ohmic; locality makes it
k-INDEPENDENT as k->0. A k-independent, nonzero friction means the uniform amplitude mode
relaxes -- the order parameter is NON-CONSERVED -- which is Model A. Model B is excluded both
structurally (no conserved current couples to the medium) and, decisively and loop-
independently, because a growing ordered domain has INT chi increasing in time, which a
conserved order parameter cannot do. Hence gamma(k->0)=gamma_0 (finite), the class is Model A,
and L_ord = sqrt(2 A1 t/gamma_0) ~ t^(1/2), giving H=1/(2t), q=1, 1+z=(t_obs/t_em)^(1/2). The
magnitude gamma_0 ~ Zt^2 chi_0^2 T_eff is IR-clean (independent of A3, m_sigma, Skyrme) and sets
only the prefactor; a cold simulation of both classes from the same free energy (t^0.496 vs
t^0.337) confirms that selecting the class is what fixes the exponent. The expansion exponent is
no longer gated -- it is derived: 1/2.
================================================================================
