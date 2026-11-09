# AgentFabric Bicep Module

Azure service tag: **AgentFabric**

## Overview

This directory contains Bicep variable files for the **AgentFabric** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AgentFabric.bicep** - Global/cloud-wide IP address ranges
- **region/AgentFabric_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AgentFabric module to access all IP ranges for this service tag:

```bicep
import * as agentfabric from './AgentFabric.bicep'

// Use the variable in your template
var allowedIPs = agentfabric.AgentFabric
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as agentfabricEastUS from './region/AgentFabric_EastUS.bicep'

// Use the regional variable
var eastUSIPs = agentfabricEastUS.AgentFabric_EastUS
```

### From GitHub Container Registry (GHCR)

You can also import this module directly from GHCR:

`br:ghcr.io/rdeveen/azure-ip-addresses-bicep/azure-public/agent-fabric/agent-fabric:latest`



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AgentFabric
- **Module Directory**: agent-fabric
