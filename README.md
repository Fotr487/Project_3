# Project_3
Final project for the Engeto Academy hurray.... xD
This project let you extract results of the Czech parliament elections from 2017. The source URL for this project can be found here
https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

Libraries
You can find the list of libraries needed for running this project in the file "requirements.txt".

Running the Elections Scraper
You will need two arguments to run the Elections Scraper project (main_scrapper.py):

The first one is URL you get when you click on 'X' which is in table under collumn ("Výběr okrsku");
The second one is the name for your file
The results will be downloaded and saved to a .csv file for you.

Example
Elections Scraper will get you the results of municipality Liberec:

First argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103
Second argument: results_liberec
The program will notify you once the process is coming to an end and when the process has finished:

THE JOB IS DONE ψ(｀∇´)ψ,
results_Liberec.csv  IS READY FOR CHECKING.
I HOPE YOU WILL USE THIS DATA FOR GOOD. XD
MAY THE FORCE BE WITH YOU...


Export sample:

ID Name Registered voters Envelopes Valid Votes

544531;Čtveřín;401;261;258;22;0;2;11;34;11;2;3;3;0;1;34;1;7;87;0;0;2;0;2;1;0;34;1

546607;Dětřichov;540;282;281;12;0;0;13;50;28;1;3;6;2;0;12;1;1;97;0;4;1;2;0;0;0;45;3

530468;Dlouhý Most;697;442;442;43;1;0;21;61;28;10;5;8;0;3;50;0;12;131;1;0;9;1;1;0;1;53;3

563994;Dolní Řasnice;415;229;227;19;0;0;8;34;17;2;1;1;0;0;15;0;5;82;1;0;1;0;0;0;0;40;1
