"""E-way bill.

Domain billing / application gst-tax-engine.
E-way bill required flag when taxable exceeds threshold.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='gst-tax-engine',
    slug='eway-bill',
    title='E-way bill',
    mission='E-way bill required flag when taxable exceeds threshold.',
    tools=('gst-tax-engine.eway_bill',),
    keywords=('e-way', 'eway', 'e-way bill', 'eway bill'),
)
