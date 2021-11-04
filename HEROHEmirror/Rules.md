[Home](https://econdesousa.github.io){: .btn}
[Research Interests](https://econdesousa.github.io/ResearchInterests){: .btn}
[Publications](https://econdesousa.github.io/Publications){: .btn}
[Supervisions](https://econdesousa.github.io/Supervision){: .btn}
[External Links](https://econdesousa.github.io/Links){: .btn}
[Contacts](https://econdesousa.github.io/Contacts){: .btn}
[CV](assets/CurriculumVitaeECS.pdf){:.btn target="_blank" rel="noopener"}
[HEROHE](https://econdesousa.github.io/HEROHE/index){: .btn}

# HEROHE Grand-Challenge

[HEROHE](https://econdesousa.github.io/HEROHE/index){: .btn}
[Rules](https://econdesousa.github.io/HEROHE/Rules){: .btn}
[Dataset](https://econdesousa.github.io/HEROHE/Dataset){: .btn}
[Results](https://econdesousa.github.io/HEROHE/Results){: .btn}

<center>
	<figure>
		<img src="https://econdesousa.github.io/assets/HEROHE_ECDP2020_alpha.jpg" style="width:80%">
		<figcaption>This page is a copy of the <a href="https://ecdp2020.grand-challenge.org/Rules">Grand-Challenge web page</a>!</figcaption>

	</figure>
</center>

## Rules

Please respect the rules of the Challenge. The organization reserves the right to not consider submissions that fail to abide to the rules presented in this page:



## Registration
Both individual and team participations are welcome in the Challenge. This Challenge is part of the 16th European Congress on Digital Pathology (ECDP2020). 
For each team, at least one person must be registered in the congress to be eligible to the challenge's prizes. 

The contact information provided will not be used for any purposes other than those related to the congress or this Challenge.

Once the registration is completed and accepted, participants will receive instructions on how to download the dataset.

Please note that each person can only belong to one team.

Registration links: 

* EDCP2020](http://ecdp2020.org)
* [HEROHE grand-challenge](https://ecdp2020.grand-challenge.org/)


## Participation
Participation in the Challenge is conditioned to the proper submission of:
* Short method description, the code (or compiled version<sup>*</sup>), and test set prediction until January 24th, 2020 until 9 a.m., January 28th, 2020 (Greenwich Mean Time - Portuguese time zone).


To be eligible for the prizes, it is also mandatory that at least one member of each team properly register and attend ECDP2020.

Results will be made publicly available on the Challenge website after the submission deadline.

Challenge participants grant the Challenge organization the permission to use the result of their methods. Nevertheless, participating teams maintain full ownership and rights to their method. The Challenge organization does not claim any ownership or rights to the developed works.

The best performing methods will be invited to collaborate on a journal paper describing and summarizing the different approaches used and the respective results achieved on the Challenge.

To ensure a fair comparison of the submitted methods, the usage of any private dataset during the development of the methods is not allowed.

Note that submission of a result in the Grand Challenge HEROHE does not warrant the presentation of a poster/oral presentation at ECDP2020. Each team is encouraged to submit their work as an abstract according to the abstract submission rules of ECDP2020.

<sup>*</sup> If the team decides to provide only a compiled version, it is their sole responsibility to ensure that it is ready to run on all major operating systems.

## Data
The presented dataset contains 360 cases, 144 positives and 216 negatives. Each whole-slide image was saved in the  [MIRAX](https://openslide.org/formats/mirax/) format.

For more information please the Dataset page.


## Attribution

The downloaded dataset, or any data derived from this dataset, cannot be given or redistributed under any circumstances to persons not belonging to the registered team.

This dataset was designed for being used exclusively in the context of the HEROHE Grand-Challenge and / or the submission of communications to the ECDP2020. 
The dataset, or any data derived from this dataset, cannot be used for any other purposes, including but not limited to military, industrial development/patenting, 
or academic use (including journal publications, conference papers, technical reports, presentations at conferences and meetings or teaching).

The organization anticipates that the results of this challenge will be published in an international peer-reviewed scientific journal. 
If and when this happens, the dataset will become available for research purposes under the Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0). 
The corresponding publication should thus be cited. Updates on this issue will become available in the challenge web page.

## Submission
A zipped file must be submitted until January 28 (Portuguese time) at https://ecdp2020.grand-challenge.org/evaluation/submissions/create/. 
The submitted zipped file should contain three files/folders inside: 
one word file with the methods description, 
one csv file with the predictions, 
and a folder with the code and the corresponding README file.

This submission will be used to rank the methods for prize distribution.

Note that each team can only participate in the challenge once, i.e., each team can only submit an algorithm. If several attempts of submission are performed, only the last will be considered.




## Details regarding the submission files:
The code (or compiled version<sup>*</sup>) must be released ready to use with minimal user interaction and should have a README file with a detailed explanation on how to run it. 
It should receive as input a folder with the test dataset (please refer possible file conversions needed previously) and should return a .csv file with the predictions.

The predictions file must be in the csv file format and should

* be named after the team,
* have one header row (pre-filled by us<sup>**</sup>),
* have one row per sample, and
* have three columns


The caseID should match the slide’s filename (without file extension)

The soft prediction should be a value, between 0 and 1 with the probability of that sample being positive.

The hard prediction should be an integer 0 (for negative slides) or 1 (for positive slides).

The short method description should include references to any source used during the work.

<sup>**</sup> A .csv file with the header and the caseID column already filled will be released with the test dataset


## Prizes
The teams with the best results in the Challenge will be awarded with 1000 euros, 500 euros and 250 euros, for the first, second and third places, respectively. The representant of each of three best teams will also receive a free registration for the next year ECDP2021. The Challenge prizes will be paid by IPATIMUP - Instituto de Patologia e Imunologia Molecular da Universidade do Porto, the entity that provides the organizational support of ECDP2020, through a sponsorship from ROCHE.

The Challenge prizes will be awarded during the ECDP2020 conference, to be held in Porto, 13th-15th May 2020. Specifically,  ECDP2020  has allocated prizes to be distributed among the three teams with the best performance<sup>***</sup>.

Eligibility to the Challenge's prizes is conditioned to the quality of the method and participation at the conference<sup>***</sup>.



## Awarded:

| Rank	| Team	    | Team representative |
| ----  | ----      | ----                |
| 1	    | Macaroon	| Ming Feng           |
| 2	    | MITEL     | Vincenzo Della Mea  |
| 3	    | Piaz	    | Ehsan Montahaei     |


<sup>***</sup> ECDP2020 was cancelled due to the coronavirus pandemic, so these points were not taken into account


## Evaluation
Submissions are scored based on the [F1-score](https://en.wikipedia.org/wiki/F1_score),  the harmonic mean of precision and recall

![F1_score](/assets/image.webp)


## Evaluation panel:
* Conde-Sousa, Eduardo (PhD) - i3S/INEB
* Araújo, Teresa (PhD student) - INESC TEC and Faculty of Engineering of Universidade do Porto
* Aresta, Guilherme (PhD student) - INESC TEC and Faculty of Engineering of Universidade do Porto
* Aguiar, Paulo (PhD) - i3S/INEB
* Eloy, Catarina (MD, PhD) - i3S/IPATIMUP and Faculty of Medicine of Universidade do Porto
* Polónia, António (MD, PhD) - i3S/IPATIMUP



![ROCHE logo](/assets/ROCHElogo.jpeg)


[Home](https://econdesousa.github.io){: .btn}
[Research Interests](https://econdesousa.github.io/ResearchInterests){: .btn}
[Publications](https://econdesousa.github.io/Publications){: .btn}
[Supervisions](https://econdesousa.github.io/Supervision){: .btn}
[External Links](https://econdesousa.github.io/Links){: .btn}
[Contacts](https://econdesousa.github.io/Contacts){: .btn}
[CV](assets/CurriculumVitaeECS.pdf){:.btn target="_blank" rel="noopener"}
[HEROHE](https://econdesousa.github.io/HEROHE/index){: .btn}


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3JWYKYVYDZ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3JWYKYVYDZ');
</script>