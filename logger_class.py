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
    instance = None
    fname = "logs/log01.log"
    # Actual functionality of Logger class will be in private class.

    class __LoggerSingleton:
        def __init__(self):
            self.filename = Logger.fname

        # not related to being singleton
        # but it's better to keep common method as private
        def _write_log(self, level, message):
            with open(self.filename, "a+") as logging_file:
                logging_file.write("[{0}] {1}\n".format(level, message))

        def critical(self, message):
            self._write_log("CRITICAL", message)

        def error(self, message):
            self._write_log("ERROR", message)

        def warning(self, message):
            self._write_log("WARNING", message)

        def info(self, message):
            self._write_log("INFO", message)

        def debug(self, message):
            self._write_log("DEBUG", message)

    # 'static' class method which instantiates Logger class.
    def __new__(cls):
        if not Logger.instance:
            Logger.instance = Logger.__LoggerSingleton()
        return Logger.instance

    # to call the private class attrs which is saved in
    # 'instance' class variable.
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
