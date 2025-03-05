# Neuroimaging Software

This directory contains detailed information about neuroimaging software packages, including installation guides, usage examples, and comparison of features.

## Major Neuroimaging Packages Comparison

| Software | Primary Focus | Programming Language | License | GUI | Command Line | Works on Linux | Works on Mac | Works on Windows |
|----------|---------------|----------------------|---------|-----|--------------|----------------|--------------|------------------|
| FSL | General MRI/fMRI/DWI | C++/Python | FSL License | ✓ | ✓ | ✓ | ✓ | Via VM Only |
| SPM | General MRI/fMRI | MATLAB | GPL | ✓ | ✓ | Via MATLAB | Via MATLAB | Via MATLAB |
| AFNI | General MRI/fMRI | C/Python/R | Open Source | ✓ | ✓ | ✓ | ✓ | Via VM Only |
| FreeSurfer | Structural MRI | C/C++ | FreeSurfer License | ✓ | ✓ | ✓ | ✓ | Via VM Only |
| ANTs | Registration | C++ | Apache 2.0 | ✗ | ✓ | ✓ | ✓ | ✓ |
| fMRIPrep | fMRI Preprocessing | Python | Apache 2.0 | ✗ | ✓ | ✓ | ✓ | ✓ |
| MRtrix3 | Diffusion MRI | C++/Python | MPL 2.0 | ✓ | ✓ | ✓ | ✓ | ✓ |
| Nilearn | Machine Learning for Neuroimaging | Python | BSD 3-Clause | ✗ | ✓ | ✓ | ✓ | ✓ |

## Installation Guides

### FSL

FSL (FMRIB Software Library) is a comprehensive library of analysis tools for brain imaging data.

#### Prerequisites

- Linux or macOS (Windows users need to use a virtual machine)
- At least 16GB of RAM recommended

#### Installation Steps

1. Download the installer from [FSL website](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation)
2. Run the installer script:

```bash
python3 fslinstaller.py
```

3. Follow the installation prompts

#### Docker Installation

```bash
docker pull fslaccesshub/fsl:latest
docker run -it fslaccesshub/fsl
```

#### Troubleshooting

- **Issue**: FSL commands not found
  - **Solution**: Make sure FSL is in your PATH by adding `FSLDIR` to your `.bashrc` or `.zshrc`
- **Issue**: FSLeyes fails to start
  - **Solution**: Check Python dependencies with `pip install -U wxpython matplotlib`

### SPM

SPM (Statistical Parametric Mapping) is a software package designed for the analysis of brain imaging data sequences.

#### SPM Prerequisites

- MATLAB (version 2014b or later recommended)
- MATLAB Image Processing Toolbox

#### SPM Installation

1. Download SPM from the [SPM website](https://www.fil.ion.ucl.ac.uk/spm/software/download/)
2. Unzip the package into a directory of your choice
3. Add SPM to MATLAB's path:

```matlab
addpath('/path/to/spm12')
savepath
```

4. Start SPM in MATLAB:

```matlab
spm
```

#### SPM Troubleshooting

- **Issue**: Missing MEX files
  - **Solution**: Run `spm_make_standalone` in MATLAB to compile MEX files
- **Issue**: Compatibility with newer MATLAB versions
  - **Solution**: Check the SPM mailing list for patches for your MATLAB version

## Usage Examples

### Basic fMRI Analysis with FSL

```bash
# Convert DICOM to NIFTI
dcm2niix -z y -o output_dir input_dir

# Brain extraction
bet functional.nii.gz functional_brain.nii.gz -F

# Motion correction
mcflirt -in functional_brain.nii.gz -out functional_mc -plots

# Spatial smoothing
susan functional_mc.nii.gz 510 2 3 1 1 functional_smooth.nii.gz

# FEAT analysis
feat design.fsf
```

### Cortical Surface Reconstruction with FreeSurfer

```bash
# Full reconstruction
recon-all -i T1.nii.gz -s subject_name -all

# Viewing results
freeview -v mri/T1.mgz -f surf/lh.pial:edgecolor=red surf/rh.pial:edgecolor=red
```

### Functional Connectivity Analysis with Nilearn

```python
import nilearn as nl
from nilearn import datasets, plotting, connectome
import matplotlib.pyplot as plt

# Load example dataset
adhd_dataset = datasets.fetch_adhd(n_subjects=1)
func_file = adhd_dataset.func[0]
confounds_file = adhd_dataset.confounds[0]
confounds = nl.image.load_img(confounds_file)

# Extract time series from atlas
atlas = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
masker = nl.input_data.NiftiLabelsMasker(labels_img=atlas.maps, standardize=True)
time_series = masker.fit_transform(func_file, confounds=confounds)

# Compute correlation matrix
correlation_matrix = connectome.ConnectivityMeasure(kind='correlation').fit_transform([time_series])[0]

# Plot correlation matrix
plt.figure(figsize=(10, 10))
plotting.plot_matrix(correlation_matrix, figure=plt.gcf(), labels=atlas.labels, colorbar=True)
plt.title('Functional Connectivity Matrix')
plt.show()
```

## Current Research and Development

### Major Updates in 2023-2024

- **FSL 6.0**: Enhanced GPU support for PALM permutation testing
- **SPM12 r7771**: Enhanced compatibility with Matlab 2022a and 2022b
- **fMRIPrep 23.1.0**: Now supports longitudinal analysis
- **FreeSurfer 7.4.1**: Improved surface registration and cortical parcellation algorithms
- **ANTs 2.5.0**: Improved registration algorithms and new deep learning components

### Emerging Tools and Techniques

- **QSIPrep**: Robust preprocessing for q-space imaging
- **Nilearn 0.10.0**: New and improved visualization capabilities
- **TemplateFlow**: Framework for multi-template neuroimaging
- **Brainiak**: Advanced fMRI analysis with ML integration
- **NeuroDesk**: Containerized neuroimaging applications

## Learning Resources

### Tutorials and Workshops

- [**FSL Course**](https://fsl.fmrib.ox.ac.uk/fslcourse/): Official FSL training materials
- [**SPM Course**](https://www.fil.ion.ucl.ac.uk/spm/course/): Official SPM course materials
- [**AFNI Boot Camp**](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/educational/bootcamp_recordings.html): Video recordings of AFNI trainings
- [**FreeSurfer Tutorial**](https://surfer.nmr.mgh.harvard.edu/fswiki/Tutorials): Official FreeSurfer tutorials
- [**Nilearn Examples**](https://nilearn.github.io/stable/auto_examples/index.html): Examples gallery for Nilearn

### Books and Publications

- "Handbook of Functional MRI Data Analysis" by Poldrack, Mumford, and Nichols
- "Statistical Parametric Mapping: The Analysis of Functional Brain Images" by Friston, Ashburner, Kiebel, Nichols, and Penny
- "Introduction to Neuroimaging Analysis" by Jenkinson and Chappell

## Community Support

### Mailing Lists and Forums

- [FSL Jiscmail](https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=FSL)
- [SPM Jiscmail](https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=SPM)
- [AFNI Message Board](https://afni.nimh.nih.gov/afni/community/board/)
- [FreeSurfer Mailing List](https://mail.nmr.mgh.harvard.edu/mailman/listinfo/freesurfer)
- [Neurostars](https://neurostars.org/) - Q&A forum for neuroimaging

### Conferences and Events

- **Organization for Human Brain Mapping (OHBM)** - Annual meeting
- **Society for Neuroscience (SfN)** - Annual meeting
- **Brainhack** - Community-organized hackathons
- **INCF Neuroinformatics** - Annual congress
