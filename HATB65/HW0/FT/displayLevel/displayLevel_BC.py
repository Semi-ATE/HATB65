# -*- coding: utf-8 -*-
"""

Do **NOT** change anything in this module, as it is automatically generated thus your changes **WILL** be lost in time!

If you have the need to add things, add it to 'displayLevel.py' or 'common.py'

BTW : YOU SHOULD **NOT** BE READING THIS !!!
"""

from math import inf, nan
from ate_test_app.sequencers.DutTesting.TestParameters import OutputParameter
from ate_test_app.sequencers.DutTesting.DutTestCaseABC import DutTestCaseBase
from ate_test_app.sequencers.DutTesting.Result import Result
from ate_test_app.parameters.ResolverFactory import create_parameter_resolver
from ate_common.logger import (LogLevel, Logger)
from ate_common.pattern.stil_tool_base import StilToolBase

import sys
from pathlib import Path

# get to project root directory
parent_path = str(Path(__file__).joinpath('..', '..').resolve())
sys.path.append(parent_path)

from common import Context


class displayLevel_OP:
    """Class definition for the output parameters of displayLevel."""

    def __init__(self):
        self.num_outputs = 0
        self.result = OutputParameter('result', -inf, nan, 0.0, nan, inf, 0, False)
        self.result.set_format('.3f')
        self.result.set_unit('˽')

    def set_parameter(self, name: str, id: int, ltl: float, utl: float, bin: int, bin_result: int, test_desc: str):
        output = getattr(self, f'{name}')
        output.set_limits(id, ltl, utl)
        output.set_bin(bin, bin_result)
        output.set_test_description(test_desc)
        self.num_outputs += 1

    def get_output_nums(self) -> int:
        return self.num_outputs

class displayLevel_IP:
    """Class definition for the input parameters of displayLevel."""

    def __init__(self):
        self.Temperature = None

    def set_parameter(self, name: str, type: str, value: float, min_value: float, max_value: float, power: int, context: str, shmoo: bool):
        setattr(self, f'{name}', create_parameter_resolver(type, f'{name}', shmoo, value, min_value, max_value, power, context))


class displayLevel_BC(DutTestCaseBase):
    '''Base class definition for displayLevel'''

    hardware = 'HW0'
    base = 'FT'
    Type = 'custom'

    def __init__(self, instance_name: str, sbin, test_num, context, stil_tool: StilToolBase):
        super().__init__(None, None, instance_name, sbin, test_num, context)
        self.context: Context = context
        self.ip = displayLevel_IP()
        self.op = displayLevel_OP()

        self.stil_tool = stil_tool

    def aggregate_test_result(self, site_num: int, exception: bool):
        stdf_data = []
        test_result = Result.Inconclusive()
        test_bin = -1
        if not exception:
            current_result = self.op.result.get_testresult()
            test_result = self._select_testresult(test_result, current_result)
            test_bin = self._select_bin(test_bin, current_result)
            stdf_data.append(self.op.result.generate_stdf_result_record(current_result[0], site_num))
        else:
            test_result = Result.Fail()
            test_bin = self.get_sbin()
            stdf_data.append(self.op.result.generate_stdf_result_record(test_result, site_num))

        return (test_result, test_bin, stdf_data)

    def aggregate_tests_summary(self, head_num: int, site_num: int):
        stdf_data = []
        stdf_data.append(self.op.result.generate_tsr_record(head_num, site_num, self.get_average_test_execution_time()))

        return stdf_data

    def get_test_nums(self) -> int:
        return self.op.get_output_nums()

    def get_input_parameter(self, parameter_name: str):
        return getattr(self.ip, parameter_name)

    @property
    def tester(self):
        return self.context.tester

    def run_pattern(self, pattern_virtual_name: str, start_label: str = '', stop_label: str = '', timeout_in_ms: int = 1000):
        pattern_name = self.stil_tool._get_pattern_name(pattern_virtual_name)

        self.tester.run_pattern(pattern_name, start_label, stop_label, timeout_in_ms)