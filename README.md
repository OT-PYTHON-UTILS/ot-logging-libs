ot-logging-libs
=====================================
Python library for logging

## Description

This library contains logging module:
* This module allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have been arisen. 

## Getting Started
-----------------------------------------

## Installing
Create a *<b>requirements.txt</b>* file where you want to use this library and mention the url 'git+https://github.com/OT-PYTHON-UTILS/ot-logging-libs.git' along with the libraries required for the python code to execute and install it with below command.
* <b>pip install -r requirements.txt</b>

## Library Calling

<b>from otlogginglibs import logging</b>

## Example 
### <b>requirements.txt</b>

``` 
wheel
json_log_formatter
git+https://github.com/OT-PYTHON-UTILS/ot-logging-libs.git
```

</b>pip install -r requirements.txt</b>

### <b>test_logger.py</b>
```
from otlogginglibs import logging

def test_logger():
    print("Demo function")
    log_path = "/var/log/demo.log"
    logger = logging.Logger().get_logger(log_path)
    logger.info("Logs are storing at %s", log_path)

test_logger()
```
## Author

[himanshi_homepage]: https://github.com/himanshiparnami
[himanshi_avatar]: https://avatars.githubusercontent.com/u/101627875?s=200&v=4

**[![Himanshi Parnami][himanshi_avatar]][himanshi_homepage]<br/>[Himanshi Parnami][himanshi_homepage]** 

## Version History

* ## 0.1
    * Initial Release
