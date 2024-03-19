import plotly.graph_objects as go

pio.templates["background"] = go.layout.Template(
    layout=dict(
        title_font=dict(family="Rockwell", size=24),
        font=dict(color="#f2f5fa"),
        paper_bgcolor="rgb(17,17,17)",
        plot_bgcolor="rgb(17,17,17)",
        title=dict(x=0.05),
        xaxis=dict(
            automargin=True,
            gridcolor="#283442",
            linecolor="#506784",
            ticks="outside",
            title={"standoff": 15},
            zerolinecolor="#283442",
            zerolinewidth=2,
        ),
        yaxis=dict(
            automargin=True,
            gridcolor="#283442",
            linecolor="#506784",
            ticks="outside",
            title={"standoff": 15},
            zerolinecolor="#283442",
            zerolinewidth=2,
        ),
    )
)
