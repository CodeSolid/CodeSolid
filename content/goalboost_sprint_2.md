Title: Goalboost Sprint 2
Author: John Lockwood
Date: 2016-01-09 06:18
Slug: goalboost_sprint_2
Excerpt: In Sprint 2 we're locking down the security, fixing some timer problems, extending the timer UI, and beginning to look at user management.
Summary:  In Sprint 2 we're locking down the security, fixing some timer problems, extending the timer UI, and beginning to look at user management.
Category: 
Tags: 

This is a kind of standup meeting about Goalboost Sprint 2 -- where we are so far and what we're planning.

Here's the original description ofSprint 2:

<blockquote>

<p>We already have some very basic Flask-Security based authentication coded. By the end of this sprint we'll have:</p>
<p>Non-single-user user account creation in place.<br />
Basic user management -- add and delete new non-admin users to account.<br />
Token based security for the rest endpoints (management for these may come later).<br />
</blockquote>

This Sprint ends March 31st, 2016, and to date (9 January) we have done the token based security metioned above, and applied this to timer implementation.  What's currently the /timer/user page is pretty much a single page application except for the authentication.  (SPA purists would take issue with that I'm sure -- lucky for me none of them read me as far as I know).

We've also been spending significant time (since December, or a little less than a week of "real-time"), doing two things:

* Refactoring the timer implementation to make it easier to work with.  A timer now is more like a "time entry" -- a total hours for a given note on the same day.
* Coming to the realization (somewhat late) that we've been working with an ORM that's not well suited to the task at hand, and writing lots of code to get around that.
* Reworking the Timer UI based on the progress I've made so far.  It now allows editing existing time entries, though there's still a bit more to do.

I also spent a smaller amount of time on a better command line utility, "gb", a task timer for git.  This is just a stub so far.








