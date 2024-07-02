# Benchmark

Benchmark different graph libraries on the same task(s) and dataset(s) in order to compare time performance.

Inspired by the [graph benchmarks](https://github.com/timlrx/graph-benchmarks/blob/master/README.md) and results from [graph results](https://www.timlrx.com/blog/benchmark-of-popular-graph-network-packages-v2)

## Installation

- clone repository

- select Python Interpreter: use non default interperter that comes from OS. Instead install specific version. For example:
```sh
brew install python@3.12
```

Then add interpreter path in VsCode: 
Command Pallete (CMD+SHIFT+P) -> Python: Select Interpreter -> Enter interpreter path.
Path is based on brew install location for specific version. For example:
```sh
brew info python@3.12
```

- if you want to use Python virtual environment in VsCode, follow the [instructions](https://code.visualstudio.com/docs/python/environments) update .gitignore accordingly. For example:

```shell
 python3 -m venv .venv
```

- open new terminal should activate the virtual environment automatically.
  For example for venv, you should see .venv mentioned near the cursor at the terminal
  (.venv) User falcon >

If it is not auto activated, add this line to .vscode/settings.json :
```json
"python.terminal.activateEnvironment": true,
```
and open a new terminal.

- install dependencies (python modules) based on requirements-dev.txt:

```shell
pip3 install -r requirements.txt
```

## Download data
Run bash script inside "data" folder:

```shell
chmod +x download_data.sh
./download_data.sh
```

You can comment out lines with data files that you don't want to download.

## Benchmark

Example command for benchmarking all tasks and printing results to output file:

```sh
python3 <path/to/this/script> <library> <dataset> <repeations> [task] > output/file.txt
```

Substitute with specific arguments:
- library: Networkx
- Input dataset tsv file: data/small.txt
- Repeat every run number of times: 10
- task: [Optional], default = All
- Print the results to output file: output/networkx-small.txt

Example command:

```sh
python3 src/main.py networkx data/small.txt 10 > output/networkx-small.txt
```


Example command for benchmarking specific task CONNECTED_COMPONENT:

```sh
python3 src/main.py networkx data/small.txt 10 CONNECTED_COMPONENT > output/networkx-cc-small.txt
```

Task can be one of enum values from src/profiling/task.py
