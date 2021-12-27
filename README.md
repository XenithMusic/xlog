# X-Log

This is a logging package, made for my own convenience.

## Basically everything you'll ever need to know

`logger` - Class that defines everything the average user will need to use.

* `logger.debug(self,msg)` Send a debug message.
  * Example: `logger.debug("Debug message")` -> `[12:34:56] [DEBUG] Debug message`
* `logger.info(self,msg)` Send an info message.
  * Example: `logger.info("Info message")` -> `[12:34:56] [INFO] Info message`
* `logger.warn(self,msg)` Send a warning message.
  * Example: `logger.warn("Warning message")` -> `[12:34:56] [WARN] Warning message`
* `logger.error(self,msg)` Send a error message.
  * Example: `logger.error("Error message")` -> `[12:34:56] [ERROR] Error message`
* `logger.fatal(self,msg)` Send a (uncaught) error message.
  * Example: `logger.fatal("Fatal error message")` -> `[12:34:56] [FATAL] Fatal error message`

### Everything outside of a class

* `format(msg,t)` - Internal function, formats msg and type into logger message.
  * Example: `print(format("This is essentially a log.","LMAO"))` -> `[12:34:56] [LMAO] This is essentially a log.`

## Changelog

```
- 0.0.1
  - First public release
- 0.0.2
  - Fixed a syntax error.
- 0.0.3
  - Might have fixed the error where you cannot create a logger.
- 0.0.4
  - Seems I messed up and should not have put the code in the init file.
  - Moved code from init file to example file
  - Fixed formatting in README.md
  - Log file is produced.
```
