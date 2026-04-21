# MicrosoftPurviewPolicyDistribution Bicep Module

Azure service tag: **MicrosoftPurviewPolicyDistribution**

## Overview

This directory contains Bicep variable files for the **MicrosoftPurviewPolicyDistribution** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **MicrosoftPurviewPolicyDistribution.bicep** - Global/cloud-wide IP address ranges
- **region/MicrosoftPurviewPolicyDistribution_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global MicrosoftPurviewPolicyDistribution module to access all IP ranges for this service tag:

```bicep
import * as microsoftpurviewpolicydistribution from './MicrosoftPurviewPolicyDistribution.bicep'

// Use the variable in your template
var allowedIPs = microsoftpurviewpolicydistribution.MicrosoftPurviewPolicyDistribution
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as microsoftpurviewpolicydistributionEastUS from './region/MicrosoftPurviewPolicyDistribution_EastUS.bicep'

// Use the regional variable
var eastUSIPs = microsoftpurviewpolicydistributionEastUS.MicrosoftPurviewPolicyDistribution_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: MicrosoftPurviewPolicyDistribution
- **Module Directory**: microsoft-purview-policy-distribution
