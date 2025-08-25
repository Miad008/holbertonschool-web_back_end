# ES6 Classes Project

This project demonstrates core concepts of ES6 Classes including:

- Class definitions with constructors and private properties (`_property` convention)
- Getters and setters with type checking
- Instance and static methods
- Inheritance and method overriding
- Abstract classes simulation (enforcing method implementation)
- Symbol usage for unique method keys
- Custom behavior on type casting (`toString`, `valueOf`)

## Files Summary

- `0-classroom.js`: Basic class with constructor property
- `1-make_classrooms.js`: Function creating multiple ClassRoom instances
- `2-hbtn_course.js`: Class with getters/setters and type validation
- `3-currency.js`: Class with method returning formatted string
- `4-pricing.js`: Class using Currency class with static method for conversion
- `5-building.js`: Abstract class enforcing method override
- `6-sky_high.js`: Inherits from Building and overrides required method
- `7-airport.js`: Class overriding default string output (`toString`)
- `8-hbtn_class.js`: Custom casting to Number and String
- `9-hoisting.js`: Fix hoisting and usage errors in classes and instances
- `10-car.js`: Class cloning method using Symbol for private clone logic

## How to Run

- Use `npm run dev <file>` to run individual test files.
- Use `npm run full-test` to run all Jest tests.

## Requirements

- Node.js 20.x
- Jest, Babel, ESLint configured as per project setup

---

By following this project, you will master advanced ES6 class features, inheritance, method overriding, static methods, and metaprogramming basics.
