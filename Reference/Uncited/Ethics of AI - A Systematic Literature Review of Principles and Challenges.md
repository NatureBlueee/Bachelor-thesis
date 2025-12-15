

See discussions, stats, and author profiles for this publication at: <https://www.researchgate.net/publication/354651489>

# Ethics of AI: A Systematic Literature Review of Principles and Challenges

Preprint · September 2021

DOI: 10.48501/axiv.2109.07006

CITATIONS

4

READS

6,487

8 authors, including:

![Profile picture of Mahdi Fahmideh](1d7527f4316cfe2d342b08d1653d1592_img.jpg)

Profile picture of Mahdi Fahmideh

Mahdi Fahmideh

University of Southern Queensland (USQ)

99 PUBLICATIONS 1,577 CITATIONS

[SEE PROFILE](#)

![Profile picture of Aakash Ahmad](5a36d88d3904f3f2d386c7cf63fa5053_img.jpg)

Profile picture of Aakash Ahmad

Aakash Ahmad

Lancaster University Leipzig

95 PUBLICATIONS 1,265 CITATIONS

[SEE PROFILE](#)

![Profile picture of Arif Ali Khan](31cdb383e9cc2643a547f2500ed3cd08_img.jpg)

Profile picture of Arif Ali Khan

Arif Ali Khan

University of Oulu

200 PUBLICATIONS 3,954 CITATIONS

[SEE PROFILE](#)

![Profile picture of Peng Liang](a378064ca1325302ee7048e11876e5d2_img.jpg)

Profile picture of Peng Liang

Peng Liang

Wuhan University

306 PUBLICATIONS 5,588 CITATIONS

[SEE PROFILE](#)

# Ethics of AI: A Systematic Literature Review of Principles and Challenges

Arif Ali Khan<sup>1\*</sup>, Sher Badshah<sup>2</sup>, Peng Liang<sup>3</sup>, Muhammad Waseem<sup>3</sup>, Bilal Khan<sup>4</sup>, Aakash Ahmad<sup>5</sup>, Mahdi Fahmideh<sup>6</sup>, Mahmood Niaz<sup>7</sup>, Muhammad Azeem Akbar<sup>8</sup>

<sup>1</sup>M3S Empirical Software Engineering Research Unit, University of Oulu, Oulu, Finland

<sup>2</sup>Faculty of Computer Science, Dalhousie University, Halifax, Canada

<sup>3</sup>School of Computer Science, Wuhan University, Wuhan, China

<sup>4</sup>Department of Computer Science, University of Loralai, Balochistan, Pakistan

<sup>5</sup>College of Computer Science and Engineering, University of Ha'il, Saudi Arabia

<sup>6</sup>School of Business at University of Southern Queensland, Queensland, Australia

<sup>7</sup>Department of Information and Computer Science, King Fahd University of Petroleum and Minerals, Saudi Arabia

<sup>8</sup>Software Engineering Department, Lappeenranta-Lahti University of Technology, 53851 Lappeenranta, Finland  
arif.khan@oulu.fi, sh545346@dal.ca, liangp@whu.edu.cn, m.waseem@whu.edu.cn, bilal\_nasar@uol.edu.pk,  
a.abbasi@uoh.edu.sa, mahdi.fahmideh@usp.edu.au, mkniaz@kfupm.edu.sa, azeem.akbar@gmail.com

## ABSTRACT

Ethics in AI becomes a global topic of interest for both policymakers and academic researchers. In the last few years, various research organizations, lawyers, think tankers, and regulatory bodies get involved in developing AI ethics guidelines and principles. However, there is still debate about the implications of these principles. We conducted a systematic literature review (SLR) study to investigate the agreement on the significance of AI principles and identify the challenging factors that could negatively impact the adoption of AI ethics principles. The results reveal that the global convergence set consists of 22 ethical principles and 15 challenges. Transparency, privacy, accountability and fairness are identified as the most common AI ethics principles. Similarly, lack of ethical knowledge and vague principles are reported as the significant challenges for considering ethics in AI. The findings of this study are the preliminary inputs for proposing a maturity model that assesses the ethical capabilities of AI systems and provides best practices for further improvements.

## CCS CONCEPTS

- Software and its engineering → Human-centered computing
- Computing methodologies → Artificial intelligence
- Philosophical/theoretical foundations of artificial intelligence
- Social and professional topics → Empirical studies

## KEYWORDS

AI Ethics, Machine Ethics, Principles, Challenges, Systematic Literature Review

## ACM Reference Format:

Arif Ali Khan<sup>1\*</sup>, Sher Badshah<sup>2</sup>, Peng Liang<sup>3</sup>, Muhammad Waseem<sup>3</sup>, Bilal Khan<sup>4</sup>, Aakash Ahmad<sup>5</sup>, Mahdi Fahmideh<sup>6</sup>, Mahmood Niaz<sup>7</sup>, Muhammad Azeem Akbar<sup>8</sup>. 2022. Ethics of AI: A Systematic Literature Review of Principles and Challenges. In *Proceedings of ACM Conference (EASE)*. ACM, New York, NY, USA, 10 pages. <https://doi.org/XXXXXXXX.XXXXXXX>

## 1 INTRODUCTION

Artificial intelligence (AI) technologies are considered important across a vast array of industries including health, manufacturing, banking and retail [14]. However, the promises of AI systems like improving productivity, reducing costs, and safety has now been considered with worries, that these complex systems might bring more ethical harm than economical good [14].

Artificial intelligence (AI) and autonomous systems have a significant effect on the development of humanity [12]. The autonomous decision-making nature of these systems raises fundamental questions i.e., what are the potential risks involved in those systems, how these systems should perform, how to control such systems and what to do with AI-based systems? [12]. Autonomous systems are beyond the concepts of automation by characterising them with decision-making capabilities. The development of autonomous system components, such as intelligent awareness and self-decision making is based on AI concepts.

There is a political and ethical discussion to develop policies for different technologies including nuclear power, manufacturing etc. to control the ethical damage they could bring. The same ethical potential harm also exits in AI systems and more specifically they might end human control [12]. The real-world failure and misuse incidents of AI systems bring the demand and discussion for AI ethics [19]. The ethical studies of AI technologies revealed that AI and autonomous systems should not be only considered a technological effort. There is a broad discussion that the design and use of AI-based systems are culturally and ethically embedded [10]. Developing AI-based systems not only need technical efforts but also include economic, political, societal, intellectual and legal aspects [10]. These systems significantly impact the cultural norms and values of the people [10]. The AI industry and specifically the practitioners should have a deep understanding of ethics in this

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from [permissions@acm.org](mailto:permissions@acm.org).

EASE, 13-15 June 2022, Gothenburg, Sweden

© 2022 Association for Computing Machinery.

ACM ISBN 978-xxxx-xxxx-x/YY/MM...\$15.00

<https://doi.org/XXXXXXXX.XXXXXXX>

domain. Recently, AI ethics get press coverage and public voices, which supports significant related research [19]. However, the topic is still not sufficiently investigated both academically and in the real-world environment [10]. There are very few academic studies conducted on this topic, but it is still largely unknown to AI practitioners. The Ethically Aligned Design (EAD) [7] guidelines of IEEE mentioned that ethics in AI is still far from being mature in an industrial setting [18]. The limited or no knowledge of ethics for the AI industry develop the gap, which indicates the need for further academic and in practice research.

The aim of this study is to conduct a systematic literature review (SLR) and explore the available literature to identify the AI ethics principles. Moreover, the SLR study uncover the key challenging factors that are the demotivators for considering the ethics of AI. The following research questions are developed to achieve the given core objectives:

- RQ1: What are the key principles of AI ethics?
- RQ2: What are the challenges of adopting ethics in AI?

The remaining content of paper is structured as follows: Section 2 presents the background of the study and the research methodology is reported in Section 3. The SLR data are provided in Section 4 and results and analysis are discussed in Section 5. The study implications are discussed in Section 6. Finally, Section 7 provides an overview of threats to the validity of the study and Section 8 conclude the findings with future directions.

## 2 BACKGROUND

The implementation of AI or machine intelligence concepts brings a technological revolution that change both science and society. Human to machine power transformation sparked important societal debate about the principles and policies that guide the use and deployment of AI systems [8]. Various organizations have developed ad hoc committees to draft the policy documents for AI ethics. These organizations reportedly developed AI policies and guide documents [8]. In 2018, technology corporates such as SAP and Google publicly introduced guidelines and policies for AI-based systems [8]. Similarly, Amnesty International, the Association of Computing Machinery (ACM) and Access Now comes up with principles and recommendations for AI technologies. The Trustworthy AI European Commission's guidelines were developed with the aim to promote lawful, ethically sound and robust AI systems [15]. The report "Preparing for the Future of Artificial Intelligence" prepared by the Obama administration's presents a thorough survey that focuses on the current AI research, its applications and impact on society [3]. The report further presents recommendations for future AI related actions. The "Beijing AI Principles" guidelines [13] proposed various principles in the domain of AI research, development, use and governance. These principles present a framework that focus on AI ethics.

The world largest technical professional organization, IEEE launches the guidelines Ethically Aligned Design (EAD) [7] that provides a framework to address the ethical and technical values of AI systems based on a set of principles and recommendations. The EAD framework consists of the following eight general principles to guide the development and implementations of AI-based systems: human rights, well-being, data agency, effectiveness, transparency,

accountability and awareness of misuse. Organizations such as ISO and IEC also embark on developing standard for AI [5]. ISO/IEC JTC 1/SC 42 [5] is a joint ISO/IEC international standard committee that focus on the entire AI ecosystem including ethical and social concerns, standardization, AI governance, AI computational approach and trustworthiness [5]. The effort of different organizations to shape AI ethics not only determine the need of guidelines, tools, techniques, but also the interest of these organizations to manage ethics in a way that meet their respective priorities.

However, recently published studies reported that the existing guidelines developed for ethics of AI are not effective and adopted in practice [20]. It is evident from the empirical study conducted by McNamara et al. [11] to test the influence of the ACM code of ethics in the decision-making process of software development. The results of the study revealed that the ACM code of ethics have no impact in making ethical decisions. The lack of effective techniques makes it challenging to successfully scale the available guidelines into practice [20]. Vakkuri et al. [20] used the accountability, responsibility, and transparency (ART) framework [6] and developed the conceptual model to explore ethical consideration in the AI environment. The conceptual model is empirically validated by conducting multiple case studies. The empirical results are concluded by highlighting that AI ethics principles are still not in practice; however, some common concepts are considered such as documentation. Moreover, the study findings revealed that practitioners consider the social impact of AI systems [20].

There are no tools, methods or frameworks that fill the gap between the AI principles and their implementation in practice. Further studies in this area should conduct that explicitly discuss the AI ethics principles, challenges and provide evaluation standards/models that guide AI industry to consider ethics in practice.

## 3 RESEARCH METHOD

Systematic literature review (SLR) approach is used to explore the available primary studies. SLR is a widely adopted literature survey method in evidence-based software engineering domain. SLR is "a means of evaluating and interpreting all available research relevant to a particular research question, topic area, or phenomenon of interest" [9]. The Kitchenham and Charters [9] SLR guidelines are used to conduct this study and systematically address the research questions. The SLR process plan is provided in Figure 1 and thoroughly discussed in the following sub-sections.

### 3.1 Research questions (RQs)

Research questions development in SLR studies is the most significant phase [9]. Developing research questions require deep understanding of the research area in general and the research problem in specific. We primarily studied relevant articles [19][10][18][7][8][15][3] to better understand the problem and develop the questions of interest. The questions are finally developed based on the research concepts discussed in the mentioned research sources [3-9]. The details of the research questions are provided in Section 1.

### 3.2 Data sources

The authors had a series of team discussions to identify the list of digital data sources. The selected digital repositories are explored

![Figure 1: SLR research process flowchart. The process is divided into three phases: Phase I (Planning the Review), Phase II (Conducting the Review), and Phase III (Reporting the Review). Phase I involves Identifying the Problem, Specifying the Research Questions, and Defining the Study Protocol. Phase II involves Selecting the Primary Studies, Assessing the Studies Quality, and Analysing and Synthesising the Data. Phase III involves Mapping Results to Research Questions, Analyzing Threats to the Validity, and Documenting the Results. The flow leads to Research Protocol and Review Results, which feed into the Research Phase and Phase Activity, and then into the Phase Transition Activity Transition, completing the cycle.](7fb5215fd72210a2e4cce6df55550c89_img.jpg)

Figure 1: SLR research process flowchart. The process is divided into three phases: Phase I (Planning the Review), Phase II (Conducting the Review), and Phase III (Reporting the Review). Phase I involves Identifying the Problem, Specifying the Research Questions, and Defining the Study Protocol. Phase II involves Selecting the Primary Studies, Assessing the Studies Quality, and Analysing and Synthesising the Data. Phase III involves Mapping Results to Research Questions, Analyzing Threats to the Validity, and Documenting the Results. The flow leads to Research Protocol and Review Results, which feed into the Research Phase and Phase Activity, and then into the Phase Transition Activity Transition, completing the cycle.

Figure 1: SLR research process

to extract the relevant data in order to address the given research questions (see Section 1). Finally, the following digital libraries are selected based on the authors SLR experience, discussions and guidelines provided by Chen et al. [4]: Springer Link, Science Direct, IEEE Xplore, Wiley Online Library and ACM Digital Library. These are the world leading digital data sources which collect a large number of original information and communication technology studies [4].

### 3.3 Search strategy

The research questions are analysed by the second and third authors to extract the terms or keywords used for the search process. All the authors participated in the group discussion to finalise the search terms and retrieve the relevant data from the selected repositories. Pilot search terms and strings are made that finally contributed to develop the following agreed search string:

(“artificial intelligence ethics” OR “AI ethics” OR “machine learning ethics” OR “software ethics”) AND (“resistance” OR “barriers” OR “limitations” OR “challenges”)

The “principles” and “guidelines” terms were excluded from the final search string because these terms return irrelevant data from different other domains. The given search string was specifically tested during the pilot attempts to explore the data related to the AI “principles” and “guidelines” and we noticed that it precisely returns the desire results related to the RQ1, i.e., “principles” and “guidelines”.

The search terms are concatenated using “AND” and “OR” operators to develop the search strings. The selected digital repositories have a customised search mechanism. The search strings are executed using the personalised search mechanism of electronic data sources.

### 3.4 Inclusion/Exclusion criteria

The inclusion/exclusion criteria are developed to filter the search string findings and remove irrelevant, not accessible, redundant and low-quality studies. The criteria are developed by the first and

fifth authors, which are finalised by all the authors in the regular consensus meeting (see Table 1).

### 3.5 Study selection

The search string discussed in Section 3.3 is used to explore the selected digital repositories. The search process was initiated on 23rd December 2020 and ended on 5th February 2021. The search string retrieved total 811 studies in the first phase, which were further filtered based on the study title, abstract and keywords (see Figure 2). In the second phase of the selection process, the inclusion/exclusion of the 60 studies are performed based on the full-text review. Finally, 24 primary studies are shortlisted using the SLR approach. Moreover, backward snowballing [21] is performed to search the references of the selected 24 studies. The backward snowballing is previously used by Tingting et al. [1] to explore text analysis techniques in software architectural and we used with the aim to explore the references list of the selected primary studies to identify relevant studies that are missed during the SLR process. Additionally, 5 studies are selected, which are further filtered using the inclusion/exclusion criteria (see Figure 2). Eventually, only 3 studies fulfil the selection criteria and the final data sets consist of total 27 primary studies (24 SLR + 3 backward snowballing). Final set of the selected studies is provided in Appendix A, where each study is labeled as [Sn] to differentiate from the general list of references.

![Figure 2: Studies selection process flowchart. The process starts with Digital Libraries (ACM Digital Library, IEEE Xplore, Science Direct, Springer Link, Wiley Online Library) and a Literature Search String. The Literature Search String is: (‘artificial intelligence ethics’ OR ‘AI ethics’ OR ‘machine learning ethics’ OR ‘software ethics’) AND (‘resistance’ OR ‘barriers’ OR ‘limitations’ OR ‘challenges’). The process involves Primary Studies Selection Phases: 1. Total Studies Retrieved 811. 2. Initially Selected Studies 60. 3. Finally Selected Studies 24. 4. Backward Snowballing 5. The process continues with Literature Inclusion in the SLR 27. The flowchart details the number of studies retrieved and selected at each phase.](10ac14a735447206df16a3124982177a_img.jpg)

Figure 2: Studies selection process flowchart. The process starts with Digital Libraries (ACM Digital Library, IEEE Xplore, Science Direct, Springer Link, Wiley Online Library) and a Literature Search String. The Literature Search String is: (‘artificial intelligence ethics’ OR ‘AI ethics’ OR ‘machine learning ethics’ OR ‘software ethics’) AND (‘resistance’ OR ‘barriers’ OR ‘limitations’ OR ‘challenges’). The process involves Primary Studies Selection Phases: 1. Total Studies Retrieved 811. 2. Initially Selected Studies 60. 3. Finally Selected Studies 24. 4. Backward Snowballing 5. The process continues with Literature Inclusion in the SLR 27. The flowchart details the number of studies retrieved and selected at each phase.

Figure 2: Studies selection process

### 3.6 Quality assessment (QA)

The assessment criteria are developed to evaluate the quality of the selected primary studies and remove the research bias. The quality assessment phase interprets the significance and completeness of each selected primary study [9]. The QA criteria checklist provided by Kitchenham and Charters [9] are analysed and designed the QA questions provided in Table 2. Each selected primary study evaluated against the quality assessment questions (QA1-QA6). Score (1) assigned if the study comprehensively addresses the quality assessment questions (see Table 2). Similarly, 0.5 points are assigned to those who have partially addressed the QA questions. Studies with no evidence of addressing the QA questions are assigned 0 points.

Table 1: Inclusion/Exclusion criteria

| #   | Inclusion criteria                                                                                   |
|-----|------------------------------------------------------------------------------------------------------|
| In1 | Consider articles that specifically focus on AI ethics.                                              |
| In2 | Primary studies published in conferences, research workshops, book chapters, journals and magazines. |
| In3 | Peer-reviewed and available in full text                                                             |
| In4 | Written in the English language                                                                      |
| No. | Exclusion criteria                                                                                   |
| Ex1 | If two studies are published from the same project, then exclude the one with minimum contribution.  |
| Ex2 | Exclude grey literature material.                                                                    |
| Ex3 | Remove duplicate studies.                                                                            |
| Ex4 | Discuss ethics in other domains.                                                                     |

Table 2: Quality assessment criteria

| No. | Assessment Questions                                                | Score   |
|-----|---------------------------------------------------------------------|---------|
| QA1 | Does the adopted research method address the research problem?      | 1/0.5/0 |
| QA2 | Does the study have clear research objectives?                      | 1/0.5/0 |
| QA3 | Does the study explicitly discuss the proposed research approach?   | 1/0.5/0 |
| QA4 | Is the study clearly reported the experimental setting?             | 1/0.5/0 |
| QA5 | Do the study results and findings are systematically discussed?     | 1/0.5/0 |
| QA6 | Does the study present the real-world implications of the research? | 1/0.5/0 |

### 3.7 Data extraction

The relevant data to address the RQs are collected by thoroughly reading the selected primary studies and extract the AI ethics principles (RQ1) and challenges (RQ2). The extracted data are recorded on excel sheets. Most of the data are collected by the second and third authors. They assess the quality of the primary studies based on the criteria discussed in Section 3.6. Moreover, the first, fourth and fifth authors participated in the review meeting to finalize the QA score of each study (Appendix A). Additionally, authors at positions six and seven are invited to assess the inter-personal bias in the data extraction process. They were asked to randomly select 15 primary studies from a set of total primary studies and perform the data extraction process as conducted by the other authors. Finally, the Kendalls coefficient of concordance (W) test is performed to statistically evaluate the significant differences in the data extraction process between both the groups (authors 1-5 and 6-7). Kendalls coefficient of concordance (W) is a widely adopted statistical approach to evaluate a level of agreement between groups of people, which assess a set of n-objects [16]. The Kendalls coefficient of concordance (W) assessment score varies from 0 to 1, where (W=1) shows strong agreement between the people and (W=0) refers to complete disagreement [16]. We used R-3.6.3 to conduct the (W) test for evaluating the level of agreement between both groups of authors. The test results (W=0.792) given in Table 3 show that both author's groups are at a positive agreement level for the data extraction process. Based on the test results, we identified that no personal bias exists between the authors that could impact the data extraction process. Following is the R-code developed to run the (W) test.

```
library(Desctools)
```

```
AI_Ethics <- data.frame(AuthorsGroup1=c(3,5,3,4,5,5,3,3,5,2,2,6,4,4,2),Author6=c(3,6,4,5,4,4,2,4,4,3,2,5,5,4,2),Author7=c(2,5,4,4,3,4,2,5,3,4,2,5,5,5,4,1))KendallW(AI_Ethics, TRUE)KendallW(AI_Ethics, TRUE, test=TRUE)KendallW(t(d.att[, -1]), test = TRUE)
```

Table 3: Kendall's coefficient of concordance (W) test values (DS-Data Set, df-Degrees of freedom,  $\chi^2$ -chi square, S-Subjects, R-Raters, PV-Probability Values)

| DS        | $\chi^2$ | df | S  | R | PV    | W     |
|-----------|----------|----|----|---|-------|-------|
| AI_Ethics | 33.287   | 14 | 15 | 3 | 0.002 | 0.792 |

## 4 REPORTING THE REVIEW

The data collected from the selected 27 primary studies are analyzed and discussed in the following sections.

### 4.1 Temporal distribution

The year wise distribution of the primary studies is shown in Figure 3. Of the 27 studies, total 4, 17, 4 and 2 are respectively published in 2021 (till 5th February), 2020, 2019 and 2018. The first relevant study was found in 2018 and since then, there has been a gradual increase in the number of research publication. The SLR string was finally executed on 5th February 2021, therefore the given results only cover the first two months of 2021. The increasing number of publications reveal that AI ethics is significant, and state of the art research direction. There is still need of substantial research work to explore ethics in AI.

![Figure 3: Temporal and publication types based distribution of primary studies. The figure shows a stacked bar chart (Years and Types of Publications) from 2018 to 2021, and a donut chart (Types of Publications) showing the distribution of publication types (Journal Articles, Magazine Publication, Books Chapters, Conference Proceedings) in 2021. The bar chart shows a general trend of increasing publication volume over time, with Conference Proceedings being the most frequent type in 2021 (13 studies). The donut chart shows that Journal Articles account for 70% of publications, Magazine Publication for 4%, Books Chapters for 4%, and Conference Proceedings for 6%.](55d2bfe1c3d04e86df8d7a104d802172_img.jpg)

Figure 3: Temporal and publication types based distribution of primary studies. The figure shows a stacked bar chart (Years and Types of Publications) from 2018 to 2021, and a donut chart (Types of Publications) showing the distribution of publication types (Journal Articles, Magazine Publication, Books Chapters, Conference Proceedings) in 2021. The bar chart shows a general trend of increasing publication volume over time, with Conference Proceedings being the most frequent type in 2021 (13 studies). The donut chart shows that Journal Articles account for 70% of publications, Magazine Publication for 4%, Books Chapters for 4%, and Conference Proceedings for 6%.

Figure 3: Temporal and publication types based distribution of primary studies

### 4.2 Publication type

The selected primary studies are classified across four major types i.e., journal, conference (including workshop), book chapter and magazine. Figure 3 shows that 19 (70%) studies are published in journals, 6 (22%) in conferences, 1 (4%) book chapter and 1 (4%) is a magazine article. We noticed that journals are the most active venues to publish relevant studies.

## 5 DETAIL RESULTS AND ANALYSIS

The detail results to address RQ1 and RQ2 are discussed in the following sections.

### 5.1 RQ1 (AI Ethics Principles)

The final set of the primary studies consist of 27 articles and total 21 AI ethics principles are extracted from these articles. The identified principles along with their respective references are provided in Table 4. Moreover, a word cloud is generated to graphically represent the significance of the reported principles (See Figure 4). Of the 21 principles, transparency (n=17) is the most frequently mentioned principle, followed by privacy (n=16). The third and fourth most common principles are accountability (n=15) and fairness (n=14) respectively.

**5.1.1 Transparency.** Transparency of operations is a major concern in AI/autonomous systems [S5]. It answers how and why a specific decision is made by the system and further triggers the other constructs including interpretability and explainability. It should not only consider for the AI system operations, but must be part of the technical process [S5] to make the decision-making actions more transparent and trustworthy. Both operational and technical transparency could be achieved by developing standards and models that measure and testify the levels of transparency. Such standards could assist the AI system development organizations to assess their level of transparency and provide best practices for further improvements. Moreover, transparency should consider for a wide

![Figure 4: Word cloud of the identified AI ethics principles. The word cloud displays various AI ethics principles, with 'Privacy', 'Transparency', 'Fairness', 'Accountability', and 'Autonomy' being the most prominent terms.](2c51e13558d27d3452dfec3fb73aaed1_img.jpg)

Figure 4: Word cloud of the identified AI ethics principles. The word cloud displays various AI ethics principles, with 'Privacy', 'Transparency', 'Fairness', 'Accountability', and 'Autonomy' being the most prominent terms.

Figure 4: Word cloud of the identified AI ethics principles

range of system stakeholders; however, the level of transparency should be varied for them [S4].

**5.1.2 Privacy.** AI/autonomous system must assure user and data privacy throughout the system lifecycle. It could broadly be defined as “the right to control information about oneself” [S22]. Regulatory institutions are consistently involved in establishing legislation for data privacy and protection [S7]. However, privacy becomes more challenging in data driven AI environment, where the system subsequently processes user data including cleaning, merging, and interpretation [S7]. The data access in self-governing AI systems develop the primary concern of data privacy, which is commonly related to security and transparency [S21]. It is worth noting that AI technologies bring complex challenges associated with data privacy and integrity, which demand more relevant future research [S22].

**5.1.3 Accountability.** Accountability is the third most frequently reported principle which specifically focuses on liability issues [S5]. It refers to safeguarding justice by assigning responsibility and prevent harm [S3]. The stakeholders must be accountable for the system decisions and actions to minimize the culpability problems [S4, S5]. Ensure both technical and social accountability before and after the system development, implementation and operation [S5]. Accountability is closely linked with transparency because the system must be understood before making the liability decisions [S5].

**5.1.4 Fairness.** Fairness is considered a significant principle of AI ethics. Discrimination between individuals or groups made by the decision-making systems lead to ethical fairness problems, which impact public values including dignity and justice [S11]. Avoiding unfair biases of AI systems could foster social fairness. AI and autonomous systems should not deceive people by impairing their autonomy [S4]. It could achieve by explicitly making the decision-making process more transparent and identifying the accountable entities.

**Analysis.** Based on the SLR findings, we identified that the above principles received significant attention, which are compatible with the widely adopted accountability, responsibility and transparency (ART) framework [6] of ethics in AI. Responsibility is not a highly cited principle in the selected primary studies and the reason might be that it is considered an associated one with accountability [15]. Moreover, Vakkuri et al. [S5] developed a relational framework

Table 4: Identified AI ethics principles

| ID   | Principles       | Reference                                                                          | Frequency |
|------|------------------|------------------------------------------------------------------------------------|-----------|
| P-01 | Transparency     | [S1][S2][S3][S4][S5][S6][S7][S8][S9][S10] [S11][S12][S13][S14][S15][S16][S17][S25] | 17        |
| P-02 | Privacy          | [S1][S2][S18][S3][S5][S7][S8][S21][S22] [S9][S11][S13][S14][S15][S16][S17]         | 16        |
| P-03 | Accountability   | [S1][S2][S3][S4][S5][S6][S7][S9][S10][S12] [S13][S14][S15][S17][S25]               | 15        |
| P-04 | Fairness         | [S1][S18][S4][S5][S6][S7][S8][S21] [S10][S11][S13][S14][S15][S17]                  | 14        |
| P-05 | Autonomy         | [S1][S2][S18][S4][S8][S11][S22][S19][S16][S20]                                     | 10        |
| P-06 | Explainability   | [S6][S19][S9][S11][S13][S14][S16][S20]                                             | 8         |
| P-07 | Justice          | [S1][S18][S3][S6][S8][S19][S20]                                                    | 7         |
| P-08 | Non-maleficence  | [S1][S18][S5][S6][S19][S20]                                                        | 7         |
| P-09 | Human Dignity    | [S1][S5][S21][S22][S10][S16]                                                       | 6         |
| P-10 | Beneficence      | [S1][S18][S21][S22][S19][S20]                                                      | 6         |
| P-11 | Responsibility   | [S1][S2][S5][S9][S12]                                                              | 5         |
| P-12 | Safety           | [S2][S6][S7][S10][S25]                                                             | 5         |
| P-13 | Data Security    | [S2][S9][S16][S17]                                                                 | 4         |
| P-14 | Sustainability   | [S1][S6]                                                                           | 2         |
| P-15 | Freedom          | [S1]                                                                               | 1         |
| P-16 | Solidarity       | [S1]                                                                               | 1         |
| P-17 | Prosperity       | [S2]                                                                               | 1         |
| P-18 | Effectiveness    | [S2]                                                                               | 1         |
| P-19 | Accuracy         | [S2]                                                                               | 1         |
| p-20 | Predictability   | [S5]                                                                               | 1         |
| P-21 | Interpretability | [S6]                                                                               | 1         |

based on the key ART constructs with an additional fairness principle. The framework is empirically evaluated to know the opinions and perceptions of the practitioners [S5]. However, the findings of their study are only based on the five major principles and have not considered the other significant principles reported in Table 4.

#### Key Findings of RQ1

**Finding 1:** Thorough overview of the identified primary studies return a set of 21 AI ethics principles.

**Finding 2:** Transparency, Privacy and Accountability are respectively identified as the most frequently cited principles.

### 5.2 RQ2 (Challenges)

Systematic review of the 27 primary studies returns a total 15 challenging factors (See Table 5). Moreover, word cloud is generated to demonstrate the significance of the reported factors (See Figure 5).

We further followed thematic analysis guidelines developed by Braun and Clarke [2] to systematically organize the identified challenges across broader themes. The first two authors thoroughly studied the selected primary studies and developed the preliminary codes to define the research themes. Both authors analyzed the codes and merged them to develop the broader themes. All the authors participated in the consent meeting to finalize the thematic mapping and tagged each theme with a precise name. Finally, three core themes (*knowledge and expertise, organizational management, tools and technologies*) (see Figure 6) are defined and the identified challenges (sub-themes) are presented across the core themes. Thematic map is provided in Figure 6, which presents the core themes (main categories) and sub-themes (challenging factors). Moreover,

![Word cloud showing the identified AI ethics challenges. Key terms include 'Extra constraints', 'Highly general', 'Vague principles', 'Lack of ethical knowledge', 'Conflict in practice', and 'Lack of technical understanding'.](ab9eb65dcbc2696ec77b66f70f9e0e91_img.jpg)

Word cloud showing the identified AI ethics challenges. Key terms include 'Extra constraints', 'Highly general', 'Vague principles', 'Lack of ethical knowledge', 'Conflict in practice', and 'Lack of technical understanding'.

Figure 5: Word cloud of the identified AI ethics challenges

the challenging factors having low frequency are not discussed in details because of the page limitation. However, the complete list of the identified factors is provided in Table 5. The details of the highly cited (frequency>1) challenging factors is as follow and :

**5.2.1 Lack of ethical knowledge.** Lack of ethical knowledge is one of the main reasons that AI ethics in practice is still far from being mature [S14]. AI systems development organizations believe that government institutions are not in the position of providing experts to this emerging area, while some opine that establishing ethics in AI is not possible without the political approach [S15]. Similarly, management and technical staff are not aware of the moral and ethical complexity of the AI systems. AI ethics are in their infancy, not enough ethical standards and frameworks are available that provide details guidelines to the AI industry.

**5.2.2 Vague principles.** There are various AI ethics principles as we discussed in Section 5.1. However, in practice, majority of the

organizations are reluctant to adopt these principles which are highly vague in their definition [S23]. For example, it is not clear how specifically consider “fairness” and “human dignity” in AI ethics [S17]. It is very challenging to consider AI ethics in real world settings using these vaguely formulated principles [S3].

**5.2.3 Highly general principles.** The available principles are highly general and broad in concept to specifically consider in the AI industry [S18]. They are subjective in the term and used in various other domains than AI. Policymakers involved in drafting AI ethics principles might not have strong technical understanding of AI system development processes, which makes the principles more general and ambiguous.

**5.2.4 Conflict in practice.** Organizations, committees and groups involved in developing the AI ethics guidelines and principles have opinion conflicts regarding the real world implementation of AI ethics [S13, S16]. For example, the UK house of lords suggested that robots cannot solely be in operation, but they should be guided by human beings [S10], on the other hand, in various hospitals’ robots make autonomous decisions in diagnosis and surgical endeavours. It shows interpretation and understanding conflict for AI ethics in practice.

**5.2.5 Interpret principles differently.** AI ethics principles are widely considered ambiguous and general by majority of the organizations [S20]. It has been found that tech firms involved in the development of AI and autonomous systems follow ethical guidelines based on their own understandings [S27]. There are no universally agreed ethical principles that can bring all the institutions on one page.

**5.2.6 Lack of technical understanding.** The policymakers have lack of technical knowledge, which makes AI ethics in practice a challenging effort [S10, S13]. They are not aware of the technical aspects of AI systems and the advancement in AI technologies as well their limitations. Lack of technical understanding develops the gap between system design and ethical thinking [S10]. The ethicists must have skills of grasping technical knowledge using their ethical framework [S10].

**5.2.7 Extra constraints.** Situational constraints could interfere with an employee’s motivation to consider ethics in AI system development process. The possible constraints include lack of information, incorrect guidelines, organizational rules and policies, and top management interruptions. Organizational management should be highly aware of the AI ethics debate and keen to engage with the constraints proactively [S26].

**Analysis.** The above reported challenges provide an overview of the most common and frequently cited factors that could be potential barriers for scaling ethics in AI. *Lack of ethical knowledge* is identified as the most common challenge of AI ethics. Major ethical mistakes are made because of no moral awareness of specific problem [S14]. Practitioners only consider software development activities as the main responsibilities; however, they have limited interest to consider ethical aspects [S5]. The ethical uncertainty in AI systems could only be diminish by acquiring ethical knowledge. Continuous awareness of ethical policies, codes and regulations assist to properly manage the ethical values in AI and autonomous systems.

Table 5: AI ethics challenging factors

| #     | Challenges                         | Reference                         |
|-------|------------------------------------|-----------------------------------|
| Ch-01 | Lack of ethical knowledge          | [S14], [S15], [S18], [S21], [S23] |
| Ch-02 | Vague principles                   | [S3], [S17], [S24]                |
| Ch-03 | Highly general principles          | [S19], [S20]                      |
| Ch-04 | Conflict in practice               | [S19], [S16]                      |
| Ch-05 | Interpret principles differently   | [S19], [S20]                      |
| Ch-06 | Lack of technical understanding    | [S10], [S13]                      |
| Ch-07 | Extra constraints                  | [S11], [S24]                      |
| Ch-08 | Lack of Audit and Monitoring       | [S20]                             |
| Ch-09 | No Legal frameworks                | [S20]                             |
| Ch-10 | Business interest                  | [S25]                             |
| Ch-11 | Pluralism of ethical methods       | [S14]                             |
| Ch-12 | Cases of ethical dilemmas          | [S14]                             |
| Ch-13 | Machine distortion                 | [S14]                             |
| Ch-14 | Lack of Guidance and Adoption      | [S26]                             |
| Ch-15 | Lack of Cross-cultural Cooperation | [S27]                             |

We noticed that very few studies are published where the barriers of AI ethics are directly or indirectly mentioned. It is evident from the frequency distribution of the challenging factors given in Table 5. This finding reveals that the AI ethics challenges aspect is very young field and requires considerable research effort from diverse disciplines to be mature. The significance of AI technologies in various sectors calls for rush research to uncover the relevant challenges that hinder the process of considering ethics in AI.

#### Key Findings of RQ2

**Finding 3:** We noticed that only (n=17, 63%) primary studies discussed the AI ethics challenging factors.

**Finding 4:** The core themes of the identified challenges are: (knowledge and expertise, organizational management, tools and technologies).

**Finding 5:** *Lack of ethical knowledge* (n=5, 29%) is the most frequently cited challenge followed by *Vague principles* (n=3, 18%).

The long-term plan of the research is to propose a maturity model that could be used to evaluate the ethical capabilities of the organizations involved in developing AI systems. The findings of this systematic review are the initial inputs for the development of the proposed model. Figure 7 shows the preliminary structure of the model and demonstrates how the findings of this review contribute in the development of the principles and challenges component. The identified principles and challenges will be classified across capability and maturity levels. Moreover, best practices will provide to tackle the identified challenges and implement the AI ethics principles. The given model is a proposed idea that will be systematically developed based on the industrial empirical studies and the concepts of the widely adopted CMMI process model [17]. Case study approach is selected to evaluate the real-world significance of the model.

![](91be14371a97fb5ce9eeb29ae18d07c3_img.jpg)

Figure 6 is a thematic mapping diagram titled "AI Ethics Challenging Factors Mapping". The central concept is "Knowledge and Expertise" (CH-1), which branches into: Highly General Principles (CH-3), Interpret Principles Differently (CH-5), Vague Principles (CH-2), and Lack of Guidance and Adoption (CH-14). "Knowledge and Expertise" also connects to "Tools and Technologies" (CH-4), which branches into: Conflict in Practice (CH-13), Machine Distortion (CH-15), Lack of Technical Understanding (CH-6), and No Legal Frameworks (CH-9). "Tools and Technologies" also connects to "Organizational Management" (CH-10), which branches into: Business Interest (CH-7), Cases of Ethical Dilemma (CH-12), and Lack of Audit and Monitoring (CH-8). "Organizational Management" also connects to "Extra Constraints" (CH-11). The mapping process is shown as a flow from "Theme" to "Sub-theme" to "Challenging Factor" (CH-N).

Figure 6: Thematic mapping of the identified challenges

![](891ff9b651838b7f59e9a1612a739e15_img.jpg)

Figure 7 is a bar chart illustrating a proposed capability maturity model of AI ethics. The Y-axis represents Maturity, and the X-axis represents Capability. The chart shows four levels of maturity: Level-1, Level-2, Level-3, and Level-4. The Level-4 bar is labeled "Level-n". The chart indicates that the maturity level is "comprise of" the capability level. The legend defines the data sources: AI Ethics Principles, Challenging Factors, Practices, Literature Study, Industrial Survey, and Industrial Case Studies.

Figure 7: A proposed capability maturity model of AI ethics

## 6 RESEARCH AND INDUSTRIAL IMPLICATIONS

This SLR study has both research and industrial implications by providing a set of AI ethics principles and challenging factors. This study contributes to academic research by explicitly exploring the available AI ethics primary studies. Similarly, the study findings make a concrete research contribution by providing a significant overview of AI ethics principles and challenges which can be core focus areas for future studies. In the industrial domain, the practitioners shall encapsulate the reported principles and challenges when they focus on ethics in AI projects. Additionally, the proposed

maturity model is the first step to actualizing the AI ethics principles in the industrial setting. The model will assist the practitioners to assess and improve the ethical capabilities of a specific AI software development organization. Finally, this SLR study provides a consolidated knowledge base of literature that has not been done before.

## 7 THREATS TO VALIDITY

### 7.1 Construct validity

A relevant construct validity could be "data items" since we as the researchers observed, decided, and pick up the text fragments or content from the identified studies. The data items extraction process might not be well performed for several reasons. For example, an inappropriate search strategy could possibly return a set of irrelevant primary studies. However, we tried to minimize such threats by following operation measures e.g. developing a formal search strategy and constantly revising it during the regular consensus meetings, following SLR inclusion and exclusion criteria, performing studies quality assessment and mitigating interpersonal bias using a common data extraction form. Moreover, we tried to extract the most relevant primary studies by customising the final search string based on the peculiarities of the selected digital libraries.

### 7.2 Internal validity

Internal validity refers to specific factors that may affect the data extraction, results, and analysis process. The search process might miss some relevant studies that focus on AI ethics challenges and principles, and it could be a possible threat to the study's internal validity. To lessen this threat, all the authors actively participated in the consent meetings to review the search activities, explored the research questions to extract relevant terms, and continuously revised the search strings based on their pilot implementation.

Additionally, all the authors have substantial experience performing SLR-based studies in the software engineering domain.

### 7.3 External validity

External validity is related to the generalizability of the study findings. The results are summaries based on 27 primary studies, because of the novelty of the research topic, very few studies published in this domain. The primary studies sample size ( $n=27$ ) might not be strong enough to generalize the study findings, however, we plan to extend this study in future by conducting an industrial study to evaluate the SLR findings and know the perceptions of the practitioners.

### 7.4 Conclusion validity

Potential threats to the conclusion validity of the study might exist, which could impact the credibility level of final conclusions. However, the study is conducted based on the well-defined SLR guidelines that focused on strict studies selection criteria to identify quality studies for final results and discussions. Additionally, all the authors participated in brainstorming sessions to discuss the study findings and draw precise conclusions.

## 8 CONCLUSIONS AND FUTURE DIRECTIONS

Ethics in AI gets significant attention in the last couple of years and there is a need of systematic literature study that discuss the principles and uncover the key challenges of AI ethics. This study is conducted to fill the given research gap by following the SLR approach. We identified total 27 relevant primary studies and the systematic review of the selected studies return 22 principles and 15 challenging factors. We noticed that most of the studies focus on four major principles i.e., *transparency*, *privacy*, *accountability* and *fairness*, which should consider by the AI system designers. Moreover, the decision-making systems should also be aware of the ethical principles to know the implications of their actions.

The challenges of ethics in AI are identified to provide an understanding of the factors that hinder the implementation of ethical principles. The most frequently reported challenging factors are *lack of ethical knowledge* and *vague principles*. The knowledge and understanding of ethics are important for both management and technical teams. It further removes the vagueness in AI principles. Lack of ethical knowledge could undermine the significance of decision-making systems.

We plan to extend this study by conducting an industrial survey to investigate the understanding of AI ethics in practice and identify the best practices to tackle the given challenging factors and manage the reported principles. Moreover, industrial case studies will be conducted in AI industry to assess the effectiveness of the proposed maturity model in practice.

## REFERENCES

1. Tingting Bi, Peng Liang, Antony Tang, and Chen Yang. 2018. A systematic mapping study on text analysis techniques in software architecture. *Journal of Systems and Software* 144 (2018), 533–558.
2. Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology. *Qualitative Research in Psychology* 3, 2 (2006), 77–101.
3. Alan Bundy. 2017. Preparing for the future of artificial intelligence. *AI & Society* 32 (2017), 285–287.
4. Lianping Chen, Muhammad Ali Babar, and He Zhang. 2010. Towards an evidence-based understanding of electronic data sources. In *Proceedings of the 14th International Conference on Evaluation and Assessment in Software Engineering* (EASE), 1–4.
5. ISO/IEC Committee. 2017. ISO/IEC JTC 1/SC 42 Artificial intelligence. Retrieved February 26, 2022 from <https://www.iso.org/committee/6794475.html>.
6. Virginia Dignum. 2017. Responsible Autonomy. In *Proceedings of the 26th International Joint Conference on Artificial Intelligence* IJCAI, 4698–4704.
7. IEEE. 2019. Ethically aligned design: A vision for prioritizing human well-being without autonomous and intelligent systems, first edition. Retrieved February 27, 2022 from <https://tinyurl.com/yah4jz6>.
8. Anna Jobin, Marcello Ienca, and Effy Yavena. 2019. The global landscape of AI ethics guidelines. *Nature Machine Intelligence* 1, 9 (2019), 389–399.
9. B. Kitchenham and S. Charters. 2007. Guidelines for Performing Systematic Literature Reviews in Software Engineering. Technical Report EBSE Technical Report EBSE-2007-01. Keele University and Durham University.
10. Jaana Leikas, Raija Koivisto, and Nadezhda Gotcheva. 2019. Ethical framework for designing autonomous intelligent systems. *Journal of Open Innovation: Technology, Market, and Complexity* 5, 1 (2019), 18.
11. Andrew McNamara, Justin Smith, and Emerson Murphy-Hill. 2018. Does ACM's code of ethics change ethical decision making in software development?. In *Proceedings of the 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering* (ESEC/FSE), 729–733.
12. Vincent C Müller. 2020. Ethics of Artificial Intelligence and Robotics. Retrieved February 26, 2022 from <https://plato.stanford.edu/archives/sum2021/entries/ethics-ai/>.
13. Beijing Academy of Artificial Intelligence. 2019. *Beijing AI Principles*. Retrieved February 26, 2022 from <https://www.pre-bai.ac.cn/news/beijing-ai-principles-en.html>.
14. Christina Pazzanese. 2020. Ethical concerns mount as AI takes bigger decision-making role in more industries. *The Harvard Gazette* 26 (2020).
15. AP Pekka, W Bauer, U Bergmann, M Bieliková, C Bonefeld-Dahl, Y Bonnet, L Bouarfa, et al. 2018. The European Commission's high-level expert group on artificial intelligence: Ethics guidelines for trustworthy AI. *Working Document for Stakeholders' Consultation* (2018), 1–37.
16. Sidney Siegel. 1957. Nonparametric statistics. *The American Statistician* 11, 3 (1957), 13–19.
17. CMMI Product Team. 2002. Capability maturity model® integration (CMMI SM), version 1.1. *CMMI for Systems Engineering, Software Engineering, Integrated Product and Process Development, and Supplier Sourcing* (CMMI-SE/SW/IPP/SS, V1.1) 2 (2002).
18. Ville Vakkuri, Kai-Kristian Kemell, and Pekka Abrahamsson. 2019. AI ethics in industry: a research framework. *arXiv preprint arXiv:1910.12695* (2019).
19. Ville Vakkuri, Kai-Kristian Kemell, and Pekka Abrahamsson. 2019. Implementing ethics in ai: Initial results of an industrial multiple case study. In *Proceedings of the 20th International Conference on Product-Focused Software Process Improvement (PROFES)*. Springer, 331–338.
20. Ville Vakkuri, Kai-Kristian Kemell, Marianna Jantunen, and Pekka Abrahamsson. 2020. "This is Just a Prototype": How Ethics Are Ignored in Software Startup-Like Environments. In *Proceedings of the 21st International Conference on Agile Software Development (XP)*. 195–210.
21. Claes Wohlin. 2014. Guidelines for snowballing in systematic literature studies and a replication in software engineering. In *Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering* (EASE), 1–10.

Table 6: Selected primary studies

| #   | Selected Studies                                                                                                                                                                                                                                                                                                                                                                      | Q1  | Q2  | Q3  | Q4  | Total |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|-----|-----|-------|
| S1  | Anna Jobin, Marcello Ienca, and Effy Vayena. 2019. The global landscape of AI ethics guidelines. <i>Nature Machine Intelligence</i> 1, 9 (2019), 389-399.                                                                                                                                                                                                                             | 1   | 1   | 1   | 1   | 4     |
| S2  | Siau, Keng, and Weiyu Wang. 2020. Artificial intelligence (AI) ethics: ethics of AI and ethical AI. <i>Journal of Database Management</i> 31, 2 (2020), 74-87.                                                                                                                                                                                                                        | 1   | 1   | 1   | 1   | 4     |
| S3  | Canca Cansu. 2020. Operationalizing AI ethics principles. <i>Communications of the ACM</i> 63, 12 (2020), 18-21.                                                                                                                                                                                                                                                                      | 1   | 1   | 1   | 1   | 4     |
| S4  | Hoffmann A, Lauren, Sarah T, Roberts, Christine T, Wolf, and Stacy Wood. 2018. Beyond fairness, accountability, and transparency in the ethics of algorithms: Contributions and perspectives from LIS. <i>Proceedings of the Association for Information Science and Technology</i> 55, 1 (2018), 694-696.                                                                            | 1   | 1   | 0   | 0.5 | 2.5   |
| S5  | Ville Vakkuri, Kai-Kristian Kemell, Joni Kultanen and Pekka Abrahamsson. 2020. The Current State of Industrial Practice in Artificial Intelligence Ethics. <i>IEEE Software</i> 37, 4 (2020), 50-57.                                                                                                                                                                                  | 1   | 1   | 1   | 1   | 4     |
| S6  | Charles D. Raab. 2020. Information privacy, impact assessment, and the place of ethics. <i>Computer Law &amp; Security Review</i> 37 (2020), 105404.                                                                                                                                                                                                                                  | 1   | 1   | 1   | 1   | 4     |
| S7  | Wenjun Wu, Tiejun Huang and Ke Gong. 2020. Ethical principles and governance technology development of AI in China. <i>Engineering</i> 6, 3 (2020), 302-309.                                                                                                                                                                                                                          | 1   | 1   | 1   | 1   | 4     |
| S8  | Sara Gerke, Timo Minssen, and Glenn Cohen. 2020. Ethical and legal challenges of artificial intelligence-driven healthcare. <i>In Artificial Intelligence in Healthcare</i> . (2020), 295-336.                                                                                                                                                                                        | 1   | 0.5 | 1   | 0.5 | 3     |
| S9  | Richard Benjamins. 2021. A choices framework for the responsible use of AI. <i>AI and Ethics</i> 1, 1 (2021), 49-53.                                                                                                                                                                                                                                                                  | 1   | 1   | 1   | 1   | 4     |
| S10 | Thilo Hagendorff. 2020. The ethics of AI ethics: An evaluation of guidelines. <i>Minds and Machines</i> 30, 1 (2020), 99-120.                                                                                                                                                                                                                                                         | 1   | 1   | 1   | 1   | 4     |
| S11 | Nagadiya Balasubramaniam, Marjo Kauppinen, Sari Kujala and Kari Hiekkanen. 2020. Ethical Guidelines for Solving Ethical Issues and Developing AI Systems. In <i>Proceedings of the 21st International Conference on Product-Focused Software Process Improvement (PROFES)</i> , LNCS, vol 12562, Springer, Cham, 331-346.                                                             | 1   | 1   | 1   | 1   | 4     |
| S12 | Ville Vakkuri and Kai-Kristian Kemell. 2019. Implementing AI Ethics in Practice: An Empirical Evaluation of the RESOLVEDD Strategy. In <i>Proceedings of 10th International Conference on Software Business (ICSOB)</i> , LNBIIP, vol 370, Springer, Cham, 260-275                                                                                                                    | 1   | 1   | 1   | 1   | 4     |
| S13 | Ray Eitel-Porter. 2021. Beyond the promise: implementing ethical AI. <i>AI and Ethics</i> 1, 1 (2021), 73-80.                                                                                                                                                                                                                                                                         | 1   | 1   | 1   | 1   | 4     |
| S14 | Tomas Hauer. 2020. Machine Ethics, Allottery and Philosophical Anti-Dualism: Will AI Ever Make Ethically Autonomous Decisions?. <i>Society</i> 57, 4 (2020), 425-433.                                                                                                                                                                                                                 | 1   | 1   | 1   | 1   | 4     |
| S15 | Josef Baker-Brunnbauer. 2020. Management perspective of ethics in artificial intelligence. <i>AI and Ethics</i> (2020), 1-9.                                                                                                                                                                                                                                                          | 1   | 1   | 1   | 1   | 4     |
| S16 | Banu Buruk, Perihan Elif Ekmekci and Berna Arda. 2020. A critical perspective on guidelines for responsible and trustworthy artificial intelligence. <i>Medicine, Health Care and Philosophy</i> 23, 3 (2020), 387-399.                                                                                                                                                               | 1   | 1   | 1   | 1   | 4     |
| S17 | Mittelstadt, Brent. 2019. Principles alone cannot guarantee ethical AI. <i>Nature Machine Intelligence</i> 1, 11 (2019), 501-507.                                                                                                                                                                                                                                                     | 1   | 1   | 1   | 1   | 4     |
| S18 | Jess Whittlestone, Rune Nyrup, Anna Alexandrova, and Stephen Cave. 2019. The Role and Limits of Principles in AI Ethics: Towards a Focus on Tensions. In <i>Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES)</i> , ACM, New York, NY, USA, 195-200.                                                                                                           | 1   | 1   | 0   | 1   | 3     |
| S19 | Luciano Floridi, Josh Cowl, Monica Beltrametti, Raja Chatila, Patrice Chazerand, Virginia Dignum, Christoph Luetge, Robert Madelin, Ugo Pagallo, Francesca Rossi, Burkhard Schafer, Peggy Valcke and Effy Vayena. 2018. AI4People—an ethical framework for a good AI society: opportunities, risks, principles, and recommendations. <i>Minds and Machines</i> 28, 4 (2018), 689-707. | 1   | 1   | 1   | 1   | 4     |
| S20 | Jessica Morley, Luciano Floridi, Libby Kinsey, and Anat Elhalal. 2020. From what to how: an initial review of publicly available AI ethics tools, methods and research to translate principles into practices. <i>Science and Engineering Ethics</i> 26, 4 (2020), 2141-2168.                                                                                                         | 1   | 1   | 1   | 1   | 4     |
| S21 | Ángel G. de Ágreda. 2020. Ethics of autonomous weapons systems and its applicability to any AI systems. <i>Telecommunications Policy</i> 44, 6 (2020), 101953.                                                                                                                                                                                                                        | 1   | 1   | 1   | 1   | 4     |
| S22 | Shuili Du, and Chunyan Xie. 2020. Paradoxes of artificial intelligence in consumer markets: Ethical challenges and opportunities. <i>Journal of Business Research</i> (2020).                                                                                                                                                                                                         | 1   | 1   | 1   | 1   | 4     |
| S23 | Mark Coeckelbergh. 2020. 11 Challenges for Policymakers. <i>AI Ethics</i> , MIT Press, 2020, 167-181.                                                                                                                                                                                                                                                                                 | 0.5 | 0.5 | 1   | 1   | 3     |
| S24 | E. L. Sidorenko, Z. I. Khisamova and U. E. Monastyrsky. 2021. The Main Ethical Risks of Using Artificial Intelligence in Business. In <i>Current Achievements, Challenges and Digital Chances of Knowledge Based Economy</i> , Springer, Cham, 423-429.                                                                                                                               | 1   | 1   | 0.5 | 3   | 4     |
| S25 | Chris Rees. 2020. The Ethics of Artificial Intelligence. In <i>Unimagined Futures—ICT Opportunities and Challenges</i> , Springer, Cham, 55-69.                                                                                                                                                                                                                                       | 1   | 1   | 1   | 1   | 4     |
| S26 | Jan Jöhnk, Malte Weißert and Katrin Wyrtki. 2021. Ready or Not, AI Comes—An Interview Study of Organizational AI Readiness Factors. <i>Business &amp; Information Systems Engineering</i> 63, 1 (2021), 5-20.                                                                                                                                                                         | 1   | 1   | 1   | 1   | 4     |
| S27 | Seán S. ÓhEigeartaigh, Jess Whittlestone, Yang Liu, Yi Zeng, and Zhe Liu. 2020. Overcoming barriers to cross-cultural cooperation in AI ethics and governance. <i>Philosophy &amp; Technology</i> 33, 4 (2020), 571-593.                                                                                                                                                              | 1   | 1   | 1   | 1   | 4     |