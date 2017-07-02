Schedule resilient cron jobs and make sure they eventually run often enough.

# NAME

micron – Schedule jobs

# SYNOPSIS

`micron [-h] [-d DIRECTORY] [-f]`

# OPTIONS

`-h, --help`
:   Show help message and exit.


`-d DIRECTORY, --directory DIRECTORY`
:   Runtime directory.


`-f, --foreground`
:   Run in the foreground (i.e. do not daemonise).

# JOB FILE

Jobs are defined in the **~/.micron/jobs.yaml** file (or wherever
it is depending on what you made of the **--directory** option).
This file is reloaded every cycle.

```
foo:
    every:      1 week
    command:    /usr/bin/foo
    retry:      1 hour
    maxretry:   3
    # random:     30 minutes
```

Every job starts with a unique key (e.g. called **sleep**, here). Duration
are written in a natural language. The following fields are available,
newlines are fine – no need to escape – and you can comment them out
with **#**.

every
:   How often the job should run.

command
:   Command to run, as you would type it in a shell.

cwd
:   Current working directory. It defaults to **/** when micron is run as
    a daemon, micron's own current working directory otherwise.

retry
:   Time to wait before running the job again after a failure, i.e. a non-zero
    exit code. It defaults to 1 hour.

maxretry
:   How many times to retry a failed job, i.e. one exiting with a non-zero
    code. There is no retry by default.

random
:   How long to wait for before starting the job at its scheduled
    time. There is no wait by default.

timeout
:   How long to wait before interrupting the job after it starts.
    This isn't implemented yet. There will be no timeout by default.

# CONFIGURATION FILE

Configuration is defined in the **~/.micron/config.yaml** file (or wherever
it is depending on what you made of the **--directory** option).
The following optional parameters can be set:

loopsleep
:   How long in seconds to sleep for at the end of each cycle. Defaults
    to 60 seconds.

notify:
:   A boolean specifying whether or not to open a notification window
    after a job failure. Defaults to **false**.
