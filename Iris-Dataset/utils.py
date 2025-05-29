import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def boxplots(dataframe: pd.DataFrame, numeric_features: list, target: str, ncols: int=5, nrows: int=5, figsize: tuple=(10,10)) :
    """
     Generates a box plot for all the numeric features present in your dataframe
    """

    fig = plt.figure(figsize=figsize)

    for i, col in enumerate(numeric_features) :
        ax = fig.add_subplot(nrows, ncols, i+1)
        sns.boxplot(data=dataframe, x=col, hue=target, orient='h', ax=ax)
        ax.set_title(col)

    fig.suptitle("Box Plots of Numeric Columns")
    fig.tight_layout()
    plt.show()

def histplots(dataframe: pd.DataFrame, numeric_features: list, target: str, ncols: int=5, nrows: int=5, figsize: tuple=(10,10)) :
    """
     Generates a histogram plot for all the numeric features present in your dataframe showing their density distribution
    """

    fig = plt.figure(figsize=figsize)

    for i, col in enumerate(numeric_features) :
        ax = fig.add_subplot(nrows, ncols, i+1)
        sns.histplot(data=dataframe, x=col, ax=ax, kde=True, color="blue", hue=target)
        ax.set_title(col)

    fig.suptitle("Distribution of Numeric Columns")
    fig.tight_layout()
    plt.show()