# graph-rolling-window
how to make a graph using accumulated sum over a rolling window

## plots.*

This is ROUGH CODE. 

I did a line chart instead of bar chart but if you look at the plotly documentation you can easily do something else. 

I recommend (if you have VSCODE you just have to open the file and it will work) but I use Jupyter notebooks to explore things. I am including my notebook here and the plots are interactive inside Jupyter so you can play around with it until you like it. 

You need plotly-orca installed to save it as a static image. I’ve included the link to that in the python code.

Instead of calculating an aggregate sum up till now I actually recommend swapping that line of code with this:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html

```python
temp.rolling('30d').sum()
```

This would calculate the average usage past 30 days. 

## date_vs_accummulated_codec_plot

Attached is the python script to create the plots from videos_export.csv
Also attached is the plots it produces.

I choose to use log scale to show the accumulated totals, so we could see the different orders of magnitude.  Clearly h264 is still dominant, and vp8 is secondary in overall usage.
However, hevc is up and coming, seeing the most relative growth of them all.

I also included the raw codec data vs date plot.  This shows how h264 cratered at the start of 2020, and has roughly equal usage with hevc this year.

I'm not sure if this is the story you were looking for, but it is the data that was given to me!
The script itself is actually quite complicated, because sorting dates in python is not straightforward (you have to use datetime objects, which are powerful but confusing)