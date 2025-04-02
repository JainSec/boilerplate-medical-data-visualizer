import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('/workspace/boilerplate-medical-data-visualizer/medical_examination.csv')

# 2
df['height_meters_2'] = df['height']/100 * df['height']/100
df['BMI'] = df['weight'] / df['height_meters_2']
df.drop(columns=['height_meters_2'], inplace=True)
def overweight(BMI):
    if BMI > 25:
        return 1
    else:
        return 0
df['overweight'] = df['BMI'].apply(overweight)
df.drop(columns=['BMI'], inplace=True)

# 3
def checker(value):
    if value <=1:
        return 0
    else:
        return 1

df['cholesterol'] = df['cholesterol'].apply(checker)
df['gluc'] = df['gluc'].apply(checker)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar', height=5, aspect=1)
    g.set_axis_labels("variable", "total")

    # 8
    fig = g.fig

    # 9
    fig.savefig('catplot.png')
    return fig
    


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    df_heat = df_heat.drop(columns=['BMI'], errors='ignore')
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', square=True, linewidths=.5, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
