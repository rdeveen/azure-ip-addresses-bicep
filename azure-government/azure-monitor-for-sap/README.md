# AzureMonitorForSAP Bicep Module

Azure service tag: **AzureMonitorForSAP**

## Overview

This directory contains Bicep variable files for the **AzureMonitorForSAP** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureMonitorForSAP.bicep** - Global/cloud-wide IP address ranges
- **region/AzureMonitorForSAP_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureMonitorForSAP module to access all IP ranges for this service tag:

```bicep
import * as azuremonitorforsap from './AzureMonitorForSAP.bicep'

// Use the variable in your template
var allowedIPs = azuremonitorforsap.AzureMonitorForSAP
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuremonitorforsapEastUS from './region/AzureMonitorForSAP_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuremonitorforsapEastUS.AzureMonitorForSAP_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureMonitorForSAP
- **Module Directory**: azure-monitor-for-sap
