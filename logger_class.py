#   Filename:       logger.py
#   Description:    Utility function for logging
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


class Logger(object):
    def __init__(self, filename):
        self.filename = filename

    def write_log(self, level, message):
        with open(self.filename, "a+") as logging_file:
            logging_file.write("[{0}] {1}\n".format(level, message))

    def critical(self, message):
        self.write_log("CRITICAL", message)

    def error(self, message):
        self.write_log("ERROR", message)

    def warning(self, message):
        self.write_log("WARNING", message)

    def info(self, message):
        self.write_log("INFO", message)

    def debug(self, message):
        self.write_log("DEBUG", message)