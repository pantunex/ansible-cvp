#!/usr/bin/python
# coding: utf-8 -*-
# pylint: disable=logging-format-interpolation
# pylint: disable=dangerous-default-value
# pylint:disable=duplicate-code
# flake8: noqa: W503
# flake8: noqa: W1202
# flake8: noqa: R0801

"""
    test_cv_device_tools_generic.py - Generic testcases for cv device tools
"""

from __future__ import (absolute_import, division, print_function)
import requests.packages.urllib3
import ssl
import sys
import pytest
import logging
sys.path.append("./")
sys.path.append("../")
sys.path.append("../../")
from ansible_collections.arista.cvp.plugins.module_utils.device_tools import FIELD_FQDN, FIELD_SYSMAC, FIELD_ID, FIELD_PARENT_NAME, FIELD_PARENT_ID
from ansible_collections.arista.cvp.plugins.module_utils.device_tools import DeviceInventory, CvDeviceTools, FIELD_CONTAINER_NAME, FIELD_SERIAL
from lib.utils import cvp_login


# Hack to silent SSL warning
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

# ---------------------------------------------------------------------------- #
#   FIXTURES Management
# ---------------------------------------------------------------------------- #


@pytest.fixture(scope="class")
def CvDeviceTools_Manager(request):
    logging.info("Execute fixture to create class elements")
    request.cls.cvp = cvp_login()
    request.cls.inventory = CvDeviceTools(cv_connection=request.cls.cvp)

# ---------------------------------------------------------------------------- #
#   PYTEST
# ---------------------------------------------------------------------------- #


@pytest.mark.usefixtures("CvDeviceTools_Manager")
class TestCvDeviceToolsGeneric():

    def test_cvp_connection(self):
        assert True
        logging.info("Connected to CVP")

    @pytest.mark.api
    def test_search_by_getter_setter(self):
        self.inventory.search_by = FIELD_SYSMAC
        assert self.inventory.search_by == FIELD_SYSMAC
        logging.info(
            "Setter & Getter for search_by using {} is valid".format(FIELD_SYSMAC))
        self.inventory.search_by = FIELD_FQDN
        assert self.inventory.search_by == FIELD_FQDN
        logging.info(
            "Setter & Getter for search_by using {} is valid".format(FIELD_FQDN))

    @pytest.mark.api
    def test_check_mode_getter_setter(self):
        self.inventory.check_mode = True
        assert self.inventory.check_mode is True
        logging.info(
            "Setter & Getter for search_by using {} is valid".format(FIELD_SYSMAC))
        self.inventory.check_mode = False
        assert self.inventory.check_mode is False
        logging.info(
            "Setter & Getter for check_mode is valid")
