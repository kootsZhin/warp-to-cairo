# warp-to-cairo
warp-to-cairo is a simple tool converting starknet warp outputs ([NethermindEth/warp](https://github.com/NethermindEth/warp)) outputs into readable cairo contracts.  

The warp outputs transpiled from solidity are stored in JSON format, which is hardly readable and for one to study the results, this tool is designed to convert these outputs into more readable format for further study and development.

# Usage
1. Install virual environment.

```bash
pipenv install
pipenv shell
```

2. Put the warp transpiled outputs at ```./inputs```.

3. Run

```bash
python3 main.py
```

4. Contract outputs will be stored at ```./artifacts``` and abis at ```./artifacts/abis```.
```bash
Successfully converted 1 files (0:00:00.000945)
```

# Repository Structure
```bash
.
├── Pipfile
├── Pipfile.lock
├── __pycache__
│   └── constants.cpython-37.pyc
├── artifacts
│   ├── ERC20.cairo
│   └── abis
│       └── ERC20.json
├── inputs
│   └── ERC20.json
├── main.py
└── src
    ├── constants.py
    └── processor.py

5 directories, 9 files
```
