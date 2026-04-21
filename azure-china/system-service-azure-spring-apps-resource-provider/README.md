# SystemServiceAzureSpringAppsResourceProvider Bicep Module

Azure service tag: **SystemServiceAzureSpringAppsResourceProvider**

## Overview

This directory contains Bicep variable files for the **SystemServiceAzureSpringAppsResourceProvider** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **SystemServiceAzureSpringAppsResourceProvider.bicep** - Global/cloud-wide IP address ranges
- **region/SystemServiceAzureSpringAppsResourceProvider_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global SystemServiceAzureSpringAppsResourceProvider module to access all IP ranges for this service tag:

```bicep
import * as systemserviceazurespringappsresourceprovider from './SystemServiceAzureSpringAppsResourceProvider.bicep'

// Use the variable in your template
var allowedIPs = systemserviceazurespringappsresourceprovider.SystemServiceAzureSpringAppsResourceProvider
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as systemserviceazurespringappsresourceproviderEastUS from './region/SystemServiceAzureSpringAppsResourceProvider_EastUS.bicep'

// Use the regional variable
var eastUSIPs = systemserviceazurespringappsresourceproviderEastUS.SystemServiceAzureSpringAppsResourceProvider_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: SystemServiceAzureSpringAppsResourceProvider
- **Module Directory**: system-service-azure-spring-apps-resource-provider
