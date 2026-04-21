# KustoAnalytics Bicep Module

Azure service tag: **KustoAnalytics**

## Overview

This directory contains Bicep variable files for the **KustoAnalytics** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **KustoAnalytics.bicep** - Global/cloud-wide IP address ranges
- **region/KustoAnalytics_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global KustoAnalytics module to access all IP ranges for this service tag:

```bicep
import * as kustoanalytics from './KustoAnalytics.bicep'

// Use the variable in your template
var allowedIPs = kustoanalytics.KustoAnalytics
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as kustoanalyticsEastUS from './region/KustoAnalytics_EastUS.bicep'

// Use the regional variable
var eastUSIPs = kustoanalyticsEastUS.KustoAnalytics_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: KustoAnalytics
- **Module Directory**: kusto-analytics
