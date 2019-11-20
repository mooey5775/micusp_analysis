import os
from collections import deque

research = ["BIO.G0.02.6", "BIO.G0.03.1", "BIO.G0.03.2", "BIO.G0.03.3", "BIO.G0.04.2", "BIO.G0.04.3", "BIO.G0.07.2", "BIO.G0.07.3", "BIO.G0.08.1", "BIO.G0.10.1", "BIO.G0.10.2", "BIO.G0.11.2", "BIO.G0.12.1", "BIO.G0.14.1", "BIO.G0.17.1", "BIO.G0.21.1", "BIO.G0.22.1", "BIO.G0.23.1", "BIO.G0.27.1", "BIO.G0.28.1", "BIO.G1.02.1", "BIO.G1.05.1", "BIO.G2.01.1", "BIO.G2.03.1", "BIO.G2.04.1", "BIO.G3.01.1", "CEE.G0.01.2", "CEE.G0.01.3", "CEE.G0.03.1", "CEE.G0.04.1", "CEE.G0.05.1", "CEE.G0.06.1", "CEE.G1.02.1", "CEE.G3.01.1", "CEE.G3.02.1", "CEE.G3.03.1", "ECO.G0.06.1", "ECO.G0.08.1", "ECO.G1.01.1", "ECO.G1.02.1", "ECO.G1.03.1", "ECO.G2.01.1", "ECO.G2.04.1", "ECO.G2.05.1", "ECO.G2.08.1", "ECO.G3.01.1", "ECO.G3.02.1", "EDU.G1.03.1", "EDU.G1.05.1", "IOE.G0.02.1", "IOE.G0.05.1", "IOE.G0.10.1", "IOE.G1.01.1", "IOE.G1.02.2", "IOE.G1.02.4", "IOE.G1.07.1", "IOE.G1.08.1", "IOE.G2.01.1", "IOE.G2.03.1", "IOE.G3.01.1", "LIN.G0.01.1", "LIN.G0.03.1", "LIN.G0.04.1", "LIN.G0.07.1", "LIN.G0.08.1", "LIN.G0.10.2", "LIN.G1.01.1", "LIN.G1.01.2", "LIN.G1.01.3", "LIN.G1.01.4", "LIN.G1.01.5", "LIN.G1.05.1", "LIN.G1.06.1", "LIN.G2.03.1", "LIN.G3.02.1", "MEC.G0.02.1", "MEC.G0.04.1", "MEC.G0.05.1", "MEC.G0.07.1", "MEC.G0.08.1", "MEC.G0.08.2", "MEC.G0.08.3", "MEC.G0.08.5", "MEC.G0.08.6", "MEC.G0.10.1", "MEC.G0.11.2", "MEC.G1.01.1", "MEC.G1.05.1", "MEC.G1.06.1", "MEC.G1.07.1", "MEC.G2.01.1", "MEC.G2.03.1", "MEC.G2.04.1", "MEC.G3.01.1", "NRE.G0.01.1", "NRE.G0.03.2", "NRE.G1.18.1", "NRE.G1.20.1", "NRE.G1.21.1", "NRE.G1.27.1", "NRE.G1.27.2", "NRE.G1.27.4", "NRE.G2.07.1", "NRE.G3.01.1", "NUR.G0.13.1", "NUR.G0.15.2", "NUR.G3.05.1", "PHI.G1.02.2", "PHY.G0.01.1", "PHY.G0.02.1", "PHY.G0.03.1", "PHY.G0.04.1", "PHY.G0.04.2", "PHY.G2.05.1", "PHY.G2.06.1", "POL.G0.01.2", "POL.G0.13.1", "POL.G0.30.1", "PSY.G0.04.1", "PSY.G0.08.1", "PSY.G0.16.1", "PSY.G0.18.1", "PSY.G0.21.1", "PSY.G0.27.1", "PSY.G0.28.1", "PSY.G0.29.1", "PSY.G0.30.1", "PSY.G0.32.2", "PSY.G0.39.1", "PSY.G2.01.1", "PSY.G2.13.1", "PSY.G3.06.1", "SOC.G0.02.2", "SOC.G0.03.1", "SOC.G0.11.1", "SOC.G1.10.5", "SOC.G3.04.1", "SOC.G3.05.2", "SOC.G3.07.1", "SOC.G3.08.1"]

MICUSP_DIR = "micusp_body"

research = deque(research)

if not os.path.exists("research_segs"):
    os.makedirs("research_segs")

counter = 0
while research:
    with open(os.path.join("research_segs", f"research_{str(counter).zfill(2)}.txt"), "w") as researchs:
        for i in range(30):
            if not research:
                break
            text = research.popleft()
            with open(os.path.join(MICUSP_DIR, text + ".txt")) as f:
                researchs.write(f.read())
            researchs.write("\n")

    counter += 1
