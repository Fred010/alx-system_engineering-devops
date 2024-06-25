# Postmortem Report: System Outage on June 24, 2024

## Issue Summary

**Duration**: June 24, 2024, 10:00 AM - 2:30 PM (UTC)

**Impact**: The main website experienced significant downtime, rendering the service unavailable to users. Approximately 80% of our users were unable to access the site, resulting in a surge of support tickets and customer complaints.

**Root Cause**: The outage was caused by a misconfiguration in the database connection pool settings, leading to resource exhaustion and failure to handle incoming requests.

## Timeline

- **10:00 AM**: Issue detected by monitoring alert indicating high database response times.
- **10:05 AM**: On-call engineer confirmed the issue by noticing the website was not loading.
- **10:10 AM**: Initial investigation into web server logs and application error logs commenced.
- **10:30 AM**: Misleading investigation path: suspected DDoS attack due to traffic spike patterns.
- **11:00 AM**: Escalated to the Database Team for further analysis.
- **11:15 AM**: Database Team identified high connection counts and slow queries.
- **12:00 PM**: Further misleading path: assumed issue with specific slow queries and began optimizing them.
- **1:00 PM**: Realized misconfiguration in the connection pool settings after reviewing configuration files.
- **1:30 PM**: Configuration changes applied and database connection pool settings updated.
- **2:00 PM**: Services gradually restored and monitoring confirmed normal operation.
- **2:30 PM**: Full service restoration confirmed, post-incident review initiated.

## Root Cause and Resolution

**Root Cause**:
The primary cause of the outage was a misconfigured database connection pool. The pool was set to allow an unlimited number of connections, leading to resource exhaustion on the database server. As the number of incoming requests surged, the database server could not handle the load, causing slow queries and eventually making the website inaccessible.

**Resolution**:
The issue was resolved by updating the database connection pool settings to a fixed, manageable number of connections. This involved:
1. Accessing the database configuration files.
2. Setting the maximum number of connections to a value that the database server could handle efficiently.
3. Restarting the application servers to apply the new settings.
4. Monitoring the system to ensure stability and normal operation post-fix.

## Corrective and Preventative Measures

**Improvements**:
- Implement stricter configuration reviews to avoid similar misconfigurations.
- Enhance monitoring to detect and alert on resource exhaustion conditions earlier.
- Conduct regular load testing to understand the limits of our infrastructure.

**Tasks**:
1. **Patch Database Configuration**: Update the configuration templates to ensure appropriate connection limits are set.
2. **Add Monitoring**: Implement monitoring for database connection pool usage and alert thresholds for high usage.
3. **Conduct Training**: Provide additional training for engineers on best practices for configuration management.
4. **Regular Load Testing**: Schedule and perform quarterly load tests to evaluate system performance under stress.
5. **Incident Review Process**: Enhance the post-incident review process to include a step-by-step analysis of misleading paths taken during the investigation.

By implementing these measures, we aim to prevent similar incidents in the future and improve our response time and accuracy in diagnosing and resolving system issues.
