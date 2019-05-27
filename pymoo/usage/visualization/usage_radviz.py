# START scatter2d_load
from pymoo.factory import get_problem
F = get_problem("zdt3").pareto_front()
# END scatter2d_load

# START scatter2d
from pymoo.analytics.visualization.pcp import pcp
pcp().add(F).show()
# END scatter2d


# START pcp_highlight
plot = pcp()
plot.set_axis_style(color="grey", alpha=0.5)
plot.add(F, color="grey", alpha=0.3)
plot.add(F[50], linewidth=5, color="red")
plot.add(F[75], linewidth=5, color="blue")
plot.show()
# END pcp_highlight


# START pcp_other
plot = pcp(title=("Run", {'pad': 30}),
           n_ticks=10,
           legend=(True, {'loc': "upper left"}),
           labels=["profit", "cost", "sustainability", "environment", "satisfaction", "time"]
           )

plot.set_axis_style(color="grey", alpha=1)
plot.add(F, color="grey", alpha=0.3)
plot.add(F[50], linewidth=5, color="red", label="Solution A")
plot.add(F[75], linewidth=5, color="blue", label="Solution B")
plot.show()
# END pcp_other

# START pcp_norm
plot.reset()
plot.normalize_each_axis = False
plot.bounds = [[1, 1, 1, 2, 2, 5], [32, 32, 32, 32, 32, 32]]
plot.show()
# END pcp_norm
