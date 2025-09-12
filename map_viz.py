import plotly.express as px

def trajectory_map(df, color_option='temperature'):
    """Create animated map of ARGO float trajectories"""
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color=color_option,
        size_max=8,
        animation_frame=df['time'].astype(str),
        hover_name='float_id',
        hover_data=['depth','temperature','salinity'],
        projection='natural earth',
        title='Float Trajectories Over Time'
    )
    return fig
