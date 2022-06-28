# python-batch-example

An example of a batch processing script in Python.

Run with:
```bash
$ python example.py >! log &
```

Check status of the run with:
```bash
$ jobs
$ tail log
```
Note the log file may be buffered, so it won't updated continuously.
