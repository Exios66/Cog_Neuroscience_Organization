# Scripts

This directory contains utility scripts for various tasks related to the Cognitive Neuroscience Organization's research and development workflows.

## Script Categories

- **Data Processing**: Scripts for processing and converting neuroimaging data
- **Analysis**: Scripts for running analyses on neuroimaging data
- **Visualization**: Scripts for generating visualizations and figures
- **Automation**: Scripts for automating common tasks and workflows
- **Deployment**: Scripts for deploying applications and services

## Usage

Most scripts can be run from the command line with appropriate arguments. Each script includes a help message that can be accessed with the `-h` or `--help` flag:

```bash
python scripts/process_fmri_data.py --help
```

## Script Documentation

Each script should include:

1. A descriptive header comment explaining its purpose
2. Documentation of input parameters and expected outputs
3. Example usage commands
4. Dependencies and requirements

## Contributing

When adding new scripts, please follow these guidelines:

1. Place the script in the appropriate subdirectory based on its function
2. Include comprehensive documentation within the script
3. Add the script to this README with a brief description
4. Ensure the script follows our coding standards
5. Add appropriate error handling and user feedback

## Available Scripts

### Data Processing

- `convert_nifti.py`: Convert neuroimaging data between different formats
- `preprocess_fmri.py`: Preprocess fMRI data with standard pipelines

### Analysis

- `functional_connectivity.py`: Compute functional connectivity matrices
- `statistical_analysis.py`: Run statistical analyses on neuroimaging data

### Visualization

- `plot_brain_maps.py`: Generate brain maps from neuroimaging data
- `create_figures.py`: Create publication-quality figures from results

### Automation

- `batch_process.py`: Process multiple datasets in batch mode
- `monitor_jobs.py`: Monitor and report on long-running jobs

### Deployment

- `setup_environment.py`: Set up development environment
- `deploy_web_app.py`: Deploy web applications to servers
