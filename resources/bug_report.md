# Bug Report

There are 2 bugs present in our application. They are listed below. Often times you will be given sparse information regarding a bug. The following simulates how bugs may be communicated to your team. Its our job to:

1) Make sense of what the bug reports are trying to convey.
2) Reproduce the bug on our end.
3) Run and evaluate your test suite to see if your tests address the bug.
4) Document and log a hypothesis about what could be wrong.
5) If no tests cover the bug, write one to address it and then implement the fix. If a unit test exists but is flawed, fix it and then make sure the implementation code corresponds with the test and serves as a solution the bug.
6) Document the fix in your debugging log and if necessary add additional guard rails prevent a similar bug in the future (skills, hooks etc).

   The following are bugs in this branch of the code:

---
Bug 1
**How to replicate:**

For some reason our system allows an empty string. We don't want that. Please handle
Try it yourself. You'll see it allows an empty string.

---

Bug 2 
**How to replicate:**

Our board is visualizing the Triage in an inverted format. When this adds up we won't see the most important ones at the top Please fix!
---
