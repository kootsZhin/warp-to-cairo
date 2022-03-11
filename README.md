# warp-to-cairo
warp-to-cairo is a simple tool converting starknet warp outputs ([NethermindEth/warp](https://github.com/NethermindEth/warp)) outputs into readable cairo contracts.  

The warp outputs transpiled from solidity are stored in JSON format, which is hardly readable and for one to study the results, this tool is designed to convert these outputs into more readable format for further study and development.  

**Updates:** [NethermindEth/warp](https://github.com/NethermindEth/warp) already supported this! Check out ```warp transpile --cairo-output```.  

## How to use
1. Install virual environment

```bash
pipenv install
pipenv shell
```

2. Put the warp transpiled outputs at ```./inputs```

3. Run ```convert```

```bash
convert
```

4. Contract outputs will be stored at ```./artifacts``` and abis at ```./artifacts/abis```
```bash
Successfully converted 1 files (0:00:00.000945)
```

## Blueprint
```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── __pycache__
│   └── constants.cpython-37.pyc
├── artifacts
│   ├── ERC20.cairo
│   └── abis
│       └── ERC20.json
├── build
│   └── bdist.macosx-12.2-arm64
├── cli
│   ├── __init__.py
│   ├── script.py
│   └── utils
│       ├── constants.py
│       └── processor.py
├── inputs
│   └── ERC20.json
├── setup.py
└── warp_to_cairo.egg-info
    ├── PKG-INFO
    ├── SOURCES.txt
    ├── dependency_links.txt
    ├── entry_points.txt
    ├── requires.txt
    └── top_level.txt
```
