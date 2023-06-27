// --------------------------------------------------------------------------------------- //
// Implimentation of RDataFrame in C++.					                   //
// Comments on creating a singly produced VLQ search			                   //
// To Run on Command Line:   root -l callRDF.C\(\"Muon(OR)Electron\",\"testNumber\"\,\"root://cmsxrootd.fnal.gov//store/...file.root\")      //
// --------------------------------------------------------------------------------------- //

#define rdf_cxx
#include "analyzer_RDF.h"
#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "Math/Vector4D.h"
#include <TFile.h>
#include <TChain.h>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>
#include <TCanvas.h>
#include <TStyle.h>
#include <TH3.h>
#include <algorithm> // std::sort
#include <TFile.h>
#include <TH1.h>
#include <TF1.h>
#include <TRandom3.h>
#include <sstream>
#include <chrono> // for high_resolution_clock

using namespace ROOT::VecOps;
void rdf::analyzer_RDF(TString testNum)
{
  ROOT::EnableImplicitMT();
  TStopwatch time;
  time.Start();
  bool isNominal = this->isNominal;
  TString sample = this->sample;
  
// --------------------------------------------------------------------------------------------------------------------
// 							LAMBDA FXNS
// --------------------------------------------------------------------------------------------------------------------

// ----------------------------------------------------
//           Bprime truth extraction:
// ----------------------------------------------------
auto Bprime_gen_info = [sample](unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<float> &GenPart_mass, ROOT::VecOps::RVec<float> &GenPart_pt, ROOT::VecOps::RVec<float> &GenPart_phi, ROOT::VecOps::RVec<float> &GenPart_eta, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &GenPart_status, ROOT::VecOps::RVec<int> &GenPart_statusFlags)
{
  ROOT::VecOps::RVec<float> BPrimeInfo(6, -999);
  if (sample != "Bprime")
  {
    return BPrimeInfo;
  }

  for (unsigned int i = 0; i < nGenPart; i++)
  {
    int id = GenPart_pdgId[i];
    if (abs(id) != 6000007)
    {
      continue;
    }

    std::bitset<15> statusFlags(GenPart_statusFlags[i]);
    if (statusFlags.to_string()[1] == '0')
    {
      continue;
    } // takes the last B'
    BPrimeInfo[0] = GenPart_pt[i];
    BPrimeInfo[1] = GenPart_eta[i];
    BPrimeInfo[2] = GenPart_phi[i];
    BPrimeInfo[3] = GenPart_mass[i];
    BPrimeInfo[4] = GenPart_pdgId[i];
    BPrimeInfo[5] = GenPart_status[i];
  }

  return BPrimeInfo; // if entries -999, then no Bprime was found
};

// ----------------------------------------------------
//           t truth extraction:
// ----------------------------------------------------
auto t_gen_info = [sample](unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<float> &GenPart_mass, ROOT::VecOps::RVec<float> &GenPart_pt, ROOT::VecOps::RVec<float> &GenPart_phi, ROOT::VecOps::RVec<float> &GenPart_eta, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &GenPart_status)
{
  ROOT::VecOps::RVec<float> t_gen_info(30, -999);
  if (sample != "Bprime")
  {
    return t_gen_info;
  }

  int trueLeptonicT = -1;
  for (unsigned int i = 0; i < nGenPart; i++)
  {
    int id = GenPart_pdgId[i];
    int motherIdx = GenPart_genPartIdxMother[i];

    if (abs(GenPart_pdgId[motherIdx]) != 6)
    {
      continue;
    } // find t daughters
    if (abs(id) != 24 && abs(id) != 5)
    {
      continue;
    }

    // store t info
    t_gen_info[0] = GenPart_pt[motherIdx];
    t_gen_info[1] = GenPart_eta[motherIdx];
    t_gen_info[2] = GenPart_phi[motherIdx];
    t_gen_info[3] = GenPart_mass[motherIdx];
    t_gen_info[4] = GenPart_pdgId[motherIdx];
    t_gen_info[5] = GenPart_status[motherIdx];

    int igen = i;
    for (unsigned int j = i; j < nGenPart; j++)
    {
      if (GenPart_pdgId[j] != id)
      {
        continue;
      }
      if (GenPart_genPartIdxMother[j] != igen)
      {
        continue;
      }
      igen = j; // take the last copy of t daughter
    }

    if (abs(id) == 5)
    { // store b info
      t_gen_info[6] = GenPart_pt[igen];
      t_gen_info[7] = GenPart_eta[igen];
      t_gen_info[8] = GenPart_phi[igen]; // did not record gen mass, because =0 for all b
      t_gen_info[9] = GenPart_pdgId[igen];
      t_gen_info[10] = GenPart_status[igen];
    }
    else
    { // store W info
      t_gen_info[11] = GenPart_pt[igen];
      t_gen_info[12] = GenPart_eta[igen];
      t_gen_info[13] = GenPart_phi[igen];
      t_gen_info[14] = GenPart_mass[igen];
      t_gen_info[15] = GenPart_pdgId[igen];
      t_gen_info[16] = GenPart_status[igen];
      for (unsigned int j = igen; j < nGenPart; j++)
      {
        if (GenPart_genPartIdxMother[j] != igen)
        {
          continue;
        } // look for W daughters
        int j_id = GenPart_pdgId[j];

        int jgen = j;
        for (unsigned int k = j; k < nGenPart; k++)
        {
          if (GenPart_pdgId[k] != j_id)
          {
            continue;
          }
          if (GenPart_genPartIdxMother[k] != j_id)
          {
            continue;
          }
          jgen = k; // take the last copy of W daughter
        }

        int n = 0;
        if (abs(j_id) == 11 || abs(j_id) == 13 || abs(j_id) == 15)
        {
          trueLeptonicT = 1;
        } // store e/mu/tau first
        else if (abs(j_id) == 12 || abs(j_id) == 14 || abs(j_id) == 16)
        {
          trueLeptonicT = 1;
          n = 6;
        } // then neutrinos
        else if (trueLeptonicT == -1)
        {
          trueLeptonicT = 0;
        } // quark 1
        else if (trueLeptonicT == 0)
        {
          n = 6;
        } // quark 2
        else
        {
          std::cout << "error" << std::endl;
        }

        t_gen_info[17 + n] = GenPart_pt[jgen];
        t_gen_info[18 + n] = GenPart_eta[jgen];
        t_gen_info[19 + n] = GenPart_phi[jgen];
        t_gen_info[20 + n] = GenPart_mass[jgen];
        t_gen_info[21 + n] = GenPart_pdgId[jgen];
        t_gen_info[22 + n] = GenPart_status[jgen];
      }
    }
  }
  t_gen_info[29] = trueLeptonicT;

  return t_gen_info;
};

  // ----------------------------------------------------
  //           W truth extraction:
  // ----------------------------------------------------
  auto W_gen_info = [sample](unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<float> &GenPart_mass, ROOT::VecOps::RVec<float> &GenPart_pt, ROOT::VecOps::RVec<float> &GenPart_phi, ROOT::VecOps::RVec<float> &GenPart_eta, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &GenPart_status, int daughterW_gen_pdgId)
  {
    ROOT::VecOps::RVec<float> W_gen_info(19, -999);
    if (sample != "Bprime")
    {
      return W_gen_info;
    }
    int trueLeptonicW = -1;

    for (unsigned int i = 0; i < nGenPart; i++)
    {
      int id = GenPart_pdgId[i];
      int motherIdx = GenPart_genPartIdxMother[i];

      if (abs(id) > 17 || GenPart_pdgId[motherIdx] != (-daughterW_gen_pdgId))
      {
        continue;
      } // look for daughters of W

      if (trueLeptonicW == -1)
      {
        W_gen_info[0] = GenPart_pt[motherIdx];
        W_gen_info[1] = GenPart_eta[motherIdx];
        W_gen_info[2] = GenPart_phi[motherIdx];
        W_gen_info[3] = GenPart_mass[motherIdx];
        W_gen_info[4] = GenPart_pdgId[motherIdx];
        W_gen_info[5] = GenPart_status[motherIdx];
      }

      int igen = i;
      for (unsigned int j = igen; j < nGenPart; j++)
      {
        if (GenPart_pdgId[j] != id)
        {
          continue;
        }
        if (GenPart_genPartIdxMother[j] != igen)
        {
          continue;
        }
        igen = j; // take the last copy of W daughter
      }

      int n = 0;
      if (abs(id) == 11 || abs(id) == 13 || abs(id) == 15)
      {
        trueLeptonicW = 1;
      } // store e/mu/tau first
      else if (abs(id) == 12 || abs(id) == 14 || abs(id) == 16)
      {
        trueLeptonicW = 1;
        n = 6;
      } // then neutrinos
      else if (trueLeptonicW == -1)
      {
        trueLeptonicW = 0;
      } // quark 1
      else if (trueLeptonicW == 0)
      {
        n = 6;
      } // quark 2
      else
      {
        std::cout << "error" << std::endl;
      }

      W_gen_info[6 + n] = GenPart_pt[i];
      W_gen_info[7 + n] = GenPart_eta[i];
      W_gen_info[8 + n] = GenPart_phi[i];
      W_gen_info[9 + n] = GenPart_mass[i];
      W_gen_info[10 + n] = GenPart_pdgId[i];
      W_gen_info[11 + n] = GenPart_status[i];
    }
    W_gen_info[18] = trueLeptonicW;

    return W_gen_info;
  };

  // ----------------------------------------------------
  //           W,t truth extraction for bkg:
  // ----------------------------------------------------

  auto t_bkg_idx = [sample](unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &GenPart_statusFlags)
  {
    if (sample == "Bprime")
    {
      ROOT::VecOps::RVec<int> t_daughter_idx;
      return t_daughter_idx;
    }

    ROOT::VecOps::RVec<int> t_idx;
    for (unsigned int i = 0; i < nGenPart; i++)
    {
      if (abs(GenPart_pdgId[i]) != 6)
      {
        continue;
      }
      std::bitset<15> statusFlags(GenPart_statusFlags[i]);

      if (statusFlags.to_string()[1] == '0')
      {
        continue;
      } // take last copy of t
      t_idx.push_back(i);
    }

    int Nt = t_idx.size();
    ROOT::VecOps::RVec<int> t_daughter_idx(Nt * 3, -99);

    for (unsigned int i = 0; i < Nt; i++)
    {
      for (unsigned int j = t_idx[i]; j < nGenPart; j++)
      {
        if (GenPart_genPartIdxMother[j] != t_idx[i])
        {
          continue;
        } // pick out daughters of t

        int id = GenPart_pdgId[j];
        if (abs(id) != 5 && abs(id) != 24)
        {
          continue;
        } // pick out daughter b, W

        if (abs(id) == 5)
        {
          t_daughter_idx[i * 3] = j;
        } // record the first copy of b
        else
        {
          int jgen = j;
          for (unsigned int k = j; k < nGenPart; k++)
          {
            if (GenPart_pdgId[k] != id)
            {
              continue;
            }
            if (GenPart_genPartIdxMother[k] != jgen)
            {
              continue;
            }
            jgen = k; // take the last copy of W
          }

          int n = 1;
          for (unsigned int k = j; k < nGenPart; k++)
          {
            if (GenPart_genPartIdxMother[k] != jgen)
            {
              continue;
            } // pick out daughters of W
            if (abs(GenPart_pdgId[k]) > 17)
            {
              continue;
            }                              // to exclude 24->22,24
            t_daughter_idx[i * 3 + n] = k; // record the first copy of W daughter
            n += 1;
          }
        }
      }
    }
    return t_daughter_idx;
  };

  auto W_bkg_idx = [sample](unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &GenPart_statusFlags, ROOT::VecOps::RVec<int> &t_bkg_idx)
  {
    if (sample == "Bprime")
    {
      ROOT::VecOps::RVec<int> W_daughter_idx;
      return W_daughter_idx;
    }
    //std::cout << "Event" << std::endl;
    ROOT::VecOps::RVec<int> W_idx;
    for (unsigned int i = 0; i < nGenPart; i++)
    {
      if (abs(GenPart_pdgId[i]) != 24)
      {
        continue;
      }

      std::bitset<15> statusFlags(GenPart_statusFlags[i]);
      if (statusFlags.to_string()[1] == '0')
      {
        continue;
      } // take last copy of W

      bool exclude = false;
      for (unsigned int j = 0; j < t_bkg_idx.size(); j += 3)
      {
        if (i == GenPart_genPartIdxMother[t_bkg_idx[j + 1]])
        {
          exclude = true;
          break;
        } // exclude W's from t
      }

      if (exclude)
      {
        continue;
      }
      W_idx.push_back(i);
    }

    int nW = W_idx.size();
    ROOT::VecOps::RVec<int> W_daughter_idx(nW * 2, -99);

    for (unsigned int i = 0; i < nW; i++)
    {
      int n = 0;
      for (unsigned int j = 0; j < nGenPart; j++)
      {
        if (GenPart_genPartIdxMother[j] != W_idx[i])
        {
          continue;
        } // pick out daughters of W
        if (abs(GenPart_pdgId[j]) > 17)
        {
          continue;
        } // to exclude 24->22,24

        W_daughter_idx[i * 2 + n] = j; // record the first copy of W daughter
        n += 1;
      }
    }

    return W_daughter_idx;
  };

  // The following functions could probably all go to the plotting marco
  auto leptonicCheck = [sample](int trueLeptonicT, int trueLeptonicW)
  {
    if (sample != "Bprime")
    {
      return -9;
    } // not sure if this line is needed. check.

    int trueLeptonicMode = -9;

    if ((trueLeptonicT != 1) && (trueLeptonicW == 1))
    {
      trueLeptonicMode = 0;
    } // leptonic W
    else if ((trueLeptonicT == 1) && (trueLeptonicW != 1))
    {
      trueLeptonicMode = 1;
    } // leptonic T
    else if ((trueLeptonicT == 1) && (trueLeptonicW == 1))
    {
      trueLeptonicMode = 2;
    } // dileptonic
    else if ((trueLeptonicT == 0) && (trueLeptonicW == 0))
    {
      trueLeptonicMode = -1;
    } // hadronic

    return trueLeptonicMode;
  };

  auto FatJet_matching_sig = [sample](ROOT::VecOps::RVec<float> &goodcleanFatJets, ROOT::VecOps::RVec<float> &gcFatJet_eta, ROOT::VecOps::RVec<float> &gcFatJet_phi, int NFatJets, ROOT::VecOps::RVec<int> &FatJet_subJetIdx1, unsigned int nSubJet, ROOT::VecOps::RVec<int> &SubJet_hadronFlavour, ROOT::VecOps::RVec<int> &GenPart_pdgId, double daughterb_gen_eta, double daughterb_gen_phi, double tDaughter1_gen_eta, double tDaughter1_gen_phi, int tDaughter1_gen_pdgId, double tDaughter2_gen_eta, double tDaughter2_gen_phi, int tDaughter2_gen_pdgId, double WDaughter1_gen_eta, double WDaughter1_gen_phi, int WDaughter1_gen_pdgId, double WDaughter2_gen_eta, double WDaughter2_gen_phi, int WDaughter2_gen_pdgId)
  {
    ROOT::VecOps::RVec<int> matched_GenPart(NFatJets, -9);
    if (sample != "Bprime")
    {
      return matched_GenPart;
    }

    ROOT::VecOps::RVec<int> gcFatJet_subJetIdx1 = FatJet_subJetIdx1[goodcleanFatJets];

    // std::cout << "Event: " << std::endl;
    for (unsigned int i = 0; i < NFatJets; i++)
    {
      // std::cout << "\n" << "Fatjet: " << std::endl;
      double fatjet_eta = gcFatJet_eta[i];
      double fatjet_phi = gcFatJet_phi[i];

      double dR_b = DeltaR(fatjet_eta, daughterb_gen_eta, fatjet_phi, daughterb_gen_phi);
      double dR_q1 = DeltaR(fatjet_eta, tDaughter1_gen_eta, fatjet_phi, tDaughter1_gen_phi);
      double dR_q2 = DeltaR(fatjet_eta, tDaughter2_gen_eta, fatjet_phi, tDaughter2_gen_phi);

      double dR_q3 = DeltaR(fatjet_eta, WDaughter1_gen_eta, fatjet_phi, WDaughter1_gen_phi);
      double dR_q4 = DeltaR(fatjet_eta, WDaughter2_gen_eta, fatjet_phi, WDaughter2_gen_phi);

      if (dR_b < 0.8 && dR_q1 < 0.8 && dR_q2 < 0.8)
      {
        if (abs(tDaughter1_gen_pdgId) < 6)
        {
          matched_GenPart[i] = 6;
        } // pos stands for hadronic t
        else
        {
          matched_GenPart[i] = -6;
        } // neg stands for leptonic t
      }
      else if (dR_q1 < 0.8 && dR_q2 < 0.8)
      {
        if (abs(tDaughter1_gen_pdgId) < 6)
        {
          matched_GenPart[i] = 24;
        }
        else
        {
          matched_GenPart[i] = -24;
        }
      }

      if (dR_q3 < 0.8 && dR_q4 < 0.8)
      {
        if (abs(WDaughter1_gen_pdgId) < 6)
        {
          matched_GenPart[i] = 24;
        }
        else
        {
          matched_GenPart[i] = -24;
        }
      }

      if (matched_GenPart[i] != -9)
      {
        continue;
      }

      int firstsub = FatJet_subJetIdx1[i];
      for (int isub = firstsub; isub < nSubJet; isub++)
      {
        if (SubJet_hadronFlavour[isub] != 0)
        {
          matched_GenPart[i] = SubJet_hadronFlavour[isub];
        }
        else
        {
          matched_GenPart[i] = 0;
        }
      }
    }
    return matched_GenPart;
  };

  auto FatJet_matching_bkg = [sample](ROOT::VecOps::RVec<float> &goodcleanFatJets, ROOT::VecOps::RVec<float> &gcFatJet_eta, ROOT::VecOps::RVec<float> &gcFatJet_phi, int NFatJets, ROOT::VecOps::RVec<int> &FatJet_subJetIdx1, unsigned int nSubJet, ROOT::VecOps::RVec<int> &SubJet_hadronFlavour, unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<float> &GenPart_phi, ROOT::VecOps::RVec<float> &GenPart_eta, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &t_bkg_idx, ROOT::VecOps::RVec<int> &W_bkg_idx)
  {
    ROOT::VecOps::RVec<int> matched_GenPart(NFatJets, -9);
    if (sample == "Bprime")
    {
      return matched_GenPart;
    }

    ROOT::VecOps::RVec<int> gcFatJet_subJetIdx1 = FatJet_subJetIdx1[goodcleanFatJets];

    int ntD = t_bkg_idx.size();
    int nWD = W_bkg_idx.size();

    ROOT::VecOps::RVec<double> t_eta(ntD, -9);
    ROOT::VecOps::RVec<double> t_phi(ntD, -9);
    ROOT::VecOps::RVec<double> W_eta(nWD, -9);
    ROOT::VecOps::RVec<double> W_phi(nWD, -9);

    if (ntD != 0)
    {
      for (unsigned int i = 0; i < ntD; i++)
      {
        int igen = t_bkg_idx[i];
        int id = GenPart_pdgId[igen];
        for (unsigned int j = igen; j < nGenPart; j++)
        {
          if (GenPart_pdgId[j] != id)
          {
            continue;
          }
          if (GenPart_genPartIdxMother[j] != igen)
          {
            continue;
          }
          igen = j; // take the last copy of t daughter
        }
        t_eta[i] = GenPart_eta[igen];
        t_phi[i] = GenPart_phi[igen];
      }
    }

    if (nWD != 0)
    {
      for (unsigned int i = 0; i < nWD; i++)
      {
        int igen = W_bkg_idx[i];
        int id = GenPart_pdgId[igen];
        for (unsigned int j = igen; j < nGenPart; j++)
        {
          if (GenPart_pdgId[j] != id)
          {
            continue;
          }
          if (GenPart_genPartIdxMother[j] != igen)
          {
            continue;
          }
          igen = j; // take the last copy of W daughter
        }
        W_eta[i] = GenPart_eta[igen];
        W_phi[i] = GenPart_phi[igen];
      }
    }

    for (unsigned int i = 0; i < NFatJets; i++)
    {
      double fatjet_eta = gcFatJet_eta[i];
      double fatjet_phi = gcFatJet_phi[i];

      for (unsigned int j = 0; j < t_bkg_idx.size() / 3; j++)
      {
        double dR_b = DeltaR(fatjet_eta, t_eta[j * 3], fatjet_phi, t_phi[j * 3]);
        double dR_q1 = DeltaR(fatjet_eta, t_eta[j * 3 + 1], fatjet_phi, t_phi[j * 3 + 1]);
        double dR_q2 = DeltaR(fatjet_eta, t_eta[j * 3 + 2], fatjet_phi, t_phi[j * 3 + 2]);

        if (dR_b < 0.8 && dR_q1 < 0.8 && dR_q2 < 0.8)
        {
          if (abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) < 6)
          {
            matched_GenPart[i] = 6;
            break;
          } // pos stands for hadronic t
          else
          {
            matched_GenPart[i] = -6;
            break;
          } // neg stands for leptonic t
        }
        else if (dR_q1 < 0.8 && dR_q2 < 0.8)
        {
          if (abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) < 6)
          {
            matched_GenPart[i] = 24;
            break;
          }
          else
          {
            matched_GenPart[i] = -24;
            break;
          }
        }
      }

      if (matched_GenPart[i] != -9)
      {
        continue;
      }
      for (unsigned int j = 0; j < W_bkg_idx.size() / 2; j++)
      {
        double dR_q1 = DeltaR(fatjet_eta, W_eta[j * 2], fatjet_phi, W_phi[j * 2]);
        double dR_q2 = DeltaR(fatjet_eta, W_eta[j * 2 + 1], fatjet_phi, W_phi[j * 2 + 1]);

        if (dR_q1 < 0.8 && dR_q2 < 0.8)
        {
          if (abs(GenPart_pdgId[j * 2]) < 6)
          {
            matched_GenPart[i] = 24;
            break;
          }
          else
          {
            matched_GenPart[i] = -24;
            break;
          }
        }
      }

      if (matched_GenPart[i] != -9)
      {
        continue;
      }
      int firstsub = FatJet_subJetIdx1[i];
      for (int isub = firstsub; isub < nSubJet; isub++)
      {
        if (SubJet_hadronFlavour[isub] != 0)
        {
          matched_GenPart[i] = SubJet_hadronFlavour[isub];
        }
        else
        {
          matched_GenPart[i] = 0;
        }
      }
    }
    return matched_GenPart;
  };

  // ----------------------------------------------------
  //   		ttbar background mass CALCULATOR:
  // ----------------------------------------------------

  auto genttbarMassCalc = [sample](unsigned int nGenPart, ROOT::VecOps::RVec<int> &GenPart_pdgId, ROOT::VecOps::RVec<float> &GenPart_mass, ROOT::VecOps::RVec<float> &GenPart_pt, ROOT::VecOps::RVec<float> &GenPart_phi, ROOT::VecOps::RVec<float> &GenPart_eta, ROOT::VecOps::RVec<int> &GenPart_genPartIdxMother, ROOT::VecOps::RVec<int> &GenPart_status)
  {
    int returnVar = 0;
    if (sample == "ttbar")
    {
      int genTTbarMass = -999;
      double topPtWeight = 1.0;
      TLorentzVector top, antitop;
      bool gottop = false;
      bool gotantitop = false;
      bool gottoppt = false;
      bool gotantitoppt = false;
      float toppt, antitoppt;
      for (unsigned int p = 0; p < nGenPart; p++)
      {
        int id = GenPart_pdgId[p];
        if (abs(id) != 6)
        {
          continue;
        }
        if (GenPart_mass[p] < 10)
        {
          continue;
        }
        int motherid = GenPart_pdgId[GenPart_genPartIdxMother[p]];
        if (abs(motherid) != 6)
        {
          if (!gottop && id == 6)
          {
            top.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], GenPart_mass[p]);
            gottop = true;
          }
          if (!gotantitop && id == -6)
          {
            antitop.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], GenPart_mass[p]);
            gotantitop = true;
          }
        }
        if (GenPart_status[p] == 62)
        {
          if (!gottoppt && id == 6)
          {
            toppt = GenPart_pt[p];
            gottoppt = true;
          }
          if (!gotantitoppt && id == -6)
          {
            antitoppt = GenPart_pt[p];
            gotantitoppt = true;
          }
        }
      }
      if (gottop && gotantitop)
      {
        genTTbarMass = (top + antitop).M();
      }
      if (gottoppt && gotantitoppt)
      {
        float SFtop = TMath::Exp(0.0615 - 0.0005 * toppt);
        float SFantitop = TMath::Exp(0.0615 - 0.0005 * antitoppt);
        topPtWeight = TMath::Sqrt(SFtop * SFantitop);
      }
      returnVar = genTTbarMass;
    }
    return returnVar;
  };

  // ----------------------------------------------------
  //     minM_lep_jet VECTOR RETURN + NJETSDEEPFLAV
  // ----------------------------------------------------

  auto minM_lep_jet_calc = [isNominal](ROOT::VecOps::RVec<float> &jet_pt, ROOT::VecOps::RVec<float> &jet_eta, ROOT::VecOps::RVec<float> &jet_phi, ROOT::VecOps::RVec<float> &jet_mass, TLorentzVector lepton_lv)
  {
    float ind_MinMlj = -1; // This gets changed into int in .Define()
    float minMleppJet = 1e8;
    TLorentzVector jet_lv;

    for (unsigned int ijet = 0; ijet < jet_pt.size(); ijet++)
    {
      jet_lv.SetPtEtaPhiM(jet_pt.at(ijet), jet_eta.at(ijet), jet_phi.at(ijet), jet_mass.at(ijet));
      if ((lepton_lv + jet_lv).M() < minMleppJet)
      {
        minMleppJet = fabs((lepton_lv + jet_lv).M());
        ind_MinMlj = ijet;
      }
    }
    ROOT::VecOps::RVec<float> minMlj = {minMleppJet, ind_MinMlj};
    return minMlj;
  };

  // -------------------------------------------------------
  //               Flags and First Filter
  // -------------------------------------------------------
  // Twiki with reccommended ultralegacy values
  auto rdf_input = ROOT::RDataFrame("Events", files); // Initial data
  //  std::cout << "Number of Events: " << rdf.Count().GetValue() << std::endl;
  //Bprime_gen_info, {"nGenPart", "GenPart_pdgId", "GenPart_mass", "GenPart_pt", "GenPart_phi", "GenPart_eta", "GenPart_genPartIdxMother", "GenPart_status", "GenPart_statusFlags"}
  //"Bprime_gen_info(sample, nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status, GenPart_statusFlags)"

  //t_gen_info, {"nGenPart", "GenPart_pdgId", "GenPart_mass", "GenPart_pt", "GenPart_phi", "GenPart_eta", "GenPart_genPartIdxMother", "GenPart_status"}
  //"t_gen_info(nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status)"
  auto rdf = rdf_input.Define("Bprime_gen_info", Bprime_gen_info, {"nGenPart", "GenPart_pdgId", "GenPart_mass", "GenPart_pt", "GenPart_phi", "GenPart_eta", "GenPart_genPartIdxMother", "GenPart_status", "GenPart_statusFlags"})
                 .Define("Bprime_gen_pt", "Bprime_gen_info[0]")
                 .Define("Bprime_gen_eta", "(double) Bprime_gen_info[1]")
                 .Define("Bprime_gen_phi", "(double) Bprime_gen_info[2]")
                 .Define("Bprime_gen_mass", "Bprime_gen_info[3]")
                 .Define("Bprime_gen_pdgId", "(int) Bprime_gen_info[4]")
                 .Define("Bprime_gen_status", "(int) Bprime_gen_info[5]")
                 .Define("t_gen_info", t_gen_info, {"nGenPart", "GenPart_pdgId", "GenPart_mass", "GenPart_pt", "GenPart_phi", "GenPart_eta", "GenPart_genPartIdxMother", "GenPart_status"})
                 .Define("t_gen_pt", "t_gen_info[0]")
                 .Define("t_gen_eta", "(double) t_gen_info[1]")
                 .Define("t_gen_phi", "(double) t_gen_info[2]")
                 .Define("t_gen_mass", "t_gen_info[3]")
                 .Define("t_gen_pdgId", "(int) t_gen_info[4]")
                 .Define("t_gen_status", "(int) t_gen_info[5]")
                 .Define("daughterb_gen_pt", "t_gen_info[6]")
                 .Define("daughterb_gen_eta", "(double) t_gen_info[7]")
                 .Define("daughterb_gen_phi", "(double) t_gen_info[8]")
                 .Define("daughterb_gen_pdgId", "(int) t_gen_info[9]")
                 .Define("daughterb_gen_status", "(int) t_gen_info[10]")
                 .Define("daughterW_gen_pt", "t_gen_info[11]")
                 .Define("daughterW_gen_eta", "(double) t_gen_info[12]")
                 .Define("daughterW_gen_phi", "(double) t_gen_info[13]")
                 .Define("daughterW_gen_mass", "t_gen_info[14]")
                 .Define("daughterW_gen_pdgId", "(int) t_gen_info[15]")
                 .Define("daughterW_gen_status", "(int) t_gen_info[16]")
                 .Define("tDaughter1_gen_pt", "t_gen_info[17]") // e/mu/tau or quark1
                 .Define("tDaughter1_gen_eta", "(double) t_gen_info[18]")
                 .Define("tDaughter1_gen_phi", "(double) t_gen_info[19]")
                 .Define("tDaughter1_gen_mass", "t_gen_info[20]")
                 .Define("tDaughter1_gen_pdgId", "(int) t_gen_info[21]")
                 .Define("tDaughter1_gen_status", "(int) t_gen_info[22]")
                 .Define("tDaughter2_gen_pt", "t_gen_info[23]") // neutrino or quark2
                 .Define("tDaughter2_gen_eta", "(double) t_gen_info[24]")
                 .Define("tDaughter2_gen_phi", "(double) t_gen_info[25]")
                 .Define("tDaughter2_gen_mass", "t_gen_info[26]")
                 .Define("tDaughter2_gen_pdgId", "(int) t_gen_info[27]")
                 .Define("tDaughter2_gen_status", "(int) t_gen_info[28]")
                 .Define("trueLeptonicT", "(int) t_gen_info[29]")
                 .Define("W_gen_info", W_gen_info, {"nGenPart", "GenPart_pdgId", "GenPart_mass", "GenPart_pt", "GenPart_phi", "GenPart_eta", "GenPart_genPartIdxMother", "GenPart_status", "daughterW_gen_pdgId"})
                 .Define("W_gen_pt", "W_gen_info[0]")
                 .Define("W_gen_eta", "(double) W_gen_info[1]")
                 .Define("W_gen_phi", "(double) W_gen_info[2]")
                 .Define("W_gen_mass", "W_gen_info[3]")
                 .Define("W_gen_pdgId", "(int) W_gen_info[4]")
                 .Define("W_gen_status", "(int) W_gen_info[5]")
                 .Define("WDaughter1_gen_pt", "W_gen_info[6]")
                 .Define("WDaughter1_gen_eta", "(double) W_gen_info[7]")
                 .Define("WDaughter1_gen_phi", "(double) W_gen_info[8]")
                 .Define("WDaughter1_gen_mass", "W_gen_info[9]")
                 .Define("WDaughter1_gen_pdgId", "(int) W_gen_info[10]")
                 .Define("WDaughter1_gen_status", "(int) W_gen_info[11]")
                 .Define("WDaughter2_gen_pt", "W_gen_info[12]")
                 .Define("WDaughter2_gen_eta", "(double) W_gen_info[13]")
                 .Define("WDaughter2_gen_phi", "(double) W_gen_info[14]")
                 .Define("WDaughter2_gen_mass", "W_gen_info[15]")
                 .Define("WDaughter2_gen_pdgId", "(int) W_gen_info[16]")
                 .Define("WDaughter2_gen_status", "(int) W_gen_info[17]")
                 .Define("trueLeptonicW", "(int) W_gen_info[18]")
                 .Define("trueLeptonicMode", leptonicCheck, {"trueLeptonicT", "trueLeptonicW"})
                 .Define("t_bkg_idx", t_bkg_idx, {"nGenPart", "GenPart_pdgId", "GenPart_genPartIdxMother", "GenPart_statusFlags"})
                 .Define("W_bkg_idx", W_bkg_idx, {"nGenPart", "GenPart_pdgId", "GenPart_genPartIdxMother", "GenPart_statusFlags", "t_bkg_idx"});
  //  std::cout << "Number of Events passing Preselection (HT Cut): " << HT_calc.Count().GetValue() << std::endl;

  // ---------------------------------------------------------
  //               Save rdf before any cuts
  // ---------------------------------------------------------

  TString outputFileNC = "RDF_" + sample + "_nocuts_" + testNum + ".root";
  const char *stdOutputFileNC = outputFileNC;
  std::cout << "------------------------------------------------" << std::endl
            << ">>> Saving original Snapshot..." << std::endl;
  rdf.Snapshot("Events", stdOutputFileNC);
  std::cout << "Output File: " << outputFileNC << std::endl
            << "-------------------------------------------------" << std::endl;

  auto METfilters = rdf.Filter("Flag_EcalDeadCellTriggerPrimitiveFilter == 1 && Flag_goodVertices == 1 && Flag_HBHENoiseFilter == 1 && Flag_HBHENoiseIsoFilter == 1 && Flag_eeBadScFilter == 1 && Flag_globalSuperTightHalo2016Filter == 1 && Flag_BadPFMuonFilter == 1 && Flag_ecalBadCalibFilter == 1", "MET Filters")
                        .Filter("MET_pt > 50", "Pass MET > 50")
                        .Filter("nJet > 0 && nFatJet > 0", "Event has jets");

  // ---------------------------------------------------------
  //                    Lepton Filters
  // ---------------------------------------------------------

  auto LepDefs = METfilters.Define("TPassMu", "Muon_tightId==true && Muon_pt>50 && abs(Muon_eta)<2.4")
                     .Define("nTPassMu", "(int) Sum(TPassMu)")
                     .Define("TPassEl", "Electron_mvaFall17V2noIso_WP90 == true && Electron_pt>80 && abs(Electron_eta)<2.5")
                     .Define("nTPassEl", "(int) Sum(TPassEl)")
                     .Define("LPassMu", "Muon_tightId==true && Muon_pt>25 && abs(Muon_eta)<2.4")
                     .Define("LPassEl", "Electron_mvaFall17V2noIso_WP90 == true && Electron_pt>25 && abs(Electron_eta)<2.5")
                     .Define("Muon_ptPass", "Muon_pt[LPassMu == true]")
                     .Define("Muon_etaPass", "Muon_eta[LPassMu == true]")
                     .Define("Muon_phiPass", "Muon_phi[LPassMu == true]")
                     .Define("Muon_massPass", "Muon_mass[LPassMu == true]")
                     .Define("Electron_ptPass", "Electron_pt[LPassEl == true]")
                     .Define("Electron_etaPass", "Electron_eta[LPassEl == true]")
                     .Define("Electron_phiPass", "Electron_phi[LPassEl == true]")
                     .Define("Electron_massPass", "Electron_mass[LPassEl == true]")
                     .Define("TLMuon_P4", "fVectorConstructor(Muon_ptPass,Muon_etaPass,Muon_phiPass,Muon_massPass)")
                     .Define("TLElectron_P4", "fVectorConstructor(Electron_ptPass,Electron_etaPass,Electron_phiPass,Electron_massPass)")
                     .Define("LMuon_JetIdx", "Muon_jetIdx[LPassMu == true]")
                     .Define("LMuon_MiniIso", "Muon_miniIsoId[LPassMu]")
                     .Define("LElectron_JetIdx", "Electron_jetIdx[LPassEl]")
                     .Define("LElectron_MiniIso", "Electron_miniPFRelIso_all[LPassEl]");
                     
  auto CleanJets = LepDefs.Define("Jet_P4", "fVectorConstructor(Jet_pt,Jet_eta,Jet_phi,Jet_mass)")
                       .Define("cleanJets", "cleanJets(Jet_P4,Jet_rawFactor,TLMuon_P4,LMuon_JetIdx,TLElectron_P4,LElectron_JetIdx)")
                       .Define("cleanJet_pt", "cleanJets[0]")
                       .Define("cleanJet_eta", "cleanJets[1]")
                       .Define("cleanJvector<TLorentzVectoret_phi", "cleanJets[2]")
                       .Define("cleanJet_mass", "cleanJets[3]")
                       .Define("cleanJet_rawFactor", "cleanJets[4]")
                       .Define("goodcleanJets", "cleanJet_pt > 30 && abs(cleanJet_eta) < 2.4 && Jet_jetId > 1")
                       .Define("NJets_central", "(int) Sum(goodcleanJets)")
                       .Define("gcJet_pt", "cleanJet_pt[goodcleanJets == true]")
                       .Define("gcJet_eta", "cleanJet_eta[goodcleanJets == true]")
                       .Define("gcJet_phi", "cleanJet_phi[goodcleanJets == true]")
                       .Define("gcJet_mass", "cleanJet_mass[goodcleanJets == true]")
                       .Define("gcJet_DeepFlav", "Jet_btagDeepFlavB[goodcleanJets == true]")
                       .Define("gcJet_DeepFlavM", "gcJet_DeepFlav > 0.2783")
                       .Define("NJets_DeepFlavM", "(int) Sum(gcJet_DeepFlavM)")
                       .Define("goodcleanForwardJets", "cleanJet_pt > 30 && abs(cleanJet_eta) >= 2.4 && Jet_jetId > 1")
                       .Define("NJets_forward", "(int) Sum(goodcleanForwardJets)")
                       .Define("gcforwJet_pt", "cleanJet_pt[goodcleanForwardJets == true]")
                       .Define("gcforwJet_eta", "cleanJet_eta[goodcleanForwardJets == true]")
                       .Define("gcforwJet_phi", "cleanJet_phi[goodcleanForwardJets == true]")
                       .Define("gcforwJet_mass", "cleanJet_mass[goodcleanForwardJets == true]")
                       .Define("gcforwJet_DeepFlav", "Jet_btagDeepFlavB[goodcleanForwardJets == true]")
                       .Define("dR_LIM_AK4", "(float) 0.4")
                       .Define("ptrel25", "25")
                       .Define("Muon_2Dcut_ptrel25", "cut_ptrel(dR_LIM_AK4, ptrel25, TLMuon_P4, NJets_central, gcJet_eta, gcJet_phi, gcJet_pt, gcJet_mass)")
                       .Define("Electron_2Dcut_ptrel25", "cut_ptrel(dR_LIM_AK4, ptrel25, TLElectron_P4, NJets_central, gcJet_eta, gcJet_phi, gcJet_pt, gcJet_mass)")
                       .Define("ptrel40", "40")
                       .Define("Muon_2Dcut_ptrel40", "cut_ptrel(dR_LIM_AK4, ptrel40, TLMuon_P4, NJets_central, gcJet_eta, gcJet_phi, gcJet_pt, gcJet_mass)")
                       .Define("Electron_2Dcut_ptrel40", "cut_ptrel(dR_LIM_AK4, ptrel40, TLElectron_P4, NJets_central, gcJet_eta, gcJet_phi, gcJet_pt, gcJet_mass)");
  
  // Want a list of pass/fail 0/1s for muons with the cut "minDR(jet,muon) > dR_LIM_AK4 || ptRel(minDRjet,muon) > X"
  // to-do list:
  // test the muon lorentzVector against all the goodcleanJet lorentzVectors and calc DR, find the jet that is the minimum DR
  // using that jet, calc ptRel = (jet.Vect().Cross(muon.Vect())).Mag()/jet.P();
  // then we can eval if minDR > 0.4 || ptRel > 25 or 40
  // repeat for electrons
  // ideally, function takes in a list of lepton lorentzVectors, list of jet lorentzVectors
  // best reference is ROOT::VecOps page and ROOT::TLorentzVector page

  // auto LepSelect = CleanJets.Define("isMu","(nMuon > 0 && nTPassMu == 1 && HLT_Mu50_v == 1 && (nElectron == 0 || (nElectron > 0 && nTPassEl == 0)))") \
  //   .Define("isEl","(nElectron > 0 && nTPassEl == 1 && (HLT_Ele115_CaloIdVT_GsfTrkIdT_v == 1 || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v == 1) && (nMuon == 0 || (nMuon > 0 && nTPassMu == 0)))") \
  //   .Filter("isMu || isEl","Event is either muon or electron");

  // auto Lep_df1 = Lep_df0.Define("assignleps","assign_leps(isMu,isEl,TPassMu,TPassEl,Muon_pt,Muon_eta,Muon_phi,Muon_mass,Muon_miniPFRelIso_all,Electron_pt,Electron_eta,Electron_phi,Electron_mass,Electron_miniPFRelIso_all)") \
  //   .Define("lepton_pt","assignleps[0]")				\
  //   .Define("lepton_eta","assignleps[1]")				\
  //   .Define("lepton_phi","assignleps[2]")				\
  //   .Define("lepton_mass","assignleps[3]")				\
  //   .Define("lepton_miniIso","assignleps[4]");

  // --------------------------------------------------------
  // 		      JET SELECTION w/ cleaning
  // --------------------------------------------------------

  // auto jet_ft0 = Lep_df1.Filter("nJet > 0 && nFatJet > 0","Event has jets");
  // //  std::cout << "Number of Events with at least one AK4 and AK8 Jet: " << jet_ft0.Count().GetValue() << std::endl;

  // auto jet_df0 = jet_ft0.Define("goodJets","Jet_pt > 30 && abs(Jet_eta) < 2.4 && Jet_jetId > 1") \
  //   .Define("goodcleanFatJets","cleanJets(FatJet_pt,FatJet_mass,goodFatJets,FatJet_eta,FatJet_phi,\
  // 			      				            lepton_pt,lepton_mass,lepton_eta,lepton_phi,dR_LIM_AK8)")\
  //   .Define("dR_LIM_AK8","(float) 0.8")					\
  //   .Define("goodFatJets","FatJet_jetId > 1 && abs(FatJet_eta) < 2.4 && FatJet_pt > 200") \
  //   .Define("NFatJets","(int) Sum(goodcleanFatJets)")			\
  //   .Define("gcFatJet_pt","FatJet_pt[goodcleanFatJets == true]")	\
  //   .Define("gcFatJet_eta","FatJet_eta[goodcleanFatJets == true]")	\
  //   .Define("gcFatJet_phi","FatJet_phi[goodcleanFatJets == true]")	\
  //   .Define("gcFatJet_mass","FatJet_mass[goodcleanFatJets == true]")	\
  //   .Define("gcFatJet_msoftdrop","FatJet_msoftdrop[goodcleanFatJets == true]");

  // // ---------------------------------------------------------
  // // 	  HT Calculation and Final Preselection Cut
  // // ---------------------------------------------------------
  // auto HT_calc = jet_df0.Define("Jet_HT","Sum(Jet_pt[goodcleanJets == true])") \
  //   .Filter("Jet_HT > 250","Pass HT > 250")						\
  //   .Filter("NFatJets > 0","Pass N good central AK8 > 0");

  // // ---------------------------------------------------------
  // //    Uncomment to save seperate Preselection .root file
  // // ---------------------------------------------------------
  // //TString outputFilePS = "RDF_"+sample+"_presel_"+testNum+".root";
  // //const char* stdOutputFilePS = outputFilePS;
  // //std::cout << "------------------------------------------------" << std::endl << ">>> Saving Preselection Snapshot..." << std::endl;
  // //HT_calc.Snapshot("Events", stdOutputFilePS);
  // //std::cout << "Output File: " << outputFilePS << std::endl << "-------------------------------------------------" << std::endl;
  // // }
  // //----------------------------------------------------------
  // //       Uncomment from here to the bottom if starting from a preselection file!!
  // //----------------------------------------------------------
  // //	auto HT_calc = rdf;

  // // ---------------------------------------------------------
  // // 		Post Preselection Analysis
  // // ---------------------------------------------------------

  // auto postPresel = HT_calc.Define("genttbarMass",genttbarMassCalc,{"nGenPart","GenPart_pdgId","GenPart_mass", \
  // 	"GenPart_pt","GenPart_phi","GenPart_eta",			\
  // 	"GenPart_genPartIdxMother","GenPart_status"})			\
  //   .Define("lepton_lv","lvConstructor(lepton_pt,lepton_eta,lepton_phi,lepton_mass)") \
  //   .Define("Jets_lv","fVectorConstructor(gcJet_pt,gcJet_eta,gcJet_phi,gcJet_mass)") \
  //   .Define("FatJet_lv","fVectorConstructor(gcFatJet_pt,gcFatJet_eta,gcFatJet_phi,gcFatJet_mass)") \
  //   .Define("Jet_ST","Jet_HT + lepton_pt + MET_pt")			\
  //   .Define("FatJet_pt_1","FatJet_pt[0]")				\
  //   .Define("FatJet_pt_2","FatJet_pt[1]")				\
  //   .Define("FatJet_sdMass","FatJet_msoftdrop[goodcleanFatJets == true]") \
  //   .Define("FatJet_sdMass_1","FatJet_sdMass[0]")			\
  //   .Define("FatJet_sdMass_2","FatJet_sdMass[1]")			\
  //   .Define("dpak8_J","FatJet_deepTag_QCDothers[goodcleanFatJets == true]") \
  //   .Define("dpak8_J_1","dpak8_J[0]")					\
  //   .Define("dpak8_J_2","dpak8_J[1]")					\
  //   .Define("raw_dpak8_T","(FatJet_deepTag_TvsQCD * FatJet_deepTag_QCD) / (1 - FatJet_deepTag_TvsQCD)") \
  //   .Define("dpak8_T","raw_dpak8_T[goodcleanFatJets == true]")		\
  //   .Define("dpak8_T_1","dpak8_T[0]")					\
  //   .Define("dpak8_T_2","dpak8_T[1]")					\
  //   .Define("raw_dpak8_W","(FatJet_deepTag_WvsQCD * FatJet_deepTag_QCD) / (1 - FatJet_deepTag_WvsQCD)") \
  //   .Define("dpak8_W","raw_dpak8_W[goodcleanFatJets == true]")		\
  //   .Define("dpak8_W_1","dpak8_W[0]")					\
  //   .Define("dpak8_W_2","dpak8_W[1]")					\
  //   .Define("dpak8_tag","maxFxn(dpak8_J,dpak8_T,dpak8_W)")		\
  //   .Define("dpak8_tag_1","dpak8_tag[0]")				\
  //   .Define("dpak8_tag_2","dpak8_tag[1]")				\
  //   .Define("nJ_dpak8","Sum(dpak8_tag == 0)")				\
  //   .Define("nT_dpak8","Sum(dpak8_tag == 1)")				\
  //   .Define("nW_dpak8","Sum(dpak8_tag == 2)")				\
  //   .Define("pNet_J","FatJet_particleNet_QCD[goodcleanFatJets == true]") \
  //   .Define("pNet_J_1","pNet_J[0]")					\
  //   .Define("pNet_J_2","pNet_J[1]")					\
  //   .Define("raw_pNet_T","(FatJet_particleNet_TvsQCD * FatJet_particleNet_QCD) / (1 - FatJet_particleNet_TvsQCD)") \
  //   .Define("pNet_T","raw_pNet_T[goodcleanFatJets == true]")		\
  //   .Define("pNet_T_alt","FatJet_particleNet_TvsQCD[goodcleanFatJets == true]")            \
  //   .Define("pNet_T_1","pNet_T[0]")					\
  //   .Define("pNet_T_2","pNet_T[1]")					\
  //   .Define("raw_pNet_W","(FatJet_particleNet_WvsQCD * FatJet_particleNet_QCD) / (1 - FatJet_particleNet_WvsQCD)") \
  //   .Define("pNet_W","raw_pNet_W[goodcleanFatJets == true]")		\
  //   .Define("pNet_W_alt","FatJet_particleNet_WvsQCD[goodcleanFatJets == true]")
  //   .Define("pNet_W_1","pNet_W[0]")					\
  //   .Define("pNet_W_2","pNet_W[1]")					\
  //   .Define("pNet_tag","maxFxn(pNet_J,pNet_T,pNet_W)")			\
  //   .Define("pNet_tag_alt","JetDiscriminator(pNet_T_alt, pNet_W_alt)")  \
  //   .Define("pNet_tag_1","pNet_tag[0]")					\
  //   .Define("pNet_tag_2","pNet_tag[1]")					\
  //   .Define("nJ_pNet","Sum(pNet_tag == 0)")				\
  //   .Define("nT_pNet","Sum(pNet_tag == 1)")				\
  //   .Define("nW_pNet","Sum(pNet_tag == 2)")				\
  //   .Define("raw_tau21","(FatJet_tau2 / FatJet_tau1)")			\
  //   .Define("tau21","raw_tau21[goodcleanFatJets == true]")		\
  //   .Define("tau21_1","tau21[0]")					\
  //   .Define("tau21_2","tau21[1]")					\
  //   .Define("minDR_ptRel_lead_lepAK8","minDR_ptRel_lead_calc(gcFatJet_pt,gcFatJet_eta,gcFatJet_phi, \
  // 									   gcFatJet_mass,lepton_lv)")\
  //   .Define("minDR_lep_FatJet","minDR_ptRel_lead_lepAK8[0]")		\
  //   .Define("ptRel_lep_FatJet","minDR_ptRel_lead_lepAK8[1]")		\
  //   .Define("minDR_leadAK8otherAK8","minDR_ptRel_lead_lepAK8[2]")	\
  //   .Define("minDR_ptRel_lead_lepAK4","minDR_ptRel_lead_calc(gcJet_pt,gcJet_eta,gcJet_phi, \
  // 					      				   gcJet_mass,lepton_lv)")\
  //   .Define("minDR_lep_Jet","minDR_ptRel_lead_lepAK4[0]")		\
  //   .Define("ptRel_lep_Jet","minDR_ptRel_lead_lepAK4[1]")		\
  //   .Define("DR_lep_FatJets","DR_calc(gcFatJet_pt,gcFatJet_eta,gcFatJet_phi,gcFatJet_mass, \
  // 					      	    lepton_pt,lepton_eta, lepton_phi,lepton_mass)")\
  //   .Define("DR_lep_Jets","DR_calc(gcJet_pt,gcJet_eta,gcJet_phi,gcJet_mass, \
  // 					   	 lepton_pt,lepton_eta,lepton_phi,lepton_mass)")\
  //   .Define("W_lv","W_reco(MET_pt,MET_phi,lepton_lv)")			\
  //   .Define("W_pt", "W_lv.Pt()")
  //   .Define("W_eta", "W_lv.Eta()")
  //   .Define("W_phi", "W_lv.Phi()")
  //   .Define("W_mass", "W_lv.M()")
  //   .Define("W_MT", "sqrt(2*lepton_pt*MET_pt*(1-cos(lepton_phi - MET_phi)))")
  //   .Define("minMlj_output",minM_lep_jet_calc,{"gcJet_pt","gcJet_eta", "gcJet_phi","gcJet_mass", \
  // 	  "lepton_lv"})							\
  //   .Define("DR_W_lep","dR_Wt_Calc(W_lv,lepton_lv)")			\
  //   .Define("minM_lep_Jet","minMlj_output[0]")				\
  //   .Define("minM_lep_Jet_jetID","(int) minMlj_output[1]")		\
  //   .Define("leptonicParticle","isLeptonic_X(minM_lep_Jet)")		\
  //   .Define("t_output","t_reco(leptonicParticle,gcJet_pt,gcJet_eta,gcJet_phi,gcJet_mass, \
  // 					 W_lv,minM_lep_Jet,minM_lep_Jet_jetID)")\
  //   .Define("t_pt","t_output[0]")					\
  //   .Define("t_eta","t_output[1]")					\
  //   .Define("t_phi","t_output[2]")					\
  //   .Define("t_mass","t_output[3]")					\
  //   .Define("DR_W_b","t_output[4]")					\
  //   .Define("t_lv","lvConstructor(t_pt,t_eta,t_phi,t_mass)")
  //   .Define("Bprime_output","BPrime_reco(t_lv,W_lv,leptonicParticle,\
  // 	  				       gcFatJet_pt,gcFatJet_eta,gcFatJet_phi,gcFatJet_mass,pNet_tag,gcFatJet_msoftdrop)")\
  //   .Define("Bprime_output_alt","BPrime_reco_alt(lepton_lv, t_lv,W_lv,leptonicParticle, gcFatJet_pt,gcFatJet_eta,gcFatJet_phi,gcFatJet_mass,pNet_tag,gcFatJet_msoftdrop)")
  //   .Define("Bprime_mass","Bprime_output[0]")				\
  //   .Define("Bprime_pt","Bprime_output[1]")				\
  //   .Define("Bprime_eta","Bprime_output[2]")				\
  //   .Define("Bprime_phi","Bprime_output[3]")				\
  //   .Define("Bprime_DR","Bprime_output[4]")				\
  //   .Define("Bprime_ptbal","Bprime_output[5]")				\
  //   .Define("Bprime_chi2","Bprime_output[6]")				\
  //   .Define("BPrime_lv","lvConstructor(Bprime_pt,Bprime_eta,Bprime_phi,Bprime_mass)") \
  //   .Define("isValidBDecay","Bprime_output[7]")				\
  //   .Define("taggedWbjetJet","Bprime_output[8]")			\
  //   .Define("taggedTjet","Bprime_output[9]")				\
  //   .Define("taggedWjet","Bprime_output[10]")				\
  //   .Define("dnn_scores",predictMLP,{"pNet_J_1","pNet_T_1","dpak8_T_1","FatJet_pt_1","FatJet_sdMass_1","tau21_1","nT_dpak8","nT_pNet","Jet_HT","Jet_ST","MET_pt","NJets_DeepFlavM","NJets_forward"}) \
  //   .Define("mlp_HT250_WJets","dnn_scores[0]")				\
  //   .Define("mlp_HT250_TTbar","dnn_scores[1]")				\
  //   .Define("mlp_HT250_Bprime","dnn_scores[2]")				\
  //   .Define("mlp_HT500_WJets","dnn_scores[3]")				\
  //   .Define("mlp_HT500_TTbar","dnn_scores[4]")				\
  //   .Define("mlp_HT500_Bprime","dnn_scores[5]")
  //   .Define("genFatJet_matching_sig", FatJet_matching_sig, {"goodcleanFatJets", "gcFatJet_eta", "gcFatJet_phi", "NFatJets", "FatJet_subJetIdx1", "nSubJet", "SubJet_hadronFlavour", "GenPart_pdgId", "daughterb_gen_eta", "daughterb_gen_phi", "tDaughter1_gen_eta", "tDaughter1_gen_phi", "tDaughter1_gen_pdgId", "tDaughter2_gen_eta", "tDaughter2_gen_phi", "tDaughter2_gen_pdgId", "WDaughter1_gen_eta", "WDaughter1_gen_phi", "WDaughter1_gen_pdgId", "WDaughter2_gen_eta", "WDaughter2_gen_phi", "WDaughter2_gen_pdgId"})
  //   .Define("genFatJet_matching_bkg", FatJet_matching_bkg, {"goodcleanFatJets", "gcFatJet_eta", "gcFatJet_phi", "NFatJets", "FatJet_subJetIdx1", "nSubJet", "SubJet_hadronFlavour", "nGenPart", "GenPart_pdgId", "GenPart_phi", "GenPart_eta", "GenPart_genPartIdxMother", "t_bkg_idx", "W_bkg_idx"});

  // // -------------------------------------------------
  // // 		Save Snapshot to file
  // // -------------------------------------------------

  std::cout << "-------------------------------------------------" << std::endl
            << ">>> Saving " << sample << " Snapshot..." << std::endl;
  TString finalFile = "RDF_" + sample + "_finalsel_" + testNum + ".root";
  const char *stdfinalFile = finalFile;
  CleanJets.Snapshot("Events", stdfinalFile); 
  std::cout << "Output File: " << finalFile << std::endl
            << "-------------------------------------------------" << std::endl;

  time.Stop();
  time.Print();
  std::cout << "Cut statistics:" << std::endl;
  CleanJets.Report()->Print();
}