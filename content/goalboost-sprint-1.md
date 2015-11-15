Title: Goalboost Sprint 1
Author: John Lockwood
Date: 2015-11-15 10:30
Slug: goalboost_sprint_1
Excerpt: Goalboost Employee Owned Time and Billing Sprint 1 is in progress.  Here's a status update with some remaining deliverables.
Summary: Goalboost Employee Owned Time and Billing Sprint 1 is in progress.  Here's a status update with some remaining deliverables.
Category: 
Tags: 

An interesting side-effect of doing an "Agile" project on a part time basis with only one employee owner on a part time basis is that daily standups make no sense at all.  Working part time, on a given calendar day one might get an hour and a half of work done, and working alone, there's no one to stand up around a table and talk to.  Nevertheless, I think periodic progress reports on the [Goalboost](http://localhost:8000/goalboost.html) project are in order.

## Retrospective

Looking back on the product roadmap, it looks like Sprint 1 started on October 24, 2015.  I've been trying to fit it in as "fourth quarter, 2005",
but it started 24 days late for that.  Also, if we plan for 16 sprints, it might be cool to finish up just as 2020 begins.  Of course the project really started before the RoadMap, so it's all good.  The original plan for Sprint 1 was this:

<p style="padding-left:5em;"><em>Sprint 1 - It's About Time
At the end of this sprint, we will have stood up various ways to create and use timers.  This is already in progress.  The assumption for now is that
we have just one project in the universe, Goalboost itself.  By the end of this sprint we should have:<br />
<ul style="padding-left:5em;"><li>A User / Timer rest-based API with lousy security (we'll fix that in Sprint 2).</li>
<li>A hosted app we can point to.  That way there'll be no guessing about how brain dead it still is.  It'll be obvious.</li>
<li>Some sort of UI for entering / viewing timers.  We may steal some of this from Goalboost-that-was, the Java-versionator(tm).</li>
<li>A way to dump the hard-coded [Goalboost hours](https://raw.githubusercontent.com/CodeSolid/Goalboost/master/docs/hours.json) from the app itself.  This probably means we need at least a half-day one-time import script.</li></ul>
</em></p>

## What's been done to date:

* Between "Sprint 0" (so to speak) and Sprint 1, I've logged 108.4 hours on the project.  Given some calculations I made earlier, as long as I'm working on this alone, 125 hours spread over a calendar quarter constitutes a sprint.
* The project is deployed and hosted.  [Here it is](http://goalboost.com), in all its inglorious alpha quality.
* So far the API is perhaps 80-90% done.  Seen strictly from the point of view of "function points" it's only maybe 60%, but given that we've paid down the learning curve on those, the rest should go more quickly.
* Meantime on the front end (currently the app's main page), we've built out the Angular user interface a bit, but none of it is wired to the API at this 
point.
* The [development page](http://www.goalboost.com/development) was not on the original roadmap for *per se*, but I think it was a good idea.  Also, if we don't finish the timer page in time, the development page fits the bill minimally for "some sort of UI for entering / viewing timers".

## What's left to do.

Here's what we're planning to do before December 31st.

* Create a goalboost project on the server.  We have model class we can use at the command line, though we may not have API / UI stood up for projects yet.
* We've written most of the code an importer will need to import hours.json.  We need to finish that up and write some kind of view on the data that we can link to.
* We might tweak the User model as needed to get Github account in there. This is optional at this point.

## Planning for next Sprint

In the next Sprint the focuses will be on:

* Polishing up the UI.
* Further work on security and authentication.

We also need to work on making the code more accessible to other programmers.  There's not much in the way of instructions, etc.