# DataCamp Course Style Guidelines

You will need to follow DataCamp's style guidelines for your course to help create a consistent look and feel for students. While you may have your own preferred style, these style guidelines are what DataCamp students are familiar with, and your style may not be understood if it's not clear when you are referring to specific pieces of the code. Make sure to adhere to **all** of the following in your course.

# Grammar
## Use American English

Since we are an American company and the USA contains our largest group of students, DataCamp content is written in American English.

  

*   _Correct:_ This standardizes the modeling of colors.
*   _Incorrect:_ This standardises the modelling of colours.

  

Using American English also means using American punctuation rules.

  

*   Commas, periods, and exclamation marks should be placed inside quotation marks when applicable. Ex: “I love DataCamp,” said Michael.
*   Include a comma after the following abbreviations: i.e., e.g.,

## Use full sentences

Learners will read the content you create, and you will not be there to clarify what you've written, so make sure to use full, properly punctuated, and **clear** sentences.

# Spacing and punctuation
## Comma usage

Use the Oxford comma when writing content. The Oxford comma places a comma between the word “and” or “or” and the last item in a list. Because DataCamp content frequently covers complex topics, the Oxford comma can be helpful to clarify the meaning of sentences.

  

*   _Good:_ DataCamp has courses in R, Python, SQL, and spreadsheets.
*   _Bad:_ DataCamp has courses in R, Python, SQL, and spreadsheets.

## Spacing

There should only be one space following punctuation marks and between sentences.

  

*   _Good:_ Calculate the sum. Print the value.
*   _Bad:_ Calculate the sum. Print the value.

## Hyphens

Use hyphens to link all the words in a compound adjective. Do not use a hyphen if the construction includes very or an adverb ending in -ly.

  

*   _Good:_ The company makes data-driven decisions.
*   _Bad:_ The company makes data driven decisions.
*   _Good:_ The project had quickly diminishing returns.
*   _Bad:_ The project had quickly-diminishing returns.

# Abbreviations
## Ampersands

Ampersands should not be used in place of "and."

  

*   _Good_: DataCamp has courses about data science and machine learning.
*   _Bad_: DataCamp has courses about data science & machine learning.

## Versus, vs.

Always use the full word “versus” in full sentences.

  

*   _Good_: When should I use R versus Python for data analysis?
*   _Bad:_ When should I use R vs. Python for data analysis?

  

Always use the lowercase abbreviation “vs.” in chapter, lesson, exercise, and slide titles.

*   _Good_: TensorFlow vs. Keras for Deep Learning

# Data-related terms
## DataFrames, data frames

When using one of these terms, follow the appropriate usage based on the context of coding language.

  

*   In the context of Python: DataFrame, DataFrames
*   In the context of R: data frame, data frames

## Dataset

Always write “dataset” as one word.

*   Correct: The course uses a large dataset.
*   Incorrect: The course uses a large data set.

# Formatting
## Use parentheses after function/method names

This formatting helps distinguish functions and methods from variable names.

  

*   _Good_: Call the `mean()` function.
*   _Bad_: Call the `mean` function.

  

Use a dot before method/attribute names

*   _Good:_ Use the `.fit()` method to fit your model.
*   _Bad:_ Use the `fit()` method to fit your model.

## Format functions, methods, statements, and package names as inline code

Module and library names should also be formatted this way.

  

*   _Good_: The `seaborn` package produces pretty plots.
*   _Bad_: The _seaborn_ package produces pretty plots.

## Packages

Follow the style of the original name of the package, including the original capitalization style. Even at the beginning of a sentence, packages should not be capitalized unless the package name is capitalized.

  

*   _Good:_ `forcats` is an R package for working with categorical data.
*   _Bad:_ `Forcats` is an R package for working with categorical data.

# Code
## Code style

Follow these standard style guides for any code in exercises or code written on slides.

*   R: [The tidyverse style guide](http://style.tidyverse.org/)
*   Python: [PEP 8](https://www.python.org/dev/peps/pep-0008)
*   SQL: [Holywell's SQL Style guide](https://www.sqlstyle.guide/)
*   Shell: [Shell Style Guide](https://google.github.io/styleguide/shell.xml)
*   C++ (for `rcpp`): [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

## Code comments

Start each comment on a _new_ line, not on the same line as the code. It is _not_ okay to do this to ensure your code fits our 15 line limit.

_Good_:

```r
# Calculate the sum of x
y <- sum(x)
```

_Bad_:

```r
y <- sum(x) # Calculate the sum of x
```

Add a single space after the comment character.

_Good_:

```r
# Calculate the sum of x
y <- sum(x)
```

_Bad_:

```r
#Calculate the sum of x
y <- sum(x)
```

Capitalize the first letter of every comment.

_Good_:

```r
# Calculate the sum of x
y <- sum(x)
```

_Bad_:

```r
# calculate the sum of x
y <- sum(x)
```

If you have one sentence, don't use ending punctuation.

_Good_:

```r
# Calculate the sum of x
y <- sum(x)
```

_Bad_:

```r
# Calculate the sum of x.
y <- sum(x)
```

If you have multiple sentences in your comment, end each with a period. However, keep comment length short (< 60 characters).

  

G_ood_:

```r
# Calculate the sum of x. Assign the result to y.
y <- sum(x)
```

_Bad_:

```r
# Calculate the sum of x.  Assign the result to y
y <- sum(x)
```

Don't use backticks or quotes to refer to variables or functions inside comments.

_Good_:

```r
# Calculate the sum of x
y <- sum(x)
```

_Bad_:

```r
# Calculate the sum of `x`
y <- sum(x)
```

Code comments must be identical for sample code and solution code.

_Good_:

```less
@sample_code
# Calculate the sum of x
y <- ___(___)

@solution_code
# Calculate the sum of x
y <- sum(x)
```

_Bad_:

```less
@sample_code
# Calculate the sum of x
y <- ___(___)

@solution_code
# Use sum() on x
y <- sum(x)
```

# Instructions and hints
## Instructions

Instructions should be bulleted, even if there is only one instruction. All instructions should have ending punctuation, even if the last word is formatted as inline code.

## Hints

Hints should also be bulleted and always have ending punctuation.