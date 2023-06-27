#!/bin/bash

hostname

# Take in Input Arguments
infilename=${1}  # Filename is a really long string
outputDir=${2}
testnum=${3}

# Print out Input Arguments
echo "filename: ${infilename}"
echo "output dir: ${outputDir}"
echo "testnum: ${testnum}"

# Setup Environment
scratch=${PWD}  
macroDir=${PWD}
source /cvmfs/cms.cern.ch/cmsset_default.sh
scramv1 project CMSSW CMSSW_11_0_0
cd CMSSW_11_0_0
cmsenv

# Unpack the tar file
echo "unpacking tar"
tar -xf ${scratch}/rdfjobs.tar
rm ${scratch}/rdfjobs.tar

eval `scramv1 runtime -sh`
cd src/vlq-BtoTW-RDF/

export PATH=$PATH:$macroDir

# Run analyzer_RDF files through two C files
echo "Running RDF:"
root -l -b -q runRDF.C\(\"${testnum}\",\"${infilename}\"\) 

# Viewing ROOT Files
echo "ROOT Files:"
ls -l *${testnum}*.root

# Remove our copy of the files to clean up
echo "Removing presel files:"
rm *preselTree*.root

# Copy Output to EOS

echo "xrdcp output for condor"
for FILE in *${testnum}*.root
do
  echo "xrdcp -f ${FILE} root://cmseos.fnal.gov/${outputDir}/${FILE}"
  xrdcp -f ${FILE} root://cmseos.fnal.gov/${outputDir}/${FILE} 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done

echo "done"