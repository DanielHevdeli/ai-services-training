# Monitoring
### TODO:
- What are the differences between metrics, logs and traces.
- Watch [Prometheus 101](https://www.youtube.com/results?search_query=prometheus)
- What metric types exist in Prometheus?
- Read [Promql guide](https://valyala.medium.com/promql-tutorial-for-beginners-9ab455142085)

### Final Exercise:
- Locally deploy a Prometheus instance, a Grafana instance and a Linux VM.
- Deploy Node-Exporter on your linux vm and scrape it using prometheus.
- Connect your Prometheus to your Grafana.
- Build a basic Grafana dashboard with 4 panels (read the node exporter docs to understand what metrics it exposes):
  - CPU Usage - Shows the percentage of time the CPU spends doing work (not idle).
  - Memory Usage - Displays how much RAM is currently used on the host.
  - Disk Space - Shows available disk space for non-temporary filesystems.
  - Network Traffic - Shows how much data the system is receiving over the network per second.