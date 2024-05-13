# VSDBG
VSDBG is a simple helper utility for debugging PyPi packages in Visual Studio Code.
Quite simply, this package makes it easy to open a debugging session for a python package that has been installed with

```bash
pip install <path to repo>
```

## Installation Requirements

1. Python 3.6+

## Usage

This package contains a single function which opens a debugging session on a local port.
To use vsdbg on a PyPi repo, first clone the repository you plan to debug to a local directory:

```bash
git clone <package repository>
```

To install the repository in development mode, run:

```bash
pip install -e <path to local repository>
```

The "-e" flag installs the PyPi package with symlinks that point back to the local repository, thereby allowing you to edit/debug it after installing it through pip.

Open the repository folder in VS Code.
In one of the primary ".py" files of your code (`__init__`.py or `__main__`.py are great options) add the following line to your imports:

```python
import vsdbg
```

This imports and calls the dbg function using the default port `5678`.
Alternative ports can be specified using:

```python
import vsdbg
vsdbg.dbg(port=5679)
```
for instance.

By default, vsdbg will halt the execution of the program once it has been imported until the user attaches a debugger (i.e. hits `F5` in VSCode).

To use vsdbg without halting execution (mainly for long-executing scripts) you can import thusly:

```python
import vsdbg
vsdbg.dbg(wait=False)
```

To tell VS Code to listen on port `5678` for a debugging session, press `F5` or select from the menu `Run -> Start Debugging`.

VS Code requires a `launch.json` file to configure its debugger. When prompted, select "Remote Attach" from the dropdown menu. Then select `localhost`.

By default, Remote Attach will listen on port `5678`, or it can be configured to a new port by editing the launch.json file.

You can now call the python package from any terminal. Execution will pause when the package reaches the `vsdbg.dbg()` call, and it will wait for the debugger to connect before proceeding.

To attach the VS Code debugger, simply press `F5` or select "Run and Debug" from the menu. VS Code will attach to the open debug session and you will be able to step through the code and set breakpoints as you would with any other python package.
