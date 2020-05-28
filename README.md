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

### Notes

You want aggregation right? So everything up to that date.

Hmmm so maybe some scaling is needed. H264 is so popular it fades out the trend in the other codecs.

How would you feel about showing it as a percentage of the total at that date. As in still aggregation. But rather than raw counts. Normalized to percentage. That way you can see the relation better. 

Ok I set you up with a very very basic plot

And the data frame as you need it to do what you need

I explain in the email that I use plotly because it’s interactive

The python script has links to the docs

But I highly recommend playing with it inside a jupytwr notebook which I’ve also included

You can easily change it to a bar chart or any other type of plot

I don’t love bar charts

You can also do a rolling average

I would definitely recommend a rolling average

I think that intuitively is a better measure

Because of course overtime things will increase but that gives you what’s happening as a trend line

I’d do it more detailed but I think you are very capable of figuring out the code and I have to go back to this course I’m taking on databases

But totally use the notebook Inside vs code

But don’t spend too much time working on making plots perfect - guilty of that myself

And then I lose track of time

If you want to do forecasting

You can try looking into Facebook prophet

## date_vs_accummulated_codec_plot

Attached is the python script to create the plots from videos_export.csv
Also attached is the plots it produces.

I choose to use log scale to show the accumulated totals, so we could see the different orders of magnitude.  Clearly h264 is still dominant, and vp8 is secondary in overall usage.
However, hevc is up and coming, seeing the most relative growth of them all.

I also included the raw codec data vs date plot.  This shows how h264 cratered at the start of 2020, and has roughly equal usage with hevc this year.

I'm not sure if this is the story you were looking for, but it is the data that was given to me!
The script itself is actually quite complicated, because sorting dates in python is not straightforward (you have to use datetime objects, which are powerful but confusing)

### Notes

Matplotlib is probably the best plotting library in existence right now

[You can read csvs into python using numpy.Loadtxt](https://pythonspot.com/matplotlib-histogram/)

I like matplotlib over plotly. plotly is good for pandas.