#!/usr/bin/env conda run -n ATE python
# -*- coding: utf-8 -*-
"""
By Zlin526F
"""

import os, sys
from pathlib import Path
test_path = os.path.abspath(Path(__file__).joinpath('..'))
sys.path.append(test_path)

from displayLevel_BC import displayLevel_BC

from ate_common.logger import LogLevel


class displayLevel(displayLevel_BC):

    '''
    for debug puposes, a logger is available to log infomration and porpagate them to the UI.
    logging can be used as described below:
    self.log_info(<message>)
    self.log_debug(<message>)
    self.log_warning(<message>)
    self.log_error(<message>)
    self.log_measure(<message>)

    <do_not_touch>
    show different messages
    Input Parameter | Shmoo | Min | Default | Max | Unit | fmt
    ----------------+-------+-----+---------+-----+------+----
    ip.Temperature  |  Yes  | -40 |   25    | 170 | °C   | .0f

    Parameter         | MPR | LSL | (LTL) |  Nom  | (UTL) | USL  | Unit | fmt
    ------------------+-----+-----+-------+-------+-------+------+------+----
    op.result         | No  |  -∞ |  (-∞) | 0.000 | (+∞)  | +∞   | ˽    | .3f
    </do_not_touch>

    '''
    def do(self):
        """Default implementation for test."""

        breakpoint()
        self.context.logger.set_logger_level(LogLevel.Debug())

        self.log_debug("This is a debug level message1")
        self.log_measure("This is a measure level message")
        self.log_info("This is a info level message")
        self.log_warning("This is a warning level message")
        self.log_error("This is a error level message")

        self.op.result.default()
