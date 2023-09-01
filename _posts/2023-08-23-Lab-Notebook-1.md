---
layout: post
title: Lab Notebook 1
description: Progress with hacks for week 1!
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 1}}
---

# Java Hello



```java
// class definition
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    // constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    // method to start the car
    public void start() {
        isRunning = true;
        System.out.println(year + " " + make + " " + model + " is now running.");
    }

    // method to stop the car
    public void stop() {
        isRunning = false;
        System.out.println(year + " " + make + " " + model + " has stopped.");
    }

    // method to check if the car is running
    public boolean isCarRunning() {
        return isRunning;
    }

    // method to set the year of the car
    public void setYear(int newYear) {
        year = newYear;
    }

    // method to get the year of the car
    public int getYear() {
        return year;
    }

    // method to get the make of the car
    public String getMake() {
        return make;
    }

    // method to get the model of the car
    public String getModel() {
        return model;
    }
}

public class CarExample {
    public static void main(String[] args) {
        // instantiate an object of the Car class
        Car myCar = new Car("Toyota", "Camry", 2023);

        // call methods on the object
        myCar.start();
        System.out.println(myCar.getYear() + " " + myCar.getMake() + " " + myCar.getModel() + " is running.");

        myCar.stop();
        System.out.println(myCar.getYear() + " " + myCar.getMake() + " " + myCar.getModel() + " has stopped.");

        // method to change the year of the car
        myCar.setYear(2024);
        System.out.println("Updated year of the car: " + myCar.getYear());
    }
}

CarExample.main(null);

```

    2023 Toyota Camry is now running.
    2023 Toyota Camry is running.
    2023 Toyota Camry has stopped.
    2023 Toyota Camry has stopped.
    Updated year of the car: 2024


## Explain Anatomy of a Class in comments of program (Diagram key parts of the class):


```java
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    // constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    // method to start the car
    public void start() {
        isRunning = true;
        System.out.println(year + " " + make + " " + model + " is now running.");
    }

    // method to stop the car
    public void stop() {
        isRunning = false;
        System.out.println(year + " " + make + " " + model + " has stopped.");
    }

    // method to check if the car is running
    public boolean isCarRunning() {
        return isRunning;
    }

    // method to set the year of the car
    public void setYear(int newYear) {
        year = newYear;
    }

    // method to get the year of the car
    public int getYear() {
        return year;
    }

    // method to get the make of the car
    public String getMake() {
        return make;
    }

    // method to get the model of the car
    public String getModel() {
        return model;
    }
}
```

In this code snippet, the anatomy of the Car class is explained with comments:

- The class is defined using the class keyword.
- It has instance variables (make, model, year, isRunning) that hold information about the car's attributes.
- A constructor is defined with parameters (make, model, year) that initialize the instance variables.
- The class also contains other methods (not shown) to interact with the car object.

## Comment for Class Definition and Object Instantiation:


```java
// Class definition
class Car {
    // ...
}

public class CarExample {
    public static void main(String[] args) {
        // Instantiate an object of the Car class
        Car myCar = new Car("Toyota", "Camry", 2023);
        // ...
    }
    // ...
}
```

In this code snippet, the anatomy of the Car class is explained with comments:

- The class is defined using the class keyword.
- It has instance variables (make, model, year, isRunning) that hold information about the car's attributes.
- A constructor is defined with parameters (make, model, year) that initialize the instance variables.
- The class also contains other methods (not shown) to interact with the car object.

## Comment in code where there is a definition of a Class and an instance of a Class (ie object):


```java
// class definition
class Car {

}

//instantiate an object of the Car class
Car myCar = new Car("Toyota", "Camry", 2023);

```

- The class is defined with the comment "Class definition."
- An instance of the Car class is created and assigned to the variable myCar.
- This line instantiates a new car object with the make "Toyota," model "Camry," and year 2023.

## Comment in code where there are constructors and highlight the signature difference in the signature:


```java
class Car {
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }
}
```

- The comment "Constructor" indicates the presence of a constructor within the Car class.
- The constructor has a signature that includes three parameters: make (String), model (String), and year (int). This signature defines the inputs required to create an instance of the class.

## Call an object method with a parameter (i.e., setters):


```java
// method to set the year of the car
public void setYear(int newYear) {
    year = newYear;
}

// call the setYear method with a new year value
setYear(myCar, 2024);
```

- The comment "Method to set the year of the car" identifies a method used for setting the year of the car object.
- The method takes a parameter newYear (int) that represents the new year value.
- The method is called later with the line "setYear(myCar, 2024);", where myCar is the object on which the method is being called, and 2024 is the new year value being passed as an argument.

# Java Console Games

## Make RPS, Tic-Tack-Toe, and Higher Lower into different cells and objects.  Document each cell in Jupyter Notebooks.

### RPS
<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/08/30/Rock-Paper-Scissors.html">Here</a></li>
</html>

### Tic-Tack-Toe
<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/08/30/Tic-Tack-Toe.html">Here</a></li>
</html>

### Higher or Lower
<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/08/30/Higher-Lower.html">Here</a></li>
</html>

##


```java

```
