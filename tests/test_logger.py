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
    def test_info_logger(self):
        message = "test_logger is working?"
        # make sure logs directory is created
        if not os.path.isdir("logs"):
            os.system("mkdir logs")
            print("directory created")
        log = Logger()
        log.info(message)

        with open(log.filename, "r") as log_file:
            log_lines = log_file.readlines()

        # for this test to be reused, remove the file
        os.system("rm " + log.filename)

        # get last line
        last_log_line = log_lines[-1].rstrip("\n")

        self.assertEqual(last_log_line, "[INFO] " + message)


# keeping singleton test seperate to keep instance creation
# in this class only, makes testing easy.
# Or else, other tests might influence the instantiation.
class TestLoggerSingleton(unittest.TestCase):
    def test_singleton_property(self):
        default_fname = "logs/log01.log"
        fname1 = "logs/file1.log"
        fname2 = "logs/file2.log"
        fname3 = "logs/file3.log"

        log1 = Logger()

        log2 = Logger()

        log3 = Logger()

        # singleton logger will have only 1 instance
        # each object's filename will be the last
        # filename set i.e. 'default_fname'
        self.assertEqual(log1.filename, default_fname)
        self.assertEqual(log2.filename, default_fname)
        self.assertEqual(log3.filename, default_fname)

        log1.filename = fname1
        log2.filename = fname2
        log3.filename = fname3

        # singleton logger will have only 1 instance
        # each object's filename will be the last
        # filename set i.e. 'fname3'.
        self.assertEqual(log1.filename, fname3)
        self.assertEqual(log2.filename, fname3)
        self.assertEqual(log3.filename, fname3)

        # due to singleton property, instances will be same.
        self.assertEqual(log1, log2)
        self.assertEqual(log3, log2)


if __name__ == "__main__":
    unittest.main()
