.. _exercise_downloader:

###################
Threaded Downloader
###################

If you have a lot of web sites (or web services) to hit at once, you may find that you're waiting a long time for each request to return.

In that case, your computer isn't doing much, and it could be waiting on multiple requests all at once.

In the examples, we had a news site scraper that used asyncio to asynchronously gather a bunch of data.

Your job is to write a version of that that uses threads, instead.

A Queue?
========

You will need a way to launch a bunch of threads at once, but probably not one for each request you want to make -- that could be a lot of threads!

So you'll probably want to use a job Queue -- and then launch a handfull of threads to process those jobs.

Experiment a bit -- how many threads give you maximum performance?





