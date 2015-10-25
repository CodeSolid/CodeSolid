Title: GoalBoost Roadmap 0.1
Author: John Lockwood
Date: 2015-10-24 14:58
Slug: goalboost_roadmap
Excerpt: Because as Yogi Berra said:  "If you dont' know where you're going, you'll end up someplace else."
Summary: 
Category: 
Tags: 

This is a draft roadmap for the [Goalboost](/goalboost.html) project.  I'll be adding to this and versioning it.

## Some Quasi-Mathematical Assumptions

* If John Lockwood were to have one year (full time) to do nothing but write some SASS software, at the end of the year there'd be something cool I could market.  That's not much of an "employee owned" software shop with me in it,
but I'm hoping someone will catch on if I start buildging the thing, and then we'll revise from there.
* One year contains 2,000 hours.  That's based on a 40 hour week, 50 weeks per year, two weeks vacation.
* I can't work 40 hours per week on this because I'm only able to work part time for now.  Rather agressively, I can try to dedicate 10 hours per week, or 1/4 effort.  That means I should be able to write something cool in four years.
* That also means there'll be 16 quarters to this project, and each quarter will have 2000/16 hours in it.  Or in other words, for each 3 months that goes by in real time, I can dedicate 125 hours, which if we weren't having to count in dog years like this would be more or less a 3-week sprint.  So we have something like sixteen three-week sprints.

## What needs to really happen:

... is that we need to size each sprint's activities more precisely,
so we'll know better if the assuptions below are brain dead.

## Sprint 1 - *It's About Time*
At the end of this sprint, we will have stood up various ways to create and use timers.  This is already in progress.  The assumption for now is that
we have just one project in the universe, Goalboost itself.  By the end of this sprint we should have:

- A User / Timer rest-based API with lousy security (we'll fix that in Sprint 2).
- A hosted app we can point to.  That way there'll be no guessing about how brain dead it still is.  It'll be obvious.
- Some sort of UI for entering / viewing timers.  We may steal some of this from Goalboost-that-was, the Java-versionator(tm).
- A way to dump the hard-coded [Goalboost hours](https://raw.githubusercontent.com/CodeSolid/Goalboost/master/docs/hours.json) from the app itself.  This probably means we need at least a half-day one-time import script.

## Sprint 2 - *We Love Users - Customers Who Can't Pay Yet*
We already have some very basic Flask-Security based authentication coded. By the end of this sprint we'll have:

- Non-single-user user account creation in place.
- Basic user management -- add and delete new non-admin users to account.
- Token based security for the rest endpoints (management for these may come later).

## Sprint 3 - *Timers Need a Home -- Invoices and Projects*
* Models and testing for invoices and projects.
* UI to create invoices.
## Sprint 4 - *If you can bill them, I can bill you*
Here we'll focus on ways to send invoices.  

- We'll be able to email an invoice by the end of this sprint.
- That sounds unambitious, but it involves either a new security model for the invoice link or a basic PDF invoice "report".
## Sprint 5 - *No seriously, you'll want to be billing people*

- Begin work on [paypal invoice integration](https://developer.paypal.com/docs/classic/invoicing/IntroInvoiceAPI/).  Do proof of concept.
## Sprint 6
- Finish Paypal proof of concept.
## Sprint 7 *It's all right here in my report*
- Reports and queries.

## Sprint 8
- Basically it all trails off from here.  We need more detail front loaded, and more detail here.
## Sprint 9
## Sprint 10
## Sprint 11
## Sprint 12
## Sprint 13
## Sprint 14
## Sprint 15
## Sprint 16