# OpenAgents Manual Setup Guide (Fix for PATH issue)

It seems the `openagents` command isn't in your system PATH. We can fix this by using the full path to the executable.

## 1. Clean Structure Plan

Please ensure your folder looks like this (we will create `academic_network`):

```text
d:\Profolio\文章\Thesis\Graduate-thesis\
├── academic_network\       <-- [NEW] The OpenAgents runtime environment
│   └── agents\             <-- We will put our agents here
├── Reflections\
│   └── Hackathon\
│       └── agents\         <-- [SOURCE] Where we designed our agents
└── ...
```

## 2. Manual Commands

Please open your PowerShell/Terminal and run these commands one by one.

### Step A: Initialize the Network
(We use the full path typically found on Windows User installs)

```powershell
# Try running with the full path
& "$env:APPDATA\Python\Python313\Scripts\openagents.exe" init ./academic_network
```

> **If that fails**, try this alternative:
> `python -m openagents.cli init ./academic_network`

### Step B: Install Our Agents
Now we copy the configuration files we wrote into the running network.

```powershell
# Create agents directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "academic_network/agents"

# Copy our defined agents to the network
Copy-Item "Reflections/Hackathon/agents/*.yaml" -Destination "academic_network/agents/" -Force
```

### Step C: Start the Network
Keep this terminal window open!

```powershell
& "$env:APPDATA\Python\Python313\Scripts\openagents.exe" network start ./academic_network
```

### Step D: Start the Studio
Open a **NEW** terminal window and run:

```powershell
& "$env:APPDATA\Python\Python313\Scripts\openagents.exe" studio -s
```

## 3. Verification

Go to [http://localhost:8050](http://localhost:8050). You should see the Studio interface.
We can then try to start an agent:

```powershell
# In a 3rd terminal
& "$env:APPDATA\Python\Python313\Scripts\openagents.exe" agent start ./academic_network/agents/literature_agent.yaml
```
