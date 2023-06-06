# Automate benchmark tests on Tower via CLI

This sub-directory contains scripts that allow for 'automation' of running nf-core pipelines on Tower for benchmarking.

## Setup
1. Install the Tower CLI
```
wget -L https://github.com/seqeralabs/tower-cli/releases/download/v0.7.3/tw-0.8.0-linux-x86_64
mv tw-* tw
chmod +x ./tw
sudo mv tw /usr/local/bin/
```

2. Make sure you have Python (v3.6+) installed
3. Set your `TOWER_ACCESS_TOKEN` as an environment variable. The scripts check for this variable and will throw an error if not set.
```
export TOWER_ACCESS_TOKEN=<your access token>
```
4. (Optionally) Configure the workspace ID as a environment variable using `TOWER_WORKSPACE_ID`. This can also be set in the config YAML provided to the script using `workspace: <your workspace>`.

5. These scripts don't use any specific non-default packages but you can set up a minimal conda environment in Linux as such:
```
wget -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash miniconda.sh -p <prefix_to_a_specific_path> 

source .bash_profile

conda env create -f environment.yaml
```

Most packages used in these scripts are available in base, with the exception of potentially `pyyaml`. If not installed, you can also just run:
```
pip install pyyaml
```

## Usage

### Config for running pipelines in `benchmark_tests.yaml`
In this config, specify what
 - Workspace
 - Compute-env
 - Pipelines (their version-controlled repository URLs) and their revisions (i.e. `v1.10.0` or `dev`) you want to run
 - (Optional) Name for your workflow: Specify a human-readable name or a random name will be autogenerated for you.
 - (Optional) Profile for your pipeline (i.e. `profile test` or `profile test_full`)
 - (Optional) Pipeline parameters in the `parameters` block: You can specify pipeline-specific parameters here. They will be supplied to the Tower CLI as the `--params-file` option. For example, you can specify the `outdir` for your pipeline results here.
 - (Optionla) Specify Nextflow configuration options in `config`: These will be supplied to the Tower CLI as the `--config` option.

All pipelines specified in this config will be launched simultaneously. 

There are default examples of the config file provided in this repo that can be edited or just used out of the box.

You can save versions of these configs for provenance (i.e. `run_benchmarks_profile_test.yaml`, `benchmarks_profile_test_full.yaml`)

### Run the script
You can execute launching of the pipelines by running the script as follows:
```
python run_benchmarks.py --config benchmark_tests.yaml
```

All pipelines you specified will be launched into the provided workspace on Tower.
