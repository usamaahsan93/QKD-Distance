# Analysis of achievable distance of BB84 and KMB09 QKD Protocols
This is the source code of the mentioned [research paper](https://doi.org/10.1142/S0219749920500331).

This research is conducted by:

Muhammad Mubashir Khan
[![LinkedIn](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/linkedin-16x16.png)](https://www.linkedin.com/in/muhammad-mubashir-khan-251a802b/)
[![ORCID](https://ndownloader.figshare.com/files/8439032/preview/8439032/preview.jpg)](https://orcid.org/0000-0002-0011-9525)         
         
Asad Arfeen
[![ORCID](https://ndownloader.figshare.com/files/8439032/preview/8439032/preview.jpg)](https://orcid.org/0000-0002-2419-6621)
         
Usama Ahsan
[![LinkedIn](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/linkedin-16x16.png)](https://www.linkedin.com/in/usamaahsan93/)
[![ORCID](https://ndownloader.figshare.com/files/8439032/preview/8439032/preview.jpg)](https://orcid.org/0000-0002-4245-9851)
[![GitHub](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/github-16x16.png)](https://github.com/usamaahsan93)
[![Goodreads](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/goodreads-16x16.png)](https://www.goodreads.com/usamaahsan93)

Saneeha Ahmed

Tahreem Mumtaz

This research is transformed into an interactive work using Heroku App Visit the link [here](https://qkddistance.herokuapp.com/) for this.

### Required Packages
numpy == 1.15.1

matplotlib == 2.2.3

scipy == 1.1.0

pandas == 0.23.4

### Files used by Heroku App
1. Procfile
2. setup.sh
3. QKDdistance.py
4. requirements.txt

### Code files used in the research
1. OF_main.py : It shows the dispersion and relative loss of the optic fiber.
2. RsiftAndQBER.py : It generates the graph of Rsift and QBER for a given protocol specifications.
3. effKMB09.py : This code generates the efficiency of KMB09 protocol and determine the max efficiency obtained through it.
4. poissonCurve.py : This code generates the Poisson distirbution for different values of mu.
5. summaryGraph.py : This code generates the summary of all the attributes used and determine the optimal solution.


