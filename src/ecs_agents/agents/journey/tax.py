"""Journey: tax desk.

Domain journey / application *.
GST + e-way + TCS 194O across billing engines.
"""

from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='tax',
    title='Journey: tax desk',
    mission='GST + e-way + TCS 194O across billing engines.',
    tools=('gst-tax-engine.compute_gst', 'gst-tax-engine.eway_bill', 'tcs-tds-compliance-engine.compute_tcs_194o'),
    keywords=('tax desk', 'gst journey'),
    scenario='gst-interstate-eway',
)
