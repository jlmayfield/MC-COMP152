---
layout: page
title: COMP152 - Project 2 - Job Scheduler
permalink: /teaching/COMP152/projects/scheduler
mathjax: true
---

This project is loosely based on problem *P-9.57* where we are directed to consider the use of priority queues in operation systems. Computers need to run a large number of discrete processes or jobs, but only one such job can be running on the CPU at any given time. The operating system on a computer is responsible for operating a *scheduler* that turns over the CPU to the many different jobs waiting to use it. Not all process jobs are created equal however. Different jobs have different priorities. The scheduler must respect those priorities while attempting to process jobs on an otherwise first-come, first-served basis. So, at its core and in its simplest form, the scheduler is running a priority queue.

The idea of a priority-based scheduler is fairly straight forward, but the implications on actual CPU preformance are harder to pin done. To understand how a scheduler will behave on a particular set of jobs, we can turn to *simulation* where aa statistical model can be used to generate a set of real-world like jobs, and a discrete event simulator can be used evaluate what will happen when those jobs are presented to the scheduler.

For this project, you'll be writing a simple job scheduler simulator that takes a previously generated set of jobs for the CPU, simulates their execution, and reports basic statistics about delays in processing that result.

Below you'll find more details beginning first with a discussion of the program's input and output file formats. Within the presentation of the files you'll find some concrete examples of what the simulator needs to do. Following the look at the file formats, you'll see a quick look at the program's UI and, of course, a break down of your target versioning.


## File Formats and Example Simulation Results

This program does all of its core input and output through three files: the *jobs file*, the *simulation log*, and the *simulation report*.  The jobs file acts as the program's input. It contains a sequence of jobs that need to be run on the CPU.  The simulation log is the first output and it contains basic information about the simulation of each individual job found in the job file. The final output comes in the form a human-centered simulation report which provides some basic descriptive statistics about the data recorded in the simulation log. In a nutshell, the program will simulate jobs found in the jobs file, record the results of running those jobs in the simulation log, and then produce a high-level report based on that log.

#### Jobs File

The jobs file is a CSV file where each line of the file represents a job.  Jobs themselves are represented by 3 values: *time*, *length*, and *priority*.  Time is a positive integer and represents the time at which the job will arrive at the scheduler.  The length is also a positive integer and it represents the time it will take the CPU to complete the job once started. The job priority is an integer ranging from -20 to 20 (inclusive) and represents the job's priority. To make your lives a bit easier, we'll assume that the highest priority jobs have a priority value of -20 and the lowest priority jobs have a priority of 20.

A small job file might look like this:
```
1,5,0
3,7,2
4,10,-10
```

Here we have three jobs, the first starts at time 1, takes 5 time steps to complete, and has a priority of 0.  Thus, our simulation would begin with this job at *T=1* and the job would complete at *T=6*.  In the meantime, the next two jobs would hit the scheduler. The last job in the file would end up following the first as it has a higher priority than the second job (-10 vs 2). Once it completes, the second job in the file would reach the CPU and when it's done, the simulation will end.

In general, *we cannot assume that jobs are listed in start time order like we see in this example.* That means that this paritcular example simulation could result from any file that contains those three lines in any order.

#### Simulation Log

The simulation log is a record of the completed jobs. It too is a CSV file with each line representing a completed job. Each completed job is represented by 4 values: *arrival time*, *completed time*, *length*, and *priority*. The arrival time, length, and priority are the same values found in the jobs file. The completed time is a positive integer that represnts the time the job was finished by the CPU.

The simulation log for our simple job file from above would look like this:
```
1,6,5,0
4,16,10,-10
3,23,7,2
```

For this simulation, the first job started at *T=1* and finished at *T=6*. While this job was being completed, the other two jobs from the job file arrived at the scheduler. The last one in the file jumps to the front of the line because it has higher priority. It starts at *T=6*, when the first job finished, and then ends 10 time units later at *T=16*. The final job then starts. It completes 7 time units later at *T=23*.

It's helpful to notice that the simulation log lists jobs in the order in which they are completed. This means the second number of each row should be increasing from row to row. In general, where we can have multiple equivalent job files, the simulation log for each of those job files will be the same.

#### Simulation Report

The Simulation report is a basic text file (txt file extension). It's not a CSV file. Its intended audience is a human being. The report summarizes the simulation log with some basic descriptive statistics. In the course of developing your project you'll see two versions of the simulation report: one for version 1.5 and one for version 3.

A version 1.5 report contains the total number of jobs, as well as the minimum, maximum, and average wait time for all the jobs except the first (the first job always has 0 wait time ).  In our example above we had two jobs that had to wait for the CPU. The first arrived at 4, completed at 16, and had a length of 10. This means that it spent 2 time units waiting for the CPU (Time  4 and 5).  The second job completed arrived at time unit 3, was completed at 23, and needed 7 time units to complete.  This means it waited 13 time units before it was executed. If we exclude the first job from our calculation, then the average wait was *(13+2)/2 = 7.5* time units.  A version 1.5 simulation report file for this scenario should look like this:

```
Scheduler Simulation Report

Jobs Executed: 3
Minimum Wait:  2
Maximum Wait:  13
Average Wait:  7.5
```

For version 3 you would add the count and the min/max/average wait time for each priority. Exclude the initial job from this report as well. This new data should be reported in tabular format like you see in the complete version 3 report below.

```
Scheduler Simulation Report

Jobs Executed: 3
Minimum Wait: 2
Maximum Wait: 13
Average Wait: 7.5

Priority  Count  Min. Wait  Max. Wait  Avg. Wait
-10       1      2          2          2
2         1      13         13         13
```

The more detailed version 3 report you'd see for our simple example is not particularly interesting because we only have one job per priority as noted by the Count column.  This means the minimum, maximum, and average are all the same. For lengthier simulations we'd expect some or all of the priority levels to have multiple jobs and therefore have a different minimum, maximum, and average.

## Program UI Design

The UI for this program is very simple compared to your last project. Users run the simulator from the CLI in one of two ways:

1. They pass the filename for the jobs file as a command-line argument. i.e. `$ python3 main.py myjobfile.csv`
2. They pass zero command-line arguments and are then prompted to enter the jobs file filename when the program launches. In repl.it, this is equivalent to hitting the big green Run button.

Once the program has a jobs file filename, it proceeds to run the simulation, log the job data, and then write the report. Of course, only some of this functionality will work until you reach the later versions of the project. Our versioning strategy for this project will start by getting something working for the inputs (reading the job file) and outputs (writing the log and report) before we get down to the simulation.

## Versions

As was the case in your previous project, your work will follow a process of iterative refinement resulting in a sequence of versions that incermentally build upon one another. Each version effectively unlocks a higher grade range with the overall quality of the program determining where the grade will fall within that range. Below is a quick table of versions and their associated grade ranges. Full details of each version follows.

| Version | Feature |  Grade |
| ---: | :--: | :--: |
| 0 |  Load jobs from file to Time-based Heap | D |
| 1 | Load simulation log from file to List | C- to C |
| 1.5 | Compute Min/Max/Avg Delay/Wait From List. Write to Report File with total Jobs.  | C to C+ |
| 2 | `scheduleuntilT` function to load jobs from Time Heap to Priority Heap | B-
| 2.5 | `simulateScheduler` and full simulation program | B to B + |
| 3 | Add Min/Max/Average wait/delay by Priority to Report | A- to A |

#### Version 0

The version 0 program should have the basic starting UI working such that users can provide the jobs file filename as either a CLI argument or interactively when the program is launched. Once launched the program should read the jobs file and load the jobs into a time-based heap from which the simulation can be run. The time-based heap allows us to work through jobs in the order in which they will arrive at the CPU rather than the order in which we encounter them in the file.  The heap will, in-effect, sort the jobs by time.

No official log file nor a report are produced from this version. However, you should go ahead and have the program write the contents of your job heap to a file as a good intermediate step that lets you test your heap construction while also getting ready to produce a file as the result of your program.

To carry out the desired features of version 0, your program should make use of the following design requirements:
* Within the program, jobs should be represented by basic [named tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple) such that a job starting at time 1, taking 4 time units to finish, and having a priority of 0 could be represented as `Job(1,4,0)`.
* Write and utilize a function called `loadjobfile` that takes the name of the job file as it's input and which returns a min-heap of jobs where heap order is determined by job start time.

Putting the desired funcitonality together with design requirements leads to a program with the following behaviors:

1. Load a job file based on either a CLI argument or an interactive prompt.
2. The job file contents are loaded into a min-heap such that they come out of the heap in the order they will arrive at the scheduler.
3. Jobs in the heap should be represented with named-tuples.
4. The final heap should be written to a file (one job per line) for the purposes of testing and setting up the final file output mechanisms. We'll treat this file as an intermediate simulation log.


#### Version 1

A successful simulation will generate a log file with details about each completed job.  We'll want to load that file into a list in order to write our final report. That process is the focus of version 1.

We'll once again use named-tuples to represent jobs. Because finished jobs have one more attribute than a yet to be computed job, we'll need a second named-tuple type. Such a type would represent a job that started at time 1, ended at time 6, took 5 time steps to finish, and had a priority of 0 as `FinishedJob(1,6,5,0)`.

To stick with the design we used in version 0, you should design and write a function named `loadlogfile` that takes the name of the log file as its input and returns a list of `FinishedJob` tuples as its result.


Given that the simulation code has yet to be written, we'll need to create *mock-ups* of the log files. At this stage we can either use a file that we computed by hand, like the example described above, or it could be made-up, possible nonsensical data that meets the general structure required (CSV with 4 numbers per line).

The really important thing to recognize here is that we can mock-up key files in order to work on parts of a our program that are dependent on a part of the program we have yet to complete or even start. Put another way, *the order you write your code does not need to follow the order in which it will be executed*. Knowing about key intermediate files and data structures allow you to work through parts of a project in nearly any order you'd like.


This version is also a good time to get an intermediate report file generated. After the mock-log has been loaded, write a report that starts with the preamble (*Scheduler Simulation Report*) then follows with the job count and then the raw log contents.  To keep it simple, we'll leave out any statistic that requires real effort to compute. This leaves us with just the count of the total number of jobs, a.k.a. the length of our jobs list. By following this statistic with a re-write of the log, we can gut-check that we've loaded up the file properly.

Once you've added the version 1 code to your version 0 project you should have the following:
1. The program starts and produces a log-like file listing the contents of your time-based heap as described in version 0.
2. The program also loads in a mock-up log file and produces the report-like file that lists the number of jobs in the log followed by a raw data-dump of the log.
3. Named-tuples are used to represent entries from the log file and a file named `loadlogfile` is designed and used for constructing a list of those tuples based on the log file.

#### Version 1.5

Now that we can get the log file data into the program, we can start fleshing out the report. This step benefits from a good log file mock-up, one that represents believable data.  This should include our example log from above, but can also include any log that is in the ballpark of a simulation log (numbers aren't totally random and fit the criteria for simulation logs). No matter what, you'll need or want to compute all the required statistics by hand so that you can verify your results.

This version definitely benefits from some helper functions. Obvious candidates include:

1. `maxwait` - Takes a log list as its input, returns the maximum wait time of the entries in that list.
2. `minwait` - Takes the log list as its input, returns the minimum wait time of the entries in that list.
3. `avgwait` - Takes the log list as its input, returns the average wait time of the entries in that list.

When given all but the first log entry from our simulation, these function will compute our desired statistics. If you're so inclined, you could combine these into a single function that returns all three values. Such a function could reduce the total work by only needing to get the wait time of each entry once and then computing the three statistics. On the other hand, it puts all of your testing eggs in one basket and might prove harder to implement due to increased complexity that comes from doing three tasks at once. It's your choice.

Now that you can compute some simulation statistics, we can make a more convincing report. This leaves us with a version 1.5 program with the following capabilities:

1. Launches, reads a job file, makes a log-like file as described in version 0.
2. Reads in a proper log file as described in version 1.
3. Produces a report for the log file that lists total number of jobs along with minimum, maximum, and average wait time.
4. Wait time statistics are computed using one or more helper functions.

#### Version 2

At this point we have the bookends of our program pretty far along. We can read in a job file and produce a report from a log file. It's now time to turn our attention to the simulation and the generation log files. There's a lot going on in the simulation, so it's good to start with just one little piece and work up form there.

Our simulator doesn't work by counting through time one unit at a time. Instead it lets the times and lengths of the jobs dictate the current simulation time. To see how this works, consider the small example from our job file discussion.  The first job started at *T=1* and finished at *T=6*. While that job was at the CPU, the remaining two jobs got scheduled. Within the simulator, this happens by taking the first job out of the scheduler heap, computing the time at which it finishes (*T=6*), then adding any jobs from the time-heap to the scheduler heap that have an arrival time less than or equal to the finishing time of our current job (*T <= 6*). We then start again by removing the next job from the scheduler and updating everything accordingly. In the event that there are no jobs in the scheduler but still jobs in the time queue, we can simply remove the first job from the time queue and job the simulation time up to that start time. For example, say our simple job file had a fourth job that started at *T=100*. We'd finish the third job at *T=32* and find that the scheudler heap was empty but the time heap was not. We then proceed by removing the next item from the time-heap, bumping the simulation clock to it's start time, add it to the scheduler, and then proceed forward with something in the scheduler heap.

What has arrived from this discussion of the simulator is the design of a helpful function:

* `scheduleuntilT` - Takes as its input the time-based heap of jobs, a priority-based heap of jobs, and a time value. The function returns nothing and instead moves jobs from the time heap to the priority heap so long as their start time is no larger than the time value.

Let's say that our time-based heap is called `toDo` and our priority-based heap is called `active`. In our running example, `toDo` would be empty because we just removed the first and only job from it. The heap `active` contains our remaining two jobs. If we were to run `scheduleuntilT(toDo,active,6)`, then we would remove the two jobs from `active` and put them into `toDo` as they both have start times less than 6. This leaves `active` empty and `toDo` filled with our remaining jobs arranged in priority order. If we had that *T=100* job in the active heap as well, then that would stay in active as it's start time is greater than 6.

Your only task for version 2 is to complete `scheduleuntilT`. It's our baby step into the simulator. We don't need or want to modify how the full program runs and will instead focus on testing our critical unit outside of the program's current functionality. You can use actual `unittests` or just test it by hand at the console. Either way, your goal here is to have a working and well-tested `scheduleuntilT` and to not break any version 0 to 1.5 code in the process. This leaves you with the following:

1. A program that does everything from the previous versions and that does not use `scheduleuntilT` to do that work.
2. The function `scheduleuntilT` that is completed and that shows evidence of robust testing.

#### Version 2.5

It's time to complete the simulation. Once again, by writing a stand-alone function we can develop and test the simulator independent of the its role in the program as a whole. Such a function should look like this:

* `simulate` - Takes as its inputs the time-based job heap and the desired name of the log file. It returns nothing. Instead, it generates the log file for the simulation.

The function `scheduleuntilT` should be used by `simulate` to manage the movement of jobs from the time heap to the scheduler, i.e. the priority-based heap. On top of this, `simulate` has to manage the actual completion and logging of the jobs. We'll spend some class time talking more about the nuts and bolts of this process but the discussions above and in the file descriptions at the top should provide most of the core details.

When version 2.5 is done you can now do a complete run of the program as follows:
1. Job files is loaded as described in version 0.
2. The jobs are processed and logged by `simulate` which makes good use of `scheduleuntilT` from version 2.0
3. The log produced by the simulate function (rather than a mock-up) is then used to generate a report as described in version 1.5.

#### Version 3

The last version of our program extends our report to include a more nuanced look at our log data. In general, we are less tolerant of long wait times for higher priority tasks. This makes wait time statistics by priority level desirable.

You already have one or more functions that give you the desired statistics, you just need to use them with log entries for specific priority groups. This is an *excellent* time to use your old friend the dictionary. Imagine a dictionary where keys are the priority values and the value associated with those keys is the list of all the wait times. With such a dictionary you could generate the desired report with relative ease.

How you choose to complete this version is up to you, but you should consider some of the design ideas used already when deciding how best to proceed. 
