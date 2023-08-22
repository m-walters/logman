# logman

**Note: This has not been maintained since 2016 (though I would guess it is still compatible with `logging` module).**

Fancy python logging manager class.  
Uses python [`logging`](https://docs.python.org/2/library/logging.html) module.
With little hassle, this class provides a high degree of flexibility and control over:

1. where messages are logged, which can include multiple files along with console printing
2. the format of the log messages in each location, and
3. which messages go where

When `logman` is instantiated it must be provided with a *name*, *level*, and *message format*.  
It can optionally be given a logfile. With no logfile, a StreamHandler is created, as oppose to a FileHandler, which will log information to the console.

As mentioned in the `logging` module documentation, good practice is to use `__name__` for the name so that records will be uniquely associated with the corresponding module (should the user choose to include the label in their message format).

The instance must be given what's called a level. Loggers have five levels which can be thought of as degrees of severity. More information can be found [here](https://docs.python.org/2/howto/logging.html#logging-basic-tutorial), but, in increasing severity, the levels are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`. Loggers are initialized with a certain level, and they ignore messages that fall below this level, but include all those higher in level. Messages, or records, are ascribed a level when issued.

For example, a standard implementation would involve creating a logger at the debug level, to catch all the information, and then adding a StreamHandler at the info level. Messages given the info level will be printed to console, and also written into the log since info is higher than debug. Messages labeled with debug will write to the log, but not print to the console. The following code will do this:

```python
import logman

sformat = '%(name)s : %(message)s'
logger = logman.logman(__name__, "debug", sformat, "run.log")
logger.add_handler("info", "%(message)s")
```

Because `add_handler()` wasn't given a file, it automatically creates a StreamHandler.  
Now is a good time to address message formats. With `logging` you can customize the record formats to automatically include [all sorts of information] (https://docs.python.org/2/library/logging.html#logrecord-attributes) that would otherwise be quite a hassle to configure. In the example above, the format of the records in the file includes the logger name at the beginning of each message, but we don't care about that for the console printing. Note, When you're logging from different modules you'll have to create new loggers in them, but they'll all write to the same file if you tell them to.

Okay, so let's finally look at what creating a log record would actually look like. In this example there's a parameter module with class prm. I want to write the parameters to the log file, but I don't need them printing to the console.

```python
from params import prm

logger.printl("debug", "Vomit of parameters:")
logger.printl("debug", str(prm.__dict__))
```

Notice how you don't need to specify all the additional information, such as the module name, when creating the record as it is now automated.  
For a more orderly output, the following would be preferable:

```python
d = prm.__dict__
for i in d:
    logger.printl("debug", str(i) + ":\t" + str(d[i]))
```

\- Michael W
