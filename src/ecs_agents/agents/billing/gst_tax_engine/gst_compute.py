"""GST compute.

Domain billing / application gst-tax-engine.
Intra CGST+SGST vs inter IGST on a taxable value.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='gst-tax-engine',
    slug='gst-compute',
    title='GST compute',
    mission='Intra CGST+SGST vs inter IGST on a taxable value.',
    tools=('gst-tax-engine.compute_gst',),
    keywords=('compute gst', 'cgst', 'sgst', 'igst', 'gst slab'),
    scenario='gst-interstate-eway',
)
