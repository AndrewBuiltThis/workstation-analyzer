# Workstation Analyzer

### You are too smart to have to be dealing with users who can't tell you the information you need about their machines.

### To quote my dad's favorite artist, 🎵*times they are'a changin'*🎵

![Workstation Analyzer Output](/workstation-analyzer.png?raw=true "Workstation Analyzer")

This application was built for a simple purpose: to allow system administrators and analysts to get relevant information on a machine without needing to go back-and-forth with customers *and* to allow information to get collected in a programmatic and consistent manner. I extended this beyond a simple output (JSON) and used a Pythonic templating engine to create an interactive HTML report.

# Here's How It Works

The application has a few moving parts that were kept in isolation so that folks can easily modify and deploy this application for their area. The application uses:
* The Windows OS
* Python 2.7; and
* Jinja2, a Pythonic HTML Templating Engine;

I originally wrote this to operate on Linux, but after much ado, I decided to first release the Windows version as most organization's desktop users use Windows rather than Linux. #SAD!

## What to Expect
This application is initiated via the .bat file, meaning that this is a command-line interface *only* for inputting data. The .bat file effectively serves as an input form to collect specific information on you, the organization and any specific tests you want to run (network test endpoints, open ports, etc.). The .bat file will run the analysis and create both a JSON file and an HTML document. My eventual plan is to integrate this with a MongoDB backend to store the results, but this is the lightweight version.

## How To Make it Work For You

CHILL, HOMIE. But okay, here's the skinny:

1. Ensure that Python 2.7 is setup *and* set in the machine's environmental PATH variable. I didn't build a ton of error-logging on this since, well, I'll be using it too and I made it for me, too :);
2. Make sure you're running on a Windows machine. I tested this on Windows 10 and a good bit of the parsing *may be OS specific* but I don't know. Test it and tell me!
3. Ensure that the directory you plop this into that you have read-write access to. Otherwise, ya know, it won't create anything; and
4. Do not remove any of the GTG (Geographic Technologies Group) references! Why? Well, I work there and I made this while there and it would be kinda rude to do so. Plus I think we have a legal team, so **obey my commands**

## Known Limits
1. This code *for sure* can be cleaned up and significantly refactored -- that wasn't my priority in this #AppOfTheWeek, so we're on the same page;
2. I'll be adding inline code as we go along ... no need to fear;
3. Two components, the user-table and the available network table, aren't working as I'm running into some issues with how Python and JavaScript handle specific object types. That'll be fixed shortly. However, the raw data (JSON file) is correct; and
4. As I already said, don't remove any of the crediting information from any of the elements. It would be a real d-move. 

Feel free to reach out for help or question!

Cheers,
A
