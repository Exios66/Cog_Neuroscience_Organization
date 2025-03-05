"""
Comprehensive Neuroscience Workflow Example

This script demonstrates a full neuroscience workflow, including:
1. Organizing data according to BIDS standards
2. Setting up a basic neuroimaging analysis pipeline
3. Implementing multivariate pattern analysis (MVPA)
4. Building a computational neural model
5. Creating visualizations of brain data

Required packages:
- nilearn, nibabel, numpy, matplotlib
- scikit-learn, pandas
- brian2 (for neural modeling)
- pybids (for BIDS organization)
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Check if required packages are installed
try:
    import nilearn
    from nilearn import datasets, image, plotting, masking, decoding, surface
    import nibabel as nib
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    print("Core neuroimaging packages imported successfully!")
except ImportError as e:
    print(f"Error importing core packages: {e}")
    print("Install with: pip install nilearn nibabel scikit-learn pandas matplotlib")

# Additional imports with try-except to handle optional dependencies
try:
    import brian2
    has_brian2 = True
    print("Brian2 imported successfully for neural modeling!")
except ImportError:
    has_brian2 = False
    print("Brian2 not found. Neural modeling examples will be skipped.")
    print("Install with: pip install brian2")

try:
    from bids import BIDSLayout
    has_pybids = True
    print("PyBIDS imported successfully for BIDS management!")
except ImportError:
    has_pybids = False
    print("PyBIDS not found. BIDS organization examples will be skipped.")
    print("Install with: pip install pybids")

# Create a project directory structure
def create_project_structure():
    """Create a basic project directory structure."""
    print("\n--- PART 1: Creating Project Structure ---")
    base_dir = Path("./neuroscience_project")
    
    # Main directories
    dirs = [
        base_dir / "data" / "raw",
        base_dir / "data" / "bids",
        base_dir / "data" / "derivatives",
        base_dir / "code",
        base_dir / "results" / "figures",
    ]
    
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {d}")
    
    return base_dir

# Download sample data
def download_sample_data(base_dir):
    """Download sample fMRI data from nilearn."""
    print("\n--- PART 2: Downloading Sample Data ---")
    data_dir = base_dir / "data" / "raw"
    
    # Download Haxby 2001 dataset
    print("Downloading Haxby dataset (this may take a moment)...")
    haxby_dataset = datasets.fetch_haxby(data_dir=str(data_dir))
    print(f"Data downloaded to: {data_dir}")
    print(f"Subject ID: {haxby_dataset.subject}")
    
    # Get info about the dataset
    fmri_img = haxby_dataset.func[0]
    mask_img = haxby_dataset.mask
    print(f"fMRI dimensions: {nib.load(fmri_img).shape}")
    
    # Get labels and sessions
    labels = pd.read_csv(haxby_dataset.session_target[0], sep=" ")
    unique_labels = labels['labels'].unique()
    print(f"Task conditions: {unique_labels}")
    
    return haxby_dataset

# BIDS Organization
def organize_data_as_bids(base_dir, dataset):
    """Organize the downloaded data according to BIDS standards."""
    print("\n--- PART 3: Organizing Data in BIDS Format ---")
    
    if not has_pybids:
        print("PyBIDS not installed. Skipping BIDS organization.")
        return
    
    # In a real scenario, you would use a tool like dcm2bids or HeuDiConv
    # For this example, we'll manually create a simple BIDS structure
    bids_dir = base_dir / "data" / "bids"
    
    # Create BIDS directory structure
    subj_dir = bids_dir / "sub-01"
    func_dir = subj_dir / "func"
    anat_dir = subj_dir / "anat"
    func_dir.mkdir(parents=True, exist_ok=True)
    anat_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a dataset_description.json
    dataset_description = bids_dir / "dataset_description.json"
    with open(dataset_description, 'w') as f:
        f.write('{\n')
        f.write('  "Name": "Haxby 2001 Dataset",\n')
        f.write('  "BIDSVersion": "1.6.0",\n')
        f.write('  "DatasetType": "raw",\n')
        f.write('  "License": "CC0",\n')
        f.write('  "Authors": ["Haxby, J.V.", "Gobbini, M.I.", "Furey, M.L."]\n')
        f.write('}\n')
    
    # Copy the data
    # In a real scenario, you would convert DICOM to NIFTI and rename files
    # For simplicity, we'll just indicate the paths
    print(f"Created BIDS structure at: {bids_dir}")
    print("In a real scenario, you would use tools like dcm2bids or HeuDiConv")
    print("to convert DICOM to NIFTI and organize the data.")
    
    # Create a sample task JSON file
    task_json = func_dir / "sub-01_task-objectviewing_bold.json"
    with open(task_json, 'w') as f:
        f.write('{\n')
        f.write('  "TaskName": "object viewing",\n')
        f.write('  "RepetitionTime": 2.5,\n')
        f.write('  "EchoTime": 0.030,\n')
        f.write('  "FlipAngle": 90,\n')
        f.write('  "TaskDescription": "Subjects viewed images of different categories"\n')
        f.write('}\n')
    
    # Demonstrate BIDS validation (in a real scenario)
    print("\nBIDS Validation Command (run this in terminal):")
    print("bids-validator " + str(bids_dir))
    
    return bids_dir

# Preprocessing and Basic Analysis
def preprocess_data(base_dir, dataset):
    """Perform basic preprocessing on the fMRI data."""
    print("\n--- PART 4: Preprocessing fMRI Data ---")
    
    # In a real pipeline, you would use tools like fMRIPrep
    # For this example, we'll perform minimal preprocessing with nilearn
    
    # Load data
    fmri_img = dataset.func[0]
    mask_img = dataset.mask
    
    # Simple preprocessing
    print("Performing preprocessing...")
    # 1. Spatial smoothing
    fmri_img_smooth = image.smooth_img(fmri_img, fwhm=6)
    
    # 2. Masking
    masker = masking.NiftiMasker(
        mask_img=mask_img,
        standardize=True,
        detrend=True,
        high_pass=0.01,
        t_r=2.5,
        memory='nilearn_cache'
    )
    
    # Transform data to 2D matrix: timepoints × voxels
    fmri_masked = masker.fit_transform(fmri_img_smooth)
    print(f"Preprocessed data shape: {fmri_masked.shape}")
    
    # Save preprocessed data
    derivatives_dir = base_dir / "data" / "derivatives" / "preprocessed"
    derivatives_dir.mkdir(parents=True, exist_ok=True)
    
    # In a real pipeline, you would save the preprocessed data
    print(f"Preprocessed data prepared for analysis")
    
    return fmri_masked, masker

# MVPA Analysis
def perform_mvpa(dataset, fmri_masked):
    """Perform Multivariate Pattern Analysis."""
    print("\n--- PART 5: Multivariate Pattern Analysis (MVPA) ---")
    
    # Load experimental information
    labels = pd.read_csv(dataset.session_target[0], sep=" ")
    
    # Select relevant conditions (e.g., faces vs houses)
    condition_mask = labels['labels'].isin(['face', 'house'])
    X = fmri_masked[condition_mask]
    y = labels['labels'][condition_mask].values
    
    print(f"MVPA data shape: {X.shape}, with classes: {np.unique(y)}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Train SVM classifier
    print("Training SVM classifier...")
    clf = SVC(kernel='linear')
    clf.fit(X_train, y_train)
    
    # Test the classifier
    score = clf.score(X_test, y_test)
    print(f"Classification accuracy: {score:.2f}")
    
    # Get feature weights (important voxels)
    weights = clf.coef_[0]
    
    return weights, clf

# Visualization
def visualize_results(base_dir, dataset, masker, weights):
    """Create visualizations of brain data and results."""
    print("\n--- PART 6: Visualization ---")
    
    # Create figures directory
    fig_dir = base_dir / "results" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Visualize an fMRI volume
    print("Creating brain visualizations...")
    fmri_img = dataset.func[0]
    first_vol = image.index_img(fmri_img, 0)
    
    # Plot using nilearn
    plt.figure(figsize=(10, 6))
    plotting.plot_epi(first_vol, title='First fMRI Volume')
    plt.savefig(fig_dir / "fmri_volume.png")
    
    # 2. Create weight/importance map
    # Convert SVM weights back to 3D
    weight_img = masker.inverse_transform(weights)
    
    # Plot weight map
    plt.figure(figsize=(10, 6))
    plotting.plot_stat_map(
        weight_img,
        display_mode='z',
        cut_coords=5,
        title='SVM Weights: Face vs House'
    )
    plt.savefig(fig_dir / "svm_weights.png")
    
    # 3. Create a brain glass view
    plt.figure(figsize=(10, 8))
    display = plotting.plot_glass_brain(
        weight_img,
        display_mode='lyrz',
        plot_abs=False,
        colorbar=True,
        title='Face vs House Discrimination Pattern'
    )
    plt.savefig(fig_dir / "glass_brain.png")
    
    # 4. Create a surface plot
    print("Creating surface visualization...")
    fsaverage = datasets.fetch_surf_fsaverage()
    
    # Project the volume to the surface
    texture = surface.vol_to_surf(weight_img, fsaverage.pial_right)
    
    # Plot the projected results
    plt.figure(figsize=(10, 8))
    plotting.plot_surf_stat_map(
        fsaverage.infl_right,
        texture,
        hemi='right',
        view='lateral',
        colorbar=True,
        bg_map=fsaverage.sulc_right,
        threshold=0.5,
        title='Surface Projection: Face vs House'
    )
    plt.savefig(fig_dir / "surface_proj.png")
    
    print(f"Visualizations saved in: {fig_dir}")
    
    return fig_dir

# Neural Model (using Brian2)
def build_neural_model():
    """Build a computational neural model using Brian2."""
    print("\n--- PART 7: Computational Neural Modeling ---")
    
    if not has_brian2:
        print("Brian2 is not installed. Skipping neural modeling.")
        return None
    
    # Import necessary Brian2 components locally
    from brian2 import (
        NeuronGroup, StateMonitor, run, 
        ms, mV, nA, ufarad, siemens, umetre, cm, msiemens,
        volt, amp, second, Hz, exp
    )
    
    # Set up a simple Hodgkin-Huxley model
    print("Building Hodgkin-Huxley model...")
    
    # Start by building the HH model
    brian2.defaultclock.dt = 0.01*ms  # Simulation time step

    # HH model parameters
    area = 20000*umetre**2
    Cm = 1*ufarad*cm**-2 * area
    gl = 5e-5*siemens*cm**-2 * area
    El = -65*mV
    EK = -90*mV
    ENa = 50*mV
    g_na = 100*msiemens*cm**-2 * area
    g_kd = 30*msiemens*cm**-2 * area
    VT = -63*mV

    # HH model equations
    eqs = '''
    dv/dt = (gl*(El-v) + g_na*m**3*h*(ENa-v) + g_kd*n**4*(EK-v) + I)/Cm : volt
    dm/dt = alpha_m*(1-m)-beta_m*m : 1
    dn/dt = alpha_n*(1-n)-beta_n*n : 1
    dh/dt = alpha_h*(1-h)-beta_h*h : 1
    alpha_m = 0.32*(mV**-1)*(13*mV-v+VT)/
            (exp((13*mV-v+VT)/(4*mV))-1)/ms : Hz
    beta_m = 0.28*(mV**-1)*(v-VT-40*mV)/
            (exp((v-VT-40*mV)/(5*mV))-1)/ms : Hz
    alpha_h = 0.128*exp((17*mV-v+VT)/(18*mV))/ms : Hz
    beta_h = 4/(1+exp((40*mV-v+VT)/(5*mV)))/ms : Hz
    alpha_n = 0.032*(mV**-1)*(15*mV-v+VT)/
            (exp((15*mV-v+VT)/(5*mV))-1)/ms : Hz
    beta_n = 0.5*exp((10*mV-v+VT)/(40*mV))/ms : Hz
    I : amp
    '''

    # Create neuron group
    neurons = NeuronGroup(1, eqs, method='exponential_euler')
    
    # Set initial conditions
    neurons.v = -70*mV
    neurons.m = 0
    neurons.h = 1
    neurons.n = 0
    
    # Apply a current pulse
    neurons.I = 0.7*nA
    
    # Record the membrane potential
    trace = StateMonitor(neurons, 'v', record=0)
    
    # Run the simulation
    run(50*ms)
    neurons.I = 0*nA
    run(50*ms)
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(trace.t/ms, trace.v[0]/mV)
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane potential (mV)')
    plt.title('Hodgkin-Huxley Model: Action Potential')
    plt.grid(True)
    
    # Save the figure
    model_dir = Path("./neuroscience_project/results/figures")
    model_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(model_dir / "hh_model.png")
    
    print(f"Neural model simulation completed and saved")
    
    return trace

# Main function to run the entire workflow
def main():
    """Execute the complete neuroscience workflow."""
    print("=== COGNITIVE NEUROSCIENCE WORKFLOW DEMONSTRATION ===")
    
    # 1. Create project structure
    base_dir = create_project_structure()
    
    # 2. Download sample data
    dataset = download_sample_data(base_dir)
    
    # 3. Organize data as BIDS
    bids_dir = organize_data_as_bids(base_dir, dataset)
    
    # 4. Preprocess data
    fmri_masked, masker = preprocess_data(base_dir, dataset)
    
    # 5. MVPA Analysis
    weights, classifier = perform_mvpa(dataset, fmri_masked)
    
    # 6. Visualization
    fig_dir = visualize_results(base_dir, dataset, masker, weights)
    
    # 7. Neural modeling
    trace = build_neural_model()
    
    print("\n=== WORKFLOW COMPLETED SUCCESSFULLY ===")
    print(f"Project directory: {base_dir}")
    print(f"Results saved in: {base_dir / 'results'}")
    print("\nNext steps:")
    print("1. Explore the generated visualizations")
    print("2. Try modifying parameters or analysis techniques")
    print("3. Extend with additional analyses or models")

if __name__ == "__main__":
    main() 