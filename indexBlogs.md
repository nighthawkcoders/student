---
layout: blogs
permalink: /blogs
title: Blogs
--- 
View my Github page [https://github.com/sumedhaKl] 
## Blog 
![The San Juan mountains are beautiful!](assets/images/san-juan-mountains.jpg "San Juan Mountains")

So, <mark>what will our blog be about?</mark> 
## Overview of Hacks, Study and Tangibles
Blogging in GitHub pages is a way to learn and code at the same time.
- Plans, Lists, [Scrum Boards](https://clickup.com/blog/scrum-board/) help you to track key events, show progress and record time.  Effort is a big part of your class grade.  Show plans and time spent!
- [Hacks(Todo)](https://levelup.gitconnected.com/six-ultimate-daily-hacks-for-every-programmer-60f5f10feae) enable you to stay in focus with key requirements of the class.  Each Hack will produce Tangibles.
- Tangibles or [Tangible Artifacts](https://en.wikipedia.org/wiki/Artifact_(software_development)) are things you accumulate as a learner and coder.
ClickUpClickUp
How to Build and Use a Scrum Board (With Examples) | ClickUp
Want to learn about Scrum boards? This article highlights what they are, how to use them and how to build one.
Written by
Erica Chappell
Est. reading time
18 minutes
Apr 7th, 2022
https://clickup.com/blog/scrum-board/

Medium]
15 Ultimate Daily Hacks for Every Programmer
You don’t need to import TensorFlow to print “hello world”
Reading time
7 min read
Apr 25th, 2021 (148 kB)
https://levelup.gitconnected.com/six-ultimate-daily-hacks-for-every-programmer-60f5f10feae

Wikipedia
Artifact (software development)
An artifact is one of many kinds of tangible by-products produced during the development of software. Some artifacts (e.g., use cases, class diagrams, and other Unified Modeling Language (UML) models, requirements and design documents) help describe the function, architecture, and design of software. Other artifacts are concerned with the process of development itself—such as project plans, business cases, and risk assessments.
The term artifact in connection with software development is largely associated with specific development methods or processes e.g., Unified Process. This usage of the term may have originated with those methods.
Build tools often refer to source code compiled for testing as an artifact, because the executable is necessary to carrying out the testing plan.  Without the executable to test, the testing plan artifact is limited to non-execution based testing.  In non-execution based testing, the artifacts are the walkthroughs, inspections and correctness proofs.  On the other hand, execution based testing requires at minimum two artifacts: a test suite and the executable.  Artifact occasionally may refer to the released code (in the case of a code library) or released executable (in the case of a program) produced, but more commonly an artifact is the byproduct of software development rather than the product itself. Open source code libraries often contain a testing harness to allow contributors to ensure their changes do not cause regression bugs in the code library.
Much of what are considered artifacts is software documentation.
In end-user development an artifact is either an application or a complex data object that is created by an end-user without the need to know a general programming language. Artifacts describe automated behavior or control sequences, such as database requests or grammar rules, or user-generated content.
Artifacts vary in their maintainability.  Maintainability is primarily affected by the role the artifact fulfills.  The role can be either practical or symbolic.  In the earliest stages of software development, artifacts may be created by the design team to serve a symbolic role to show the project sponsor how serious the contractor is about meeting the project's needs.  Symbolic artifacts often convey information poorly, but are impressive-looking. Symbolic enhance understanding.  Generally speaking, Illuminated Scrolls are also considered unmaintainable due to the diligence it requires to preserve the symbolic quality.  For this reason, once Illuminated Scrolls are shown to the project sponsor and approved, they are replaced by artifacts which serve a practical role.  Practical artifacts usually need to be maintained throughout the project lifecycle, and, as such, are generally highly maintainable.
Artifacts are significant from a project management perspective as deliverables. The deliverables of a software project are likely to be the same as its artifacts with the addition of the software itself.
The sense of artifacts as byproducts is similar to the use of the term artifact in science to refer to something that arises from the process in hand rather than the issue itself, i.e., a result of interest that stems from the means rather than the end.
To collect, organize and manage artifacts, a Software development folder may be utilized.
// POST: api/Todo
[HttpPost]
public async Task<ActionResult<TodoItem>> PostTodoItem(TodoItem item)
{
   _context.TodoItems.Add(item);
   await _context.SaveChangesAsync();

   return CreatedAtAction(nameof(GetTodoItem), new { id = item.Id }, item);
}
Show less