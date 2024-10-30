# Q1: What action did Alex take to integrate the purported time-saving package into the deployment process? (provide the full command)

Into the classical powershell history file (ConsoleHost_history.txt), we find the nuget package installation :
![History](./assets/2024-09-22T22:56:27,889083437+02:00.png)

# Q2: Identify the URL from which the package was downloaded ?

Checking Web History :
![Url](./assets/2024-10-13T18_19_20,030404275+02_00.png)

# Q3: Who is the threat actor responsible for publishing the malicious package? (the name of the package publisher)

We go to the nuget package website and find the author :
![Author](./assets/2024-09-22T22:50:36,269150422+02:00.png)

# Q4: When did the attacker initiate the download of the package? Provide the timestamp in UTC format (YYYY-MM-DD HH:MM)

Shellbags enter the chat :
![Shellbags](./assets/2024-09-22T23:31:12,279787801+02:00.png)

# Q5: Despite restrictions, the attacker successfully uploaded the malicious file to the official site by altering one key detail. What is the modified package ID of the malicious package?

The ID term is quite confusing. It's my first time with nuget on forensics investigation. We quickly find the [.nuspec](https://learn.microsoft.com/en-us/nuget/reference/nuspec) file :
![Nuspec](./assets/2024-09-23T11:24:44,751570569+02:00.png)

# Q6: Which deceptive technique did the attacker employ during the initial access phase to manipulate user perception? (technique name)

We clearly see that we want to replicate the PublishIgnore string by deleting the "e". It's typosquatting.

# Q7: Determine the full path of the file within the package containing the malicious code ?

Go to nuget default package location :
![Path](./assets/2024-09-22T23:04:04,348522189+02:00.png)

# Q8: When tampering with the system's security settings, what command did the attacker employ?

At the start of the init.ps1 found before, we have 2 interesting command at the start :
![Tampering](./assets/2024-10-13T18_27_20,217521588+02_00.png)

# Q9: Following the security settings alteration, the attacker downloaded a malicious file to ensure continued access to the system. Provide the SHA1 hash of this file

When reading the powershell script, we quickly see the uninstall.exe. I basically do a research of the exe file on Autopsy. We find our hash in the Windows Defender MP Microsoft Protection logs ([MPLog](https://www.thedfirspot.com/post/windows-defender-mp-logs-a-story-of-artifacts)) :
![MPLog](./assets/2024-09-23T23:34:33,655079928+02:00.png)

# Q10: Identify the framework utilised by the malicious file for command and control communication.

TDB

# Q11: At what precise moment was the malicious file executed?

It's Prefetch time. Let's use the classic combo [PECmd](https://github.com/EricZimmerman/PECmd) + [TimelineExplorer](https://www.sans.org/tools/timeline-explorer/) from Eric Zimmerman.
We parse the prefetch directory and export the timeline in csv :
![PECmd](./assets/2024-09-23T16:18:53,985898322+02:00.png)
And now open in TimelineExplorer and search for our uninstall.exe :
![Timeline](./assets/2024-09-23T16:18:58,652206989+02:00.png)

# Q12: The attacker made a mistake and didn’t stop all the features of the security measures on the machine. When was the malicious file detected? Provide the timestamp in UTC.

We check event id [1117](https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus#event-id-1117) in the Microsoft-Windos-Windows Defender%4Operational. With the research of string uninstall.exe from Q9 I have a hit on this file too :
![Evtx](./assets/2024-09-23T16:40:54,982953179+02:00.png)

# Q13: After establishing a connection with the C2 server, what was the first action taken by the attacker to enumerate the environment? Provide the name of the process.

I go back to the prefetch timeline. Check just after Updater.exe, we find whoami :
![Whoami](./assets/2024-10-16T21_20_15,299323062+02_00.png)

# Q14: To ensure continued access to the compromised machine, the attacker created a scheduled task. What is the name of the created task?

We go to the default path C:\Windows\System32\Taks and check unusual task.
MicrosoftSystemDailyUpdate is what we looking for.

# Q15: When was the scheduled task created? Provide the timestamp in UTC.

We open the xml file :
![Task](./assets/2024-09-23T17:59:10,444476816+02:00.png)

# Q16: Upon concluding the intrusion, the attacker left behind a specific file on the compromised host. What is the name of this file?

We find an unusual Updater.exe on C:\ProgramData. So I open the file on VT :
![VT](./assets/2024-10-16T21_46_09,571966584+02_00.png)

# Q17: As an anti-forensics measure. The threat actor changed the file name after executing it. What is the new file name?

TBD

# Q18: Identify the malware family associated with the file mentioned in the previous question (17).

The 3 family labels present on the main page not match. So I check in Community, and find in the last post.

# Q19: When was the file dropped onto the system? Provide the timestamp in UTC.

We open the [Master File Table](https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table) in Timeline explorer after using [MFTECmd](https://github.com/EricZimmerman/MFTECmd). Same process as PECmd from Q11. We search for Updater.exe :
![MFT](./assets/2024-10-16T22_15_07,052799708+02_00.png)
