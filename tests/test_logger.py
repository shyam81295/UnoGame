#   Filename:       tests/test_logger.py
#   Description:    Tests class 'Logger'
#
#   Copyright (C) 2020 Shyam Singh
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import sys
import unittest

from logger_class import Logger


class TestLogger(unittest.TestCase):
    def test_logger(self):
        filename = "logs/defg.log"
        message = "test_logger is working?"
        # make sure logs directory is created
        os.system("mkdir logs")
        log = Logger(filename)
        log.info(message)

        with open(filename, "r") as log_file:
            log_lines = log_file.readlines()

        # for this test to be reused, remove the file
        os.system("rm " + filename)

        # get last line
        last_log_line = log_lines[-1].rstrip("\n")

        self.assertEqual(last_log_line, "[INFO] " + message)


if __name__ == "__main__":
    unittest.main()
