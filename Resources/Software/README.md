# Core Software README

# Neuroscience Software Resources

This directory contains a curated collection of software tools, repositories, and platforms relevant to cognitive neuroscience research. These resources are organized by category to help researchers find the most appropriate tools for their needs.

## Neuroimaging Software

### General Neuroimaging Packages

- [**FSL**](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/) - Comprehensive library of analysis tools for FMRI, MRI and DTI brain imaging data.
- [**SPM**](https://www.fil.ion.ucl.ac.uk/spm/) - Software package designed for the analysis of brain imaging data sequences.
- [**AFNI**](https://afni.nimh.nih.gov/) - A set of C programs for processing, analyzing, and displaying functional MRI data.
- [**FreeSurfer**](https://surfer.nmr.mgh.harvard.edu/) - Software package for processing and analyzing human brain MRI images.
- [**ANTs**](https://github.com/ANTsX/ANTs) - Advanced Normalization Tools for brain image registration.
- [**NiBabel**](https://nipy.org/nibabel/) - Python package for access to neuroimaging file formats.
- [**Nipype**](https://nipype.readthedocs.io/) - Python-based neuroimaging data analysis framework.

### fMRI-Specific Tools

- [**fMRIPrep**](https://fmriprep.org/) - A robust preprocessing pipeline for functional MRI data.
- [**XCP-D**](https://github.com/PennLINC/xcp_d) - XCP-D derivatives processor for fMRI data analysis.
- [**CONN**](https://web.conn-toolbox.org/) - MATLAB-based cross-platform software for computation, display, and analysis of functional connectivity in fMRI.
- [**tedana**](https://github.com/ME-ICA/tedana) - Multi-echo fMRI combination and denoising.

### EEG/MEG Analysis

- [**MNE-Python**](https://mne.tools/stable/index.html) - Python package for processing electrophysiology data.
- [**FieldTrip**](https://www.fieldtriptoolbox.org/) - MATLAB toolbox for EEG, MEG, and iEEG analysis.
- [**EEGLAB**](https://sccn.ucsd.edu/eeglab/index.php) - Interactive MATLAB toolbox for processing continuous and event-related EEG data.
- [**Brainstorm**](https://neuroimage.usc.edu/brainstorm/) - Application for MEG/EEG/fNIRS analysis with a rich user interface.

### PET/SPECT Analysis

- [**PMOD**](https://www.pmod.com/) - Software for quantitative PET/SPECT/MRI analysis.
- [**PETPVC**](https://github.com/UCL/PETPVC) - Toolbox for PET partial volume correction.
- [**PETSurfer**](https://surfer.nmr.mgh.harvard.edu/fswiki/PetSurfer) - PET analysis tools integrated with FreeSurfer.

### Diffusion MRI Tools

- [**MRtrix3**](https://www.mrtrix.org/) - Advanced tools for the analysis of diffusion MRI data.
- [**DIPY**](https://dipy.org/) - Python package for diffusion MRI analysis.
- [**DSI Studio**](http://dsi-studio.labsolver.org/) - Tool for diffusion MRI analysis and tractography.
- [**TrackVis**](http://trackvis.org/) - Free software for diffusion MRI fiber track visualization and analysis.

## Neural Data Analysis

### Statistical Analysis

- [**R**](https://www.r-project.org/) - Programming language for statistical computing and graphics.
- [**Stan**](https://mc-stan.org/) - State-of-the-art platform for Bayesian modeling and inference.
- [**JASP**](https://jasp-stats.org/) - Free and open-source software for statistical analysis.
- [**PsychoPy**](https://www.psychopy.org/) - Psychology software in Python for creating experiments.
- [**jamovi**](https://www.jamovi.org/) - Free and open statistical software built on R.

### Machine Learning Frameworks

- [**scikit-learn**](https://scikit-learn.org/) - Python module for machine learning.
- [**TensorFlow**](https://www.tensorflow.org/) - Platform for machine learning.
- [**PyTorch**](https://pytorch.org/) - Open source machine learning framework.
- [**Keras**](https://keras.io/) - Deep learning API running on top of TensorFlow.
- [**Nilearn**](https://nilearn.github.io/) - Machine learning for neuroimaging in Python.
- [**PyMVPA**](https://www.pymvpa.org/) - MultiVariate Pattern Analysis in Python.
- [**DeepLabCut**](http://www.mackenziemathislab.org/deeplabcut) - Tool for markerless pose estimation of animals.

### Computational Neuroscience

- [**NEURON**](https://neuron.yale.edu/neuron/) - Simulation environment for models of neurons and networks.
- [**Brian2**](https://briansimulator.org/) - Python package for simulating neural networks.
- [**NEST**](https://www.nest-simulator.org/) - Simulator for spiking neural network models.
- [**BluePyOpt**](https://github.com/BlueBrain/BluePyOpt) - Python package for neuron model parameter optimization.
- [**NetPyNE**](http://netpyne.org/) - Python package for network modeling using NEURON.

## Visualization Tools

### Brain Visualization

- [**BrainNet Viewer**](https://www.nitrc.org/projects/bnv/) - Open source package for visualizing brain networks.
- [**Connectome Workbench**](https://www.humanconnectome.org/software/connectome-workbench) - Set of visualization and discovery tools.
- [**3D Slicer**](https://www.slicer.org/) - Open source software for visualization and image analysis.
- [**MRIcroGL**](https://www.nitrc.org/projects/mricrogl/) - Program for visualizing medical images.
- [**ITK-SNAP**](http://www.itksnap.org/) - Tool for segmentation of 3D medical images.
- [**Pycortex**](https://github.com/gallantlab/pycortex) - Python-based visualization of cortical activity.

### Data Visualization

- [**Matplotlib**](https://matplotlib.org/) - Plotting library for Python.
- [**Seaborn**](https://seaborn.pydata.org/) - Statistical data visualization for Python.
- [**Plotly**](https://plotly.com/python/) - Interactive graphing library for Python.
- [**ggplot2**](https://ggplot2.tidyverse.org/) - System for declaratively creating graphics in R.
- [**D3.js**](https://d3js.org/) - JavaScript library for visualizing data.

## Data Management

### BIDS Tools

- [**BIDS Validator**](https://github.com/bids-standard/bids-validator) - Tool for validating BIDS datasets.
- [**PyBIDS**](https://github.com/bids-standard/pybids) - Python tools for working with BIDS datasets.
- [**BIDS Apps**](https://bids-apps.neuroimaging.io/) - Portable neuroimaging pipelines that understand BIDS datasets.
- [**DcmToNifti**](https://github.com/rordenlab/dcm2niix) - DICOM to NIfTI converter.

### Data Sharing Platforms

- [**OpenNeuro**](https://openneuro.org/) - Platform for sharing neuroimaging data.
- [**NITRC**](https://www.nitrc.org/) - Neuroimaging Informatics Tools and Resources Clearinghouse.
- [**XNAT**](https://www.xnat.org/) - Open source imaging informatics platform.
- [**DataLad**](https://www.datalad.org/) - A data management solution built on git and git-annex.
- [**Brainlife.io**](https://brainlife.io/) - Platform for sharing and analyzing neuroscience data.
- [**LORIS**](https://loris.ca/) - Web-based data management system for neuroimaging research.

## Online Communities and Forums

- [**Neurostars**](https://neurostars.org/) - Question and answer site for neuroscience researchers.
- [**NeuroImaging Tools & Resources Collaboratory**](https://www.nitrc.org/forum/) - Forum for neuroimaging tools.
- [**BrainHack**](https://brainhack.org/) - Community-driven collaboration for neuroscience projects.
- [**OHBM**](https://www.humanbrainmapping.org/) - Organization for Human Brain Mapping community.
- [**MNE Forum**](https://mne.discourse.group/) - Community forum for MNE-Python users.
- [**FSL Jiscmail**](https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=fsl) - FSL users mailing list.
- [**SPM Jiscmail**](https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=spm) - SPM users mailing list.

## Educational Resources

### Courses and Tutorials

- [**Neuromatch Academy**](https://neuromatch.io/academy/) - Online summer school in computational neuroscience.
- [**Andy's Brain Book**](https://andysbrainbook.readthedocs.io/) - Comprehensive guides for fMRI analysis.
- [**Mind Boggle**](https://mindboggle.info/) - Software for automated neuroimage analysis.
- [**Neuroimaging Informatics Technology Initiative**](https://nifti.nimh.nih.gov/) - Information about the NIfTI standard.
- [**Nipype Beginner's Guide**](https://miykael.github.io/nipype_tutorial/) - Tutorial for Nipype.
- [**The Turing Way**](https://the-turing-way.netlify.app/) - Guide to reproducible data science.
- [**NITRC Training**](https://www.nitrc.org/project/list_training.php) - Training resources for neuroimaging tools.

### Code Repositories and Package Indexes

- [**GitHub**](https://github.com/) - Platform for version control and collaboration.
- [**GitLab**](https://gitlab.com/) - Web-based DevOps platform.
- [**Open Science Framework**](https://osf.io/) - Platform for supporting reproducible research.
- [**PyPI**](https://pypi.org/) - Python Package Index for Python software.
- [**CRAN**](https://cran.r-project.org/) - Comprehensive R Archive Network for R packages.
- [**NeuroDebian**](https://neuro.debian.net/) - Packaging of neuroscience research software for Debian and Ubuntu.

## Contributing

We welcome contributions to this directory! If you have suggestions for additional software resources or updates to existing information, please:

1. Fork the repository
2. Add your suggested changes
3. Submit a pull request with a clear description of your additions or modifications

## License

The resources listed here are subject to their own respective licenses. Please refer to each resource's website for specific licensing information.
