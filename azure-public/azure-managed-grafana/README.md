# AzureManagedGrafana Bicep Module

Azure service tag: **AzureManagedGrafana**

## Overview

This directory contains Bicep variable files for the **AzureManagedGrafana** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureManagedGrafana.bicep** - Global/cloud-wide IP address ranges
- **region/AzureManagedGrafana_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureManagedGrafana module to access all IP ranges for this service tag:

```bicep
import * as azuremanagedgrafana from './AzureManagedGrafana.bicep'

// Use the variable in your template
var allowedIPs = azuremanagedgrafana.AzureManagedGrafana
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuremanagedgrafanaEastUS from './region/AzureManagedGrafana_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuremanagedgrafanaEastUS.AzureManagedGrafana_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureManagedGrafana
- **Module Directory**: azure-managed-grafana
