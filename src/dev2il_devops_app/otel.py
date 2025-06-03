def setup_otel(app):
    import prometheus_client
    from opentelemetry import metrics
    from opentelemetry.exporter.prometheus import PrometheusMetricReader
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.system_metrics import SystemMetricsInstrumentor
    from opentelemetry.sdk.metrics import MeterProvider
    from opentelemetry.sdk.resources import SERVICE_NAME, Resource


    resource = Resource.create(attributes={
        SERVICE_NAME: app.title
    })
    prometheus_client.start_http_server(port=9000)
    reader = PrometheusMetricReader()
    provider = MeterProvider(resource=resource, metric_readers=[reader])
    metrics.set_meter_provider(provider)
    SystemMetricsInstrumentor().instrument()
    FastAPIInstrumentor.instrument_app(app)