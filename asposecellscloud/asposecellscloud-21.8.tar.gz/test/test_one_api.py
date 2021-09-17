# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
import os
import sys
import unittest
import warnings
import shutil

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import WorkbookEncryptionRequest
from asposecellscloud.models import WorkbookProtectionRequest
from asposecellscloud.models import ImportIntArrayOption
from asposecellscloud.models import CalculationOptions
from asposecellscloud.models import WorkbookSettings
from asposecellscloud.models import PasswordRequest
from datetime import datetime
global_api = None

class TestOne(unittest.TestCase):
    """ CellsWorkbookApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_one_call(self):
        """
        Test case for cells_workbook_put_convert_workbook

        Convert workbook from request content to some format.
        """
        fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "Book1.xlsx"
        format ='pdf'       
        password = None
        outPath = None             
        result = self.api.cells_workbook_put_convert_workbook(fullfilename,format=format)
        shutil.copy(result,"book1.pdf")
        # export_filename = "D:\\projects\\test\\Aspose.Cells\\output\\book1.pdf"
        # with open(export_filename,'wb') as f:
        #         f.write(result)
        # self.assertEqual(result.code,200)
        #result = self.api.download_file("Book1.xlsx")
        #print(result)
        #shutil.copy(result,"book1.xlsx")
        pass


if __name__ == '__main__':
    unittest.main()
