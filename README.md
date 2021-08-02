# Autonated Network Testing with Pygnmi, Pytest, and OpenConfig
This repo demonstrates how you can use Python to perform quick assurance of your network in terms its confiugrational and/or operational states.

## Usage
1. Install needed Python libraries `pip install -r requirements.txt`.
2. Modify the IP addresses and ports in test files `tests/test_arista.py` and `tests/test_nokia.py`.
3. Set credentials for connectivity to network devices as environment variables: `export PYGNMI_USER='xxx' && export PYGNMI_PASS='yyy'`.
4. Run tests `pytest -v`.

## Want to automate networks like profi?
[Join Zero-to-Hero Network Automation Training](https://bit.ly/2WStZhj)

(c) 2021, Karneliuk.com
