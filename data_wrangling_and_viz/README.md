# Week 6: Data Wrangling and Visualisation

## Weekly Learning Outcomes

> - Apply data wrangling techniques for the grouping and reshaping of simple data sets  (MLO 2)
> - Select and present the results of data analysis through appropriate visualisation  (MLO 2)
> - Demonstrate the considerations required when handling time-series data ( MLO 1)

<details><summary><h2>Reading for this Week</h2></summary>

### Lesson 1

Core text : Section 8.1, 8.2 and 8.3

### Lesson 2

Core text : Chapter 9

### Lesson 3

Core text : Chapter 10

### Lesson 4

Core text : Chapter 11
</details>

So, just like Week 4, there isn't much to write about here. Everything can realistically be found in the core textbook, and rewriting it all here would be too time-consuming and perhaps infringing on copy-pasting. So take my word for it, I've completed some exercises that exemplify data manipulation and visualisation.

## Activity 1

### Exercise 1.1

Using a given dataset, manipulate it so that it can be read in two given formats. This required:

- `MultiIndex`s

Nice and simple, just read in a file that looks awful, then build up the `MultiIndex`s for both rows and columns

### Exercise 1.2

Given another dataset, merge it with the first dataset and perform some data manipulation tasks:

- `merge()`
- `groupby()`

The textbook mentions using `.pivot()`, `.melt()`, `.stack()` and `.unstack()` but `.groupby()` proved to be pretty useful for this.

## Activity 2

### Exercise 2.1

Investigate how Matplotlib can be integrated with Tkinter. It can be done using the `matplotlib.backends.backend_tkagg` module that contains a bunch of Tkinter widgets that are written as if they are matplotlib items. For example, we use `FigureCanvasTkAgg` to do most of the legwork, producing a canvas that be used in a tkinter GUI. We can also use `NavigationToolbar2Tk` to create a navigation bar to zoom into and pan around a figure.

### Exercise 2.2

Using the merged data from the previous activity, find out:

1. What is the overall success rate (pass or above in year 2) of all students in each of the subject areas?
2. Compare the year 1/year 2 performance in all subjects for each college

and present it in a suitable format. For me, that was pie charts. This is useful because it shows me the percentage of passes/fails in each subject. I didn't do the second one since it took so long to figure out the first one lmaooo

### Exercise 2.3

Given reasoning for the above representation. Pie charts. Cos percentages. Yeah

### Exercise 2.4

Find a way to embed this into a prototype GUI

Omg this is beautiful I'm so chuffed with it it's unreal. Managed to get a figure placed in the GUI by a Plot button, then I have some other navigation buttons that cycle through the different charts that I have :)
