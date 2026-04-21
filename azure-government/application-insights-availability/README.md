# ApplicationInsightsAvailability Bicep Module

Azure service tag: **ApplicationInsightsAvailability**

## Overview

This directory contains Bicep variable files for the **ApplicationInsightsAvailability** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ApplicationInsightsAvailability.bicep** - Global/cloud-wide IP address ranges
- **region/ApplicationInsightsAvailability_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ApplicationInsightsAvailability module to access all IP ranges for this service tag:

```bicep
import * as applicationinsightsavailability from './ApplicationInsightsAvailability.bicep'

// Use the variable in your template
var allowedIPs = applicationinsightsavailability.ApplicationInsightsAvailability
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as applicationinsightsavailabilityEastUS from './region/ApplicationInsightsAvailability_EastUS.bicep'

// Use the regional variable
var eastUSIPs = applicationinsightsavailabilityEastUS.ApplicationInsightsAvailability_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: ApplicationInsightsAvailability
- **Module Directory**: application-insights-availability
