import os 

# Question: A lot of the samples have _PSweights_.  The samples we were working with before didn't have this.  Is it good or bad?
# Sample Dictionaries: samples, samples_2022, samples_2022EE, samples_2023, samples_2023BPix, samples_test, samples_QCD

class sample:
    def __init__(self, prefix, year, textlist, samplename): #, color
        self.prefix = prefix
        self.year = year
        self.textlist = textlist
        self.samplename = samplename
        #self.color = color


Bprime_M1000_2022 = sample("Bprime_M1000_2022", "2022", "Bprime_M1000_2022NanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1000_2022EE = sample("Bprime_M1000_2022EE", "2022EE", "Bprime_M1000_2022EENanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1000_2023 = sample("Bprime_M1000_2023", "2023", "Bprime_M1000_2023NanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1000_2023BPix = sample("Bprime_M1000_2023BPix", "2023BPix", "Bprime_M1000_2023BPixNanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1200_2022 = sample("Bprime_M1200_2022", "2022", "Bprime_M1200_2022NanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1200_2022EE = sample("Bprime_M1200_2022EE", "2022EE", "Bprime_M1200_2022EENanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1200_2023 = sample("Bprime_M1200_2023", "2023", "Bprime_M1200_2023NanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1200_2023BPix = sample("Bprime_M1200_2023BPix", "2023BPix", "Bprime_M1200_2023BPixNanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1300_2022 = sample("Bprime_M1300_2022", "2022", "Bprime_M1300_2022NanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1300_2022EE = sample("Bprime_M1300_2022EE", "2022EE", "Bprime_M1300_2022EENanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1300_2023 = sample("Bprime_M1300_2023", "2023", "Bprime_M1300_2023NanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1300_2023BPix = sample("Bprime_M1300_2023BPix", "2023BPix", "Bprime_M1300_2023BPixNanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1400_2022 = sample("Bprime_M1400_2022", "2022", "Bprime_M1400_2022NanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1400_2022EE = sample("Bprime_M1400_2022EE", "2022EE", "Bprime_M1400_2022EENanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1400_2023 = sample("Bprime_M1400_2023", "2023", "Bprime_M1400_2023NanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1400_2023BPix = sample("Bprime_M1400_2023BPix", "2023BPix", "Bprime_M1400_2023BPixNanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1500_2022 = sample("Bprime_M1500_2022", "2022", "Bprime_M1500_2022NanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1500_2022EE = sample("Bprime_M1500_2022EE", "2022EE", "Bprime_M1500_2022EENanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1500_2023 = sample("Bprime_M1500_2023", "2023", "Bprime_M1500_2023NanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1500_2023BPix = sample("Bprime_M1500_2023BPix", "2023BPix", "Bprime_M1500_2023BPixNanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1600_2022 = sample("Bprime_M1600_2022", "2022", "Bprime_M1600_2022NanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1600_2022EE = sample("Bprime_M1600_2022EE", "2022EE", "Bprime_M1600_2022EENanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1600_2023 = sample("Bprime_M1600_2023", "2023", "Bprime_M1600_2023NanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1600_2023BPix = sample("Bprime_M1600_2023BPix", "2023BPix", "Bprime_M1600_2023BPixNanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1700_2022 = sample("Bprime_M1700_2022", "2022", "Bprime_M1700_2022NanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1700_2022EE = sample("Bprime_M1700_2022EE", "2022EE", "Bprime_M1700_2022EENanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1700_2023 = sample("Bprime_M1700_2023", "2023", "Bprime_M1700_2023NanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1700_2023BPix = sample("Bprime_M1700_2023BPix", "2023BPix", "Bprime_M1700_2023BPixNanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1800_2022 = sample("Bprime_M1800_2022", "2022", "Bprime_M1800_2022NanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1800_2022EE = sample("Bprime_M1800_2022EE", "2022EE", "Bprime_M1800_2022EENanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1800_2023 = sample("Bprime_M1800_2023", "2023", "Bprime_M1800_2023NanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M1800_2023BPix = sample("Bprime_M1800_2023BPix", "2023BPix", "Bprime_M1800_2023BPixNanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M2000_2022 = sample("Bprime_M2000_2022", "2022", "Bprime_M2000_2022NanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M2000_2022EE = sample("Bprime_M2000_2022EE", "2022EE", "Bprime_M2000_2022EENanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M2000_2023 = sample("Bprime_M2000_2023", "2023", "Bprime_M2000_2023NanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M2000_2023BPix = sample("Bprime_M2000_2023BPix", "2023BPix", "Bprime_M2000_2023BPixNanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M2200_2022 = sample("Bprime_M2200_2022", "2022", "Bprime_M2200_2022NanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M2200_2022EE = sample("Bprime_M2200_2022EE", "2022EE", "Bprime_M2200_2022EENanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M2200_2023 = sample("Bprime_M2200_2023", "2023", "Bprime_M2200_2023NanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M2200_2023BPix = sample("Bprime_M2200_2023BPix", "2023BPix", "Bprime_M2200_2023BPixNanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M800_2022 = sample("Bprime_M800_2022", "2022", "Bprime_M800_2022NanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M800_2022EE  = sample("Bprime_M800_2022EE", "2022EE", "Bprime_M800_2022EENanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M800_2023  = sample("Bprime_M800_2023", "2023", "Bprime_M800_2023NanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
Bprime_M800_2023BPix  = sample("Bprime_M800_2023BPix", "2023BPix", "Bprime_M800_2023BPixNanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
DYMHT12002022 = sample("DYMHT12002022", "2022", "DYMHT12002022NanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT12002022EE = sample("DYMHT12002022EE", "2022EE", "DYMHT12002022EENanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT12002023 = sample("DYMHT12002023", "2023", "DYMHT12002023NanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
DYMHT12002023BPix = sample("DYMHT12002023BPix", "2023BPix", "DYMHT12002023BPixNanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT2002022 = sample("DYMHT2002022", "2022", "DYMHT2002022NanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT2002022EE = sample("DYMHT2002022EE", "2022EE", "DYMHT2002022EENanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT2002023 = sample("DYMHT2002023", "2023", "DYMHT2002023NanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
DYMHT2002023BPix = sample("DYMHT2002023BPix", "2023BPix", "DYMHT2002023BPixNanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT25002022 = sample("DYMHT25002022", "2022", "DYMHT25002022NanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT25002022EE = sample("DYMHT25002022EE", "2022EE", "DYMHT25002022EENanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT25002023 = sample("DYMHT25002023", "2023", "DYMHT25002023NanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
DYMHT25002023BPix = sample("DYMHT25002023BPix", "2023BPix", "DYMHT25002023BPixNanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT4002022 = sample("DYMHT4002022", "2022", "DYMHT4002022NanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT4002022EE = sample("DYMHT4002022EE", "2022EE", "DYMHT4002022EENanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT4002023 = sample("DYMHT4002023", "2023", "DYMHT4002023NanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
DYMHT4002023BPix = sample("DYMHT4002023BPix", "2023BPix", "DYMHT4002023BPixNanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT6002022 = sample("DYMHT6002022", "2022", "DYMHT6002022NanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT6002022EE = sample("DYMHT6002022EE", "2022EE", "DYMHT6002022EENanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT6002023 = sample("DYMHT6002023", "2023", "DYMHT6002023NanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
DYMHT6002023BPix = sample("DYMHT6002023BPix", "2023BPix", "DYMHT6002023BPixNanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT8002022 = sample("DYMHT8002022", "2022", "DYMHT8002022NanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT8002022EE = sample("DYMHT8002022EE", "2022EE", "DYMHT8002022EENanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT8002023 = sample("DYMHT8002023", "2023", "DYMHT8002023NanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
DYMHT8002023BPix = sample("DYMHT8002023BPix", "2023BPix", "DYMHT8002023BPixNanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
JetHTRun2022B    = sample("JetHTRun2022B", "2022", "JetHTRun2022BNanoList.txt", "/JetHT/Run2022EEB-ver2_HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2022C    = sample("JetHTRun2022C", "2022", "JetHTRun2022CNanoList.txt", "/JetHT/Run2022EEC-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2022D    = sample("JetHTRun2022D", "2022", "JetHTRun2022DNanoList.txt", "/JetHT/Run2022EED-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2022E    = sample("JetHTRun2022E", "2022", "JetHTRun2022ENanoList.txt", "/JetHT/Run2022EEE-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2022F    = sample("JetHTRun2022F", "2022", "JetHTRun2022FNanoList.txt", "/JetHT/Run2022EEF-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2022EEF       = sample("JetHTRun2022EEF", "2022EE", "JetHTRun2022EEFNanoList.txt", "/JetHT/Run2022EEF-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2022EEG       = sample("JetHTRun2022EEG", "2022EE", "JetHTRun2022EEGNanoList.txt", "/JetHT/Run2022EEG-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2022EEH       = sample("JetHTRun2022EEH", "2022EE", "JetHTRun2022EEHNanoList.txt", "/JetHT/Run2022EEH-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023B       = sample("JetHTRun2023B", "2023", "JetHTRun2023BNanoList.txt", "/JetHT/Run2023B-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023C       = sample("JetHTRun2023C", "2023", "JetHTRun2023CNanoList.txt", "/JetHT/Run2023C-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023D       = sample("JetHTRun2023D", "2023", "JetHTRun2023DNanoList.txt", "/JetHT/Run2023D-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023E       = sample("JetHTRun2023E", "2023", "JetHTRun2023ENanoList.txt", "/JetHT/Run2023E-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023F       = sample("JetHTRun2023F", "2023", "JetHTRun2023FNanoList.txt", "/JetHT/Run2023F-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023BPixA       = sample("JetHTRun2023BPixA", "2023BPix", "JetHTRun2023BPixANanoList.txt", "/JetHT/Run2023BPixA-2023BPix_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2023BPixB       = sample("JetHTRun2023BPixB", "2023BPix", "JetHTRun2023BPixBNanoList.txt", "/JetHT/Run2023BPixB-2023BPix_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023BPixC       = sample("JetHTRun2023BPixC", "2023BPix", "JetHTRun2023BPixCNanoList.txt", "/JetHT/Run2023BPixC-2023BPix_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2023BPixD       = sample("JetHTRun2023BPixD", "2023BPix", "JetHTRun2023BPixDNanoList.txt", "/JetHT/Run2023BPixD-2023BPix_MiniAODv2_NanoAODv9-v2/NANOAOD")
QCDHT10002022  = sample("QCDHT10002022", "2022", "QCDHT10002022NanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT10002022EE     = sample("QCDHT10002022EE", "2022EE", "QCDHT10002022EENanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT10002023     = sample("QCDHT10002023", "2023", "QCDHT10002023NanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT10002023BPix     = sample("QCDHT10002023BPix", "2023BPix", "QCDHT10002023BPixNanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT15002022  = sample("QCDHT15002022", "2022", "QCDHT15002022NanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT15002022EE     = sample("QCDHT15002022EE", "2022EE", "QCDHT15002022EENanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT15002023     = sample("QCDHT15002023", "2023", "QCDHT15002023NanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT15002023BPix     = sample("QCDHT15002023BPix", "2023BPix", "QCDHT15002023BPixNanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT20002022  = sample("QCDHT20002022", "2022", "QCDHT20002022NanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT20002022EE     = sample("QCDHT20002022EE", "2022EE", "QCDHT20002022EENanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT20002023     = sample("QCDHT20002023", "2023", "QCDHT20002023NanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT20002023BPix     = sample("QCDHT20002023BPix", "2023BPix", "QCDHT20002023BPixNanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT2002022   = sample("QCDHT2002022", "2022", "QCDHT2002022NanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT2002022EE      = sample("QCDHT2002022EE", "2022EE", "QCDHT2002022EENanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT2002023      = sample("QCDHT2002023", "2023", "QCDHT2002023NanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT2002023BPix      = sample("QCDHT2002023BPix", "2023BPix", "QCDHT2002023BPixNanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT3002022   = sample("QCDHT3002022", "2022", "QCDHT3002022NanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT3002022EE      = sample("QCDHT3002022EE", "2022EE", "QCDHT3002022EENanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT3002023      = sample("QCDHT3002023", "2023", "QCDHT3002023NanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT3002023BPix      = sample("QCDHT3002023BPix", "2023BPix", "QCDHT3002023BPixNanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT5002022   = sample("QCDHT5002022", "2022", "QCDHT5002022NanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT5002022EE      = sample("QCDHT5002022EE", "2022EE", "QCDHT5002022EENanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT5002023      = sample("QCDHT5002023", "2023", "QCDHT5002023NanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT5002023BPix      = sample("QCDHT5002023BPix", "2023BPix", "QCDHT5002023BPixNanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT7002022   = sample("QCDHT7002022", "2022", "QCDHT7002022NanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT7002022EE      = sample("QCDHT7002022EE", "2022EE", "QCDHT7002022EENanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT7002023      = sample("QCDHT7002023", "2023", "QCDHT7002023NanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
QCDHT7002023BPix      = sample("QCDHT7002023BPix", "2023BPix", "QCDHT7002023BPixNanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
SingleElecRun2022A = sample("SingleElecRun2022A", "2022", "SingleElecRun2022A2022NanoList.txt", "/SingleElectron/Run2022EEB-ver1_HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2022B = sample("SingleElecRun2022B", "2022", "SingleElecRun2022B2022NanoList.txt", "/SingleElectron/Run2022EEB-ver2_HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2022C = sample("SingleElecRun2022C", "2022", "SingleElecRun2022C2022NanoList.txt", "/SingleElectron/Run2022EEC-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2022D = sample("SingleElecRun2022D", "2022", "SingleElecRun2022D2022NanoList.txt", "/SingleElectron/Run2022EED-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2022E = sample("SingleElecRun2022E", "2022", "SingleElecRun2022E2022NanoList.txt", "/SingleElectron/Run2022EEE-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2022F = sample("SingleElecRun2022F", "2022", "SingleElecRun2022F2022NanoList.txt", "/SingleElectron/Run2022EEF-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2022EEF  = sample("SingleElecRun2022EEF", "2022EE", "SingleElecRun2022EEF2022EENanoList.txt", "/SingleElectron/Run2022EEF-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2022EEG  = sample("SingleElecRun2022EEG", "2022EE", "SingleElecRun2022EEG2022EENanoList.txt", "/SingleElectron/Run2022EEG-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2022EEH  = sample("SingleElecRun2022EEH", "2022EE", "SingleElecRun2022EEH2022EENanoList.txt", "/SingleElectron/Run2022EEH-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023B  = sample("SingleElecRun2023B", "2023", "SingleElecRun2023B2023NanoList.txt", "/SingleElectron/Run2023B-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023C  = sample("SingleElecRun2023C", "2023", "SingleElecRun2023C2023NanoList.txt", "/SingleElectron/Run2023C-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023D  = sample("SingleElecRun2023D", "2023", "SingleElecRun2023D2023NanoList.txt", "/SingleElectron/Run2023D-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023E  = sample("SingleElecRun2023E", "2023", "SingleElecRun2023E2023NanoList.txt", "/SingleElectron/Run2023E-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023F  = sample("SingleElecRun2023F", "2023", "SingleElecRun2023F2023NanoList.txt", "/SingleElectron/Run2023F-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023BPixA  = sample("SingleElecRun2023BPixA", "2023BPix", "SingleElecRun2023BPixA2023BPixNanoList.txt", "/EGamma/Run2023BPixA-2023BPix_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023BPixB  = sample("SingleElecRun2023BPixB", "2023BPix", "SingleElecRun2023BPixB2023BPixNanoList.txt", "/EGamma/Run2023BPixB-2023BPix_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023BPixC  = sample("SingleElecRun2023BPixC", "2023BPix", "SingleElecRun2023BPixC2023BPixNanoList.txt", "/EGamma/Run2023BPixC-2023BPix_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2023BPixD  = sample("SingleElecRun2023BPixD", "2023BPix", "SingleElecRun2023BPixD2023BPixNanoList.txt", "/EGamma/Run2023BPixD-2023BPix_MiniAODv2_NanoAODv9-v3/NANOAOD")
SingleMuonRun2022A = sample("SingleMuonRun2022A", "2022", "SingleMuonRun2022A2022NanoList.txt", "/SingleMuon/Run2022EEB-ver1_HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2022B = sample("SingleMuonRun2022B", "2022", "SingleMuonRun2022B2022NanoList.txt", "/SingleMuon/Run2022EEB-ver2_HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2022C = sample("SingleMuonRun2022C", "2022", "SingleMuonRun2022C2022NanoList.txt", "/SingleMuon/Run2022EEC-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2022D = sample("SingleMuonRun2022D", "2022", "SingleMuonRun2022D2022NanoList.txt", "/SingleMuon/Run2022EED-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2022E = sample("SingleMuonRun2022E", "2022", "SingleMuonRun2022E2022NanoList.txt", "/SingleMuon/Run2022EEE-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2022F = sample("SingleMuonRun2022F", "2022", "SingleMuonRun2022F2022NanoList.txt", "/SingleMuon/Run2022EEF-HIPM_2022EE_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2022EEF  = sample("SingleMuonRun2022EEF", "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/SingleMuon/Run2022EEF-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2022EEG  = sample("SingleMuonRun2022EEG", "2022EE", "SingleMuonRun2022EEG2022EENanoList.txt", "/SingleMuon/Run2022EEG-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2022EEH  = sample("SingleMuonRun2022EEH", "2022EE", "SingleMuonRun2022EEH2022EENanoList.txt", "/SingleMuon/Run2022EEH-2022EE_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2023B  = sample("SingleMuonRun2023B", "2023", "SingleMuonRun2023B2023NanoList.txt", "/SingleMuon/Run2023B-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2023C  = sample("SingleMuonRun2023C", "2023", "SingleMuonRun2023C2023NanoList.txt", "/SingleMuon/Run2023C-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2023D  = sample("SingleMuonRun2023D", "2023", "SingleMuonRun2023D2023NanoList.txt", "/SingleMuon/Run2023D-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2023E  = sample("SingleMuonRun2023E", "2023", "SingleMuonRun2023E2023NanoList.txt", "/SingleMuon/Run2023E-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2023F  = sample("SingleMuonRun2023F", "2023", "SingleMuonRun2023F2023NanoList.txt", "/SingleMuon/Run2023F-2023_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2023BPixA  = sample("SingleMuonRun2023BPixA", "2023BPix", "SingleMuonRun2023BPixA2023BPixNanoList.txt", "/SingleMuon/Run2023BPixA-2023BPix_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2023BPixB  = sample("SingleMuonRun2023BPixB", "2023BPix", "SingleMuonRun2023BPixB2023BPixNanoList.txt", "/SingleMuon/Run2023BPixB-2023BPix_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2023BPixC  = sample("SingleMuonRun2023BPixC", "2023BPix", "SingleMuonRun2023BPixC2023BPixNanoList.txt", "/SingleMuon/Run2023BPixC-2023BPix_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2023BPixD  = sample("SingleMuonRun2023BPixD", "2023BPix", "SingleMuonRun2023BPixD2023BPixNanoList.txt", "/SingleMuon/Run2023BPixD-2023BPix_MiniAODv2_NanoAODv9-v1/NANOAOD")
STs2022 = sample("STs2022", "2022", "STs2022NanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STs2022EE = sample("STs2022EE", "2022EE", "STs2022EENanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
STs2023 = sample("STs2023", "2023", "STs2023NanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
STs2023BPix = sample("STs2023BPix", "2023BPix", "STs2023BPixNanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
STt2022 = sample("STt2022", "2022", "STt2022NanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STt2022EE = sample("STt2022EE", "2022EE", "STt2022EENanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
STt2023 = sample("STt2023", "2023", "STt2023NanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
STt2023BPix = sample("STt2023BPix", "2023BPix", "STt2023BPixNanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
STtb2022 = sample("STtb2022", "2022", "STtb2022NanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STtb2022EE = sample("STtb2022EE", "2022EE", "STtb2022EENanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
STtb2023 = sample("STtb2023", "2023", "STtb2023NanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
STtb2023BPix = sample("STtb2023BPix", "2023BPix", "STtb2023BPixNanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
STtW2022 = sample("STtW2022", "2022", "STtW2022NanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STtW2022EE = sample("STtW2022EE", "2022EE", "STtW2022EENanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
STtW2023 = sample("STtW2023", "2023", "STtW2023NanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
STtW2023BPix = sample("STtW2023BPix", "2023BPix", "STtW2023BPixNanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
STtWb2022 = sample("STtWb2022", "2022", "STtWb2022NanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STtWb2022EE = sample("STtWb2022EE", "2022EE", "STtWb2022EENanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
STtWb2023 = sample("STtWb2023", "2023", "STtWb2023NanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
STtWb2023BPix = sample("STtWb2023BPix", "2023BPix", "STtWb2023BPixNanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
TTHB2022 = sample("TTHB2022", "2022", "TTHB2022NanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTHB2022EE = sample("TTHB2022EE", "2022EE", "TTHB2022EENanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
TTHB2023 = sample("TTHB2023", "2023", "TTHB2023NanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
TTHB2023BPix = sample("TTHB2023BPix", "2023BPix", "TTHB2023BPixNanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
TTHnonB2022 = sample("TTHnonB2022", "2022", "TTHnonB2022NanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTHnonB2022EE = sample("TTHnonB2022EE", "2022EE", "TTHnonB2022EENanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
TTHnonB2023 = sample("TTHnonB2023", "2023", "TTHnonB2023NanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
TTHnonB2023BPix = sample("TTHnonB2023BPix", "2023BPix", "TTHnonB2023BPixNanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
TTMT10002022 = sample("TTMT10002022", "2022", "TTMT10002022NanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTMT10002022EE = sample("TTMT10002022EE", "2022EE", "TTMT10002022EENanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTMT10002023 = sample("TTMT10002023", "2023", "TTMT10002023NanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
TTMT10002023BPix = sample("TTMT10002023BPix", "2023BPix", "TTMT10002023BPixNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTMT7002022 = sample("TTMT7002022", "2022", "TTMT7002022NanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTMT7002022EE = sample("TTMT7002022EE", "2022EE", "TTMT7002022EENanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTMT7002023 = sample("TTMT7002023", "2023", "TTMT7002023NanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
TTMT7002023BPix = sample("TTMT7002023BPix", "2023BPix", "TTMT7002023BPixNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTTo2L2Nu2022 = sample("TTTo2L2Nu2022", "2022", "TTTo2L2Nu2022NanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTTo2L2Nu2022EE = sample("TTTo2L2Nu2022EE", "2022EE", "TTTo2L2Nu2022EENanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTTo2L2Nu2023 = sample("TTTo2L2Nu2023", "2023", "TTTo2L2Nu2023NanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTTo2L2Nu2023BPix = sample("TTTo2L2Nu2023BPix", "2023BPix", "TTTo2L2Nu2023BPixNanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTToHadronic2022 = sample("TTToHadronic2022", "2022", "TTToHadronic2022NanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTToHadronic2022EE = sample("TTToHadronic2022EE", "2022EE", "TTToHadronic2022EENanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTToHadronic2023 = sample("TTToHadronic2023", "2023", "TTToHadronic2023NanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTToHadronic2023BPix = sample("TTToHadronic2023BPix", "2023BPix", "TTToHadronic2023BPixNanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTToSemiLeptonic2022 = sample("TTToSemiLeptonic2022", "2022", "TTToSemiLeptonic2022NanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTToSemiLeptonic2022EE = sample("TTToSemiLeptonic2022EE", "2022EE", "TTToSemiLeptonic2022EENanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTToSemiLeptonic2023 = sample("TTToSemiLeptonic2023", "2023", "TTToSemiLeptonic2023NanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTToSemiLeptonic2023BPix = sample("TTToSemiLeptonic2023BPix", "2023BPix", "TTToSemiLeptonic2023BPixNanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTWl2022 = sample("TTWl2022", "2022", "TTWl2022NanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTWl2022EE = sample("TTWl2022EE", "2022EE", "TTWl2022EENanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTWl2023 = sample("TTWl2023", "2023", "TTWl2023NanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTWl2023BPix = sample("TTWl2023BPix", "2023BPix", "TTWl2023BPixNanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTWq2022 = sample("TTWq2022", "2022", "TTWq2022NanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTWq2022EE = sample("TTWq2022EE", "2022EE", "TTWq2022EENanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTWq2023 = sample("TTWq2023", "2023", "TTWq2023NanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTWq2023BPix = sample("TTWq2023BPix", "2023BPix", "TTWq2023BPixNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTZM102022 = sample("TTZM102022", "2022", "TTZM102022NanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTZM102022EE = sample("TTZM102022EE", "2022EE", "TTZM102022EENanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTZM102023 = sample("TTZM102023", "2023", "TTZM102023NanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTZM102023BPix = sample("TTZM102023BPix", "2023BPix", "TTZM102023BPixNanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTZM1to102022 = sample("TTZM1to102022", "2022", "TTZM1to102022NanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTZM1to102022EE = sample("TTZM1to102022EE", "2022EE", "TTZM1to102022EENanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTZM1to102023 = sample("TTZM1to102023", "2023", "TTZM1to102023NanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTZM1to102023BPix = sample("TTZM1to102023BPix", "2023BPix", "TTZM1to102023BPixNanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT12002022 = sample("WJetsHT12002022", "2022", "WJetsHT12002022NanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT12002022EE = sample("WJetsHT12002022EE", "2022EE", "WJetsHT12002022EENanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT12002023 = sample("WJetsHT12002023", "2023", "WJetsHT12002023NanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
WJetsHT12002023BPix = sample("WJetsHT12002023BPix", "2023BPix", "WJetsHT12002023BPixNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT1200ext2023BPix = sample("WJetsHT1200ext2023BPix", "2023BPix", "WJetsHT1200ext2023BPixNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WJetsHT2002022 = sample("WJetsHT2002022", "2022", "WJetsHT2002022NanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT2002022EE = sample("WJetsHT2002022EE", "2022EE", "WJetsHT2002022EENanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT2002023 = sample("WJetsHT2002023", "2023", "WJetsHT2002023NanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
WJetsHT2002023BPix = sample("WJetsHT2002023BPix", "2023BPix", "WJetsHT2002023BPixNanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT25002022 = sample("WJetsHT25002022", "2022", "WJetsHT25002022NanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
WJetsHT25002022EE = sample("WJetsHT25002022EE", "2022EE", "WJetsHT25002022EENanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
WJetsHT25002023 = sample("WJetsHT25002023", "2023", "WJetsHT25002023NanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v2/NANOAODSIM")
WJetsHT25002023BPix = sample("WJetsHT25002023BPix", "2023BPix", "WJetsHT25002023BPixNanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v2/NANOAODSIM")
WJetsHT4002022 = sample("WJetsHT4002022", "2022", "WJetsHT4002022NanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT4002022EE = sample("WJetsHT4002022EE", "2022EE", "WJetsHT4002022EENanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT4002023 = sample("WJetsHT4002023", "2023", "WJetsHT4002023NanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
WJetsHT4002023BPix = sample("WJetsHT4002023BPix", "2023BPix", "WJetsHT4002023BPixNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT400ext2023BPix = sample("WJetsHT400ext2023BPix", "2023BPix", "WJetsHT400ext2023BPixNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WJetsHT6002022 = sample("WJetsHT6002022", "2022", "WJetsHT6002022NanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT6002022EE = sample("WJetsHT6002022EE", "2022EE", "WJetsHT6002022EENanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT6002023 = sample("WJetsHT6002023", "2023", "WJetsHT6002023NanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
WJetsHT6002023BPix = sample("WJetsHT6002023BPix", "2023BPix", "WJetsHT6002023BPixNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT600ext2023BPix = sample("WJetsHT600ext2023BPix", "2023BPix", "WJetsHT600ext2023BPixNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WJetsHT8002022 = sample("WJetsHT8002022", "2022", "WJetsHT8002022NanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT8002022EE = sample("WJetsHT8002022EE", "2022EE", "WJetsHT8002022EENanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT8002023 = sample("WJetsHT8002023", "2023", "WJetsHT8002023NanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v3/NANOAODSIM")
WJetsHT8002023BPix = sample("WJetsHT8002023BPix", "2023BPix", "WJetsHT8002023BPixNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT800ext2023BPix = sample("WJetsHT800ext2023BPix", "2023BPix", "WJetsHT800ext2023BPixNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WW2022 = sample("WW2022", "2022", "WW2022NanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WW2022EE = sample("WW2022EE", "2022EE", "WW2022EENanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WW2023 = sample("WW2023", "2023", "WW2023NanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
WW2023BPix = sample("WW2023BPix", "2023BPix", "WW2023BPixNanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
WZ2022 = sample("WZ2022", "2022", "WZ2022NanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WZ2022EE = sample("WZ2022EE", "2022EE", "WZ2022EENanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WZ2023 = sample("WZ2023", "2023", "WZ2023NanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
WZ2023BPix = sample("WZ2023BPix", "2023BPix", "WZ2023BPixNanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
ZZ2022 = sample("ZZ2022", "2022", "ZZ2022NanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
ZZ2022EE = sample("ZZ2022EE", "2022EE", "ZZ2022EENanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
ZZ2023 = sample("ZZ2023", "2023", "ZZ2023NanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")

samples_data = {
    "SingleElecRun2022B":SingleElecRun2022B,
    "SingleElecRun2022C":SingleElecRun2022C,
    "SingleElecRun2022D":SingleElecRun2022D,
    "SingleElecRun2022E":SingleElecRun2022E,
    "SingleElecRun2022F":SingleElecRun2022F,
    "SingleElecRun2022EEF":SingleElecRun2022EEF,
    "SingleElecRun2022EEG":SingleElecRun2022EEG,
    "SingleElecRun2022EEH":SingleElecRun2022EEH,
    "SingleElecRun2023B":SingleElecRun2023B,
    "SingleElecRun2023C":SingleElecRun2023C,
    "SingleElecRun2023D":SingleElecRun2023D,
    "SingleElecRun2023E":SingleElecRun2023E,
    "SingleElecRun2023F":SingleElecRun2023F,
    "SingleElecRun2023BPixA":SingleElecRun2023BPixA,
    "SingleElecRun2023BPixB":SingleElecRun2023BPixB,
    "SingleElecRun2023BPixC":SingleElecRun2023BPixC,
    "SingleElecRun2023BPixD":SingleElecRun2023BPixD,
    "SingleMuonRun2022B":SingleMuonRun2022B,
    "SingleMuonRun2022C":SingleMuonRun2022C,
    "SingleMuonRun2022D":SingleMuonRun2022D,
    "SingleMuonRun2022E":SingleMuonRun2022E,
    "SingleMuonRun2022F":SingleMuonRun2022F,
    "SingleMuonRun2022EEF":SingleMuonRun2022EEF,
    "SingleMuonRun2022EEG":SingleMuonRun2022EEG,
    "SingleMuonRun2022EEH":SingleMuonRun2022EEH,
    "SingleMuonRun2023B":SingleMuonRun2023B,
    "SingleMuonRun2023C":SingleMuonRun2023C,
    "SingleMuonRun2023D":SingleMuonRun2023D,
    "SingleMuonRun2023E":SingleMuonRun2023E,
    "SingleMuonRun2023F":SingleMuonRun2023F,
    "SingleMuonRun2023BPixA":SingleMuonRun2023BPixA,
    "SingleMuonRun2023BPixB":SingleMuonRun2023BPixB,
    "SingleMuonRun2023BPixC":SingleMuonRun2023BPixC,
    "SingleMuonRun2023BPixD":SingleMuonRun2023BPixD,
}

samples={
    "Bprime_M1000_2022":Bprime_M1000_2022,
    "Bprime_M1000_2022EE":Bprime_M1000_2022EE,
    "Bprime_M1000_2023":Bprime_M1000_2023,
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1200_2022":Bprime_M1200_2022,
    "Bprime_M1200_2022EE":Bprime_M1200_2022EE,
    "Bprime_M1200_2023":Bprime_M1200_2023,
    "Bprime_M1200_2023BPix":Bprime_M1200_2023BPix,
    "Bprime_M1300_2022":Bprime_M1300_2022,
    "Bprime_M1300_2022EE":Bprime_M1300_2022EE,
    "Bprime_M1300_2023":Bprime_M1300_2023,
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1400_2022":Bprime_M1400_2022,
    "Bprime_M1400_2022EE":Bprime_M1400_2022EE,
    "Bprime_M1400_2023":Bprime_M1400_2023,
    "Bprime_M1400_2023BPix":Bprime_M1400_2023BPix,
    "Bprime_M1500_2022":Bprime_M1500_2022,
    "Bprime_M1500_2022EE":Bprime_M1500_2022EE,
    "Bprime_M1500_2023":Bprime_M1500_2023,
    "Bprime_M1500_2023BPix":Bprime_M1500_2023BPix,
    "Bprime_M1600_2022":Bprime_M1600_2022,
    "Bprime_M1600_2022EE":Bprime_M1600_2022EE,
    "Bprime_M1600_2023":Bprime_M1600_2023,
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M1700_2022":Bprime_M1700_2022,
    "Bprime_M1700_2022EE":Bprime_M1700_2022EE,
    "Bprime_M1700_2023":Bprime_M1700_2023,
    "Bprime_M1700_2023BPix":Bprime_M1700_2023BPix,
    "Bprime_M1800_2022":Bprime_M1800_2022,
    "Bprime_M1800_2022EE":Bprime_M1800_2022EE,
    "Bprime_M1800_2023":Bprime_M1800_2023,
    "Bprime_M1800_2023BPix":Bprime_M1800_2023BPix,
    "Bprime_M2000_2022":Bprime_M2000_2022,
    "Bprime_M2000_2022EE":Bprime_M2000_2022EE,
    "Bprime_M2000_2023":Bprime_M2000_2023,
    "Bprime_M2000_2023BPix":Bprime_M2000_2023BPix,
    "Bprime_M2200_2022":Bprime_M2200_2022,
    "Bprime_M2200_2022EE":Bprime_M2200_2022EE,
    "Bprime_M2200_2023":Bprime_M2200_2023,
    "Bprime_M2200_2023BPix":Bprime_M2200_2023BPix,
    "Bprime_M800_2022":Bprime_M800_2022,
    "Bprime_M800_2022EE":Bprime_M800_2022EE,
    "Bprime_M800_2023":Bprime_M800_2023,
    "Bprime_M800_2023BPix":Bprime_M800_2023BPix,
    "DYMHT12002022":DYMHT12002022,
    "DYMHT12002022EE":DYMHT12002022EE,
    "DYMHT12002023":DYMHT12002023,
    "DYMHT12002023BPix":DYMHT12002023BPix,
    "DYMHT2002022":DYMHT2002022,
    "DYMHT2002022EE":DYMHT2002022EE,
    "DYMHT2002023":DYMHT2002023,
    "DYMHT2002023BPix":DYMHT2002023BPix,
    "DYMHT25002022":DYMHT25002022,
    "DYMHT25002022EE":DYMHT25002022EE,
    "DYMHT25002023":DYMHT25002023,
    "DYMHT25002023BPix":DYMHT25002023BPix,
    "DYMHT4002022":DYMHT4002022,
    "DYMHT4002022EE":DYMHT4002022EE,
    "DYMHT4002023":DYMHT4002023,
    "DYMHT4002023BPix":DYMHT4002023BPix,
    "DYMHT6002022":DYMHT6002022,
    "DYMHT6002022EE":DYMHT6002022EE,
    "DYMHT6002023":DYMHT6002023,
    "DYMHT6002023BPix":DYMHT6002023BPix,
    "DYMHT8002022":DYMHT8002022,
    "DYMHT8002022EE":DYMHT8002022EE,
    "DYMHT8002023":DYMHT8002023,
    "DYMHT8002023BPix":DYMHT8002023BPix,
    # "JetHTRun2022B":JetHTRun2022B,
    # "JetHTRun2022C":JetHTRun2022C,
    # "JetHTRun2022D":JetHTRun2022D,
    # "JetHTRun2022E":JetHTRun2022E,
    # "JetHTRun2022F":JetHTRun2022F,
    # "JetHTRun2022EEF":JetHTRun2022EEF,
    # "JetHTRun2022EEG":JetHTRun2022EEG,
    # "JetHTRun2022EEH":JetHTRun2022EEH,
    # "JetHTRun2023B":JetHTRun2023B,
    # "JetHTRun2023C":JetHTRun2023C,
    # "JetHTRun2023D":JetHTRun2023D,
    # "JetHTRun2023E":JetHTRun2023E,
    # "JetHTRun2023F":JetHTRun2023F,
    # "JetHTRun2023BPixA":JetHTRun2023BPixA,
    # "JetHTRun2023BPixB":JetHTRun2023BPixB,
    # "JetHTRun2023BPixC":JetHTRun2023BPixC,
    # "JetHTRun2023BPixD":JetHTRun2023BPixD,
    "QCDHT10002022":QCDHT10002022,
    "QCDHT10002022EE":QCDHT10002022EE,
    "QCDHT10002023":QCDHT10002023,
    "QCDHT10002023BPix":QCDHT10002023BPix,
    "QCDHT15002022":QCDHT15002022,
    "QCDHT15002022EE":QCDHT15002022EE,
    "QCDHT15002023":QCDHT15002023,
    "QCDHT15002023BPix":QCDHT15002023BPix,
    "QCDHT20002022":QCDHT20002022,
    "QCDHT20002022EE":QCDHT20002022EE,
    "QCDHT20002023":QCDHT20002023,
    "QCDHT20002023BPix":QCDHT20002023BPix,
    "QCDHT2002022":QCDHT2002022,
    "QCDHT2002022EE":QCDHT2002022EE,
    "QCDHT2002023":QCDHT2002023,
    "QCDHT2002023BPix":QCDHT2002023BPix,
    "QCDHT3002022":QCDHT3002022,
    "QCDHT3002022EE":QCDHT3002022EE,
    "QCDHT3002023":QCDHT3002023,
    "QCDHT3002023BPix":QCDHT3002023BPix,
    "QCDHT5002022":QCDHT5002022,
    "QCDHT5002022EE":QCDHT5002022EE,
    "QCDHT5002023":QCDHT5002023,
    "QCDHT5002023BPix":QCDHT5002023BPix,
    "QCDHT7002022":QCDHT7002022,
    "QCDHT7002022EE":QCDHT7002022EE,
    "QCDHT7002023":QCDHT7002023,
    "QCDHT7002023BPix":QCDHT7002023BPix,
    # "SingleElecRun2022B":SingleElecRun2022B,
    # "SingleElecRun2022C":SingleElecRun2022C,
    # "SingleElecRun2022D":SingleElecRun2022D,
    # "SingleElecRun2022E":SingleElecRun2022E,
    # "SingleElecRun2022F":SingleElecRun2022F,
    # "SingleElecRun2022EEF":SingleElecRun2022EEF,
    # "SingleElecRun2022EEG":SingleElecRun2022EEG,
    # "SingleElecRun2022EEH":SingleElecRun2022EEH,
    # "SingleElecRun2023B":SingleElecRun2023B,
    # "SingleElecRun2023C":SingleElecRun2023C,
    # "SingleElecRun2023D":SingleElecRun2023D,
    # "SingleElecRun2023E":SingleElecRun2023E,
    # "SingleElecRun2023F":SingleElecRun2023F,
    # "SingleElecRun2023BPixA":SingleElecRun2023BPixA,
    # "SingleElecRun2023BPixB":SingleElecRun2023BPixB,
    # "SingleElecRun2023BPixC":SingleElecRun2023BPixC,
    # "SingleElecRun2023BPixD":SingleElecRun2023BPixD,
    # "SingleMuonRun2022B":SingleMuonRun2022B,
    # "SingleMuonRun2022C":SingleMuonRun2022C,
    # "SingleMuonRun2022D":SingleMuonRun2022D,
    # "SingleMuonRun2022E":SingleMuonRun2022E,
    # "SingleMuonRun2022F":SingleMuonRun2022F,
    # "SingleMuonRun2022EEF":SingleMuonRun2022EEF,
    # "SingleMuonRun2022EEG":SingleMuonRun2022EEG,
    # "SingleMuonRun2022EEH":SingleMuonRun2022EEH,
    # "SingleMuonRun2023B":SingleMuonRun2023B,
    # "SingleMuonRun2023C":SingleMuonRun2023C,
    # "SingleMuonRun2023D":SingleMuonRun2023D,
    # "SingleMuonRun2023E":SingleMuonRun2023E,
    # "SingleMuonRun2023F":SingleMuonRun2023F,
    # "SingleMuonRun2023BPixA":SingleMuonRun2023BPixA,
    # "SingleMuonRun2023BPixB":SingleMuonRun2023BPixB,
    # "SingleMuonRun2023BPixC":SingleMuonRun2023BPixC,
    # "SingleMuonRun2023BPixD":SingleMuonRun2023BPixD,
    "STs2022":STs2022,
    "STs2022EE":STs2022EE,
    "STs2023":STs2023,
    "STs2023BPix":STs2023BPix,
    "STt2022":STt2022,
    "STt2022EE":STt2022EE,
    "STt2023":STt2023,
    "STt2023BPix":STt2023BPix,
    "STtb2022":STtb2022,
    "STtb2022EE":STtb2022EE,
    "STtb2023":STtb2023,
    "STtb2023BPix":STtb2023BPix,
    "STtW2022":STtW2022,
    "STtW2022EE":STtW2022EE,
    "STtW2023":STtW2023,
    "STtW2023BPix":STtW2023BPix,
    "STtWb2022":STtWb2022,
    "STtWb2022EE":STtWb2022EE,
    "STtWb2023":STtWb2023,
    "STtWb2023BPix":STtWb2023BPix,
    "TTHB2022":TTHB2022,
    "TTHB2022EE":TTHB2022EE,
    "TTHB2023":TTHB2023,
    "TTHB2023BPix":TTHB2023BPix,
    "TTHnonB2022":TTHnonB2022,
    "TTHnonB2022EE":TTHnonB2022EE,
    "TTHnonB2023":TTHnonB2023,
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTMT10002022":TTMT10002022,
    "TTMT10002022EE":TTMT10002022EE,
    "TTMT10002023":TTMT10002023,
    "TTMT10002023BPix":TTMT10002023BPix,
    "TTMT7002022":TTMT7002022,
    "TTMT7002022EE":TTMT7002022EE,
    "TTMT7002023":TTMT7002023,
    "TTMT7002023BPix":TTMT7002023BPix,
    "TTTo2L2Nu2022":TTTo2L2Nu2022,
    "TTTo2L2Nu2022EE":TTTo2L2Nu2022EE,
    "TTTo2L2Nu2023":TTTo2L2Nu2023,
    "TTTo2L2Nu2023BPix":TTTo2L2Nu2023BPix,
    "TTToHadronic2022":TTToHadronic2022,
    "TTToHadronic2022EE":TTToHadronic2022EE,
    "TTToHadronic2023":TTToHadronic2023,
    "TTToHadronic2023BPix":TTToHadronic2023BPix,
    "TTToSemiLeptonic2022":TTToSemiLeptonic2022,
    "TTToSemiLeptonic2022EE":TTToSemiLeptonic2022EE,
    "TTToSemiLeptonic2023":TTToSemiLeptonic2023,
    "TTToSemiLeptonic2023BPix":TTToSemiLeptonic2023BPix,
    "TTWl2022":TTWl2022,
    "TTWl2022EE":TTWl2022EE,
    "TTWl2023":TTWl2023,
    "TTWl2023BPix":TTWl2023BPix,
    "TTWq2022":TTWq2022,
    "TTWq2022EE":TTWq2022EE,
    "TTWq2023":TTWq2023,
    "TTWq2023BPix":TTWq2023BPix,
    "TTZM102022":TTZM102022,
    "TTZM102022EE":TTZM102022EE,
    "TTZM102023":TTZM102023,
    "TTZM102023BPix":TTZM102023BPix,
    "TTZM1to102022":TTZM1to102022,
    "TTZM1to102022EE":TTZM1to102022EE,
    "TTZM1to102023":TTZM1to102023,
    "TTZM1to102023BPix":TTZM1to102023BPix,
    "WJetsHT12002022":WJetsHT12002022,
    "WJetsHT12002022EE":WJetsHT12002022EE,
    "WJetsHT12002023":WJetsHT12002023,
    "WJetsHT12002023BPix":WJetsHT12002023BPix,
    "WJetsHT1200ext2023BPix":WJetsHT1200ext2023BPix,
    "WJetsHT2002022":WJetsHT2002022,
    "WJetsHT2002022EE":WJetsHT2002022EE,
    "WJetsHT2002023":WJetsHT2002023,
    "WJetsHT2002023BPix":WJetsHT2002023BPix,
    "WJetsHT25002022":WJetsHT25002022,
    "WJetsHT25002022EE":WJetsHT25002022EE,
    "WJetsHT25002023":WJetsHT25002023,
    "WJetsHT25002023BPix":WJetsHT25002023BPix,
    "WJetsHT4002022":WJetsHT4002022,
    "WJetsHT4002022EE":WJetsHT4002022EE,
    "WJetsHT4002023":WJetsHT4002023,
    "WJetsHT4002023BPix":WJetsHT4002023BPix,
    "WJetsHT400ext2023BPix":WJetsHT400ext2023BPix,
    "WJetsHT6002022":WJetsHT6002022,
    "WJetsHT6002022EE":WJetsHT6002022EE,
    "WJetsHT6002023":WJetsHT6002023,
    "WJetsHT6002023BPix":WJetsHT6002023BPix,
    "WJetsHT600ext2023BPix":WJetsHT600ext2023BPix,
    "WJetsHT8002022":WJetsHT8002022,
    "WJetsHT8002022EE":WJetsHT8002022EE,
    "WJetsHT8002023":WJetsHT8002023,
    "WJetsHT8002023BPix":WJetsHT8002023BPix,
    "WJetsHT800ext2023BPix":WJetsHT800ext2023BPix,
    "WW2022":WW2022,
    "WW2022EE":WW2022EE,
    "WW2023":WW2023,
    "WW2023BPix":WW2023BPix,
    "WZ2022":WZ2022,
    "WZ2022EE":WZ2022EE,
    "WZ2023":WZ2023,
    "WZ2023BPix":WZ2023BPix,
    "ZZ2022":ZZ2022,
    "ZZ2022EE":ZZ2022EE,
    "ZZ2023":ZZ2023,
    "ZZ2023BPix":ZZ2023BPix,
}

samples_2022 = {
    
    "DYMHT12002022":DYMHT12002022,
    "DYMHT2002022":DYMHT2002022,
    "DYMHT25002022":DYMHT25002022,
    "DYMHT4002022":DYMHT4002022,
    "DYMHT6002022":DYMHT6002022,
    "DYMHT8002022":DYMHT8002022,
    # "JetHTRun2022B":JetHTRun2022B,
    # "JetHTRun2022C":JetHTRun2022C,
    # "JetHTRun2022D":JetHTRun2022D,
    # "JetHTRun2022E":JetHTRun2022E,
    # "JetHTRun2022F":JetHTRun2022F,
    "QCDHT10002022":QCDHT10002022,
    "QCDHT15002022":QCDHT15002022,
    "QCDHT20002022":QCDHT20002022,
    "QCDHT2002022":QCDHT2002022,
    "QCDHT3002022":QCDHT3002022,
    "QCDHT5002022":QCDHT5002022,
    "QCDHT7002022":QCDHT7002022,
    "SingleElecRun2022B":SingleElecRun2022B,
    "SingleElecRun2022C":SingleElecRun2022C,
    "SingleElecRun2022D":SingleElecRun2022D,
    "SingleElecRun2022E":SingleElecRun2022E,
    "SingleElecRun2022F":SingleElecRun2022F,
    "SingleMuonRun2022B":SingleMuonRun2022B,
    "SingleMuonRun2022C":SingleMuonRun2022C,
    "SingleMuonRun2022D":SingleMuonRun2022D,
    "SingleMuonRun2022E":SingleMuonRun2022E,
    "SingleMuonRun2022F":SingleMuonRun2022F,
    "STs2022":STs2022,
    "STt2022":STt2022,
    "STtb2022":STtb2022,
    "STtW2022":STtW2022,
    "STtWb2022":STtWb2022,
    "TTHB2022":TTHB2022,
    "TTHnonB2022":TTHnonB2022,
    "TTMT10002022":TTMT10002022,
    "TTMT7002022":TTMT7002022,
    "TTTo2L2Nu2022":TTTo2L2Nu2022,
    "TTToHadronic2022":TTToHadronic2022,
    "TTToSemiLeptonic2022":TTToSemiLeptonic2022,
    "TTWl2022":TTWl2022,
    "TTWq2022":TTWq2022,
    "TTZM102022":TTZM102022,
    "TTZM1to102022":TTZM1to102022,
    "WJetsHT12002022":WJetsHT12002022,
    "WJetsHT2002022":WJetsHT2002022,
    "WJetsHT25002022":WJetsHT25002022,
    "WJetsHT4002022":WJetsHT4002022,
    "WJetsHT6002022":WJetsHT6002022,
    "WJetsHT8002022":WJetsHT8002022,
    "WW2022":WW2022,
    "WZ2022":WZ2022,
    "ZZ2022":ZZ2022,

}

samples_2022EE = {
    "Bprime_M1000_2022EE":Bprime_M1000_2022EE,
    "Bprime_M1200_2022EE":Bprime_M1200_2022EE,
    "Bprime_M1300_2022EE":Bprime_M1300_2022EE,
    "Bprime_M1400_2022EE":Bprime_M1400_2022EE,
    "Bprime_M1500_2022EE":Bprime_M1500_2022EE,
    "Bprime_M1600_2022EE":Bprime_M1600_2022EE,
    "Bprime_M1700_2022EE":Bprime_M1700_2022EE,
    "Bprime_M1800_2022EE":Bprime_M1800_2022EE,
    "Bprime_M2000_2022EE":Bprime_M2000_2022EE,
    "Bprime_M2200_2022EE":Bprime_M2200_2022EE,
    "Bprime_M800_2022EE":Bprime_M800_2022EE,
    "DYMHT12002022EE":DYMHT12002022EE,
    "DYMHT2002022EE":DYMHT2002022EE,
    "DYMHT25002022EE":DYMHT25002022EE,
    "DYMHT4002022EE":DYMHT4002022EE,
    "DYMHT6002022EE":DYMHT6002022EE,
    "DYMHT8002022EE":DYMHT8002022EE,
    # "JetHTRun2022EEF":JetHTRun2022EEF,
    # "JetHTRun2022EEG":JetHTRun2022EEG,
    # "JetHTRun2022EEH":JetHTRun2022EEH,
    "QCDHT10002022EE":QCDHT10002022EE,
    "QCDHT15002022EE":QCDHT15002022EE,
    "QCDHT20002022EE":QCDHT20002022EE,
    "QCDHT2002022EE":QCDHT2002022EE,
    "QCDHT3002022EE":QCDHT3002022EE,
    "QCDHT5002022EE":QCDHT5002022EE,
    "QCDHT7002022EE":QCDHT7002022EE,
    "SingleElecRun2022EEF":SingleElecRun2022EEF,
    "SingleElecRun2022EEG":SingleElecRun2022EEG,
    "SingleElecRun2022EEH":SingleElecRun2022EEH,
    "SingleMuonRun2022EEF":SingleMuonRun2022EEF,
    "SingleMuonRun2022EEG":SingleMuonRun2022EEG,
    "SingleMuonRun2022EEH":SingleMuonRun2022EEH,
    "STs2022EE":STs2022EE,
    "STt2022EE":STt2022EE,
    "STtb2022EE":STtb2022EE,
    "STtW2022EE":STtW2022EE,
    "STtWb2022EE":STtWb2022EE,
    "TTHB2022EE":TTHB2022EE,
    "TTHnonB2022EE":TTHnonB2022EE,
    "TTMT10002022EE":TTMT10002022EE,
    "TTMT7002022EE":TTMT7002022EE,
    "TTTo2L2Nu2022EE":TTTo2L2Nu2022EE,
    "TTToHadronic2022EE":TTToHadronic2022EE,
    "TTToSemiLeptonic2022EE":TTToSemiLeptonic2022EE,
    "TTWl2022EE":TTWl2022EE,
    "TTWq2022EE":TTWq2022EE,
    "TTZM102022EE":TTZM102022EE,
    "TTZM1to102022EE":TTZM1to102022EE,
    "WJetsHT12002022EE":WJetsHT12002022EE,
    "WJetsHT2002022EE":WJetsHT2002022EE,
    "WJetsHT25002022EE":WJetsHT25002022EE,
    "WJetsHT4002022EE":WJetsHT4002022EE,
    "WJetsHT6002022EE":WJetsHT6002022EE,
    "WJetsHT8002022EE":WJetsHT8002022EE,
    "WW2022EE":WW2022EE,
    "WZ2022EE":WZ2022EE,
    "ZZ2022EE":ZZ2022EE,
}

samples_2023 = {
    "Bprime_M1000_2023":Bprime_M1000_2023,
    "Bprime_M1200_2023":Bprime_M1200_2023,
    "Bprime_M1300_2023":Bprime_M1300_2023,
    "Bprime_M1400_2023":Bprime_M1400_2023,
    "Bprime_M1500_2023":Bprime_M1500_2023,
    "Bprime_M1600_2023":Bprime_M1600_2023,
    "Bprime_M1700_2023":Bprime_M1700_2023,
    "Bprime_M1800_2023":Bprime_M1800_2023,
    "Bprime_M2000_2023":Bprime_M2000_2023,
    "Bprime_M2200_2023":Bprime_M2200_2023,
    "Bprime_M800_2023":Bprime_M800_2023,
    "DYMHT12002023":DYMHT12002023,
    "DYMHT2002023":DYMHT2002023,
    "DYMHT25002023":DYMHT25002023,
    "DYMHT4002023":DYMHT4002023,
    "DYMHT6002023":DYMHT6002023,
    "DYMHT8002023":DYMHT8002023,
    # "JetHTRun2023B":JetHTRun2023B,
    # "JetHTRun2023C":JetHTRun2023C,
    # "JetHTRun2023D":JetHTRun2023D,
    # "JetHTRun2023E":JetHTRun2023E,
    # "JetHTRun2023F":JetHTRun2023F,
    "QCDHT10002023":QCDHT10002023,
    "QCDHT15002023":QCDHT15002023,
    "QCDHT20002023":QCDHT20002023,
    "QCDHT2002023":QCDHT2002023,
    "QCDHT3002023":QCDHT3002023,
    "QCDHT5002023":QCDHT5002023,
    "QCDHT7002023":QCDHT7002023,
    "SingleElecRun2023B":SingleElecRun2023B,
    "SingleElecRun2023C":SingleElecRun2023C,
    "SingleElecRun2023D":SingleElecRun2023D,
    "SingleElecRun2023E":SingleElecRun2023E,
    "SingleElecRun2023F":SingleElecRun2023F,
    "SingleMuonRun2023B":SingleMuonRun2023B,
    "SingleMuonRun2023C":SingleMuonRun2023C,
    "SingleMuonRun2023D":SingleMuonRun2023D,
    "SingleMuonRun2023E":SingleMuonRun2023E,
    "SingleMuonRun2023F":SingleMuonRun2023F,
    "STs2023":STs2023,
    "STt2023":STt2023,
    "STtb2023":STtb2023,
    "STtW2023":STtW2023,
    "STtWb2023":STtWb2023,
    "TTHB2023":TTHB2023,
    "TTHnonB2023":TTHnonB2023,
    "TTMT10002023":TTMT10002023,
    "TTMT7002023":TTMT7002023,
    "TTTo2L2Nu2023":TTTo2L2Nu2023,
    "TTToHadronic2023":TTToHadronic2023,
    "TTToSemiLeptonic2023":TTToSemiLeptonic2023,
    "TTWl2023":TTWl2023,
    "TTWq2023":TTWq2023,
    "TTZM102023":TTZM102023,
    "TTZM1to102023":TTZM1to102023,
    "WJetsHT12002023":WJetsHT12002023,
    "WJetsHT2002023":WJetsHT2002023,
    "WJetsHT25002023":WJetsHT25002023,
    "WJetsHT4002023":WJetsHT4002023,
    "WJetsHT6002023":WJetsHT6002023,
    "WJetsHT8002023":WJetsHT8002023,
    "WW2023":WW2023,
    "WZ2023":WZ2023,
    "ZZ2023":ZZ2023,
}

samples_2023BPix = {
    # "JetHTRun2023BPixA":JetHTRun2023BPixA,
    # "JetHTRun2023BPixB":JetHTRun2023BPixB,
    # "JetHTRun2023BPixC":JetHTRun2023BPixC,
    # "JetHTRun2023BPixD":JetHTRun2023BPixD,
    "SingleElecRun2023BPixA":SingleElecRun2023BPixA,
    "SingleElecRun2023BPixB":SingleElecRun2023BPixB,
    "SingleElecRun2023BPixC":SingleElecRun2023BPixC,
    "SingleElecRun2023BPixD":SingleElecRun2023BPixD,
    "SingleMuonRun2023BPixA":SingleMuonRun2023BPixA,
    "SingleMuonRun2023BPixB":SingleMuonRun2023BPixB,
    "SingleMuonRun2023BPixC":SingleMuonRun2023BPixC,
    "SingleMuonRun2023BPixD":SingleMuonRun2023BPixD,
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1200_2023BPix":Bprime_M1200_2023BPix,
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1400_2023BPix":Bprime_M1400_2023BPix,
    "Bprime_M1500_2023BPix":Bprime_M1500_2023BPix,
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M1700_2023BPix":Bprime_M1700_2023BPix,
    "Bprime_M1800_2023BPix":Bprime_M1800_2023BPix,
    "Bprime_M2000_2023BPix":Bprime_M2000_2023BPix,
    "Bprime_M2200_2023BPix":Bprime_M2200_2023BPix,
    "Bprime_M800_2023BPix":Bprime_M800_2023BPix,
    "DYMHT12002023BPix":DYMHT12002023BPix,
    "DYMHT2002023BPix":DYMHT2002023BPix,
    "DYMHT25002023BPix":DYMHT25002023BPix,
    "DYMHT4002023BPix":DYMHT4002023BPix,
    "DYMHT6002023BPix":DYMHT6002023BPix,
    "DYMHT8002023BPix":DYMHT8002023BPix,
    "QCDHT10002023BPix":QCDHT10002023BPix,
    "QCDHT15002023BPix":QCDHT15002023BPix,
    "QCDHT20002023BPix":QCDHT20002023BPix,
    "QCDHT2002023BPix":QCDHT2002023BPix,
    "QCDHT3002023BPix":QCDHT3002023BPix,
    "QCDHT5002023BPix":QCDHT5002023BPix,
    "QCDHT7002023BPix":QCDHT7002023BPix,
    "STs2023BPix":STs2023BPix,
    "STt2023BPix":STt2023BPix,
    "STtb2023BPix":STtb2023BPix,
    "STtW2023BPix":STtW2023BPix,
    "STtWb2023BPix":STtWb2023BPix,
    "TTHB2023BPix":TTHB2023BPix,
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTMT10002023BPix":TTMT10002023BPix,
    "TTMT7002023BPix":TTMT7002023BPix,
    "TTTo2L2Nu2023BPix":TTTo2L2Nu2023BPix,
    "TTToHadronic2023BPix":TTToHadronic2023BPix,
    "TTToSemiLeptonic2023BPix":TTToSemiLeptonic2023BPix,
    "TTWl2023BPix":TTWl2023BPix,
    "TTWq2023BPix":TTWq2023BPix,
    "TTZM102023BPix":TTZM102023BPix,
    "TTZM1to102023BPix":TTZM1to102023BPix,
    "WJetsHT12002023BPix":WJetsHT12002023BPix,
    "WJetsHT2002023BPix":WJetsHT2002023BPix,
    "WJetsHT25002023BPix":WJetsHT25002023BPix,
    "WJetsHT4002023BPix":WJetsHT4002023BPix,
    "WJetsHT6002023BPix":WJetsHT6002023BPix,
    "WJetsHT8002023BPix":WJetsHT8002023BPix,
    "WW2023BPix":WW2023BPix,
    "WZ2023BPix":WZ2023BPix,
    "ZZ2023BPix":ZZ2023BPix,
}


samples_BPrime = {
    #"Bprime_M800_2023BPix":Bprime_M800_2023BPix,
    "Bprime_M1400_2023BPix":Bprime_M1400_2023BPix,
    #"Bprime_M2000_2023BPix":Bprime_M2000_2023BPix,
}

samples_WJets = {
    "WJetsHT12002023BPix":WJetsHT12002023BPix,
    "WJetsHT1200ext2023BPix":WJetsHT1200ext2023BPix,
    "WJetsHT4002023BPix":WJetsHT4002023BPix,
    "WJetsHT400ext2023BPix":WJetsHT400ext2023BPix,
    "WJetsHT6002023BPix":WJetsHT6002023BPix,
    "WJetsHT600ext2023BPix":WJetsHT600ext2023BPix,
    "WJetsHT8002023":WJetsHT8002023,
    "WJetsHT800ext2023BPix":WJetsHT800ext2023BPix,
}
samples_redo = {
    "SingleElecRun2023BPixB":SingleElecRun2023BPixB,
    "SingleElecRun2023BPixC":SingleElecRun2023BPixC,
    #"SingleElecRun2023BPixD":SingleElecRun2023BPixD,
    #"TTMT10002022":TTMT10002022,
    #"TTMT7002022":TTMT7002022,
}
