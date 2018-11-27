Title: My first talk: Slick 101 at ScalaMAD
Date: 2017-02-28
Category: Talks
Tags: scala,talks,slick,library,sql,programming,meetup
Slug: my-first-talk
Lang: en

Last 30th January 2017 I had the opportunity to give a talk at [ScalaMAD](https://www.meetup.com/Scala-Programming-Madrid/) MeetUp. The talk I prepared was: **[Slick 101](https://goo.gl/4d5WQ1)**.

### What is [Slick](http://slick.lightbend.com/)?

<img style="display: block; margin-left: auto; margin-right: auto" src="{static}/images/slick-101/slick-logo.png">

> “We don’t try to fight the relational model, we embrace it through a functional paradigm.”

[Slick](http://slick.lightbend.com/) is a library for Scala that makes it easy to work with relational databases. It is not a ORM (Object-Relational Mapping) as other libraries or frameworks like Hibernate. Instead, [Slick](http://slick.lightbend.com/) is a FRM (Functional Relational Mapping), which means it is implemented based on functional programming. Then main difference between FRM and ORM is that FRM does not hide the database in an abstraction layer like ORM. It gives us full control of our database and all the possible operations. It also works asynchronously, which makes [Slick](http://slick.lightbend.com/) a perfect library for reactive applications

### What was the content?

The main purpose of this talk was to introduce the core concepts to start working with [Slick](http://slick.lightbend.com/). To do it, we show how this library offers all database data as collections (`Collections`) from Scala, and what the advantages are of managing this collections from a functional programming point of view.

The content of the presentation was:

1. What is Slick?
2. Plain SQL
3. Slick DSL
  * Defining our Schema
  * Slick Operations
  * Operating with database
    * Selecting data
    * Inserting data
    * Deleting data
    * Updating data
4. Combining Actions

##### Some pictures from the event

<img style="display: block; margin-left: auto; margin-right: auto" src="{static}/images/slick-101/inserting-data.jpeg">

<img style="display: block; margin-left: auto; margin-right: auto" src="{static}/images/slick-101/inserting-data-2.jpeg">

<img style="display: block; margin-left: auto; margin-right: auto" src="{static}/images/slick-101/selecting-data.jpeg">

### Links

* Slides: [https://goo.gl/4d5WQ1](https://goo.gl/4d5WQ1)
* Event link: [https://www.meetup.com/Scala-Programming-Madrid/events/236355445/](https://www.meetup.com/Scala-Programming-Madrid/events/236355445/)
