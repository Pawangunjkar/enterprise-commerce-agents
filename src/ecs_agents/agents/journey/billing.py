"""Journey: billing.

Domain journey / application *.
QR, GST invoice, dunning.
"""

from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='billing',
    title='Journey: billing',
    mission='QR, GST invoice, dunning.',
    tools=('payment-gateway-service.create_bharat_qr', 'invoice-service.issue_invoice', 'dunning-service.dunning_schedule', 'gst-tax-engine.compute_gst'),
    keywords=('billing journey', 'collections journey'),
    scenario='billing-invoice-dunning',
)
