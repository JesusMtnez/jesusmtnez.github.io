Title: Mi primera charla: Slick 101 en ScalaMAD
Date: 2017-02-28
Category: Talks
Tags: scala,talks,slick,library,sql,programming,meetup
Slug: my-first-talk
Lang: es

El pasado 30 de enero de 2017 tuve la oportunidad de asistir como ponente al MeetUp de [ScalaMAD](https://www.meetup.com/Scala-Programming-Madrid/), la comunidad de Scala de Madrid. La charla que preparé fué: **[Slick 101](https://goo.gl/4d5WQ1)**.

### ¿Qué es [Slick](http://slick.lightbend.com/)?

<img style="display: block; margin-left: auto; margin-right: auto" src="{filename}/images/slick-101/slick-logo.png">

> “We don’t try to fight the relational model, we embrace it through a functional paradigm.”

[Slick](http://slick.lightbend.com/) es librería de Scala que permite trabajar con bases de datos relacionales. A diferencia de librerías y frameworks como Hibernate, [Slick](http://slick.lightbend.com/) no es un ORM (Object-Relational Mapping), es un FRM (Functional Relational Mapping). Toda su implementación está basada en la programación funcional y a diferencia de los ORM, no nos oculta la base de datos tras una capa ORM, si no que nos da control completo sobre nuestra base de datos y las operaciones que se realizan sobre ella. Además todas las operaciones que se realizan son asíncronas, lo que hace de [Slick](http://slick.lightbend.com/) un librería perfecta para las aplicaciones reactivas.

### ¿Qué hicimos en la charla?

En esta charla introduje lo principales conceptos para poder trabajar con [Slick](http://slick.lightbend.com/). Además vimos como pone a disposición del programador toda la base de datos como colecciones (`Collections`) de Scala, y las ventajas asociadas a la hora de manejar estas colecciones desde un enfoque funcional.

El contenido de la presentación fué:

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

##### Algunas imágenes de la charla

<img style="display: block; margin-left: auto; margin-right: auto" src="{filename}/images/slick-101/inserting-data.jpeg">

<img style="display: block; margin-left: auto; margin-right: auto" src="{filename}/images/slick-101/inserting-data-2.jpeg">

<img style="display: block; margin-left: auto; margin-right: auto" src="{filename}/images/slick-101/selecting-data.jpeg">

### Enlaces de interés

* La presentación: [https://goo.gl/4d5WQ1](https://goo.gl/4d5WQ1)
* Enlace al evento: [https://www.meetup.com/Scala-Programming-Madrid/events/236355445/](https://www.meetup.com/Scala-Programming-Madrid/events/236355445/)
