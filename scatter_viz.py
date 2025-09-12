import plotly.express as px

def scatter_plot(df, x_axis='temperature', y_axis='depth'):
    """Create custom X-Y scatter plot"""
    fig = px.scatter(
        df, x=x_axis, y=y_axis, color='float_id',
        hover_data=['time','temperature','salinity','depth']
    )
    if y_axis == 'depth':
        fig.update_yaxes(autorange='reversed')
    if x_axis == 'depth':
        fig.update_xaxes(autorange='reversed')
    return fig

