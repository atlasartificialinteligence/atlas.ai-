# TOOLS.md

## Environment Notes

### OpenClaw Runtime

- Main OpenClaw instance runs on a VPS, not on Erick's local machine.
- Telegram access can work even when the local Control UI is not tunneled.

### SSH / Control Access

- OpenClaw Control UI is typically accessed from Erick's Mac using an SSH local tunnel.
- Example tunnel:
  - `ssh -L 18789:127.0.0.1:18789 openclaw@100.106.52.10`
- After the tunnel is active, the Control UI is available at:
  - `http://127.0.0.1:18789/`

### Operational Reminder

- The SSH tunnel is for local browser access to the Control UI.
- It is not the same thing as the Gateway process itself.
- Cronjobs and heartbeats depend on the Gateway running on the VPS, not on the SSH tunnel being open on Erick's Mac.
