### in  nanoAOD_processing.py

from bbWWProcessor import EventProcess
import awkward as ak
import os
import uproot

import time
startTime = time.time()

import argparse

parser = argparse.ArgumentParser(description='Run3 analysis for H->hh->bbWW')
parser.add_argument("-i", "--inputFileList", dest="infile_list", type=str, nargs='+', default=[], help="input file name. [Default: [] ]")
parser.add_argument("-o", "--outputFile", dest="outfile", type=str, default="out.root", help="output file name. [Default: out.root]")
parser.add_argument("-ry", "--runyear", dest="Runyear", type=int, default=2022, help="Runyear of the file. [Default: 2022]")
parser.add_argument("-MC", dest="isMC", type=int, default=0, help="Is the file MC. [Default: 0]")
parser.add_argument("-t", "--truth", dest="dnn_truth_value", type=int, default="8", help="DNN Truth value, HH:0 TTbar:1 ST:2 DY:3 H:4 TTbarV(X):5 VV(V):6 Other:7 Data:8. [Default: 8 (Data)]")
parser.add_argument("-d", "--debug", dest="debug", type=int, default="0", help="Debug. [Default: 0 (False)]")
parser.add_argument("-XS", dest="XS", type=float, default=1.0, help="Cross Section. [Default: 1.0]")
parser.add_argument("-SF", dest="SF", type=int, default=0, help="Add Scale Factors. [Default: 0 (False)]")
args, unknown = parser.parse_known_args()

flist = args.infile_list
outname = args.outfile
outfile = uproot.recreate(outname)

args = parser.parse_args()

if len(flist) == 0:
    raise Exception("No input files, use python3 run_bbWW_processing.py -i InputFileList -o OutputFile")

#index = 0
#fname_list = ["run2022C_data_doublemuon_nanoaod.root"]
#fname = fname_list[index]

#Prepare for DNN training, give truth values
#dnn_truth_value = 8
dnn_truth_value = args.dnn_truth_value
#value list example HH:0 TTbar:1 ST:2 DY:3 H:4 TTbarV(X):5 VV(V):6 Other:7 Data:8

debug = args.debug

Runyear = args.Runyear
isMC = args.isMC
XS = args.XS
doSF = args.SF
do_genMatch = True
DYEstimation = True

print("Processing: ", flist)
print("Will save as: ", outname)
print("Args are = ", args)


for fname in flist:
    print("Starting file: ", fname)
    eventProcess = EventProcess(fname, isMC, doSF, do_genMatch, Runyear, dnn_truth_value, XS, debug, DYEstimation)
    if eventProcess.skip_file: continue

    if doSF:
        if isMC:
            eventProcess.add_scale_factors()
            print("Scale Factors in seconds: " + str((time.time() - startTime)))
            eventProcess.btag_SF()
            print("BTag SF in seconds: " + str((time.time() - startTime)))
        eventProcess.jet_corrector()
        print("Jet Corrector in seconds: " + str((time.time() - startTime)))
        eventProcess.met_corrector()
        print("MET Corrector in seconds: " + str((time.time() - startTime)))

    if do_genMatch:
        eventProcess.single_lepton_genpart()
        eventProcess.double_lepton_genpart()
        eventProcess.recoJet_to_genJet()
        eventProcess.recoLep_to_genLep()
        eventProcess.recoMET_to_genMET()
        print('GenParts in seconds: ' + str((time.time() - startTime)))

    eventProcess.all_obj_selection()
    print('Object Selection in seconds: ' + str((time.time() - startTime)))
    if debug: eventProcess.print_object_selection()
    eventProcess.single_lepton_category()
    eventProcess.double_lepton_category()
    print('Categories in seconds: ' + str((time.time() - startTime)))
    if debug: eventProcess.print_event_selection()


    eventProcess.update_outfile(outfile)

    print('Updated in seconds: ' + str((time.time() - startTime)))
    print('Filename = ', outname)

print("Finished processing all files!")
