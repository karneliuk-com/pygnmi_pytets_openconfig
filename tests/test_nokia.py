# Modules
from pygnmi.client import gNMIclient
import os
import re

# Vars
target_ip = "192.168.100.11"
target_port = 57400

# Tests
def test_gnmi_connecivity():
    username = os.getenv("PYGNMI_USER")
    password = os.getenv("PYGNMI_PASS")

    with gNMIclient(target=(target_ip, target_port), username=username,
                    password=password, insecure=True) as gc:
        result = gc.capabilities()

    assert "gnmi_version" in result
    assert "supported_encodings" in result
    assert "supported_models" in result


def test_openconfig_interfaces():
    username = os.getenv("PYGNMI_USER")
    password = os.getenv("PYGNMI_PASS")

    with gNMIclient(target=(target_ip, target_port), username=username,
                    password=password, insecure=True) as gc:
        gc.capabilities()

        result = gc.get(path=["/openconfig-interfaces:interfaces"])

    for entry_dict in result['notification'][0]['update'][0]['val']['interface']:
        if re.match(r'.*ethernetCsmacd.*', entry_dict["config"]["type"]):
            assert entry_dict["state"]["admin-status"] == entry_dict["state"]["oper-status"]


def test_openconfig_bfd():
    username = os.getenv("PYGNMI_USER")
    password = os.getenv("PYGNMI_PASS")

    with gNMIclient(target=(target_ip, target_port), username=username,
                    password=password, insecure=True) as gc:
        gc.capabilities()

        result = gc.get(path=["/openconfig-bfd:bfd"])

    for entry_dict in result['notification'][0]['update'][0]['val']['interfaces']['interface']:
        assert "peers" in entry_dict
        assert "peer" in entry_dict["peers"]
        assert len(entry_dict["peers"]["peer"]) > 0
        
        for bfd_peer_dict in entry_dict["peers"]["peer"]:
            assert bfd_peer_dict["state"]["session-state"] == "UP"


def test_openconfig_bgp():
    username = os.getenv("PYGNMI_USER")
    password = os.getenv("PYGNMI_PASS")

    with gNMIclient(target=(target_ip, target_port), username=username,
                    password=password, insecure=True) as gc:
        gc.capabilities()

        result = gc.get(path=["/openconfig-network-instance:network-instances"])

    for entry_dict in result['notification'][0]['update'][0]['val']['network-instance'][0]['protocols']['protocol']:
        if re.match(r'.*BGP.*', entry_dict["identifier"]):
            assert len(entry_dict["bgp"]["neighbors"]["neighbor"]) > 0
            
            for bgp_neighbor_dict in entry_dict["bgp"]["neighbors"]["neighbor"]:
                assert bgp_neighbor_dict["state"]["session-state"] == "ESTABLISHED"
