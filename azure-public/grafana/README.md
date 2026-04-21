# Grafana Bicep Module

Azure service tag: **Grafana**

## Overview

This directory contains Bicep variable files for the **Grafana** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **Grafana.bicep** - Global/cloud-wide IP address ranges
- **region/Grafana_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global Grafana module to access all IP ranges for this service tag:

```bicep
import * as grafana from './Grafana.bicep'

// Use the variable in your template
var allowedIPs = grafana.Grafana
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as grafanaEastUS from './region/Grafana_EastUS.bicep'

// Use the regional variable
var eastUSIPs = grafanaEastUS.Grafana_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: Grafana
- **Module Directory**: grafana
