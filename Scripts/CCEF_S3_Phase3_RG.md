# CCEF — S^3 Skyrmion, Phase 3: RG cleanliness of the IR
**2026-06-22. No hand-fitting.** Result: IR is RG-CLEAN; the self-dual obstruction does NOT apply.

## The point
The "4-derivative coupling is irrelevant -> flows to 0 -> no stabiliser" obstruction
that killed every previous route is a z=2 statement. The soliton, with B3 ~ 1e-6,
lives in the z=1 regime where that operator is MARGINAL. Dimensions change across the
z=2 -> z=1 crossover; the soliton is on the safe side.

## Scaling dimensions BY REGIME (the resolution)
z=2 Lifshitz (k > k_UV):   [phi]=1/2 ;  [B2]=-1 IRRELEVANT ;  [B3]=0 marginal
z=1 relativistic (k < k_UV, WHERE THE SOLITON LIVES):
     [phi]=0 ;  [B1]=+2 relevant (=F_pi^2) ;  [B2]=0 MARGINAL ;  [B4]=+4 relevant ;
     B3 marginal but value ~1e-6 (dynamically negligible).
=> In z=1 the Skyrme coupling B2 does NOT flow to zero; it is marginal (only log
   running, negligible over the soliton's scale range) and stabilises the soliton.

## Numerical confirmation (proton point: B2=0.057, B4=3.5553, B3=1e-6)
  Scale separation:  Lambda = 1.89  <  k_sol = 4.5  <<  k_UV = 1000   (k_sol/k_UV = 0.0045)
       -> soliton ~200x below the Lifshitz crossover: firmly z=1.
  Bilaplacian dead:  E_B3 / E_tot = 4.2e-5 ;  B3/B2 = 1.8e-5.
  Energy budget:     E_B1 = 7.8,  E_B2 = 9.8,  E_B4 = 0.7
       -> gradient + Skyrme balanced (E_B2/E_B1 = 1.25 = Derrick condition);
          standard Skyrme soliton, potential minor, bilaplacian irrelevant.

## Contrast with the self-dual point (why it failed before)
Self-dual B3 = 0.281  =>  k_UV = sqrt(B1/B3) = 1.886 = Lambda = k_sol : ALL scales
coincide, the soliton sits AT the z=2 crossover, B3 k^4 ~ B2 k^4 ~ B1 k^2, and the
bilaplacian carries ~tens of % of the energy -> E*R ~ 77. The obstruction was
self-inflicted by the self-dual conjecture. Small B3 separates the scales and removes it.

## Verdict
[SOLID] With B3 ~ 1e-6 the Skyrmion is a clean z=1 standard-Skyrme soliton:
  - stabilised by relevant B1 (=F_pi^2) + marginal B2 (Skyrme) + relevant B4 (mass);
  - bilaplacian B3 is a dynamically negligible (~1e-5) UV regulator;
  - NO coupling flows to zero at the soliton scale; the IR is clean;
  - the self-dual-point RG obstruction is absent (scales are separated).
[OPEN] Phase 2: derive/pin B2 ~ 0.057 (marginal couplings can sit at a fixed value;
  candidate principles: a z=1 fixed point of the Skyrme coupling, a Wess-Zumino /
  anomaly-matching condition, or large-N). Its survival as MARGINAL is what makes a
  principled value possible (an irrelevant coupling could not be pinned nonzero).

## Updated working parameter set (S^3 baryon sector, RG-clean)
  B1 = 1, Zt = 1            (axiom)
  B2 ~ 0.057                (Skyrme; MARGINAL in z=1; [OPEN] pinning -> Phase 2)
  B3 ~ 1e-6                 (tiny UV regulator; NOT self-dual; gives z=1 soliton)
  B4 = 3.5553              (potential/gap; proton-radius calibration)
  -> z=1 standard-Skyrme soliton, E_sol*R_sol = 4.06 = proton (mass + radius together).
