from ROOT import *
from array import array
import sys, os, pwd, subprocess
import optparse, shlex, re
import time
from time import gmtime, strftime
import math
import pickle
dirMC_16 = '/eos/user/d/daebi/2016_data_fullSF/'
dirData_16 = '/eos/user/d/daebi/2016_data_fullSF/data/'
SamplesMC_16 = [
'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1.root',
'DYToLL_0J_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'DYToLL_1J_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'DYToLL_2J_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'DYToLL_2J_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluHToBB_M125_13TeV_amcatnloFXFX_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'GluGluHToBB_M125_13TeV_amcatnloFXFX_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1.root',
'GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluHToTauTau_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluHToWWToLNuQQ_M125_13TeV_powheg_JHUGenV628_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-750_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-700_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
#'GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2.root', #File is empty ):
'GluGluToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-1000_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-260_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-270_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-300_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-350_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-450_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-500_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-550_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-600_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-650_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-750_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-800_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2VTo2L2Nu_M-900_narrow_13TeV-madgraph-v2/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
#'GluGluToRadionToHHTo2B2WToLNu2J_M-650_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root', #Sample doesn't exist
'GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_13TeV-madgraph/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'HZJ_HToWW_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ST_s-channel_4f_leptonDecays_13TeV_PSweights-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ST_t-channel_antitop_4f_inclusiveDecays_13TeV_PSweights-powhegV2-madspin/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2.root',
'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'ST_tWll_5f_LO_13TeV-MadGraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'TGJets_leptonDecays_13TeV_amcatnlo_madspin_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'THQ_ctcvcp_HIncl_M125_TuneCP5_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext3-v1.root',
'ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1.root',
'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/out_RunIISummer16NanoAODv7-Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1.root',
'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext3-v1.root',
'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'tZq_ll_4f_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'tZq_ll_4f_PSweights_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFHToGG_M125_13TeV_amcatnlo_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'VBFHToGG_M125_13TeV_amcatnlo_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1.root',
'VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFHToTauTau_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFHToWWToLNuQQ_M125_13TeV_powheg_JHUGenV628_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-1200_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToBulkGravitonToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VBFToRadionToHHTo2B2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1.root',
'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WWTo2L2Nu_13TeV-powheg/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WWTo2L2Nu_DoubleScattering_13TeV-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WWToLNuQQ_13TeV-powheg/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1.root',
'WWToLNuQQ_13TeV-powheg/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ZHToTauTau_M125_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ZZTo4L_13TeV_powheg_pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root',
'ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/out_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1.root'
]
SamplesData_16 = [
#'MuonEG/MuonEG_UL_2016.root',
#'SingleElectron/SingleElectron_UL_2016.root',
#'SingleMuon/SingleMuon_UL_2016.root',
#'DoubleEG/DoubleEG_UL_2016.root',
#'DoubleMuon/DoubleMuon_UL_2016.root',
'SingleLepton_UL_2016_NoDuplicates.root',
'DoubleLepton_UL_2016_NoDuplicates.root'
]
###################################################### 
#/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17/NANOAODSIM
RootFile = {}
Single_Tree = {} 
Double_Tree = {}
nEvents = {} 
xsection = {}

personInfo = pickle.load(open("../dataset/dataset_names/2016/2016_Datasets.pkl", "rb"))
# define function for processing the external os commands
def LoadData():
    # 80X MC
    for i in range(0,len(SamplesMC_16)):
        sample = SamplesMC_16[i].split('/')[0]
        dataset_part2_temp = ((SamplesMC_16[i].split('/')[1]).strip('.root')).split('_')[1:]
        dataset_part2 = "_".join(dataset_part2_temp)
        dataset_part3 = "NANOAODSIM"
        dataset_name = "/"+sample+"/"+dataset_part2+"/"+dataset_part3

        if sample in nEvents:
            print("Already found sample ", sample, " extending!!!")
            nEvents[sample] += int(personInfo['nevents'][dataset_name])
            if xsection[sample] != personInfo['xs'][dataset_name]:
                print("BAD XSEC FOR THIS SAMPLE, EXTENSION DOESN'T MATCH!")
        else:
            print("New sample ", sample)
            Single_Tree[sample] = TChain("Single_Tree")
            Double_Tree[sample] = TChain("Double_Tree")
            nEvents[sample] = int(personInfo['nevents'][dataset_name])
            xsection[sample] = personInfo['xs'][dataset_name]

        Single_Tree[sample].Add(dirMC_16+'/'+SamplesMC_16[i])
        Double_Tree[sample].Add(dirMC_16+'/'+SamplesMC_16[i])

        if (not Single_Tree[sample]): print(sample+' has no Single tree')
        else:
            print(sample,"nevents",nEvents[sample],"xsection",xsection[sample])
        if (not Double_Tree[sample]): print(sample+' has no Double tree')
        else:
            print(sample,"nevents",nEvents[sample],"xsection",xsection[sample])

    for i in range(0,len(SamplesData_16)):

        sample = SamplesData_16[i].split('/')[0]
        RootFile[sample] = TFile(dirData_16+'/'+SamplesData_16[i],"READ")
        if ('Single' in sample):
            Single_Tree[sample]  = RootFile[sample].Get("Single_Tree")
            if (not Single_Tree[sample]): print(sample+' has no Single tree')
            else: 
                print(sample,"nevents: ", Single_Tree[sample].GetEntries())
        else:
            Double_Tree[sample]  = RootFile[sample].Get("Double_Tree")        
            if (not Double_Tree[sample]): print(sample+' has no Double tree')
            else:
                print(sample,"nevents: ", Double_Tree[sample].GetEntries())
#LoadData()
