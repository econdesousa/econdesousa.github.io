[Home](https://econdesousa.github.io){: .btn}
[Research Interests](https://econdesousa.github.io/ResearchInterests){: .btn}
[Publications](https://econdesousa.github.io/Publications){: .btn}
[Supervisions](https://econdesousa.github.io/Supervision){: .btn}
[External Links](https://econdesousa.github.io/Links){: .btn}
[Contacts](https://econdesousa.github.io/Contacts){: .btn}
[CV](assets/CurriculumVitaeECS.pdf){:.btn target="_blank" rel="noopener"}
[HEROHE](https://econdesousa.github.io/HEROHE/index){: .btn}

# HEROHE Grand-Challenge

<center>
	<figure>
		<img src="https://econdesousa.github.io/assets/HEROHE_ECDP2020_alpha.jpg" style="width:80%">
		<figcaption>This page is a copy of the <a href="https://ecdp2020.grand-challenge.org/Dataset/">Grand-Challenge web page</a>!</figcaption>

	</figure>
</center>

## Biological Information
HER2 is a transmembrane protein receptor with tyrosine kinase activity and is ampliﬁed and/or overexpressed 
in approximately 15–20% of BC. The overexpression and/or amplification of HER2 has been associated with 
aggressive clinical behavior but with a high probability of response to HER2 targeted therapy. Consequently, 
the correct identification of HER2 positive BC selects patients expected to benefit from targeted therapy, 
making HER2 a helpful marker for therapy decision making in patients with BC.

## Ground Truth 
The presented dataset contains 360 cases, 144 positives and 216 negatives. 
The classification of this dataset used the latest American Society of 
Clinical Oncology/College of American Pathologists (ASCO/CAP) classification of breast 
cancer (Focused Update 2018). The ground truth can be accessed in the accompanying excel 
file (HEROHE_HER2_STATUS.xlsx).


## Data Format
Whole slide images were scanned in a [3D Histech Pannoramic 1000](https://www.3dhistech.com/pannoramic_1000) 
digital scanner and saved in the [MIRAX](https://openslide.org/formats/mirax/) format. Each whole slide 
image is stored divided into one .mrxs and a folder (with the same basename) containing many .dat files. 

The [MIRAX](https://openslide.org/formats/mirax/) format is not supported by Bio-Formats, so images cannot 
be opened directly in most software packages. The [OpenSlide](https://openslide.org/) library provides a simple 
interface to read whole-slide images through a C API and a Python API

3D Histech provides two free software tools for viewing and exporting the files to commonly used formats, 
such as tiff or jpeg. We recommend participants to use [CaseViewer](http://www.3dhistech.com/caseviewer), 
which is the latest (you should download the version with Converter to be able to export the files to other formats). 
Other alternatives are 3D Histech’s [Panoramic Viewer](http://www.3dhistech.com/pannoramic_viewer), an older viewer 
that also provide export options, or other image analysis software that can open directly 3D Histech files such as 
[QuPath](https://qupath.github.io/), or [Arivis](https://www.arivis.com/en/imaging-science/arivis-vision4d). 
Participants are free to choose the software they like and if they want to convert the files to any 
other format beforehand.


## Download
Before you can download the dataset, please read the Rules section. 

### Training Dataset
Download link: (NOT AVAILABLE NOW)

Alternative Google Drive: (NOT AVAILABLE NOW)

Note: Image 325 has no tumor. Although there was tumor on the slide, unfortunately, 
the small tumor is located on the periphery of the slide and was not digitized and we 
missed that. To avoid any problems we ask you to consider disregarding this sample from 
the dataset, given that it can cause repercussions on your results.

### Test Dataset
(NOT AVAILABLE NOW)



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