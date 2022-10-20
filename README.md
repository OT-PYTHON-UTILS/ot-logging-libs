ot-logging-libs
=====================================
Python library for logging

## Description

This library contains logging module:
* This module allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have been arisen. 

## Getting Started
-----------------------------------------

## Installing
<b>pip install -r requirements.txt</b>

## Library Calling

<b>from otlogginglibs import logging</b>

## Example 

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
