Title: Redesigning the Goalboost Timer
Author: John Lockwood
Date: 2015-12-09 07:17
Slug: redesigning_the_goalboost_timer
Excerpt:  The idea of Agile includes refactoring.  Thank goodness, because if you didn't do it right up front, you probably did it wrong.
Summary:  The idea of Agile includes refactoring.  Thank goodness, because if you didn't do it right up front, you probably did it wrong.
Category: 
Tags: 

These are some developer notes on a timer re-design I want to do.  The current timer implementation has some nice features (it generally works, and it supports both my own workflow and the current demo.  But there are many skeletons burried there too, and the last thing we want to do is make this burial ground sacred -- these bodies need to be dug up and laid to rest properly.

How's that for setting up a cognitive framework to motivate the effort?  Pretty awesome, right?  Or at least, pretty gruesome.

1) Skeleton # 1 - multiple entries per timer.  This effectively means the timer is really a task, since one can't take notes on a single effort (of course we could add that).  It also complicates the programming model quite a bit.  Actually the more I think about this, the more I realize this is (Maybe) not a bad design so much as a good design with a bad data structure.  Python OrderedDict may solve this well on that side at least.   I need to sketch / whiteboard out several alternatives.

2) Duplicate code.  We're running timers in Python and Javascript.  If we don't do this, can we still maintain a start / stop locally.  A local timer
utility that talks to the server would be nice, but that would mean having API support for start and stop, and the best API support is what the UI is coded to, sadly.  Start and stop made the API a bit unweildy from a rest standpoint,
but we've already looked at doing patch -- see UserCurrentTimerResource.patch

3) The whole UserTimer concept.  We're not using that in the web site, so do we really need it?  An alternative to it is to keep the id of the running timer on the user as an optimization, and then have the TimerManager (that's the thing!) business object manage that as an optimization?  Or just do an update on the database.  Point is we need to 