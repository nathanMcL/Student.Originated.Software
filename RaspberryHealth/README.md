---
System Performance Data Collection:
---

---
Inspiration:
---
Wanting to improve on my data collection, and programming, while utilizing a Raspberry Pi with Debian GNU/Linux 11 Operating System, I want to automate the collection of the data. Once the data is collected, ssh from my remote Windows computer to the Raspberry Pi, locate the csv of collected data and download/copy the data remotely.

---
How to run our demo on our included data:

[![](https://mermaid.ink/img/pako:eNpt0s1ymzAQB_BX2dGpnYnzAD50xga7X8FOB5weIIetWWAn-nCFsEuN373CapvQhhMj_fRfsexZ7E1JYi4qaU77Bq2DLC40-GeRp33rSN2Z-rZtHmE2ezdE6QPE6HCA5ZuEdJf4w7eH_m04sRwNROcEWcO4fQnr0fXsVtMAcf7AdIKFlOAaumY9vkTZyQywCmin-XtHsE1hg4raqWss-bh1kMv-dbU2nR3gfb5m6cjCt34sSIC6hIwVTS0ffeCHEBjd7yAjdSCLrrNTmPKPAT7mkU-qjeWfBF95tmZInSVdu-Y3hoDpSHqATyE2wC8dSnb9JHTFdeMG-PxcftdiPS284bGDd4EkpIztJ-oFSgJKudZc8R61g5iOjI6N_qeR4_U2gcfcPr1SdyXDR2yD2pA7GfsEmcXKZ_9_hT_-Pvf0L4uRZQ-Lo2_pMxc3QpFVyKUfwfO4WAg_F4oKMfevJVXYSVeIQl88xc6ZtNd7MXe2oxvRHUr_E2LG2qIS8wpl61epZGdsEsb6Ot2XX9qv7mY?type=png)](https://mermaid.live/edit#pako:eNpt0s1ymzAQB_BX2dGpnYnzAD50xga7X8FOB5weIIetWWAn-nCFsEuN373CapvQhhMj_fRfsexZ7E1JYi4qaU77Bq2DLC40-GeRp33rSN2Z-rZtHmE2ezdE6QPE6HCA5ZuEdJf4w7eH_m04sRwNROcEWcO4fQnr0fXsVtMAcf7AdIKFlOAaumY9vkTZyQywCmin-XtHsE1hg4raqWss-bh1kMv-dbU2nR3gfb5m6cjCt34sSIC6hIwVTS0ffeCHEBjd7yAjdSCLrrNTmPKPAT7mkU-qjeWfBF95tmZInSVdu-Y3hoDpSHqATyE2wC8dSnb9JHTFdeMG-PxcftdiPS284bGDd4EkpIztJ-oFSgJKudZc8R61g5iOjI6N_qeR4_U2gcfcPr1SdyXDR2yD2pA7GfsEmcXKZ_9_hT_-Pvf0L4uRZQ-Lo2_pMxc3QpFVyKUfwfO4WAg_F4oKMfevJVXYSVeIQl88xc6ZtNd7MXe2oxvRHUr_E2LG2qIS8wpl61epZGdsEsb6Ot2XX9qv7mY)

---
Work in progress :)
<a href="https://asciinema.org/a/HrMKbH6qOB9BEQdnmsucGfUBO" target="_blank"><img src="https://asciinema.org/a/HrMKbH6qOB9BEQdnmsucGfUBO.svg" /></a>

---
How to run our tests and what they mean:
---
Utilzing and implementing SystemLog.sh bash script found in the SystemLogResources folder to collect the data(you may need to change the bash script associated network).<br>
Once the csv has been generated you will have a collection of data with headers:<br>
Operating System Name, Date and Time, CPU Temperature, Wi-Fi strength measured by <br>
-dBm, Memory Usage, Disk Usage, Network Traffic Rx/Tx.


---
How we built it (your tech stack):
---
Raspberry Pi with Debian GNU/Linux 11 Operating System.
Pycharm & VS Code with Python 3.12.
Windows Surface Book


---
Challenges we ran into:
---
Trying to get the code files to mesh with MenuMain.<br>
Trying to schedule the crontab -e file with command to execute the program at set times.<br>
Trying to execute the program using Pycharm and in a separate IDE VS Code environment to simulate the Gitpod VS code environment prior to upload. <br>
Trying to debug the program in gitpod. Trying to create a comprehendible readme file.  <br>
 
---
Accomplishments that we're proud of:
---
So far everything!

---
What we learned:
---
Running the program in Pycharm, and Running the program with VS Code, is not Gitpod! Describing and articulating what this project is technically, is part of the process.  

---
What's next for the project next quarter (as an app engineered for the web):
---

Moving this project ahead for next quarter (8 Jan 2024). I am looking forward to improving the program's functions. I am working on incorporating another CSV file of data from a Raspberry pi Zero. I am excited to learn how I could better describe the data visually.

![Screenshot (427)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/0ad34771-2dea-4351-881b-777cdfdb418e)



---
Raspberry Health WireFrame
---


![RaspberryHealthwire_WireFrameLucid](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/7f2c8a86-a828-4e9a-889a-e0fe7b6e185d)

